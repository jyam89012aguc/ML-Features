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


# 21d acceleration for money_flow_index
def bo_042_money_flow_index_money_flow_index_accel_21d_3d_v001_signal(high, low, closeadj, volume):
    base = _mfi(high, low, closeadj, volume, 14)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for money_flow_index
def bo_042_money_flow_index_money_flow_index_accel_63d_3d_v002_signal(high, low, closeadj, volume):
    base = _mfi(high, low, closeadj, volume, 14)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for money_flow_index
def bo_042_money_flow_index_money_flow_index_accel_126d_3d_v003_signal(high, low, closeadj, volume):
    base = _mfi(high, low, closeadj, volume, 14)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for money_flow_index
def bo_042_money_flow_index_money_flow_index_accel_norm_63d_3d_v004_signal(high, low, closeadj, volume):
    base = _mfi(high, low, closeadj, volume, 14)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for money_flow_index
def bo_042_money_flow_index_money_flow_index_jerk_21d_3d_v005_signal(high, low, closeadj, volume):
    base = _mfi(high, low, closeadj, volume, 14)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for money_flow_index
def bo_042_money_flow_index_money_flow_index_jerk_63d_3d_v006_signal(high, low, closeadj, volume):
    base = _mfi(high, low, closeadj, volume, 14)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# range-normalized acceleration for money_flow_index
def bo_042_money_flow_index_money_flow_index_rngaccel_63_252_3d_v010_signal(high, low, closeadj, volume):
    base = _mfi(high, low, closeadj, volume, 14)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# 252d acceleration for money_flow_index
def bo_042_money_flow_index_money_flow_index_accel_252d_3d_v012_signal(high, low, closeadj, volume):
    base = _mfi(high, low, closeadj, volume, 14)
    result = _accel(base, 252)
    return _clean(result)

# 21d acceleration for money_flow_index_mean_42d
def bo_042_money_flow_index_money_flow_index_mean_42d_accel_21d_3d_v017_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 42)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for money_flow_index_mean_42d
def bo_042_money_flow_index_money_flow_index_mean_42d_accel_63d_3d_v018_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 42)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for money_flow_index_mean_42d
def bo_042_money_flow_index_money_flow_index_mean_42d_accel_126d_3d_v019_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 42)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for money_flow_index_mean_42d
def bo_042_money_flow_index_money_flow_index_mean_42d_accel_norm_63d_3d_v020_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 42)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for money_flow_index_mean_42d
def bo_042_money_flow_index_money_flow_index_mean_42d_jerk_21d_3d_v021_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 42)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for money_flow_index_mean_42d
def bo_042_money_flow_index_money_flow_index_mean_42d_jerk_63d_3d_v022_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 42)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# range-normalized acceleration for money_flow_index_mean_42d
def bo_042_money_flow_index_money_flow_index_mean_42d_rngaccel_63_252_3d_v026_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 42)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# 252d acceleration for money_flow_index_mean_42d
def bo_042_money_flow_index_money_flow_index_mean_42d_accel_252d_3d_v028_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 42)
    result = _accel(base, 252)
    return _clean(result)

# 21d normalized acceleration for money_flow_index_mean_42d
def bo_042_money_flow_index_money_flow_index_mean_42d_accel_norm_21d_3d_v031_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 42)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# 21d acceleration for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_accel_21d_3d_v033_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _accel(base, 21)
    return _clean(result)

# 63d acceleration for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_accel_63d_3d_v034_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _accel(base, 63)
    return _clean(result)

# 126d acceleration for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_accel_126d_3d_v035_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _accel(base, 126)
    return _clean(result)

# 63d normalized acceleration for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_accel_norm_63d_3d_v036_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _safe_div(_accel(base, 63), base.abs())
    return _clean(result)

# 21d jerk for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_jerk_21d_3d_v037_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 63d jerk for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_jerk_63d_3d_v038_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    s = _slope(base, 63); result = _slope(s, 63)
    return _clean(result)

# range-normalized acceleration for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_rngaccel_63_252_3d_v042_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    rng = base.rolling(252, min_periods=126).max() - base.rolling(252, min_periods=126).min(); result = _safe_div(_accel(base, 63), rng.abs())
    return _clean(result)

# 252d acceleration for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_accel_252d_3d_v044_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _accel(base, 252)
    return _clean(result)

# 21d normalized acceleration for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_accel_norm_21d_3d_v047_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# 21d acceleration for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_accel_21d_3d_v049_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _accel(base, 21)
    return _clean(result)

# 21d jerk for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_jerk_21d_3d_v053_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 252d acceleration for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_accel_252d_3d_v060_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _accel(base, 252)
    return _clean(result)

# 21d normalized acceleration for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_accel_norm_21d_3d_v063_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# 21d acceleration for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_accel_21d_3d_v065_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = _accel(base, 21)
    return _clean(result)

# 21d jerk for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_jerk_21d_3d_v069_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 21d normalized acceleration for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_accel_norm_21d_3d_v079_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# 21d acceleration for money_flow_index_distmax_378d
def bo_042_money_flow_index_money_flow_index_distmax_378d_accel_21d_3d_v081_signal(high, low, closeadj, volume):
    base = _safe_div((_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(378, min_periods=max(2, 378//2)).max(), (_mfi(high, low, closeadj, volume, 14)).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _accel(base, 21)
    return _clean(result)

# 21d jerk for money_flow_index_distmax_378d
def bo_042_money_flow_index_money_flow_index_distmax_378d_jerk_21d_3d_v085_signal(high, low, closeadj, volume):
    base = _safe_div((_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(378, min_periods=max(2, 378//2)).max(), (_mfi(high, low, closeadj, volume, 14)).rolling(378, min_periods=max(2, 378//2)).max().abs())
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 21d normalized acceleration for money_flow_index_distmax_378d
def bo_042_money_flow_index_money_flow_index_distmax_378d_accel_norm_21d_3d_v095_signal(high, low, closeadj, volume):
    base = _safe_div((_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(378, min_periods=max(2, 378//2)).max(), (_mfi(high, low, closeadj, volume, 14)).rolling(378, min_periods=max(2, 378//2)).max().abs())
    result = _safe_div(_accel(base, 21), base.abs())
    return _clean(result)

# 21d acceleration for money_flow_index_upper_gap_126d
def bo_042_money_flow_index_money_flow_index_upper_gap_126d_accel_21d_3d_v129_signal(high, low, closeadj, volume):
    base = (_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _accel(base, 21)
    return _clean(result)

# 21d jerk for money_flow_index_upper_gap_126d
def bo_042_money_flow_index_money_flow_index_upper_gap_126d_jerk_21d_3d_v133_signal(high, low, closeadj, volume):
    base = (_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    s = _slope(base, 21); result = _slope(s, 21)
    return _clean(result)

# 252d acceleration for money_flow_index_upper_gap_126d
def bo_042_money_flow_index_money_flow_index_upper_gap_126d_accel_252d_3d_v140_signal(high, low, closeadj, volume):
    base = (_mfi(high, low, closeadj, volume, 14)) - (_mfi(high, low, closeadj, volume, 14)).rolling(126, min_periods=max(2, 126//2)).quantile(0.75)
    result = _accel(base, 252)
    return _clean(result)

REGISTRY = {fn.__name__: {"inputs": ['high', 'low', 'closeadj', 'volume'], "func": fn} for fn in [bo_042_money_flow_index_money_flow_index_accel_21d_3d_v001_signal, bo_042_money_flow_index_money_flow_index_accel_63d_3d_v002_signal, bo_042_money_flow_index_money_flow_index_accel_126d_3d_v003_signal, bo_042_money_flow_index_money_flow_index_accel_norm_63d_3d_v004_signal, bo_042_money_flow_index_money_flow_index_jerk_21d_3d_v005_signal, bo_042_money_flow_index_money_flow_index_jerk_63d_3d_v006_signal, bo_042_money_flow_index_money_flow_index_rngaccel_63_252_3d_v010_signal, bo_042_money_flow_index_money_flow_index_accel_252d_3d_v012_signal, bo_042_money_flow_index_money_flow_index_mean_42d_accel_21d_3d_v017_signal, bo_042_money_flow_index_money_flow_index_mean_42d_accel_63d_3d_v018_signal, bo_042_money_flow_index_money_flow_index_mean_42d_accel_126d_3d_v019_signal, bo_042_money_flow_index_money_flow_index_mean_42d_accel_norm_63d_3d_v020_signal, bo_042_money_flow_index_money_flow_index_mean_42d_jerk_21d_3d_v021_signal, bo_042_money_flow_index_money_flow_index_mean_42d_jerk_63d_3d_v022_signal, bo_042_money_flow_index_money_flow_index_mean_42d_rngaccel_63_252_3d_v026_signal, bo_042_money_flow_index_money_flow_index_mean_42d_accel_252d_3d_v028_signal, bo_042_money_flow_index_money_flow_index_mean_42d_accel_norm_21d_3d_v031_signal, bo_042_money_flow_index_money_flow_index_mean_126d_accel_21d_3d_v033_signal, bo_042_money_flow_index_money_flow_index_mean_126d_accel_63d_3d_v034_signal, bo_042_money_flow_index_money_flow_index_mean_126d_accel_126d_3d_v035_signal, bo_042_money_flow_index_money_flow_index_mean_126d_accel_norm_63d_3d_v036_signal, bo_042_money_flow_index_money_flow_index_mean_126d_jerk_21d_3d_v037_signal, bo_042_money_flow_index_money_flow_index_mean_126d_jerk_63d_3d_v038_signal, bo_042_money_flow_index_money_flow_index_mean_126d_rngaccel_63_252_3d_v042_signal, bo_042_money_flow_index_money_flow_index_mean_126d_accel_252d_3d_v044_signal, bo_042_money_flow_index_money_flow_index_mean_126d_accel_norm_21d_3d_v047_signal, bo_042_money_flow_index_money_flow_index_z_126d_accel_21d_3d_v049_signal, bo_042_money_flow_index_money_flow_index_z_126d_jerk_21d_3d_v053_signal, bo_042_money_flow_index_money_flow_index_z_126d_accel_252d_3d_v060_signal, bo_042_money_flow_index_money_flow_index_z_126d_accel_norm_21d_3d_v063_signal, bo_042_money_flow_index_money_flow_index_z_378d_accel_21d_3d_v065_signal, bo_042_money_flow_index_money_flow_index_z_378d_jerk_21d_3d_v069_signal, bo_042_money_flow_index_money_flow_index_z_378d_accel_norm_21d_3d_v079_signal, bo_042_money_flow_index_money_flow_index_distmax_378d_accel_21d_3d_v081_signal, bo_042_money_flow_index_money_flow_index_distmax_378d_jerk_21d_3d_v085_signal, bo_042_money_flow_index_money_flow_index_distmax_378d_accel_norm_21d_3d_v095_signal, bo_042_money_flow_index_money_flow_index_upper_gap_126d_accel_21d_3d_v129_signal, bo_042_money_flow_index_money_flow_index_upper_gap_126d_jerk_21d_3d_v133_signal, bo_042_money_flow_index_money_flow_index_upper_gap_126d_accel_252d_3d_v140_signal]}
BREAKOUTS_REGISTRY_3RD_001_150 = REGISTRY

if __name__ == "__main__":
    print(f"registered {len(REGISTRY)} breakout feature functions")
