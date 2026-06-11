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


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan).rolling(w, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f31_cashflow_accel_fcf(fcf, w):
    g = _diff(fcf, w) / fcf.shift(w).abs().replace(0, np.nan)
    return _diff(g, w)


def _f31_cashflow_accel_ncfo(ncfo, w):
    g = _diff(ncfo, w) / ncfo.shift(w).abs().replace(0, np.nan)
    return _diff(g, w)


def _f31_cashflow_accel_growth(s, w):
    g = _diff(s, w) / s.shift(w).abs().replace(0, np.nan)
    return _diff(g, w)


# 5d slope of 21d FCF acceleration × close
def f31cfa_f31_cash_flow_acceleration_fcfaccel_21d_slope_v001_signal(fcf, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d FCF acceleration × close
def f31cfa_f31_cash_flow_acceleration_fcfaccel_21d_slope_v002_signal(fcf, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d FCF acceleration × close
def f31cfa_f31_cash_flow_acceleration_fcfaccel_63d_slope_v003_signal(fcf, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF acceleration × close
def f31cfa_f31_cash_flow_acceleration_fcfaccel_63d_slope_v004_signal(fcf, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d FCF acceleration × close
def f31cfa_f31_cash_flow_acceleration_fcfaccel_63d_slope_v005_signal(fcf, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d FCF acceleration × close
def f31cfa_f31_cash_flow_acceleration_fcfaccel_126d_slope_v006_signal(fcf, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d FCF acceleration × close
def f31cfa_f31_cash_flow_acceleration_fcfaccel_126d_slope_v007_signal(fcf, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d FCF acceleration × close
def f31cfa_f31_cash_flow_acceleration_fcfaccel_252d_slope_v008_signal(fcf, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF acceleration × close
def f31cfa_f31_cash_flow_acceleration_fcfaccel_252d_slope_v009_signal(fcf, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d NCFO acceleration × close
def f31cfa_f31_cash_flow_acceleration_ncfoaccel_21d_slope_v010_signal(ncfo, closeadj):
    base = _f31_cashflow_accel_ncfo(ncfo, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d NCFO acceleration × close
def f31cfa_f31_cash_flow_acceleration_ncfoaccel_21d_slope_v011_signal(ncfo, closeadj):
    base = _f31_cashflow_accel_ncfo(ncfo, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d NCFO acceleration × close
def f31cfa_f31_cash_flow_acceleration_ncfoaccel_63d_slope_v012_signal(ncfo, closeadj):
    base = _f31_cashflow_accel_ncfo(ncfo, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d NCFO acceleration × close
def f31cfa_f31_cash_flow_acceleration_ncfoaccel_63d_slope_v013_signal(ncfo, closeadj):
    base = _f31_cashflow_accel_ncfo(ncfo, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d NCFO acceleration × close
def f31cfa_f31_cash_flow_acceleration_ncfoaccel_126d_slope_v014_signal(ncfo, closeadj):
    base = _f31_cashflow_accel_ncfo(ncfo, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d NCFO acceleration × close
def f31cfa_f31_cash_flow_acceleration_ncfoaccel_252d_slope_v015_signal(ncfo, closeadj):
    base = _f31_cashflow_accel_ncfo(ncfo, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d opinc acceleration × close
def f31cfa_f31_cash_flow_acceleration_opincaccel_21d_slope_v016_signal(opinc, closeadj):
    base = _f31_cashflow_accel_growth(opinc, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d opinc acceleration × close
def f31cfa_f31_cash_flow_acceleration_opincaccel_63d_slope_v017_signal(opinc, closeadj):
    base = _f31_cashflow_accel_growth(opinc, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d opinc acceleration × close
def f31cfa_f31_cash_flow_acceleration_opincaccel_252d_slope_v018_signal(opinc, closeadj):
    base = _f31_cashflow_accel_growth(opinc, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d EBITDA acceleration × close
def f31cfa_f31_cash_flow_acceleration_ebitdaaccel_21d_slope_v019_signal(ebitda, closeadj):
    base = _f31_cashflow_accel_growth(ebitda, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d EBITDA acceleration × close
def f31cfa_f31_cash_flow_acceleration_ebitdaaccel_63d_slope_v020_signal(ebitda, closeadj):
    base = _f31_cashflow_accel_growth(ebitda, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d EBITDA acceleration × close
def f31cfa_f31_cash_flow_acceleration_ebitdaaccel_252d_slope_v021_signal(ebitda, closeadj):
    base = _f31_cashflow_accel_growth(ebitda, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d netinc acceleration × close
def f31cfa_f31_cash_flow_acceleration_netincaccel_21d_slope_v022_signal(netinc, closeadj):
    base = _f31_cashflow_accel_growth(netinc, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d netinc acceleration × close
def f31cfa_f31_cash_flow_acceleration_netincaccel_63d_slope_v023_signal(netinc, closeadj):
    base = _f31_cashflow_accel_growth(netinc, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d netinc acceleration × close
def f31cfa_f31_cash_flow_acceleration_netincaccel_252d_slope_v024_signal(netinc, closeadj):
    base = _f31_cashflow_accel_growth(netinc, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF accel mean
def f31cfa_f31_cash_flow_acceleration_fcfaccelmean_63d_slope_v025_signal(fcf, closeadj):
    base = _mean(_f31_cashflow_accel_fcf(fcf, 63), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF accel mean
def f31cfa_f31_cash_flow_acceleration_fcfaccelmean_126d_slope_v026_signal(fcf, closeadj):
    base = _mean(_f31_cashflow_accel_fcf(fcf, 252), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d NCFO accel mean
def f31cfa_f31_cash_flow_acceleration_ncfoaccelmean_63d_slope_v027_signal(ncfo, closeadj):
    base = _mean(_f31_cashflow_accel_ncfo(ncfo, 63), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d NCFO accel mean
def f31cfa_f31_cash_flow_acceleration_ncfoaccelmean_126d_slope_v028_signal(ncfo, closeadj):
    base = _mean(_f31_cashflow_accel_ncfo(ncfo, 252), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF accel std
def f31cfa_f31_cash_flow_acceleration_fcfaccelstd_63d_slope_v029_signal(fcf, closeadj):
    base = _std(_f31_cashflow_accel_fcf(fcf, 63), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF accel std
def f31cfa_f31_cash_flow_acceleration_fcfaccelstd_252d_slope_v030_signal(fcf, closeadj):
    base = _std(_f31_cashflow_accel_fcf(fcf, 252), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d NCFO accel std
def f31cfa_f31_cash_flow_acceleration_ncfoaccelstd_63d_slope_v031_signal(ncfo, closeadj):
    base = _std(_f31_cashflow_accel_ncfo(ncfo, 63), 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d NCFO accel std
def f31cfa_f31_cash_flow_acceleration_ncfoaccelstd_252d_slope_v032_signal(ncfo, closeadj):
    base = _std(_f31_cashflow_accel_ncfo(ncfo, 252), 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d FCF accel zscore
def f31cfa_f31_cash_flow_acceleration_fcfaccelz_252d_slope_v033_signal(fcf, closeadj):
    base = _z(_f31_cashflow_accel_fcf(fcf, 63), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d NCFO accel zscore
def f31cfa_f31_cash_flow_acceleration_ncfoaccelz_252d_slope_v034_signal(ncfo, closeadj):
    base = _z(_f31_cashflow_accel_ncfo(ncfo, 63), 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d FCF accel zscore
def f31cfa_f31_cash_flow_acceleration_fcfaccelz_504d_slope_v035_signal(fcf, closeadj):
    base = _z(_f31_cashflow_accel_fcf(fcf, 252), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d NCFO accel zscore
def f31cfa_f31_cash_flow_acceleration_ncfoaccelz_504d_slope_v036_signal(ncfo, closeadj):
    base = _z(_f31_cashflow_accel_ncfo(ncfo, 252), 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF per-share accel
def f31cfa_f31_cash_flow_acceleration_fcfaccelps_21d_slope_v037_signal(fcf, sharesbas, closeadj):
    fcfps = fcf / sharesbas.replace(0, np.nan)
    base = _f31_cashflow_accel_growth(fcfps, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF per-share accel
def f31cfa_f31_cash_flow_acceleration_fcfaccelps_63d_slope_v038_signal(fcf, sharesbas, closeadj):
    fcfps = fcf / sharesbas.replace(0, np.nan)
    base = _f31_cashflow_accel_growth(fcfps, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF per-share accel
def f31cfa_f31_cash_flow_acceleration_fcfaccelps_252d_slope_v039_signal(fcf, sharesbas, closeadj):
    fcfps = fcf / sharesbas.replace(0, np.nan)
    base = _f31_cashflow_accel_growth(fcfps, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d NCFO per-share accel
def f31cfa_f31_cash_flow_acceleration_ncfoaccelps_63d_slope_v040_signal(ncfo, sharesbas, closeadj):
    nps = ncfo / sharesbas.replace(0, np.nan)
    base = _f31_cashflow_accel_growth(nps, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d NCFO per-share accel
def f31cfa_f31_cash_flow_acceleration_ncfoaccelps_252d_slope_v041_signal(ncfo, sharesbas, closeadj):
    nps = ncfo / sharesbas.replace(0, np.nan)
    base = _f31_cashflow_accel_growth(nps, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF margin accel
def f31cfa_f31_cash_flow_acceleration_fcfmarginaccel_63d_slope_v042_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _f31_cashflow_accel_growth(m, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF margin accel
def f31cfa_f31_cash_flow_acceleration_fcfmarginaccel_252d_slope_v043_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    base = _f31_cashflow_accel_growth(m, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d NCFO margin accel
def f31cfa_f31_cash_flow_acceleration_ncfomarginaccel_63d_slope_v044_signal(ncfo, revenue, closeadj):
    m = ncfo / revenue.replace(0, np.nan)
    base = _f31_cashflow_accel_growth(m, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d NCFO margin accel
def f31cfa_f31_cash_flow_acceleration_ncfomarginaccel_252d_slope_v045_signal(ncfo, revenue, closeadj):
    m = ncfo / revenue.replace(0, np.nan)
    base = _f31_cashflow_accel_growth(m, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF/asset accel
def f31cfa_f31_cash_flow_acceleration_fcftoassetaccel_63d_slope_v046_signal(fcf, assets, closeadj):
    m = fcf / assets.replace(0, np.nan)
    base = _f31_cashflow_accel_growth(m, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF/asset accel
def f31cfa_f31_cash_flow_acceleration_fcftoassetaccel_252d_slope_v047_signal(fcf, assets, closeadj):
    m = fcf / assets.replace(0, np.nan)
    base = _f31_cashflow_accel_growth(m, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF/equity accel
def f31cfa_f31_cash_flow_acceleration_fcftoequityaccel_63d_slope_v048_signal(fcf, equity, closeadj):
    m = fcf / equity.replace(0, np.nan)
    base = _f31_cashflow_accel_growth(m, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF/equity accel
def f31cfa_f31_cash_flow_acceleration_fcftoequityaccel_252d_slope_v049_signal(fcf, equity, closeadj):
    m = fcf / equity.replace(0, np.nan)
    base = _f31_cashflow_accel_growth(m, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d NCFO/asset accel
def f31cfa_f31_cash_flow_acceleration_ncfotoassetaccel_63d_slope_v050_signal(ncfo, assets, closeadj):
    m = ncfo / assets.replace(0, np.nan)
    base = _f31_cashflow_accel_growth(m, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d NCFO/asset accel
def f31cfa_f31_cash_flow_acceleration_ncfotoassetaccel_252d_slope_v051_signal(ncfo, assets, closeadj):
    m = ncfo / assets.replace(0, np.nan)
    base = _f31_cashflow_accel_growth(m, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF accel × margin
def f31cfa_f31_cash_flow_acceleration_fcfaccelxmargin_63d_slope_v052_signal(fcf, revenue, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    m = fcf / revenue.replace(0, np.nan)
    base = a * m * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF accel × margin
def f31cfa_f31_cash_flow_acceleration_fcfaccelxmargin_252d_slope_v053_signal(fcf, revenue, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 252)
    m = fcf / revenue.replace(0, np.nan)
    base = a * m * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d NCFO accel × margin
def f31cfa_f31_cash_flow_acceleration_ncfoaccelxmargin_63d_slope_v054_signal(ncfo, revenue, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 63)
    m = ncfo / revenue.replace(0, np.nan)
    base = a * m * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d NCFO accel × margin
def f31cfa_f31_cash_flow_acceleration_ncfoaccelxmargin_252d_slope_v055_signal(ncfo, revenue, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 252)
    m = ncfo / revenue.replace(0, np.nan)
    base = a * m * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF accel × revenue
def f31cfa_f31_cash_flow_acceleration_fcfaccelxrev_63d_slope_v056_signal(fcf, revenue, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    base = a * revenue.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF accel × revenue
def f31cfa_f31_cash_flow_acceleration_fcfaccelxrev_252d_slope_v057_signal(fcf, revenue, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 252)
    base = a * revenue.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF-capex acceleration
def f31cfa_f31_cash_flow_acceleration_fcfmcapxaccel_21d_slope_v058_signal(fcf, capex, closeadj):
    s = fcf - capex
    base = _f31_cashflow_accel_growth(s, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF-capex acceleration
def f31cfa_f31_cash_flow_acceleration_fcfmcapxaccel_63d_slope_v059_signal(fcf, capex, closeadj):
    s = fcf - capex
    base = _f31_cashflow_accel_growth(s, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF-capex acceleration
def f31cfa_f31_cash_flow_acceleration_fcfmcapxaccel_252d_slope_v060_signal(fcf, capex, closeadj):
    s = fcf - capex
    base = _f31_cashflow_accel_growth(s, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF accel pos count
def f31cfa_f31_cash_flow_acceleration_fcfaccelposcnt_63d_slope_v061_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 21)
    base = (a).rolling(63, min_periods=21).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF accel pos count
def f31cfa_f31_cash_flow_acceleration_fcfaccelposcnt_252d_slope_v062_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 21)
    base = (a).rolling(252, min_periods=63).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d NCFO accel pos count
def f31cfa_f31_cash_flow_acceleration_ncfoaccelposcnt_252d_slope_v063_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 21)
    base = (a).rolling(252, min_periods=63).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d NCFO accel pos count
def f31cfa_f31_cash_flow_acceleration_ncfoaccelposcnt_63d_slope_v064_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 21)
    base = (a).rolling(63, min_periods=21).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF accel ratio (63v252)
def f31cfa_f31_cash_flow_acceleration_fcfaccelratio_63v252_slope_v065_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    b = _f31_cashflow_accel_fcf(fcf, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of FCF accel diff 21m63
def f31cfa_f31_cash_flow_acceleration_fcfacceldiff_21m63_slope_v066_signal(fcf, closeadj):
    base = (_f31_cashflow_accel_fcf(fcf, 21) - _f31_cashflow_accel_fcf(fcf, 63)) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF accel diff 63m252
def f31cfa_f31_cash_flow_acceleration_fcfacceldiff_63m252_slope_v067_signal(fcf, closeadj):
    base = (_f31_cashflow_accel_fcf(fcf, 63) - _f31_cashflow_accel_fcf(fcf, 252)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of NCFO accel diff 21m63
def f31cfa_f31_cash_flow_acceleration_ncfoacceldiff_21m63_slope_v068_signal(ncfo, closeadj):
    base = (_f31_cashflow_accel_ncfo(ncfo, 21) - _f31_cashflow_accel_ncfo(ncfo, 63)) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of NCFO accel diff 63m252
def f31cfa_f31_cash_flow_acceleration_ncfoacceldiff_63m252_slope_v069_signal(ncfo, closeadj):
    base = (_f31_cashflow_accel_ncfo(ncfo, 63) - _f31_cashflow_accel_ncfo(ncfo, 252)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF accel × ebitda
def f31cfa_f31_cash_flow_acceleration_fcfaccelxebitda_21d_slope_v070_signal(fcf, ebitda, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 21) * ebitda.abs() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF accel × ebitda
def f31cfa_f31_cash_flow_acceleration_fcfaccelxebitda_252d_slope_v071_signal(fcf, ebitda, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 252) * ebitda.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF accel × wc 63d
def f31cfa_f31_cash_flow_acceleration_fcfaccelxwc_63d_slope_v072_signal(fcf, workingcapital, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    wc = _diff(workingcapital, 63)
    base = a * wc * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF accel × wc 252d
def f31cfa_f31_cash_flow_acceleration_fcfaccelxwc_252d_slope_v073_signal(fcf, workingcapital, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 252)
    wc = _diff(workingcapital, 252)
    base = a * wc * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d gp accel
def f31cfa_f31_cash_flow_acceleration_gpaccel_21d_slope_v074_signal(gp, closeadj):
    base = _f31_cashflow_accel_growth(gp, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gp accel
def f31cfa_f31_cash_flow_acceleration_gpaccel_63d_slope_v075_signal(gp, closeadj):
    base = _f31_cashflow_accel_growth(gp, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gp accel
def f31cfa_f31_cash_flow_acceleration_gpaccel_252d_slope_v076_signal(gp, closeadj):
    base = _f31_cashflow_accel_growth(gp, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ebitda+ncfo composite accel
def f31cfa_f31_cash_flow_acceleration_ebitdancfocompose_21d_slope_v077_signal(ebitda, ncfo, closeadj):
    s = ebitda + ncfo
    base = _f31_cashflow_accel_growth(s, 21) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ebitda+ncfo composite accel
def f31cfa_f31_cash_flow_acceleration_ebitdancfocompose_252d_slope_v078_signal(ebitda, ncfo, closeadj):
    s = ebitda + ncfo
    base = _f31_cashflow_accel_growth(s, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF accel × eps
def f31cfa_f31_cash_flow_acceleration_fcfaccelxeps_63d_slope_v079_signal(fcf, eps, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 63) * eps.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF accel × eps 252d
def f31cfa_f31_cash_flow_acceleration_fcfaccelxeps_252d_slope_v080_signal(fcf, eps, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 252) * eps.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF accel × level 63d
def f31cfa_f31_cash_flow_acceleration_fcfaccelxlevel_63d_slope_v081_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    base = a * fcf.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of NCFO accel × level 252d
def f31cfa_f31_cash_flow_acceleration_ncfoaccelxlevel_252d_slope_v082_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 252)
    base = a * ncfo.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d FCF accel × debt
def f31cfa_f31_cash_flow_acceleration_fcfaccelxdebt_21d_slope_v083_signal(fcf, debt, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 21) * debt.abs() * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF accel × debt
def f31cfa_f31_cash_flow_acceleration_fcfaccelxdebt_252d_slope_v084_signal(fcf, debt, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 252) * debt.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF accel × current ratio 63d
def f31cfa_f31_cash_flow_acceleration_fcfaccelxcurratio_63d_slope_v085_signal(fcf, currentratio, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 63) * currentratio * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF accel × current ratio 252d
def f31cfa_f31_cash_flow_acceleration_fcfaccelxcurratio_252d_slope_v086_signal(fcf, currentratio, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 252) * currentratio * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF share intensity 63d
def f31cfa_f31_cash_flow_acceleration_fcfshareintensity_63d_slope_v087_signal(fcf, sharesbas, closeadj):
    s = fcf / sharesbas.replace(0, np.nan)
    a = _f31_cashflow_accel_growth(s, 63)
    base = a * sharesbas * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF share intensity 252d
def f31cfa_f31_cash_flow_acceleration_fcfshareintensity_252d_slope_v088_signal(fcf, sharesbas, closeadj):
    s = fcf / sharesbas.replace(0, np.nan)
    a = _f31_cashflow_accel_growth(s, 252)
    base = a * sharesbas * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF accel EMA63
def f31cfa_f31_cash_flow_acceleration_fcfaccelema_63d_slope_v089_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 21)
    base = a.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF accel EMA252
def f31cfa_f31_cash_flow_acceleration_fcfaccelema_252d_slope_v090_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    base = a.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of NCFO accel EMA63
def f31cfa_f31_cash_flow_acceleration_ncfoaccelema_63d_slope_v091_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 21)
    base = a.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of NCFO accel EMA252
def f31cfa_f31_cash_flow_acceleration_ncfoaccelema_252d_slope_v092_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 63)
    base = a.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF accel squared 63d
def f31cfa_f31_cash_flow_acceleration_fcfaccelsq_63d_slope_v093_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    base = a * a.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF accel squared 252d
def f31cfa_f31_cash_flow_acceleration_fcfaccelsq_252d_slope_v094_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 252)
    base = a * a.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of NCFO accel squared 63d
def f31cfa_f31_cash_flow_acceleration_ncfoaccelsq_63d_slope_v095_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 63)
    base = a * a.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of NCFO accel squared 252d
def f31cfa_f31_cash_flow_acceleration_ncfoaccelsq_252d_slope_v096_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 252)
    base = a * a.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF accel area
def f31cfa_f31_cash_flow_acceleration_fcfaccelarea_63d_slope_v097_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 21)
    base = a.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF accel area
def f31cfa_f31_cash_flow_acceleration_fcfaccelarea_252d_slope_v098_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 21)
    base = a.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d NCFO accel area
def f31cfa_f31_cash_flow_acceleration_ncfoaccelarea_63d_slope_v099_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 21)
    base = a.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d NCFO accel area
def f31cfa_f31_cash_flow_acceleration_ncfoaccelarea_252d_slope_v100_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 21)
    base = a.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d cashflow composite accel
def f31cfa_f31_cash_flow_acceleration_cashaccelcomp_63d_slope_v101_signal(fcf, ncfo, closeadj):
    s = fcf + ncfo
    base = _f31_cashflow_accel_growth(s, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d cashflow composite accel
def f31cfa_f31_cash_flow_acceleration_cashaccelcomp_252d_slope_v102_signal(fcf, ncfo, closeadj):
    s = fcf + ncfo
    base = _f31_cashflow_accel_growth(s, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF-NCFO accel divergence 63d
def f31cfa_f31_cash_flow_acceleration_fcfminusncfo_63d_slope_v103_signal(fcf, ncfo, closeadj):
    base = (_f31_cashflow_accel_fcf(fcf, 63) - _f31_cashflow_accel_ncfo(ncfo, 63)) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF-NCFO accel divergence 252d
def f31cfa_f31_cash_flow_acceleration_fcfminusncfo_252d_slope_v104_signal(fcf, ncfo, closeadj):
    base = (_f31_cashflow_accel_fcf(fcf, 252) - _f31_cashflow_accel_ncfo(ncfo, 252)) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF accel × revenue growth 63d
def f31cfa_f31_cash_flow_acceleration_fcfaccelxrevg_63d_slope_v105_signal(fcf, revenue, closeadj):
    rg = _diff(revenue, 63) / revenue.shift(63).abs().replace(0, np.nan)
    base = _f31_cashflow_accel_fcf(fcf, 63) * rg * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF accel × revenue growth 252d
def f31cfa_f31_cash_flow_acceleration_fcfaccelxrevg_252d_slope_v106_signal(fcf, revenue, closeadj):
    rg = _diff(revenue, 252) / revenue.shift(252).abs().replace(0, np.nan)
    base = _f31_cashflow_accel_fcf(fcf, 252) * rg * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of NCFO accel × revenue growth 63d
def f31cfa_f31_cash_flow_acceleration_ncfoaccelxrevg_63d_slope_v107_signal(ncfo, revenue, closeadj):
    rg = _diff(revenue, 63) / revenue.shift(63).abs().replace(0, np.nan)
    base = _f31_cashflow_accel_ncfo(ncfo, 63) * rg * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of NCFO accel × revenue growth 252d
def f31cfa_f31_cash_flow_acceleration_ncfoaccelxrevg_252d_slope_v108_signal(ncfo, revenue, closeadj):
    rg = _diff(revenue, 252) / revenue.shift(252).abs().replace(0, np.nan)
    base = _f31_cashflow_accel_ncfo(ncfo, 252) * rg * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of FCF accel × eps growth 21d
def f31cfa_f31_cash_flow_acceleration_fcfaccelxepsg_21d_slope_v109_signal(fcf, eps, closeadj):
    eg = _diff(eps, 21) / eps.shift(21).abs().replace(0, np.nan)
    base = _f31_cashflow_accel_fcf(fcf, 21) * eg * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF accel × eps growth 252d
def f31cfa_f31_cash_flow_acceleration_fcfaccelxepsg_252d_slope_v110_signal(fcf, eps, closeadj):
    eg = _diff(eps, 252) / eps.shift(252).abs().replace(0, np.nan)
    base = _f31_cashflow_accel_fcf(fcf, 252) * eg * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of (NCFO-capex)/revenue accel 63d
def f31cfa_f31_cash_flow_acceleration_ncfoxcapxratio_63d_slope_v111_signal(ncfo, capex, revenue, closeadj):
    s = (ncfo - capex) / revenue.replace(0, np.nan)
    base = _f31_cashflow_accel_growth(s, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of (NCFO-capex)/revenue accel 252d
def f31cfa_f31_cash_flow_acceleration_ncfoxcapxratio_252d_slope_v112_signal(ncfo, capex, revenue, closeadj):
    s = (ncfo - capex) / revenue.replace(0, np.nan)
    base = _f31_cashflow_accel_growth(s, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF accel × quality 63d
def f31cfa_f31_cash_flow_acceleration_fcfaccelxqual_63d_slope_v113_signal(fcf, ebitda, closeadj):
    q = fcf / ebitda.replace(0, np.nan)
    base = _f31_cashflow_accel_fcf(fcf, 63) * q * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF accel × quality 252d
def f31cfa_f31_cash_flow_acceleration_fcfaccelxqual_252d_slope_v114_signal(fcf, ebitda, closeadj):
    q = fcf / ebitda.replace(0, np.nan)
    base = _f31_cashflow_accel_fcf(fcf, 252) * q * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF/NCFO accel ratio 63d
def f31cfa_f31_cash_flow_acceleration_fcfvsncfoaccel_63d_slope_v115_signal(fcf, ncfo, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    b = _f31_cashflow_accel_ncfo(ncfo, 63).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF/NCFO accel ratio 252d
def f31cfa_f31_cash_flow_acceleration_fcfvsncfoaccel_252d_slope_v116_signal(fcf, ncfo, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 252)
    b = _f31_cashflow_accel_ncfo(ncfo, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF accel rolling 252d mean
def f31cfa_f31_cash_flow_acceleration_fcfaccelxavg_252d_slope_v117_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    base = _mean(a, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of NCFO accel rolling 252d mean
def f31cfa_f31_cash_flow_acceleration_ncfoaccelxavg_252d_slope_v118_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 63)
    base = _mean(a, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF/equity accel × equity 63d
def f31cfa_f31_cash_flow_acceleration_fcftoeqxlevel_63d_slope_v119_signal(fcf, equity, closeadj):
    s = fcf / equity.replace(0, np.nan)
    base = _f31_cashflow_accel_growth(s, 63) * equity.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF/equity accel × equity 252d
def f31cfa_f31_cash_flow_acceleration_fcftoeqxlevel_252d_slope_v120_signal(fcf, equity, closeadj):
    s = fcf / equity.replace(0, np.nan)
    base = _f31_cashflow_accel_growth(s, 252) * equity.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF accel sign sum 63d
def f31cfa_f31_cash_flow_acceleration_fcfaccelsignsum_63d_slope_v121_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 21)
    sg = np.sign(a)
    base = sg.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF accel sign sum 252d
def f31cfa_f31_cash_flow_acceleration_fcfaccelsignsum_252d_slope_v122_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 21)
    sg = np.sign(a)
    base = sg.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of NCFO accel sign sum 63d
def f31cfa_f31_cash_flow_acceleration_ncfoaccelsignsum_63d_slope_v123_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 21)
    sg = np.sign(a)
    base = sg.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of NCFO accel sign sum 252d
def f31cfa_f31_cash_flow_acceleration_ncfoaccelsignsum_252d_slope_v124_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 21)
    sg = np.sign(a)
    base = sg.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF accel × tax 63d
def f31cfa_f31_cash_flow_acceleration_fcfaccelxtax_63d_slope_v125_signal(fcf, taxexp, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 63) * taxexp.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF accel × tax 252d
def f31cfa_f31_cash_flow_acceleration_fcfaccelxtax_252d_slope_v126_signal(fcf, taxexp, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 252) * taxexp.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF accel × intexp 63d
def f31cfa_f31_cash_flow_acceleration_fcfaccelxint_63d_slope_v127_signal(fcf, intexp, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 63) * intexp.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF accel × intexp 252d
def f31cfa_f31_cash_flow_acceleration_fcfaccelxint_252d_slope_v128_signal(fcf, intexp, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 252) * intexp.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF accel × retearn 63d
def f31cfa_f31_cash_flow_acceleration_fcfaccelxretearn_63d_slope_v129_signal(fcf, retearn, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 63) * retearn.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF accel × retearn 252d
def f31cfa_f31_cash_flow_acceleration_fcfaccelxretearn_252d_slope_v130_signal(fcf, retearn, closeadj):
    base = _f31_cashflow_accel_fcf(fcf, 252) * retearn.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of NCFO accel × liabilities 63d
def f31cfa_f31_cash_flow_acceleration_ncfoaccelxliab_63d_slope_v131_signal(ncfo, liabilities, closeadj):
    base = _f31_cashflow_accel_ncfo(ncfo, 63) * liabilities.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of NCFO accel × liabilities 252d
def f31cfa_f31_cash_flow_acceleration_ncfoaccelxliab_252d_slope_v132_signal(ncfo, liabilities, closeadj):
    base = _f31_cashflow_accel_ncfo(ncfo, 252) * liabilities.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF/sharesbas accel zscore 252d
def f31cfa_f31_cash_flow_acceleration_fcfpsaccelz_252d_slope_v133_signal(fcf, sharesbas, closeadj):
    s = fcf / sharesbas.replace(0, np.nan)
    a = _f31_cashflow_accel_growth(s, 63)
    base = _z(a, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF/sharesbas accel zscore 504d
def f31cfa_f31_cash_flow_acceleration_fcfpsaccelz_504d_slope_v134_signal(fcf, sharesbas, closeadj):
    s = fcf / sharesbas.replace(0, np.nan)
    a = _f31_cashflow_accel_growth(s, 252)
    base = _z(a, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of multi-window FCF accel composite
def f31cfa_f31_cash_flow_acceleration_fcfaccelmulti_slope_v135_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 21)
    b = _f31_cashflow_accel_fcf(fcf, 63)
    c = _f31_cashflow_accel_fcf(fcf, 252)
    base = (a + b + c) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of multi-window NCFO accel composite
def f31cfa_f31_cash_flow_acceleration_ncfoaccelmulti_slope_v136_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 21)
    b = _f31_cashflow_accel_ncfo(ncfo, 63)
    c = _f31_cashflow_accel_ncfo(ncfo, 252)
    base = (a + b + c) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF accel health 63d
def f31cfa_f31_cash_flow_acceleration_fcfaccelhealth_63d_slope_v137_signal(fcf, currentratio, revenue, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    base = a * currentratio * revenue.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF accel health 252d
def f31cfa_f31_cash_flow_acceleration_fcfaccelhealth_252d_slope_v138_signal(fcf, currentratio, revenue, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 252)
    base = a * currentratio * revenue.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF accel × netinc growth 63d
def f31cfa_f31_cash_flow_acceleration_fcfaccelxnetincg_63d_slope_v139_signal(fcf, netinc, closeadj):
    ng = _diff(netinc, 63) / netinc.shift(63).abs().replace(0, np.nan)
    base = _f31_cashflow_accel_fcf(fcf, 63) * ng * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF accel × netinc growth 252d
def f31cfa_f31_cash_flow_acceleration_fcfaccelxnetincg_252d_slope_v140_signal(fcf, netinc, closeadj):
    ng = _diff(netinc, 252) / netinc.shift(252).abs().replace(0, np.nan)
    base = _f31_cashflow_accel_fcf(fcf, 252) * ng * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of FCF accel anomaly 63d
def f31cfa_f31_cash_flow_acceleration_fcfaccelanomaly_63d_slope_v141_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    bm = a.expanding(min_periods=63).mean()
    base = (a - bm) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of FCF accel anomaly 252d
def f31cfa_f31_cash_flow_acceleration_fcfaccelanomaly_252d_slope_v142_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 252)
    bm = a.expanding(min_periods=126).mean()
    base = (a - bm) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of EBITDA accel × FCF 63d
def f31cfa_f31_cash_flow_acceleration_ebitdaaccelxfcf_63d_slope_v143_signal(ebitda, fcf, closeadj):
    a = _f31_cashflow_accel_growth(ebitda, 63)
    base = a * fcf.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of EBITDA accel × FCF 252d
def f31cfa_f31_cash_flow_acceleration_ebitdaaccelxfcf_252d_slope_v144_signal(ebitda, fcf, closeadj):
    a = _f31_cashflow_accel_growth(ebitda, 252)
    base = a * fcf.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of NCFO/sharesbas × level 63d
def f31cfa_f31_cash_flow_acceleration_ncfopsxlevel_63d_slope_v145_signal(ncfo, sharesbas, closeadj):
    s = ncfo / sharesbas.replace(0, np.nan)
    a = _f31_cashflow_accel_growth(s, 63)
    base = a * sharesbas * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of NCFO/sharesbas × level 252d
def f31cfa_f31_cash_flow_acceleration_ncfopsxlevel_252d_slope_v146_signal(ncfo, sharesbas, closeadj):
    s = ncfo / sharesbas.replace(0, np.nan)
    a = _f31_cashflow_accel_growth(s, 252)
    base = a * sharesbas * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of joint cashflow accel 63d
def f31cfa_f31_cash_flow_acceleration_jointcashaccel_63d_slope_v147_signal(fcf, ebitda, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    b = _f31_cashflow_accel_growth(ebitda, 63)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of joint cashflow accel 252d
def f31cfa_f31_cash_flow_acceleration_jointcashaccel_252d_slope_v148_signal(fcf, ebitda, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 252)
    b = _f31_cashflow_accel_growth(ebitda, 252)
    base = a * b * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of NCFO accel × FCF/NCFO quality 63d
def f31cfa_f31_cash_flow_acceleration_ncfoaccelxquality_63d_slope_v149_signal(ncfo, fcf, closeadj):
    q = fcf / ncfo.replace(0, np.nan)
    a = _f31_cashflow_accel_ncfo(ncfo, 63)
    base = a * q * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of composite cashflow severity 252d
def f31cfa_f31_cash_flow_acceleration_compositesev_252d_slope_v150_signal(fcf, ncfo, ebitda, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    b = _f31_cashflow_accel_ncfo(ncfo, 63)
    c = _f31_cashflow_accel_growth(ebitda, 63)
    s = (a + b + c).rolling(252, min_periods=63).sum()
    base = s * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31cfa_f31_cash_flow_acceleration_fcfaccel_21d_slope_v001_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccel_21d_slope_v002_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccel_63d_slope_v003_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccel_63d_slope_v004_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccel_63d_slope_v005_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccel_126d_slope_v006_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccel_126d_slope_v007_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccel_252d_slope_v008_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccel_252d_slope_v009_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccel_21d_slope_v010_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccel_21d_slope_v011_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccel_63d_slope_v012_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccel_63d_slope_v013_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccel_126d_slope_v014_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccel_252d_slope_v015_signal,
    f31cfa_f31_cash_flow_acceleration_opincaccel_21d_slope_v016_signal,
    f31cfa_f31_cash_flow_acceleration_opincaccel_63d_slope_v017_signal,
    f31cfa_f31_cash_flow_acceleration_opincaccel_252d_slope_v018_signal,
    f31cfa_f31_cash_flow_acceleration_ebitdaaccel_21d_slope_v019_signal,
    f31cfa_f31_cash_flow_acceleration_ebitdaaccel_63d_slope_v020_signal,
    f31cfa_f31_cash_flow_acceleration_ebitdaaccel_252d_slope_v021_signal,
    f31cfa_f31_cash_flow_acceleration_netincaccel_21d_slope_v022_signal,
    f31cfa_f31_cash_flow_acceleration_netincaccel_63d_slope_v023_signal,
    f31cfa_f31_cash_flow_acceleration_netincaccel_252d_slope_v024_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelmean_63d_slope_v025_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelmean_126d_slope_v026_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelmean_63d_slope_v027_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelmean_126d_slope_v028_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelstd_63d_slope_v029_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelstd_252d_slope_v030_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelstd_63d_slope_v031_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelstd_252d_slope_v032_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelz_252d_slope_v033_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelz_252d_slope_v034_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelz_504d_slope_v035_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelz_504d_slope_v036_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelps_21d_slope_v037_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelps_63d_slope_v038_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelps_252d_slope_v039_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelps_63d_slope_v040_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelps_252d_slope_v041_signal,
    f31cfa_f31_cash_flow_acceleration_fcfmarginaccel_63d_slope_v042_signal,
    f31cfa_f31_cash_flow_acceleration_fcfmarginaccel_252d_slope_v043_signal,
    f31cfa_f31_cash_flow_acceleration_ncfomarginaccel_63d_slope_v044_signal,
    f31cfa_f31_cash_flow_acceleration_ncfomarginaccel_252d_slope_v045_signal,
    f31cfa_f31_cash_flow_acceleration_fcftoassetaccel_63d_slope_v046_signal,
    f31cfa_f31_cash_flow_acceleration_fcftoassetaccel_252d_slope_v047_signal,
    f31cfa_f31_cash_flow_acceleration_fcftoequityaccel_63d_slope_v048_signal,
    f31cfa_f31_cash_flow_acceleration_fcftoequityaccel_252d_slope_v049_signal,
    f31cfa_f31_cash_flow_acceleration_ncfotoassetaccel_63d_slope_v050_signal,
    f31cfa_f31_cash_flow_acceleration_ncfotoassetaccel_252d_slope_v051_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxmargin_63d_slope_v052_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxmargin_252d_slope_v053_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelxmargin_63d_slope_v054_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelxmargin_252d_slope_v055_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxrev_63d_slope_v056_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxrev_252d_slope_v057_signal,
    f31cfa_f31_cash_flow_acceleration_fcfmcapxaccel_21d_slope_v058_signal,
    f31cfa_f31_cash_flow_acceleration_fcfmcapxaccel_63d_slope_v059_signal,
    f31cfa_f31_cash_flow_acceleration_fcfmcapxaccel_252d_slope_v060_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelposcnt_63d_slope_v061_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelposcnt_252d_slope_v062_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelposcnt_252d_slope_v063_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelposcnt_63d_slope_v064_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelratio_63v252_slope_v065_signal,
    f31cfa_f31_cash_flow_acceleration_fcfacceldiff_21m63_slope_v066_signal,
    f31cfa_f31_cash_flow_acceleration_fcfacceldiff_63m252_slope_v067_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoacceldiff_21m63_slope_v068_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoacceldiff_63m252_slope_v069_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxebitda_21d_slope_v070_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxebitda_252d_slope_v071_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxwc_63d_slope_v072_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxwc_252d_slope_v073_signal,
    f31cfa_f31_cash_flow_acceleration_gpaccel_21d_slope_v074_signal,
    f31cfa_f31_cash_flow_acceleration_gpaccel_63d_slope_v075_signal,
    f31cfa_f31_cash_flow_acceleration_gpaccel_252d_slope_v076_signal,
    f31cfa_f31_cash_flow_acceleration_ebitdancfocompose_21d_slope_v077_signal,
    f31cfa_f31_cash_flow_acceleration_ebitdancfocompose_252d_slope_v078_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxeps_63d_slope_v079_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxeps_252d_slope_v080_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxlevel_63d_slope_v081_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelxlevel_252d_slope_v082_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxdebt_21d_slope_v083_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxdebt_252d_slope_v084_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxcurratio_63d_slope_v085_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxcurratio_252d_slope_v086_signal,
    f31cfa_f31_cash_flow_acceleration_fcfshareintensity_63d_slope_v087_signal,
    f31cfa_f31_cash_flow_acceleration_fcfshareintensity_252d_slope_v088_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelema_63d_slope_v089_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelema_252d_slope_v090_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelema_63d_slope_v091_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelema_252d_slope_v092_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelsq_63d_slope_v093_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelsq_252d_slope_v094_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelsq_63d_slope_v095_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelsq_252d_slope_v096_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelarea_63d_slope_v097_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelarea_252d_slope_v098_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelarea_63d_slope_v099_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelarea_252d_slope_v100_signal,
    f31cfa_f31_cash_flow_acceleration_cashaccelcomp_63d_slope_v101_signal,
    f31cfa_f31_cash_flow_acceleration_cashaccelcomp_252d_slope_v102_signal,
    f31cfa_f31_cash_flow_acceleration_fcfminusncfo_63d_slope_v103_signal,
    f31cfa_f31_cash_flow_acceleration_fcfminusncfo_252d_slope_v104_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxrevg_63d_slope_v105_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxrevg_252d_slope_v106_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelxrevg_63d_slope_v107_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelxrevg_252d_slope_v108_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxepsg_21d_slope_v109_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxepsg_252d_slope_v110_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoxcapxratio_63d_slope_v111_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoxcapxratio_252d_slope_v112_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxqual_63d_slope_v113_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxqual_252d_slope_v114_signal,
    f31cfa_f31_cash_flow_acceleration_fcfvsncfoaccel_63d_slope_v115_signal,
    f31cfa_f31_cash_flow_acceleration_fcfvsncfoaccel_252d_slope_v116_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxavg_252d_slope_v117_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelxavg_252d_slope_v118_signal,
    f31cfa_f31_cash_flow_acceleration_fcftoeqxlevel_63d_slope_v119_signal,
    f31cfa_f31_cash_flow_acceleration_fcftoeqxlevel_252d_slope_v120_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelsignsum_63d_slope_v121_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelsignsum_252d_slope_v122_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelsignsum_63d_slope_v123_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelsignsum_252d_slope_v124_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxtax_63d_slope_v125_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxtax_252d_slope_v126_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxint_63d_slope_v127_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxint_252d_slope_v128_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxretearn_63d_slope_v129_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxretearn_252d_slope_v130_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelxliab_63d_slope_v131_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelxliab_252d_slope_v132_signal,
    f31cfa_f31_cash_flow_acceleration_fcfpsaccelz_252d_slope_v133_signal,
    f31cfa_f31_cash_flow_acceleration_fcfpsaccelz_504d_slope_v134_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelmulti_slope_v135_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelmulti_slope_v136_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelhealth_63d_slope_v137_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelhealth_252d_slope_v138_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxnetincg_63d_slope_v139_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxnetincg_252d_slope_v140_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelanomaly_63d_slope_v141_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelanomaly_252d_slope_v142_signal,
    f31cfa_f31_cash_flow_acceleration_ebitdaaccelxfcf_63d_slope_v143_signal,
    f31cfa_f31_cash_flow_acceleration_ebitdaaccelxfcf_252d_slope_v144_signal,
    f31cfa_f31_cash_flow_acceleration_ncfopsxlevel_63d_slope_v145_signal,
    f31cfa_f31_cash_flow_acceleration_ncfopsxlevel_252d_slope_v146_signal,
    f31cfa_f31_cash_flow_acceleration_jointcashaccel_63d_slope_v147_signal,
    f31cfa_f31_cash_flow_acceleration_jointcashaccel_252d_slope_v148_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelxquality_63d_slope_v149_signal,
    f31cfa_f31_cash_flow_acceleration_compositesev_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_CASH_FLOW_ACCELERATION_REGISTRY_SLOPE = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    fund_walk = lambda mu, sd, base: pd.Series(base * np.exp(np.cumsum(np.random.normal(mu, sd, n))))
    revenue = fund_walk(0.0006, 0.015, 1e8).rename("revenue")
    netinc = fund_walk(0.0005, 0.02, 1e7).rename("netinc")
    fcf = fund_walk(0.0005, 0.025, 8e6).rename("fcf")
    equity = fund_walk(0.0004, 0.012, 5e8).rename("equity")
    debt = fund_walk(0.0004, 0.015, 3e8).rename("debt")
    assets = fund_walk(0.0004, 0.012, 1.2e9).rename("assets")
    ebitda = fund_walk(0.0005, 0.018, 2e7).rename("ebitda")
    capex = fund_walk(0.0004, 0.022, 5e6).rename("capex")
    eps = fund_walk(0.0005, 0.02, 2.0).rename("eps")
    sharesbas = fund_walk(0.0001, 0.005, 1e7).rename("sharesbas")
    ncfo = fund_walk(0.0005, 0.022, 1.5e7).rename("ncfo")
    opinc = fund_walk(0.0005, 0.02, 2.5e7).rename("opinc")
    gp = fund_walk(0.0005, 0.018, 4e7).rename("gp")
    workingcapital = fund_walk(0.0004, 0.02, 3e7).rename("workingcapital")
    currentratio = fund_walk(0.0001, 0.01, 1.5).rename("currentratio")
    intexp = fund_walk(0.0003, 0.018, 5e6).rename("intexp")
    retearn = fund_walk(0.0005, 0.02, 1e8).rename("retearn")
    liabilities = fund_walk(0.0004, 0.012, 7e8).rename("liabilities")
    taxexp = fund_walk(0.0004, 0.022, 4e6).rename("taxexp")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf,
        "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda,
        "capex": capex, "eps": eps, "sharesbas": sharesbas, "ncfo": ncfo,
        "opinc": opinc, "gp": gp, "workingcapital": workingcapital,
        "currentratio": currentratio, "intexp": intexp, "retearn": retearn,
        "liabilities": liabilities, "taxexp": taxexp,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f31_cashflow_accel_fcf", "_f31_cashflow_accel_ncfo", "_f31_cashflow_accel_growth")
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
    print(f"OK f31_cash_flow_acceleration_2nd_derivatives_001_150_claude: {n_features} features pass")
