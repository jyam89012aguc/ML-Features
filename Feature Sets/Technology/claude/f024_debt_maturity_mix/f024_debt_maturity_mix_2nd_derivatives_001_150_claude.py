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


# 21d slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_slope_21d_2d_v001_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_slope_63d_2d_v002_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_slope_126d_2d_v003_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_slope_252d_2d_v004_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_slope_504d_2d_v005_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_slope_21d_2d_v006_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_slope_63d_2d_v007_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_slope_126d_2d_v008_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_slope_252d_2d_v009_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_slope_504d_2d_v010_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_slope_21d_2d_v011_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_slope_63d_2d_v012_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_slope_126d_2d_v013_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_slope_252d_2d_v014_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_slope_504d_2d_v015_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_slope_21d_2d_v016_signal(debtc, closeadj):
    base = debtc
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_slope_63d_2d_v017_signal(debtc, closeadj):
    base = debtc
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_slope_126d_2d_v018_signal(debtc, closeadj):
    base = debtc
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_slope_252d_2d_v019_signal(debtc, closeadj):
    base = debtc
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_slope_504d_2d_v020_signal(debtc, closeadj):
    base = debtc
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_slope_21d_2d_v021_signal(debtnc, closeadj):
    base = debtnc
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_slope_63d_2d_v022_signal(debtnc, closeadj):
    base = debtnc
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_slope_126d_2d_v023_signal(debtnc, closeadj):
    base = debtnc
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_slope_252d_2d_v024_signal(debtnc, closeadj):
    base = debtnc
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_slope_504d_2d_v025_signal(debtnc, closeadj):
    base = debtnc
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_slope_21d_2d_v026_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_slope_63d_2d_v027_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_slope_126d_2d_v028_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_slope_252d_2d_v029_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_slope_504d_2d_v030_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_slope_21d_2d_v031_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_slope_63d_2d_v032_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_slope_126d_2d_v033_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_slope_252d_2d_v034_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_slope_504d_2d_v035_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_sm21_sl21_2d_v036_signal(debtc, debt, closeadj):
    base = _mean(_f024_curshare(debtc, debt), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_sm63_sl21_2d_v037_signal(debtc, debt, closeadj):
    base = _mean(_f024_curshare(debtc, debt), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_sm63_sl63_2d_v038_signal(debtc, debt, closeadj):
    base = _mean(_f024_curshare(debtc, debt), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_sm252_sl63_2d_v039_signal(debtc, debt, closeadj):
    base = _mean(_f024_curshare(debtc, debt), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_sm252_sl126_2d_v040_signal(debtc, debt, closeadj):
    base = _mean(_f024_curshare(debtc, debt), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_sm21_sl21_2d_v041_signal(debtnc, debt, closeadj):
    base = _mean(debtnc / debt.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_sm63_sl21_2d_v042_signal(debtnc, debt, closeadj):
    base = _mean(debtnc / debt.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_sm63_sl63_2d_v043_signal(debtnc, debt, closeadj):
    base = _mean(debtnc / debt.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_sm252_sl63_2d_v044_signal(debtnc, debt, closeadj):
    base = _mean(debtnc / debt.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_sm252_sl126_2d_v045_signal(debtnc, debt, closeadj):
    base = _mean(debtnc / debt.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_sm21_sl21_2d_v046_signal(debtc, cashneq, closeadj):
    base = _mean(debtc / cashneq.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_sm63_sl21_2d_v047_signal(debtc, cashneq, closeadj):
    base = _mean(debtc / cashneq.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_sm63_sl63_2d_v048_signal(debtc, cashneq, closeadj):
    base = _mean(debtc / cashneq.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_sm252_sl63_2d_v049_signal(debtc, cashneq, closeadj):
    base = _mean(debtc / cashneq.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_sm252_sl126_2d_v050_signal(debtc, cashneq, closeadj):
    base = _mean(debtc / cashneq.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_sm21_sl21_2d_v051_signal(debtc, closeadj):
    base = _mean(debtc, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_sm63_sl21_2d_v052_signal(debtc, closeadj):
    base = _mean(debtc, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_sm63_sl63_2d_v053_signal(debtc, closeadj):
    base = _mean(debtc, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_sm252_sl63_2d_v054_signal(debtc, closeadj):
    base = _mean(debtc, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_sm252_sl126_2d_v055_signal(debtc, closeadj):
    base = _mean(debtc, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_sm21_sl21_2d_v056_signal(debtnc, closeadj):
    base = _mean(debtnc, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_sm63_sl21_2d_v057_signal(debtnc, closeadj):
    base = _mean(debtnc, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_sm63_sl63_2d_v058_signal(debtnc, closeadj):
    base = _mean(debtnc, 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_sm252_sl63_2d_v059_signal(debtnc, closeadj):
    base = _mean(debtnc, 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_sm252_sl126_2d_v060_signal(debtnc, closeadj):
    base = _mean(debtnc, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_sm21_sl21_2d_v061_signal(debtc, debtnc, debt, closeadj):
    base = _mean((debtc - debtnc) / debt.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_sm63_sl21_2d_v062_signal(debtc, debtnc, debt, closeadj):
    base = _mean((debtc - debtnc) / debt.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_sm63_sl63_2d_v063_signal(debtc, debtnc, debt, closeadj):
    base = _mean((debtc - debtnc) / debt.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_sm252_sl63_2d_v064_signal(debtc, debtnc, debt, closeadj):
    base = _mean((debtc - debtnc) / debt.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_sm252_sl126_2d_v065_signal(debtc, debtnc, debt, closeadj):
    base = _mean((debtc - debtnc) / debt.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_sm21_sl21_2d_v066_signal(debtc, assets, closeadj):
    base = _mean(debtc / assets.replace(0, np.nan).abs(), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_sm63_sl21_2d_v067_signal(debtc, assets, closeadj):
    base = _mean(debtc / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_sm63_sl63_2d_v068_signal(debtc, assets, closeadj):
    base = _mean(debtc / assets.replace(0, np.nan).abs(), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_sm252_sl63_2d_v069_signal(debtc, assets, closeadj):
    base = _mean(debtc / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_sm252_sl126_2d_v070_signal(debtc, assets, closeadj):
    base = _mean(debtc / assets.replace(0, np.nan).abs(), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_pctslope_21d_2d_v071_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_pctslope_63d_2d_v072_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_pctslope_252d_2d_v073_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_pctslope_21d_2d_v074_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_pctslope_63d_2d_v075_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_pctslope_252d_2d_v076_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_pctslope_21d_2d_v077_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_pctslope_63d_2d_v078_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_pctslope_252d_2d_v079_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_pctslope_21d_2d_v080_signal(debtc, closeadj):
    base = debtc
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_pctslope_63d_2d_v081_signal(debtc, closeadj):
    base = debtc
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_pctslope_252d_2d_v082_signal(debtc, closeadj):
    base = debtc
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_pctslope_21d_2d_v083_signal(debtnc, closeadj):
    base = debtnc
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_pctslope_63d_2d_v084_signal(debtnc, closeadj):
    base = debtnc
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_pctslope_252d_2d_v085_signal(debtnc, closeadj):
    base = debtnc
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_pctslope_21d_2d_v086_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_pctslope_63d_2d_v087_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_pctslope_252d_2d_v088_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_pctslope_21d_2d_v089_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_pctslope_63d_2d_v090_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_pctslope_252d_2d_v091_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_sgnslope_21d_2d_v092_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_sgnslope_63d_2d_v093_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_sgnslope_252d_2d_v094_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_sgnslope_21d_2d_v095_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_sgnslope_63d_2d_v096_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_sgnslope_252d_2d_v097_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_sgnslope_21d_2d_v098_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_sgnslope_63d_2d_v099_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_sgnslope_252d_2d_v100_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_sgnslope_21d_2d_v101_signal(debtc, closeadj):
    base = debtc
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_sgnslope_63d_2d_v102_signal(debtc, closeadj):
    base = debtc
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_sgnslope_252d_2d_v103_signal(debtc, closeadj):
    base = debtc
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_sgnslope_21d_2d_v104_signal(debtnc, closeadj):
    base = debtnc
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_sgnslope_63d_2d_v105_signal(debtnc, closeadj):
    base = debtnc
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_sgnslope_252d_2d_v106_signal(debtnc, closeadj):
    base = debtnc
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_sgnslope_21d_2d_v107_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_sgnslope_63d_2d_v108_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_sgnslope_252d_2d_v109_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_sgnslope_21d_2d_v110_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_sgnslope_63d_2d_v111_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_sgnslope_252d_2d_v112_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_logmagslope_21d_2d_v113_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_logmagslope_63d_2d_v114_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_logmagslope_252d_2d_v115_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_logmagslope_21d_2d_v116_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_logmagslope_63d_2d_v117_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_logmagslope_252d_2d_v118_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_logmagslope_21d_2d_v119_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_logmagslope_63d_2d_v120_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_logmagslope_252d_2d_v121_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_logmagslope_21d_2d_v122_signal(debtc, closeadj):
    base = debtc
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_logmagslope_63d_2d_v123_signal(debtc, closeadj):
    base = debtc
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_logmagslope_252d_2d_v124_signal(debtc, closeadj):
    base = debtc
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_logmagslope_21d_2d_v125_signal(debtnc, closeadj):
    base = debtnc
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_logmagslope_63d_2d_v126_signal(debtnc, closeadj):
    base = debtnc
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_logmagslope_252d_2d_v127_signal(debtnc, closeadj):
    base = debtnc
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_logmagslope_21d_2d_v128_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_logmagslope_63d_2d_v129_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_logmagslope_252d_2d_v130_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_logmagslope_21d_2d_v131_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_logmagslope_63d_2d_v132_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_logmagslope_252d_2d_v133_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|debtc_share|
def f024dmm_f024_debt_maturity_mix_debtc_share_logslope_63d_2d_v134_signal(debtc, debt, closeadj):
    base = np.log((_f024_curshare(debtc, debt)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|debtc_share|
def f024dmm_f024_debt_maturity_mix_debtc_share_logslope_252d_2d_v135_signal(debtc, debt, closeadj):
    base = np.log((_f024_curshare(debtc, debt)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|debtnc_share|
def f024dmm_f024_debt_maturity_mix_debtnc_share_logslope_63d_2d_v136_signal(debtnc, debt, closeadj):
    base = np.log((debtnc / debt.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|debtnc_share|
def f024dmm_f024_debt_maturity_mix_debtnc_share_logslope_252d_2d_v137_signal(debtnc, debt, closeadj):
    base = np.log((debtnc / debt.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|debtc_to_cash|
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_logslope_63d_2d_v138_signal(debtc, cashneq, closeadj):
    base = np.log((debtc / cashneq.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|debtc_to_cash|
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_logslope_252d_2d_v139_signal(debtc, cashneq, closeadj):
    base = np.log((debtc / cashneq.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|debtc_lvl|
def f024dmm_f024_debt_maturity_mix_debtc_lvl_logslope_63d_2d_v140_signal(debtc, closeadj):
    base = np.log((debtc).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|debtc_lvl|
def f024dmm_f024_debt_maturity_mix_debtc_lvl_logslope_252d_2d_v141_signal(debtc, closeadj):
    base = np.log((debtc).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|debtnc_lvl|
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_logslope_63d_2d_v142_signal(debtnc, closeadj):
    base = np.log((debtnc).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|debtnc_lvl|
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_logslope_252d_2d_v143_signal(debtnc, closeadj):
    base = np.log((debtnc).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|maturity_skew|
def f024dmm_f024_debt_maturity_mix_maturity_skew_logslope_63d_2d_v144_signal(debtc, debtnc, debt, closeadj):
    base = np.log(((debtc - debtnc) / debt.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|maturity_skew|
def f024dmm_f024_debt_maturity_mix_maturity_skew_logslope_252d_2d_v145_signal(debtc, debtnc, debt, closeadj):
    base = np.log(((debtc - debtnc) / debt.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|debtc_to_asset|
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_logslope_63d_2d_v146_signal(debtc, assets, closeadj):
    base = np.log((debtc / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|debtc_to_asset|
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_logslope_252d_2d_v147_signal(debtc, assets, closeadj):
    base = np.log((debtc / assets.replace(0, np.nan).abs()).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

