import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


# ===== folder domain primitives (52-week / multi-year cycle position) =====
def _f07cy_prox_high(c, w):
    hi = c.rolling(w, min_periods=max(1, w // 2)).max()
    return c / hi.replace(0, np.nan)


def _f07cy_prox_low(c, w):
    lo = c.rolling(w, min_periods=max(1, w // 2)).min()
    return c / lo.replace(0, np.nan)


def _f07cy_range_pos(c, w):
    hi = c.rolling(w, min_periods=max(1, w // 2)).max()
    lo = c.rolling(w, min_periods=max(1, w // 2)).min()
    return (c - lo) / (hi - lo).replace(0, np.nan)


def _f07cy_drawdown(c, w):
    hi = c.rolling(w, min_periods=max(1, w // 2)).max()
    return c / hi.replace(0, np.nan) - 1.0


def _f07cy_recovery(c, w):
    lo = c.rolling(w, min_periods=max(1, w // 2)).min()
    return c / lo.replace(0, np.nan) - 1.0


def _f07cy_loggap_high(c, w):
    hi = c.rolling(w, min_periods=max(1, w // 2)).max()
    return np.log(c.replace(0, np.nan) / hi.replace(0, np.nan))


def _f07cy_loggap_low(c, w):
    lo = c.rolling(w, min_periods=max(1, w // 2)).min()
    return np.log(c.replace(0, np.nan) / lo.replace(0, np.nan))


# jerk2d 21d raw) proximity to 252d high
def f07cy_f07_fiftytwo_week_cycle_position_proxhi_252d_jerk_v001_signal(closeadj):
    base = _f07cy_prox_high(closeadj, 252)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) proximity to 252d low
def f07cy_f07_fiftytwo_week_cycle_position_proxlo_252d_jerk_v002_signal(closeadj):
    base = _f07cy_prox_low(closeadj, 252)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d raw) 1260d cycle range position
def f07cy_f07_fiftytwo_week_cycle_position_rngpos_1260d_jerk_v003_signal(closeadj):
    base = _f07cy_range_pos(closeadj, 1260)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) 252d range-pos z vs 126d
def f07cy_f07_fiftytwo_week_cycle_position_rngposz_252d_jerk_v004_signal(closeadj):
    base = _z(_f07cy_range_pos(closeadj, 252), 126)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) 504d range-pos z vs 252d
def f07cy_f07_fiftytwo_week_cycle_position_rngposz_504d_jerk_v005_signal(closeadj):
    base = _z(_f07cy_range_pos(closeadj, 504), 252)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) share of quarter the 252d drawdown was worsening
def f07cy_f07_fiftytwo_week_cycle_position_ddworsen_252d_jerk_v006_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 252)
    base = (dd < dd.shift(1)).astype(float).rolling(63, min_periods=21).mean()
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) sign x sqrt magnitude of 504d recovery
def f07cy_f07_fiftytwo_week_cycle_position_recovsignmag_504d_jerk_v007_signal(closeadj):
    rec = _f07cy_recovery(closeadj, 504)
    base = np.sign(rec) * (rec.abs() ** 0.5)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) 252d recovery z vs 126d
def f07cy_f07_fiftytwo_week_cycle_position_recovz_252d_jerk_v008_signal(closeadj):
    base = _z(_f07cy_recovery(closeadj, 252), 126)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) 252d off-floor z vs 252d
def f07cy_f07_fiftytwo_week_cycle_position_offfloorz_252d_jerk_v009_signal(closeadj):
    base = _z(_f07cy_prox_low(closeadj, 252), 252)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d raw) 1260d log-gap z vs 504d
def f07cy_f07_fiftytwo_week_cycle_position_deepgapz_1260d_jerk_v010_signal(closeadj):
    base = _z(_f07cy_loggap_high(closeadj, 1260), 504)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d raw) 1260d log-amplitude z vs 252d
def f07cy_f07_fiftytwo_week_cycle_position_amplz_1260d_jerk_v011_signal(closeadj):
    hi = _rmax(closeadj, 1260)
    lo = _rmin(closeadj, 1260)
    base = _z(np.log(hi.replace(0, np.nan) / lo.replace(0, np.nan)), 252)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) 252d proximity-high rank vs 252d
def f07cy_f07_fiftytwo_week_cycle_position_proxhirank_252d_jerk_v012_signal(closeadj):
    base = _rank(_f07cy_prox_high(closeadj, 252), 252)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) 252d range-pos rank vs 252d
def f07cy_f07_fiftytwo_week_cycle_position_rngposrank_252d_jerk_v013_signal(closeadj):
    base = _rank(_f07cy_range_pos(closeadj, 252), 252)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) 504d range-pos rank vs 252d
def f07cy_f07_fiftytwo_week_cycle_position_rngposrank_504d_jerk_v014_signal(closeadj):
    base = _rank(_f07cy_range_pos(closeadj, 504), 252)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) 504d drawdown rank vs 504d
def f07cy_f07_fiftytwo_week_cycle_position_ddrank_504d_jerk_v015_signal(closeadj):
    base = _rank(_f07cy_drawdown(closeadj, 504), 504)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) 252d recovery rank vs 504d
def f07cy_f07_fiftytwo_week_cycle_position_recovrank_252d_jerk_v016_signal(closeadj):
    base = _rank(_f07cy_recovery(closeadj, 252), 504)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d raw) 1260d midpoint-skew rank vs 504d
def f07cy_f07_fiftytwo_week_cycle_position_midskewrank_1260d_jerk_v017_signal(closeadj):
    hi = _rmax(closeadj, 1260)
    lo = _rmin(closeadj, 1260)
    mid = (hi + lo) / 2.0
    base = _rank((closeadj - mid) / (hi - lo).replace(0, np.nan), 504)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) EMA-smoothed 252d range position
def f07cy_f07_fiftytwo_week_cycle_position_rngposema_252d_jerk_v018_signal(closeadj):
    base = _f07cy_range_pos(closeadj, 252).ewm(span=42, min_periods=21).mean()
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) 252d range-pos minus its slow EMA
def f07cy_f07_fiftytwo_week_cycle_position_rngposdisp_252d_jerk_v019_signal(closeadj):
    rp = _f07cy_range_pos(closeadj, 252)
    base = rp - rp.ewm(span=63, min_periods=21).mean()
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) EMA-smoothed 504d proximity to high
def f07cy_f07_fiftytwo_week_cycle_position_proxhiema_504d_jerk_v020_signal(closeadj):
    base = _f07cy_prox_high(closeadj, 504).ewm(span=63, min_periods=21).mean()
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) EMA-smoothed 252d log-gap to high
def f07cy_f07_fiftytwo_week_cycle_position_loggaphiema_252d_jerk_v021_signal(closeadj):
    base = _f07cy_loggap_high(closeadj, 252).ewm(span=21, min_periods=10).mean()
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) convex top-hug bias 252d
def f07cy_f07_fiftytwo_week_cycle_position_tophug_252d_jerk_v022_signal(closeadj):
    rp = _f07cy_range_pos(closeadj, 252)
    base = np.sign(rp - 0.5) * (rp - 0.5) ** 2 * 4.0
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) sign x sqrt magnitude of 252d drawdown
def f07cy_f07_fiftytwo_week_cycle_position_ddsignmag_252d_jerk_v023_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 252)
    base = np.sign(dd) * (dd.abs() ** 0.5)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) cube of 252d drawdown
def f07cy_f07_fiftytwo_week_cycle_position_ddcube_252d_jerk_v024_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 252)
    base = dd ** 3 * 100.0
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) convex approach to 252d high (proximity above 0.8 squared)
def f07cy_f07_fiftytwo_week_cycle_position_approachconv_252d_jerk_v025_signal(closeadj):
    p = _f07cy_prox_high(closeadj, 252)
    e = (p - 0.8).clip(lower=0)
    base = e ** 2 * 25.0
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) 252d recovery/drawdown balance
def f07cy_f07_fiftytwo_week_cycle_position_vbalance_252d_jerk_v026_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 252).abs()
    rec = _f07cy_recovery(closeadj, 252)
    base = (rec - dd) / (rec + dd).replace(0, np.nan)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) 504d recovery/drawdown balance
def f07cy_f07_fiftytwo_week_cycle_position_vbalance_504d_jerk_v027_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 504).abs()
    rec = _f07cy_recovery(closeadj, 504)
    base = (rec - dd) / (rec + dd).replace(0, np.nan)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) 252d-high / 504d-high freshness
def f07cy_f07_fiftytwo_week_cycle_position_anchfresh_504d_jerk_v028_signal(closeadj):
    base = _rmax(closeadj, 252) / _rmax(closeadj, 504).replace(0, np.nan)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) 504d minus 252d range position spread
def f07cy_f07_fiftytwo_week_cycle_position_posspr_504d_jerk_v029_signal(closeadj):
    base = _f07cy_range_pos(closeadj, 504) - _f07cy_range_pos(closeadj, 252)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d raw) 252d minus 1260d recovery spread
def f07cy_f07_fiftytwo_week_cycle_position_recovspr_1260d_jerk_v030_signal(closeadj):
    base = _f07cy_recovery(closeadj, 252) - _f07cy_recovery(closeadj, 1260)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) 252d/504d drawdown ratio
def f07cy_f07_fiftytwo_week_cycle_position_ddratio_504d_jerk_v031_signal(closeadj):
    base = _f07cy_drawdown(closeadj, 252) / _f07cy_drawdown(closeadj, 504).replace(0, np.nan)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) 252d range amplitude / price
def f07cy_f07_fiftytwo_week_cycle_position_amplitude_252d_jerk_v032_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    base = (hi - lo) / closeadj.replace(0, np.nan)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) 252d high extension over mean
def f07cy_f07_fiftytwo_week_cycle_position_hiextend_252d_jerk_v033_signal(closeadj):
    hi = _rmax(closeadj, 252)
    mn = _mean(closeadj, 252)
    base = (hi - mn) / mn.replace(0, np.nan)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) 252d low extension under mean
def f07cy_f07_fiftytwo_week_cycle_position_loextend_252d_jerk_v034_signal(closeadj):
    lo = _rmin(closeadj, 252)
    mn = _mean(closeadj, 252)
    base = (mn - lo) / mn.replace(0, np.nan)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) 252d ceiling-vs-floor extension asymmetry
def f07cy_f07_fiftytwo_week_cycle_position_extasym_252d_jerk_v035_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    mn = _mean(closeadj, 252)
    up = (hi - mn) / mn.replace(0, np.nan)
    dn = (mn - lo) / mn.replace(0, np.nan)
    base = (up - dn) / (up + dn).replace(0, np.nan)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d raw) log span 1260d-high vs 252d-low
def f07cy_f07_fiftytwo_week_cycle_position_span_1260d_jerk_v036_signal(closeadj):
    hi = _rmax(closeadj, 1260)
    lo = _rmin(closeadj, 252)
    base = np.log(hi.replace(0, np.nan) / lo.replace(0, np.nan))
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) fraction of year within 5% of 252d high
def f07cy_f07_fiftytwo_week_cycle_position_nearhitime_252d_jerk_v037_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 252)
    base = (dd >= -0.05).astype(float).rolling(252, min_periods=126).mean()
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) fraction of year in upper third
def f07cy_f07_fiftytwo_week_cycle_position_uppertime_252d_jerk_v038_signal(closeadj):
    rp = _f07cy_range_pos(closeadj, 252)
    base = (rp >= 0.6667).astype(float).rolling(252, min_periods=126).mean()
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) fraction of year above the 252d midpoint
def f07cy_f07_fiftytwo_week_cycle_position_uppermidtime_252d_jerk_v039_signal(closeadj):
    rp = _f07cy_range_pos(closeadj, 252)
    base = (rp >= 0.5).astype(float).rolling(252, min_periods=126).mean()
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) fraction of year >10% below 504d high
def f07cy_f07_fiftytwo_week_cycle_position_underwater_504d_jerk_v040_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 504)
    base = (dd <= -0.10).astype(float).rolling(252, min_periods=126).mean()
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) fresh-252d-high rate over quarter
def f07cy_f07_fiftytwo_week_cycle_position_newhifreq_252d_jerk_v041_signal(closeadj):
    hi = closeadj.rolling(252, min_periods=126).max()
    base = (closeadj >= hi.shift(1) * 0.99999).astype(float).rolling(63, min_periods=21).mean()
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) cross-window range-pos dispersion 252/504/1260
def f07cy_f07_fiftytwo_week_cycle_position_posdisp_504d_jerk_v042_signal(closeadj):
    p1 = _f07cy_range_pos(closeadj, 252)
    p2 = _f07cy_range_pos(closeadj, 504)
    p3 = _f07cy_range_pos(closeadj, 1260)
    base = pd.concat([p1, p2, p3], axis=1).std(axis=1)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) quarter volatility of 252d range position
def f07cy_f07_fiftytwo_week_cycle_position_posvol_252d_jerk_v043_signal(closeadj):
    base = _f07cy_range_pos(closeadj, 252).rolling(63, min_periods=21).std()
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) 252d ulcer pain index over quarter
def f07cy_f07_fiftytwo_week_cycle_position_ulcer_252d_jerk_v044_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 252)
    base = (dd ** 2).rolling(63, min_periods=21).mean() ** 0.5
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) 252d net move vs total path efficiency
def f07cy_f07_fiftytwo_week_cycle_position_patheff_252d_jerk_v045_signal(closeadj):
    net = (closeadj - closeadj.shift(252)).abs()
    path = closeadj.diff().abs().rolling(252, min_periods=126).sum()
    base = net / path.replace(0, np.nan)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) EMA of 504d log-gap off low
def f07cy_f07_fiftytwo_week_cycle_position_recovsmooth_504d_jerk_v046_signal(closeadj):
    base = _f07cy_loggap_low(closeadj, 504).ewm(span=42, min_periods=21).mean()
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d raw) EMA of 1260d log-gap off low
def f07cy_f07_fiftytwo_week_cycle_position_loggaplosmooth_1260d_jerk_v047_signal(closeadj):
    base = _f07cy_loggap_low(closeadj, 1260).ewm(span=42, min_periods=21).mean()
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) intraday 252d range position
def f07cy_f07_fiftytwo_week_cycle_position_hlrngpos_252d_jerk_v048_signal(closeadj, high, low):
    hi = high.rolling(252, min_periods=126).max()
    lo = low.rolling(252, min_periods=126).min()
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) intraday true-low proximity rank vs 252d
def f07cy_f07_fiftytwo_week_cycle_position_trueproxlorank_252d_jerk_v049_signal(closeadj, low):
    lo = low.rolling(252, min_periods=126).min()
    base = _rank(closeadj / lo.replace(0, np.nan), 252)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) ATR-scaled distance to 252d high
def f07cy_f07_fiftytwo_week_cycle_position_gapatr_252d_jerk_v050_signal(closeadj, high, low):
    hi = closeadj.rolling(252, min_periods=126).max()
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = (closeadj - hi) / atr.replace(0, np.nan)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) ATR-scaled distance off 252d low
def f07cy_f07_fiftytwo_week_cycle_position_lowgapatr_252d_jerk_v051_signal(closeadj, high, low):
    lo = closeadj.rolling(252, min_periods=126).min()
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = (closeadj - lo) / atr.replace(0, np.nan)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 21d raw) intraday-high premium over close-high (252d)
def f07cy_f07_fiftytwo_week_cycle_position_hipremium_252d_jerk_v052_signal(closeadj, high):
    ht = high.rolling(252, min_periods=126).max()
    hc = closeadj.rolling(252, min_periods=126).max()
    base = (ht - hc) / hc.replace(0, np.nan)
    d1 = base - base.shift(21)
    sl = d1 - d1.shift(21)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) proximity to 252d high
def f07cy_f07_fiftytwo_week_cycle_position_proxhi_252d_jerk_v053_signal(closeadj):
    base = _f07cy_prox_high(closeadj, 252)
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) proximity to 252d low
def f07cy_f07_fiftytwo_week_cycle_position_proxlo_252d_jerk_v054_signal(closeadj):
    base = _f07cy_prox_low(closeadj, 252)
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 84d z-scored vs 126d) 1260d cycle range position
def f07cy_f07_fiftytwo_week_cycle_position_rngpos_1260d_jerk_v055_signal(closeadj):
    base = _f07cy_range_pos(closeadj, 1260)
    d1 = base - base.shift(84)
    sl = d1 - d1.shift(84)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) 252d range-pos z vs 126d
def f07cy_f07_fiftytwo_week_cycle_position_rngposz_252d_jerk_v056_signal(closeadj):
    base = _z(_f07cy_range_pos(closeadj, 252), 126)
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d z-scored vs 126d) 504d range-pos z vs 252d
def f07cy_f07_fiftytwo_week_cycle_position_rngposz_504d_jerk_v057_signal(closeadj):
    base = _z(_f07cy_range_pos(closeadj, 504), 252)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) share of quarter the 252d drawdown was worsening
def f07cy_f07_fiftytwo_week_cycle_position_ddworsen_252d_jerk_v058_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 252)
    base = (dd < dd.shift(1)).astype(float).rolling(63, min_periods=21).mean()
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d z-scored vs 126d) sign x sqrt magnitude of 504d recovery
def f07cy_f07_fiftytwo_week_cycle_position_recovsignmag_504d_jerk_v059_signal(closeadj):
    rec = _f07cy_recovery(closeadj, 504)
    base = np.sign(rec) * (rec.abs() ** 0.5)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) 252d recovery z vs 126d
def f07cy_f07_fiftytwo_week_cycle_position_recovz_252d_jerk_v060_signal(closeadj):
    base = _z(_f07cy_recovery(closeadj, 252), 126)
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) 252d off-floor z vs 252d
def f07cy_f07_fiftytwo_week_cycle_position_offfloorz_252d_jerk_v061_signal(closeadj):
    base = _z(_f07cy_prox_low(closeadj, 252), 252)
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 84d z-scored vs 126d) 1260d log-gap z vs 504d
def f07cy_f07_fiftytwo_week_cycle_position_deepgapz_1260d_jerk_v062_signal(closeadj):
    base = _z(_f07cy_loggap_high(closeadj, 1260), 504)
    d1 = base - base.shift(84)
    sl = d1 - d1.shift(84)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 84d z-scored vs 126d) 1260d log-amplitude z vs 252d
def f07cy_f07_fiftytwo_week_cycle_position_amplz_1260d_jerk_v063_signal(closeadj):
    hi = _rmax(closeadj, 1260)
    lo = _rmin(closeadj, 1260)
    base = _z(np.log(hi.replace(0, np.nan) / lo.replace(0, np.nan)), 252)
    d1 = base - base.shift(84)
    sl = d1 - d1.shift(84)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) 252d proximity-high rank vs 252d
def f07cy_f07_fiftytwo_week_cycle_position_proxhirank_252d_jerk_v064_signal(closeadj):
    base = _rank(_f07cy_prox_high(closeadj, 252), 252)
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) 252d range-pos rank vs 252d
def f07cy_f07_fiftytwo_week_cycle_position_rngposrank_252d_jerk_v065_signal(closeadj):
    base = _rank(_f07cy_range_pos(closeadj, 252), 252)
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d z-scored vs 126d) 504d range-pos rank vs 252d
def f07cy_f07_fiftytwo_week_cycle_position_rngposrank_504d_jerk_v066_signal(closeadj):
    base = _rank(_f07cy_range_pos(closeadj, 504), 252)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d z-scored vs 126d) 504d drawdown rank vs 504d
def f07cy_f07_fiftytwo_week_cycle_position_ddrank_504d_jerk_v067_signal(closeadj):
    base = _rank(_f07cy_drawdown(closeadj, 504), 504)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) 252d recovery rank vs 504d
def f07cy_f07_fiftytwo_week_cycle_position_recovrank_252d_jerk_v068_signal(closeadj):
    base = _rank(_f07cy_recovery(closeadj, 252), 504)
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 84d z-scored vs 126d) 1260d midpoint-skew rank vs 504d
def f07cy_f07_fiftytwo_week_cycle_position_midskewrank_1260d_jerk_v069_signal(closeadj):
    hi = _rmax(closeadj, 1260)
    lo = _rmin(closeadj, 1260)
    mid = (hi + lo) / 2.0
    base = _rank((closeadj - mid) / (hi - lo).replace(0, np.nan), 504)
    d1 = base - base.shift(84)
    sl = d1 - d1.shift(84)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) EMA-smoothed 252d range position
def f07cy_f07_fiftytwo_week_cycle_position_rngposema_252d_jerk_v070_signal(closeadj):
    base = _f07cy_range_pos(closeadj, 252).ewm(span=42, min_periods=21).mean()
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) 252d range-pos minus its slow EMA
def f07cy_f07_fiftytwo_week_cycle_position_rngposdisp_252d_jerk_v071_signal(closeadj):
    rp = _f07cy_range_pos(closeadj, 252)
    base = rp - rp.ewm(span=63, min_periods=21).mean()
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d z-scored vs 126d) EMA-smoothed 504d proximity to high
def f07cy_f07_fiftytwo_week_cycle_position_proxhiema_504d_jerk_v072_signal(closeadj):
    base = _f07cy_prox_high(closeadj, 504).ewm(span=63, min_periods=21).mean()
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) EMA-smoothed 252d log-gap to high
def f07cy_f07_fiftytwo_week_cycle_position_loggaphiema_252d_jerk_v073_signal(closeadj):
    base = _f07cy_loggap_high(closeadj, 252).ewm(span=21, min_periods=10).mean()
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) convex top-hug bias 252d
def f07cy_f07_fiftytwo_week_cycle_position_tophug_252d_jerk_v074_signal(closeadj):
    rp = _f07cy_range_pos(closeadj, 252)
    base = np.sign(rp - 0.5) * (rp - 0.5) ** 2 * 4.0
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) sign x sqrt magnitude of 252d drawdown
def f07cy_f07_fiftytwo_week_cycle_position_ddsignmag_252d_jerk_v075_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 252)
    base = np.sign(dd) * (dd.abs() ** 0.5)
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) cube of 252d drawdown
def f07cy_f07_fiftytwo_week_cycle_position_ddcube_252d_jerk_v076_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 252)
    base = dd ** 3 * 100.0
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) convex approach to 252d high (proximity above 0.8 squared)
def f07cy_f07_fiftytwo_week_cycle_position_approachconv_252d_jerk_v077_signal(closeadj):
    p = _f07cy_prox_high(closeadj, 252)
    e = (p - 0.8).clip(lower=0)
    base = e ** 2 * 25.0
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) 252d recovery/drawdown balance
def f07cy_f07_fiftytwo_week_cycle_position_vbalance_252d_jerk_v078_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 252).abs()
    rec = _f07cy_recovery(closeadj, 252)
    base = (rec - dd) / (rec + dd).replace(0, np.nan)
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d z-scored vs 126d) 504d recovery/drawdown balance
def f07cy_f07_fiftytwo_week_cycle_position_vbalance_504d_jerk_v079_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 504).abs()
    rec = _f07cy_recovery(closeadj, 504)
    base = (rec - dd) / (rec + dd).replace(0, np.nan)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d z-scored vs 126d) 252d-high / 504d-high freshness
def f07cy_f07_fiftytwo_week_cycle_position_anchfresh_504d_jerk_v080_signal(closeadj):
    base = _rmax(closeadj, 252) / _rmax(closeadj, 504).replace(0, np.nan)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d z-scored vs 126d) 504d minus 252d range position spread
def f07cy_f07_fiftytwo_week_cycle_position_posspr_504d_jerk_v081_signal(closeadj):
    base = _f07cy_range_pos(closeadj, 504) - _f07cy_range_pos(closeadj, 252)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 84d z-scored vs 126d) 252d minus 1260d recovery spread
def f07cy_f07_fiftytwo_week_cycle_position_recovspr_1260d_jerk_v082_signal(closeadj):
    base = _f07cy_recovery(closeadj, 252) - _f07cy_recovery(closeadj, 1260)
    d1 = base - base.shift(84)
    sl = d1 - d1.shift(84)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d z-scored vs 126d) 252d/504d drawdown ratio
def f07cy_f07_fiftytwo_week_cycle_position_ddratio_504d_jerk_v083_signal(closeadj):
    base = _f07cy_drawdown(closeadj, 252) / _f07cy_drawdown(closeadj, 504).replace(0, np.nan)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) 252d range amplitude / price
def f07cy_f07_fiftytwo_week_cycle_position_amplitude_252d_jerk_v084_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    base = (hi - lo) / closeadj.replace(0, np.nan)
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) 252d high extension over mean
def f07cy_f07_fiftytwo_week_cycle_position_hiextend_252d_jerk_v085_signal(closeadj):
    hi = _rmax(closeadj, 252)
    mn = _mean(closeadj, 252)
    base = (hi - mn) / mn.replace(0, np.nan)
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) 252d low extension under mean
def f07cy_f07_fiftytwo_week_cycle_position_loextend_252d_jerk_v086_signal(closeadj):
    lo = _rmin(closeadj, 252)
    mn = _mean(closeadj, 252)
    base = (mn - lo) / mn.replace(0, np.nan)
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) 252d ceiling-vs-floor extension asymmetry
def f07cy_f07_fiftytwo_week_cycle_position_extasym_252d_jerk_v087_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    mn = _mean(closeadj, 252)
    up = (hi - mn) / mn.replace(0, np.nan)
    dn = (mn - lo) / mn.replace(0, np.nan)
    base = (up - dn) / (up + dn).replace(0, np.nan)
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 84d z-scored vs 126d) log span 1260d-high vs 252d-low
def f07cy_f07_fiftytwo_week_cycle_position_span_1260d_jerk_v088_signal(closeadj):
    hi = _rmax(closeadj, 1260)
    lo = _rmin(closeadj, 252)
    base = np.log(hi.replace(0, np.nan) / lo.replace(0, np.nan))
    d1 = base - base.shift(84)
    sl = d1 - d1.shift(84)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) fraction of year within 5% of 252d high
def f07cy_f07_fiftytwo_week_cycle_position_nearhitime_252d_jerk_v089_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 252)
    base = (dd >= -0.05).astype(float).rolling(252, min_periods=126).mean()
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) fraction of year in upper third
def f07cy_f07_fiftytwo_week_cycle_position_uppertime_252d_jerk_v090_signal(closeadj):
    rp = _f07cy_range_pos(closeadj, 252)
    base = (rp >= 0.6667).astype(float).rolling(252, min_periods=126).mean()
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) fraction of year above the 252d midpoint
def f07cy_f07_fiftytwo_week_cycle_position_uppermidtime_252d_jerk_v091_signal(closeadj):
    rp = _f07cy_range_pos(closeadj, 252)
    base = (rp >= 0.5).astype(float).rolling(252, min_periods=126).mean()
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d z-scored vs 126d) fraction of year >10% below 504d high
def f07cy_f07_fiftytwo_week_cycle_position_underwater_504d_jerk_v092_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 504)
    base = (dd <= -0.10).astype(float).rolling(252, min_periods=126).mean()
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) fresh-252d-high rate over quarter
def f07cy_f07_fiftytwo_week_cycle_position_newhifreq_252d_jerk_v093_signal(closeadj):
    hi = closeadj.rolling(252, min_periods=126).max()
    base = (closeadj >= hi.shift(1) * 0.99999).astype(float).rolling(63, min_periods=21).mean()
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d z-scored vs 126d) cross-window range-pos dispersion 252/504/1260
def f07cy_f07_fiftytwo_week_cycle_position_posdisp_504d_jerk_v094_signal(closeadj):
    p1 = _f07cy_range_pos(closeadj, 252)
    p2 = _f07cy_range_pos(closeadj, 504)
    p3 = _f07cy_range_pos(closeadj, 1260)
    base = pd.concat([p1, p2, p3], axis=1).std(axis=1)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) quarter volatility of 252d range position
def f07cy_f07_fiftytwo_week_cycle_position_posvol_252d_jerk_v095_signal(closeadj):
    base = _f07cy_range_pos(closeadj, 252).rolling(63, min_periods=21).std()
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) 252d ulcer pain index over quarter
def f07cy_f07_fiftytwo_week_cycle_position_ulcer_252d_jerk_v096_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 252)
    base = (dd ** 2).rolling(63, min_periods=21).mean() ** 0.5
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) 252d net move vs total path efficiency
def f07cy_f07_fiftytwo_week_cycle_position_patheff_252d_jerk_v097_signal(closeadj):
    net = (closeadj - closeadj.shift(252)).abs()
    path = closeadj.diff().abs().rolling(252, min_periods=126).sum()
    base = net / path.replace(0, np.nan)
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d z-scored vs 126d) EMA of 504d log-gap off low
def f07cy_f07_fiftytwo_week_cycle_position_recovsmooth_504d_jerk_v098_signal(closeadj):
    base = _f07cy_loggap_low(closeadj, 504).ewm(span=42, min_periods=21).mean()
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 84d z-scored vs 126d) EMA of 1260d log-gap off low
def f07cy_f07_fiftytwo_week_cycle_position_loggaplosmooth_1260d_jerk_v099_signal(closeadj):
    base = _f07cy_loggap_low(closeadj, 1260).ewm(span=42, min_periods=21).mean()
    d1 = base - base.shift(84)
    sl = d1 - d1.shift(84)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) intraday 252d range position
def f07cy_f07_fiftytwo_week_cycle_position_hlrngpos_252d_jerk_v100_signal(closeadj, high, low):
    hi = high.rolling(252, min_periods=126).max()
    lo = low.rolling(252, min_periods=126).min()
    base = (closeadj - lo) / (hi - lo).replace(0, np.nan)
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) intraday true-low proximity rank vs 252d
def f07cy_f07_fiftytwo_week_cycle_position_trueproxlorank_252d_jerk_v101_signal(closeadj, low):
    lo = low.rolling(252, min_periods=126).min()
    base = _rank(closeadj / lo.replace(0, np.nan), 252)
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) ATR-scaled distance to 252d high
def f07cy_f07_fiftytwo_week_cycle_position_gapatr_252d_jerk_v102_signal(closeadj, high, low):
    hi = closeadj.rolling(252, min_periods=126).max()
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = (closeadj - hi) / atr.replace(0, np.nan)
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) ATR-scaled distance off 252d low
def f07cy_f07_fiftytwo_week_cycle_position_lowgapatr_252d_jerk_v103_signal(closeadj, high, low):
    lo = closeadj.rolling(252, min_periods=126).min()
    atr = (high - low).rolling(21, min_periods=5).mean()
    base = (closeadj - lo) / atr.replace(0, np.nan)
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 42d z-scored vs 126d) intraday-high premium over close-high (252d)
def f07cy_f07_fiftytwo_week_cycle_position_hipremium_252d_jerk_v104_signal(closeadj, high):
    ht = high.rolling(252, min_periods=126).max()
    hc = closeadj.rolling(252, min_periods=126).max()
    base = (ht - hc) / hc.replace(0, np.nan)
    d1 = base - base.shift(42)
    sl = d1 - d1.shift(42)
    result = _z(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) proximity to 252d high
def f07cy_f07_fiftytwo_week_cycle_position_proxhi_252d_jerk_v105_signal(closeadj):
    base = _f07cy_prox_high(closeadj, 252)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) proximity to 252d low
def f07cy_f07_fiftytwo_week_cycle_position_proxlo_252d_jerk_v106_signal(closeadj):
    base = _f07cy_prox_low(closeadj, 252)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 126d percentile-ranked vs 126d) 1260d cycle range position
def f07cy_f07_fiftytwo_week_cycle_position_rngpos_1260d_jerk_v107_signal(closeadj):
    base = _f07cy_range_pos(closeadj, 1260)
    d1 = base - base.shift(126)
    sl = d1 - d1.shift(126)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) 252d range-pos z vs 126d
def f07cy_f07_fiftytwo_week_cycle_position_rngposz_252d_jerk_v108_signal(closeadj):
    base = _z(_f07cy_range_pos(closeadj, 252), 126)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 84d percentile-ranked vs 126d) 504d range-pos z vs 252d
def f07cy_f07_fiftytwo_week_cycle_position_rngposz_504d_jerk_v109_signal(closeadj):
    base = _z(_f07cy_range_pos(closeadj, 504), 252)
    d1 = base - base.shift(84)
    sl = d1 - d1.shift(84)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) share of quarter the 252d drawdown was worsening
def f07cy_f07_fiftytwo_week_cycle_position_ddworsen_252d_jerk_v110_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 252)
    base = (dd < dd.shift(1)).astype(float).rolling(63, min_periods=21).mean()
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 84d percentile-ranked vs 126d) sign x sqrt magnitude of 504d recovery
def f07cy_f07_fiftytwo_week_cycle_position_recovsignmag_504d_jerk_v111_signal(closeadj):
    rec = _f07cy_recovery(closeadj, 504)
    base = np.sign(rec) * (rec.abs() ** 0.5)
    d1 = base - base.shift(84)
    sl = d1 - d1.shift(84)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) 252d recovery z vs 126d
def f07cy_f07_fiftytwo_week_cycle_position_recovz_252d_jerk_v112_signal(closeadj):
    base = _z(_f07cy_recovery(closeadj, 252), 126)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) 252d off-floor z vs 252d
def f07cy_f07_fiftytwo_week_cycle_position_offfloorz_252d_jerk_v113_signal(closeadj):
    base = _z(_f07cy_prox_low(closeadj, 252), 252)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 126d percentile-ranked vs 126d) 1260d log-gap z vs 504d
def f07cy_f07_fiftytwo_week_cycle_position_deepgapz_1260d_jerk_v114_signal(closeadj):
    base = _z(_f07cy_loggap_high(closeadj, 1260), 504)
    d1 = base - base.shift(126)
    sl = d1 - d1.shift(126)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 126d percentile-ranked vs 126d) 1260d log-amplitude z vs 252d
def f07cy_f07_fiftytwo_week_cycle_position_amplz_1260d_jerk_v115_signal(closeadj):
    hi = _rmax(closeadj, 1260)
    lo = _rmin(closeadj, 1260)
    base = _z(np.log(hi.replace(0, np.nan) / lo.replace(0, np.nan)), 252)
    d1 = base - base.shift(126)
    sl = d1 - d1.shift(126)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) 252d proximity-high rank vs 252d
def f07cy_f07_fiftytwo_week_cycle_position_proxhirank_252d_jerk_v116_signal(closeadj):
    base = _rank(_f07cy_prox_high(closeadj, 252), 252)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) 252d range-pos rank vs 252d
def f07cy_f07_fiftytwo_week_cycle_position_rngposrank_252d_jerk_v117_signal(closeadj):
    base = _rank(_f07cy_range_pos(closeadj, 252), 252)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 84d percentile-ranked vs 126d) 504d range-pos rank vs 252d
def f07cy_f07_fiftytwo_week_cycle_position_rngposrank_504d_jerk_v118_signal(closeadj):
    base = _rank(_f07cy_range_pos(closeadj, 504), 252)
    d1 = base - base.shift(84)
    sl = d1 - d1.shift(84)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 84d percentile-ranked vs 126d) 504d drawdown rank vs 504d
def f07cy_f07_fiftytwo_week_cycle_position_ddrank_504d_jerk_v119_signal(closeadj):
    base = _rank(_f07cy_drawdown(closeadj, 504), 504)
    d1 = base - base.shift(84)
    sl = d1 - d1.shift(84)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) 252d recovery rank vs 504d
def f07cy_f07_fiftytwo_week_cycle_position_recovrank_252d_jerk_v120_signal(closeadj):
    base = _rank(_f07cy_recovery(closeadj, 252), 504)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 126d percentile-ranked vs 126d) 1260d midpoint-skew rank vs 504d
def f07cy_f07_fiftytwo_week_cycle_position_midskewrank_1260d_jerk_v121_signal(closeadj):
    hi = _rmax(closeadj, 1260)
    lo = _rmin(closeadj, 1260)
    mid = (hi + lo) / 2.0
    base = _rank((closeadj - mid) / (hi - lo).replace(0, np.nan), 504)
    d1 = base - base.shift(126)
    sl = d1 - d1.shift(126)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) EMA-smoothed 252d range position
def f07cy_f07_fiftytwo_week_cycle_position_rngposema_252d_jerk_v122_signal(closeadj):
    base = _f07cy_range_pos(closeadj, 252).ewm(span=42, min_periods=21).mean()
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) 252d range-pos minus its slow EMA
def f07cy_f07_fiftytwo_week_cycle_position_rngposdisp_252d_jerk_v123_signal(closeadj):
    rp = _f07cy_range_pos(closeadj, 252)
    base = rp - rp.ewm(span=63, min_periods=21).mean()
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 84d percentile-ranked vs 126d) EMA-smoothed 504d proximity to high
def f07cy_f07_fiftytwo_week_cycle_position_proxhiema_504d_jerk_v124_signal(closeadj):
    base = _f07cy_prox_high(closeadj, 504).ewm(span=63, min_periods=21).mean()
    d1 = base - base.shift(84)
    sl = d1 - d1.shift(84)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) EMA-smoothed 252d log-gap to high
def f07cy_f07_fiftytwo_week_cycle_position_loggaphiema_252d_jerk_v125_signal(closeadj):
    base = _f07cy_loggap_high(closeadj, 252).ewm(span=21, min_periods=10).mean()
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) convex top-hug bias 252d
def f07cy_f07_fiftytwo_week_cycle_position_tophug_252d_jerk_v126_signal(closeadj):
    rp = _f07cy_range_pos(closeadj, 252)
    base = np.sign(rp - 0.5) * (rp - 0.5) ** 2 * 4.0
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) sign x sqrt magnitude of 252d drawdown
def f07cy_f07_fiftytwo_week_cycle_position_ddsignmag_252d_jerk_v127_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 252)
    base = np.sign(dd) * (dd.abs() ** 0.5)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) cube of 252d drawdown
def f07cy_f07_fiftytwo_week_cycle_position_ddcube_252d_jerk_v128_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 252)
    base = dd ** 3 * 100.0
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) convex approach to 252d high (proximity above 0.8 squared)
def f07cy_f07_fiftytwo_week_cycle_position_approachconv_252d_jerk_v129_signal(closeadj):
    p = _f07cy_prox_high(closeadj, 252)
    e = (p - 0.8).clip(lower=0)
    base = e ** 2 * 25.0
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) 252d recovery/drawdown balance
def f07cy_f07_fiftytwo_week_cycle_position_vbalance_252d_jerk_v130_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 252).abs()
    rec = _f07cy_recovery(closeadj, 252)
    base = (rec - dd) / (rec + dd).replace(0, np.nan)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 84d percentile-ranked vs 126d) 504d recovery/drawdown balance
def f07cy_f07_fiftytwo_week_cycle_position_vbalance_504d_jerk_v131_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 504).abs()
    rec = _f07cy_recovery(closeadj, 504)
    base = (rec - dd) / (rec + dd).replace(0, np.nan)
    d1 = base - base.shift(84)
    sl = d1 - d1.shift(84)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 84d percentile-ranked vs 126d) 252d-high / 504d-high freshness
def f07cy_f07_fiftytwo_week_cycle_position_anchfresh_504d_jerk_v132_signal(closeadj):
    base = _rmax(closeadj, 252) / _rmax(closeadj, 504).replace(0, np.nan)
    d1 = base - base.shift(84)
    sl = d1 - d1.shift(84)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 84d percentile-ranked vs 126d) 504d minus 252d range position spread
def f07cy_f07_fiftytwo_week_cycle_position_posspr_504d_jerk_v133_signal(closeadj):
    base = _f07cy_range_pos(closeadj, 504) - _f07cy_range_pos(closeadj, 252)
    d1 = base - base.shift(84)
    sl = d1 - d1.shift(84)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 126d percentile-ranked vs 126d) 252d minus 1260d recovery spread
def f07cy_f07_fiftytwo_week_cycle_position_recovspr_1260d_jerk_v134_signal(closeadj):
    base = _f07cy_recovery(closeadj, 252) - _f07cy_recovery(closeadj, 1260)
    d1 = base - base.shift(126)
    sl = d1 - d1.shift(126)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 84d percentile-ranked vs 126d) 252d/504d drawdown ratio
def f07cy_f07_fiftytwo_week_cycle_position_ddratio_504d_jerk_v135_signal(closeadj):
    base = _f07cy_drawdown(closeadj, 252) / _f07cy_drawdown(closeadj, 504).replace(0, np.nan)
    d1 = base - base.shift(84)
    sl = d1 - d1.shift(84)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) 252d range amplitude / price
def f07cy_f07_fiftytwo_week_cycle_position_amplitude_252d_jerk_v136_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    base = (hi - lo) / closeadj.replace(0, np.nan)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) 252d high extension over mean
def f07cy_f07_fiftytwo_week_cycle_position_hiextend_252d_jerk_v137_signal(closeadj):
    hi = _rmax(closeadj, 252)
    mn = _mean(closeadj, 252)
    base = (hi - mn) / mn.replace(0, np.nan)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) 252d low extension under mean
def f07cy_f07_fiftytwo_week_cycle_position_loextend_252d_jerk_v138_signal(closeadj):
    lo = _rmin(closeadj, 252)
    mn = _mean(closeadj, 252)
    base = (mn - lo) / mn.replace(0, np.nan)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) 252d ceiling-vs-floor extension asymmetry
def f07cy_f07_fiftytwo_week_cycle_position_extasym_252d_jerk_v139_signal(closeadj):
    hi = _rmax(closeadj, 252)
    lo = _rmin(closeadj, 252)
    mn = _mean(closeadj, 252)
    up = (hi - mn) / mn.replace(0, np.nan)
    dn = (mn - lo) / mn.replace(0, np.nan)
    base = (up - dn) / (up + dn).replace(0, np.nan)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 126d percentile-ranked vs 126d) log span 1260d-high vs 252d-low
def f07cy_f07_fiftytwo_week_cycle_position_span_1260d_jerk_v140_signal(closeadj):
    hi = _rmax(closeadj, 1260)
    lo = _rmin(closeadj, 252)
    base = np.log(hi.replace(0, np.nan) / lo.replace(0, np.nan))
    d1 = base - base.shift(126)
    sl = d1 - d1.shift(126)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) fraction of year within 5% of 252d high
def f07cy_f07_fiftytwo_week_cycle_position_nearhitime_252d_jerk_v141_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 252)
    base = (dd >= -0.05).astype(float).rolling(252, min_periods=126).mean()
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) fraction of year in upper third
def f07cy_f07_fiftytwo_week_cycle_position_uppertime_252d_jerk_v142_signal(closeadj):
    rp = _f07cy_range_pos(closeadj, 252)
    base = (rp >= 0.6667).astype(float).rolling(252, min_periods=126).mean()
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) fraction of year above the 252d midpoint
def f07cy_f07_fiftytwo_week_cycle_position_uppermidtime_252d_jerk_v143_signal(closeadj):
    rp = _f07cy_range_pos(closeadj, 252)
    base = (rp >= 0.5).astype(float).rolling(252, min_periods=126).mean()
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 84d percentile-ranked vs 126d) fraction of year >10% below 504d high
def f07cy_f07_fiftytwo_week_cycle_position_underwater_504d_jerk_v144_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 504)
    base = (dd <= -0.10).astype(float).rolling(252, min_periods=126).mean()
    d1 = base - base.shift(84)
    sl = d1 - d1.shift(84)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) fresh-252d-high rate over quarter
def f07cy_f07_fiftytwo_week_cycle_position_newhifreq_252d_jerk_v145_signal(closeadj):
    hi = closeadj.rolling(252, min_periods=126).max()
    base = (closeadj >= hi.shift(1) * 0.99999).astype(float).rolling(63, min_periods=21).mean()
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 84d percentile-ranked vs 126d) cross-window range-pos dispersion 252/504/1260
def f07cy_f07_fiftytwo_week_cycle_position_posdisp_504d_jerk_v146_signal(closeadj):
    p1 = _f07cy_range_pos(closeadj, 252)
    p2 = _f07cy_range_pos(closeadj, 504)
    p3 = _f07cy_range_pos(closeadj, 1260)
    base = pd.concat([p1, p2, p3], axis=1).std(axis=1)
    d1 = base - base.shift(84)
    sl = d1 - d1.shift(84)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) quarter volatility of 252d range position
def f07cy_f07_fiftytwo_week_cycle_position_posvol_252d_jerk_v147_signal(closeadj):
    base = _f07cy_range_pos(closeadj, 252).rolling(63, min_periods=21).std()
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) 252d ulcer pain index over quarter
def f07cy_f07_fiftytwo_week_cycle_position_ulcer_252d_jerk_v148_signal(closeadj):
    dd = _f07cy_drawdown(closeadj, 252)
    base = (dd ** 2).rolling(63, min_periods=21).mean() ** 0.5
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 63d percentile-ranked vs 126d) 252d net move vs total path efficiency
def f07cy_f07_fiftytwo_week_cycle_position_patheff_252d_jerk_v149_signal(closeadj):
    net = (closeadj - closeadj.shift(252)).abs()
    path = closeadj.diff().abs().rolling(252, min_periods=126).sum()
    base = net / path.replace(0, np.nan)
    d1 = base - base.shift(63)
    sl = d1 - d1.shift(63)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# jerk2d 84d percentile-ranked vs 126d) EMA of 504d log-gap off low
def f07cy_f07_fiftytwo_week_cycle_position_recovsmooth_504d_jerk_v150_signal(closeadj):
    base = _f07cy_loggap_low(closeadj, 504).ewm(span=42, min_periods=21).mean()
    d1 = base - base.shift(84)
    sl = d1 - d1.shift(84)
    result = _rank(sl, 126)
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f07cy_f07_fiftytwo_week_cycle_position_proxhi_252d_jerk_v001_signal,
    f07cy_f07_fiftytwo_week_cycle_position_proxlo_252d_jerk_v002_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rngpos_1260d_jerk_v003_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rngposz_252d_jerk_v004_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rngposz_504d_jerk_v005_signal,
    f07cy_f07_fiftytwo_week_cycle_position_ddworsen_252d_jerk_v006_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recovsignmag_504d_jerk_v007_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recovz_252d_jerk_v008_signal,
    f07cy_f07_fiftytwo_week_cycle_position_offfloorz_252d_jerk_v009_signal,
    f07cy_f07_fiftytwo_week_cycle_position_deepgapz_1260d_jerk_v010_signal,
    f07cy_f07_fiftytwo_week_cycle_position_amplz_1260d_jerk_v011_signal,
    f07cy_f07_fiftytwo_week_cycle_position_proxhirank_252d_jerk_v012_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rngposrank_252d_jerk_v013_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rngposrank_504d_jerk_v014_signal,
    f07cy_f07_fiftytwo_week_cycle_position_ddrank_504d_jerk_v015_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recovrank_252d_jerk_v016_signal,
    f07cy_f07_fiftytwo_week_cycle_position_midskewrank_1260d_jerk_v017_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rngposema_252d_jerk_v018_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rngposdisp_252d_jerk_v019_signal,
    f07cy_f07_fiftytwo_week_cycle_position_proxhiema_504d_jerk_v020_signal,
    f07cy_f07_fiftytwo_week_cycle_position_loggaphiema_252d_jerk_v021_signal,
    f07cy_f07_fiftytwo_week_cycle_position_tophug_252d_jerk_v022_signal,
    f07cy_f07_fiftytwo_week_cycle_position_ddsignmag_252d_jerk_v023_signal,
    f07cy_f07_fiftytwo_week_cycle_position_ddcube_252d_jerk_v024_signal,
    f07cy_f07_fiftytwo_week_cycle_position_approachconv_252d_jerk_v025_signal,
    f07cy_f07_fiftytwo_week_cycle_position_vbalance_252d_jerk_v026_signal,
    f07cy_f07_fiftytwo_week_cycle_position_vbalance_504d_jerk_v027_signal,
    f07cy_f07_fiftytwo_week_cycle_position_anchfresh_504d_jerk_v028_signal,
    f07cy_f07_fiftytwo_week_cycle_position_posspr_504d_jerk_v029_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recovspr_1260d_jerk_v030_signal,
    f07cy_f07_fiftytwo_week_cycle_position_ddratio_504d_jerk_v031_signal,
    f07cy_f07_fiftytwo_week_cycle_position_amplitude_252d_jerk_v032_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hiextend_252d_jerk_v033_signal,
    f07cy_f07_fiftytwo_week_cycle_position_loextend_252d_jerk_v034_signal,
    f07cy_f07_fiftytwo_week_cycle_position_extasym_252d_jerk_v035_signal,
    f07cy_f07_fiftytwo_week_cycle_position_span_1260d_jerk_v036_signal,
    f07cy_f07_fiftytwo_week_cycle_position_nearhitime_252d_jerk_v037_signal,
    f07cy_f07_fiftytwo_week_cycle_position_uppertime_252d_jerk_v038_signal,
    f07cy_f07_fiftytwo_week_cycle_position_uppermidtime_252d_jerk_v039_signal,
    f07cy_f07_fiftytwo_week_cycle_position_underwater_504d_jerk_v040_signal,
    f07cy_f07_fiftytwo_week_cycle_position_newhifreq_252d_jerk_v041_signal,
    f07cy_f07_fiftytwo_week_cycle_position_posdisp_504d_jerk_v042_signal,
    f07cy_f07_fiftytwo_week_cycle_position_posvol_252d_jerk_v043_signal,
    f07cy_f07_fiftytwo_week_cycle_position_ulcer_252d_jerk_v044_signal,
    f07cy_f07_fiftytwo_week_cycle_position_patheff_252d_jerk_v045_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recovsmooth_504d_jerk_v046_signal,
    f07cy_f07_fiftytwo_week_cycle_position_loggaplosmooth_1260d_jerk_v047_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hlrngpos_252d_jerk_v048_signal,
    f07cy_f07_fiftytwo_week_cycle_position_trueproxlorank_252d_jerk_v049_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapatr_252d_jerk_v050_signal,
    f07cy_f07_fiftytwo_week_cycle_position_lowgapatr_252d_jerk_v051_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hipremium_252d_jerk_v052_signal,
    f07cy_f07_fiftytwo_week_cycle_position_proxhi_252d_jerk_v053_signal,
    f07cy_f07_fiftytwo_week_cycle_position_proxlo_252d_jerk_v054_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rngpos_1260d_jerk_v055_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rngposz_252d_jerk_v056_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rngposz_504d_jerk_v057_signal,
    f07cy_f07_fiftytwo_week_cycle_position_ddworsen_252d_jerk_v058_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recovsignmag_504d_jerk_v059_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recovz_252d_jerk_v060_signal,
    f07cy_f07_fiftytwo_week_cycle_position_offfloorz_252d_jerk_v061_signal,
    f07cy_f07_fiftytwo_week_cycle_position_deepgapz_1260d_jerk_v062_signal,
    f07cy_f07_fiftytwo_week_cycle_position_amplz_1260d_jerk_v063_signal,
    f07cy_f07_fiftytwo_week_cycle_position_proxhirank_252d_jerk_v064_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rngposrank_252d_jerk_v065_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rngposrank_504d_jerk_v066_signal,
    f07cy_f07_fiftytwo_week_cycle_position_ddrank_504d_jerk_v067_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recovrank_252d_jerk_v068_signal,
    f07cy_f07_fiftytwo_week_cycle_position_midskewrank_1260d_jerk_v069_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rngposema_252d_jerk_v070_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rngposdisp_252d_jerk_v071_signal,
    f07cy_f07_fiftytwo_week_cycle_position_proxhiema_504d_jerk_v072_signal,
    f07cy_f07_fiftytwo_week_cycle_position_loggaphiema_252d_jerk_v073_signal,
    f07cy_f07_fiftytwo_week_cycle_position_tophug_252d_jerk_v074_signal,
    f07cy_f07_fiftytwo_week_cycle_position_ddsignmag_252d_jerk_v075_signal,
    f07cy_f07_fiftytwo_week_cycle_position_ddcube_252d_jerk_v076_signal,
    f07cy_f07_fiftytwo_week_cycle_position_approachconv_252d_jerk_v077_signal,
    f07cy_f07_fiftytwo_week_cycle_position_vbalance_252d_jerk_v078_signal,
    f07cy_f07_fiftytwo_week_cycle_position_vbalance_504d_jerk_v079_signal,
    f07cy_f07_fiftytwo_week_cycle_position_anchfresh_504d_jerk_v080_signal,
    f07cy_f07_fiftytwo_week_cycle_position_posspr_504d_jerk_v081_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recovspr_1260d_jerk_v082_signal,
    f07cy_f07_fiftytwo_week_cycle_position_ddratio_504d_jerk_v083_signal,
    f07cy_f07_fiftytwo_week_cycle_position_amplitude_252d_jerk_v084_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hiextend_252d_jerk_v085_signal,
    f07cy_f07_fiftytwo_week_cycle_position_loextend_252d_jerk_v086_signal,
    f07cy_f07_fiftytwo_week_cycle_position_extasym_252d_jerk_v087_signal,
    f07cy_f07_fiftytwo_week_cycle_position_span_1260d_jerk_v088_signal,
    f07cy_f07_fiftytwo_week_cycle_position_nearhitime_252d_jerk_v089_signal,
    f07cy_f07_fiftytwo_week_cycle_position_uppertime_252d_jerk_v090_signal,
    f07cy_f07_fiftytwo_week_cycle_position_uppermidtime_252d_jerk_v091_signal,
    f07cy_f07_fiftytwo_week_cycle_position_underwater_504d_jerk_v092_signal,
    f07cy_f07_fiftytwo_week_cycle_position_newhifreq_252d_jerk_v093_signal,
    f07cy_f07_fiftytwo_week_cycle_position_posdisp_504d_jerk_v094_signal,
    f07cy_f07_fiftytwo_week_cycle_position_posvol_252d_jerk_v095_signal,
    f07cy_f07_fiftytwo_week_cycle_position_ulcer_252d_jerk_v096_signal,
    f07cy_f07_fiftytwo_week_cycle_position_patheff_252d_jerk_v097_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recovsmooth_504d_jerk_v098_signal,
    f07cy_f07_fiftytwo_week_cycle_position_loggaplosmooth_1260d_jerk_v099_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hlrngpos_252d_jerk_v100_signal,
    f07cy_f07_fiftytwo_week_cycle_position_trueproxlorank_252d_jerk_v101_signal,
    f07cy_f07_fiftytwo_week_cycle_position_gapatr_252d_jerk_v102_signal,
    f07cy_f07_fiftytwo_week_cycle_position_lowgapatr_252d_jerk_v103_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hipremium_252d_jerk_v104_signal,
    f07cy_f07_fiftytwo_week_cycle_position_proxhi_252d_jerk_v105_signal,
    f07cy_f07_fiftytwo_week_cycle_position_proxlo_252d_jerk_v106_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rngpos_1260d_jerk_v107_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rngposz_252d_jerk_v108_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rngposz_504d_jerk_v109_signal,
    f07cy_f07_fiftytwo_week_cycle_position_ddworsen_252d_jerk_v110_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recovsignmag_504d_jerk_v111_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recovz_252d_jerk_v112_signal,
    f07cy_f07_fiftytwo_week_cycle_position_offfloorz_252d_jerk_v113_signal,
    f07cy_f07_fiftytwo_week_cycle_position_deepgapz_1260d_jerk_v114_signal,
    f07cy_f07_fiftytwo_week_cycle_position_amplz_1260d_jerk_v115_signal,
    f07cy_f07_fiftytwo_week_cycle_position_proxhirank_252d_jerk_v116_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rngposrank_252d_jerk_v117_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rngposrank_504d_jerk_v118_signal,
    f07cy_f07_fiftytwo_week_cycle_position_ddrank_504d_jerk_v119_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recovrank_252d_jerk_v120_signal,
    f07cy_f07_fiftytwo_week_cycle_position_midskewrank_1260d_jerk_v121_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rngposema_252d_jerk_v122_signal,
    f07cy_f07_fiftytwo_week_cycle_position_rngposdisp_252d_jerk_v123_signal,
    f07cy_f07_fiftytwo_week_cycle_position_proxhiema_504d_jerk_v124_signal,
    f07cy_f07_fiftytwo_week_cycle_position_loggaphiema_252d_jerk_v125_signal,
    f07cy_f07_fiftytwo_week_cycle_position_tophug_252d_jerk_v126_signal,
    f07cy_f07_fiftytwo_week_cycle_position_ddsignmag_252d_jerk_v127_signal,
    f07cy_f07_fiftytwo_week_cycle_position_ddcube_252d_jerk_v128_signal,
    f07cy_f07_fiftytwo_week_cycle_position_approachconv_252d_jerk_v129_signal,
    f07cy_f07_fiftytwo_week_cycle_position_vbalance_252d_jerk_v130_signal,
    f07cy_f07_fiftytwo_week_cycle_position_vbalance_504d_jerk_v131_signal,
    f07cy_f07_fiftytwo_week_cycle_position_anchfresh_504d_jerk_v132_signal,
    f07cy_f07_fiftytwo_week_cycle_position_posspr_504d_jerk_v133_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recovspr_1260d_jerk_v134_signal,
    f07cy_f07_fiftytwo_week_cycle_position_ddratio_504d_jerk_v135_signal,
    f07cy_f07_fiftytwo_week_cycle_position_amplitude_252d_jerk_v136_signal,
    f07cy_f07_fiftytwo_week_cycle_position_hiextend_252d_jerk_v137_signal,
    f07cy_f07_fiftytwo_week_cycle_position_loextend_252d_jerk_v138_signal,
    f07cy_f07_fiftytwo_week_cycle_position_extasym_252d_jerk_v139_signal,
    f07cy_f07_fiftytwo_week_cycle_position_span_1260d_jerk_v140_signal,
    f07cy_f07_fiftytwo_week_cycle_position_nearhitime_252d_jerk_v141_signal,
    f07cy_f07_fiftytwo_week_cycle_position_uppertime_252d_jerk_v142_signal,
    f07cy_f07_fiftytwo_week_cycle_position_uppermidtime_252d_jerk_v143_signal,
    f07cy_f07_fiftytwo_week_cycle_position_underwater_504d_jerk_v144_signal,
    f07cy_f07_fiftytwo_week_cycle_position_newhifreq_252d_jerk_v145_signal,
    f07cy_f07_fiftytwo_week_cycle_position_posdisp_504d_jerk_v146_signal,
    f07cy_f07_fiftytwo_week_cycle_position_posvol_252d_jerk_v147_signal,
    f07cy_f07_fiftytwo_week_cycle_position_ulcer_252d_jerk_v148_signal,
    f07cy_f07_fiftytwo_week_cycle_position_patheff_252d_jerk_v149_signal,
    f07cy_f07_fiftytwo_week_cycle_position_recovsmooth_504d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F07_FIFTYTWO_WEEK_CYCLE_POSITION_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.01, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")
    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}
    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)
    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)
    print("OK f07_fiftytwo_week_cycle_position_3rd_derivatives_001_150_claude: %d features pass" % n_features)
