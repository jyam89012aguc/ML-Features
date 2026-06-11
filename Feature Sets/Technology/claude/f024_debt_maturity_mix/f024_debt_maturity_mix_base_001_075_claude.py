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


def _pct_change(s, n):
    return s.pct_change(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f024_curshare(debtc, debt):
    return debtc / debt.replace(0, np.nan).abs()


# 21d mean of debtc_share scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtc_share_mean_21d_base_v001_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of debtc_share scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtc_share_mean_63d_base_v002_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of debtc_share scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtc_share_mean_126d_base_v003_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of debtc_share scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtc_share_mean_252d_base_v004_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of debtc_share scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtc_share_mean_504d_base_v005_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of debtnc_share scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtnc_share_mean_21d_base_v006_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of debtnc_share scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtnc_share_mean_63d_base_v007_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of debtnc_share scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtnc_share_mean_126d_base_v008_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of debtnc_share scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtnc_share_mean_252d_base_v009_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of debtnc_share scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtnc_share_mean_504d_base_v010_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of debtc_to_cash scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_mean_21d_base_v011_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of debtc_to_cash scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_mean_63d_base_v012_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of debtc_to_cash scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_mean_126d_base_v013_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of debtc_to_cash scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_mean_252d_base_v014_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of debtc_to_cash scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_mean_504d_base_v015_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of debtc_lvl scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtc_lvl_mean_21d_base_v016_signal(debtc, closeadj):
    base = debtc
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of debtc_lvl scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtc_lvl_mean_63d_base_v017_signal(debtc, closeadj):
    base = debtc
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of debtc_lvl scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtc_lvl_mean_126d_base_v018_signal(debtc, closeadj):
    base = debtc
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of debtc_lvl scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtc_lvl_mean_252d_base_v019_signal(debtc, closeadj):
    base = debtc
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of debtc_lvl scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtc_lvl_mean_504d_base_v020_signal(debtc, closeadj):
    base = debtc
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of debtnc_lvl scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_mean_21d_base_v021_signal(debtnc, closeadj):
    base = debtnc
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of debtnc_lvl scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_mean_63d_base_v022_signal(debtnc, closeadj):
    base = debtnc
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of debtnc_lvl scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_mean_126d_base_v023_signal(debtnc, closeadj):
    base = debtnc
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of debtnc_lvl scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_mean_252d_base_v024_signal(debtnc, closeadj):
    base = debtnc
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of debtnc_lvl scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_mean_504d_base_v025_signal(debtnc, closeadj):
    base = debtnc
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of maturity_skew scaled by closeadj
def f024dmm_f024_debt_maturity_mix_maturity_skew_mean_21d_base_v026_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of maturity_skew scaled by closeadj
def f024dmm_f024_debt_maturity_mix_maturity_skew_mean_63d_base_v027_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of maturity_skew scaled by closeadj
def f024dmm_f024_debt_maturity_mix_maturity_skew_mean_126d_base_v028_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of maturity_skew scaled by closeadj
def f024dmm_f024_debt_maturity_mix_maturity_skew_mean_252d_base_v029_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of maturity_skew scaled by closeadj
def f024dmm_f024_debt_maturity_mix_maturity_skew_mean_504d_base_v030_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of debtc_to_asset scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_mean_21d_base_v031_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of debtc_to_asset scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_mean_63d_base_v032_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of debtc_to_asset scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_mean_126d_base_v033_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of debtc_to_asset scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_mean_252d_base_v034_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of debtc_to_asset scaled by closeadj
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_mean_504d_base_v035_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_median_63d_base_v036_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_median_252d_base_v037_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_median_504d_base_v038_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_median_63d_base_v039_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_median_252d_base_v040_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_median_504d_base_v041_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_median_63d_base_v042_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_median_252d_base_v043_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_median_504d_base_v044_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_median_63d_base_v045_signal(debtc, closeadj):
    base = debtc
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_median_252d_base_v046_signal(debtc, closeadj):
    base = debtc
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_median_504d_base_v047_signal(debtc, closeadj):
    base = debtc
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_median_63d_base_v048_signal(debtnc, closeadj):
    base = debtnc
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_median_252d_base_v049_signal(debtnc, closeadj):
    base = debtnc
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_median_504d_base_v050_signal(debtnc, closeadj):
    base = debtnc
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_median_63d_base_v051_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_median_252d_base_v052_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_median_504d_base_v053_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_median_63d_base_v054_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_median_252d_base_v055_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_median_504d_base_v056_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_rmax_252d_base_v057_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_rmax_504d_base_v058_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_rmax_252d_base_v059_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_rmax_504d_base_v060_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_rmax_252d_base_v061_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_rmax_504d_base_v062_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_rmax_252d_base_v063_signal(debtc, closeadj):
    base = debtc
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of debtc_lvl
def f024dmm_f024_debt_maturity_mix_debtc_lvl_rmax_504d_base_v064_signal(debtc, closeadj):
    base = debtc
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_rmax_252d_base_v065_signal(debtnc, closeadj):
    base = debtnc
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of debtnc_lvl
def f024dmm_f024_debt_maturity_mix_debtnc_lvl_rmax_504d_base_v066_signal(debtnc, closeadj):
    base = debtnc
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_rmax_252d_base_v067_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of maturity_skew
def f024dmm_f024_debt_maturity_mix_maturity_skew_rmax_504d_base_v068_signal(debtc, debtnc, debt, closeadj):
    base = (debtc - debtnc) / debt.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_rmax_252d_base_v069_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of debtc_to_asset
def f024dmm_f024_debt_maturity_mix_debtc_to_asset_rmax_504d_base_v070_signal(debtc, assets, closeadj):
    base = debtc / assets.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_rmin_252d_base_v071_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of debtc_share
def f024dmm_f024_debt_maturity_mix_debtc_share_rmin_504d_base_v072_signal(debtc, debt, closeadj):
    base = _f024_curshare(debtc, debt)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_rmin_252d_base_v073_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of debtnc_share
def f024dmm_f024_debt_maturity_mix_debtnc_share_rmin_504d_base_v074_signal(debtnc, debt, closeadj):
    base = debtnc / debt.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of debtc_to_cash
def f024dmm_f024_debt_maturity_mix_debtc_to_cash_rmin_252d_base_v075_signal(debtc, cashneq, closeadj):
    base = debtc / cashneq.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

