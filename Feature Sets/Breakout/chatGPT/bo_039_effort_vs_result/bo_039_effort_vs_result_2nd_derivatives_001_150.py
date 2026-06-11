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


# 21d slope for effort_vs_result
def bo_039_effort_vs_result_effort_vs_result_slope_21d_2d_v001_signal(volume, closeadj):
    base = _safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for effort_vs_result
def bo_039_effort_vs_result_effort_vs_result_slope_63d_2d_v002_signal(volume, closeadj):
    base = _safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for effort_vs_result
def bo_039_effort_vs_result_effort_vs_result_slope_126d_2d_v003_signal(volume, closeadj):
    base = _safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for effort_vs_result
def bo_039_effort_vs_result_effort_vs_result_slope_252d_2d_v004_signal(volume, closeadj):
    base = _safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for effort_vs_result
def bo_039_effort_vs_result_effort_vs_result_sm63_slope21_2d_v005_signal(volume, closeadj):
    base = _safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for effort_vs_result
def bo_039_effort_vs_result_effort_vs_result_sm252_slope63_2d_v006_signal(volume, closeadj):
    base = _safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for effort_vs_result
def bo_039_effort_vs_result_effort_vs_result_pctslope_63d_2d_v007_signal(volume, closeadj):
    base = _safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for effort_vs_result
def bo_039_effort_vs_result_effort_vs_result_slopez_21_126_2d_v008_signal(volume, closeadj):
    base = _safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for effort_vs_result
def bo_039_effort_vs_result_effort_vs_result_slopez_63_252_2d_v009_signal(volume, closeadj):
    base = _safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for effort_vs_result
def bo_039_effort_vs_result_effort_vs_result_cumslope_63d_2d_v010_signal(volume, closeadj):
    base = _safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for effort_vs_result
def bo_039_effort_vs_result_effort_vs_result_logmagslope_63d_2d_v011_signal(volume, closeadj):
    base = _safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for effort_vs_result
def bo_039_effort_vs_result_effort_vs_result_slope_rank_gap_2d_v012_signal(volume, closeadj):
    base = _safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for effort_vs_result
def bo_039_effort_vs_result_effort_vs_result_slope_504d_2d_v013_signal(volume, closeadj):
    base = _safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for effort_vs_result
def bo_039_effort_vs_result_effort_vs_result_sm126_slope63_2d_v014_signal(volume, closeadj):
    base = _safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for effort_vs_result
def bo_039_effort_vs_result_effort_vs_result_slopez_126_504_2d_v015_signal(volume, closeadj):
    base = _safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 63d slope for effort_vs_result_mean_63d
def bo_039_effort_vs_result_effort_vs_result_mean_63d_slope_63d_2d_v017_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 63)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for effort_vs_result_mean_63d
def bo_039_effort_vs_result_effort_vs_result_mean_63d_slope_126d_2d_v018_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 63)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for effort_vs_result_mean_63d
def bo_039_effort_vs_result_effort_vs_result_mean_63d_slope_252d_2d_v019_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 63)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for effort_vs_result_mean_63d
def bo_039_effort_vs_result_effort_vs_result_mean_63d_sm63_slope21_2d_v020_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 63)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for effort_vs_result_mean_63d
def bo_039_effort_vs_result_effort_vs_result_mean_63d_sm252_slope63_2d_v021_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 63)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for effort_vs_result_mean_63d
def bo_039_effort_vs_result_effort_vs_result_mean_63d_pctslope_63d_2d_v022_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 63)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for effort_vs_result_mean_63d
def bo_039_effort_vs_result_effort_vs_result_mean_63d_slopez_21_126_2d_v023_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 63)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for effort_vs_result_mean_63d
def bo_039_effort_vs_result_effort_vs_result_mean_63d_slopez_63_252_2d_v024_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 63)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for effort_vs_result_mean_63d
def bo_039_effort_vs_result_effort_vs_result_mean_63d_cumslope_63d_2d_v025_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 63)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for effort_vs_result_mean_63d
def bo_039_effort_vs_result_effort_vs_result_mean_63d_logmagslope_63d_2d_v026_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 63)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for effort_vs_result_mean_63d
def bo_039_effort_vs_result_effort_vs_result_mean_63d_slope_rank_gap_2d_v027_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 63)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for effort_vs_result_mean_63d
def bo_039_effort_vs_result_effort_vs_result_mean_63d_slope_504d_2d_v028_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 63)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for effort_vs_result_mean_63d
def bo_039_effort_vs_result_effort_vs_result_mean_63d_sm126_slope63_2d_v029_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 63)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for effort_vs_result_mean_63d
def bo_039_effort_vs_result_effort_vs_result_mean_63d_slopez_126_504_2d_v030_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 63)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for effort_vs_result_mean_200d
def bo_039_effort_vs_result_effort_vs_result_mean_200d_slope_21d_2d_v031_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for effort_vs_result_mean_200d
def bo_039_effort_vs_result_effort_vs_result_mean_200d_slope_63d_2d_v032_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for effort_vs_result_mean_200d
def bo_039_effort_vs_result_effort_vs_result_mean_200d_slope_126d_2d_v033_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for effort_vs_result_mean_200d
def bo_039_effort_vs_result_effort_vs_result_mean_200d_slope_252d_2d_v034_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for effort_vs_result_mean_200d
def bo_039_effort_vs_result_effort_vs_result_mean_200d_sm63_slope21_2d_v035_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for effort_vs_result_mean_200d
def bo_039_effort_vs_result_effort_vs_result_mean_200d_sm252_slope63_2d_v036_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for effort_vs_result_mean_200d
def bo_039_effort_vs_result_effort_vs_result_mean_200d_pctslope_63d_2d_v037_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for effort_vs_result_mean_200d
def bo_039_effort_vs_result_effort_vs_result_mean_200d_slopez_21_126_2d_v038_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for effort_vs_result_mean_200d
def bo_039_effort_vs_result_effort_vs_result_mean_200d_slopez_63_252_2d_v039_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for effort_vs_result_mean_200d
def bo_039_effort_vs_result_effort_vs_result_mean_200d_cumslope_63d_2d_v040_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for effort_vs_result_mean_200d
def bo_039_effort_vs_result_effort_vs_result_mean_200d_logmagslope_63d_2d_v041_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for effort_vs_result_mean_200d
def bo_039_effort_vs_result_effort_vs_result_mean_200d_slope_rank_gap_2d_v042_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for effort_vs_result_mean_200d
def bo_039_effort_vs_result_effort_vs_result_mean_200d_slope_504d_2d_v043_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for effort_vs_result_mean_200d
def bo_039_effort_vs_result_effort_vs_result_mean_200d_sm126_slope63_2d_v044_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for effort_vs_result_mean_200d
def bo_039_effort_vs_result_effort_vs_result_mean_200d_slopez_126_504_2d_v045_signal(volume, closeadj):
    base = _mean(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for effort_vs_result_z_200d
def bo_039_effort_vs_result_effort_vs_result_z_200d_slope_21d_2d_v046_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for effort_vs_result_z_200d
def bo_039_effort_vs_result_effort_vs_result_z_200d_slope_63d_2d_v047_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for effort_vs_result_z_200d
def bo_039_effort_vs_result_effort_vs_result_z_200d_slope_126d_2d_v048_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for effort_vs_result_z_200d
def bo_039_effort_vs_result_effort_vs_result_z_200d_slope_252d_2d_v049_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for effort_vs_result_z_200d
def bo_039_effort_vs_result_effort_vs_result_z_200d_sm63_slope21_2d_v050_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for effort_vs_result_z_200d
def bo_039_effort_vs_result_effort_vs_result_z_200d_sm252_slope63_2d_v051_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for effort_vs_result_z_200d
def bo_039_effort_vs_result_effort_vs_result_z_200d_pctslope_63d_2d_v052_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for effort_vs_result_z_200d
def bo_039_effort_vs_result_effort_vs_result_z_200d_slopez_21_126_2d_v053_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for effort_vs_result_z_200d
def bo_039_effort_vs_result_effort_vs_result_z_200d_slopez_63_252_2d_v054_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for effort_vs_result_z_200d
def bo_039_effort_vs_result_effort_vs_result_z_200d_cumslope_63d_2d_v055_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for effort_vs_result_z_200d
def bo_039_effort_vs_result_effort_vs_result_z_200d_logmagslope_63d_2d_v056_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for effort_vs_result_z_200d
def bo_039_effort_vs_result_effort_vs_result_z_200d_slope_rank_gap_2d_v057_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for effort_vs_result_z_200d
def bo_039_effort_vs_result_effort_vs_result_z_200d_slope_504d_2d_v058_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for effort_vs_result_z_200d
def bo_039_effort_vs_result_effort_vs_result_z_200d_sm126_slope63_2d_v059_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for effort_vs_result_z_200d
def bo_039_effort_vs_result_effort_vs_result_z_200d_slopez_126_504_2d_v060_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 200)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for effort_vs_result_z_756d
def bo_039_effort_vs_result_effort_vs_result_z_756d_slope_21d_2d_v061_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 756)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for effort_vs_result_z_756d
def bo_039_effort_vs_result_effort_vs_result_z_756d_slope_63d_2d_v062_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 756)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for effort_vs_result_z_756d
def bo_039_effort_vs_result_effort_vs_result_z_756d_slope_126d_2d_v063_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 756)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for effort_vs_result_z_756d
def bo_039_effort_vs_result_effort_vs_result_z_756d_slope_252d_2d_v064_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 756)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for effort_vs_result_z_756d
def bo_039_effort_vs_result_effort_vs_result_z_756d_sm63_slope21_2d_v065_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 756)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for effort_vs_result_z_756d
def bo_039_effort_vs_result_effort_vs_result_z_756d_sm252_slope63_2d_v066_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 756)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for effort_vs_result_z_756d
def bo_039_effort_vs_result_effort_vs_result_z_756d_pctslope_63d_2d_v067_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 756)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for effort_vs_result_z_756d
def bo_039_effort_vs_result_effort_vs_result_z_756d_slopez_21_126_2d_v068_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 756)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for effort_vs_result_z_756d
def bo_039_effort_vs_result_effort_vs_result_z_756d_slopez_63_252_2d_v069_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 756)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for effort_vs_result_z_756d
def bo_039_effort_vs_result_effort_vs_result_z_756d_cumslope_63d_2d_v070_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 756)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for effort_vs_result_z_756d
def bo_039_effort_vs_result_effort_vs_result_z_756d_logmagslope_63d_2d_v071_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 756)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for effort_vs_result_z_756d
def bo_039_effort_vs_result_effort_vs_result_z_756d_slope_rank_gap_2d_v072_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 756)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for effort_vs_result_z_756d
def bo_039_effort_vs_result_effort_vs_result_z_756d_slope_504d_2d_v073_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 756)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for effort_vs_result_z_756d
def bo_039_effort_vs_result_effort_vs_result_z_756d_sm126_slope63_2d_v074_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 756)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for effort_vs_result_z_756d
def bo_039_effort_vs_result_effort_vs_result_z_756d_slopez_126_504_2d_v075_signal(volume, closeadj):
    base = _z(_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs()), 756)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for effort_vs_result_distmax_756d
def bo_039_effort_vs_result_effort_vs_result_distmax_756d_slope_21d_2d_v076_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for effort_vs_result_distmax_756d
def bo_039_effort_vs_result_effort_vs_result_distmax_756d_slope_63d_2d_v077_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for effort_vs_result_distmax_756d
def bo_039_effort_vs_result_effort_vs_result_distmax_756d_slope_126d_2d_v078_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for effort_vs_result_distmax_756d
def bo_039_effort_vs_result_effort_vs_result_distmax_756d_slope_252d_2d_v079_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for effort_vs_result_distmax_756d
def bo_039_effort_vs_result_effort_vs_result_distmax_756d_sm63_slope21_2d_v080_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for effort_vs_result_distmax_756d
def bo_039_effort_vs_result_effort_vs_result_distmax_756d_sm252_slope63_2d_v081_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for effort_vs_result_distmax_756d
def bo_039_effort_vs_result_effort_vs_result_distmax_756d_pctslope_63d_2d_v082_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for effort_vs_result_distmax_756d
def bo_039_effort_vs_result_effort_vs_result_distmax_756d_slopez_21_126_2d_v083_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for effort_vs_result_distmax_756d
def bo_039_effort_vs_result_effort_vs_result_distmax_756d_slopez_63_252_2d_v084_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for effort_vs_result_distmax_756d
def bo_039_effort_vs_result_effort_vs_result_distmax_756d_cumslope_63d_2d_v085_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for effort_vs_result_distmax_756d
def bo_039_effort_vs_result_effort_vs_result_distmax_756d_logmagslope_63d_2d_v086_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for effort_vs_result_distmax_756d
def bo_039_effort_vs_result_effort_vs_result_distmax_756d_slope_rank_gap_2d_v087_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for effort_vs_result_distmax_756d
def bo_039_effort_vs_result_effort_vs_result_distmax_756d_slope_504d_2d_v088_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for effort_vs_result_distmax_756d
def bo_039_effort_vs_result_effort_vs_result_distmax_756d_sm126_slope63_2d_v089_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for effort_vs_result_distmax_756d
def bo_039_effort_vs_result_effort_vs_result_distmax_756d_slopez_126_504_2d_v090_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).max().abs())
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for effort_vs_result_distmin_756d
def bo_039_effort_vs_result_effort_vs_result_distmin_756d_slope_21d_2d_v091_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for effort_vs_result_distmin_756d
def bo_039_effort_vs_result_effort_vs_result_distmin_756d_slope_63d_2d_v092_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for effort_vs_result_distmin_756d
def bo_039_effort_vs_result_effort_vs_result_distmin_756d_slope_126d_2d_v093_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for effort_vs_result_distmin_756d
def bo_039_effort_vs_result_effort_vs_result_distmin_756d_slope_252d_2d_v094_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for effort_vs_result_distmin_756d
def bo_039_effort_vs_result_effort_vs_result_distmin_756d_sm63_slope21_2d_v095_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for effort_vs_result_distmin_756d
def bo_039_effort_vs_result_effort_vs_result_distmin_756d_sm252_slope63_2d_v096_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for effort_vs_result_distmin_756d
def bo_039_effort_vs_result_effort_vs_result_distmin_756d_pctslope_63d_2d_v097_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for effort_vs_result_distmin_756d
def bo_039_effort_vs_result_effort_vs_result_distmin_756d_slopez_21_126_2d_v098_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for effort_vs_result_distmin_756d
def bo_039_effort_vs_result_effort_vs_result_distmin_756d_slopez_63_252_2d_v099_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for effort_vs_result_distmin_756d
def bo_039_effort_vs_result_effort_vs_result_distmin_756d_cumslope_63d_2d_v100_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for effort_vs_result_distmin_756d
def bo_039_effort_vs_result_effort_vs_result_distmin_756d_logmagslope_63d_2d_v101_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for effort_vs_result_distmin_756d
def bo_039_effort_vs_result_effort_vs_result_distmin_756d_slope_rank_gap_2d_v102_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for effort_vs_result_distmin_756d
def bo_039_effort_vs_result_effort_vs_result_distmin_756d_slope_504d_2d_v103_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for effort_vs_result_distmin_756d
def bo_039_effort_vs_result_effort_vs_result_distmin_756d_sm126_slope63_2d_v104_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for effort_vs_result_distmin_756d
def bo_039_effort_vs_result_effort_vs_result_distmin_756d_slopez_126_504_2d_v105_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).min().abs())
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for effort_vs_result_distmed_756d
def bo_039_effort_vs_result_effort_vs_result_distmed_756d_slope_21d_2d_v106_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for effort_vs_result_distmed_756d
def bo_039_effort_vs_result_effort_vs_result_distmed_756d_slope_63d_2d_v107_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for effort_vs_result_distmed_756d
def bo_039_effort_vs_result_effort_vs_result_distmed_756d_slope_126d_2d_v108_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for effort_vs_result_distmed_756d
def bo_039_effort_vs_result_effort_vs_result_distmed_756d_slope_252d_2d_v109_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for effort_vs_result_distmed_756d
def bo_039_effort_vs_result_effort_vs_result_distmed_756d_sm63_slope21_2d_v110_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for effort_vs_result_distmed_756d
def bo_039_effort_vs_result_effort_vs_result_distmed_756d_sm252_slope63_2d_v111_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for effort_vs_result_distmed_756d
def bo_039_effort_vs_result_effort_vs_result_distmed_756d_pctslope_63d_2d_v112_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for effort_vs_result_distmed_756d
def bo_039_effort_vs_result_effort_vs_result_distmed_756d_slopez_21_126_2d_v113_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for effort_vs_result_distmed_756d
def bo_039_effort_vs_result_effort_vs_result_distmed_756d_slopez_63_252_2d_v114_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for effort_vs_result_distmed_756d
def bo_039_effort_vs_result_effort_vs_result_distmed_756d_cumslope_63d_2d_v115_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for effort_vs_result_distmed_756d
def bo_039_effort_vs_result_effort_vs_result_distmed_756d_logmagslope_63d_2d_v116_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for effort_vs_result_distmed_756d
def bo_039_effort_vs_result_effort_vs_result_distmed_756d_slope_rank_gap_2d_v117_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for effort_vs_result_distmed_756d
def bo_039_effort_vs_result_effort_vs_result_distmed_756d_slope_504d_2d_v118_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for effort_vs_result_distmed_756d
def bo_039_effort_vs_result_effort_vs_result_distmed_756d_sm126_slope63_2d_v119_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for effort_vs_result_distmed_756d
def bo_039_effort_vs_result_effort_vs_result_distmed_756d_slopez_126_504_2d_v120_signal(volume, closeadj):
    base = _safe_div((_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median(), (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(756, min_periods=max(2, 756//2)).median().abs())
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for effort_vs_result_upper_gap_200d
def bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_slope_21d_2d_v121_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for effort_vs_result_upper_gap_200d
def bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_slope_63d_2d_v122_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for effort_vs_result_upper_gap_200d
def bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_slope_126d_2d_v123_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for effort_vs_result_upper_gap_200d
def bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_slope_252d_2d_v124_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for effort_vs_result_upper_gap_200d
def bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_sm63_slope21_2d_v125_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for effort_vs_result_upper_gap_200d
def bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_sm252_slope63_2d_v126_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for effort_vs_result_upper_gap_200d
def bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_pctslope_63d_2d_v127_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for effort_vs_result_upper_gap_200d
def bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_slopez_21_126_2d_v128_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for effort_vs_result_upper_gap_200d
def bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_slopez_63_252_2d_v129_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for effort_vs_result_upper_gap_200d
def bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_cumslope_63d_2d_v130_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for effort_vs_result_upper_gap_200d
def bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_logmagslope_63d_2d_v131_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for effort_vs_result_upper_gap_200d
def bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_slope_rank_gap_2d_v132_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for effort_vs_result_upper_gap_200d
def bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_slope_504d_2d_v133_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for effort_vs_result_upper_gap_200d
def bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_sm126_slope63_2d_v134_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for effort_vs_result_upper_gap_200d
def bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_slopez_126_504_2d_v135_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.75)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for effort_vs_result_lower_gap_200d
def bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_slope_21d_2d_v136_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for effort_vs_result_lower_gap_200d
def bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_slope_63d_2d_v137_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for effort_vs_result_lower_gap_200d
def bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_slope_126d_2d_v138_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for effort_vs_result_lower_gap_200d
def bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_slope_252d_2d_v139_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for effort_vs_result_lower_gap_200d
def bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_sm63_slope21_2d_v140_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for effort_vs_result_lower_gap_200d
def bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_sm252_slope63_2d_v141_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for effort_vs_result_lower_gap_200d
def bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_pctslope_63d_2d_v142_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for effort_vs_result_lower_gap_200d
def bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_slopez_21_126_2d_v143_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for effort_vs_result_lower_gap_200d
def bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_slopez_63_252_2d_v144_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for effort_vs_result_lower_gap_200d
def bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_cumslope_63d_2d_v145_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for effort_vs_result_lower_gap_200d
def bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_logmagslope_63d_2d_v146_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for effort_vs_result_lower_gap_200d
def bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_slope_rank_gap_2d_v147_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for effort_vs_result_lower_gap_200d
def bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_slope_504d_2d_v148_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for effort_vs_result_lower_gap_200d
def bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_sm126_slope63_2d_v149_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for effort_vs_result_lower_gap_200d
def bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_slopez_126_504_2d_v150_signal(volume, closeadj):
    base = (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())) - (_safe_div(volume.rolling(21, min_periods=11).sum(), closeadj.diff(21).abs())).rolling(200, min_periods=max(2, 200//2)).quantile(0.25)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

REGISTRY = {fn.__name__: {"inputs": ['volume', 'closeadj'], "func": fn} for fn in [bo_039_effort_vs_result_effort_vs_result_slope_21d_2d_v001_signal, bo_039_effort_vs_result_effort_vs_result_slope_63d_2d_v002_signal, bo_039_effort_vs_result_effort_vs_result_slope_126d_2d_v003_signal, bo_039_effort_vs_result_effort_vs_result_slope_252d_2d_v004_signal, bo_039_effort_vs_result_effort_vs_result_sm63_slope21_2d_v005_signal, bo_039_effort_vs_result_effort_vs_result_sm252_slope63_2d_v006_signal, bo_039_effort_vs_result_effort_vs_result_pctslope_63d_2d_v007_signal, bo_039_effort_vs_result_effort_vs_result_slopez_21_126_2d_v008_signal, bo_039_effort_vs_result_effort_vs_result_slopez_63_252_2d_v009_signal, bo_039_effort_vs_result_effort_vs_result_cumslope_63d_2d_v010_signal, bo_039_effort_vs_result_effort_vs_result_logmagslope_63d_2d_v011_signal, bo_039_effort_vs_result_effort_vs_result_slope_rank_gap_2d_v012_signal, bo_039_effort_vs_result_effort_vs_result_slope_504d_2d_v013_signal, bo_039_effort_vs_result_effort_vs_result_sm126_slope63_2d_v014_signal, bo_039_effort_vs_result_effort_vs_result_slopez_126_504_2d_v015_signal, bo_039_effort_vs_result_effort_vs_result_mean_63d_slope_63d_2d_v017_signal, bo_039_effort_vs_result_effort_vs_result_mean_63d_slope_126d_2d_v018_signal, bo_039_effort_vs_result_effort_vs_result_mean_63d_slope_252d_2d_v019_signal, bo_039_effort_vs_result_effort_vs_result_mean_63d_sm63_slope21_2d_v020_signal, bo_039_effort_vs_result_effort_vs_result_mean_63d_sm252_slope63_2d_v021_signal, bo_039_effort_vs_result_effort_vs_result_mean_63d_pctslope_63d_2d_v022_signal, bo_039_effort_vs_result_effort_vs_result_mean_63d_slopez_21_126_2d_v023_signal, bo_039_effort_vs_result_effort_vs_result_mean_63d_slopez_63_252_2d_v024_signal, bo_039_effort_vs_result_effort_vs_result_mean_63d_cumslope_63d_2d_v025_signal, bo_039_effort_vs_result_effort_vs_result_mean_63d_logmagslope_63d_2d_v026_signal, bo_039_effort_vs_result_effort_vs_result_mean_63d_slope_rank_gap_2d_v027_signal, bo_039_effort_vs_result_effort_vs_result_mean_63d_slope_504d_2d_v028_signal, bo_039_effort_vs_result_effort_vs_result_mean_63d_sm126_slope63_2d_v029_signal, bo_039_effort_vs_result_effort_vs_result_mean_63d_slopez_126_504_2d_v030_signal, bo_039_effort_vs_result_effort_vs_result_mean_200d_slope_21d_2d_v031_signal, bo_039_effort_vs_result_effort_vs_result_mean_200d_slope_63d_2d_v032_signal, bo_039_effort_vs_result_effort_vs_result_mean_200d_slope_126d_2d_v033_signal, bo_039_effort_vs_result_effort_vs_result_mean_200d_slope_252d_2d_v034_signal, bo_039_effort_vs_result_effort_vs_result_mean_200d_sm63_slope21_2d_v035_signal, bo_039_effort_vs_result_effort_vs_result_mean_200d_sm252_slope63_2d_v036_signal, bo_039_effort_vs_result_effort_vs_result_mean_200d_pctslope_63d_2d_v037_signal, bo_039_effort_vs_result_effort_vs_result_mean_200d_slopez_21_126_2d_v038_signal, bo_039_effort_vs_result_effort_vs_result_mean_200d_slopez_63_252_2d_v039_signal, bo_039_effort_vs_result_effort_vs_result_mean_200d_cumslope_63d_2d_v040_signal, bo_039_effort_vs_result_effort_vs_result_mean_200d_logmagslope_63d_2d_v041_signal, bo_039_effort_vs_result_effort_vs_result_mean_200d_slope_rank_gap_2d_v042_signal, bo_039_effort_vs_result_effort_vs_result_mean_200d_slope_504d_2d_v043_signal, bo_039_effort_vs_result_effort_vs_result_mean_200d_sm126_slope63_2d_v044_signal, bo_039_effort_vs_result_effort_vs_result_mean_200d_slopez_126_504_2d_v045_signal, bo_039_effort_vs_result_effort_vs_result_z_200d_slope_21d_2d_v046_signal, bo_039_effort_vs_result_effort_vs_result_z_200d_slope_63d_2d_v047_signal, bo_039_effort_vs_result_effort_vs_result_z_200d_slope_126d_2d_v048_signal, bo_039_effort_vs_result_effort_vs_result_z_200d_slope_252d_2d_v049_signal, bo_039_effort_vs_result_effort_vs_result_z_200d_sm63_slope21_2d_v050_signal, bo_039_effort_vs_result_effort_vs_result_z_200d_sm252_slope63_2d_v051_signal, bo_039_effort_vs_result_effort_vs_result_z_200d_pctslope_63d_2d_v052_signal, bo_039_effort_vs_result_effort_vs_result_z_200d_slopez_21_126_2d_v053_signal, bo_039_effort_vs_result_effort_vs_result_z_200d_slopez_63_252_2d_v054_signal, bo_039_effort_vs_result_effort_vs_result_z_200d_cumslope_63d_2d_v055_signal, bo_039_effort_vs_result_effort_vs_result_z_200d_logmagslope_63d_2d_v056_signal, bo_039_effort_vs_result_effort_vs_result_z_200d_slope_rank_gap_2d_v057_signal, bo_039_effort_vs_result_effort_vs_result_z_200d_slope_504d_2d_v058_signal, bo_039_effort_vs_result_effort_vs_result_z_200d_sm126_slope63_2d_v059_signal, bo_039_effort_vs_result_effort_vs_result_z_200d_slopez_126_504_2d_v060_signal, bo_039_effort_vs_result_effort_vs_result_z_756d_slope_21d_2d_v061_signal, bo_039_effort_vs_result_effort_vs_result_z_756d_slope_63d_2d_v062_signal, bo_039_effort_vs_result_effort_vs_result_z_756d_slope_126d_2d_v063_signal, bo_039_effort_vs_result_effort_vs_result_z_756d_slope_252d_2d_v064_signal, bo_039_effort_vs_result_effort_vs_result_z_756d_sm63_slope21_2d_v065_signal, bo_039_effort_vs_result_effort_vs_result_z_756d_sm252_slope63_2d_v066_signal, bo_039_effort_vs_result_effort_vs_result_z_756d_pctslope_63d_2d_v067_signal, bo_039_effort_vs_result_effort_vs_result_z_756d_slopez_21_126_2d_v068_signal, bo_039_effort_vs_result_effort_vs_result_z_756d_slopez_63_252_2d_v069_signal, bo_039_effort_vs_result_effort_vs_result_z_756d_cumslope_63d_2d_v070_signal, bo_039_effort_vs_result_effort_vs_result_z_756d_logmagslope_63d_2d_v071_signal, bo_039_effort_vs_result_effort_vs_result_z_756d_slope_rank_gap_2d_v072_signal, bo_039_effort_vs_result_effort_vs_result_z_756d_slope_504d_2d_v073_signal, bo_039_effort_vs_result_effort_vs_result_z_756d_sm126_slope63_2d_v074_signal, bo_039_effort_vs_result_effort_vs_result_z_756d_slopez_126_504_2d_v075_signal, bo_039_effort_vs_result_effort_vs_result_distmax_756d_slope_21d_2d_v076_signal, bo_039_effort_vs_result_effort_vs_result_distmax_756d_slope_63d_2d_v077_signal, bo_039_effort_vs_result_effort_vs_result_distmax_756d_slope_126d_2d_v078_signal, bo_039_effort_vs_result_effort_vs_result_distmax_756d_slope_252d_2d_v079_signal, bo_039_effort_vs_result_effort_vs_result_distmax_756d_sm63_slope21_2d_v080_signal, bo_039_effort_vs_result_effort_vs_result_distmax_756d_sm252_slope63_2d_v081_signal, bo_039_effort_vs_result_effort_vs_result_distmax_756d_pctslope_63d_2d_v082_signal, bo_039_effort_vs_result_effort_vs_result_distmax_756d_slopez_21_126_2d_v083_signal, bo_039_effort_vs_result_effort_vs_result_distmax_756d_slopez_63_252_2d_v084_signal, bo_039_effort_vs_result_effort_vs_result_distmax_756d_cumslope_63d_2d_v085_signal, bo_039_effort_vs_result_effort_vs_result_distmax_756d_logmagslope_63d_2d_v086_signal, bo_039_effort_vs_result_effort_vs_result_distmax_756d_slope_rank_gap_2d_v087_signal, bo_039_effort_vs_result_effort_vs_result_distmax_756d_slope_504d_2d_v088_signal, bo_039_effort_vs_result_effort_vs_result_distmax_756d_sm126_slope63_2d_v089_signal, bo_039_effort_vs_result_effort_vs_result_distmax_756d_slopez_126_504_2d_v090_signal, bo_039_effort_vs_result_effort_vs_result_distmin_756d_slope_21d_2d_v091_signal, bo_039_effort_vs_result_effort_vs_result_distmin_756d_slope_63d_2d_v092_signal, bo_039_effort_vs_result_effort_vs_result_distmin_756d_slope_126d_2d_v093_signal, bo_039_effort_vs_result_effort_vs_result_distmin_756d_slope_252d_2d_v094_signal, bo_039_effort_vs_result_effort_vs_result_distmin_756d_sm63_slope21_2d_v095_signal, bo_039_effort_vs_result_effort_vs_result_distmin_756d_sm252_slope63_2d_v096_signal, bo_039_effort_vs_result_effort_vs_result_distmin_756d_pctslope_63d_2d_v097_signal, bo_039_effort_vs_result_effort_vs_result_distmin_756d_slopez_21_126_2d_v098_signal, bo_039_effort_vs_result_effort_vs_result_distmin_756d_slopez_63_252_2d_v099_signal, bo_039_effort_vs_result_effort_vs_result_distmin_756d_cumslope_63d_2d_v100_signal, bo_039_effort_vs_result_effort_vs_result_distmin_756d_logmagslope_63d_2d_v101_signal, bo_039_effort_vs_result_effort_vs_result_distmin_756d_slope_rank_gap_2d_v102_signal, bo_039_effort_vs_result_effort_vs_result_distmin_756d_slope_504d_2d_v103_signal, bo_039_effort_vs_result_effort_vs_result_distmin_756d_sm126_slope63_2d_v104_signal, bo_039_effort_vs_result_effort_vs_result_distmin_756d_slopez_126_504_2d_v105_signal, bo_039_effort_vs_result_effort_vs_result_distmed_756d_slope_21d_2d_v106_signal, bo_039_effort_vs_result_effort_vs_result_distmed_756d_slope_63d_2d_v107_signal, bo_039_effort_vs_result_effort_vs_result_distmed_756d_slope_126d_2d_v108_signal, bo_039_effort_vs_result_effort_vs_result_distmed_756d_slope_252d_2d_v109_signal, bo_039_effort_vs_result_effort_vs_result_distmed_756d_sm63_slope21_2d_v110_signal, bo_039_effort_vs_result_effort_vs_result_distmed_756d_sm252_slope63_2d_v111_signal, bo_039_effort_vs_result_effort_vs_result_distmed_756d_pctslope_63d_2d_v112_signal, bo_039_effort_vs_result_effort_vs_result_distmed_756d_slopez_21_126_2d_v113_signal, bo_039_effort_vs_result_effort_vs_result_distmed_756d_slopez_63_252_2d_v114_signal, bo_039_effort_vs_result_effort_vs_result_distmed_756d_cumslope_63d_2d_v115_signal, bo_039_effort_vs_result_effort_vs_result_distmed_756d_logmagslope_63d_2d_v116_signal, bo_039_effort_vs_result_effort_vs_result_distmed_756d_slope_rank_gap_2d_v117_signal, bo_039_effort_vs_result_effort_vs_result_distmed_756d_slope_504d_2d_v118_signal, bo_039_effort_vs_result_effort_vs_result_distmed_756d_sm126_slope63_2d_v119_signal, bo_039_effort_vs_result_effort_vs_result_distmed_756d_slopez_126_504_2d_v120_signal, bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_slope_21d_2d_v121_signal, bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_slope_63d_2d_v122_signal, bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_slope_126d_2d_v123_signal, bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_slope_252d_2d_v124_signal, bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_sm63_slope21_2d_v125_signal, bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_sm252_slope63_2d_v126_signal, bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_pctslope_63d_2d_v127_signal, bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_slopez_21_126_2d_v128_signal, bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_slopez_63_252_2d_v129_signal, bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_cumslope_63d_2d_v130_signal, bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_logmagslope_63d_2d_v131_signal, bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_slope_rank_gap_2d_v132_signal, bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_slope_504d_2d_v133_signal, bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_sm126_slope63_2d_v134_signal, bo_039_effort_vs_result_effort_vs_result_upper_gap_200d_slopez_126_504_2d_v135_signal, bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_slope_21d_2d_v136_signal, bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_slope_63d_2d_v137_signal, bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_slope_126d_2d_v138_signal, bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_slope_252d_2d_v139_signal, bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_sm63_slope21_2d_v140_signal, bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_sm252_slope63_2d_v141_signal, bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_pctslope_63d_2d_v142_signal, bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_slopez_21_126_2d_v143_signal, bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_slopez_63_252_2d_v144_signal, bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_cumslope_63d_2d_v145_signal, bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_logmagslope_63d_2d_v146_signal, bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_slope_rank_gap_2d_v147_signal, bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_slope_504d_2d_v148_signal, bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_sm126_slope63_2d_v149_signal, bo_039_effort_vs_result_effort_vs_result_lower_gap_200d_slopez_126_504_2d_v150_signal]}
BREAKOUTS_REGISTRY_2ND_001_150 = REGISTRY

if __name__ == "__main__":
    print(f"registered {len(REGISTRY)} breakout feature functions")
