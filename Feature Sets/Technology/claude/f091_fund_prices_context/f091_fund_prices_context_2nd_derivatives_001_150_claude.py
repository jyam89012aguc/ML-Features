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
def _f091_etf_rel(closeadj, etf_close):
    return closeadj.pct_change(periods=63) - etf_close.pct_change(periods=63)


# 21d slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_slope_21d_2d_v001_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_slope_63d_2d_v002_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_slope_126d_2d_v003_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_slope_252d_2d_v004_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_slope_504d_2d_v005_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_slope_21d_2d_v006_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_slope_63d_2d_v007_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_slope_126d_2d_v008_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_slope_252d_2d_v009_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_slope_504d_2d_v010_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_slope_21d_2d_v011_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_slope_63d_2d_v012_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_slope_126d_2d_v013_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_slope_252d_2d_v014_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_slope_504d_2d_v015_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_slope_21d_2d_v016_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_slope_63d_2d_v017_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_slope_126d_2d_v018_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_slope_252d_2d_v019_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_slope_504d_2d_v020_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_slope_21d_2d_v021_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_slope_63d_2d_v022_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_slope_126d_2d_v023_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_slope_252d_2d_v024_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_slope_504d_2d_v025_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_slope_21d_2d_v026_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_slope_63d_2d_v027_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_slope_126d_2d_v028_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_slope_252d_2d_v029_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_slope_504d_2d_v030_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d slope of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_slope_21d_2d_v031_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_slope_63d_2d_v032_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d slope of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_slope_126d_2d_v033_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_slope_252d_2d_v034_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d slope of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_slope_504d_2d_v035_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = _slope_diff_norm(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_sm21_sl21_2d_v036_signal(closeadj, xlk_close):
    base = _mean(_f091_etf_rel(closeadj, xlk_close), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_sm63_sl21_2d_v037_signal(closeadj, xlk_close):
    base = _mean(_f091_etf_rel(closeadj, xlk_close), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_sm63_sl63_2d_v038_signal(closeadj, xlk_close):
    base = _mean(_f091_etf_rel(closeadj, xlk_close), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_sm252_sl63_2d_v039_signal(closeadj, xlk_close):
    base = _mean(_f091_etf_rel(closeadj, xlk_close), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_sm252_sl126_2d_v040_signal(closeadj, xlk_close):
    base = _mean(_f091_etf_rel(closeadj, xlk_close), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_sm21_sl21_2d_v041_signal(closeadj, xlk_close):
    base = _mean(closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_sm63_sl21_2d_v042_signal(closeadj, xlk_close):
    base = _mean(closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_sm63_sl63_2d_v043_signal(closeadj, xlk_close):
    base = _mean(closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_sm252_sl63_2d_v044_signal(closeadj, xlk_close):
    base = _mean(closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_sm252_sl126_2d_v045_signal(closeadj, xlk_close):
    base = _mean(closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_sm21_sl21_2d_v046_signal(closeadj, smh_close):
    base = _mean(closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_sm63_sl21_2d_v047_signal(closeadj, smh_close):
    base = _mean(closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_sm63_sl63_2d_v048_signal(closeadj, smh_close):
    base = _mean(closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_sm252_sl63_2d_v049_signal(closeadj, smh_close):
    base = _mean(closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_sm252_sl126_2d_v050_signal(closeadj, smh_close):
    base = _mean(closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_sm21_sl21_2d_v051_signal(closeadj, igv_close):
    base = _mean(closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_sm63_sl21_2d_v052_signal(closeadj, igv_close):
    base = _mean(closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_sm63_sl63_2d_v053_signal(closeadj, igv_close):
    base = _mean(closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_sm252_sl63_2d_v054_signal(closeadj, igv_close):
    base = _mean(closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_sm252_sl126_2d_v055_signal(closeadj, igv_close):
    base = _mean(closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_sm21_sl21_2d_v056_signal(xlk_close, closeadj):
    base = _mean(xlk_close.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_sm63_sl21_2d_v057_signal(xlk_close, closeadj):
    base = _mean(xlk_close.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_sm63_sl63_2d_v058_signal(xlk_close, closeadj):
    base = _mean(xlk_close.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_sm252_sl63_2d_v059_signal(xlk_close, closeadj):
    base = _mean(xlk_close.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_sm252_sl126_2d_v060_signal(xlk_close, closeadj):
    base = _mean(xlk_close.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_sm21_sl21_2d_v061_signal(smh_close, closeadj):
    base = _mean(smh_close.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_sm63_sl21_2d_v062_signal(smh_close, closeadj):
    base = _mean(smh_close.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_sm63_sl63_2d_v063_signal(smh_close, closeadj):
    base = _mean(smh_close.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_sm252_sl63_2d_v064_signal(smh_close, closeadj):
    base = _mean(smh_close.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_sm252_sl126_2d_v065_signal(smh_close, closeadj):
    base = _mean(smh_close.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d smooth then 21d slope of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_sm21_sl21_2d_v066_signal(igv_close, closeadj):
    base = _mean(igv_close.pct_change(periods=252), 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 21d slope of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_sm63_sl21_2d_v067_signal(igv_close, closeadj):
    base = _mean(igv_close.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d smooth then 63d slope of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_sm63_sl63_2d_v068_signal(igv_close, closeadj):
    base = _mean(igv_close.pct_change(periods=252), 63)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 63d slope of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_sm252_sl63_2d_v069_signal(igv_close, closeadj):
    base = _mean(igv_close.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d smooth then 126d slope of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_sm252_sl126_2d_v070_signal(igv_close, closeadj):
    base = _mean(igv_close.pct_change(periods=252), 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_pctslope_21d_2d_v071_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_pctslope_63d_2d_v072_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_pctslope_252d_2d_v073_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_pctslope_21d_2d_v074_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_pctslope_63d_2d_v075_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_pctslope_252d_2d_v076_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_pctslope_21d_2d_v077_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_pctslope_63d_2d_v078_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_pctslope_252d_2d_v079_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_pctslope_21d_2d_v080_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_pctslope_63d_2d_v081_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_pctslope_252d_2d_v082_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_pctslope_21d_2d_v083_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_pctslope_63d_2d_v084_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_pctslope_252d_2d_v085_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_pctslope_21d_2d_v086_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_pctslope_63d_2d_v087_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_pctslope_252d_2d_v088_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d pct-change slope of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_pctslope_21d_2d_v089_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d pct-change slope of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_pctslope_63d_2d_v090_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d pct-change slope of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_pctslope_252d_2d_v091_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_sgnslope_21d_2d_v092_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_sgnslope_63d_2d_v093_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_sgnslope_252d_2d_v094_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_sgnslope_21d_2d_v095_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_sgnslope_63d_2d_v096_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_sgnslope_252d_2d_v097_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_sgnslope_21d_2d_v098_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_sgnslope_63d_2d_v099_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_sgnslope_252d_2d_v100_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_sgnslope_21d_2d_v101_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_sgnslope_63d_2d_v102_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_sgnslope_252d_2d_v103_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_sgnslope_21d_2d_v104_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_sgnslope_63d_2d_v105_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_sgnslope_252d_2d_v106_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_sgnslope_21d_2d_v107_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_sgnslope_63d_2d_v108_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_sgnslope_252d_2d_v109_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 21d slope of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_sgnslope_21d_2d_v110_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 63d slope of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_sgnslope_63d_2d_v111_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# sign of 252d slope of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_sgnslope_252d_2d_v112_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_logmagslope_21d_2d_v113_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_logmagslope_63d_2d_v114_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_logmagslope_252d_2d_v115_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_logmagslope_21d_2d_v116_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_logmagslope_63d_2d_v117_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_logmagslope_252d_2d_v118_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_logmagslope_21d_2d_v119_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_logmagslope_63d_2d_v120_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_logmagslope_252d_2d_v121_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_logmagslope_21d_2d_v122_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_logmagslope_63d_2d_v123_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_logmagslope_252d_2d_v124_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_logmagslope_21d_2d_v125_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_logmagslope_63d_2d_v126_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_logmagslope_252d_2d_v127_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_logmagslope_21d_2d_v128_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_logmagslope_63d_2d_v129_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_logmagslope_252d_2d_v130_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 21d slope of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_logmagslope_21d_2d_v131_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 21)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 63d slope of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_logmagslope_63d_2d_v132_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 63)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# log-magnitude × sign of 252d slope of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_logmagslope_252d_2d_v133_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    s = _slope_diff_norm(base, 252)
    result = np.log(s.abs().replace(0, np.nan)) * np.sign(s) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rel_xlk_63d|
def f091fnd_f091_fund_prices_context_rel_xlk_63d_logslope_63d_2d_v134_signal(closeadj, xlk_close):
    base = np.log((_f091_etf_rel(closeadj, xlk_close)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rel_xlk_63d|
def f091fnd_f091_fund_prices_context_rel_xlk_63d_logslope_252d_2d_v135_signal(closeadj, xlk_close):
    base = np.log((_f091_etf_rel(closeadj, xlk_close)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rel_xlk_252d|
def f091fnd_f091_fund_prices_context_rel_xlk_252d_logslope_63d_2d_v136_signal(closeadj, xlk_close):
    base = np.log((closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rel_xlk_252d|
def f091fnd_f091_fund_prices_context_rel_xlk_252d_logslope_252d_2d_v137_signal(closeadj, xlk_close):
    base = np.log((closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rel_smh_252d|
def f091fnd_f091_fund_prices_context_rel_smh_252d_logslope_63d_2d_v138_signal(closeadj, smh_close):
    base = np.log((closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rel_smh_252d|
def f091fnd_f091_fund_prices_context_rel_smh_252d_logslope_252d_2d_v139_signal(closeadj, smh_close):
    base = np.log((closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|rel_igv_252d|
def f091fnd_f091_fund_prices_context_rel_igv_252d_logslope_63d_2d_v140_signal(closeadj, igv_close):
    base = np.log((closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|rel_igv_252d|
def f091fnd_f091_fund_prices_context_rel_igv_252d_logslope_252d_2d_v141_signal(closeadj, igv_close):
    base = np.log((closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|xlk_trend_252|
def f091fnd_f091_fund_prices_context_xlk_trend_252_logslope_63d_2d_v142_signal(xlk_close, closeadj):
    base = np.log((xlk_close.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|xlk_trend_252|
def f091fnd_f091_fund_prices_context_xlk_trend_252_logslope_252d_2d_v143_signal(xlk_close, closeadj):
    base = np.log((xlk_close.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|smh_trend_252|
def f091fnd_f091_fund_prices_context_smh_trend_252_logslope_63d_2d_v144_signal(smh_close, closeadj):
    base = np.log((smh_close.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|smh_trend_252|
def f091fnd_f091_fund_prices_context_smh_trend_252_logslope_252d_2d_v145_signal(smh_close, closeadj):
    base = np.log((smh_close.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d slope of log|igv_trend_252|
def f091fnd_f091_fund_prices_context_igv_trend_252_logslope_63d_2d_v146_signal(igv_close, closeadj):
    base = np.log((igv_close.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d slope of log|igv_trend_252|
def f091fnd_f091_fund_prices_context_igv_trend_252_logslope_252d_2d_v147_signal(igv_close, closeadj):
    base = np.log((igv_close.pct_change(periods=252)).abs().replace(0, np.nan))
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

