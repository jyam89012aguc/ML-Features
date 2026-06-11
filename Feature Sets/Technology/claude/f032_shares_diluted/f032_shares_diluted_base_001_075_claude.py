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
def _f032_dil_spread(shareswadil, sharesbas):
    return (shareswadil - sharesbas) / sharesbas.replace(0, np.nan).abs()


# 21d mean of shareswa_lvl scaled by closeadj
def f032shd_f032_shares_diluted_shareswa_lvl_mean_21d_base_v001_signal(shareswa, closeadj):
    base = shareswa
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of shareswa_lvl scaled by closeadj
def f032shd_f032_shares_diluted_shareswa_lvl_mean_63d_base_v002_signal(shareswa, closeadj):
    base = shareswa
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of shareswa_lvl scaled by closeadj
def f032shd_f032_shares_diluted_shareswa_lvl_mean_126d_base_v003_signal(shareswa, closeadj):
    base = shareswa
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of shareswa_lvl scaled by closeadj
def f032shd_f032_shares_diluted_shareswa_lvl_mean_252d_base_v004_signal(shareswa, closeadj):
    base = shareswa
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of shareswa_lvl scaled by closeadj
def f032shd_f032_shares_diluted_shareswa_lvl_mean_504d_base_v005_signal(shareswa, closeadj):
    base = shareswa
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of shareswadil_lvl scaled by closeadj
def f032shd_f032_shares_diluted_shareswadil_lvl_mean_21d_base_v006_signal(shareswadil, closeadj):
    base = shareswadil
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of shareswadil_lvl scaled by closeadj
def f032shd_f032_shares_diluted_shareswadil_lvl_mean_63d_base_v007_signal(shareswadil, closeadj):
    base = shareswadil
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of shareswadil_lvl scaled by closeadj
def f032shd_f032_shares_diluted_shareswadil_lvl_mean_126d_base_v008_signal(shareswadil, closeadj):
    base = shareswadil
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of shareswadil_lvl scaled by closeadj
def f032shd_f032_shares_diluted_shareswadil_lvl_mean_252d_base_v009_signal(shareswadil, closeadj):
    base = shareswadil
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of shareswadil_lvl scaled by closeadj
def f032shd_f032_shares_diluted_shareswadil_lvl_mean_504d_base_v010_signal(shareswadil, closeadj):
    base = shareswadil
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dil_spread scaled by closeadj
def f032shd_f032_shares_diluted_dil_spread_mean_21d_base_v011_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dil_spread scaled by closeadj
def f032shd_f032_shares_diluted_dil_spread_mean_63d_base_v012_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dil_spread scaled by closeadj
def f032shd_f032_shares_diluted_dil_spread_mean_126d_base_v013_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dil_spread scaled by closeadj
def f032shd_f032_shares_diluted_dil_spread_mean_252d_base_v014_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dil_spread scaled by closeadj
def f032shd_f032_shares_diluted_dil_spread_mean_504d_base_v015_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dilbasic_ratio scaled by closeadj
def f032shd_f032_shares_diluted_dilbasic_ratio_mean_21d_base_v016_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dilbasic_ratio scaled by closeadj
def f032shd_f032_shares_diluted_dilbasic_ratio_mean_63d_base_v017_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dilbasic_ratio scaled by closeadj
def f032shd_f032_shares_diluted_dilbasic_ratio_mean_126d_base_v018_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dilbasic_ratio scaled by closeadj
def f032shd_f032_shares_diluted_dilbasic_ratio_mean_252d_base_v019_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dilbasic_ratio scaled by closeadj
def f032shd_f032_shares_diluted_dilbasic_ratio_mean_504d_base_v020_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of shareswa_yoy scaled by closeadj
def f032shd_f032_shares_diluted_shareswa_yoy_mean_21d_base_v021_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of shareswa_yoy scaled by closeadj
def f032shd_f032_shares_diluted_shareswa_yoy_mean_63d_base_v022_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of shareswa_yoy scaled by closeadj
def f032shd_f032_shares_diluted_shareswa_yoy_mean_126d_base_v023_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of shareswa_yoy scaled by closeadj
def f032shd_f032_shares_diluted_shareswa_yoy_mean_252d_base_v024_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of shareswa_yoy scaled by closeadj
def f032shd_f032_shares_diluted_shareswa_yoy_mean_504d_base_v025_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of shareswadil_yoy scaled by closeadj
def f032shd_f032_shares_diluted_shareswadil_yoy_mean_21d_base_v026_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of shareswadil_yoy scaled by closeadj
def f032shd_f032_shares_diluted_shareswadil_yoy_mean_63d_base_v027_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of shareswadil_yoy scaled by closeadj
def f032shd_f032_shares_diluted_shareswadil_yoy_mean_126d_base_v028_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of shareswadil_yoy scaled by closeadj
def f032shd_f032_shares_diluted_shareswadil_yoy_mean_252d_base_v029_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of shareswadil_yoy scaled by closeadj
def f032shd_f032_shares_diluted_shareswadil_yoy_mean_504d_base_v030_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of dilution_overhang scaled by closeadj
def f032shd_f032_shares_diluted_dilution_overhang_mean_21d_base_v031_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of dilution_overhang scaled by closeadj
def f032shd_f032_shares_diluted_dilution_overhang_mean_63d_base_v032_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of dilution_overhang scaled by closeadj
def f032shd_f032_shares_diluted_dilution_overhang_mean_126d_base_v033_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of dilution_overhang scaled by closeadj
def f032shd_f032_shares_diluted_dilution_overhang_mean_252d_base_v034_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of dilution_overhang scaled by closeadj
def f032shd_f032_shares_diluted_dilution_overhang_mean_504d_base_v035_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_median_63d_base_v036_signal(shareswa, closeadj):
    base = shareswa
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_median_252d_base_v037_signal(shareswa, closeadj):
    base = shareswa
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_median_504d_base_v038_signal(shareswa, closeadj):
    base = shareswa
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_median_63d_base_v039_signal(shareswadil, closeadj):
    base = shareswadil
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_median_252d_base_v040_signal(shareswadil, closeadj):
    base = shareswadil
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_median_504d_base_v041_signal(shareswadil, closeadj):
    base = shareswadil
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of dil_spread
def f032shd_f032_shares_diluted_dil_spread_median_63d_base_v042_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of dil_spread
def f032shd_f032_shares_diluted_dil_spread_median_252d_base_v043_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of dil_spread
def f032shd_f032_shares_diluted_dil_spread_median_504d_base_v044_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_median_63d_base_v045_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_median_252d_base_v046_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_median_504d_base_v047_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_median_63d_base_v048_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_median_252d_base_v049_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_median_504d_base_v050_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_median_63d_base_v051_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_median_252d_base_v052_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_median_504d_base_v053_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_median_63d_base_v054_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_median_252d_base_v055_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_median_504d_base_v056_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_rmax_252d_base_v057_signal(shareswa, closeadj):
    base = shareswa
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_rmax_504d_base_v058_signal(shareswa, closeadj):
    base = shareswa
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_rmax_252d_base_v059_signal(shareswadil, closeadj):
    base = shareswadil
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_rmax_504d_base_v060_signal(shareswadil, closeadj):
    base = shareswadil
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of dil_spread
def f032shd_f032_shares_diluted_dil_spread_rmax_252d_base_v061_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of dil_spread
def f032shd_f032_shares_diluted_dil_spread_rmax_504d_base_v062_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_rmax_252d_base_v063_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of dilbasic_ratio
def f032shd_f032_shares_diluted_dilbasic_ratio_rmax_504d_base_v064_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil / sharesbas.replace(0, np.nan).abs()
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_rmax_252d_base_v065_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of shareswa_yoy
def f032shd_f032_shares_diluted_shareswa_yoy_rmax_504d_base_v066_signal(shareswa, closeadj):
    base = shareswa.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_rmax_252d_base_v067_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of shareswadil_yoy
def f032shd_f032_shares_diluted_shareswadil_yoy_rmax_504d_base_v068_signal(shareswadil, closeadj):
    base = shareswadil.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_rmax_252d_base_v069_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of dilution_overhang
def f032shd_f032_shares_diluted_dilution_overhang_rmax_504d_base_v070_signal(shareswadil, sharesbas, closeadj):
    base = shareswadil - sharesbas
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_rmin_252d_base_v071_signal(shareswa, closeadj):
    base = shareswa
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of shareswa_lvl
def f032shd_f032_shares_diluted_shareswa_lvl_rmin_504d_base_v072_signal(shareswa, closeadj):
    base = shareswa
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_rmin_252d_base_v073_signal(shareswadil, closeadj):
    base = shareswadil
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of shareswadil_lvl
def f032shd_f032_shares_diluted_shareswadil_lvl_rmin_504d_base_v074_signal(shareswadil, closeadj):
    base = shareswadil
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of dil_spread
def f032shd_f032_shares_diluted_dil_spread_rmin_252d_base_v075_signal(shareswadil, sharesbas, closeadj):
    base = _f032_dil_spread(shareswadil, sharesbas)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

