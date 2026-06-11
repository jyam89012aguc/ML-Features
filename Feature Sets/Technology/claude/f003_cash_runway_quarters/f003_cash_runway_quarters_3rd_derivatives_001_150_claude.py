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
def _f003_burn(ncfo):
    return (-ncfo).clip(lower=0)


def _f003_runway(cashneq, investmentsc, ncfo):
    burn = (-ncfo).clip(lower=0)
    return (cashneq.fillna(0) + investmentsc.fillna(0)) / burn.replace(0, np.nan)


def _f003_fcf_runway(cashneq, investmentsc, fcf):
    burn = (-fcf).clip(lower=0)
    return (cashneq.fillna(0) + investmentsc.fillna(0)) / burn.replace(0, np.nan)


# 21d acceleration of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_accel_21d_3d_v001_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_accel_63d_3d_v002_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_accel_126d_3d_v003_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_accel_252d_3d_v004_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of runway
def f003cr_f003_cash_runway_quarters_runway_accel_21d_3d_v005_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of runway
def f003cr_f003_cash_runway_quarters_runway_accel_63d_3d_v006_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of runway
def f003cr_f003_cash_runway_quarters_runway_accel_126d_3d_v007_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of runway
def f003cr_f003_cash_runway_quarters_runway_accel_252d_3d_v008_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_accel_21d_3d_v009_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_accel_63d_3d_v010_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_accel_126d_3d_v011_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_accel_252d_3d_v012_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_accel_21d_3d_v013_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_accel_63d_3d_v014_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_accel_126d_3d_v015_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_accel_252d_3d_v016_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_accel_21d_3d_v017_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_accel_63d_3d_v018_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_accel_126d_3d_v019_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_accel_252d_3d_v020_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_accel_21d_3d_v021_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_accel_63d_3d_v022_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_accel_126d_3d_v023_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_accel_252d_3d_v024_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_accel_21d_3d_v025_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_accel_63d_3d_v026_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_accel_126d_3d_v027_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_accel_252d_3d_v028_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_slopez_21d_z126_3d_v029_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_slopez_63d_z252_3d_v030_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_slopez_126d_z252_3d_v031_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_slopez_252d_z504_3d_v032_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of runway
def f003cr_f003_cash_runway_quarters_runway_slopez_21d_z126_3d_v033_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of runway
def f003cr_f003_cash_runway_quarters_runway_slopez_63d_z252_3d_v034_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of runway
def f003cr_f003_cash_runway_quarters_runway_slopez_126d_z252_3d_v035_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of runway
def f003cr_f003_cash_runway_quarters_runway_slopez_252d_z504_3d_v036_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_slopez_21d_z126_3d_v037_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_slopez_63d_z252_3d_v038_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_slopez_126d_z252_3d_v039_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_slopez_252d_z504_3d_v040_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_slopez_21d_z126_3d_v041_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_slopez_63d_z252_3d_v042_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_slopez_126d_z252_3d_v043_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_slopez_252d_z504_3d_v044_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_slopez_21d_z126_3d_v045_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_slopez_63d_z252_3d_v046_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_slopez_126d_z252_3d_v047_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_slopez_252d_z504_3d_v048_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_slopez_21d_z126_3d_v049_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_slopez_63d_z252_3d_v050_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_slopez_126d_z252_3d_v051_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_slopez_252d_z504_3d_v052_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_slopez_21d_z126_3d_v053_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_slopez_63d_z252_3d_v054_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_slopez_126d_z252_3d_v055_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_slopez_252d_z504_3d_v056_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_jerk_21d_3d_v057_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_jerk_63d_3d_v058_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_jerk_126d_3d_v059_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of runway
def f003cr_f003_cash_runway_quarters_runway_jerk_21d_3d_v060_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of runway
def f003cr_f003_cash_runway_quarters_runway_jerk_63d_3d_v061_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of runway
def f003cr_f003_cash_runway_quarters_runway_jerk_126d_3d_v062_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_jerk_21d_3d_v063_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_jerk_63d_3d_v064_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_jerk_126d_3d_v065_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_jerk_21d_3d_v066_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_jerk_63d_3d_v067_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_jerk_126d_3d_v068_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_jerk_21d_3d_v069_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_jerk_63d_3d_v070_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_jerk_126d_3d_v071_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_jerk_21d_3d_v072_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_jerk_63d_3d_v073_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_jerk_126d_3d_v074_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_jerk_21d_3d_v075_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_jerk_63d_3d_v076_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_jerk_126d_3d_v077_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of burn_lvl smoothed over 252d
def f003cr_f003_cash_runway_quarters_burn_lvl_smoothaccel_63d_sm252_3d_v078_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of burn_lvl smoothed over 504d
def f003cr_f003_cash_runway_quarters_burn_lvl_smoothaccel_252d_sm504_3d_v079_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of runway smoothed over 252d
def f003cr_f003_cash_runway_quarters_runway_smoothaccel_63d_sm252_3d_v080_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of runway smoothed over 504d
def f003cr_f003_cash_runway_quarters_runway_smoothaccel_252d_sm504_3d_v081_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of fcf_runway smoothed over 252d
def f003cr_f003_cash_runway_quarters_fcf_runway_smoothaccel_63d_sm252_3d_v082_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of fcf_runway smoothed over 504d
def f003cr_f003_cash_runway_quarters_fcf_runway_smoothaccel_252d_sm504_3d_v083_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of burn_to_asset smoothed over 252d
def f003cr_f003_cash_runway_quarters_burn_to_asset_smoothaccel_63d_sm252_3d_v084_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of burn_to_asset smoothed over 504d
def f003cr_f003_cash_runway_quarters_burn_to_asset_smoothaccel_252d_sm504_3d_v085_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of burn_to_mcap smoothed over 252d
def f003cr_f003_cash_runway_quarters_burn_to_mcap_smoothaccel_63d_sm252_3d_v086_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of burn_to_mcap smoothed over 504d
def f003cr_f003_cash_runway_quarters_burn_to_mcap_smoothaccel_252d_sm504_3d_v087_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of burn_to_cash smoothed over 252d
def f003cr_f003_cash_runway_quarters_burn_to_cash_smoothaccel_63d_sm252_3d_v088_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of burn_to_cash smoothed over 504d
def f003cr_f003_cash_runway_quarters_burn_to_cash_smoothaccel_252d_sm504_3d_v089_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of fcf_burn_to_mcap smoothed over 252d
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_smoothaccel_63d_sm252_3d_v090_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of fcf_burn_to_mcap smoothed over 504d
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_smoothaccel_252d_sm504_3d_v091_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_accelz_21d_z252_3d_v092_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_accelz_63d_z504_3d_v093_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of runway
def f003cr_f003_cash_runway_quarters_runway_accelz_21d_z252_3d_v094_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of runway
def f003cr_f003_cash_runway_quarters_runway_accelz_63d_z504_3d_v095_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_accelz_21d_z252_3d_v096_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_accelz_63d_z504_3d_v097_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_accelz_21d_z252_3d_v098_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_accelz_63d_z504_3d_v099_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_accelz_21d_z252_3d_v100_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_accelz_63d_z504_3d_v101_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_accelz_21d_z252_3d_v102_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_accelz_63d_z504_3d_v103_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_accelz_21d_z252_3d_v104_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of fcf_burn_to_mcap
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_accelz_63d_z504_3d_v105_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in burn_lvl (raw count, no price scaling)
def f003cr_f003_cash_runway_quarters_burn_lvl_signflip_63d_3d_v106_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in burn_lvl (raw count, no price scaling)
def f003cr_f003_cash_runway_quarters_burn_lvl_signflip_252d_3d_v107_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in runway (raw count, no price scaling)
def f003cr_f003_cash_runway_quarters_runway_signflip_63d_3d_v108_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in runway (raw count, no price scaling)
def f003cr_f003_cash_runway_quarters_runway_signflip_252d_3d_v109_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in fcf_runway (raw count, no price scaling)
def f003cr_f003_cash_runway_quarters_fcf_runway_signflip_63d_3d_v110_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in fcf_runway (raw count, no price scaling)
def f003cr_f003_cash_runway_quarters_fcf_runway_signflip_252d_3d_v111_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in burn_to_asset (raw count, no price scaling)
def f003cr_f003_cash_runway_quarters_burn_to_asset_signflip_63d_3d_v112_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in burn_to_asset (raw count, no price scaling)
def f003cr_f003_cash_runway_quarters_burn_to_asset_signflip_252d_3d_v113_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in burn_to_mcap (raw count, no price scaling)
def f003cr_f003_cash_runway_quarters_burn_to_mcap_signflip_63d_3d_v114_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in burn_to_mcap (raw count, no price scaling)
def f003cr_f003_cash_runway_quarters_burn_to_mcap_signflip_252d_3d_v115_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in burn_to_cash (raw count, no price scaling)
def f003cr_f003_cash_runway_quarters_burn_to_cash_signflip_63d_3d_v116_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in burn_to_cash (raw count, no price scaling)
def f003cr_f003_cash_runway_quarters_burn_to_cash_signflip_252d_3d_v117_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in fcf_burn_to_mcap (raw count, no price scaling)
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_signflip_63d_3d_v118_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in fcf_burn_to_mcap (raw count, no price scaling)
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_signflip_252d_3d_v119_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of burn_lvl normalized by 252d range
def f003cr_f003_cash_runway_quarters_burn_lvl_rngaccel_63d_r252_3d_v120_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of burn_lvl normalized by 504d range
def f003cr_f003_cash_runway_quarters_burn_lvl_rngaccel_252d_r504_3d_v121_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of runway normalized by 252d range
def f003cr_f003_cash_runway_quarters_runway_rngaccel_63d_r252_3d_v122_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of runway normalized by 504d range
def f003cr_f003_cash_runway_quarters_runway_rngaccel_252d_r504_3d_v123_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_runway normalized by 252d range
def f003cr_f003_cash_runway_quarters_fcf_runway_rngaccel_63d_r252_3d_v124_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_runway normalized by 504d range
def f003cr_f003_cash_runway_quarters_fcf_runway_rngaccel_252d_r504_3d_v125_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of burn_to_asset normalized by 252d range
def f003cr_f003_cash_runway_quarters_burn_to_asset_rngaccel_63d_r252_3d_v126_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of burn_to_asset normalized by 504d range
def f003cr_f003_cash_runway_quarters_burn_to_asset_rngaccel_252d_r504_3d_v127_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of burn_to_mcap normalized by 252d range
def f003cr_f003_cash_runway_quarters_burn_to_mcap_rngaccel_63d_r252_3d_v128_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of burn_to_mcap normalized by 504d range
def f003cr_f003_cash_runway_quarters_burn_to_mcap_rngaccel_252d_r504_3d_v129_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of burn_to_cash normalized by 252d range
def f003cr_f003_cash_runway_quarters_burn_to_cash_rngaccel_63d_r252_3d_v130_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of burn_to_cash normalized by 504d range
def f003cr_f003_cash_runway_quarters_burn_to_cash_rngaccel_252d_r504_3d_v131_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of fcf_burn_to_mcap normalized by 252d range
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_rngaccel_63d_r252_3d_v132_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of fcf_burn_to_mcap normalized by 504d range
def f003cr_f003_cash_runway_quarters_fcf_burn_to_mcap_rngaccel_252d_r504_3d_v133_signal(fcf, marketcap, closeadj):
    base = (-fcf).clip(lower=0) / marketcap.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_cumslope_21d_3d_v134_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_cumslope_63d_3d_v135_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of burn_lvl
def f003cr_f003_cash_runway_quarters_burn_lvl_cumslope_252d_3d_v136_signal(ncfo, closeadj):
    base = _f003_burn(ncfo)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of runway
def f003cr_f003_cash_runway_quarters_runway_cumslope_21d_3d_v137_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of runway
def f003cr_f003_cash_runway_quarters_runway_cumslope_63d_3d_v138_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of runway
def f003cr_f003_cash_runway_quarters_runway_cumslope_252d_3d_v139_signal(cashneq, investmentsc, ncfo, closeadj):
    base = _f003_runway(cashneq, investmentsc, ncfo)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_cumslope_21d_3d_v140_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_cumslope_63d_3d_v141_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of fcf_runway
def f003cr_f003_cash_runway_quarters_fcf_runway_cumslope_252d_3d_v142_signal(cashneq, investmentsc, fcf, closeadj):
    base = _f003_fcf_runway(cashneq, investmentsc, fcf)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_cumslope_21d_3d_v143_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_cumslope_63d_3d_v144_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of burn_to_asset
def f003cr_f003_cash_runway_quarters_burn_to_asset_cumslope_252d_3d_v145_signal(ncfo, assets, closeadj):
    base = _f003_burn(ncfo) / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_cumslope_21d_3d_v146_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_cumslope_63d_3d_v147_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of burn_to_mcap
def f003cr_f003_cash_runway_quarters_burn_to_mcap_cumslope_252d_3d_v148_signal(ncfo, marketcap, closeadj):
    base = _f003_burn(ncfo) / marketcap.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_cumslope_21d_3d_v149_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of burn_to_cash
def f003cr_f003_cash_runway_quarters_burn_to_cash_cumslope_63d_3d_v150_signal(ncfo, cashneq, closeadj):
    base = _f003_burn(ncfo) / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

