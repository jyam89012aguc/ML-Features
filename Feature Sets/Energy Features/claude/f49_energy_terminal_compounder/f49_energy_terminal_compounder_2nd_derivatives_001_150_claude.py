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


# ===== folder domain primitives =====
def _f49_quality_composite(roic, fcf, revenue, w):
    rq = roic.rolling(w, min_periods=max(2, w // 2)).mean()
    fy = fcf / revenue.replace(0, np.nan).abs()
    fq = fy.rolling(w, min_periods=max(2, w // 2)).mean()
    return rq + fq


def _f49_compounder_score(roic, ebitdamargin, w):
    rq = roic.rolling(w, min_periods=max(2, w // 2)).mean()
    mq = ebitdamargin.rolling(w, min_periods=max(2, w // 2)).mean()
    return rq * mq


def _f49_terminal_quality(fcf, revenue, roic, w):
    fy = fcf / revenue.replace(0, np.nan).abs()
    fq = fy.rolling(w, min_periods=max(2, w // 2)).mean()
    rq = roic.rolling(w, min_periods=max(2, w // 2)).mean()
    return fq * rq



def etc_f49_energy_terminal_compounder_quality_composite_5d_raw_21_sl5_slope_v001_signal(roic, fcf, revenue):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_f49_quality_composite(roic, fcf, revenue, 5))
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_raw_21_sl10_slope_v002_signal(roic, fcf, revenue):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_f49_quality_composite(roic, fcf, revenue, 5))
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_raw_21_sl21_slope_v003_signal(roic, fcf, revenue):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_f49_quality_composite(roic, fcf, revenue, 5))
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_raw_21_sl42_slope_v004_signal(roic, fcf, revenue):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_f49_quality_composite(roic, fcf, revenue, 5))
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_raw_21_sl63_slope_v005_signal(roic, fcf, revenue):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_f49_quality_composite(roic, fcf, revenue, 5))
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_raw_21_sl126_slope_v006_signal(roic, fcf, revenue):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_f49_quality_composite(roic, fcf, revenue, 5))
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_raw_21_sl189_slope_v007_signal(roic, fcf, revenue):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_f49_quality_composite(roic, fcf, revenue, 5))
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_raw_21_sl252_slope_v008_signal(roic, fcf, revenue):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_f49_quality_composite(roic, fcf, revenue, 5))
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_scXclose_21_sl5_slope_v009_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_scXclose_21_sl10_slope_v010_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_scXclose_21_sl21_slope_v011_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_scXclose_21_sl42_slope_v012_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_scXclose_21_sl63_slope_v013_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_scXclose_21_sl126_slope_v014_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_scXclose_21_sl189_slope_v015_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_scXclose_21_sl252_slope_v016_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_logabs_21_sl5_slope_v017_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.log((_f49_quality_composite(roic, fcf, revenue, 5)).abs() + 1.0) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_logabs_21_sl10_slope_v018_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.log((_f49_quality_composite(roic, fcf, revenue, 5)).abs() + 1.0) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_logabs_21_sl21_slope_v019_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.log((_f49_quality_composite(roic, fcf, revenue, 5)).abs() + 1.0) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_logabs_21_sl42_slope_v020_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.log((_f49_quality_composite(roic, fcf, revenue, 5)).abs() + 1.0) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_logabs_21_sl63_slope_v021_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.log((_f49_quality_composite(roic, fcf, revenue, 5)).abs() + 1.0) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_logabs_21_sl126_slope_v022_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.log((_f49_quality_composite(roic, fcf, revenue, 5)).abs() + 1.0) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_logabs_21_sl189_slope_v023_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.log((_f49_quality_composite(roic, fcf, revenue, 5)).abs() + 1.0) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_logabs_21_sl252_slope_v024_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.log((_f49_quality_composite(roic, fcf, revenue, 5)).abs() + 1.0) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_sign_21_sl5_slope_v025_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f49_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_sign_21_sl10_slope_v026_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f49_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_sign_21_sl21_slope_v027_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f49_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_sign_21_sl42_slope_v028_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f49_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_sign_21_sl63_slope_v029_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f49_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_sign_21_sl126_slope_v030_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f49_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_sign_21_sl189_slope_v031_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f49_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_sign_21_sl252_slope_v032_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f49_quality_composite(roic, fcf, revenue, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_signsq_21_sl5_slope_v033_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f49_quality_composite(roic, fcf, revenue, 5)) * (_f49_quality_composite(roic, fcf, revenue, 5)).pow(2) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_signsq_21_sl10_slope_v034_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f49_quality_composite(roic, fcf, revenue, 5)) * (_f49_quality_composite(roic, fcf, revenue, 5)).pow(2) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_signsq_21_sl21_slope_v035_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f49_quality_composite(roic, fcf, revenue, 5)) * (_f49_quality_composite(roic, fcf, revenue, 5)).pow(2) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_signsq_21_sl42_slope_v036_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f49_quality_composite(roic, fcf, revenue, 5)) * (_f49_quality_composite(roic, fcf, revenue, 5)).pow(2) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_signsq_21_sl63_slope_v037_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f49_quality_composite(roic, fcf, revenue, 5)) * (_f49_quality_composite(roic, fcf, revenue, 5)).pow(2) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_signsq_21_sl126_slope_v038_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f49_quality_composite(roic, fcf, revenue, 5)) * (_f49_quality_composite(roic, fcf, revenue, 5)).pow(2) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_signsq_21_sl189_slope_v039_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f49_quality_composite(roic, fcf, revenue, 5)) * (_f49_quality_composite(roic, fcf, revenue, 5)).pow(2) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_signsq_21_sl252_slope_v040_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (np.sign(_f49_quality_composite(roic, fcf, revenue, 5)) * (_f49_quality_composite(roic, fcf, revenue, 5)).pow(2) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_21_sl5_slope_v041_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_21_sl10_slope_v042_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_21_sl21_slope_v043_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_21_sl42_slope_v044_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_21_sl63_slope_v045_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_21_sl126_slope_v046_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_21_sl189_slope_v047_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_21_sl252_slope_v048_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_42_sl5_slope_v049_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_42_sl10_slope_v050_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_42_sl21_slope_v051_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_42_sl42_slope_v052_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_42_sl63_slope_v053_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_42_sl126_slope_v054_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_42_sl189_slope_v055_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_42_sl252_slope_v056_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_63_sl5_slope_v057_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_63_sl10_slope_v058_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_63_sl21_slope_v059_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_63_sl42_slope_v060_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_63_sl63_slope_v061_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_63_sl126_slope_v062_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_63_sl189_slope_v063_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_63_sl252_slope_v064_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_126_sl5_slope_v065_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_126_sl10_slope_v066_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_126_sl21_slope_v067_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_126_sl42_slope_v068_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_126_sl63_slope_v069_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_126_sl126_slope_v070_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_126_sl189_slope_v071_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_zN_126_sl252_slope_v072_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_z(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_21_sl5_slope_v073_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_21_sl10_slope_v074_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_21_sl21_slope_v075_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_21_sl42_slope_v076_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_21_sl63_slope_v077_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_21_sl126_slope_v078_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_21_sl189_slope_v079_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_21_sl252_slope_v080_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_42_sl5_slope_v081_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_42_sl10_slope_v082_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_42_sl21_slope_v083_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_42_sl42_slope_v084_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_42_sl63_slope_v085_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_42_sl126_slope_v086_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_42_sl189_slope_v087_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_42_sl252_slope_v088_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_63_sl5_slope_v089_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_63_sl10_slope_v090_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_63_sl21_slope_v091_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_63_sl42_slope_v092_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_63_sl63_slope_v093_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_63_sl126_slope_v094_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_63_sl189_slope_v095_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_63_sl252_slope_v096_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_126_sl5_slope_v097_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_126_sl10_slope_v098_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_126_sl21_slope_v099_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_126_sl42_slope_v100_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_126_sl63_slope_v101_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_126_sl126_slope_v102_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_126_sl189_slope_v103_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_126_sl252_slope_v104_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_mean(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_21_sl5_slope_v105_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_21_sl10_slope_v106_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_21_sl21_slope_v107_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_21_sl42_slope_v108_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_21_sl63_slope_v109_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_21_sl126_slope_v110_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_21_sl189_slope_v111_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_21_sl252_slope_v112_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_42_sl5_slope_v113_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_42_sl10_slope_v114_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_42_sl21_slope_v115_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_42_sl42_slope_v116_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_42_sl63_slope_v117_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_42_sl126_slope_v118_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_42_sl189_slope_v119_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_42_sl252_slope_v120_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_63_sl5_slope_v121_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_63_sl10_slope_v122_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_63_sl21_slope_v123_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_63_sl42_slope_v124_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_63_sl63_slope_v125_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_63_sl126_slope_v126_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_63_sl189_slope_v127_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_63_sl252_slope_v128_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_126_sl5_slope_v129_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_126_sl10_slope_v130_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_126_sl21_slope_v131_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_126_sl42_slope_v132_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_126_sl63_slope_v133_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_126_sl126_slope_v134_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_126_sl189_slope_v135_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_126_sl252_slope_v136_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = (_std(_f49_quality_composite(roic, fcf, revenue, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_21_sl5_slope_v137_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_21_sl10_slope_v138_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_21_sl21_slope_v139_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_21_sl42_slope_v140_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_21_sl63_slope_v141_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_21_sl126_slope_v142_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_21_sl189_slope_v143_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_21_sl252_slope_v144_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_42_sl5_slope_v145_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_42_sl10_slope_v146_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_42_sl21_slope_v147_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_42_sl42_slope_v148_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_42_sl63_slope_v149_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_42_sl126_slope_v150_signal(roic, fcf, revenue, closeadj):
    base_tmp = _f49_quality_composite(roic, fcf, revenue, 5)
    transformed = ((_f49_quality_composite(roic, fcf, revenue, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    etc_f49_energy_terminal_compounder_quality_composite_5d_raw_21_sl5_slope_v001_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_raw_21_sl10_slope_v002_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_raw_21_sl21_slope_v003_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_raw_21_sl42_slope_v004_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_raw_21_sl63_slope_v005_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_raw_21_sl126_slope_v006_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_raw_21_sl189_slope_v007_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_raw_21_sl252_slope_v008_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_scXclose_21_sl5_slope_v009_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_scXclose_21_sl10_slope_v010_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_scXclose_21_sl21_slope_v011_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_scXclose_21_sl42_slope_v012_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_scXclose_21_sl63_slope_v013_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_scXclose_21_sl126_slope_v014_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_scXclose_21_sl189_slope_v015_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_scXclose_21_sl252_slope_v016_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_logabs_21_sl5_slope_v017_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_logabs_21_sl10_slope_v018_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_logabs_21_sl21_slope_v019_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_logabs_21_sl42_slope_v020_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_logabs_21_sl63_slope_v021_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_logabs_21_sl126_slope_v022_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_logabs_21_sl189_slope_v023_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_logabs_21_sl252_slope_v024_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_sign_21_sl5_slope_v025_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_sign_21_sl10_slope_v026_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_sign_21_sl21_slope_v027_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_sign_21_sl42_slope_v028_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_sign_21_sl63_slope_v029_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_sign_21_sl126_slope_v030_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_sign_21_sl189_slope_v031_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_sign_21_sl252_slope_v032_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_signsq_21_sl5_slope_v033_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_signsq_21_sl10_slope_v034_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_signsq_21_sl21_slope_v035_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_signsq_21_sl42_slope_v036_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_signsq_21_sl63_slope_v037_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_signsq_21_sl126_slope_v038_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_signsq_21_sl189_slope_v039_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_signsq_21_sl252_slope_v040_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_21_sl5_slope_v041_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_21_sl10_slope_v042_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_21_sl21_slope_v043_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_21_sl42_slope_v044_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_21_sl63_slope_v045_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_21_sl126_slope_v046_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_21_sl189_slope_v047_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_21_sl252_slope_v048_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_42_sl5_slope_v049_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_42_sl10_slope_v050_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_42_sl21_slope_v051_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_42_sl42_slope_v052_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_42_sl63_slope_v053_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_42_sl126_slope_v054_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_42_sl189_slope_v055_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_42_sl252_slope_v056_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_63_sl5_slope_v057_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_63_sl10_slope_v058_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_63_sl21_slope_v059_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_63_sl42_slope_v060_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_63_sl63_slope_v061_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_63_sl126_slope_v062_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_63_sl189_slope_v063_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_63_sl252_slope_v064_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_126_sl5_slope_v065_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_126_sl10_slope_v066_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_126_sl21_slope_v067_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_126_sl42_slope_v068_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_126_sl63_slope_v069_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_126_sl126_slope_v070_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_126_sl189_slope_v071_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_zN_126_sl252_slope_v072_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_21_sl5_slope_v073_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_21_sl10_slope_v074_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_21_sl21_slope_v075_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_21_sl42_slope_v076_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_21_sl63_slope_v077_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_21_sl126_slope_v078_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_21_sl189_slope_v079_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_21_sl252_slope_v080_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_42_sl5_slope_v081_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_42_sl10_slope_v082_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_42_sl21_slope_v083_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_42_sl42_slope_v084_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_42_sl63_slope_v085_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_42_sl126_slope_v086_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_42_sl189_slope_v087_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_42_sl252_slope_v088_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_63_sl5_slope_v089_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_63_sl10_slope_v090_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_63_sl21_slope_v091_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_63_sl42_slope_v092_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_63_sl63_slope_v093_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_63_sl126_slope_v094_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_63_sl189_slope_v095_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_63_sl252_slope_v096_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_126_sl5_slope_v097_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_126_sl10_slope_v098_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_126_sl21_slope_v099_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_126_sl42_slope_v100_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_126_sl63_slope_v101_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_126_sl126_slope_v102_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_126_sl189_slope_v103_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_meanN_126_sl252_slope_v104_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_21_sl5_slope_v105_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_21_sl10_slope_v106_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_21_sl21_slope_v107_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_21_sl42_slope_v108_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_21_sl63_slope_v109_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_21_sl126_slope_v110_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_21_sl189_slope_v111_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_21_sl252_slope_v112_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_42_sl5_slope_v113_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_42_sl10_slope_v114_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_42_sl21_slope_v115_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_42_sl42_slope_v116_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_42_sl63_slope_v117_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_42_sl126_slope_v118_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_42_sl189_slope_v119_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_42_sl252_slope_v120_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_63_sl5_slope_v121_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_63_sl10_slope_v122_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_63_sl21_slope_v123_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_63_sl42_slope_v124_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_63_sl63_slope_v125_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_63_sl126_slope_v126_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_63_sl189_slope_v127_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_63_sl252_slope_v128_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_126_sl5_slope_v129_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_126_sl10_slope_v130_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_126_sl21_slope_v131_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_126_sl42_slope_v132_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_126_sl63_slope_v133_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_126_sl126_slope_v134_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_126_sl189_slope_v135_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_stdN_126_sl252_slope_v136_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_21_sl5_slope_v137_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_21_sl10_slope_v138_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_21_sl21_slope_v139_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_21_sl42_slope_v140_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_21_sl63_slope_v141_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_21_sl126_slope_v142_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_21_sl189_slope_v143_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_21_sl252_slope_v144_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_42_sl5_slope_v145_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_42_sl10_slope_v146_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_42_sl21_slope_v147_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_42_sl42_slope_v148_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_42_sl63_slope_v149_signal,
    etc_f49_energy_terminal_compounder_quality_composite_5d_emaN_42_sl126_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_ENERGY_TERMINAL_COMPOUNDER_REGISTRY_SLOPE_001_150 = REGISTRY


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
    print(f"OK {__file__}: {n_features} features pass")
