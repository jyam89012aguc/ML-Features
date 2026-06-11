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


def _diff(s, n):
    return s.diff(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _jerk(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f36_cashflow_jerk_fcf(fcf, w):
    accel = _diff(fcf, w)
    return _diff(accel, w)


def _f36_cashflow_jerk_ncfo(ncfo, w):
    accel = _diff(ncfo, w)
    return _diff(accel, w)


def _f36_cashflow_jerk_fcfmargin(fcf, revenue, w):
    m = _safe_div(fcf, revenue.abs())
    accel = _diff(m, w)
    return _diff(accel, w)


def _f36_cashflow_jerk_ncfomargin(ncfo, revenue, w):
    m = _safe_div(ncfo, revenue.abs())
    accel = _diff(m, w)
    return _diff(accel, w)


# 5d jerk of 21d FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_21d_jerk_v001_signal(fcf, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 21) * closeadj * 1e-6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_21d_jerk_v002_signal(fcf, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 21) * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_63d_jerk_v003_signal(fcf, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 63) * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_63d_jerk_v004_signal(fcf, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 63) * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 126d FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_126d_jerk_v005_signal(fcf, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 126) * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_126d_jerk_v006_signal(fcf, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 126) * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_252d_jerk_v007_signal(fcf, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 252) * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_252d_jerk_v008_signal(fcf, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 252) * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_21d_jerk_v009_signal(ncfo, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 21) * closeadj * 1e-6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_21d_jerk_v010_signal(ncfo, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 21) * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_63d_jerk_v011_signal(ncfo, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 63) * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_63d_jerk_v012_signal(ncfo, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 63) * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 126d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_126d_jerk_v013_signal(ncfo, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 126) * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_126d_jerk_v014_signal(ncfo, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 126) * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_252d_jerk_v015_signal(ncfo, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 252) * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_252d_jerk_v016_signal(ncfo, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 252) * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_21d_jerk_v017_signal(fcf, revenue, closeadj):
    base = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_21d_jerk_v018_signal(fcf, revenue, closeadj):
    base = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_63d_jerk_v019_signal(fcf, revenue, closeadj):
    base = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_63d_jerk_v020_signal(fcf, revenue, closeadj):
    base = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 126d FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_126d_jerk_v021_signal(fcf, revenue, closeadj):
    base = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_126d_jerk_v022_signal(fcf, revenue, closeadj):
    base = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_252d_jerk_v023_signal(fcf, revenue, closeadj):
    base = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_252d_jerk_v024_signal(fcf, revenue, closeadj):
    base = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_21d_jerk_v025_signal(ncfo, revenue, closeadj):
    base = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 21) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 21d ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_21d_jerk_v026_signal(ncfo, revenue, closeadj):
    base = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 21) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_63d_jerk_v027_signal(ncfo, revenue, closeadj):
    base = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 63) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 63d ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_63d_jerk_v028_signal(ncfo, revenue, closeadj):
    base = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 63) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 126d ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_126d_jerk_v029_signal(ncfo, revenue, closeadj):
    base = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 126) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_126d_jerk_v030_signal(ncfo, revenue, closeadj):
    base = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 126) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 252d ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_252d_jerk_v031_signal(ncfo, revenue, closeadj):
    base = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_252d_jerk_v032_signal(ncfo, revenue, closeadj):
    base = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d |FCF jerk| × close
def f36cfj_f36_cash_flow_jerk_fcf_abs_21d_jerk_v033_signal(fcf, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 21).abs() * closeadj * 1e-6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d |FCF jerk| × close
def f36cfj_f36_cash_flow_jerk_fcf_abs_63d_jerk_v034_signal(fcf, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 63).abs() * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 126d |ncfo jerk| × close
def f36cfj_f36_cash_flow_jerk_ncfo_abs_126d_jerk_v035_signal(ncfo, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 126).abs() * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 21d FCF jerk squared × close
def f36cfj_f36_cash_flow_jerk_fcf_sq_21d_jerk_v036_signal(fcf, closeadj):
    j = _f36_cashflow_jerk_fcf(fcf, 21)
    base = j * j.abs() * closeadj * 1e-12
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 63d ncfo jerk squared × close
def f36cfj_f36_cash_flow_jerk_ncfo_sq_63d_jerk_v037_signal(ncfo, closeadj):
    j = _f36_cashflow_jerk_ncfo(ncfo, 63)
    base = j * j.abs() * closeadj * 1e-12
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 252d FCF margin jerk squared × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_sq_252d_jerk_v038_signal(fcf, revenue, closeadj):
    j = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252)
    base = j * j.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk mean × close
def f36cfj_f36_cash_flow_jerk_fcf_mean_63d_jerk_v039_signal(fcf, closeadj):
    base = _mean(_f36_cashflow_jerk_fcf(fcf, 63), 63) * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF jerk mean × close
def f36cfj_f36_cash_flow_jerk_fcf_mean_252d_jerk_v040_signal(fcf, closeadj):
    base = _mean(_f36_cashflow_jerk_fcf(fcf, 252), 252) * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of ncfo jerk mean × close
def f36cfj_f36_cash_flow_jerk_ncfo_mean_63d_jerk_v041_signal(ncfo, closeadj):
    base = _mean(_f36_cashflow_jerk_ncfo(ncfo, 63), 63) * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF margin jerk mean × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_mean_252d_jerk_v042_signal(fcf, revenue, closeadj):
    base = _mean(_f36_cashflow_jerk_fcfmargin(fcf, revenue, 252), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk std × close
def f36cfj_f36_cash_flow_jerk_fcf_std_63d_jerk_v043_signal(fcf, closeadj):
    base = _std(_f36_cashflow_jerk_fcf(fcf, 63), 63) * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk std × close
def f36cfj_f36_cash_flow_jerk_ncfo_std_252d_jerk_v044_signal(ncfo, closeadj):
    base = _std(_f36_cashflow_jerk_ncfo(ncfo, 252), 252) * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF margin jerk std × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_std_252d_jerk_v045_signal(fcf, revenue, closeadj):
    base = _std(_f36_cashflow_jerk_fcfmargin(fcf, revenue, 252), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk z × close
def f36cfj_f36_cash_flow_jerk_fcf_z_252d_jerk_v046_signal(fcf, closeadj):
    base = _z(_f36_cashflow_jerk_fcf(fcf, 63), 252) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk z × close
def f36cfj_f36_cash_flow_jerk_ncfo_z_252d_jerk_v047_signal(ncfo, closeadj):
    base = _z(_f36_cashflow_jerk_ncfo(ncfo, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF margin jerk z × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_z_252d_jerk_v048_signal(fcf, revenue, closeadj):
    base = _z(_f36_cashflow_jerk_fcfmargin(fcf, revenue, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo margin jerk z × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_z_252d_jerk_v049_signal(ncfo, revenue, closeadj):
    base = _z(_f36_cashflow_jerk_ncfomargin(ncfo, revenue, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk × revenue × close
def f36cfj_f36_cash_flow_jerk_fcf_xrev_63d_jerk_v050_signal(fcf, revenue, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 63) * revenue.abs() * closeadj * 1e-12
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk × revenue × close
def f36cfj_f36_cash_flow_jerk_ncfo_xrev_252d_jerk_v051_signal(ncfo, revenue, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 252) * revenue.abs() * closeadj * 1e-12
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF margin jerk × revenue × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_xrev_252d_jerk_v052_signal(fcf, revenue, closeadj):
    base = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252) * revenue.abs() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk × ebitda × close
def f36cfj_f36_cash_flow_jerk_fcf_xebitda_63d_jerk_v053_signal(fcf, ebitda, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 63) * ebitda.abs() * closeadj * 1e-12
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk × ebitda × close
def f36cfj_f36_cash_flow_jerk_ncfo_xebitda_252d_jerk_v054_signal(ncfo, ebitda, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 252) * ebitda.abs() * closeadj * 1e-12
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk diff (63m252) × close
def f36cfj_f36_cash_flow_jerk_fcf_diff_63m252_jerk_v055_signal(fcf, closeadj):
    base = (_f36_cashflow_jerk_fcf(fcf, 63) - _f36_cashflow_jerk_fcf(fcf, 252)) * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of ncfo jerk diff (21m63) × close
def f36cfj_f36_cash_flow_jerk_ncfo_diff_21m63_jerk_v056_signal(ncfo, closeadj):
    base = (_f36_cashflow_jerk_ncfo(ncfo, 21) - _f36_cashflow_jerk_ncfo(ncfo, 63)) * closeadj * 1e-6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF vs ncfo × close
def f36cfj_f36_cash_flow_jerk_fcfvsncfo_252d_jerk_v057_signal(fcf, ncfo, closeadj):
    base = (_f36_cashflow_jerk_fcf(fcf, 252) - _f36_cashflow_jerk_ncfo(ncfo, 252)) * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCFm vs ncfom × close
def f36cfj_f36_cash_flow_jerk_fcfmvsncfom_63d_jerk_v058_signal(fcf, ncfo, revenue, closeadj):
    base = (_f36_cashflow_jerk_fcfmargin(fcf, revenue, 63) - _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 63)) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of FCF jerk EMA (21d) × close
def f36cfj_f36_cash_flow_jerk_fcf_ema_21d_jerk_v059_signal(fcf, closeadj):
    j = _f36_cashflow_jerk_fcf(fcf, 21)
    base = j.ewm(span=21, adjust=False).mean() * closeadj * 1e-6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of ncfo jerk EMA (63d) × close
def f36cfj_f36_cash_flow_jerk_ncfo_ema_63d_jerk_v060_signal(ncfo, closeadj):
    j = _f36_cashflow_jerk_ncfo(ncfo, 63)
    base = j.ewm(span=63, adjust=False).mean() * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF margin jerk EMA (252d) × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_ema_252d_jerk_v061_signal(fcf, revenue, closeadj):
    j = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252)
    base = j.ewm(span=252, adjust=False).mean() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF jerk negcount × close
def f36cfj_f36_cash_flow_jerk_fcf_negcount_252d_jerk_v062_signal(fcf, closeadj):
    j = _f36_cashflow_jerk_fcf(fcf, 63)
    base = (j).rolling(252, min_periods=63).mean() * closeadj * 0.001
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk poscount × close
def f36cfj_f36_cash_flow_jerk_ncfo_poscount_252d_jerk_v063_signal(ncfo, closeadj):
    j = _f36_cashflow_jerk_ncfo(ncfo, 63)
    base = (j).rolling(252, min_periods=63).mean() * closeadj * 0.001
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF jerk extremecount × close
def f36cfj_f36_cash_flow_jerk_fcf_extremecount_504d_jerk_v064_signal(fcf, closeadj):
    j = _f36_cashflow_jerk_fcf(fcf, 63)
    z = _z(j, 252)
    flag = (z.abs() > 2.0).astype(float)
    base = flag.rolling(504, min_periods=126).sum() * closeadj * 0.001
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF jerk sum × close
def f36cfj_f36_cash_flow_jerk_fcf_sum_252d_jerk_v065_signal(fcf, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 63).rolling(252, min_periods=63).sum() * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk sum × close
def f36cfj_f36_cash_flow_jerk_ncfo_sum_252d_jerk_v066_signal(ncfo, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 63).rolling(252, min_periods=63).sum() * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF margin jerk sum × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_sum_252d_jerk_v067_signal(fcf, revenue, closeadj):
    base = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 63).rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo margin jerk sum × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_sum_252d_jerk_v068_signal(ncfo, revenue, closeadj):
    base = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 63).rolling(252, min_periods=63).sum() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of FCF jerk × momentum × close
def f36cfj_f36_cash_flow_jerk_fcf_xmom_21d_jerk_v069_signal(fcf, closeadj):
    mom = closeadj.pct_change(21)
    base = _f36_cashflow_jerk_fcf(fcf, 21) * mom * closeadj * 1e-6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of ncfo jerk × momentum × close
def f36cfj_f36_cash_flow_jerk_ncfo_xmom_63d_jerk_v070_signal(ncfo, closeadj):
    mom = closeadj.pct_change(63)
    base = _f36_cashflow_jerk_ncfo(ncfo, 63) * mom * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF margin jerk × momentum × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_xmom_252d_jerk_v071_signal(fcf, revenue, closeadj):
    mom = closeadj.pct_change(252)
    base = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252) * mom * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk normrev × close
def f36cfj_f36_cash_flow_jerk_fcf_normrev_63d_jerk_v072_signal(fcf, revenue, closeadj):
    j = _f36_cashflow_jerk_fcf(fcf, 63)
    rs = _std(revenue, 63).replace(0, np.nan)
    base = j / rs * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk normrev × close
def f36cfj_f36_cash_flow_jerk_ncfo_normrev_252d_jerk_v073_signal(ncfo, revenue, closeadj):
    j = _f36_cashflow_jerk_ncfo(ncfo, 252)
    rs = _std(revenue, 252).replace(0, np.nan)
    base = j / rs * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk × ato × close
def f36cfj_f36_cash_flow_jerk_fcf_xato_63d_jerk_v074_signal(fcf, revenue, assets, closeadj):
    ato = _safe_div(revenue, assets.abs())
    base = _f36_cashflow_jerk_fcf(fcf, 63) * ato * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk × ato × close
def f36cfj_f36_cash_flow_jerk_ncfo_xato_252d_jerk_v075_signal(ncfo, revenue, assets, closeadj):
    ato = _safe_div(revenue, assets.abs())
    base = _f36_cashflow_jerk_ncfo(ncfo, 252) * ato * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk × cr × close
def f36cfj_f36_cash_flow_jerk_fcf_xcr_63d_jerk_v076_signal(fcf, currentratio, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 63) * currentratio * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk × cr × close
def f36cfj_f36_cash_flow_jerk_ncfo_xcr_252d_jerk_v077_signal(ncfo, currentratio, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 252) * currentratio * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk × debt × close
def f36cfj_f36_cash_flow_jerk_fcf_xdebt_63d_jerk_v078_signal(fcf, debt, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 63) * debt.abs() * closeadj * 1e-12
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk × debt × close
def f36cfj_f36_cash_flow_jerk_ncfo_xdebt_252d_jerk_v079_signal(ncfo, debt, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 252) * debt.abs() * closeadj * 1e-12
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk × equity × close
def f36cfj_f36_cash_flow_jerk_fcf_xequity_63d_jerk_v080_signal(fcf, equity, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 63) * equity.abs() * closeadj * 1e-12
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk × equity × close
def f36cfj_f36_cash_flow_jerk_ncfo_xequity_252d_jerk_v081_signal(ncfo, equity, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 252) * equity.abs() * closeadj * 1e-12
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk × eps × close
def f36cfj_f36_cash_flow_jerk_fcf_xeps_63d_jerk_v082_signal(fcf, eps, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 63) * eps * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk × eps × close
def f36cfj_f36_cash_flow_jerk_ncfo_xeps_252d_jerk_v083_signal(ncfo, eps, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 252) * eps * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk × netinc × close
def f36cfj_f36_cash_flow_jerk_fcf_xnetinc_63d_jerk_v084_signal(fcf, netinc, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 63) * netinc.abs() * closeadj * 1e-12
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk × netinc × close
def f36cfj_f36_cash_flow_jerk_ncfo_xnetinc_252d_jerk_v085_signal(ncfo, netinc, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 252) * netinc.abs() * closeadj * 1e-12
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk × wc × close
def f36cfj_f36_cash_flow_jerk_fcf_xwc_63d_jerk_v086_signal(fcf, workingcapital, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 63) * workingcapital.abs() * closeadj * 1e-12
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk × wc × close
def f36cfj_f36_cash_flow_jerk_ncfo_xwc_252d_jerk_v087_signal(ncfo, workingcapital, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 252) * workingcapital.abs() * closeadj * 1e-12
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk normretvol × close
def f36cfj_f36_cash_flow_jerk_fcf_normretvol_63d_jerk_v088_signal(fcf, closeadj):
    rv = _std(closeadj.pct_change(), 21).replace(0, np.nan)
    base = _f36_cashflow_jerk_fcf(fcf, 63) / rv * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk normretvol × close
def f36cfj_f36_cash_flow_jerk_ncfo_normretvol_252d_jerk_v089_signal(ncfo, closeadj):
    rv = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    base = _f36_cashflow_jerk_ncfo(ncfo, 252) / rv * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk × revtrend × close
def f36cfj_f36_cash_flow_jerk_fcf_xrevtrend_63d_jerk_v090_signal(fcf, revenue, closeadj):
    rt = _diff(revenue, 63) / revenue.abs().replace(0, np.nan)
    base = _f36_cashflow_jerk_fcf(fcf, 63) * rt * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of composite (252d) × close
def f36cfj_f36_cash_flow_jerk_composite_252d_jerk_v091_signal(fcf, ncfo, revenue, closeadj):
    a = _f36_cashflow_jerk_fcf(fcf, 252) * 1e-6
    b = _f36_cashflow_jerk_ncfo(ncfo, 252) * 1e-6
    c = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252)
    base = (a + b + c) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 5d FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_5d_jerk_v092_signal(fcf, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 5) * closeadj * 1e-6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 10d FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_10d_jerk_v093_signal(fcf, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 10) * closeadj * 1e-6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 42d FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_42d_jerk_v094_signal(fcf, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 42) * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 189d FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_189d_jerk_v095_signal(fcf, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 189) * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 378d FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_378d_jerk_v096_signal(fcf, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 378) * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 5d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_5d_jerk_v097_signal(ncfo, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 5) * closeadj * 1e-6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 10d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_10d_jerk_v098_signal(ncfo, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 10) * closeadj * 1e-6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 42d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_42d_jerk_v099_signal(ncfo, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 42) * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 189d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_189d_jerk_v100_signal(ncfo, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 189) * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 378d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_378d_jerk_v101_signal(ncfo, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 378) * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 5d FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_5d_jerk_v102_signal(fcf, revenue, closeadj):
    base = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 42d FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_42d_jerk_v103_signal(fcf, revenue, closeadj):
    base = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 189d FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_189d_jerk_v104_signal(fcf, revenue, closeadj):
    base = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of 5d ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_5d_jerk_v105_signal(ncfo, revenue, closeadj):
    base = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 5) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of 42d ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_42d_jerk_v106_signal(ncfo, revenue, closeadj):
    base = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 42) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of 189d ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_189d_jerk_v107_signal(ncfo, revenue, closeadj):
    base = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 189) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk × growth × close
def f36cfj_f36_cash_flow_jerk_fcf_xgrowth_63d_jerk_v108_signal(fcf, revenue, closeadj):
    g = revenue.pct_change(63)
    base = _f36_cashflow_jerk_fcf(fcf, 63) * g * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk × growth × close
def f36cfj_f36_cash_flow_jerk_ncfo_xgrowth_252d_jerk_v109_signal(ncfo, revenue, closeadj):
    g = revenue.pct_change(252)
    base = _f36_cashflow_jerk_ncfo(ncfo, 252) * g * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF margin jerk × growth × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_xgrowth_252d_jerk_v110_signal(fcf, revenue, closeadj):
    g = revenue.pct_change(252)
    base = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252) * g * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk × dollar volume
def f36cfj_f36_cash_flow_jerk_fcf_xdv_63d_jerk_v111_signal(fcf, closeadj, volume):
    dv = closeadj * volume
    base = _f36_cashflow_jerk_fcf(fcf, 63) * dv * 1e-9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk × dollar volume
def f36cfj_f36_cash_flow_jerk_ncfo_xdv_252d_jerk_v112_signal(ncfo, closeadj, volume):
    dv = closeadj * volume
    base = _f36_cashflow_jerk_ncfo(ncfo, 252) * dv * 1e-9
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk × volz × close
def f36cfj_f36_cash_flow_jerk_fcf_xvolz_63d_jerk_v113_signal(fcf, closeadj, volume):
    base = _f36_cashflow_jerk_fcf(fcf, 63) * _z(volume, 63) * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of FCF jerk × shortret × close
def f36cfj_f36_cash_flow_jerk_fcf_xshortret_21d_jerk_v114_signal(fcf, closeadj):
    r = closeadj.pct_change(5)
    base = _f36_cashflow_jerk_fcf(fcf, 21) * r * closeadj * 1e-6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of ncfo jerk × longret × close
def f36cfj_f36_cash_flow_jerk_ncfo_xlongret_63d_jerk_v115_signal(ncfo, closeadj):
    r = closeadj.pct_change(126)
    base = _f36_cashflow_jerk_ncfo(ncfo, 63) * r * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF jerk EMA (252d) × close
def f36cfj_f36_cash_flow_jerk_fcf_ema_252d_jerk_v116_signal(fcf, closeadj):
    j = _f36_cashflow_jerk_fcf(fcf, 252)
    base = j.ewm(span=252, adjust=False).mean() * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of ncfo jerk EMA (21d) × close
def f36cfj_f36_cash_flow_jerk_ncfo_ema_21d_jerk_v117_signal(ncfo, closeadj):
    j = _f36_cashflow_jerk_ncfo(ncfo, 21)
    base = j.ewm(span=21, adjust=False).mean() * closeadj * 1e-6
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of FCF margin jerk EMA (21d) × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_ema_21d_jerk_v118_signal(fcf, revenue, closeadj):
    j = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 21)
    base = j.ewm(span=21, adjust=False).mean() * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of ncfo margin jerk EMA (63d) × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_ema_63d_jerk_v119_signal(ncfo, revenue, closeadj):
    j = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 63)
    base = j.ewm(span=63, adjust=False).mean() * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF × ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_fcfxncfo_63d_jerk_v120_signal(fcf, ncfo, closeadj):
    a = _f36_cashflow_jerk_fcf(fcf, 63)
    b = _f36_cashflow_jerk_ncfo(ncfo, 63)
    base = a * b * closeadj * 1e-18
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCFm × ncfom jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmxncfom_252d_jerk_v121_signal(fcf, ncfo, revenue, closeadj):
    a = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252)
    b = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 252)
    base = a * b * closeadj * 100.0
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF minus ncfo × close
def f36cfj_f36_cash_flow_jerk_fcfminusncfo_63d_jerk_v122_signal(fcf, ncfo, closeadj):
    base = (_f36_cashflow_jerk_fcf(fcf, 63) - _f36_cashflow_jerk_ncfo(ncfo, 63)) * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfom minus fcfm × close
def f36cfj_f36_cash_flow_jerk_ncfomminusfcfm_252d_jerk_v123_signal(fcf, ncfo, revenue, closeadj):
    base = (_f36_cashflow_jerk_ncfomargin(ncfo, revenue, 252) - _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252)) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of FCF jerk × intexp × close
def f36cfj_f36_cash_flow_jerk_fcf_xintexp_21d_jerk_v124_signal(fcf, intexp, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 21) * intexp.abs() * closeadj * 1e-11
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk × taxexp × close
def f36cfj_f36_cash_flow_jerk_ncfo_xtaxexp_252d_jerk_v125_signal(ncfo, taxexp, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 252) * taxexp.abs() * closeadj * 1e-11
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk × capex × close
def f36cfj_f36_cash_flow_jerk_fcf_xcapex_63d_jerk_v126_signal(fcf, capex, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 63) * capex.abs() * closeadj * 1e-11
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF margin jerk × capex × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_xcapex_252d_jerk_v127_signal(fcf, revenue, capex, closeadj):
    base = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252) * capex.abs() * closeadj * 1e-5
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk × range × close
def f36cfj_f36_cash_flow_jerk_fcf_xrange_63d_jerk_v128_signal(fcf, closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    base = _f36_cashflow_jerk_fcf(fcf, 63) * rng * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk × range × close
def f36cfj_f36_cash_flow_jerk_ncfo_xrange_252d_jerk_v129_signal(ncfo, closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    base = _f36_cashflow_jerk_ncfo(ncfo, 252) * rng * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk × sqrt(rev) × close
def f36cfj_f36_cash_flow_jerk_fcf_xrevsq_63d_jerk_v130_signal(fcf, revenue, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 63) * (revenue.abs() ** 0.5) * closeadj * 1e-9
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of meanof4 (252d) × close
def f36cfj_f36_cash_flow_jerk_meanof4_252d_jerk_v131_signal(fcf, ncfo, revenue, closeadj):
    a = _f36_cashflow_jerk_fcf(fcf, 252) * 1e-6
    b = _f36_cashflow_jerk_ncfo(ncfo, 252) * 1e-6
    c = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252)
    d = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 252)
    base = ((a + b + c + d) / 4.0) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of meanof4 (63d) × close
def f36cfj_f36_cash_flow_jerk_meanof4_63d_jerk_v132_signal(fcf, ncfo, revenue, closeadj):
    a = _f36_cashflow_jerk_fcf(fcf, 63) * 1e-6
    b = _f36_cashflow_jerk_ncfo(ncfo, 63) * 1e-6
    c = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 63)
    d = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 63)
    base = ((a + b + c + d) / 4.0) * closeadj
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d jerk of meanof4 (21d) × close
def f36cfj_f36_cash_flow_jerk_meanof4_21d_jerk_v133_signal(fcf, ncfo, revenue, closeadj):
    a = _f36_cashflow_jerk_fcf(fcf, 21) * 1e-6
    b = _f36_cashflow_jerk_ncfo(ncfo, 21) * 1e-6
    c = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 21)
    d = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 21)
    base = ((a + b + c + d) / 4.0) * closeadj
    result = _jerk(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk dispersion (63d) × close
def f36cfj_f36_cash_flow_jerk_fcf_dispersion_63d_jerk_v134_signal(fcf, closeadj):
    base = _std(_f36_cashflow_jerk_fcf(fcf, 21), 63) * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk dispersion (252d) × close
def f36cfj_f36_cash_flow_jerk_ncfo_dispersion_252d_jerk_v135_signal(ncfo, closeadj):
    base = _std(_f36_cashflow_jerk_ncfo(ncfo, 63), 252) * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF margin jerk dispersion (252d) × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_dispersion_252d_jerk_v136_signal(fcf, revenue, closeadj):
    base = _std(_f36_cashflow_jerk_fcfmargin(fcf, revenue, 63), 252) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk × sharesbas × close
def f36cfj_f36_cash_flow_jerk_fcf_xsharesbas_63d_jerk_v137_signal(fcf, sharesbas, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 63) * sharesbas * closeadj * 1e-12
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk × sharesbas × close
def f36cfj_f36_cash_flow_jerk_ncfo_xsharesbas_252d_jerk_v138_signal(ncfo, sharesbas, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 252) * sharesbas * closeadj * 1e-12
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF jerk × ncfi × close
def f36cfj_f36_cash_flow_jerk_fcf_xncfi_252d_jerk_v139_signal(fcf, ncfi, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 252) * ncfi.abs() * closeadj * 1e-12
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk × liab × close
def f36cfj_f36_cash_flow_jerk_fcf_xliab_63d_jerk_v140_signal(fcf, liabilities, closeadj):
    base = _f36_cashflow_jerk_fcf(fcf, 63) * liabilities.abs() * closeadj * 1e-12
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk × liab × close
def f36cfj_f36_cash_flow_jerk_ncfo_xliab_252d_jerk_v141_signal(ncfo, liabilities, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 252) * liabilities.abs() * closeadj * 1e-12
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF jerk range × close
def f36cfj_f36_cash_flow_jerk_fcf_range_252d_jerk_v142_signal(fcf, closeadj):
    j = _f36_cashflow_jerk_fcf(fcf, 21)
    rng = j.rolling(252, min_periods=63).max() - j.rolling(252, min_periods=63).min()
    base = rng * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk range × close
def f36cfj_f36_cash_flow_jerk_ncfo_range_252d_jerk_v143_signal(ncfo, closeadj):
    j = _f36_cashflow_jerk_ncfo(ncfo, 21)
    rng = j.rolling(252, min_periods=63).max() - j.rolling(252, min_periods=63).min()
    base = rng * closeadj * 1e-6
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF jerk skew (63d) × close
def f36cfj_f36_cash_flow_jerk_fcf_skew_63d_jerk_v144_signal(fcf, closeadj):
    j = _f36_cashflow_jerk_fcf(fcf, 21)
    base = j.rolling(63, min_periods=21).skew() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of FCF jerk skew (252d) × close
def f36cfj_f36_cash_flow_jerk_fcf_skew_252d_jerk_v145_signal(fcf, closeadj):
    j = _f36_cashflow_jerk_fcf(fcf, 21)
    base = j.rolling(252, min_periods=63).skew() * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk × eps trend × close
def f36cfj_f36_cash_flow_jerk_fcf_xepstrend_63d_jerk_v146_signal(fcf, eps, closeadj):
    et = _diff(eps, 63)
    base = _f36_cashflow_jerk_fcf(fcf, 63) * et * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of FCF jerk × ebitda growth × close
def f36cfj_f36_cash_flow_jerk_fcf_xebitdagrowth_63d_jerk_v147_signal(fcf, ebitda, closeadj):
    g = ebitda.pct_change(63)
    base = _f36_cashflow_jerk_fcf(fcf, 63) * g * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of ncfo jerk × netinc × close
def f36cfj_f36_cash_flow_jerk_ncfo_xnetinc_252d_jerk_v148_signal(ncfo, netinc, closeadj):
    base = _f36_cashflow_jerk_ncfo(ncfo, 252) * netinc.abs() * closeadj * 1e-12
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d jerk of severitysum (252d) × close
def f36cfj_f36_cash_flow_jerk_severitysum_252d_jerk_v149_signal(fcf, ncfo, revenue, closeadj):
    a = _f36_cashflow_jerk_fcf(fcf, 252).abs() * 1e-6
    b = _f36_cashflow_jerk_ncfo(ncfo, 252).abs() * 1e-6
    c = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252).abs()
    base = (a + b + c) * closeadj
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d jerk of severityxrev (63d) × close
def f36cfj_f36_cash_flow_jerk_severityxrev_63d_jerk_v150_signal(fcf, ncfo, revenue, closeadj):
    a = _f36_cashflow_jerk_fcf(fcf, 63).abs() * 1e-6
    b = _f36_cashflow_jerk_ncfo(ncfo, 63).abs() * 1e-6
    base = (a + b) * revenue.abs() * closeadj * 1e-6
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36cfj_f36_cash_flow_jerk_fcf_21d_jerk_v001_signal,
    f36cfj_f36_cash_flow_jerk_fcf_21d_jerk_v002_signal,
    f36cfj_f36_cash_flow_jerk_fcf_63d_jerk_v003_signal,
    f36cfj_f36_cash_flow_jerk_fcf_63d_jerk_v004_signal,
    f36cfj_f36_cash_flow_jerk_fcf_126d_jerk_v005_signal,
    f36cfj_f36_cash_flow_jerk_fcf_126d_jerk_v006_signal,
    f36cfj_f36_cash_flow_jerk_fcf_252d_jerk_v007_signal,
    f36cfj_f36_cash_flow_jerk_fcf_252d_jerk_v008_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_21d_jerk_v009_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_21d_jerk_v010_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_63d_jerk_v011_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_63d_jerk_v012_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_126d_jerk_v013_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_126d_jerk_v014_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_252d_jerk_v015_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_252d_jerk_v016_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_21d_jerk_v017_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_21d_jerk_v018_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_63d_jerk_v019_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_63d_jerk_v020_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_126d_jerk_v021_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_126d_jerk_v022_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_252d_jerk_v023_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_252d_jerk_v024_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_21d_jerk_v025_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_21d_jerk_v026_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_63d_jerk_v027_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_63d_jerk_v028_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_126d_jerk_v029_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_126d_jerk_v030_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_252d_jerk_v031_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_252d_jerk_v032_signal,
    f36cfj_f36_cash_flow_jerk_fcf_abs_21d_jerk_v033_signal,
    f36cfj_f36_cash_flow_jerk_fcf_abs_63d_jerk_v034_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_abs_126d_jerk_v035_signal,
    f36cfj_f36_cash_flow_jerk_fcf_sq_21d_jerk_v036_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_sq_63d_jerk_v037_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_sq_252d_jerk_v038_signal,
    f36cfj_f36_cash_flow_jerk_fcf_mean_63d_jerk_v039_signal,
    f36cfj_f36_cash_flow_jerk_fcf_mean_252d_jerk_v040_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_mean_63d_jerk_v041_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_mean_252d_jerk_v042_signal,
    f36cfj_f36_cash_flow_jerk_fcf_std_63d_jerk_v043_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_std_252d_jerk_v044_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_std_252d_jerk_v045_signal,
    f36cfj_f36_cash_flow_jerk_fcf_z_252d_jerk_v046_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_z_252d_jerk_v047_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_z_252d_jerk_v048_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_z_252d_jerk_v049_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xrev_63d_jerk_v050_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xrev_252d_jerk_v051_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_xrev_252d_jerk_v052_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xebitda_63d_jerk_v053_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xebitda_252d_jerk_v054_signal,
    f36cfj_f36_cash_flow_jerk_fcf_diff_63m252_jerk_v055_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_diff_21m63_jerk_v056_signal,
    f36cfj_f36_cash_flow_jerk_fcfvsncfo_252d_jerk_v057_signal,
    f36cfj_f36_cash_flow_jerk_fcfmvsncfom_63d_jerk_v058_signal,
    f36cfj_f36_cash_flow_jerk_fcf_ema_21d_jerk_v059_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_ema_63d_jerk_v060_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_ema_252d_jerk_v061_signal,
    f36cfj_f36_cash_flow_jerk_fcf_negcount_252d_jerk_v062_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_poscount_252d_jerk_v063_signal,
    f36cfj_f36_cash_flow_jerk_fcf_extremecount_504d_jerk_v064_signal,
    f36cfj_f36_cash_flow_jerk_fcf_sum_252d_jerk_v065_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_sum_252d_jerk_v066_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_sum_252d_jerk_v067_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_sum_252d_jerk_v068_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xmom_21d_jerk_v069_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xmom_63d_jerk_v070_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_xmom_252d_jerk_v071_signal,
    f36cfj_f36_cash_flow_jerk_fcf_normrev_63d_jerk_v072_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_normrev_252d_jerk_v073_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xato_63d_jerk_v074_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xato_252d_jerk_v075_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xcr_63d_jerk_v076_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xcr_252d_jerk_v077_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xdebt_63d_jerk_v078_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xdebt_252d_jerk_v079_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xequity_63d_jerk_v080_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xequity_252d_jerk_v081_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xeps_63d_jerk_v082_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xeps_252d_jerk_v083_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xnetinc_63d_jerk_v084_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xnetinc_252d_jerk_v085_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xwc_63d_jerk_v086_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xwc_252d_jerk_v087_signal,
    f36cfj_f36_cash_flow_jerk_fcf_normretvol_63d_jerk_v088_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_normretvol_252d_jerk_v089_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xrevtrend_63d_jerk_v090_signal,
    f36cfj_f36_cash_flow_jerk_composite_252d_jerk_v091_signal,
    f36cfj_f36_cash_flow_jerk_fcf_5d_jerk_v092_signal,
    f36cfj_f36_cash_flow_jerk_fcf_10d_jerk_v093_signal,
    f36cfj_f36_cash_flow_jerk_fcf_42d_jerk_v094_signal,
    f36cfj_f36_cash_flow_jerk_fcf_189d_jerk_v095_signal,
    f36cfj_f36_cash_flow_jerk_fcf_378d_jerk_v096_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_5d_jerk_v097_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_10d_jerk_v098_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_42d_jerk_v099_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_189d_jerk_v100_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_378d_jerk_v101_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_5d_jerk_v102_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_42d_jerk_v103_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_189d_jerk_v104_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_5d_jerk_v105_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_42d_jerk_v106_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_189d_jerk_v107_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xgrowth_63d_jerk_v108_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xgrowth_252d_jerk_v109_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_xgrowth_252d_jerk_v110_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xdv_63d_jerk_v111_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xdv_252d_jerk_v112_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xvolz_63d_jerk_v113_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xshortret_21d_jerk_v114_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xlongret_63d_jerk_v115_signal,
    f36cfj_f36_cash_flow_jerk_fcf_ema_252d_jerk_v116_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_ema_21d_jerk_v117_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_ema_21d_jerk_v118_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_ema_63d_jerk_v119_signal,
    f36cfj_f36_cash_flow_jerk_fcfxncfo_63d_jerk_v120_signal,
    f36cfj_f36_cash_flow_jerk_fcfmxncfom_252d_jerk_v121_signal,
    f36cfj_f36_cash_flow_jerk_fcfminusncfo_63d_jerk_v122_signal,
    f36cfj_f36_cash_flow_jerk_ncfomminusfcfm_252d_jerk_v123_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xintexp_21d_jerk_v124_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xtaxexp_252d_jerk_v125_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xcapex_63d_jerk_v126_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_xcapex_252d_jerk_v127_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xrange_63d_jerk_v128_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xrange_252d_jerk_v129_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xrevsq_63d_jerk_v130_signal,
    f36cfj_f36_cash_flow_jerk_meanof4_252d_jerk_v131_signal,
    f36cfj_f36_cash_flow_jerk_meanof4_63d_jerk_v132_signal,
    f36cfj_f36_cash_flow_jerk_meanof4_21d_jerk_v133_signal,
    f36cfj_f36_cash_flow_jerk_fcf_dispersion_63d_jerk_v134_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_dispersion_252d_jerk_v135_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_dispersion_252d_jerk_v136_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xsharesbas_63d_jerk_v137_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xsharesbas_252d_jerk_v138_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xncfi_252d_jerk_v139_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xliab_63d_jerk_v140_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xliab_252d_jerk_v141_signal,
    f36cfj_f36_cash_flow_jerk_fcf_range_252d_jerk_v142_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_range_252d_jerk_v143_signal,
    f36cfj_f36_cash_flow_jerk_fcf_skew_63d_jerk_v144_signal,
    f36cfj_f36_cash_flow_jerk_fcf_skew_252d_jerk_v145_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xepstrend_63d_jerk_v146_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xebitdagrowth_63d_jerk_v147_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xnetinc_252d_jerk_v148_signal,
    f36cfj_f36_cash_flow_jerk_severitysum_252d_jerk_v149_signal,
    f36cfj_f36_cash_flow_jerk_severityxrev_63d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_CASH_FLOW_JERK_REGISTRY_JERK = REGISTRY


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
    revenue = pd.Series(1e7 * np.exp(np.cumsum(np.random.normal(0.0008, 0.01, n))), name="revenue")
    netinc = pd.Series(1e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.012, n))) * np.sign(np.random.normal(0.5, 1.0, n)), name="netinc")
    ebitda = pd.Series(2e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.01, n))) * np.sign(np.random.normal(0.7, 1.0, n)), name="ebitda")
    eps = pd.Series(np.cumsum(np.random.normal(0.001, 0.05, n)) + 1.0, name="eps")
    fcf = pd.Series(8e5 * np.exp(np.cumsum(np.random.normal(0.0005, 0.013, n))) * np.sign(np.random.normal(0.6, 1.0, n)), name="fcf")
    ncfo = pd.Series(1.2e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.012, n))) * np.sign(np.random.normal(0.8, 1.0, n)), name="ncfo")
    ncfi = pd.Series(7e5 * np.exp(np.cumsum(np.random.normal(0.0003, 0.011, n))) * np.sign(np.random.normal(0.4, 1.0, n)), name="ncfi")
    capex = pd.Series(9e5 * np.exp(np.cumsum(np.random.normal(0.0004, 0.011, n))), name="capex")
    intexp = pd.Series(2e5 * np.exp(np.cumsum(np.random.normal(0.0003, 0.008, n))), name="intexp")
    taxexp = pd.Series(3e5 * np.exp(np.cumsum(np.random.normal(0.0004, 0.009, n))), name="taxexp")
    sharesbas = pd.Series(1e7 + np.cumsum(np.random.normal(1e3, 5e3, n)), name="sharesbas")
    liabilities = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.007, n))), name="liabilities")
    assets = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0004, 0.006, n))), name="assets")
    debt = pd.Series(1e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.008, n))), name="debt")
    equity = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0005, 0.007, n))), name="equity")
    workingcapital = pd.Series(8e6 * np.exp(np.cumsum(np.random.normal(0.0004, 0.01, n))) * np.sign(np.random.normal(0.7, 1.0, n)), name="workingcapital")
    currentratio = pd.Series(1.5 + np.cumsum(np.random.normal(0.0, 0.01, n)) * 0.1, name="currentratio")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "netinc": netinc, "ebitda": ebitda, "eps": eps,
        "fcf": fcf, "ncfo": ncfo, "ncfi": ncfi, "capex": capex,
        "intexp": intexp, "taxexp": taxexp, "sharesbas": sharesbas, "liabilities": liabilities,
        "assets": assets, "debt": debt, "equity": equity, "workingcapital": workingcapital, "currentratio": currentratio,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f36_cashflow_jerk_fcf", "_f36_cashflow_jerk_ncfo", "_f36_cashflow_jerk_fcfmargin", "_f36_cashflow_jerk_ncfomargin")
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
    print(f"OK f36_cash_flow_jerk_3rd_derivatives_001_150_claude: {n_features} features pass")
