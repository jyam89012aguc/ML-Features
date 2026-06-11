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


# ===== folder domain primitives (cashflow jerk = 3rd derivative of FCF/ncfo) =====
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


# 21d FCF jerk × close / scale
def f36cfj_f36_cash_flow_jerk_fcf_21d_base_v001_signal(fcf, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 21) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_63d_base_v002_signal(fcf, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 63) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 126d FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_126d_base_v003_signal(fcf, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 126) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_252d_base_v004_signal(fcf, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 252) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_21d_base_v005_signal(ncfo, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 21) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_63d_base_v006_signal(ncfo, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 63) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_126d_base_v007_signal(ncfo, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 126) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_252d_base_v008_signal(ncfo, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_21d_base_v009_signal(fcf, revenue, closeadj):
    result = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_63d_base_v010_signal(fcf, revenue, closeadj):
    result = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_126d_base_v011_signal(fcf, revenue, closeadj):
    result = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_252d_base_v012_signal(fcf, revenue, closeadj):
    result = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_21d_base_v013_signal(ncfo, revenue, closeadj):
    result = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_63d_base_v014_signal(ncfo, revenue, closeadj):
    result = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_126d_base_v015_signal(ncfo, revenue, closeadj):
    result = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_252d_base_v016_signal(ncfo, revenue, closeadj):
    result = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d |FCF jerk| × close
def f36cfj_f36_cash_flow_jerk_fcf_abs_21d_base_v017_signal(fcf, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 21).abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d |FCF jerk| × close
def f36cfj_f36_cash_flow_jerk_fcf_abs_63d_base_v018_signal(fcf, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 63).abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 126d |ncfo jerk| × close
def f36cfj_f36_cash_flow_jerk_ncfo_abs_126d_base_v019_signal(ncfo, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 126).abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF jerk squared × close
def f36cfj_f36_cash_flow_jerk_fcf_sq_21d_base_v020_signal(fcf, closeadj):
    j = _f36_cashflow_jerk_fcf(fcf, 21)
    result = j * j.abs() * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo jerk squared × close
def f36cfj_f36_cash_flow_jerk_ncfo_sq_63d_base_v021_signal(ncfo, closeadj):
    j = _f36_cashflow_jerk_ncfo(ncfo, 63)
    result = j * j.abs() * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF margin jerk squared × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_sq_252d_base_v022_signal(fcf, revenue, closeadj):
    j = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252)
    result = j * j.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_mean_63d_base_v023_signal(fcf, closeadj):
    result = _mean(_f36_cashflow_jerk_fcf(fcf, 63), 63) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_mean_252d_base_v024_signal(fcf, closeadj):
    result = _mean(_f36_cashflow_jerk_fcf(fcf, 252), 252) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d mean of ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_mean_63d_base_v025_signal(ncfo, closeadj):
    result = _mean(_f36_cashflow_jerk_ncfo(ncfo, 63), 63) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d mean of FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_mean_252d_base_v026_signal(fcf, revenue, closeadj):
    result = _mean(_f36_cashflow_jerk_fcfmargin(fcf, revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d std of FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_std_63d_base_v027_signal(fcf, closeadj):
    result = _std(_f36_cashflow_jerk_fcf(fcf, 63), 63) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_std_252d_base_v028_signal(ncfo, closeadj):
    result = _std(_f36_cashflow_jerk_ncfo(ncfo, 252), 252) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d std of FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_std_252d_base_v029_signal(fcf, revenue, closeadj):
    result = _std(_f36_cashflow_jerk_fcfmargin(fcf, revenue, 252), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_z_252d_base_v030_signal(fcf, closeadj):
    result = _z(_f36_cashflow_jerk_fcf(fcf, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_z_252d_base_v031_signal(ncfo, closeadj):
    result = _z(_f36_cashflow_jerk_ncfo(ncfo, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_z_252d_base_v032_signal(fcf, revenue, closeadj):
    result = _z(_f36_cashflow_jerk_fcfmargin(fcf, revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d zscore of ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_z_252d_base_v033_signal(ncfo, revenue, closeadj):
    result = _z(_f36_cashflow_jerk_ncfomargin(ncfo, revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × revenue level × close
def f36cfj_f36_cash_flow_jerk_fcf_xrev_63d_base_v034_signal(fcf, revenue, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 63) * revenue.abs() * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk × revenue level × close
def f36cfj_f36_cash_flow_jerk_ncfo_xrev_252d_base_v035_signal(ncfo, revenue, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) * revenue.abs() * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF margin jerk × revenue × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_xrev_252d_base_v036_signal(fcf, revenue, closeadj):
    result = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252) * revenue.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × ebitda × close
def f36cfj_f36_cash_flow_jerk_fcf_xebitda_63d_base_v037_signal(fcf, ebitda, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 63) * ebitda.abs() * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk × ebitda × close
def f36cfj_f36_cash_flow_jerk_ncfo_xebitda_252d_base_v038_signal(ncfo, ebitda, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) * ebitda.abs() * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk minus 252d FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_diff_63m252_base_v039_signal(fcf, closeadj):
    a = _f36_cashflow_jerk_fcf(fcf, 63)
    b = _f36_cashflow_jerk_fcf(fcf, 252)
    result = (a - b) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncfo jerk minus 63d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_diff_21m63_base_v040_signal(ncfo, closeadj):
    a = _f36_cashflow_jerk_ncfo(ncfo, 21)
    b = _f36_cashflow_jerk_ncfo(ncfo, 63)
    result = (a - b) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF jerk minus ncfo jerk (capex jerk proxy)
def f36cfj_f36_cash_flow_jerk_fcfvsncfo_252d_base_v041_signal(fcf, ncfo, closeadj):
    a = _f36_cashflow_jerk_fcf(fcf, 252)
    b = _f36_cashflow_jerk_ncfo(ncfo, 252)
    result = (a - b) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF margin jerk minus ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmvsncfom_63d_base_v042_signal(fcf, ncfo, revenue, closeadj):
    a = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 63)
    b = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 63)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d EMA of FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_ema_21d_base_v043_signal(fcf, closeadj):
    j = _f36_cashflow_jerk_fcf(fcf, 21)
    result = j.ewm(span=21, adjust=False).mean() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_ema_63d_base_v044_signal(ncfo, closeadj):
    j = _f36_cashflow_jerk_ncfo(ncfo, 63)
    result = j.ewm(span=63, adjust=False).mean() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_ema_252d_base_v045_signal(fcf, revenue, closeadj):
    j = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252)
    result = j.ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of negative FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_negcount_252d_base_v046_signal(fcf, closeadj):
    j = _f36_cashflow_jerk_fcf(fcf, 63)
    result = (j).rolling(252, min_periods=63).mean() * closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of positive ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_poscount_252d_base_v047_signal(ncfo, closeadj):
    j = _f36_cashflow_jerk_ncfo(ncfo, 63)
    result = (j).rolling(252, min_periods=63).mean() * closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of large FCF jerk events × close
def f36cfj_f36_cash_flow_jerk_fcf_extremecount_504d_base_v048_signal(fcf, closeadj):
    j = _f36_cashflow_jerk_fcf(fcf, 63)
    z = _z(j, 252)
    flag = (z.abs() > 2.0).astype(float)
    result = flag.rolling(504, min_periods=126).sum() * closeadj * 0.001
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_sum_252d_base_v049_signal(fcf, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 63).rolling(252, min_periods=63).sum() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_sum_252d_base_v050_signal(ncfo, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 63).rolling(252, min_periods=63).sum() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_sum_252d_base_v051_signal(fcf, revenue, closeadj):
    result = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 63).rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d sum of ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_sum_252d_base_v052_signal(ncfo, revenue, closeadj):
    result = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 63).rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF jerk × close-momentum
def f36cfj_f36_cash_flow_jerk_fcf_xmom_21d_base_v053_signal(fcf, closeadj):
    mom = closeadj.pct_change(21)
    result = _f36_cashflow_jerk_fcf(fcf, 21) * mom * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo jerk × close-momentum
def f36cfj_f36_cash_flow_jerk_ncfo_xmom_63d_base_v054_signal(ncfo, closeadj):
    mom = closeadj.pct_change(63)
    result = _f36_cashflow_jerk_ncfo(ncfo, 63) * mom * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF margin jerk × close-momentum
def f36cfj_f36_cash_flow_jerk_fcfmargin_xmom_252d_base_v055_signal(fcf, revenue, closeadj):
    mom = closeadj.pct_change(252)
    result = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252) * mom * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk normalized by revenue std × close
def f36cfj_f36_cash_flow_jerk_fcf_normrev_63d_base_v056_signal(fcf, revenue, closeadj):
    j = _f36_cashflow_jerk_fcf(fcf, 63)
    rs = _std(revenue, 63).replace(0, np.nan)
    result = j / rs * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk normalized by revenue std × close
def f36cfj_f36_cash_flow_jerk_ncfo_normrev_252d_base_v057_signal(ncfo, revenue, closeadj):
    j = _f36_cashflow_jerk_ncfo(ncfo, 252)
    rs = _std(revenue, 252).replace(0, np.nan)
    result = j / rs * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × asset turnover × close
def f36cfj_f36_cash_flow_jerk_fcf_xato_63d_base_v058_signal(fcf, revenue, assets, closeadj):
    ato = _safe_div(revenue, assets.abs())
    result = _f36_cashflow_jerk_fcf(fcf, 63) * ato * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk × asset turnover × close
def f36cfj_f36_cash_flow_jerk_ncfo_xato_252d_base_v059_signal(ncfo, revenue, assets, closeadj):
    ato = _safe_div(revenue, assets.abs())
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) * ato * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × current ratio × close
def f36cfj_f36_cash_flow_jerk_fcf_xcr_63d_base_v060_signal(fcf, currentratio, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 63) * currentratio * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk × current ratio × close
def f36cfj_f36_cash_flow_jerk_ncfo_xcr_252d_base_v061_signal(ncfo, currentratio, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) * currentratio * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × debt × close
def f36cfj_f36_cash_flow_jerk_fcf_xdebt_63d_base_v062_signal(fcf, debt, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 63) * debt.abs() * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk × debt × close
def f36cfj_f36_cash_flow_jerk_ncfo_xdebt_252d_base_v063_signal(ncfo, debt, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) * debt.abs() * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × equity × close
def f36cfj_f36_cash_flow_jerk_fcf_xequity_63d_base_v064_signal(fcf, equity, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 63) * equity.abs() * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk × equity × close
def f36cfj_f36_cash_flow_jerk_ncfo_xequity_252d_base_v065_signal(ncfo, equity, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) * equity.abs() * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × eps × close
def f36cfj_f36_cash_flow_jerk_fcf_xeps_63d_base_v066_signal(fcf, eps, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 63) * eps * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk × eps × close
def f36cfj_f36_cash_flow_jerk_ncfo_xeps_252d_base_v067_signal(ncfo, eps, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) * eps * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × netinc × close
def f36cfj_f36_cash_flow_jerk_fcf_xnetinc_63d_base_v068_signal(fcf, netinc, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 63) * netinc.abs() * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk × netinc × close
def f36cfj_f36_cash_flow_jerk_ncfo_xnetinc_252d_base_v069_signal(ncfo, netinc, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) * netinc.abs() * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × workingcapital × close
def f36cfj_f36_cash_flow_jerk_fcf_xwc_63d_base_v070_signal(fcf, workingcapital, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 63) * workingcapital.abs() * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk × workingcapital × close
def f36cfj_f36_cash_flow_jerk_ncfo_xwc_252d_base_v071_signal(ncfo, workingcapital, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) * workingcapital.abs() * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk normalized by 21d return vol × close
def f36cfj_f36_cash_flow_jerk_fcf_normretvol_63d_base_v072_signal(fcf, closeadj):
    rv = _std(closeadj.pct_change(), 21).replace(0, np.nan)
    result = _f36_cashflow_jerk_fcf(fcf, 63) / rv * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk normalized by 63d return vol × close
def f36cfj_f36_cash_flow_jerk_ncfo_normretvol_252d_base_v073_signal(ncfo, closeadj):
    rv = _std(closeadj.pct_change(), 63).replace(0, np.nan)
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) / rv * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × revenue trend × close
def f36cfj_f36_cash_flow_jerk_fcf_xrevtrend_63d_base_v074_signal(fcf, revenue, closeadj):
    rt = _diff(revenue, 63) / revenue.abs().replace(0, np.nan)
    result = _f36_cashflow_jerk_fcf(fcf, 63) * rt * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite cashflow jerk: FCF + ncfo + FCF margin all × close
def f36cfj_f36_cash_flow_jerk_composite_252d_base_v075_signal(fcf, ncfo, revenue, closeadj):
    a = _f36_cashflow_jerk_fcf(fcf, 252) * 1e-6
    b = _f36_cashflow_jerk_ncfo(ncfo, 252) * 1e-6
    c = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252)
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36cfj_f36_cash_flow_jerk_fcf_21d_base_v001_signal,
    f36cfj_f36_cash_flow_jerk_fcf_63d_base_v002_signal,
    f36cfj_f36_cash_flow_jerk_fcf_126d_base_v003_signal,
    f36cfj_f36_cash_flow_jerk_fcf_252d_base_v004_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_21d_base_v005_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_63d_base_v006_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_126d_base_v007_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_252d_base_v008_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_21d_base_v009_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_63d_base_v010_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_126d_base_v011_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_252d_base_v012_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_21d_base_v013_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_63d_base_v014_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_126d_base_v015_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_252d_base_v016_signal,
    f36cfj_f36_cash_flow_jerk_fcf_abs_21d_base_v017_signal,
    f36cfj_f36_cash_flow_jerk_fcf_abs_63d_base_v018_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_abs_126d_base_v019_signal,
    f36cfj_f36_cash_flow_jerk_fcf_sq_21d_base_v020_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_sq_63d_base_v021_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_sq_252d_base_v022_signal,
    f36cfj_f36_cash_flow_jerk_fcf_mean_63d_base_v023_signal,
    f36cfj_f36_cash_flow_jerk_fcf_mean_252d_base_v024_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_mean_63d_base_v025_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_mean_252d_base_v026_signal,
    f36cfj_f36_cash_flow_jerk_fcf_std_63d_base_v027_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_std_252d_base_v028_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_std_252d_base_v029_signal,
    f36cfj_f36_cash_flow_jerk_fcf_z_252d_base_v030_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_z_252d_base_v031_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_z_252d_base_v032_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_z_252d_base_v033_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xrev_63d_base_v034_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xrev_252d_base_v035_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_xrev_252d_base_v036_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xebitda_63d_base_v037_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xebitda_252d_base_v038_signal,
    f36cfj_f36_cash_flow_jerk_fcf_diff_63m252_base_v039_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_diff_21m63_base_v040_signal,
    f36cfj_f36_cash_flow_jerk_fcfvsncfo_252d_base_v041_signal,
    f36cfj_f36_cash_flow_jerk_fcfmvsncfom_63d_base_v042_signal,
    f36cfj_f36_cash_flow_jerk_fcf_ema_21d_base_v043_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_ema_63d_base_v044_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_ema_252d_base_v045_signal,
    f36cfj_f36_cash_flow_jerk_fcf_negcount_252d_base_v046_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_poscount_252d_base_v047_signal,
    f36cfj_f36_cash_flow_jerk_fcf_extremecount_504d_base_v048_signal,
    f36cfj_f36_cash_flow_jerk_fcf_sum_252d_base_v049_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_sum_252d_base_v050_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_sum_252d_base_v051_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_sum_252d_base_v052_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xmom_21d_base_v053_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xmom_63d_base_v054_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_xmom_252d_base_v055_signal,
    f36cfj_f36_cash_flow_jerk_fcf_normrev_63d_base_v056_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_normrev_252d_base_v057_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xato_63d_base_v058_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xato_252d_base_v059_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xcr_63d_base_v060_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xcr_252d_base_v061_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xdebt_63d_base_v062_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xdebt_252d_base_v063_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xequity_63d_base_v064_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xequity_252d_base_v065_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xeps_63d_base_v066_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xeps_252d_base_v067_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xnetinc_63d_base_v068_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xnetinc_252d_base_v069_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xwc_63d_base_v070_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xwc_252d_base_v071_signal,
    f36cfj_f36_cash_flow_jerk_fcf_normretvol_63d_base_v072_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_normretvol_252d_base_v073_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xrevtrend_63d_base_v074_signal,
    f36cfj_f36_cash_flow_jerk_composite_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_CASH_FLOW_JERK_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e7 * np.exp(np.cumsum(np.random.normal(0.0008, 0.01, n))), name="revenue")
    netinc = pd.Series(1e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.012, n))) * np.sign(np.random.normal(0.5, 1.0, n)), name="netinc")
    ebitda = pd.Series(2e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.01, n))) * np.sign(np.random.normal(0.7, 1.0, n)), name="ebitda")
    fcf = pd.Series(8e5 * np.exp(np.cumsum(np.random.normal(0.0005, 0.013, n))) * np.sign(np.random.normal(0.6, 1.0, n)), name="fcf")
    ncfo = pd.Series(1.2e6 * np.exp(np.cumsum(np.random.normal(0.0006, 0.012, n))) * np.sign(np.random.normal(0.8, 1.0, n)), name="ncfo")
    eps = pd.Series(np.cumsum(np.random.normal(0.001, 0.05, n)) + 1.0, name="eps")
    assets = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0004, 0.006, n))), name="assets")
    debt = pd.Series(1e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.008, n))), name="debt")
    equity = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0005, 0.007, n))), name="equity")
    workingcapital = pd.Series(8e6 * np.exp(np.cumsum(np.random.normal(0.0004, 0.01, n))) * np.sign(np.random.normal(0.7, 1.0, n)), name="workingcapital")
    currentratio = pd.Series(1.5 + np.cumsum(np.random.normal(0.0, 0.01, n)) * 0.1, name="currentratio")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "netinc": netinc, "ebitda": ebitda,
        "fcf": fcf, "ncfo": ncfo, "eps": eps, "assets": assets, "debt": debt, "equity": equity,
        "workingcapital": workingcapital, "currentratio": currentratio,
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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f36_cash_flow_jerk_base_001_075_claude: {n_features} features pass")
