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
def _f31_cashflow_accel_fcf(fcf, w):
    g = _diff(fcf, w) / fcf.shift(w).abs().replace(0, np.nan)
    return _diff(g, w)


def _f31_cashflow_accel_ncfo(ncfo, w):
    g = _diff(ncfo, w) / ncfo.shift(w).abs().replace(0, np.nan)
    return _diff(g, w)


def _f31_cashflow_accel_growth(s, w):
    g = _diff(s, w) / s.shift(w).abs().replace(0, np.nan)
    return _diff(g, w)


# 21d acceleration of FCF growth weighted by closeadj
def f31cfa_f31_cash_flow_acceleration_fcfaccel_21d_base_v001_signal(fcf, closeadj):
    result = _f31_cashflow_accel_fcf(fcf, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of FCF growth
def f31cfa_f31_cash_flow_acceleration_fcfaccel_63d_base_v002_signal(fcf, closeadj):
    result = _f31_cashflow_accel_fcf(fcf, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d acceleration of FCF growth
def f31cfa_f31_cash_flow_acceleration_fcfaccel_126d_base_v003_signal(fcf, closeadj):
    result = _f31_cashflow_accel_fcf(fcf, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of FCF growth
def f31cfa_f31_cash_flow_acceleration_fcfaccel_252d_base_v004_signal(fcf, closeadj):
    result = _f31_cashflow_accel_fcf(fcf, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d acceleration of NCFO growth weighted by closeadj
def f31cfa_f31_cash_flow_acceleration_ncfoaccel_21d_base_v005_signal(ncfo, closeadj):
    result = _f31_cashflow_accel_ncfo(ncfo, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of NCFO growth
def f31cfa_f31_cash_flow_acceleration_ncfoaccel_63d_base_v006_signal(ncfo, closeadj):
    result = _f31_cashflow_accel_ncfo(ncfo, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d acceleration of NCFO growth
def f31cfa_f31_cash_flow_acceleration_ncfoaccel_126d_base_v007_signal(ncfo, closeadj):
    result = _f31_cashflow_accel_ncfo(ncfo, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of NCFO growth
def f31cfa_f31_cash_flow_acceleration_ncfoaccel_252d_base_v008_signal(ncfo, closeadj):
    result = _f31_cashflow_accel_ncfo(ncfo, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cashflow acceleration of opinc
def f31cfa_f31_cash_flow_acceleration_opincaccel_21d_base_v009_signal(opinc, closeadj):
    result = _f31_cashflow_accel_growth(opinc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashflow acceleration of opinc
def f31cfa_f31_cash_flow_acceleration_opincaccel_63d_base_v010_signal(opinc, closeadj):
    result = _f31_cashflow_accel_growth(opinc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashflow acceleration of opinc
def f31cfa_f31_cash_flow_acceleration_opincaccel_252d_base_v011_signal(opinc, closeadj):
    result = _f31_cashflow_accel_growth(opinc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cashflow acceleration of EBITDA
def f31cfa_f31_cash_flow_acceleration_ebitdaaccel_21d_base_v012_signal(ebitda, closeadj):
    result = _f31_cashflow_accel_growth(ebitda, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashflow acceleration of EBITDA
def f31cfa_f31_cash_flow_acceleration_ebitdaaccel_63d_base_v013_signal(ebitda, closeadj):
    result = _f31_cashflow_accel_growth(ebitda, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashflow acceleration of EBITDA
def f31cfa_f31_cash_flow_acceleration_ebitdaaccel_252d_base_v014_signal(ebitda, closeadj):
    result = _f31_cashflow_accel_growth(ebitda, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cashflow acceleration of netinc
def f31cfa_f31_cash_flow_acceleration_netincaccel_21d_base_v015_signal(netinc, closeadj):
    result = _f31_cashflow_accel_growth(netinc, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashflow acceleration of netinc
def f31cfa_f31_cash_flow_acceleration_netincaccel_63d_base_v016_signal(netinc, closeadj):
    result = _f31_cashflow_accel_growth(netinc, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashflow acceleration of netinc
def f31cfa_f31_cash_flow_acceleration_netincaccel_252d_base_v017_signal(netinc, closeadj):
    result = _f31_cashflow_accel_growth(netinc, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel rolling mean over 63d
def f31cfa_f31_cash_flow_acceleration_fcfaccelmean_63d_base_v018_signal(fcf, closeadj):
    result = _mean(_f31_cashflow_accel_fcf(fcf, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel rolling mean over 126d
def f31cfa_f31_cash_flow_acceleration_fcfaccelmean_126d_base_v019_signal(fcf, closeadj):
    result = _mean(_f31_cashflow_accel_fcf(fcf, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d NCFO accel rolling mean over 63d
def f31cfa_f31_cash_flow_acceleration_ncfoaccelmean_63d_base_v020_signal(ncfo, closeadj):
    result = _mean(_f31_cashflow_accel_ncfo(ncfo, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d NCFO accel rolling mean over 126d
def f31cfa_f31_cash_flow_acceleration_ncfoaccelmean_126d_base_v021_signal(ncfo, closeadj):
    result = _mean(_f31_cashflow_accel_ncfo(ncfo, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel rolling std
def f31cfa_f31_cash_flow_acceleration_fcfaccelstd_63d_base_v022_signal(fcf, closeadj):
    result = _std(_f31_cashflow_accel_fcf(fcf, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel rolling std
def f31cfa_f31_cash_flow_acceleration_fcfaccelstd_252d_base_v023_signal(fcf, closeadj):
    result = _std(_f31_cashflow_accel_fcf(fcf, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d NCFO accel rolling std
def f31cfa_f31_cash_flow_acceleration_ncfoaccelstd_63d_base_v024_signal(ncfo, closeadj):
    result = _std(_f31_cashflow_accel_ncfo(ncfo, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d NCFO accel rolling std
def f31cfa_f31_cash_flow_acceleration_ncfoaccelstd_252d_base_v025_signal(ncfo, closeadj):
    result = _std(_f31_cashflow_accel_ncfo(ncfo, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel zscore over 252d
def f31cfa_f31_cash_flow_acceleration_fcfaccelz_252d_base_v026_signal(fcf, closeadj):
    result = _z(_f31_cashflow_accel_fcf(fcf, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d NCFO accel zscore over 252d
def f31cfa_f31_cash_flow_acceleration_ncfoaccelz_252d_base_v027_signal(ncfo, closeadj):
    result = _z(_f31_cashflow_accel_ncfo(ncfo, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d FCF accel zscore over 504d
def f31cfa_f31_cash_flow_acceleration_fcfaccelz_504d_base_v028_signal(fcf, closeadj):
    result = _z(_f31_cashflow_accel_fcf(fcf, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d NCFO accel zscore over 504d
def f31cfa_f31_cash_flow_acceleration_ncfoaccelz_504d_base_v029_signal(ncfo, closeadj):
    result = _z(_f31_cashflow_accel_ncfo(ncfo, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF accel scaled by sharesbas (per-share cashflow accel)
def f31cfa_f31_cash_flow_acceleration_fcfaccelps_21d_base_v030_signal(fcf, sharesbas, closeadj):
    fcfps = fcf / sharesbas.replace(0, np.nan)
    result = _f31_cashflow_accel_growth(fcfps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel per-share
def f31cfa_f31_cash_flow_acceleration_fcfaccelps_63d_base_v031_signal(fcf, sharesbas, closeadj):
    fcfps = fcf / sharesbas.replace(0, np.nan)
    result = _f31_cashflow_accel_growth(fcfps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel per-share
def f31cfa_f31_cash_flow_acceleration_fcfaccelps_252d_base_v032_signal(fcf, sharesbas, closeadj):
    fcfps = fcf / sharesbas.replace(0, np.nan)
    result = _f31_cashflow_accel_growth(fcfps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cashflow accel of NCFO per-share
def f31cfa_f31_cash_flow_acceleration_ncfoaccelps_63d_base_v033_signal(ncfo, sharesbas, closeadj):
    nps = ncfo / sharesbas.replace(0, np.nan)
    result = _f31_cashflow_accel_growth(nps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cashflow accel of NCFO per-share
def f31cfa_f31_cash_flow_acceleration_ncfoaccelps_252d_base_v034_signal(ncfo, sharesbas, closeadj):
    nps = ncfo / sharesbas.replace(0, np.nan)
    result = _f31_cashflow_accel_growth(nps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF margin acceleration (FCF/revenue)
def f31cfa_f31_cash_flow_acceleration_fcfmarginaccel_63d_base_v035_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    result = _f31_cashflow_accel_growth(m, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF margin acceleration
def f31cfa_f31_cash_flow_acceleration_fcfmarginaccel_252d_base_v036_signal(fcf, revenue, closeadj):
    m = fcf / revenue.replace(0, np.nan)
    result = _f31_cashflow_accel_growth(m, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d NCFO margin acceleration (NCFO/revenue)
def f31cfa_f31_cash_flow_acceleration_ncfomarginaccel_63d_base_v037_signal(ncfo, revenue, closeadj):
    m = ncfo / revenue.replace(0, np.nan)
    result = _f31_cashflow_accel_growth(m, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d NCFO margin acceleration
def f31cfa_f31_cash_flow_acceleration_ncfomarginaccel_252d_base_v038_signal(ncfo, revenue, closeadj):
    m = ncfo / revenue.replace(0, np.nan)
    result = _f31_cashflow_accel_growth(m, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of FCF/assets
def f31cfa_f31_cash_flow_acceleration_fcftoassetaccel_63d_base_v039_signal(fcf, assets, closeadj):
    m = fcf / assets.replace(0, np.nan)
    result = _f31_cashflow_accel_growth(m, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of FCF/assets
def f31cfa_f31_cash_flow_acceleration_fcftoassetaccel_252d_base_v040_signal(fcf, assets, closeadj):
    m = fcf / assets.replace(0, np.nan)
    result = _f31_cashflow_accel_growth(m, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of FCF/equity
def f31cfa_f31_cash_flow_acceleration_fcftoequityaccel_63d_base_v041_signal(fcf, equity, closeadj):
    m = fcf / equity.replace(0, np.nan)
    result = _f31_cashflow_accel_growth(m, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of FCF/equity
def f31cfa_f31_cash_flow_acceleration_fcftoequityaccel_252d_base_v042_signal(fcf, equity, closeadj):
    m = fcf / equity.replace(0, np.nan)
    result = _f31_cashflow_accel_growth(m, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of NCFO/assets
def f31cfa_f31_cash_flow_acceleration_ncfotoassetaccel_63d_base_v043_signal(ncfo, assets, closeadj):
    m = ncfo / assets.replace(0, np.nan)
    result = _f31_cashflow_accel_growth(m, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of NCFO/assets
def f31cfa_f31_cash_flow_acceleration_ncfotoassetaccel_252d_base_v044_signal(ncfo, assets, closeadj):
    m = ncfo / assets.replace(0, np.nan)
    result = _f31_cashflow_accel_growth(m, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel × current FCF margin
def f31cfa_f31_cash_flow_acceleration_fcfaccelxmargin_63d_base_v045_signal(fcf, revenue, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    m = fcf / revenue.replace(0, np.nan)
    result = a * m * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel × current FCF margin
def f31cfa_f31_cash_flow_acceleration_fcfaccelxmargin_252d_base_v046_signal(fcf, revenue, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 252)
    m = fcf / revenue.replace(0, np.nan)
    result = a * m * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d NCFO accel × current NCFO margin
def f31cfa_f31_cash_flow_acceleration_ncfoaccelxmargin_63d_base_v047_signal(ncfo, revenue, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 63)
    m = ncfo / revenue.replace(0, np.nan)
    result = a * m * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d NCFO accel × current NCFO margin
def f31cfa_f31_cash_flow_acceleration_ncfoaccelxmargin_252d_base_v048_signal(ncfo, revenue, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 252)
    m = ncfo / revenue.replace(0, np.nan)
    result = a * m * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel × revenue (pressure)
def f31cfa_f31_cash_flow_acceleration_fcfaccelxrev_63d_base_v049_signal(fcf, revenue, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    result = a * revenue.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel × revenue
def f31cfa_f31_cash_flow_acceleration_fcfaccelxrev_252d_base_v050_signal(fcf, revenue, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 252)
    result = a * revenue.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF minus capex acceleration (free cash post-capex shift)
def f31cfa_f31_cash_flow_acceleration_fcfmcapxaccel_21d_base_v051_signal(fcf, capex, closeadj):
    s = fcf - capex
    result = _f31_cashflow_accel_growth(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF minus capex acceleration
def f31cfa_f31_cash_flow_acceleration_fcfmcapxaccel_63d_base_v052_signal(fcf, capex, closeadj):
    s = fcf - capex
    result = _f31_cashflow_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF minus capex acceleration
def f31cfa_f31_cash_flow_acceleration_fcfmcapxaccel_252d_base_v053_signal(fcf, capex, closeadj):
    s = fcf - capex
    result = _f31_cashflow_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of days FCF accel > 0
def f31cfa_f31_cash_flow_acceleration_fcfaccelposcnt_63d_base_v054_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 21)
    result = (a).rolling(63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days FCF accel > 0
def f31cfa_f31_cash_flow_acceleration_fcfaccelposcnt_252d_base_v055_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 21)
    result = (a).rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days NCFO accel > 0
def f31cfa_f31_cash_flow_acceleration_ncfoaccelposcnt_252d_base_v056_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 21)
    result = (a).rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of days NCFO accel > 0
def f31cfa_f31_cash_flow_acceleration_ncfoaccelposcnt_63d_base_v057_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 21)
    result = (a).rolling(63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel ratio (63d / 252d)
def f31cfa_f31_cash_flow_acceleration_fcfaccelratio_63v252_base_v058_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    b = _f31_cashflow_accel_fcf(fcf, 252).replace(0, np.nan)
    result = a / b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF accel - 63d FCF accel (recent burst)
def f31cfa_f31_cash_flow_acceleration_fcfacceldiff_21m63_base_v059_signal(fcf, closeadj):
    result = (_f31_cashflow_accel_fcf(fcf, 21) - _f31_cashflow_accel_fcf(fcf, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel - 252d FCF accel
def f31cfa_f31_cash_flow_acceleration_fcfacceldiff_63m252_base_v060_signal(fcf, closeadj):
    result = (_f31_cashflow_accel_fcf(fcf, 63) - _f31_cashflow_accel_fcf(fcf, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d NCFO accel - 63d NCFO accel
def f31cfa_f31_cash_flow_acceleration_ncfoacceldiff_21m63_base_v061_signal(ncfo, closeadj):
    result = (_f31_cashflow_accel_ncfo(ncfo, 21) - _f31_cashflow_accel_ncfo(ncfo, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d NCFO accel - 252d NCFO accel
def f31cfa_f31_cash_flow_acceleration_ncfoacceldiff_63m252_base_v062_signal(ncfo, closeadj):
    result = (_f31_cashflow_accel_ncfo(ncfo, 63) - _f31_cashflow_accel_ncfo(ncfo, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d FCF accel × EBITDA
def f31cfa_f31_cash_flow_acceleration_fcfaccelxebitda_21d_base_v063_signal(fcf, ebitda, closeadj):
    result = _f31_cashflow_accel_fcf(fcf, 21) * ebitda.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel × EBITDA
def f31cfa_f31_cash_flow_acceleration_fcfaccelxebitda_252d_base_v064_signal(fcf, ebitda, closeadj):
    result = _f31_cashflow_accel_fcf(fcf, 252) * ebitda.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel × workingcapital change
def f31cfa_f31_cash_flow_acceleration_fcfaccelxwc_63d_base_v065_signal(fcf, workingcapital, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    wc = _diff(workingcapital, 63)
    result = a * wc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel × workingcapital change
def f31cfa_f31_cash_flow_acceleration_fcfaccelxwc_252d_base_v066_signal(fcf, workingcapital, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 252)
    wc = _diff(workingcapital, 252)
    result = a * wc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d gp acceleration scaled by closeadj
def f31cfa_f31_cash_flow_acceleration_gpaccel_21d_base_v067_signal(gp, closeadj):
    result = _f31_cashflow_accel_growth(gp, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gp acceleration scaled by closeadj
def f31cfa_f31_cash_flow_acceleration_gpaccel_63d_base_v068_signal(gp, closeadj):
    result = _f31_cashflow_accel_growth(gp, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gp acceleration
def f31cfa_f31_cash_flow_acceleration_gpaccel_252d_base_v069_signal(gp, closeadj):
    result = _f31_cashflow_accel_growth(gp, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ebitda + ncfo acceleration composite
def f31cfa_f31_cash_flow_acceleration_ebitdancfocompose_21d_base_v070_signal(ebitda, ncfo, closeadj):
    s = ebitda + ncfo
    result = _f31_cashflow_accel_growth(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ebitda + ncfo acceleration composite
def f31cfa_f31_cash_flow_acceleration_ebitdancfocompose_252d_base_v071_signal(ebitda, ncfo, closeadj):
    s = ebitda + ncfo
    result = _f31_cashflow_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel scaled by EPS magnitude
def f31cfa_f31_cash_flow_acceleration_fcfaccelxeps_63d_base_v072_signal(fcf, eps, closeadj):
    result = _f31_cashflow_accel_fcf(fcf, 63) * eps.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d FCF accel scaled by EPS magnitude
def f31cfa_f31_cash_flow_acceleration_fcfaccelxeps_252d_base_v073_signal(fcf, eps, closeadj):
    result = _f31_cashflow_accel_fcf(fcf, 252) * eps.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d FCF accel × current FCF level (compounding pressure)
def f31cfa_f31_cash_flow_acceleration_fcfaccelxlevel_63d_base_v074_signal(fcf, closeadj):
    a = _f31_cashflow_accel_fcf(fcf, 63)
    result = a * fcf.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d NCFO accel × current NCFO level
def f31cfa_f31_cash_flow_acceleration_ncfoaccelxlevel_252d_base_v075_signal(ncfo, closeadj):
    a = _f31_cashflow_accel_ncfo(ncfo, 252)
    result = a * ncfo.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f31cfa_f31_cash_flow_acceleration_fcfaccel_21d_base_v001_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccel_63d_base_v002_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccel_126d_base_v003_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccel_252d_base_v004_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccel_21d_base_v005_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccel_63d_base_v006_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccel_126d_base_v007_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccel_252d_base_v008_signal,
    f31cfa_f31_cash_flow_acceleration_opincaccel_21d_base_v009_signal,
    f31cfa_f31_cash_flow_acceleration_opincaccel_63d_base_v010_signal,
    f31cfa_f31_cash_flow_acceleration_opincaccel_252d_base_v011_signal,
    f31cfa_f31_cash_flow_acceleration_ebitdaaccel_21d_base_v012_signal,
    f31cfa_f31_cash_flow_acceleration_ebitdaaccel_63d_base_v013_signal,
    f31cfa_f31_cash_flow_acceleration_ebitdaaccel_252d_base_v014_signal,
    f31cfa_f31_cash_flow_acceleration_netincaccel_21d_base_v015_signal,
    f31cfa_f31_cash_flow_acceleration_netincaccel_63d_base_v016_signal,
    f31cfa_f31_cash_flow_acceleration_netincaccel_252d_base_v017_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelmean_63d_base_v018_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelmean_126d_base_v019_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelmean_63d_base_v020_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelmean_126d_base_v021_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelstd_63d_base_v022_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelstd_252d_base_v023_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelstd_63d_base_v024_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelstd_252d_base_v025_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelz_252d_base_v026_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelz_252d_base_v027_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelz_504d_base_v028_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelz_504d_base_v029_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelps_21d_base_v030_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelps_63d_base_v031_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelps_252d_base_v032_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelps_63d_base_v033_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelps_252d_base_v034_signal,
    f31cfa_f31_cash_flow_acceleration_fcfmarginaccel_63d_base_v035_signal,
    f31cfa_f31_cash_flow_acceleration_fcfmarginaccel_252d_base_v036_signal,
    f31cfa_f31_cash_flow_acceleration_ncfomarginaccel_63d_base_v037_signal,
    f31cfa_f31_cash_flow_acceleration_ncfomarginaccel_252d_base_v038_signal,
    f31cfa_f31_cash_flow_acceleration_fcftoassetaccel_63d_base_v039_signal,
    f31cfa_f31_cash_flow_acceleration_fcftoassetaccel_252d_base_v040_signal,
    f31cfa_f31_cash_flow_acceleration_fcftoequityaccel_63d_base_v041_signal,
    f31cfa_f31_cash_flow_acceleration_fcftoequityaccel_252d_base_v042_signal,
    f31cfa_f31_cash_flow_acceleration_ncfotoassetaccel_63d_base_v043_signal,
    f31cfa_f31_cash_flow_acceleration_ncfotoassetaccel_252d_base_v044_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxmargin_63d_base_v045_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxmargin_252d_base_v046_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelxmargin_63d_base_v047_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelxmargin_252d_base_v048_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxrev_63d_base_v049_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxrev_252d_base_v050_signal,
    f31cfa_f31_cash_flow_acceleration_fcfmcapxaccel_21d_base_v051_signal,
    f31cfa_f31_cash_flow_acceleration_fcfmcapxaccel_63d_base_v052_signal,
    f31cfa_f31_cash_flow_acceleration_fcfmcapxaccel_252d_base_v053_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelposcnt_63d_base_v054_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelposcnt_252d_base_v055_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelposcnt_252d_base_v056_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelposcnt_63d_base_v057_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelratio_63v252_base_v058_signal,
    f31cfa_f31_cash_flow_acceleration_fcfacceldiff_21m63_base_v059_signal,
    f31cfa_f31_cash_flow_acceleration_fcfacceldiff_63m252_base_v060_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoacceldiff_21m63_base_v061_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoacceldiff_63m252_base_v062_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxebitda_21d_base_v063_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxebitda_252d_base_v064_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxwc_63d_base_v065_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxwc_252d_base_v066_signal,
    f31cfa_f31_cash_flow_acceleration_gpaccel_21d_base_v067_signal,
    f31cfa_f31_cash_flow_acceleration_gpaccel_63d_base_v068_signal,
    f31cfa_f31_cash_flow_acceleration_gpaccel_252d_base_v069_signal,
    f31cfa_f31_cash_flow_acceleration_ebitdancfocompose_21d_base_v070_signal,
    f31cfa_f31_cash_flow_acceleration_ebitdancfocompose_252d_base_v071_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxeps_63d_base_v072_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxeps_252d_base_v073_signal,
    f31cfa_f31_cash_flow_acceleration_fcfaccelxlevel_63d_base_v074_signal,
    f31cfa_f31_cash_flow_acceleration_ncfoaccelxlevel_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_CASH_FLOW_ACCELERATION_REGISTRY_001_075 = REGISTRY


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
    assets = fund_walk(0.0004, 0.012, 1.2e9).rename("assets")
    ebitda = fund_walk(0.0005, 0.018, 2e7).rename("ebitda")
    capex = fund_walk(0.0004, 0.022, 5e6).rename("capex")
    eps = fund_walk(0.0005, 0.02, 2.0).rename("eps")
    sharesbas = fund_walk(0.0001, 0.005, 1e7).rename("sharesbas")
    ncfo = fund_walk(0.0005, 0.022, 1.5e7).rename("ncfo")
    opinc = fund_walk(0.0005, 0.02, 2.5e7).rename("opinc")
    gp = fund_walk(0.0005, 0.018, 4e7).rename("gp")
    workingcapital = fund_walk(0.0004, 0.02, 3e7).rename("workingcapital")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf,
        "equity": equity, "assets": assets, "ebitda": ebitda, "capex": capex,
        "eps": eps, "sharesbas": sharesbas, "ncfo": ncfo, "opinc": opinc,
        "gp": gp, "workingcapital": workingcapital,
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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f31_cash_flow_acceleration_base_001_075_claude: {n_features} features pass")
