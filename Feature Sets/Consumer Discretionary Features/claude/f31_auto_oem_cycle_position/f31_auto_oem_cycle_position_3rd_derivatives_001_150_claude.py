import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f31_revenue_cycle_phase(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return (revenue - m) / sd.replace(0, np.nan)


def _f31_margin_cycle_pos(ebitdamargin, w):
    lo = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).min()
    hi = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).max()
    return (ebitdamargin - lo) / (hi - lo).replace(0, np.nan)


def _f31_oem_cycle_score(revenue, ebitdamargin, w):
    rphase = _f31_revenue_cycle_phase(revenue, w)
    mpos = _f31_margin_cycle_pos(ebitdamargin, w)
    return rphase * mpos


# Group A v001-v030: jerk of phase × close
def f31aoc_f31_auto_oem_cycle_position_phase_63d_jerk_v001_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_63d_jerk_v002_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_63d_jerk_v003_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_63d_jerk_v004_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_63d_jerk_v005_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_126d_jerk_v006_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_126d_jerk_v007_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 126) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_126d_jerk_v008_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_126d_jerk_v009_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_126d_jerk_v010_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_252d_jerk_v011_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_252d_jerk_v012_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_252d_jerk_v013_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_252d_jerk_v014_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_252d_jerk_v015_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_504d_jerk_v016_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_504d_jerk_v017_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 504) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_504d_jerk_v018_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_504d_jerk_v019_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 504) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_504d_jerk_v020_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_378d_jerk_v021_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_378d_jerk_v022_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 378) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_378d_jerk_v023_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_378d_jerk_v024_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_378d_jerk_v025_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_21d_jerk_v026_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_21d_jerk_v027_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_21d_jerk_v028_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_42d_jerk_v029_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 42) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_42d_jerk_v030_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Group B v031-v060: jerks of margin cycle pos × closeadj
def f31aoc_f31_auto_oem_cycle_position_mpos_63d_jerk_v031_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_63d_jerk_v032_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_63d_jerk_v033_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_63d_jerk_v034_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_63d_jerk_v035_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_126d_jerk_v036_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_126d_jerk_v037_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 126) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_126d_jerk_v038_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_126d_jerk_v039_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_126d_jerk_v040_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_252d_jerk_v041_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_252d_jerk_v042_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_252d_jerk_v043_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_252d_jerk_v044_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_252d_jerk_v045_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_504d_jerk_v046_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_504d_jerk_v047_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 504) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_504d_jerk_v048_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_504d_jerk_v049_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 504) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_504d_jerk_v050_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_378d_jerk_v051_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_378d_jerk_v052_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 378) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_378d_jerk_v053_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_378d_jerk_v054_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_378d_jerk_v055_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_21d_jerk_v056_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_21d_jerk_v057_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_21d_jerk_v058_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_42d_jerk_v059_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 42) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_42d_jerk_v060_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Group C v061-v090: jerks of OEM cycle score × closeadj
def f31aoc_f31_auto_oem_cycle_position_score_63d_jerk_v061_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 63) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_63d_jerk_v062_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 63) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_63d_jerk_v063_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_63d_jerk_v064_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_63d_jerk_v065_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_126d_jerk_v066_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 126) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_126d_jerk_v067_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 126) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_126d_jerk_v068_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_126d_jerk_v069_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_126d_jerk_v070_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_252d_jerk_v071_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 252) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_252d_jerk_v072_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 252) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_252d_jerk_v073_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_252d_jerk_v074_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 252) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_252d_jerk_v075_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_504d_jerk_v076_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 504) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_504d_jerk_v077_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 504) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_504d_jerk_v078_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_504d_jerk_v079_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 504) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_504d_jerk_v080_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 504) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_378d_jerk_v081_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 378) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_378d_jerk_v082_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 378) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_378d_jerk_v083_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 378) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_378d_jerk_v084_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 378) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_378d_jerk_v085_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 378) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_21d_jerk_v086_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_21d_jerk_v087_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 21) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_21d_jerk_v088_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_42d_jerk_v089_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 42) * closeadj
    result = _jerk(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_42d_jerk_v090_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Group D v091-v120: jerks of complex bases
def f31aoc_f31_auto_oem_cycle_position_phase_x_capex_63d_jerk_v091_signal(revenue, capex, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 63) * _mean(capex, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capex_63d_jerk_v092_signal(revenue, capex, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 63) * _mean(capex, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capex_126d_jerk_v093_signal(revenue, capex, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 126) * _mean(capex, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capex_126d_jerk_v094_signal(revenue, capex, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 126) * _mean(capex, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capex_252d_jerk_v095_signal(revenue, capex, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 252) * _mean(capex, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capex_252d_jerk_v096_signal(revenue, capex, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 252) * _mean(capex, 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capex_504d_jerk_v097_signal(revenue, capex, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 504) * _mean(capex, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capex_504d_jerk_v098_signal(revenue, capex, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 504) * _mean(capex, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_63d_jerk_v099_signal(revenue, ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 63) * _mean(revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_63d_jerk_v100_signal(revenue, ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 63) * _mean(revenue, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_126d_jerk_v101_signal(revenue, ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 126) * _mean(revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_126d_jerk_v102_signal(revenue, ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 126) * _mean(revenue, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_252d_jerk_v103_signal(revenue, ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 252) * _mean(revenue, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_252d_jerk_v104_signal(revenue, ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 252) * _mean(revenue, 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_504d_jerk_v105_signal(revenue, ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 504) * _mean(revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_504d_jerk_v106_signal(revenue, ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 504) * _mean(revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_rev_63d_jerk_v107_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 63) * _mean(revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_rev_63d_jerk_v108_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 63) * _mean(revenue, 21) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_rev_126d_jerk_v109_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 126) * _mean(revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_rev_126d_jerk_v110_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 126) * _mean(revenue, 63) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_rev_252d_jerk_v111_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 252) * _mean(revenue, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_rev_252d_jerk_v112_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 252) * _mean(revenue, 126) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_rev_504d_jerk_v113_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 504) * _mean(revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_rev_504d_jerk_v114_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 504) * _mean(revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_rev_378d_jerk_v115_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 378) * _mean(revenue, 189) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_rev_378d_jerk_v116_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 378) * _mean(revenue, 189) * closeadj
    result = _jerk(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_signed_63d_jerk_v117_signal(revenue, ebitdamargin, closeadj):
    s = _f31_oem_cycle_score(revenue, ebitdamargin, 63)
    base = np.sign(s) * s.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_signed_126d_jerk_v118_signal(revenue, ebitdamargin, closeadj):
    s = _f31_oem_cycle_score(revenue, ebitdamargin, 126)
    base = np.sign(s) * s.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_signed_252d_jerk_v119_signal(revenue, ebitdamargin, closeadj):
    s = _f31_oem_cycle_score(revenue, ebitdamargin, 252)
    base = np.sign(s) * s.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_signed_504d_jerk_v120_signal(revenue, ebitdamargin, closeadj):
    s = _f31_oem_cycle_score(revenue, ebitdamargin, 504)
    base = np.sign(s) * s.abs() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Group E v121-v150: jerks of z / ema / other bases
def f31aoc_f31_auto_oem_cycle_position_phasez_63d_jerk_v121_signal(revenue, closeadj):
    base = _z(_f31_revenue_cycle_phase(revenue, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phasez_126d_jerk_v122_signal(revenue, closeadj):
    base = _z(_f31_revenue_cycle_phase(revenue, 126), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phasez_252d_jerk_v123_signal(revenue, closeadj):
    base = _z(_f31_revenue_cycle_phase(revenue, 252), 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mposz_63d_jerk_v124_signal(ebitdamargin, closeadj):
    base = _z(_f31_margin_cycle_pos(ebitdamargin, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mposz_126d_jerk_v125_signal(ebitdamargin, closeadj):
    base = _z(_f31_margin_cycle_pos(ebitdamargin, 126), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mposz_252d_jerk_v126_signal(ebitdamargin, closeadj):
    base = _z(_f31_margin_cycle_pos(ebitdamargin, 252), 504) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_ema_63d_jerk_v127_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 63).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_ema_126d_jerk_v128_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 126).ewm(span=42, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_ema_252d_jerk_v129_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 252).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_ema_63d_jerk_v130_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 63).ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_ema_126d_jerk_v131_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 126).ewm(span=42, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_ema_252d_jerk_v132_signal(ebitdamargin, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 252).ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_margin_63d_jerk_v133_signal(revenue, ebitdamargin, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 63) * _mean(ebitdamargin, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_margin_126d_jerk_v134_signal(revenue, ebitdamargin, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 126) * _mean(ebitdamargin, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_margin_252d_jerk_v135_signal(revenue, ebitdamargin, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 252) * _mean(ebitdamargin, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_revgrow_63d_jerk_v136_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 63) * revenue.pct_change(63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_revgrow_126d_jerk_v137_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 126) * revenue.pct_change(126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_revgrow_252d_jerk_v138_signal(revenue, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 252) * revenue.pct_change(252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_div_63d_jerk_v139_signal(revenue, ebitdamargin, closeadj):
    p = _f31_revenue_cycle_phase(revenue, 63)
    m = _f31_margin_cycle_pos(ebitdamargin, 63)
    base = (p - 2.0 * m + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_div_126d_jerk_v140_signal(revenue, ebitdamargin, closeadj):
    p = _f31_revenue_cycle_phase(revenue, 126)
    m = _f31_margin_cycle_pos(ebitdamargin, 126)
    base = (p - 2.0 * m + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_div_252d_jerk_v141_signal(revenue, ebitdamargin, closeadj):
    p = _f31_revenue_cycle_phase(revenue, 252)
    m = _f31_margin_cycle_pos(ebitdamargin, 252)
    base = (p - 2.0 * m + 1.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capexz_63d_jerk_v142_signal(revenue, capex, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 63) * _z(capex, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capexz_126d_jerk_v143_signal(revenue, capex, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 126) * _z(capex, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_phase_x_capexz_252d_jerk_v144_signal(revenue, capex, closeadj):
    base = _f31_revenue_cycle_phase(revenue, 252) * _z(capex, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_margin_63d_jerk_v145_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 63) * ebitdamargin * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_margin_126d_jerk_v146_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 126) * ebitdamargin * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_score_x_margin_252d_jerk_v147_signal(revenue, ebitdamargin, closeadj):
    base = _f31_oem_cycle_score(revenue, ebitdamargin, 252) * ebitdamargin * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_capex_63d_jerk_v148_signal(ebitdamargin, capex, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 63) * _mean(capex, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_capex_126d_jerk_v149_signal(ebitdamargin, capex, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 126) * _mean(capex, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f31aoc_f31_auto_oem_cycle_position_mpos_x_capex_252d_jerk_v150_signal(ebitdamargin, capex, closeadj):
    base = _f31_margin_cycle_pos(ebitdamargin, 252) * _mean(capex, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31aoc_f31_auto_oem_cycle_position_phase_63d_jerk_v001_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_63d_jerk_v002_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_63d_jerk_v003_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_63d_jerk_v004_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_63d_jerk_v005_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_126d_jerk_v006_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_126d_jerk_v007_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_126d_jerk_v008_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_126d_jerk_v009_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_126d_jerk_v010_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_252d_jerk_v011_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_252d_jerk_v012_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_252d_jerk_v013_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_252d_jerk_v014_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_252d_jerk_v015_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_504d_jerk_v016_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_504d_jerk_v017_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_504d_jerk_v018_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_504d_jerk_v019_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_504d_jerk_v020_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_378d_jerk_v021_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_378d_jerk_v022_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_378d_jerk_v023_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_378d_jerk_v024_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_378d_jerk_v025_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_21d_jerk_v026_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_21d_jerk_v027_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_21d_jerk_v028_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_42d_jerk_v029_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_42d_jerk_v030_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_63d_jerk_v031_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_63d_jerk_v032_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_63d_jerk_v033_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_63d_jerk_v034_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_63d_jerk_v035_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_126d_jerk_v036_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_126d_jerk_v037_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_126d_jerk_v038_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_126d_jerk_v039_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_126d_jerk_v040_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_252d_jerk_v041_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_252d_jerk_v042_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_252d_jerk_v043_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_252d_jerk_v044_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_252d_jerk_v045_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_504d_jerk_v046_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_504d_jerk_v047_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_504d_jerk_v048_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_504d_jerk_v049_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_504d_jerk_v050_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_378d_jerk_v051_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_378d_jerk_v052_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_378d_jerk_v053_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_378d_jerk_v054_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_378d_jerk_v055_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_21d_jerk_v056_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_21d_jerk_v057_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_21d_jerk_v058_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_42d_jerk_v059_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_42d_jerk_v060_signal,
    f31aoc_f31_auto_oem_cycle_position_score_63d_jerk_v061_signal,
    f31aoc_f31_auto_oem_cycle_position_score_63d_jerk_v062_signal,
    f31aoc_f31_auto_oem_cycle_position_score_63d_jerk_v063_signal,
    f31aoc_f31_auto_oem_cycle_position_score_63d_jerk_v064_signal,
    f31aoc_f31_auto_oem_cycle_position_score_63d_jerk_v065_signal,
    f31aoc_f31_auto_oem_cycle_position_score_126d_jerk_v066_signal,
    f31aoc_f31_auto_oem_cycle_position_score_126d_jerk_v067_signal,
    f31aoc_f31_auto_oem_cycle_position_score_126d_jerk_v068_signal,
    f31aoc_f31_auto_oem_cycle_position_score_126d_jerk_v069_signal,
    f31aoc_f31_auto_oem_cycle_position_score_126d_jerk_v070_signal,
    f31aoc_f31_auto_oem_cycle_position_score_252d_jerk_v071_signal,
    f31aoc_f31_auto_oem_cycle_position_score_252d_jerk_v072_signal,
    f31aoc_f31_auto_oem_cycle_position_score_252d_jerk_v073_signal,
    f31aoc_f31_auto_oem_cycle_position_score_252d_jerk_v074_signal,
    f31aoc_f31_auto_oem_cycle_position_score_252d_jerk_v075_signal,
    f31aoc_f31_auto_oem_cycle_position_score_504d_jerk_v076_signal,
    f31aoc_f31_auto_oem_cycle_position_score_504d_jerk_v077_signal,
    f31aoc_f31_auto_oem_cycle_position_score_504d_jerk_v078_signal,
    f31aoc_f31_auto_oem_cycle_position_score_504d_jerk_v079_signal,
    f31aoc_f31_auto_oem_cycle_position_score_504d_jerk_v080_signal,
    f31aoc_f31_auto_oem_cycle_position_score_378d_jerk_v081_signal,
    f31aoc_f31_auto_oem_cycle_position_score_378d_jerk_v082_signal,
    f31aoc_f31_auto_oem_cycle_position_score_378d_jerk_v083_signal,
    f31aoc_f31_auto_oem_cycle_position_score_378d_jerk_v084_signal,
    f31aoc_f31_auto_oem_cycle_position_score_378d_jerk_v085_signal,
    f31aoc_f31_auto_oem_cycle_position_score_21d_jerk_v086_signal,
    f31aoc_f31_auto_oem_cycle_position_score_21d_jerk_v087_signal,
    f31aoc_f31_auto_oem_cycle_position_score_21d_jerk_v088_signal,
    f31aoc_f31_auto_oem_cycle_position_score_42d_jerk_v089_signal,
    f31aoc_f31_auto_oem_cycle_position_score_42d_jerk_v090_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capex_63d_jerk_v091_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capex_63d_jerk_v092_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capex_126d_jerk_v093_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capex_126d_jerk_v094_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capex_252d_jerk_v095_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capex_252d_jerk_v096_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capex_504d_jerk_v097_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capex_504d_jerk_v098_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_63d_jerk_v099_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_63d_jerk_v100_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_126d_jerk_v101_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_126d_jerk_v102_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_252d_jerk_v103_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_252d_jerk_v104_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_504d_jerk_v105_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_rev_504d_jerk_v106_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_rev_63d_jerk_v107_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_rev_63d_jerk_v108_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_rev_126d_jerk_v109_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_rev_126d_jerk_v110_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_rev_252d_jerk_v111_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_rev_252d_jerk_v112_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_rev_504d_jerk_v113_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_rev_504d_jerk_v114_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_rev_378d_jerk_v115_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_rev_378d_jerk_v116_signal,
    f31aoc_f31_auto_oem_cycle_position_score_signed_63d_jerk_v117_signal,
    f31aoc_f31_auto_oem_cycle_position_score_signed_126d_jerk_v118_signal,
    f31aoc_f31_auto_oem_cycle_position_score_signed_252d_jerk_v119_signal,
    f31aoc_f31_auto_oem_cycle_position_score_signed_504d_jerk_v120_signal,
    f31aoc_f31_auto_oem_cycle_position_phasez_63d_jerk_v121_signal,
    f31aoc_f31_auto_oem_cycle_position_phasez_126d_jerk_v122_signal,
    f31aoc_f31_auto_oem_cycle_position_phasez_252d_jerk_v123_signal,
    f31aoc_f31_auto_oem_cycle_position_mposz_63d_jerk_v124_signal,
    f31aoc_f31_auto_oem_cycle_position_mposz_126d_jerk_v125_signal,
    f31aoc_f31_auto_oem_cycle_position_mposz_252d_jerk_v126_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_ema_63d_jerk_v127_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_ema_126d_jerk_v128_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_ema_252d_jerk_v129_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_ema_63d_jerk_v130_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_ema_126d_jerk_v131_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_ema_252d_jerk_v132_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_margin_63d_jerk_v133_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_margin_126d_jerk_v134_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_margin_252d_jerk_v135_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_revgrow_63d_jerk_v136_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_revgrow_126d_jerk_v137_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_revgrow_252d_jerk_v138_signal,
    f31aoc_f31_auto_oem_cycle_position_div_63d_jerk_v139_signal,
    f31aoc_f31_auto_oem_cycle_position_div_126d_jerk_v140_signal,
    f31aoc_f31_auto_oem_cycle_position_div_252d_jerk_v141_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capexz_63d_jerk_v142_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capexz_126d_jerk_v143_signal,
    f31aoc_f31_auto_oem_cycle_position_phase_x_capexz_252d_jerk_v144_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_margin_63d_jerk_v145_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_margin_126d_jerk_v146_signal,
    f31aoc_f31_auto_oem_cycle_position_score_x_margin_252d_jerk_v147_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_capex_63d_jerk_v148_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_capex_126d_jerk_v149_signal,
    f31aoc_f31_auto_oem_cycle_position_mpos_x_capex_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_AUTO_OEM_CYCLE_POSITION_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    capex = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")

    cols = {"closeadj": closeadj, "revenue": revenue, "capex": capex, "ebitdamargin": ebitdamargin}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f31_revenue_cycle_phase", "_f31_margin_cycle_pos", "_f31_oem_cycle_score")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f31_auto_oem_cycle_position_3rd_derivatives_001_150_claude: {n_features} features pass")
