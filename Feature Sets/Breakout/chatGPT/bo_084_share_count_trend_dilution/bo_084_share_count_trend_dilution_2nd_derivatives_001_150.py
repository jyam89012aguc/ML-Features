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


# 21d slope for share_count_dilution
def bo_084_share_count_trend_dilution_share_count_dilution_slope_21d_2d_v001_signal(shareswadil):
    base = _growth(shareswadil, 252)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for share_count_dilution
def bo_084_share_count_trend_dilution_share_count_dilution_slope_63d_2d_v002_signal(shareswadil):
    base = _growth(shareswadil, 252)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for share_count_dilution
def bo_084_share_count_trend_dilution_share_count_dilution_slope_126d_2d_v003_signal(shareswadil):
    base = _growth(shareswadil, 252)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for share_count_dilution
def bo_084_share_count_trend_dilution_share_count_dilution_slope_252d_2d_v004_signal(shareswadil):
    base = _growth(shareswadil, 252)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for share_count_dilution
def bo_084_share_count_trend_dilution_share_count_dilution_sm63_slope21_2d_v005_signal(shareswadil):
    base = _growth(shareswadil, 252)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for share_count_dilution
def bo_084_share_count_trend_dilution_share_count_dilution_sm252_slope63_2d_v006_signal(shareswadil):
    base = _growth(shareswadil, 252)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for share_count_dilution
def bo_084_share_count_trend_dilution_share_count_dilution_pctslope_63d_2d_v007_signal(shareswadil):
    base = _growth(shareswadil, 252)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for share_count_dilution
def bo_084_share_count_trend_dilution_share_count_dilution_slopez_21_126_2d_v008_signal(shareswadil):
    base = _growth(shareswadil, 252)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for share_count_dilution
def bo_084_share_count_trend_dilution_share_count_dilution_slopez_63_252_2d_v009_signal(shareswadil):
    base = _growth(shareswadil, 252)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for share_count_dilution
def bo_084_share_count_trend_dilution_share_count_dilution_cumslope_63d_2d_v010_signal(shareswadil):
    base = _growth(shareswadil, 252)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for share_count_dilution
def bo_084_share_count_trend_dilution_share_count_dilution_logmagslope_63d_2d_v011_signal(shareswadil):
    base = _growth(shareswadil, 252)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for share_count_dilution
def bo_084_share_count_trend_dilution_share_count_dilution_slope_rank_gap_2d_v012_signal(shareswadil):
    base = _growth(shareswadil, 252)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for share_count_dilution
def bo_084_share_count_trend_dilution_share_count_dilution_slope_504d_2d_v013_signal(shareswadil):
    base = _growth(shareswadil, 252)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for share_count_dilution
def bo_084_share_count_trend_dilution_share_count_dilution_sm126_slope63_2d_v014_signal(shareswadil):
    base = _growth(shareswadil, 252)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for share_count_dilution
def bo_084_share_count_trend_dilution_share_count_dilution_slopez_126_504_2d_v015_signal(shareswadil):
    base = _growth(shareswadil, 252)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 63d slope for share_count_dilution_mean_63d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_slope_63d_2d_v017_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 63)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for share_count_dilution_mean_63d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_slope_126d_2d_v018_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 63)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for share_count_dilution_mean_63d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_slope_252d_2d_v019_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 63)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for share_count_dilution_mean_63d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_sm63_slope21_2d_v020_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 63)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for share_count_dilution_mean_63d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_sm252_slope63_2d_v021_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 63)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for share_count_dilution_mean_63d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_pctslope_63d_2d_v022_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 63)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for share_count_dilution_mean_63d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_slopez_21_126_2d_v023_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 63)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for share_count_dilution_mean_63d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_slopez_63_252_2d_v024_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 63)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for share_count_dilution_mean_63d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_cumslope_63d_2d_v025_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 63)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for share_count_dilution_mean_63d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_logmagslope_63d_2d_v026_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 63)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for share_count_dilution_mean_63d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_slope_rank_gap_2d_v027_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 63)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for share_count_dilution_mean_63d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_slope_504d_2d_v028_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 63)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for share_count_dilution_mean_63d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_sm126_slope63_2d_v029_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 63)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for share_count_dilution_mean_63d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_slopez_126_504_2d_v030_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 63)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for share_count_dilution_mean_200d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_slope_21d_2d_v031_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 200)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for share_count_dilution_mean_200d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_slope_63d_2d_v032_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 200)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for share_count_dilution_mean_200d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_slope_126d_2d_v033_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 200)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for share_count_dilution_mean_200d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_slope_252d_2d_v034_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 200)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for share_count_dilution_mean_200d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_sm63_slope21_2d_v035_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 200)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for share_count_dilution_mean_200d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_sm252_slope63_2d_v036_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 200)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for share_count_dilution_mean_200d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_pctslope_63d_2d_v037_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 200)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for share_count_dilution_mean_200d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_slopez_21_126_2d_v038_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 200)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for share_count_dilution_mean_200d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_slopez_63_252_2d_v039_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 200)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for share_count_dilution_mean_200d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_cumslope_63d_2d_v040_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 200)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for share_count_dilution_mean_200d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_logmagslope_63d_2d_v041_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 200)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for share_count_dilution_mean_200d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_slope_rank_gap_2d_v042_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 200)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for share_count_dilution_mean_200d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_slope_504d_2d_v043_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 200)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for share_count_dilution_mean_200d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_sm126_slope63_2d_v044_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 200)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for share_count_dilution_mean_200d
def bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_slopez_126_504_2d_v045_signal(shareswadil):
    base = _mean(_growth(shareswadil, 252), 200)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for share_count_dilution_z_200d
def bo_084_share_count_trend_dilution_share_count_dilution_z_200d_slope_21d_2d_v046_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 200)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for share_count_dilution_z_200d
def bo_084_share_count_trend_dilution_share_count_dilution_z_200d_slope_63d_2d_v047_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 200)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for share_count_dilution_z_200d
def bo_084_share_count_trend_dilution_share_count_dilution_z_200d_slope_126d_2d_v048_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 200)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for share_count_dilution_z_200d
def bo_084_share_count_trend_dilution_share_count_dilution_z_200d_slope_252d_2d_v049_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 200)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for share_count_dilution_z_200d
def bo_084_share_count_trend_dilution_share_count_dilution_z_200d_sm63_slope21_2d_v050_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 200)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for share_count_dilution_z_200d
def bo_084_share_count_trend_dilution_share_count_dilution_z_200d_sm252_slope63_2d_v051_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 200)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for share_count_dilution_z_200d
def bo_084_share_count_trend_dilution_share_count_dilution_z_200d_pctslope_63d_2d_v052_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 200)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for share_count_dilution_z_200d
def bo_084_share_count_trend_dilution_share_count_dilution_z_200d_slopez_21_126_2d_v053_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 200)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for share_count_dilution_z_200d
def bo_084_share_count_trend_dilution_share_count_dilution_z_200d_slopez_63_252_2d_v054_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 200)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for share_count_dilution_z_200d
def bo_084_share_count_trend_dilution_share_count_dilution_z_200d_cumslope_63d_2d_v055_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 200)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for share_count_dilution_z_200d
def bo_084_share_count_trend_dilution_share_count_dilution_z_200d_logmagslope_63d_2d_v056_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 200)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for share_count_dilution_z_200d
def bo_084_share_count_trend_dilution_share_count_dilution_z_200d_slope_rank_gap_2d_v057_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 200)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for share_count_dilution_z_200d
def bo_084_share_count_trend_dilution_share_count_dilution_z_200d_slope_504d_2d_v058_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 200)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for share_count_dilution_z_200d
def bo_084_share_count_trend_dilution_share_count_dilution_z_200d_sm126_slope63_2d_v059_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 200)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for share_count_dilution_z_200d
def bo_084_share_count_trend_dilution_share_count_dilution_z_200d_slopez_126_504_2d_v060_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 200)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for share_count_dilution_z_756d
def bo_084_share_count_trend_dilution_share_count_dilution_z_756d_slope_21d_2d_v061_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 756)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for share_count_dilution_z_756d
def bo_084_share_count_trend_dilution_share_count_dilution_z_756d_slope_63d_2d_v062_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 756)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for share_count_dilution_z_756d
def bo_084_share_count_trend_dilution_share_count_dilution_z_756d_slope_126d_2d_v063_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 756)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for share_count_dilution_z_756d
def bo_084_share_count_trend_dilution_share_count_dilution_z_756d_slope_252d_2d_v064_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 756)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for share_count_dilution_z_756d
def bo_084_share_count_trend_dilution_share_count_dilution_z_756d_sm63_slope21_2d_v065_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 756)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for share_count_dilution_z_756d
def bo_084_share_count_trend_dilution_share_count_dilution_z_756d_sm252_slope63_2d_v066_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 756)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for share_count_dilution_z_756d
def bo_084_share_count_trend_dilution_share_count_dilution_z_756d_pctslope_63d_2d_v067_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 756)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for share_count_dilution_z_756d
def bo_084_share_count_trend_dilution_share_count_dilution_z_756d_slopez_21_126_2d_v068_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 756)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for share_count_dilution_z_756d
def bo_084_share_count_trend_dilution_share_count_dilution_z_756d_slopez_63_252_2d_v069_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 756)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for share_count_dilution_z_756d
def bo_084_share_count_trend_dilution_share_count_dilution_z_756d_cumslope_63d_2d_v070_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 756)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for share_count_dilution_z_756d
def bo_084_share_count_trend_dilution_share_count_dilution_z_756d_logmagslope_63d_2d_v071_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 756)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for share_count_dilution_z_756d
def bo_084_share_count_trend_dilution_share_count_dilution_z_756d_slope_rank_gap_2d_v072_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 756)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for share_count_dilution_z_756d
def bo_084_share_count_trend_dilution_share_count_dilution_z_756d_slope_504d_2d_v073_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 756)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for share_count_dilution_z_756d
def bo_084_share_count_trend_dilution_share_count_dilution_z_756d_sm126_slope63_2d_v074_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 756)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for share_count_dilution_z_756d
def bo_084_share_count_trend_dilution_share_count_dilution_z_756d_slopez_126_504_2d_v075_signal(shareswadil):
    base = _z(_growth(shareswadil, 252), 756)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for share_count_dilution_distmax_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_slope_21d_2d_v076_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for share_count_dilution_distmax_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_slope_63d_2d_v077_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for share_count_dilution_distmax_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_slope_126d_2d_v078_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for share_count_dilution_distmax_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_slope_252d_2d_v079_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for share_count_dilution_distmax_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_sm63_slope21_2d_v080_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for share_count_dilution_distmax_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_sm252_slope63_2d_v081_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for share_count_dilution_distmax_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_pctslope_63d_2d_v082_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for share_count_dilution_distmax_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_slopez_21_126_2d_v083_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for share_count_dilution_distmax_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_slopez_63_252_2d_v084_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for share_count_dilution_distmax_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_cumslope_63d_2d_v085_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for share_count_dilution_distmax_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_logmagslope_63d_2d_v086_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for share_count_dilution_distmax_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_slope_rank_gap_2d_v087_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for share_count_dilution_distmax_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_slope_504d_2d_v088_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for share_count_dilution_distmax_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_sm126_slope63_2d_v089_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for share_count_dilution_distmax_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_slopez_126_504_2d_v090_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for share_count_dilution_distmin_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_slope_21d_2d_v091_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for share_count_dilution_distmin_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_slope_63d_2d_v092_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for share_count_dilution_distmin_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_slope_126d_2d_v093_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for share_count_dilution_distmin_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_slope_252d_2d_v094_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for share_count_dilution_distmin_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_sm63_slope21_2d_v095_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for share_count_dilution_distmin_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_sm252_slope63_2d_v096_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for share_count_dilution_distmin_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_pctslope_63d_2d_v097_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for share_count_dilution_distmin_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_slopez_21_126_2d_v098_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for share_count_dilution_distmin_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_slopez_63_252_2d_v099_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for share_count_dilution_distmin_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_cumslope_63d_2d_v100_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for share_count_dilution_distmin_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_logmagslope_63d_2d_v101_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min().abs())
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for share_count_dilution_distmin_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_slope_rank_gap_2d_v102_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for share_count_dilution_distmin_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_slope_504d_2d_v103_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for share_count_dilution_distmin_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_sm126_slope63_2d_v104_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for share_count_dilution_distmin_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_slopez_126_504_2d_v105_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for share_count_dilution_distmed_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_slope_21d_2d_v106_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for share_count_dilution_distmed_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_slope_63d_2d_v107_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for share_count_dilution_distmed_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_slope_126d_2d_v108_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for share_count_dilution_distmed_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_slope_252d_2d_v109_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for share_count_dilution_distmed_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_sm63_slope21_2d_v110_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for share_count_dilution_distmed_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_sm252_slope63_2d_v111_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for share_count_dilution_distmed_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_pctslope_63d_2d_v112_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for share_count_dilution_distmed_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_slopez_21_126_2d_v113_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for share_count_dilution_distmed_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_slopez_63_252_2d_v114_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for share_count_dilution_distmed_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_cumslope_63d_2d_v115_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for share_count_dilution_distmed_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_logmagslope_63d_2d_v116_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median().abs())
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for share_count_dilution_distmed_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_slope_rank_gap_2d_v117_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for share_count_dilution_distmed_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_slope_504d_2d_v118_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for share_count_dilution_distmed_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_sm126_slope63_2d_v119_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for share_count_dilution_distmed_756d
def bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_slopez_126_504_2d_v120_signal(shareswadil):
    base = _safe_div((_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median(), (_growth(shareswadil, 252)).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for share_count_dilution_upper_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_slope_21d_2d_v121_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for share_count_dilution_upper_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_slope_63d_2d_v122_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for share_count_dilution_upper_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_slope_126d_2d_v123_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for share_count_dilution_upper_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_slope_252d_2d_v124_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for share_count_dilution_upper_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_sm63_slope21_2d_v125_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for share_count_dilution_upper_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_sm252_slope63_2d_v126_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for share_count_dilution_upper_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_pctslope_63d_2d_v127_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for share_count_dilution_upper_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_slopez_21_126_2d_v128_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for share_count_dilution_upper_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_slopez_63_252_2d_v129_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for share_count_dilution_upper_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_cumslope_63d_2d_v130_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for share_count_dilution_upper_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_logmagslope_63d_2d_v131_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for share_count_dilution_upper_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_slope_rank_gap_2d_v132_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for share_count_dilution_upper_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_slope_504d_2d_v133_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for share_count_dilution_upper_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_sm126_slope63_2d_v134_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for share_count_dilution_upper_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_slopez_126_504_2d_v135_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for share_count_dilution_lower_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_slope_21d_2d_v136_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for share_count_dilution_lower_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_slope_63d_2d_v137_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for share_count_dilution_lower_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_slope_126d_2d_v138_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for share_count_dilution_lower_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_slope_252d_2d_v139_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for share_count_dilution_lower_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_sm63_slope21_2d_v140_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for share_count_dilution_lower_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_sm252_slope63_2d_v141_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for share_count_dilution_lower_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_pctslope_63d_2d_v142_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for share_count_dilution_lower_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_slopez_21_126_2d_v143_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for share_count_dilution_lower_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_slopez_63_252_2d_v144_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for share_count_dilution_lower_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_cumslope_63d_2d_v145_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for share_count_dilution_lower_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_logmagslope_63d_2d_v146_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for share_count_dilution_lower_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_slope_rank_gap_2d_v147_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for share_count_dilution_lower_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_slope_504d_2d_v148_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for share_count_dilution_lower_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_sm126_slope63_2d_v149_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for share_count_dilution_lower_gap_200d
def bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_slopez_126_504_2d_v150_signal(shareswadil):
    base = (_growth(shareswadil, 252)) - (_growth(shareswadil, 252)).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

REGISTRY = {fn.__name__: {"inputs": ['shareswadil'], "func": fn} for fn in [bo_084_share_count_trend_dilution_share_count_dilution_slope_21d_2d_v001_signal, bo_084_share_count_trend_dilution_share_count_dilution_slope_63d_2d_v002_signal, bo_084_share_count_trend_dilution_share_count_dilution_slope_126d_2d_v003_signal, bo_084_share_count_trend_dilution_share_count_dilution_slope_252d_2d_v004_signal, bo_084_share_count_trend_dilution_share_count_dilution_sm63_slope21_2d_v005_signal, bo_084_share_count_trend_dilution_share_count_dilution_sm252_slope63_2d_v006_signal, bo_084_share_count_trend_dilution_share_count_dilution_pctslope_63d_2d_v007_signal, bo_084_share_count_trend_dilution_share_count_dilution_slopez_21_126_2d_v008_signal, bo_084_share_count_trend_dilution_share_count_dilution_slopez_63_252_2d_v009_signal, bo_084_share_count_trend_dilution_share_count_dilution_cumslope_63d_2d_v010_signal, bo_084_share_count_trend_dilution_share_count_dilution_logmagslope_63d_2d_v011_signal, bo_084_share_count_trend_dilution_share_count_dilution_slope_rank_gap_2d_v012_signal, bo_084_share_count_trend_dilution_share_count_dilution_slope_504d_2d_v013_signal, bo_084_share_count_trend_dilution_share_count_dilution_sm126_slope63_2d_v014_signal, bo_084_share_count_trend_dilution_share_count_dilution_slopez_126_504_2d_v015_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_slope_63d_2d_v017_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_slope_126d_2d_v018_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_slope_252d_2d_v019_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_sm63_slope21_2d_v020_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_sm252_slope63_2d_v021_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_pctslope_63d_2d_v022_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_slopez_21_126_2d_v023_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_slopez_63_252_2d_v024_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_cumslope_63d_2d_v025_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_logmagslope_63d_2d_v026_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_slope_rank_gap_2d_v027_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_slope_504d_2d_v028_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_sm126_slope63_2d_v029_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_63d_slopez_126_504_2d_v030_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_slope_21d_2d_v031_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_slope_63d_2d_v032_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_slope_126d_2d_v033_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_slope_252d_2d_v034_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_sm63_slope21_2d_v035_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_sm252_slope63_2d_v036_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_pctslope_63d_2d_v037_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_slopez_21_126_2d_v038_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_slopez_63_252_2d_v039_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_cumslope_63d_2d_v040_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_logmagslope_63d_2d_v041_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_slope_rank_gap_2d_v042_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_slope_504d_2d_v043_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_sm126_slope63_2d_v044_signal, bo_084_share_count_trend_dilution_share_count_dilution_mean_200d_slopez_126_504_2d_v045_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_200d_slope_21d_2d_v046_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_200d_slope_63d_2d_v047_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_200d_slope_126d_2d_v048_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_200d_slope_252d_2d_v049_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_200d_sm63_slope21_2d_v050_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_200d_sm252_slope63_2d_v051_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_200d_pctslope_63d_2d_v052_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_200d_slopez_21_126_2d_v053_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_200d_slopez_63_252_2d_v054_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_200d_cumslope_63d_2d_v055_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_200d_logmagslope_63d_2d_v056_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_200d_slope_rank_gap_2d_v057_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_200d_slope_504d_2d_v058_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_200d_sm126_slope63_2d_v059_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_200d_slopez_126_504_2d_v060_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_756d_slope_21d_2d_v061_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_756d_slope_63d_2d_v062_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_756d_slope_126d_2d_v063_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_756d_slope_252d_2d_v064_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_756d_sm63_slope21_2d_v065_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_756d_sm252_slope63_2d_v066_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_756d_pctslope_63d_2d_v067_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_756d_slopez_21_126_2d_v068_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_756d_slopez_63_252_2d_v069_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_756d_cumslope_63d_2d_v070_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_756d_logmagslope_63d_2d_v071_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_756d_slope_rank_gap_2d_v072_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_756d_slope_504d_2d_v073_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_756d_sm126_slope63_2d_v074_signal, bo_084_share_count_trend_dilution_share_count_dilution_z_756d_slopez_126_504_2d_v075_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_slope_21d_2d_v076_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_slope_63d_2d_v077_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_slope_126d_2d_v078_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_slope_252d_2d_v079_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_sm63_slope21_2d_v080_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_sm252_slope63_2d_v081_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_pctslope_63d_2d_v082_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_slopez_21_126_2d_v083_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_slopez_63_252_2d_v084_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_cumslope_63d_2d_v085_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_logmagslope_63d_2d_v086_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_slope_rank_gap_2d_v087_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_slope_504d_2d_v088_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_sm126_slope63_2d_v089_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmax_756d_slopez_126_504_2d_v090_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_slope_21d_2d_v091_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_slope_63d_2d_v092_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_slope_126d_2d_v093_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_slope_252d_2d_v094_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_sm63_slope21_2d_v095_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_sm252_slope63_2d_v096_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_pctslope_63d_2d_v097_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_slopez_21_126_2d_v098_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_slopez_63_252_2d_v099_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_cumslope_63d_2d_v100_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_logmagslope_63d_2d_v101_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_slope_rank_gap_2d_v102_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_slope_504d_2d_v103_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_sm126_slope63_2d_v104_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmin_756d_slopez_126_504_2d_v105_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_slope_21d_2d_v106_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_slope_63d_2d_v107_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_slope_126d_2d_v108_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_slope_252d_2d_v109_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_sm63_slope21_2d_v110_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_sm252_slope63_2d_v111_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_pctslope_63d_2d_v112_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_slopez_21_126_2d_v113_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_slopez_63_252_2d_v114_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_cumslope_63d_2d_v115_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_logmagslope_63d_2d_v116_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_slope_rank_gap_2d_v117_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_slope_504d_2d_v118_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_sm126_slope63_2d_v119_signal, bo_084_share_count_trend_dilution_share_count_dilution_distmed_756d_slopez_126_504_2d_v120_signal, bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_slope_21d_2d_v121_signal, bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_slope_63d_2d_v122_signal, bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_slope_126d_2d_v123_signal, bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_slope_252d_2d_v124_signal, bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_sm63_slope21_2d_v125_signal, bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_sm252_slope63_2d_v126_signal, bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_pctslope_63d_2d_v127_signal, bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_slopez_21_126_2d_v128_signal, bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_slopez_63_252_2d_v129_signal, bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_cumslope_63d_2d_v130_signal, bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_logmagslope_63d_2d_v131_signal, bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_slope_rank_gap_2d_v132_signal, bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_slope_504d_2d_v133_signal, bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_sm126_slope63_2d_v134_signal, bo_084_share_count_trend_dilution_share_count_dilution_upper_gap_200d_slopez_126_504_2d_v135_signal, bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_slope_21d_2d_v136_signal, bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_slope_63d_2d_v137_signal, bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_slope_126d_2d_v138_signal, bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_slope_252d_2d_v139_signal, bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_sm63_slope21_2d_v140_signal, bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_sm252_slope63_2d_v141_signal, bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_pctslope_63d_2d_v142_signal, bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_slopez_21_126_2d_v143_signal, bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_slopez_63_252_2d_v144_signal, bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_cumslope_63d_2d_v145_signal, bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_logmagslope_63d_2d_v146_signal, bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_slope_rank_gap_2d_v147_signal, bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_slope_504d_2d_v148_signal, bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_sm126_slope63_2d_v149_signal, bo_084_share_count_trend_dilution_share_count_dilution_lower_gap_200d_slopez_126_504_2d_v150_signal]}
BREAKOUTS_REGISTRY_2ND_001_150 = REGISTRY

if __name__ == "__main__":
    print(f"registered {len(REGISTRY)} breakout feature functions")
