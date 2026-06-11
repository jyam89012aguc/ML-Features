"""f25_vwap_deviation base features 076-150.

Second half of base features. Each spells the VWAP formula fully inline.
Structurally distinct from 001-075: no shared expression up to a window
change. Domain: VWAP DEVIATION - features reference VWAP, anchored-VWAP,
VWAP-bands, VWAP-slope, VWAP residuals, TWAP-vs-VWAP contrast, and
combined-window VWAP signals.

NaN policy: only replace([inf,-inf],nan) at the final return. Window > 21
uses closeadj; <= 21 uses close.
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


# === Multi-window log-VWAP differentials (cross-window, sparse) =============


def f25vw_f25_vwap_deviation_vwap_diff_4_12d_base_v076_signal(high, low, close, volume):
    """log(VWAP(4) / VWAP(12)) - very short cross-week VWAP ratio."""
    typ = (high + low + close) / 3.0
    v1 = (typ * volume).rolling(4, min_periods=4).sum() / volume.rolling(4, min_periods=4).sum().replace(0.0, np.nan)
    v2 = (typ * volume).rolling(12, min_periods=12).sum() / volume.rolling(12, min_periods=12).sum().replace(0.0, np.nan)
    return np.log(v1 / v2).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_vwap_diff_30_180d_base_v077_signal(high, low, closeadj, volume):
    """log(VWAP(30) / VWAP(180)) - medium cross-long VWAP ratio."""
    typ = (high + low + closeadj) / 3.0
    v1 = (typ * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    v2 = (typ * volume).rolling(180, min_periods=180).sum() / volume.rolling(180, min_periods=180).sum().replace(0.0, np.nan)
    return np.log(v1 / v2).replace([np.inf, -np.inf], np.nan)


# === VWAP-deviation MAD / interquartile measures ============================


def f25vw_f25_vwap_deviation_vwap_resid_mad_40d_base_v078_signal(high, low, closeadj, volume):
    """Median absolute deviation of (close - VWAP(40)) over 40d normalized by VWAP."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(40, min_periods=40).sum() / volume.rolling(40, min_periods=40).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    med = dev.rolling(40, min_periods=40).median()
    mad = (dev - med).abs().rolling(40, min_periods=40).median()
    return (mad / vwap).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_vwap_resid_iqr_75d_base_v079_signal(high, low, closeadj, volume):
    """Interquartile range of (close - VWAP(75)) over 75d normalized by VWAP."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(75, min_periods=75).sum() / volume.rolling(75, min_periods=75).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    q1 = dev.rolling(75, min_periods=75).quantile(0.25)
    q3 = dev.rolling(75, min_periods=75).quantile(0.75)
    return ((q3 - q1) / vwap).replace([np.inf, -np.inf], np.nan)


# === VWAP-residual median quantile rank =====================================


def f25vw_f25_vwap_deviation_vwap_resid_median_norm_60d_base_v080_signal(high, low, closeadj, volume):
    """median of (close - VWAP(60)) over 60d, normalized by VWAP - residual baseline."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(60, min_periods=60).sum() / volume.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    return (dev.rolling(60, min_periods=60).median() / vwap).replace([np.inf, -np.inf], np.nan)


# === VWAP-anchored Z-score by quantile (not sd) =============================


def f25vw_f25_vwap_deviation_vwap_resid_qrank_30d_base_v081_signal(high, low, closeadj, volume):
    """(close - VWAP(30)) quantile-rank over 30d - non-parametric residual position."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    return (dev.rolling(30, min_periods=30).rank(pct=True) - 0.5).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_vwap_resid_qrank_180d_base_v082_signal(high, low, closeadj, volume):
    """(close - VWAP(150)) quantile-rank over 180d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(150, min_periods=150).sum() / volume.rolling(150, min_periods=150).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    return (dev.rolling(180, min_periods=180).rank(pct=True) - 0.5).replace([np.inf, -np.inf], np.nan)


# === VWAP vs EMA(close, N) ratio (volume-weighting vs time-weighting) =======


def f25vw_f25_vwap_deviation_vwap_ema_diff_15d_base_v083_signal(high, low, close, volume):
    """log(VWAP(15) / EMA(close, 15)) - volume-weighted vs exponentially time-weighted."""
    typ = (high + low + close) / 3.0
    vwap = (typ * volume).rolling(15, min_periods=15).sum() / volume.rolling(15, min_periods=15).sum().replace(0.0, np.nan)
    ema = close.ewm(span=15, adjust=False, min_periods=15).mean()
    return np.log(vwap / ema).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_vwap_ema_diff_100d_base_v084_signal(high, low, closeadj, volume):
    """log(VWAP(100) / EMA(close, 100))."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(100, min_periods=100).sum() / volume.rolling(100, min_periods=100).sum().replace(0.0, np.nan)
    ema = closeadj.ewm(span=100, adjust=False, min_periods=100).mean()
    return np.log(vwap / ema).replace([np.inf, -np.inf], np.nan)


# === Two-VWAP slope correlation =============================================


def f25vw_f25_vwap_deviation_corr_vwap_slopes_60d_base_v085_signal(high, low, closeadj, volume):
    """rolling corr of VWAP(20).diff(5) with VWAP(60).diff(21) over 60d - slope-agree."""
    typ = (high + low + closeadj) / 3.0
    v1 = (typ * volume).rolling(20, min_periods=20).sum() / volume.rolling(20, min_periods=20).sum().replace(0.0, np.nan)
    v2 = (typ * volume).rolling(60, min_periods=60).sum() / volume.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    return v1.diff(5).rolling(60, min_periods=60).corr(v2.diff(21)).replace([np.inf, -np.inf], np.nan)


# === Days-since features ===================================================


def f25vw_f25_vwap_deviation_dayssince_vwap_slope_flip_50d_base_v086_signal(high, low, closeadj, volume):
    """Days since sign(VWAP(50).diff(10)) changed - persistence of VWAP-slope direction."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(50, min_periods=50).sum() / volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    sgn = np.sign(vwap.diff(10))
    out = pd.Series(np.nan, index=sgn.index, dtype=float)
    last = None; prev = np.nan
    for i in range(len(sgn)):
        v = sgn.iat[i]
        if not np.isfinite(v): continue
        if not np.isfinite(prev):
            prev = v; last = i; out.iat[i] = 0.0; continue
        if v != prev: last = i
        prev = v
        out.iat[i] = float(i - last)
    return out.replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_dayssince_vwap_band_break_50d_base_v087_signal(high, low, closeadj, volume):
    """Days since last close-outside-VWAP-2sigma-band event for VWAP(50)."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(50, min_periods=50).sum() / volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    sigma = (typ - vwap).rolling(50, min_periods=50).std().replace(0.0, np.nan)
    dev = closeadj - vwap
    is_outside = (dev.abs() > 2.0 * sigma).astype(float).where(~sigma.isna())
    out = pd.Series(np.nan, index=is_outside.index, dtype=float)
    last = None
    for i in range(len(is_outside)):
        v = is_outside.iat[i]
        if not np.isfinite(v):
            continue
        if v > 0.5:
            last = i
        if last is not None:
            out.iat[i] = float(i - last)
        else:
            out.iat[i] = float(i)  # never seen
    return out.replace([np.inf, -np.inf], np.nan)


# === Range / spread features ===============================================


def f25vw_f25_vwap_deviation_vwap_range_30d_base_v088_signal(high, low, closeadj, volume):
    """(max(VWAP(15), 30d) - min(VWAP(15), 30d)) / VWAP(15) - VWAP-path width."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(15, min_periods=15).sum() / volume.rolling(15, min_periods=15).sum().replace(0.0, np.nan)
    mx = vwap.rolling(30, min_periods=30).max()
    mn = vwap.rolling(30, min_periods=30).min()
    return ((mx - mn) / vwap).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_vwap_range_120d_base_v089_signal(high, low, closeadj, volume):
    """(max - min)/VWAP for VWAP(40) over 120d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(40, min_periods=40).sum() / volume.rolling(40, min_periods=40).sum().replace(0.0, np.nan)
    mx = vwap.rolling(120, min_periods=120).max()
    mn = vwap.rolling(120, min_periods=120).min()
    return ((mx - mn) / vwap).replace([np.inf, -np.inf], np.nan)


# === Trough/peak relative VWAP ratio ========================================


def f25vw_f25_vwap_deviation_close_pos_vs_vwap_range_50d_base_v090_signal(high, low, closeadj, volume):
    """(close - min(VWAP(20),50d)) / (max(VWAP(20),50d) - min(VWAP(20),50d)) - 0.5 - close position in VWAP range."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(20, min_periods=20).sum() / volume.rolling(20, min_periods=20).sum().replace(0.0, np.nan)
    mx = vwap.rolling(50, min_periods=50).max()
    mn = vwap.rolling(50, min_periods=50).min()
    rng = (mx - mn).replace(0.0, np.nan)
    return ((closeadj - mn) / rng - 0.5).replace([np.inf, -np.inf], np.nan)


# === VWAP-deviation rolling sum signed by direction =========================


def f25vw_f25_vwap_deviation_signed_dev_sum_45d_base_v091_signal(high, low, closeadj, volume):
    """sum of sign(close-VWAP(45))*|close-VWAP(45)| / sum |close-VWAP(45)| - signed-magnitude balance."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(45, min_periods=45).sum() / volume.rolling(45, min_periods=45).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    s = dev.rolling(45, min_periods=45).sum()
    a = dev.abs().rolling(45, min_periods=45).sum().replace(0.0, np.nan)
    return (s / a).replace([np.inf, -np.inf], np.nan)


# === Multi-anchor AVWAP ratio ==============================================


def f25vw_f25_vwap_deviation_avwap_high_age_norm_90d_base_v092_signal(high, low, closeadj, volume):
    """Days since rolling 90d high (anchor age for AVWAP-high) / 90."""
    typ = (high + low + closeadj) / 3.0
    out = pd.Series(np.nan, index=typ.index, dtype=float)
    tyv = typ.values
    n = 90
    for i in range(len(typ)):
        if i < n - 1: continue
        s0 = i - n + 1
        w = tyv[s0:i + 1]
        if not np.all(np.isfinite(w)): continue
        a = int(np.argmax(w))
        out.iat[i] = float(n - 1 - a) / float(n)
    return out.replace([np.inf, -np.inf], np.nan)


# === VWAP-residual entropy / dispersion ====================================


def f25vw_f25_vwap_deviation_vwap_resid_above_frac_55d_base_v093_signal(high, low, closeadj, volume):
    """Fraction of last 55 bars where close > VWAP(45). Different window than v074."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(45, min_periods=45).sum() / volume.rolling(45, min_periods=45).sum().replace(0.0, np.nan)
    above = (closeadj > vwap).astype(float).where(~vwap.isna())
    return above.rolling(55, min_periods=55).mean().replace([np.inf, -np.inf], np.nan)


# === VWAP-residual streak max ==============================================


def f25vw_f25_vwap_deviation_max_run_above_vwap_60d_base_v094_signal(high, low, closeadj, volume):
    """Maximum run of consecutive bars closing above VWAP(35) within 60d window."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(35, min_periods=35).sum() / volume.rolling(35, min_periods=35).sum().replace(0.0, np.nan)
    above = (closeadj > vwap).astype(float).where(~vwap.isna()).values
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    n = 60
    for i in range(len(closeadj)):
        if i < n - 1: continue
        window = above[i - n + 1:i + 1]
        if np.any(~np.isfinite(window)): continue
        run = 0; mx = 0
        for v in window:
            if v > 0.5:
                run = run + 1
                if run > mx: mx = run
            else:
                run = 0
        out.iat[i] = float(mx)
    return out.replace([np.inf, -np.inf], np.nan)


# === VWAP cross frequency over different windows ===========================


def f25vw_f25_vwap_deviation_vwap_xover_short_45d_base_v095_signal(high, low, closeadj, volume):
    """Count of close-VWAP(35) crossovers over 45d - shorter version than v052."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(35, min_periods=35).sum() / volume.rolling(35, min_periods=35).sum().replace(0.0, np.nan)
    sgn = np.sign(closeadj - vwap)
    flip = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    return flip.rolling(45, min_periods=45).sum().replace([np.inf, -np.inf], np.nan)


# === Sign-based combinations ===============================================


def f25vw_f25_vwap_deviation_sign_concord_short_long_30d_base_v096_signal(high, low, closeadj, volume):
    """sign(close-VWAP(10)) * sign(close-VWAP(60)) - concordance of short/long VWAP-sides."""
    typ = (high + low + closeadj) / 3.0
    v1 = (typ * volume).rolling(10, min_periods=10).sum() / volume.rolling(10, min_periods=10).sum().replace(0.0, np.nan)
    v2 = (typ * volume).rolling(60, min_periods=60).sum() / volume.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    return (np.sign(closeadj - v1) * np.sign(closeadj - v2)).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_sign_dev_slope_xor_50d_base_v097_signal(high, low, closeadj, volume):
    """sign(close-VWAP(50)) - sign(VWAP(50).diff(10)) - dev vs slope discordance."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(50, min_periods=50).sum() / volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    return (np.sign(closeadj - vwap) - np.sign(vwap.diff(10))).replace([np.inf, -np.inf], np.nan)


# === VWAP slope acceleration ===============================================


def f25vw_f25_vwap_deviation_vwap_jerk_proxy_35d_base_v098_signal(high, low, closeadj, volume):
    """(VWAP(35).diff(5) - VWAP(35).diff(5).shift(5)) / VWAP - jerk proxy (slope of slope)."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(35, min_periods=35).sum() / volume.rolling(35, min_periods=35).sum().replace(0.0, np.nan)
    slope = vwap.diff(5)
    return ((slope - slope.shift(5)) / vwap).replace([np.inf, -np.inf], np.nan)


# === Local-extreme detection vs VWAP =======================================


def f25vw_f25_vwap_deviation_high_minus_vwap_norm_50d_base_v099_signal(high, low, closeadj, volume):
    """(high - VWAP(50)) / sigma - intra-bar upside extent vs VWAP."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(50, min_periods=50).sum() / volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    sigma = (typ - vwap).rolling(50, min_periods=50).std().replace(0.0, np.nan)
    return ((high - vwap) / sigma).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_hl_range_vs_vwap_band_50d_base_v100_signal(high, low, closeadj, volume):
    """(high - low) / sigma_vwap(50) - intraday-range scaled by VWAP-band width."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(50, min_periods=50).sum() / volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    sigma = (typ - vwap).rolling(50, min_periods=50).std().replace(0.0, np.nan)
    return ((high - low) / sigma).replace([np.inf, -np.inf], np.nan)


# === Recent VWAP-crossing momentum =========================================


def f25vw_f25_vwap_deviation_post_cross_return_30d_base_v101_signal(high, low, closeadj, volume):
    """Rolling 30d mean of sign(close-VWAP(20)).shift(1) * return - signed-return when above/below VWAP."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(20, min_periods=20).sum() / volume.rolling(20, min_periods=20).sum().replace(0.0, np.nan)
    sgn = np.sign(closeadj - vwap); ret = closeadj.pct_change()
    return (sgn.shift(1) * ret).rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


# === VWAP gap normalized by volume ==========================================


def f25vw_f25_vwap_deviation_vwap_gap_volnorm_25d_base_v102_signal(high, low, close, volume):
    """(close - VWAP(25)) * volume_mean / VWAP(25) - volume-weighted gap magnitude."""
    typ = (high + low + close) / 3.0
    vwap = (typ * volume).rolling(25, min_periods=25).sum() / volume.rolling(25, min_periods=25).sum().replace(0.0, np.nan)
    vol_mean = volume.rolling(25, min_periods=25).mean().replace(0.0, np.nan)
    return ((close - vwap) / vwap * (volume / vol_mean)).replace([np.inf, -np.inf], np.nan)


# === VWAP up-vs-down volume bias ===========================================


def f25vw_f25_vwap_deviation_vwap_signed_vol_25d_base_v103_signal(high, low, close, volume):
    """sum(sign(close-VWAP)*volume) / sum(volume) over 25d - signed-volume balance vs VWAP."""
    typ = (high + low + close) / 3.0
    vwap = (typ * volume).rolling(25, min_periods=25).sum() / volume.rolling(25, min_periods=25).sum().replace(0.0, np.nan)
    sgn = np.sign(close - vwap)
    signed_vol = (sgn * volume).rolling(25, min_periods=25).sum()
    total = volume.rolling(25, min_periods=25).sum().replace(0.0, np.nan)
    return (signed_vol / total).replace([np.inf, -np.inf], np.nan)


# === Position relative to AVWAP-low and AVWAP-high simultaneously ==========


def f25vw_f25_vwap_deviation_avwap_channel_pos_75d_base_v104_signal(high, low, closeadj, volume):
    """(close - AVWAP_low) / (AVWAP_high - AVWAP_low) - 0.5 over 75d anchor."""
    typ = (high + low + closeadj) / 3.0
    al = pd.Series(np.nan, index=typ.index, dtype=float)
    ah = pd.Series(np.nan, index=typ.index, dtype=float)
    tv = (typ * volume).values; vv = volume.values; tyv = typ.values
    n = 75
    for i in range(len(typ)):
        if i < n - 1: continue
        s0 = i - n + 1
        w = tyv[s0:i + 1]
        if not np.all(np.isfinite(w)): continue
        a_lo = s0 + int(np.argmin(w))
        a_hi = s0 + int(np.argmax(w))
        nlo = float(np.nansum(tv[a_lo:i + 1])); dlo = float(np.nansum(vv[a_lo:i + 1]))
        nhi = float(np.nansum(tv[a_hi:i + 1])); dhi = float(np.nansum(vv[a_hi:i + 1]))
        if dlo != 0.0 and dhi != 0.0:
            al.iat[i] = nlo / dlo
            ah.iat[i] = nhi / dhi
    rng = (ah - al)
    return ((closeadj - al) / rng - 0.5).replace([np.inf, -np.inf], np.nan)


# === VWAP-bandwidth dynamics ===============================================


def f25vw_f25_vwap_deviation_vwap_band_width_diff_45d_base_v105_signal(high, low, closeadj, volume):
    """sigma / VWAP for VWAP(45) - VWAP(150) - difference of band widths."""
    typ = (high + low + closeadj) / 3.0
    v1 = (typ * volume).rolling(45, min_periods=45).sum() / volume.rolling(45, min_periods=45).sum().replace(0.0, np.nan)
    v2 = (typ * volume).rolling(150, min_periods=150).sum() / volume.rolling(150, min_periods=150).sum().replace(0.0, np.nan)
    s1 = (typ - v1).rolling(45, min_periods=45).std()
    s2 = (typ - v2).rolling(150, min_periods=150).std()
    return ((s1 / v1) - (s2 / v2)).replace([np.inf, -np.inf], np.nan)


# === Position vs VWAP in bear / bull regimes ===============================


def f25vw_f25_vwap_deviation_vwap_resid_when_up_60d_base_v106_signal(high, low, closeadj, volume):
    """mean of (close-VWAP(30))/VWAP when VWAP-slope>0, else NaN, smoothed over 60d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    slope = vwap.diff(10)
    dev = (closeadj - vwap) / vwap
    masked = dev.where(slope > 0)
    return masked.rolling(60, min_periods=20).mean().replace([np.inf, -np.inf], np.nan)


# === VWAP-residual mean reversion speed ====================================


def f25vw_f25_vwap_deviation_vwap_resid_ar1_60d_base_v107_signal(high, low, closeadj, volume):
    """AR(1) coefficient (regression slope) of (close-VWAP(45)) on lag1 over 60d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(45, min_periods=45).sum() / volume.rolling(45, min_periods=45).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    lag1 = dev.shift(1)
    cov = dev.rolling(60, min_periods=60).cov(lag1)
    var = lag1.rolling(60, min_periods=60).var().replace(0.0, np.nan)
    return (cov / var).replace([np.inf, -np.inf], np.nan)


# === VWAP-residual entropy via sign run-length =============================


def f25vw_f25_vwap_deviation_sign_change_density_120d_base_v108_signal(high, low, closeadj, volume):
    """Fraction of 120d bars where sign(close-VWAP(40)) flipped from prior bar."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(40, min_periods=40).sum() / volume.rolling(40, min_periods=40).sum().replace(0.0, np.nan)
    sgn = np.sign(closeadj - vwap)
    flip = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
    return flip.rolling(120, min_periods=120).mean().replace([np.inf, -np.inf], np.nan)


# === Anchor-distance ratio =================================================


def f25vw_f25_vwap_deviation_dist_avwap_low_vs_high_60d_base_v109_signal(high, low, closeadj, volume):
    """|close - AVWAP_low(60)| / |close - AVWAP_high(60)| - anchor-distance balance."""
    typ = (high + low + closeadj) / 3.0
    al = pd.Series(np.nan, index=typ.index, dtype=float)
    ah = pd.Series(np.nan, index=typ.index, dtype=float)
    tv = (typ * volume).values; vv = volume.values; tyv = typ.values
    n = 60
    for i in range(len(typ)):
        if i < n - 1: continue
        s0 = i - n + 1
        w = tyv[s0:i + 1]
        if not np.all(np.isfinite(w)): continue
        a_lo = s0 + int(np.argmin(w))
        a_hi = s0 + int(np.argmax(w))
        nlo = float(np.nansum(tv[a_lo:i + 1])); dlo = float(np.nansum(vv[a_lo:i + 1]))
        nhi = float(np.nansum(tv[a_hi:i + 1])); dhi = float(np.nansum(vv[a_hi:i + 1]))
        if dlo != 0.0 and dhi != 0.0:
            al.iat[i] = nlo / dlo
            ah.iat[i] = nhi / dhi
    return ((closeadj - al).abs() / (closeadj - ah).abs().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Rolling beta of close on VWAP =========================================


def f25vw_f25_vwap_deviation_beta_close_vwap_45d_base_v110_signal(high, low, closeadj, volume):
    """Rolling slope of close.diff(1) regressed on VWAP(20).diff(1) over 45d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(20, min_periods=20).sum() / volume.rolling(20, min_periods=20).sum().replace(0.0, np.nan)
    rc = closeadj.diff(1)
    rv = vwap.diff(1)
    cov = rc.rolling(45, min_periods=45).cov(rv)
    var = rv.rolling(45, min_periods=45).var().replace(0.0, np.nan)
    return (cov / var).replace([np.inf, -np.inf], np.nan)


# === VWAP-trend strength (slope / vol) =====================================


def f25vw_f25_vwap_deviation_vwap_trend_strength_60d_base_v111_signal(high, low, closeadj, volume):
    """VWAP(60).diff(21) / sigma_vwap(60) - VWAP-slope normalized by VWAP-vol."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(60, min_periods=60).sum() / volume.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    sigma = (typ - vwap).rolling(60, min_periods=60).std().replace(0.0, np.nan)
    return (vwap.diff(21) / sigma).replace([np.inf, -np.inf], np.nan)


# === VWAP-deviation rolling MAX/MIN absolute ===============================


def f25vw_f25_vwap_deviation_max_abs_dev_30d_base_v112_signal(high, low, closeadj, volume):
    """max(|close - VWAP(30)|, 30d) / VWAP - largest recent deviation magnitude."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    dev = (closeadj - vwap).abs()
    return (dev.rolling(30, min_periods=30).max() / vwap).replace([np.inf, -np.inf], np.nan)


# === VWAP signal: log-MAD-z =================================================


def f25vw_f25_vwap_deviation_vwap_resid_mad_z_70d_base_v113_signal(high, low, closeadj, volume):
    """(close - VWAP(70) - median) / MAD over 70d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(70, min_periods=70).sum() / volume.rolling(70, min_periods=70).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    med = dev.rolling(70, min_periods=70).median()
    mad = (dev - med).abs().rolling(70, min_periods=70).median().replace(0.0, np.nan)
    return ((dev - med) / mad).replace([np.inf, -np.inf], np.nan)


# === VWAP slope-band z =====================================================


def f25vw_f25_vwap_deviation_vwap_slope_z_70d_base_v114_signal(high, low, closeadj, volume):
    """z-score of VWAP(40).diff(21) over 70d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(40, min_periods=40).sum() / volume.rolling(40, min_periods=40).sum().replace(0.0, np.nan)
    slope = vwap.diff(21)
    mu = slope.rolling(70, min_periods=70).mean()
    sd = slope.rolling(70, min_periods=70).std().replace(0.0, np.nan)
    return ((slope - mu) / sd).replace([np.inf, -np.inf], np.nan)


# === VWAP slope sign vs price-trend agreement =============================


def f25vw_f25_vwap_deviation_vwap_close_slope_agree_50d_base_v115_signal(high, low, closeadj, volume):
    """sign(VWAP(50).diff(21)) * sign(close.diff(21)) - VWAP vs close slope concordance."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(50, min_periods=50).sum() / volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    return (np.sign(vwap.diff(21)) * np.sign(closeadj.diff(21))).replace([np.inf, -np.inf], np.nan)


# === Logistic of VWAP-gap-vs-band ratio ====================================


def f25vw_f25_vwap_deviation_vwap_band_pos_rolling_zscore_35d_base_v116_signal(high, low, closeadj, volume):
    """z-score of normalized band-position over 120d - regime-relative band-position."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(35, min_periods=35).sum() / volume.rolling(35, min_periods=35).sum().replace(0.0, np.nan)
    sigma = (typ - vwap).rolling(35, min_periods=35).std().replace(0.0, np.nan)
    pos = (closeadj - vwap) / sigma
    mu = pos.rolling(120, min_periods=120).mean()
    sd = pos.rolling(120, min_periods=120).std().replace(0.0, np.nan)
    return ((pos - mu) / sd).replace([np.inf, -np.inf], np.nan)


# === VWAP-low residual scaled by close =====================================


def f25vw_f25_vwap_deviation_avwap_low_resid_z_60d_base_v117_signal(high, low, closeadj, volume):
    """z-score of log(close / AVWAP_low(60)) over trailing 60d."""
    typ = (high + low + closeadj) / 3.0
    avw = pd.Series(np.nan, index=typ.index, dtype=float)
    tv = (typ * volume).values; vv = volume.values; tyv = typ.values
    n = 60
    for i in range(len(typ)):
        if i < n - 1: continue
        s0 = i - n + 1
        w = tyv[s0:i + 1]
        if not np.all(np.isfinite(w)): continue
        a = s0 + int(np.argmin(w))
        num = float(np.nansum(tv[a:i + 1]))
        den = float(np.nansum(vv[a:i + 1]))
        if den != 0.0:
            avw.iat[i] = num / den
    r = np.log(closeadj / avw)
    mu = r.rolling(60, min_periods=60).mean()
    sd = r.rolling(60, min_periods=60).std().replace(0.0, np.nan)
    return ((r - mu) / sd).replace([np.inf, -np.inf], np.nan)


# === Anchored-VWAP curvature ===============================================


def f25vw_f25_vwap_deviation_avwap_high_curv_55d_base_v118_signal(high, low, closeadj, volume):
    """AVWAP_high(55) - 2*AVWAP_high(55).shift(10) + AVWAP_high(55).shift(20), normalized."""
    typ = (high + low + closeadj) / 3.0
    avw = pd.Series(np.nan, index=typ.index, dtype=float)
    tv = (typ * volume).values; vv = volume.values; tyv = typ.values
    n = 55
    for i in range(len(typ)):
        if i < n - 1: continue
        s0 = i - n + 1
        w = tyv[s0:i + 1]
        if not np.all(np.isfinite(w)): continue
        a = s0 + int(np.argmax(w))
        num = float(np.nansum(tv[a:i + 1]))
        den = float(np.nansum(vv[a:i + 1]))
        if den != 0.0:
            avw.iat[i] = num / den
    return ((avw - 2.0 * avw.shift(10) + avw.shift(20)) / avw).replace([np.inf, -np.inf], np.nan)


# === Frequency of close > VWAP across multiple windows =====================


def f25vw_f25_vwap_deviation_avg_above_kvwap_50d_base_v119_signal(high, low, closeadj, volume):
    """Mean over (close>VWAP(n)) for n in {15,30,60,120} - cross-window aboveness ratio."""
    typ = (high + low + closeadj) / 3.0
    sigs = []
    for n in (15, 30, 60, 120):
        vwap = (typ * volume).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
        sigs.append((closeadj > vwap).astype(float).where(~vwap.isna()))
    mat = pd.concat(sigs, axis=1)
    return mat.mean(axis=1).replace([np.inf, -np.inf], np.nan)


# === VWAP-residual rolling skewness ========================================


def f25vw_f25_vwap_deviation_vwap_resid_skew_100d_base_v120_signal(high, low, closeadj, volume):
    """Rolling skewness of (close - VWAP(35)) over 100d - residual asymmetry."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(35, min_periods=35).sum() / volume.rolling(35, min_periods=35).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    return dev.rolling(100, min_periods=100).skew().replace([np.inf, -np.inf], np.nan)


# === Multi-window VWAP dispersion ==========================================


def f25vw_f25_vwap_deviation_multi_vwap_dispersion_45d_base_v121_signal(high, low, closeadj, volume):
    """std across VWAP(15,30,60,90,120) / mean - 5-VWAP ribbon dispersion."""
    typ = (high + low + closeadj) / 3.0
    series = []
    for n in (15, 30, 60, 90, 120):
        v = (typ * volume).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
        series.append(v)
    mat = pd.concat(series, axis=1)
    return (mat.std(axis=1) / mat.mean(axis=1)).replace([np.inf, -np.inf], np.nan)


# === Multi-VWAP ordering count =============================================


def f25vw_f25_vwap_deviation_multi_vwap_descord_count_base_v122_signal(high, low, closeadj, volume):
    """For VWAPs(8,16,32,64,128), count of pairs in descending order. Ribbon-ordering count."""
    typ = (high + low + closeadj) / 3.0
    series = []
    for n in (8, 16, 32, 64, 128):
        v = (typ * volume).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
        series.append(v)
    cnt = pd.Series(0.0, index=typ.index)
    mask = ~series[0].isna()
    for i in range(len(series)):
        for j in range(i + 1, len(series)):
            cnt = cnt + (series[i] < series[j]).astype(float)
            mask = mask & ~series[i].isna() & ~series[j].isna()
    return cnt.where(mask).replace([np.inf, -np.inf], np.nan)


# === Reversion-rate near VWAP ==============================================


def f25vw_f25_vwap_deviation_reversion_rate_vwap_40d_base_v123_signal(high, low, closeadj, volume):
    """Mean of -sign(dev.shift(1)) * dev.diff(1) / sigma over 40d - reversion strength."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(40, min_periods=40).sum() / volume.rolling(40, min_periods=40).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    sigma = dev.rolling(40, min_periods=40).std().replace(0.0, np.nan)
    react = (-np.sign(dev.shift(1)) * dev.diff(1)) / sigma
    return react.rolling(40, min_periods=40).mean().replace([np.inf, -np.inf], np.nan)


# === Hurst-style R/S of VWAP residual ======================================


def f25vw_f25_vwap_deviation_resid_rs_70d_base_v124_signal(high, low, closeadj, volume):
    """R/S-style: range(cumsum(dev - mean)) / std(dev) for VWAP(30) over 70d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    dev = closeadj - vwap

    def _rs(x):
        if not np.all(np.isfinite(x)): return np.nan
        m = x.mean()
        z = np.cumsum(x - m)
        r = z.max() - z.min()
        s = x.std(ddof=0)
        if s == 0 or not np.isfinite(r / s) or r / s <= 0: return np.nan
        return float(np.log(r / s) / np.log(len(x)))

    return dev.rolling(70, min_periods=70).apply(_rs, raw=True).replace([np.inf, -np.inf], np.nan)


# === Variance ratio of VWAP-deviation ======================================


def f25vw_f25_vwap_deviation_resid_var_ratio_60d_base_v125_signal(high, low, closeadj, volume):
    """var(dev.diff(5)) / (5*var(dev.diff(1))) - variance ratio of VWAP residual."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(35, min_periods=35).sum() / volume.rolling(35, min_periods=35).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    v5 = dev.diff(5).rolling(60, min_periods=60).var()
    v1 = dev.diff(1).rolling(60, min_periods=60).var().replace(0.0, np.nan)
    return (v5 / (5.0 * v1)).replace([np.inf, -np.inf], np.nan)


# === VWAP-deviation cyclical-test (autocorr ratio) ========================


def f25vw_f25_vwap_deviation_resid_autocorr_ratio_80d_base_v126_signal(high, low, closeadj, volume):
    """autocorr(dev, lag5) - autocorr(dev, lag21) - short vs medium memory."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(40, min_periods=40).sum() / volume.rolling(40, min_periods=40).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    a5 = dev.rolling(80, min_periods=80).corr(dev.shift(5))
    a21 = dev.rolling(80, min_periods=80).corr(dev.shift(21))
    return (a5 - a21).replace([np.inf, -np.inf], np.nan)


# === VWAP-deviation skewness sign ==========================================


def f25vw_f25_vwap_deviation_sign_resid_skew_50d_base_v127_signal(high, low, closeadj, volume):
    """sign of skew((close-VWAP(50)), 50d) - discrete asymmetry indicator."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(50, min_periods=50).sum() / volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    return np.sign(dev.rolling(50, min_periods=50).skew()).replace([np.inf, -np.inf], np.nan)


# === VWAP-deviation absolute mean ==========================================


def f25vw_f25_vwap_deviation_mean_abs_resid_norm_25d_base_v128_signal(high, low, close, volume):
    """mean(|close - VWAP(25)|) / VWAP(25) over 25d - VWAP-residual scale."""
    typ = (high + low + close) / 3.0
    vwap = (typ * volume).rolling(25, min_periods=25).sum() / volume.rolling(25, min_periods=25).sum().replace(0.0, np.nan)
    return ((close - vwap).abs().rolling(25, min_periods=25).mean() / vwap).replace([np.inf, -np.inf], np.nan)


# === High vs VWAP percentile rank ==========================================


def f25vw_f25_vwap_deviation_high_vs_vwap_rank_60d_base_v129_signal(high, low, closeadj, volume):
    """Percentile rank of (high - VWAP(60)) over 60d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(60, min_periods=60).sum() / volume.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    return (high - vwap).rolling(60, min_periods=60).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f25vw_f25_vwap_deviation_hl_vwap_rank_diff_60d_base_v130_signal(high, low, closeadj, volume):
    """rank(high-VWAP(60)) - rank(low-VWAP(60)) over 60d - bar-width-vs-VWAP rank delta."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(60, min_periods=60).sum() / volume.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    rh = (high - vwap).rolling(60, min_periods=60).rank(pct=True)
    rl = (low - vwap).rolling(60, min_periods=60).rank(pct=True)
    return (rh - rl).replace([np.inf, -np.inf], np.nan)


# === Bar-by-bar VWAP-side switching probability ============================


def f25vw_f25_vwap_deviation_vwap_side_prob_80d_base_v131_signal(high, low, closeadj, volume):
    """rolling mean of sign(close-VWAP(25))*sign(close.shift(1)-VWAP(25).shift(1)) over 80d.
    1 means same side persistently, -1 means flipping."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(25, min_periods=25).sum() / volume.rolling(25, min_periods=25).sum().replace(0.0, np.nan)
    s = np.sign(closeadj - vwap)
    return (s * s.shift(1)).rolling(80, min_periods=80).mean().replace([np.inf, -np.inf], np.nan)


# === VWAP-deviation kurt ===================================================


def f25vw_f25_vwap_deviation_resid_kurt_120d_base_v132_signal(high, low, closeadj, volume):
    """Rolling kurt of (close - VWAP(25)) over 120d - tail-heaviness of short-VWAP residual."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(25, min_periods=25).sum() / volume.rolling(25, min_periods=25).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    return dev.rolling(120, min_periods=120).kurt().replace([np.inf, -np.inf], np.nan)


# === Composite VWAP-state =================================================


def f25vw_f25_vwap_deviation_composite_state_50d_base_v133_signal(high, low, closeadj, volume):
    """sign(close-VWAP(50)) + 0.5*sign(VWAP(50).diff(10)) - composite VWAP regime score."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(50, min_periods=50).sum() / volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    return (np.sign(closeadj - vwap) + 0.5 * np.sign(vwap.diff(10))).replace([np.inf, -np.inf], np.nan)


# === VWAP-deviation rolling regression R^2 vs time =========================


def f25vw_f25_vwap_deviation_resid_time_rsq_40d_base_v134_signal(high, low, closeadj, volume):
    """R^2 of regressing (close-VWAP(40)) on time index over 40d - trend in residual."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(40, min_periods=40).sum() / volume.rolling(40, min_periods=40).sum().replace(0.0, np.nan)
    dev = closeadj - vwap

    def _r2(x):
        if not np.all(np.isfinite(x)): return np.nan
        t = np.arange(len(x), dtype=float)
        tm = t.mean(); xm = x.mean()
        cov = np.mean((t - tm) * (x - xm))
        vt = np.mean((t - tm) ** 2); vx = np.mean((x - xm) ** 2)
        if vt == 0 or vx == 0: return np.nan
        return float(cov ** 2 / (vt * vx))

    return dev.rolling(40, min_periods=40).apply(_r2, raw=True).replace([np.inf, -np.inf], np.nan)


# === Hour-glass / convergence rate of long & short VWAP ===================


def f25vw_f25_vwap_deviation_vwap_convergence_rate_60d_base_v135_signal(high, low, closeadj, volume):
    """diff of |VWAP(20) - VWAP(60)| over 21d - rate of VWAP-window convergence."""
    typ = (high + low + closeadj) / 3.0
    v1 = (typ * volume).rolling(20, min_periods=20).sum() / volume.rolling(20, min_periods=20).sum().replace(0.0, np.nan)
    v2 = (typ * volume).rolling(60, min_periods=60).sum() / volume.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    spread = (v1 - v2).abs()
    return spread.diff(21).replace([np.inf, -np.inf], np.nan)


# === Days-since high-water vs VWAP =========================================


def f25vw_f25_vwap_deviation_dayssince_above_vwap_band_60d_base_v136_signal(high, low, closeadj, volume):
    """Days since last close>VWAP(50)+1sigma."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(50, min_periods=50).sum() / volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    sigma = (typ - vwap).rolling(50, min_periods=50).std().replace(0.0, np.nan)
    cond = (closeadj > (vwap + sigma)).astype(float).where(~sigma.isna())
    out = pd.Series(np.nan, index=cond.index, dtype=float)
    last = None
    for i in range(len(cond)):
        v = cond.iat[i]
        if not np.isfinite(v): continue
        if v > 0.5: last = i
        if last is not None:
            out.iat[i] = float(i - last)
        else:
            out.iat[i] = float(i)
    return out.replace([np.inf, -np.inf], np.nan)


# === VWAP-residual rolling efficiency ======================================


def f25vw_f25_vwap_deviation_resid_efficiency_50d_base_v137_signal(high, low, closeadj, volume):
    """|dev[t] - dev[t-50]| / sum(|dev.diff(1)|, 50) over (close-VWAP(35)) - path efficiency."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(35, min_periods=35).sum() / volume.rolling(35, min_periods=35).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    direction = (dev - dev.shift(50)).abs()
    pathlen = dev.diff(1).abs().rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    return (direction / pathlen).replace([np.inf, -np.inf], np.nan)


# === Range of (close - VWAP) ===============================================


def f25vw_f25_vwap_deviation_dev_quantile_spread_60d_base_v138_signal(high, low, closeadj, volume):
    """(q90 - q10) of (close-VWAP(45)) over 60d normalized by VWAP."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(45, min_periods=45).sum() / volume.rolling(45, min_periods=45).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    q90 = dev.rolling(60, min_periods=60).quantile(0.9)
    q10 = dev.rolling(60, min_periods=60).quantile(0.1)
    return ((q90 - q10) / vwap).replace([np.inf, -np.inf], np.nan)


# === VWAP-band crossing speed ==============================================


def f25vw_f25_vwap_deviation_band_xover_count_90d_base_v139_signal(high, low, closeadj, volume):
    """Count of times close enters/exits VWAP(40)+-1sigma band in 90d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(40, min_periods=40).sum() / volume.rolling(40, min_periods=40).sum().replace(0.0, np.nan)
    sigma = (typ - vwap).rolling(40, min_periods=40).std().replace(0.0, np.nan)
    state = ((closeadj > vwap + sigma).astype(float) - (closeadj < vwap - sigma).astype(float)).where(~sigma.isna())
    change = (state != state.shift(1)).astype(float).where(~state.isna() & ~state.shift(1).isna())
    return change.rolling(90, min_periods=90).sum().replace([np.inf, -np.inf], np.nan)


# === Lag-1 VWAP-direction agreement ========================================


def f25vw_f25_vwap_deviation_vwap_dir_persistence_45d_base_v140_signal(high, low, closeadj, volume):
    """mean of sign(VWAP(30).diff(1)) * sign(VWAP(30).diff(1).shift(1)) over 45d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    d = np.sign(vwap.diff(1))
    return (d * d.shift(1)).rolling(45, min_periods=45).mean().replace([np.inf, -np.inf], np.nan)


# === Short-window VWAP raw distance (sparse: only here) ====================


def f25vw_f25_vwap_deviation_logclose_vwap_3d_base_v141_signal(high, low, close, volume):
    """log(close / VWAP(3)) - very short-window VWAP distance (intra-week reference)."""
    typ = (high + low + close) / 3.0
    vwap = (typ * volume).rolling(3, min_periods=3).sum() / volume.rolling(3, min_periods=3).sum().replace(0.0, np.nan)
    return np.log(close / vwap).replace([np.inf, -np.inf], np.nan)


# === Volume-tilt of VWAP residual ===========================================


def f25vw_f25_vwap_deviation_resid_vol_corr_60d_base_v142_signal(high, low, closeadj, volume):
    """Rolling corr of (close-VWAP(30)) with volume over 60d - high-volume regime tilt."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    return dev.rolling(60, min_periods=60).corr(volume).replace([np.inf, -np.inf], np.nan)


# === VWAP-derived ratio compared to ATR-distance ===========================


def f25vw_f25_vwap_deviation_band_width_atr_ratio_40d_base_v143_signal(high, low, closeadj, volume):
    """sigma_VWAP(40) / ATR(40) - VWAP-band-width vs ATR ratio."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(40, min_periods=40).sum() / volume.rolling(40, min_periods=40).sum().replace(0.0, np.nan)
    sigma = (typ - vwap).rolling(40, min_periods=40).std()
    pc = closeadj.shift(1)
    tr = pd.concat([(high - low), (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 40.0, adjust=False, min_periods=40).mean().replace(0.0, np.nan)
    return (sigma / atr).replace([np.inf, -np.inf], np.nan)


# === Range vs VWAP-band ratio ==============================================


def f25vw_f25_vwap_deviation_intraday_range_vs_vwap_sigma_30d_base_v144_signal(high, low, closeadj, volume):
    """(high-low) mean / sigma_VWAP(30) over 30d - intraday range vs VWAP-band width."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    sigma = (typ - vwap).rolling(30, min_periods=30).std().replace(0.0, np.nan)
    rng = (high - low).rolling(30, min_periods=30).mean()
    return (rng / sigma).replace([np.inf, -np.inf], np.nan)


# === Sign(close-VWAP) cluster strength =====================================


def f25vw_f25_vwap_deviation_dominant_side_strength_90d_base_v145_signal(high, low, closeadj, volume):
    """max(|sum(above)/n|, |sum(below)/n|) - which VWAP-side dominates more in 90d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(50, min_periods=50).sum() / volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    above = (closeadj > vwap).astype(float).where(~vwap.isna()).rolling(90, min_periods=90).mean()
    return (2.0 * above - 1.0).abs().replace([np.inf, -np.inf], np.nan)


# === VWAP up-day / down-day count ratio ====================================


def f25vw_f25_vwap_deviation_vwap_up_day_ratio_70d_base_v146_signal(high, low, closeadj, volume):
    """fraction of bars in 70d with VWAP(25).diff(1) > 0."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(25, min_periods=25).sum() / volume.rolling(25, min_periods=25).sum().replace(0.0, np.nan)
    up = (vwap.diff(1) > 0).astype(float).where(~vwap.diff(1).isna())
    return up.rolling(70, min_periods=70).mean().replace([np.inf, -np.inf], np.nan)


# === VWAP-velocity correlation with price-velocity =========================


def f25vw_f25_vwap_deviation_vwap_lead_corr_55d_base_v147_signal(high, low, closeadj, volume):
    """Rolling corr of VWAP(30).diff(5) leading close.diff(5).shift(-5) over 55d -
    does VWAP-slope predict next-week price-slope?"""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(30, min_periods=30).sum() / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    vs = vwap.diff(5)
    cs = closeadj.diff(5).shift(-5)
    return vs.rolling(55, min_periods=55).corr(cs).replace([np.inf, -np.inf], np.nan)


# === VWAP-deviation rolling tau =============================================


def f25vw_f25_vwap_deviation_resid_tail_count_45d_base_v148_signal(high, low, closeadj, volume):
    """Count of days where (close-VWAP(45)) exceeds 1.5*sigma in trailing 45d."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(45, min_periods=45).sum() / volume.rolling(45, min_periods=45).sum().replace(0.0, np.nan)
    sigma = (typ - vwap).rolling(45, min_periods=45).std().replace(0.0, np.nan)
    dev = closeadj - vwap
    tail = (dev.abs() > 1.5 * sigma).astype(float).where(~sigma.isna())
    return tail.rolling(45, min_periods=45).sum().replace([np.inf, -np.inf], np.nan)


# === VWAP deviation half-life proxy ========================================


def f25vw_f25_vwap_deviation_resid_halflife_proxy_50d_base_v149_signal(high, low, closeadj, volume):
    """-log(2) / log(|AR(1) coef|) clipped - half-life proxy of VWAP residual mean-reversion."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(40, min_periods=40).sum() / volume.rolling(40, min_periods=40).sum().replace(0.0, np.nan)
    dev = closeadj - vwap
    lag1 = dev.shift(1)
    cov = dev.rolling(50, min_periods=50).cov(lag1)
    var = lag1.rolling(50, min_periods=50).var().replace(0.0, np.nan)
    ar1 = (cov / var).clip(-0.999, 0.999).abs().replace(0.0, np.nan)
    return (-np.log(2.0) / np.log(ar1)).replace([np.inf, -np.inf], np.nan)


# === VWAP residual sign sum ratio ==========================================


def f25vw_f25_vwap_deviation_resid_sign_volsum_50d_base_v150_signal(high, low, closeadj, volume):
    """sum(sign(close-VWAP(25))*volume, 50d) / sum(volume, 50d) for closeadj long window."""
    typ = (high + low + closeadj) / 3.0
    vwap = (typ * volume).rolling(25, min_periods=25).sum() / volume.rolling(25, min_periods=25).sum().replace(0.0, np.nan)
    sgn = np.sign(closeadj - vwap)
    sv = (sgn * volume).rolling(50, min_periods=50).sum()
    tv = volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    return (sv / tv).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f25_vwap_deviation_base_076_150_REGISTRY = {
    "f25vw_f25_vwap_deviation_vwap_diff_4_12d_base_v076_signal": {"inputs": ["high", "low", "close", "volume"], "func": f25vw_f25_vwap_deviation_vwap_diff_4_12d_base_v076_signal},
    "f25vw_f25_vwap_deviation_vwap_diff_30_180d_base_v077_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_diff_30_180d_base_v077_signal},
    "f25vw_f25_vwap_deviation_vwap_resid_mad_40d_base_v078_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_resid_mad_40d_base_v078_signal},
    "f25vw_f25_vwap_deviation_vwap_resid_iqr_75d_base_v079_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_resid_iqr_75d_base_v079_signal},
    "f25vw_f25_vwap_deviation_vwap_resid_median_norm_60d_base_v080_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_resid_median_norm_60d_base_v080_signal},
    "f25vw_f25_vwap_deviation_vwap_resid_qrank_30d_base_v081_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_resid_qrank_30d_base_v081_signal},
    "f25vw_f25_vwap_deviation_vwap_resid_qrank_180d_base_v082_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_resid_qrank_180d_base_v082_signal},
    "f25vw_f25_vwap_deviation_vwap_ema_diff_15d_base_v083_signal": {"inputs": ["high", "low", "close", "volume"], "func": f25vw_f25_vwap_deviation_vwap_ema_diff_15d_base_v083_signal},
    "f25vw_f25_vwap_deviation_vwap_ema_diff_100d_base_v084_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_ema_diff_100d_base_v084_signal},
    "f25vw_f25_vwap_deviation_corr_vwap_slopes_60d_base_v085_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_corr_vwap_slopes_60d_base_v085_signal},
    "f25vw_f25_vwap_deviation_dayssince_vwap_slope_flip_50d_base_v086_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_dayssince_vwap_slope_flip_50d_base_v086_signal},
    "f25vw_f25_vwap_deviation_dayssince_vwap_band_break_50d_base_v087_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_dayssince_vwap_band_break_50d_base_v087_signal},
    "f25vw_f25_vwap_deviation_vwap_range_30d_base_v088_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_range_30d_base_v088_signal},
    "f25vw_f25_vwap_deviation_vwap_range_120d_base_v089_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_range_120d_base_v089_signal},
    "f25vw_f25_vwap_deviation_close_pos_vs_vwap_range_50d_base_v090_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_close_pos_vs_vwap_range_50d_base_v090_signal},
    "f25vw_f25_vwap_deviation_signed_dev_sum_45d_base_v091_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_signed_dev_sum_45d_base_v091_signal},
    "f25vw_f25_vwap_deviation_avwap_high_age_norm_90d_base_v092_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_avwap_high_age_norm_90d_base_v092_signal},
    "f25vw_f25_vwap_deviation_vwap_resid_above_frac_55d_base_v093_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_resid_above_frac_55d_base_v093_signal},
    "f25vw_f25_vwap_deviation_max_run_above_vwap_60d_base_v094_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_max_run_above_vwap_60d_base_v094_signal},
    "f25vw_f25_vwap_deviation_vwap_xover_short_45d_base_v095_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_xover_short_45d_base_v095_signal},
    "f25vw_f25_vwap_deviation_sign_concord_short_long_30d_base_v096_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_sign_concord_short_long_30d_base_v096_signal},
    "f25vw_f25_vwap_deviation_sign_dev_slope_xor_50d_base_v097_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_sign_dev_slope_xor_50d_base_v097_signal},
    "f25vw_f25_vwap_deviation_vwap_jerk_proxy_35d_base_v098_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_jerk_proxy_35d_base_v098_signal},
    "f25vw_f25_vwap_deviation_high_minus_vwap_norm_50d_base_v099_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_high_minus_vwap_norm_50d_base_v099_signal},
    "f25vw_f25_vwap_deviation_hl_range_vs_vwap_band_50d_base_v100_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_hl_range_vs_vwap_band_50d_base_v100_signal},
    "f25vw_f25_vwap_deviation_post_cross_return_30d_base_v101_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_post_cross_return_30d_base_v101_signal},
    "f25vw_f25_vwap_deviation_vwap_gap_volnorm_25d_base_v102_signal": {"inputs": ["high", "low", "close", "volume"], "func": f25vw_f25_vwap_deviation_vwap_gap_volnorm_25d_base_v102_signal},
    "f25vw_f25_vwap_deviation_vwap_signed_vol_25d_base_v103_signal": {"inputs": ["high", "low", "close", "volume"], "func": f25vw_f25_vwap_deviation_vwap_signed_vol_25d_base_v103_signal},
    "f25vw_f25_vwap_deviation_avwap_channel_pos_75d_base_v104_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_avwap_channel_pos_75d_base_v104_signal},
    "f25vw_f25_vwap_deviation_vwap_band_width_diff_45d_base_v105_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_band_width_diff_45d_base_v105_signal},
    "f25vw_f25_vwap_deviation_vwap_resid_when_up_60d_base_v106_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_resid_when_up_60d_base_v106_signal},
    "f25vw_f25_vwap_deviation_vwap_resid_ar1_60d_base_v107_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_resid_ar1_60d_base_v107_signal},
    "f25vw_f25_vwap_deviation_sign_change_density_120d_base_v108_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_sign_change_density_120d_base_v108_signal},
    "f25vw_f25_vwap_deviation_dist_avwap_low_vs_high_60d_base_v109_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_dist_avwap_low_vs_high_60d_base_v109_signal},
    "f25vw_f25_vwap_deviation_beta_close_vwap_45d_base_v110_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_beta_close_vwap_45d_base_v110_signal},
    "f25vw_f25_vwap_deviation_vwap_trend_strength_60d_base_v111_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_trend_strength_60d_base_v111_signal},
    "f25vw_f25_vwap_deviation_max_abs_dev_30d_base_v112_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_max_abs_dev_30d_base_v112_signal},
    "f25vw_f25_vwap_deviation_vwap_resid_mad_z_70d_base_v113_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_resid_mad_z_70d_base_v113_signal},
    "f25vw_f25_vwap_deviation_vwap_slope_z_70d_base_v114_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_slope_z_70d_base_v114_signal},
    "f25vw_f25_vwap_deviation_vwap_close_slope_agree_50d_base_v115_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_close_slope_agree_50d_base_v115_signal},
    "f25vw_f25_vwap_deviation_vwap_band_pos_rolling_zscore_35d_base_v116_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_band_pos_rolling_zscore_35d_base_v116_signal},
    "f25vw_f25_vwap_deviation_avwap_low_resid_z_60d_base_v117_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_avwap_low_resid_z_60d_base_v117_signal},
    "f25vw_f25_vwap_deviation_avwap_high_curv_55d_base_v118_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_avwap_high_curv_55d_base_v118_signal},
    "f25vw_f25_vwap_deviation_avg_above_kvwap_50d_base_v119_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_avg_above_kvwap_50d_base_v119_signal},
    "f25vw_f25_vwap_deviation_vwap_resid_skew_100d_base_v120_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_resid_skew_100d_base_v120_signal},
    "f25vw_f25_vwap_deviation_multi_vwap_dispersion_45d_base_v121_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_multi_vwap_dispersion_45d_base_v121_signal},
    "f25vw_f25_vwap_deviation_multi_vwap_descord_count_base_v122_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_multi_vwap_descord_count_base_v122_signal},
    "f25vw_f25_vwap_deviation_reversion_rate_vwap_40d_base_v123_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_reversion_rate_vwap_40d_base_v123_signal},
    "f25vw_f25_vwap_deviation_resid_rs_70d_base_v124_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_resid_rs_70d_base_v124_signal},
    "f25vw_f25_vwap_deviation_resid_var_ratio_60d_base_v125_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_resid_var_ratio_60d_base_v125_signal},
    "f25vw_f25_vwap_deviation_resid_autocorr_ratio_80d_base_v126_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_resid_autocorr_ratio_80d_base_v126_signal},
    "f25vw_f25_vwap_deviation_sign_resid_skew_50d_base_v127_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_sign_resid_skew_50d_base_v127_signal},
    "f25vw_f25_vwap_deviation_mean_abs_resid_norm_25d_base_v128_signal": {"inputs": ["high", "low", "close", "volume"], "func": f25vw_f25_vwap_deviation_mean_abs_resid_norm_25d_base_v128_signal},
    "f25vw_f25_vwap_deviation_high_vs_vwap_rank_60d_base_v129_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_high_vs_vwap_rank_60d_base_v129_signal},
    "f25vw_f25_vwap_deviation_hl_vwap_rank_diff_60d_base_v130_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_hl_vwap_rank_diff_60d_base_v130_signal},
    "f25vw_f25_vwap_deviation_vwap_side_prob_80d_base_v131_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_side_prob_80d_base_v131_signal},
    "f25vw_f25_vwap_deviation_resid_kurt_120d_base_v132_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_resid_kurt_120d_base_v132_signal},
    "f25vw_f25_vwap_deviation_composite_state_50d_base_v133_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_composite_state_50d_base_v133_signal},
    "f25vw_f25_vwap_deviation_resid_time_rsq_40d_base_v134_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_resid_time_rsq_40d_base_v134_signal},
    "f25vw_f25_vwap_deviation_vwap_convergence_rate_60d_base_v135_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_convergence_rate_60d_base_v135_signal},
    "f25vw_f25_vwap_deviation_dayssince_above_vwap_band_60d_base_v136_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_dayssince_above_vwap_band_60d_base_v136_signal},
    "f25vw_f25_vwap_deviation_resid_efficiency_50d_base_v137_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_resid_efficiency_50d_base_v137_signal},
    "f25vw_f25_vwap_deviation_dev_quantile_spread_60d_base_v138_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_dev_quantile_spread_60d_base_v138_signal},
    "f25vw_f25_vwap_deviation_band_xover_count_90d_base_v139_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_band_xover_count_90d_base_v139_signal},
    "f25vw_f25_vwap_deviation_vwap_dir_persistence_45d_base_v140_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_dir_persistence_45d_base_v140_signal},
    "f25vw_f25_vwap_deviation_logclose_vwap_3d_base_v141_signal": {"inputs": ["high", "low", "close", "volume"], "func": f25vw_f25_vwap_deviation_logclose_vwap_3d_base_v141_signal},
    "f25vw_f25_vwap_deviation_resid_vol_corr_60d_base_v142_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_resid_vol_corr_60d_base_v142_signal},
    "f25vw_f25_vwap_deviation_band_width_atr_ratio_40d_base_v143_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_band_width_atr_ratio_40d_base_v143_signal},
    "f25vw_f25_vwap_deviation_intraday_range_vs_vwap_sigma_30d_base_v144_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_intraday_range_vs_vwap_sigma_30d_base_v144_signal},
    "f25vw_f25_vwap_deviation_dominant_side_strength_90d_base_v145_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_dominant_side_strength_90d_base_v145_signal},
    "f25vw_f25_vwap_deviation_vwap_up_day_ratio_70d_base_v146_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_up_day_ratio_70d_base_v146_signal},
    "f25vw_f25_vwap_deviation_vwap_lead_corr_55d_base_v147_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_vwap_lead_corr_55d_base_v147_signal},
    "f25vw_f25_vwap_deviation_resid_tail_count_45d_base_v148_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_resid_tail_count_45d_base_v148_signal},
    "f25vw_f25_vwap_deviation_resid_halflife_proxy_50d_base_v149_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_resid_halflife_proxy_50d_base_v149_signal},
    "f25vw_f25_vwap_deviation_resid_sign_volsum_50d_base_v150_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f25vw_f25_vwap_deviation_resid_sign_volsum_50d_base_v150_signal},
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
    for name, entry in f25_vwap_deviation_base_076_150_REGISTRY.items():
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
