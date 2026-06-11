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


# 756d mean for ath_recency_drought
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_756d_base_v006_signal(closeadj):
    base = closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)
    result = _mean(base, 756)
    return _clean(result)

# 252d std for ath_recency_drought
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_rstd_252d_base_v013_signal(closeadj):
    base = closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)
    result = _std(base, 252)
    return _clean(result)

# 21/126 ewm gap for ath_recency_drought
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_ewm_21_126_base_v027_signal(closeadj):
    base = closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)
    result = _ema(base, 21) - _ema(base, 126)
    return _clean(result)

# 63/252 ewm gap for ath_recency_drought
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_ewm_63_252_base_v028_signal(closeadj):
    base = closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True)
    result = _ema(base, 63) - _ema(base, 252)
    return _clean(result)

# 756d mean for ath_recency_drought_mean_42d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_mean_756d_base_v036_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 42)
    result = _mean(base, 756)
    return _clean(result)

# 63d std for ath_recency_drought_mean_42d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_rstd_63d_base_v041_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 42)
    result = _std(base, 63)
    return _clean(result)

# 126d std for ath_recency_drought_mean_42d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_rstd_126d_base_v042_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 42)
    result = _std(base, 126)
    return _clean(result)

# 252d std for ath_recency_drought_mean_42d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_rstd_252d_base_v043_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 42)
    result = _std(base, 252)
    return _clean(result)

# 21/126 ewm gap for ath_recency_drought_mean_42d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_ewm_21_126_base_v057_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 42)
    result = _ema(base, 21) - _ema(base, 126)
    return _clean(result)

# 63/252 ewm gap for ath_recency_drought_mean_42d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_ewm_63_252_base_v058_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 42)
    result = _ema(base, 63) - _ema(base, 252)
    return _clean(result)

# 504d mean for ath_recency_drought_mean_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_mean_504d_base_v065_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _mean(base, 504)
    return _clean(result)

# 756d mean for ath_recency_drought_mean_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_mean_756d_base_v066_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _mean(base, 756)
    return _clean(result)

# 504d z-score for ath_recency_drought_mean_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_z_504d_base_v070_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _z(base, 504)
    return _clean(result)

# 126d std for ath_recency_drought_mean_126d
def bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_rstd_126d_base_v072_signal(closeadj):
    base = _mean(closeadj.rolling(756, min_periods=378).apply(lambda x: float(len(x) - 1 - np.argmax(x)), raw=True), 126)
    result = _std(base, 126)
    return _clean(result)

REGISTRY = {fn.__name__: {"inputs": ['closeadj'], "func": fn} for fn in [bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_756d_base_v006_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_rstd_252d_base_v013_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_ewm_21_126_base_v027_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_ewm_63_252_base_v028_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_mean_756d_base_v036_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_rstd_63d_base_v041_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_rstd_126d_base_v042_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_rstd_252d_base_v043_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_ewm_21_126_base_v057_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_42d_ewm_63_252_base_v058_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_mean_504d_base_v065_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_mean_756d_base_v066_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_z_504d_base_v070_signal, bo_017_all_time_high_recency_vs_history_ath_recency_drought_mean_126d_rstd_126d_base_v072_signal]}
BREAKOUTS_REGISTRY_001_075 = REGISTRY

if __name__ == "__main__":
    print(f"registered {len(REGISTRY)} breakout feature functions")
