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
def _f50_quality_composite(roic, fcf, revenue, w):
    rq = roic.rolling(w, min_periods=max(2, w // 2)).mean()
    fy = fcf / revenue.replace(0, np.nan).abs()
    fq = fy.rolling(w, min_periods=max(2, w // 2)).mean()
    return rq * fq


def _f50_idiosyncratic_signal(closeadj, revenue, w):
    pr = closeadj.pct_change(periods=w)
    rg = revenue.pct_change(periods=w)
    return (pr - rg) * closeadj


def _f50_alpha_score(roic, ebitdamargin, w):
    rq = roic.rolling(w, min_periods=max(2, w // 2)).mean()
    mq = ebitdamargin.rolling(w, min_periods=max(2, w // 2)).mean()
    return (rq - rq.rolling(w, min_periods=max(2, w // 2)).mean()) + (mq - mq.rolling(w, min_periods=max(2, w // 2)).mean())



def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_raw_21_jk5_jerk_v001_signal(roic, fcf, revenue):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_f50_quality_composite(roic, fcf, revenue, 5))
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_raw_21_jk10_jerk_v002_signal(roic, fcf, revenue):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_f50_quality_composite(roic, fcf, revenue, 5))
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_raw_21_jk21_jerk_v003_signal(roic, fcf, revenue):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_f50_quality_composite(roic, fcf, revenue, 5))
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_raw_21_jk42_jerk_v004_signal(roic, fcf, revenue):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_f50_quality_composite(roic, fcf, revenue, 5))
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_raw_21_jk63_jerk_v005_signal(roic, fcf, revenue):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_f50_quality_composite(roic, fcf, revenue, 5))
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_raw_21_jk126_jerk_v006_signal(roic, fcf, revenue):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_f50_quality_composite(roic, fcf, revenue, 5))
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_scXclose_21_jk5_jerk_v007_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_scXclose_21_jk10_jerk_v008_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_scXclose_21_jk21_jerk_v009_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_scXclose_21_jk42_jerk_v010_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_scXclose_21_jk63_jerk_v011_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_scXclose_21_jk126_jerk_v012_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_logabs_21_jk5_jerk_v013_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.log((_f50_quality_composite(roic, fcf, revenue, 5)).abs() + 1.0) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_logabs_21_jk10_jerk_v014_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.log((_f50_quality_composite(roic, fcf, revenue, 5)).abs() + 1.0) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_logabs_21_jk21_jerk_v015_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.log((_f50_quality_composite(roic, fcf, revenue, 5)).abs() + 1.0) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_logabs_21_jk42_jerk_v016_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.log((_f50_quality_composite(roic, fcf, revenue, 5)).abs() + 1.0) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_logabs_21_jk63_jerk_v017_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.log((_f50_quality_composite(roic, fcf, revenue, 5)).abs() + 1.0) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_logabs_21_jk126_jerk_v018_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.log((_f50_quality_composite(roic, fcf, revenue, 5)).abs() + 1.0) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_sign_21_jk5_jerk_v019_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f50_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_sign_21_jk10_jerk_v020_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f50_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_sign_21_jk21_jerk_v021_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f50_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_sign_21_jk42_jerk_v022_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f50_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_sign_21_jk63_jerk_v023_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f50_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_sign_21_jk126_jerk_v024_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f50_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_signsq_21_jk5_jerk_v025_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f50_quality_composite(roic, fcf, revenue, 5)) * (_f50_quality_composite(roic, fcf, revenue, 5)).pow(2) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_signsq_21_jk10_jerk_v026_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f50_quality_composite(roic, fcf, revenue, 5)) * (_f50_quality_composite(roic, fcf, revenue, 5)).pow(2) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_signsq_21_jk21_jerk_v027_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f50_quality_composite(roic, fcf, revenue, 5)) * (_f50_quality_composite(roic, fcf, revenue, 5)).pow(2) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_signsq_21_jk42_jerk_v028_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f50_quality_composite(roic, fcf, revenue, 5)) * (_f50_quality_composite(roic, fcf, revenue, 5)).pow(2) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_signsq_21_jk63_jerk_v029_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f50_quality_composite(roic, fcf, revenue, 5)) * (_f50_quality_composite(roic, fcf, revenue, 5)).pow(2) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_signsq_21_jk126_jerk_v030_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f50_quality_composite(roic, fcf, revenue, 5)) * (_f50_quality_composite(roic, fcf, revenue, 5)).pow(2) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_21_jk5_jerk_v031_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_21_jk10_jerk_v032_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_21_jk21_jerk_v033_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_21_jk42_jerk_v034_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_21_jk63_jerk_v035_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_21_jk126_jerk_v036_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_42_jk5_jerk_v037_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_42_jk10_jerk_v038_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_42_jk21_jerk_v039_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_42_jk42_jerk_v040_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_42_jk63_jerk_v041_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_42_jk126_jerk_v042_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_63_jk5_jerk_v043_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_63_jk10_jerk_v044_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_63_jk21_jerk_v045_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_63_jk42_jerk_v046_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_63_jk63_jerk_v047_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_63_jk126_jerk_v048_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_126_jk5_jerk_v049_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_126_jk10_jerk_v050_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_126_jk21_jerk_v051_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_126_jk42_jerk_v052_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_126_jk63_jerk_v053_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_126_jk126_jerk_v054_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f50_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_21_jk5_jerk_v055_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_21_jk10_jerk_v056_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_21_jk21_jerk_v057_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_21_jk42_jerk_v058_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_21_jk63_jerk_v059_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_21_jk126_jerk_v060_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_42_jk5_jerk_v061_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_42_jk10_jerk_v062_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_42_jk21_jerk_v063_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_42_jk42_jerk_v064_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_42_jk63_jerk_v065_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_42_jk126_jerk_v066_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_63_jk5_jerk_v067_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_63_jk10_jerk_v068_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_63_jk21_jerk_v069_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_63_jk42_jerk_v070_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_63_jk63_jerk_v071_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_63_jk126_jerk_v072_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_126_jk5_jerk_v073_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_126_jk10_jerk_v074_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_126_jk21_jerk_v075_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_126_jk42_jerk_v076_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_126_jk63_jerk_v077_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_126_jk126_jerk_v078_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f50_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_21_jk5_jerk_v079_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_21_jk10_jerk_v080_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_21_jk21_jerk_v081_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_21_jk42_jerk_v082_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_21_jk63_jerk_v083_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_21_jk126_jerk_v084_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_42_jk5_jerk_v085_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_42_jk10_jerk_v086_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_42_jk21_jerk_v087_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_42_jk42_jerk_v088_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_42_jk63_jerk_v089_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_42_jk126_jerk_v090_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_63_jk5_jerk_v091_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_63_jk10_jerk_v092_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_63_jk21_jerk_v093_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_63_jk42_jerk_v094_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_63_jk63_jerk_v095_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_63_jk126_jerk_v096_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_126_jk5_jerk_v097_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_126_jk10_jerk_v098_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_126_jk21_jerk_v099_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_126_jk42_jerk_v100_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_126_jk63_jerk_v101_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_126_jk126_jerk_v102_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f50_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_21_jk5_jerk_v103_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_21_jk10_jerk_v104_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_21_jk21_jerk_v105_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_21_jk42_jerk_v106_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_21_jk63_jerk_v107_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_21_jk126_jerk_v108_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_42_jk5_jerk_v109_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_42_jk10_jerk_v110_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_42_jk21_jerk_v111_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_42_jk42_jerk_v112_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_42_jk63_jerk_v113_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_42_jk126_jerk_v114_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_63_jk5_jerk_v115_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=63, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_63_jk10_jerk_v116_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=63, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_63_jk21_jerk_v117_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=63, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_63_jk42_jerk_v118_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=63, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_63_jk63_jerk_v119_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=63, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_63_jk126_jerk_v120_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=63, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_126_jk5_jerk_v121_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=126, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_126_jk10_jerk_v122_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=126, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_126_jk21_jerk_v123_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=126, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_126_jk42_jerk_v124_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=126, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_126_jk63_jerk_v125_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=126, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_126_jk126_jerk_v126_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).ewm(span=126, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_21_jk5_jerk_v127_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(21, min_periods=max(2, 21 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_21_jk10_jerk_v128_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(21, min_periods=max(2, 21 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_21_jk21_jerk_v129_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(21, min_periods=max(2, 21 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_21_jk42_jerk_v130_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(21, min_periods=max(2, 21 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_21_jk63_jerk_v131_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(21, min_periods=max(2, 21 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_21_jk126_jerk_v132_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(21, min_periods=max(2, 21 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_42_jk5_jerk_v133_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(42, min_periods=max(2, 42 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_42_jk10_jerk_v134_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(42, min_periods=max(2, 42 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_42_jk21_jerk_v135_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(42, min_periods=max(2, 42 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_42_jk42_jerk_v136_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(42, min_periods=max(2, 42 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_42_jk63_jerk_v137_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(42, min_periods=max(2, 42 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_42_jk126_jerk_v138_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(42, min_periods=max(2, 42 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_63_jk5_jerk_v139_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_63_jk10_jerk_v140_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_63_jk21_jerk_v141_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_63_jk42_jerk_v142_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_63_jk63_jerk_v143_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_63_jk126_jerk_v144_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_126_jk5_jerk_v145_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_126_jk10_jerk_v146_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_126_jk21_jerk_v147_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_126_jk42_jerk_v148_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_126_jk63_jerk_v149_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_126_jk126_jerk_v150_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f50_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f50_quality_composite(roic, fcf, revenue, 5)).rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_raw_21_jk5_jerk_v001_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_raw_21_jk10_jerk_v002_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_raw_21_jk21_jerk_v003_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_raw_21_jk42_jerk_v004_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_raw_21_jk63_jerk_v005_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_raw_21_jk126_jerk_v006_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_scXclose_21_jk5_jerk_v007_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_scXclose_21_jk10_jerk_v008_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_scXclose_21_jk21_jerk_v009_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_scXclose_21_jk42_jerk_v010_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_scXclose_21_jk63_jerk_v011_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_scXclose_21_jk126_jerk_v012_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_logabs_21_jk5_jerk_v013_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_logabs_21_jk10_jerk_v014_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_logabs_21_jk21_jerk_v015_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_logabs_21_jk42_jerk_v016_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_logabs_21_jk63_jerk_v017_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_logabs_21_jk126_jerk_v018_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_sign_21_jk5_jerk_v019_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_sign_21_jk10_jerk_v020_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_sign_21_jk21_jerk_v021_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_sign_21_jk42_jerk_v022_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_sign_21_jk63_jerk_v023_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_sign_21_jk126_jerk_v024_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_signsq_21_jk5_jerk_v025_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_signsq_21_jk10_jerk_v026_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_signsq_21_jk21_jerk_v027_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_signsq_21_jk42_jerk_v028_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_signsq_21_jk63_jerk_v029_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_signsq_21_jk126_jerk_v030_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_21_jk5_jerk_v031_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_21_jk10_jerk_v032_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_21_jk21_jerk_v033_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_21_jk42_jerk_v034_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_21_jk63_jerk_v035_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_21_jk126_jerk_v036_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_42_jk5_jerk_v037_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_42_jk10_jerk_v038_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_42_jk21_jerk_v039_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_42_jk42_jerk_v040_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_42_jk63_jerk_v041_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_42_jk126_jerk_v042_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_63_jk5_jerk_v043_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_63_jk10_jerk_v044_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_63_jk21_jerk_v045_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_63_jk42_jerk_v046_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_63_jk63_jerk_v047_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_63_jk126_jerk_v048_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_126_jk5_jerk_v049_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_126_jk10_jerk_v050_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_126_jk21_jerk_v051_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_126_jk42_jerk_v052_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_126_jk63_jerk_v053_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_zN_126_jk126_jerk_v054_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_21_jk5_jerk_v055_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_21_jk10_jerk_v056_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_21_jk21_jerk_v057_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_21_jk42_jerk_v058_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_21_jk63_jerk_v059_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_21_jk126_jerk_v060_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_42_jk5_jerk_v061_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_42_jk10_jerk_v062_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_42_jk21_jerk_v063_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_42_jk42_jerk_v064_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_42_jk63_jerk_v065_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_42_jk126_jerk_v066_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_63_jk5_jerk_v067_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_63_jk10_jerk_v068_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_63_jk21_jerk_v069_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_63_jk42_jerk_v070_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_63_jk63_jerk_v071_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_63_jk126_jerk_v072_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_126_jk5_jerk_v073_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_126_jk10_jerk_v074_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_126_jk21_jerk_v075_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_126_jk42_jerk_v076_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_126_jk63_jerk_v077_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_meanN_126_jk126_jerk_v078_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_21_jk5_jerk_v079_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_21_jk10_jerk_v080_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_21_jk21_jerk_v081_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_21_jk42_jerk_v082_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_21_jk63_jerk_v083_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_21_jk126_jerk_v084_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_42_jk5_jerk_v085_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_42_jk10_jerk_v086_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_42_jk21_jerk_v087_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_42_jk42_jerk_v088_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_42_jk63_jerk_v089_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_42_jk126_jerk_v090_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_63_jk5_jerk_v091_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_63_jk10_jerk_v092_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_63_jk21_jerk_v093_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_63_jk42_jerk_v094_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_63_jk63_jerk_v095_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_63_jk126_jerk_v096_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_126_jk5_jerk_v097_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_126_jk10_jerk_v098_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_126_jk21_jerk_v099_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_126_jk42_jerk_v100_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_126_jk63_jerk_v101_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_stdN_126_jk126_jerk_v102_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_21_jk5_jerk_v103_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_21_jk10_jerk_v104_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_21_jk21_jerk_v105_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_21_jk42_jerk_v106_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_21_jk63_jerk_v107_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_21_jk126_jerk_v108_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_42_jk5_jerk_v109_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_42_jk10_jerk_v110_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_42_jk21_jerk_v111_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_42_jk42_jerk_v112_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_42_jk63_jerk_v113_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_42_jk126_jerk_v114_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_63_jk5_jerk_v115_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_63_jk10_jerk_v116_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_63_jk21_jerk_v117_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_63_jk42_jerk_v118_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_63_jk63_jerk_v119_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_63_jk126_jerk_v120_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_126_jk5_jerk_v121_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_126_jk10_jerk_v122_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_126_jk21_jerk_v123_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_126_jk42_jerk_v124_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_126_jk63_jerk_v125_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_emaN_126_jk126_jerk_v126_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_21_jk5_jerk_v127_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_21_jk10_jerk_v128_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_21_jk21_jerk_v129_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_21_jk42_jerk_v130_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_21_jk63_jerk_v131_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_21_jk126_jerk_v132_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_42_jk5_jerk_v133_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_42_jk10_jerk_v134_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_42_jk21_jerk_v135_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_42_jk42_jerk_v136_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_42_jk63_jerk_v137_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_42_jk126_jerk_v138_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_63_jk5_jerk_v139_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_63_jk10_jerk_v140_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_63_jk21_jerk_v141_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_63_jk42_jerk_v142_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_63_jk63_jerk_v143_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_63_jk126_jerk_v144_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_126_jk5_jerk_v145_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_126_jk10_jerk_v146_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_126_jk21_jerk_v147_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_126_jk42_jerk_v148_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_126_jk63_jerk_v149_signal,
    eia_f50_energy_idiosyncratic_alpha_quality_composite_5d_qrank_126_jk126_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F50_ENERGY_IDIOSYNCRATIC_ALPHA_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    eps     = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "netinc": netinc, "fcf": fcf,
        "eps": eps, "ebitdamargin": ebitdamargin, "roic": roic,
    }

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
    print(f"OK {__file__}: {n_features} features pass")
