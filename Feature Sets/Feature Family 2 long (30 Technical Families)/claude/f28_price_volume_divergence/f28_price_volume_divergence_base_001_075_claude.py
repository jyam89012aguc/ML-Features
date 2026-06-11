"""f28_price_volume_divergence base features 001-075.

Domain: PRICE vs VOLUME DISAGREEMENT (divergence). Bearish divergence: price
makes new high but volume not at new high. Bullish divergence: price makes
new low but volume not at new low. Distinct from f24 (confirmation/agreement)
which measures AGREEMENT, and from f14 (price-momentum) which uses an
indicator instead of volume.

Feature families included: sign-XOR disagreement, slope disagreement,
peak/trough disagreement, rolling Pearson/Spearman corr (negative=divergence),
beta of volume change on price change, divergence severity, regression
residuals, distribution skew/vol disagreement, OBV-light divergence,
time-domain lag of corr, cumulative divergence, bounded transforms,
volume-price asymmetry, hidden divergence (continuation pattern), discrete
divergence states. NaN policy: never fillna(<value>); only replace(inf,nan)
at the final return. Windows > 21d use closeadj; <=21d use close.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=n).mean()


def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _zscore(s: pd.Series, n: int) -> pd.Series:
    m = s.rolling(n, min_periods=n).mean()
    sd = s.rolling(n, min_periods=n).std()
    return (s - m) / sd.replace(0.0, np.nan)


def _slope_norm_fn(x):
    """OLS slope of x vs time index, normalized by abs(mean). NaN-safe."""
    n = len(x); t = np.arange(n, dtype=float)
    mt = t.mean(); mx = x.mean()
    cov = float(np.sum((t - mt) * (x - mx)))
    var = float(np.sum((t - mt) ** 2))
    if var == 0.0 or not np.isfinite(mx) or abs(mx) < 1e-15:
        return np.nan
    return float((cov / var) / abs(mx))


def _slope_raw_fn(x):
    """OLS slope of x vs time index, raw (no normalization)."""
    n = len(x); t = np.arange(n, dtype=float)
    mt = t.mean(); mx = x.mean()
    cov = float(np.sum((t - mt) * (x - mx)))
    var = float(np.sum((t - mt) ** 2))
    if var == 0.0:
        return np.nan
    return float(cov / var)


def _spearman_fn(xy):
    """Spearman correlation of two flattened columns: xy is a 2-col array."""
    if xy.ndim == 1:
        return np.nan
    a = xy[:, 0]; b = xy[:, 1]
    if not (np.all(np.isfinite(a)) and np.all(np.isfinite(b))):
        return np.nan
    if np.std(a) == 0.0 or np.std(b) == 0.0:
        return np.nan
    ra = pd.Series(a).rank().values
    rb = pd.Series(b).rank().values
    num = float(np.sum((ra - ra.mean()) * (rb - rb.mean())))
    den = float(np.sqrt(np.sum((ra - ra.mean()) ** 2) * np.sum((rb - rb.mean()) ** 2)))
    if den == 0.0:
        return np.nan
    return num / den


def _obv(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Light OBV — used sparingly. f23 owns OBV; here just a few features."""
    sgn = np.sign(close.diff())
    return (sgn * volume).cumsum()


def _streak_idx(x):
    """Bars since last value > 0.5 within window x; len(x) if none."""
    idx = np.where(x > 0.5)[0]
    if idx.size == 0:
        return float(len(x))
    return float(len(x) - 1 - idx[-1])


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# === SIGN-XOR disagreement (basic divergence indicator) ====================


def f28pd_f28_price_volume_divergence_sign_xor_close_vol_5d_base_v001_signal(close, volume):
    """1 if sign(close.diff(5)) != sign(volume.diff(5)) else 0. Basic disagreement bit."""
    sp = np.sign(close.diff(5))
    sv = np.sign(volume.diff(5))
    out = (sp != sv).astype(float).where(~sp.isna() & ~sv.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_xor_count_20d_base_v002_signal(close, volume):
    """Count of disagreement bits over last 20 bars."""
    sp = np.sign(close.diff(1))
    sv = np.sign(volume.diff(1))
    bit = (sp != sv).astype(float).where(~sp.isna() & ~sv.isna())
    return bit.rolling(20, min_periods=20).sum().replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_xor_count_60d_base_v003_signal(closeadj, volume):
    """Count of disagreement bits over last 60 bars."""
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    bit = (sp != sv).astype(float).where(~sp.isna() & ~sv.isna())
    return bit.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_xor_streak_40d_base_v004_signal(closeadj, volume):
    """Consecutive bars (last 40) where sign(close.diff)!=sign(volume.diff)."""
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    bit = (sp != sv).astype(float).where(~sp.isna() & ~sv.isna())
    def _consec(x):
        c = 0
        for v in x[::-1]:
            if v > 0.5:
                c += 1
            else:
                break
        return float(c)
    return bit.rolling(40, min_periods=40).apply(_consec, raw=True).replace([np.inf, -np.inf], np.nan)


# === SLOPE DISAGREEMENT (regression slopes of close vs volume) =============


def f28pd_f28_price_volume_divergence_slope_diff_sign_15d_base_v005_signal(close, volume):
    """sign(close_slope) * -sign(volume_slope) over 15d. +1 = diverging."""
    cs = close.rolling(15, min_periods=15).apply(_slope_raw_fn, raw=True)
    vs = volume.rolling(15, min_periods=15).apply(_slope_raw_fn, raw=True)
    return (np.sign(cs) * (-1.0) * np.sign(vs)).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_slope_diff_45d_base_v006_signal(closeadj, volume):
    """log(close).slope - log(volume).slope over 45d. Negative = price up, volume down (bearish)."""
    lc = np.log(closeadj).rolling(45, min_periods=45).apply(_slope_raw_fn, raw=True)
    lv = np.log(volume.replace(0.0, np.nan)).rolling(45, min_periods=45).apply(_slope_raw_fn, raw=True)
    return (lc - lv).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_slope_diff_abs_120d_base_v007_signal(closeadj, volume):
    """|log(close).slope - log(volume).slope| over 120d. Magnitude of slope divergence."""
    lc = np.log(closeadj).rolling(120, min_periods=120).apply(_slope_raw_fn, raw=True)
    lv = np.log(volume.replace(0.0, np.nan)).rolling(120, min_periods=120).apply(_slope_raw_fn, raw=True)
    return (lc - lv).abs().replace([np.inf, -np.inf], np.nan)


# === ROLLING PEARSON CORR (negative corr = divergence) =====================


def f28pd_f28_price_volume_divergence_corr_pct_30d_base_v008_signal(closeadj, volume):
    """30d corr(close.pct_change, volume.pct_change). Negative = divergence."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    return rp.rolling(30, min_periods=30).corr(rv).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_corr_pct_90d_base_v009_signal(closeadj, volume):
    """90d corr(close.pct_change, volume.pct_change)."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    return rp.rolling(90, min_periods=90).corr(rv).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_corr_diff_45d_base_v010_signal(closeadj, volume):
    """45d corr(close.diff, volume.diff). Pearson on raw diffs."""
    return closeadj.diff().rolling(45, min_periods=45).corr(volume.diff()).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_neg_corr_pct_60d_base_v011_signal(closeadj, volume):
    """-corr(close.pct_change, volume.pct_change) 60d. Positive=divergence."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    c = rp.rolling(60, min_periods=60).corr(rv)
    return (-1.0 * c).replace([np.inf, -np.inf], np.nan)


# === SPEARMAN CORR (rank-based, robust to outliers) ========================


def f28pd_f28_price_volume_divergence_spearman_50d_base_v012_signal(closeadj, volume):
    """50d Spearman correlation between close and volume (rank-based). Negative=divergence."""
    rc = closeadj.rolling(50, min_periods=50).rank(pct=False)
    rv = volume.rolling(50, min_periods=50).rank(pct=False)
    return rc.rolling(50, min_periods=50).corr(rv).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_spearman_100d_base_v013_signal(closeadj, volume):
    """100d Spearman correlation between close and volume."""
    rc = closeadj.rolling(100, min_periods=100).rank(pct=False)
    rv = volume.rolling(100, min_periods=100).rank(pct=False)
    return rc.rolling(100, min_periods=100).corr(rv).replace([np.inf, -np.inf], np.nan)


# === BETA (volume on price; negative = divergence regime) ==================


def f28pd_f28_price_volume_divergence_beta_vol_price_55d_base_v014_signal(closeadj, volume):
    """OLS beta of volume.pct_change on close.pct_change over 55d. Negative = divergence."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    cov = rp.rolling(55, min_periods=55).cov(rv)
    var = rp.rolling(55, min_periods=55).var()
    return (cov / var.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_beta_sign_120d_base_v015_signal(closeadj, volume):
    """sign(beta(volume.pct_change on close.pct_change)) over 120d. -1 = persistent divergence."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    cov = rp.rolling(120, min_periods=120).cov(rv)
    var = rp.rolling(120, min_periods=120).var()
    beta = cov / var.replace(0.0, np.nan)
    return np.sign(beta).replace([np.inf, -np.inf], np.nan)


# === PEAK / TROUGH DIVERGENCE (binary unconfirmed extremes) ================


def f28pd_f28_price_volume_divergence_bear_div_unconf_high_30d_base_v016_signal(closeadj, volume):
    """1 if close is new 30d high but volume is NOT new 30d high (bearish unconfirmed)."""
    cmax = closeadj.rolling(30, min_periods=30).max()
    vmax = volume.rolling(30, min_periods=30).max()
    bull = (closeadj >= cmax).astype(float)
    vhigh = (volume >= vmax).astype(float)
    out = (bull * (1.0 - vhigh)).where(~cmax.isna() & ~vmax.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_bull_div_unconf_low_30d_base_v017_signal(closeadj, volume):
    """1 if close is new 30d low but volume is NOT new 30d low (bullish unconfirmed)."""
    cmin = closeadj.rolling(30, min_periods=30).min()
    vmin = volume.rolling(30, min_periods=30).min()
    plow = (closeadj <= cmin).astype(float)
    vlow = (volume <= vmin).astype(float)
    out = (plow * (1.0 - vlow)).where(~cmin.isna() & ~vmin.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_days_since_unconf_high_60d_base_v018_signal(closeadj, volume):
    """Bars since last unconfirmed price-high (high but volume not at high), 60d window."""
    cmax = closeadj.rolling(30, min_periods=30).max()
    vmax = volume.rolling(30, min_periods=30).max()
    bit = ((closeadj >= cmax).astype(float) * (1.0 - (volume >= vmax).astype(float))).where(~cmax.isna() & ~vmax.isna())
    return bit.rolling(60, min_periods=60).apply(_streak_idx, raw=True).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_days_since_unconf_low_80d_base_v019_signal(closeadj, volume):
    """Bars since last unconfirmed price-low (low but volume not at low), 80d window."""
    cmin = closeadj.rolling(30, min_periods=30).min()
    vmin = volume.rolling(30, min_periods=30).min()
    bit = ((closeadj <= cmin).astype(float) * (1.0 - (volume <= vmin).astype(float))).where(~cmin.isna() & ~vmin.isna())
    return bit.rolling(80, min_periods=80).apply(_streak_idx, raw=True).replace([np.inf, -np.inf], np.nan)


# === DISTRIBUTION DIVERGENCE (skew, vol of price vs vol) ===================


def f28pd_f28_price_volume_divergence_skew_diff_50d_base_v020_signal(closeadj, volume):
    """50d skew(log-returns) - skew(log-volume-changes). Distribution shape disagreement."""
    rp = np.log(closeadj / closeadj.shift(1))
    rv = np.log(volume / volume.shift(1)).replace([np.inf, -np.inf], np.nan)
    return (rp.rolling(50, min_periods=50).skew() - rv.rolling(50, min_periods=50).skew()).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_vol_ratio_log_60d_base_v021_signal(closeadj, volume):
    """log(std(close.pct_change,60) / std(volume.pct_change,60)). Vol-of-vol ratio (log)."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    sp = rp.rolling(60, min_periods=60).std()
    sv = rv.rolling(60, min_periods=60).std()
    return np.log(sp / sv.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_kurt_diff_80d_base_v022_signal(closeadj, volume):
    """80d kurt(log-returns) - kurt(log-volume-changes). Tail-shape disagreement."""
    rp = np.log(closeadj / closeadj.shift(1))
    rv = np.log(volume / volume.shift(1)).replace([np.inf, -np.inf], np.nan)
    return (rp.rolling(80, min_periods=80).kurt() - rv.rolling(80, min_periods=80).kurt()).replace([np.inf, -np.inf], np.nan)


# === OBV DIVERGENCE (light, since f23 owns OBV) ============================


def f28pd_f28_price_volume_divergence_obv_close_slope_diff_45d_base_v023_signal(closeadj, volume):
    """slope_norm(OBV,45) - slope_norm(close,45). Negative when OBV diverges down from price."""
    obv = _obv(closeadj, volume)
    so = obv.rolling(45, min_periods=45).apply(_slope_norm_fn, raw=True)
    sc = closeadj.rolling(45, min_periods=45).apply(_slope_norm_fn, raw=True)
    return (so - sc).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_obv_sign_disagree_30d_base_v024_signal(closeadj, volume):
    """sign(OBV.diff(30)) - sign(close.diff(30)). 0 if agreeing, -2/2 if disagreeing."""
    obv = _obv(closeadj, volume)
    return (np.sign(obv.diff(30)) - np.sign(closeadj.diff(30))).replace([np.inf, -np.inf], np.nan)


# === BOUNDED TRANSFORMS OF DIVERGENCE ======================================


def f28pd_f28_price_volume_divergence_tanh_div_signed_30d_base_v025_signal(close, volume):
    """tanh of (sign(price.diff(5)) * z_volume_30d - sign(volume.diff(5)) * z_volume_30d)/2.
    A bounded signed disagreement that differs from raw corr by including price direction prefactor."""
    rp = close.pct_change(5)
    rv = volume.pct_change(5)
    sp = np.sign(rp)
    sv = np.sign(rv)
    vmag = (volume - volume.rolling(30, min_periods=30).mean()) / volume.rolling(30, min_periods=30).std().replace(0.0, np.nan)
    return np.tanh((sp - sv) * vmag * 0.5).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_arctan_slope_diff_50d_base_v026_signal(closeadj, volume):
    """arctan of (slope(log-close) - slope(log-volume)) normalized by 50d std of close slope."""
    lp = np.log(closeadj)
    lv = np.log(volume.replace(0.0, np.nan))
    sp = lp.rolling(50, min_periods=50).apply(_slope_raw_fn, raw=True)
    sv = lv.rolling(50, min_periods=50).apply(_slope_raw_fn, raw=True)
    sig = sp.rolling(50, min_periods=50).std()
    return np.arctan((sp - sv) / sig.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_sigmoid_xor_freq_40d_base_v027_signal(closeadj, volume):
    """sigmoid(2*(xor_freq - 0.5)) where xor_freq = mean of disagreement bits over 40d."""
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    bit = (sp != sv).astype(float).where(~sp.isna() & ~sv.isna())
    freq = bit.rolling(40, min_periods=40).mean()
    z = 2.0 * (freq - 0.5)
    return (1.0 / (1.0 + np.exp(-z.clip(-30.0, 30.0)))).replace([np.inf, -np.inf], np.nan)


# === VOLUME-PRICE ASYMMETRY (up-vol / down-vol) ============================




def f28pd_f28_price_volume_divergence_updown_vol_asym_100d_base_v029_signal(closeadj, volume):
    """(sum_vol_up - sum_vol_down) / (sum_vol_up + sum_vol_down) over 100d. Bounded [-1,1]."""
    up = (closeadj.diff(1) > 0).astype(float)
    dn = (closeadj.diff(1) < 0).astype(float)
    uv = (up * volume).rolling(100, min_periods=100).sum()
    dv = (dn * volume).rolling(100, min_periods=100).sum()
    return ((uv - dv) / (uv + dv).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === DIVERGENCE SEVERITY (max divergence over window) ======================


def f28pd_f28_price_volume_divergence_max_neg_corr_window_60d_base_v030_signal(closeadj, volume):
    """Most-negative 20d corr(close.pct_change, volume.pct_change) observed over last 60d."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    c20 = rp.rolling(20, min_periods=20).corr(rv)
    return c20.rolling(60, min_periods=60).min().replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_corr_dev_from_mean_120d_base_v031_signal(closeadj, volume):
    """Current 30d corr minus 120d rolling mean of 30d corr. Recent divergence vs baseline."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    c30 = rp.rolling(30, min_periods=30).corr(rv)
    return (c30 - c30.rolling(120, min_periods=120).mean()).replace([np.inf, -np.inf], np.nan)


# === REGRESSION RESIDUAL (volume on price) =================================


def f28pd_f28_price_volume_divergence_resid_std_vol_on_price_50d_base_v032_signal(closeadj, volume):
    """50d std-of-residuals of OLS regression of volume on close, normalized by mean volume.
    Computed via rolling sums: residual variance = var(y) - cov(x,y)^2/var(x)."""
    n = 50
    x = closeadj; y = volume
    mx = x.rolling(n, min_periods=n).mean()
    my = y.rolling(n, min_periods=n).mean()
    vx = x.rolling(n, min_periods=n).var()
    vy = y.rolling(n, min_periods=n).var()
    cxy = x.rolling(n, min_periods=n).cov(y)
    res_var = vy - (cxy * cxy) / vx.replace(0.0, np.nan)
    res_var = res_var.clip(lower=0.0)
    return (np.sqrt(res_var) / my.abs().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_rsq_vol_on_price_80d_base_v033_signal(closeadj, volume):
    """80d R^2 of OLS volume on close. LOW R^2 = price and volume don't co-move (divergence).
    R^2 = corr(x,y)^2."""
    n = 80
    c = closeadj.rolling(n, min_periods=n).corr(volume)
    return (c * c).replace([np.inf, -np.inf], np.nan)


# === CUMULATIVE DIVERGENCE =================================================


def f28pd_f28_price_volume_divergence_cum_sign_diff_45d_base_v034_signal(closeadj, volume):
    """Mean of (sign(price.diff) - sign(volume.diff)) over 45d. Cumulative directional gap."""
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    return (sp - sv).rolling(45, min_periods=45).mean().replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_cum_div_zscore_100d_base_v035_signal(closeadj, volume):
    """z-score of rolling-cum (sign(price.diff)-sign(vol.diff)) over 100d."""
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    cum = (sp - sv).rolling(20, min_periods=20).sum()
    return _zscore(cum, 100).replace([np.inf, -np.inf], np.nan)


# === HIDDEN DIVERGENCE (higher-low in price but lower-low in volume) =======


def f28pd_f28_price_volume_divergence_hidden_bull_25d_base_v036_signal(close, volume):
    """1 if price has higher-low (close > 25d-ago min) but volume has lower-low (vol < 25d-ago min)."""
    pmin = close.rolling(25, min_periods=25).min()
    vmin = volume.rolling(25, min_periods=25).min()
    pmin_prev = pmin.shift(13)
    vmin_prev = vmin.shift(13)
    hl_price = (pmin > pmin_prev).astype(float)
    ll_vol = (vmin < vmin_prev).astype(float)
    out = (hl_price * ll_vol).where(~pmin.isna() & ~pmin_prev.isna() & ~vmin_prev.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_hidden_bear_50d_base_v037_signal(closeadj, volume):
    """1 if price has lower-high (cmax < cmax_prev) but volume has higher-high (vmax > vmax_prev)."""
    pmax = closeadj.rolling(50, min_periods=50).max()
    vmax = volume.rolling(50, min_periods=50).max()
    pmax_prev = pmax.shift(25)
    vmax_prev = vmax.shift(25)
    lh_price = (pmax < pmax_prev).astype(float)
    hh_vol = (vmax > vmax_prev).astype(float)
    out = (lh_price * hh_vol).where(~pmax.isna() & ~pmax_prev.isna() & ~vmax_prev.isna())
    return out.replace([np.inf, -np.inf], np.nan)


# === LAG-CORRELATION (time-domain divergence) ==============================


def f28pd_f28_price_volume_divergence_lead_lag_corr_diff_60d_base_v038_signal(closeadj, volume):
    """corr(price.pct, vol.pct.shift(5)) - corr(price.pct, vol.pct.shift(-5)) over 60d.
    Positive: volume leads price (divergence in time)."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    c_lag = rp.rolling(60, min_periods=60).corr(rv.shift(5))
    c_lead = rp.rolling(60, min_periods=60).corr(rv.shift(-5))
    return (c_lag - c_lead).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_corr_lag_minus_synced_45d_base_v039_signal(closeadj, volume):
    """corr(price, vol.shift(3)) - corr(price, vol) at 45d. Time-shift divergence."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    c_shift = rp.rolling(45, min_periods=45).corr(rv.shift(3))
    c_sync = rp.rolling(45, min_periods=45).corr(rv)
    return (c_shift - c_sync).replace([np.inf, -np.inf], np.nan)


# === XOR PERCENTILE RANK (regime indicator) ================================


def f28pd_f28_price_volume_divergence_xor_freq_pctrank_120d_base_v040_signal(closeadj, volume):
    """Percentile rank (over 120d) of 20d XOR-frequency. Indicates current regime severity."""
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    bit = (sp != sv).astype(float).where(~sp.isna() & ~sv.isna())
    freq = bit.rolling(20, min_periods=20).mean()
    return freq.rolling(120, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === RAW SLOPE-DISAGREEMENT MAGNITUDE (Sharpe-like) ========================


def f28pd_f28_price_volume_divergence_sharpe_div_30d_base_v041_signal(close, volume):
    """|slope(log-close) - slope(log-volume)| / std(log-close-diff) over 30d. Sharpe-like."""
    lp = np.log(close)
    lv = np.log(volume.replace(0.0, np.nan))
    sp = lp.rolling(30, min_periods=30).apply(_slope_raw_fn, raw=True)
    sv = lv.rolling(30, min_periods=30).apply(_slope_raw_fn, raw=True)
    sd = lp.diff().rolling(30, min_periods=30).std()
    return ((sp - sv).abs() / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === SIGN-OF-CORR (discrete divergence regime) =============================


def f28pd_f28_price_volume_divergence_corr_sign_60d_base_v042_signal(closeadj, volume):
    """sign of 60d corr(close.pct, volume.pct). -1 = divergence regime."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    c = rp.rolling(60, min_periods=60).corr(rv)
    return np.sign(c).replace([np.inf, -np.inf], np.nan)


# === FRACTION OF NEGATIVE CORR DAYS (regime persistence) ===================


def f28pd_f28_price_volume_divergence_neg_corr_frac_100d_base_v043_signal(closeadj, volume):
    """Fraction of last 100 bars where 15d corr(price,vol) was negative."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    c15 = rp.rolling(15, min_periods=15).corr(rv)
    neg = (c15 < 0.0).astype(float).where(~c15.isna())
    return neg.rolling(100, min_periods=100).mean().replace([np.inf, -np.inf], np.nan)


# === DOWN-DAY VOLUME ANOMALY (price down with high volume = strong) ========


def f28pd_f28_price_volume_divergence_down_day_vol_zscore_50d_base_v044_signal(close, volume):
    """Most-recent down-day volume z-score against 50d mean/std of all-day volume.
    High value when price drops on heavy volume — confirming, NOT diverging — invert sign."""
    is_dn = (close.diff(1) < 0).astype(float).where(~close.diff(1).isna())
    vm = volume.rolling(50, min_periods=50).mean()
    vs = volume.rolling(50, min_periods=50).std()
    z = (volume - vm) / vs.replace(0.0, np.nan)
    return (-1.0 * z * is_dn).replace([np.inf, -np.inf], np.nan)


# === UP-DAY VOLUME ANOMALY =================================================


def f28pd_f28_price_volume_divergence_up_day_low_vol_60d_base_v045_signal(closeadj, volume):
    """On up-days: -log(volume / 60d-mean-volume). Positive when up-day on LOW volume = divergence."""
    is_up = (closeadj.diff(1) > 0).astype(float).where(~closeadj.diff(1).isna())
    vm = volume.rolling(60, min_periods=60).mean()
    return (-np.log(volume / vm.replace(0.0, np.nan)) * is_up).replace([np.inf, -np.inf], np.nan)


# === HIGH/LOW CONFIRMATION (uses high/low, OHLC) ===========================


def f28pd_f28_price_volume_divergence_high_unconf_5d_base_v046_signal(high, volume):
    """1 if today is 5d-high but volume is below 5d-mean. Intraday-scale unconfirmed high."""
    h5 = high.rolling(5, min_periods=5).max()
    vm = volume.rolling(5, min_periods=5).mean()
    out = ((high >= h5).astype(float) * (volume < vm).astype(float)).where(~h5.isna() & ~vm.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_low_unconf_5d_base_v047_signal(low, volume):
    """1 if today is 5d-low but volume is below 5d-mean. Intraday-scale unconfirmed low."""
    l5 = low.rolling(5, min_periods=5).min()
    vm = volume.rolling(5, min_periods=5).mean()
    out = ((low <= l5).astype(float) * (volume < vm).astype(float)).where(~l5.isna() & ~vm.isna())
    return out.replace([np.inf, -np.inf], np.nan)


# === SIGN-OF-PRICE * SIGN-OF-VOL-PRODUCT ===================================


def f28pd_f28_price_volume_divergence_neg_prod_sign_30d_base_v048_signal(closeadj, volume):
    """-1 * sign(price.diff(30)) * sign(volume.diff(30)). +1 = diverging."""
    return (-1.0 * np.sign(closeadj.diff(30)) * np.sign(volume.diff(30))).replace([np.inf, -np.inf], np.nan)


# === VOLUME-PRICE TREND DIFFERENTIAL (using EMA) ===========================


def f28pd_f28_price_volume_divergence_ema_diff_log_70d_base_v049_signal(closeadj, volume):
    """log(EMA(close,70)/EMA(close,70).shift(21)) - log(EMA(vol,70)/EMA(vol,70).shift(21)).
    Smoothed slope-of-MAs differential."""
    ec = _ema(closeadj, 70)
    ev = _ema(volume, 70)
    return (np.log(ec / ec.shift(21)) - np.log(ev / ev.shift(21).replace(0.0, np.nan))).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_sma_diff_log_25d_base_v050_signal(close, volume):
    """log(SMA(close,25)/SMA(close,25).shift(10)) - log(SMA(vol,25)/SMA(vol,25).shift(10))."""
    mc = _sma(close, 25)
    mv = _sma(volume, 25)
    return (np.log(mc / mc.shift(10)) - np.log(mv / mv.shift(10).replace(0.0, np.nan))).replace([np.inf, -np.inf], np.nan)


# === RANK OF (PRICE) MINUS RANK OF (VOLUME) ================================


def f28pd_f28_price_volume_divergence_rank_diff_45d_base_v051_signal(closeadj, volume):
    """percentile_rank(close,45d) - percentile_rank(volume,45d). Cross-sectional rank gap."""
    rc = closeadj.rolling(45, min_periods=45).rank(pct=True)
    rv = volume.rolling(45, min_periods=45).rank(pct=True)
    return (rc - rv).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_rank_diff_180d_base_v052_signal(closeadj, volume):
    """percentile_rank(close,180d) - percentile_rank(volume,180d). Long-window rank gap."""
    rc = closeadj.rolling(180, min_periods=180).rank(pct=True)
    rv = volume.rolling(180, min_periods=180).rank(pct=True)
    return (rc - rv).replace([np.inf, -np.inf], np.nan)


# === ROC RATIO PRICE / ROC RATIO VOLUME ====================================


def f28pd_f28_price_volume_divergence_roc_ratio_log_22d_base_v053_signal(close, volume):
    """log((close/close.shift(22)) / (volume/volume.shift(22))). Pure log-ROC ratio."""
    rp = close / close.shift(22)
    rv = volume / volume.shift(22).replace(0.0, np.nan)
    return np.log(rp / rv).replace([np.inf, -np.inf], np.nan)


# === BEARISH/BULLISH DIV COUNTS ============================================


def f28pd_f28_price_volume_divergence_bear_count_60d_base_v054_signal(closeadj, volume):
    """Count of bearish divergence days (price up >0 but volume down <0) over 60d."""
    bear = ((closeadj.diff(1) > 0) & (volume.diff(1) < 0)).astype(float).where(~closeadj.diff(1).isna() & ~volume.diff(1).isna())
    return bear.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_bull_count_60d_base_v055_signal(closeadj, volume):
    """Count of bullish divergence days (price down <0 but volume up >0) over 60d."""
    bull = ((closeadj.diff(1) < 0) & (volume.diff(1) > 0)).astype(float).where(~closeadj.diff(1).isna() & ~volume.diff(1).isna())
    return bull.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_bear_minus_bull_120d_base_v056_signal(closeadj, volume):
    """(bear_count - bull_count) over 120d. Net bias of divergence type."""
    bear = ((closeadj.diff(1) > 0) & (volume.diff(1) < 0)).astype(float).where(~closeadj.diff(1).isna() & ~volume.diff(1).isna())
    bull = ((closeadj.diff(1) < 0) & (volume.diff(1) > 0)).astype(float).where(~closeadj.diff(1).isna() & ~volume.diff(1).isna())
    return (bear - bull).rolling(120, min_periods=120).sum().replace([np.inf, -np.inf], np.nan)


# === MOMENTUM RATIO PRICE vs VOLUME (signed) ===============================


def f28pd_f28_price_volume_divergence_mom_diff_signed_45d_base_v057_signal(closeadj, volume):
    """(close-close.shift(45))/close.shift(45)  -  (vol-vol.shift(45))/vol.shift(45). Signed ROC diff."""
    pc = closeadj.pct_change(45)
    vc = volume.pct_change(45)
    return (pc - vc).replace([np.inf, -np.inf], np.nan)


# === ABSOLUTE DIVERGENCE INTEGRAL ==========================================


def f28pd_f28_price_volume_divergence_integral_abs_30d_base_v058_signal(close, volume):
    """Sum over 30d of |z(price.diff) - z(volume.diff)|. Standardized cumulative divergence."""
    pd_ = close.diff(1)
    vd = volume.diff(1)
    zp = (pd_ - pd_.rolling(30, min_periods=30).mean()) / pd_.rolling(30, min_periods=30).std().replace(0.0, np.nan)
    zv = (vd - vd.rolling(30, min_periods=30).mean()) / vd.rolling(30, min_periods=30).std().replace(0.0, np.nan)
    return (zp - zv).abs().rolling(30, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


# === VOLUME WEIGHTED PRICE DEVIATION =======================================


def f28pd_f28_price_volume_divergence_vwap_dev_65d_base_v059_signal(closeadj, volume):
    """(close - VWAP_65d) / close. VWAP = sum(close*vol)/sum(vol). Diverges when price runs ahead of weighted avg."""
    n = 65
    vwap = (closeadj * volume).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return ((closeadj - vwap) / closeadj).replace([np.inf, -np.inf], np.nan)


# === EXPANDING DIVERGENCE STREAK ===========================================


def f28pd_f28_price_volume_divergence_streak_disagree_5d_base_v060_signal(close, volume):
    """Consecutive bars (last 5) where sign(close.diff(1)) != sign(volume.diff(1)). Short streak."""
    sp = np.sign(close.diff(1))
    sv = np.sign(volume.diff(1))
    bit = (sp != sv).astype(float).where(~sp.isna() & ~sv.isna())
    def _consec(x):
        c = 0
        for v in x[::-1]:
            if v > 0.5:
                c += 1
            else:
                break
        return float(c)
    return bit.rolling(5, min_periods=5).apply(_consec, raw=True).replace([np.inf, -np.inf], np.nan)


# === DIVERGENCE FREQUENCY VS BASELINE ======================================


def f28pd_f28_price_volume_divergence_xor_freq_excess_80d_base_v061_signal(closeadj, volume):
    """20d XOR-frequency minus 80d mean of 20d XOR-frequency. Recent vs baseline divergence."""
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    bit = (sp != sv).astype(float).where(~sp.isna() & ~sv.isna())
    freq = bit.rolling(20, min_periods=20).mean()
    return (freq - freq.rolling(80, min_periods=80).mean()).replace([np.inf, -np.inf], np.nan)


# === EXTREME VOLUME ON COUNTER-PRICE-DAY ===================================


def f28pd_f28_price_volume_divergence_counter_extreme_vol_45d_base_v062_signal(closeadj, volume):
    """Most-recent volume z-score among last 45d on counter-trend days (price-direction != avg direction).
    Computed as mean z-vol of counter-days in last 45 bars."""
    rp = closeadj.diff(1)
    sgn_avg = np.sign(closeadj.diff(45))
    counter = (np.sign(rp) != sgn_avg).astype(float).where(~rp.isna() & ~sgn_avg.isna())
    vm = volume.rolling(45, min_periods=45).mean()
    vs = volume.rolling(45, min_periods=45).std()
    zv = (volume - vm) / vs.replace(0.0, np.nan)
    return (counter * zv).rolling(45, min_periods=45).mean().replace([np.inf, -np.inf], np.nan)


# === STANDARDIZED PRICE MOVE / STANDARDIZED VOLUME MOVE ====================


def f28pd_f28_price_volume_divergence_z_diff_25d_base_v063_signal(close, volume):
    """z(close.pct_change, 25) - z(volume.pct_change, 25). Standardized intraday divergence."""
    rp = close.pct_change()
    rv = volume.pct_change()
    zp = (rp - rp.rolling(25, min_periods=25).mean()) / rp.rolling(25, min_periods=25).std().replace(0.0, np.nan)
    zv = (rv - rv.rolling(25, min_periods=25).mean()) / rv.rolling(25, min_periods=25).std().replace(0.0, np.nan)
    return (zp - zv).replace([np.inf, -np.inf], np.nan)


# === ROLLING MAX-DIVERGENCE-GAP (peak-vs-trough timing) ====================


def f28pd_f28_price_volume_divergence_peakgap_120d_base_v064_signal(closeadj, volume):
    """Bars between 120d price-peak and 120d volume-peak (signed: price-peak-idx minus vol-peak-idx).
    Positive = price peaked after volume (a classic divergence pattern)."""
    a_idx = closeadj.rolling(120, min_periods=120).apply(lambda x: float(int(np.argmax(x))), raw=True)
    b_idx = volume.rolling(120, min_periods=120).apply(lambda x: float(int(np.argmax(x))), raw=True)
    return (a_idx - b_idx).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_troughgap_60d_base_v065_signal(closeadj, volume):
    """Bars between 60d price-trough and 60d volume-trough (signed)."""
    a_idx = closeadj.rolling(60, min_periods=60).apply(lambda x: float(int(np.argmin(x))), raw=True)
    b_idx = volume.rolling(60, min_periods=60).apply(lambda x: float(int(np.argmin(x))), raw=True)
    return (a_idx - b_idx).replace([np.inf, -np.inf], np.nan)


# === SIGN OF SLOPE-DIFFERENCE (discrete regime) ============================


def f28pd_f28_price_volume_divergence_slope_sign_diff_80d_base_v066_signal(closeadj, volume):
    """sign(slope(close,80)) - sign(slope(volume,80)). Range {-2,0,2}."""
    sc = closeadj.rolling(80, min_periods=80).apply(_slope_raw_fn, raw=True)
    sv = volume.rolling(80, min_periods=80).apply(_slope_raw_fn, raw=True)
    return (np.sign(sc) - np.sign(sv)).replace([np.inf, -np.inf], np.nan)


# === ABS SLOPE DIFF RANK ===================================================


def f28pd_f28_price_volume_divergence_absslope_diff_rank_60d_base_v067_signal(closeadj, volume):
    """60d percentile rank of |slope(log-close,30) - slope(log-vol,30)|."""
    sp = np.log(closeadj).rolling(30, min_periods=30).apply(_slope_raw_fn, raw=True)
    sv = np.log(volume.replace(0.0, np.nan)).rolling(30, min_periods=30).apply(_slope_raw_fn, raw=True)
    return (sp - sv).abs().rolling(60, min_periods=60).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === DOWN-DAY VOL FRACTION (asymmetry) =====================================


def f28pd_f28_price_volume_divergence_downvol_frac_75d_base_v068_signal(closeadj, volume):
    """sum_vol_on_down_days / sum_total_vol over 75d. Higher = down-day volume dominates."""
    dn = (closeadj.diff(1) < 0).astype(float)
    dv = (dn * volume).rolling(75, min_periods=75).sum()
    tv = volume.rolling(75, min_periods=75).sum()
    return (dv / tv.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === MIN-MAX NORMALIZED DIVERGENCE =========================================


def f28pd_f28_price_volume_divergence_minmax_dev_45d_base_v069_signal(closeadj, volume):
    """(close-close.min_45)/range_45 - (vol-vol.min_45)/range_45. Position-in-range gap."""
    cmin = closeadj.rolling(45, min_periods=45).min()
    cmax = closeadj.rolling(45, min_periods=45).max()
    vmin = volume.rolling(45, min_periods=45).min()
    vmax = volume.rolling(45, min_periods=45).max()
    cp = (closeadj - cmin) / (cmax - cmin).replace(0.0, np.nan)
    vp = (volume - vmin) / (vmax - vmin).replace(0.0, np.nan)
    return (cp - vp).replace([np.inf, -np.inf], np.nan)


# === VOLUME-SHOCK ON FLAT PRICE ============================================


def f28pd_f28_price_volume_divergence_vol_shock_flat_50d_base_v070_signal(closeadj, volume):
    """volume z-score (50d) multiplied by indicator that |price.pct_change| < 0.2 sigma. Vol shock without price reaction."""
    rp = closeadj.pct_change()
    sd = rp.rolling(50, min_periods=50).std()
    flat = (rp.abs() < 0.2 * sd).astype(float).where(~rp.isna() & ~sd.isna())
    vm = volume.rolling(50, min_periods=50).mean()
    vs = volume.rolling(50, min_periods=50).std()
    zv = (volume - vm) / vs.replace(0.0, np.nan)
    return (flat * zv).replace([np.inf, -np.inf], np.nan)


# === LOG VOLUME REGRESSION RESIDUAL ========================================


def f28pd_f28_price_volume_divergence_logvol_resid_close_60d_base_v071_signal(closeadj, volume):
    """Residual of log-volume from OLS on log-close over 60d (current point's residual).
    High abs = divergence. y_hat = a + b*x where b = cov/var, a = my - b*mx."""
    n = 60
    lp = np.log(closeadj)
    lv = np.log(volume.replace(0.0, np.nan))
    mx = lp.rolling(n, min_periods=n).mean()
    my = lv.rolling(n, min_periods=n).mean()
    vx = lp.rolling(n, min_periods=n).var()
    cxy = lp.rolling(n, min_periods=n).cov(lv)
    b = cxy / vx.replace(0.0, np.nan)
    a = my - b * mx
    return (lv - (a + b * lp)).replace([np.inf, -np.inf], np.nan)


# === RANGE EXPANSION VS VOLUME EXPANSION ===================================


def f28pd_f28_price_volume_divergence_range_vol_expand_40d_base_v072_signal(high, low, volume):
    """log((high-low) / mean_40d(high-low)) - log(volume/mean_40d(volume)).
    Range-expansion not matched by volume expansion = divergence."""
    rng = high - low
    rng_norm = rng / rng.rolling(40, min_periods=40).mean()
    vol_norm = volume / volume.rolling(40, min_periods=40).mean()
    return (np.log(rng_norm) - np.log(vol_norm.replace(0.0, np.nan))).replace([np.inf, -np.inf], np.nan)


# === VOL OF DIVERGENCE SIGNAL ==============================================


def f28pd_f28_price_volume_divergence_corr_volatility_70d_base_v073_signal(closeadj, volume):
    """70d std of 20d corr(price.pct, vol.pct). High std = unstable agreement (regime change)."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    c20 = rp.rolling(20, min_periods=20).corr(rv)
    return c20.rolling(70, min_periods=70).std().replace([np.inf, -np.inf], np.nan)


# === DIVERGENCE EVENT DAYS-SINCE ===========================================


def f28pd_f28_price_volume_divergence_days_since_bear_event_60d_base_v074_signal(closeadj, volume):
    """Bars since last bearish-divergence event (price up but volume down in last 5d simultaneously) in 60d window."""
    up5 = (closeadj.diff(5) > 0).astype(float)
    dn5v = (volume.diff(5) < 0).astype(float)
    ev = (up5 * dn5v).where(~closeadj.diff(5).isna() & ~volume.diff(5).isna())
    return ev.rolling(60, min_periods=60).apply(_streak_idx, raw=True).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_days_since_bull_event_100d_base_v075_signal(closeadj, volume):
    """Bars since last bullish-divergence event (price down but volume up in last 5d) in 100d window."""
    dn5 = (closeadj.diff(5) < 0).astype(float)
    up5v = (volume.diff(5) > 0).astype(float)
    ev = (dn5 * up5v).where(~closeadj.diff(5).isna() & ~volume.diff(5).isna())
    return ev.rolling(100, min_periods=100).apply(_streak_idx, raw=True).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f28_price_volume_divergence_base_001_075_REGISTRY = {
    "f28pd_f28_price_volume_divergence_sign_xor_close_vol_5d_base_v001_signal": {"inputs": ["close", "volume"], "func": f28pd_f28_price_volume_divergence_sign_xor_close_vol_5d_base_v001_signal},
    "f28pd_f28_price_volume_divergence_xor_count_20d_base_v002_signal": {"inputs": ["close", "volume"], "func": f28pd_f28_price_volume_divergence_xor_count_20d_base_v002_signal},
    "f28pd_f28_price_volume_divergence_xor_count_60d_base_v003_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_xor_count_60d_base_v003_signal},
    "f28pd_f28_price_volume_divergence_xor_streak_40d_base_v004_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_xor_streak_40d_base_v004_signal},
    "f28pd_f28_price_volume_divergence_slope_diff_sign_15d_base_v005_signal": {"inputs": ["close", "volume"], "func": f28pd_f28_price_volume_divergence_slope_diff_sign_15d_base_v005_signal},
    "f28pd_f28_price_volume_divergence_slope_diff_45d_base_v006_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_slope_diff_45d_base_v006_signal},
    "f28pd_f28_price_volume_divergence_slope_diff_abs_120d_base_v007_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_slope_diff_abs_120d_base_v007_signal},
    "f28pd_f28_price_volume_divergence_corr_pct_30d_base_v008_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_corr_pct_30d_base_v008_signal},
    "f28pd_f28_price_volume_divergence_corr_pct_90d_base_v009_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_corr_pct_90d_base_v009_signal},
    "f28pd_f28_price_volume_divergence_corr_diff_45d_base_v010_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_corr_diff_45d_base_v010_signal},
    "f28pd_f28_price_volume_divergence_neg_corr_pct_60d_base_v011_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_neg_corr_pct_60d_base_v011_signal},
    "f28pd_f28_price_volume_divergence_spearman_50d_base_v012_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_spearman_50d_base_v012_signal},
    "f28pd_f28_price_volume_divergence_spearman_100d_base_v013_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_spearman_100d_base_v013_signal},
    "f28pd_f28_price_volume_divergence_beta_vol_price_55d_base_v014_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_beta_vol_price_55d_base_v014_signal},
    "f28pd_f28_price_volume_divergence_beta_sign_120d_base_v015_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_beta_sign_120d_base_v015_signal},
    "f28pd_f28_price_volume_divergence_bear_div_unconf_high_30d_base_v016_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_bear_div_unconf_high_30d_base_v016_signal},
    "f28pd_f28_price_volume_divergence_bull_div_unconf_low_30d_base_v017_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_bull_div_unconf_low_30d_base_v017_signal},
    "f28pd_f28_price_volume_divergence_days_since_unconf_high_60d_base_v018_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_days_since_unconf_high_60d_base_v018_signal},
    "f28pd_f28_price_volume_divergence_days_since_unconf_low_80d_base_v019_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_days_since_unconf_low_80d_base_v019_signal},
    "f28pd_f28_price_volume_divergence_skew_diff_50d_base_v020_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_skew_diff_50d_base_v020_signal},
    "f28pd_f28_price_volume_divergence_vol_ratio_log_60d_base_v021_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_vol_ratio_log_60d_base_v021_signal},
    "f28pd_f28_price_volume_divergence_kurt_diff_80d_base_v022_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_kurt_diff_80d_base_v022_signal},
    "f28pd_f28_price_volume_divergence_obv_close_slope_diff_45d_base_v023_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_obv_close_slope_diff_45d_base_v023_signal},
    "f28pd_f28_price_volume_divergence_obv_sign_disagree_30d_base_v024_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_obv_sign_disagree_30d_base_v024_signal},
    "f28pd_f28_price_volume_divergence_tanh_div_signed_30d_base_v025_signal": {"inputs": ["close", "volume"], "func": f28pd_f28_price_volume_divergence_tanh_div_signed_30d_base_v025_signal},
    "f28pd_f28_price_volume_divergence_arctan_slope_diff_50d_base_v026_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_arctan_slope_diff_50d_base_v026_signal},
    "f28pd_f28_price_volume_divergence_sigmoid_xor_freq_40d_base_v027_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_sigmoid_xor_freq_40d_base_v027_signal},
    "f28pd_f28_price_volume_divergence_updown_vol_asym_100d_base_v029_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_updown_vol_asym_100d_base_v029_signal},
    "f28pd_f28_price_volume_divergence_max_neg_corr_window_60d_base_v030_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_max_neg_corr_window_60d_base_v030_signal},
    "f28pd_f28_price_volume_divergence_corr_dev_from_mean_120d_base_v031_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_corr_dev_from_mean_120d_base_v031_signal},
    "f28pd_f28_price_volume_divergence_resid_std_vol_on_price_50d_base_v032_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_resid_std_vol_on_price_50d_base_v032_signal},
    "f28pd_f28_price_volume_divergence_rsq_vol_on_price_80d_base_v033_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_rsq_vol_on_price_80d_base_v033_signal},
    "f28pd_f28_price_volume_divergence_cum_sign_diff_45d_base_v034_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_cum_sign_diff_45d_base_v034_signal},
    "f28pd_f28_price_volume_divergence_cum_div_zscore_100d_base_v035_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_cum_div_zscore_100d_base_v035_signal},
    "f28pd_f28_price_volume_divergence_hidden_bull_25d_base_v036_signal": {"inputs": ["close", "volume"], "func": f28pd_f28_price_volume_divergence_hidden_bull_25d_base_v036_signal},
    "f28pd_f28_price_volume_divergence_hidden_bear_50d_base_v037_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_hidden_bear_50d_base_v037_signal},
    "f28pd_f28_price_volume_divergence_lead_lag_corr_diff_60d_base_v038_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_lead_lag_corr_diff_60d_base_v038_signal},
    "f28pd_f28_price_volume_divergence_corr_lag_minus_synced_45d_base_v039_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_corr_lag_minus_synced_45d_base_v039_signal},
    "f28pd_f28_price_volume_divergence_xor_freq_pctrank_120d_base_v040_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_xor_freq_pctrank_120d_base_v040_signal},
    "f28pd_f28_price_volume_divergence_sharpe_div_30d_base_v041_signal": {"inputs": ["close", "volume"], "func": f28pd_f28_price_volume_divergence_sharpe_div_30d_base_v041_signal},
    "f28pd_f28_price_volume_divergence_corr_sign_60d_base_v042_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_corr_sign_60d_base_v042_signal},
    "f28pd_f28_price_volume_divergence_neg_corr_frac_100d_base_v043_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_neg_corr_frac_100d_base_v043_signal},
    "f28pd_f28_price_volume_divergence_down_day_vol_zscore_50d_base_v044_signal": {"inputs": ["close", "volume"], "func": f28pd_f28_price_volume_divergence_down_day_vol_zscore_50d_base_v044_signal},
    "f28pd_f28_price_volume_divergence_up_day_low_vol_60d_base_v045_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_up_day_low_vol_60d_base_v045_signal},
    "f28pd_f28_price_volume_divergence_high_unconf_5d_base_v046_signal": {"inputs": ["high", "volume"], "func": f28pd_f28_price_volume_divergence_high_unconf_5d_base_v046_signal},
    "f28pd_f28_price_volume_divergence_low_unconf_5d_base_v047_signal": {"inputs": ["low", "volume"], "func": f28pd_f28_price_volume_divergence_low_unconf_5d_base_v047_signal},
    "f28pd_f28_price_volume_divergence_neg_prod_sign_30d_base_v048_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_neg_prod_sign_30d_base_v048_signal},
    "f28pd_f28_price_volume_divergence_ema_diff_log_70d_base_v049_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_ema_diff_log_70d_base_v049_signal},
    "f28pd_f28_price_volume_divergence_sma_diff_log_25d_base_v050_signal": {"inputs": ["close", "volume"], "func": f28pd_f28_price_volume_divergence_sma_diff_log_25d_base_v050_signal},
    "f28pd_f28_price_volume_divergence_rank_diff_45d_base_v051_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_rank_diff_45d_base_v051_signal},
    "f28pd_f28_price_volume_divergence_rank_diff_180d_base_v052_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_rank_diff_180d_base_v052_signal},
    "f28pd_f28_price_volume_divergence_roc_ratio_log_22d_base_v053_signal": {"inputs": ["close", "volume"], "func": f28pd_f28_price_volume_divergence_roc_ratio_log_22d_base_v053_signal},
    "f28pd_f28_price_volume_divergence_bear_count_60d_base_v054_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_bear_count_60d_base_v054_signal},
    "f28pd_f28_price_volume_divergence_bull_count_60d_base_v055_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_bull_count_60d_base_v055_signal},
    "f28pd_f28_price_volume_divergence_bear_minus_bull_120d_base_v056_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_bear_minus_bull_120d_base_v056_signal},
    "f28pd_f28_price_volume_divergence_mom_diff_signed_45d_base_v057_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_mom_diff_signed_45d_base_v057_signal},
    "f28pd_f28_price_volume_divergence_integral_abs_30d_base_v058_signal": {"inputs": ["close", "volume"], "func": f28pd_f28_price_volume_divergence_integral_abs_30d_base_v058_signal},
    "f28pd_f28_price_volume_divergence_vwap_dev_65d_base_v059_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_vwap_dev_65d_base_v059_signal},
    "f28pd_f28_price_volume_divergence_streak_disagree_5d_base_v060_signal": {"inputs": ["close", "volume"], "func": f28pd_f28_price_volume_divergence_streak_disagree_5d_base_v060_signal},
    "f28pd_f28_price_volume_divergence_xor_freq_excess_80d_base_v061_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_xor_freq_excess_80d_base_v061_signal},
    "f28pd_f28_price_volume_divergence_counter_extreme_vol_45d_base_v062_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_counter_extreme_vol_45d_base_v062_signal},
    "f28pd_f28_price_volume_divergence_z_diff_25d_base_v063_signal": {"inputs": ["close", "volume"], "func": f28pd_f28_price_volume_divergence_z_diff_25d_base_v063_signal},
    "f28pd_f28_price_volume_divergence_peakgap_120d_base_v064_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_peakgap_120d_base_v064_signal},
    "f28pd_f28_price_volume_divergence_troughgap_60d_base_v065_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_troughgap_60d_base_v065_signal},
    "f28pd_f28_price_volume_divergence_slope_sign_diff_80d_base_v066_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_slope_sign_diff_80d_base_v066_signal},
    "f28pd_f28_price_volume_divergence_absslope_diff_rank_60d_base_v067_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_absslope_diff_rank_60d_base_v067_signal},
    "f28pd_f28_price_volume_divergence_downvol_frac_75d_base_v068_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_downvol_frac_75d_base_v068_signal},
    "f28pd_f28_price_volume_divergence_minmax_dev_45d_base_v069_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_minmax_dev_45d_base_v069_signal},
    "f28pd_f28_price_volume_divergence_vol_shock_flat_50d_base_v070_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_vol_shock_flat_50d_base_v070_signal},
    "f28pd_f28_price_volume_divergence_logvol_resid_close_60d_base_v071_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_logvol_resid_close_60d_base_v071_signal},
    "f28pd_f28_price_volume_divergence_range_vol_expand_40d_base_v072_signal": {"inputs": ["high", "low", "volume"], "func": f28pd_f28_price_volume_divergence_range_vol_expand_40d_base_v072_signal},
    "f28pd_f28_price_volume_divergence_corr_volatility_70d_base_v073_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_corr_volatility_70d_base_v073_signal},
    "f28pd_f28_price_volume_divergence_days_since_bear_event_60d_base_v074_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_days_since_bear_event_60d_base_v074_signal},
    "f28pd_f28_price_volume_divergence_days_since_bull_event_100d_base_v075_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_days_since_bull_event_100d_base_v075_signal},
}


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------


def _synthetic_inputs(n: int = 800, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    seg = n // 4
    rest = n - 3 * seg
    ret = np.concatenate([
        rng.normal(0.0012, 0.011, seg),
        rng.normal(-0.0005, 0.018, seg),
        rng.normal(-0.0010, 0.014, seg),
        rng.normal(0.0008, 0.012, rest),
    ])
    close = 50.0 * np.exp(np.cumsum(ret))
    adj_drift = rng.normal(0.0, 0.0003, size=n).cumsum()
    closeadj = close * np.exp(adj_drift)
    intraday = rng.normal(0.0, 0.008, size=n)
    open_ = close * np.exp(-intraday * 0.5)
    high = np.maximum(close, open_) * np.exp(np.abs(rng.normal(0.0, 0.006, size=n)))
    low = np.minimum(close, open_) * np.exp(-np.abs(rng.normal(0.0, 0.006, size=n)))
    volume = rng.lognormal(mean=13.0, sigma=0.6, size=n)
    idx = pd.RangeIndex(n)
    return pd.DataFrame({
        "open": pd.Series(open_, index=idx, dtype=float),
        "high": pd.Series(high, index=idx, dtype=float),
        "low": pd.Series(low, index=idx, dtype=float),
        "close": pd.Series(close, index=idx, dtype=float),
        "closeadj": pd.Series(closeadj, index=idx, dtype=float),
        "volume": pd.Series(volume, index=idx, dtype=float),
    })


def _self_test() -> None:
    df = _synthetic_inputs(n=800, seed=42)
    results: dict[str, pd.Series] = {}
    for name, entry in f28_price_volume_divergence_base_001_075_REGISTRY.items():
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out, pd.Series), f"{name}: not a Series"
        assert len(out) == len(df), f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0, f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1, f"{name}: constant/all-zero"
        results[name] = out

    warm = 252
    coverage_ok = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5)
    frac = coverage_ok / len(results)
    assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:]
    aligned = aligned.replace([np.inf, -np.inf], np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        for i, a in enumerate(corr.columns):
            for j, b in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i, j]:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK base_001_075: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
