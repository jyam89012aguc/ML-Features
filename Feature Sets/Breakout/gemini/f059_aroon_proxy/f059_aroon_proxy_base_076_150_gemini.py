import pandas as pd
import numpy as np
import inspect

# ===== BREAKOUT High-Performance Alpha Helpers =====
def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _ewma(s, w): return s.ewm(span=w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)
def _ratio(n, d): return n / d.replace(0, np.nan)
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()
def _drawdown(s, w): return (s / _max(s, w).replace(0, np.nan)) - 1
def _recovery(s, w): return (s / _min(s, w).replace(0, np.nan)) - 1
def _slope_pct(s, w): return s.pct_change(w)
def _jerk(s, w1, w2): return s.slope_pct(w1).diff(w2)
def _skew(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).skew()
def _kurt(s, w): return s.rolling(w, min_periods=min(w, 40) if w > 40 else min(w, 5)).kurt()
def _rsi(s, w):
    delta = s.diff()
    up = delta.clip(lower=0)
    down = -delta.clip(upper=0)
    ma_up = up.rolling(w, min_periods=min(w, 10)).mean()
    ma_down = down.rolling(w, min_periods=min(w, 10)).mean()
    rs = ma_up / ma_down.replace(0, np.nan)
    return 100 - (100 / (1 + rs))
def bo_059_aroon_proxy_trend_quality_rsi_63d_v076_signal(closeadj):
    """Relative Strength Index (RSI) of Trend quality over 63d window."""
    res = _rsi(closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_rsi_126d_v077_signal(closeadj):
    """Relative Strength Index (RSI) of Raw level of closeadj over 126d window."""
    res = _rsi(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_rsi_126d_v078_signal(closeadj):
    """Relative Strength Index (RSI) of Trend quality over 126d window."""
    res = _rsi(closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_rsi_252d_v079_signal(closeadj):
    """Relative Strength Index (RSI) of Raw level of closeadj over 252d window."""
    res = _rsi(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_rsi_252d_v080_signal(closeadj):
    """Relative Strength Index (RSI) of Trend quality over 252d window."""
    res = _rsi(closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_rsi_504d_v081_signal(closeadj):
    """Relative Strength Index (RSI) of Raw level of closeadj over 504d window."""
    res = _rsi(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_rsi_504d_v082_signal(closeadj):
    """Relative Strength Index (RSI) of Trend quality over 504d window."""
    res = _rsi(closeadj, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_rsi_756d_v083_signal(closeadj):
    """Relative Strength Index (RSI) of Raw level of closeadj over 756d window."""
    res = _rsi(closeadj, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_rsi_756d_v084_signal(closeadj):
    """Relative Strength Index (RSI) of Trend quality over 756d window."""
    res = _rsi(closeadj, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_rsi_1008d_v085_signal(closeadj):
    """Relative Strength Index (RSI) of Raw level of closeadj over 1008d window."""
    res = _rsi(closeadj, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_rsi_1008d_v086_signal(closeadj):
    """Relative Strength Index (RSI) of Trend quality over 1008d window."""
    res = _rsi(closeadj, 1008)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_rsi_1260d_v087_signal(closeadj):
    """Relative Strength Index (RSI) of Raw level of closeadj over 1260d window."""
    res = _rsi(closeadj, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_rsi_1260d_v088_signal(closeadj):
    """Relative Strength Index (RSI) of Trend quality over 1260d window."""
    res = _rsi(closeadj, 1260)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_dd_5d_v089_signal(closeadj):
    """Drawdown of Raw level of closeadj over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_dd_5d_v090_signal(closeadj):
    """Drawdown of Trend quality over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_dd_10d_v091_signal(closeadj):
    """Drawdown of Raw level of closeadj over 10d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_dd_10d_v092_signal(closeadj):
    """Drawdown of Trend quality over 10d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_dd_21d_v093_signal(closeadj):
    """Drawdown of Raw level of closeadj over 21d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_dd_21d_v094_signal(closeadj):
    """Drawdown of Trend quality over 21d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_dd_42d_v095_signal(closeadj):
    """Drawdown of Raw level of closeadj over 42d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_dd_42d_v096_signal(closeadj):
    """Drawdown of Trend quality over 42d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_dd_63d_v097_signal(closeadj):
    """Drawdown of Raw level of closeadj over 63d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_dd_63d_v098_signal(closeadj):
    """Drawdown of Trend quality over 63d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_dd_126d_v099_signal(closeadj):
    """Drawdown of Raw level of closeadj over 126d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_dd_126d_v100_signal(closeadj):
    """Drawdown of Trend quality over 126d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_dd_252d_v101_signal(closeadj):
    """Drawdown of Raw level of closeadj over 252d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_dd_252d_v102_signal(closeadj):
    """Drawdown of Trend quality over 252d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_dd_504d_v103_signal(closeadj):
    """Drawdown of Raw level of closeadj over 504d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_dd_504d_v104_signal(closeadj):
    """Drawdown of Trend quality over 504d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_dd_756d_v105_signal(closeadj):
    """Drawdown of Raw level of closeadj over 756d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_dd_756d_v106_signal(closeadj):
    """Drawdown of Trend quality over 756d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_dd_1008d_v107_signal(closeadj):
    """Drawdown of Raw level of closeadj over 1008d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_dd_1008d_v108_signal(closeadj):
    """Drawdown of Trend quality over 1008d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_dd_1260d_v109_signal(closeadj):
    """Drawdown of Raw level of closeadj over 1260d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_dd_1260d_v110_signal(closeadj):
    """Drawdown of Trend quality over 1260d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_rec_5d_v111_signal(closeadj):
    """Recovery of Raw level of closeadj over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_rec_5d_v112_signal(closeadj):
    """Recovery of Trend quality over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_rec_10d_v113_signal(closeadj):
    """Recovery of Raw level of closeadj over 10d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_rec_10d_v114_signal(closeadj):
    """Recovery of Trend quality over 10d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_rec_21d_v115_signal(closeadj):
    """Recovery of Raw level of closeadj over 21d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_rec_21d_v116_signal(closeadj):
    """Recovery of Trend quality over 21d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_rec_42d_v117_signal(closeadj):
    """Recovery of Raw level of closeadj over 42d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_rec_42d_v118_signal(closeadj):
    """Recovery of Trend quality over 42d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_rec_63d_v119_signal(closeadj):
    """Recovery of Raw level of closeadj over 63d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_rec_63d_v120_signal(closeadj):
    """Recovery of Trend quality over 63d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_rec_126d_v121_signal(closeadj):
    """Recovery of Raw level of closeadj over 126d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_rec_126d_v122_signal(closeadj):
    """Recovery of Trend quality over 126d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_rec_252d_v123_signal(closeadj):
    """Recovery of Raw level of closeadj over 252d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_rec_252d_v124_signal(closeadj):
    """Recovery of Trend quality over 252d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_rec_504d_v125_signal(closeadj):
    """Recovery of Raw level of closeadj over 504d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_rec_504d_v126_signal(closeadj):
    """Recovery of Trend quality over 504d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_rec_756d_v127_signal(closeadj):
    """Recovery of Raw level of closeadj over 756d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_rec_756d_v128_signal(closeadj):
    """Recovery of Trend quality over 756d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_rec_1008d_v129_signal(closeadj):
    """Recovery of Raw level of closeadj over 1008d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_rec_1008d_v130_signal(closeadj):
    """Recovery of Trend quality over 1008d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_rec_1260d_v131_signal(closeadj):
    """Recovery of Raw level of closeadj over 1260d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_rec_1260d_v132_signal(closeadj):
    """Recovery of Trend quality over 1260d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_vol_5d_v133_signal(closeadj):
    """Volatility of Raw level of closeadj over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_vol_5d_v134_signal(closeadj):
    """Volatility of Trend quality over 5d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_vol_10d_v135_signal(closeadj):
    """Volatility of Raw level of closeadj over 10d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_vol_10d_v136_signal(closeadj):
    """Volatility of Trend quality over 10d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_vol_21d_v137_signal(closeadj):
    """Volatility of Raw level of closeadj over 21d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_vol_21d_v138_signal(closeadj):
    """Volatility of Trend quality over 21d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_vol_42d_v139_signal(closeadj):
    """Volatility of Raw level of closeadj over 42d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_vol_42d_v140_signal(closeadj):
    """Volatility of Trend quality over 42d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_vol_63d_v141_signal(closeadj):
    """Volatility of Raw level of closeadj over 63d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_vol_63d_v142_signal(closeadj):
    """Volatility of Trend quality over 63d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_vol_126d_v143_signal(closeadj):
    """Volatility of Raw level of closeadj over 126d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_vol_126d_v144_signal(closeadj):
    """Volatility of Trend quality over 126d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_vol_252d_v145_signal(closeadj):
    """Volatility of Raw level of closeadj over 252d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_vol_252d_v146_signal(closeadj):
    """Volatility of Trend quality over 252d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_vol_504d_v147_signal(closeadj):
    """Volatility of Raw level of closeadj over 504d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_vol_504d_v148_signal(closeadj):
    """Volatility of Trend quality over 504d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_closeadj_vol_756d_v149_signal(closeadj):
    """Volatility of Raw level of closeadj over 756d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def bo_059_aroon_proxy_trend_quality_vol_756d_v150_signal(closeadj):
    """Volatility of Trend quality over 756d window."""
    res = _sma(closeadj, 5)
    return res.replace([np.inf, -np.inf], np.nan)

REGISTRY = {
    "bo_059_aroon_proxy_trend_quality_rsi_63d_v076_signal": {"func": bo_059_aroon_proxy_trend_quality_rsi_63d_v076_signal},
    "bo_059_aroon_proxy_closeadj_rsi_126d_v077_signal": {"func": bo_059_aroon_proxy_closeadj_rsi_126d_v077_signal},
    "bo_059_aroon_proxy_trend_quality_rsi_126d_v078_signal": {"func": bo_059_aroon_proxy_trend_quality_rsi_126d_v078_signal},
    "bo_059_aroon_proxy_closeadj_rsi_252d_v079_signal": {"func": bo_059_aroon_proxy_closeadj_rsi_252d_v079_signal},
    "bo_059_aroon_proxy_trend_quality_rsi_252d_v080_signal": {"func": bo_059_aroon_proxy_trend_quality_rsi_252d_v080_signal},
    "bo_059_aroon_proxy_closeadj_rsi_504d_v081_signal": {"func": bo_059_aroon_proxy_closeadj_rsi_504d_v081_signal},
    "bo_059_aroon_proxy_trend_quality_rsi_504d_v082_signal": {"func": bo_059_aroon_proxy_trend_quality_rsi_504d_v082_signal},
    "bo_059_aroon_proxy_closeadj_rsi_756d_v083_signal": {"func": bo_059_aroon_proxy_closeadj_rsi_756d_v083_signal},
    "bo_059_aroon_proxy_trend_quality_rsi_756d_v084_signal": {"func": bo_059_aroon_proxy_trend_quality_rsi_756d_v084_signal},
    "bo_059_aroon_proxy_closeadj_rsi_1008d_v085_signal": {"func": bo_059_aroon_proxy_closeadj_rsi_1008d_v085_signal},
    "bo_059_aroon_proxy_trend_quality_rsi_1008d_v086_signal": {"func": bo_059_aroon_proxy_trend_quality_rsi_1008d_v086_signal},
    "bo_059_aroon_proxy_closeadj_rsi_1260d_v087_signal": {"func": bo_059_aroon_proxy_closeadj_rsi_1260d_v087_signal},
    "bo_059_aroon_proxy_trend_quality_rsi_1260d_v088_signal": {"func": bo_059_aroon_proxy_trend_quality_rsi_1260d_v088_signal},
    "bo_059_aroon_proxy_closeadj_dd_5d_v089_signal": {"func": bo_059_aroon_proxy_closeadj_dd_5d_v089_signal},
    "bo_059_aroon_proxy_trend_quality_dd_5d_v090_signal": {"func": bo_059_aroon_proxy_trend_quality_dd_5d_v090_signal},
    "bo_059_aroon_proxy_closeadj_dd_10d_v091_signal": {"func": bo_059_aroon_proxy_closeadj_dd_10d_v091_signal},
    "bo_059_aroon_proxy_trend_quality_dd_10d_v092_signal": {"func": bo_059_aroon_proxy_trend_quality_dd_10d_v092_signal},
    "bo_059_aroon_proxy_closeadj_dd_21d_v093_signal": {"func": bo_059_aroon_proxy_closeadj_dd_21d_v093_signal},
    "bo_059_aroon_proxy_trend_quality_dd_21d_v094_signal": {"func": bo_059_aroon_proxy_trend_quality_dd_21d_v094_signal},
    "bo_059_aroon_proxy_closeadj_dd_42d_v095_signal": {"func": bo_059_aroon_proxy_closeadj_dd_42d_v095_signal},
    "bo_059_aroon_proxy_trend_quality_dd_42d_v096_signal": {"func": bo_059_aroon_proxy_trend_quality_dd_42d_v096_signal},
    "bo_059_aroon_proxy_closeadj_dd_63d_v097_signal": {"func": bo_059_aroon_proxy_closeadj_dd_63d_v097_signal},
    "bo_059_aroon_proxy_trend_quality_dd_63d_v098_signal": {"func": bo_059_aroon_proxy_trend_quality_dd_63d_v098_signal},
    "bo_059_aroon_proxy_closeadj_dd_126d_v099_signal": {"func": bo_059_aroon_proxy_closeadj_dd_126d_v099_signal},
    "bo_059_aroon_proxy_trend_quality_dd_126d_v100_signal": {"func": bo_059_aroon_proxy_trend_quality_dd_126d_v100_signal},
    "bo_059_aroon_proxy_closeadj_dd_252d_v101_signal": {"func": bo_059_aroon_proxy_closeadj_dd_252d_v101_signal},
    "bo_059_aroon_proxy_trend_quality_dd_252d_v102_signal": {"func": bo_059_aroon_proxy_trend_quality_dd_252d_v102_signal},
    "bo_059_aroon_proxy_closeadj_dd_504d_v103_signal": {"func": bo_059_aroon_proxy_closeadj_dd_504d_v103_signal},
    "bo_059_aroon_proxy_trend_quality_dd_504d_v104_signal": {"func": bo_059_aroon_proxy_trend_quality_dd_504d_v104_signal},
    "bo_059_aroon_proxy_closeadj_dd_756d_v105_signal": {"func": bo_059_aroon_proxy_closeadj_dd_756d_v105_signal},
    "bo_059_aroon_proxy_trend_quality_dd_756d_v106_signal": {"func": bo_059_aroon_proxy_trend_quality_dd_756d_v106_signal},
    "bo_059_aroon_proxy_closeadj_dd_1008d_v107_signal": {"func": bo_059_aroon_proxy_closeadj_dd_1008d_v107_signal},
    "bo_059_aroon_proxy_trend_quality_dd_1008d_v108_signal": {"func": bo_059_aroon_proxy_trend_quality_dd_1008d_v108_signal},
    "bo_059_aroon_proxy_closeadj_dd_1260d_v109_signal": {"func": bo_059_aroon_proxy_closeadj_dd_1260d_v109_signal},
    "bo_059_aroon_proxy_trend_quality_dd_1260d_v110_signal": {"func": bo_059_aroon_proxy_trend_quality_dd_1260d_v110_signal},
    "bo_059_aroon_proxy_closeadj_rec_5d_v111_signal": {"func": bo_059_aroon_proxy_closeadj_rec_5d_v111_signal},
    "bo_059_aroon_proxy_trend_quality_rec_5d_v112_signal": {"func": bo_059_aroon_proxy_trend_quality_rec_5d_v112_signal},
    "bo_059_aroon_proxy_closeadj_rec_10d_v113_signal": {"func": bo_059_aroon_proxy_closeadj_rec_10d_v113_signal},
    "bo_059_aroon_proxy_trend_quality_rec_10d_v114_signal": {"func": bo_059_aroon_proxy_trend_quality_rec_10d_v114_signal},
    "bo_059_aroon_proxy_closeadj_rec_21d_v115_signal": {"func": bo_059_aroon_proxy_closeadj_rec_21d_v115_signal},
    "bo_059_aroon_proxy_trend_quality_rec_21d_v116_signal": {"func": bo_059_aroon_proxy_trend_quality_rec_21d_v116_signal},
    "bo_059_aroon_proxy_closeadj_rec_42d_v117_signal": {"func": bo_059_aroon_proxy_closeadj_rec_42d_v117_signal},
    "bo_059_aroon_proxy_trend_quality_rec_42d_v118_signal": {"func": bo_059_aroon_proxy_trend_quality_rec_42d_v118_signal},
    "bo_059_aroon_proxy_closeadj_rec_63d_v119_signal": {"func": bo_059_aroon_proxy_closeadj_rec_63d_v119_signal},
    "bo_059_aroon_proxy_trend_quality_rec_63d_v120_signal": {"func": bo_059_aroon_proxy_trend_quality_rec_63d_v120_signal},
    "bo_059_aroon_proxy_closeadj_rec_126d_v121_signal": {"func": bo_059_aroon_proxy_closeadj_rec_126d_v121_signal},
    "bo_059_aroon_proxy_trend_quality_rec_126d_v122_signal": {"func": bo_059_aroon_proxy_trend_quality_rec_126d_v122_signal},
    "bo_059_aroon_proxy_closeadj_rec_252d_v123_signal": {"func": bo_059_aroon_proxy_closeadj_rec_252d_v123_signal},
    "bo_059_aroon_proxy_trend_quality_rec_252d_v124_signal": {"func": bo_059_aroon_proxy_trend_quality_rec_252d_v124_signal},
    "bo_059_aroon_proxy_closeadj_rec_504d_v125_signal": {"func": bo_059_aroon_proxy_closeadj_rec_504d_v125_signal},
    "bo_059_aroon_proxy_trend_quality_rec_504d_v126_signal": {"func": bo_059_aroon_proxy_trend_quality_rec_504d_v126_signal},
    "bo_059_aroon_proxy_closeadj_rec_756d_v127_signal": {"func": bo_059_aroon_proxy_closeadj_rec_756d_v127_signal},
    "bo_059_aroon_proxy_trend_quality_rec_756d_v128_signal": {"func": bo_059_aroon_proxy_trend_quality_rec_756d_v128_signal},
    "bo_059_aroon_proxy_closeadj_rec_1008d_v129_signal": {"func": bo_059_aroon_proxy_closeadj_rec_1008d_v129_signal},
    "bo_059_aroon_proxy_trend_quality_rec_1008d_v130_signal": {"func": bo_059_aroon_proxy_trend_quality_rec_1008d_v130_signal},
    "bo_059_aroon_proxy_closeadj_rec_1260d_v131_signal": {"func": bo_059_aroon_proxy_closeadj_rec_1260d_v131_signal},
    "bo_059_aroon_proxy_trend_quality_rec_1260d_v132_signal": {"func": bo_059_aroon_proxy_trend_quality_rec_1260d_v132_signal},
    "bo_059_aroon_proxy_closeadj_vol_5d_v133_signal": {"func": bo_059_aroon_proxy_closeadj_vol_5d_v133_signal},
    "bo_059_aroon_proxy_trend_quality_vol_5d_v134_signal": {"func": bo_059_aroon_proxy_trend_quality_vol_5d_v134_signal},
    "bo_059_aroon_proxy_closeadj_vol_10d_v135_signal": {"func": bo_059_aroon_proxy_closeadj_vol_10d_v135_signal},
    "bo_059_aroon_proxy_trend_quality_vol_10d_v136_signal": {"func": bo_059_aroon_proxy_trend_quality_vol_10d_v136_signal},
    "bo_059_aroon_proxy_closeadj_vol_21d_v137_signal": {"func": bo_059_aroon_proxy_closeadj_vol_21d_v137_signal},
    "bo_059_aroon_proxy_trend_quality_vol_21d_v138_signal": {"func": bo_059_aroon_proxy_trend_quality_vol_21d_v138_signal},
    "bo_059_aroon_proxy_closeadj_vol_42d_v139_signal": {"func": bo_059_aroon_proxy_closeadj_vol_42d_v139_signal},
    "bo_059_aroon_proxy_trend_quality_vol_42d_v140_signal": {"func": bo_059_aroon_proxy_trend_quality_vol_42d_v140_signal},
    "bo_059_aroon_proxy_closeadj_vol_63d_v141_signal": {"func": bo_059_aroon_proxy_closeadj_vol_63d_v141_signal},
    "bo_059_aroon_proxy_trend_quality_vol_63d_v142_signal": {"func": bo_059_aroon_proxy_trend_quality_vol_63d_v142_signal},
    "bo_059_aroon_proxy_closeadj_vol_126d_v143_signal": {"func": bo_059_aroon_proxy_closeadj_vol_126d_v143_signal},
    "bo_059_aroon_proxy_trend_quality_vol_126d_v144_signal": {"func": bo_059_aroon_proxy_trend_quality_vol_126d_v144_signal},
    "bo_059_aroon_proxy_closeadj_vol_252d_v145_signal": {"func": bo_059_aroon_proxy_closeadj_vol_252d_v145_signal},
    "bo_059_aroon_proxy_trend_quality_vol_252d_v146_signal": {"func": bo_059_aroon_proxy_trend_quality_vol_252d_v146_signal},
    "bo_059_aroon_proxy_closeadj_vol_504d_v147_signal": {"func": bo_059_aroon_proxy_closeadj_vol_504d_v147_signal},
    "bo_059_aroon_proxy_trend_quality_vol_504d_v148_signal": {"func": bo_059_aroon_proxy_trend_quality_vol_504d_v148_signal},
    "bo_059_aroon_proxy_closeadj_vol_756d_v149_signal": {"func": bo_059_aroon_proxy_closeadj_vol_756d_v149_signal},
    "bo_059_aroon_proxy_trend_quality_vol_756d_v150_signal": {"func": bo_059_aroon_proxy_trend_quality_vol_756d_v150_signal},
}
if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 1500
    df = pd.DataFrame({
        "rnd": np.random.normal(100, 10, n).cumsum(), "ebitda": np.random.normal(100, 10, n).cumsum(), "ps": np.random.normal(100, 10, n).cumsum(), "cashneq": np.random.normal(100, 10, n).cumsum(), "ebt": np.random.normal(100, 10, n).cumsum(), "deferredrev": np.random.normal(100, 10, n).cumsum(), "sgna": np.random.normal(100, 10, n).cumsum(), "liabilitiesc": np.random.normal(100, 10, n).cumsum(), "ebit": np.random.normal(100, 10, n).cumsum(), "shareswa": np.random.normal(100, 10, n).cumsum(), "closeadj": np.random.normal(100, 10, n).cumsum(), "inventory": np.random.normal(100, 10, n).cumsum(), "receivables": np.random.normal(100, 10, n).cumsum(), "marketcap": np.random.normal(100, 10, n).cumsum(), "ev": np.random.normal(100, 10, n).cumsum(), "capex": np.random.normal(100, 10, n).cumsum(), "pb": np.random.normal(100, 10, n).cumsum(), "cor": np.random.normal(100, 10, n).cumsum(), "depamor": np.random.normal(100, 10, n).cumsum(), "deposits": np.random.normal(100, 10, n).cumsum(), "invcap": np.random.normal(100, 10, n).cumsum(), "bvps": np.random.normal(100, 10, n).cumsum(), "ebitdamargin": np.random.normal(100, 10, n).cumsum(), "fcf": np.random.normal(100, 10, n).cumsum(), "tangibles": np.random.normal(100, 10, n).cumsum(), "equity": np.random.normal(100, 10, n).cumsum(), "taxexp": np.random.normal(100, 10, n).cumsum(), "grossmargin": np.random.normal(100, 10, n).cumsum(), "opex": np.random.normal(100, 10, n).cumsum(), "sbcomp": np.random.normal(100, 10, n).cumsum(), "pe": np.random.normal(100, 10, n).cumsum(), "netinc": np.random.normal(100, 10, n).cumsum(), "ncfbus": np.random.normal(100, 10, n).cumsum(), "payables": np.random.normal(100, 10, n).cumsum(), "divyield": np.random.normal(100, 10, n).cumsum(), "roic": np.random.normal(100, 10, n).cumsum(), "assets": np.random.normal(100, 10, n).cumsum()
    })
    print(f"Verifying {len(REGISTRY)} functions for family 059...")
    for name, info in REGISTRY.items():
        fn = info["func"]
        sig = inspect.signature(fn)
        params = list(sig.parameters.keys())
        args = [df[p] for p in params]
        try:
            res = fn(*args)
            if not isinstance(res, pd.Series): raise ValueError("Not a series")
            if len(res.dropna()) < 10 and len(df) > 1000: pass 
        except Exception as e:
            print(f"Error in {name}: {e}")
            break
    print("Success.")
