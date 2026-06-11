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


# 126d change for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_chg_126d_base_v076_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = base.diff(126)
    return _clean(result)

# 252d change for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_chg_252d_base_v077_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = base.diff(252)
    return _clean(result)

# 126d pct change for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_pct_126d_base_v079_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _ret(base, 126)
    return _clean(result)

# 252d pct change for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_pct_252d_base_v080_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _ret(base, 252)
    return _clean(result)

# 126d distance from max for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_distmax_126d_base_v081_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    mx = base.rolling(126, min_periods=63).max(); result = _safe_div(base - mx, mx.abs())
    return _clean(result)

# 252d distance from max for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_distmax_252d_base_v082_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    mx = base.rolling(252, min_periods=126).max(); result = _safe_div(base - mx, mx.abs())
    return _clean(result)

# 504d distance from max for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_distmax_504d_base_v083_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    mx = base.rolling(504, min_periods=252).max(); result = _safe_div(base - mx, mx.abs())
    return _clean(result)

# 126d distance from median for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_distmed_126d_base_v084_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    med = base.rolling(126, min_periods=63).median(); result = _safe_div(base - med, med.abs())
    return _clean(result)

# 252d distance from median for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_distmed_252d_base_v085_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    med = base.rolling(252, min_periods=126).median(); result = _safe_div(base - med, med.abs())
    return _clean(result)

# 504d distance from median for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_distmed_504d_base_v086_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    med = base.rolling(504, min_periods=252).median(); result = _safe_div(base - med, med.abs())
    return _clean(result)

# 21/126 ewm gap for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_ewm_21_126_base_v087_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _ema(base, 21) - _ema(base, 126)
    return _clean(result)

# 63/252 ewm gap for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_ewm_63_252_base_v088_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _ema(base, 63) - _ema(base, 252)
    return _clean(result)

# 126d stability for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_stability_126d_base_v089_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _safe_div(_mean(base, 126), _std(base, 126).abs())
    return _clean(result)

# 252d stability for money_flow_index_mean_126d
def bo_042_money_flow_index_money_flow_index_mean_126d_stability_252d_base_v090_signal(high, low, closeadj, volume):
    base = _mean(_mfi(high, low, closeadj, volume, 14), 126)
    result = _safe_div(_mean(base, 252), _std(base, 252).abs())
    return _clean(result)

# 21d mean for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_mean_21d_base_v091_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _mean(base, 21)
    return _clean(result)

# 63d mean for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_mean_63d_base_v092_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _mean(base, 63)
    return _clean(result)

# 126d mean for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_mean_126d_base_v093_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _mean(base, 126)
    return _clean(result)

# 63d z-score for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_z_63d_base_v097_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _z(base, 63)
    return _clean(result)

# 126d z-score for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_z_126d_base_v098_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _z(base, 126)
    return _clean(result)

# 63d std for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_rstd_63d_base_v101_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _std(base, 63)
    return _clean(result)

# 126d std for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_rstd_126d_base_v102_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _std(base, 126)
    return _clean(result)

# 21d change for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_chg_21d_base_v104_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = base.diff(21)
    return _clean(result)

# 63d change for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_chg_63d_base_v105_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = base.diff(63)
    return _clean(result)

# 252d change for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_chg_252d_base_v107_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = base.diff(252)
    return _clean(result)

# 63d pct change for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_pct_63d_base_v108_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _ret(base, 63)
    return _clean(result)

# 252d pct change for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_pct_252d_base_v110_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _ret(base, 252)
    return _clean(result)

# 126d distance from max for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_distmax_126d_base_v111_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    mx = base.rolling(126, min_periods=63).max(); result = _safe_div(base - mx, mx.abs())
    return _clean(result)

# 126d distance from median for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_distmed_126d_base_v114_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    med = base.rolling(126, min_periods=63).median(); result = _safe_div(base - med, med.abs())
    return _clean(result)

# 21/126 ewm gap for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_ewm_21_126_base_v117_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _ema(base, 21) - _ema(base, 126)
    return _clean(result)

# 63/252 ewm gap for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_ewm_63_252_base_v118_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _ema(base, 63) - _ema(base, 252)
    return _clean(result)

# 126d stability for money_flow_index_z_126d
def bo_042_money_flow_index_money_flow_index_z_126d_stability_126d_base_v119_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 126)
    result = _safe_div(_mean(base, 126), _std(base, 126).abs())
    return _clean(result)

# 21d mean for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_mean_21d_base_v121_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = _mean(base, 21)
    return _clean(result)

# 63d mean for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_mean_63d_base_v122_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = _mean(base, 63)
    return _clean(result)

# 126d mean for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_mean_126d_base_v123_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = _mean(base, 126)
    return _clean(result)

# 63d z-score for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_z_63d_base_v127_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = _z(base, 63)
    return _clean(result)

# 126d z-score for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_z_126d_base_v128_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = _z(base, 126)
    return _clean(result)

# 63d std for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_rstd_63d_base_v131_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = _std(base, 63)
    return _clean(result)

# 126d std for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_rstd_126d_base_v132_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = _std(base, 126)
    return _clean(result)

# 21d change for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_chg_21d_base_v134_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = base.diff(21)
    return _clean(result)

# 63d change for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_chg_63d_base_v135_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = base.diff(63)
    return _clean(result)

# 252d change for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_chg_252d_base_v137_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = base.diff(252)
    return _clean(result)

# 63d pct change for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_pct_63d_base_v138_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = _ret(base, 63)
    return _clean(result)

# 252d pct change for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_pct_252d_base_v140_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = _ret(base, 252)
    return _clean(result)

# 126d distance from max for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_distmax_126d_base_v141_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    mx = base.rolling(126, min_periods=63).max(); result = _safe_div(base - mx, mx.abs())
    return _clean(result)

# 126d distance from median for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_distmed_126d_base_v144_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    med = base.rolling(126, min_periods=63).median(); result = _safe_div(base - med, med.abs())
    return _clean(result)

# 21/126 ewm gap for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_ewm_21_126_base_v147_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = _ema(base, 21) - _ema(base, 126)
    return _clean(result)

# 63/252 ewm gap for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_ewm_63_252_base_v148_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = _ema(base, 63) - _ema(base, 252)
    return _clean(result)

# 126d stability for money_flow_index_z_378d
def bo_042_money_flow_index_money_flow_index_z_378d_stability_126d_base_v149_signal(high, low, closeadj, volume):
    base = _z(_mfi(high, low, closeadj, volume, 14), 378)
    result = _safe_div(_mean(base, 126), _std(base, 126).abs())
    return _clean(result)

REGISTRY = {fn.__name__: {"inputs": ['high', 'low', 'closeadj', 'volume'], "func": fn} for fn in [bo_042_money_flow_index_money_flow_index_mean_126d_chg_126d_base_v076_signal, bo_042_money_flow_index_money_flow_index_mean_126d_chg_252d_base_v077_signal, bo_042_money_flow_index_money_flow_index_mean_126d_pct_126d_base_v079_signal, bo_042_money_flow_index_money_flow_index_mean_126d_pct_252d_base_v080_signal, bo_042_money_flow_index_money_flow_index_mean_126d_distmax_126d_base_v081_signal, bo_042_money_flow_index_money_flow_index_mean_126d_distmax_252d_base_v082_signal, bo_042_money_flow_index_money_flow_index_mean_126d_distmax_504d_base_v083_signal, bo_042_money_flow_index_money_flow_index_mean_126d_distmed_126d_base_v084_signal, bo_042_money_flow_index_money_flow_index_mean_126d_distmed_252d_base_v085_signal, bo_042_money_flow_index_money_flow_index_mean_126d_distmed_504d_base_v086_signal, bo_042_money_flow_index_money_flow_index_mean_126d_ewm_21_126_base_v087_signal, bo_042_money_flow_index_money_flow_index_mean_126d_ewm_63_252_base_v088_signal, bo_042_money_flow_index_money_flow_index_mean_126d_stability_126d_base_v089_signal, bo_042_money_flow_index_money_flow_index_mean_126d_stability_252d_base_v090_signal, bo_042_money_flow_index_money_flow_index_z_126d_mean_21d_base_v091_signal, bo_042_money_flow_index_money_flow_index_z_126d_mean_63d_base_v092_signal, bo_042_money_flow_index_money_flow_index_z_126d_mean_126d_base_v093_signal, bo_042_money_flow_index_money_flow_index_z_126d_z_63d_base_v097_signal, bo_042_money_flow_index_money_flow_index_z_126d_z_126d_base_v098_signal, bo_042_money_flow_index_money_flow_index_z_126d_rstd_63d_base_v101_signal, bo_042_money_flow_index_money_flow_index_z_126d_rstd_126d_base_v102_signal, bo_042_money_flow_index_money_flow_index_z_126d_chg_21d_base_v104_signal, bo_042_money_flow_index_money_flow_index_z_126d_chg_63d_base_v105_signal, bo_042_money_flow_index_money_flow_index_z_126d_chg_252d_base_v107_signal, bo_042_money_flow_index_money_flow_index_z_126d_pct_63d_base_v108_signal, bo_042_money_flow_index_money_flow_index_z_126d_pct_252d_base_v110_signal, bo_042_money_flow_index_money_flow_index_z_126d_distmax_126d_base_v111_signal, bo_042_money_flow_index_money_flow_index_z_126d_distmed_126d_base_v114_signal, bo_042_money_flow_index_money_flow_index_z_126d_ewm_21_126_base_v117_signal, bo_042_money_flow_index_money_flow_index_z_126d_ewm_63_252_base_v118_signal, bo_042_money_flow_index_money_flow_index_z_126d_stability_126d_base_v119_signal, bo_042_money_flow_index_money_flow_index_z_378d_mean_21d_base_v121_signal, bo_042_money_flow_index_money_flow_index_z_378d_mean_63d_base_v122_signal, bo_042_money_flow_index_money_flow_index_z_378d_mean_126d_base_v123_signal, bo_042_money_flow_index_money_flow_index_z_378d_z_63d_base_v127_signal, bo_042_money_flow_index_money_flow_index_z_378d_z_126d_base_v128_signal, bo_042_money_flow_index_money_flow_index_z_378d_rstd_63d_base_v131_signal, bo_042_money_flow_index_money_flow_index_z_378d_rstd_126d_base_v132_signal, bo_042_money_flow_index_money_flow_index_z_378d_chg_21d_base_v134_signal, bo_042_money_flow_index_money_flow_index_z_378d_chg_63d_base_v135_signal, bo_042_money_flow_index_money_flow_index_z_378d_chg_252d_base_v137_signal, bo_042_money_flow_index_money_flow_index_z_378d_pct_63d_base_v138_signal, bo_042_money_flow_index_money_flow_index_z_378d_pct_252d_base_v140_signal, bo_042_money_flow_index_money_flow_index_z_378d_distmax_126d_base_v141_signal, bo_042_money_flow_index_money_flow_index_z_378d_distmed_126d_base_v144_signal, bo_042_money_flow_index_money_flow_index_z_378d_ewm_21_126_base_v147_signal, bo_042_money_flow_index_money_flow_index_z_378d_ewm_63_252_base_v148_signal, bo_042_money_flow_index_money_flow_index_z_378d_stability_126d_base_v149_signal]}
BREAKOUTS_REGISTRY_076_150 = REGISTRY

if __name__ == "__main__":
    print(f"registered {len(REGISTRY)} breakout feature functions")
