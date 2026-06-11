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


# 21d mean for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_21d_base_v001_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _mean(base, 21)
    return _clean(result)

# 63d mean for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_base_v002_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _mean(base, 63)
    return _clean(result)

# 126d mean for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_126d_base_v003_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _mean(base, 126)
    return _clean(result)

# 252d mean for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_252d_base_v004_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _mean(base, 252)
    return _clean(result)

# 504d mean for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_504d_base_v005_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _mean(base, 504)
    return _clean(result)

# 756d mean for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_756d_base_v006_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _mean(base, 756)
    return _clean(result)

# 63d z-score for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_63d_base_v007_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _z(base, 63)
    return _clean(result)

# 126d z-score for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_126d_base_v008_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _z(base, 126)
    return _clean(result)

# 252d z-score for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_252d_base_v009_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _z(base, 252)
    return _clean(result)

# 504d z-score for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_z_504d_base_v010_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _z(base, 504)
    return _clean(result)

# 63d std for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_rstd_63d_base_v011_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _std(base, 63)
    return _clean(result)

# 126d std for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_rstd_126d_base_v012_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _std(base, 126)
    return _clean(result)

# 252d std for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_rstd_252d_base_v013_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _std(base, 252)
    return _clean(result)

# 21d change for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_chg_21d_base_v014_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = base.diff(21)
    return _clean(result)

# 63d change for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_chg_63d_base_v015_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = base.diff(63)
    return _clean(result)

# 126d change for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_chg_126d_base_v016_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = base.diff(126)
    return _clean(result)

# 252d change for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_chg_252d_base_v017_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = base.diff(252)
    return _clean(result)

# 126d distance from max for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_126d_base_v021_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    mx = base.rolling(126, min_periods=63).max(); result = _safe_div(base - mx, mx.abs())
    return _clean(result)

# 252d distance from median for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_distmed_252d_base_v025_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    med = base.rolling(252, min_periods=126).median(); result = _safe_div(base - med, med.abs())
    return _clean(result)

# 21/126 ewm gap for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_ewm_21_126_base_v027_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _ema(base, 21) - _ema(base, 126)
    return _clean(result)

# 63/252 ewm gap for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_ewm_63_252_base_v028_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _ema(base, 63) - _ema(base, 252)
    return _clean(result)

# 126d stability for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_stability_126d_base_v029_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _safe_div(_mean(base, 126), _std(base, 126).abs())
    return _clean(result)

# 252d stability for revenue_growth_persistence
def bo_069_revenue_growth_persistence_revenue_growth_persistence_stability_252d_base_v030_signal(revenue):
    base = (_growth(revenue, 252).diff(252) > 0).astype(float)
    result = _safe_div(_mean(base, 252), _std(base, 252).abs())
    return _clean(result)

# 21d mean for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_mean_21d_base_v031_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _mean(base, 21)
    return _clean(result)

# 63d mean for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_mean_63d_base_v032_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _mean(base, 63)
    return _clean(result)

# 126d mean for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_mean_126d_base_v033_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _mean(base, 126)
    return _clean(result)

# 252d mean for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_mean_252d_base_v034_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _mean(base, 252)
    return _clean(result)

# 504d mean for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_mean_504d_base_v035_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _mean(base, 504)
    return _clean(result)

# 756d mean for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_mean_756d_base_v036_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _mean(base, 756)
    return _clean(result)

# 63d z-score for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_z_63d_base_v037_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _z(base, 63)
    return _clean(result)

# 126d z-score for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_z_126d_base_v038_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _z(base, 126)
    return _clean(result)

# 252d z-score for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_z_252d_base_v039_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _z(base, 252)
    return _clean(result)

# 504d z-score for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_z_504d_base_v040_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _z(base, 504)
    return _clean(result)

# 63d std for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_rstd_63d_base_v041_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _std(base, 63)
    return _clean(result)

# 126d std for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_rstd_126d_base_v042_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _std(base, 126)
    return _clean(result)

# 252d std for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_rstd_252d_base_v043_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _std(base, 252)
    return _clean(result)

# 21d change for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_chg_21d_base_v044_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = base.diff(21)
    return _clean(result)

# 63d change for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_chg_63d_base_v045_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = base.diff(63)
    return _clean(result)

# 126d change for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_chg_126d_base_v046_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = base.diff(126)
    return _clean(result)

# 252d change for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_chg_252d_base_v047_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = base.diff(252)
    return _clean(result)

# 63d pct change for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_pct_63d_base_v048_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _ret(base, 63)
    return _clean(result)

# 126d pct change for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_pct_126d_base_v049_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _ret(base, 126)
    return _clean(result)

# 252d pct change for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_pct_252d_base_v050_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _ret(base, 252)
    return _clean(result)

# 126d distance from max for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_distmax_126d_base_v051_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    mx = base.rolling(126, min_periods=63).max(); result = _safe_div(base - mx, mx.abs())
    return _clean(result)

# 252d distance from max for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_distmax_252d_base_v052_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    mx = base.rolling(252, min_periods=126).max(); result = _safe_div(base - mx, mx.abs())
    return _clean(result)

# 252d distance from median for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_distmed_252d_base_v055_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    med = base.rolling(252, min_periods=126).median(); result = _safe_div(base - med, med.abs())
    return _clean(result)

# 504d distance from median for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_distmed_504d_base_v056_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    med = base.rolling(504, min_periods=252).median(); result = _safe_div(base - med, med.abs())
    return _clean(result)

# 21/126 ewm gap for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_ewm_21_126_base_v057_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _ema(base, 21) - _ema(base, 126)
    return _clean(result)

# 63/252 ewm gap for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_ewm_63_252_base_v058_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _ema(base, 63) - _ema(base, 252)
    return _clean(result)

# 126d stability for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_stability_126d_base_v059_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _safe_div(_mean(base, 126), _std(base, 126).abs())
    return _clean(result)

# 252d stability for revenue_growth_persistence_mean_63d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_stability_252d_base_v060_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 63)
    result = _safe_div(_mean(base, 252), _std(base, 252).abs())
    return _clean(result)

# 21d mean for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_mean_21d_base_v061_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _mean(base, 21)
    return _clean(result)

# 63d mean for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_mean_63d_base_v062_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _mean(base, 63)
    return _clean(result)

# 126d mean for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_mean_126d_base_v063_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _mean(base, 126)
    return _clean(result)

# 252d mean for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_mean_252d_base_v064_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _mean(base, 252)
    return _clean(result)

# 504d mean for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_mean_504d_base_v065_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _mean(base, 504)
    return _clean(result)

# 756d mean for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_mean_756d_base_v066_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _mean(base, 756)
    return _clean(result)

# 63d z-score for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_z_63d_base_v067_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _z(base, 63)
    return _clean(result)

# 126d z-score for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_z_126d_base_v068_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _z(base, 126)
    return _clean(result)

# 252d z-score for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_z_252d_base_v069_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _z(base, 252)
    return _clean(result)

# 504d z-score for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_z_504d_base_v070_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _z(base, 504)
    return _clean(result)

# 63d std for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_rstd_63d_base_v071_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _std(base, 63)
    return _clean(result)

# 126d std for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_rstd_126d_base_v072_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _std(base, 126)
    return _clean(result)

# 252d std for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_rstd_252d_base_v073_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = _std(base, 252)
    return _clean(result)

# 21d change for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_chg_21d_base_v074_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = base.diff(21)
    return _clean(result)

# 63d change for revenue_growth_persistence_mean_200d
def bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_chg_63d_base_v075_signal(revenue):
    base = _mean((_growth(revenue, 252).diff(252) > 0).astype(float), 200)
    result = base.diff(63)
    return _clean(result)

REGISTRY = {fn.__name__: {"inputs": ['revenue'], "func": fn} for fn in [bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_21d_base_v001_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_base_v002_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_126d_base_v003_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_252d_base_v004_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_504d_base_v005_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_756d_base_v006_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_63d_base_v007_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_126d_base_v008_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_252d_base_v009_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_z_504d_base_v010_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_rstd_63d_base_v011_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_rstd_126d_base_v012_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_rstd_252d_base_v013_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_chg_21d_base_v014_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_chg_63d_base_v015_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_chg_126d_base_v016_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_chg_252d_base_v017_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_distmax_126d_base_v021_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_distmed_252d_base_v025_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_ewm_21_126_base_v027_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_ewm_63_252_base_v028_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_stability_126d_base_v029_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_stability_252d_base_v030_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_mean_21d_base_v031_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_mean_63d_base_v032_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_mean_126d_base_v033_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_mean_252d_base_v034_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_mean_504d_base_v035_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_mean_756d_base_v036_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_z_63d_base_v037_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_z_126d_base_v038_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_z_252d_base_v039_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_z_504d_base_v040_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_rstd_63d_base_v041_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_rstd_126d_base_v042_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_rstd_252d_base_v043_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_chg_21d_base_v044_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_chg_63d_base_v045_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_chg_126d_base_v046_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_chg_252d_base_v047_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_pct_63d_base_v048_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_pct_126d_base_v049_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_pct_252d_base_v050_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_distmax_126d_base_v051_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_distmax_252d_base_v052_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_distmed_252d_base_v055_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_distmed_504d_base_v056_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_ewm_21_126_base_v057_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_ewm_63_252_base_v058_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_stability_126d_base_v059_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_63d_stability_252d_base_v060_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_mean_21d_base_v061_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_mean_63d_base_v062_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_mean_126d_base_v063_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_mean_252d_base_v064_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_mean_504d_base_v065_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_mean_756d_base_v066_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_z_63d_base_v067_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_z_126d_base_v068_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_z_252d_base_v069_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_z_504d_base_v070_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_rstd_63d_base_v071_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_rstd_126d_base_v072_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_rstd_252d_base_v073_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_chg_21d_base_v074_signal, bo_069_revenue_growth_persistence_revenue_growth_persistence_mean_200d_chg_63d_base_v075_signal]}
BREAKOUTS_REGISTRY_001_075 = REGISTRY

if __name__ == "__main__":
    print(f"registered {len(REGISTRY)} breakout feature functions")
