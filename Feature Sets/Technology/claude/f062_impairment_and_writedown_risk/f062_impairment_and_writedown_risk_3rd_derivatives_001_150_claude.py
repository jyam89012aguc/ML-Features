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


# 21d acceleration of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_accel_21d_3d_v001_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_accel_63d_3d_v002_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_accel_126d_3d_v003_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_accel_252d_3d_v004_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_accel_21d_3d_v005_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_accel_63d_3d_v006_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_accel_126d_3d_v007_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_accel_252d_3d_v008_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_accel_21d_3d_v009_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_accel_63d_3d_v010_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_accel_126d_3d_v011_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_accel_252d_3d_v012_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_accel_21d_3d_v013_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_accel_63d_3d_v014_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_accel_126d_3d_v015_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_accel_252d_3d_v016_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_accel_21d_3d_v017_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_accel_63d_3d_v018_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_accel_126d_3d_v019_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_accel_252d_3d_v020_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_accel_21d_3d_v021_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_accel_63d_3d_v022_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_accel_126d_3d_v023_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_accel_252d_3d_v024_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_accel_21d_3d_v025_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_accel_63d_3d_v026_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_accel_126d_3d_v027_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_accel_252d_3d_v028_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_slopez_21d_z126_3d_v029_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_slopez_63d_z252_3d_v030_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_slopez_126d_z252_3d_v031_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_slopez_252d_z504_3d_v032_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_slopez_21d_z126_3d_v033_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_slopez_63d_z252_3d_v034_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_slopez_126d_z252_3d_v035_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_slopez_252d_z504_3d_v036_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_slopez_21d_z126_3d_v037_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_slopez_63d_z252_3d_v038_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_slopez_126d_z252_3d_v039_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_slopez_252d_z504_3d_v040_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_slopez_21d_z126_3d_v041_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_slopez_63d_z252_3d_v042_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_slopez_126d_z252_3d_v043_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_slopez_252d_z504_3d_v044_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_slopez_21d_z126_3d_v045_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_slopez_63d_z252_3d_v046_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_slopez_126d_z252_3d_v047_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_slopez_252d_z504_3d_v048_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_slopez_21d_z126_3d_v049_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_slopez_63d_z252_3d_v050_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_slopez_126d_z252_3d_v051_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_slopez_252d_z504_3d_v052_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_slopez_21d_z126_3d_v053_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_slopez_63d_z252_3d_v054_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_slopez_126d_z252_3d_v055_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_slopez_252d_z504_3d_v056_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_jerk_21d_3d_v057_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_jerk_63d_3d_v058_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_jerk_126d_3d_v059_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_jerk_21d_3d_v060_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_jerk_63d_3d_v061_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_jerk_126d_3d_v062_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_jerk_21d_3d_v063_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_jerk_63d_3d_v064_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_jerk_126d_3d_v065_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_jerk_21d_3d_v066_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_jerk_63d_3d_v067_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_jerk_126d_3d_v068_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_jerk_21d_3d_v069_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_jerk_63d_3d_v070_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_jerk_126d_3d_v071_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_jerk_21d_3d_v072_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_jerk_63d_3d_v073_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_jerk_126d_3d_v074_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_jerk_21d_3d_v075_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_jerk_63d_3d_v076_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_jerk_126d_3d_v077_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of intang_burden smoothed over 252d
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_smoothaccel_63d_sm252_3d_v078_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of intang_burden smoothed over 504d
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_smoothaccel_252d_sm504_3d_v079_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of amort_intensity smoothed over 252d
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_smoothaccel_63d_sm252_3d_v080_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of amort_intensity smoothed over 504d
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_smoothaccel_252d_sm504_3d_v081_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of intang_yoy_chg smoothed over 252d
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_smoothaccel_63d_sm252_3d_v082_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of intang_yoy_chg smoothed over 504d
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_smoothaccel_252d_sm504_3d_v083_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of intang_decline_flag smoothed over 252d
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_smoothaccel_63d_sm252_3d_v084_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of intang_decline_flag smoothed over 504d
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_smoothaccel_252d_sm504_3d_v085_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of opex_impair_proxy smoothed over 252d
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_smoothaccel_63d_sm252_3d_v086_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of opex_impair_proxy smoothed over 504d
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_smoothaccel_252d_sm504_3d_v087_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of amort_to_opex_proxy smoothed over 252d
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_smoothaccel_63d_sm252_3d_v088_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of amort_to_opex_proxy smoothed over 504d
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_smoothaccel_252d_sm504_3d_v089_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of intang_minus_equity smoothed over 252d
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_smoothaccel_63d_sm252_3d_v090_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of intang_minus_equity smoothed over 504d
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_smoothaccel_252d_sm504_3d_v091_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_accelz_21d_z252_3d_v092_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_accelz_63d_z504_3d_v093_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_accelz_21d_z252_3d_v094_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_accelz_63d_z504_3d_v095_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_accelz_21d_z252_3d_v096_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_accelz_63d_z504_3d_v097_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_accelz_21d_z252_3d_v098_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_accelz_63d_z504_3d_v099_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_accelz_21d_z252_3d_v100_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_accelz_63d_z504_3d_v101_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_accelz_21d_z252_3d_v102_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_accelz_63d_z504_3d_v103_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_accelz_21d_z252_3d_v104_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of intang_minus_equity
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_accelz_63d_z504_3d_v105_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in intang_burden (raw count, no price scaling)
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_signflip_63d_3d_v106_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in intang_burden (raw count, no price scaling)
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_signflip_252d_3d_v107_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in amort_intensity (raw count, no price scaling)
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_signflip_63d_3d_v108_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in amort_intensity (raw count, no price scaling)
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_signflip_252d_3d_v109_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in intang_yoy_chg (raw count, no price scaling)
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_signflip_63d_3d_v110_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in intang_yoy_chg (raw count, no price scaling)
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_signflip_252d_3d_v111_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in intang_decline_flag (raw count, no price scaling)
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_signflip_63d_3d_v112_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in intang_decline_flag (raw count, no price scaling)
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_signflip_252d_3d_v113_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in opex_impair_proxy (raw count, no price scaling)
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_signflip_63d_3d_v114_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in opex_impair_proxy (raw count, no price scaling)
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_signflip_252d_3d_v115_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in amort_to_opex_proxy (raw count, no price scaling)
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_signflip_63d_3d_v116_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in amort_to_opex_proxy (raw count, no price scaling)
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_signflip_252d_3d_v117_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in intang_minus_equity (raw count, no price scaling)
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_signflip_63d_3d_v118_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in intang_minus_equity (raw count, no price scaling)
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_signflip_252d_3d_v119_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_burden normalized by 252d range
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_rngaccel_63d_r252_3d_v120_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_burden normalized by 504d range
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_rngaccel_252d_r504_3d_v121_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of amort_intensity normalized by 252d range
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_rngaccel_63d_r252_3d_v122_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of amort_intensity normalized by 504d range
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_rngaccel_252d_r504_3d_v123_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_yoy_chg normalized by 252d range
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_rngaccel_63d_r252_3d_v124_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_yoy_chg normalized by 504d range
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_rngaccel_252d_r504_3d_v125_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_decline_flag normalized by 252d range
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_rngaccel_63d_r252_3d_v126_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_decline_flag normalized by 504d range
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_rngaccel_252d_r504_3d_v127_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of opex_impair_proxy normalized by 252d range
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_rngaccel_63d_r252_3d_v128_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of opex_impair_proxy normalized by 504d range
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_rngaccel_252d_r504_3d_v129_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of amort_to_opex_proxy normalized by 252d range
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_rngaccel_63d_r252_3d_v130_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of amort_to_opex_proxy normalized by 504d range
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_rngaccel_252d_r504_3d_v131_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of intang_minus_equity normalized by 252d range
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_rngaccel_63d_r252_3d_v132_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of intang_minus_equity normalized by 504d range
def f062iwr_f062_impairment_and_writedown_risk_intang_minus_equity_rngaccel_252d_r504_3d_v133_signal(intangibles, equity, closeadj):
    base = intangibles - equity
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_cumslope_21d_3d_v134_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_cumslope_63d_3d_v135_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of intang_burden
def f062iwr_f062_impairment_and_writedown_risk_intang_burden_cumslope_252d_3d_v136_signal(intangibles, assets, closeadj):
    base = _f062_intang_burden(intangibles, assets)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_cumslope_21d_3d_v137_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_cumslope_63d_3d_v138_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of amort_intensity
def f062iwr_f062_impairment_and_writedown_risk_amort_intensity_cumslope_252d_3d_v139_signal(depamor, intangibles, closeadj):
    base = depamor / intangibles.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_cumslope_21d_3d_v140_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_cumslope_63d_3d_v141_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of intang_yoy_chg
def f062iwr_f062_impairment_and_writedown_risk_intang_yoy_chg_cumslope_252d_3d_v142_signal(intangibles, closeadj):
    base = intangibles.diff(periods=252)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_cumslope_21d_3d_v143_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_cumslope_63d_3d_v144_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of intang_decline_flag
def f062iwr_f062_impairment_and_writedown_risk_intang_decline_flag_cumslope_252d_3d_v145_signal(intangibles, closeadj):
    base = (intangibles.diff(periods=63) < 0).astype(float)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_cumslope_21d_3d_v146_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_cumslope_63d_3d_v147_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of opex_impair_proxy
def f062iwr_f062_impairment_and_writedown_risk_opex_impair_proxy_cumslope_252d_3d_v148_signal(opex, closeadj):
    base = (opex.diff(periods=63) - opex.rolling(252, min_periods=63).mean().diff(periods=63))
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_cumslope_21d_3d_v149_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of amort_to_opex_proxy
def f062iwr_f062_impairment_and_writedown_risk_amort_to_opex_proxy_cumslope_63d_3d_v150_signal(depamor, opex, closeadj):
    base = depamor / opex.abs().replace(0, np.nan)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

