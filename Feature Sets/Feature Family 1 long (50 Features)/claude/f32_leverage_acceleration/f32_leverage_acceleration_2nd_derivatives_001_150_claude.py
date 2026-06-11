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


# 5d slope of 21d D/E acceleration × close
def f32la_f32_leverage_acceleration_deaccel_21d_slope_v001_signal(debt, equity, closeadj):
    base = _f32_leverage_accel_de(debt, equity, 21) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d D/E acceleration × close
def f32la_f32_leverage_acceleration_deaccel_21d_slope_v002_signal(debt, equity, closeadj):
    base = _f32_leverage_accel_de(debt, equity, 21) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 63d D/E acceleration × close
def f32la_f32_leverage_acceleration_deaccel_63d_slope_v003_signal(debt, equity, closeadj):
    base = _f32_leverage_accel_de(debt, equity, 63) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d D/E acceleration × close
def f32la_f32_leverage_acceleration_deaccel_63d_slope_v004_signal(debt, equity, closeadj):
    base = _f32_leverage_accel_de(debt, equity, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d D/E acceleration × close
def f32la_f32_leverage_acceleration_deaccel_63d_slope_v005_signal(debt, equity, closeadj):
    base = _f32_leverage_accel_de(debt, equity, 63) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 126d D/E acceleration × close
def f32la_f32_leverage_acceleration_deaccel_126d_slope_v006_signal(debt, equity, closeadj):
    base = _f32_leverage_accel_de(debt, equity, 126) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d D/E acceleration × close
def f32la_f32_leverage_acceleration_deaccel_126d_slope_v007_signal(debt, equity, closeadj):
    base = _f32_leverage_accel_de(debt, equity, 126) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d D/E acceleration × close
def f32la_f32_leverage_acceleration_deaccel_252d_slope_v008_signal(debt, equity, closeadj):
    base = _f32_leverage_accel_de(debt, equity, 252) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d D/E acceleration × close
def f32la_f32_leverage_acceleration_deaccel_252d_slope_v009_signal(debt, equity, closeadj):
    base = _f32_leverage_accel_de(debt, equity, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d debt acceleration × close
def f32la_f32_leverage_acceleration_debtaccel_21d_slope_v010_signal(debt, closeadj):
    base = _f32_leverage_accel_debt(debt, 21) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 21d debt acceleration × close
def f32la_f32_leverage_acceleration_debtaccel_21d_slope_v011_signal(debt, closeadj):
    base = _f32_leverage_accel_debt(debt, 21) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d debt acceleration × close
def f32la_f32_leverage_acceleration_debtaccel_63d_slope_v012_signal(debt, closeadj):
    base = _f32_leverage_accel_debt(debt, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 63d debt acceleration × close
def f32la_f32_leverage_acceleration_debtaccel_63d_slope_v013_signal(debt, closeadj):
    base = _f32_leverage_accel_debt(debt, 63) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 126d debt acceleration × close
def f32la_f32_leverage_acceleration_debtaccel_126d_slope_v014_signal(debt, closeadj):
    base = _f32_leverage_accel_debt(debt, 126) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d debt acceleration × close
def f32la_f32_leverage_acceleration_debtaccel_252d_slope_v015_signal(debt, closeadj):
    base = _f32_leverage_accel_debt(debt, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d liab acceleration × close
def f32la_f32_leverage_acceleration_liabaccel_21d_slope_v016_signal(liabilities, closeadj):
    base = _f32_leverage_accel_growth(liabilities, 21) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d liab acceleration × close
def f32la_f32_leverage_acceleration_liabaccel_63d_slope_v017_signal(liabilities, closeadj):
    base = _f32_leverage_accel_growth(liabilities, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d liab acceleration × close
def f32la_f32_leverage_acceleration_liabaccel_252d_slope_v018_signal(liabilities, closeadj):
    base = _f32_leverage_accel_growth(liabilities, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d debt/asset acceleration × close
def f32la_f32_leverage_acceleration_dataccel_21d_slope_v019_signal(debt, assets, closeadj):
    s = debt / assets.replace(0, np.nan)
    base = _f32_leverage_accel_growth(s, 21) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d debt/asset acceleration × close
def f32la_f32_leverage_acceleration_dataccel_63d_slope_v020_signal(debt, assets, closeadj):
    s = debt / assets.replace(0, np.nan)
    base = _f32_leverage_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d debt/asset acceleration × close
def f32la_f32_leverage_acceleration_dataccel_252d_slope_v021_signal(debt, assets, closeadj):
    s = debt / assets.replace(0, np.nan)
    base = _f32_leverage_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d debt/EBITDA accel × close
def f32la_f32_leverage_acceleration_debitebitdaaccel_21d_slope_v022_signal(debt, ebitda, closeadj):
    s = debt / ebitda.replace(0, np.nan)
    base = _f32_leverage_accel_growth(s, 21) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d debt/EBITDA accel × close
def f32la_f32_leverage_acceleration_debitebitdaaccel_63d_slope_v023_signal(debt, ebitda, closeadj):
    s = debt / ebitda.replace(0, np.nan)
    base = _f32_leverage_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d debt/EBITDA accel × close
def f32la_f32_leverage_acceleration_debitebitdaaccel_252d_slope_v024_signal(debt, ebitda, closeadj):
    s = debt / ebitda.replace(0, np.nan)
    base = _f32_leverage_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d D/E accel mean
def f32la_f32_leverage_acceleration_deaccelmean_63d_slope_v025_signal(debt, equity, closeadj):
    base = _mean(_f32_leverage_accel_de(debt, equity, 63), 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d D/E accel mean
def f32la_f32_leverage_acceleration_deaccelmean_126d_slope_v026_signal(debt, equity, closeadj):
    base = _mean(_f32_leverage_accel_de(debt, equity, 252), 126) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d debt accel mean
def f32la_f32_leverage_acceleration_debtaccelmean_63d_slope_v027_signal(debt, closeadj):
    base = _mean(_f32_leverage_accel_debt(debt, 63), 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d debt accel mean
def f32la_f32_leverage_acceleration_debtaccelmean_126d_slope_v028_signal(debt, closeadj):
    base = _mean(_f32_leverage_accel_debt(debt, 252), 126) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d D/E accel std
def f32la_f32_leverage_acceleration_deaccelstd_63d_slope_v029_signal(debt, equity, closeadj):
    base = _std(_f32_leverage_accel_de(debt, equity, 63), 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d D/E accel std
def f32la_f32_leverage_acceleration_deaccelstd_252d_slope_v030_signal(debt, equity, closeadj):
    base = _std(_f32_leverage_accel_de(debt, equity, 252), 126) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d debt accel std
def f32la_f32_leverage_acceleration_debtaccelstd_63d_slope_v031_signal(debt, closeadj):
    base = _std(_f32_leverage_accel_debt(debt, 63), 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d debt accel std
def f32la_f32_leverage_acceleration_debtaccelstd_252d_slope_v032_signal(debt, closeadj):
    base = _std(_f32_leverage_accel_debt(debt, 252), 126) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d D/E accel zscore
def f32la_f32_leverage_acceleration_deaccelz_252d_slope_v033_signal(debt, equity, closeadj):
    base = _z(_f32_leverage_accel_de(debt, equity, 63), 252) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 252d debt accel zscore
def f32la_f32_leverage_acceleration_debtaccelz_252d_slope_v034_signal(debt, closeadj):
    base = _z(_f32_leverage_accel_debt(debt, 63), 252) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d D/E accel zscore
def f32la_f32_leverage_acceleration_deaccelz_504d_slope_v035_signal(debt, equity, closeadj):
    base = _z(_f32_leverage_accel_de(debt, equity, 252), 504) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 504d debt accel zscore
def f32la_f32_leverage_acceleration_debtaccelz_504d_slope_v036_signal(debt, closeadj):
    base = _z(_f32_leverage_accel_debt(debt, 252), 504) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d debt per share accel
def f32la_f32_leverage_acceleration_debtps_21d_slope_v037_signal(debt, sharesbas, closeadj):
    dps = debt / sharesbas.replace(0, np.nan)
    base = _f32_leverage_accel_growth(dps, 21) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d debt per share accel
def f32la_f32_leverage_acceleration_debtps_63d_slope_v038_signal(debt, sharesbas, closeadj):
    dps = debt / sharesbas.replace(0, np.nan)
    base = _f32_leverage_accel_growth(dps, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d debt per share accel
def f32la_f32_leverage_acceleration_debtps_252d_slope_v039_signal(debt, sharesbas, closeadj):
    dps = debt / sharesbas.replace(0, np.nan)
    base = _f32_leverage_accel_growth(dps, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d debt/revenue accel
def f32la_f32_leverage_acceleration_debttorev_63d_slope_v040_signal(debt, revenue, closeadj):
    s = debt / revenue.replace(0, np.nan)
    base = _f32_leverage_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d debt/revenue accel
def f32la_f32_leverage_acceleration_debttorev_252d_slope_v041_signal(debt, revenue, closeadj):
    s = debt / revenue.replace(0, np.nan)
    base = _f32_leverage_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d liab/eq accel
def f32la_f32_leverage_acceleration_liabtoeq_63d_slope_v042_signal(liabilities, equity, closeadj):
    s = liabilities / equity.replace(0, np.nan)
    base = _f32_leverage_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d liab/eq accel
def f32la_f32_leverage_acceleration_liabtoeq_252d_slope_v043_signal(liabilities, equity, closeadj):
    s = liabilities / equity.replace(0, np.nan)
    base = _f32_leverage_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d liab/asset accel
def f32la_f32_leverage_acceleration_liabtoasset_63d_slope_v044_signal(liabilities, assets, closeadj):
    s = liabilities / assets.replace(0, np.nan)
    base = _f32_leverage_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d liab/asset accel
def f32la_f32_leverage_acceleration_liabtoasset_252d_slope_v045_signal(liabilities, assets, closeadj):
    s = liabilities / assets.replace(0, np.nan)
    base = _f32_leverage_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d debt/FCF accel
def f32la_f32_leverage_acceleration_debttofcf_63d_slope_v046_signal(debt, fcf, closeadj):
    s = debt / fcf.replace(0, np.nan)
    base = _f32_leverage_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d debt/FCF accel
def f32la_f32_leverage_acceleration_debttofcf_252d_slope_v047_signal(debt, fcf, closeadj):
    s = debt / fcf.replace(0, np.nan)
    base = _f32_leverage_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d debt/NCFO accel
def f32la_f32_leverage_acceleration_debttoncfo_63d_slope_v048_signal(debt, ncfo, closeadj):
    s = debt / ncfo.replace(0, np.nan)
    base = _f32_leverage_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d debt/NCFO accel
def f32la_f32_leverage_acceleration_debttoncfo_252d_slope_v049_signal(debt, ncfo, closeadj):
    s = debt / ncfo.replace(0, np.nan)
    base = _f32_leverage_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d intexp/ebitda accel
def f32la_f32_leverage_acceleration_intebitda_63d_slope_v050_signal(intexp, ebitda, closeadj):
    s = intexp / ebitda.replace(0, np.nan)
    base = _f32_leverage_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d intexp/ebitda accel
def f32la_f32_leverage_acceleration_intebitda_252d_slope_v051_signal(intexp, ebitda, closeadj):
    s = intexp / ebitda.replace(0, np.nan)
    base = _f32_leverage_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d D/E accel × level
def f32la_f32_leverage_acceleration_deaccelxlevel_63d_slope_v052_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    de = debt / equity.replace(0, np.nan)
    base = a * de * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d D/E accel × level
def f32la_f32_leverage_acceleration_deaccelxlevel_252d_slope_v053_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 252)
    de = debt / equity.replace(0, np.nan)
    base = a * de * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d debt accel × level
def f32la_f32_leverage_acceleration_debtaccelxlevel_63d_slope_v054_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 63)
    base = a * debt.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d debt accel × level
def f32la_f32_leverage_acceleration_debtaccelxlevel_252d_slope_v055_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 252)
    base = a * debt.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d debt accel × current ratio
def f32la_f32_leverage_acceleration_debtaccelxcur_63d_slope_v056_signal(debt, currentratio, closeadj):
    a = _f32_leverage_accel_debt(debt, 63)
    base = a * currentratio * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d debt accel × current ratio
def f32la_f32_leverage_acceleration_debtaccelxcur_252d_slope_v057_signal(debt, currentratio, closeadj):
    a = _f32_leverage_accel_debt(debt, 252)
    base = a * currentratio * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d debt-equity accel
def f32la_f32_leverage_acceleration_dminuseaccel_21d_slope_v058_signal(debt, equity, closeadj):
    s = debt - equity
    base = _f32_leverage_accel_growth(s, 21) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d debt-equity accel
def f32la_f32_leverage_acceleration_dminuseaccel_63d_slope_v059_signal(debt, equity, closeadj):
    s = debt - equity
    base = _f32_leverage_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d debt-equity accel
def f32la_f32_leverage_acceleration_dminuseaccel_252d_slope_v060_signal(debt, equity, closeadj):
    s = debt - equity
    base = _f32_leverage_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d D/E accel pos count
def f32la_f32_leverage_acceleration_deposcnt_63d_slope_v061_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 21)
    base = (a).rolling(63, min_periods=21).mean() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d D/E accel pos count
def f32la_f32_leverage_acceleration_deposcnt_252d_slope_v062_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 21)
    base = (a).rolling(252, min_periods=63).mean() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d debt accel pos count
def f32la_f32_leverage_acceleration_debtposcnt_252d_slope_v063_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 21)
    base = (a).rolling(252, min_periods=63).mean() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d debt accel pos count
def f32la_f32_leverage_acceleration_debtposcnt_63d_slope_v064_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 21)
    base = (a).rolling(63, min_periods=21).mean() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of D/E accel ratio 63v252
def f32la_f32_leverage_acceleration_deaccelratio_63v252_slope_v065_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    b = _f32_leverage_accel_de(debt, equity, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of D/E accel diff 21m63
def f32la_f32_leverage_acceleration_deacceldiff_21m63_slope_v066_signal(debt, equity, closeadj):
    base = (_f32_leverage_accel_de(debt, equity, 21) - _f32_leverage_accel_de(debt, equity, 63)) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of D/E accel diff 63m252
def f32la_f32_leverage_acceleration_deacceldiff_63m252_slope_v067_signal(debt, equity, closeadj):
    base = (_f32_leverage_accel_de(debt, equity, 63) - _f32_leverage_accel_de(debt, equity, 252)) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of debt accel diff 21m63
def f32la_f32_leverage_acceleration_debtacceldiff_21m63_slope_v068_signal(debt, closeadj):
    base = (_f32_leverage_accel_debt(debt, 21) - _f32_leverage_accel_debt(debt, 63)) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of debt accel diff 63m252
def f32la_f32_leverage_acceleration_debtacceldiff_63m252_slope_v069_signal(debt, closeadj):
    base = (_f32_leverage_accel_debt(debt, 63) - _f32_leverage_accel_debt(debt, 252)) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d debt accel × intexp
def f32la_f32_leverage_acceleration_debtaccelxint_21d_slope_v070_signal(debt, intexp, closeadj):
    base = _f32_leverage_accel_debt(debt, 21) * intexp.abs() * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d debt accel × intexp
def f32la_f32_leverage_acceleration_debtaccelxint_252d_slope_v071_signal(debt, intexp, closeadj):
    base = _f32_leverage_accel_debt(debt, 252) * intexp.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of debt accel × wc 63d
def f32la_f32_leverage_acceleration_debtaccelxwc_63d_slope_v072_signal(debt, workingcapital, closeadj):
    a = _f32_leverage_accel_debt(debt, 63)
    wc = _diff(workingcapital, 63)
    base = a * wc * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt accel × wc 252d
def f32la_f32_leverage_acceleration_debtaccelxwc_252d_slope_v073_signal(debt, workingcapital, closeadj):
    a = _f32_leverage_accel_debt(debt, 252)
    wc = _diff(workingcapital, 252)
    base = a * wc * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d eq accel
def f32la_f32_leverage_acceleration_eqaccel_21d_slope_v074_signal(equity, closeadj):
    base = _f32_leverage_accel_growth(equity, 21) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d eq accel
def f32la_f32_leverage_acceleration_eqaccel_63d_slope_v075_signal(equity, closeadj):
    base = _f32_leverage_accel_growth(equity, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d eq accel
def f32la_f32_leverage_acceleration_eqaccel_252d_slope_v076_signal(equity, closeadj):
    base = _f32_leverage_accel_growth(equity, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d levcompose accel
def f32la_f32_leverage_acceleration_levcompose_21d_slope_v077_signal(debt, liabilities, closeadj):
    s = debt + liabilities
    base = _f32_leverage_accel_growth(s, 21) * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d levcompose accel
def f32la_f32_leverage_acceleration_levcompose_252d_slope_v078_signal(debt, liabilities, closeadj):
    s = debt + liabilities
    base = _f32_leverage_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of D/E accel × eps 63d
def f32la_f32_leverage_acceleration_deaccelxeps_63d_slope_v079_signal(debt, equity, eps, closeadj):
    base = _f32_leverage_accel_de(debt, equity, 63) * eps.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E accel × eps 252d
def f32la_f32_leverage_acceleration_deaccelxeps_252d_slope_v080_signal(debt, equity, eps, closeadj):
    base = _f32_leverage_accel_de(debt, equity, 252) * eps.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of debt accel × debt level 63d
def f32la_f32_leverage_acceleration_debtaccelxlev_63d_slope_v081_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 63)
    base = a * debt.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of liab accel × liab level 252d
def f32la_f32_leverage_acceleration_liabaccelxlev_252d_slope_v082_signal(liabilities, closeadj):
    a = _f32_leverage_accel_growth(liabilities, 252)
    base = a * liabilities.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of 21d D/E accel × revenue
def f32la_f32_leverage_acceleration_deaccelxrev_21d_slope_v083_signal(debt, equity, revenue, closeadj):
    base = _f32_leverage_accel_de(debt, equity, 21) * revenue.abs() * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d D/E accel × revenue
def f32la_f32_leverage_acceleration_deaccelxrev_252d_slope_v084_signal(debt, equity, revenue, closeadj):
    base = _f32_leverage_accel_de(debt, equity, 252) * revenue.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of D/E accel × current ratio 63d
def f32la_f32_leverage_acceleration_deaccelxcurratio_63d_slope_v085_signal(debt, equity, currentratio, closeadj):
    base = _f32_leverage_accel_de(debt, equity, 63) * currentratio * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E accel × current ratio 252d
def f32la_f32_leverage_acceleration_deaccelxcurratio_252d_slope_v086_signal(debt, equity, currentratio, closeadj):
    base = _f32_leverage_accel_de(debt, equity, 252) * currentratio * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of debt share intensity 63d
def f32la_f32_leverage_acceleration_debtshareintensity_63d_slope_v087_signal(debt, sharesbas, closeadj):
    s = debt / sharesbas.replace(0, np.nan)
    a = _f32_leverage_accel_growth(s, 63)
    base = a * sharesbas * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt share intensity 252d
def f32la_f32_leverage_acceleration_debtshareintensity_252d_slope_v088_signal(debt, sharesbas, closeadj):
    s = debt / sharesbas.replace(0, np.nan)
    a = _f32_leverage_accel_growth(s, 252)
    base = a * sharesbas * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of D/E accel EMA63
def f32la_f32_leverage_acceleration_deaccelema_63d_slope_v089_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 21)
    base = a.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E accel EMA252
def f32la_f32_leverage_acceleration_deaccelema_252d_slope_v090_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    base = a.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of debt accel EMA63
def f32la_f32_leverage_acceleration_debtaccelema_63d_slope_v091_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 21)
    base = a.ewm(span=63, adjust=False).mean() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt accel EMA252
def f32la_f32_leverage_acceleration_debtaccelema_252d_slope_v092_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 63)
    base = a.ewm(span=252, adjust=False).mean() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of D/E accel squared 63d
def f32la_f32_leverage_acceleration_deaccelsq_63d_slope_v093_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    base = a * a.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E accel squared 252d
def f32la_f32_leverage_acceleration_deaccelsq_252d_slope_v094_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 252)
    base = a * a.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of debt accel squared 63d
def f32la_f32_leverage_acceleration_debtaccelsq_63d_slope_v095_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 63)
    base = a * a.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt accel squared 252d
def f32la_f32_leverage_acceleration_debtaccelsq_252d_slope_v096_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 252)
    base = a * a.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d D/E accel area
def f32la_f32_leverage_acceleration_deaccelarea_63d_slope_v097_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 21)
    base = a.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d D/E accel area
def f32la_f32_leverage_acceleration_deaccelarea_252d_slope_v098_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 21)
    base = a.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d debt accel area
def f32la_f32_leverage_acceleration_debtaccelarea_63d_slope_v099_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 21)
    base = a.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d debt accel area
def f32la_f32_leverage_acceleration_debtaccelarea_252d_slope_v100_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 21)
    base = a.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of 63d levcomp accel
def f32la_f32_leverage_acceleration_levaccelcomp_63d_slope_v101_signal(debt, equity, closeadj):
    s = debt + equity
    base = _f32_leverage_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of 252d levcomp accel
def f32la_f32_leverage_acceleration_levaccelcomp_252d_slope_v102_signal(debt, equity, closeadj):
    s = debt + equity
    base = _f32_leverage_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of D/E - debt accel divergence 63d
def f32la_f32_leverage_acceleration_deminusdebt_63d_slope_v103_signal(debt, equity, closeadj):
    base = (_f32_leverage_accel_de(debt, equity, 63) - _f32_leverage_accel_debt(debt, 63)) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E - debt accel divergence 252d
def f32la_f32_leverage_acceleration_deminusdebt_252d_slope_v104_signal(debt, equity, closeadj):
    base = (_f32_leverage_accel_de(debt, equity, 252) - _f32_leverage_accel_debt(debt, 252)) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of D/E accel × revg 63d
def f32la_f32_leverage_acceleration_deaccelxrevg_63d_slope_v105_signal(debt, equity, revenue, closeadj):
    rg = _diff(revenue, 63) / revenue.shift(63).abs().replace(0, np.nan)
    base = _f32_leverage_accel_de(debt, equity, 63) * rg * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E accel × revg 252d
def f32la_f32_leverage_acceleration_deaccelxrevg_252d_slope_v106_signal(debt, equity, revenue, closeadj):
    rg = _diff(revenue, 252) / revenue.shift(252).abs().replace(0, np.nan)
    base = _f32_leverage_accel_de(debt, equity, 252) * rg * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of debt accel × revg 63d
def f32la_f32_leverage_acceleration_debtaccelxrevg_63d_slope_v107_signal(debt, revenue, closeadj):
    rg = _diff(revenue, 63) / revenue.shift(63).abs().replace(0, np.nan)
    base = _f32_leverage_accel_debt(debt, 63) * rg * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt accel × revg 252d
def f32la_f32_leverage_acceleration_debtaccelxrevg_252d_slope_v108_signal(debt, revenue, closeadj):
    rg = _diff(revenue, 252) / revenue.shift(252).abs().replace(0, np.nan)
    base = _f32_leverage_accel_debt(debt, 252) * rg * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d slope of D/E accel × eps growth 21d
def f32la_f32_leverage_acceleration_deaccelxepsg_21d_slope_v109_signal(debt, equity, eps, closeadj):
    eg = _diff(eps, 21) / eps.shift(21).abs().replace(0, np.nan)
    base = _f32_leverage_accel_de(debt, equity, 21) * eg * closeadj
    result = _slope_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E accel × eps growth 252d
def f32la_f32_leverage_acceleration_deaccelxepsg_252d_slope_v110_signal(debt, equity, eps, closeadj):
    eg = _diff(eps, 252) / eps.shift(252).abs().replace(0, np.nan)
    base = _f32_leverage_accel_de(debt, equity, 252) * eg * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of net debt × revenue accel 63d
def f32la_f32_leverage_acceleration_netdebtxrev_63d_slope_v111_signal(debt, ncfo, revenue, closeadj):
    s = (debt - ncfo) / revenue.replace(0, np.nan)
    base = _f32_leverage_accel_growth(s, 63) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of net debt × revenue accel 252d
def f32la_f32_leverage_acceleration_netdebtxrev_252d_slope_v112_signal(debt, ncfo, revenue, closeadj):
    s = (debt - ncfo) / revenue.replace(0, np.nan)
    base = _f32_leverage_accel_growth(s, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of D/E accel × quality 63d
def f32la_f32_leverage_acceleration_deaccelxqual_63d_slope_v113_signal(debt, equity, fcf, ebitda, closeadj):
    q = fcf / ebitda.replace(0, np.nan)
    base = _f32_leverage_accel_de(debt, equity, 63) * q * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E accel × quality 252d
def f32la_f32_leverage_acceleration_deaccelxqual_252d_slope_v114_signal(debt, equity, fcf, ebitda, closeadj):
    q = fcf / ebitda.replace(0, np.nan)
    base = _f32_leverage_accel_de(debt, equity, 252) * q * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of D/E vs debt accel ratio 63d
def f32la_f32_leverage_acceleration_devsdebt_63d_slope_v115_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    b = _f32_leverage_accel_debt(debt, 63).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E vs debt accel ratio 252d
def f32la_f32_leverage_acceleration_devsdebt_252d_slope_v116_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 252)
    b = _f32_leverage_accel_debt(debt, 252).replace(0, np.nan)
    base = (a / b) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E accel rolling 252d mean
def f32la_f32_leverage_acceleration_deaccelxavg_252d_slope_v117_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    base = _mean(a, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt accel rolling 252d mean
def f32la_f32_leverage_acceleration_debtaccelxavg_252d_slope_v118_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 63)
    base = _mean(a, 252) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of D/E accel × equity 63d
def f32la_f32_leverage_acceleration_debttoeqxlevel_63d_slope_v119_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    base = a * equity.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E accel × equity 252d
def f32la_f32_leverage_acceleration_debttoeqxlevel_252d_slope_v120_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 252)
    base = a * equity.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of D/E accel sign sum 63d
def f32la_f32_leverage_acceleration_deaccelsignsum_63d_slope_v121_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 21)
    sg = np.sign(a)
    base = sg.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E accel sign sum 252d
def f32la_f32_leverage_acceleration_deaccelsignsum_252d_slope_v122_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 21)
    sg = np.sign(a)
    base = sg.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of debt accel sign sum 63d
def f32la_f32_leverage_acceleration_debtaccelsignsum_63d_slope_v123_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 21)
    sg = np.sign(a)
    base = sg.rolling(63, min_periods=21).sum() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt accel sign sum 252d
def f32la_f32_leverage_acceleration_debtaccelsignsum_252d_slope_v124_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 21)
    sg = np.sign(a)
    base = sg.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of debt accel × tax 63d
def f32la_f32_leverage_acceleration_debtaccelxtax_63d_slope_v125_signal(debt, taxexp, closeadj):
    base = _f32_leverage_accel_debt(debt, 63) * taxexp.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt accel × tax 252d
def f32la_f32_leverage_acceleration_debtaccelxtax_252d_slope_v126_signal(debt, taxexp, closeadj):
    base = _f32_leverage_accel_debt(debt, 252) * taxexp.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of debt accel × intexp 63d
def f32la_f32_leverage_acceleration_debtaccelxintexp_63d_slope_v127_signal(debt, intexp, closeadj):
    base = _f32_leverage_accel_debt(debt, 63) * intexp.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt accel × intexp 252d
def f32la_f32_leverage_acceleration_debtaccelxintexp_252d_slope_v128_signal(debt, intexp, closeadj):
    base = _f32_leverage_accel_debt(debt, 252) * intexp.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of debt accel × retearn 63d
def f32la_f32_leverage_acceleration_debtaccelxretearn_63d_slope_v129_signal(debt, retearn, closeadj):
    base = _f32_leverage_accel_debt(debt, 63) * retearn.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt accel × retearn 252d
def f32la_f32_leverage_acceleration_debtaccelxretearn_252d_slope_v130_signal(debt, retearn, closeadj):
    base = _f32_leverage_accel_debt(debt, 252) * retearn.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of liab accel × intexp 63d
def f32la_f32_leverage_acceleration_liabaccelxintexp_63d_slope_v131_signal(liabilities, intexp, closeadj):
    base = _f32_leverage_accel_growth(liabilities, 63) * intexp.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of liab accel × intexp 252d
def f32la_f32_leverage_acceleration_liabaccelxintexp_252d_slope_v132_signal(liabilities, intexp, closeadj):
    base = _f32_leverage_accel_growth(liabilities, 252) * intexp.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of debt/sharesbas accel zscore 252d
def f32la_f32_leverage_acceleration_debtpsaccelz_252d_slope_v133_signal(debt, sharesbas, closeadj):
    s = debt / sharesbas.replace(0, np.nan)
    a = _f32_leverage_accel_growth(s, 63)
    base = _z(a, 252) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt/sharesbas accel zscore 504d
def f32la_f32_leverage_acceleration_debtpsaccelz_504d_slope_v134_signal(debt, sharesbas, closeadj):
    s = debt / sharesbas.replace(0, np.nan)
    a = _f32_leverage_accel_growth(s, 252)
    base = _z(a, 504) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of multi-window D/E accel
def f32la_f32_leverage_acceleration_deaccelmulti_slope_v135_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 21)
    b = _f32_leverage_accel_de(debt, equity, 63)
    c = _f32_leverage_accel_de(debt, equity, 252)
    base = (a + b + c) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of multi-window debt accel
def f32la_f32_leverage_acceleration_debtaccelmulti_slope_v136_signal(debt, closeadj):
    a = _f32_leverage_accel_debt(debt, 21)
    b = _f32_leverage_accel_debt(debt, 63)
    c = _f32_leverage_accel_debt(debt, 252)
    base = (a + b + c) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of D/E accel health 63d
def f32la_f32_leverage_acceleration_deaccelhealth_63d_slope_v137_signal(debt, equity, currentratio, revenue, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    base = a * currentratio * revenue.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E accel health 252d
def f32la_f32_leverage_acceleration_deaccelhealth_252d_slope_v138_signal(debt, equity, currentratio, revenue, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 252)
    base = a * currentratio * revenue.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of debt accel × netinc growth 63d
def f32la_f32_leverage_acceleration_debtaccelxnetincg_63d_slope_v139_signal(debt, netinc, closeadj):
    ng = _diff(netinc, 63) / netinc.shift(63).abs().replace(0, np.nan)
    base = _f32_leverage_accel_debt(debt, 63) * ng * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of debt accel × netinc growth 252d
def f32la_f32_leverage_acceleration_debtaccelxnetincg_252d_slope_v140_signal(debt, netinc, closeadj):
    ng = _diff(netinc, 252) / netinc.shift(252).abs().replace(0, np.nan)
    base = _f32_leverage_accel_debt(debt, 252) * ng * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of D/E accel anomaly 63d
def f32la_f32_leverage_acceleration_deaccelanomaly_63d_slope_v141_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    bm = a.expanding(min_periods=63).mean()
    base = (a - bm) * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of D/E accel anomaly 252d
def f32la_f32_leverage_acceleration_deaccelanomaly_252d_slope_v142_signal(debt, equity, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 252)
    bm = a.expanding(min_periods=126).mean()
    base = (a - bm) * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of intexp accel × debt 63d
def f32la_f32_leverage_acceleration_intexpaccelxdebt_63d_slope_v143_signal(intexp, debt, closeadj):
    a = _f32_leverage_accel_growth(intexp, 63)
    base = a * debt.abs() * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of intexp accel × debt 252d
def f32la_f32_leverage_acceleration_intexpaccelxdebt_252d_slope_v144_signal(intexp, debt, closeadj):
    a = _f32_leverage_accel_growth(intexp, 252)
    base = a * debt.abs() * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of liab/sharesbas × level 63d
def f32la_f32_leverage_acceleration_liabpsxlevel_63d_slope_v145_signal(liabilities, sharesbas, closeadj):
    s = liabilities / sharesbas.replace(0, np.nan)
    a = _f32_leverage_accel_growth(s, 63)
    base = a * sharesbas * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of liab/sharesbas × level 252d
def f32la_f32_leverage_acceleration_liabpsxlevel_252d_slope_v146_signal(liabilities, sharesbas, closeadj):
    s = liabilities / sharesbas.replace(0, np.nan)
    a = _f32_leverage_accel_growth(s, 252)
    base = a * sharesbas * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of joint leverage accel 63d
def f32la_f32_leverage_acceleration_jointlevaccel_63d_slope_v147_signal(debt, equity, intexp, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    b = _f32_leverage_accel_growth(intexp, 63)
    base = a * b * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of joint leverage accel 252d
def f32la_f32_leverage_acceleration_jointlevaccel_252d_slope_v148_signal(debt, equity, intexp, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 252)
    b = _f32_leverage_accel_growth(intexp, 252)
    base = a * b * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d slope of debt accel × debt/EBITDA quality 63d
def f32la_f32_leverage_acceleration_debtaccelxquality_63d_slope_v149_signal(debt, ebitda, closeadj):
    q = debt / ebitda.replace(0, np.nan)
    a = _f32_leverage_accel_debt(debt, 63)
    base = a * q * closeadj
    result = _slope_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d slope of composite leverage severity 252d
def f32la_f32_leverage_acceleration_compositesev_252d_slope_v150_signal(debt, equity, liabilities, closeadj):
    a = _f32_leverage_accel_de(debt, equity, 63)
    b = _f32_leverage_accel_debt(debt, 63)
    c = _f32_leverage_accel_growth(liabilities, 63)
    s = (a + b + c).rolling(252, min_periods=63).sum()
    base = s * closeadj
    result = _slope_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f32la_f32_leverage_acceleration_deaccel_21d_slope_v001_signal,
    f32la_f32_leverage_acceleration_deaccel_21d_slope_v002_signal,
    f32la_f32_leverage_acceleration_deaccel_63d_slope_v003_signal,
    f32la_f32_leverage_acceleration_deaccel_63d_slope_v004_signal,
    f32la_f32_leverage_acceleration_deaccel_63d_slope_v005_signal,
    f32la_f32_leverage_acceleration_deaccel_126d_slope_v006_signal,
    f32la_f32_leverage_acceleration_deaccel_126d_slope_v007_signal,
    f32la_f32_leverage_acceleration_deaccel_252d_slope_v008_signal,
    f32la_f32_leverage_acceleration_deaccel_252d_slope_v009_signal,
    f32la_f32_leverage_acceleration_debtaccel_21d_slope_v010_signal,
    f32la_f32_leverage_acceleration_debtaccel_21d_slope_v011_signal,
    f32la_f32_leverage_acceleration_debtaccel_63d_slope_v012_signal,
    f32la_f32_leverage_acceleration_debtaccel_63d_slope_v013_signal,
    f32la_f32_leverage_acceleration_debtaccel_126d_slope_v014_signal,
    f32la_f32_leverage_acceleration_debtaccel_252d_slope_v015_signal,
    f32la_f32_leverage_acceleration_liabaccel_21d_slope_v016_signal,
    f32la_f32_leverage_acceleration_liabaccel_63d_slope_v017_signal,
    f32la_f32_leverage_acceleration_liabaccel_252d_slope_v018_signal,
    f32la_f32_leverage_acceleration_dataccel_21d_slope_v019_signal,
    f32la_f32_leverage_acceleration_dataccel_63d_slope_v020_signal,
    f32la_f32_leverage_acceleration_dataccel_252d_slope_v021_signal,
    f32la_f32_leverage_acceleration_debitebitdaaccel_21d_slope_v022_signal,
    f32la_f32_leverage_acceleration_debitebitdaaccel_63d_slope_v023_signal,
    f32la_f32_leverage_acceleration_debitebitdaaccel_252d_slope_v024_signal,
    f32la_f32_leverage_acceleration_deaccelmean_63d_slope_v025_signal,
    f32la_f32_leverage_acceleration_deaccelmean_126d_slope_v026_signal,
    f32la_f32_leverage_acceleration_debtaccelmean_63d_slope_v027_signal,
    f32la_f32_leverage_acceleration_debtaccelmean_126d_slope_v028_signal,
    f32la_f32_leverage_acceleration_deaccelstd_63d_slope_v029_signal,
    f32la_f32_leverage_acceleration_deaccelstd_252d_slope_v030_signal,
    f32la_f32_leverage_acceleration_debtaccelstd_63d_slope_v031_signal,
    f32la_f32_leverage_acceleration_debtaccelstd_252d_slope_v032_signal,
    f32la_f32_leverage_acceleration_deaccelz_252d_slope_v033_signal,
    f32la_f32_leverage_acceleration_debtaccelz_252d_slope_v034_signal,
    f32la_f32_leverage_acceleration_deaccelz_504d_slope_v035_signal,
    f32la_f32_leverage_acceleration_debtaccelz_504d_slope_v036_signal,
    f32la_f32_leverage_acceleration_debtps_21d_slope_v037_signal,
    f32la_f32_leverage_acceleration_debtps_63d_slope_v038_signal,
    f32la_f32_leverage_acceleration_debtps_252d_slope_v039_signal,
    f32la_f32_leverage_acceleration_debttorev_63d_slope_v040_signal,
    f32la_f32_leverage_acceleration_debttorev_252d_slope_v041_signal,
    f32la_f32_leverage_acceleration_liabtoeq_63d_slope_v042_signal,
    f32la_f32_leverage_acceleration_liabtoeq_252d_slope_v043_signal,
    f32la_f32_leverage_acceleration_liabtoasset_63d_slope_v044_signal,
    f32la_f32_leverage_acceleration_liabtoasset_252d_slope_v045_signal,
    f32la_f32_leverage_acceleration_debttofcf_63d_slope_v046_signal,
    f32la_f32_leverage_acceleration_debttofcf_252d_slope_v047_signal,
    f32la_f32_leverage_acceleration_debttoncfo_63d_slope_v048_signal,
    f32la_f32_leverage_acceleration_debttoncfo_252d_slope_v049_signal,
    f32la_f32_leverage_acceleration_intebitda_63d_slope_v050_signal,
    f32la_f32_leverage_acceleration_intebitda_252d_slope_v051_signal,
    f32la_f32_leverage_acceleration_deaccelxlevel_63d_slope_v052_signal,
    f32la_f32_leverage_acceleration_deaccelxlevel_252d_slope_v053_signal,
    f32la_f32_leverage_acceleration_debtaccelxlevel_63d_slope_v054_signal,
    f32la_f32_leverage_acceleration_debtaccelxlevel_252d_slope_v055_signal,
    f32la_f32_leverage_acceleration_debtaccelxcur_63d_slope_v056_signal,
    f32la_f32_leverage_acceleration_debtaccelxcur_252d_slope_v057_signal,
    f32la_f32_leverage_acceleration_dminuseaccel_21d_slope_v058_signal,
    f32la_f32_leverage_acceleration_dminuseaccel_63d_slope_v059_signal,
    f32la_f32_leverage_acceleration_dminuseaccel_252d_slope_v060_signal,
    f32la_f32_leverage_acceleration_deposcnt_63d_slope_v061_signal,
    f32la_f32_leverage_acceleration_deposcnt_252d_slope_v062_signal,
    f32la_f32_leverage_acceleration_debtposcnt_252d_slope_v063_signal,
    f32la_f32_leverage_acceleration_debtposcnt_63d_slope_v064_signal,
    f32la_f32_leverage_acceleration_deaccelratio_63v252_slope_v065_signal,
    f32la_f32_leverage_acceleration_deacceldiff_21m63_slope_v066_signal,
    f32la_f32_leverage_acceleration_deacceldiff_63m252_slope_v067_signal,
    f32la_f32_leverage_acceleration_debtacceldiff_21m63_slope_v068_signal,
    f32la_f32_leverage_acceleration_debtacceldiff_63m252_slope_v069_signal,
    f32la_f32_leverage_acceleration_debtaccelxint_21d_slope_v070_signal,
    f32la_f32_leverage_acceleration_debtaccelxint_252d_slope_v071_signal,
    f32la_f32_leverage_acceleration_debtaccelxwc_63d_slope_v072_signal,
    f32la_f32_leverage_acceleration_debtaccelxwc_252d_slope_v073_signal,
    f32la_f32_leverage_acceleration_eqaccel_21d_slope_v074_signal,
    f32la_f32_leverage_acceleration_eqaccel_63d_slope_v075_signal,
    f32la_f32_leverage_acceleration_eqaccel_252d_slope_v076_signal,
    f32la_f32_leverage_acceleration_levcompose_21d_slope_v077_signal,
    f32la_f32_leverage_acceleration_levcompose_252d_slope_v078_signal,
    f32la_f32_leverage_acceleration_deaccelxeps_63d_slope_v079_signal,
    f32la_f32_leverage_acceleration_deaccelxeps_252d_slope_v080_signal,
    f32la_f32_leverage_acceleration_debtaccelxlev_63d_slope_v081_signal,
    f32la_f32_leverage_acceleration_liabaccelxlev_252d_slope_v082_signal,
    f32la_f32_leverage_acceleration_deaccelxrev_21d_slope_v083_signal,
    f32la_f32_leverage_acceleration_deaccelxrev_252d_slope_v084_signal,
    f32la_f32_leverage_acceleration_deaccelxcurratio_63d_slope_v085_signal,
    f32la_f32_leverage_acceleration_deaccelxcurratio_252d_slope_v086_signal,
    f32la_f32_leverage_acceleration_debtshareintensity_63d_slope_v087_signal,
    f32la_f32_leverage_acceleration_debtshareintensity_252d_slope_v088_signal,
    f32la_f32_leverage_acceleration_deaccelema_63d_slope_v089_signal,
    f32la_f32_leverage_acceleration_deaccelema_252d_slope_v090_signal,
    f32la_f32_leverage_acceleration_debtaccelema_63d_slope_v091_signal,
    f32la_f32_leverage_acceleration_debtaccelema_252d_slope_v092_signal,
    f32la_f32_leverage_acceleration_deaccelsq_63d_slope_v093_signal,
    f32la_f32_leverage_acceleration_deaccelsq_252d_slope_v094_signal,
    f32la_f32_leverage_acceleration_debtaccelsq_63d_slope_v095_signal,
    f32la_f32_leverage_acceleration_debtaccelsq_252d_slope_v096_signal,
    f32la_f32_leverage_acceleration_deaccelarea_63d_slope_v097_signal,
    f32la_f32_leverage_acceleration_deaccelarea_252d_slope_v098_signal,
    f32la_f32_leverage_acceleration_debtaccelarea_63d_slope_v099_signal,
    f32la_f32_leverage_acceleration_debtaccelarea_252d_slope_v100_signal,
    f32la_f32_leverage_acceleration_levaccelcomp_63d_slope_v101_signal,
    f32la_f32_leverage_acceleration_levaccelcomp_252d_slope_v102_signal,
    f32la_f32_leverage_acceleration_deminusdebt_63d_slope_v103_signal,
    f32la_f32_leverage_acceleration_deminusdebt_252d_slope_v104_signal,
    f32la_f32_leverage_acceleration_deaccelxrevg_63d_slope_v105_signal,
    f32la_f32_leverage_acceleration_deaccelxrevg_252d_slope_v106_signal,
    f32la_f32_leverage_acceleration_debtaccelxrevg_63d_slope_v107_signal,
    f32la_f32_leverage_acceleration_debtaccelxrevg_252d_slope_v108_signal,
    f32la_f32_leverage_acceleration_deaccelxepsg_21d_slope_v109_signal,
    f32la_f32_leverage_acceleration_deaccelxepsg_252d_slope_v110_signal,
    f32la_f32_leverage_acceleration_netdebtxrev_63d_slope_v111_signal,
    f32la_f32_leverage_acceleration_netdebtxrev_252d_slope_v112_signal,
    f32la_f32_leverage_acceleration_deaccelxqual_63d_slope_v113_signal,
    f32la_f32_leverage_acceleration_deaccelxqual_252d_slope_v114_signal,
    f32la_f32_leverage_acceleration_devsdebt_63d_slope_v115_signal,
    f32la_f32_leverage_acceleration_devsdebt_252d_slope_v116_signal,
    f32la_f32_leverage_acceleration_deaccelxavg_252d_slope_v117_signal,
    f32la_f32_leverage_acceleration_debtaccelxavg_252d_slope_v118_signal,
    f32la_f32_leverage_acceleration_debttoeqxlevel_63d_slope_v119_signal,
    f32la_f32_leverage_acceleration_debttoeqxlevel_252d_slope_v120_signal,
    f32la_f32_leverage_acceleration_deaccelsignsum_63d_slope_v121_signal,
    f32la_f32_leverage_acceleration_deaccelsignsum_252d_slope_v122_signal,
    f32la_f32_leverage_acceleration_debtaccelsignsum_63d_slope_v123_signal,
    f32la_f32_leverage_acceleration_debtaccelsignsum_252d_slope_v124_signal,
    f32la_f32_leverage_acceleration_debtaccelxtax_63d_slope_v125_signal,
    f32la_f32_leverage_acceleration_debtaccelxtax_252d_slope_v126_signal,
    f32la_f32_leverage_acceleration_debtaccelxintexp_63d_slope_v127_signal,
    f32la_f32_leverage_acceleration_debtaccelxintexp_252d_slope_v128_signal,
    f32la_f32_leverage_acceleration_debtaccelxretearn_63d_slope_v129_signal,
    f32la_f32_leverage_acceleration_debtaccelxretearn_252d_slope_v130_signal,
    f32la_f32_leverage_acceleration_liabaccelxintexp_63d_slope_v131_signal,
    f32la_f32_leverage_acceleration_liabaccelxintexp_252d_slope_v132_signal,
    f32la_f32_leverage_acceleration_debtpsaccelz_252d_slope_v133_signal,
    f32la_f32_leverage_acceleration_debtpsaccelz_504d_slope_v134_signal,
    f32la_f32_leverage_acceleration_deaccelmulti_slope_v135_signal,
    f32la_f32_leverage_acceleration_debtaccelmulti_slope_v136_signal,
    f32la_f32_leverage_acceleration_deaccelhealth_63d_slope_v137_signal,
    f32la_f32_leverage_acceleration_deaccelhealth_252d_slope_v138_signal,
    f32la_f32_leverage_acceleration_debtaccelxnetincg_63d_slope_v139_signal,
    f32la_f32_leverage_acceleration_debtaccelxnetincg_252d_slope_v140_signal,
    f32la_f32_leverage_acceleration_deaccelanomaly_63d_slope_v141_signal,
    f32la_f32_leverage_acceleration_deaccelanomaly_252d_slope_v142_signal,
    f32la_f32_leverage_acceleration_intexpaccelxdebt_63d_slope_v143_signal,
    f32la_f32_leverage_acceleration_intexpaccelxdebt_252d_slope_v144_signal,
    f32la_f32_leverage_acceleration_liabpsxlevel_63d_slope_v145_signal,
    f32la_f32_leverage_acceleration_liabpsxlevel_252d_slope_v146_signal,
    f32la_f32_leverage_acceleration_jointlevaccel_63d_slope_v147_signal,
    f32la_f32_leverage_acceleration_jointlevaccel_252d_slope_v148_signal,
    f32la_f32_leverage_acceleration_debtaccelxquality_63d_slope_v149_signal,
    f32la_f32_leverage_acceleration_compositesev_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F32_LEVERAGE_ACCELERATION_REGISTRY_SLOPE = REGISTRY


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
    eps = fund_walk(0.0005, 0.02, 2.0).rename("eps")
    sharesbas = fund_walk(0.0001, 0.005, 1e7).rename("sharesbas")
    ncfo = fund_walk(0.0005, 0.022, 1.5e7).rename("ncfo")
    workingcapital = fund_walk(0.0004, 0.02, 3e7).rename("workingcapital")
    currentratio = fund_walk(0.0001, 0.01, 1.5).rename("currentratio")
    intexp = fund_walk(0.0003, 0.018, 5e6).rename("intexp")
    retearn = fund_walk(0.0005, 0.02, 1e8).rename("retearn")
    liabilities = fund_walk(0.0004, 0.012, 7e8).rename("liabilities")
    taxexp = fund_walk(0.0004, 0.022, 4e6).rename("taxexp")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf,
        "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda,
        "eps": eps, "sharesbas": sharesbas, "ncfo": ncfo,
        "workingcapital": workingcapital, "currentratio": currentratio,
        "intexp": intexp, "retearn": retearn, "liabilities": liabilities,
        "taxexp": taxexp,
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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f32_leverage_acceleration_2nd_derivatives_001_150_claude: {n_features} features pass")
