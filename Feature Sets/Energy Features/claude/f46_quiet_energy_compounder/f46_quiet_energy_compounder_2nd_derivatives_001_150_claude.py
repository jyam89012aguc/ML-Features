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
def _f46_low_vol_signal(closeadj, w):
    r = closeadj.pct_change()
    vol = r.rolling(w, min_periods=max(2, w // 2)).std()
    return (1.0 / vol.replace(0, np.nan)) * closeadj


def _f46_steady_growth(netinc, w):
    m = netinc.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = netinc.rolling(w, min_periods=max(2, w // 2)).std()
    return m / sd.replace(0, np.nan).abs()


def _f46_compounder_composite(closeadj, netinc, w):
    r = closeadj.pct_change()
    vol = r.rolling(w, min_periods=max(2, w // 2)).std()
    g = netinc.pct_change(periods=w)
    return (g / vol.replace(0, np.nan).abs()) * closeadj



def qec_f46_quiet_energy_compounder_low_vol_signal_5d_raw_21_sl5_slope_v001_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_f46_low_vol_signal(closeadj, 5))
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_raw_21_sl10_slope_v002_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_f46_low_vol_signal(closeadj, 5))
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_raw_21_sl21_slope_v003_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_f46_low_vol_signal(closeadj, 5))
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_raw_21_sl42_slope_v004_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_f46_low_vol_signal(closeadj, 5))
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_raw_21_sl63_slope_v005_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_f46_low_vol_signal(closeadj, 5))
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_raw_21_sl126_slope_v006_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_f46_low_vol_signal(closeadj, 5))
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_raw_21_sl189_slope_v007_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_f46_low_vol_signal(closeadj, 5))
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_raw_21_sl252_slope_v008_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_f46_low_vol_signal(closeadj, 5))
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_scXclose_21_sl5_slope_v009_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_scXclose_21_sl10_slope_v010_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_scXclose_21_sl21_slope_v011_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_scXclose_21_sl42_slope_v012_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_scXclose_21_sl63_slope_v013_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_scXclose_21_sl126_slope_v014_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_scXclose_21_sl189_slope_v015_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_scXclose_21_sl252_slope_v016_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_logabs_21_sl5_slope_v017_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.log((_f46_low_vol_signal(closeadj, 5)).abs() + 1.0) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_logabs_21_sl10_slope_v018_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.log((_f46_low_vol_signal(closeadj, 5)).abs() + 1.0) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_logabs_21_sl21_slope_v019_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.log((_f46_low_vol_signal(closeadj, 5)).abs() + 1.0) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_logabs_21_sl42_slope_v020_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.log((_f46_low_vol_signal(closeadj, 5)).abs() + 1.0) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_logabs_21_sl63_slope_v021_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.log((_f46_low_vol_signal(closeadj, 5)).abs() + 1.0) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_logabs_21_sl126_slope_v022_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.log((_f46_low_vol_signal(closeadj, 5)).abs() + 1.0) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_logabs_21_sl189_slope_v023_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.log((_f46_low_vol_signal(closeadj, 5)).abs() + 1.0) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_logabs_21_sl252_slope_v024_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.log((_f46_low_vol_signal(closeadj, 5)).abs() + 1.0) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_sign_21_sl5_slope_v025_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.sign(_f46_low_vol_signal(closeadj, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_sign_21_sl10_slope_v026_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.sign(_f46_low_vol_signal(closeadj, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_sign_21_sl21_slope_v027_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.sign(_f46_low_vol_signal(closeadj, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_sign_21_sl42_slope_v028_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.sign(_f46_low_vol_signal(closeadj, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_sign_21_sl63_slope_v029_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.sign(_f46_low_vol_signal(closeadj, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_sign_21_sl126_slope_v030_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.sign(_f46_low_vol_signal(closeadj, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_sign_21_sl189_slope_v031_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.sign(_f46_low_vol_signal(closeadj, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_sign_21_sl252_slope_v032_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.sign(_f46_low_vol_signal(closeadj, 5)) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_signsq_21_sl5_slope_v033_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.sign(_f46_low_vol_signal(closeadj, 5)) * (_f46_low_vol_signal(closeadj, 5)).pow(2) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_signsq_21_sl10_slope_v034_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.sign(_f46_low_vol_signal(closeadj, 5)) * (_f46_low_vol_signal(closeadj, 5)).pow(2) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_signsq_21_sl21_slope_v035_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.sign(_f46_low_vol_signal(closeadj, 5)) * (_f46_low_vol_signal(closeadj, 5)).pow(2) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_signsq_21_sl42_slope_v036_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.sign(_f46_low_vol_signal(closeadj, 5)) * (_f46_low_vol_signal(closeadj, 5)).pow(2) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_signsq_21_sl63_slope_v037_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.sign(_f46_low_vol_signal(closeadj, 5)) * (_f46_low_vol_signal(closeadj, 5)).pow(2) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_signsq_21_sl126_slope_v038_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.sign(_f46_low_vol_signal(closeadj, 5)) * (_f46_low_vol_signal(closeadj, 5)).pow(2) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_signsq_21_sl189_slope_v039_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.sign(_f46_low_vol_signal(closeadj, 5)) * (_f46_low_vol_signal(closeadj, 5)).pow(2) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_signsq_21_sl252_slope_v040_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (np.sign(_f46_low_vol_signal(closeadj, 5)) * (_f46_low_vol_signal(closeadj, 5)).pow(2) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_21_sl5_slope_v041_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_21_sl10_slope_v042_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_21_sl21_slope_v043_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_21_sl42_slope_v044_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_21_sl63_slope_v045_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_21_sl126_slope_v046_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_21_sl189_slope_v047_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_21_sl252_slope_v048_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_42_sl5_slope_v049_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_42_sl10_slope_v050_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_42_sl21_slope_v051_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_42_sl42_slope_v052_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_42_sl63_slope_v053_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_42_sl126_slope_v054_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_42_sl189_slope_v055_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_42_sl252_slope_v056_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_63_sl5_slope_v057_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_63_sl10_slope_v058_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_63_sl21_slope_v059_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_63_sl42_slope_v060_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_63_sl63_slope_v061_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_63_sl126_slope_v062_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_63_sl189_slope_v063_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_63_sl252_slope_v064_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_126_sl5_slope_v065_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_126_sl10_slope_v066_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_126_sl21_slope_v067_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_126_sl42_slope_v068_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_126_sl63_slope_v069_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_126_sl126_slope_v070_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_126_sl189_slope_v071_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_126_sl252_slope_v072_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_z(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_21_sl5_slope_v073_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_21_sl10_slope_v074_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_21_sl21_slope_v075_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_21_sl42_slope_v076_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_21_sl63_slope_v077_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_21_sl126_slope_v078_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_21_sl189_slope_v079_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_21_sl252_slope_v080_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_42_sl5_slope_v081_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_42_sl10_slope_v082_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_42_sl21_slope_v083_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_42_sl42_slope_v084_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_42_sl63_slope_v085_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_42_sl126_slope_v086_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_42_sl189_slope_v087_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_42_sl252_slope_v088_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_63_sl5_slope_v089_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_63_sl10_slope_v090_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_63_sl21_slope_v091_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_63_sl42_slope_v092_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_63_sl63_slope_v093_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_63_sl126_slope_v094_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_63_sl189_slope_v095_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_63_sl252_slope_v096_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_126_sl5_slope_v097_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_126_sl10_slope_v098_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_126_sl21_slope_v099_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_126_sl42_slope_v100_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_126_sl63_slope_v101_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_126_sl126_slope_v102_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_126_sl189_slope_v103_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_126_sl252_slope_v104_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_mean(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_21_sl5_slope_v105_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_21_sl10_slope_v106_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_21_sl21_slope_v107_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_21_sl42_slope_v108_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_21_sl63_slope_v109_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_21_sl126_slope_v110_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_21_sl189_slope_v111_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_21_sl252_slope_v112_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 21) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_42_sl5_slope_v113_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_42_sl10_slope_v114_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_42_sl21_slope_v115_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_42_sl42_slope_v116_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_42_sl63_slope_v117_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_42_sl126_slope_v118_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_42_sl189_slope_v119_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_42_sl252_slope_v120_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 42) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_63_sl5_slope_v121_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_63_sl10_slope_v122_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_63_sl21_slope_v123_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_63_sl42_slope_v124_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_63_sl63_slope_v125_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_63_sl126_slope_v126_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_63_sl189_slope_v127_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_63_sl252_slope_v128_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 63) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_126_sl5_slope_v129_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_126_sl10_slope_v130_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_126_sl21_slope_v131_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_126_sl42_slope_v132_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_126_sl63_slope_v133_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_126_sl126_slope_v134_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_126_sl189_slope_v135_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_126_sl252_slope_v136_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = (_std(_f46_low_vol_signal(closeadj, 5), 126) * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_21_sl5_slope_v137_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_21_sl10_slope_v138_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_21_sl21_slope_v139_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_21_sl42_slope_v140_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_21_sl63_slope_v141_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_21_sl126_slope_v142_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_21_sl189_slope_v143_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_21_sl252_slope_v144_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_42_sl5_slope_v145_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_42_sl10_slope_v146_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_42_sl21_slope_v147_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_42_sl42_slope_v148_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_42_sl63_slope_v149_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_42_sl126_slope_v150_signal(closeadj):
    base_tmp = _f46_low_vol_signal(closeadj, 5)
    transformed = ((_f46_low_vol_signal(closeadj, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _slope_diff_norm(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_raw_21_sl5_slope_v001_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_raw_21_sl10_slope_v002_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_raw_21_sl21_slope_v003_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_raw_21_sl42_slope_v004_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_raw_21_sl63_slope_v005_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_raw_21_sl126_slope_v006_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_raw_21_sl189_slope_v007_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_raw_21_sl252_slope_v008_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_scXclose_21_sl5_slope_v009_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_scXclose_21_sl10_slope_v010_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_scXclose_21_sl21_slope_v011_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_scXclose_21_sl42_slope_v012_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_scXclose_21_sl63_slope_v013_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_scXclose_21_sl126_slope_v014_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_scXclose_21_sl189_slope_v015_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_scXclose_21_sl252_slope_v016_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_logabs_21_sl5_slope_v017_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_logabs_21_sl10_slope_v018_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_logabs_21_sl21_slope_v019_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_logabs_21_sl42_slope_v020_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_logabs_21_sl63_slope_v021_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_logabs_21_sl126_slope_v022_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_logabs_21_sl189_slope_v023_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_logabs_21_sl252_slope_v024_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_sign_21_sl5_slope_v025_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_sign_21_sl10_slope_v026_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_sign_21_sl21_slope_v027_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_sign_21_sl42_slope_v028_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_sign_21_sl63_slope_v029_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_sign_21_sl126_slope_v030_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_sign_21_sl189_slope_v031_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_sign_21_sl252_slope_v032_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_signsq_21_sl5_slope_v033_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_signsq_21_sl10_slope_v034_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_signsq_21_sl21_slope_v035_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_signsq_21_sl42_slope_v036_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_signsq_21_sl63_slope_v037_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_signsq_21_sl126_slope_v038_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_signsq_21_sl189_slope_v039_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_signsq_21_sl252_slope_v040_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_21_sl5_slope_v041_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_21_sl10_slope_v042_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_21_sl21_slope_v043_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_21_sl42_slope_v044_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_21_sl63_slope_v045_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_21_sl126_slope_v046_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_21_sl189_slope_v047_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_21_sl252_slope_v048_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_42_sl5_slope_v049_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_42_sl10_slope_v050_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_42_sl21_slope_v051_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_42_sl42_slope_v052_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_42_sl63_slope_v053_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_42_sl126_slope_v054_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_42_sl189_slope_v055_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_42_sl252_slope_v056_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_63_sl5_slope_v057_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_63_sl10_slope_v058_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_63_sl21_slope_v059_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_63_sl42_slope_v060_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_63_sl63_slope_v061_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_63_sl126_slope_v062_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_63_sl189_slope_v063_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_63_sl252_slope_v064_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_126_sl5_slope_v065_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_126_sl10_slope_v066_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_126_sl21_slope_v067_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_126_sl42_slope_v068_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_126_sl63_slope_v069_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_126_sl126_slope_v070_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_126_sl189_slope_v071_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_zN_126_sl252_slope_v072_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_21_sl5_slope_v073_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_21_sl10_slope_v074_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_21_sl21_slope_v075_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_21_sl42_slope_v076_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_21_sl63_slope_v077_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_21_sl126_slope_v078_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_21_sl189_slope_v079_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_21_sl252_slope_v080_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_42_sl5_slope_v081_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_42_sl10_slope_v082_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_42_sl21_slope_v083_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_42_sl42_slope_v084_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_42_sl63_slope_v085_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_42_sl126_slope_v086_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_42_sl189_slope_v087_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_42_sl252_slope_v088_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_63_sl5_slope_v089_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_63_sl10_slope_v090_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_63_sl21_slope_v091_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_63_sl42_slope_v092_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_63_sl63_slope_v093_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_63_sl126_slope_v094_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_63_sl189_slope_v095_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_63_sl252_slope_v096_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_126_sl5_slope_v097_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_126_sl10_slope_v098_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_126_sl21_slope_v099_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_126_sl42_slope_v100_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_126_sl63_slope_v101_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_126_sl126_slope_v102_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_126_sl189_slope_v103_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_meanN_126_sl252_slope_v104_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_21_sl5_slope_v105_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_21_sl10_slope_v106_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_21_sl21_slope_v107_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_21_sl42_slope_v108_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_21_sl63_slope_v109_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_21_sl126_slope_v110_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_21_sl189_slope_v111_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_21_sl252_slope_v112_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_42_sl5_slope_v113_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_42_sl10_slope_v114_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_42_sl21_slope_v115_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_42_sl42_slope_v116_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_42_sl63_slope_v117_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_42_sl126_slope_v118_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_42_sl189_slope_v119_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_42_sl252_slope_v120_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_63_sl5_slope_v121_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_63_sl10_slope_v122_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_63_sl21_slope_v123_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_63_sl42_slope_v124_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_63_sl63_slope_v125_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_63_sl126_slope_v126_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_63_sl189_slope_v127_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_63_sl252_slope_v128_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_126_sl5_slope_v129_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_126_sl10_slope_v130_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_126_sl21_slope_v131_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_126_sl42_slope_v132_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_126_sl63_slope_v133_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_126_sl126_slope_v134_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_126_sl189_slope_v135_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_stdN_126_sl252_slope_v136_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_21_sl5_slope_v137_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_21_sl10_slope_v138_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_21_sl21_slope_v139_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_21_sl42_slope_v140_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_21_sl63_slope_v141_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_21_sl126_slope_v142_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_21_sl189_slope_v143_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_21_sl252_slope_v144_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_42_sl5_slope_v145_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_42_sl10_slope_v146_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_42_sl21_slope_v147_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_42_sl42_slope_v148_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_42_sl63_slope_v149_signal,
    qec_f46_quiet_energy_compounder_low_vol_signal_5d_emaN_42_sl126_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F46_QUIET_ENERGY_COMPOUNDER_REGISTRY_SLOPE_001_150 = REGISTRY


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
    domain_primitives = ("_f46_low_vol_signal", "_f46_steady_growth", "_f46_compounder_composite",)
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
