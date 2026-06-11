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


# 21d acceleration of asset turnover (revenue/assets)
def f33ea_f33_efficiency_acceleration_atrnaccel_21d_base_v001_signal(revenue, assets, closeadj):
    result = _f33_efficiency_accel_assetturn(revenue, assets, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of asset turnover
def f33ea_f33_efficiency_acceleration_atrnaccel_63d_base_v002_signal(revenue, assets, closeadj):
    result = _f33_efficiency_accel_assetturn(revenue, assets, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d acceleration of asset turnover
def f33ea_f33_efficiency_acceleration_atrnaccel_126d_base_v003_signal(revenue, assets, closeadj):
    result = _f33_efficiency_accel_assetturn(revenue, assets, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of asset turnover
def f33ea_f33_efficiency_acceleration_atrnaccel_252d_base_v004_signal(revenue, assets, closeadj):
    result = _f33_efficiency_accel_assetturn(revenue, assets, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d acceleration of equity turnover (revenue/equity)
def f33ea_f33_efficiency_acceleration_eqtrnaccel_21d_base_v005_signal(revenue, equity, closeadj):
    result = _f33_efficiency_accel_eqturn(revenue, equity, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of equity turnover
def f33ea_f33_efficiency_acceleration_eqtrnaccel_63d_base_v006_signal(revenue, equity, closeadj):
    result = _f33_efficiency_accel_eqturn(revenue, equity, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d acceleration of equity turnover
def f33ea_f33_efficiency_acceleration_eqtrnaccel_126d_base_v007_signal(revenue, equity, closeadj):
    result = _f33_efficiency_accel_eqturn(revenue, equity, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of equity turnover
def f33ea_f33_efficiency_acceleration_eqtrnaccel_252d_base_v008_signal(revenue, equity, closeadj):
    result = _f33_efficiency_accel_eqturn(revenue, equity, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d acceleration of ROA (netinc/assets)
def f33ea_f33_efficiency_acceleration_roaaccel_21d_base_v009_signal(netinc, assets, closeadj):
    s = netinc / assets.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of ROA
def f33ea_f33_efficiency_acceleration_roaaccel_63d_base_v010_signal(netinc, assets, closeadj):
    s = netinc / assets.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of ROA
def f33ea_f33_efficiency_acceleration_roaaccel_252d_base_v011_signal(netinc, assets, closeadj):
    s = netinc / assets.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d acceleration of ROE (netinc/equity)
def f33ea_f33_efficiency_acceleration_roeaccel_21d_base_v012_signal(netinc, equity, closeadj):
    s = netinc / equity.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of ROE
def f33ea_f33_efficiency_acceleration_roeaccel_63d_base_v013_signal(netinc, equity, closeadj):
    s = netinc / equity.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of ROE
def f33ea_f33_efficiency_acceleration_roeaccel_252d_base_v014_signal(netinc, equity, closeadj):
    s = netinc / equity.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d acceleration of GP/assets
def f33ea_f33_efficiency_acceleration_gpaccel_21d_base_v015_signal(gp, assets, closeadj):
    s = gp / assets.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of GP/assets
def f33ea_f33_efficiency_acceleration_gpaccel_63d_base_v016_signal(gp, assets, closeadj):
    s = gp / assets.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of GP/assets
def f33ea_f33_efficiency_acceleration_gpaccel_252d_base_v017_signal(gp, assets, closeadj):
    s = gp / assets.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel rolling mean
def f33ea_f33_efficiency_acceleration_atrnaccelmean_63d_base_v018_signal(revenue, assets, closeadj):
    result = _mean(_f33_efficiency_accel_assetturn(revenue, assets, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel rolling mean
def f33ea_f33_efficiency_acceleration_atrnaccelmean_126d_base_v019_signal(revenue, assets, closeadj):
    result = _mean(_f33_efficiency_accel_assetturn(revenue, assets, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d equity turnover accel rolling mean
def f33ea_f33_efficiency_acceleration_eqtrnaccelmean_63d_base_v020_signal(revenue, equity, closeadj):
    result = _mean(_f33_efficiency_accel_eqturn(revenue, equity, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d equity turnover accel rolling mean
def f33ea_f33_efficiency_acceleration_eqtrnaccelmean_126d_base_v021_signal(revenue, equity, closeadj):
    result = _mean(_f33_efficiency_accel_eqturn(revenue, equity, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel rolling std
def f33ea_f33_efficiency_acceleration_atrnaccelstd_63d_base_v022_signal(revenue, assets, closeadj):
    result = _std(_f33_efficiency_accel_assetturn(revenue, assets, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel rolling std
def f33ea_f33_efficiency_acceleration_atrnaccelstd_252d_base_v023_signal(revenue, assets, closeadj):
    result = _std(_f33_efficiency_accel_assetturn(revenue, assets, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d equity turnover accel rolling std
def f33ea_f33_efficiency_acceleration_eqtrnaccelstd_63d_base_v024_signal(revenue, equity, closeadj):
    result = _std(_f33_efficiency_accel_eqturn(revenue, equity, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d equity turnover accel rolling std
def f33ea_f33_efficiency_acceleration_eqtrnaccelstd_252d_base_v025_signal(revenue, equity, closeadj):
    result = _std(_f33_efficiency_accel_eqturn(revenue, equity, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel zscore
def f33ea_f33_efficiency_acceleration_atrnaccelz_252d_base_v026_signal(revenue, assets, closeadj):
    result = _z(_f33_efficiency_accel_assetturn(revenue, assets, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d equity turnover accel zscore
def f33ea_f33_efficiency_acceleration_eqtrnaccelz_252d_base_v027_signal(revenue, equity, closeadj):
    result = _z(_f33_efficiency_accel_eqturn(revenue, equity, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d asset turnover accel zscore
def f33ea_f33_efficiency_acceleration_atrnaccelz_504d_base_v028_signal(revenue, assets, closeadj):
    result = _z(_f33_efficiency_accel_assetturn(revenue, assets, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d equity turnover accel zscore
def f33ea_f33_efficiency_acceleration_eqtrnaccelz_504d_base_v029_signal(revenue, equity, closeadj):
    result = _z(_f33_efficiency_accel_eqturn(revenue, equity, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d acceleration of revenue per share
def f33ea_f33_efficiency_acceleration_revpsaccel_21d_base_v030_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(rps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of revenue per share
def f33ea_f33_efficiency_acceleration_revpsaccel_63d_base_v031_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(rps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of revenue per share
def f33ea_f33_efficiency_acceleration_revpsaccel_252d_base_v032_signal(revenue, sharesbas, closeadj):
    rps = revenue / sharesbas.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(rps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of opinc/assets (operating efficiency)
def f33ea_f33_efficiency_acceleration_opincxasset_63d_base_v033_signal(opinc, assets, closeadj):
    s = opinc / assets.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of opinc/assets
def f33ea_f33_efficiency_acceleration_opincxasset_252d_base_v034_signal(opinc, assets, closeadj):
    s = opinc / assets.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of EBITDA/assets
def f33ea_f33_efficiency_acceleration_ebitdaxasset_63d_base_v035_signal(ebitda, assets, closeadj):
    s = ebitda / assets.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of EBITDA/assets
def f33ea_f33_efficiency_acceleration_ebitdaxasset_252d_base_v036_signal(ebitda, assets, closeadj):
    s = ebitda / assets.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of opinc/equity
def f33ea_f33_efficiency_acceleration_opincxeq_63d_base_v037_signal(opinc, equity, closeadj):
    s = opinc / equity.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of opinc/equity
def f33ea_f33_efficiency_acceleration_opincxeq_252d_base_v038_signal(opinc, equity, closeadj):
    s = opinc / equity.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of EBITDA/equity
def f33ea_f33_efficiency_acceleration_ebitdaxeq_63d_base_v039_signal(ebitda, equity, closeadj):
    s = ebitda / equity.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of EBITDA/equity
def f33ea_f33_efficiency_acceleration_ebitdaxeq_252d_base_v040_signal(ebitda, equity, closeadj):
    s = ebitda / equity.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of FCF/assets
def f33ea_f33_efficiency_acceleration_fcfxasset_63d_base_v041_signal(fcf, assets, closeadj):
    s = fcf / assets.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of FCF/assets
def f33ea_f33_efficiency_acceleration_fcfxasset_252d_base_v042_signal(fcf, assets, closeadj):
    s = fcf / assets.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of NCFO/assets
def f33ea_f33_efficiency_acceleration_ncfoxasset_63d_base_v043_signal(ncfo, assets, closeadj):
    s = ncfo / assets.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of NCFO/assets
def f33ea_f33_efficiency_acceleration_ncfoxasset_252d_base_v044_signal(ncfo, assets, closeadj):
    s = ncfo / assets.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel × current asset turnover
def f33ea_f33_efficiency_acceleration_atrnaccelxlevel_63d_base_v045_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    at = revenue / assets.replace(0, np.nan)
    result = a * at * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel × current asset turnover
def f33ea_f33_efficiency_acceleration_atrnaccelxlevel_252d_base_v046_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 252)
    at = revenue / assets.replace(0, np.nan)
    result = a * at * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d equity turnover accel × current equity turnover
def f33ea_f33_efficiency_acceleration_eqtrnaccelxlevel_63d_base_v047_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 63)
    eqt = revenue / equity.replace(0, np.nan)
    result = a * eqt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d equity turnover accel × current equity turnover
def f33ea_f33_efficiency_acceleration_eqtrnaccelxlevel_252d_base_v048_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 252)
    eqt = revenue / equity.replace(0, np.nan)
    result = a * eqt * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel × revenue
def f33ea_f33_efficiency_acceleration_atrnaccelxrev_63d_base_v049_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    result = a * revenue.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel × revenue
def f33ea_f33_efficiency_acceleration_atrnaccelxrev_252d_base_v050_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 252)
    result = a * revenue.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d acceleration of capex/revenue (capital intensity)
def f33ea_f33_efficiency_acceleration_capxrev_21d_base_v051_signal(capex, revenue, closeadj):
    s = capex / revenue.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of capex/revenue
def f33ea_f33_efficiency_acceleration_capxrev_63d_base_v052_signal(capex, revenue, closeadj):
    s = capex / revenue.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of capex/revenue
def f33ea_f33_efficiency_acceleration_capxrev_252d_base_v053_signal(capex, revenue, closeadj):
    s = capex / revenue.replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of days asset turnover accel > 0
def f33ea_f33_efficiency_acceleration_atrnposcnt_63d_base_v054_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 21)
    result = (a).rolling(63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days asset turnover accel > 0
def f33ea_f33_efficiency_acceleration_atrnposcnt_252d_base_v055_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 21)
    result = (a).rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days eq turnover accel > 0
def f33ea_f33_efficiency_acceleration_eqtrnposcnt_252d_base_v056_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 21)
    result = (a).rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of days eq turnover accel > 0
def f33ea_f33_efficiency_acceleration_eqtrnposcnt_63d_base_v057_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 21)
    result = (a).rolling(63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel ratio (63d / 252d)
def f33ea_f33_efficiency_acceleration_atrnratio_63v252_base_v058_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    b = _f33_efficiency_accel_assetturn(revenue, assets, 252).replace(0, np.nan)
    result = a / b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d asset turnover accel - 63d
def f33ea_f33_efficiency_acceleration_atrndiff_21m63_base_v059_signal(revenue, assets, closeadj):
    result = (_f33_efficiency_accel_assetturn(revenue, assets, 21) - _f33_efficiency_accel_assetturn(revenue, assets, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel - 252d
def f33ea_f33_efficiency_acceleration_atrndiff_63m252_base_v060_signal(revenue, assets, closeadj):
    result = (_f33_efficiency_accel_assetturn(revenue, assets, 63) - _f33_efficiency_accel_assetturn(revenue, assets, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d eq turnover accel - 63d
def f33ea_f33_efficiency_acceleration_eqtrndiff_21m63_base_v061_signal(revenue, equity, closeadj):
    result = (_f33_efficiency_accel_eqturn(revenue, equity, 21) - _f33_efficiency_accel_eqturn(revenue, equity, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d eq turnover accel - 252d
def f33ea_f33_efficiency_acceleration_eqtrndiff_63m252_base_v062_signal(revenue, equity, closeadj):
    result = (_f33_efficiency_accel_eqturn(revenue, equity, 63) - _f33_efficiency_accel_eqturn(revenue, equity, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d asset turnover accel × EBITDA
def f33ea_f33_efficiency_acceleration_atrnaccelxebitda_21d_base_v063_signal(revenue, assets, ebitda, closeadj):
    result = _f33_efficiency_accel_assetturn(revenue, assets, 21) * ebitda.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel × EBITDA
def f33ea_f33_efficiency_acceleration_atrnaccelxebitda_252d_base_v064_signal(revenue, assets, ebitda, closeadj):
    result = _f33_efficiency_accel_assetturn(revenue, assets, 252) * ebitda.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel × workingcapital change
def f33ea_f33_efficiency_acceleration_atrnaccelxwc_63d_base_v065_signal(revenue, assets, workingcapital, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    wc = _diff(workingcapital, 63)
    result = a * wc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d asset turnover accel × workingcapital change
def f33ea_f33_efficiency_acceleration_atrnaccelxwc_252d_base_v066_signal(revenue, assets, workingcapital, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 252)
    wc = _diff(workingcapital, 252)
    result = a * wc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ROA accel × close
def f33ea_f33_efficiency_acceleration_roaxlevel_21d_base_v067_signal(netinc, assets, closeadj):
    s = netinc / assets.replace(0, np.nan)
    a = _f33_efficiency_accel_growth(s, 21)
    result = a * netinc.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ROE accel × equity
def f33ea_f33_efficiency_acceleration_roexlevel_63d_base_v068_signal(netinc, equity, closeadj):
    s = netinc / equity.replace(0, np.nan)
    a = _f33_efficiency_accel_growth(s, 63)
    result = a * equity.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ROA accel × assets
def f33ea_f33_efficiency_acceleration_roaxasset_252d_base_v069_signal(netinc, assets, closeadj):
    s = netinc / assets.replace(0, np.nan)
    a = _f33_efficiency_accel_growth(s, 252)
    result = a * assets.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d efficiency composite: revenue/(assets+equity)
def f33ea_f33_efficiency_acceleration_effcompose_21d_base_v070_signal(revenue, assets, equity, closeadj):
    s = revenue / (assets + equity).replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d efficiency composite
def f33ea_f33_efficiency_acceleration_effcompose_252d_base_v071_signal(revenue, assets, equity, closeadj):
    s = revenue / (assets + equity).replace(0, np.nan)
    result = _f33_efficiency_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel × eps magnitude
def f33ea_f33_efficiency_acceleration_atrnaccelxeps_63d_base_v072_signal(revenue, assets, eps, closeadj):
    result = _f33_efficiency_accel_assetturn(revenue, assets, 63) * eps.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eq turnover accel × eps magnitude
def f33ea_f33_efficiency_acceleration_eqtrnaccelxeps_252d_base_v073_signal(revenue, equity, eps, closeadj):
    result = _f33_efficiency_accel_eqturn(revenue, equity, 252) * eps.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d asset turnover accel × current asset turnover level
def f33ea_f33_efficiency_acceleration_atrnaccelxlev_63d_base_v074_signal(revenue, assets, closeadj):
    a = _f33_efficiency_accel_assetturn(revenue, assets, 63)
    at = revenue / assets.replace(0, np.nan)
    result = a * at.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d eq turnover accel × current eq turnover level
def f33ea_f33_efficiency_acceleration_eqtrnaccelxlev_252d_base_v075_signal(revenue, equity, closeadj):
    a = _f33_efficiency_accel_eqturn(revenue, equity, 252)
    eqt = revenue / equity.replace(0, np.nan)
    result = a * eqt.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33ea_f33_efficiency_acceleration_atrnaccel_21d_base_v001_signal,
    f33ea_f33_efficiency_acceleration_atrnaccel_63d_base_v002_signal,
    f33ea_f33_efficiency_acceleration_atrnaccel_126d_base_v003_signal,
    f33ea_f33_efficiency_acceleration_atrnaccel_252d_base_v004_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccel_21d_base_v005_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccel_63d_base_v006_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccel_126d_base_v007_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccel_252d_base_v008_signal,
    f33ea_f33_efficiency_acceleration_roaaccel_21d_base_v009_signal,
    f33ea_f33_efficiency_acceleration_roaaccel_63d_base_v010_signal,
    f33ea_f33_efficiency_acceleration_roaaccel_252d_base_v011_signal,
    f33ea_f33_efficiency_acceleration_roeaccel_21d_base_v012_signal,
    f33ea_f33_efficiency_acceleration_roeaccel_63d_base_v013_signal,
    f33ea_f33_efficiency_acceleration_roeaccel_252d_base_v014_signal,
    f33ea_f33_efficiency_acceleration_gpaccel_21d_base_v015_signal,
    f33ea_f33_efficiency_acceleration_gpaccel_63d_base_v016_signal,
    f33ea_f33_efficiency_acceleration_gpaccel_252d_base_v017_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelmean_63d_base_v018_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelmean_126d_base_v019_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelmean_63d_base_v020_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelmean_126d_base_v021_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelstd_63d_base_v022_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelstd_252d_base_v023_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelstd_63d_base_v024_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelstd_252d_base_v025_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelz_252d_base_v026_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelz_252d_base_v027_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelz_504d_base_v028_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelz_504d_base_v029_signal,
    f33ea_f33_efficiency_acceleration_revpsaccel_21d_base_v030_signal,
    f33ea_f33_efficiency_acceleration_revpsaccel_63d_base_v031_signal,
    f33ea_f33_efficiency_acceleration_revpsaccel_252d_base_v032_signal,
    f33ea_f33_efficiency_acceleration_opincxasset_63d_base_v033_signal,
    f33ea_f33_efficiency_acceleration_opincxasset_252d_base_v034_signal,
    f33ea_f33_efficiency_acceleration_ebitdaxasset_63d_base_v035_signal,
    f33ea_f33_efficiency_acceleration_ebitdaxasset_252d_base_v036_signal,
    f33ea_f33_efficiency_acceleration_opincxeq_63d_base_v037_signal,
    f33ea_f33_efficiency_acceleration_opincxeq_252d_base_v038_signal,
    f33ea_f33_efficiency_acceleration_ebitdaxeq_63d_base_v039_signal,
    f33ea_f33_efficiency_acceleration_ebitdaxeq_252d_base_v040_signal,
    f33ea_f33_efficiency_acceleration_fcfxasset_63d_base_v041_signal,
    f33ea_f33_efficiency_acceleration_fcfxasset_252d_base_v042_signal,
    f33ea_f33_efficiency_acceleration_ncfoxasset_63d_base_v043_signal,
    f33ea_f33_efficiency_acceleration_ncfoxasset_252d_base_v044_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxlevel_63d_base_v045_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxlevel_252d_base_v046_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxlevel_63d_base_v047_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxlevel_252d_base_v048_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxrev_63d_base_v049_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxrev_252d_base_v050_signal,
    f33ea_f33_efficiency_acceleration_capxrev_21d_base_v051_signal,
    f33ea_f33_efficiency_acceleration_capxrev_63d_base_v052_signal,
    f33ea_f33_efficiency_acceleration_capxrev_252d_base_v053_signal,
    f33ea_f33_efficiency_acceleration_atrnposcnt_63d_base_v054_signal,
    f33ea_f33_efficiency_acceleration_atrnposcnt_252d_base_v055_signal,
    f33ea_f33_efficiency_acceleration_eqtrnposcnt_252d_base_v056_signal,
    f33ea_f33_efficiency_acceleration_eqtrnposcnt_63d_base_v057_signal,
    f33ea_f33_efficiency_acceleration_atrnratio_63v252_base_v058_signal,
    f33ea_f33_efficiency_acceleration_atrndiff_21m63_base_v059_signal,
    f33ea_f33_efficiency_acceleration_atrndiff_63m252_base_v060_signal,
    f33ea_f33_efficiency_acceleration_eqtrndiff_21m63_base_v061_signal,
    f33ea_f33_efficiency_acceleration_eqtrndiff_63m252_base_v062_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxebitda_21d_base_v063_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxebitda_252d_base_v064_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxwc_63d_base_v065_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxwc_252d_base_v066_signal,
    f33ea_f33_efficiency_acceleration_roaxlevel_21d_base_v067_signal,
    f33ea_f33_efficiency_acceleration_roexlevel_63d_base_v068_signal,
    f33ea_f33_efficiency_acceleration_roaxasset_252d_base_v069_signal,
    f33ea_f33_efficiency_acceleration_effcompose_21d_base_v070_signal,
    f33ea_f33_efficiency_acceleration_effcompose_252d_base_v071_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxeps_63d_base_v072_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxeps_252d_base_v073_signal,
    f33ea_f33_efficiency_acceleration_atrnaccelxlev_63d_base_v074_signal,
    f33ea_f33_efficiency_acceleration_eqtrnaccelxlev_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_EFFICIENCY_ACCELERATION_REGISTRY_001_075 = REGISTRY


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
        "equity": equity, "assets": assets, "ebitda": ebitda,
        "capex": capex, "eps": eps, "sharesbas": sharesbas, "ncfo": ncfo,
        "opinc": opinc, "gp": gp, "workingcapital": workingcapital,
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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f33_efficiency_acceleration_base_001_075_claude: {n_features} features pass")
