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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


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
def _f49_quality_composite(roic, fcf, revenue, w):
    rq = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    fy = fcf / revenue.replace(0, np.nan)
    fy_m = fy.rolling(w, min_periods=max(1, w // 2)).mean()
    return rq * fy_m


def _f49_compounder_score(roic, ebitdamargin, w):
    rq = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    eq = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return rq + eq


def _f49_terminal_quality(fcf, revenue, dps, w):
    fg = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    rg = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    dg = dps.rolling(w, min_periods=max(1, w // 2)).mean()
    return (fg / rg.replace(0, np.nan)) * dg


# ===== features =====
def f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s00_sw21_slope_v001_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 5)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s00_sw63_slope_v002_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 5)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s00_sw126_slope_v003_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 5)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_5d_s00_sw21_slope_v004_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 5)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_5d_s00_sw63_slope_v005_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 5)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_5d_s00_sw126_slope_v006_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 5)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_5d_s00_sw21_slope_v007_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 5)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_5d_s00_sw63_slope_v008_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 5)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_5d_s00_sw126_slope_v009_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 5)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_10d_s00_sw21_slope_v010_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 10)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_10d_s00_sw63_slope_v011_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 10)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_10d_s00_sw126_slope_v012_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 10)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_10d_s00_sw21_slope_v013_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 10)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_10d_s00_sw63_slope_v014_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 10)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_10d_s00_sw126_slope_v015_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 10)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_10d_s00_sw21_slope_v016_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 10)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_10d_s00_sw63_slope_v017_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 10)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_10d_s00_sw126_slope_v018_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 10)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_21d_s00_sw21_slope_v019_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_21d_s00_sw63_slope_v020_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_21d_s00_sw126_slope_v021_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_21d_s00_sw21_slope_v022_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 21)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_21d_s00_sw63_slope_v023_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 21)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_21d_s00_sw126_slope_v024_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_21d_s00_sw21_slope_v025_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_21d_s00_sw63_slope_v026_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_21d_s00_sw126_slope_v027_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 21)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_42d_s00_sw21_slope_v028_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 42)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_42d_s00_sw63_slope_v029_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 42)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_42d_s00_sw126_slope_v030_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 42)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_42d_s00_sw21_slope_v031_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 42)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_42d_s00_sw63_slope_v032_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 42)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_42d_s00_sw126_slope_v033_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 42)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_42d_s00_sw21_slope_v034_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 42)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_42d_s00_sw63_slope_v035_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 42)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_42d_s00_sw126_slope_v036_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 42)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_63d_s00_sw21_slope_v037_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_63d_s00_sw63_slope_v038_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_63d_s00_sw126_slope_v039_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 63)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_63d_s00_sw21_slope_v040_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 63)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_63d_s00_sw63_slope_v041_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 63)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_63d_s00_sw126_slope_v042_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_63d_s00_sw21_slope_v043_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_63d_s00_sw63_slope_v044_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_63d_s00_sw126_slope_v045_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 63)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_84d_s00_sw21_slope_v046_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 84)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_84d_s00_sw63_slope_v047_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 84)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_84d_s00_sw126_slope_v048_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 84)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_84d_s00_sw21_slope_v049_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 84)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_84d_s00_sw63_slope_v050_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 84)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_84d_s00_sw126_slope_v051_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 84)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_84d_s00_sw21_slope_v052_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 84)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_84d_s00_sw63_slope_v053_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 84)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_84d_s00_sw126_slope_v054_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 84)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s00_sw21_slope_v055_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 105)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s00_sw63_slope_v056_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 105)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s00_sw126_slope_v057_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 105)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_105d_s00_sw21_slope_v058_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 105)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_105d_s00_sw63_slope_v059_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 105)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_105d_s00_sw126_slope_v060_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 105)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_105d_s00_sw21_slope_v061_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 105)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_105d_s00_sw63_slope_v062_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 105)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_105d_s00_sw126_slope_v063_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 105)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s00_sw21_slope_v064_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 126)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s00_sw63_slope_v065_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 126)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s00_sw126_slope_v066_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 126)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_126d_s00_sw21_slope_v067_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 126)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_126d_s00_sw63_slope_v068_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 126)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_126d_s00_sw126_slope_v069_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 126)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_126d_s00_sw21_slope_v070_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 126)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_126d_s00_sw63_slope_v071_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 126)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_126d_s00_sw126_slope_v072_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 126)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s00_sw21_slope_v073_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 147)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s00_sw63_slope_v074_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 147)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s00_sw126_slope_v075_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 147)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_147d_s00_sw21_slope_v076_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 147)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_147d_s00_sw63_slope_v077_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 147)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_147d_s00_sw126_slope_v078_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 147)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_147d_s00_sw21_slope_v079_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 147)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_147d_s00_sw63_slope_v080_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 147)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_147d_s00_sw126_slope_v081_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 147)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_168d_s00_sw21_slope_v082_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 168)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_168d_s00_sw63_slope_v083_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 168)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_168d_s00_sw126_slope_v084_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 168)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_168d_s00_sw21_slope_v085_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 168)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_168d_s00_sw63_slope_v086_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 168)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_168d_s00_sw126_slope_v087_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 168)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_168d_s00_sw21_slope_v088_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 168)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_168d_s00_sw63_slope_v089_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 168)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_168d_s00_sw126_slope_v090_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 168)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_189d_s00_sw21_slope_v091_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 189)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_189d_s00_sw63_slope_v092_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 189)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_189d_s00_sw126_slope_v093_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 189)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_189d_s00_sw21_slope_v094_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 189)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_189d_s00_sw63_slope_v095_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 189)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_189d_s00_sw126_slope_v096_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 189)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_189d_s00_sw21_slope_v097_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 189)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_189d_s00_sw63_slope_v098_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 189)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_189d_s00_sw126_slope_v099_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 189)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_210d_s00_sw21_slope_v100_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 210)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_210d_s00_sw63_slope_v101_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 210)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_210d_s00_sw126_slope_v102_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 210)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_210d_s00_sw21_slope_v103_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 210)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_210d_s00_sw63_slope_v104_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 210)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_210d_s00_sw126_slope_v105_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 210)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_210d_s00_sw21_slope_v106_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 210)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_210d_s00_sw63_slope_v107_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 210)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_210d_s00_sw126_slope_v108_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 210)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_231d_s00_sw21_slope_v109_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 231)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_231d_s00_sw63_slope_v110_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 231)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_231d_s00_sw126_slope_v111_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 231)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_231d_s00_sw21_slope_v112_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 231)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_231d_s00_sw63_slope_v113_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 231)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_231d_s00_sw126_slope_v114_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 231)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_231d_s00_sw21_slope_v115_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 231)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_231d_s00_sw63_slope_v116_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 231)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_231d_s00_sw126_slope_v117_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 231)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_252d_s00_sw21_slope_v118_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 252)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_252d_s00_sw63_slope_v119_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 252)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_252d_s00_sw126_slope_v120_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 252)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_252d_s00_sw21_slope_v121_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 252)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_252d_s00_sw63_slope_v122_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 252)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_252d_s00_sw126_slope_v123_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 252)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_252d_s00_sw21_slope_v124_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 252)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_252d_s00_sw63_slope_v125_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 252)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_252d_s00_sw126_slope_v126_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 252)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_294d_s00_sw21_slope_v127_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 294)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_294d_s00_sw63_slope_v128_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 294)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_294d_s00_sw126_slope_v129_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 294)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_294d_s00_sw21_slope_v130_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 294)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_294d_s00_sw63_slope_v131_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 294)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_294d_s00_sw126_slope_v132_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 294)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_294d_s00_sw21_slope_v133_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 294)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_294d_s00_sw63_slope_v134_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 294)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_294d_s00_sw126_slope_v135_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 294)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_336d_s00_sw21_slope_v136_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 336)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_336d_s00_sw63_slope_v137_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 336)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_336d_s00_sw126_slope_v138_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 336)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_336d_s00_sw21_slope_v139_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 336)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_336d_s00_sw63_slope_v140_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 336)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_336d_s00_sw126_slope_v141_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 336)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_336d_s00_sw21_slope_v142_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 336)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_336d_s00_sw63_slope_v143_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 336)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_336d_s00_sw126_slope_v144_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 336)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_378d_s00_sw21_slope_v145_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 378)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_378d_s00_sw63_slope_v146_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 378)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_378d_s00_sw126_slope_v147_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 378)
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_378d_s00_sw21_slope_v148_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 378)
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_378d_s00_sw63_slope_v149_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 378)
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_378d_s00_sw126_slope_v150_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 378)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s00_sw21_slope_v001_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s00_sw63_slope_v002_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s00_sw126_slope_v003_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_5d_s00_sw21_slope_v004_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_5d_s00_sw63_slope_v005_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_5d_s00_sw126_slope_v006_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_5d_s00_sw21_slope_v007_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_5d_s00_sw63_slope_v008_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_5d_s00_sw126_slope_v009_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_10d_s00_sw21_slope_v010_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_10d_s00_sw63_slope_v011_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_10d_s00_sw126_slope_v012_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_10d_s00_sw21_slope_v013_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_10d_s00_sw63_slope_v014_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_10d_s00_sw126_slope_v015_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_10d_s00_sw21_slope_v016_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_10d_s00_sw63_slope_v017_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_10d_s00_sw126_slope_v018_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_21d_s00_sw21_slope_v019_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_21d_s00_sw63_slope_v020_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_21d_s00_sw126_slope_v021_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_21d_s00_sw21_slope_v022_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_21d_s00_sw63_slope_v023_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_21d_s00_sw126_slope_v024_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_21d_s00_sw21_slope_v025_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_21d_s00_sw63_slope_v026_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_21d_s00_sw126_slope_v027_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_42d_s00_sw21_slope_v028_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_42d_s00_sw63_slope_v029_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_42d_s00_sw126_slope_v030_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_42d_s00_sw21_slope_v031_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_42d_s00_sw63_slope_v032_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_42d_s00_sw126_slope_v033_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_42d_s00_sw21_slope_v034_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_42d_s00_sw63_slope_v035_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_42d_s00_sw126_slope_v036_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_63d_s00_sw21_slope_v037_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_63d_s00_sw63_slope_v038_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_63d_s00_sw126_slope_v039_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_63d_s00_sw21_slope_v040_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_63d_s00_sw63_slope_v041_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_63d_s00_sw126_slope_v042_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_63d_s00_sw21_slope_v043_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_63d_s00_sw63_slope_v044_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_63d_s00_sw126_slope_v045_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_84d_s00_sw21_slope_v046_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_84d_s00_sw63_slope_v047_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_84d_s00_sw126_slope_v048_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_84d_s00_sw21_slope_v049_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_84d_s00_sw63_slope_v050_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_84d_s00_sw126_slope_v051_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_84d_s00_sw21_slope_v052_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_84d_s00_sw63_slope_v053_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_84d_s00_sw126_slope_v054_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s00_sw21_slope_v055_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s00_sw63_slope_v056_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s00_sw126_slope_v057_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_105d_s00_sw21_slope_v058_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_105d_s00_sw63_slope_v059_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_105d_s00_sw126_slope_v060_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_105d_s00_sw21_slope_v061_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_105d_s00_sw63_slope_v062_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_105d_s00_sw126_slope_v063_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s00_sw21_slope_v064_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s00_sw63_slope_v065_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s00_sw126_slope_v066_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_126d_s00_sw21_slope_v067_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_126d_s00_sw63_slope_v068_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_126d_s00_sw126_slope_v069_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_126d_s00_sw21_slope_v070_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_126d_s00_sw63_slope_v071_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_126d_s00_sw126_slope_v072_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s00_sw21_slope_v073_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s00_sw63_slope_v074_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s00_sw126_slope_v075_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_147d_s00_sw21_slope_v076_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_147d_s00_sw63_slope_v077_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_147d_s00_sw126_slope_v078_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_147d_s00_sw21_slope_v079_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_147d_s00_sw63_slope_v080_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_147d_s00_sw126_slope_v081_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_168d_s00_sw21_slope_v082_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_168d_s00_sw63_slope_v083_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_168d_s00_sw126_slope_v084_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_168d_s00_sw21_slope_v085_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_168d_s00_sw63_slope_v086_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_168d_s00_sw126_slope_v087_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_168d_s00_sw21_slope_v088_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_168d_s00_sw63_slope_v089_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_168d_s00_sw126_slope_v090_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_189d_s00_sw21_slope_v091_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_189d_s00_sw63_slope_v092_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_189d_s00_sw126_slope_v093_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_189d_s00_sw21_slope_v094_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_189d_s00_sw63_slope_v095_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_189d_s00_sw126_slope_v096_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_189d_s00_sw21_slope_v097_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_189d_s00_sw63_slope_v098_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_189d_s00_sw126_slope_v099_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_210d_s00_sw21_slope_v100_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_210d_s00_sw63_slope_v101_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_210d_s00_sw126_slope_v102_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_210d_s00_sw21_slope_v103_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_210d_s00_sw63_slope_v104_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_210d_s00_sw126_slope_v105_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_210d_s00_sw21_slope_v106_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_210d_s00_sw63_slope_v107_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_210d_s00_sw126_slope_v108_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_231d_s00_sw21_slope_v109_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_231d_s00_sw63_slope_v110_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_231d_s00_sw126_slope_v111_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_231d_s00_sw21_slope_v112_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_231d_s00_sw63_slope_v113_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_231d_s00_sw126_slope_v114_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_231d_s00_sw21_slope_v115_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_231d_s00_sw63_slope_v116_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_231d_s00_sw126_slope_v117_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_252d_s00_sw21_slope_v118_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_252d_s00_sw63_slope_v119_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_252d_s00_sw126_slope_v120_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_252d_s00_sw21_slope_v121_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_252d_s00_sw63_slope_v122_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_252d_s00_sw126_slope_v123_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_252d_s00_sw21_slope_v124_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_252d_s00_sw63_slope_v125_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_252d_s00_sw126_slope_v126_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_294d_s00_sw21_slope_v127_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_294d_s00_sw63_slope_v128_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_294d_s00_sw126_slope_v129_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_294d_s00_sw21_slope_v130_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_294d_s00_sw63_slope_v131_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_294d_s00_sw126_slope_v132_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_294d_s00_sw21_slope_v133_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_294d_s00_sw63_slope_v134_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_294d_s00_sw126_slope_v135_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_336d_s00_sw21_slope_v136_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_336d_s00_sw63_slope_v137_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_336d_s00_sw126_slope_v138_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_336d_s00_sw21_slope_v139_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_336d_s00_sw63_slope_v140_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_336d_s00_sw126_slope_v141_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_336d_s00_sw21_slope_v142_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_336d_s00_sw63_slope_v143_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_336d_s00_sw126_slope_v144_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_378d_s00_sw21_slope_v145_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_378d_s00_sw63_slope_v146_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_378d_s00_sw126_slope_v147_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_378d_s00_sw21_slope_v148_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_378d_s00_sw63_slope_v149_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_378d_s00_sw126_slope_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_UTILITY_TERMINAL_COMPOUNDER_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    dps     = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    roic    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    cols = {"closeadj": closeadj, "dps": dps, "ebitdamargin": ebitdamargin, "fcf": fcf, "revenue": revenue, "roic": roic}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f49_quality_composite", "_f49_compounder_score", "_f49_terminal_quality",)
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
    print(f"OK f49_utility_terminal_compounder_2nd_derivatives_001_150_claude: {n_features} features pass")
