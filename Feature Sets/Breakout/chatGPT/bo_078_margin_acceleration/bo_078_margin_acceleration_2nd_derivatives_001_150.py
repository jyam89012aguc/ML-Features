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


# 21d slope for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_slope_21d_2d_v001_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_slope_63d_2d_v002_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_slope_126d_2d_v003_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_slope_252d_2d_v004_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_sm63_slope21_2d_v005_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_sm252_slope63_2d_v006_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_pctslope_63d_2d_v007_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_slopez_21_126_2d_v008_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_slopez_63_252_2d_v009_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_cumslope_63d_2d_v010_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_logmagslope_63d_2d_v011_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_slope_rank_gap_2d_v012_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_slope_504d_2d_v013_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_sm126_slope63_2d_v014_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for margin_acceleration
def bo_078_margin_acceleration_margin_acceleration_slopez_126_504_2d_v015_signal(opinc, revenue):
    base = _margin(opinc, revenue).diff(252).diff(252)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_slope_21d_2d_v016_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_slope_63d_2d_v017_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_slope_126d_2d_v018_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_slope_252d_2d_v019_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_sm63_slope21_2d_v020_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_sm252_slope63_2d_v021_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_pctslope_63d_2d_v022_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_slopez_21_126_2d_v023_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_slopez_63_252_2d_v024_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_cumslope_63d_2d_v025_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_logmagslope_63d_2d_v026_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_slope_rank_gap_2d_v027_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_slope_504d_2d_v028_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_sm126_slope63_2d_v029_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for margin_acceleration_mean_55d
def bo_078_margin_acceleration_margin_acceleration_mean_55d_slopez_126_504_2d_v030_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 55)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_slope_21d_2d_v031_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_slope_63d_2d_v032_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_slope_126d_2d_v033_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_slope_252d_2d_v034_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_sm63_slope21_2d_v035_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_sm252_slope63_2d_v036_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_pctslope_63d_2d_v037_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_slopez_21_126_2d_v038_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_slopez_63_252_2d_v039_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_cumslope_63d_2d_v040_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_logmagslope_63d_2d_v041_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_slope_rank_gap_2d_v042_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_slope_504d_2d_v043_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_sm126_slope63_2d_v044_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for margin_acceleration_mean_150d
def bo_078_margin_acceleration_margin_acceleration_mean_150d_slopez_126_504_2d_v045_signal(opinc, revenue):
    base = _mean(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_slope_21d_2d_v046_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_slope_63d_2d_v047_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_slope_126d_2d_v048_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_slope_252d_2d_v049_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_sm63_slope21_2d_v050_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_sm252_slope63_2d_v051_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_pctslope_63d_2d_v052_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_slopez_21_126_2d_v053_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_slopez_63_252_2d_v054_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_cumslope_63d_2d_v055_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_logmagslope_63d_2d_v056_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_slope_rank_gap_2d_v057_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_slope_504d_2d_v058_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_sm126_slope63_2d_v059_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for margin_acceleration_z_150d
def bo_078_margin_acceleration_margin_acceleration_z_150d_slopez_126_504_2d_v060_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 150)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_slope_21d_2d_v061_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_slope_63d_2d_v062_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_slope_126d_2d_v063_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_slope_252d_2d_v064_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_sm63_slope21_2d_v065_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_sm252_slope63_2d_v066_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_pctslope_63d_2d_v067_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_slopez_21_126_2d_v068_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_slopez_63_252_2d_v069_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_cumslope_63d_2d_v070_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_logmagslope_63d_2d_v071_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_slope_rank_gap_2d_v072_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 126d smoothed 63d slope for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_sm126_slope63_2d_v074_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for margin_acceleration_z_504d
def bo_078_margin_acceleration_margin_acceleration_z_504d_slopez_126_504_2d_v075_signal(opinc, revenue):
    base = _z(_margin(opinc, revenue).diff(252).diff(252), 504)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_slope_21d_2d_v091_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_slope_63d_2d_v092_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_slope_126d_2d_v093_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_slope_252d_2d_v094_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_sm63_slope21_2d_v095_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_sm252_slope63_2d_v096_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_pctslope_63d_2d_v097_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_slopez_21_126_2d_v098_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_slopez_63_252_2d_v099_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_cumslope_63d_2d_v100_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_logmagslope_63d_2d_v101_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_slope_rank_gap_2d_v102_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 126d smoothed 63d slope for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_sm126_slope63_2d_v104_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for margin_acceleration_distmin_504d
def bo_078_margin_acceleration_margin_acceleration_distmin_504d_slopez_126_504_2d_v105_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).min().abs())
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_slope_21d_2d_v106_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_slope_63d_2d_v107_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_slope_126d_2d_v108_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_slope_252d_2d_v109_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_sm63_slope21_2d_v110_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_sm252_slope63_2d_v111_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_pctslope_63d_2d_v112_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_slopez_21_126_2d_v113_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_slopez_63_252_2d_v114_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_cumslope_63d_2d_v115_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_logmagslope_63d_2d_v116_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_slope_rank_gap_2d_v117_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 126d smoothed 63d slope for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_sm126_slope63_2d_v119_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for margin_acceleration_distmed_504d
def bo_078_margin_acceleration_margin_acceleration_distmed_504d_slopez_126_504_2d_v120_signal(opinc, revenue):
    base = _safe_div((_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median(), (_margin(opinc, revenue).diff(252).diff(252)).rolling(504, min_periods=max(2, 504//2)).median().abs())
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_slope_21d_2d_v121_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_slope_63d_2d_v122_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_slope_126d_2d_v123_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_slope_252d_2d_v124_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_sm63_slope21_2d_v125_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_sm252_slope63_2d_v126_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_pctslope_63d_2d_v127_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_slopez_21_126_2d_v128_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_slopez_63_252_2d_v129_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_cumslope_63d_2d_v130_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_logmagslope_63d_2d_v131_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_slope_rank_gap_2d_v132_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_slope_504d_2d_v133_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_sm126_slope63_2d_v134_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for margin_acceleration_upper_gap_150d
def bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_slopez_126_504_2d_v135_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.75)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for margin_acceleration_lower_gap_150d
def bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_slope_21d_2d_v136_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for margin_acceleration_lower_gap_150d
def bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_slope_63d_2d_v137_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for margin_acceleration_lower_gap_150d
def bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_slope_126d_2d_v138_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for margin_acceleration_lower_gap_150d
def bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_slope_252d_2d_v139_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for margin_acceleration_lower_gap_150d
def bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_sm63_slope21_2d_v140_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for margin_acceleration_lower_gap_150d
def bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_sm252_slope63_2d_v141_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for margin_acceleration_lower_gap_150d
def bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_pctslope_63d_2d_v142_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for margin_acceleration_lower_gap_150d
def bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_slopez_21_126_2d_v143_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for margin_acceleration_lower_gap_150d
def bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_slopez_63_252_2d_v144_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for margin_acceleration_lower_gap_150d
def bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_cumslope_63d_2d_v145_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for margin_acceleration_lower_gap_150d
def bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_logmagslope_63d_2d_v146_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for margin_acceleration_lower_gap_150d
def bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_slope_rank_gap_2d_v147_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for margin_acceleration_lower_gap_150d
def bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_slope_504d_2d_v148_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for margin_acceleration_lower_gap_150d
def bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_sm126_slope63_2d_v149_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for margin_acceleration_lower_gap_150d
def bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_slopez_126_504_2d_v150_signal(opinc, revenue):
    base = (_margin(opinc, revenue).diff(252).diff(252)) - (_margin(opinc, revenue).diff(252).diff(252)).rolling(150, min_periods=max(2, 150//2)).quantile(0.25)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

REGISTRY = {fn.__name__: {"inputs": ['opinc', 'revenue'], "func": fn} for fn in [bo_078_margin_acceleration_margin_acceleration_slope_21d_2d_v001_signal, bo_078_margin_acceleration_margin_acceleration_slope_63d_2d_v002_signal, bo_078_margin_acceleration_margin_acceleration_slope_126d_2d_v003_signal, bo_078_margin_acceleration_margin_acceleration_slope_252d_2d_v004_signal, bo_078_margin_acceleration_margin_acceleration_sm63_slope21_2d_v005_signal, bo_078_margin_acceleration_margin_acceleration_sm252_slope63_2d_v006_signal, bo_078_margin_acceleration_margin_acceleration_pctslope_63d_2d_v007_signal, bo_078_margin_acceleration_margin_acceleration_slopez_21_126_2d_v008_signal, bo_078_margin_acceleration_margin_acceleration_slopez_63_252_2d_v009_signal, bo_078_margin_acceleration_margin_acceleration_cumslope_63d_2d_v010_signal, bo_078_margin_acceleration_margin_acceleration_logmagslope_63d_2d_v011_signal, bo_078_margin_acceleration_margin_acceleration_slope_rank_gap_2d_v012_signal, bo_078_margin_acceleration_margin_acceleration_slope_504d_2d_v013_signal, bo_078_margin_acceleration_margin_acceleration_sm126_slope63_2d_v014_signal, bo_078_margin_acceleration_margin_acceleration_slopez_126_504_2d_v015_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_slope_21d_2d_v016_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_slope_63d_2d_v017_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_slope_126d_2d_v018_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_slope_252d_2d_v019_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_sm63_slope21_2d_v020_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_sm252_slope63_2d_v021_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_pctslope_63d_2d_v022_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_slopez_21_126_2d_v023_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_slopez_63_252_2d_v024_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_cumslope_63d_2d_v025_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_logmagslope_63d_2d_v026_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_slope_rank_gap_2d_v027_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_slope_504d_2d_v028_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_sm126_slope63_2d_v029_signal, bo_078_margin_acceleration_margin_acceleration_mean_55d_slopez_126_504_2d_v030_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_slope_21d_2d_v031_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_slope_63d_2d_v032_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_slope_126d_2d_v033_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_slope_252d_2d_v034_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_sm63_slope21_2d_v035_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_sm252_slope63_2d_v036_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_pctslope_63d_2d_v037_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_slopez_21_126_2d_v038_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_slopez_63_252_2d_v039_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_cumslope_63d_2d_v040_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_logmagslope_63d_2d_v041_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_slope_rank_gap_2d_v042_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_slope_504d_2d_v043_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_sm126_slope63_2d_v044_signal, bo_078_margin_acceleration_margin_acceleration_mean_150d_slopez_126_504_2d_v045_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_slope_21d_2d_v046_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_slope_63d_2d_v047_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_slope_126d_2d_v048_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_slope_252d_2d_v049_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_sm63_slope21_2d_v050_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_sm252_slope63_2d_v051_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_pctslope_63d_2d_v052_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_slopez_21_126_2d_v053_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_slopez_63_252_2d_v054_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_cumslope_63d_2d_v055_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_logmagslope_63d_2d_v056_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_slope_rank_gap_2d_v057_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_slope_504d_2d_v058_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_sm126_slope63_2d_v059_signal, bo_078_margin_acceleration_margin_acceleration_z_150d_slopez_126_504_2d_v060_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_slope_21d_2d_v061_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_slope_63d_2d_v062_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_slope_126d_2d_v063_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_slope_252d_2d_v064_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_sm63_slope21_2d_v065_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_sm252_slope63_2d_v066_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_pctslope_63d_2d_v067_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_slopez_21_126_2d_v068_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_slopez_63_252_2d_v069_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_cumslope_63d_2d_v070_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_logmagslope_63d_2d_v071_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_slope_rank_gap_2d_v072_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_sm126_slope63_2d_v074_signal, bo_078_margin_acceleration_margin_acceleration_z_504d_slopez_126_504_2d_v075_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_slope_21d_2d_v091_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_slope_63d_2d_v092_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_slope_126d_2d_v093_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_slope_252d_2d_v094_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_sm63_slope21_2d_v095_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_sm252_slope63_2d_v096_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_pctslope_63d_2d_v097_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_slopez_21_126_2d_v098_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_slopez_63_252_2d_v099_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_cumslope_63d_2d_v100_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_logmagslope_63d_2d_v101_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_slope_rank_gap_2d_v102_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_sm126_slope63_2d_v104_signal, bo_078_margin_acceleration_margin_acceleration_distmin_504d_slopez_126_504_2d_v105_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_slope_21d_2d_v106_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_slope_63d_2d_v107_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_slope_126d_2d_v108_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_slope_252d_2d_v109_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_sm63_slope21_2d_v110_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_sm252_slope63_2d_v111_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_pctslope_63d_2d_v112_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_slopez_21_126_2d_v113_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_slopez_63_252_2d_v114_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_cumslope_63d_2d_v115_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_logmagslope_63d_2d_v116_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_slope_rank_gap_2d_v117_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_sm126_slope63_2d_v119_signal, bo_078_margin_acceleration_margin_acceleration_distmed_504d_slopez_126_504_2d_v120_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_slope_21d_2d_v121_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_slope_63d_2d_v122_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_slope_126d_2d_v123_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_slope_252d_2d_v124_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_sm63_slope21_2d_v125_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_sm252_slope63_2d_v126_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_pctslope_63d_2d_v127_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_slopez_21_126_2d_v128_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_slopez_63_252_2d_v129_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_cumslope_63d_2d_v130_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_logmagslope_63d_2d_v131_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_slope_rank_gap_2d_v132_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_slope_504d_2d_v133_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_sm126_slope63_2d_v134_signal, bo_078_margin_acceleration_margin_acceleration_upper_gap_150d_slopez_126_504_2d_v135_signal, bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_slope_21d_2d_v136_signal, bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_slope_63d_2d_v137_signal, bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_slope_126d_2d_v138_signal, bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_slope_252d_2d_v139_signal, bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_sm63_slope21_2d_v140_signal, bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_sm252_slope63_2d_v141_signal, bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_pctslope_63d_2d_v142_signal, bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_slopez_21_126_2d_v143_signal, bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_slopez_63_252_2d_v144_signal, bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_cumslope_63d_2d_v145_signal, bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_logmagslope_63d_2d_v146_signal, bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_slope_rank_gap_2d_v147_signal, bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_slope_504d_2d_v148_signal, bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_sm126_slope63_2d_v149_signal, bo_078_margin_acceleration_margin_acceleration_lower_gap_150d_slopez_126_504_2d_v150_signal]}
BREAKOUTS_REGISTRY_2ND_001_150 = REGISTRY

if __name__ == "__main__":
    print(f"registered {len(REGISTRY)} breakout feature functions")
