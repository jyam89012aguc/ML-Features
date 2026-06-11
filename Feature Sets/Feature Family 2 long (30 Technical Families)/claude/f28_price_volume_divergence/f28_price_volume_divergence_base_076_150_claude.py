"""f28_price_volume_divergence base features 076-150.

Structurally distinct from base_001_075: different window-tier (longer or
mixed), different normalization (log vs z vs rank), different aggregation
(median, MAD, quantile), and several rank/percentile/streak families not
used in file 1. Same domain: price-volume DISAGREEMENT.

NaN policy: only replace(inf,nan) at the final return; no fillna.
Window > 21d -> closeadj; <= 21d -> close. OHLC for in-bar features.
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


def _streak_idx(x):
    idx = np.where(x > 0.5)[0]
    if idx.size == 0:
        return float(len(x))
    return float(len(x) - 1 - idx[-1])


def _slope_raw(x):
    n = len(x); t = np.arange(n, dtype=float)
    mt = t.mean(); mx = x.mean()
    var = float(np.sum((t - mt) ** 2))
    if var == 0.0:
        return np.nan
    return float(np.sum((t - mt) * (x - mx)) / var)


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


# === LONGER-WINDOW XOR FAMILY (different bracket than file 1) ==============


def f28pd_f28_price_volume_divergence_xor_count_180d_base_v076_signal(closeadj, volume):
    """Count of XOR-disagreement bits over 180d (long-baseline divergence frequency)."""
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    bit = (sp != sv).astype(float).where(~sp.isna() & ~sv.isna())
    return bit.rolling(180, min_periods=180).sum().replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_xor_ema_freq_45d_base_v077_signal(closeadj, volume):
    """EMA(45) of disagreement bit (smoothed disagreement frequency)."""
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    bit = (sp != sv).astype(float).where(~sp.isna() & ~sv.isna())
    return bit.ewm(span=45, adjust=False, min_periods=45).mean().replace([np.inf, -np.inf], np.nan)


# === MEDIAN-BASED divergence (robust kernel; file 1 used SMA/EMA only) =====


def f28pd_f28_price_volume_divergence_median_diff_log_50d_base_v078_signal(closeadj, volume):
    """log(median(close,50)/median(close,50).shift(21)) - log(median(vol,50)/median(vol,50).shift(21))."""
    mc = closeadj.rolling(50, min_periods=50).median()
    mv = volume.rolling(50, min_periods=50).median()
    return (np.log(mc / mc.shift(21)) - np.log(mv / mv.shift(21).replace(0.0, np.nan))).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_median_rank_diff_80d_base_v079_signal(closeadj, volume):
    """80d percentile rank of close-median minus 80d percentile rank of volume-median."""
    mc = closeadj.rolling(20, min_periods=20).median()
    mv = volume.rolling(20, min_periods=20).median()
    return (mc.rolling(80, min_periods=80).rank(pct=True) - mv.rolling(80, min_periods=80).rank(pct=True)).replace([np.inf, -np.inf], np.nan)


# === KENDALL-TAU-LIKE concordant/discordant count ==========================


def f28pd_f28_price_volume_divergence_concord_frac_35d_base_v080_signal(closeadj, volume):
    """Fraction of 35d pairs (i,j) where sign(close.diff)==sign(volume.diff). Low = divergence-dominant.
    Approximation: just rolling mean of equal-sign indicator."""
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    same = (sp == sv).astype(float).where(~sp.isna() & ~sv.isna())
    return same.rolling(35, min_periods=35).mean().replace([np.inf, -np.inf], np.nan)


# === EWM-CORRELATION between price.pct_change and volume.pct_change ========


def f28pd_f28_price_volume_divergence_ewm_corr_45d_base_v081_signal(closeadj, volume):
    """EWM correlation between close.pct_change and volume.pct_change at span 45."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    return rp.ewm(span=45, min_periods=45).corr(rv).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_ewm_corr_neg_115d_base_v082_signal(closeadj, volume):
    """-1 * EWM corr at span 115 between close.pct_change and volume.pct_change."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    return (-1.0 * rp.ewm(span=115, min_periods=115).corr(rv)).replace([np.inf, -np.inf], np.nan)


# === LONG-WINDOW SPEARMAN ==================================================


def f28pd_f28_price_volume_divergence_spearman_200d_base_v083_signal(closeadj, volume):
    """200d Spearman correlation between close and volume (rank-based)."""
    rc = closeadj.rolling(200, min_periods=200).rank(pct=False)
    rv = volume.rolling(200, min_periods=200).rank(pct=False)
    return rc.rolling(200, min_periods=200).corr(rv).replace([np.inf, -np.inf], np.nan)


# === BETA ON LOG-RETURNS (different scaling than v014/v015) ================


def f28pd_f28_price_volume_divergence_beta_logvolume_logreturn_75d_base_v084_signal(closeadj, volume):
    """OLS beta of log-volume.diff on log-close.diff over 75d. Negative = divergence."""
    rp = np.log(closeadj).diff()
    rv = np.log(volume.replace(0.0, np.nan)).diff()
    cov = rp.rolling(75, min_periods=75).cov(rv)
    var = rp.rolling(75, min_periods=75).var()
    return (cov / var.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_beta_dev_from_baseline_200d_base_v085_signal(closeadj, volume):
    """30d-beta minus 200d-mean of 30d-beta. Recent beta deviation from baseline."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    cov = rp.rolling(30, min_periods=30).cov(rv)
    var = rp.rolling(30, min_periods=30).var()
    b = cov / var.replace(0.0, np.nan)
    return (b - b.rolling(200, min_periods=200).mean()).replace([np.inf, -np.inf], np.nan)


# === TRIPLE-WINDOW DIVERGENCE PEAK / TROUGH ================================


def f28pd_f28_price_volume_divergence_high_unconf_long_120d_base_v086_signal(closeadj, volume):
    """1 if today is 120d-high but volume is BELOW 120d-median. Long unconfirmed top."""
    cmax = closeadj.rolling(120, min_periods=120).max()
    vmed = volume.rolling(120, min_periods=120).median()
    out = ((closeadj >= cmax).astype(float) * (volume < vmed).astype(float)).where(~cmax.isna() & ~vmed.isna())
    return out.replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_low_unconf_long_120d_base_v087_signal(closeadj, volume):
    """1 if today is 120d-low but volume is BELOW 120d-median. Unclimactic bottom (often hidden bullish)."""
    cmin = closeadj.rolling(120, min_periods=120).min()
    vmed = volume.rolling(120, min_periods=120).median()
    out = ((closeadj <= cmin).astype(float) * (volume < vmed).astype(float)).where(~cmin.isna() & ~vmed.isna())
    return out.replace([np.inf, -np.inf], np.nan)


# === SHANNON ENTROPY OF SIGN PATTERN =======================================


def f28pd_f28_price_volume_divergence_sign_entropy_60d_base_v088_signal(closeadj, volume):
    """Shannon entropy (base 2) of (sgn_price, sgn_volume) joint distribution over 60d, 4 states.
    Range [0, 2]. Maximum entropy = perfectly random, low = one state dominates."""
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    code = (sp > 0).astype(float) * 2 + (sv > 0).astype(float)  # 0..3
    code = code.where(~sp.isna() & ~sv.isna())
    def _ent(x):
        if len(x) == 0 or not np.all(np.isfinite(x)):
            return np.nan
        u, c = np.unique(x, return_counts=True)
        p = c / c.sum()
        p = p[p > 0]
        return float(-np.sum(p * np.log2(p)))
    return code.rolling(60, min_periods=60).apply(_ent, raw=True).replace([np.inf, -np.inf], np.nan)


# === EWM RATIO PRICE / EWM RATIO VOLUME (with different spans) =============


def f28pd_f28_price_volume_divergence_ewm_log_ratio_short_long_base_v089_signal(closeadj, volume):
    """log(EMA(close,12)/EMA(close,40)) - log(EMA(vol,12)/EMA(vol,40)). Short/long EMA differential gap."""
    return (np.log(_ema(closeadj, 12) / _ema(closeadj, 40)) - np.log(_ema(volume, 12) / _ema(volume, 40))).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_ewm_log_ratio_mid_long_base_v090_signal(closeadj, volume):
    """log(EMA(close,30)/EMA(close,90)) - log(EMA(vol,30)/EMA(vol,90)). Mid/long differential."""
    return (np.log(_ema(closeadj, 30) / _ema(closeadj, 90)) - np.log(_ema(volume, 30) / _ema(volume, 90))).replace([np.inf, -np.inf], np.nan)


# === MAD-NORMALIZED DIVERGENCE ============================================


def f28pd_f28_price_volume_divergence_mad_div_45d_base_v091_signal(closeadj, volume):
    """|close.diff - median(close.diff,45)| - |volume.diff - median(volume.diff,45)|. Robust gap."""
    cp = closeadj.diff(1)
    cv = volume.diff(1)
    mc = cp.rolling(45, min_periods=45).median()
    mv = cv.rolling(45, min_periods=45).median()
    return ((cp - mc).abs() - (cv - mv).abs()).replace([np.inf, -np.inf], np.nan)


# === DIVERGENCE PERSISTENCE (autocorr of XOR-bit) ==========================


def f28pd_f28_price_volume_divergence_xor_autocorr_lag1_80d_base_v092_signal(closeadj, volume):
    """80d autocorr(lag=1) of disagreement-bit. Persistent disagreement state = positive AC."""
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    bit = (sp != sv).astype(float).where(~sp.isna() & ~sv.isna())
    return bit.rolling(80, min_periods=80).apply(lambda x: float(pd.Series(x).autocorr(lag=1)) if pd.Series(x).std() > 0 else np.nan, raw=False).replace([np.inf, -np.inf], np.nan)


# === UP/DOWN VOLUME asymmetry at different aggregation =====================


def f28pd_f28_price_volume_divergence_updown_vol_diff_zscore_45d_base_v093_signal(closeadj, volume):
    """z-score (over 45d) of (sum_vol_up_5d - sum_vol_down_5d). Recent up-vs-down skew."""
    up5 = ((closeadj.diff(1) > 0).astype(float) * volume).rolling(5, min_periods=5).sum()
    dn5 = ((closeadj.diff(1) < 0).astype(float) * volume).rolling(5, min_periods=5).sum()
    diff = up5 - dn5
    return ((diff - diff.rolling(45, min_periods=45).mean()) / diff.rolling(45, min_periods=45).std().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === VOLUME-WEIGHTED-RETURN VS UNWEIGHTED RETURN ===========================


def f28pd_f28_price_volume_divergence_vwret_unwret_diff_30d_base_v094_signal(close, volume):
    """sum(ret*vol)/sum(vol) - mean(ret) over 30d. If positive, volume tilts toward positive returns."""
    r = close.pct_change()
    vw = (r * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    uw = r.rolling(30, min_periods=30).mean()
    return (vw - uw).replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_vwret_unwret_diff_120d_base_v095_signal(closeadj, volume):
    """120d version of v094. Long-window vol-weighted vs unweighted return gap."""
    r = closeadj.pct_change()
    vw = (r * volume).rolling(120, min_periods=120).sum() / volume.rolling(120, min_periods=120).sum().replace(0.0, np.nan)
    uw = r.rolling(120, min_periods=120).mean()
    return (vw - uw).replace([np.inf, -np.inf], np.nan)


# === SIGN OF MA-DIFFERENTIAL (discrete) ====================================


def f28pd_f28_price_volume_divergence_sma_diff_sign_30d_base_v096_signal(closeadj, volume):
    """sign(SMA(close,30)/SMA(close,30).shift(15)) - sign(SMA(vol,30)/SMA(vol,30).shift(15)).
    Discrete trend-direction disagreement of MAs. Range {-2,0,2}."""
    mc = _sma(closeadj, 30)
    mv = _sma(volume, 30)
    sgnp = np.sign(np.log(mc / mc.shift(15)))
    sgnv = np.sign(np.log(mv / mv.shift(15)))
    return (sgnp - sgnv).replace([np.inf, -np.inf], np.nan)


# === ABSOLUTE DEVIATION STD (vol of div signal) ============================


def f28pd_f28_price_volume_divergence_xor_freq_std_60d_base_v097_signal(closeadj, volume):
    """60d std of 20d-XOR-frequency. High = unstable agreement regime."""
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    bit = (sp != sv).astype(float).where(~sp.isna() & ~sv.isna())
    freq = bit.rolling(20, min_periods=20).mean()
    return freq.rolling(60, min_periods=60).std().replace([np.inf, -np.inf], np.nan)


# === RANK OF RETURN VS RANK OF VOL-CHANGE ==================================


def f28pd_f28_price_volume_divergence_rank_ret_rank_volret_diff_50d_base_v098_signal(closeadj, volume):
    """50d rank(return.pct_change) - 50d rank(volume.pct_change). Cross-sectional return-rank gap."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    return (rp.rolling(50, min_periods=50).rank(pct=True) - rv.rolling(50, min_periods=50).rank(pct=True)).replace([np.inf, -np.inf], np.nan)


# === LONG-WINDOW UNCONFIRMED EXTREME RATE ==================================


def f28pd_f28_price_volume_divergence_unconf_high_rate_252d_base_v099_signal(closeadj, volume):
    """Fraction of last 252d on which today's close was 20d-high but volume was NOT 20d-high."""
    cmax = closeadj.rolling(20, min_periods=20).max()
    vmax = volume.rolling(20, min_periods=20).max()
    bit = ((closeadj >= cmax).astype(float) * (1.0 - (volume >= vmax).astype(float))).where(~cmax.isna() & ~vmax.isna())
    return bit.rolling(252, min_periods=252).mean().replace([np.inf, -np.inf], np.nan)


def f28pd_f28_price_volume_divergence_unconf_low_rate_252d_base_v100_signal(closeadj, volume):
    """Fraction of last 252d on which today's close was 20d-low but volume was NOT 20d-low."""
    cmin = closeadj.rolling(20, min_periods=20).min()
    vmin = volume.rolling(20, min_periods=20).min()
    bit = ((closeadj <= cmin).astype(float) * (1.0 - (volume <= vmin).astype(float))).where(~cmin.isna() & ~vmin.isna())
    return bit.rolling(252, min_periods=252).mean().replace([np.inf, -np.inf], np.nan)


# === DIVERGENCE ON LARGE-MAG DAYS ONLY =====================================


def f28pd_f28_price_volume_divergence_big_move_xor_60d_base_v101_signal(closeadj, volume):
    """Fraction of last 60d where |price.pct_change| > 60d std AND sign(price.diff) != sign(volume.diff).
    Sharpness-weighted divergence rate."""
    rp = closeadj.pct_change()
    big = (rp.abs() > rp.rolling(60, min_periods=60).std()).astype(float)
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    bit = (sp != sv).astype(float).where(~sp.isna() & ~sv.isna())
    return (big * bit).rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


# === DIVERGENCE-RANGE (DIFF OF MAX-MIN) ====================================


def f28pd_f28_price_volume_divergence_log_range_diff_40d_base_v102_signal(closeadj, volume):
    """log((max(close,40)-min(close,40))/close) - log((max(vol,40)-min(vol,40))/mean(vol,40)).
    Relative ranges differ."""
    pr = (closeadj.rolling(40, min_periods=40).max() - closeadj.rolling(40, min_periods=40).min()) / closeadj
    vr = (volume.rolling(40, min_periods=40).max() - volume.rolling(40, min_periods=40).min()) / volume.rolling(40, min_periods=40).mean()
    return (np.log(pr) - np.log(vr.replace(0.0, np.nan))).replace([np.inf, -np.inf], np.nan)


# === Z-SCORE PEAK ASYMMETRY ================================================


def f28pd_f28_price_volume_divergence_z_peak_asym_70d_base_v103_signal(closeadj, volume):
    """z(close,70) at most recent 70d-max minus z(volume,70) at most recent 70d-max."""
    n = 70
    cmax_z = ((closeadj - closeadj.rolling(n, min_periods=n).mean()) / closeadj.rolling(n, min_periods=n).std().replace(0.0, np.nan))
    vmax_z = ((volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan))
    return (cmax_z - vmax_z).replace([np.inf, -np.inf], np.nan)


# === CUMULATIVE SIGN PRODUCT (-1 = consistently disagreeing) ==============


def f28pd_f28_price_volume_divergence_cum_neg_prod_60d_base_v104_signal(closeadj, volume):
    """-1 * mean(sign(price.diff)*sign(vol.diff)) over 60d. +1 = persistent divergence, -1 = persistent agreement."""
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    return (-1.0 * (sp * sv).rolling(60, min_periods=60).mean()).replace([np.inf, -np.inf], np.nan)


# === LARGE-PRICE-RANGE / LOW-VOL DAY (no-confirm) ==========================


def f28pd_f28_price_volume_divergence_wide_range_lowvol_30d_base_v105_signal(high, low, closeadj, volume):
    """Mean over 30d of indicator{ (high-low)/close > 1.5*30d-mean AND volume < 30d-median(volume) }.
    Wide-range, low-volume days = divergence signal."""
    rng = (high - low) / closeadj
    wide = (rng > 1.5 * rng.rolling(30, min_periods=30).mean()).astype(float)
    low_vol = (volume < volume.rolling(30, min_periods=30).median()).astype(float)
    bit = (wide * low_vol).where(~rng.rolling(30, min_periods=30).mean().isna() & ~volume.rolling(30, min_periods=30).median().isna())
    return bit.rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


# === DIVERGENCE INTENSITY (mean abs sign diff) =============================


def f28pd_f28_price_volume_divergence_abs_signdiff_mean_75d_base_v106_signal(closeadj, volume):
    """75d mean of |sign(close.diff)-sign(vol.diff)|. Range [0,2]."""
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    return (sp - sv).abs().rolling(75, min_periods=75).mean().replace([np.inf, -np.inf], np.nan)


# === MEDIAN VOL OF UP-DAYS / MEDIAN VOL OF DOWN-DAYS =======================


def f28pd_f28_price_volume_divergence_med_updown_vol_logratio_55d_base_v107_signal(closeadj, volume):
    """log(median_vol_on_up_55d / median_vol_on_down_55d). Robust update of v028."""
    is_up = (closeadj.diff(1) > 0)
    is_dn = (closeadj.diff(1) < 0)
    vol_up = volume.where(is_up)
    vol_dn = volume.where(is_dn)
    mu = vol_up.rolling(55, min_periods=10).median()
    md = vol_dn.rolling(55, min_periods=10).median()
    return np.log(mu / md.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === RANGE-EXPANSION on counter-vol day ====================================


def f28pd_f28_price_volume_divergence_range_low_vol_zscore_55d_base_v108_signal(high, low, closeadj, volume):
    """z((high-low)/close, 55) on days with z(vol,55) < 0. Wide-range LOW-volume days."""
    rng = (high - low) / closeadj
    zr = (rng - rng.rolling(55, min_periods=55).mean()) / rng.rolling(55, min_periods=55).std().replace(0.0, np.nan)
    zv = (volume - volume.rolling(55, min_periods=55).mean()) / volume.rolling(55, min_periods=55).std().replace(0.0, np.nan)
    lowvol = (zv < 0.0).astype(float).where(~zv.isna())
    return (lowvol * zr).replace([np.inf, -np.inf], np.nan)


# === MFI-LIKE divergence (without using full MFI) ==========================


def f28pd_f28_price_volume_divergence_money_flow_diff_45d_base_v109_signal(high, low, closeadj, volume):
    """log(sum(typprice*vol on up,45) / sum(typprice*vol on down,45)) - log(close/close.shift(45)).
    A money-flow-direction vs price-direction divergence."""
    typ = (high + low + closeadj) / 3.0
    up = (typ.diff(1) > 0).astype(float)
    dn = (typ.diff(1) < 0).astype(float)
    mf_up = (up * typ * volume).rolling(45, min_periods=45).sum()
    mf_dn = (dn * typ * volume).rolling(45, min_periods=45).sum()
    return (np.log(mf_up / mf_dn.replace(0.0, np.nan)) - np.log(closeadj / closeadj.shift(45))).replace([np.inf, -np.inf], np.nan)


# === DIVERGENCE OF VOL OF VOL (volatility of volume) =======================


def f28pd_f28_price_volume_divergence_vol_of_vol_diff_100d_base_v110_signal(closeadj, volume):
    """100d std of std(price.pct,20) MINUS std of std(vol.pct,20). Vol-regime gap."""
    sp = closeadj.pct_change().rolling(20, min_periods=20).std()
    sv = volume.pct_change().rolling(20, min_periods=20).std()
    return (sp.rolling(100, min_periods=100).std() - sv.rolling(100, min_periods=100).std()).replace([np.inf, -np.inf], np.nan)


# === TAIL EVENTS: BIG PRICE NO BIG VOL =====================================


def f28pd_f28_price_volume_divergence_big_price_no_big_vol_60d_base_v111_signal(closeadj, volume):
    """Fraction of last 60d on which |price.ret| > 95th-percentile-of-60d but vol < 50th-percentile-of-60d."""
    rp = closeadj.pct_change().abs()
    p95 = rp.rolling(60, min_periods=60).quantile(0.95)
    p50v = volume.rolling(60, min_periods=60).quantile(0.50)
    big_no = ((rp > p95).astype(float) * (volume < p50v).astype(float)).where(~p95.isna() & ~p50v.isna())
    return big_no.rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


# === BIG VOL NO BIG PRICE ==================================================


def f28pd_f28_price_volume_divergence_big_vol_no_big_price_80d_base_v112_signal(closeadj, volume):
    """Fraction of last 80d on which vol > 95th-percentile-of-80d but |price.ret| < 50th-percentile-of-80d."""
    rp = closeadj.pct_change().abs()
    p95v = volume.rolling(80, min_periods=80).quantile(0.95)
    p50r = rp.rolling(80, min_periods=80).quantile(0.50)
    big_no = ((volume > p95v).astype(float) * (rp < p50r).astype(float)).where(~p95v.isna() & ~p50r.isna())
    return big_no.rolling(80, min_periods=80).mean().replace([np.inf, -np.inf], np.nan)


# === SHORT-WINDOW BOUNDED DIVERGENCE =======================================


def f28pd_f28_price_volume_divergence_tanh_disagree_15d_base_v113_signal(close, volume):
    """tanh of (sgn(close.diff(15)) - sgn(volume.diff(15))) * 0.5. Bounded sign-diff."""
    return np.tanh(0.5 * (np.sign(close.diff(15)) - np.sign(volume.diff(15)))).replace([np.inf, -np.inf], np.nan)


# === CORR STD - CORR LEVEL ================================================


def f28pd_f28_price_volume_divergence_corr_std_minus_level_50d_base_v114_signal(closeadj, volume):
    """50d std of 15d-corr MINUS current 50d-mean of 15d-corr. Divergence regime indicator."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    c15 = rp.rolling(15, min_periods=15).corr(rv)
    return (c15.rolling(50, min_periods=50).std() - c15.rolling(50, min_periods=50).mean()).replace([np.inf, -np.inf], np.nan)


# === LOG SUM-VOL ON UP DAYS - LOG SUM-VOL ON DOWN DAYS, 20d ================


def f28pd_f28_price_volume_divergence_log_sumvol_up_down_diff_20d_base_v115_signal(close, volume):
    """log(sum_vol_up_20d) - log(sum_vol_down_20d). Different normalization than v028."""
    up = (close.diff(1) > 0).astype(float)
    dn = (close.diff(1) < 0).astype(float)
    su = (up * volume).rolling(20, min_periods=20).sum()
    sd = (dn * volume).rolling(20, min_periods=20).sum()
    return (np.log(su.replace(0.0, np.nan)) - np.log(sd.replace(0.0, np.nan))).replace([np.inf, -np.inf], np.nan)


# === DIVERGENCE Z-SCORE (return-z VS volume-z) =============================


def f28pd_f28_price_volume_divergence_z_close_z_vol_prod_55d_base_v116_signal(closeadj, volume):
    """-1 * z(close,55) * z(volume,55). High when one is up, other is down."""
    zc = (closeadj - closeadj.rolling(55, min_periods=55).mean()) / closeadj.rolling(55, min_periods=55).std().replace(0.0, np.nan)
    zv = (volume - volume.rolling(55, min_periods=55).mean()) / volume.rolling(55, min_periods=55).std().replace(0.0, np.nan)
    return (-1.0 * zc * zv).replace([np.inf, -np.inf], np.nan)


# === SPEARMAN OF DIFFS =====================================================


def f28pd_f28_price_volume_divergence_spearman_diff_45d_base_v117_signal(closeadj, volume):
    """45d Spearman of (close.diff(1)) vs (volume.diff(1)). Differential rank correlation."""
    rp = closeadj.diff().rolling(45, min_periods=45).rank(pct=False)
    rv = volume.diff().rolling(45, min_periods=45).rank(pct=False)
    return rp.rolling(45, min_periods=45).corr(rv).replace([np.inf, -np.inf], np.nan)


# === LONG-LAG CORR DIFF (asymmetric lead/lag profile) ======================


def f28pd_f28_price_volume_divergence_long_lead_lag_90d_base_v118_signal(closeadj, volume):
    """corr(price.pct, vol.pct.shift(10)) - corr(price.pct, vol.pct.shift(-10)) over 90d."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    cl = rp.rolling(90, min_periods=90).corr(rv.shift(10))
    cn = rp.rolling(90, min_periods=90).corr(rv.shift(-10))
    return (cl - cn).replace([np.inf, -np.inf], np.nan)


# === DIVERGENCE - ROLLING ENTROPY OF DIRECTION ============================


def f28pd_f28_price_volume_divergence_dir_disagree_entropy_45d_base_v119_signal(closeadj, volume):
    """Entropy of |sign(price.diff) - sign(volume.diff)| values (in {0,1,2}) over 45d."""
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    val = (sp - sv).abs().where(~sp.isna() & ~sv.isna())
    def _ent(x):
        if len(x) == 0 or not np.all(np.isfinite(x)):
            return np.nan
        u, c = np.unique(x, return_counts=True)
        p = c / c.sum()
        p = p[p > 0]
        return float(-np.sum(p * np.log2(p)))
    return val.rolling(45, min_periods=45).apply(_ent, raw=True).replace([np.inf, -np.inf], np.nan)


# === COVARIANCE-NORMALIZED DIVERGENCE ======================================


def f28pd_f28_price_volume_divergence_cov_normalized_30d_base_v120_signal(close, volume):
    """-cov(close.pct, volume.pct, 30) / (std_price*mean_volume). Scaled negative covariance."""
    rp = close.pct_change()
    rv = volume.pct_change()
    c = rp.rolling(30, min_periods=30).cov(rv)
    sp = rp.rolling(30, min_periods=30).std()
    mv = volume.rolling(30, min_periods=30).mean()
    return (-1.0 * c / (sp * mv).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ROLLING-MIN-OF-CORR (divergence severity) =============================


def f28pd_f28_price_volume_divergence_min_corr_30in120d_base_v121_signal(closeadj, volume):
    """Min of 30d corr(price.pct, vol.pct) seen in last 120d. Severity of past divergence."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    c30 = rp.rolling(30, min_periods=30).corr(rv)
    return c30.rolling(120, min_periods=120).min().replace([np.inf, -np.inf], np.nan)


# === ABSOLUTE-CORR (low = no relationship at all) =========================


def f28pd_f28_price_volume_divergence_abs_corr_neg_50d_base_v122_signal(closeadj, volume):
    """-|corr(price.pct, vol.pct, 50)|. Negative-absolute: low when uncorrelated (no link)."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    c = rp.rolling(50, min_periods=50).corr(rv)
    return (-1.0 * c.abs()).replace([np.inf, -np.inf], np.nan)


# === LONG OBV-SLOPE-PRICE-SLOPE (uses OBV) =================================


def f28pd_f28_price_volume_divergence_obv_price_slope_diff_100d_base_v123_signal(closeadj, volume):
    """slope(OBV,100)/std(OBV,100) - slope(closeadj,100)/std(closeadj,100). Standardized."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    so = obv.rolling(100, min_periods=100).apply(_slope_raw, raw=True) / obv.rolling(100, min_periods=100).std().replace(0.0, np.nan)
    sc = closeadj.rolling(100, min_periods=100).apply(_slope_raw, raw=True) / closeadj.rolling(100, min_periods=100).std().replace(0.0, np.nan)
    return (so - sc).replace([np.inf, -np.inf], np.nan)


# === COMPLEMENT-OF-CONFIRMATION (regime persistence) ======================


def f28pd_f28_price_volume_divergence_disagree_persistence_140d_base_v124_signal(closeadj, volume):
    """140d sum of (1 - same-sign-bit). Long-window count of disagreement days."""
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    same = (sp == sv).astype(float).where(~sp.isna() & ~sv.isna())
    return (1.0 - same).rolling(140, min_periods=140).sum().replace([np.inf, -np.inf], np.nan)


# === HURST-RS OF DISAGREEMENT BIT ==========================================


def f28pd_f28_price_volume_divergence_hurst_xor_60d_base_v125_signal(closeadj, volume):
    """Hurst R/S of disagreement-bit time series over 60d (>0.5 = trending divergence, <0.5 mean-reverting)."""
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    bit = (sp != sv).astype(float).where(~sp.isna() & ~sv.isna())
    def _hurst(x):
        n = len(x)
        if n < 16 or not np.all(np.isfinite(x)):
            return np.nan
        y = np.asarray(x, dtype=float)
        m = y.mean(); d = y - m; z = np.cumsum(d)
        R = z.max() - z.min(); S = y.std(ddof=0)
        if S == 0.0 or R / S <= 0.0:
            return np.nan
        return float(np.log(R / S) / np.log(n))
    return bit.rolling(60, min_periods=60).apply(_hurst, raw=True).replace([np.inf, -np.inf], np.nan)


# === DIVERGENCE - MOMENTUM ALIGN ==========================================


def f28pd_f28_price_volume_divergence_mom_align_sign_22d_base_v126_signal(close, volume):
    """sign(close.diff(22)) * sign(volume.diff(22)) * -1. +1 = diverging at 22d momentum scale."""
    return (-1.0 * np.sign(close.diff(22)) * np.sign(volume.diff(22))).replace([np.inf, -np.inf], np.nan)


# === MAGNITUDE OF NEGATIVE CORR ============================================


def f28pd_f28_price_volume_divergence_neg_corr_mag_40d_base_v127_signal(closeadj, volume):
    """min(0, corr(price.pct, vol.pct, 40)). Zero if positive corr, else negative magnitude."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    c = rp.rolling(40, min_periods=40).corr(rv)
    return c.clip(upper=0.0).replace([np.inf, -np.inf], np.nan)


# === DAYS-SINCE BIG UNCONFIRMED HIGH =======================================


def f28pd_f28_price_volume_divergence_dsince_unconf_high_120d_base_v128_signal(closeadj, volume):
    """Bars since last 60d-high with vol < 60d-median(vol). Longer-window pure unconfirmed."""
    cmax = closeadj.rolling(60, min_periods=60).max()
    vmed = volume.rolling(60, min_periods=60).median()
    ev = ((closeadj >= cmax).astype(float) * (volume < vmed).astype(float)).where(~cmax.isna() & ~vmed.isna())
    return ev.rolling(120, min_periods=120).apply(_streak_idx, raw=True).replace([np.inf, -np.inf], np.nan)


# === RATIO OF BEAR EVENTS TO BULL EVENTS ===================================


def f28pd_f28_price_volume_divergence_bear_bull_ratio_80d_base_v129_signal(closeadj, volume):
    """log((1+bear_count_80d) / (1+bull_count_80d)). Positive = bear-div dominant."""
    bear = ((closeadj.diff(1) > 0) & (volume.diff(1) < 0)).astype(float).where(~closeadj.diff(1).isna() & ~volume.diff(1).isna())
    bull = ((closeadj.diff(1) < 0) & (volume.diff(1) > 0)).astype(float).where(~closeadj.diff(1).isna() & ~volume.diff(1).isna())
    bc = bear.rolling(80, min_periods=80).sum()
    blc = bull.rolling(80, min_periods=80).sum()
    return np.log((1.0 + bc) / (1.0 + blc)).replace([np.inf, -np.inf], np.nan)


# === DISTRIBUTIONAL OVERLAP (quantile-based) ===============================


def f28pd_f28_price_volume_divergence_q75_minus_q25_logdiff_70d_base_v130_signal(closeadj, volume):
    """IQR(close, 70) / close - IQR(volume, 70) / mean(volume, 70)."""
    pq75 = closeadj.rolling(70, min_periods=70).quantile(0.75)
    pq25 = closeadj.rolling(70, min_periods=70).quantile(0.25)
    vq75 = volume.rolling(70, min_periods=70).quantile(0.75)
    vq25 = volume.rolling(70, min_periods=70).quantile(0.25)
    return ((pq75 - pq25) / closeadj - (vq75 - vq25) / volume.rolling(70, min_periods=70).mean().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === MIN-Z DIFF (extreme z difference) =====================================


def f28pd_f28_price_volume_divergence_zclose_zvol_diff_signed_35d_base_v131_signal(close, volume):
    """z(close,35) - z(volume,35). Just standardized level difference; signed."""
    zc = (close - close.rolling(35, min_periods=35).mean()) / close.rolling(35, min_periods=35).std().replace(0.0, np.nan)
    zv = (volume - volume.rolling(35, min_periods=35).mean()) / volume.rolling(35, min_periods=35).std().replace(0.0, np.nan)
    return (zc - zv).replace([np.inf, -np.inf], np.nan)


# === Z-SCORE OF NEG-CORR ===================================================


def f28pd_f28_price_volume_divergence_neg_corr_zscore_125d_base_v132_signal(closeadj, volume):
    """z-score of -corr(price.pct, vol.pct, 25) using its 125d distribution. Standardized recent divergence."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    nc = -rp.rolling(25, min_periods=25).corr(rv)
    return ((nc - nc.rolling(125, min_periods=125).mean()) / nc.rolling(125, min_periods=125).std().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === VWAP-CROSS DIVERGENCE =================================================


def f28pd_f28_price_volume_divergence_vwap_cross_freq_120d_base_v133_signal(closeadj, volume):
    """Fraction of last 120d on which close crossed above or below 30d-VWAP. High cross-rate = price-vol disagreement."""
    n = 30
    vwap = (closeadj * volume).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    s = np.sign(closeadj - vwap)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(120, min_periods=120).mean().replace([np.inf, -np.inf], np.nan)


# === DIVERGENCE STREAK INTENSITY ===========================================


def f28pd_f28_price_volume_divergence_max_streak_xor_140d_base_v134_signal(closeadj, volume):
    """Max XOR-disagreement streak observed in trailing 140d (Tracks longest divergence run)."""
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    bit = (sp != sv).astype(float).where(~sp.isna() & ~sv.isna())
    def _max_streak(x):
        m = 0; c = 0
        for v in x:
            if v > 0.5:
                c += 1
                if c > m: m = c
            else:
                c = 0
        return float(m)
    return bit.rolling(140, min_periods=140).apply(_max_streak, raw=True).replace([np.inf, -np.inf], np.nan)


# === DIVERGENCE - VOLUME-ADJUSTED PRICE MOM ================================


def f28pd_f28_price_volume_divergence_pricerise_volfall_pctrank_100d_base_v135_signal(closeadj, volume):
    """Percentile rank (over 100d) of (close.pct_change(22)) - (volume.pct_change(22))."""
    return (closeadj.pct_change(22) - volume.pct_change(22)).rolling(100, min_periods=100).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === OBV ACCELERATION DIFF (light OBV) =====================================


def f28pd_f28_price_volume_divergence_obv_accel_minus_price_accel_60d_base_v136_signal(closeadj, volume):
    """(OBV.diff(21) - OBV.diff(21).shift(21)) / OBV.std(60) - same for closeadj. Acceleration gap."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    oa = (obv.diff(21) - obv.diff(21).shift(21)) / obv.rolling(60, min_periods=60).std().replace(0.0, np.nan)
    ca = (closeadj.diff(21) - closeadj.diff(21).shift(21)) / closeadj.rolling(60, min_periods=60).std().replace(0.0, np.nan)
    return (oa - ca).replace([np.inf, -np.inf], np.nan)


# === DOWN-VOL ASYMMETRY INDEX (uses high/low/close) =======================


def f28pd_f28_price_volume_divergence_down_close_high_vol_50d_base_v137_signal(high, low, closeadj, volume):
    """Mean over 50d of (vol z-score) * indicator{close < midpoint(high,low)}. Down-bar high-volume avg."""
    mid = 0.5 * (high + low)
    dn_bar = (closeadj < mid).astype(float)
    zv = (volume - volume.rolling(50, min_periods=50).mean()) / volume.rolling(50, min_periods=50).std().replace(0.0, np.nan)
    return (dn_bar * zv).rolling(50, min_periods=50).mean().replace([np.inf, -np.inf], np.nan)


# === SHORT-TERM DIVERGENCE MOMENTUM =======================================


def f28pd_f28_price_volume_divergence_xor_freq_4d_base_v138_signal(close, volume):
    """Mean XOR-disagreement bit over 4 days (very short-window). Useful for short-term signals."""
    sp = np.sign(close.diff(1))
    sv = np.sign(volume.diff(1))
    bit = (sp != sv).astype(float).where(~sp.isna() & ~sv.isna())
    return bit.rolling(4, min_periods=4).mean().replace([np.inf, -np.inf], np.nan)


# === LONG-WINDOW CORR DEVIATION FROM ZERO ==================================


def f28pd_f28_price_volume_divergence_corr_dev_from_zero_252d_base_v139_signal(closeadj, volume):
    """|corr(price.pct, vol.pct, 252)|. Long-window |corr|. Low = persistent independence/divergence."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    return rp.rolling(252, min_periods=252).corr(rv).abs().replace([np.inf, -np.inf], np.nan)


# === ARCTAN OF Z(LOG-VOL-RES) ==============================================


def f28pd_f28_price_volume_divergence_arctan_logvol_res_75d_base_v140_signal(closeadj, volume):
    """arctan of residual (log-vol regressed on log-price) over 75d, normalized by 75d-std of residual.
    Bounded transform of regression divergence."""
    n = 75
    lp = np.log(closeadj)
    lv = np.log(volume.replace(0.0, np.nan))
    mx = lp.rolling(n, min_periods=n).mean()
    my = lv.rolling(n, min_periods=n).mean()
    vx = lp.rolling(n, min_periods=n).var()
    cxy = lp.rolling(n, min_periods=n).cov(lv)
    b = cxy / vx.replace(0.0, np.nan)
    a = my - b * mx
    res = lv - (a + b * lp)
    sd = res.rolling(n, min_periods=n).std()
    return np.arctan(res / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === DIVERGENCE-SHARPE (mean / std) ========================================


def f28pd_f28_price_volume_divergence_signed_div_sharpe_85d_base_v141_signal(closeadj, volume):
    """mean(z_price - z_vol, 85) / std(z_price - z_vol, 85). Sharpe-style of standardized gap."""
    zp = (closeadj - closeadj.rolling(85, min_periods=85).mean()) / closeadj.rolling(85, min_periods=85).std().replace(0.0, np.nan)
    zv = (volume - volume.rolling(85, min_periods=85).mean()) / volume.rolling(85, min_periods=85).std().replace(0.0, np.nan)
    gap = zp - zv
    return (gap.rolling(85, min_periods=85).mean() / gap.rolling(85, min_periods=85).std().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === SHARP RANGE VS VOLUME ON RECENT WINDOW ================================


def f28pd_f28_price_volume_divergence_atr_vol_logratio_25d_base_v142_signal(high, low, close, volume):
    """log(ATR-like(25) / ATR-mean) - log(volume / vol-mean). Short ATR-vol gap."""
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(14, min_periods=14).mean()
    return (np.log(atr / atr.rolling(25, min_periods=25).mean()) - np.log(volume / volume.rolling(25, min_periods=25).mean())).replace([np.inf, -np.inf], np.nan)


# === PRICE-DIRECTION TRANSITION WEIGHTED BY VOL ============================


def f28pd_f28_price_volume_divergence_vol_weighted_dir_change_45d_base_v143_signal(closeadj, volume):
    """45d mean of vol * indicator{sign(price.diff)!=sign(prev price.diff)} normalized by 45d mean vol.
    Vol-weighted price reversal rate (price reversing with above-avg vol)."""
    s = np.sign(closeadj.diff(1))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    weighted = (flip * volume).rolling(45, min_periods=45).mean()
    mv = volume.rolling(45, min_periods=45).mean()
    return (weighted / mv.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === SCATTER ANGLE (atan2 of slopes) =======================================


def f28pd_f28_price_volume_divergence_angle_atan2_50d_base_v144_signal(closeadj, volume):
    """atan2(slope_vol_50, slope_price_50). Angle in (-pi, pi]. Bounded."""
    sp = np.log(closeadj).rolling(50, min_periods=50).apply(_slope_raw, raw=True)
    sv = np.log(volume.replace(0.0, np.nan)).rolling(50, min_periods=50).apply(_slope_raw, raw=True)
    out = pd.Series(np.arctan2(sv.values, sp.values), index=closeadj.index)
    return out.where(~sp.isna() & ~sv.isna()).replace([np.inf, -np.inf], np.nan)


# === DETREND COVARIANCE OF Z SCORES ========================================


def f28pd_f28_price_volume_divergence_zret_zvolret_cov_60d_base_v145_signal(closeadj, volume):
    """60d cov(z(price.pct,60), z(vol.pct,60)). Negative=divergence regime."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    zp = (rp - rp.rolling(60, min_periods=60).mean()) / rp.rolling(60, min_periods=60).std().replace(0.0, np.nan)
    zv = (rv - rv.rolling(60, min_periods=60).mean()) / rv.rolling(60, min_periods=60).std().replace(0.0, np.nan)
    return zp.rolling(60, min_periods=60).cov(zv).replace([np.inf, -np.inf], np.nan)


# === RANK PEAK PRICE - RANK PEAK VOL =======================================


def f28pd_f28_price_volume_divergence_rank_at_peak_diff_90d_base_v146_signal(closeadj, volume):
    """percentile-rank(close) at 90d high minus percentile-rank(volume) at 90d high.
    Difference of ranks of latest price-peak day vs volume-peak day."""
    pr_at = closeadj.rolling(90, min_periods=90).apply(lambda x: float(np.argmax(x) + 1) / float(len(x)), raw=True)
    vr_at = volume.rolling(90, min_periods=90).apply(lambda x: float(np.argmax(x) + 1) / float(len(x)), raw=True)
    return (pr_at - vr_at).replace([np.inf, -np.inf], np.nan)


# === DIVERGENCE FREQUENCY EWM ==============================================


def f28pd_f28_price_volume_divergence_xor_ewm_long_150d_base_v147_signal(closeadj, volume):
    """EWM(span=150) of disagreement-bit. Very-smoothed long-baseline disagreement."""
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    bit = (sp != sv).astype(float).where(~sp.isna() & ~sv.isna())
    return bit.ewm(span=150, adjust=False, min_periods=150).mean().replace([np.inf, -np.inf], np.nan)


# === SPEARMAN WITH LAGGED VOLUME ===========================================


def f28pd_f28_price_volume_divergence_spearman_lag_60d_base_v148_signal(closeadj, volume):
    """60d Spearman of (close) vs (volume.shift(5)). Lagged-rank divergence."""
    rc = closeadj.rolling(60, min_periods=60).rank(pct=False)
    rv = volume.shift(5).rolling(60, min_periods=60).rank(pct=False)
    return rc.rolling(60, min_periods=60).corr(rv).replace([np.inf, -np.inf], np.nan)


# === BIG-PRICE-SMALL-VOL ENERGY ============================================


def f28pd_f28_price_volume_divergence_energy_price_minus_vol_45d_base_v149_signal(closeadj, volume):
    """log(sum((price.pct)^2 * 1, 45)) - log(sum((vol.pct)^2 * 1, 45)). Energy difference."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    ep = (rp ** 2).rolling(45, min_periods=45).sum()
    ev = (rv ** 2).rolling(45, min_periods=45).sum()
    return (np.log(ep.replace(0.0, np.nan)) - np.log(ev.replace(0.0, np.nan))).replace([np.inf, -np.inf], np.nan)


# === BOUNDED COMPOSITE DIVERGENCE ==========================================


def f28pd_f28_price_volume_divergence_composite_tanh_70d_base_v150_signal(closeadj, volume):
    """tanh of (negative correlation 70d  +  sign-disagreement-mean 70d). Composite bounded divergence."""
    rp = closeadj.pct_change()
    rv = volume.pct_change()
    c = rp.rolling(70, min_periods=70).corr(rv)
    sp = np.sign(closeadj.diff(1))
    sv = np.sign(volume.diff(1))
    bit = (sp != sv).astype(float).where(~sp.isna() & ~sv.isna())
    f = bit.rolling(70, min_periods=70).mean() - 0.5
    return np.tanh((-c) + f).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f28_price_volume_divergence_base_076_150_REGISTRY = {
    "f28pd_f28_price_volume_divergence_xor_count_180d_base_v076_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_xor_count_180d_base_v076_signal},
    "f28pd_f28_price_volume_divergence_xor_ema_freq_45d_base_v077_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_xor_ema_freq_45d_base_v077_signal},
    "f28pd_f28_price_volume_divergence_median_diff_log_50d_base_v078_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_median_diff_log_50d_base_v078_signal},
    "f28pd_f28_price_volume_divergence_median_rank_diff_80d_base_v079_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_median_rank_diff_80d_base_v079_signal},
    "f28pd_f28_price_volume_divergence_concord_frac_35d_base_v080_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_concord_frac_35d_base_v080_signal},
    "f28pd_f28_price_volume_divergence_ewm_corr_45d_base_v081_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_ewm_corr_45d_base_v081_signal},
    "f28pd_f28_price_volume_divergence_ewm_corr_neg_115d_base_v082_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_ewm_corr_neg_115d_base_v082_signal},
    "f28pd_f28_price_volume_divergence_spearman_200d_base_v083_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_spearman_200d_base_v083_signal},
    "f28pd_f28_price_volume_divergence_beta_logvolume_logreturn_75d_base_v084_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_beta_logvolume_logreturn_75d_base_v084_signal},
    "f28pd_f28_price_volume_divergence_beta_dev_from_baseline_200d_base_v085_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_beta_dev_from_baseline_200d_base_v085_signal},
    "f28pd_f28_price_volume_divergence_high_unconf_long_120d_base_v086_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_high_unconf_long_120d_base_v086_signal},
    "f28pd_f28_price_volume_divergence_low_unconf_long_120d_base_v087_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_low_unconf_long_120d_base_v087_signal},
    "f28pd_f28_price_volume_divergence_sign_entropy_60d_base_v088_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_sign_entropy_60d_base_v088_signal},
    "f28pd_f28_price_volume_divergence_ewm_log_ratio_short_long_base_v089_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_ewm_log_ratio_short_long_base_v089_signal},
    "f28pd_f28_price_volume_divergence_ewm_log_ratio_mid_long_base_v090_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_ewm_log_ratio_mid_long_base_v090_signal},
    "f28pd_f28_price_volume_divergence_mad_div_45d_base_v091_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_mad_div_45d_base_v091_signal},
    "f28pd_f28_price_volume_divergence_xor_autocorr_lag1_80d_base_v092_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_xor_autocorr_lag1_80d_base_v092_signal},
    "f28pd_f28_price_volume_divergence_updown_vol_diff_zscore_45d_base_v093_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_updown_vol_diff_zscore_45d_base_v093_signal},
    "f28pd_f28_price_volume_divergence_vwret_unwret_diff_30d_base_v094_signal": {"inputs": ["close", "volume"], "func": f28pd_f28_price_volume_divergence_vwret_unwret_diff_30d_base_v094_signal},
    "f28pd_f28_price_volume_divergence_vwret_unwret_diff_120d_base_v095_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_vwret_unwret_diff_120d_base_v095_signal},
    "f28pd_f28_price_volume_divergence_sma_diff_sign_30d_base_v096_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_sma_diff_sign_30d_base_v096_signal},
    "f28pd_f28_price_volume_divergence_xor_freq_std_60d_base_v097_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_xor_freq_std_60d_base_v097_signal},
    "f28pd_f28_price_volume_divergence_rank_ret_rank_volret_diff_50d_base_v098_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_rank_ret_rank_volret_diff_50d_base_v098_signal},
    "f28pd_f28_price_volume_divergence_unconf_high_rate_252d_base_v099_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_unconf_high_rate_252d_base_v099_signal},
    "f28pd_f28_price_volume_divergence_unconf_low_rate_252d_base_v100_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_unconf_low_rate_252d_base_v100_signal},
    "f28pd_f28_price_volume_divergence_big_move_xor_60d_base_v101_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_big_move_xor_60d_base_v101_signal},
    "f28pd_f28_price_volume_divergence_log_range_diff_40d_base_v102_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_log_range_diff_40d_base_v102_signal},
    "f28pd_f28_price_volume_divergence_z_peak_asym_70d_base_v103_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_z_peak_asym_70d_base_v103_signal},
    "f28pd_f28_price_volume_divergence_cum_neg_prod_60d_base_v104_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_cum_neg_prod_60d_base_v104_signal},
    "f28pd_f28_price_volume_divergence_wide_range_lowvol_30d_base_v105_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_wide_range_lowvol_30d_base_v105_signal},
    "f28pd_f28_price_volume_divergence_abs_signdiff_mean_75d_base_v106_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_abs_signdiff_mean_75d_base_v106_signal},
    "f28pd_f28_price_volume_divergence_med_updown_vol_logratio_55d_base_v107_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_med_updown_vol_logratio_55d_base_v107_signal},
    "f28pd_f28_price_volume_divergence_range_low_vol_zscore_55d_base_v108_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_range_low_vol_zscore_55d_base_v108_signal},
    "f28pd_f28_price_volume_divergence_money_flow_diff_45d_base_v109_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_money_flow_diff_45d_base_v109_signal},
    "f28pd_f28_price_volume_divergence_vol_of_vol_diff_100d_base_v110_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_vol_of_vol_diff_100d_base_v110_signal},
    "f28pd_f28_price_volume_divergence_big_price_no_big_vol_60d_base_v111_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_big_price_no_big_vol_60d_base_v111_signal},
    "f28pd_f28_price_volume_divergence_big_vol_no_big_price_80d_base_v112_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_big_vol_no_big_price_80d_base_v112_signal},
    "f28pd_f28_price_volume_divergence_tanh_disagree_15d_base_v113_signal": {"inputs": ["close", "volume"], "func": f28pd_f28_price_volume_divergence_tanh_disagree_15d_base_v113_signal},
    "f28pd_f28_price_volume_divergence_corr_std_minus_level_50d_base_v114_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_corr_std_minus_level_50d_base_v114_signal},
    "f28pd_f28_price_volume_divergence_log_sumvol_up_down_diff_20d_base_v115_signal": {"inputs": ["close", "volume"], "func": f28pd_f28_price_volume_divergence_log_sumvol_up_down_diff_20d_base_v115_signal},
    "f28pd_f28_price_volume_divergence_z_close_z_vol_prod_55d_base_v116_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_z_close_z_vol_prod_55d_base_v116_signal},
    "f28pd_f28_price_volume_divergence_spearman_diff_45d_base_v117_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_spearman_diff_45d_base_v117_signal},
    "f28pd_f28_price_volume_divergence_long_lead_lag_90d_base_v118_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_long_lead_lag_90d_base_v118_signal},
    "f28pd_f28_price_volume_divergence_dir_disagree_entropy_45d_base_v119_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_dir_disagree_entropy_45d_base_v119_signal},
    "f28pd_f28_price_volume_divergence_cov_normalized_30d_base_v120_signal": {"inputs": ["close", "volume"], "func": f28pd_f28_price_volume_divergence_cov_normalized_30d_base_v120_signal},
    "f28pd_f28_price_volume_divergence_min_corr_30in120d_base_v121_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_min_corr_30in120d_base_v121_signal},
    "f28pd_f28_price_volume_divergence_abs_corr_neg_50d_base_v122_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_abs_corr_neg_50d_base_v122_signal},
    "f28pd_f28_price_volume_divergence_obv_price_slope_diff_100d_base_v123_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_obv_price_slope_diff_100d_base_v123_signal},
    "f28pd_f28_price_volume_divergence_disagree_persistence_140d_base_v124_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_disagree_persistence_140d_base_v124_signal},
    "f28pd_f28_price_volume_divergence_hurst_xor_60d_base_v125_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_hurst_xor_60d_base_v125_signal},
    "f28pd_f28_price_volume_divergence_mom_align_sign_22d_base_v126_signal": {"inputs": ["close", "volume"], "func": f28pd_f28_price_volume_divergence_mom_align_sign_22d_base_v126_signal},
    "f28pd_f28_price_volume_divergence_neg_corr_mag_40d_base_v127_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_neg_corr_mag_40d_base_v127_signal},
    "f28pd_f28_price_volume_divergence_dsince_unconf_high_120d_base_v128_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_dsince_unconf_high_120d_base_v128_signal},
    "f28pd_f28_price_volume_divergence_bear_bull_ratio_80d_base_v129_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_bear_bull_ratio_80d_base_v129_signal},
    "f28pd_f28_price_volume_divergence_q75_minus_q25_logdiff_70d_base_v130_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_q75_minus_q25_logdiff_70d_base_v130_signal},
    "f28pd_f28_price_volume_divergence_zclose_zvol_diff_signed_35d_base_v131_signal": {"inputs": ["close", "volume"], "func": f28pd_f28_price_volume_divergence_zclose_zvol_diff_signed_35d_base_v131_signal},
    "f28pd_f28_price_volume_divergence_neg_corr_zscore_125d_base_v132_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_neg_corr_zscore_125d_base_v132_signal},
    "f28pd_f28_price_volume_divergence_vwap_cross_freq_120d_base_v133_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_vwap_cross_freq_120d_base_v133_signal},
    "f28pd_f28_price_volume_divergence_max_streak_xor_140d_base_v134_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_max_streak_xor_140d_base_v134_signal},
    "f28pd_f28_price_volume_divergence_pricerise_volfall_pctrank_100d_base_v135_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_pricerise_volfall_pctrank_100d_base_v135_signal},
    "f28pd_f28_price_volume_divergence_obv_accel_minus_price_accel_60d_base_v136_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_obv_accel_minus_price_accel_60d_base_v136_signal},
    "f28pd_f28_price_volume_divergence_down_close_high_vol_50d_base_v137_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_down_close_high_vol_50d_base_v137_signal},
    "f28pd_f28_price_volume_divergence_xor_freq_4d_base_v138_signal": {"inputs": ["close", "volume"], "func": f28pd_f28_price_volume_divergence_xor_freq_4d_base_v138_signal},
    "f28pd_f28_price_volume_divergence_corr_dev_from_zero_252d_base_v139_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_corr_dev_from_zero_252d_base_v139_signal},
    "f28pd_f28_price_volume_divergence_arctan_logvol_res_75d_base_v140_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_arctan_logvol_res_75d_base_v140_signal},
    "f28pd_f28_price_volume_divergence_signed_div_sharpe_85d_base_v141_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_signed_div_sharpe_85d_base_v141_signal},
    "f28pd_f28_price_volume_divergence_atr_vol_logratio_25d_base_v142_signal": {"inputs": ["high", "low", "close", "volume"], "func": f28pd_f28_price_volume_divergence_atr_vol_logratio_25d_base_v142_signal},
    "f28pd_f28_price_volume_divergence_vol_weighted_dir_change_45d_base_v143_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_vol_weighted_dir_change_45d_base_v143_signal},
    "f28pd_f28_price_volume_divergence_angle_atan2_50d_base_v144_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_angle_atan2_50d_base_v144_signal},
    "f28pd_f28_price_volume_divergence_zret_zvolret_cov_60d_base_v145_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_zret_zvolret_cov_60d_base_v145_signal},
    "f28pd_f28_price_volume_divergence_rank_at_peak_diff_90d_base_v146_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_rank_at_peak_diff_90d_base_v146_signal},
    "f28pd_f28_price_volume_divergence_xor_ewm_long_150d_base_v147_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_xor_ewm_long_150d_base_v147_signal},
    "f28pd_f28_price_volume_divergence_spearman_lag_60d_base_v148_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_spearman_lag_60d_base_v148_signal},
    "f28pd_f28_price_volume_divergence_energy_price_minus_vol_45d_base_v149_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_energy_price_minus_vol_45d_base_v149_signal},
    "f28pd_f28_price_volume_divergence_composite_tanh_70d_base_v150_signal": {"inputs": ["closeadj", "volume"], "func": f28pd_f28_price_volume_divergence_composite_tanh_70d_base_v150_signal},
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
    for name, entry in f28_price_volume_divergence_base_076_150_REGISTRY.items():
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
    print(f"OK base_076_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
