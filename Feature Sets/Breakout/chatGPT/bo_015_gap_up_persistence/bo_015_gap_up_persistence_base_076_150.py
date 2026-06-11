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


# 126d change for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_chg_126d_base_v076_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = base.diff(126)
    return _clean(result)

# 252d change for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_chg_252d_base_v077_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = base.diff(252)
    return _clean(result)

# 63d pct change for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_pct_63d_base_v078_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _ret(base, 63)
    return _clean(result)

# 126d pct change for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_pct_126d_base_v079_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _ret(base, 126)
    return _clean(result)

# 252d pct change for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_pct_252d_base_v080_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _ret(base, 252)
    return _clean(result)

# 126d distance from max for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_distmax_126d_base_v081_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    mx = base.rolling(126, min_periods=63).max(); result = _safe_div(base - mx, mx.abs())
    return _clean(result)

# 252d distance from max for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_distmax_252d_base_v082_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    mx = base.rolling(252, min_periods=126).max(); result = _safe_div(base - mx, mx.abs())
    return _clean(result)

# 504d distance from max for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_distmax_504d_base_v083_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    mx = base.rolling(504, min_periods=252).max(); result = _safe_div(base - mx, mx.abs())
    return _clean(result)

# 126d distance from median for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_distmed_126d_base_v084_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    med = base.rolling(126, min_periods=63).median(); result = _safe_div(base - med, med.abs())
    return _clean(result)

# 252d distance from median for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_distmed_252d_base_v085_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    med = base.rolling(252, min_periods=126).median(); result = _safe_div(base - med, med.abs())
    return _clean(result)

# 504d distance from median for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_distmed_504d_base_v086_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    med = base.rolling(504, min_periods=252).median(); result = _safe_div(base - med, med.abs())
    return _clean(result)

# 21/126 ewm gap for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_ewm_21_126_base_v087_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _ema(base, 21) - _ema(base, 126)
    return _clean(result)

# 63/252 ewm gap for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_ewm_63_252_base_v088_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _ema(base, 63) - _ema(base, 252)
    return _clean(result)

# 126d stability for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_stability_126d_base_v089_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _safe_div(_mean(base, 126), _std(base, 126).abs())
    return _clean(result)

# 252d stability for gap_up_persistence_mean_84d
def bo_015_gap_up_persistence_gap_up_persistence_mean_84d_stability_252d_base_v090_signal(open, closeadj):
    base = _mean(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _safe_div(_mean(base, 252), _std(base, 252).abs())
    return _clean(result)

# 21d mean for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_mean_21d_base_v091_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _mean(base, 21)
    return _clean(result)

# 63d mean for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_mean_63d_base_v092_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _mean(base, 63)
    return _clean(result)

# 126d mean for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_mean_126d_base_v093_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _mean(base, 126)
    return _clean(result)

# 252d mean for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_mean_252d_base_v094_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _mean(base, 252)
    return _clean(result)

# 504d mean for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_mean_504d_base_v095_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _mean(base, 504)
    return _clean(result)

# 756d mean for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_mean_756d_base_v096_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _mean(base, 756)
    return _clean(result)

# 63d z-score for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_z_63d_base_v097_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _z(base, 63)
    return _clean(result)

# 126d z-score for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_z_126d_base_v098_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _z(base, 126)
    return _clean(result)

# 252d z-score for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_z_252d_base_v099_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _z(base, 252)
    return _clean(result)

# 504d z-score for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_z_504d_base_v100_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _z(base, 504)
    return _clean(result)

# 63d std for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_rstd_63d_base_v101_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _std(base, 63)
    return _clean(result)

# 126d std for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_rstd_126d_base_v102_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _std(base, 126)
    return _clean(result)

# 252d std for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_rstd_252d_base_v103_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _std(base, 252)
    return _clean(result)

# 21d change for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_chg_21d_base_v104_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = base.diff(21)
    return _clean(result)

# 63d change for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_chg_63d_base_v105_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = base.diff(63)
    return _clean(result)

# 126d change for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_chg_126d_base_v106_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = base.diff(126)
    return _clean(result)

# 252d change for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_chg_252d_base_v107_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = base.diff(252)
    return _clean(result)

# 63d pct change for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_pct_63d_base_v108_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _ret(base, 63)
    return _clean(result)

# 126d pct change for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_pct_126d_base_v109_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _ret(base, 126)
    return _clean(result)

# 252d pct change for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_pct_252d_base_v110_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _ret(base, 252)
    return _clean(result)

# 126d distance from max for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_distmax_126d_base_v111_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    mx = base.rolling(126, min_periods=63).max(); result = _safe_div(base - mx, mx.abs())
    return _clean(result)

# 252d distance from max for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_distmax_252d_base_v112_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    mx = base.rolling(252, min_periods=126).max(); result = _safe_div(base - mx, mx.abs())
    return _clean(result)

# 504d distance from max for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_distmax_504d_base_v113_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    mx = base.rolling(504, min_periods=252).max(); result = _safe_div(base - mx, mx.abs())
    return _clean(result)

# 126d distance from median for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_distmed_126d_base_v114_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    med = base.rolling(126, min_periods=63).median(); result = _safe_div(base - med, med.abs())
    return _clean(result)

# 252d distance from median for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_distmed_252d_base_v115_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    med = base.rolling(252, min_periods=126).median(); result = _safe_div(base - med, med.abs())
    return _clean(result)

# 504d distance from median for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_distmed_504d_base_v116_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    med = base.rolling(504, min_periods=252).median(); result = _safe_div(base - med, med.abs())
    return _clean(result)

# 21/126 ewm gap for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_ewm_21_126_base_v117_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _ema(base, 21) - _ema(base, 126)
    return _clean(result)

# 63/252 ewm gap for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_ewm_63_252_base_v118_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _ema(base, 63) - _ema(base, 252)
    return _clean(result)

# 126d stability for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_stability_126d_base_v119_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _safe_div(_mean(base, 126), _std(base, 126).abs())
    return _clean(result)

# 252d stability for gap_up_persistence_z_84d
def bo_015_gap_up_persistence_gap_up_persistence_z_84d_stability_252d_base_v120_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 84)
    result = _safe_div(_mean(base, 252), _std(base, 252).abs())
    return _clean(result)

# 21d mean for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_mean_21d_base_v121_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _mean(base, 21)
    return _clean(result)

# 63d mean for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_mean_63d_base_v122_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _mean(base, 63)
    return _clean(result)

# 126d mean for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_mean_126d_base_v123_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _mean(base, 126)
    return _clean(result)

# 252d mean for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_mean_252d_base_v124_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _mean(base, 252)
    return _clean(result)

# 504d mean for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_mean_504d_base_v125_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _mean(base, 504)
    return _clean(result)

# 756d mean for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_mean_756d_base_v126_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _mean(base, 756)
    return _clean(result)

# 63d z-score for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_z_63d_base_v127_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _z(base, 63)
    return _clean(result)

# 126d z-score for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_z_126d_base_v128_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _z(base, 126)
    return _clean(result)

# 252d z-score for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_z_252d_base_v129_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _z(base, 252)
    return _clean(result)

# 504d z-score for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_z_504d_base_v130_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _z(base, 504)
    return _clean(result)

# 63d std for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_rstd_63d_base_v131_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _std(base, 63)
    return _clean(result)

# 126d std for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_rstd_126d_base_v132_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _std(base, 126)
    return _clean(result)

# 252d std for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_rstd_252d_base_v133_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _std(base, 252)
    return _clean(result)

# 21d change for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_chg_21d_base_v134_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = base.diff(21)
    return _clean(result)

# 63d change for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_chg_63d_base_v135_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = base.diff(63)
    return _clean(result)

# 126d change for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_chg_126d_base_v136_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = base.diff(126)
    return _clean(result)

# 252d change for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_chg_252d_base_v137_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = base.diff(252)
    return _clean(result)

# 63d pct change for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_pct_63d_base_v138_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _ret(base, 63)
    return _clean(result)

# 126d pct change for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_pct_126d_base_v139_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _ret(base, 126)
    return _clean(result)

# 252d pct change for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_pct_252d_base_v140_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _ret(base, 252)
    return _clean(result)

# 126d distance from max for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_distmax_126d_base_v141_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    mx = base.rolling(126, min_periods=63).max(); result = _safe_div(base - mx, mx.abs())
    return _clean(result)

# 252d distance from max for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_distmax_252d_base_v142_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    mx = base.rolling(252, min_periods=126).max(); result = _safe_div(base - mx, mx.abs())
    return _clean(result)

# 504d distance from max for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_distmax_504d_base_v143_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    mx = base.rolling(504, min_periods=252).max(); result = _safe_div(base - mx, mx.abs())
    return _clean(result)

# 126d distance from median for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_distmed_126d_base_v144_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    med = base.rolling(126, min_periods=63).median(); result = _safe_div(base - med, med.abs())
    return _clean(result)

# 252d distance from median for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_distmed_252d_base_v145_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    med = base.rolling(252, min_periods=126).median(); result = _safe_div(base - med, med.abs())
    return _clean(result)

# 504d distance from median for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_distmed_504d_base_v146_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    med = base.rolling(504, min_periods=252).median(); result = _safe_div(base - med, med.abs())
    return _clean(result)

# 21/126 ewm gap for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_ewm_21_126_base_v147_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _ema(base, 21) - _ema(base, 126)
    return _clean(result)

# 63/252 ewm gap for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_ewm_63_252_base_v148_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _ema(base, 63) - _ema(base, 252)
    return _clean(result)

# 126d stability for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_stability_126d_base_v149_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _safe_div(_mean(base, 126), _std(base, 126).abs())
    return _clean(result)

# 252d stability for gap_up_persistence_z_252d
def bo_015_gap_up_persistence_gap_up_persistence_z_252d_stability_252d_base_v150_signal(open, closeadj):
    base = _z(_safe_div(open - closeadj.shift(1), closeadj.shift(1).abs()) * (closeadj > open).astype(float), 252)
    result = _safe_div(_mean(base, 252), _std(base, 252).abs())
    return _clean(result)

REGISTRY = {fn.__name__: {"inputs": ['open', 'closeadj'], "func": fn} for fn in [bo_015_gap_up_persistence_gap_up_persistence_mean_84d_chg_126d_base_v076_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_chg_252d_base_v077_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_pct_63d_base_v078_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_pct_126d_base_v079_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_pct_252d_base_v080_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_distmax_126d_base_v081_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_distmax_252d_base_v082_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_distmax_504d_base_v083_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_distmed_126d_base_v084_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_distmed_252d_base_v085_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_distmed_504d_base_v086_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_ewm_21_126_base_v087_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_ewm_63_252_base_v088_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_stability_126d_base_v089_signal, bo_015_gap_up_persistence_gap_up_persistence_mean_84d_stability_252d_base_v090_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_mean_21d_base_v091_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_mean_63d_base_v092_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_mean_126d_base_v093_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_mean_252d_base_v094_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_mean_504d_base_v095_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_mean_756d_base_v096_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_z_63d_base_v097_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_z_126d_base_v098_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_z_252d_base_v099_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_z_504d_base_v100_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_rstd_63d_base_v101_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_rstd_126d_base_v102_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_rstd_252d_base_v103_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_chg_21d_base_v104_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_chg_63d_base_v105_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_chg_126d_base_v106_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_chg_252d_base_v107_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_pct_63d_base_v108_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_pct_126d_base_v109_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_pct_252d_base_v110_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_distmax_126d_base_v111_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_distmax_252d_base_v112_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_distmax_504d_base_v113_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_distmed_126d_base_v114_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_distmed_252d_base_v115_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_distmed_504d_base_v116_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_ewm_21_126_base_v117_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_ewm_63_252_base_v118_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_stability_126d_base_v119_signal, bo_015_gap_up_persistence_gap_up_persistence_z_84d_stability_252d_base_v120_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_mean_21d_base_v121_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_mean_63d_base_v122_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_mean_126d_base_v123_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_mean_252d_base_v124_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_mean_504d_base_v125_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_mean_756d_base_v126_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_z_63d_base_v127_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_z_126d_base_v128_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_z_252d_base_v129_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_z_504d_base_v130_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_rstd_63d_base_v131_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_rstd_126d_base_v132_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_rstd_252d_base_v133_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_chg_21d_base_v134_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_chg_63d_base_v135_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_chg_126d_base_v136_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_chg_252d_base_v137_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_pct_63d_base_v138_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_pct_126d_base_v139_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_pct_252d_base_v140_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_distmax_126d_base_v141_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_distmax_252d_base_v142_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_distmax_504d_base_v143_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_distmed_126d_base_v144_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_distmed_252d_base_v145_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_distmed_504d_base_v146_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_ewm_21_126_base_v147_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_ewm_63_252_base_v148_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_stability_126d_base_v149_signal, bo_015_gap_up_persistence_gap_up_persistence_z_252d_stability_252d_base_v150_signal]}
BREAKOUTS_REGISTRY_076_150 = REGISTRY

if __name__ == "__main__":
    print(f"registered {len(REGISTRY)} breakout feature functions")
