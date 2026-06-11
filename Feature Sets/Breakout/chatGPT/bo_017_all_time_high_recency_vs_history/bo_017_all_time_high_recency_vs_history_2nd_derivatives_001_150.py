import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _clean(s):
    return s.replace([np.inf, -np.inf], np.nan)


def _safe_div(a, b):
    if hasattr(b, "replace"):
        denom = b.replace(0, np.nan)
    else:
        denom = np.nan if b == 0 else b
    return a / denom


def _z(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return _safe_div(s - m, sd)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _ret(s, n):
    denom = s.shift(n).abs()
    denom = denom.where(denom != 0, 1.0)
    return (s - s.shift(n)) / denom


def _slope(s, w):
    denom = s.abs().rolling(w, min_periods=max(2, w // 2)).mean()
    denom = denom.where(denom != 0, 1.0)
    return s.diff(periods=w) / denom


def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(2, span // 2)).mean()


def _true_range(high, low, close):
    prev = close.shift(1)
    a = high - low
    b = (high - prev).abs()
    c = (low - prev).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def _atr(high, low, close, w):
    return _true_range(high, low, close).rolling(w, min_periods=max(2, w // 2)).mean()


def _roll_slope(s, w):
    x = pd.Series(np.arange(w), index=range(w), dtype=float)
    xm = x.mean()
    denom = ((x - xm) ** 2).sum()
    return s.rolling(w, min_periods=max(3, w // 2)).apply(
        lambda y: float(np.dot(np.asarray(y) - np.nanmean(y), x[-len(y):] - x[-len(y):].mean()) / denom)
        if len(y) >= 3 and denom != 0 else np.nan,
        raw=False,
    )


def _obv(close, volume):
    direction = np.sign(close.diff()).fillna(0.0)
    return (direction * volume).cumsum()


def _adline(high, low, close, volume):
    mfm = _safe_div((close - low) - (high - close), high - low)
    return (mfm.fillna(0.0) * volume).cumsum()


def _mfi(high, low, close, volume, w):
    typical = (high + low + close) / 3.0
    flow = typical * volume
    pos = flow.where(typical.diff() > 0, 0.0).rolling(w, min_periods=max(2, w // 2)).sum()
    neg = flow.where(typical.diff() < 0, 0.0).abs().rolling(w, min_periods=max(2, w // 2)).sum()
    return 100.0 - (100.0 / (1.0 + _safe_div(pos, neg)))


def _growth(s, n):
    return _safe_div(s - s.shift(n), s.shift(n).abs())


def _margin(num, den):
    return _safe_div(num, den.abs())



def _accel(s, w):
    return s.diff(periods=w).diff(periods=w)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


# 21d slope z-score for ath_recency_drought
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_slopez_21_126_2d_v008_signal(closeadj):
    base = closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for ath_recency_drought
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_slopez_63_252_2d_v009_signal(closeadj):
    base = closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# slope regime gap for ath_recency_drought
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_slope_rank_gap_2d_v012_signal(closeadj):
    base = closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 126d slope z-score for ath_recency_drought
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_slopez_126_504_2d_v015_signal(closeadj):
    base = closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope z-score for ath_recency_drought_mean_42d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_slopez_21_126_2d_v023_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 42)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# slope regime gap for ath_recency_drought_mean_42d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_slope_rank_gap_2d_v027_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 42)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 126d slope z-score for ath_recency_drought_mean_42d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_slopez_126_504_2d_v030_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 42)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 63d slope z-score for ath_recency_drought_mean_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_slopez_63_252_2d_v039_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# slope regime gap for ath_recency_drought_mean_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_slope_rank_gap_2d_v042_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for ath_recency_drought_mean_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_slope_504d_2d_v043_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _slope(base, 504)
    return _clean(result)

# 126d slope z-score for ath_recency_drought_mean_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_slopez_126_504_2d_v045_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope z-score for ath_recency_drought_z_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_126d_slopez_21_126_2d_v053_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# slope regime gap for ath_recency_drought_z_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_126d_slope_rank_gap_2d_v057_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for ath_recency_drought_z_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_126d_slope_504d_2d_v058_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _slope(base, 504)
    return _clean(result)

# 126d slope z-score for ath_recency_drought_z_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_126d_slopez_126_504_2d_v060_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 252d slope for ath_recency_drought_z_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_slope_252d_2d_v064_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 378)
    result = _slope(base, 252)
    return _clean(result)

# 252d smoothed 63d slope for ath_recency_drought_z_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_sm252_slope63_2d_v066_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 378)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 21d slope z-score for ath_recency_drought_z_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_slopez_21_126_2d_v068_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 378)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for ath_recency_drought_z_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_slopez_63_252_2d_v069_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 378)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# slope regime gap for ath_recency_drought_z_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_slope_rank_gap_2d_v072_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 378)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for ath_recency_drought_z_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_slope_504d_2d_v073_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 378)
    result = _slope(base, 504)
    return _clean(result)

# 126d slope z-score for ath_recency_drought_z_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_slopez_126_504_2d_v075_signal(closeadj):
    base = _z(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 378)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope z-score for ath_recency_drought_distmax_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmax_378d_slopez_21_126_2d_v083_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).max(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# slope regime gap for ath_recency_drought_distmax_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmax_378d_slope_rank_gap_2d_v087_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).max(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for ath_recency_drought_distmax_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmax_378d_slope_504d_2d_v088_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).max(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _slope(base, 504)
    return _clean(result)

# 126d slope z-score for ath_recency_drought_distmax_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmax_378d_slopez_126_504_2d_v090_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).max(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for ath_recency_drought_distmin_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmin_378d_slope_21d_2d_v091_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).min(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).min().abs())
    result = _slope(base, 21)
    return _clean(result)

# 252d slope for ath_recency_drought_distmed_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_slope_252d_2d_v109_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _slope(base, 252)
    return _clean(result)

# 252d smoothed 63d slope for ath_recency_drought_distmed_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_sm252_slope63_2d_v111_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d slope z-score for ath_recency_drought_distmed_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_slopez_63_252_2d_v114_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# slope regime gap for ath_recency_drought_distmed_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_slope_rank_gap_2d_v117_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for ath_recency_drought_distmed_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_slope_504d_2d_v118_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _slope(base, 504)
    return _clean(result)

# 126d slope z-score for ath_recency_drought_distmed_378d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_slopez_126_504_2d_v120_signal(closeadj):
    base = _safe_div((closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median(), (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope z-score for ath_recency_drought_upper_gap_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_upper_gap_126d_slopez_21_126_2d_v128_signal(closeadj):
    base = (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# slope regime gap for ath_recency_drought_upper_gap_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_upper_gap_126d_slope_rank_gap_2d_v132_signal(closeadj):
    base = (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for ath_recency_drought_upper_gap_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_upper_gap_126d_slope_504d_2d_v133_signal(closeadj):
    base = (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _slope(base, 504)
    return _clean(result)

# 126d slope z-score for ath_recency_drought_upper_gap_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_upper_gap_126d_slopez_126_504_2d_v135_signal(closeadj):
    base = (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 63d slope z-score for ath_recency_drought_lower_gap_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_lower_gap_126d_slopez_63_252_2d_v144_signal(closeadj):
    base = (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(126, min_periods=max(2, 126//2)).quantile(0.25)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# slope regime gap for ath_recency_drought_lower_gap_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_lower_gap_126d_slope_rank_gap_2d_v147_signal(closeadj):
    base = (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(126, min_periods=max(2, 126//2)).quantile(0.25)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for ath_recency_drought_lower_gap_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_lower_gap_126d_slope_504d_2d_v148_signal(closeadj):
    base = (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(126, min_periods=max(2, 126//2)).quantile(0.25)
    result = _slope(base, 504)
    return _clean(result)

# 126d slope z-score for ath_recency_drought_lower_gap_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_lower_gap_126d_slopez_126_504_2d_v150_signal(closeadj):
    base = (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)) - (closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)).rolling(126, min_periods=max(2, 126//2)).quantile(0.25)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

REGISTRY = {fn.__name__: {"inputs": ['closeadj'], "func": fn} for fn in [bo_017_all_time_high_recency_vs_history_ath_recency_drought_slopez_21_126_2d_v008_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_slopez_63_252_2d_v009_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_slope_rank_gap_2d_v012_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_slopez_126_504_2d_v015_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_slopez_21_126_2d_v023_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_slope_rank_gap_2d_v027_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_slopez_126_504_2d_v030_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_slopez_63_252_2d_v039_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_slope_rank_gap_2d_v042_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_slope_504d_2d_v043_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_slopez_126_504_2d_v045_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_126d_slopez_21_126_2d_v053_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_126d_slope_rank_gap_2d_v057_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_126d_slope_504d_2d_v058_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_126d_slopez_126_504_2d_v060_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_slope_252d_2d_v064_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_sm252_slope63_2d_v066_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_slopez_21_126_2d_v068_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_slopez_63_252_2d_v069_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_slope_rank_gap_2d_v072_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_slope_504d_2d_v073_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_z_378d_slopez_126_504_2d_v075_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmax_378d_slopez_21_126_2d_v083_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmax_378d_slope_rank_gap_2d_v087_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmax_378d_slope_504d_2d_v088_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmax_378d_slopez_126_504_2d_v090_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmin_378d_slope_21d_2d_v091_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_slope_252d_2d_v109_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_sm252_slope63_2d_v111_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_slopez_63_252_2d_v114_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_slope_rank_gap_2d_v117_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_slope_504d_2d_v118_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_distmed_378d_slopez_126_504_2d_v120_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_upper_gap_126d_slopez_21_126_2d_v128_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_upper_gap_126d_slope_rank_gap_2d_v132_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_upper_gap_126d_slope_504d_2d_v133_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_upper_gap_126d_slopez_126_504_2d_v135_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_lower_gap_126d_slopez_63_252_2d_v144_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_lower_gap_126d_slope_rank_gap_2d_v147_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_lower_gap_126d_slope_504d_2d_v148_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_lower_gap_126d_slopez_126_504_2d_v150_signal]}
BREAKOUTS_REGISTRY_2ND_001_150 = REGISTRY

if __name__ == "__main__":
    print(f"registered {len(REGISTRY)} breakout feature functions")
