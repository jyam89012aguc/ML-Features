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
def _f32_leverage_accel_de(debt, equity, w):
    de = debt / equity.replace(0, np.nan)
    g = _diff(de, w) / de.shift(w).abs().replace(0, np.nan)
    return _diff(g, w)


def _f32_leverage_accel_debt(debt, w):
    g = _diff(debt, w) / debt.shift(w).abs().replace(0, np.nan)
    return _diff(g, w)


def _f32_leverage_accel_growth(s, w):
    g = _diff(s, w) / s.shift(w).abs().replace(0, np.nan)
    return _diff(g, w)


# 21d acceleration of debt/equity ratio
def f32la_f32_leverage_acceleration_deaccel_21d_base_v001_signal(debt, equity, closeadj):
    result = _f32_leverage_accel_de(debt, equity, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of debt/equity ratio
def f32la_f32_leverage_acceleration_deaccel_63d_base_v002_signal(debt, equity, closeadj):
    result = _f32_leverage_accel_de(debt, equity, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d acceleration of debt/equity ratio
def f32la_f32_leverage_acceleration_deaccel_126d_base_v003_signal(debt, equity, closeadj):
    result = _f32_leverage_accel_de(debt, equity, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of debt/equity ratio
def f32la_f32_leverage_acceleration_deaccel_252d_base_v004_signal(debt, equity, closeadj):
    result = _f32_leverage_accel_de(debt, equity, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d acceleration of total debt
def f32la_f32_leverage_acceleration_debtaccel_21d_base_v005_signal(debt, closeadj):
    result = _f32_leverage_accel_debt(debt, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of total debt
def f32la_f32_leverage_acceleration_debtaccel_63d_base_v006_signal(debt, closeadj):
    result = _f32_leverage_accel_debt(debt, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 126d acceleration of total debt
def f32la_f32_leverage_acceleration_debtaccel_126d_base_v007_signal(debt, closeadj):
    result = _f32_leverage_accel_debt(debt, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of total debt
def f32la_f32_leverage_acceleration_debtaccel_252d_base_v008_signal(debt, closeadj):
    result = _f32_leverage_accel_debt(debt, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d acceleration of liabilities
def f32la_f32_leverage_acceleration_liabaccel_21d_base_v009_signal(liabilities, closeadj):
    result = _f32_leverage_accel_growth(liabilities, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of liabilities
def f32la_f32_leverage_acceleration_liabaccel_63d_base_v010_signal(liabilities, closeadj):
    result = _f32_leverage_accel_growth(liabilities, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of liabilities
def f32la_f32_leverage_acceleration_liabaccel_252d_base_v011_signal(liabilities, closeadj):
    result = _f32_leverage_accel_growth(liabilities, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d acceleration of debt/assets ratio
def f32la_f32_leverage_acceleration_dataccel_21d_base_v012_signal(debt, assets, closeadj):
    s = debt / assets.replace(0, np.nan)
    result = _f32_leverage_accel_growth(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of debt/assets ratio
def f32la_f32_leverage_acceleration_dataccel_63d_base_v013_signal(debt, assets, closeadj):
    s = debt / assets.replace(0, np.nan)
    result = _f32_leverage_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of debt/assets ratio
def f32la_f32_leverage_acceleration_dataccel_252d_base_v014_signal(debt, assets, closeadj):
    s = debt / assets.replace(0, np.nan)
    result = _f32_leverage_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d acceleration of debt/EBITDA ratio
def f32la_f32_leverage_acceleration_debitebitdaaccel_21d_base_v015_signal(debt, ebitda, closeadj):
    s = debt / ebitda.replace(0, np.nan)
    result = _f32_leverage_accel_growth(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of debt/EBITDA ratio
def f32la_f32_leverage_acceleration_debitebitdaaccel_63d_base_v016_signal(debt, ebitda, closeadj):
    s = debt / ebitda.replace(0, np.nan)
    result = _f32_leverage_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of debt/EBITDA ratio
def f32la_f32_leverage_acceleration_debitebitdaaccel_252d_base_v017_signal(debt, ebitda, closeadj):
    s = debt / ebitda.replace(0, np.nan)
    result = _f32_leverage_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d D/E accel rolling mean over 63d
def f32la_f32_leverage_acceleration_deaccelmean_63d_base_v018_signal(debt, equity, closeadj):
    result = _mean(_f32_leverage_accel_de(debt, equity, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d D/E accel rolling mean over 126d
def f32la_f32_leverage_acceleration_deaccelmean_126d_base_v019_signal(debt, equity, closeadj):
    result = _mean(_f32_leverage_accel_de(debt, equity, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt accel rolling mean over 63d
def f32la_f32_leverage_acceleration_debtaccelmean_63d_base_v020_signal(debt, closeadj):
    result = _mean(_f32_leverage_accel_debt(debt, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt accel rolling mean over 126d
def f32la_f32_leverage_acceleration_debtaccelmean_126d_base_v021_signal(debt, closeadj):
    result = _mean(_f32_leverage_accel_debt(debt, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d D/E accel rolling std
def f32la_f32_leverage_acceleration_deaccelstd_63d_base_v022_signal(debt, equity, closeadj):
    result = _std(_f32_leverage_accel_de(debt, equity, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d D/E accel rolling std
def f32la_f32_leverage_acceleration_deaccelstd_252d_base_v023_signal(debt, equity, closeadj):
    result = _std(_f32_leverage_accel_de(debt, equity, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt accel rolling std
def f32la_f32_leverage_acceleration_debtaccelstd_63d_base_v024_signal(debt, closeadj):
    result = _std(_f32_leverage_accel_debt(debt, 63), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt accel rolling std
def f32la_f32_leverage_acceleration_debtaccelstd_252d_base_v025_signal(debt, closeadj):
    result = _std(_f32_leverage_accel_debt(debt, 252), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d D/E accel zscore
def f32la_f32_leverage_acceleration_deaccelz_252d_base_v026_signal(debt, equity, closeadj):
    result = _z(_f32_leverage_accel_de(debt, equity, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt accel zscore
def f32la_f32_leverage_acceleration_debtaccelz_252d_base_v027_signal(debt, closeadj):
    result = _z(_f32_leverage_accel_debt(debt, 63), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d D/E accel zscore
def f32la_f32_leverage_acceleration_deaccelz_504d_base_v028_signal(debt, equity, closeadj):
    result = _z(_f32_leverage_accel_de(debt, equity, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d debt accel zscore
def f32la_f32_leverage_acceleration_debtaccelz_504d_base_v029_signal(debt, closeadj):
    result = _z(_f32_leverage_accel_debt(debt, 252), 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d acceleration of debt per share
def f32la_f32_leverage_acceleration_debtps_21d_base_v030_signal(debt, sharesbas, closeadj):
    dps = debt / sharesbas.replace(0, np.nan)
    result = _f32_leverage_accel_growth(dps, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of debt per share
def f32la_f32_leverage_acceleration_debtps_63d_base_v031_signal(debt, sharesbas, closeadj):
    dps = debt / sharesbas.replace(0, np.nan)
    result = _f32_leverage_accel_growth(dps, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of debt per share
def f32la_f32_leverage_acceleration_debtps_252d_base_v032_signal(debt, sharesbas, closeadj):
    dps = debt / sharesbas.replace(0, np.nan)
    result = _f32_leverage_accel_growth(dps, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of debt/revenue
def f32la_f32_leverage_acceleration_debttorev_63d_base_v033_signal(debt, revenue, closeadj):
    s = debt / revenue.replace(0, np.nan)
    result = _f32_leverage_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of debt/revenue
def f32la_f32_leverage_acceleration_debttorev_252d_base_v034_signal(debt, revenue, closeadj):
    s = debt / revenue.replace(0, np.nan)
    result = _f32_leverage_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of liabilities/equity
def f32la_f32_leverage_acceleration_liabtoeq_63d_base_v035_signal(liabilities, equity, closeadj):
    s = liabilities / equity.replace(0, np.nan)
    result = _f32_leverage_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of liabilities/equity
def f32la_f32_leverage_acceleration_liabtoeq_252d_base_v036_signal(liabilities, equity, closeadj):
    s = liabilities / equity.replace(0, np.nan)
    result = _f32_leverage_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of liabilities/assets
def f32la_f32_leverage_acceleration_liabtoasset_63d_base_v037_signal(liabilities, assets, closeadj):
    s = liabilities / assets.replace(0, np.nan)
    result = _f32_leverage_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of liabilities/assets
def f32la_f32_leverage_acceleration_liabtoasset_252d_base_v038_signal(liabilities, assets, closeadj):
    s = liabilities / assets.replace(0, np.nan)
    result = _f32_leverage_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of debt/FCF
def f32la_f32_leverage_acceleration_debttofcf_63d_base_v039_signal(debt, fcf, closeadj):
    s = debt / fcf.replace(0, np.nan)
    result = _f32_leverage_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of debt/FCF
def f32la_f32_leverage_acceleration_debttofcf_252d_base_v040_signal(debt, fcf, closeadj):
    s = debt / fcf.replace(0, np.nan)
    result = _f32_leverage_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of debt/NCFO
def f32la_f32_leverage_acceleration_debttoncfo_63d_base_v041_signal(debt, ncfo, closeadj):
    s = debt / ncfo.replace(0, np.nan)
    result = _f32_leverage_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of debt/NCFO
def f32la_f32_leverage_acceleration_debttoncfo_252d_base_v042_signal(debt, ncfo, closeadj):
    s = debt / ncfo.replace(0, np.nan)
    result = _f32_leverage_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of intexp/ebitda (interest burden accel)
def f32la_f32_leverage_acceleration_intebitda_63d_base_v043_signal(intexp, ebitda, closeadj):
    s = intexp / ebitda.replace(0, np.nan)
    result = _f32_leverage_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of intexp/ebitda
def f32la_f32_leverage_acceleration_intebitda_252d_base_v044_signal(intexp, ebitda, closeadj):
    s = intexp / ebitda.replace(0, np.nan)
    result = _f32_leverage_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d D/E accel × current D/E
def f32la_f32_leverage_acceleration_deaccelxlevel_63d_base_v045_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    de = debt / equity.replace(0, np.nan)
    result = a * de * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d D/E accel × current D/E
def f32la_f32_leverage_acceleration_deaccelxlevel_252d_base_v046_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 252)
    de = debt / equity.replace(0, np.nan)
    result = a * de * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt accel × current debt
def f32la_f32_leverage_acceleration_debtaccelxlevel_63d_base_v047_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 63)
    result = a * debt.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt accel × current debt
def f32la_f32_leverage_acceleration_debtaccelxlevel_252d_base_v048_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 252)
    result = a * debt.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt accel × current ratio
def f32la_f32_leverage_acceleration_debtaccelxcur_63d_base_v049_signal(debt, currentratio, closeadj):
    a = _f32_leverage_accel_debt(debt, 63)
    result = a * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt accel × current ratio
def f32la_f32_leverage_acceleration_debtaccelxcur_252d_base_v050_signal(debt, currentratio, closeadj):
    a = _f32_leverage_accel_debt(debt, 252)
    result = a * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt minus equity acceleration
def f32la_f32_leverage_acceleration_dminuseaccel_21d_base_v051_signal(debt, equity, closeadj):
    s = debt - equity
    result = _f32_leverage_accel_growth(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt minus equity acceleration
def f32la_f32_leverage_acceleration_dminuseaccel_63d_base_v052_signal(debt, equity, closeadj):
    s = debt - equity
    result = _f32_leverage_accel_growth(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt minus equity acceleration
def f32la_f32_leverage_acceleration_dminuseaccel_252d_base_v053_signal(debt, equity, closeadj):
    s = debt - equity
    result = _f32_leverage_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of days D/E accel > 0
def f32la_f32_leverage_acceleration_deposcnt_63d_base_v054_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 21)
    result = (a).rolling(63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days D/E accel > 0
def f32la_f32_leverage_acceleration_deposcnt_252d_base_v055_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 21)
    result = (a).rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days debt accel > 0
def f32la_f32_leverage_acceleration_debtposcnt_252d_base_v056_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 21)
    result = (a).rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d count of days debt accel > 0
def f32la_f32_leverage_acceleration_debtposcnt_63d_base_v057_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 21)
    result = (a).rolling(63, min_periods=21).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d D/E accel ratio (63d / 252d)
def f32la_f32_leverage_acceleration_deaccelratio_63v252_base_v058_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    b = _f32_leverage_accel_de(debt, equity, 252).replace(0, np.nan)
    result = a / b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d D/E accel - 63d D/E accel
def f32la_f32_leverage_acceleration_deacceldiff_21m63_base_v059_signal(debt, equity, closeadj):
    result = (_f32_leverage_accel_de(debt, equity, 21) - _f32_leverage_accel_de(debt, equity, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d D/E accel - 252d D/E accel
def f32la_f32_leverage_acceleration_deacceldiff_63m252_base_v060_signal(debt, equity, closeadj):
    result = (_f32_leverage_accel_de(debt, equity, 63) - _f32_leverage_accel_de(debt, equity, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt accel - 63d debt accel
def f32la_f32_leverage_acceleration_debtacceldiff_21m63_base_v061_signal(debt, closeadj):
    result = (_f32_leverage_accel_debt(debt, 21) - _f32_leverage_accel_debt(debt, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt accel - 252d debt accel
def f32la_f32_leverage_acceleration_debtacceldiff_63m252_base_v062_signal(debt, closeadj):
    result = (_f32_leverage_accel_debt(debt, 63) - _f32_leverage_accel_debt(debt, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d debt accel × intexp
def f32la_f32_leverage_acceleration_debtaccelxint_21d_base_v063_signal(debt, intexp, closeadj):
    result = _f32_leverage_accel_debt(debt, 21) * intexp.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt accel × intexp
def f32la_f32_leverage_acceleration_debtaccelxint_252d_base_v064_signal(debt, intexp, closeadj):
    result = _f32_leverage_accel_debt(debt, 252) * intexp.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt accel × workingcapital
def f32la_f32_leverage_acceleration_debtaccelxwc_63d_base_v065_signal(debt, workingcapital, closeadj):
    a = _f32_leverage_accel_debt(debt, 63)
    wc = _diff(workingcapital, 63)
    result = a * wc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d debt accel × workingcapital
def f32la_f32_leverage_acceleration_debtaccelxwc_252d_base_v066_signal(debt, workingcapital, closeadj):
    a = _f32_leverage_accel_debt(debt, 252)
    wc = _diff(workingcapital, 252)
    result = a * wc * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d acceleration of equity (deleverage)
def f32la_f32_leverage_acceleration_eqaccel_21d_base_v067_signal(equity, closeadj):
    result = _f32_leverage_accel_growth(equity, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d acceleration of equity
def f32la_f32_leverage_acceleration_eqaccel_63d_base_v068_signal(equity, closeadj):
    result = _f32_leverage_accel_growth(equity, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d acceleration of equity
def f32la_f32_leverage_acceleration_eqaccel_252d_base_v069_signal(equity, closeadj):
    result = _f32_leverage_accel_growth(equity, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite leverage accel: debt + liabilities
def f32la_f32_leverage_acceleration_levcompose_21d_base_v070_signal(debt, liabilities, closeadj):
    s = debt + liabilities
    result = _f32_leverage_accel_growth(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite leverage accel
def f32la_f32_leverage_acceleration_levcompose_252d_base_v071_signal(debt, liabilities, closeadj):
    s = debt + liabilities
    result = _f32_leverage_accel_growth(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d D/E accel × eps magnitude
def f32la_f32_leverage_acceleration_deaccelxeps_63d_base_v072_signal(debt, equity, eps, closeadj):
    result = _f32_leverage_accel_de(debt, equity, 63) * eps.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d D/E accel × eps magnitude
def f32la_f32_leverage_acceleration_deaccelxeps_252d_base_v073_signal(debt, equity, eps, closeadj):
    result = _f32_leverage_accel_de(debt, equity, 252) * eps.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d debt accel × current debt
def f32la_f32_leverage_acceleration_debtaccelxlev_63d_base_v074_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 63)
    result = a * debt.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d liab accel × liab level
def f32la_f32_leverage_acceleration_liabaccelxlev_252d_base_v075_signal(liabilities, closeadj):
    a = _f32_leverage_accel_growth(liabilities, 252)
    result = a * liabilities.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f32la_f32_leverage_acceleration_deaccel_21d_base_v001_signal,
    f32la_f32_leverage_acceleration_deaccel_63d_base_v002_signal,
    f32la_f32_leverage_acceleration_deaccel_126d_base_v003_signal,
    f32la_f32_leverage_acceleration_deaccel_252d_base_v004_signal,
    f32la_f32_leverage_acceleration_debtaccel_21d_base_v005_signal,
    f32la_f32_leverage_acceleration_debtaccel_63d_base_v006_signal,
    f32la_f32_leverage_acceleration_debtaccel_126d_base_v007_signal,
    f32la_f32_leverage_acceleration_debtaccel_252d_base_v008_signal,
    f32la_f32_leverage_acceleration_liabaccel_21d_base_v009_signal,
    f32la_f32_leverage_acceleration_liabaccel_63d_base_v010_signal,
    f32la_f32_leverage_acceleration_liabaccel_252d_base_v011_signal,
    f32la_f32_leverage_acceleration_dataccel_21d_base_v012_signal,
    f32la_f32_leverage_acceleration_dataccel_63d_base_v013_signal,
    f32la_f32_leverage_acceleration_dataccel_252d_base_v014_signal,
    f32la_f32_leverage_acceleration_debitebitdaaccel_21d_base_v015_signal,
    f32la_f32_leverage_acceleration_debitebitdaaccel_63d_base_v016_signal,
    f32la_f32_leverage_acceleration_debitebitdaaccel_252d_base_v017_signal,
    f32la_f32_leverage_acceleration_deaccelmean_63d_base_v018_signal,
    f32la_f32_leverage_acceleration_deaccelmean_126d_base_v019_signal,
    f32la_f32_leverage_acceleration_debtaccelmean_63d_base_v020_signal,
    f32la_f32_leverage_acceleration_debtaccelmean_126d_base_v021_signal,
    f32la_f32_leverage_acceleration_deaccelstd_63d_base_v022_signal,
    f32la_f32_leverage_acceleration_deaccelstd_252d_base_v023_signal,
    f32la_f32_leverage_acceleration_debtaccelstd_63d_base_v024_signal,
    f32la_f32_leverage_acceleration_debtaccelstd_252d_base_v025_signal,
    f32la_f32_leverage_acceleration_deaccelz_252d_base_v026_signal,
    f32la_f32_leverage_acceleration_debtaccelz_252d_base_v027_signal,
    f32la_f32_leverage_acceleration_deaccelz_504d_base_v028_signal,
    f32la_f32_leverage_acceleration_debtaccelz_504d_base_v029_signal,
    f32la_f32_leverage_acceleration_debtps_21d_base_v030_signal,
    f32la_f32_leverage_acceleration_debtps_63d_base_v031_signal,
    f32la_f32_leverage_acceleration_debtps_252d_base_v032_signal,
    f32la_f32_leverage_acceleration_debttorev_63d_base_v033_signal,
    f32la_f32_leverage_acceleration_debttorev_252d_base_v034_signal,
    f32la_f32_leverage_acceleration_liabtoeq_63d_base_v035_signal,
    f32la_f32_leverage_acceleration_liabtoeq_252d_base_v036_signal,
    f32la_f32_leverage_acceleration_liabtoasset_63d_base_v037_signal,
    f32la_f32_leverage_acceleration_liabtoasset_252d_base_v038_signal,
    f32la_f32_leverage_acceleration_debttofcf_63d_base_v039_signal,
    f32la_f32_leverage_acceleration_debttofcf_252d_base_v040_signal,
    f32la_f32_leverage_acceleration_debttoncfo_63d_base_v041_signal,
    f32la_f32_leverage_acceleration_debttoncfo_252d_base_v042_signal,
    f32la_f32_leverage_acceleration_intebitda_63d_base_v043_signal,
    f32la_f32_leverage_acceleration_intebitda_252d_base_v044_signal,
    f32la_f32_leverage_acceleration_deaccelxlevel_63d_base_v045_signal,
    f32la_f32_leverage_acceleration_deaccelxlevel_252d_base_v046_signal,
    f32la_f32_leverage_acceleration_debtaccelxlevel_63d_base_v047_signal,
    f32la_f32_leverage_acceleration_debtaccelxlevel_252d_base_v048_signal,
    f32la_f32_leverage_acceleration_debtaccelxcur_63d_base_v049_signal,
    f32la_f32_leverage_acceleration_debtaccelxcur_252d_base_v050_signal,
    f32la_f32_leverage_acceleration_dminuseaccel_21d_base_v051_signal,
    f32la_f32_leverage_acceleration_dminuseaccel_63d_base_v052_signal,
    f32la_f32_leverage_acceleration_dminuseaccel_252d_base_v053_signal,
    f32la_f32_leverage_acceleration_deposcnt_63d_base_v054_signal,
    f32la_f32_leverage_acceleration_deposcnt_252d_base_v055_signal,
    f32la_f32_leverage_acceleration_debtposcnt_252d_base_v056_signal,
    f32la_f32_leverage_acceleration_debtposcnt_63d_base_v057_signal,
    f32la_f32_leverage_acceleration_deaccelratio_63v252_base_v058_signal,
    f32la_f32_leverage_acceleration_deacceldiff_21m63_base_v059_signal,
    f32la_f32_leverage_acceleration_deacceldiff_63m252_base_v060_signal,
    f32la_f32_leverage_acceleration_debtacceldiff_21m63_base_v061_signal,
    f32la_f32_leverage_acceleration_debtacceldiff_63m252_base_v062_signal,
    f32la_f32_leverage_acceleration_debtaccelxint_21d_base_v063_signal,
    f32la_f32_leverage_acceleration_debtaccelxint_252d_base_v064_signal,
    f32la_f32_leverage_acceleration_debtaccelxwc_63d_base_v065_signal,
    f32la_f32_leverage_acceleration_debtaccelxwc_252d_base_v066_signal,
    f32la_f32_leverage_acceleration_eqaccel_21d_base_v067_signal,
    f32la_f32_leverage_acceleration_eqaccel_63d_base_v068_signal,
    f32la_f32_leverage_acceleration_eqaccel_252d_base_v069_signal,
    f32la_f32_leverage_acceleration_levcompose_21d_base_v070_signal,
    f32la_f32_leverage_acceleration_levcompose_252d_base_v071_signal,
    f32la_f32_leverage_acceleration_deaccelxeps_63d_base_v072_signal,
    f32la_f32_leverage_acceleration_deaccelxeps_252d_base_v073_signal,
    f32la_f32_leverage_acceleration_debtaccelxlev_63d_base_v074_signal,
    f32la_f32_leverage_acceleration_liabaccelxlev_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_LEVERAGE_ACCELERATION_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    fund_walk = lambda mu, sd, base: pd.Series(base * np.exp(np.cumsum(np.random.normal(mu, sd, n))))
    revenue = fund_walk(0.0006, 0.015, 1e8).rename("revenue")
    fcf = fund_walk(0.0005, 0.025, 8e6).rename("fcf")
    equity = fund_walk(0.0004, 0.012, 5e8).rename("equity")
    debt = fund_walk(0.0004, 0.015, 3e8).rename("debt")
    assets = fund_walk(0.0004, 0.012, 1.2e9).rename("assets")
    ebitda = fund_walk(0.0005, 0.018, 2e7).rename("ebitda")
    eps = fund_walk(0.0005, 0.02, 2.0).rename("eps")
    sharesbas = fund_walk(0.0001, 0.005, 1e7).rename("sharesbas")
    ncfo = fund_walk(0.0005, 0.022, 1.5e7).rename("ncfo")
    workingcapital = fund_walk(0.0004, 0.02, 3e7).rename("workingcapital")
    currentratio = fund_walk(0.0001, 0.01, 1.5).rename("currentratio")
    intexp = fund_walk(0.0003, 0.018, 5e6).rename("intexp")
    liabilities = fund_walk(0.0004, 0.012, 7e8).rename("liabilities")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "fcf": fcf,
        "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda,
        "eps": eps, "sharesbas": sharesbas, "ncfo": ncfo,
        "workingcapital": workingcapital, "currentratio": currentratio,
        "intexp": intexp, "liabilities": liabilities,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f32_leverage_accel_de", "_f32_leverage_accel_debt", "_f32_leverage_accel_growth")
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
    print(f"OK f32_leverage_acceleration_base_001_075_claude: {n_features} features pass")
