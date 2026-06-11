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


def _slope_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan).rolling(w, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f33_efficiency_accel_assetturn(revenue, assets, w):
    at = revenue / assets.replace(0, np.nan)
    g = _diff(at, w) / at.shift(w).abs().replace(0, np.nan)
    return _diff(g, w)


def _f33_efficiency_accel_eqturn(revenue, equity, w):
    eqt = revenue / equity.replace(0, np.nan)
    g = _diff(eqt, w) / eqt.shift(w).abs().replace(0, np.nan)
    return _diff(g, w)


def _f33_efficiency_accel_growth(s, w):
    g = _diff(s, w) / s.shift(w).abs().replace(0, np.nan)
    return _diff(g, w)


# 5d slope of 21d asset turnover acceleration × close
def f33ea_f33_efficiency_acceleration_atrnaccel_21d_slope_v001_signal(revenue, assets, closeadj):
    base = _f33_efficiency_accel_assetturn(revenue, assets, 21) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d asset turnover acceleration × close
def f33ea_f33_efficiency_acceleration_atrnaccel_21d_slope_v002_signal(revenue, assets, closeadj):
    base = _f33_efficiency_accel_assetturn(revenue, assets, 21) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d asset turnover acceleration × close
def f33ea_f33_efficiency_acceleration_atrnaccel_63d_slope_v003_signal(revenue, assets, closeadj):
    base = _f33_efficiency_accel_assetturn(revenue, assets, 63) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d asset turnover acceleration × close
def f33ea_f33_efficiency_acceleration_atrnaccel_63d_slope_v004_signal(revenue, assets, closeadj):
    base = _f33_efficiency_accel_assetturn(revenue, assets, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d asset turnover acceleration × close
def f33ea_f33_efficiency_acceleration_atrnaccel_63d_slope_v005_signal(revenue, assets, closeadj):
    base = _f33_efficiency_accel_assetturn(revenue, assets, 63) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d asset turnover acceleration × close
def f33ea_f33_efficiency_acceleration_atrnaccel_126d_slope_v006_signal(revenue, assets, closeadj):
    base = _f33_efficiency_accel_assetturn(revenue, assets, 126) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d asset turnover acceleration × close
def f33ea_f33_efficiency_acceleration_atrnaccel_126d_slope_v007_signal(revenue, assets, closeadj):
    base = _f33_efficiency_accel_assetturn(revenue, assets, 126) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d asset turnover acceleration × close
def f33ea_f33_efficiency_acceleration_atrnaccel_252d_slope_v008_signal(revenue, assets, closeadj):
    base = _f33_efficiency_accel_assetturn(revenue, assets, 252) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d asset turnover acceleration × close
def f33ea_f33_efficiency_acceleration_atrnaccel_252d_slope_v009_signal(revenue, assets, closeadj):
    base = _f33_efficiency_accel_assetturn(revenue, assets, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d eq turnover acceleration × close
def f33ea_f33_efficiency_acceleration_eqtrnaccel_21d_slope_v010_signal(revenue, equity, closeadj):
    base = _f33_efficiency_accel_eqturn(revenue, equity, 21) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d eq turnover acceleration × close
def f33ea_f33_efficiency_acceleration_eqtrnaccel_21d_slope_v011_signal(revenue, equity, closeadj):
    base = _f33_efficiency_accel_eqturn(revenue, equity, 21) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d eq turnover acceleration × close
def f33ea_f33_efficiency_acceleration_eqtrnaccel_63d_slope_v012_signal(revenue, equity, closeadj):
    base = _f33_efficiency_accel_eqturn(revenue, equity, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d eq turnover acceleration × close
def f33ea_f33_efficiency_acceleration_eqtrnaccel_63d_slope_v013_signal(revenue, equity, closeadj):
    base = _f33_efficiency_accel_eqturn(revenue, equity, 63) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d eq turnover acceleration × close
def f33ea_f33_efficiency_acceleration_eqtrnaccel_126d_slope_v014_signal(revenue, equity, closeadj):
    base = _f33_efficiency_accel_eqturn(revenue, equity, 126) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d eq turnover acceleration × close
def f33ea_f33_efficiency_acceleration_eqtrnaccel_252d_slope_v015_signal(revenue, equity, closeadj):
    base = _f33_efficiency_accel_eqturn(revenue, equity, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ROA acceleration × close
def f33ea_f33_efficiency_acceleration_roaaccel_21d_slope_v016_signal(netinc, assets, closeadj):
    s = netinc / assets.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 21) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ROA acceleration × close
def f33ea_f33_efficiency_acceleration_roaaccel_63d_slope_v017_signal(netinc, assets, closeadj):
    s = netinc / assets.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ROA acceleration × close
def f33ea_f33_efficiency_acceleration_roaaccel_252d_slope_v018_signal(netinc, assets, closeadj):
    s = netinc / assets.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ROE acceleration × close
def f33ea_f33_efficiency_acceleration_roeaccel_21d_slope_v019_signal(netinc, equity, closeadj):
    s = netinc / equity.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 21) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ROE acceleration × close
def f33ea_f33_efficiency_acceleration_roeaccel_63d_slope_v020_signal(netinc, equity, closeadj):
    s = netinc / equity.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ROE acceleration × close
def f33ea_f33_efficiency_acceleration_roeaccel_252d_slope_v021_signal(netinc, equity, closeadj):
    s = netinc / equity.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d gp/assets acceleration × close
def f33ea_f33_efficiency_acceleration_gpaccel_21d_slope_v022_signal(gp, assets, closeadj):
    s = gp / assets.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 21) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d gp/assets acceleration × close
def f33ea_f33_efficiency_acceleration_gpaccel_63d_slope_v023_signal(gp, assets, closeadj):
    s = gp / assets.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d gp/assets acceleration × close
def f33ea_f33_efficiency_acceleration_gpaccel_252d_slope_v024_signal(gp, assets, closeadj):
    s = gp / assets.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d asset turnover accel mean
def f33ea_f33_efficiency_acceleration_atrnaccelmean_63d_slope_v025_signal(revenue, assets, closeadj):
    base = _mean(_f33_efficiency_accel_assetturn(revenue, assets, 63), 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d asset turnover accel mean
def f33ea_f33_efficiency_acceleration_atrnaccelmean_126d_slope_v026_signal(revenue, assets, closeadj):
    base = _mean(_f33_efficiency_accel_assetturn(revenue, assets, 252), 126) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d eq turnover accel mean
def f33ea_f33_efficiency_acceleration_eqtrnaccelmean_63d_slope_v027_signal(revenue, equity, closeadj):
    base = _mean(_f33_efficiency_accel_eqturn(revenue, equity, 63), 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d eq turnover accel mean
def f33ea_f33_efficiency_acceleration_eqtrnaccelmean_126d_slope_v028_signal(revenue, equity, closeadj):
    base = _mean(_f33_efficiency_accel_eqturn(revenue, equity, 252), 126) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d asset turnover accel std
def f33ea_f33_efficiency_acceleration_atrnaccelstd_63d_slope_v029_signal(revenue, assets, closeadj):
    base = _std(_f33_efficiency_accel_assetturn(revenue, assets, 63), 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d asset turnover accel std
def f33ea_f33_efficiency_acceleration_atrnaccelstd_252d_slope_v030_signal(revenue, assets, closeadj):
    base = _std(_f33_efficiency_accel_assetturn(revenue, assets, 252), 126) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d eq turnover accel std
def f33ea_f33_efficiency_acceleration_eqtrnaccelstd_63d_slope_v031_signal(revenue, equity, closeadj):
    base = _std(_f33_efficiency_accel_eqturn(revenue, equity, 63), 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d eq turnover accel std
def f33ea_f33_efficiency_acceleration_eqtrnaccelstd_252d_slope_v032_signal(revenue, equity, closeadj):
    base = _std(_f33_efficiency_accel_eqturn(revenue, equity, 252), 126) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d asset turnover accel zscore
def f33ea_f33_efficiency_acceleration_atrnaccelz_252d_slope_v033_signal(revenue, assets, closeadj):
    base = _z(_f33_efficiency_accel_assetturn(revenue, assets, 63), 252) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d eq turnover accel zscore
def f33ea_f33_efficiency_acceleration_eqtrnaccelz_252d_slope_v034_signal(revenue, equity, closeadj):
    base = _z(_f33_efficiency_accel_eqturn(revenue, equity, 63), 252) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d asset turnover accel zscore
def f33ea_f33_efficiency_acceleration_atrnaccelz_504d_slope_v035_signal(revenue, assets, closeadj):
    base = _z(_f33_efficiency_accel_assetturn(revenue, assets, 252), 504) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d eq turnover accel zscore
def f33ea_f33_efficiency_acceleration_eqtrnaccelz_504d_slope_v036_signal(revenue, equity, closeadj):
    base = _z(_f33_efficiency_accel_eqturn(revenue, equity, 252), 504) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d revenue/sharesbas accel
def f33ea_f33_efficiency_acceleration_revpsaccel_21d_slope_v037_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(rps, 21) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d revenue/sharesbas accel
def f33ea_f33_efficiency_acceleration_revpsaccel_63d_slope_v038_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(rps, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d revenue/sharesbas accel
def f33ea_f33_efficiency_acceleration_revpsaccel_252d_slope_v039_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(rps, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d opinc/asset accel
def f33ea_f33_efficiency_acceleration_opincxasset_63d_slope_v040_signal(opinc, assets, closeadj):
    s = opinc / assets.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d opinc/asset accel
def f33ea_f33_efficiency_acceleration_opincxasset_252d_slope_v041_signal(opinc, assets, closeadj):
    s = opinc / assets.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d EBITDA/asset accel
def f33ea_f33_efficiency_acceleration_ebitdaxasset_63d_slope_v042_signal(ebitda, assets, closeadj):
    s = ebitda / assets.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d EBITDA/asset accel
def f33ea_f33_efficiency_acceleration_ebitdaxasset_252d_slope_v043_signal(ebitda, assets, closeadj):
    s = ebitda / assets.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d opinc/eq accel
def f33ea_f33_efficiency_acceleration_opincxeq_63d_slope_v044_signal(opinc, equity, closeadj):
    s = opinc / equity.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d opinc/eq accel
def f33ea_f33_efficiency_acceleration_opincxeq_252d_slope_v045_signal(opinc, equity, closeadj):
    s = opinc / equity.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d EBITDA/eq accel
def f33ea_f33_efficiency_acceleration_ebitdaxeq_63d_slope_v046_signal(ebitda, equity, closeadj):
    s = ebitda / equity.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d EBITDA/eq accel
def f33ea_f33_efficiency_acceleration_ebitdaxeq_252d_slope_v047_signal(ebitda, equity, closeadj):
    s = ebitda / equity.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d FCF/asset accel
def f33ea_f33_efficiency_acceleration_fcfxasset_63d_slope_v048_signal(fcf, assets, closeadj):
    s = fcf / assets.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d FCF/asset accel
def f33ea_f33_efficiency_acceleration_fcfxasset_252d_slope_v049_signal(fcf, assets, closeadj):
    s = fcf / assets.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d NCFO/asset accel
def f33ea_f33_efficiency_acceleration_ncfoxasset_63d_slope_v050_signal(ncfo, assets, closeadj):
    s = ncfo / assets.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d NCFO/asset accel
def f33ea_f33_efficiency_acceleration_ncfoxasset_252d_slope_v051_signal(ncfo, assets, closeadj):
    s = ncfo / assets.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asset turnover accel × level 63d
def f33ea_f33_efficiency_acceleration_atrnaccelxlevel_63d_slope_v052_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    at = revenue / assets.replace(0, np.nan)
    base = a * at * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of asset turnover accel × level 252d
def f33ea_f33_efficiency_acceleration_atrnaccelxlevel_252d_slope_v053_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 252)
    at = revenue / assets.replace(0, np.nan)
    base = a * at * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of eq turnover accel × level 63d
def f33ea_f33_efficiency_acceleration_eqtrnaccelxlevel_63d_slope_v054_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 63)
    eqt = revenue / equity.replace(0, np.nan)
    base = a * eqt * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of eq turnover accel × level 252d
def f33ea_f33_efficiency_acceleration_eqtrnaccelxlevel_252d_slope_v055_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 252)
    eqt = revenue / equity.replace(0, np.nan)
    base = a * eqt * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asset turnover accel × revenue 63d
def f33ea_f33_efficiency_acceleration_atrnaccelxrev_63d_slope_v056_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    base = a * revenue.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of asset turnover accel × revenue 252d
def f33ea_f33_efficiency_acceleration_atrnaccelxrev_252d_slope_v057_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 252)
    base = a * revenue.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d capex/revenue accel
def f33ea_f33_efficiency_acceleration_capxrev_21d_slope_v058_signal(capex, revenue, closeadj):
    s = capex / revenue.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 21) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d capex/revenue accel
def f33ea_f33_efficiency_acceleration_capxrev_63d_slope_v059_signal(capex, revenue, closeadj):
    s = capex / revenue.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d capex/revenue accel
def f33ea_f33_efficiency_acceleration_capxrev_252d_slope_v060_signal(capex, revenue, closeadj):
    s = capex / revenue.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d asset turnover accel pos count
def f33ea_f33_efficiency_acceleration_atrnposcnt_63d_slope_v061_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 21)
    base = (a).rolling(63, min_periods=21).mean() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d asset turnover accel pos count
def f33ea_f33_efficiency_acceleration_atrnposcnt_252d_slope_v062_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 21)
    base = (a).rolling(252, min_periods=63).mean() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d eq turnover accel pos count
def f33ea_f33_efficiency_acceleration_eqtrnposcnt_252d_slope_v063_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 21)
    base = (a).rolling(252, min_periods=63).mean() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d eq turnover accel pos count
def f33ea_f33_efficiency_acceleration_eqtrnposcnt_63d_slope_v064_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 21)
    base = (a).rolling(63, min_periods=21).mean() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asset turnover accel ratio 63v252
def f33ea_f33_efficiency_acceleration_atrnratio_63v252_slope_v065_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    b = _f33_efficiency_accel_assetturn(revenue, assets, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of asset turnover accel diff 21m63
def f33ea_f33_efficiency_acceleration_atrndiff_21m63_slope_v066_signal(revenue, assets, closeadj):
    base = (_f33_efficiency_accel_assetturn(revenue, assets, 21) - _f33_efficiency_accel_assetturn(revenue, assets, 63)) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asset turnover accel diff 63m252
def f33ea_f33_efficiency_acceleration_atrndiff_63m252_slope_v067_signal(revenue, assets, closeadj):
    base = (_f33_efficiency_accel_assetturn(revenue, assets, 63) - _f33_efficiency_accel_assetturn(revenue, assets, 252)) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of eq turnover accel diff 21m63
def f33ea_f33_efficiency_acceleration_eqtrndiff_21m63_slope_v068_signal(revenue, equity, closeadj):
    base = (_f33_efficiency_accel_eqturn(revenue, equity, 21) - _f33_efficiency_accel_eqturn(revenue, equity, 63)) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of eq turnover accel diff 63m252
def f33ea_f33_efficiency_acceleration_eqtrndiff_63m252_slope_v069_signal(revenue, equity, closeadj):
    base = (_f33_efficiency_accel_eqturn(revenue, equity, 63) - _f33_efficiency_accel_eqturn(revenue, equity, 252)) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of asset turnover accel × ebitda 21d
def f33ea_f33_efficiency_acceleration_atrnaccelxebitda_21d_slope_v070_signal(revenue, assets, ebitda, closeadj):
    base = _f33_efficiency_accel_assetturn(revenue, assets, 21) * ebitda.abs() * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of asset turnover accel × ebitda 252d
def f33ea_f33_efficiency_acceleration_atrnaccelxebitda_252d_slope_v071_signal(revenue, assets, ebitda, closeadj):
    base = _f33_efficiency_accel_assetturn(revenue, assets, 252) * ebitda.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asset turnover accel × wc 63d
def f33ea_f33_efficiency_acceleration_atrnaccelxwc_63d_slope_v072_signal(revenue, assets, workingcapital, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    wc = _diff(workingcapital, 63)
    base = a * wc * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of asset turnover accel × wc 252d
def f33ea_f33_efficiency_acceleration_atrnaccelxwc_252d_slope_v073_signal(revenue, assets, workingcapital, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 252)
    wc = _diff(workingcapital, 252)
    base = a * wc * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d ROA × level
def f33ea_f33_efficiency_acceleration_roaxlevel_21d_slope_v074_signal(netinc, assets, closeadj):
    s = netinc / assets.replace(0, np.nan)
    a = _f33_efficiency_accel_growth(s, 21)
    base = a * netinc.abs() * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d ROE × level
def f33ea_f33_efficiency_acceleration_roexlevel_63d_slope_v075_signal(netinc, equity, closeadj):
    s = netinc / equity.replace(0, np.nan)
    a = _f33_efficiency_accel_growth(s, 63)
    base = a * equity.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d ROA × asset
def f33ea_f33_efficiency_acceleration_roaxasset_252d_slope_v076_signal(netinc, assets, closeadj):
    s = netinc / assets.replace(0, np.nan)
    a = _f33_efficiency_accel_growth(s, 252)
    base = a * assets.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d efficiency composite
def f33ea_f33_efficiency_acceleration_effcompose_21d_slope_v077_signal(revenue, assets, equity, closeadj):
    s = revenue / (assets + equity).replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 21) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d efficiency composite
def f33ea_f33_efficiency_acceleration_effcompose_252d_slope_v078_signal(revenue, assets, equity, closeadj):
    s = revenue / (assets + equity).replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asset turnover accel × eps 63d
def f33ea_f33_efficiency_acceleration_atrnaccelxeps_63d_slope_v079_signal(revenue, assets, eps, closeadj):
    base = _f33_efficiency_accel_assetturn(revenue, assets, 63) * eps.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of eq turnover accel × eps 252d
def f33ea_f33_efficiency_acceleration_eqtrnaccelxeps_252d_slope_v080_signal(revenue, equity, eps, closeadj):
    base = _f33_efficiency_accel_eqturn(revenue, equity, 252) * eps.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asset turnover accel × level 63d
def f33ea_f33_efficiency_acceleration_atrnaccelxlev_63d_slope_v081_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    at = revenue / assets.replace(0, np.nan)
    base = a * at.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of eq turnover accel × level 252d
def f33ea_f33_efficiency_acceleration_eqtrnaccelxlev_252d_slope_v082_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 252)
    eqt = revenue / equity.replace(0, np.nan)
    base = a * eqt.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d asset turnover accel × debt
def f33ea_f33_efficiency_acceleration_atrnaccelxdebt_21d_slope_v083_signal(revenue, assets, debt, closeadj):
    base = _f33_efficiency_accel_assetturn(revenue, assets, 21) * debt.abs() * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d asset turnover accel × debt
def f33ea_f33_efficiency_acceleration_atrnaccelxdebt_252d_slope_v084_signal(revenue, assets, debt, closeadj):
    base = _f33_efficiency_accel_assetturn(revenue, assets, 252) * debt.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asset turnover accel × current ratio 63d
def f33ea_f33_efficiency_acceleration_atrnaccelxcur_63d_slope_v085_signal(revenue, assets, currentratio, closeadj):
    base = _f33_efficiency_accel_assetturn(revenue, assets, 63) * currentratio * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of asset turnover accel × current ratio 252d
def f33ea_f33_efficiency_acceleration_atrnaccelxcur_252d_slope_v086_signal(revenue, assets, currentratio, closeadj):
    base = _f33_efficiency_accel_assetturn(revenue, assets, 252) * currentratio * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revenue share intensity 63d
def f33ea_f33_efficiency_acceleration_revshareintensity_63d_slope_v087_signal(revenue, sharesbas, closeadj):
    s = revenue / sharesbas.replace(0, np.nan)
    a = _f33_efficiency_accel_growth(s, 63)
    base = a * sharesbas * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revenue share intensity 252d
def f33ea_f33_efficiency_acceleration_revshareintensity_252d_slope_v088_signal(revenue, sharesbas, closeadj):
    s = revenue / sharesbas.replace(0, np.nan)
    a = _f33_efficiency_accel_growth(s, 252)
    base = a * sharesbas * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asset turnover accel EMA63
def f33ea_f33_efficiency_acceleration_atrnaccelema_63d_slope_v089_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 21)
    base = a.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of asset turnover accel EMA252
def f33ea_f33_efficiency_acceleration_atrnaccelema_252d_slope_v090_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    base = a.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of eq turnover accel EMA63
def f33ea_f33_efficiency_acceleration_eqtrnaccelema_63d_slope_v091_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 21)
    base = a.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of eq turnover accel EMA252
def f33ea_f33_efficiency_acceleration_eqtrnaccelema_252d_slope_v092_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 63)
    base = a.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asset turnover accel squared 63d
def f33ea_f33_efficiency_acceleration_atrnaccelsq_63d_slope_v093_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    base = a * a.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of asset turnover accel squared 252d
def f33ea_f33_efficiency_acceleration_atrnaccelsq_252d_slope_v094_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 252)
    base = a * a.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of eq turnover accel squared 63d
def f33ea_f33_efficiency_acceleration_eqtrnaccelsq_63d_slope_v095_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 63)
    base = a * a.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of eq turnover accel squared 252d
def f33ea_f33_efficiency_acceleration_eqtrnaccelsq_252d_slope_v096_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 252)
    base = a * a.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d asset turnover accel area
def f33ea_f33_efficiency_acceleration_atrnaccelarea_63d_slope_v097_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 21)
    base = a.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d asset turnover accel area
def f33ea_f33_efficiency_acceleration_atrnaccelarea_252d_slope_v098_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 21)
    base = a.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d eq turnover accel area
def f33ea_f33_efficiency_acceleration_eqtrnaccelarea_63d_slope_v099_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 21)
    base = a.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d eq turnover accel area
def f33ea_f33_efficiency_acceleration_eqtrnaccelarea_252d_slope_v100_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 21)
    base = a.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d turnover combo
def f33ea_f33_efficiency_acceleration_turncombo_63d_slope_v101_signal(revenue, assets, equity, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    b = _f33_efficiency_accel_eqturn(revenue, equity, 63)
    base = (a + b) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d turnover combo
def f33ea_f33_efficiency_acceleration_turncombo_252d_slope_v102_signal(revenue, assets, equity, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 252)
    b = _f33_efficiency_accel_eqturn(revenue, equity, 252)
    base = (a + b) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asset - eq turnover accel divergence 63d
def f33ea_f33_efficiency_acceleration_atrnminuseq_63d_slope_v103_signal(revenue, assets, equity, closeadj):
    base = (_f33_efficiency_accel_assetturn(revenue, assets, 63) - _f33_efficiency_accel_eqturn(revenue, equity, 63)) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of asset - eq turnover accel divergence 252d
def f33ea_f33_efficiency_acceleration_atrnminuseq_252d_slope_v104_signal(revenue, assets, equity, closeadj):
    base = (_f33_efficiency_accel_assetturn(revenue, assets, 252) - _f33_efficiency_accel_eqturn(revenue, equity, 252)) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asset turnover accel × revg 63d
def f33ea_f33_efficiency_acceleration_atrnaccelxrevg_63d_slope_v105_signal(revenue, assets, closeadj):
    rg = _diff(revenue, 63) / revenue.shift(63).abs().replace(0, np.nan)
    base = _f33_efficiency_accel_assetturn(revenue, assets, 63) * rg * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of asset turnover accel × revg 252d
def f33ea_f33_efficiency_acceleration_atrnaccelxrevg_252d_slope_v106_signal(revenue, assets, closeadj):
    rg = _diff(revenue, 252) / revenue.shift(252).abs().replace(0, np.nan)
    base = _f33_efficiency_accel_assetturn(revenue, assets, 252) * rg * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of eq turnover accel × revg 63d
def f33ea_f33_efficiency_acceleration_eqtrnaccelxrevg_63d_slope_v107_signal(revenue, equity, closeadj):
    rg = _diff(revenue, 63) / revenue.shift(63).abs().replace(0, np.nan)
    base = _f33_efficiency_accel_eqturn(revenue, equity, 63) * rg * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of eq turnover accel × revg 252d
def f33ea_f33_efficiency_acceleration_eqtrnaccelxrevg_252d_slope_v108_signal(revenue, equity, closeadj):
    rg = _diff(revenue, 252) / revenue.shift(252).abs().replace(0, np.nan)
    base = _f33_efficiency_accel_eqturn(revenue, equity, 252) * rg * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of asset turnover accel × eps growth 21d
def f33ea_f33_efficiency_acceleration_atrnaccelxepsg_21d_slope_v109_signal(revenue, assets, eps, closeadj):
    eg = _diff(eps, 21) / eps.shift(21).abs().replace(0, np.nan)
    base = _f33_efficiency_accel_assetturn(revenue, assets, 21) * eg * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of asset turnover accel × eps growth 252d
def f33ea_f33_efficiency_acceleration_atrnaccelxepsg_252d_slope_v110_signal(revenue, assets, eps, closeadj):
    eg = _diff(eps, 252) / eps.shift(252).abs().replace(0, np.nan)
    base = _f33_efficiency_accel_assetturn(revenue, assets, 252) * eg * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of (gp-capex)/revenue accel 63d
def f33ea_f33_efficiency_acceleration_gpmcapxratio_63d_slope_v111_signal(gp, capex, revenue, closeadj):
    s = (gp - capex) / revenue.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of (gp-capex)/revenue accel 252d
def f33ea_f33_efficiency_acceleration_gpmcapxratio_252d_slope_v112_signal(gp, capex, revenue, closeadj):
    s = (gp - capex) / revenue.replace(0, np.nan)
    base = _f33_efficiency_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asset turnover accel × quality 63d
def f33ea_f33_efficiency_acceleration_atrnaccelxqual_63d_slope_v113_signal(revenue, assets, fcf, ebitda, closeadj):
    q = fcf / ebitda.replace(0, np.nan)
    base = _f33_efficiency_accel_assetturn(revenue, assets, 63) * q * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of asset turnover accel × quality 252d
def f33ea_f33_efficiency_acceleration_atrnaccelxqual_252d_slope_v114_signal(revenue, assets, fcf, ebitda, closeadj):
    q = fcf / ebitda.replace(0, np.nan)
    base = _f33_efficiency_accel_assetturn(revenue, assets, 252) * q * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asset/eq turnover accel ratio 63d
def f33ea_f33_efficiency_acceleration_atrnvseq_63d_slope_v115_signal(revenue, assets, equity, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    b = _f33_efficiency_accel_eqturn(revenue, equity, 63).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of asset/eq turnover accel ratio 252d
def f33ea_f33_efficiency_acceleration_atrnvseq_252d_slope_v116_signal(revenue, assets, equity, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 252)
    b = _f33_efficiency_accel_eqturn(revenue, equity, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of asset turnover accel rolling 252d mean
def f33ea_f33_efficiency_acceleration_atrnaccelxavg_252d_slope_v117_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    base = _mean(a, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of eq turnover accel rolling 252d mean
def f33ea_f33_efficiency_acceleration_eqtrnaccelxavg_252d_slope_v118_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 63)
    base = _mean(a, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asset turnover × asset 63d
def f33ea_f33_efficiency_acceleration_atrnxasset_63d_slope_v119_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    base = a * assets.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of eq turnover × equity 252d
def f33ea_f33_efficiency_acceleration_eqtrnxeq_252d_slope_v120_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 252)
    base = a * equity.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asset turnover accel sign sum 63d
def f33ea_f33_efficiency_acceleration_atrnaccelsignsum_63d_slope_v121_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 21)
    sg = np.sign(a)
    base = sg.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of asset turnover accel sign sum 252d
def f33ea_f33_efficiency_acceleration_atrnaccelsignsum_252d_slope_v122_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 21)
    sg = np.sign(a)
    base = sg.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of eq turnover accel sign sum 63d
def f33ea_f33_efficiency_acceleration_eqtrnaccelsignsum_63d_slope_v123_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 21)
    sg = np.sign(a)
    base = sg.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of eq turnover accel sign sum 252d
def f33ea_f33_efficiency_acceleration_eqtrnaccelsignsum_252d_slope_v124_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 21)
    sg = np.sign(a)
    base = sg.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asset turnover accel × tax 63d
def f33ea_f33_efficiency_acceleration_atrnaccelxtax_63d_slope_v125_signal(revenue, assets, taxexp, closeadj):
    base = _f33_efficiency_accel_assetturn(revenue, assets, 63) * taxexp.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of asset turnover accel × tax 252d
def f33ea_f33_efficiency_acceleration_atrnaccelxtax_252d_slope_v126_signal(revenue, assets, taxexp, closeadj):
    base = _f33_efficiency_accel_assetturn(revenue, assets, 252) * taxexp.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of eq turnover accel × intexp 63d
def f33ea_f33_efficiency_acceleration_eqtrnaccelxint_63d_slope_v127_signal(revenue, equity, intexp, closeadj):
    base = _f33_efficiency_accel_eqturn(revenue, equity, 63) * intexp.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of eq turnover accel × intexp 252d
def f33ea_f33_efficiency_acceleration_eqtrnaccelxint_252d_slope_v128_signal(revenue, equity, intexp, closeadj):
    base = _f33_efficiency_accel_eqturn(revenue, equity, 252) * intexp.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asset turnover accel × retearn 63d
def f33ea_f33_efficiency_acceleration_atrnaccelxretearn_63d_slope_v129_signal(revenue, assets, retearn, closeadj):
    base = _f33_efficiency_accel_assetturn(revenue, assets, 63) * retearn.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of asset turnover accel × retearn 252d
def f33ea_f33_efficiency_acceleration_atrnaccelxretearn_252d_slope_v130_signal(revenue, assets, retearn, closeadj):
    base = _f33_efficiency_accel_assetturn(revenue, assets, 252) * retearn.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of eq turnover accel × liabilities 63d
def f33ea_f33_efficiency_acceleration_eqtrnaccelxliab_63d_slope_v131_signal(revenue, equity, liabilities, closeadj):
    base = _f33_efficiency_accel_eqturn(revenue, equity, 63) * liabilities.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of eq turnover accel × liabilities 252d
def f33ea_f33_efficiency_acceleration_eqtrnaccelxliab_252d_slope_v132_signal(revenue, equity, liabilities, closeadj):
    base = _f33_efficiency_accel_eqturn(revenue, equity, 252) * liabilities.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of revenue/sharesbas accel zscore 252d
def f33ea_f33_efficiency_acceleration_revpsaccelz_252d_slope_v133_signal(revenue, sharesbas, closeadj):
    s = revenue / sharesbas.replace(0, np.nan)
    a = _f33_efficiency_accel_growth(s, 63)
    base = _z(a, 252) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of revenue/sharesbas accel zscore 504d
def f33ea_f33_efficiency_acceleration_revpsaccelz_504d_slope_v134_signal(revenue, sharesbas, closeadj):
    s = revenue / sharesbas.replace(0, np.nan)
    a = _f33_efficiency_accel_growth(s, 252)
    base = _z(a, 504) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of multi-window asset turnover accel
def f33ea_f33_efficiency_acceleration_atrnaccelmulti_slope_v135_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 21)
    b = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    c = _f33_efficiency_accel_assetturn(revenue, assets, 252)
    base = (a + b + c) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of multi-window eq turnover accel
def f33ea_f33_efficiency_acceleration_eqtrnaccelmulti_slope_v136_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 21)
    b = _f33_efficiency_accel_eqturn(revenue, equity, 63)
    c = _f33_efficiency_accel_eqturn(revenue, equity, 252)
    base = (a + b + c) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asset turnover health 63d
def f33ea_f33_efficiency_acceleration_atrnhealth_63d_slope_v137_signal(revenue, assets, currentratio, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    base = a * currentratio * revenue.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of asset turnover health 252d
def f33ea_f33_efficiency_acceleration_atrnhealth_252d_slope_v138_signal(revenue, assets, currentratio, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 252)
    base = a * currentratio * revenue.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asset turnover accel × netinc growth 63d
def f33ea_f33_efficiency_acceleration_atrnaccelxnig_63d_slope_v139_signal(revenue, assets, netinc, closeadj):
    ng = _diff(netinc, 63) / netinc.shift(63).abs().replace(0, np.nan)
    base = _f33_efficiency_accel_assetturn(revenue, assets, 63) * ng * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of asset turnover accel × netinc growth 252d
def f33ea_f33_efficiency_acceleration_atrnaccelxnig_252d_slope_v140_signal(revenue, assets, netinc, closeadj):
    ng = _diff(netinc, 252) / netinc.shift(252).abs().replace(0, np.nan)
    base = _f33_efficiency_accel_assetturn(revenue, assets, 252) * ng * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of asset turnover accel anomaly 63d
def f33ea_f33_efficiency_acceleration_atrnaccelanomaly_63d_slope_v141_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    bm = a.expanding(min_periods=63).mean()
    base = (a - bm) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of asset turnover accel anomaly 252d
def f33ea_f33_efficiency_acceleration_atrnaccelanomaly_252d_slope_v142_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 252)
    bm = a.expanding(min_periods=126).mean()
    base = (a - bm) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of EBITDA accel × asset turnover 63d
def f33ea_f33_efficiency_acceleration_ebitdaaccelxat_63d_slope_v143_signal(ebitda, revenue, assets, closeadj):
    a = _f33_efficiency_accel_growth(ebitda, 63)
    at = revenue / assets.replace(0, np.nan)
    base = a * at * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of EBITDA accel × asset turnover 252d
def f33ea_f33_efficiency_acceleration_ebitdaaccelxat_252d_slope_v144_signal(ebitda, revenue, assets, closeadj):
    a = _f33_efficiency_accel_growth(ebitda, 252)
    at = revenue / assets.replace(0, np.nan)
    base = a * at * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of opinc/sharesbas × level 63d
def f33ea_f33_efficiency_acceleration_opincpsxlevel_63d_slope_v145_signal(opinc, sharesbas, closeadj):
    s = opinc / sharesbas.replace(0, np.nan)
    a = _f33_efficiency_accel_growth(s, 63)
    base = a * sharesbas * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of opinc/sharesbas × level 252d
def f33ea_f33_efficiency_acceleration_opincpsxlevel_252d_slope_v146_signal(opinc, sharesbas, closeadj):
    s = opinc / sharesbas.replace(0, np.nan)
    a = _f33_efficiency_accel_growth(s, 252)
    base = a * sharesbas * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of joint efficiency accel 63d
def f33ea_f33_efficiency_acceleration_jointeffaccel_63d_slope_v147_signal(revenue, assets, equity, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    b = _f33_efficiency_accel_eqturn(revenue, equity, 63)
    base = a * b * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of joint efficiency accel 252d
def f33ea_f33_efficiency_acceleration_jointeffaccel_252d_slope_v148_signal(revenue, assets, equity, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 252)
    b = _f33_efficiency_accel_eqturn(revenue, equity, 252)
    base = a * b * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of eq turnover accel × ROE quality 63d
def f33ea_f33_efficiency_acceleration_eqtrnaccelxquality_63d_slope_v149_signal(revenue, equity, netinc, closeadj):
    q = netinc / equity.replace(0, np.nan)
    a = _f33_efficiency_accel_eqturn(revenue, equity, 63)
    base = a * q * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of composite efficiency severity 252d
def f33ea_f33_efficiency_acceleration_compositesev_252d_slope_v150_signal(revenue, assets, equity, netinc, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    b = _f33_efficiency_accel_eqturn(revenue, equity, 63)
    s_roa = netinc / assets.replace(0, np.nan)
    c = _f33_efficiency_accel_growth(s_roa, 63)
    s = (a + b + c).rolling(252, min_periods=63).sum()
    base = s * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33ea_f33_efficiency_acceleration_atrnaccel_21d_slope_v001_signal,
    f33ea_f33_efficiency_acceleration_atrnaccel_21d_slope_v002_signal,
    f33ea_f33_efficiency_acceleration_atrnaccel_63d_slope_v003_signal,
    f33ea_f33_efficiency_acceleration_atrnaccel_63d_slope_v004_signal,
    f33ea_f33_efficiency_acceleration_atrnaccel_63d_slope_v005_signal,
    f33ea_f33_efficiency_acceleration_atrnaccel_126d_slope_v006_signal,
    f33ea_f33_efficiency_acceleration_atrnaccel_126d_slope_v007_signal,
    f33ea_f33_efficiency_acceleration_atrnaccel_252d_slope_v008_signal,
    f33ea_f33_efficiency_acceleration_atrnaccel_252d_slope_v009_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccel_21d_slope_v010_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccel_21d_slope_v011_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccel_63d_slope_v012_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccel_63d_slope_v013_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccel_126d_slope_v014_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccel_252d_slope_v015_signal,
    f33ea_f33_efficiency_acceleration_roaaccel_21d_slope_v016_signal,
    f33ea_f33_efficiency_acceleration_roaaccel_63d_slope_v017_signal,
    f33ea_f33_efficiency_acceleration_roaaccel_252d_slope_v018_signal,
    f33ea_f33_efficiency_acceleration_roeaccel_21d_slope_v019_signal,
    f33ea_f33_efficiency_acceleration_roeaccel_63d_slope_v020_signal,
    f33ea_f33_efficiency_acceleration_roeaccel_252d_slope_v021_signal,
    f33ea_f33_efficiency_acceleration_gpaccel_21d_slope_v022_signal,
    f33ea_f33_efficiency_acceleration_gpaccel_63d_slope_v023_signal,
    f33ea_f33_efficiency_acceleration_gpaccel_252d_slope_v024_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelmean_63d_slope_v025_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelmean_126d_slope_v026_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelmean_63d_slope_v027_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelmean_126d_slope_v028_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelstd_63d_slope_v029_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelstd_252d_slope_v030_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelstd_63d_slope_v031_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelstd_252d_slope_v032_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelz_252d_slope_v033_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelz_252d_slope_v034_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelz_504d_slope_v035_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelz_504d_slope_v036_signal,
    f33ea_f33_efficiency_acceleration_revpsaccel_21d_slope_v037_signal,
    f33ea_f33_efficiency_acceleration_revpsaccel_63d_slope_v038_signal,
    f33ea_f33_efficiency_acceleration_revpsaccel_252d_slope_v039_signal,
    f33ea_f33_efficiency_acceleration_opincxasset_63d_slope_v040_signal,
    f33ea_f33_efficiency_acceleration_opincxasset_252d_slope_v041_signal,
    f33ea_f33_efficiency_acceleration_ebitdaxasset_63d_slope_v042_signal,
    f33ea_f33_efficiency_acceleration_ebitdaxasset_252d_slope_v043_signal,
    f33ea_f33_efficiency_acceleration_opincxeq_63d_slope_v044_signal,
    f33ea_f33_efficiency_acceleration_opincxeq_252d_slope_v045_signal,
    f33ea_f33_efficiency_acceleration_ebitdaxeq_63d_slope_v046_signal,
    f33ea_f33_efficiency_acceleration_ebitdaxeq_252d_slope_v047_signal,
    f33ea_f33_efficiency_acceleration_fcfxasset_63d_slope_v048_signal,
    f33ea_f33_efficiency_acceleration_fcfxasset_252d_slope_v049_signal,
    f33ea_f33_efficiency_acceleration_ncfoxasset_63d_slope_v050_signal,
    f33ea_f33_efficiency_acceleration_ncfoxasset_252d_slope_v051_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxlevel_63d_slope_v052_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxlevel_252d_slope_v053_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxlevel_63d_slope_v054_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxlevel_252d_slope_v055_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxrev_63d_slope_v056_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxrev_252d_slope_v057_signal,
    f33ea_f33_efficiency_acceleration_capxrev_21d_slope_v058_signal,
    f33ea_f33_efficiency_acceleration_capxrev_63d_slope_v059_signal,
    f33ea_f33_efficiency_acceleration_capxrev_252d_slope_v060_signal,
    f33ea_f33_efficiency_acceleration_atrnposcnt_63d_slope_v061_signal,
    f33ea_f33_efficiency_acceleration_atrnposcnt_252d_slope_v062_signal,
    f33ea_f33_efficiency_acceleration_eqtrnposcnt_252d_slope_v063_signal,
    f33ea_f33_efficiency_acceleration_eqtrnposcnt_63d_slope_v064_signal,
    f33ea_f33_efficiency_acceleration_atrnratio_63v252_slope_v065_signal,
    f33ea_f33_efficiency_acceleration_atrndiff_21m63_slope_v066_signal,
    f33ea_f33_efficiency_acceleration_atrndiff_63m252_slope_v067_signal,
    f33ea_f33_efficiency_acceleration_eqtrndiff_21m63_slope_v068_signal,
    f33ea_f33_efficiency_acceleration_eqtrndiff_63m252_slope_v069_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxebitda_21d_slope_v070_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxebitda_252d_slope_v071_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxwc_63d_slope_v072_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxwc_252d_slope_v073_signal,
    f33ea_f33_efficiency_acceleration_roaxlevel_21d_slope_v074_signal,
    f33ea_f33_efficiency_acceleration_roexlevel_63d_slope_v075_signal,
    f33ea_f33_efficiency_acceleration_roaxasset_252d_slope_v076_signal,
    f33ea_f33_efficiency_acceleration_effcompose_21d_slope_v077_signal,
    f33ea_f33_efficiency_acceleration_effcompose_252d_slope_v078_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxeps_63d_slope_v079_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxeps_252d_slope_v080_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxlev_63d_slope_v081_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxlev_252d_slope_v082_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxdebt_21d_slope_v083_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxdebt_252d_slope_v084_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxcur_63d_slope_v085_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxcur_252d_slope_v086_signal,
    f33ea_f33_efficiency_acceleration_revshareintensity_63d_slope_v087_signal,
    f33ea_f33_efficiency_acceleration_revshareintensity_252d_slope_v088_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelema_63d_slope_v089_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelema_252d_slope_v090_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelema_63d_slope_v091_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelema_252d_slope_v092_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelsq_63d_slope_v093_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelsq_252d_slope_v094_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelsq_63d_slope_v095_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelsq_252d_slope_v096_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelarea_63d_slope_v097_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelarea_252d_slope_v098_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelarea_63d_slope_v099_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelarea_252d_slope_v100_signal,
    f33ea_f33_efficiency_acceleration_turncombo_63d_slope_v101_signal,
    f33ea_f33_efficiency_acceleration_turncombo_252d_slope_v102_signal,
    f33ea_f33_efficiency_acceleration_atrnminuseq_63d_slope_v103_signal,
    f33ea_f33_efficiency_acceleration_atrnminuseq_252d_slope_v104_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxrevg_63d_slope_v105_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxrevg_252d_slope_v106_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxrevg_63d_slope_v107_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxrevg_252d_slope_v108_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxepsg_21d_slope_v109_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxepsg_252d_slope_v110_signal,
    f33ea_f33_efficiency_acceleration_gpmcapxratio_63d_slope_v111_signal,
    f33ea_f33_efficiency_acceleration_gpmcapxratio_252d_slope_v112_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxqual_63d_slope_v113_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxqual_252d_slope_v114_signal,
    f33ea_f33_efficiency_acceleration_atrnvseq_63d_slope_v115_signal,
    f33ea_f33_efficiency_acceleration_atrnvseq_252d_slope_v116_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxavg_252d_slope_v117_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxavg_252d_slope_v118_signal,
    f33ea_f33_efficiency_acceleration_atrnxasset_63d_slope_v119_signal,
    f33ea_f33_efficiency_acceleration_eqtrnxeq_252d_slope_v120_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelsignsum_63d_slope_v121_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelsignsum_252d_slope_v122_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelsignsum_63d_slope_v123_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelsignsum_252d_slope_v124_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxtax_63d_slope_v125_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxtax_252d_slope_v126_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxint_63d_slope_v127_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxint_252d_slope_v128_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxretearn_63d_slope_v129_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxretearn_252d_slope_v130_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxliab_63d_slope_v131_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxliab_252d_slope_v132_signal,
    f33ea_f33_efficiency_acceleration_revpsaccelz_252d_slope_v133_signal,
    f33ea_f33_efficiency_acceleration_revpsaccelz_504d_slope_v134_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelmulti_slope_v135_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelmulti_slope_v136_signal,
    f33ea_f33_efficiency_acceleration_atrnhealth_63d_slope_v137_signal,
    f33ea_f33_efficiency_acceleration_atrnhealth_252d_slope_v138_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxnig_63d_slope_v139_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxnig_252d_slope_v140_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelanomaly_63d_slope_v141_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelanomaly_252d_slope_v142_signal,
    f33ea_f33_efficiency_acceleration_ebitdaaccelxat_63d_slope_v143_signal,
    f33ea_f33_efficiency_acceleration_ebitdaaccelxat_252d_slope_v144_signal,
    f33ea_f33_efficiency_acceleration_opincpsxlevel_63d_slope_v145_signal,
    f33ea_f33_efficiency_acceleration_opincpsxlevel_252d_slope_v146_signal,
    f33ea_f33_efficiency_acceleration_jointeffaccel_63d_slope_v147_signal,
    f33ea_f33_efficiency_acceleration_jointeffaccel_252d_slope_v148_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxquality_63d_slope_v149_signal,
    f33ea_f33_efficiency_acceleration_compositesev_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_EFFICIENCY_ACCELERATION_REGISTRY_SLOPE = REGISTRY


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
    domain_primitives = ("_f33_efficiency_accel_assetturn", "_f33_efficiency_accel_eqturn", "_f33_efficiency_accel_growth")
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
    print(f"OK f33_efficiency_acceleration_2nd_derivatives_001_150_claude: {n_features} features pass")
