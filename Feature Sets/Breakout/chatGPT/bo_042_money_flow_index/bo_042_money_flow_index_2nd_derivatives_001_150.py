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


# 21d slope for money_flow_index
def bo_042_money_flow_index_money_flow_index_slope_21d_2d_v001_signal(high, low, closeadj, volume):
    base = _mfi(high, low, closeadj, volume, 14)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for money_flow_index
def bo_042_money_flow_index_money_flow_index_slope_63d_2d_v002_signal(high, low, closeadj, volume):
    base = _mfi(high, low, closeadj, volume, 14)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for money_flow_index
def bo_042_money_flow_index_money_flow_index_slope_126d_2d_v003_signal(high, low, closeadj, volume):
    base = _mfi(high, low, closeadj, volume, 14)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for money_flow_index
def bo_042_money_flow_index_money_flow_index_slope_252d_2d_v004_signal(high, low, closeadj, volume):
    base = _mfi(high, low, closeadj, volume, 14)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for money_flow_index
def bo_042_money_flow_index_money_flow_index_sm63_slope21_2d_v005_signal(high, low, closeadj, volume):
    base = _mfi(high, low, closeadj, volume, 14)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for money_flow_index
def bo_042_money_flow_index_money_flow_index_sm252_slope63_2d_v006_signal(high, low, closeadj, volume):
    base = _mfi(high, low, closeadj, volume, 14)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 21d slope z-score for money_flow_index
def bo_042_money_flow_index_money_flow_index_slopez_21_126_2d_v008_signal(high, low, closeadj, volume):
    base = _mfi(high, low, closeadj, volume, 14)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d cumulative slope for money_flow_index
def bo_042_money_flow_index_money_flow_index_cumslope_63d_2d_v010_signal(high, low, closeadj, volume):
    base = _mfi(high, low, closeadj, volume, 14)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for money_flow_index
def bo_042_money_flow_index_money_flow_index_logmagslope_63d_2d_v011_signal(high, low, closeadj, volume):
    base = _mfi(high, low, closeadj, volume, 14)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# 504d slope for money_flow_index
def bo_042_money_flow_index_money_flow_index_slope_504d_2d_v013_signal(high, low, closeadj, volume):
    base = _mfi(high, low, closeadj, volume, 14)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for money_flow_index
def bo_042_money_flow_index_money_flow_index_sm126_slope63_2d_v014_signal(high, low, closeadj, volume):
    base = _mfi(high, low, closeadj, volume, 14)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 21d slope for money_flow_index_mean_42d
def bo_042_money_flow_index_money_flow_index_mean_42d_slope_21d_2d_v016_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 42)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for money_flow_index_mean_42d
def bo_042_money_flow_index_money_flow_index_mean_42d_slope_63d_2d_v017_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 42)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for money_flow_index_mean_42d
def bo_042_money_flow_index_money_flow_index_mean_42d_slope_126d_2d_v018_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 42)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for money_flow_index_mean_42d
def bo_042_money_flow_index_money_flow_index_mean_42d_slope_252d_2d_v019_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 42)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for money_flow_index_mean_42d
def bo_042_money_flow_index_money_flow_index_mean_42d_sm63_slope21_2d_v020_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 42)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for money_flow_index_mean_42d
def bo_042_money_flow_index_money_flow_index_mean_42d_sm252_slope63_2d_v021_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 42)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for money_flow_index_mean_42d
def bo_042_money_flow_index_money_flow_index_mean_42d_pctslope_63d_2d_v022_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 42)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for money_flow_index_mean_42d
def bo_042_money_flow_index_money_flow_index_mean_42d_slopez_21_126_2d_v023_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 42)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d cumulative slope for money_flow_index_mean_42d
def bo_042_money_flow_index_money_flow_index_mean_42d_cumslope_63d_2d_v025_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 42)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for money_flow_index_mean_42d
def bo_042_money_flow_index_money_flow_index_mean_42d_logmagslope_63d_2d_v026_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 42)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# 504d slope for money_flow_index_mean_42d
def bo_042_money_flow_index_money_flow_index_mean_42d_slope_504d_2d_v028_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 42)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for money_flow_index_mean_42d
def bo_042_money_flow_index_money_flow_index_mean_42d_sm126_slope63_2d_v029_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 42)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 21d slope for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_slope_21d_2d_v031_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _slope(base, 21)
    return _clean(result)

# 126d slope for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_slope_126d_2d_v033_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_slope_252d_2d_v034_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_sm63_slope21_2d_v035_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_sm252_slope63_2d_v036_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_pctslope_63d_2d_v037_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_slopez_21_126_2d_v038_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d cumulative slope for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_cumslope_63d_2d_v040_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_logmagslope_63d_2d_v041_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# 504d slope for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_slope_504d_2d_v043_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_sm126_slope63_2d_v044_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 21d slope for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_slope_21d_2d_v046_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_slope_63d_2d_v047_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _slope(base, 63)
    return _clean(result)

# 63d smoothed 21d slope for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_sm63_slope21_2d_v050_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 63d pct slope for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_pctslope_63d_2d_v052_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_slopez_21_126_2d_v053_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d cumulative slope for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_cumslope_63d_2d_v055_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_logmagslope_63d_2d_v056_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# 126d smoothed 63d slope for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_sm126_slope63_2d_v059_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 21d slope for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_slope_21d_2d_v061_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_slope_63d_2d_v062_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = _slope(base, 63)
    return _clean(result)

# 63d smoothed 21d slope for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_sm63_slope21_2d_v065_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 63d pct slope for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_pctslope_63d_2d_v067_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = _slope_pct(base, 63)
    return _clean(result)

# 63d cumulative slope for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_cumslope_63d_2d_v070_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_logmagslope_63d_2d_v071_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# 126d smoothed 63d slope for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_sm126_slope63_2d_v074_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 21d slope for money_flow_index_distmax_378d
def bo_042_money_flow_index_money_flow_index_distmax_378d_slope_21d_2d_v076_signal(high, low, closeadj, volume):
    base = _safe_div((_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(378, min_periods=max(2, 378//2)).max(), (_mfi(high, low, closeadj, volume, 14)).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for money_flow_index_distmax_378d
def bo_042_money_flow_index_money_flow_index_distmax_378d_slope_63d_2d_v077_signal(high, low, closeadj, volume):
    base = _safe_div((_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(378, min_periods=max(2, 378//2)).max(), (_mfi(high, low, closeadj, volume, 14)).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _slope(base, 63)
    return _clean(result)

# 63d smoothed 21d slope for money_flow_index_distmax_378d
def bo_042_money_flow_index_money_flow_index_distmax_378d_sm63_slope21_2d_v080_signal(high, low, closeadj, volume):
    base = _safe_div((_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(378, min_periods=max(2, 378//2)).max(), (_mfi(high, low, closeadj, volume, 14)).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 63d pct slope for money_flow_index_distmax_378d
def bo_042_money_flow_index_money_flow_index_distmax_378d_pctslope_63d_2d_v082_signal(high, low, closeadj, volume):
    base = _safe_div((_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(378, min_periods=max(2, 378//2)).max(), (_mfi(high, low, closeadj, volume, 14)).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _slope_pct(base, 63)
    return _clean(result)

# 63d cumulative slope for money_flow_index_distmax_378d
def bo_042_money_flow_index_money_flow_index_distmax_378d_cumslope_63d_2d_v085_signal(high, low, closeadj, volume):
    base = _safe_div((_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(378, min_periods=max(2, 378//2)).max(), (_mfi(high, low, closeadj, volume, 14)).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for money_flow_index_distmax_378d
def bo_042_money_flow_index_money_flow_index_distmax_378d_logmagslope_63d_2d_v086_signal(high, low, closeadj, volume):
    base = _safe_div((_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(378, min_periods=max(2, 378//2)).max(), (_mfi(high, low, closeadj, volume, 14)).rolling(378, min_periods=max(2, 378//2)).max().abs())
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# 126d smoothed 63d slope for money_flow_index_distmax_378d
def bo_042_money_flow_index_money_flow_index_distmax_378d_sm126_slope63_2d_v089_signal(high, low, closeadj, volume):
    base = _safe_div((_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(378, min_periods=max(2, 378//2)).max(), (_mfi(high, low, closeadj, volume, 14)).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 21d slope for money_flow_index_upper_gap_126d
def bo_042_money_flow_index_money_flow_index_upper_gap_126d_slope_21d_2d_v121_signal(high, low, closeadj, volume):
    base = (_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for money_flow_index_upper_gap_126d
def bo_042_money_flow_index_money_flow_index_upper_gap_126d_slope_63d_2d_v122_signal(high, low, closeadj, volume):
    base = (_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _slope(base, 63)
    return _clean(result)

# 63d smoothed 21d slope for money_flow_index_upper_gap_126d
def bo_042_money_flow_index_money_flow_index_upper_gap_126d_sm63_slope21_2d_v125_signal(high, low, closeadj, volume):
    base = (_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 21d slope z-score for money_flow_index_upper_gap_126d
def bo_042_money_flow_index_money_flow_index_upper_gap_126d_slopez_21_126_2d_v128_signal(high, low, closeadj, volume):
    base = (_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d cumulative slope for money_flow_index_upper_gap_126d
def bo_042_money_flow_index_money_flow_index_upper_gap_126d_cumslope_63d_2d_v130_signal(high, low, closeadj, volume):
    base = (_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for money_flow_index_upper_gap_126d
def bo_042_money_flow_index_money_flow_index_upper_gap_126d_logmagslope_63d_2d_v131_signal(high, low, closeadj, volume):
    base = (_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# 126d smoothed 63d slope for money_flow_index_upper_gap_126d
def bo_042_money_flow_index_money_flow_index_upper_gap_126d_sm126_slope63_2d_v134_signal(high, low, closeadj, volume):
    base = (_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 21d slope for money_flow_index_lower_gap_126d
def bo_042_money_flow_index_money_flow_index_lower_gap_126d_slope_21d_2d_v136_signal(high, low, closeadj, volume):
    base = (_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(126, min_periods=max(2, 126//2)).quantile(0.25)
    result = _slope(base, 21)
    return _clean(result)

# 63d smoothed 21d slope for money_flow_index_lower_gap_126d
def bo_042_money_flow_index_money_flow_index_lower_gap_126d_sm63_slope21_2d_v140_signal(high, low, closeadj, volume):
    base = (_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(126, min_periods=max(2, 126//2)).quantile(0.25)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

REGISTRY = {fn.__name__: {"inputs": ['high', 'low', 'closeadj', 'volume'], "func": fn} for fn in [bo_042_money_flow_index_money_flow_index_slope_21d_2d_v001_signal, bo_042_money_flow_index_money_flow_index_slope_63d_2d_v002_signal, bo_042_money_flow_index_money_flow_index_slope_126d_2d_v003_signal, bo_042_money_flow_index_money_flow_index_slope_252d_2d_v004_signal, bo_042_money_flow_index_money_flow_index_sm63_slope21_2d_v005_signal, bo_042_money_flow_index_money_flow_index_sm252_slope63_2d_v006_signal, bo_042_money_flow_index_money_flow_index_slopez_21_126_2d_v008_signal, bo_042_money_flow_index_money_flow_index_cumslope_63d_2d_v010_signal, bo_042_money_flow_index_money_flow_index_logmagslope_63d_2d_v011_signal, bo_042_money_flow_index_money_flow_index_slope_504d_2d_v013_signal, bo_042_money_flow_index_money_flow_index_sm126_slope63_2d_v014_signal, bo_042_money_flow_index_money_flow_index_mean_42d_slope_21d_2d_v016_signal, bo_042_money_flow_index_money_flow_index_mean_42d_slope_63d_2d_v017_signal, bo_042_money_flow_index_money_flow_index_mean_42d_slope_126d_2d_v018_signal, bo_042_money_flow_index_money_flow_index_mean_42d_slope_252d_2d_v019_signal, bo_042_money_flow_index_money_flow_index_mean_42d_sm63_slope21_2d_v020_signal, bo_042_money_flow_index_money_flow_index_mean_42d_sm252_slope63_2d_v021_signal, bo_042_money_flow_index_money_flow_index_mean_42d_pctslope_63d_2d_v022_signal, bo_042_money_flow_index_money_flow_index_mean_42d_slopez_21_126_2d_v023_signal, bo_042_money_flow_index_money_flow_index_mean_42d_cumslope_63d_2d_v025_signal, bo_042_money_flow_index_money_flow_index_mean_42d_logmagslope_63d_2d_v026_signal, bo_042_money_flow_index_money_flow_index_mean_42d_slope_504d_2d_v028_signal, bo_042_money_flow_index_money_flow_index_mean_42d_sm126_slope63_2d_v029_signal, bo_042_money_flow_index_money_flow_index_mean_126d_slope_21d_2d_v031_signal, bo_042_money_flow_index_money_flow_index_mean_126d_slope_126d_2d_v033_signal, bo_042_money_flow_index_money_flow_index_mean_126d_slope_252d_2d_v034_signal, bo_042_money_flow_index_money_flow_index_mean_126d_sm63_slope21_2d_v035_signal, bo_042_money_flow_index_money_flow_index_mean_126d_sm252_slope63_2d_v036_signal, bo_042_money_flow_index_money_flow_index_mean_126d_pctslope_63d_2d_v037_signal, bo_042_money_flow_index_money_flow_index_mean_126d_slopez_21_126_2d_v038_signal, bo_042_money_flow_index_money_flow_index_mean_126d_cumslope_63d_2d_v040_signal, bo_042_money_flow_index_money_flow_index_mean_126d_logmagslope_63d_2d_v041_signal, bo_042_money_flow_index_money_flow_index_mean_126d_slope_504d_2d_v043_signal, bo_042_money_flow_index_money_flow_index_mean_126d_sm126_slope63_2d_v044_signal, bo_042_money_flow_index_money_flow_index_z_126d_slope_21d_2d_v046_signal, bo_042_money_flow_index_money_flow_index_z_126d_slope_63d_2d_v047_signal, bo_042_money_flow_index_money_flow_index_z_126d_sm63_slope21_2d_v050_signal, bo_042_money_flow_index_money_flow_index_z_126d_pctslope_63d_2d_v052_signal, bo_042_money_flow_index_money_flow_index_z_126d_slopez_21_126_2d_v053_signal, bo_042_money_flow_index_money_flow_index_z_126d_cumslope_63d_2d_v055_signal, bo_042_money_flow_index_money_flow_index_z_126d_logmagslope_63d_2d_v056_signal, bo_042_money_flow_index_money_flow_index_z_126d_sm126_slope63_2d_v059_signal, bo_042_money_flow_index_money_flow_index_z_378d_slope_21d_2d_v061_signal, bo_042_money_flow_index_money_flow_index_z_378d_slope_63d_2d_v062_signal, bo_042_money_flow_index_money_flow_index_z_378d_sm63_slope21_2d_v065_signal, bo_042_money_flow_index_money_flow_index_z_378d_pctslope_63d_2d_v067_signal, bo_042_money_flow_index_money_flow_index_z_378d_cumslope_63d_2d_v070_signal, bo_042_money_flow_index_money_flow_index_z_378d_logmagslope_63d_2d_v071_signal, bo_042_money_flow_index_money_flow_index_z_378d_sm126_slope63_2d_v074_signal, bo_042_money_flow_index_money_flow_index_distmax_378d_slope_21d_2d_v076_signal, bo_042_money_flow_index_money_flow_index_distmax_378d_slope_63d_2d_v077_signal, bo_042_money_flow_index_money_flow_index_distmax_378d_sm63_slope21_2d_v080_signal, bo_042_money_flow_index_money_flow_index_distmax_378d_pctslope_63d_2d_v082_signal, bo_042_money_flow_index_money_flow_index_distmax_378d_cumslope_63d_2d_v085_signal, bo_042_money_flow_index_money_flow_index_distmax_378d_logmagslope_63d_2d_v086_signal, bo_042_money_flow_index_money_flow_index_distmax_378d_sm126_slope63_2d_v089_signal, bo_042_money_flow_index_money_flow_index_upper_gap_126d_slope_21d_2d_v121_signal, bo_042_money_flow_index_money_flow_index_upper_gap_126d_slope_63d_2d_v122_signal, bo_042_money_flow_index_money_flow_index_upper_gap_126d_sm63_slope21_2d_v125_signal, bo_042_money_flow_index_money_flow_index_upper_gap_126d_slopez_21_126_2d_v128_signal, bo_042_money_flow_index_money_flow_index_upper_gap_126d_cumslope_63d_2d_v130_signal, bo_042_money_flow_index_money_flow_index_upper_gap_126d_logmagslope_63d_2d_v131_signal, bo_042_money_flow_index_money_flow_index_upper_gap_126d_sm126_slope63_2d_v134_signal, bo_042_money_flow_index_money_flow_index_lower_gap_126d_slope_21d_2d_v136_signal, bo_042_money_flow_index_money_flow_index_lower_gap_126d_sm63_slope21_2d_v140_signal]}
BREAKOUTS_REGISTRY_2ND_001_150 = REGISTRY

if __name__ == "__main__":
    print(f"registered {len(REGISTRY)} breakout feature functions")
