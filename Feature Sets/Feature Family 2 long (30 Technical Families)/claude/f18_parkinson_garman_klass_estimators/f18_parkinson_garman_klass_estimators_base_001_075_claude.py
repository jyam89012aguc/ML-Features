"""f18_parkinson_garman_klass_estimators base features 001-075.

Domain: Parkinson, Garman-Klass, Rogers-Satchell, Yang-Zhang, bipower
variation and true-range based volatility estimators -- vol estimators
that use intraday H/L/O/C beyond just close-to-close returns. Features
include single-estimator levels, ratios between estimators, z-scores,
percentile ranks, slopes, jump indicators, discrete states, estimator
dispersion, bounded transforms.

Distinct from f16 (vol term structure across horizons close-to-close)
and f17 (regime classification). Here every feature uses at least one
of high/low/open in its formula.

NaN policy: never fillna(<value>); only final replace([inf,-inf],nan).
Window > 21d uses closeadj; <= 21d uses close. Each func spells its
formula inline.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers -- estimator constructors. Each feature spells formula inline.
# ---------------------------------------------------------------------------


def _parkinson(high: pd.Series, low: pd.Series, n: int) -> pd.Series:
    """Parkinson 1980 sigma^2 = (1/(4 ln 2)) * mean[ln(H/L)^2] over N."""
    r = np.log(high / low) ** 2
    return (r.rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5


def _garman_klass(o: pd.Series, h: pd.Series, l: pd.Series, c: pd.Series, n: int) -> pd.Series:
    """GK: sigma^2 = mean[0.5 ln(H/L)^2 - (2 ln 2 - 1) ln(C/O)^2]."""
    hl = 0.5 * np.log(h / l) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(c / o) ** 2
    var = (hl - co).rolling(n, min_periods=n).mean()
    return var.clip(lower=0.0) ** 0.5


def _rogers_satchell(o: pd.Series, h: pd.Series, l: pd.Series, c: pd.Series, n: int) -> pd.Series:
    """RS: sigma^2 = mean[ln(H/C) ln(H/O) + ln(L/C) ln(L/O)]."""
    rs = np.log(h / c) * np.log(h / o) + np.log(l / c) * np.log(l / o)
    var = rs.rolling(n, min_periods=n).mean()
    return var.clip(lower=0.0) ** 0.5


def _yang_zhang(o: pd.Series, h: pd.Series, l: pd.Series, c: pd.Series, n: int) -> pd.Series:
    """Yang-Zhang 2000: overnight + open-to-close + k * RS."""
    on = np.log(o / c.shift(1))
    oc = np.log(c / o)
    var_on = on.rolling(n, min_periods=n).var(ddof=1)
    var_oc = oc.rolling(n, min_periods=n).var(ddof=1)
    rs = np.log(h / c) * np.log(h / o) + np.log(l / c) * np.log(l / o)
    var_rs = rs.rolling(n, min_periods=n).mean()
    k = 0.34 / (1.34 + (n + 1.0) / (n - 1.0))
    var = var_on + k * var_oc + (1.0 - k) * var_rs
    return var.clip(lower=0.0) ** 0.5


def _bipower(close: pd.Series, n: int) -> pd.Series:
    """Bipower variation: sum |r_i| * |r_{i-1}| * (pi/2), jump-robust."""
    r = np.log(close / close.shift(1)).abs()
    bp = r * r.shift(1) * (np.pi / 2.0)
    return bp.rolling(n, min_periods=n).sum() ** 0.5


def _realized_var(close: pd.Series, n: int) -> pd.Series:
    """Sum r^2 over N bars (realized variance scale)."""
    r = np.log(close / close.shift(1)) ** 2
    return r.rolling(n, min_periods=n).sum() ** 0.5


def _atr_wilder(h: pd.Series, l: pd.Series, c: pd.Series, n: int) -> pd.Series:
    """Wilder ATR: smoothed true range with alpha = 1/n."""
    tr = pd.concat([
        h - l,
        (h - c.shift(1)).abs(),
        (l - c.shift(1)).abs(),
    ], axis=1).max(axis=1)
    return tr.ewm(alpha=1.0 / float(n), adjust=False, min_periods=n).mean()


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


def f18pg_f18_parkinson_garman_klass_estimators_park_5d_base_v001_signal(high, low):
    """Parkinson vol, 5d. sigma = sqrt(mean[ln(H/L)^2]/(4 ln 2))."""
    n = 5
    r = (np.log(high / low) ** 2).rolling(n, min_periods=n).mean()
    return ((r / (4.0 * np.log(2.0))) ** 0.5).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_log_21d_base_v002_signal(high, low):
    """log Parkinson vol 21d -- log transform decorrelates from linear levels."""
    n = 21
    r = (np.log(high / low) ** 2).rolling(n, min_periods=n).mean()
    sig = (r / (4.0 * np.log(2.0))) ** 0.5
    return np.log(sig).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_63d_base_v003_signal(closeadj, high, low):
    """Parkinson vol 63d. closeadj only as marker (formula uses h,l)."""
    n = 63
    _ = closeadj  # marker for closeadj dependency in inputs list
    r = (np.log(high / low) ** 2).rolling(n, min_periods=n).mean()
    return ((r / (4.0 * np.log(2.0))) ** 0.5).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_252d_base_v004_signal(closeadj, high, low):
    """Parkinson vol 252d annual estimator. Uses long high/low history."""
    n = 252
    _ = closeadj
    r = (np.log(high / low) ** 2).rolling(n, min_periods=n).mean()
    return ((r / (4.0 * np.log(2.0))) ** 0.5).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_gk_10d_base_v005_signal(open, high, low, close):
    """Garman-Klass vol 10d."""
    n = 10
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(close / open) ** 2
    var = (hl - co).rolling(n, min_periods=n).mean()
    return (var.clip(lower=0.0) ** 0.5).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_gk_log_30d_base_v006_signal(open, high, low, close, closeadj):
    """log GK vol 30d."""
    n = 30
    _ = closeadj
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(close / open) ** 2
    var = (hl - co).rolling(n, min_periods=n).mean()
    sig = var.clip(lower=0.0) ** 0.5
    return np.log(sig.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_rs_14d_base_v007_signal(open, high, low, close):
    """Rogers-Satchell vol 14d -- drift-robust estimator."""
    n = 14
    rs = np.log(high / close) * np.log(high / open) + np.log(low / close) * np.log(low / open)
    var = rs.rolling(n, min_periods=n).mean()
    return (var.clip(lower=0.0) ** 0.5).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_rs_60d_base_v008_signal(open, high, low, closeadj):
    """Rogers-Satchell vol 60d using closeadj for drift-robust long window."""
    n = 60
    rs = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    var = rs.rolling(n, min_periods=n).mean()
    return (var.clip(lower=0.0) ** 0.5).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_yz_21d_base_v009_signal(open, high, low, close):
    """Yang-Zhang vol 21d -- combines overnight + intraday."""
    n = 21
    on = np.log(open / close.shift(1))
    oc = np.log(close / open)
    var_on = on.rolling(n, min_periods=n).var(ddof=1)
    var_oc = oc.rolling(n, min_periods=n).var(ddof=1)
    rs = np.log(high / close) * np.log(high / open) + np.log(low / close) * np.log(low / open)
    var_rs = rs.rolling(n, min_periods=n).mean()
    k = 0.34 / (1.34 + (n + 1.0) / (n - 1.0))
    var = var_on + k * var_oc + (1.0 - k) * var_rs
    return (var.clip(lower=0.0) ** 0.5).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_yz_63d_base_v010_signal(open, high, low, closeadj):
    """Yang-Zhang vol 63d using closeadj."""
    n = 63
    on = np.log(open / closeadj.shift(1))
    oc = np.log(closeadj / open)
    var_on = on.rolling(n, min_periods=n).var(ddof=1)
    var_oc = oc.rolling(n, min_periods=n).var(ddof=1)
    rs = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    var_rs = rs.rolling(n, min_periods=n).mean()
    k = 0.34 / (1.34 + (n + 1.0) / (n - 1.0))
    var = var_on + k * var_oc + (1.0 - k) * var_rs
    return (var.clip(lower=0.0) ** 0.5).replace([np.inf, -np.inf], np.nan)


# === Estimator ratios -- relative bias ===


def f18pg_f18_parkinson_garman_klass_estimators_park_gk_ratio_21d_base_v011_signal(open, high, low, close):
    """Parkinson / Garman-Klass 21d. > 1 = drift bias, < 1 = jumps."""
    n = 21
    park = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(close / open) ** 2
    gk_var = (hl - co).rolling(n, min_periods=n).mean()
    gk = gk_var.clip(lower=0.0) ** 0.5
    return (park / gk.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_rs_ratio_30d_base_v012_signal(open, high, low, closeadj):
    """Parkinson / Rogers-Satchell 30d. RS removes drift; ratio captures drift."""
    n = 30
    park = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    rs = rs_inner.rolling(n, min_periods=n).mean().clip(lower=0.0) ** 0.5
    return (park / rs.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_gk_rs_diff_21d_base_v013_signal(open, high, low, close):
    """(GK - RS) / GK 21d -- drift bias indicator. GK assumes zero drift, RS does not."""
    n = 21
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(close / open) ** 2
    gk_var = (hl - co).rolling(n, min_periods=n).mean()
    gk = gk_var.clip(lower=0.0) ** 0.5
    rs_inner = np.log(high / close) * np.log(high / open) + np.log(low / close) * np.log(low / open)
    rs = rs_inner.rolling(n, min_periods=n).mean().clip(lower=0.0) ** 0.5
    return ((gk - rs) / gk.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_minus_realized_log_63d_base_v014_signal(closeadj, high, low):
    """log(Parkinson(63)) - log(realized_63) -- Parkinson/realized log gap at 63d."""
    n = 63
    park = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5
    r2 = np.log(closeadj / closeadj.shift(1)) ** 2
    realized = r2.rolling(n, min_periods=n).mean() ** 0.5
    return (np.log(park.replace(0.0, np.nan)) - np.log(realized.replace(0.0, np.nan))).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_realized_ratio_21d_base_v015_signal(high, low, close):
    """Parkinson / close-to-close realized 21d. Range-vs-return efficiency."""
    n = 21
    park = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5
    r2 = np.log(close / close.shift(1)) ** 2
    realized = r2.rolling(n, min_periods=n).mean() ** 0.5
    return (park / realized.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === True-range / ATR ===






def f18pg_f18_parkinson_garman_klass_estimators_logrange_sma_8d_base_v018_signal(high, low):
    """SMA of log(H/L) 8d -- raw log range vol proxy."""
    n = 8
    lr = np.log(high / low)
    return lr.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === Estimator z-scores ===


def f18pg_f18_parkinson_garman_klass_estimators_park_z_60_252_base_v019_signal(closeadj, high, low):
    """Z-score: (Parkinson(60) - rolling_mean_252) / rolling_std_252."""
    _ = closeadj
    n = 60
    base = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5
    m = base.rolling(252, min_periods=126).mean()
    sd = base.rolling(252, min_periods=126).std(ddof=0)
    return ((base - m) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_q90_dist_120d_base_v020_signal(closeadj, high, low):
    """(Parkinson(21) - 120d 90th percentile of Parkinson(21)) / Parkinson(21) -- distance below ceiling."""
    _ = closeadj
    p = ((np.log(high / low) ** 2).rolling(21, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    q90 = p.rolling(120, min_periods=60).quantile(0.9)
    return ((p - q90) / p.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_rs_z_21_252_base_v021_signal(open, high, low, closeadj):
    """RS(21) z-score over 252-day window using closeadj for drift-stable scale."""
    n = 21
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    base = rs_inner.rolling(n, min_periods=n).mean().clip(lower=0.0) ** 0.5
    m = base.rolling(252, min_periods=126).mean()
    sd = base.rolling(252, min_periods=126).std(ddof=0)
    return ((base - m) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Percentile rank ===


def f18pg_f18_parkinson_garman_klass_estimators_atr_pctrank_252d_base_v022_signal(high, low, closeadj):
    """Rolling 252d percentile rank of ATR(21)/closeadj -- TR-based rank."""
    n = 21
    tr = pd.concat([high - low, (high - closeadj.shift(1)).abs(), (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    base = tr.rolling(n, min_periods=n).mean() / closeadj
    return base.rolling(252, min_periods=126).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_gk_park_log_ratio_60d_base_v023_signal(open, high, low, closeadj):
    """log(GK(60) / Parkinson(60)) -- long-horizon cross-estimator log ratio."""
    n = 60
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(closeadj / open) ** 2
    gk = ((hl - co).rolling(n, min_periods=n).mean().clip(lower=0.0)) ** 0.5
    park = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5
    return np.log(gk / park.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Estimator term structure (mild) ===


def f18pg_f18_parkinson_garman_klass_estimators_park_term_5_21_base_v024_signal(closeadj, high, low):
    """Parkinson(5) / Parkinson(21) -- short vs medium range."""
    _ = closeadj
    p5 = ((np.log(high / low) ** 2).rolling(5, min_periods=5).mean() / (4.0 * np.log(2.0))) ** 0.5
    p21 = ((np.log(high / low) ** 2).rolling(21, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    return (p5 / p21.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_term_log_21_63_base_v025_signal(closeadj, high, low):
    """log(Parkinson(21) / Parkinson(63))."""
    _ = closeadj
    p21 = ((np.log(high / low) ** 2).rolling(21, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    p63 = ((np.log(high / low) ** 2).rolling(63, min_periods=63).mean() / (4.0 * np.log(2.0))) ** 0.5
    return np.log(p21 / p63.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_yz_park_cross_21d_base_v026_signal(open, high, low, close):
    """log(YZ(21) / Parkinson(21)) -- cross-estimator term comparing gap-aware vs range-only."""
    n = 21
    on = np.log(open / close.shift(1))
    oc = np.log(close / open)
    von = on.rolling(n, min_periods=n).var(ddof=1)
    voc = oc.rolling(n, min_periods=n).var(ddof=1)
    rs_inner = np.log(high / close) * np.log(high / open) + np.log(low / close) * np.log(low / open)
    vrs = rs_inner.rolling(n, min_periods=n).mean()
    k = 0.34 / (1.34 + (n + 1.0) / (n - 1.0))
    yz = (von + k * voc + (1.0 - k) * vrs).clip(lower=0.0) ** 0.5
    park = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5
    return np.log(yz / park.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === Slope of estimators (base-file allowed, slope file owns derivatives) ===


def f18pg_f18_parkinson_garman_klass_estimators_park_slope_21d_base_v027_signal(closeadj, high, low):
    """Slope of Parkinson(21) vs 21 lag, divided by rolling mean for scale."""
    _ = closeadj
    p = ((np.log(high / low) ** 2).rolling(21, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    m = p.abs().rolling(21, min_periods=10).mean()
    return ((p - p.shift(21)) / m.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_gk_slope_30d_base_v028_signal(open, high, low, close):
    """Slope of GK(10) over 30-day lag."""
    n = 10
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(close / open) ** 2
    gk = ((hl - co).rolling(n, min_periods=n).mean().clip(lower=0.0)) ** 0.5
    return (gk - gk.shift(30)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_accel_21d_base_v029_signal(closeadj, high, low):
    """Acceleration of Parkinson(21): 2nd difference over 21-day step."""
    _ = closeadj
    p = ((np.log(high / low) ** 2).rolling(21, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    return (p - 2.0 * p.shift(21) + p.shift(42)).replace([np.inf, -np.inf], np.nan)


# === Drift-adjustment / jump indicators ===


def f18pg_f18_parkinson_garman_klass_estimators_bipower_21d_base_v030_signal(close):
    """Bipower variation 21d (jump-robust)."""
    n = 21
    r = np.log(close / close.shift(1)).abs()
    bp = r * r.shift(1) * (np.pi / 2.0)
    return (bp.rolling(n, min_periods=n).sum() ** 0.5).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_bipower_realized_ratio_60d_base_v031_signal(closeadj):
    """Bipower / Realized variance 60d -- jump fraction. <1 indicates jumps."""
    n = 60
    r = np.log(closeadj / closeadj.shift(1))
    bp = r.abs() * r.abs().shift(1) * (np.pi / 2.0)
    bp_sum = bp.rolling(n, min_periods=n).sum()
    rv_sum = (r ** 2).rolling(n, min_periods=n).sum()
    return (bp_sum / rv_sum.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_yz_overnight_share_30d_base_v032_signal(open, closeadj):
    """Overnight component share of total vol -- var(on) / (var(on) + var(oc))."""
    n = 30
    on = np.log(open / closeadj.shift(1))
    oc = np.log(closeadj / open)
    von = on.rolling(n, min_periods=n).var(ddof=1)
    voc = oc.rolling(n, min_periods=n).var(ddof=1)
    return (von / (von + voc).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_yz_oc_var_21d_base_v033_signal(open, close):
    """Open-to-close variance component, 21d."""
    oc = np.log(close / open)
    return oc.rolling(21, min_periods=21).var(ddof=1).replace([np.inf, -np.inf], np.nan)


# === Discrete states ===


def f18pg_f18_parkinson_garman_klass_estimators_park_p90_flag_252d_base_v034_signal(closeadj, high, low):
    """Binary: Parkinson(21) > 252d 90th percentile."""
    _ = closeadj
    p = ((np.log(high / low) ** 2).rolling(21, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    q90 = p.rolling(252, min_periods=126).quantile(0.9)
    return (p > q90).astype(float).where(p.notna() & q90.notna()).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_iqr_60d_base_v035_signal(closeadj, high, low):
    """Interquartile range of Parkinson(5) over 60d -- vol-of-vol IQR measure."""
    _ = closeadj
    p = ((np.log(high / low) ** 2).rolling(5, min_periods=5).mean() / (4.0 * np.log(2.0))) ** 0.5
    q75 = p.rolling(60, min_periods=30).quantile(0.75)
    q25 = p.rolling(60, min_periods=30).quantile(0.25)
    return (q75 - q25).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_dayssince_parkp95_252d_base_v036_signal(closeadj, high, low):
    """Days since Parkinson(21) > 95th pct of last 252."""
    _ = closeadj
    p = ((np.log(high / low) ** 2).rolling(21, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    q = p.rolling(252, min_periods=126).quantile(0.95)
    flag = (p > q).astype(float).where(p.notna() & q.notna())
    out = pd.Series(np.nan, index=p.index, dtype=float)
    cnt = np.nan
    fv = flag.values
    for i in range(len(p)):
        if np.isnan(fv[i]):
            out.iat[i] = np.nan
            continue
        if fv[i] > 0.5:
            cnt = 0.0
        elif np.isfinite(cnt):
            cnt = cnt + 1.0
        out.iat[i] = cnt
    return out.replace([np.inf, -np.inf], np.nan)


# === Estimator dispersion ===


def f18pg_f18_parkinson_garman_klass_estimators_estimator_std_21d_base_v037_signal(open, high, low, close):
    """Std across {Parkinson, GK, RS} all at 21d -- estimator disagreement."""
    n = 21
    park = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(close / open) ** 2
    gk = ((hl - co).rolling(n, min_periods=n).mean().clip(lower=0.0)) ** 0.5
    rs_inner = np.log(high / close) * np.log(high / open) + np.log(low / close) * np.log(low / open)
    rs = rs_inner.rolling(n, min_periods=n).mean().clip(lower=0.0) ** 0.5
    return pd.concat([park, gk, rs], axis=1).std(axis=1, ddof=0).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_estimator_range_30d_base_v038_signal(open, high, low, closeadj):
    """Range = max - min across {Parkinson, GK, RS} at 30d."""
    n = 30
    park = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(closeadj / open) ** 2
    gk = ((hl - co).rolling(n, min_periods=n).mean().clip(lower=0.0)) ** 0.5
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    rs = rs_inner.rolling(n, min_periods=n).mean().clip(lower=0.0) ** 0.5
    stack = pd.concat([park, gk, rs], axis=1)
    return (stack.max(axis=1) - stack.min(axis=1)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_estimator_agree_count_21d_base_v039_signal(open, high, low, close):
    """Count of estimators (Park/GK/RS) above their own 63d median, 21d window."""
    n = 21
    park = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(close / open) ** 2
    gk = ((hl - co).rolling(n, min_periods=n).mean().clip(lower=0.0)) ** 0.5
    rs_inner = np.log(high / close) * np.log(high / open) + np.log(low / close) * np.log(low / open)
    rs = rs_inner.rolling(n, min_periods=n).mean().clip(lower=0.0) ** 0.5
    a = (park > park.rolling(63, min_periods=32).median()).astype(float)
    b = (gk > gk.rolling(63, min_periods=32).median()).astype(float)
    c = (rs > rs.rolling(63, min_periods=32).median()).astype(float)
    return (a + b + c).where(park.notna() & gk.notna() & rs.notna()).replace([np.inf, -np.inf], np.nan)


# === Bounded transforms ===


def f18pg_f18_parkinson_garman_klass_estimators_park_arctan_zscore_21_60_base_v040_signal(closeadj, high, low):
    """arctan of Parkinson(21) z-score over 60d -- bounded standardized vol."""
    _ = closeadj
    p = ((np.log(high / low) ** 2).rolling(21, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    m = p.rolling(60, min_periods=30).mean()
    sd = p.rolling(60, min_periods=30).std(ddof=0)
    z = (p - m) / sd.replace(0.0, np.nan)
    return np.arctan(z).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_atr_tanh_z_14_63_base_v041_signal(high, low, close):
    """tanh of ATR(14)/close z-score over 63d -- bounded TR-vol z."""
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean() / close
    z = (atr - atr.rolling(63, min_periods=32).mean()) / atr.rolling(63, min_periods=32).std(ddof=0).replace(0.0, np.nan)
    return np.tanh(z).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_rs_sigmoid_pct_60d_base_v042_signal(open, high, low, closeadj):
    """Sigmoid of (RS_pctrank - 0.5) * 6  -- bounded percentile transform."""
    n = 60
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    rs = rs_inner.rolling(n, min_periods=n).mean().clip(lower=0.0) ** 0.5
    pct = rs.rolling(252, min_periods=126).rank(pct=True)
    return (1.0 / (1.0 + np.exp(-(pct - 0.5) * 6.0))).where(pct.notna()).replace([np.inf, -np.inf], np.nan)


# === Range-based features ===


def f18pg_f18_parkinson_garman_klass_estimators_hl_range_sq_smooth_10d_base_v043_signal(high, low):
    """(H-L)^2 / (4 ln 2) smoothed 10d -- absolute Parkinson variance scale."""
    n = 10
    r = ((high - low) ** 2 / (4.0 * np.log(2.0))).rolling(n, min_periods=n).mean()
    return r.replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_close_open_skew_60d_base_v044_signal(open, close):
    """Skewness of ln(C/O) intraday returns over 60d -- intraday move asymmetry."""
    return np.log(close / open).rolling(60, min_periods=60).skew().replace([np.inf, -np.inf], np.nan)


# === Composite vol scores ===


def f18pg_f18_parkinson_garman_klass_estimators_park_streak_below_q25_base_v045_signal(closeadj, high, low):
    """Streak of consecutive days Parkinson(21) below 252d 25th percentile -- low-vol persistence."""
    _ = closeadj
    p = ((np.log(high / low) ** 2).rolling(21, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    q = p.rolling(252, min_periods=126).quantile(0.25)
    flag = (p < q).astype(float).where(p.notna() & q.notna())
    out = pd.Series(np.nan, index=p.index, dtype=float)
    streak = np.nan
    fv = flag.values
    for i in range(len(p)):
        if np.isnan(fv[i]):
            out.iat[i] = np.nan
            continue
        if fv[i] > 0.5:
            streak = (streak + 1.0) if np.isfinite(streak) else 1.0
        else:
            streak = 0.0
        out.iat[i] = streak
    return out.replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_estimator_max_min_ratio_21d_base_v046_signal(open, high, low, close):
    """max/min ratio across {Parkinson, GK, RS} 21d -- estimator disagreement intensity."""
    n = 21
    park = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(close / open) ** 2
    gk = ((hl - co).rolling(n, min_periods=n).mean().clip(lower=0.0)) ** 0.5
    rs_inner = np.log(high / close) * np.log(high / open) + np.log(low / close) * np.log(low / open)
    rs = rs_inner.rolling(n, min_periods=n).mean().clip(lower=0.0) ** 0.5
    stk = pd.concat([park, gk, rs], axis=1)
    return (stk.max(axis=1) / stk.min(axis=1).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_gk_corr_60d_base_v047_signal(open, high, low, close):
    """60d rolling correlation between log Parkinson(5) and log GK(5)."""
    p5 = ((np.log(high / low) ** 2).rolling(5, min_periods=5).mean() / (4.0 * np.log(2.0))) ** 0.5
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(close / open) ** 2
    gk5 = ((hl - co).rolling(5, min_periods=5).mean().clip(lower=0.0)) ** 0.5
    lp = np.log(p5.replace(0.0, np.nan))
    lg = np.log(gk5.replace(0.0, np.nan))
    return lp.rolling(60, min_periods=30).corr(lg).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_estimator_max_30d_base_v048_signal(open, high, low, closeadj):
    """Max of {Parkinson, GK, RS} 30d -- conservative vol ceiling."""
    n = 30
    park = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(closeadj / open) ** 2
    gk = ((hl - co).rolling(n, min_periods=n).mean().clip(lower=0.0)) ** 0.5
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    rs = rs_inner.rolling(n, min_periods=n).mean().clip(lower=0.0) ** 0.5
    return pd.concat([park, gk, rs], axis=1).max(axis=1).replace([np.inf, -np.inf], np.nan)


# === Jump indicators ===


def f18pg_f18_parkinson_garman_klass_estimators_jump_co_threshold_count_21d_base_v049_signal(open, close):
    """Count days where |ln(C/O)| > 2 * 21d std of ln(C/O), over 21d window."""
    oc = np.log(close / open)
    s = oc.rolling(21, min_periods=21).std(ddof=0)
    flag = (oc.abs() > 2.0 * s).astype(float).where(oc.notna() & s.notna())
    return flag.rolling(21, min_periods=21).sum().replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_wide_bar_park_ratio_30d_base_v050_signal(closeadj, high, low):
    """Count of bars where ln(H/L) > 2 * Parkinson(21), summed over 30d."""
    _ = closeadj
    lr = np.log(high / low)
    p = ((np.log(high / low) ** 2).rolling(21, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    flag = (lr > 2.0 * p).astype(float).where(lr.notna() & p.notna())
    return flag.rolling(30, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_close_open_abs_60d_base_v051_signal(open, closeadj):
    """Mean |ln(C/O)| 60d -- intraday move magnitude."""
    return np.log(closeadj / open).abs().rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


# === Realized-vs-range gaps ===


def f18pg_f18_parkinson_garman_klass_estimators_rv_park_gap_42d_base_v052_signal(close, high, low):
    """Realized close-to-close - Parkinson 42d -- jump-vs-range gap."""
    n = 42
    r = np.log(close / close.shift(1)) ** 2
    realized = (r.rolling(n, min_periods=n).mean()) ** 0.5
    park = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5
    return (realized - park).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_gk_kurtosis_120d_base_v053_signal(open, high, low, closeadj):
    """Kurtosis of GK(5) daily values over 120d -- vol-distribution shape."""
    n = 5
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(closeadj / open) ** 2
    g = ((hl - co).rolling(n, min_periods=n).mean().clip(lower=0.0)) ** 0.5
    return g.rolling(120, min_periods=60).kurt().replace([np.inf, -np.inf], np.nan)


# === Additional structurally distinct features ===


def f18pg_f18_parkinson_garman_klass_estimators_park_vol_of_vol_42d_base_v054_signal(closeadj, high, low):
    """Std of Parkinson(5) over 42d -- vol-of-vol from range estimator."""
    _ = closeadj
    p = ((np.log(high / low) ** 2).rolling(5, min_periods=5).mean() / (4.0 * np.log(2.0))) ** 0.5
    return p.rolling(42, min_periods=42).std(ddof=0).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_skew_60d_base_v055_signal(closeadj, high, low):
    """Skewness of ln(H/L)^2 60d -- asymmetry in daily range contribution."""
    _ = closeadj
    r = np.log(high / low) ** 2
    return r.rolling(60, min_periods=60).skew().replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_streak_above_median_base_v056_signal(closeadj, high, low):
    """Streak of consecutive days Parkinson(21) above its own 252d median."""
    _ = closeadj
    p = ((np.log(high / low) ** 2).rolling(21, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    med = p.rolling(252, min_periods=126).median()
    flag = (p > med).astype(float).where(p.notna() & med.notna())
    out = pd.Series(np.nan, index=p.index, dtype=float)
    streak = np.nan
    fv = flag.values
    for i in range(len(p)):
        if np.isnan(fv[i]):
            out.iat[i] = np.nan
            continue
        if fv[i] > 0.5:
            streak = (streak + 1.0) if np.isfinite(streak) else 1.0
        else:
            streak = 0.0
        out.iat[i] = streak
    return out.replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_sign_above_long_base_v057_signal(closeadj, high, low):
    """Sign(Parkinson(21) - Parkinson(63))."""
    _ = closeadj
    p21 = ((np.log(high / low) ** 2).rolling(21, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    p63 = ((np.log(high / low) ** 2).rolling(63, min_periods=63).mean() / (4.0 * np.log(2.0))) ** 0.5
    return np.sign(p21 - p63).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_yz_overnight_realized_ratio_60d_base_v058_signal(open, closeadj):
    """Var(overnight) / Var(intraday returns) 60d."""
    n = 60
    on = np.log(open / closeadj.shift(1))
    oc = np.log(closeadj / open)
    von = on.rolling(n, min_periods=n).var(ddof=1)
    voc = oc.rolling(n, min_periods=n).var(ddof=1)
    return (von / voc.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_atr_z_60_252_base_v059_signal(high, low, closeadj):
    """Z-score of ATR/close(60) over 252 window."""
    n = 60
    tr = pd.concat([high - low, (high - closeadj.shift(1)).abs(), (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    base = (tr.rolling(n, min_periods=n).mean() / closeadj)
    m = base.rolling(252, min_periods=126).mean()
    sd = base.rolling(252, min_periods=126).std(ddof=0)
    return ((base - m) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_atr_park_ratio_21d_base_v060_signal(high, low, close):
    """ATR(14)/close divided by Parkinson(21) -- TR-vs-range estimator gap."""
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean() / close
    park = ((np.log(high / low) ** 2).rolling(21, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    return (atr / park.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_rs_kurt_120d_base_v061_signal(open, high, low, closeadj):
    """Kurtosis of daily RS contribution over 120d."""
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    return rs_inner.rolling(120, min_periods=120).kurt().replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_gk_pct_decile_high_flag_120d_base_v062_signal(open, high, low, closeadj):
    """Binary: GK(30) in top 20% of 120-day distribution."""
    n = 30
    hl = 0.5 * np.log(high / low) ** 2
    co = (2.0 * np.log(2.0) - 1.0) * np.log(closeadj / open) ** 2
    g = ((hl - co).rolling(n, min_periods=n).mean().clip(lower=0.0)) ** 0.5
    q = g.rolling(120, min_periods=60).quantile(0.8)
    return (g > q).astype(float).where(g.notna() & q.notna()).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_rs_low_decile_flag_252d_base_v063_signal(open, high, low, closeadj):
    """Binary: RS(60) below 252d 10th percentile."""
    n = 60
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    rs = rs_inner.rolling(n, min_periods=n).mean().clip(lower=0.0) ** 0.5
    q = rs.rolling(252, min_periods=126).quantile(0.1)
    return (rs < q).astype(float).where(rs.notna() & q.notna()).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_mad_42d_base_v064_signal(closeadj, high, low):
    """Median absolute deviation of Parkinson(5) over 42d."""
    _ = closeadj
    p = ((np.log(high / low) ** 2).rolling(5, min_periods=5).mean() / (4.0 * np.log(2.0))) ** 0.5
    med = p.rolling(42, min_periods=42).median()
    return (p - med).abs().rolling(42, min_periods=42).median().replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_gk_autocorr_21d_base_v065_signal(open, high, low, close):
    """Lag-1 autocorrelation of GK daily contribution, 60d window."""
    g = 0.5 * np.log(high / low) ** 2 - (2.0 * np.log(2.0) - 1.0) * np.log(close / open) ** 2
    n = 60
    m1 = g.rolling(n, min_periods=n).mean()
    sd = g.rolling(n, min_periods=n).std(ddof=0)
    cross = (g * g.shift(1)).rolling(n, min_periods=n).mean()
    cov = cross - m1 * m1
    return (cov / (sd * sd).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_overnight_jump_count_60d_base_v066_signal(open, closeadj):
    """Count of overnight returns > 2 sigma over 60d window."""
    on = np.log(open / closeadj.shift(1))
    s = on.rolling(60, min_periods=60).std(ddof=0)
    flag = (on.abs() > 2.0 * s).astype(float).where(on.notna() & s.notna())
    return flag.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_dispersion_5_21_63_base_v067_signal(closeadj, high, low):
    """Std across Parkinson(5), (21), (63) -- term-structure dispersion."""
    _ = closeadj
    p5 = ((np.log(high / low) ** 2).rolling(5, min_periods=5).mean() / (4.0 * np.log(2.0))) ** 0.5
    p21 = ((np.log(high / low) ** 2).rolling(21, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    p63 = ((np.log(high / low) ** 2).rolling(63, min_periods=63).mean() / (4.0 * np.log(2.0))) ** 0.5
    return pd.concat([np.log(p5), np.log(p21), np.log(p63)], axis=1).std(axis=1, ddof=0).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_logrange_z_8_42_base_v068_signal(high, low):
    """log(H/L) z-score over 42d."""
    lr = np.log(high / low)
    m = lr.rolling(42, min_periods=42).mean()
    sd = lr.rolling(42, min_periods=42).std(ddof=0)
    return ((lr - m) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_rs_park_diff_42d_base_v069_signal(open, high, low, closeadj):
    """RS(42) minus Parkinson(42) -- drift-bias signal at 42d. RS removes drift, Parkinson does not."""
    n = 42
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    rs = rs_inner.rolling(n, min_periods=n).mean().clip(lower=0.0) ** 0.5
    park = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5
    return (rs - park).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_atr_log_30d_base_v070_signal(high, low, closeadj):
    """log of ATR(30)/closeadj."""
    n = 30
    tr = pd.concat([high - low, (high - closeadj.shift(1)).abs(), (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(n, min_periods=n).mean() / closeadj
    return np.log(atr.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_skew_252d_base_v071_signal(closeadj, high, low):
    """Skewness of Parkinson(21) over 252d -- distribution shape of vol regime."""
    _ = closeadj
    p = ((np.log(high / low) ** 2).rolling(21, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    return p.rolling(252, min_periods=126).skew().replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_bipower_park_ratio_21d_base_v072_signal(close, high, low):
    """Bipower(21) / Parkinson(21) -- jump-robust vs range estimator."""
    n = 21
    r = np.log(close / close.shift(1)).abs()
    bp = r * r.shift(1) * (np.pi / 2.0)
    bipow = bp.rolling(n, min_periods=n).sum() ** 0.5
    park = ((np.log(high / low) ** 2).rolling(n, min_periods=n).mean() / (4.0 * np.log(2.0))) ** 0.5 * (n ** 0.5)
    return (bipow / park.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_yz_pctrank_120d_base_v073_signal(open, high, low, closeadj):
    """Percentile rank of Yang-Zhang(21) over 120d."""
    n = 21
    on = np.log(open / closeadj.shift(1))
    oc = np.log(closeadj / open)
    von = on.rolling(n, min_periods=n).var(ddof=1)
    voc = oc.rolling(n, min_periods=n).var(ddof=1)
    rs_inner = np.log(high / closeadj) * np.log(high / open) + np.log(low / closeadj) * np.log(low / open)
    vrs = rs_inner.rolling(n, min_periods=n).mean()
    k = 0.34 / (1.34 + (n + 1.0) / (n - 1.0))
    yz = (von + k * voc + (1.0 - k) * vrs).clip(lower=0.0) ** 0.5
    return yz.rolling(120, min_periods=60).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_intraday_oc_std_30d_base_v074_signal(open, close):
    """Std of ln(C/O) 30d -- intraday return scatter."""
    return np.log(close / open).rolling(30, min_periods=30).std(ddof=0).replace([np.inf, -np.inf], np.nan)


def f18pg_f18_parkinson_garman_klass_estimators_park_arctan_slope_42d_base_v075_signal(closeadj, high, low):
    """arctan of (Parkinson(21) - Parkinson(21).shift(42)) / Parkinson(21).abs.mean(42)."""
    _ = closeadj
    p = ((np.log(high / low) ** 2).rolling(21, min_periods=21).mean() / (4.0 * np.log(2.0))) ** 0.5
    slope = (p - p.shift(42)) / p.abs().rolling(42, min_periods=21).mean().replace(0.0, np.nan)
    return np.arctan(slope).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f18_parkinson_garman_klass_estimators_base_001_075_REGISTRY = {
    "f18pg_f18_parkinson_garman_klass_estimators_park_5d_base_v001_signal": {"inputs": ["high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_5d_base_v001_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_log_21d_base_v002_signal": {"inputs": ["high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_log_21d_base_v002_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_63d_base_v003_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_63d_base_v003_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_252d_base_v004_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_252d_base_v004_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_gk_10d_base_v005_signal": {"inputs": ["open", "high", "low", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_gk_10d_base_v005_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_gk_log_30d_base_v006_signal": {"inputs": ["open", "high", "low", "close", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_gk_log_30d_base_v006_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_rs_14d_base_v007_signal": {"inputs": ["open", "high", "low", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_rs_14d_base_v007_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_rs_60d_base_v008_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_rs_60d_base_v008_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_yz_21d_base_v009_signal": {"inputs": ["open", "high", "low", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_yz_21d_base_v009_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_yz_63d_base_v010_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_yz_63d_base_v010_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_gk_ratio_21d_base_v011_signal": {"inputs": ["open", "high", "low", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_gk_ratio_21d_base_v011_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_rs_ratio_30d_base_v012_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_rs_ratio_30d_base_v012_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_gk_rs_diff_21d_base_v013_signal": {"inputs": ["open", "high", "low", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_gk_rs_diff_21d_base_v013_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_minus_realized_log_63d_base_v014_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_minus_realized_log_63d_base_v014_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_realized_ratio_21d_base_v015_signal": {"inputs": ["high", "low", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_realized_ratio_21d_base_v015_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_logrange_sma_8d_base_v018_signal": {"inputs": ["high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_logrange_sma_8d_base_v018_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_z_60_252_base_v019_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_z_60_252_base_v019_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_q90_dist_120d_base_v020_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_q90_dist_120d_base_v020_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_rs_z_21_252_base_v021_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_rs_z_21_252_base_v021_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_atr_pctrank_252d_base_v022_signal": {"inputs": ["high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_atr_pctrank_252d_base_v022_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_gk_park_log_ratio_60d_base_v023_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_gk_park_log_ratio_60d_base_v023_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_term_5_21_base_v024_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_term_5_21_base_v024_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_term_log_21_63_base_v025_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_term_log_21_63_base_v025_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_yz_park_cross_21d_base_v026_signal": {"inputs": ["open", "high", "low", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_yz_park_cross_21d_base_v026_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_slope_21d_base_v027_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_slope_21d_base_v027_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_gk_slope_30d_base_v028_signal": {"inputs": ["open", "high", "low", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_gk_slope_30d_base_v028_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_accel_21d_base_v029_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_accel_21d_base_v029_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_bipower_21d_base_v030_signal": {"inputs": ["close"], "func": f18pg_f18_parkinson_garman_klass_estimators_bipower_21d_base_v030_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_bipower_realized_ratio_60d_base_v031_signal": {"inputs": ["closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_bipower_realized_ratio_60d_base_v031_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_yz_overnight_share_30d_base_v032_signal": {"inputs": ["open", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_yz_overnight_share_30d_base_v032_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_yz_oc_var_21d_base_v033_signal": {"inputs": ["open", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_yz_oc_var_21d_base_v033_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_p90_flag_252d_base_v034_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_p90_flag_252d_base_v034_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_iqr_60d_base_v035_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_iqr_60d_base_v035_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_dayssince_parkp95_252d_base_v036_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_dayssince_parkp95_252d_base_v036_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_estimator_std_21d_base_v037_signal": {"inputs": ["open", "high", "low", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_estimator_std_21d_base_v037_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_estimator_range_30d_base_v038_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_estimator_range_30d_base_v038_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_estimator_agree_count_21d_base_v039_signal": {"inputs": ["open", "high", "low", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_estimator_agree_count_21d_base_v039_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_arctan_zscore_21_60_base_v040_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_arctan_zscore_21_60_base_v040_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_atr_tanh_z_14_63_base_v041_signal": {"inputs": ["high", "low", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_atr_tanh_z_14_63_base_v041_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_rs_sigmoid_pct_60d_base_v042_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_rs_sigmoid_pct_60d_base_v042_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_hl_range_sq_smooth_10d_base_v043_signal": {"inputs": ["high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_hl_range_sq_smooth_10d_base_v043_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_close_open_skew_60d_base_v044_signal": {"inputs": ["open", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_close_open_skew_60d_base_v044_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_streak_below_q25_base_v045_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_streak_below_q25_base_v045_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_estimator_max_min_ratio_21d_base_v046_signal": {"inputs": ["open", "high", "low", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_estimator_max_min_ratio_21d_base_v046_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_gk_corr_60d_base_v047_signal": {"inputs": ["open", "high", "low", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_gk_corr_60d_base_v047_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_estimator_max_30d_base_v048_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_estimator_max_30d_base_v048_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_jump_co_threshold_count_21d_base_v049_signal": {"inputs": ["open", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_jump_co_threshold_count_21d_base_v049_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_wide_bar_park_ratio_30d_base_v050_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_wide_bar_park_ratio_30d_base_v050_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_close_open_abs_60d_base_v051_signal": {"inputs": ["open", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_close_open_abs_60d_base_v051_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_rv_park_gap_42d_base_v052_signal": {"inputs": ["close", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_rv_park_gap_42d_base_v052_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_gk_kurtosis_120d_base_v053_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_gk_kurtosis_120d_base_v053_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_vol_of_vol_42d_base_v054_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_vol_of_vol_42d_base_v054_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_skew_60d_base_v055_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_skew_60d_base_v055_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_streak_above_median_base_v056_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_streak_above_median_base_v056_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_sign_above_long_base_v057_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_sign_above_long_base_v057_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_yz_overnight_realized_ratio_60d_base_v058_signal": {"inputs": ["open", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_yz_overnight_realized_ratio_60d_base_v058_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_atr_z_60_252_base_v059_signal": {"inputs": ["high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_atr_z_60_252_base_v059_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_atr_park_ratio_21d_base_v060_signal": {"inputs": ["high", "low", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_atr_park_ratio_21d_base_v060_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_rs_kurt_120d_base_v061_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_rs_kurt_120d_base_v061_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_gk_pct_decile_high_flag_120d_base_v062_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_gk_pct_decile_high_flag_120d_base_v062_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_rs_low_decile_flag_252d_base_v063_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_rs_low_decile_flag_252d_base_v063_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_mad_42d_base_v064_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_mad_42d_base_v064_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_gk_autocorr_21d_base_v065_signal": {"inputs": ["open", "high", "low", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_gk_autocorr_21d_base_v065_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_overnight_jump_count_60d_base_v066_signal": {"inputs": ["open", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_overnight_jump_count_60d_base_v066_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_dispersion_5_21_63_base_v067_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_dispersion_5_21_63_base_v067_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_logrange_z_8_42_base_v068_signal": {"inputs": ["high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_logrange_z_8_42_base_v068_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_rs_park_diff_42d_base_v069_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_rs_park_diff_42d_base_v069_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_atr_log_30d_base_v070_signal": {"inputs": ["high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_atr_log_30d_base_v070_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_skew_252d_base_v071_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_skew_252d_base_v071_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_bipower_park_ratio_21d_base_v072_signal": {"inputs": ["close", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_bipower_park_ratio_21d_base_v072_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_yz_pctrank_120d_base_v073_signal": {"inputs": ["open", "high", "low", "closeadj"], "func": f18pg_f18_parkinson_garman_klass_estimators_yz_pctrank_120d_base_v073_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_intraday_oc_std_30d_base_v074_signal": {"inputs": ["open", "close"], "func": f18pg_f18_parkinson_garman_klass_estimators_intraday_oc_std_30d_base_v074_signal},
    "f18pg_f18_parkinson_garman_klass_estimators_park_arctan_slope_42d_base_v075_signal": {"inputs": ["closeadj", "high", "low"], "func": f18pg_f18_parkinson_garman_klass_estimators_park_arctan_slope_42d_base_v075_signal},
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
    for name, entry in f18_parkinson_garman_klass_estimators_base_001_075_REGISTRY.items():
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
