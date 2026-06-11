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


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


# ===== folder domain primitives =====
def _f062_intang_burden(intangibles, assets):
    return intangibles / assets.replace(0, np.nan).abs()


# 21d slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_slope_21d_2d_v001_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_slope_63d_2d_v002_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_slope_126d_2d_v003_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_slope_252d_2d_v004_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_slope_504d_2d_v005_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_slope_21d_2d_v006_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_slope_63d_2d_v007_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_slope_126d_2d_v008_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_slope_252d_2d_v009_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_slope_504d_2d_v010_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_slope_21d_2d_v011_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_slope_63d_2d_v012_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_slope_126d_2d_v013_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_slope_252d_2d_v014_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_slope_504d_2d_v015_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_slope_21d_2d_v016_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_slope_63d_2d_v017_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_slope_126d_2d_v018_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_slope_252d_2d_v019_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_slope_504d_2d_v020_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_slope_21d_2d_v021_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_slope_63d_2d_v022_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_slope_126d_2d_v023_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_slope_252d_2d_v024_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_slope_504d_2d_v025_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_slope_21d_2d_v026_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_slope_63d_2d_v027_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_slope_126d_2d_v028_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_slope_252d_2d_v029_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_slope_504d_2d_v030_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_slope_21d_2d_v031_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_slope_63d_2d_v032_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_slope_126d_2d_v033_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_slope_252d_2d_v034_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_slope_504d_2d_v035_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_sm21_sl21_2d_v036_signal(intangibles, assets, closeadj):
    base = _mean(_f062_intang_burden(intangibles, assets), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_sm63_sl21_2d_v037_signal(intangibles, assets, closeadj):
    base = _mean(_f062_intang_burden(intangibles, assets), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_sm63_sl63_2d_v038_signal(intangibles, assets, closeadj):
    base = _mean(_f062_intang_burden(intangibles, assets), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_sm252_sl63_2d_v039_signal(intangibles, assets, closeadj):
    base = _mean(_f062_intang_burden(intangibles, assets), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_sm252_sl126_2d_v040_signal(intangibles, assets, closeadj):
    base = _mean(_f062_intang_burden(intangibles, assets), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_sm21_sl21_2d_v041_signal(depamor, intangibles, closeadj):
    base = _mean(depamor / intangibles.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_sm63_sl21_2d_v042_signal(depamor, intangibles, closeadj):
    base = _mean(depamor / intangibles.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_sm63_sl63_2d_v043_signal(depamor, intangibles, closeadj):
    base = _mean(depamor / intangibles.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_sm252_sl63_2d_v044_signal(depamor, intangibles, closeadj):
    base = _mean(depamor / intangibles.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_sm252_sl126_2d_v045_signal(depamor, intangibles, closeadj):
    base = _mean(depamor / intangibles.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_sm21_sl21_2d_v046_signal(intangibles, closeadj):
    base = _mean(intangibles.diff(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_sm63_sl21_2d_v047_signal(intangibles, closeadj):
    base = _mean(intangibles.diff(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_sm63_sl63_2d_v048_signal(intangibles, closeadj):
    base = _mean(intangibles.diff(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_sm252_sl63_2d_v049_signal(intangibles, closeadj):
    base = _mean(intangibles.diff(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_sm252_sl126_2d_v050_signal(intangibles, closeadj):
    base = _mean(intangibles.diff(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_sm21_sl21_2d_v051_signal(intangibles, closeadj):
    base = _mean((intangibles.diff(periods=63) < 0).astype(float), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_sm63_sl21_2d_v052_signal(intangibles, closeadj):
    base = _mean((intangibles.diff(periods=63) < 0).astype(float), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_sm63_sl63_2d_v053_signal(intangibles, closeadj):
    base = _mean((intangibles.diff(periods=63) < 0).astype(float), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_sm252_sl63_2d_v054_signal(intangibles, closeadj):
    base = _mean((intangibles.diff(periods=63) < 0).astype(float), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_sm252_sl126_2d_v055_signal(intangibles, closeadj):
    base = _mean((intangibles.diff(periods=63) < 0).astype(float), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_sm21_sl21_2d_v056_signal(opex, closeadj):
    base = _mean((opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63)), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_sm63_sl21_2d_v057_signal(opex, closeadj):
    base = _mean((opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63)), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_sm63_sl63_2d_v058_signal(opex, closeadj):
    base = _mean((opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63)), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_sm252_sl63_2d_v059_signal(opex, closeadj):
    base = _mean((opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63)), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_sm252_sl126_2d_v060_signal(opex, closeadj):
    base = _mean((opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63)), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_sm21_sl21_2d_v061_signal(depamor, opex, closeadj):
    base = _mean(depamor / opex.abs().replace(0, np.nan), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_sm63_sl21_2d_v062_signal(depamor, opex, closeadj):
    base = _mean(depamor / opex.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_sm63_sl63_2d_v063_signal(depamor, opex, closeadj):
    base = _mean(depamor / opex.abs().replace(0, np.nan), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_sm252_sl63_2d_v064_signal(depamor, opex, closeadj):
    base = _mean(depamor / opex.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_sm252_sl126_2d_v065_signal(depamor, opex, closeadj):
    base = _mean(depamor / opex.abs().replace(0, np.nan), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_sm21_sl21_2d_v066_signal(intangibles, equity, closeadj):
    base = _mean(intangibles - equity, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_sm63_sl21_2d_v067_signal(intangibles, equity, closeadj):
    base = _mean(intangibles - equity, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_sm63_sl63_2d_v068_signal(intangibles, equity, closeadj):
    base = _mean(intangibles - equity, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_sm252_sl63_2d_v069_signal(intangibles, equity, closeadj):
    base = _mean(intangibles - equity, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_sm252_sl126_2d_v070_signal(intangibles, equity, closeadj):
    base = _mean(intangibles - equity, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_pctslope_21d_2d_v071_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_pctslope_63d_2d_v072_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_pctslope_252d_2d_v073_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_pctslope_21d_2d_v074_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_pctslope_63d_2d_v075_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_pctslope_252d_2d_v076_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_pctslope_21d_2d_v077_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_pctslope_63d_2d_v078_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_pctslope_252d_2d_v079_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_pctslope_21d_2d_v080_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_pctslope_63d_2d_v081_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_pctslope_252d_2d_v082_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_pctslope_21d_2d_v083_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_pctslope_63d_2d_v084_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_pctslope_252d_2d_v085_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_pctslope_21d_2d_v086_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_pctslope_63d_2d_v087_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_pctslope_252d_2d_v088_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_pctslope_21d_2d_v089_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_pctslope_63d_2d_v090_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_pctslope_252d_2d_v091_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_sgnslope_21d_2d_v092_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_sgnslope_63d_2d_v093_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_sgnslope_252d_2d_v094_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_sgnslope_21d_2d_v095_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_sgnslope_63d_2d_v096_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_sgnslope_252d_2d_v097_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_sgnslope_21d_2d_v098_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_sgnslope_63d_2d_v099_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_sgnslope_252d_2d_v100_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_sgnslope_21d_2d_v101_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_sgnslope_63d_2d_v102_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_sgnslope_252d_2d_v103_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_sgnslope_21d_2d_v104_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_sgnslope_63d_2d_v105_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_sgnslope_252d_2d_v106_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_sgnslope_21d_2d_v107_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_sgnslope_63d_2d_v108_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_sgnslope_252d_2d_v109_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_sgnslope_21d_2d_v110_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_sgnslope_63d_2d_v111_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_sgnslope_252d_2d_v112_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_logmagslope_21d_2d_v113_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_logmagslope_63d_2d_v114_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_logmagslope_252d_2d_v115_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_logmagslope_21d_2d_v116_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_logmagslope_63d_2d_v117_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_logmagslope_252d_2d_v118_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_logmagslope_21d_2d_v119_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_logmagslope_63d_2d_v120_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_logmagslope_252d_2d_v121_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_logmagslope_21d_2d_v122_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_logmagslope_63d_2d_v123_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_logmagslope_252d_2d_v124_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_logmagslope_21d_2d_v125_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_logmagslope_63d_2d_v126_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_logmagslope_252d_2d_v127_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_logmagslope_21d_2d_v128_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_logmagslope_63d_2d_v129_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_logmagslope_252d_2d_v130_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_logmagslope_21d_2d_v131_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_logmagslope_63d_2d_v132_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_logmagslope_252d_2d_v133_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|intang_burden|
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_logslope_63d_2d_v134_signal(intangibles, assets, closeadj):
    base = np.log((_f062_intang_burden(intangibles, assets)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|intang_burden|
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_logslope_252d_2d_v135_signal(intangibles, assets, closeadj):
    base = np.log((_f062_intang_burden(intangibles, assets)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|amort_intensity|
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_logslope_63d_2d_v136_signal(depamor, intangibles, closeadj):
    base = np.log((depamor / intangibles.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|amort_intensity|
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_logslope_252d_2d_v137_signal(depamor, intangibles, closeadj):
    base = np.log((depamor / intangibles.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|intang_yoy_chg|
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_logslope_63d_2d_v138_signal(intangibles, closeadj):
    base = np.log((intangibles.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|intang_yoy_chg|
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_logslope_252d_2d_v139_signal(intangibles, closeadj):
    base = np.log((intangibles.diff(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|intang_decline_flag|
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_logslope_63d_2d_v140_signal(intangibles, closeadj):
    base = np.log(((intangibles.diff(periods=63) < 0).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|intang_decline_flag|
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_logslope_252d_2d_v141_signal(intangibles, closeadj):
    base = np.log(((intangibles.diff(periods=63) < 0).astype(float)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|opex_impair_proxy|
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_logslope_63d_2d_v142_signal(opex, closeadj):
    base = np.log(((opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|opex_impair_proxy|
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_logslope_252d_2d_v143_signal(opex, closeadj):
    base = np.log(((opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|amort_to_opex_proxy|
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_logslope_63d_2d_v144_signal(depamor, opex, closeadj):
    base = np.log((depamor / opex.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|amort_to_opex_proxy|
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_logslope_252d_2d_v145_signal(depamor, opex, closeadj):
    base = np.log((depamor / opex.abs().replace(0, np.nan)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|intang_minus_equity|
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_logslope_63d_2d_v146_signal(intangibles, equity, closeadj):
    base = np.log((intangibles - equity).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|intang_minus_equity|
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_logslope_252d_2d_v147_signal(intangibles, equity, closeadj):
    base = np.log((intangibles - equity).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

