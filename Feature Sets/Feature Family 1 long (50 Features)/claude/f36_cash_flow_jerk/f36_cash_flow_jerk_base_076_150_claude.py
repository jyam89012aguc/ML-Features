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


# 5d short FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_5d_base_v076_signal(fcf, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 5) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 10d short FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_10d_base_v077_signal(fcf, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 10) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 42d FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_42d_base_v078_signal(fcf, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 42) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 189d FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_189d_base_v079_signal(fcf, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 189) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 378d FCF jerk × close
def f36cfj_f36_cash_flow_jerk_fcf_378d_base_v080_signal(fcf, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 378) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 5d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_5d_base_v081_signal(ncfo, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 5) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 10d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_10d_base_v082_signal(ncfo, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 10) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 42d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_42d_base_v083_signal(ncfo, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 42) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 189d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_189d_base_v084_signal(ncfo, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 189) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 378d ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_ncfo_378d_base_v085_signal(ncfo, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 378) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 5d FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_5d_base_v086_signal(fcf, revenue, closeadj):
    result = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_42d_base_v087_signal(fcf, revenue, closeadj):
    result = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_189d_base_v088_signal(fcf, revenue, closeadj):
    result = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 5d ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_5d_base_v089_signal(ncfo, revenue, closeadj):
    result = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 42d ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_42d_base_v090_signal(ncfo, revenue, closeadj):
    result = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 189d ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_189d_base_v091_signal(ncfo, revenue, closeadj):
    result = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × revenue growth × close
def f36cfj_f36_cash_flow_jerk_fcf_xgrowth_63d_base_v092_signal(fcf, revenue, closeadj):
    g = revenue.pct_change(63)
    result = _f36_cashflow_jerk_fcf(fcf, 63) * g * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk × revenue growth × close
def f36cfj_f36_cash_flow_jerk_ncfo_xgrowth_252d_base_v093_signal(ncfo, revenue, closeadj):
    g = revenue.pct_change(252)
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) * g * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF margin jerk × revenue growth × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_xgrowth_252d_base_v094_signal(fcf, revenue, closeadj):
    g = revenue.pct_change(252)
    result = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252) * g * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × dollar volume
def f36cfj_f36_cash_flow_jerk_fcf_xdv_63d_base_v095_signal(fcf, closeadj, volume):
    dv = closeadj * volume
    result = _f36_cashflow_jerk_fcf(fcf, 63) * dv * 1e-9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk × dollar volume
def f36cfj_f36_cash_flow_jerk_ncfo_xdv_252d_base_v096_signal(ncfo, closeadj, volume):
    dv = closeadj * volume
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) * dv * 1e-9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × volume zscore × close
def f36cfj_f36_cash_flow_jerk_fcf_xvolz_63d_base_v097_signal(fcf, closeadj, volume):
    result = _f36_cashflow_jerk_fcf(fcf, 63) * _z(volume, 63) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF jerk × short return × close
def f36cfj_f36_cash_flow_jerk_fcf_xshortret_21d_base_v098_signal(fcf, closeadj):
    r = closeadj.pct_change(5)
    result = _f36_cashflow_jerk_fcf(fcf, 21) * r * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo jerk × long return × close
def f36cfj_f36_cash_flow_jerk_ncfo_xlongret_63d_base_v099_signal(ncfo, closeadj):
    r = closeadj.pct_change(126)
    result = _f36_cashflow_jerk_ncfo(ncfo, 63) * r * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF jerk EMA × close
def f36cfj_f36_cash_flow_jerk_fcf_ema_252d_base_v100_signal(fcf, closeadj):
    j = _f36_cashflow_jerk_fcf(fcf, 252)
    result = j.ewm(span=252, adjust=False).mean() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ncfo jerk EMA × close
def f36cfj_f36_cash_flow_jerk_ncfo_ema_21d_base_v101_signal(ncfo, closeadj):
    j = _f36_cashflow_jerk_ncfo(ncfo, 21)
    result = j.ewm(span=21, adjust=False).mean() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF margin jerk EMA × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_ema_21d_base_v102_signal(fcf, revenue, closeadj):
    j = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 21)
    result = j.ewm(span=21, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo margin jerk EMA × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_ema_63d_base_v103_signal(ncfo, revenue, closeadj):
    j = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 63)
    result = j.ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_fcfxncfo_63d_base_v104_signal(fcf, ncfo, closeadj):
    a = _f36_cashflow_jerk_fcf(fcf, 63)
    b = _f36_cashflow_jerk_ncfo(ncfo, 63)
    result = a * b * closeadj * 1e-18
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF margin jerk × ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmxncfom_252d_base_v105_signal(fcf, ncfo, revenue, closeadj):
    a = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252)
    b = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 252)
    result = a * b * closeadj * 100.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk minus ncfo jerk × close
def f36cfj_f36_cash_flow_jerk_fcfminusncfo_63d_base_v106_signal(fcf, ncfo, closeadj):
    base = (_f36_cashflow_jerk_fcf(fcf, 63) - _f36_cashflow_jerk_ncfo(ncfo, 63)) * closeadj * 1e-6
    return base.replace([np.inf, -np.inf], np.nan)


# 252d ncfo margin jerk minus FCF margin jerk × close
def f36cfj_f36_cash_flow_jerk_ncfomminusfcfm_252d_base_v107_signal(fcf, ncfo, revenue, closeadj):
    base = (_f36_cashflow_jerk_ncfomargin(ncfo, revenue, 252) - _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252)) * closeadj
    return base.replace([np.inf, -np.inf], np.nan)


# 21d FCF jerk × interest expense × close
def f36cfj_f36_cash_flow_jerk_fcf_xintexp_21d_base_v108_signal(fcf, intexp, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 21) * intexp.abs() * closeadj * 1e-11
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk × tax expense × close
def f36cfj_f36_cash_flow_jerk_ncfo_xtaxexp_252d_base_v109_signal(ncfo, taxexp, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) * taxexp.abs() * closeadj * 1e-11
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × capex × close
def f36cfj_f36_cash_flow_jerk_fcf_xcapex_63d_base_v110_signal(fcf, capex, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 63) * capex.abs() * closeadj * 1e-11
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF margin jerk × capex × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_xcapex_252d_base_v111_signal(fcf, revenue, capex, closeadj):
    result = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252) * capex.abs() * closeadj * 1e-5
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × ATR × close
def f36cfj_f36_cash_flow_jerk_fcf_xrange_63d_base_v112_signal(fcf, closeadj, high, low):
    rng = (high - low).rolling(21, min_periods=5).mean()
    result = _f36_cashflow_jerk_fcf(fcf, 63) * rng * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk × ATR × close
def f36cfj_f36_cash_flow_jerk_ncfo_xrange_252d_base_v113_signal(ncfo, closeadj, high, low):
    rng = (high - low).rolling(63, min_periods=21).mean()
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) * rng * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × sqrt(rev) × close
def f36cfj_f36_cash_flow_jerk_fcf_xrevsq_63d_base_v114_signal(fcf, revenue, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 63) * (revenue.abs() ** 0.5) * closeadj * 1e-9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite mean of all cashflow jerks × close
def f36cfj_f36_cash_flow_jerk_meanof4_252d_base_v115_signal(fcf, ncfo, revenue, closeadj):
    a = _f36_cashflow_jerk_fcf(fcf, 252) * 1e-6
    b = _f36_cashflow_jerk_ncfo(ncfo, 252) * 1e-6
    c = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252)
    d = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 252)
    result = ((a + b + c + d) / 4.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d meanof4 × close
def f36cfj_f36_cash_flow_jerk_meanof4_63d_base_v116_signal(fcf, ncfo, revenue, closeadj):
    a = _f36_cashflow_jerk_fcf(fcf, 63) * 1e-6
    b = _f36_cashflow_jerk_ncfo(ncfo, 63) * 1e-6
    c = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 63)
    d = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 63)
    result = ((a + b + c + d) / 4.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d meanof4 × close
def f36cfj_f36_cash_flow_jerk_meanof4_21d_base_v117_signal(fcf, ncfo, revenue, closeadj):
    a = _f36_cashflow_jerk_fcf(fcf, 21) * 1e-6
    b = _f36_cashflow_jerk_ncfo(ncfo, 21) * 1e-6
    c = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 21)
    d = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 21)
    result = ((a + b + c + d) / 4.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk dispersion × close
def f36cfj_f36_cash_flow_jerk_fcf_dispersion_63d_base_v118_signal(fcf, closeadj):
    result = _std(_f36_cashflow_jerk_fcf(fcf, 21), 63) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk dispersion × close
def f36cfj_f36_cash_flow_jerk_ncfo_dispersion_252d_base_v119_signal(ncfo, closeadj):
    result = _std(_f36_cashflow_jerk_ncfo(ncfo, 63), 252) * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF margin jerk dispersion × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_dispersion_252d_base_v120_signal(fcf, revenue, closeadj):
    result = _std(_f36_cashflow_jerk_fcfmargin(fcf, revenue, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × sharesbas × close
def f36cfj_f36_cash_flow_jerk_fcf_xsharesbas_63d_base_v121_signal(fcf, sharesbas, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 63) * sharesbas * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk × sharesbas × close
def f36cfj_f36_cash_flow_jerk_ncfo_xsharesbas_252d_base_v122_signal(ncfo, sharesbas, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) * sharesbas * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF jerk × ncfi × close
def f36cfj_f36_cash_flow_jerk_fcf_xncfi_252d_base_v123_signal(fcf, ncfi, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 252) * ncfi.abs() * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × liabilities × close
def f36cfj_f36_cash_flow_jerk_fcf_xliab_63d_base_v124_signal(fcf, liabilities, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 63) * liabilities.abs() * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk × liabilities × close
def f36cfj_f36_cash_flow_jerk_ncfo_xliab_252d_base_v125_signal(ncfo, liabilities, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) * liabilities.abs() * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF jerk range × close
def f36cfj_f36_cash_flow_jerk_fcf_range_252d_base_v126_signal(fcf, closeadj):
    j = _f36_cashflow_jerk_fcf(fcf, 21)
    rng = j.rolling(252, min_periods=63).max() - j.rolling(252, min_periods=63).min()
    result = rng * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk range × close
def f36cfj_f36_cash_flow_jerk_ncfo_range_252d_base_v127_signal(ncfo, closeadj):
    j = _f36_cashflow_jerk_ncfo(ncfo, 21)
    rng = j.rolling(252, min_periods=63).max() - j.rolling(252, min_periods=63).min()
    result = rng * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF margin jerk range × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_range_504d_base_v128_signal(fcf, revenue, closeadj):
    j = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 63)
    rng = j.rolling(504, min_periods=126).max() - j.rolling(504, min_periods=126).min()
    result = rng * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk skew × close
def f36cfj_f36_cash_flow_jerk_fcf_skew_63d_base_v129_signal(fcf, closeadj):
    j = _f36_cashflow_jerk_fcf(fcf, 21)
    result = j.rolling(63, min_periods=21).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF jerk skew × close
def f36cfj_f36_cash_flow_jerk_fcf_skew_252d_base_v130_signal(fcf, closeadj):
    j = _f36_cashflow_jerk_fcf(fcf, 21)
    result = j.rolling(252, min_periods=63).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk kurtosis × close
def f36cfj_f36_cash_flow_jerk_ncfo_kurt_252d_base_v131_signal(ncfo, closeadj):
    j = _f36_cashflow_jerk_ncfo(ncfo, 21)
    result = j.rolling(252, min_periods=63).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × eps trend × close
def f36cfj_f36_cash_flow_jerk_fcf_xepstrend_63d_base_v132_signal(fcf, eps, closeadj):
    et = _diff(eps, 63)
    result = _f36_cashflow_jerk_fcf(fcf, 63) * et * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk × eps trend × close
def f36cfj_f36_cash_flow_jerk_ncfo_xepstrend_252d_base_v133_signal(ncfo, eps, closeadj):
    et = _diff(eps, 252)
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) * et * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × ebitda growth × close
def f36cfj_f36_cash_flow_jerk_fcf_xebitdagrowth_63d_base_v134_signal(fcf, ebitda, closeadj):
    g = ebitda.pct_change(63)
    result = _f36_cashflow_jerk_fcf(fcf, 63) * g * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk × netinc × close
def f36cfj_f36_cash_flow_jerk_ncfo_xnetinc_long_252d_base_v135_signal(ncfo, netinc, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) * netinc.abs() * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF margin jerk × ebitda × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_xebitda_63d_base_v136_signal(fcf, revenue, ebitda, closeadj):
    result = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 63) * ebitda.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo margin jerk × ncff × close
def f36cfj_f36_cash_flow_jerk_ncfomargin_xncff_252d_base_v137_signal(ncfo, revenue, ncff, closeadj):
    result = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 252) * ncff.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF margin jerk minus ncfo margin jerk × close
def f36cfj_f36_cash_flow_jerk_fcfmvsncfom_252d_base_v138_signal(fcf, ncfo, revenue, closeadj):
    a = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252)
    b = _f36_cashflow_jerk_ncfomargin(ncfo, revenue, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo jerk minus FCF jerk × close
def f36cfj_f36_cash_flow_jerk_ncfominusfcf_63d_base_v139_signal(ncfo, fcf, closeadj):
    base = (_f36_cashflow_jerk_ncfo(ncfo, 63) - _f36_cashflow_jerk_fcf(fcf, 63)) * closeadj * 1e-6
    return base.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk minus FCF jerk × close
def f36cfj_f36_cash_flow_jerk_ncfominusfcf_252d_base_v140_signal(ncfo, fcf, closeadj):
    base = (_f36_cashflow_jerk_ncfo(ncfo, 252) - _f36_cashflow_jerk_fcf(fcf, 252)) * closeadj * 1e-6
    return base.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × retained earnings × close
def f36cfj_f36_cash_flow_jerk_fcf_xretearn_63d_base_v141_signal(fcf, retearn, closeadj):
    result = _f36_cashflow_jerk_fcf(fcf, 63) * retearn.abs() * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk × retained earnings × close
def f36cfj_f36_cash_flow_jerk_ncfo_xretearn_252d_base_v142_signal(ncfo, retearn, closeadj):
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) * retearn.abs() * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF margin jerk × retained earnings × close
def f36cfj_f36_cash_flow_jerk_fcfmargin_xretearn_252d_base_v143_signal(fcf, revenue, retearn, closeadj):
    result = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252) * retearn.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × volume sum × close
def f36cfj_f36_cash_flow_jerk_fcf_xvolsum_63d_base_v144_signal(fcf, closeadj, volume):
    vs = volume.rolling(21, min_periods=5).sum()
    result = _f36_cashflow_jerk_fcf(fcf, 63) * vs * closeadj * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk × dollar-volume sum
def f36cfj_f36_cash_flow_jerk_ncfo_xdvsum_252d_base_v145_signal(ncfo, closeadj, volume):
    dvs = (closeadj * volume).rolling(63, min_periods=21).sum()
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) * dvs * 1e-12
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF jerk × close zscore × close
def f36cfj_f36_cash_flow_jerk_fcf_xclosez_21d_base_v146_signal(fcf, closeadj):
    cz = _z(closeadj, 252)
    result = _f36_cashflow_jerk_fcf(fcf, 21) * cz * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo jerk × close zscore × close
def f36cfj_f36_cash_flow_jerk_ncfo_xclosez_252d_base_v147_signal(ncfo, closeadj):
    cz = _z(closeadj, 504)
    result = _f36_cashflow_jerk_ncfo(ncfo, 252) * cz * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF jerk × log(1+rev) × close
def f36cfj_f36_cash_flow_jerk_fcf_xlogrev_63d_base_v148_signal(fcf, revenue, closeadj):
    lr = np.log(revenue.abs() + 1.0)
    result = _f36_cashflow_jerk_fcf(fcf, 63) * lr * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite severity: |fcfj|+|ncfoj|+|fcfmj| × close
def f36cfj_f36_cash_flow_jerk_severitysum_252d_base_v149_signal(fcf, ncfo, revenue, closeadj):
    a = _f36_cashflow_jerk_fcf(fcf, 252).abs() * 1e-6
    b = _f36_cashflow_jerk_ncfo(ncfo, 252).abs() * 1e-6
    c = _f36_cashflow_jerk_fcfmargin(fcf, revenue, 252).abs()
    result = (a + b + c) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d severity × revenue × close
def f36cfj_f36_cash_flow_jerk_severityxrev_63d_base_v150_signal(fcf, ncfo, revenue, closeadj):
    a = _f36_cashflow_jerk_fcf(fcf, 63).abs() * 1e-6
    b = _f36_cashflow_jerk_ncfo(ncfo, 63).abs() * 1e-6
    result = (a + b) * revenue.abs() * closeadj * 1e-6
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36cfj_f36_cash_flow_jerk_fcf_5d_base_v076_signal,
    f36cfj_f36_cash_flow_jerk_fcf_10d_base_v077_signal,
    f36cfj_f36_cash_flow_jerk_fcf_42d_base_v078_signal,
    f36cfj_f36_cash_flow_jerk_fcf_189d_base_v079_signal,
    f36cfj_f36_cash_flow_jerk_fcf_378d_base_v080_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_5d_base_v081_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_10d_base_v082_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_42d_base_v083_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_189d_base_v084_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_378d_base_v085_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_5d_base_v086_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_42d_base_v087_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_189d_base_v088_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_5d_base_v089_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_42d_base_v090_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_189d_base_v091_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xgrowth_63d_base_v092_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xgrowth_252d_base_v093_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_xgrowth_252d_base_v094_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xdv_63d_base_v095_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xdv_252d_base_v096_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xvolz_63d_base_v097_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xshortret_21d_base_v098_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xlongret_63d_base_v099_signal,
    f36cfj_f36_cash_flow_jerk_fcf_ema_252d_base_v100_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_ema_21d_base_v101_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_ema_21d_base_v102_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_ema_63d_base_v103_signal,
    f36cfj_f36_cash_flow_jerk_fcfxncfo_63d_base_v104_signal,
    f36cfj_f36_cash_flow_jerk_fcfmxncfom_252d_base_v105_signal,
    f36cfj_f36_cash_flow_jerk_fcfminusncfo_63d_base_v106_signal,
    f36cfj_f36_cash_flow_jerk_ncfomminusfcfm_252d_base_v107_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xintexp_21d_base_v108_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xtaxexp_252d_base_v109_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xcapex_63d_base_v110_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_xcapex_252d_base_v111_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xrange_63d_base_v112_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xrange_252d_base_v113_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xrevsq_63d_base_v114_signal,
    f36cfj_f36_cash_flow_jerk_meanof4_252d_base_v115_signal,
    f36cfj_f36_cash_flow_jerk_meanof4_63d_base_v116_signal,
    f36cfj_f36_cash_flow_jerk_meanof4_21d_base_v117_signal,
    f36cfj_f36_cash_flow_jerk_fcf_dispersion_63d_base_v118_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_dispersion_252d_base_v119_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_dispersion_252d_base_v120_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xsharesbas_63d_base_v121_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xsharesbas_252d_base_v122_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xncfi_252d_base_v123_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xliab_63d_base_v124_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xliab_252d_base_v125_signal,
    f36cfj_f36_cash_flow_jerk_fcf_range_252d_base_v126_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_range_252d_base_v127_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_range_504d_base_v128_signal,
    f36cfj_f36_cash_flow_jerk_fcf_skew_63d_base_v129_signal,
    f36cfj_f36_cash_flow_jerk_fcf_skew_252d_base_v130_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_kurt_252d_base_v131_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xepstrend_63d_base_v132_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xepstrend_252d_base_v133_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xebitdagrowth_63d_base_v134_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xnetinc_long_252d_base_v135_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_xebitda_63d_base_v136_signal,
    f36cfj_f36_cash_flow_jerk_ncfomargin_xncff_252d_base_v137_signal,
    f36cfj_f36_cash_flow_jerk_fcfmvsncfom_252d_base_v138_signal,
    f36cfj_f36_cash_flow_jerk_ncfominusfcf_63d_base_v139_signal,
    f36cfj_f36_cash_flow_jerk_ncfominusfcf_252d_base_v140_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xretearn_63d_base_v141_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xretearn_252d_base_v142_signal,
    f36cfj_f36_cash_flow_jerk_fcfmargin_xretearn_252d_base_v143_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xvolsum_63d_base_v144_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xdvsum_252d_base_v145_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xclosez_21d_base_v146_signal,
    f36cfj_f36_cash_flow_jerk_ncfo_xclosez_252d_base_v147_signal,
    f36cfj_f36_cash_flow_jerk_fcf_xlogrev_63d_base_v148_signal,
    f36cfj_f36_cash_flow_jerk_severitysum_252d_base_v149_signal,
    f36cfj_f36_cash_flow_jerk_severityxrev_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_CASH_FLOW_JERK_REGISTRY_076_150 = REGISTRY


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
    ncff = pd.Series(6e5 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))) * np.sign(np.random.normal(0.3, 1.0, n)), name="ncff")
    capex = pd.Series(9e5 * np.exp(np.cumsum(np.random.normal(0.0004, 0.011, n))), name="capex")
    intexp = pd.Series(2e5 * np.exp(np.cumsum(np.random.normal(0.0003, 0.008, n))), name="intexp")
    taxexp = pd.Series(3e5 * np.exp(np.cumsum(np.random.normal(0.0004, 0.009, n))), name="taxexp")
    sharesbas = pd.Series(1e7 + np.cumsum(np.random.normal(1e3, 5e3, n)), name="sharesbas")
    liabilities = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.007, n))), name="liabilities")
    retearn = pd.Series(1e7 * np.exp(np.cumsum(np.random.normal(0.0004, 0.009, n))) * np.sign(np.random.normal(0.7, 1.0, n)), name="retearn")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "netinc": netinc, "ebitda": ebitda, "eps": eps,
        "fcf": fcf, "ncfo": ncfo, "ncfi": ncfi, "ncff": ncff, "capex": capex,
        "intexp": intexp, "taxexp": taxexp, "sharesbas": sharesbas, "liabilities": liabilities,
        "retearn": retearn,
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
    print(f"OK f36_cash_flow_jerk_base_076_150_claude: {n_features} features pass")
