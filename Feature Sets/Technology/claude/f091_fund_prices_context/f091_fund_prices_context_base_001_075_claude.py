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
def _f091_etf_rel(closeadj, etf_close):
    return closeadj.pct_change(periods=63) - etf_close.pct_change(periods=63)


# 21d mean of rel_xlk_63d scaled by closeadj
def f091fnd_f091_fund_prices_context_rel_xlk_63d_mean_21d_base_v001_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rel_xlk_63d scaled by closeadj
def f091fnd_f091_fund_prices_context_rel_xlk_63d_mean_63d_base_v002_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rel_xlk_63d scaled by closeadj
def f091fnd_f091_fund_prices_context_rel_xlk_63d_mean_126d_base_v003_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rel_xlk_63d scaled by closeadj
def f091fnd_f091_fund_prices_context_rel_xlk_63d_mean_252d_base_v004_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rel_xlk_63d scaled by closeadj
def f091fnd_f091_fund_prices_context_rel_xlk_63d_mean_504d_base_v005_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rel_xlk_252d scaled by closeadj
def f091fnd_f091_fund_prices_context_rel_xlk_252d_mean_21d_base_v006_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rel_xlk_252d scaled by closeadj
def f091fnd_f091_fund_prices_context_rel_xlk_252d_mean_63d_base_v007_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rel_xlk_252d scaled by closeadj
def f091fnd_f091_fund_prices_context_rel_xlk_252d_mean_126d_base_v008_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rel_xlk_252d scaled by closeadj
def f091fnd_f091_fund_prices_context_rel_xlk_252d_mean_252d_base_v009_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rel_xlk_252d scaled by closeadj
def f091fnd_f091_fund_prices_context_rel_xlk_252d_mean_504d_base_v010_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rel_smh_252d scaled by closeadj
def f091fnd_f091_fund_prices_context_rel_smh_252d_mean_21d_base_v011_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rel_smh_252d scaled by closeadj
def f091fnd_f091_fund_prices_context_rel_smh_252d_mean_63d_base_v012_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rel_smh_252d scaled by closeadj
def f091fnd_f091_fund_prices_context_rel_smh_252d_mean_126d_base_v013_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rel_smh_252d scaled by closeadj
def f091fnd_f091_fund_prices_context_rel_smh_252d_mean_252d_base_v014_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rel_smh_252d scaled by closeadj
def f091fnd_f091_fund_prices_context_rel_smh_252d_mean_504d_base_v015_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of rel_igv_252d scaled by closeadj
def f091fnd_f091_fund_prices_context_rel_igv_252d_mean_21d_base_v016_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of rel_igv_252d scaled by closeadj
def f091fnd_f091_fund_prices_context_rel_igv_252d_mean_63d_base_v017_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of rel_igv_252d scaled by closeadj
def f091fnd_f091_fund_prices_context_rel_igv_252d_mean_126d_base_v018_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of rel_igv_252d scaled by closeadj
def f091fnd_f091_fund_prices_context_rel_igv_252d_mean_252d_base_v019_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of rel_igv_252d scaled by closeadj
def f091fnd_f091_fund_prices_context_rel_igv_252d_mean_504d_base_v020_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of xlk_trend_252 scaled by closeadj
def f091fnd_f091_fund_prices_context_xlk_trend_252_mean_21d_base_v021_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of xlk_trend_252 scaled by closeadj
def f091fnd_f091_fund_prices_context_xlk_trend_252_mean_63d_base_v022_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of xlk_trend_252 scaled by closeadj
def f091fnd_f091_fund_prices_context_xlk_trend_252_mean_126d_base_v023_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of xlk_trend_252 scaled by closeadj
def f091fnd_f091_fund_prices_context_xlk_trend_252_mean_252d_base_v024_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of xlk_trend_252 scaled by closeadj
def f091fnd_f091_fund_prices_context_xlk_trend_252_mean_504d_base_v025_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of smh_trend_252 scaled by closeadj
def f091fnd_f091_fund_prices_context_smh_trend_252_mean_21d_base_v026_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of smh_trend_252 scaled by closeadj
def f091fnd_f091_fund_prices_context_smh_trend_252_mean_63d_base_v027_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of smh_trend_252 scaled by closeadj
def f091fnd_f091_fund_prices_context_smh_trend_252_mean_126d_base_v028_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of smh_trend_252 scaled by closeadj
def f091fnd_f091_fund_prices_context_smh_trend_252_mean_252d_base_v029_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of smh_trend_252 scaled by closeadj
def f091fnd_f091_fund_prices_context_smh_trend_252_mean_504d_base_v030_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 21d mean of igv_trend_252 scaled by closeadj
def f091fnd_f091_fund_prices_context_igv_trend_252_mean_21d_base_v031_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = _mean(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d mean of igv_trend_252 scaled by closeadj
def f091fnd_f091_fund_prices_context_igv_trend_252_mean_63d_base_v032_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 126d mean of igv_trend_252 scaled by closeadj
def f091fnd_f091_fund_prices_context_igv_trend_252_mean_126d_base_v033_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = _mean(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d mean of igv_trend_252 scaled by closeadj
def f091fnd_f091_fund_prices_context_igv_trend_252_mean_252d_base_v034_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d mean of igv_trend_252 scaled by closeadj
def f091fnd_f091_fund_prices_context_igv_trend_252_mean_504d_base_v035_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = _mean(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_median_63d_base_v036_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_median_252d_base_v037_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_median_504d_base_v038_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_median_63d_base_v039_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_median_252d_base_v040_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_median_504d_base_v041_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_median_63d_base_v042_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_median_252d_base_v043_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_median_504d_base_v044_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_median_63d_base_v045_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_median_252d_base_v046_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_median_504d_base_v047_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_median_63d_base_v048_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_median_252d_base_v049_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_median_504d_base_v050_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_median_63d_base_v051_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_median_252d_base_v052_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_median_504d_base_v053_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 63d rolling median of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_median_63d_base_v054_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = base.rolling(63, min_periods=max(1, 63//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling median of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_median_252d_base_v055_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling median of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_median_504d_base_v056_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_rmax_252d_base_v057_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_rmax_504d_base_v058_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_rmax_252d_base_v059_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_rmax_504d_base_v060_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_rmax_252d_base_v061_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_rmax_504d_base_v062_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_rmax_252d_base_v063_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of rel_igv_252d
def f091fnd_f091_fund_prices_context_rel_igv_252d_rmax_504d_base_v064_signal(closeadj, igv_close):
    base = closeadj.pct_change(periods=252) - igv_close.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_rmax_252d_base_v065_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of xlk_trend_252
def f091fnd_f091_fund_prices_context_xlk_trend_252_rmax_504d_base_v066_signal(xlk_close, closeadj):
    base = xlk_close.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_rmax_252d_base_v067_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of smh_trend_252
def f091fnd_f091_fund_prices_context_smh_trend_252_rmax_504d_base_v068_signal(smh_close, closeadj):
    base = smh_close.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling max of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_rmax_252d_base_v069_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling max of igv_trend_252
def f091fnd_f091_fund_prices_context_igv_trend_252_rmax_504d_base_v070_signal(igv_close, closeadj):
    base = igv_close.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_rmin_252d_base_v071_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of rel_xlk_63d
def f091fnd_f091_fund_prices_context_rel_xlk_63d_rmin_504d_base_v072_signal(closeadj, xlk_close):
    base = _f091_etf_rel(closeadj, xlk_close)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_rmin_252d_base_v073_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 504d rolling min of rel_xlk_252d
def f091fnd_f091_fund_prices_context_rel_xlk_252d_rmin_504d_base_v074_signal(closeadj, xlk_close):
    base = closeadj.pct_change(periods=252) - xlk_close.pct_change(periods=252)
    result = base.rolling(504, min_periods=max(1, 504//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

# 252d rolling min of rel_smh_252d
def f091fnd_f091_fund_prices_context_rel_smh_252d_rmin_252d_base_v075_signal(closeadj, smh_close):
    base = closeadj.pct_change(periods=252) - smh_close.pct_change(periods=252)
    result = base.rolling(252, min_periods=max(1, 252//2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

