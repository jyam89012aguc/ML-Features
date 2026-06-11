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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f057_trend_fit(close, w):
    # Fitted linear trend value approximated by rolling mean of log-price + slope*half_window
    lp = np.log(close.replace(0, np.nan).abs())
    m = lp.rolling(w, min_periods=max(1, w // 2)).mean()
    slope = (lp - lp.shift(w)) / float(w)
    return m + slope * (w / 2.0)


def _f057_trend_r2(close, w):
    # R^2 proxy: 1 - variance(residual) / variance(log price)
    lp = np.log(close.replace(0, np.nan).abs())
    var_total = lp.rolling(w, min_periods=max(1, w // 2)).var()
    slope = (lp - lp.shift(w)) / float(w)
    # residual variance proxy: total variance minus explained (slope^2 * (w^2-1)/12)
    explained = (slope * slope) * (w * w - 1) / 12.0
    return 1.0 - (var_total - explained) / var_total.replace(0, np.nan)


def _f057_smoothness_score(close, w):
    # Smoothness: inverse of normalized rolling std of returns
    ret = close.pct_change()
    sd = ret.rolling(w, min_periods=max(1, w // 2)).std()
    m_abs = ret.abs().rolling(w, min_periods=max(1, w // 2)).mean()
    return m_abs / sd.replace(0, np.nan)



# tfit base_w=5 variant=xclose slope_w=5
def f057trq_f057_trend_r2_tfit_5d_xclose_slope_v001_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xclose slope_w=10
def f057trq_f057_trend_r2_tfit_5d_xclose_slope_v002_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xclose slope_w=21
def f057trq_f057_trend_r2_tfit_5d_xclose_slope_v003_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xclose slope_w=42
def f057trq_f057_trend_r2_tfit_5d_xclose_slope_v004_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xclose slope_w=63
def f057trq_f057_trend_r2_tfit_5d_xclose_slope_v005_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xclose slope_w=126
def f057trq_f057_trend_r2_tfit_5d_xclose_slope_v006_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmean21 slope_w=5
def f057trq_f057_trend_r2_tfit_5d_xmean21_slope_v007_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmean21 slope_w=10
def f057trq_f057_trend_r2_tfit_5d_xmean21_slope_v008_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmean21 slope_w=21
def f057trq_f057_trend_r2_tfit_5d_xmean21_slope_v009_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmean21 slope_w=42
def f057trq_f057_trend_r2_tfit_5d_xmean21_slope_v010_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmean21 slope_w=63
def f057trq_f057_trend_r2_tfit_5d_xmean21_slope_v011_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * _mean(closeadj, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmean21 slope_w=126
def f057trq_f057_trend_r2_tfit_5d_xmean21_slope_v012_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmean63 slope_w=5
def f057trq_f057_trend_r2_tfit_5d_xmean63_slope_v013_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * _mean(closeadj, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmean63 slope_w=10
def f057trq_f057_trend_r2_tfit_5d_xmean63_slope_v014_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmean63 slope_w=21
def f057trq_f057_trend_r2_tfit_5d_xmean63_slope_v015_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * _mean(closeadj, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmean63 slope_w=42
def f057trq_f057_trend_r2_tfit_5d_xmean63_slope_v016_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmean63 slope_w=63
def f057trq_f057_trend_r2_tfit_5d_xmean63_slope_v017_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * _mean(closeadj, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmean63 slope_w=126
def f057trq_f057_trend_r2_tfit_5d_xmean63_slope_v018_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xstd63 slope_w=5
def f057trq_f057_trend_r2_tfit_5d_xstd63_slope_v019_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * _std(closeadj, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xstd63 slope_w=10
def f057trq_f057_trend_r2_tfit_5d_xstd63_slope_v020_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * _std(closeadj, 63)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xstd63 slope_w=21
def f057trq_f057_trend_r2_tfit_5d_xstd63_slope_v021_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * _std(closeadj, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xstd63 slope_w=42
def f057trq_f057_trend_r2_tfit_5d_xstd63_slope_v022_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * _std(closeadj, 63)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xstd63 slope_w=63
def f057trq_f057_trend_r2_tfit_5d_xstd63_slope_v023_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * _std(closeadj, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xstd63 slope_w=126
def f057trq_f057_trend_r2_tfit_5d_xstd63_slope_v024_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * _std(closeadj, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xclosesq slope_w=5
def f057trq_f057_trend_r2_tfit_5d_xclosesq_slope_v025_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj * closeadj / 100.0
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xclosesq slope_w=10
def f057trq_f057_trend_r2_tfit_5d_xclosesq_slope_v026_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj * closeadj / 100.0
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xclosesq slope_w=21
def f057trq_f057_trend_r2_tfit_5d_xclosesq_slope_v027_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj * closeadj / 100.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xclosesq slope_w=42
def f057trq_f057_trend_r2_tfit_5d_xclosesq_slope_v028_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj * closeadj / 100.0
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xclosesq slope_w=63
def f057trq_f057_trend_r2_tfit_5d_xclosesq_slope_v029_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj * closeadj / 100.0
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xclosesq slope_w=126
def f057trq_f057_trend_r2_tfit_5d_xclosesq_slope_v030_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj * closeadj / 100.0
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xclose2 slope_w=5
def f057trq_f057_trend_r2_tfit_5d_xclose2_slope_v031_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 5) + closeadj) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xclose2 slope_w=10
def f057trq_f057_trend_r2_tfit_5d_xclose2_slope_v032_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 5) + closeadj) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xclose2 slope_w=21
def f057trq_f057_trend_r2_tfit_5d_xclose2_slope_v033_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 5) + closeadj) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xclose2 slope_w=42
def f057trq_f057_trend_r2_tfit_5d_xclose2_slope_v034_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 5) + closeadj) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xclose2 slope_w=63
def f057trq_f057_trend_r2_tfit_5d_xclose2_slope_v035_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 5) + closeadj) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xclose2 slope_w=126
def f057trq_f057_trend_r2_tfit_5d_xclose2_slope_v036_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 5) + closeadj) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xema21 slope_w=5
def f057trq_f057_trend_r2_tfit_5d_xema21_slope_v037_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xema21 slope_w=10
def f057trq_f057_trend_r2_tfit_5d_xema21_slope_v038_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xema21 slope_w=21
def f057trq_f057_trend_r2_tfit_5d_xema21_slope_v039_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xema21 slope_w=42
def f057trq_f057_trend_r2_tfit_5d_xema21_slope_v040_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xema21 slope_w=63
def f057trq_f057_trend_r2_tfit_5d_xema21_slope_v041_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xema21 slope_w=126
def f057trq_f057_trend_r2_tfit_5d_xema21_slope_v042_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xema63 slope_w=5
def f057trq_f057_trend_r2_tfit_5d_xema63_slope_v043_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xema63 slope_w=10
def f057trq_f057_trend_r2_tfit_5d_xema63_slope_v044_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xema63 slope_w=21
def f057trq_f057_trend_r2_tfit_5d_xema63_slope_v045_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xema63 slope_w=42
def f057trq_f057_trend_r2_tfit_5d_xema63_slope_v046_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xema63 slope_w=63
def f057trq_f057_trend_r2_tfit_5d_xema63_slope_v047_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xema63 slope_w=126
def f057trq_f057_trend_r2_tfit_5d_xema63_slope_v048_signal(closeadj):
    base = _f057_trend_fit(closeadj, 5) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmix slope_w=5
def f057trq_f057_trend_r2_tfit_5d_xmix_slope_v049_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 5) * closeadj + _mean(closeadj, 63))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmix slope_w=10
def f057trq_f057_trend_r2_tfit_5d_xmix_slope_v050_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 5) * closeadj + _mean(closeadj, 63))
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmix slope_w=21
def f057trq_f057_trend_r2_tfit_5d_xmix_slope_v051_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 5) * closeadj + _mean(closeadj, 63))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmix slope_w=42
def f057trq_f057_trend_r2_tfit_5d_xmix_slope_v052_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 5) * closeadj + _mean(closeadj, 63))
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmix slope_w=63
def f057trq_f057_trend_r2_tfit_5d_xmix_slope_v053_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 5) * closeadj + _mean(closeadj, 63))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmix slope_w=126
def f057trq_f057_trend_r2_tfit_5d_xmix_slope_v054_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 5) * closeadj + _mean(closeadj, 63))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmix2 slope_w=5
def f057trq_f057_trend_r2_tfit_5d_xmix2_slope_v055_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 5) * closeadj - _mean(closeadj, 126))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmix2 slope_w=10
def f057trq_f057_trend_r2_tfit_5d_xmix2_slope_v056_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 5) * closeadj - _mean(closeadj, 126))
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmix2 slope_w=21
def f057trq_f057_trend_r2_tfit_5d_xmix2_slope_v057_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 5) * closeadj - _mean(closeadj, 126))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmix2 slope_w=42
def f057trq_f057_trend_r2_tfit_5d_xmix2_slope_v058_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 5) * closeadj - _mean(closeadj, 126))
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmix2 slope_w=63
def f057trq_f057_trend_r2_tfit_5d_xmix2_slope_v059_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 5) * closeadj - _mean(closeadj, 126))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=5 variant=xmix2 slope_w=126
def f057trq_f057_trend_r2_tfit_5d_xmix2_slope_v060_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 5) * closeadj - _mean(closeadj, 126))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xclose slope_w=5
def f057trq_f057_trend_r2_tfit_10d_xclose_slope_v061_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xclose slope_w=10
def f057trq_f057_trend_r2_tfit_10d_xclose_slope_v062_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xclose slope_w=21
def f057trq_f057_trend_r2_tfit_10d_xclose_slope_v063_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xclose slope_w=42
def f057trq_f057_trend_r2_tfit_10d_xclose_slope_v064_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xclose slope_w=63
def f057trq_f057_trend_r2_tfit_10d_xclose_slope_v065_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xclose slope_w=126
def f057trq_f057_trend_r2_tfit_10d_xclose_slope_v066_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmean21 slope_w=5
def f057trq_f057_trend_r2_tfit_10d_xmean21_slope_v067_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmean21 slope_w=10
def f057trq_f057_trend_r2_tfit_10d_xmean21_slope_v068_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmean21 slope_w=21
def f057trq_f057_trend_r2_tfit_10d_xmean21_slope_v069_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmean21 slope_w=42
def f057trq_f057_trend_r2_tfit_10d_xmean21_slope_v070_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmean21 slope_w=63
def f057trq_f057_trend_r2_tfit_10d_xmean21_slope_v071_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * _mean(closeadj, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmean21 slope_w=126
def f057trq_f057_trend_r2_tfit_10d_xmean21_slope_v072_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmean63 slope_w=5
def f057trq_f057_trend_r2_tfit_10d_xmean63_slope_v073_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * _mean(closeadj, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmean63 slope_w=10
def f057trq_f057_trend_r2_tfit_10d_xmean63_slope_v074_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmean63 slope_w=21
def f057trq_f057_trend_r2_tfit_10d_xmean63_slope_v075_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * _mean(closeadj, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmean63 slope_w=42
def f057trq_f057_trend_r2_tfit_10d_xmean63_slope_v076_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmean63 slope_w=63
def f057trq_f057_trend_r2_tfit_10d_xmean63_slope_v077_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * _mean(closeadj, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmean63 slope_w=126
def f057trq_f057_trend_r2_tfit_10d_xmean63_slope_v078_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xstd63 slope_w=5
def f057trq_f057_trend_r2_tfit_10d_xstd63_slope_v079_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * _std(closeadj, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xstd63 slope_w=10
def f057trq_f057_trend_r2_tfit_10d_xstd63_slope_v080_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * _std(closeadj, 63)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xstd63 slope_w=21
def f057trq_f057_trend_r2_tfit_10d_xstd63_slope_v081_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * _std(closeadj, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xstd63 slope_w=42
def f057trq_f057_trend_r2_tfit_10d_xstd63_slope_v082_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * _std(closeadj, 63)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xstd63 slope_w=63
def f057trq_f057_trend_r2_tfit_10d_xstd63_slope_v083_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * _std(closeadj, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xstd63 slope_w=126
def f057trq_f057_trend_r2_tfit_10d_xstd63_slope_v084_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * _std(closeadj, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xclosesq slope_w=5
def f057trq_f057_trend_r2_tfit_10d_xclosesq_slope_v085_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj * closeadj / 100.0
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xclosesq slope_w=10
def f057trq_f057_trend_r2_tfit_10d_xclosesq_slope_v086_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj * closeadj / 100.0
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xclosesq slope_w=21
def f057trq_f057_trend_r2_tfit_10d_xclosesq_slope_v087_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj * closeadj / 100.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xclosesq slope_w=42
def f057trq_f057_trend_r2_tfit_10d_xclosesq_slope_v088_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj * closeadj / 100.0
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xclosesq slope_w=63
def f057trq_f057_trend_r2_tfit_10d_xclosesq_slope_v089_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj * closeadj / 100.0
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xclosesq slope_w=126
def f057trq_f057_trend_r2_tfit_10d_xclosesq_slope_v090_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj * closeadj / 100.0
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xclose2 slope_w=5
def f057trq_f057_trend_r2_tfit_10d_xclose2_slope_v091_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 10) + closeadj) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xclose2 slope_w=10
def f057trq_f057_trend_r2_tfit_10d_xclose2_slope_v092_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 10) + closeadj) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xclose2 slope_w=21
def f057trq_f057_trend_r2_tfit_10d_xclose2_slope_v093_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 10) + closeadj) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xclose2 slope_w=42
def f057trq_f057_trend_r2_tfit_10d_xclose2_slope_v094_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 10) + closeadj) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xclose2 slope_w=63
def f057trq_f057_trend_r2_tfit_10d_xclose2_slope_v095_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 10) + closeadj) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xclose2 slope_w=126
def f057trq_f057_trend_r2_tfit_10d_xclose2_slope_v096_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 10) + closeadj) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xema21 slope_w=5
def f057trq_f057_trend_r2_tfit_10d_xema21_slope_v097_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xema21 slope_w=10
def f057trq_f057_trend_r2_tfit_10d_xema21_slope_v098_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xema21 slope_w=21
def f057trq_f057_trend_r2_tfit_10d_xema21_slope_v099_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xema21 slope_w=42
def f057trq_f057_trend_r2_tfit_10d_xema21_slope_v100_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xema21 slope_w=63
def f057trq_f057_trend_r2_tfit_10d_xema21_slope_v101_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xema21 slope_w=126
def f057trq_f057_trend_r2_tfit_10d_xema21_slope_v102_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj.ewm(span=21, min_periods=10).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xema63 slope_w=5
def f057trq_f057_trend_r2_tfit_10d_xema63_slope_v103_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xema63 slope_w=10
def f057trq_f057_trend_r2_tfit_10d_xema63_slope_v104_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xema63 slope_w=21
def f057trq_f057_trend_r2_tfit_10d_xema63_slope_v105_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xema63 slope_w=42
def f057trq_f057_trend_r2_tfit_10d_xema63_slope_v106_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xema63 slope_w=63
def f057trq_f057_trend_r2_tfit_10d_xema63_slope_v107_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xema63 slope_w=126
def f057trq_f057_trend_r2_tfit_10d_xema63_slope_v108_signal(closeadj):
    base = _f057_trend_fit(closeadj, 10) * closeadj.ewm(span=63, min_periods=21).mean()
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmix slope_w=5
def f057trq_f057_trend_r2_tfit_10d_xmix_slope_v109_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 10) * closeadj + _mean(closeadj, 63))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmix slope_w=10
def f057trq_f057_trend_r2_tfit_10d_xmix_slope_v110_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 10) * closeadj + _mean(closeadj, 63))
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmix slope_w=21
def f057trq_f057_trend_r2_tfit_10d_xmix_slope_v111_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 10) * closeadj + _mean(closeadj, 63))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmix slope_w=42
def f057trq_f057_trend_r2_tfit_10d_xmix_slope_v112_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 10) * closeadj + _mean(closeadj, 63))
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmix slope_w=63
def f057trq_f057_trend_r2_tfit_10d_xmix_slope_v113_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 10) * closeadj + _mean(closeadj, 63))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmix slope_w=126
def f057trq_f057_trend_r2_tfit_10d_xmix_slope_v114_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 10) * closeadj + _mean(closeadj, 63))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmix2 slope_w=5
def f057trq_f057_trend_r2_tfit_10d_xmix2_slope_v115_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 10) * closeadj - _mean(closeadj, 126))
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmix2 slope_w=10
def f057trq_f057_trend_r2_tfit_10d_xmix2_slope_v116_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 10) * closeadj - _mean(closeadj, 126))
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmix2 slope_w=21
def f057trq_f057_trend_r2_tfit_10d_xmix2_slope_v117_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 10) * closeadj - _mean(closeadj, 126))
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmix2 slope_w=42
def f057trq_f057_trend_r2_tfit_10d_xmix2_slope_v118_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 10) * closeadj - _mean(closeadj, 126))
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmix2 slope_w=63
def f057trq_f057_trend_r2_tfit_10d_xmix2_slope_v119_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 10) * closeadj - _mean(closeadj, 126))
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=10 variant=xmix2 slope_w=126
def f057trq_f057_trend_r2_tfit_10d_xmix2_slope_v120_signal(closeadj):
    base = (_f057_trend_fit(closeadj, 10) * closeadj - _mean(closeadj, 126))
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xclose slope_w=5
def f057trq_f057_trend_r2_tfit_21d_xclose_slope_v121_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xclose slope_w=10
def f057trq_f057_trend_r2_tfit_21d_xclose_slope_v122_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * closeadj
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xclose slope_w=21
def f057trq_f057_trend_r2_tfit_21d_xclose_slope_v123_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xclose slope_w=42
def f057trq_f057_trend_r2_tfit_21d_xclose_slope_v124_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * closeadj
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xclose slope_w=63
def f057trq_f057_trend_r2_tfit_21d_xclose_slope_v125_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xclose slope_w=126
def f057trq_f057_trend_r2_tfit_21d_xclose_slope_v126_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xmean21 slope_w=5
def f057trq_f057_trend_r2_tfit_21d_xmean21_slope_v127_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * _mean(closeadj, 21)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xmean21 slope_w=10
def f057trq_f057_trend_r2_tfit_21d_xmean21_slope_v128_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xmean21 slope_w=21
def f057trq_f057_trend_r2_tfit_21d_xmean21_slope_v129_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * _mean(closeadj, 21)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xmean21 slope_w=42
def f057trq_f057_trend_r2_tfit_21d_xmean21_slope_v130_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xmean21 slope_w=63
def f057trq_f057_trend_r2_tfit_21d_xmean21_slope_v131_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * _mean(closeadj, 21)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xmean21 slope_w=126
def f057trq_f057_trend_r2_tfit_21d_xmean21_slope_v132_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * _mean(closeadj, 21)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xmean63 slope_w=5
def f057trq_f057_trend_r2_tfit_21d_xmean63_slope_v133_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * _mean(closeadj, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xmean63 slope_w=10
def f057trq_f057_trend_r2_tfit_21d_xmean63_slope_v134_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xmean63 slope_w=21
def f057trq_f057_trend_r2_tfit_21d_xmean63_slope_v135_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * _mean(closeadj, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xmean63 slope_w=42
def f057trq_f057_trend_r2_tfit_21d_xmean63_slope_v136_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xmean63 slope_w=63
def f057trq_f057_trend_r2_tfit_21d_xmean63_slope_v137_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * _mean(closeadj, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xmean63 slope_w=126
def f057trq_f057_trend_r2_tfit_21d_xmean63_slope_v138_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * _mean(closeadj, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xstd63 slope_w=5
def f057trq_f057_trend_r2_tfit_21d_xstd63_slope_v139_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * _std(closeadj, 63)
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xstd63 slope_w=10
def f057trq_f057_trend_r2_tfit_21d_xstd63_slope_v140_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * _std(closeadj, 63)
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xstd63 slope_w=21
def f057trq_f057_trend_r2_tfit_21d_xstd63_slope_v141_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * _std(closeadj, 63)
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xstd63 slope_w=42
def f057trq_f057_trend_r2_tfit_21d_xstd63_slope_v142_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * _std(closeadj, 63)
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xstd63 slope_w=63
def f057trq_f057_trend_r2_tfit_21d_xstd63_slope_v143_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * _std(closeadj, 63)
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xstd63 slope_w=126
def f057trq_f057_trend_r2_tfit_21d_xstd63_slope_v144_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * _std(closeadj, 63)
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xclosesq slope_w=5
def f057trq_f057_trend_r2_tfit_21d_xclosesq_slope_v145_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * closeadj * closeadj / 100.0
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xclosesq slope_w=10
def f057trq_f057_trend_r2_tfit_21d_xclosesq_slope_v146_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * closeadj * closeadj / 100.0
    result = _slope_diff_norm(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xclosesq slope_w=21
def f057trq_f057_trend_r2_tfit_21d_xclosesq_slope_v147_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * closeadj * closeadj / 100.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xclosesq slope_w=42
def f057trq_f057_trend_r2_tfit_21d_xclosesq_slope_v148_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * closeadj * closeadj / 100.0
    result = _slope_diff_norm(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xclosesq slope_w=63
def f057trq_f057_trend_r2_tfit_21d_xclosesq_slope_v149_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * closeadj * closeadj / 100.0
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# tfit base_w=21 variant=xclosesq slope_w=126
def f057trq_f057_trend_r2_tfit_21d_xclosesq_slope_v150_signal(closeadj):
    base = _f057_trend_fit(closeadj, 21) * closeadj * closeadj / 100.0
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f057trq_f057_trend_r2_tfit_5d_xclose_slope_v001_signal,
    f057trq_f057_trend_r2_tfit_5d_xclose_slope_v002_signal,
    f057trq_f057_trend_r2_tfit_5d_xclose_slope_v003_signal,
    f057trq_f057_trend_r2_tfit_5d_xclose_slope_v004_signal,
    f057trq_f057_trend_r2_tfit_5d_xclose_slope_v005_signal,
    f057trq_f057_trend_r2_tfit_5d_xclose_slope_v006_signal,
    f057trq_f057_trend_r2_tfit_5d_xmean21_slope_v007_signal,
    f057trq_f057_trend_r2_tfit_5d_xmean21_slope_v008_signal,
    f057trq_f057_trend_r2_tfit_5d_xmean21_slope_v009_signal,
    f057trq_f057_trend_r2_tfit_5d_xmean21_slope_v010_signal,
    f057trq_f057_trend_r2_tfit_5d_xmean21_slope_v011_signal,
    f057trq_f057_trend_r2_tfit_5d_xmean21_slope_v012_signal,
    f057trq_f057_trend_r2_tfit_5d_xmean63_slope_v013_signal,
    f057trq_f057_trend_r2_tfit_5d_xmean63_slope_v014_signal,
    f057trq_f057_trend_r2_tfit_5d_xmean63_slope_v015_signal,
    f057trq_f057_trend_r2_tfit_5d_xmean63_slope_v016_signal,
    f057trq_f057_trend_r2_tfit_5d_xmean63_slope_v017_signal,
    f057trq_f057_trend_r2_tfit_5d_xmean63_slope_v018_signal,
    f057trq_f057_trend_r2_tfit_5d_xstd63_slope_v019_signal,
    f057trq_f057_trend_r2_tfit_5d_xstd63_slope_v020_signal,
    f057trq_f057_trend_r2_tfit_5d_xstd63_slope_v021_signal,
    f057trq_f057_trend_r2_tfit_5d_xstd63_slope_v022_signal,
    f057trq_f057_trend_r2_tfit_5d_xstd63_slope_v023_signal,
    f057trq_f057_trend_r2_tfit_5d_xstd63_slope_v024_signal,
    f057trq_f057_trend_r2_tfit_5d_xclosesq_slope_v025_signal,
    f057trq_f057_trend_r2_tfit_5d_xclosesq_slope_v026_signal,
    f057trq_f057_trend_r2_tfit_5d_xclosesq_slope_v027_signal,
    f057trq_f057_trend_r2_tfit_5d_xclosesq_slope_v028_signal,
    f057trq_f057_trend_r2_tfit_5d_xclosesq_slope_v029_signal,
    f057trq_f057_trend_r2_tfit_5d_xclosesq_slope_v030_signal,
    f057trq_f057_trend_r2_tfit_5d_xclose2_slope_v031_signal,
    f057trq_f057_trend_r2_tfit_5d_xclose2_slope_v032_signal,
    f057trq_f057_trend_r2_tfit_5d_xclose2_slope_v033_signal,
    f057trq_f057_trend_r2_tfit_5d_xclose2_slope_v034_signal,
    f057trq_f057_trend_r2_tfit_5d_xclose2_slope_v035_signal,
    f057trq_f057_trend_r2_tfit_5d_xclose2_slope_v036_signal,
    f057trq_f057_trend_r2_tfit_5d_xema21_slope_v037_signal,
    f057trq_f057_trend_r2_tfit_5d_xema21_slope_v038_signal,
    f057trq_f057_trend_r2_tfit_5d_xema21_slope_v039_signal,
    f057trq_f057_trend_r2_tfit_5d_xema21_slope_v040_signal,
    f057trq_f057_trend_r2_tfit_5d_xema21_slope_v041_signal,
    f057trq_f057_trend_r2_tfit_5d_xema21_slope_v042_signal,
    f057trq_f057_trend_r2_tfit_5d_xema63_slope_v043_signal,
    f057trq_f057_trend_r2_tfit_5d_xema63_slope_v044_signal,
    f057trq_f057_trend_r2_tfit_5d_xema63_slope_v045_signal,
    f057trq_f057_trend_r2_tfit_5d_xema63_slope_v046_signal,
    f057trq_f057_trend_r2_tfit_5d_xema63_slope_v047_signal,
    f057trq_f057_trend_r2_tfit_5d_xema63_slope_v048_signal,
    f057trq_f057_trend_r2_tfit_5d_xmix_slope_v049_signal,
    f057trq_f057_trend_r2_tfit_5d_xmix_slope_v050_signal,
    f057trq_f057_trend_r2_tfit_5d_xmix_slope_v051_signal,
    f057trq_f057_trend_r2_tfit_5d_xmix_slope_v052_signal,
    f057trq_f057_trend_r2_tfit_5d_xmix_slope_v053_signal,
    f057trq_f057_trend_r2_tfit_5d_xmix_slope_v054_signal,
    f057trq_f057_trend_r2_tfit_5d_xmix2_slope_v055_signal,
    f057trq_f057_trend_r2_tfit_5d_xmix2_slope_v056_signal,
    f057trq_f057_trend_r2_tfit_5d_xmix2_slope_v057_signal,
    f057trq_f057_trend_r2_tfit_5d_xmix2_slope_v058_signal,
    f057trq_f057_trend_r2_tfit_5d_xmix2_slope_v059_signal,
    f057trq_f057_trend_r2_tfit_5d_xmix2_slope_v060_signal,
    f057trq_f057_trend_r2_tfit_10d_xclose_slope_v061_signal,
    f057trq_f057_trend_r2_tfit_10d_xclose_slope_v062_signal,
    f057trq_f057_trend_r2_tfit_10d_xclose_slope_v063_signal,
    f057trq_f057_trend_r2_tfit_10d_xclose_slope_v064_signal,
    f057trq_f057_trend_r2_tfit_10d_xclose_slope_v065_signal,
    f057trq_f057_trend_r2_tfit_10d_xclose_slope_v066_signal,
    f057trq_f057_trend_r2_tfit_10d_xmean21_slope_v067_signal,
    f057trq_f057_trend_r2_tfit_10d_xmean21_slope_v068_signal,
    f057trq_f057_trend_r2_tfit_10d_xmean21_slope_v069_signal,
    f057trq_f057_trend_r2_tfit_10d_xmean21_slope_v070_signal,
    f057trq_f057_trend_r2_tfit_10d_xmean21_slope_v071_signal,
    f057trq_f057_trend_r2_tfit_10d_xmean21_slope_v072_signal,
    f057trq_f057_trend_r2_tfit_10d_xmean63_slope_v073_signal,
    f057trq_f057_trend_r2_tfit_10d_xmean63_slope_v074_signal,
    f057trq_f057_trend_r2_tfit_10d_xmean63_slope_v075_signal,
    f057trq_f057_trend_r2_tfit_10d_xmean63_slope_v076_signal,
    f057trq_f057_trend_r2_tfit_10d_xmean63_slope_v077_signal,
    f057trq_f057_trend_r2_tfit_10d_xmean63_slope_v078_signal,
    f057trq_f057_trend_r2_tfit_10d_xstd63_slope_v079_signal,
    f057trq_f057_trend_r2_tfit_10d_xstd63_slope_v080_signal,
    f057trq_f057_trend_r2_tfit_10d_xstd63_slope_v081_signal,
    f057trq_f057_trend_r2_tfit_10d_xstd63_slope_v082_signal,
    f057trq_f057_trend_r2_tfit_10d_xstd63_slope_v083_signal,
    f057trq_f057_trend_r2_tfit_10d_xstd63_slope_v084_signal,
    f057trq_f057_trend_r2_tfit_10d_xclosesq_slope_v085_signal,
    f057trq_f057_trend_r2_tfit_10d_xclosesq_slope_v086_signal,
    f057trq_f057_trend_r2_tfit_10d_xclosesq_slope_v087_signal,
    f057trq_f057_trend_r2_tfit_10d_xclosesq_slope_v088_signal,
    f057trq_f057_trend_r2_tfit_10d_xclosesq_slope_v089_signal,
    f057trq_f057_trend_r2_tfit_10d_xclosesq_slope_v090_signal,
    f057trq_f057_trend_r2_tfit_10d_xclose2_slope_v091_signal,
    f057trq_f057_trend_r2_tfit_10d_xclose2_slope_v092_signal,
    f057trq_f057_trend_r2_tfit_10d_xclose2_slope_v093_signal,
    f057trq_f057_trend_r2_tfit_10d_xclose2_slope_v094_signal,
    f057trq_f057_trend_r2_tfit_10d_xclose2_slope_v095_signal,
    f057trq_f057_trend_r2_tfit_10d_xclose2_slope_v096_signal,
    f057trq_f057_trend_r2_tfit_10d_xema21_slope_v097_signal,
    f057trq_f057_trend_r2_tfit_10d_xema21_slope_v098_signal,
    f057trq_f057_trend_r2_tfit_10d_xema21_slope_v099_signal,
    f057trq_f057_trend_r2_tfit_10d_xema21_slope_v100_signal,
    f057trq_f057_trend_r2_tfit_10d_xema21_slope_v101_signal,
    f057trq_f057_trend_r2_tfit_10d_xema21_slope_v102_signal,
    f057trq_f057_trend_r2_tfit_10d_xema63_slope_v103_signal,
    f057trq_f057_trend_r2_tfit_10d_xema63_slope_v104_signal,
    f057trq_f057_trend_r2_tfit_10d_xema63_slope_v105_signal,
    f057trq_f057_trend_r2_tfit_10d_xema63_slope_v106_signal,
    f057trq_f057_trend_r2_tfit_10d_xema63_slope_v107_signal,
    f057trq_f057_trend_r2_tfit_10d_xema63_slope_v108_signal,
    f057trq_f057_trend_r2_tfit_10d_xmix_slope_v109_signal,
    f057trq_f057_trend_r2_tfit_10d_xmix_slope_v110_signal,
    f057trq_f057_trend_r2_tfit_10d_xmix_slope_v111_signal,
    f057trq_f057_trend_r2_tfit_10d_xmix_slope_v112_signal,
    f057trq_f057_trend_r2_tfit_10d_xmix_slope_v113_signal,
    f057trq_f057_trend_r2_tfit_10d_xmix_slope_v114_signal,
    f057trq_f057_trend_r2_tfit_10d_xmix2_slope_v115_signal,
    f057trq_f057_trend_r2_tfit_10d_xmix2_slope_v116_signal,
    f057trq_f057_trend_r2_tfit_10d_xmix2_slope_v117_signal,
    f057trq_f057_trend_r2_tfit_10d_xmix2_slope_v118_signal,
    f057trq_f057_trend_r2_tfit_10d_xmix2_slope_v119_signal,
    f057trq_f057_trend_r2_tfit_10d_xmix2_slope_v120_signal,
    f057trq_f057_trend_r2_tfit_21d_xclose_slope_v121_signal,
    f057trq_f057_trend_r2_tfit_21d_xclose_slope_v122_signal,
    f057trq_f057_trend_r2_tfit_21d_xclose_slope_v123_signal,
    f057trq_f057_trend_r2_tfit_21d_xclose_slope_v124_signal,
    f057trq_f057_trend_r2_tfit_21d_xclose_slope_v125_signal,
    f057trq_f057_trend_r2_tfit_21d_xclose_slope_v126_signal,
    f057trq_f057_trend_r2_tfit_21d_xmean21_slope_v127_signal,
    f057trq_f057_trend_r2_tfit_21d_xmean21_slope_v128_signal,
    f057trq_f057_trend_r2_tfit_21d_xmean21_slope_v129_signal,
    f057trq_f057_trend_r2_tfit_21d_xmean21_slope_v130_signal,
    f057trq_f057_trend_r2_tfit_21d_xmean21_slope_v131_signal,
    f057trq_f057_trend_r2_tfit_21d_xmean21_slope_v132_signal,
    f057trq_f057_trend_r2_tfit_21d_xmean63_slope_v133_signal,
    f057trq_f057_trend_r2_tfit_21d_xmean63_slope_v134_signal,
    f057trq_f057_trend_r2_tfit_21d_xmean63_slope_v135_signal,
    f057trq_f057_trend_r2_tfit_21d_xmean63_slope_v136_signal,
    f057trq_f057_trend_r2_tfit_21d_xmean63_slope_v137_signal,
    f057trq_f057_trend_r2_tfit_21d_xmean63_slope_v138_signal,
    f057trq_f057_trend_r2_tfit_21d_xstd63_slope_v139_signal,
    f057trq_f057_trend_r2_tfit_21d_xstd63_slope_v140_signal,
    f057trq_f057_trend_r2_tfit_21d_xstd63_slope_v141_signal,
    f057trq_f057_trend_r2_tfit_21d_xstd63_slope_v142_signal,
    f057trq_f057_trend_r2_tfit_21d_xstd63_slope_v143_signal,
    f057trq_f057_trend_r2_tfit_21d_xstd63_slope_v144_signal,
    f057trq_f057_trend_r2_tfit_21d_xclosesq_slope_v145_signal,
    f057trq_f057_trend_r2_tfit_21d_xclosesq_slope_v146_signal,
    f057trq_f057_trend_r2_tfit_21d_xclosesq_slope_v147_signal,
    f057trq_f057_trend_r2_tfit_21d_xclosesq_slope_v148_signal,
    f057trq_f057_trend_r2_tfit_21d_xclosesq_slope_v149_signal,
    f057trq_f057_trend_r2_tfit_21d_xclosesq_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F057_TREND_R2_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    cols = {"closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f057_trend_fit", "_f057_trend_r2", "_f057_smoothness_score",)
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f057_trend_r2_2nd_derivatives_001_150_claude: {n_features} features pass")
