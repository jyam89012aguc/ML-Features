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
def _f47_quiet_fcf_growth(fcf, w):
    g = fcf.pct_change(periods=w)
    sd = g.rolling(w, min_periods=max(2, w // 2)).std()
    return g / sd.replace(0, np.nan).abs()


def _f47_low_attention_growth(closeadj, volume, fcf, w):
    dv = closeadj * volume
    attn = dv.rolling(w, min_periods=max(2, w // 2)).mean()
    g = fcf.pct_change(periods=w)
    return (g / attn.replace(0, np.nan).abs()) * closeadj


def _f47_hidden_quality(fcf, roic, w):
    fg = fcf.pct_change(periods=w)
    rq = roic.rolling(w, min_periods=max(2, w // 2)).mean()
    return (fg * rq)



def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_raw_21_jk5_jerk_v001_signal(fcf):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_f47_quiet_fcf_growth(fcf, 5))
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_raw_21_jk10_jerk_v002_signal(fcf):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_f47_quiet_fcf_growth(fcf, 5))
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_raw_21_jk21_jerk_v003_signal(fcf):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_f47_quiet_fcf_growth(fcf, 5))
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_raw_21_jk42_jerk_v004_signal(fcf):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_f47_quiet_fcf_growth(fcf, 5))
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_raw_21_jk63_jerk_v005_signal(fcf):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_f47_quiet_fcf_growth(fcf, 5))
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_raw_21_jk126_jerk_v006_signal(fcf):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_f47_quiet_fcf_growth(fcf, 5))
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_scXclose_21_jk5_jerk_v007_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_scXclose_21_jk10_jerk_v008_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_scXclose_21_jk21_jerk_v009_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_scXclose_21_jk42_jerk_v010_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_scXclose_21_jk63_jerk_v011_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_scXclose_21_jk126_jerk_v012_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logabs_21_jk5_jerk_v013_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (np.log((_f47_quiet_fcf_growth(fcf, 5)).abs() + 1.0) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logabs_21_jk10_jerk_v014_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (np.log((_f47_quiet_fcf_growth(fcf, 5)).abs() + 1.0) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logabs_21_jk21_jerk_v015_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (np.log((_f47_quiet_fcf_growth(fcf, 5)).abs() + 1.0) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logabs_21_jk42_jerk_v016_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (np.log((_f47_quiet_fcf_growth(fcf, 5)).abs() + 1.0) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logabs_21_jk63_jerk_v017_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (np.log((_f47_quiet_fcf_growth(fcf, 5)).abs() + 1.0) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logabs_21_jk126_jerk_v018_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (np.log((_f47_quiet_fcf_growth(fcf, 5)).abs() + 1.0) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sign_21_jk5_jerk_v019_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (np.sign(_f47_quiet_fcf_growth(fcf, 5)) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sign_21_jk10_jerk_v020_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (np.sign(_f47_quiet_fcf_growth(fcf, 5)) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sign_21_jk21_jerk_v021_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (np.sign(_f47_quiet_fcf_growth(fcf, 5)) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sign_21_jk42_jerk_v022_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (np.sign(_f47_quiet_fcf_growth(fcf, 5)) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sign_21_jk63_jerk_v023_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (np.sign(_f47_quiet_fcf_growth(fcf, 5)) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sign_21_jk126_jerk_v024_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (np.sign(_f47_quiet_fcf_growth(fcf, 5)) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_signsq_21_jk5_jerk_v025_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (np.sign(_f47_quiet_fcf_growth(fcf, 5)) * (_f47_quiet_fcf_growth(fcf, 5)).pow(2) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_signsq_21_jk10_jerk_v026_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (np.sign(_f47_quiet_fcf_growth(fcf, 5)) * (_f47_quiet_fcf_growth(fcf, 5)).pow(2) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_signsq_21_jk21_jerk_v027_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (np.sign(_f47_quiet_fcf_growth(fcf, 5)) * (_f47_quiet_fcf_growth(fcf, 5)).pow(2) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_signsq_21_jk42_jerk_v028_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (np.sign(_f47_quiet_fcf_growth(fcf, 5)) * (_f47_quiet_fcf_growth(fcf, 5)).pow(2) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_signsq_21_jk63_jerk_v029_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (np.sign(_f47_quiet_fcf_growth(fcf, 5)) * (_f47_quiet_fcf_growth(fcf, 5)).pow(2) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_signsq_21_jk126_jerk_v030_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (np.sign(_f47_quiet_fcf_growth(fcf, 5)) * (_f47_quiet_fcf_growth(fcf, 5)).pow(2) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_21_jk5_jerk_v031_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 21) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_21_jk10_jerk_v032_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 21) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_21_jk21_jerk_v033_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 21) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_21_jk42_jerk_v034_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 21) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_21_jk63_jerk_v035_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 21) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_21_jk126_jerk_v036_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 21) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_42_jk5_jerk_v037_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 42) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_42_jk10_jerk_v038_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 42) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_42_jk21_jerk_v039_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 42) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_42_jk42_jerk_v040_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 42) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_42_jk63_jerk_v041_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 42) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_42_jk126_jerk_v042_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 42) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_63_jk5_jerk_v043_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 63) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_63_jk10_jerk_v044_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 63) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_63_jk21_jerk_v045_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 63) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_63_jk42_jerk_v046_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 63) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_63_jk63_jerk_v047_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 63) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_63_jk126_jerk_v048_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 63) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_126_jk5_jerk_v049_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 126) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_126_jk10_jerk_v050_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 126) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_126_jk21_jerk_v051_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 126) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_126_jk42_jerk_v052_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 126) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_126_jk63_jerk_v053_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 126) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_126_jk126_jerk_v054_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_z(_f47_quiet_fcf_growth(fcf, 5), 126) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_21_jk5_jerk_v055_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 21) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_21_jk10_jerk_v056_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 21) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_21_jk21_jerk_v057_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 21) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_21_jk42_jerk_v058_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 21) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_21_jk63_jerk_v059_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 21) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_21_jk126_jerk_v060_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 21) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_42_jk5_jerk_v061_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 42) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_42_jk10_jerk_v062_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 42) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_42_jk21_jerk_v063_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 42) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_42_jk42_jerk_v064_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 42) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_42_jk63_jerk_v065_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 42) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_42_jk126_jerk_v066_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 42) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_63_jk5_jerk_v067_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 63) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_63_jk10_jerk_v068_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 63) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_63_jk21_jerk_v069_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 63) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_63_jk42_jerk_v070_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 63) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_63_jk63_jerk_v071_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 63) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_63_jk126_jerk_v072_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 63) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_126_jk5_jerk_v073_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 126) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_126_jk10_jerk_v074_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 126) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_126_jk21_jerk_v075_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 126) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_126_jk42_jerk_v076_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 126) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_126_jk63_jerk_v077_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 126) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_126_jk126_jerk_v078_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_mean(_f47_quiet_fcf_growth(fcf, 5), 126) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_21_jk5_jerk_v079_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 21) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_21_jk10_jerk_v080_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 21) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_21_jk21_jerk_v081_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 21) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_21_jk42_jerk_v082_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 21) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_21_jk63_jerk_v083_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 21) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_21_jk126_jerk_v084_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 21) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_42_jk5_jerk_v085_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 42) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_42_jk10_jerk_v086_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 42) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_42_jk21_jerk_v087_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 42) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_42_jk42_jerk_v088_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 42) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_42_jk63_jerk_v089_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 42) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_42_jk126_jerk_v090_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 42) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_63_jk5_jerk_v091_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 63) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_63_jk10_jerk_v092_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 63) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_63_jk21_jerk_v093_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 63) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_63_jk42_jerk_v094_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 63) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_63_jk63_jerk_v095_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 63) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_63_jk126_jerk_v096_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 63) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_126_jk5_jerk_v097_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 126) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_126_jk10_jerk_v098_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 126) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_126_jk21_jerk_v099_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 126) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_126_jk42_jerk_v100_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 126) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_126_jk63_jerk_v101_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 126) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_126_jk126_jerk_v102_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = (_std(_f47_quiet_fcf_growth(fcf, 5), 126) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_21_jk5_jerk_v103_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_21_jk10_jerk_v104_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_21_jk21_jerk_v105_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_21_jk42_jerk_v106_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_21_jk63_jerk_v107_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_21_jk126_jerk_v108_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=21, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_42_jk5_jerk_v109_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_42_jk10_jerk_v110_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_42_jk21_jerk_v111_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_42_jk42_jerk_v112_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_42_jk63_jerk_v113_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_42_jk126_jerk_v114_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=42, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_63_jk5_jerk_v115_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=63, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_63_jk10_jerk_v116_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=63, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_63_jk21_jerk_v117_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=63, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_63_jk42_jerk_v118_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=63, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_63_jk63_jerk_v119_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=63, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_63_jk126_jerk_v120_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=63, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_126_jk5_jerk_v121_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=126, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_126_jk10_jerk_v122_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=126, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_126_jk21_jerk_v123_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=126, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_126_jk42_jerk_v124_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=126, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_126_jk63_jerk_v125_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=126, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_126_jk126_jerk_v126_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).ewm(span=126, adjust=False).mean() * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_21_jk5_jerk_v127_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(21, min_periods=max(2, 21 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_21_jk10_jerk_v128_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(21, min_periods=max(2, 21 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_21_jk21_jerk_v129_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(21, min_periods=max(2, 21 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_21_jk42_jerk_v130_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(21, min_periods=max(2, 21 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_21_jk63_jerk_v131_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(21, min_periods=max(2, 21 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_21_jk126_jerk_v132_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(21, min_periods=max(2, 21 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_42_jk5_jerk_v133_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(42, min_periods=max(2, 42 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_42_jk10_jerk_v134_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(42, min_periods=max(2, 42 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_42_jk21_jerk_v135_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(42, min_periods=max(2, 42 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_42_jk42_jerk_v136_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(42, min_periods=max(2, 42 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_42_jk63_jerk_v137_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(42, min_periods=max(2, 42 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_42_jk126_jerk_v138_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(42, min_periods=max(2, 42 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_63_jk5_jerk_v139_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_63_jk10_jerk_v140_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_63_jk21_jerk_v141_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_63_jk42_jerk_v142_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_63_jk63_jerk_v143_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_63_jk126_jerk_v144_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(63, min_periods=max(2, 63 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_126_jk5_jerk_v145_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_126_jk10_jerk_v146_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_126_jk21_jerk_v147_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_126_jk42_jerk_v148_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_126_jk63_jerk_v149_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_126_jk126_jerk_v150_signal(fcf, closeadj):
    base_tmp = _f47_quiet_fcf_growth(fcf, 5)
    transformed = ((_f47_quiet_fcf_growth(fcf, 5)).rolling(126, min_periods=max(2, 126 // 2)).rank(pct=True) * closeadj)
    result = _jerk(transformed, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_raw_21_jk5_jerk_v001_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_raw_21_jk10_jerk_v002_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_raw_21_jk21_jerk_v003_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_raw_21_jk42_jerk_v004_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_raw_21_jk63_jerk_v005_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_raw_21_jk126_jerk_v006_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_scXclose_21_jk5_jerk_v007_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_scXclose_21_jk10_jerk_v008_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_scXclose_21_jk21_jerk_v009_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_scXclose_21_jk42_jerk_v010_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_scXclose_21_jk63_jerk_v011_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_scXclose_21_jk126_jerk_v012_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logabs_21_jk5_jerk_v013_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logabs_21_jk10_jerk_v014_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logabs_21_jk21_jerk_v015_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logabs_21_jk42_jerk_v016_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logabs_21_jk63_jerk_v017_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_logabs_21_jk126_jerk_v018_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sign_21_jk5_jerk_v019_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sign_21_jk10_jerk_v020_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sign_21_jk21_jerk_v021_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sign_21_jk42_jerk_v022_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sign_21_jk63_jerk_v023_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_sign_21_jk126_jerk_v024_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_signsq_21_jk5_jerk_v025_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_signsq_21_jk10_jerk_v026_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_signsq_21_jk21_jerk_v027_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_signsq_21_jk42_jerk_v028_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_signsq_21_jk63_jerk_v029_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_signsq_21_jk126_jerk_v030_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_21_jk5_jerk_v031_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_21_jk10_jerk_v032_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_21_jk21_jerk_v033_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_21_jk42_jerk_v034_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_21_jk63_jerk_v035_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_21_jk126_jerk_v036_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_42_jk5_jerk_v037_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_42_jk10_jerk_v038_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_42_jk21_jerk_v039_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_42_jk42_jerk_v040_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_42_jk63_jerk_v041_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_42_jk126_jerk_v042_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_63_jk5_jerk_v043_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_63_jk10_jerk_v044_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_63_jk21_jerk_v045_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_63_jk42_jerk_v046_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_63_jk63_jerk_v047_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_63_jk126_jerk_v048_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_126_jk5_jerk_v049_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_126_jk10_jerk_v050_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_126_jk21_jerk_v051_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_126_jk42_jerk_v052_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_126_jk63_jerk_v053_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_zN_126_jk126_jerk_v054_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_21_jk5_jerk_v055_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_21_jk10_jerk_v056_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_21_jk21_jerk_v057_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_21_jk42_jerk_v058_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_21_jk63_jerk_v059_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_21_jk126_jerk_v060_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_42_jk5_jerk_v061_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_42_jk10_jerk_v062_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_42_jk21_jerk_v063_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_42_jk42_jerk_v064_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_42_jk63_jerk_v065_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_42_jk126_jerk_v066_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_63_jk5_jerk_v067_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_63_jk10_jerk_v068_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_63_jk21_jerk_v069_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_63_jk42_jerk_v070_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_63_jk63_jerk_v071_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_63_jk126_jerk_v072_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_126_jk5_jerk_v073_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_126_jk10_jerk_v074_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_126_jk21_jerk_v075_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_126_jk42_jerk_v076_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_126_jk63_jerk_v077_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_meanN_126_jk126_jerk_v078_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_21_jk5_jerk_v079_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_21_jk10_jerk_v080_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_21_jk21_jerk_v081_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_21_jk42_jerk_v082_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_21_jk63_jerk_v083_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_21_jk126_jerk_v084_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_42_jk5_jerk_v085_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_42_jk10_jerk_v086_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_42_jk21_jerk_v087_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_42_jk42_jerk_v088_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_42_jk63_jerk_v089_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_42_jk126_jerk_v090_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_63_jk5_jerk_v091_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_63_jk10_jerk_v092_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_63_jk21_jerk_v093_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_63_jk42_jerk_v094_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_63_jk63_jerk_v095_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_63_jk126_jerk_v096_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_126_jk5_jerk_v097_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_126_jk10_jerk_v098_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_126_jk21_jerk_v099_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_126_jk42_jerk_v100_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_126_jk63_jerk_v101_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_stdN_126_jk126_jerk_v102_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_21_jk5_jerk_v103_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_21_jk10_jerk_v104_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_21_jk21_jerk_v105_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_21_jk42_jerk_v106_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_21_jk63_jerk_v107_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_21_jk126_jerk_v108_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_42_jk5_jerk_v109_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_42_jk10_jerk_v110_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_42_jk21_jerk_v111_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_42_jk42_jerk_v112_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_42_jk63_jerk_v113_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_42_jk126_jerk_v114_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_63_jk5_jerk_v115_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_63_jk10_jerk_v116_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_63_jk21_jerk_v117_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_63_jk42_jerk_v118_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_63_jk63_jerk_v119_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_63_jk126_jerk_v120_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_126_jk5_jerk_v121_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_126_jk10_jerk_v122_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_126_jk21_jerk_v123_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_126_jk42_jerk_v124_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_126_jk63_jerk_v125_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_emaN_126_jk126_jerk_v126_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_21_jk5_jerk_v127_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_21_jk10_jerk_v128_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_21_jk21_jerk_v129_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_21_jk42_jerk_v130_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_21_jk63_jerk_v131_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_21_jk126_jerk_v132_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_42_jk5_jerk_v133_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_42_jk10_jerk_v134_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_42_jk21_jerk_v135_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_42_jk42_jerk_v136_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_42_jk63_jerk_v137_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_42_jk126_jerk_v138_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_63_jk5_jerk_v139_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_63_jk10_jerk_v140_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_63_jk21_jerk_v141_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_63_jk42_jerk_v142_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_63_jk63_jerk_v143_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_63_jk126_jerk_v144_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_126_jk5_jerk_v145_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_126_jk10_jerk_v146_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_126_jk21_jerk_v147_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_126_jk42_jerk_v148_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_126_jk63_jerk_v149_signal,
    hec_f47_hidden_energy_compounder_quiet_fcf_growth_5d_qrank_126_jk126_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F47_HIDDEN_ENERGY_COMPOUNDER_REGISTRY_JERK_001_150 = REGISTRY


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
    domain_primitives = ("_f47_quiet_fcf_growth", "_f47_low_attention_growth", "_f47_hidden_quality",)
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
