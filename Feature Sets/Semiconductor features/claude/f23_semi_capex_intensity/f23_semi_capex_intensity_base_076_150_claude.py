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


def _max(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _min(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f23_daily_ffill(x, closeadj):
    return x.reindex(closeadj.index).ffill()


def _f23_ratio(a, b):
    return a / b.replace(0, np.nan)


def _f23_log_ratio(a, b):
    return np.log(a.replace(0, np.nan).abs() / b.replace(0, np.nan).abs())


# 21d z-score of log(capex/revenue)
def f23ci_f23_semi_capex_intensity_intensrv_logz_21d_base_v001_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / rv.abs().replace(0, np.nan))
    result = _z(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of log(capex/revenue)
def f23ci_f23_semi_capex_intensity_intensrv_logz_63d_base_v002_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / rv.abs().replace(0, np.nan))
    result = _z(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of log(capex/revenue)
def f23ci_f23_semi_capex_intensity_intensrv_logz_126d_base_v003_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / rv.abs().replace(0, np.nan))
    result = _z(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of log(capex/revenue)
def f23ci_f23_semi_capex_intensity_intensrv_logz_252d_base_v004_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / rv.abs().replace(0, np.nan))
    result = _z(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of log(capex/revenue)
def f23ci_f23_semi_capex_intensity_intensrv_logz_504d_base_v005_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / rv.abs().replace(0, np.nan))
    result = _z(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of log(capex/assets)
def f23ci_f23_semi_capex_intensity_intensas_logz_21d_base_v006_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / asx.abs().replace(0, np.nan))
    result = _z(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of log(capex/assets)
def f23ci_f23_semi_capex_intensity_intensas_logz_63d_base_v007_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / asx.abs().replace(0, np.nan))
    result = _z(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of log(capex/assets)
def f23ci_f23_semi_capex_intensity_intensas_logz_126d_base_v008_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / asx.abs().replace(0, np.nan))
    result = _z(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of log(capex/assets)
def f23ci_f23_semi_capex_intensity_intensas_logz_252d_base_v009_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / asx.abs().replace(0, np.nan))
    result = _z(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of log(capex/assets)
def f23ci_f23_semi_capex_intensity_intensas_logz_504d_base_v010_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / asx.abs().replace(0, np.nan))
    result = _z(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d z-score of log(capex/ppne)
def f23ci_f23_semi_capex_intensity_intenspp_logz_21d_base_v011_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / pp.abs().replace(0, np.nan))
    result = _z(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of log(capex/ppne)
def f23ci_f23_semi_capex_intensity_intenspp_logz_63d_base_v012_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / pp.abs().replace(0, np.nan))
    result = _z(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of log(capex/ppne)
def f23ci_f23_semi_capex_intensity_intenspp_logz_126d_base_v013_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / pp.abs().replace(0, np.nan))
    result = _z(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of log(capex/ppne)
def f23ci_f23_semi_capex_intensity_intenspp_logz_252d_base_v014_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / pp.abs().replace(0, np.nan))
    result = _z(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of log(capex/ppne)
def f23ci_f23_semi_capex_intensity_intenspp_logz_504d_base_v015_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    ratio = np.log(cx.abs().replace(0, np.nan) / pp.abs().replace(0, np.nan))
    result = _z(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_skew_21d_base_v016_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.rolling(21, min_periods=max(1, 21//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_skew_63d_base_v017_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.rolling(63, min_periods=max(1, 63//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_skew_126d_base_v018_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.rolling(126, min_periods=max(1, 126//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_skew_252d_base_v019_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_skew_504d_base_v020_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d kurtosis of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_kurt_21d_base_v021_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.rolling(21, min_periods=max(1, 21//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d kurtosis of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_kurt_63d_base_v022_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.rolling(63, min_periods=max(1, 63//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_kurt_126d_base_v023_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.rolling(126, min_periods=max(1, 126//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_kurt_252d_base_v024_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.rolling(252, min_periods=max(1, 252//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_kurt_504d_base_v025_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.rolling(504, min_periods=max(1, 504//2)).kurt()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d skew of capex/assets
def f23ci_f23_semi_capex_intensity_intensas_skew_21d_base_v026_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    result = ratio.rolling(21, min_periods=max(1, 21//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d skew of capex/assets
def f23ci_f23_semi_capex_intensity_intensas_skew_63d_base_v027_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    result = ratio.rolling(63, min_periods=max(1, 63//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d skew of capex/assets
def f23ci_f23_semi_capex_intensity_intensas_skew_126d_base_v028_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    result = ratio.rolling(126, min_periods=max(1, 126//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of capex/assets
def f23ci_f23_semi_capex_intensity_intensas_skew_252d_base_v029_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    result = ratio.rolling(252, min_periods=max(1, 252//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of capex/assets
def f23ci_f23_semi_capex_intensity_intensas_skew_504d_base_v030_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    ratio = cx / asx.replace(0, np.nan)
    result = ratio.rolling(504, min_periods=max(1, 504//2)).skew()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema fast(5) minus ema(21) on capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_ema_fast_21d_base_v031_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=21, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema fast(5) minus ema(63) on capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_ema_fast_63d_base_v032_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=63, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema fast(5) minus ema(126) on capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_ema_fast_126d_base_v033_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema fast(5) minus ema(252) on capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_ema_fast_252d_base_v034_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema fast(5) minus ema(504) on capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_ema_fast_504d_base_v035_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.ewm(span=5, adjust=False).mean() - ratio.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ema(21) minus ema(2x21) on capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_ema_slow_21d_base_v036_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.ewm(span=21, adjust=False).mean() - ratio.ewm(span=42, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ema(63) minus ema(2x63) on capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_ema_slow_63d_base_v037_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.ewm(span=63, adjust=False).mean() - ratio.ewm(span=126, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ema(126) minus ema(2x126) on capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_ema_slow_126d_base_v038_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.ewm(span=126, adjust=False).mean() - ratio.ewm(span=252, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ema(252) minus ema(2x252) on capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_ema_slow_252d_base_v039_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.ewm(span=252, adjust=False).mean() - ratio.ewm(span=504, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ema(504) minus ema(2x504) on capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_ema_slow_504d_base_v040_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.ewm(span=504, adjust=False).mean() - ratio.ewm(span=1008, adjust=False).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d above-mean mask fraction of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_hi_mask_21d_base_v041_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 21)
    result = (ratio > m).astype(float).rolling(21, min_periods=max(1, 21//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d above-mean mask fraction of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_hi_mask_63d_base_v042_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    result = (ratio > m).astype(float).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d above-mean mask fraction of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_hi_mask_126d_base_v043_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 126)
    result = (ratio > m).astype(float).rolling(126, min_periods=max(1, 126//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d above-mean mask fraction of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_hi_mask_252d_base_v044_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    result = (ratio > m).astype(float).rolling(252, min_periods=max(1, 252//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d above-mean mask fraction of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_hi_mask_504d_base_v045_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 504)
    result = (ratio > m).astype(float).rolling(504, min_periods=max(1, 504//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d below-mean mask fraction of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_lo_mask_21d_base_v046_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 21)
    result = (ratio < m).astype(float).rolling(21, min_periods=max(1, 21//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d below-mean mask fraction of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_lo_mask_63d_base_v047_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 63)
    result = (ratio < m).astype(float).rolling(63, min_periods=max(1, 63//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d below-mean mask fraction of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_lo_mask_126d_base_v048_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 126)
    result = (ratio < m).astype(float).rolling(126, min_periods=max(1, 126//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d below-mean mask fraction of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_lo_mask_252d_base_v049_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 252)
    result = (ratio < m).astype(float).rolling(252, min_periods=max(1, 252//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d below-mean mask fraction of capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_lo_mask_504d_base_v050_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    m = _mean(ratio, 504)
    result = (ratio < m).astype(float).rolling(504, min_periods=max(1, 504//2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d signed cum of capex/revenue innovations
def f23ci_f23_semi_capex_intensity_intensrv_signcum_21d_base_v051_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = pd.Series(np.sign(ratio.diff()), index=ratio.index).rolling(21, min_periods=max(1, 21//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d signed cum of capex/revenue innovations
def f23ci_f23_semi_capex_intensity_intensrv_signcum_63d_base_v052_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = pd.Series(np.sign(ratio.diff()), index=ratio.index).rolling(63, min_periods=max(1, 63//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d signed cum of capex/revenue innovations
def f23ci_f23_semi_capex_intensity_intensrv_signcum_126d_base_v053_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = pd.Series(np.sign(ratio.diff()), index=ratio.index).rolling(126, min_periods=max(1, 126//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d signed cum of capex/revenue innovations
def f23ci_f23_semi_capex_intensity_intensrv_signcum_252d_base_v054_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = pd.Series(np.sign(ratio.diff()), index=ratio.index).rolling(252, min_periods=max(1, 252//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d signed cum of capex/revenue innovations
def f23ci_f23_semi_capex_intensity_intensrv_signcum_504d_base_v055_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = pd.Series(np.sign(ratio.diff()), index=ratio.index).rolling(504, min_periods=max(1, 504//2)).sum()
    return result.replace([np.inf, -np.inf], np.nan)


# 21d run-up of capex/revenue from rolling trough
def f23ci_f23_semi_capex_intensity_intensrv_runup_21d_base_v056_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio - _min(ratio, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d run-up of capex/revenue from rolling trough
def f23ci_f23_semi_capex_intensity_intensrv_runup_63d_base_v057_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio - _min(ratio, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d run-up of capex/revenue from rolling trough
def f23ci_f23_semi_capex_intensity_intensrv_runup_126d_base_v058_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio - _min(ratio, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d run-up of capex/revenue from rolling trough
def f23ci_f23_semi_capex_intensity_intensrv_runup_252d_base_v059_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio - _min(ratio, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d run-up of capex/revenue from rolling trough
def f23ci_f23_semi_capex_intensity_intensrv_runup_504d_base_v060_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio - _min(ratio, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite z: capex/rev + capex/as + capex/pp
def f23ci_f23_semi_capex_intensity_intensmix_compos_21d_base_v061_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    r1 = cx / rv.replace(0, np.nan)
    r2 = cx / asx.replace(0, np.nan)
    r3 = cx / pp.replace(0, np.nan)
    result = _z(r1, 21) + _z(r2, 21) + _z(r3, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite z: capex/rev + capex/as + capex/pp
def f23ci_f23_semi_capex_intensity_intensmix_compos_63d_base_v062_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    r1 = cx / rv.replace(0, np.nan)
    r2 = cx / asx.replace(0, np.nan)
    r3 = cx / pp.replace(0, np.nan)
    result = _z(r1, 63) + _z(r2, 63) + _z(r3, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d composite z: capex/rev + capex/as + capex/pp
def f23ci_f23_semi_capex_intensity_intensmix_compos_126d_base_v063_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    r1 = cx / rv.replace(0, np.nan)
    r2 = cx / asx.replace(0, np.nan)
    r3 = cx / pp.replace(0, np.nan)
    result = _z(r1, 126) + _z(r2, 126) + _z(r3, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite z: capex/rev + capex/as + capex/pp
def f23ci_f23_semi_capex_intensity_intensmix_compos_252d_base_v064_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    r1 = cx / rv.replace(0, np.nan)
    r2 = cx / asx.replace(0, np.nan)
    r3 = cx / pp.replace(0, np.nan)
    result = _z(r1, 252) + _z(r2, 252) + _z(r3, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite z: capex/rev + capex/as + capex/pp
def f23ci_f23_semi_capex_intensity_intensmix_compos_504d_base_v065_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    asx = assets.reindex(closeadj.index).ffill()
    pp = ppne.reindex(closeadj.index).ffill()
    r1 = cx / rv.replace(0, np.nan)
    r2 = cx / asx.replace(0, np.nan)
    r3 = cx / pp.replace(0, np.nan)
    result = _z(r1, 504) + _z(r2, 504) + _z(r3, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d quartile rank of capex/revenue (0..1)
def f23ci_f23_semi_capex_intensity_intensrv_quartile_21d_base_v066_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.rolling(21, min_periods=max(1, 21//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d quartile rank of capex/revenue (0..1)
def f23ci_f23_semi_capex_intensity_intensrv_quartile_63d_base_v067_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.rolling(63, min_periods=max(1, 63//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d quartile rank of capex/revenue (0..1)
def f23ci_f23_semi_capex_intensity_intensrv_quartile_126d_base_v068_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.rolling(126, min_periods=max(1, 126//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d quartile rank of capex/revenue (0..1)
def f23ci_f23_semi_capex_intensity_intensrv_quartile_252d_base_v069_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.rolling(252, min_periods=max(1, 252//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d quartile rank of capex/revenue (0..1)
def f23ci_f23_semi_capex_intensity_intensrv_quartile_504d_base_v070_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    result = ratio.rolling(504, min_periods=max(1, 504//2)).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d deviation from median capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_devmedian_21d_base_v071_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(21, min_periods=max(1, 21//2)).median()
    result = ratio - med
    return result.replace([np.inf, -np.inf], np.nan)


# 63d deviation from median capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_devmedian_63d_base_v072_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(63, min_periods=max(1, 63//2)).median()
    result = ratio - med
    return result.replace([np.inf, -np.inf], np.nan)


# 126d deviation from median capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_devmedian_126d_base_v073_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(126, min_periods=max(1, 126//2)).median()
    result = ratio - med
    return result.replace([np.inf, -np.inf], np.nan)


# 252d deviation from median capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_devmedian_252d_base_v074_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(252, min_periods=max(1, 252//2)).median()
    result = ratio - med
    return result.replace([np.inf, -np.inf], np.nan)


# 504d deviation from median capex/revenue
def f23ci_f23_semi_capex_intensity_intensrv_devmedian_504d_base_v075_signal(capex, revenue, assets, ppne, closeadj):
    cx = capex.reindex(closeadj.index).ffill()
    rv = revenue.reindex(closeadj.index).ffill()
    ratio = cx / rv.replace(0, np.nan)
    med = ratio.rolling(504, min_periods=max(1, 504//2)).median()
    result = ratio - med
    return result.replace([np.inf, -np.inf], np.nan)
