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
def _f024_curshare(debtc, debt):
    return debtc / debt.replace(0, np.nan).abs()


# 21d acceleration of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_accel_21d_3d_v001_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_accel_63d_3d_v002_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_accel_126d_3d_v003_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_accel_252d_3d_v004_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_accel_21d_3d_v005_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_accel_63d_3d_v006_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_accel_126d_3d_v007_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_accel_252d_3d_v008_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_accel_21d_3d_v009_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_accel_63d_3d_v010_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_accel_126d_3d_v011_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_accel_252d_3d_v012_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_accel_21d_3d_v013_signal(debtc, closeadj):
    base = debtc
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_accel_63d_3d_v014_signal(debtc, closeadj):
    base = debtc
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_accel_126d_3d_v015_signal(debtc, closeadj):
    base = debtc
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_accel_252d_3d_v016_signal(debtc, closeadj):
    base = debtc
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_accel_21d_3d_v017_signal(debtnc, closeadj):
    base = debtnc
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_accel_63d_3d_v018_signal(debtnc, closeadj):
    base = debtnc
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_accel_126d_3d_v019_signal(debtnc, closeadj):
    base = debtnc
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_accel_252d_3d_v020_signal(debtnc, closeadj):
    base = debtnc
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_accel_21d_3d_v021_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_accel_63d_3d_v022_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_accel_126d_3d_v023_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_accel_252d_3d_v024_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d acceleration of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_accel_21d_3d_v025_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = _accel(base, 21) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_accel_63d_3d_v026_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = _accel(base, 63) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 126d acceleration of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_accel_126d_3d_v027_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = _accel(base, 126) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_accel_252d_3d_v028_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = _accel(base, 252) * closeadj / base.abs().replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_slopez_21d_z126_3d_v029_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_slopez_63d_z252_3d_v030_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_slopez_126d_z252_3d_v031_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_slopez_252d_z504_3d_v032_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_slopez_21d_z126_3d_v033_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_slopez_63d_z252_3d_v034_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_slopez_126d_z252_3d_v035_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_slopez_252d_z504_3d_v036_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_slopez_21d_z126_3d_v037_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_slopez_63d_z252_3d_v038_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_slopez_126d_z252_3d_v039_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_slopez_252d_z504_3d_v040_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_slopez_21d_z126_3d_v041_signal(debtc, closeadj):
    base = debtc
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_slopez_63d_z252_3d_v042_signal(debtc, closeadj):
    base = debtc
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_slopez_126d_z252_3d_v043_signal(debtc, closeadj):
    base = debtc
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_slopez_252d_z504_3d_v044_signal(debtc, closeadj):
    base = debtc
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_slopez_21d_z126_3d_v045_signal(debtnc, closeadj):
    base = debtnc
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_slopez_63d_z252_3d_v046_signal(debtnc, closeadj):
    base = debtnc
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_slopez_126d_z252_3d_v047_signal(debtnc, closeadj):
    base = debtnc
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_slopez_252d_z504_3d_v048_signal(debtnc, closeadj):
    base = debtnc
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_slopez_21d_z126_3d_v049_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_slopez_63d_z252_3d_v050_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_slopez_126d_z252_3d_v051_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_slopez_252d_z504_3d_v052_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope z 126d of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_slopez_21d_z126_3d_v053_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _z(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope z 252d of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_slopez_63d_z252_3d_v054_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope z 252d of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_slopez_126d_z252_3d_v055_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _z(s, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope z 504d of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_slopez_252d_z504_3d_v056_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = _z(s, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_jerk_21d_3d_v057_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_jerk_63d_3d_v058_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_jerk_126d_3d_v059_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_jerk_21d_3d_v060_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_jerk_63d_3d_v061_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_jerk_126d_3d_v062_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_jerk_21d_3d_v063_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_jerk_63d_3d_v064_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_jerk_126d_3d_v065_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_jerk_21d_3d_v066_signal(debtc, closeadj):
    base = debtc
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_jerk_63d_3d_v067_signal(debtc, closeadj):
    base = debtc
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_jerk_126d_3d_v068_signal(debtc, closeadj):
    base = debtc
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_jerk_21d_3d_v069_signal(debtnc, closeadj):
    base = debtnc
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_jerk_63d_3d_v070_signal(debtnc, closeadj):
    base = debtnc
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_jerk_126d_3d_v071_signal(debtnc, closeadj):
    base = debtnc
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_jerk_21d_3d_v072_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_jerk_63d_3d_v073_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_jerk_126d_3d_v074_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d jerk of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_jerk_21d_3d_v075_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = _slope_diff_norm(s, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d jerk of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_jerk_63d_3d_v076_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = _slope_diff_norm(s, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d jerk of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_jerk_126d_3d_v077_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 126)
    result = _slope_diff_norm(s, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of debtc_share smoothed over 252d
def f024dmm_f024_debt_maturity_mix_debtc_share_smoothaccel_63d_sm252_3d_v078_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of debtc_share smoothed over 504d
def f024dmm_f024_debt_maturity_mix_debtc_share_smoothaccel_252d_sm504_3d_v079_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of debtnc_share smoothed over 252d
def f024dmm_f024_debt_maturity_mix_debtnc_share_smoothaccel_63d_sm252_3d_v080_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of debtnc_share smoothed over 504d
def f024dmm_f024_debt_maturity_mix_debtnc_share_smoothaccel_252d_sm504_3d_v081_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of debtc_to_cash smoothed over 252d
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_smoothaccel_63d_sm252_3d_v082_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of debtc_to_cash smoothed over 504d
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_smoothaccel_252d_sm504_3d_v083_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of debtc_lvl smoothed over 252d
def f024dmm_f024_debt_maturity_mix_debtc_lvl_smoothaccel_63d_sm252_3d_v084_signal(debtc, closeadj):
    base = debtc
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of debtc_lvl smoothed over 504d
def f024dmm_f024_debt_maturity_mix_debtc_lvl_smoothaccel_252d_sm504_3d_v085_signal(debtc, closeadj):
    base = debtc
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of debtnc_lvl smoothed over 252d
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_smoothaccel_63d_sm252_3d_v086_signal(debtnc, closeadj):
    base = debtnc
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of debtnc_lvl smoothed over 504d
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_smoothaccel_252d_sm504_3d_v087_signal(debtnc, closeadj):
    base = debtnc
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of maturity_skew smoothed over 252d
def f024dmm_f024_debt_maturity_mix_maturity_skew_smoothaccel_63d_sm252_3d_v088_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of maturity_skew smoothed over 504d
def f024dmm_f024_debt_maturity_mix_maturity_skew_smoothaccel_252d_sm504_3d_v089_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel of debtc_to_asset smoothed over 252d
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_smoothaccel_63d_sm252_3d_v090_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _mean(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d accel of debtc_to_asset smoothed over 504d
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_smoothaccel_252d_sm504_3d_v091_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    a = _accel(base, 252) / base.abs().replace(0, np.nan)
    result = _mean(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_accelz_21d_z252_3d_v092_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_accelz_63d_z504_3d_v093_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_accelz_21d_z252_3d_v094_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_accelz_63d_z504_3d_v095_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_accelz_21d_z252_3d_v096_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_accelz_63d_z504_3d_v097_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_accelz_21d_z252_3d_v098_signal(debtc, closeadj):
    base = debtc
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_accelz_63d_z504_3d_v099_signal(debtc, closeadj):
    base = debtc
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_accelz_21d_z252_3d_v100_signal(debtnc, closeadj):
    base = debtnc
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_accelz_63d_z504_3d_v101_signal(debtnc, closeadj):
    base = debtnc
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_accelz_21d_z252_3d_v102_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_accelz_63d_z504_3d_v103_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d accel z 252d of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_accelz_21d_z252_3d_v104_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    a = _accel(base, 21) / base.abs().replace(0, np.nan)
    result = _z(a, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d accel z 504d of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_accelz_63d_z504_3d_v105_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    a = _accel(base, 63) / base.abs().replace(0, np.nan)
    result = _z(a, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in debtc_share (raw count, no price scaling)
def f024dmm_f024_debt_maturity_mix_debtc_share_signflip_63d_3d_v106_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in debtc_share (raw count, no price scaling)
def f024dmm_f024_debt_maturity_mix_debtc_share_signflip_252d_3d_v107_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in debtnc_share (raw count, no price scaling)
def f024dmm_f024_debt_maturity_mix_debtnc_share_signflip_63d_3d_v108_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in debtnc_share (raw count, no price scaling)
def f024dmm_f024_debt_maturity_mix_debtnc_share_signflip_252d_3d_v109_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in debtc_to_cash (raw count, no price scaling)
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_signflip_63d_3d_v110_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in debtc_to_cash (raw count, no price scaling)
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_signflip_252d_3d_v111_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in debtc_lvl (raw count, no price scaling)
def f024dmm_f024_debt_maturity_mix_debtc_lvl_signflip_63d_3d_v112_signal(debtc, closeadj):
    base = debtc
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in debtc_lvl (raw count, no price scaling)
def f024dmm_f024_debt_maturity_mix_debtc_lvl_signflip_252d_3d_v113_signal(debtc, closeadj):
    base = debtc
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in debtnc_lvl (raw count, no price scaling)
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_signflip_63d_3d_v114_signal(debtnc, closeadj):
    base = debtnc
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in debtnc_lvl (raw count, no price scaling)
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_signflip_252d_3d_v115_signal(debtnc, closeadj):
    base = debtnc
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in maturity_skew (raw count, no price scaling)
def f024dmm_f024_debt_maturity_mix_maturity_skew_signflip_63d_3d_v116_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in maturity_skew (raw count, no price scaling)
def f024dmm_f024_debt_maturity_mix_maturity_skew_signflip_252d_3d_v117_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 63d slope sign flips in debtc_to_asset (raw count, no price scaling)
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_signflip_63d_3d_v118_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# count of 252d slope sign flips in debtc_to_asset (raw count, no price scaling)
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_signflip_252d_3d_v119_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    flips = (np.sign(s) != np.sign(s.shift(1))).astype(float)
    result = flips.rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of debtc_share normalized by 252d range
def f024dmm_f024_debt_maturity_mix_debtc_share_rngaccel_63d_r252_3d_v120_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of debtc_share normalized by 504d range
def f024dmm_f024_debt_maturity_mix_debtc_share_rngaccel_252d_r504_3d_v121_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of debtnc_share normalized by 252d range
def f024dmm_f024_debt_maturity_mix_debtnc_share_rngaccel_63d_r252_3d_v122_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of debtnc_share normalized by 504d range
def f024dmm_f024_debt_maturity_mix_debtnc_share_rngaccel_252d_r504_3d_v123_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of debtc_to_cash normalized by 252d range
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_rngaccel_63d_r252_3d_v124_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of debtc_to_cash normalized by 504d range
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_rngaccel_252d_r504_3d_v125_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of debtc_lvl normalized by 252d range
def f024dmm_f024_debt_maturity_mix_debtc_lvl_rngaccel_63d_r252_3d_v126_signal(debtc, closeadj):
    base = debtc
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of debtc_lvl normalized by 504d range
def f024dmm_f024_debt_maturity_mix_debtc_lvl_rngaccel_252d_r504_3d_v127_signal(debtc, closeadj):
    base = debtc
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of debtnc_lvl normalized by 252d range
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_rngaccel_63d_r252_3d_v128_signal(debtnc, closeadj):
    base = debtnc
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of debtnc_lvl normalized by 504d range
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_rngaccel_252d_r504_3d_v129_signal(debtnc, closeadj):
    base = debtnc
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of maturity_skew normalized by 252d range
def f024dmm_f024_debt_maturity_mix_maturity_skew_rngaccel_63d_r252_3d_v130_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of maturity_skew normalized by 504d range
def f024dmm_f024_debt_maturity_mix_maturity_skew_rngaccel_252d_r504_3d_v131_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d acceleration of debtc_to_asset normalized by 252d range
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_rngaccel_63d_r252_3d_v132_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    a = _accel(base, 63)
    rng = base.rolling(252, min_periods=max(1, 252//2)).max() - base.rolling(252, min_periods=max(1, 252//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d acceleration of debtc_to_asset normalized by 504d range
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_rngaccel_252d_r504_3d_v133_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    a = _accel(base, 252)
    rng = base.rolling(504, min_periods=max(1, 504//2)).max() - base.rolling(504, min_periods=max(1, 504//2)).min()
    result = a / rng.replace(0, np.nan).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_cumslope_21d_3d_v134_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_cumslope_63d_3d_v135_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_cumslope_252d_3d_v136_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_cumslope_21d_3d_v137_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_cumslope_63d_3d_v138_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_cumslope_252d_3d_v139_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_cumslope_21d_3d_v140_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_cumslope_63d_3d_v141_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_cumslope_252d_3d_v142_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_cumslope_21d_3d_v143_signal(debtc, closeadj):
    base = debtc
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_cumslope_63d_3d_v144_signal(debtc, closeadj):
    base = debtc
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_cumslope_252d_3d_v145_signal(debtc, closeadj):
    base = debtc
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_cumslope_21d_3d_v146_signal(debtnc, closeadj):
    base = debtnc
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_cumslope_63d_3d_v147_signal(debtnc, closeadj):
    base = debtnc
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d cumulative slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_cumslope_252d_3d_v148_signal(debtnc, closeadj):
    base = debtnc
    s = _slope_diff_norm(base, 252)
    result = s.rolling(252, min_periods=max(1, 252//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d cumulative slope of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_cumslope_21d_3d_v149_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = s.rolling(21, min_periods=max(1, 21//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d cumulative slope of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_cumslope_63d_3d_v150_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = s.rolling(63, min_periods=max(1, 63//2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

