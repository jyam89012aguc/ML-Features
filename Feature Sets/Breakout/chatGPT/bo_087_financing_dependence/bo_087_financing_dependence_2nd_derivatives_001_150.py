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


# 21d slope for financing_dependence
def bo_087_financing_dependence_financing_dependence_slope_21d_2d_v001_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for financing_dependence
def bo_087_financing_dependence_financing_dependence_slope_63d_2d_v002_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for financing_dependence
def bo_087_financing_dependence_financing_dependence_slope_126d_2d_v003_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for financing_dependence
def bo_087_financing_dependence_financing_dependence_slope_252d_2d_v004_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for financing_dependence
def bo_087_financing_dependence_financing_dependence_sm63_slope21_2d_v005_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for financing_dependence
def bo_087_financing_dependence_financing_dependence_sm252_slope63_2d_v006_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for financing_dependence
def bo_087_financing_dependence_financing_dependence_pctslope_63d_2d_v007_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for financing_dependence
def bo_087_financing_dependence_financing_dependence_slopez_21_126_2d_v008_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for financing_dependence
def bo_087_financing_dependence_financing_dependence_slopez_63_252_2d_v009_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for financing_dependence
def bo_087_financing_dependence_financing_dependence_cumslope_63d_2d_v010_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for financing_dependence
def bo_087_financing_dependence_financing_dependence_logmagslope_63d_2d_v011_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for financing_dependence
def bo_087_financing_dependence_financing_dependence_slope_rank_gap_2d_v012_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for financing_dependence
def bo_087_financing_dependence_financing_dependence_slope_504d_2d_v013_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for financing_dependence
def bo_087_financing_dependence_financing_dependence_sm126_slope63_2d_v014_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for financing_dependence
def bo_087_financing_dependence_financing_dependence_slopez_126_504_2d_v015_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for financing_dependence_mean_42d
def bo_087_financing_dependence_financing_dependence_mean_42d_slope_21d_2d_v016_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 42)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for financing_dependence_mean_42d
def bo_087_financing_dependence_financing_dependence_mean_42d_slope_63d_2d_v017_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 42)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for financing_dependence_mean_42d
def bo_087_financing_dependence_financing_dependence_mean_42d_slope_126d_2d_v018_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 42)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for financing_dependence_mean_42d
def bo_087_financing_dependence_financing_dependence_mean_42d_slope_252d_2d_v019_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 42)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for financing_dependence_mean_42d
def bo_087_financing_dependence_financing_dependence_mean_42d_sm63_slope21_2d_v020_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 42)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for financing_dependence_mean_42d
def bo_087_financing_dependence_financing_dependence_mean_42d_sm252_slope63_2d_v021_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 42)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for financing_dependence_mean_42d
def bo_087_financing_dependence_financing_dependence_mean_42d_pctslope_63d_2d_v022_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 42)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for financing_dependence_mean_42d
def bo_087_financing_dependence_financing_dependence_mean_42d_slopez_21_126_2d_v023_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 42)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for financing_dependence_mean_42d
def bo_087_financing_dependence_financing_dependence_mean_42d_slopez_63_252_2d_v024_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 42)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for financing_dependence_mean_42d
def bo_087_financing_dependence_financing_dependence_mean_42d_cumslope_63d_2d_v025_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 42)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for financing_dependence_mean_42d
def bo_087_financing_dependence_financing_dependence_mean_42d_logmagslope_63d_2d_v026_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 42)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for financing_dependence_mean_42d
def bo_087_financing_dependence_financing_dependence_mean_42d_slope_rank_gap_2d_v027_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 42)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for financing_dependence_mean_42d
def bo_087_financing_dependence_financing_dependence_mean_42d_slope_504d_2d_v028_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 42)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for financing_dependence_mean_42d
def bo_087_financing_dependence_financing_dependence_mean_42d_sm126_slope63_2d_v029_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 42)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for financing_dependence_mean_42d
def bo_087_financing_dependence_financing_dependence_mean_42d_slopez_126_504_2d_v030_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 42)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for financing_dependence_mean_126d
def bo_087_financing_dependence_financing_dependence_mean_126d_slope_21d_2d_v031_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _slope(base, 21)
    return _clean(result)

# 126d slope for financing_dependence_mean_126d
def bo_087_financing_dependence_financing_dependence_mean_126d_slope_126d_2d_v033_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for financing_dependence_mean_126d
def bo_087_financing_dependence_financing_dependence_mean_126d_slope_252d_2d_v034_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for financing_dependence_mean_126d
def bo_087_financing_dependence_financing_dependence_mean_126d_sm63_slope21_2d_v035_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for financing_dependence_mean_126d
def bo_087_financing_dependence_financing_dependence_mean_126d_sm252_slope63_2d_v036_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for financing_dependence_mean_126d
def bo_087_financing_dependence_financing_dependence_mean_126d_pctslope_63d_2d_v037_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for financing_dependence_mean_126d
def bo_087_financing_dependence_financing_dependence_mean_126d_slopez_21_126_2d_v038_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for financing_dependence_mean_126d
def bo_087_financing_dependence_financing_dependence_mean_126d_slopez_63_252_2d_v039_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for financing_dependence_mean_126d
def bo_087_financing_dependence_financing_dependence_mean_126d_cumslope_63d_2d_v040_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for financing_dependence_mean_126d
def bo_087_financing_dependence_financing_dependence_mean_126d_logmagslope_63d_2d_v041_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for financing_dependence_mean_126d
def bo_087_financing_dependence_financing_dependence_mean_126d_slope_rank_gap_2d_v042_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for financing_dependence_mean_126d
def bo_087_financing_dependence_financing_dependence_mean_126d_slope_504d_2d_v043_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for financing_dependence_mean_126d
def bo_087_financing_dependence_financing_dependence_mean_126d_sm126_slope63_2d_v044_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for financing_dependence_mean_126d
def bo_087_financing_dependence_financing_dependence_mean_126d_slopez_126_504_2d_v045_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _mean(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for financing_dependence_z_126d
def bo_087_financing_dependence_financing_dependence_z_126d_slope_21d_2d_v046_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for financing_dependence_z_126d
def bo_087_financing_dependence_financing_dependence_z_126d_slope_63d_2d_v047_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for financing_dependence_z_126d
def bo_087_financing_dependence_financing_dependence_z_126d_slope_126d_2d_v048_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for financing_dependence_z_126d
def bo_087_financing_dependence_financing_dependence_z_126d_slope_252d_2d_v049_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for financing_dependence_z_126d
def bo_087_financing_dependence_financing_dependence_z_126d_sm63_slope21_2d_v050_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for financing_dependence_z_126d
def bo_087_financing_dependence_financing_dependence_z_126d_sm252_slope63_2d_v051_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for financing_dependence_z_126d
def bo_087_financing_dependence_financing_dependence_z_126d_pctslope_63d_2d_v052_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for financing_dependence_z_126d
def bo_087_financing_dependence_financing_dependence_z_126d_slopez_21_126_2d_v053_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for financing_dependence_z_126d
def bo_087_financing_dependence_financing_dependence_z_126d_slopez_63_252_2d_v054_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for financing_dependence_z_126d
def bo_087_financing_dependence_financing_dependence_z_126d_cumslope_63d_2d_v055_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for financing_dependence_z_126d
def bo_087_financing_dependence_financing_dependence_z_126d_logmagslope_63d_2d_v056_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for financing_dependence_z_126d
def bo_087_financing_dependence_financing_dependence_z_126d_slope_rank_gap_2d_v057_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for financing_dependence_z_126d
def bo_087_financing_dependence_financing_dependence_z_126d_slope_504d_2d_v058_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for financing_dependence_z_126d
def bo_087_financing_dependence_financing_dependence_z_126d_sm126_slope63_2d_v059_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for financing_dependence_z_126d
def bo_087_financing_dependence_financing_dependence_z_126d_slopez_126_504_2d_v060_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 126)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for financing_dependence_z_378d
def bo_087_financing_dependence_financing_dependence_z_378d_slope_21d_2d_v061_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 378)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for financing_dependence_z_378d
def bo_087_financing_dependence_financing_dependence_z_378d_slope_63d_2d_v062_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 378)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for financing_dependence_z_378d
def bo_087_financing_dependence_financing_dependence_z_378d_slope_126d_2d_v063_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 378)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for financing_dependence_z_378d
def bo_087_financing_dependence_financing_dependence_z_378d_slope_252d_2d_v064_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 378)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for financing_dependence_z_378d
def bo_087_financing_dependence_financing_dependence_z_378d_sm63_slope21_2d_v065_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 378)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for financing_dependence_z_378d
def bo_087_financing_dependence_financing_dependence_z_378d_sm252_slope63_2d_v066_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 378)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for financing_dependence_z_378d
def bo_087_financing_dependence_financing_dependence_z_378d_pctslope_63d_2d_v067_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 378)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for financing_dependence_z_378d
def bo_087_financing_dependence_financing_dependence_z_378d_slopez_21_126_2d_v068_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 378)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for financing_dependence_z_378d
def bo_087_financing_dependence_financing_dependence_z_378d_slopez_63_252_2d_v069_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 378)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for financing_dependence_z_378d
def bo_087_financing_dependence_financing_dependence_z_378d_cumslope_63d_2d_v070_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 378)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for financing_dependence_z_378d
def bo_087_financing_dependence_financing_dependence_z_378d_logmagslope_63d_2d_v071_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 378)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for financing_dependence_z_378d
def bo_087_financing_dependence_financing_dependence_z_378d_slope_rank_gap_2d_v072_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 378)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for financing_dependence_z_378d
def bo_087_financing_dependence_financing_dependence_z_378d_slope_504d_2d_v073_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 378)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for financing_dependence_z_378d
def bo_087_financing_dependence_financing_dependence_z_378d_sm126_slope63_2d_v074_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 378)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for financing_dependence_z_378d
def bo_087_financing_dependence_financing_dependence_z_378d_slopez_126_504_2d_v075_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _z(_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs()), 378)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for financing_dependence_distmax_378d
def bo_087_financing_dependence_financing_dependence_distmax_378d_slope_21d_2d_v076_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for financing_dependence_distmax_378d
def bo_087_financing_dependence_financing_dependence_distmax_378d_slope_63d_2d_v077_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for financing_dependence_distmax_378d
def bo_087_financing_dependence_financing_dependence_distmax_378d_slope_126d_2d_v078_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for financing_dependence_distmax_378d
def bo_087_financing_dependence_financing_dependence_distmax_378d_slope_252d_2d_v079_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for financing_dependence_distmax_378d
def bo_087_financing_dependence_financing_dependence_distmax_378d_sm63_slope21_2d_v080_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for financing_dependence_distmax_378d
def bo_087_financing_dependence_financing_dependence_distmax_378d_sm252_slope63_2d_v081_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for financing_dependence_distmax_378d
def bo_087_financing_dependence_financing_dependence_distmax_378d_pctslope_63d_2d_v082_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for financing_dependence_distmax_378d
def bo_087_financing_dependence_financing_dependence_distmax_378d_slopez_21_126_2d_v083_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for financing_dependence_distmax_378d
def bo_087_financing_dependence_financing_dependence_distmax_378d_slopez_63_252_2d_v084_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for financing_dependence_distmax_378d
def bo_087_financing_dependence_financing_dependence_distmax_378d_cumslope_63d_2d_v085_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for financing_dependence_distmax_378d
def bo_087_financing_dependence_financing_dependence_distmax_378d_logmagslope_63d_2d_v086_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max().abs())
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for financing_dependence_distmax_378d
def bo_087_financing_dependence_financing_dependence_distmax_378d_slope_rank_gap_2d_v087_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for financing_dependence_distmax_378d
def bo_087_financing_dependence_financing_dependence_distmax_378d_slope_504d_2d_v088_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for financing_dependence_distmax_378d
def bo_087_financing_dependence_financing_dependence_distmax_378d_sm126_slope63_2d_v089_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for financing_dependence_distmax_378d
def bo_087_financing_dependence_financing_dependence_distmax_378d_slopez_126_504_2d_v090_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for financing_dependence_distmin_378d
def bo_087_financing_dependence_financing_dependence_distmin_378d_slope_21d_2d_v091_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min().abs())
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for financing_dependence_distmin_378d
def bo_087_financing_dependence_financing_dependence_distmin_378d_slope_63d_2d_v092_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min().abs())
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for financing_dependence_distmin_378d
def bo_087_financing_dependence_financing_dependence_distmin_378d_slope_126d_2d_v093_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min().abs())
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for financing_dependence_distmin_378d
def bo_087_financing_dependence_financing_dependence_distmin_378d_slope_252d_2d_v094_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min().abs())
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for financing_dependence_distmin_378d
def bo_087_financing_dependence_financing_dependence_distmin_378d_sm63_slope21_2d_v095_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min().abs())
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for financing_dependence_distmin_378d
def bo_087_financing_dependence_financing_dependence_distmin_378d_sm252_slope63_2d_v096_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min().abs())
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for financing_dependence_distmin_378d
def bo_087_financing_dependence_financing_dependence_distmin_378d_pctslope_63d_2d_v097_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min().abs())
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for financing_dependence_distmin_378d
def bo_087_financing_dependence_financing_dependence_distmin_378d_slopez_21_126_2d_v098_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min().abs())
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for financing_dependence_distmin_378d
def bo_087_financing_dependence_financing_dependence_distmin_378d_slopez_63_252_2d_v099_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min().abs())
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for financing_dependence_distmin_378d
def bo_087_financing_dependence_financing_dependence_distmin_378d_cumslope_63d_2d_v100_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min().abs())
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for financing_dependence_distmin_378d
def bo_087_financing_dependence_financing_dependence_distmin_378d_logmagslope_63d_2d_v101_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min().abs())
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for financing_dependence_distmin_378d
def bo_087_financing_dependence_financing_dependence_distmin_378d_slope_rank_gap_2d_v102_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min().abs())
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for financing_dependence_distmin_378d
def bo_087_financing_dependence_financing_dependence_distmin_378d_slope_504d_2d_v103_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min().abs())
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for financing_dependence_distmin_378d
def bo_087_financing_dependence_financing_dependence_distmin_378d_sm126_slope63_2d_v104_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min().abs())
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for financing_dependence_distmin_378d
def bo_087_financing_dependence_financing_dependence_distmin_378d_slopez_126_504_2d_v105_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).min().abs())
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for financing_dependence_distmed_378d
def bo_087_financing_dependence_financing_dependence_distmed_378d_slope_21d_2d_v106_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for financing_dependence_distmed_378d
def bo_087_financing_dependence_financing_dependence_distmed_378d_slope_63d_2d_v107_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for financing_dependence_distmed_378d
def bo_087_financing_dependence_financing_dependence_distmed_378d_slope_126d_2d_v108_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for financing_dependence_distmed_378d
def bo_087_financing_dependence_financing_dependence_distmed_378d_slope_252d_2d_v109_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for financing_dependence_distmed_378d
def bo_087_financing_dependence_financing_dependence_distmed_378d_sm63_slope21_2d_v110_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for financing_dependence_distmed_378d
def bo_087_financing_dependence_financing_dependence_distmed_378d_sm252_slope63_2d_v111_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for financing_dependence_distmed_378d
def bo_087_financing_dependence_financing_dependence_distmed_378d_pctslope_63d_2d_v112_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for financing_dependence_distmed_378d
def bo_087_financing_dependence_financing_dependence_distmed_378d_slopez_21_126_2d_v113_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for financing_dependence_distmed_378d
def bo_087_financing_dependence_financing_dependence_distmed_378d_slopez_63_252_2d_v114_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for financing_dependence_distmed_378d
def bo_087_financing_dependence_financing_dependence_distmed_378d_cumslope_63d_2d_v115_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for financing_dependence_distmed_378d
def bo_087_financing_dependence_financing_dependence_distmed_378d_logmagslope_63d_2d_v116_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median().abs())
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for financing_dependence_distmed_378d
def bo_087_financing_dependence_financing_dependence_distmed_378d_slope_rank_gap_2d_v117_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for financing_dependence_distmed_378d
def bo_087_financing_dependence_financing_dependence_distmed_378d_slope_504d_2d_v118_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for financing_dependence_distmed_378d
def bo_087_financing_dependence_financing_dependence_distmed_378d_sm126_slope63_2d_v119_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for financing_dependence_distmed_378d
def bo_087_financing_dependence_financing_dependence_distmed_378d_slopez_126_504_2d_v120_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = _safe_div((_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median(), (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(378, min_periods=max(2, 378//2)).median().abs())
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for financing_dependence_upper_gap_126d
def bo_087_financing_dependence_financing_dependence_upper_gap_126d_slope_21d_2d_v121_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for financing_dependence_upper_gap_126d
def bo_087_financing_dependence_financing_dependence_upper_gap_126d_slope_63d_2d_v122_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for financing_dependence_upper_gap_126d
def bo_087_financing_dependence_financing_dependence_upper_gap_126d_slope_126d_2d_v123_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for financing_dependence_upper_gap_126d
def bo_087_financing_dependence_financing_dependence_upper_gap_126d_slope_252d_2d_v124_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for financing_dependence_upper_gap_126d
def bo_087_financing_dependence_financing_dependence_upper_gap_126d_sm63_slope21_2d_v125_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for financing_dependence_upper_gap_126d
def bo_087_financing_dependence_financing_dependence_upper_gap_126d_sm252_slope63_2d_v126_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for financing_dependence_upper_gap_126d
def bo_087_financing_dependence_financing_dependence_upper_gap_126d_pctslope_63d_2d_v127_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for financing_dependence_upper_gap_126d
def bo_087_financing_dependence_financing_dependence_upper_gap_126d_slopez_21_126_2d_v128_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for financing_dependence_upper_gap_126d
def bo_087_financing_dependence_financing_dependence_upper_gap_126d_slopez_63_252_2d_v129_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for financing_dependence_upper_gap_126d
def bo_087_financing_dependence_financing_dependence_upper_gap_126d_cumslope_63d_2d_v130_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for financing_dependence_upper_gap_126d
def bo_087_financing_dependence_financing_dependence_upper_gap_126d_logmagslope_63d_2d_v131_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for financing_dependence_upper_gap_126d
def bo_087_financing_dependence_financing_dependence_upper_gap_126d_slope_rank_gap_2d_v132_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for financing_dependence_upper_gap_126d
def bo_087_financing_dependence_financing_dependence_upper_gap_126d_slope_504d_2d_v133_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for financing_dependence_upper_gap_126d
def bo_087_financing_dependence_financing_dependence_upper_gap_126d_sm126_slope63_2d_v134_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for financing_dependence_upper_gap_126d
def bo_087_financing_dependence_financing_dependence_upper_gap_126d_slopez_126_504_2d_v135_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

# 21d slope for financing_dependence_lower_gap_126d
def bo_087_financing_dependence_financing_dependence_lower_gap_126d_slope_21d_2d_v136_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.25)
    result = _slope(base, 21)
    return _clean(result)

# 63d slope for financing_dependence_lower_gap_126d
def bo_087_financing_dependence_financing_dependence_lower_gap_126d_slope_63d_2d_v137_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.25)
    result = _slope(base, 63)
    return _clean(result)

# 126d slope for financing_dependence_lower_gap_126d
def bo_087_financing_dependence_financing_dependence_lower_gap_126d_slope_126d_2d_v138_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.25)
    result = _slope(base, 126)
    return _clean(result)

# 252d slope for financing_dependence_lower_gap_126d
def bo_087_financing_dependence_financing_dependence_lower_gap_126d_slope_252d_2d_v139_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.25)
    result = _slope(base, 252)
    return _clean(result)

# 63d smoothed 21d slope for financing_dependence_lower_gap_126d
def bo_087_financing_dependence_financing_dependence_lower_gap_126d_sm63_slope21_2d_v140_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.25)
    result = _slope(_mean(base, 63), 21)
    return _clean(result)

# 252d smoothed 63d slope for financing_dependence_lower_gap_126d
def bo_087_financing_dependence_financing_dependence_lower_gap_126d_sm252_slope63_2d_v141_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.25)
    result = _slope(_mean(base, 252), 63)
    return _clean(result)

# 63d pct slope for financing_dependence_lower_gap_126d
def bo_087_financing_dependence_financing_dependence_lower_gap_126d_pctslope_63d_2d_v142_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.25)
    result = _slope_pct(base, 63)
    return _clean(result)

# 21d slope z-score for financing_dependence_lower_gap_126d
def bo_087_financing_dependence_financing_dependence_lower_gap_126d_slopez_21_126_2d_v143_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.25)
    result = _z(_slope(base, 21), 126)
    return _clean(result)

# 63d slope z-score for financing_dependence_lower_gap_126d
def bo_087_financing_dependence_financing_dependence_lower_gap_126d_slopez_63_252_2d_v144_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.25)
    result = _z(_slope(base, 63), 252)
    return _clean(result)

# 63d cumulative slope for financing_dependence_lower_gap_126d
def bo_087_financing_dependence_financing_dependence_lower_gap_126d_cumslope_63d_2d_v145_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.25)
    result = _slope(base, 21).rolling(63, min_periods=32).sum()
    return _clean(result)

# signed log slope magnitude for financing_dependence_lower_gap_126d
def bo_087_financing_dependence_financing_dependence_lower_gap_126d_logmagslope_63d_2d_v146_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.25)
    s = _slope(base, 63); result = np.log(s.abs().replace(0, np.nan)) * np.sign(s)
    return _clean(result)

# slope regime gap for financing_dependence_lower_gap_126d
def bo_087_financing_dependence_financing_dependence_lower_gap_126d_slope_rank_gap_2d_v147_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.25)
    result = _z(_slope(base, 63), 504) - _z(_slope(base, 21), 126)
    return _clean(result)

# 504d slope for financing_dependence_lower_gap_126d
def bo_087_financing_dependence_financing_dependence_lower_gap_126d_slope_504d_2d_v148_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.25)
    result = _slope(base, 504)
    return _clean(result)

# 126d smoothed 63d slope for financing_dependence_lower_gap_126d
def bo_087_financing_dependence_financing_dependence_lower_gap_126d_sm126_slope63_2d_v149_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.25)
    result = _slope(_mean(base, 126), 63)
    return _clean(result)

# 126d slope z-score for financing_dependence_lower_gap_126d
def bo_087_financing_dependence_financing_dependence_lower_gap_126d_slopez_126_504_2d_v150_signal(ncfbus, ncfcommon, ncfdebt, assets):
    base = (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())) - (_safe_div(ncfbus + ncfcommon + ncfdebt, assets.abs())).rolling(126, min_periods=max(2, 126//2)).quantile(0.25)
    result = _z(_slope(base, 126), 504)
    return _clean(result)

REGISTRY = {fn.__name__: {"inputs": ['ncfbus', 'ncfcommon', 'ncfdebt', 'assets'], "func": fn} for fn in [bo_087_financing_dependence_financing_dependence_slope_21d_2d_v001_signal, bo_087_financing_dependence_financing_dependence_slope_63d_2d_v002_signal, bo_087_financing_dependence_financing_dependence_slope_126d_2d_v003_signal, bo_087_financing_dependence_financing_dependence_slope_252d_2d_v004_signal, bo_087_financing_dependence_financing_dependence_sm63_slope21_2d_v005_signal, bo_087_financing_dependence_financing_dependence_sm252_slope63_2d_v006_signal, bo_087_financing_dependence_financing_dependence_pctslope_63d_2d_v007_signal, bo_087_financing_dependence_financing_dependence_slopez_21_126_2d_v008_signal, bo_087_financing_dependence_financing_dependence_slopez_63_252_2d_v009_signal, bo_087_financing_dependence_financing_dependence_cumslope_63d_2d_v010_signal, bo_087_financing_dependence_financing_dependence_logmagslope_63d_2d_v011_signal, bo_087_financing_dependence_financing_dependence_slope_rank_gap_2d_v012_signal, bo_087_financing_dependence_financing_dependence_slope_504d_2d_v013_signal, bo_087_financing_dependence_financing_dependence_sm126_slope63_2d_v014_signal, bo_087_financing_dependence_financing_dependence_slopez_126_504_2d_v015_signal, bo_087_financing_dependence_financing_dependence_mean_42d_slope_21d_2d_v016_signal, bo_087_financing_dependence_financing_dependence_mean_42d_slope_63d_2d_v017_signal, bo_087_financing_dependence_financing_dependence_mean_42d_slope_126d_2d_v018_signal, bo_087_financing_dependence_financing_dependence_mean_42d_slope_252d_2d_v019_signal, bo_087_financing_dependence_financing_dependence_mean_42d_sm63_slope21_2d_v020_signal, bo_087_financing_dependence_financing_dependence_mean_42d_sm252_slope63_2d_v021_signal, bo_087_financing_dependence_financing_dependence_mean_42d_pctslope_63d_2d_v022_signal, bo_087_financing_dependence_financing_dependence_mean_42d_slopez_21_126_2d_v023_signal, bo_087_financing_dependence_financing_dependence_mean_42d_slopez_63_252_2d_v024_signal, bo_087_financing_dependence_financing_dependence_mean_42d_cumslope_63d_2d_v025_signal, bo_087_financing_dependence_financing_dependence_mean_42d_logmagslope_63d_2d_v026_signal, bo_087_financing_dependence_financing_dependence_mean_42d_slope_rank_gap_2d_v027_signal, bo_087_financing_dependence_financing_dependence_mean_42d_slope_504d_2d_v028_signal, bo_087_financing_dependence_financing_dependence_mean_42d_sm126_slope63_2d_v029_signal, bo_087_financing_dependence_financing_dependence_mean_42d_slopez_126_504_2d_v030_signal, bo_087_financing_dependence_financing_dependence_mean_126d_slope_21d_2d_v031_signal, bo_087_financing_dependence_financing_dependence_mean_126d_slope_126d_2d_v033_signal, bo_087_financing_dependence_financing_dependence_mean_126d_slope_252d_2d_v034_signal, bo_087_financing_dependence_financing_dependence_mean_126d_sm63_slope21_2d_v035_signal, bo_087_financing_dependence_financing_dependence_mean_126d_sm252_slope63_2d_v036_signal, bo_087_financing_dependence_financing_dependence_mean_126d_pctslope_63d_2d_v037_signal, bo_087_financing_dependence_financing_dependence_mean_126d_slopez_21_126_2d_v038_signal, bo_087_financing_dependence_financing_dependence_mean_126d_slopez_63_252_2d_v039_signal, bo_087_financing_dependence_financing_dependence_mean_126d_cumslope_63d_2d_v040_signal, bo_087_financing_dependence_financing_dependence_mean_126d_logmagslope_63d_2d_v041_signal, bo_087_financing_dependence_financing_dependence_mean_126d_slope_rank_gap_2d_v042_signal, bo_087_financing_dependence_financing_dependence_mean_126d_slope_504d_2d_v043_signal, bo_087_financing_dependence_financing_dependence_mean_126d_sm126_slope63_2d_v044_signal, bo_087_financing_dependence_financing_dependence_mean_126d_slopez_126_504_2d_v045_signal, bo_087_financing_dependence_financing_dependence_z_126d_slope_21d_2d_v046_signal, bo_087_financing_dependence_financing_dependence_z_126d_slope_63d_2d_v047_signal, bo_087_financing_dependence_financing_dependence_z_126d_slope_126d_2d_v048_signal, bo_087_financing_dependence_financing_dependence_z_126d_slope_252d_2d_v049_signal, bo_087_financing_dependence_financing_dependence_z_126d_sm63_slope21_2d_v050_signal, bo_087_financing_dependence_financing_dependence_z_126d_sm252_slope63_2d_v051_signal, bo_087_financing_dependence_financing_dependence_z_126d_pctslope_63d_2d_v052_signal, bo_087_financing_dependence_financing_dependence_z_126d_slopez_21_126_2d_v053_signal, bo_087_financing_dependence_financing_dependence_z_126d_slopez_63_252_2d_v054_signal, bo_087_financing_dependence_financing_dependence_z_126d_cumslope_63d_2d_v055_signal, bo_087_financing_dependence_financing_dependence_z_126d_logmagslope_63d_2d_v056_signal, bo_087_financing_dependence_financing_dependence_z_126d_slope_rank_gap_2d_v057_signal, bo_087_financing_dependence_financing_dependence_z_126d_slope_504d_2d_v058_signal, bo_087_financing_dependence_financing_dependence_z_126d_sm126_slope63_2d_v059_signal, bo_087_financing_dependence_financing_dependence_z_126d_slopez_126_504_2d_v060_signal, bo_087_financing_dependence_financing_dependence_z_378d_slope_21d_2d_v061_signal, bo_087_financing_dependence_financing_dependence_z_378d_slope_63d_2d_v062_signal, bo_087_financing_dependence_financing_dependence_z_378d_slope_126d_2d_v063_signal, bo_087_financing_dependence_financing_dependence_z_378d_slope_252d_2d_v064_signal, bo_087_financing_dependence_financing_dependence_z_378d_sm63_slope21_2d_v065_signal, bo_087_financing_dependence_financing_dependence_z_378d_sm252_slope63_2d_v066_signal, bo_087_financing_dependence_financing_dependence_z_378d_pctslope_63d_2d_v067_signal, bo_087_financing_dependence_financing_dependence_z_378d_slopez_21_126_2d_v068_signal, bo_087_financing_dependence_financing_dependence_z_378d_slopez_63_252_2d_v069_signal, bo_087_financing_dependence_financing_dependence_z_378d_cumslope_63d_2d_v070_signal, bo_087_financing_dependence_financing_dependence_z_378d_logmagslope_63d_2d_v071_signal, bo_087_financing_dependence_financing_dependence_z_378d_slope_rank_gap_2d_v072_signal, bo_087_financing_dependence_financing_dependence_z_378d_slope_504d_2d_v073_signal, bo_087_financing_dependence_financing_dependence_z_378d_sm126_slope63_2d_v074_signal, bo_087_financing_dependence_financing_dependence_z_378d_slopez_126_504_2d_v075_signal, bo_087_financing_dependence_financing_dependence_distmax_378d_slope_21d_2d_v076_signal, bo_087_financing_dependence_financing_dependence_distmax_378d_slope_63d_2d_v077_signal, bo_087_financing_dependence_financing_dependence_distmax_378d_slope_126d_2d_v078_signal, bo_087_financing_dependence_financing_dependence_distmax_378d_slope_252d_2d_v079_signal, bo_087_financing_dependence_financing_dependence_distmax_378d_sm63_slope21_2d_v080_signal, bo_087_financing_dependence_financing_dependence_distmax_378d_sm252_slope63_2d_v081_signal, bo_087_financing_dependence_financing_dependence_distmax_378d_pctslope_63d_2d_v082_signal, bo_087_financing_dependence_financing_dependence_distmax_378d_slopez_21_126_2d_v083_signal, bo_087_financing_dependence_financing_dependence_distmax_378d_slopez_63_252_2d_v084_signal, bo_087_financing_dependence_financing_dependence_distmax_378d_cumslope_63d_2d_v085_signal, bo_087_financing_dependence_financing_dependence_distmax_378d_logmagslope_63d_2d_v086_signal, bo_087_financing_dependence_financing_dependence_distmax_378d_slope_rank_gap_2d_v087_signal, bo_087_financing_dependence_financing_dependence_distmax_378d_slope_504d_2d_v088_signal, bo_087_financing_dependence_financing_dependence_distmax_378d_sm126_slope63_2d_v089_signal, bo_087_financing_dependence_financing_dependence_distmax_378d_slopez_126_504_2d_v090_signal, bo_087_financing_dependence_financing_dependence_distmin_378d_slope_21d_2d_v091_signal, bo_087_financing_dependence_financing_dependence_distmin_378d_slope_63d_2d_v092_signal, bo_087_financing_dependence_financing_dependence_distmin_378d_slope_126d_2d_v093_signal, bo_087_financing_dependence_financing_dependence_distmin_378d_slope_252d_2d_v094_signal, bo_087_financing_dependence_financing_dependence_distmin_378d_sm63_slope21_2d_v095_signal, bo_087_financing_dependence_financing_dependence_distmin_378d_sm252_slope63_2d_v096_signal, bo_087_financing_dependence_financing_dependence_distmin_378d_pctslope_63d_2d_v097_signal, bo_087_financing_dependence_financing_dependence_distmin_378d_slopez_21_126_2d_v098_signal, bo_087_financing_dependence_financing_dependence_distmin_378d_slopez_63_252_2d_v099_signal, bo_087_financing_dependence_financing_dependence_distmin_378d_cumslope_63d_2d_v100_signal, bo_087_financing_dependence_financing_dependence_distmin_378d_logmagslope_63d_2d_v101_signal, bo_087_financing_dependence_financing_dependence_distmin_378d_slope_rank_gap_2d_v102_signal, bo_087_financing_dependence_financing_dependence_distmin_378d_slope_504d_2d_v103_signal, bo_087_financing_dependence_financing_dependence_distmin_378d_sm126_slope63_2d_v104_signal, bo_087_financing_dependence_financing_dependence_distmin_378d_slopez_126_504_2d_v105_signal, bo_087_financing_dependence_financing_dependence_distmed_378d_slope_21d_2d_v106_signal, bo_087_financing_dependence_financing_dependence_distmed_378d_slope_63d_2d_v107_signal, bo_087_financing_dependence_financing_dependence_distmed_378d_slope_126d_2d_v108_signal, bo_087_financing_dependence_financing_dependence_distmed_378d_slope_252d_2d_v109_signal, bo_087_financing_dependence_financing_dependence_distmed_378d_sm63_slope21_2d_v110_signal, bo_087_financing_dependence_financing_dependence_distmed_378d_sm252_slope63_2d_v111_signal, bo_087_financing_dependence_financing_dependence_distmed_378d_pctslope_63d_2d_v112_signal, bo_087_financing_dependence_financing_dependence_distmed_378d_slopez_21_126_2d_v113_signal, bo_087_financing_dependence_financing_dependence_distmed_378d_slopez_63_252_2d_v114_signal, bo_087_financing_dependence_financing_dependence_distmed_378d_cumslope_63d_2d_v115_signal, bo_087_financing_dependence_financing_dependence_distmed_378d_logmagslope_63d_2d_v116_signal, bo_087_financing_dependence_financing_dependence_distmed_378d_slope_rank_gap_2d_v117_signal, bo_087_financing_dependence_financing_dependence_distmed_378d_slope_504d_2d_v118_signal, bo_087_financing_dependence_financing_dependence_distmed_378d_sm126_slope63_2d_v119_signal, bo_087_financing_dependence_financing_dependence_distmed_378d_slopez_126_504_2d_v120_signal, bo_087_financing_dependence_financing_dependence_upper_gap_126d_slope_21d_2d_v121_signal, bo_087_financing_dependence_financing_dependence_upper_gap_126d_slope_63d_2d_v122_signal, bo_087_financing_dependence_financing_dependence_upper_gap_126d_slope_126d_2d_v123_signal, bo_087_financing_dependence_financing_dependence_upper_gap_126d_slope_252d_2d_v124_signal, bo_087_financing_dependence_financing_dependence_upper_gap_126d_sm63_slope21_2d_v125_signal, bo_087_financing_dependence_financing_dependence_upper_gap_126d_sm252_slope63_2d_v126_signal, bo_087_financing_dependence_financing_dependence_upper_gap_126d_pctslope_63d_2d_v127_signal, bo_087_financing_dependence_financing_dependence_upper_gap_126d_slopez_21_126_2d_v128_signal, bo_087_financing_dependence_financing_dependence_upper_gap_126d_slopez_63_252_2d_v129_signal, bo_087_financing_dependence_financing_dependence_upper_gap_126d_cumslope_63d_2d_v130_signal, bo_087_financing_dependence_financing_dependence_upper_gap_126d_logmagslope_63d_2d_v131_signal, bo_087_financing_dependence_financing_dependence_upper_gap_126d_slope_rank_gap_2d_v132_signal, bo_087_financing_dependence_financing_dependence_upper_gap_126d_slope_504d_2d_v133_signal, bo_087_financing_dependence_financing_dependence_upper_gap_126d_sm126_slope63_2d_v134_signal, bo_087_financing_dependence_financing_dependence_upper_gap_126d_slopez_126_504_2d_v135_signal, bo_087_financing_dependence_financing_dependence_lower_gap_126d_slope_21d_2d_v136_signal, bo_087_financing_dependence_financing_dependence_lower_gap_126d_slope_63d_2d_v137_signal, bo_087_financing_dependence_financing_dependence_lower_gap_126d_slope_126d_2d_v138_signal, bo_087_financing_dependence_financing_dependence_lower_gap_126d_slope_252d_2d_v139_signal, bo_087_financing_dependence_financing_dependence_lower_gap_126d_sm63_slope21_2d_v140_signal, bo_087_financing_dependence_financing_dependence_lower_gap_126d_sm252_slope63_2d_v141_signal, bo_087_financing_dependence_financing_dependence_lower_gap_126d_pctslope_63d_2d_v142_signal, bo_087_financing_dependence_financing_dependence_lower_gap_126d_slopez_21_126_2d_v143_signal, bo_087_financing_dependence_financing_dependence_lower_gap_126d_slopez_63_252_2d_v144_signal, bo_087_financing_dependence_financing_dependence_lower_gap_126d_cumslope_63d_2d_v145_signal, bo_087_financing_dependence_financing_dependence_lower_gap_126d_logmagslope_63d_2d_v146_signal, bo_087_financing_dependence_financing_dependence_lower_gap_126d_slope_rank_gap_2d_v147_signal, bo_087_financing_dependence_financing_dependence_lower_gap_126d_slope_504d_2d_v148_signal, bo_087_financing_dependence_financing_dependence_lower_gap_126d_sm126_slope63_2d_v149_signal, bo_087_financing_dependence_financing_dependence_lower_gap_126d_slopez_126_504_2d_v150_signal]}
BREAKOUTS_REGISTRY_2ND_001_150 = REGISTRY

if __name__ == "__main__":
    print(f"registered {len(REGISTRY)} breakout feature functions")
