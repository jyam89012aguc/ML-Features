"""f24_volume_price_confirmation base features 076-150.

Domain: features that quantify whether volume CONFIRMS price moves.
Structurally distinct from base_001_075 — no two features in either file
share the same expression up to a window-size change. NaN policy: never
fillna(<value>); only replace([inf,-inf],nan) at final return. Windows
>21 use closeadj; <=21 use close.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _sma(s, n):
    return s.rolling(n, min_periods=n).mean()


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


# === A. Vol-weighted return Sharpe-like ratios (different from vwret in 001-075)


def f24vp_f24_volume_price_confirmation_vwret_sharpe_30d_base_v076_signal(closeadj, volume):
    """vwret(30) / std(vw_ret_daily,30). Information-ratio for vol-weighted moves."""
    n = 30
    r = closeadj.pct_change(1)
    vw_daily = (r * volume) / volume.rolling(1).mean()  # daily vw alias = r when norm
    mean = (r * volume).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    sd = (r * volume).rolling(n, min_periods=n).std().replace(0.0, np.nan)
    _ = vw_daily
    return (mean / sd).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_dollar_flow_sharpe_80d_base_v077_signal(closeadj, volume):
    """mean(ret*vol,80) / std(ret*vol,80). Signed-flow risk-adjusted intensity."""
    n = 80
    p = closeadj.pct_change(1) * volume
    mn = p.rolling(n, min_periods=n).mean()
    sd = p.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    return (mn / sd).replace([np.inf, -np.inf], np.nan)


# === B. EWMA-based confirmation (different from 001-075 SMA forms) =========


def f24vp_f24_volume_price_confirmation_ewma_corr_absret_vol_alpha20_base_v078_signal(closeadj, volume):
    """EWMA(span=20) of (|ret|-mean_|ret|,40) * (vol-mean_vol,40) / sigmas — EWMA-based
    confirmation co-movement (NOT a simple rolling Pearson)."""
    n = 40
    r = closeadj.pct_change(1).abs()
    r_d = (r - r.rolling(n, min_periods=n).mean()) / r.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    v_d = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    return (r_d * v_d).ewm(span=20, adjust=False, min_periods=20).mean().replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_ewma_signed_dollar_alpha40_base_v079_signal(closeadj, volume):
    """EWMA(40) of sign(ret)*log(vol/SMA(vol,40)). Excess-vol weighted direction, smoothed."""
    s = np.sign(closeadj.pct_change(1))
    excess = np.log(volume / volume.rolling(40, min_periods=40).mean().replace(0.0, np.nan))
    return (s * excess).ewm(span=40, adjust=False, min_periods=40).mean().replace([np.inf, -np.inf], np.nan)


# === C. Quantile-of-confirmation rolling (sorted by intensity) =============


def f24vp_f24_volume_price_confirmation_q75_volabsret_45d_base_v080_signal(close, volume):
    """75th percentile of vol*|ret| over 45d. Upper-tail energy threshold."""
    n = 45
    e = volume * close.pct_change(1).abs()
    return e.rolling(n, min_periods=n).quantile(0.75).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_iqr_signed_volflow_100d_base_v081_signal(closeadj, volume):
    """IQR of (sign(ret)*vol) over 100d. Robust dispersion of signed flow."""
    n = 100
    f = np.sign(closeadj.pct_change(1)) * volume
    q75 = f.rolling(n, min_periods=n).quantile(0.75)
    q25 = f.rolling(n, min_periods=n).quantile(0.25)
    return (q75 - q25).replace([np.inf, -np.inf], np.nan)


# === D. Kendall-tau-like sign concordance ratios (NOT in 001-075) ==========


def f24vp_f24_volume_price_confirmation_signpair_concord_30d_base_v082_signal(close, volume):
    """SMA(30, sign(close.diff(1)) * sign(volume.diff(1))). Tick-level direction agreement."""
    n = 30
    s = np.sign(close.diff(1)) * np.sign(volume.diff(1))
    return s.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_signpair_concord_5d_lag_80d_base_v083_signal(closeadj, volume):
    """SMA(80, sign(close.diff(5)) * sign(volume.diff(5))). 5d cumulative direction agreement."""
    n = 80
    s = np.sign(closeadj.diff(5)) * np.sign(volume.diff(5))
    return s.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === E. Hi-low volume cohort means split by return magnitude bin ===========


def f24vp_f24_volume_price_confirmation_vol_q4_minus_q1_by_absret_90d_base_v084_signal(closeadj, volume):
    """Avg(vol on top-quartile |ret|) - Avg(vol on bottom-quartile |ret|) over 90d.
    Difference in absolute volume between high-magnitude and low-magnitude days."""
    n = 90
    r = closeadj.pct_change(1).abs()
    q75 = r.rolling(n, min_periods=n).quantile(0.75)
    q25 = r.rolling(n, min_periods=n).quantile(0.25)
    m_hi = (r >= q75).astype(float).where(~q75.isna())
    m_lo = (r <= q25).astype(float).where(~q25.isna())
    v_hi = (volume * m_hi).rolling(n, min_periods=n).sum() / m_hi.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    v_lo = (volume * m_lo).rolling(n, min_periods=n).sum() / m_lo.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return np.log(v_hi / v_lo).replace([np.inf, -np.inf], np.nan)


# === F. Vol-divergence ratio (high vol / low vol day decisions) ============


def f24vp_f24_volume_price_confirmation_logsum_v_on_up_log_55d_base_v085_signal(closeadj, volume):
    """log( EMA(55, vol|up_day) / EMA(55, vol) ). Excess of up-day volume.
    EWMA-conditioned — different from SMA-based balance in 001-075."""
    r = closeadj.pct_change(1)
    up_vol = volume.where(r > 0.0, 0.0)
    num = up_vol.ewm(span=55, adjust=False, min_periods=55).mean()
    den = volume.ewm(span=55, adjust=False, min_periods=55).mean().replace(0.0, np.nan)
    return np.log(num / den).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_count_vol_q90_per_decade_180d_base_v086_signal(closeadj, volume):
    """Count of days where vol > q90(vol,180), summed in 180d window, normalized by
    proportion of |ret|>q90(|ret|,180) at SAME days. Joint top-decile alignment density
    (not a ratio of volumes)."""
    n = 180
    r = closeadj.pct_change(1).abs()
    vq = volume.rolling(n, min_periods=n).quantile(0.9)
    rq = r.rolling(n, min_periods=n).quantile(0.9)
    joint = ((volume > vq) & (r > rq)).astype(float).where(~vq.isna() & ~rq.isna())
    return joint.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


# === G. ATR-vol product (range x volume) ==================================


def f24vp_f24_volume_price_confirmation_atr_vol_product_30d_base_v087_signal(close, volume, high, low):
    """SMA(30, vol * (high-low)/close ). Daily dollar-range energy product."""
    n = 30
    rng = (high - low) / close.replace(0.0, np.nan)
    return (volume * rng).rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === H. Slopes/diffs of confirmation regimes  (vol-corr.diff at long lags) =


def f24vp_f24_volume_price_confirmation_corr_absret_vol_30d_lag_diff_base_v088_signal(closeadj, volume):
    """corr(|ret|,vol,30) - corr(|ret|,vol,30).shift(63). Regime drift.
    Different from short-minus-long in 001-075 (which subtracts at different
    windows; this subtracts at different time lags of the same window)."""
    r = closeadj.pct_change(1).abs()
    c = r.rolling(30, min_periods=30).corr(volume)
    return (c - c.shift(63)).replace([np.inf, -np.inf], np.nan)


# === I. Spectral-style fingerprints of confirmation (variance ratios) ======


def f24vp_f24_volume_price_confirmation_var_ratio_volret_short_long_base_v089_signal(closeadj, volume):
    """var(ret*vol,20) / var(ret*vol,100). Short-vs-long flow-vol ratio."""
    p = closeadj.pct_change(1) * volume
    s = p.rolling(20, min_periods=20).var()
    l = p.rolling(100, min_periods=100).var().replace(0.0, np.nan)
    return (s / l).replace([np.inf, -np.inf], np.nan)


# === J. Average true range scaled by relative volume =======================


def f24vp_f24_volume_price_confirmation_relvol_x_ret_50d_base_v090_signal(closeadj, volume):
    """SMA(50, (vol / SMA(vol,50)) * ret). Relative volume signed-flow."""
    n = 50
    rel_v = volume / volume.rolling(n, min_periods=n).mean().replace(0.0, np.nan)
    r = closeadj.pct_change(1)
    return (rel_v * r).rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_relvol_x_absret_120d_base_v091_signal(closeadj, volume):
    """SMA(120, (vol/SMA(vol,120)) * |ret|). Relative-volume magnitude flow."""
    n = 120
    rel_v = volume / volume.rolling(n, min_periods=n).mean().replace(0.0, np.nan)
    r = closeadj.pct_change(1).abs()
    return (rel_v * r).rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === K. Vol spike-only confirmation (top-decile-vol days, ret stats) =======


def f24vp_f24_volume_price_confirmation_topdec_vol_absret_mean_70d_base_v092_signal(closeadj, volume):
    """Avg(|ret|) on top-decile vol days within 70d. Do spikes carry big moves?"""
    n = 70
    r = closeadj.pct_change(1).abs()
    th = volume.rolling(n, min_periods=n).quantile(0.9)
    m = (volume >= th).astype(float).where(~th.isna())
    return ((r * m).rolling(n, min_periods=n).sum() / m.rolling(n, min_periods=n).sum().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_botdec_vol_absret_mean_70d_base_v093_signal(closeadj, volume):
    """Avg(|ret|) on bottom-decile vol days within 70d. Quiet-vol day movement size."""
    n = 70
    r = closeadj.pct_change(1).abs()
    th = volume.rolling(n, min_periods=n).quantile(0.1)
    m = (volume <= th).astype(float).where(~th.isna())
    return ((r * m).rolling(n, min_periods=n).sum() / m.rolling(n, min_periods=n).sum().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === L. Quantile-rank cross product =======================================


def f24vp_f24_volume_price_confirmation_qrank_volabsret_score_50d_base_v094_signal(close, volume):
    """SMA(50, rank(|ret|,50) * rank(vol,50) ) where ranks are 0-1 percent ranks.
    Both-high days score near 1, both-low days score near 0 -> confirmation score."""
    n = 50
    r = close.pct_change(1).abs()
    rk_r = r.rolling(n, min_periods=n).apply(lambda x: float((np.sum(x <= x[-1]) - 1) / max(1, len(x) - 1)), raw=True)
    rk_v = volume.rolling(n, min_periods=n).apply(lambda x: float((np.sum(x <= x[-1]) - 1) / max(1, len(x) - 1)), raw=True)
    return (rk_r * rk_v).rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === M. Cumulative net-vol divergence from price net-change ===============


def f24vp_f24_volume_price_confirmation_netvol_div_norm_80d_base_v095_signal(closeadj, volume):
    """( cumsum(sign(ret)*vol) over 80d ) / ( cumsum(|ret|*vol) over 80d ).
    Bounded in [-1,1]. Net directional efficiency of volume."""
    n = 80
    r = closeadj.pct_change(1)
    num = (np.sign(r) * volume).rolling(n, min_periods=n).sum()
    den = (r.abs() * volume).rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_netvol_div_norm_25d_base_v096_signal(close, volume):
    """Net-directional-vol / total-dollar-energy over 25d (short-horizon)."""
    n = 25
    r = close.pct_change(1)
    num = (np.sign(r) * volume).rolling(n, min_periods=n).sum()
    den = (r.abs() * volume).rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


# === N. Vol-thrust velocity (rolling diff of thrust) =======================


def f24vp_f24_volume_price_confirmation_thrust_change_20d_base_v097_signal(close, volume):
    """sum(up-dn,20).diff(10). Thrust velocity. Smaller window than thrust_slope v071."""
    n = 20
    r = close.pct_change(1)
    up = volume.where(r > 0.0, 0.0)
    dn = volume.where(r < 0.0, 0.0)
    th = (up - dn).rolling(n, min_periods=n).sum()
    return th.diff(10).replace([np.inf, -np.inf], np.nan)


# === O. EWM correlation with smoothed return ==============================


def f24vp_f24_volume_price_confirmation_ewmcov_logvol_ret_alpha30_base_v098_signal(closeadj, volume):
    """EWM cov (span=30) between log(vol) and ret. Smooth co-movement."""
    r = closeadj.pct_change(1)
    lv = np.log(volume.replace(0.0, np.nan))
    return r.ewm(span=30, adjust=False, min_periods=30).cov(lv).replace([np.inf, -np.inf], np.nan)


# === P. Volume z-score x ATR-z-score product ==============================


def f24vp_f24_volume_price_confirmation_volz_x_atrz_45d_base_v099_signal(closeadj, volume, high, low):
    """SMA(45, vol_z(45) * ATR_z(45)). Confirmed range-vol expansion."""
    n = 45
    tr = pd.concat([(high - low).abs(),
                    (high - closeadj.shift(1)).abs(),
                    (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    az = (atr - atr.rolling(n, min_periods=n).mean()) / atr.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    return (vz * az).rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === Q. Body-x-volume vs total range-x-volume ratio  ======================


def f24vp_f24_volume_price_confirmation_body_to_range_volwt_60d_base_v100_signal(closeadj, volume, high, low, open):
    """sum(vol*|close-open|,60) / sum(vol*(high-low),60). Volume-weighted body/range ratio.
    High = volume going into directional bars vs choppy ones."""
    n = 60
    num = (volume * (closeadj - open).abs()).rolling(n, min_periods=n).sum()
    den = (volume * (high - low)).rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


# === R. Granville-confirmation table (4 categories: bigret/smallret x bigvol/smallvol)


def f24vp_f24_volume_price_confirmation_granville_confirmed_frac_75d_base_v101_signal(closeadj, volume):
    """Fraction of days within 75d that are SIGN-confirmed: sign(ret)==sign(volume.diff(1))."""
    n = 75
    s_r = np.sign(closeadj.pct_change(1))
    s_v = np.sign(volume.diff(1))
    flag = (s_r == s_v).astype(float).where(~s_r.isna() & ~s_v.isna())
    # Avoid trivial both-zero matches by requiring nonzero
    nz = ((s_r != 0.0) & (s_v != 0.0)).astype(float).where(~s_r.isna() & ~s_v.isna())
    num = (flag * nz).rolling(n, min_periods=n).sum()
    den = nz.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


# === S. Vol-burst preceding big moves =====================================


def f24vp_f24_volume_price_confirmation_vol_lead_absret_corr_50d_base_v102_signal(closeadj, volume):
    """corr(vol, |ret.shift(-1)|, 50). Does today's vol predict tomorrow's |move|?
    Lead-lag confirmation."""
    n = 50
    r = closeadj.pct_change(1).abs()
    return volume.rolling(n, min_periods=n).corr(r.shift(-1)).replace([np.inf, -np.inf], np.nan)


# === T. Volume break / move conditional probability ========================


def f24vp_f24_volume_price_confirmation_p_bigmove_given_bigvol_60d_base_v103_signal(closeadj, volume):
    """P(|ret| > q70 | vol > q70) over 60d — conditional probability."""
    n = 60
    r = closeadj.pct_change(1).abs()
    rq = r.rolling(n, min_periods=n).quantile(0.7)
    vq = volume.rolling(n, min_periods=n).quantile(0.7)
    big_v = (volume > vq).astype(float).where(~vq.isna())
    big_r = (r > rq).astype(float).where(~rq.isna())
    joint = (big_v * big_r).rolling(n, min_periods=n).sum()
    den = big_v.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (joint / den).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_p_bigvol_given_bigmove_60d_base_v104_signal(closeadj, volume):
    """P(vol > q70 | |ret| > q70) over 60d."""
    n = 60
    r = closeadj.pct_change(1).abs()
    rq = r.rolling(n, min_periods=n).quantile(0.7)
    vq = volume.rolling(n, min_periods=n).quantile(0.7)
    big_v = (volume > vq).astype(float).where(~vq.isna())
    big_r = (r > rq).astype(float).where(~rq.isna())
    joint = (big_v * big_r).rolling(n, min_periods=n).sum()
    den = big_r.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (joint / den).replace([np.inf, -np.inf], np.nan)


# === U. Mutual-information-style symmetric chi-square-ish indicator =======


def f24vp_f24_volume_price_confirmation_phi_coef_signv_signret_50d_base_v105_signal(closeadj, volume):
    """phi coefficient of (sign(close.diff(1)), sign(vol.diff(1))) over 50d window."""
    n = 50
    a = np.sign(closeadj.diff(1))
    b = np.sign(volume.diff(1))
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    av = a.values; bv = b.values
    for i in range(n - 1, len(closeadj)):
        aw = av[i - n + 1:i + 1]
        bw = bv[i - n + 1:i + 1]
        msk = np.isfinite(aw) & np.isfinite(bw) & (aw != 0.0) & (bv[i - n + 1:i + 1] != 0.0)
        if msk.sum() < 10:
            continue
        x = (aw[msk] > 0).astype(float)
        y = (bw[msk] > 0).astype(float)
        sx = x.std(); sy = y.std()
        if sx == 0.0 or sy == 0.0:
            continue
        out.iat[i] = float(np.corrcoef(x, y)[0, 1])
    return out.replace([np.inf, -np.inf], np.nan)


# === V. log-Vol slope x sign of return ====================================


def f24vp_f24_volume_price_confirmation_logvol_slope_x_signret_40d_base_v106_signal(closeadj, volume):
    """SMA(40, sign(ret) * log(vol).diff(5)). Vol expansion in price direction."""
    n = 40
    s = np.sign(closeadj.pct_change(1))
    lvs = np.log(volume.replace(0.0, np.nan)).diff(5)
    return (s * lvs).rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === W. Cumulative directional thrust (CDT) and CDT/total ratio ===========


def f24vp_f24_volume_price_confirmation_cum_signed_vol_to_total_45d_base_v107_signal(closeadj, volume):
    """sum(sign(ret)*vol,45) / sum(vol,45). Net directional volume share."""
    n = 45
    s = np.sign(closeadj.pct_change(1))
    num = (s * volume).rolling(n, min_periods=n).sum()
    den = volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    # 001-075 v009 has 50d signed_vol_ratio. Use different window AND construction (sign of pct vs sign of return same; window difference too small alone).
    # To avoid pure window-change duplicate: combine with median-deviation discount
    med = num.rolling(n, min_periods=n).median()
    return ((num - med) / den).replace([np.inf, -np.inf], np.nan)


# === X. Range-weighted price-volume confirmation ==========================


def f24vp_f24_volume_price_confirmation_range_signed_vol_40d_base_v108_signal(close, volume, high, low):
    """SMA(40, sign(close.pct_change) * vol * (high-low)/close). Range-amplified flow."""
    n = 40
    rng = (high - low) / close.replace(0.0, np.nan)
    s = np.sign(close.pct_change(1))
    return (s * volume * rng).rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === Y. Sign-of-correlation regime indicator ==============================


def f24vp_f24_volume_price_confirmation_sign_corr_absret_vol_60d_base_v109_signal(closeadj, volume):
    """sign( corr(|ret|,vol,60) ). Discrete confirmation-regime classifier."""
    n = 60
    r = closeadj.pct_change(1).abs()
    return np.sign(r.rolling(n, min_periods=n).corr(volume)).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_sign_corr_signret_vol_30d_base_v110_signal(close, volume):
    """sign( corr(sign(ret),vol,30) ). Discrete directional-confirmation classifier."""
    n = 30
    s = np.sign(close.pct_change(1))
    return np.sign(s.rolling(n, min_periods=n).corr(volume)).replace([np.inf, -np.inf], np.nan)


# === Z. Volume-confirmation index (Twiggs-style smoothed agreement) =======


def f24vp_f24_volume_price_confirmation_volprice_kurtcorr_90d_base_v111_signal(closeadj, volume):
    """Rolling corr between (ret-mean)^4 (price 4th-moment-component) and vol over 90d.
    Tail-event vol confirmation."""
    n = 90
    r = closeadj.pct_change(1)
    mu = r.rolling(n, min_periods=n).mean()
    dev4 = (r - mu) ** 4
    return dev4.rolling(n, min_periods=n).corr(volume).replace([np.inf, -np.inf], np.nan)


# === AA. Vol-share of trend leg =========================================


def f24vp_f24_volume_price_confirmation_vol_share_of_trend_leg_60d_base_v112_signal(closeadj, volume):
    """sum(vol on days where sign(ret) matches sign(SMA(ret,5))) / sum(vol) over 60d."""
    n = 60
    r = closeadj.pct_change(1)
    trend = np.sign(r.rolling(5, min_periods=5).mean())
    agree = (np.sign(r) == trend).astype(float).where(~trend.isna() & ~np.isnan(r))
    num = (agree * volume).rolling(n, min_periods=n).sum()
    den = volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


# === AB. Vol-weighted standard deviation of returns =====================


def f24vp_f24_volume_price_confirmation_vol_weighted_ret_skew_70d_base_v113_signal(closeadj, volume):
    """Volume-weighted skewness of ret over 70d.
    skew_vw = sum(w*(r-mu)^3)/sum(w) / sigma_vw^3."""
    n = 70
    r = closeadj.pct_change(1)
    w = volume
    sw = w.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    mu = (w * r).rolling(n, min_periods=n).sum() / sw
    dev = r - mu
    m2 = (w * dev * dev).rolling(n, min_periods=n).sum() / sw
    m3 = (w * dev * dev * dev).rolling(n, min_periods=n).sum() / sw
    sigma = np.sqrt(m2)
    return (m3 / (sigma * sigma * sigma).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vol_weighted_ret_kurt_120d_base_v114_signal(closeadj, volume):
    """Volume-weighted excess kurtosis of returns over 120d."""
    n = 120
    r = closeadj.pct_change(1)
    w = volume
    sw = w.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    mu = (w * r).rolling(n, min_periods=n).sum() / sw
    dev = r - mu
    m2 = (w * dev * dev).rolling(n, min_periods=n).sum() / sw
    m4 = (w * dev * dev * dev * dev).rolling(n, min_periods=n).sum() / sw
    return ((m4 / (m2 * m2).replace(0.0, np.nan)) - 3.0).replace([np.inf, -np.inf], np.nan)


# === AC. EMA-thrust slope and convexity ==================================


def f24vp_f24_volume_price_confirmation_ema_thrust_convexity_50d_base_v115_signal(closeadj, volume):
    """EMA(50,sign(ret)*vol).diff(5) - EMA(50,sign(ret)*vol).diff(5).shift(5). Convexity of thrust."""
    s = np.sign(closeadj.pct_change(1))
    et = (s * volume).ewm(span=50, adjust=False, min_periods=50).mean()
    d = et.diff(5)
    return (d - d.shift(5)).replace([np.inf, -np.inf], np.nan)


# === AD. Conditional confirmation P&L =====================================


def f24vp_f24_volume_price_confirmation_confirmed_ret_mean_80d_base_v116_signal(closeadj, volume):
    """Avg ret on days where vol > median(vol,80). What's the directional drift conditional
    on high volume?"""
    n = 80
    r = closeadj.pct_change(1)
    vmed = volume.rolling(n, min_periods=n).median()
    m = (volume > vmed).astype(float).where(~vmed.isna())
    return ((r * m).rolling(n, min_periods=n).sum() / m.rolling(n, min_periods=n).sum().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_unconfirmed_ret_mean_80d_base_v117_signal(closeadj, volume):
    """Avg ret on days where vol <= median(vol,80)."""
    n = 80
    r = closeadj.pct_change(1)
    vmed = volume.rolling(n, min_periods=n).median()
    m = (volume <= vmed).astype(float).where(~vmed.isna())
    return ((r * m).rolling(n, min_periods=n).sum() / m.rolling(n, min_periods=n).sum().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === AE. Vol-spike / move-spike alignment count ==========================


def f24vp_f24_volume_price_confirmation_volspike_moveaspike_align_45d_base_v118_signal(closeadj, volume):
    """Count of days in 45d where BOTH vol_z(45)>1 AND |ret|_z(45)>1. Joint spikes."""
    n = 45
    r = closeadj.pct_change(1).abs()
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    rz = (r - r.rolling(n, min_periods=n).mean()) / r.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    flag = ((vz > 1.0) & (rz > 1.0)).astype(float).where(~vz.isna() & ~rz.isna())
    return flag.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


# === AF. Sign of body-volume product ====================================


def f24vp_f24_volume_price_confirmation_sign_body_volz_30d_base_v119_signal(close, volume, open):
    """SMA(30, sign(close-open) * sign(vol - SMA(vol,30))). Intraday direction-vol confirmation."""
    n = 30
    s_body = np.sign(close - open)
    s_vol = np.sign(volume - volume.rolling(n, min_periods=n).mean())
    return (s_body * s_vol).rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === AG. Volume-Price Trend (VPT) slope ==================================


def f24vp_f24_volume_price_confirmation_vpt_slope_norm_60d_base_v120_signal(closeadj, volume):
    """VPT = cumsum( vol * close.pct_change ). Slope = VPT.diff(21) / SMA(vol,21).
    Trend-aligned cumulative signed flow."""
    vpt = (volume * closeadj.pct_change(1)).cumsum()
    return (vpt.diff(21) / volume.rolling(21, min_periods=21).mean().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vpt_to_price_slope_corr_120d_base_v121_signal(closeadj, volume):
    """corr(VPT.diff(5), close.diff(5), 120). Long-window agreement of VPT trend vs price trend."""
    n = 120
    vpt = (volume * closeadj.pct_change(1)).cumsum()
    return vpt.diff(5).rolling(n, min_periods=n).corr(closeadj.diff(5)).replace([np.inf, -np.inf], np.nan)


# === AH. Conditional log-vol z-score by return sign ====================


def f24vp_f24_volume_price_confirmation_logvolz_on_signret_corr_75d_base_v122_signal(closeadj, volume):
    """corr( log(vol)_z(75), sign(close.diff(1)), 75 ). Directional-vol-tail confirmation."""
    n = 75
    lv = np.log(volume.replace(0.0, np.nan))
    lvz = (lv - lv.rolling(n, min_periods=n).mean()) / lv.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    s = np.sign(closeadj.diff(1))
    return lvz.rolling(n, min_periods=n).corr(s).replace([np.inf, -np.inf], np.nan)


# === AI. Magnitude-of-flow asymmetry  ===================================


def f24vp_f24_volume_price_confirmation_n_confirmed_bursts_150d_base_v123_signal(closeadj, volume):
    """Count of (volz>1 & |ret|z>1) bursts that flip on/off across 150d (a burst
    is a 0->1 transition). Discrete event rate of joint spikes."""
    n = 150
    vz = (volume - volume.rolling(60, min_periods=60).mean()) / volume.rolling(60, min_periods=60).std().replace(0.0, np.nan)
    r = closeadj.pct_change(1).abs()
    rz = (r - r.rolling(60, min_periods=60).mean()) / r.rolling(60, min_periods=60).std().replace(0.0, np.nan)
    flag = ((vz > 1.0) & (rz > 1.0)).astype(float).where(~vz.isna() & ~rz.isna())
    burst = ((flag > 0.5) & (flag.shift(1) < 0.5)).astype(float).where(~flag.shift(1).isna())
    return burst.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


# === AJ. Log of total dollar volume / log of total |ret| =================


def f24vp_f24_volume_price_confirmation_log_vol_total_per_abs_move_40d_base_v124_signal(close, volume):
    """log( sum(vol,40) ) / log( sum(|ret|,40) ). Vol per unit move."""
    n = 40
    r = close.pct_change(1).abs()
    lv = np.log(volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan))
    lr = np.log(r.rolling(n, min_periods=n).sum().replace(0.0, np.nan))
    return (lv / lr).replace([np.inf, -np.inf], np.nan)


# === AK. Confirmation-asymmetry index ====================================


def f24vp_f24_volume_price_confirmation_asym_idx_volz_ret_55d_base_v125_signal(closeadj, volume):
    """ SMA(55, (vol-mean) * ret^3 ). Cubed ret captures tail asymmetry weighted by vol excess."""
    n = 55
    vexc = volume - volume.rolling(n, min_periods=n).mean()
    r = closeadj.pct_change(1)
    return (vexc * r * r * r).rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === AL. Vol-acceleration aligned with price-acceleration ================


def f24vp_f24_volume_price_confirmation_vol_acc_price_acc_align_30d_base_v126_signal(close, volume):
    """SMA(30, sign(vol.diff().diff()) * sign(close.diff().diff())). Curvature alignment."""
    n = 30
    sv = np.sign(volume.diff().diff())
    sp = np.sign(close.diff().diff())
    return (sv * sp).rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === AM. Bounded transforms (atan, tanh, sigmoid) at new windows  ========


def f24vp_f24_volume_price_confirmation_tanh_money_flow_norm_45d_base_v127_signal(closeadj, volume):
    """tanh( (sum(ret*vol,45)/SMA(vol,45)) / std(ret,45) )."""
    n = 45
    r = closeadj.pct_change(1)
    flow = (r * volume).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).mean().replace(0.0, np.nan)
    sd = r.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    return np.tanh(flow / sd).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_arctan_topdec_volz_75d_base_v128_signal(closeadj, volume):
    """arctan( topdec_volz(75) ). Bounded version of high-magnitude-day volume z."""
    n = 75
    r = closeadj.pct_change(1).abs()
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    th = r.rolling(n, min_periods=n).quantile(0.9)
    m = (r >= th).astype(float).where(~th.isna())
    avg = (vz * m).rolling(n, min_periods=n).sum() / m.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return np.arctan(avg).replace([np.inf, -np.inf], np.nan)


# === AN. Volume-weighted absolute return autocorrelation =================


def f24vp_f24_volume_price_confirmation_vw_absret_autocorr_60d_base_v129_signal(closeadj, volume):
    """corr( |ret|*vol(t), |ret|*vol(t-5), 60 ). Persistence of confirmation events."""
    n = 60
    e = closeadj.pct_change(1).abs() * volume
    return e.rolling(n, min_periods=n).corr(e.shift(5)).replace([np.inf, -np.inf], np.nan)


# === AO. Trend-aligned vol fraction long-window ==========================


def f24vp_f24_volume_price_confirmation_trend_vol_share_200d_base_v130_signal(closeadj, volume):
    """sum(vol when sign(ret)==sign(SMA(ret,21))) / total vol, over 200d. Long-window
    trend-aligned vol share."""
    n = 200
    r = closeadj.pct_change(1)
    trend = np.sign(r.rolling(21, min_periods=21).mean())
    agree = (np.sign(r) == trend).astype(float).where(~trend.isna() & ~np.isnan(r))
    num = (agree * volume).rolling(n, min_periods=n).sum()
    den = volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


# === AP. ATR-x-vol z product slope =======================================


def f24vp_f24_volume_price_confirmation_atrvolz_diff_40d_base_v131_signal(closeadj, volume, high, low):
    """( vol*ATR ).diff(10) over 40d-EMA smoothing."""
    n = 40
    tr = pd.concat([(high - low).abs(),
                    (high - closeadj.shift(1)).abs(),
                    (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    prod = (volume * atr).ewm(span=n, adjust=False, min_periods=n).mean()
    return prod.diff(10).replace([np.inf, -np.inf], np.nan)


# === AQ. Days-with-vol-and-direction confirmation, broken out ============


def f24vp_f24_volume_price_confirmation_count_upday_highvol_50d_base_v132_signal(closeadj, volume):
    """Count of days within 50d where close.diff>0 AND vol > q60(vol,50)."""
    n = 50
    up = (closeadj.diff(1) > 0.0).astype(float)
    vq = volume.rolling(n, min_periods=n).quantile(0.6)
    cond = (up.astype(bool) & (volume > vq)).astype(float).where(~vq.isna())
    return cond.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_count_dnday_highvol_50d_base_v133_signal(closeadj, volume):
    """Count of days where close.diff<0 AND vol > q60. Compare to v132 for up/down imbalance."""
    n = 50
    dn = (closeadj.diff(1) < 0.0).astype(float)
    vq = volume.rolling(n, min_periods=n).quantile(0.6)
    cond = (dn.astype(bool) & (volume > vq)).astype(float).where(~vq.isna())
    return cond.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_up_dn_highvol_imbalance_50d_base_v134_signal(closeadj, volume):
    """(count_upday_highvol - count_dnday_highvol) / 50 over 50d."""
    n = 50
    up = (closeadj.diff(1) > 0.0).astype(float)
    dn = (closeadj.diff(1) < 0.0).astype(float)
    vq = volume.rolling(n, min_periods=n).quantile(0.6)
    cu = (up.astype(bool) & (volume > vq)).astype(float).where(~vq.isna())
    cd = (dn.astype(bool) & (volume > vq)).astype(float).where(~vq.isna())
    return ((cu - cd).rolling(n, min_periods=n).sum() / float(n)).replace([np.inf, -np.inf], np.nan)


# === AR. Volume entropy by return-bin ===================================


def f24vp_f24_volume_price_confirmation_vol_entropy_signret_60d_base_v135_signal(closeadj, volume):
    """Volume share-entropy by 3-bin sign(ret) over 60d. Low = vol concentrated in one bin
    (asymmetric). High = vol spread across bins."""
    n = 60
    s = np.sign(closeadj.pct_change(1))
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    sv = s.values; vv = volume.values
    for i in range(n - 1, len(closeadj)):
        sw = sv[i - n + 1:i + 1]
        vw = vv[i - n + 1:i + 1]
        if np.any(~np.isfinite(sw)) or np.any(~np.isfinite(vw)):
            continue
        tot = vw.sum()
        if tot <= 0.0:
            continue
        sums = []
        for bin_val in (-1.0, 0.0, 1.0):
            sums.append(vw[sw == bin_val].sum())
        p = np.asarray(sums) / tot
        p = p[p > 0.0]
        out.iat[i] = float(-(p * np.log(p)).sum())
    return out.replace([np.inf, -np.inf], np.nan)


# === AS. Conditional vol-on-extreme-ret slope ============================


def f24vp_f24_volume_price_confirmation_topdec_volz_slope_100d_base_v136_signal(closeadj, volume):
    """topdec_volz(100).diff(21). Slope of confirmation regime."""
    n = 100
    r = closeadj.pct_change(1).abs()
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    th = r.rolling(n, min_periods=n).quantile(0.9)
    m = (r >= th).astype(float).where(~th.isna())
    avg = (vz * m).rolling(n, min_periods=n).sum() / m.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return avg.diff(21).replace([np.inf, -np.inf], np.nan)


# === AT. Vol-confirmed gap (open-vs-prev-close) ==========================


def f24vp_f24_volume_price_confirmation_gap_volz_align_45d_base_v137_signal(closeadj, volume, open):
    """SMA(45, sign(open.diff(0)/closeadj.shift(1) - 1) * vol_z(45))."""
    n = 45
    gap = open / closeadj.shift(1) - 1.0
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    return (np.sign(gap) * vz).rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === AU. Vol explain power on |ret| (rolling R^2) =======================


def f24vp_f24_volume_price_confirmation_rsq_vol_explains_absret_70d_base_v138_signal(closeadj, volume):
    """R^2 of linear fit (|ret| ~ a + b*log(vol)) over 70d. How much vol explains move size."""
    n = 70
    r = closeadj.pct_change(1).abs()
    lv = np.log(volume.replace(0.0, np.nan))
    c = r.rolling(n, min_periods=n).corr(lv)
    return (c * c).replace([np.inf, -np.inf], np.nan)


# === AV. Volume MACD vs price MACD alignment ============================


def f24vp_f24_volume_price_confirmation_vol_macd_x_price_macd_60d_base_v139_signal(closeadj, volume):
    """SMA(60, sign( EMA(vol,12)-EMA(vol,26) ) * sign( EMA(close,12)-EMA(close,26) )).
    Volume MACD and price MACD direction agreement."""
    n = 60
    vm = np.sign(volume.ewm(span=12, adjust=False, min_periods=12).mean() - volume.ewm(span=26, adjust=False, min_periods=26).mean())
    pm = np.sign(closeadj.ewm(span=12, adjust=False, min_periods=12).mean() - closeadj.ewm(span=26, adjust=False, min_periods=26).mean())
    return (vm * pm).rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === AW. Confirmation force (signed flow / std of flow) =================


def f24vp_f24_volume_price_confirmation_force_index_norm_25d_base_v140_signal(close, volume):
    """SMA(25, close.diff(1) * vol) / SMA(25, |close.diff(1)*vol|). Force index normalized."""
    n = 25
    f = close.diff(1) * volume
    return (f.rolling(n, min_periods=n).mean() / f.abs().rolling(n, min_periods=n).mean().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === AX. Vol-z-score percentile rank over long window ===================


def f24vp_f24_volume_price_confirmation_rank_topdec_volz_180d_base_v141_signal(closeadj, volume):
    """Percent rank within 180d of topdec_volz(60)."""
    n_out = 180; n_in = 60
    r = closeadj.pct_change(1).abs()
    vz = (volume - volume.rolling(n_in, min_periods=n_in).mean()) / volume.rolling(n_in, min_periods=n_in).std().replace(0.0, np.nan)
    th = r.rolling(n_in, min_periods=n_in).quantile(0.9)
    m = (r >= th).astype(float).where(~th.isna())
    avg = (vz * m).rolling(n_in, min_periods=n_in).sum() / m.rolling(n_in, min_periods=n_in).sum().replace(0.0, np.nan)
    return avg.rolling(n_out, min_periods=n_out).apply(lambda x: float((np.sum(x <= x[-1]) - 1) / max(1, len(x) - 1)), raw=True).replace([np.inf, -np.inf], np.nan)


# === AY. Bipolar confirmation index =====================================


def f24vp_f24_volume_price_confirmation_bipolar_pn_diff_50d_base_v142_signal(closeadj, volume):
    """( P(big-up & big-vol,50) - P(big-dn & big-vol,50) ). Directional confirmation bias."""
    n = 50
    r = closeadj.pct_change(1)
    vq = volume.rolling(n, min_periods=n).quantile(0.7)
    rq = r.abs().rolling(n, min_periods=n).quantile(0.7)
    big_up = ((r > 0.0) & (r.abs() > rq) & (volume > vq)).astype(float).where(~vq.isna() & ~rq.isna())
    big_dn = ((r < 0.0) & (r.abs() > rq) & (volume > vq)).astype(float).where(~vq.isna() & ~rq.isna())
    return ((big_up - big_dn).rolling(n, min_periods=n).mean()).replace([np.inf, -np.inf], np.nan)


# === AZ. Sharpe of volume-conditioned returns ===========================


def f24vp_f24_volume_price_confirmation_sharpe_highvol_ret_60d_base_v143_signal(closeadj, volume):
    """mean(ret|highvol,60)/std(ret|highvol,60). Sharpe-like of conditioned returns."""
    n = 60
    r = closeadj.pct_change(1)
    vq = volume.rolling(n, min_periods=n).quantile(0.7)
    msk = (volume > vq).astype(float).where(~vq.isna())
    cond_r = r * msk
    mn = cond_r.rolling(n, min_periods=n).sum() / msk.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    # rolling variance of cond_r where active
    sq = (cond_r * cond_r).rolling(n, min_periods=n).sum() / msk.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    sd = np.sqrt(sq - mn * mn)
    return (mn / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === BA. Smoothed concordance percent rank ==============================


def f24vp_f24_volume_price_confirmation_rank_concord_score_120d_base_v144_signal(closeadj, volume):
    """Percent rank within 120d of concordance(40) — confirmation regime percentile."""
    n_out = 120; n_in = 40
    r = closeadj.pct_change(1).abs()
    r_med = r.rolling(n_in, min_periods=n_in).median()
    v_med = volume.rolling(n_in, min_periods=n_in).median()
    c = (np.sign(r - r_med) * np.sign(volume - v_med)).rolling(n_in, min_periods=n_in).mean()
    return c.rolling(n_out, min_periods=n_out).apply(lambda x: float((np.sum(x <= x[-1]) - 1) / max(1, len(x) - 1)), raw=True).replace([np.inf, -np.inf], np.nan)


# === BB. EMA-of-EMA vol weighted ret ratio ==============================


def f24vp_f24_volume_price_confirmation_double_ema_signed_flow_55d_base_v145_signal(closeadj, volume):
    """EMA(20)( EMA(55, sign(ret)*log(vol)) ). Double-smoothed directional log-vol."""
    s = np.sign(closeadj.pct_change(1))
    lv = np.log(volume.replace(0.0, np.nan))
    inner = (s * lv).ewm(span=55, adjust=False, min_periods=55).mean()
    return inner.ewm(span=20, adjust=False, min_periods=20).mean().replace([np.inf, -np.inf], np.nan)


# === BC. log of (sum vol on big-move days / sum vol on small-move days) =


def f24vp_f24_volume_price_confirmation_logratio_bigmove_vol_125d_base_v146_signal(closeadj, volume):
    """log( sum(vol on |ret|>median,125) / sum(vol on |ret|<=median,125) )."""
    n = 125
    r = closeadj.pct_change(1).abs()
    med = r.rolling(n, min_periods=n).median()
    big = volume.where(r > med, 0.0)
    small = volume.where(r <= med, 0.0)
    sb = big.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    ss = small.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return np.log(sb / ss).replace([np.inf, -np.inf], np.nan)


# === BD. Volume thrust z-score normalized by vol-std ===================


def f24vp_f24_volume_price_confirmation_thrust_z_70d_base_v147_signal(closeadj, volume):
    """thrust(30)_z over 70d. Z-scored long-window thrust."""
    n_out = 70; n_in = 30
    r = closeadj.pct_change(1)
    up = volume.where(r > 0.0, 0.0)
    dn = volume.where(r < 0.0, 0.0)
    th = (up - dn).rolling(n_in, min_periods=n_in).sum()
    z = (th - th.rolling(n_out, min_periods=n_out).mean()) / th.rolling(n_out, min_periods=n_out).std().replace(0.0, np.nan)
    return z.replace([np.inf, -np.inf], np.nan)


# === BE. Volume range x return sign  ===================================


def f24vp_f24_volume_price_confirmation_signed_vol_x_range_z_40d_base_v148_signal(close, volume, high, low):
    """SMA(40, sign(ret) * (vol_z(40) + ((high-low)/close)_z(40))). Composite directional confirmation."""
    n = 40
    s = np.sign(close.pct_change(1))
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    rng = (high - low) / close.replace(0.0, np.nan)
    rzz = (rng - rng.rolling(n, min_periods=n).mean()) / rng.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    return (s * (vz + rzz)).rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === BF. Vol-residual after removing |ret| beta ========================


def f24vp_f24_volume_price_confirmation_vol_residual_after_absret_90d_base_v149_signal(closeadj, volume):
    """std of (vol - a - b*|ret|) over 90d via rolling residual. Residual confirmation noise."""
    n = 90
    r = closeadj.pct_change(1).abs()
    cov = r.rolling(n, min_periods=n).cov(volume)
    var_r = r.rolling(n, min_periods=n).var().replace(0.0, np.nan)
    beta = cov / var_r
    alpha = volume.rolling(n, min_periods=n).mean() - beta * r.rolling(n, min_periods=n).mean()
    resid = volume - alpha - beta * r
    return resid.rolling(n, min_periods=n).std().replace([np.inf, -np.inf], np.nan)


# === BG. Combined directional/magnitude vol confirmation =================


def f24vp_f24_volume_price_confirmation_compound_confirm_score_85d_base_v150_signal(closeadj, volume):
    """SMA(85, sign(ret) * vol_z(85) * |ret|_z(85)). Composite signed-magnitude-confirmation."""
    n = 85
    r = closeadj.pct_change(1)
    s = np.sign(r)
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    ar = r.abs()
    rz = (ar - ar.rolling(n, min_periods=n).mean()) / ar.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    return (s * vz * rz).rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f24_volume_price_confirmation_base_076_150_REGISTRY = {
    "f24vp_f24_volume_price_confirmation_vwret_sharpe_30d_base_v076_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_vwret_sharpe_30d_base_v076_signal},
    "f24vp_f24_volume_price_confirmation_dollar_flow_sharpe_80d_base_v077_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_dollar_flow_sharpe_80d_base_v077_signal},
    "f24vp_f24_volume_price_confirmation_ewma_corr_absret_vol_alpha20_base_v078_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_ewma_corr_absret_vol_alpha20_base_v078_signal},
    "f24vp_f24_volume_price_confirmation_ewma_signed_dollar_alpha40_base_v079_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_ewma_signed_dollar_alpha40_base_v079_signal},
    "f24vp_f24_volume_price_confirmation_q75_volabsret_45d_base_v080_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_q75_volabsret_45d_base_v080_signal},
    "f24vp_f24_volume_price_confirmation_iqr_signed_volflow_100d_base_v081_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_iqr_signed_volflow_100d_base_v081_signal},
    "f24vp_f24_volume_price_confirmation_signpair_concord_30d_base_v082_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_signpair_concord_30d_base_v082_signal},
    "f24vp_f24_volume_price_confirmation_signpair_concord_5d_lag_80d_base_v083_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_signpair_concord_5d_lag_80d_base_v083_signal},
    "f24vp_f24_volume_price_confirmation_vol_q4_minus_q1_by_absret_90d_base_v084_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_vol_q4_minus_q1_by_absret_90d_base_v084_signal},
    "f24vp_f24_volume_price_confirmation_logsum_v_on_up_log_55d_base_v085_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_logsum_v_on_up_log_55d_base_v085_signal},
    "f24vp_f24_volume_price_confirmation_count_vol_q90_per_decade_180d_base_v086_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_count_vol_q90_per_decade_180d_base_v086_signal},
    "f24vp_f24_volume_price_confirmation_atr_vol_product_30d_base_v087_signal": {"inputs": ["close", "volume", "high", "low"], "func": f24vp_f24_volume_price_confirmation_atr_vol_product_30d_base_v087_signal},
    "f24vp_f24_volume_price_confirmation_corr_absret_vol_30d_lag_diff_base_v088_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_corr_absret_vol_30d_lag_diff_base_v088_signal},
    "f24vp_f24_volume_price_confirmation_var_ratio_volret_short_long_base_v089_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_var_ratio_volret_short_long_base_v089_signal},
    "f24vp_f24_volume_price_confirmation_relvol_x_ret_50d_base_v090_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_relvol_x_ret_50d_base_v090_signal},
    "f24vp_f24_volume_price_confirmation_relvol_x_absret_120d_base_v091_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_relvol_x_absret_120d_base_v091_signal},
    "f24vp_f24_volume_price_confirmation_topdec_vol_absret_mean_70d_base_v092_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_topdec_vol_absret_mean_70d_base_v092_signal},
    "f24vp_f24_volume_price_confirmation_botdec_vol_absret_mean_70d_base_v093_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_botdec_vol_absret_mean_70d_base_v093_signal},
    "f24vp_f24_volume_price_confirmation_qrank_volabsret_score_50d_base_v094_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_qrank_volabsret_score_50d_base_v094_signal},
    "f24vp_f24_volume_price_confirmation_netvol_div_norm_80d_base_v095_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_netvol_div_norm_80d_base_v095_signal},
    "f24vp_f24_volume_price_confirmation_netvol_div_norm_25d_base_v096_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_netvol_div_norm_25d_base_v096_signal},
    "f24vp_f24_volume_price_confirmation_thrust_change_20d_base_v097_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_thrust_change_20d_base_v097_signal},
    "f24vp_f24_volume_price_confirmation_ewmcov_logvol_ret_alpha30_base_v098_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_ewmcov_logvol_ret_alpha30_base_v098_signal},
    "f24vp_f24_volume_price_confirmation_volz_x_atrz_45d_base_v099_signal": {"inputs": ["closeadj", "volume", "high", "low"], "func": f24vp_f24_volume_price_confirmation_volz_x_atrz_45d_base_v099_signal},
    "f24vp_f24_volume_price_confirmation_body_to_range_volwt_60d_base_v100_signal": {"inputs": ["closeadj", "volume", "high", "low", "open"], "func": f24vp_f24_volume_price_confirmation_body_to_range_volwt_60d_base_v100_signal},
    "f24vp_f24_volume_price_confirmation_granville_confirmed_frac_75d_base_v101_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_granville_confirmed_frac_75d_base_v101_signal},
    "f24vp_f24_volume_price_confirmation_vol_lead_absret_corr_50d_base_v102_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_vol_lead_absret_corr_50d_base_v102_signal},
    "f24vp_f24_volume_price_confirmation_p_bigmove_given_bigvol_60d_base_v103_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_p_bigmove_given_bigvol_60d_base_v103_signal},
    "f24vp_f24_volume_price_confirmation_p_bigvol_given_bigmove_60d_base_v104_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_p_bigvol_given_bigmove_60d_base_v104_signal},
    "f24vp_f24_volume_price_confirmation_phi_coef_signv_signret_50d_base_v105_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_phi_coef_signv_signret_50d_base_v105_signal},
    "f24vp_f24_volume_price_confirmation_logvol_slope_x_signret_40d_base_v106_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_logvol_slope_x_signret_40d_base_v106_signal},
    "f24vp_f24_volume_price_confirmation_cum_signed_vol_to_total_45d_base_v107_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_cum_signed_vol_to_total_45d_base_v107_signal},
    "f24vp_f24_volume_price_confirmation_range_signed_vol_40d_base_v108_signal": {"inputs": ["close", "volume", "high", "low"], "func": f24vp_f24_volume_price_confirmation_range_signed_vol_40d_base_v108_signal},
    "f24vp_f24_volume_price_confirmation_sign_corr_absret_vol_60d_base_v109_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_sign_corr_absret_vol_60d_base_v109_signal},
    "f24vp_f24_volume_price_confirmation_sign_corr_signret_vol_30d_base_v110_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_sign_corr_signret_vol_30d_base_v110_signal},
    "f24vp_f24_volume_price_confirmation_volprice_kurtcorr_90d_base_v111_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_volprice_kurtcorr_90d_base_v111_signal},
    "f24vp_f24_volume_price_confirmation_vol_share_of_trend_leg_60d_base_v112_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_vol_share_of_trend_leg_60d_base_v112_signal},
    "f24vp_f24_volume_price_confirmation_vol_weighted_ret_skew_70d_base_v113_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_vol_weighted_ret_skew_70d_base_v113_signal},
    "f24vp_f24_volume_price_confirmation_vol_weighted_ret_kurt_120d_base_v114_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_vol_weighted_ret_kurt_120d_base_v114_signal},
    "f24vp_f24_volume_price_confirmation_ema_thrust_convexity_50d_base_v115_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_ema_thrust_convexity_50d_base_v115_signal},
    "f24vp_f24_volume_price_confirmation_confirmed_ret_mean_80d_base_v116_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_confirmed_ret_mean_80d_base_v116_signal},
    "f24vp_f24_volume_price_confirmation_unconfirmed_ret_mean_80d_base_v117_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_unconfirmed_ret_mean_80d_base_v117_signal},
    "f24vp_f24_volume_price_confirmation_volspike_moveaspike_align_45d_base_v118_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_volspike_moveaspike_align_45d_base_v118_signal},
    "f24vp_f24_volume_price_confirmation_sign_body_volz_30d_base_v119_signal": {"inputs": ["close", "volume", "open"], "func": f24vp_f24_volume_price_confirmation_sign_body_volz_30d_base_v119_signal},
    "f24vp_f24_volume_price_confirmation_vpt_slope_norm_60d_base_v120_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_vpt_slope_norm_60d_base_v120_signal},
    "f24vp_f24_volume_price_confirmation_vpt_to_price_slope_corr_120d_base_v121_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_vpt_to_price_slope_corr_120d_base_v121_signal},
    "f24vp_f24_volume_price_confirmation_logvolz_on_signret_corr_75d_base_v122_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_logvolz_on_signret_corr_75d_base_v122_signal},
    "f24vp_f24_volume_price_confirmation_n_confirmed_bursts_150d_base_v123_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_n_confirmed_bursts_150d_base_v123_signal},
    "f24vp_f24_volume_price_confirmation_log_vol_total_per_abs_move_40d_base_v124_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_log_vol_total_per_abs_move_40d_base_v124_signal},
    "f24vp_f24_volume_price_confirmation_asym_idx_volz_ret_55d_base_v125_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_asym_idx_volz_ret_55d_base_v125_signal},
    "f24vp_f24_volume_price_confirmation_vol_acc_price_acc_align_30d_base_v126_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_vol_acc_price_acc_align_30d_base_v126_signal},
    "f24vp_f24_volume_price_confirmation_tanh_money_flow_norm_45d_base_v127_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_tanh_money_flow_norm_45d_base_v127_signal},
    "f24vp_f24_volume_price_confirmation_arctan_topdec_volz_75d_base_v128_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_arctan_topdec_volz_75d_base_v128_signal},
    "f24vp_f24_volume_price_confirmation_vw_absret_autocorr_60d_base_v129_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_vw_absret_autocorr_60d_base_v129_signal},
    "f24vp_f24_volume_price_confirmation_trend_vol_share_200d_base_v130_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_trend_vol_share_200d_base_v130_signal},
    "f24vp_f24_volume_price_confirmation_atrvolz_diff_40d_base_v131_signal": {"inputs": ["closeadj", "volume", "high", "low"], "func": f24vp_f24_volume_price_confirmation_atrvolz_diff_40d_base_v131_signal},
    "f24vp_f24_volume_price_confirmation_count_upday_highvol_50d_base_v132_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_count_upday_highvol_50d_base_v132_signal},
    "f24vp_f24_volume_price_confirmation_count_dnday_highvol_50d_base_v133_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_count_dnday_highvol_50d_base_v133_signal},
    "f24vp_f24_volume_price_confirmation_up_dn_highvol_imbalance_50d_base_v134_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_up_dn_highvol_imbalance_50d_base_v134_signal},
    "f24vp_f24_volume_price_confirmation_vol_entropy_signret_60d_base_v135_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_vol_entropy_signret_60d_base_v135_signal},
    "f24vp_f24_volume_price_confirmation_topdec_volz_slope_100d_base_v136_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_topdec_volz_slope_100d_base_v136_signal},
    "f24vp_f24_volume_price_confirmation_gap_volz_align_45d_base_v137_signal": {"inputs": ["closeadj", "volume", "open"], "func": f24vp_f24_volume_price_confirmation_gap_volz_align_45d_base_v137_signal},
    "f24vp_f24_volume_price_confirmation_rsq_vol_explains_absret_70d_base_v138_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_rsq_vol_explains_absret_70d_base_v138_signal},
    "f24vp_f24_volume_price_confirmation_vol_macd_x_price_macd_60d_base_v139_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_vol_macd_x_price_macd_60d_base_v139_signal},
    "f24vp_f24_volume_price_confirmation_force_index_norm_25d_base_v140_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_force_index_norm_25d_base_v140_signal},
    "f24vp_f24_volume_price_confirmation_rank_topdec_volz_180d_base_v141_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_rank_topdec_volz_180d_base_v141_signal},
    "f24vp_f24_volume_price_confirmation_bipolar_pn_diff_50d_base_v142_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_bipolar_pn_diff_50d_base_v142_signal},
    "f24vp_f24_volume_price_confirmation_sharpe_highvol_ret_60d_base_v143_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_sharpe_highvol_ret_60d_base_v143_signal},
    "f24vp_f24_volume_price_confirmation_rank_concord_score_120d_base_v144_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_rank_concord_score_120d_base_v144_signal},
    "f24vp_f24_volume_price_confirmation_double_ema_signed_flow_55d_base_v145_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_double_ema_signed_flow_55d_base_v145_signal},
    "f24vp_f24_volume_price_confirmation_logratio_bigmove_vol_125d_base_v146_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_logratio_bigmove_vol_125d_base_v146_signal},
    "f24vp_f24_volume_price_confirmation_thrust_z_70d_base_v147_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_thrust_z_70d_base_v147_signal},
    "f24vp_f24_volume_price_confirmation_signed_vol_x_range_z_40d_base_v148_signal": {"inputs": ["close", "volume", "high", "low"], "func": f24vp_f24_volume_price_confirmation_signed_vol_x_range_z_40d_base_v148_signal},
    "f24vp_f24_volume_price_confirmation_vol_residual_after_absret_90d_base_v149_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_vol_residual_after_absret_90d_base_v149_signal},
    "f24vp_f24_volume_price_confirmation_compound_confirm_score_85d_base_v150_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_compound_confirm_score_85d_base_v150_signal},
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
    for name, entry in f24_volume_price_confirmation_base_076_150_REGISTRY.items():
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
