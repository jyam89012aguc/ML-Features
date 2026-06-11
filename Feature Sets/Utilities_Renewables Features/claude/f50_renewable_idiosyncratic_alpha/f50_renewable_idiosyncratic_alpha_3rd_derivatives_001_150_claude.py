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
def _f50_quality_composite(roic, fcf, revenue, w):
    rq = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    fy = fcf / revenue.replace(0, np.nan)
    fy_m = fy.rolling(w, min_periods=max(1, w // 2)).mean()
    return rq + fy_m


def _f50_idiosyncratic_signal(closeadj, revenue, w):
    pr = closeadj.pct_change(w)
    rg = revenue.pct_change(w)
    return pr - rg


def _f50_alpha_score(roic, ebitdamargin, w):
    rq = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    em = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return rq * em


# ===== features =====
def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_5d_s00_jw21_jerk_v001_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 5)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_5d_s00_jw63_jerk_v002_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 5)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_5d_s00_jw126_jerk_v003_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 5)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_5d_s00_jw21_jerk_v004_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 5)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_5d_s00_jw63_jerk_v005_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 5)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_5d_s00_jw126_jerk_v006_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 5)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_5d_s00_jw21_jerk_v007_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 5)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_5d_s00_jw63_jerk_v008_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 5)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_5d_s00_jw126_jerk_v009_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 5)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_10d_s00_jw21_jerk_v010_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 10)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_10d_s00_jw63_jerk_v011_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 10)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_10d_s00_jw126_jerk_v012_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 10)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_10d_s00_jw21_jerk_v013_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 10)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_10d_s00_jw63_jerk_v014_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 10)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_10d_s00_jw126_jerk_v015_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 10)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_10d_s00_jw21_jerk_v016_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 10)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_10d_s00_jw63_jerk_v017_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 10)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_10d_s00_jw126_jerk_v018_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 10)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_21d_s00_jw21_jerk_v019_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_21d_s00_jw63_jerk_v020_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_21d_s00_jw126_jerk_v021_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_21d_s00_jw21_jerk_v022_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_21d_s00_jw63_jerk_v023_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_21d_s00_jw126_jerk_v024_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_21d_s00_jw21_jerk_v025_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_21d_s00_jw63_jerk_v026_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_21d_s00_jw126_jerk_v027_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_42d_s00_jw21_jerk_v028_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_42d_s00_jw63_jerk_v029_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 42)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_42d_s00_jw126_jerk_v030_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 42)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_42d_s00_jw21_jerk_v031_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_42d_s00_jw63_jerk_v032_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 42)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_42d_s00_jw126_jerk_v033_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 42)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_42d_s00_jw21_jerk_v034_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_42d_s00_jw63_jerk_v035_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 42)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_42d_s00_jw126_jerk_v036_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 42)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_63d_s00_jw21_jerk_v037_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_63d_s00_jw63_jerk_v038_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_63d_s00_jw126_jerk_v039_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_63d_s00_jw21_jerk_v040_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_63d_s00_jw63_jerk_v041_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_63d_s00_jw126_jerk_v042_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_63d_s00_jw21_jerk_v043_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_63d_s00_jw63_jerk_v044_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_63d_s00_jw126_jerk_v045_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_84d_s00_jw21_jerk_v046_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 84)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_84d_s00_jw63_jerk_v047_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 84)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_84d_s00_jw126_jerk_v048_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 84)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_84d_s00_jw21_jerk_v049_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 84)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_84d_s00_jw63_jerk_v050_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 84)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_84d_s00_jw126_jerk_v051_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 84)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_84d_s00_jw21_jerk_v052_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 84)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_84d_s00_jw63_jerk_v053_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 84)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_84d_s00_jw126_jerk_v054_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 84)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s00_jw21_jerk_v055_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 105)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s00_jw63_jerk_v056_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 105)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s00_jw126_jerk_v057_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 105)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s00_jw21_jerk_v058_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 105)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s00_jw63_jerk_v059_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 105)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s00_jw126_jerk_v060_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 105)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s00_jw21_jerk_v061_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 105)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s00_jw63_jerk_v062_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 105)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s00_jw126_jerk_v063_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 105)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s00_jw21_jerk_v064_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s00_jw63_jerk_v065_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s00_jw126_jerk_v066_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 126)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s00_jw21_jerk_v067_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s00_jw63_jerk_v068_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s00_jw126_jerk_v069_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 126)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s00_jw21_jerk_v070_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s00_jw63_jerk_v071_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s00_jw126_jerk_v072_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 126)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s00_jw21_jerk_v073_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 147)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s00_jw63_jerk_v074_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 147)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s00_jw126_jerk_v075_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 147)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s00_jw21_jerk_v076_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 147)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s00_jw63_jerk_v077_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 147)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s00_jw126_jerk_v078_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 147)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_147d_s00_jw21_jerk_v079_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 147)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_147d_s00_jw63_jerk_v080_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 147)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_147d_s00_jw126_jerk_v081_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 147)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_168d_s00_jw21_jerk_v082_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 168)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_168d_s00_jw63_jerk_v083_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 168)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_168d_s00_jw126_jerk_v084_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 168)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_168d_s00_jw21_jerk_v085_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 168)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_168d_s00_jw63_jerk_v086_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 168)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_168d_s00_jw126_jerk_v087_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 168)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_168d_s00_jw21_jerk_v088_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 168)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_168d_s00_jw63_jerk_v089_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 168)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_168d_s00_jw126_jerk_v090_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 168)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_189d_s00_jw21_jerk_v091_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 189)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_189d_s00_jw63_jerk_v092_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 189)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_189d_s00_jw126_jerk_v093_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 189)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_189d_s00_jw21_jerk_v094_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 189)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_189d_s00_jw63_jerk_v095_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 189)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_189d_s00_jw126_jerk_v096_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 189)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_189d_s00_jw21_jerk_v097_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 189)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_189d_s00_jw63_jerk_v098_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 189)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_189d_s00_jw126_jerk_v099_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 189)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_210d_s00_jw21_jerk_v100_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 210)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_210d_s00_jw63_jerk_v101_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 210)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_210d_s00_jw126_jerk_v102_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 210)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_210d_s00_jw21_jerk_v103_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 210)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_210d_s00_jw63_jerk_v104_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 210)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_210d_s00_jw126_jerk_v105_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 210)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_210d_s00_jw21_jerk_v106_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 210)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_210d_s00_jw63_jerk_v107_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 210)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_210d_s00_jw126_jerk_v108_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 210)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_231d_s00_jw21_jerk_v109_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 231)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_231d_s00_jw63_jerk_v110_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 231)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_231d_s00_jw126_jerk_v111_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 231)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_231d_s00_jw21_jerk_v112_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 231)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_231d_s00_jw63_jerk_v113_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 231)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_231d_s00_jw126_jerk_v114_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 231)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_231d_s00_jw21_jerk_v115_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 231)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_231d_s00_jw63_jerk_v116_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 231)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_231d_s00_jw126_jerk_v117_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 231)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_252d_s00_jw21_jerk_v118_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_252d_s00_jw63_jerk_v119_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_252d_s00_jw126_jerk_v120_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_252d_s00_jw21_jerk_v121_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_252d_s00_jw63_jerk_v122_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_252d_s00_jw126_jerk_v123_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_252d_s00_jw21_jerk_v124_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_252d_s00_jw63_jerk_v125_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_252d_s00_jw126_jerk_v126_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_294d_s00_jw21_jerk_v127_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 294)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_294d_s00_jw63_jerk_v128_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 294)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_294d_s00_jw126_jerk_v129_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 294)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_294d_s00_jw21_jerk_v130_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 294)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_294d_s00_jw63_jerk_v131_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 294)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_294d_s00_jw126_jerk_v132_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 294)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_294d_s00_jw21_jerk_v133_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 294)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_294d_s00_jw63_jerk_v134_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 294)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_294d_s00_jw126_jerk_v135_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 294)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_336d_s00_jw21_jerk_v136_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 336)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_336d_s00_jw63_jerk_v137_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 336)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_336d_s00_jw126_jerk_v138_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 336)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_336d_s00_jw21_jerk_v139_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 336)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_336d_s00_jw63_jerk_v140_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 336)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_336d_s00_jw126_jerk_v141_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 336)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_336d_s00_jw21_jerk_v142_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 336)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_336d_s00_jw63_jerk_v143_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 336)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_as_re_336d_s00_jw126_jerk_v144_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f50_alpha_score(roic, ebitdamargin, 336)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_378d_s00_jw21_jerk_v145_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 378)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_378d_s00_jw63_jerk_v146_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 378)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_378d_s00_jw126_jerk_v147_signal(roic, fcf, revenue, closeadj):
    base = _f50_quality_composite(roic, fcf, revenue, 378)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_378d_s00_jw21_jerk_v148_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 378)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_378d_s00_jw63_jerk_v149_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 378)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f50ria_f50_renewable_idiosyncratic_alpha_is_cr_378d_s00_jw126_jerk_v150_signal(closeadj, revenue, roic, fcf):
    base = _f50_idiosyncratic_signal(closeadj, revenue, 378)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_5d_s00_jw21_jerk_v001_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_5d_s00_jw63_jerk_v002_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_5d_s00_jw126_jerk_v003_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_5d_s00_jw21_jerk_v004_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_5d_s00_jw63_jerk_v005_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_5d_s00_jw126_jerk_v006_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_5d_s00_jw21_jerk_v007_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_5d_s00_jw63_jerk_v008_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_5d_s00_jw126_jerk_v009_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_10d_s00_jw21_jerk_v010_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_10d_s00_jw63_jerk_v011_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_10d_s00_jw126_jerk_v012_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_10d_s00_jw21_jerk_v013_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_10d_s00_jw63_jerk_v014_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_10d_s00_jw126_jerk_v015_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_10d_s00_jw21_jerk_v016_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_10d_s00_jw63_jerk_v017_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_10d_s00_jw126_jerk_v018_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_21d_s00_jw21_jerk_v019_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_21d_s00_jw63_jerk_v020_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_21d_s00_jw126_jerk_v021_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_21d_s00_jw21_jerk_v022_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_21d_s00_jw63_jerk_v023_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_21d_s00_jw126_jerk_v024_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_21d_s00_jw21_jerk_v025_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_21d_s00_jw63_jerk_v026_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_21d_s00_jw126_jerk_v027_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_42d_s00_jw21_jerk_v028_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_42d_s00_jw63_jerk_v029_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_42d_s00_jw126_jerk_v030_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_42d_s00_jw21_jerk_v031_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_42d_s00_jw63_jerk_v032_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_42d_s00_jw126_jerk_v033_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_42d_s00_jw21_jerk_v034_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_42d_s00_jw63_jerk_v035_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_42d_s00_jw126_jerk_v036_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_63d_s00_jw21_jerk_v037_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_63d_s00_jw63_jerk_v038_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_63d_s00_jw126_jerk_v039_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_63d_s00_jw21_jerk_v040_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_63d_s00_jw63_jerk_v041_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_63d_s00_jw126_jerk_v042_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_63d_s00_jw21_jerk_v043_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_63d_s00_jw63_jerk_v044_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_63d_s00_jw126_jerk_v045_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_84d_s00_jw21_jerk_v046_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_84d_s00_jw63_jerk_v047_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_84d_s00_jw126_jerk_v048_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_84d_s00_jw21_jerk_v049_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_84d_s00_jw63_jerk_v050_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_84d_s00_jw126_jerk_v051_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_84d_s00_jw21_jerk_v052_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_84d_s00_jw63_jerk_v053_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_84d_s00_jw126_jerk_v054_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s00_jw21_jerk_v055_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s00_jw63_jerk_v056_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_105d_s00_jw126_jerk_v057_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s00_jw21_jerk_v058_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s00_jw63_jerk_v059_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_105d_s00_jw126_jerk_v060_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s00_jw21_jerk_v061_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s00_jw63_jerk_v062_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_105d_s00_jw126_jerk_v063_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s00_jw21_jerk_v064_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s00_jw63_jerk_v065_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_126d_s00_jw126_jerk_v066_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s00_jw21_jerk_v067_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s00_jw63_jerk_v068_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_126d_s00_jw126_jerk_v069_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s00_jw21_jerk_v070_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s00_jw63_jerk_v071_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_126d_s00_jw126_jerk_v072_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s00_jw21_jerk_v073_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s00_jw63_jerk_v074_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_147d_s00_jw126_jerk_v075_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s00_jw21_jerk_v076_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s00_jw63_jerk_v077_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_147d_s00_jw126_jerk_v078_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_147d_s00_jw21_jerk_v079_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_147d_s00_jw63_jerk_v080_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_147d_s00_jw126_jerk_v081_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_168d_s00_jw21_jerk_v082_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_168d_s00_jw63_jerk_v083_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_168d_s00_jw126_jerk_v084_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_168d_s00_jw21_jerk_v085_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_168d_s00_jw63_jerk_v086_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_168d_s00_jw126_jerk_v087_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_168d_s00_jw21_jerk_v088_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_168d_s00_jw63_jerk_v089_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_168d_s00_jw126_jerk_v090_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_189d_s00_jw21_jerk_v091_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_189d_s00_jw63_jerk_v092_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_189d_s00_jw126_jerk_v093_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_189d_s00_jw21_jerk_v094_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_189d_s00_jw63_jerk_v095_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_189d_s00_jw126_jerk_v096_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_189d_s00_jw21_jerk_v097_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_189d_s00_jw63_jerk_v098_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_189d_s00_jw126_jerk_v099_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_210d_s00_jw21_jerk_v100_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_210d_s00_jw63_jerk_v101_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_210d_s00_jw126_jerk_v102_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_210d_s00_jw21_jerk_v103_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_210d_s00_jw63_jerk_v104_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_210d_s00_jw126_jerk_v105_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_210d_s00_jw21_jerk_v106_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_210d_s00_jw63_jerk_v107_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_210d_s00_jw126_jerk_v108_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_231d_s00_jw21_jerk_v109_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_231d_s00_jw63_jerk_v110_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_231d_s00_jw126_jerk_v111_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_231d_s00_jw21_jerk_v112_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_231d_s00_jw63_jerk_v113_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_231d_s00_jw126_jerk_v114_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_231d_s00_jw21_jerk_v115_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_231d_s00_jw63_jerk_v116_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_231d_s00_jw126_jerk_v117_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_252d_s00_jw21_jerk_v118_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_252d_s00_jw63_jerk_v119_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_252d_s00_jw126_jerk_v120_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_252d_s00_jw21_jerk_v121_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_252d_s00_jw63_jerk_v122_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_252d_s00_jw126_jerk_v123_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_252d_s00_jw21_jerk_v124_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_252d_s00_jw63_jerk_v125_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_252d_s00_jw126_jerk_v126_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_294d_s00_jw21_jerk_v127_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_294d_s00_jw63_jerk_v128_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_294d_s00_jw126_jerk_v129_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_294d_s00_jw21_jerk_v130_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_294d_s00_jw63_jerk_v131_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_294d_s00_jw126_jerk_v132_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_294d_s00_jw21_jerk_v133_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_294d_s00_jw63_jerk_v134_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_294d_s00_jw126_jerk_v135_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_336d_s00_jw21_jerk_v136_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_336d_s00_jw63_jerk_v137_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_336d_s00_jw126_jerk_v138_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_336d_s00_jw21_jerk_v139_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_336d_s00_jw63_jerk_v140_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_336d_s00_jw126_jerk_v141_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_336d_s00_jw21_jerk_v142_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_336d_s00_jw63_jerk_v143_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_as_re_336d_s00_jw126_jerk_v144_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_378d_s00_jw21_jerk_v145_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_378d_s00_jw63_jerk_v146_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_qc_rfr_378d_s00_jw126_jerk_v147_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_378d_s00_jw21_jerk_v148_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_378d_s00_jw63_jerk_v149_signal,
    f50ria_f50_renewable_idiosyncratic_alpha_is_cr_378d_s00_jw126_jerk_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F50_RENEWABLE_IDIOSYNCRATIC_ALPHA_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    roic    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    cols = {"closeadj": closeadj, "ebitdamargin": ebitdamargin, "fcf": fcf, "revenue": revenue, "roic": roic}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f50_quality_composite", "_f50_idiosyncratic_signal", "_f50_alpha_score",)
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
    print(f"OK f50_renewable_idiosyncratic_alpha_3rd_derivatives_001_150_claude: {n_features} features pass")
