import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 5)).mean()
def _ema(s, w): return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()
def _min(s, w): return s.rolling(w, min_periods=min(w, 5)).min()
def _max(s, w): return s.rolling(w, min_periods=min(w, 5)).max()

def _rsi(c, w):
    delta = c.diff()
    gain = (delta.where(delta > 0, 0)).rolling(w).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(w).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs).replace(0, np.nan))

def _stoch(h, l, c, w):
    lw = l.rolling(w).min()
    hw = h.rolling(w).max()
    return (c - lw) / (hw - lw).abs().replace(0, np.nan)

def _osc_zscore(osc, w):
    return (osc - osc.rolling(w).mean()) / osc.rolling(w).std().replace(0, np.nan)

def _williams_r(h, l, c, w):
    hw = h.rolling(w).max()
    lw = l.rolling(w).min()
    return (hw - c) / (hw - lw).abs().replace(0, np.nan) * -100

def _cci(h, l, c, w):
    tp = (h + l + c) / 3
    ma = _sma(tp, w)
    md = tp.rolling(w).apply(lambda x: np.abs(x - x.mean()).mean(), raw=True)
    return (tp - ma) / (0.015 * md).replace(0, np.nan)

# RSI Z-score Features (v076-v090)

# RSI 5-day Z-score base oscillator
def f12osc_rsi_zscore_5d_base_v076_signal(close: pd.Series) -> pd.Series:
    rsi = _rsi(close, 5)
    res = _osc_zscore(rsi, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 10-day Z-score base oscillator
def f12osc_rsi_zscore_10d_base_v077_signal(close: pd.Series) -> pd.Series:
    rsi = _rsi(close, 10)
    res = _osc_zscore(rsi, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 14-day Z-score base oscillator
def f12osc_rsi_zscore_14d_base_v078_signal(close: pd.Series) -> pd.Series:
    rsi = _rsi(close, 14)
    res = _osc_zscore(rsi, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 21-day Z-score base oscillator
def f12osc_rsi_zscore_21d_base_v079_signal(close: pd.Series) -> pd.Series:
    rsi = _rsi(close, 21)
    res = _osc_zscore(rsi, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 42-day Z-score base oscillator using closeadj
def f12osc_rsi_zscore_42d_base_v080_signal(closeadj: pd.Series) -> pd.Series:
    rsi = _rsi(closeadj, 42)
    res = _osc_zscore(rsi, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 63-day Z-score base oscillator using closeadj
def f12osc_rsi_zscore_63d_base_v081_signal(closeadj: pd.Series) -> pd.Series:
    rsi = _rsi(closeadj, 63)
    res = _osc_zscore(rsi, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 126-day Z-score base oscillator using closeadj
def f12osc_rsi_zscore_126d_base_v082_signal(closeadj: pd.Series) -> pd.Series:
    rsi = _rsi(closeadj, 126)
    res = _osc_zscore(rsi, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 252-day Z-score base oscillator using closeadj
def f12osc_rsi_zscore_252d_base_v083_signal(closeadj: pd.Series) -> pd.Series:
    rsi = _rsi(closeadj, 252)
    res = _osc_zscore(rsi, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 3-day Z-score base oscillator
def f12osc_rsi_zscore_3d_base_v084_signal(close: pd.Series) -> pd.Series:
    rsi = _rsi(close, 3)
    res = _osc_zscore(rsi, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 8-day Z-score base oscillator
def f12osc_rsi_zscore_8d_base_v085_signal(close: pd.Series) -> pd.Series:
    rsi = _rsi(close, 8)
    res = _osc_zscore(rsi, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 34-day Z-score base oscillator using closeadj
def f12osc_rsi_zscore_34d_base_v086_signal(closeadj: pd.Series) -> pd.Series:
    rsi = _rsi(closeadj, 34)
    res = _osc_zscore(rsi, 34)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 55-day Z-score base oscillator using closeadj
def f12osc_rsi_zscore_55d_base_v087_signal(closeadj: pd.Series) -> pd.Series:
    rsi = _rsi(closeadj, 55)
    res = _osc_zscore(rsi, 55)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 89-day Z-score base oscillator using closeadj
def f12osc_rsi_zscore_89d_base_v088_signal(closeadj: pd.Series) -> pd.Series:
    rsi = _rsi(closeadj, 89)
    res = _osc_zscore(rsi, 89)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 144-day Z-score base oscillator using closeadj
def f12osc_rsi_zscore_144d_base_v089_signal(closeadj: pd.Series) -> pd.Series:
    rsi = _rsi(closeadj, 144)
    res = _osc_zscore(rsi, 144)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 233-day Z-score base oscillator using closeadj
def f12osc_rsi_zscore_233d_base_v090_signal(closeadj: pd.Series) -> pd.Series:
    rsi = _rsi(closeadj, 233)
    res = _osc_zscore(rsi, 233)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K Z-score Features (v091-v105)

# Stochastic %K 5-day Z-score base oscillator
def f12osc_stoch_k_zscore_5d_base_v091_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch(high, low, close, 5)
    res = _osc_zscore(k, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 10-day Z-score base oscillator
def f12osc_stoch_k_zscore_10d_base_v092_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch(high, low, close, 10)
    res = _osc_zscore(k, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 14-day Z-score base oscillator
def f12osc_stoch_k_zscore_14d_base_v093_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch(high, low, close, 14)
    res = _osc_zscore(k, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 21-day Z-score base oscillator
def f12osc_stoch_k_zscore_21d_base_v094_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch(high, low, close, 21)
    res = _osc_zscore(k, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 42-day Z-score base oscillator using closeadj
def f12osc_stoch_k_zscore_42d_base_v095_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 42)
    res = _osc_zscore(k, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 63-day Z-score base oscillator using closeadj
def f12osc_stoch_k_zscore_63d_base_v096_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 63)
    res = _osc_zscore(k, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 126-day Z-score base oscillator using closeadj
def f12osc_stoch_k_zscore_126d_base_v097_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 126)
    res = _osc_zscore(k, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 252-day Z-score base oscillator using closeadj
def f12osc_stoch_k_zscore_252d_base_v098_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 252)
    res = _osc_zscore(k, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 3-day Z-score base oscillator
def f12osc_stoch_k_zscore_3d_base_v099_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch(high, low, close, 3)
    res = _osc_zscore(k, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 8-day Z-score base oscillator
def f12osc_stoch_k_zscore_8d_base_v100_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch(high, low, close, 8)
    res = _osc_zscore(k, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 34-day Z-score base oscillator using closeadj
def f12osc_stoch_k_zscore_34d_base_v101_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 34)
    res = _osc_zscore(k, 34)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 55-day Z-score base oscillator using closeadj
def f12osc_stoch_k_zscore_55d_base_v102_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 55)
    res = _osc_zscore(k, 55)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 89-day Z-score base oscillator using closeadj
def f12osc_stoch_k_zscore_89d_base_v103_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 89)
    res = _osc_zscore(k, 89)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 144-day Z-score base oscillator using closeadj
def f12osc_stoch_k_zscore_144d_base_v104_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 144)
    res = _osc_zscore(k, 144)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 233-day Z-score base oscillator using closeadj
def f12osc_stoch_k_zscore_233d_base_v105_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 233)
    res = _osc_zscore(k, 233)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI Z-score Features (v106-v120)

# CCI 5-day Z-score base oscillator
def f12osc_cci_zscore_5d_base_v106_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    cci = _cci(high, low, close, 5)
    res = _osc_zscore(cci, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 10-day Z-score base oscillator
def f12osc_cci_zscore_10d_base_v107_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    cci = _cci(high, low, close, 10)
    res = _osc_zscore(cci, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 14-day Z-score base oscillator
def f12osc_cci_zscore_14d_base_v108_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    cci = _cci(high, low, close, 14)
    res = _osc_zscore(cci, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 21-day Z-score base oscillator
def f12osc_cci_zscore_21d_base_v109_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    cci = _cci(high, low, close, 21)
    res = _osc_zscore(cci, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 42-day Z-score base oscillator using closeadj
def f12osc_cci_zscore_42d_base_v110_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    cci = _cci(high * adj, low * adj, closeadj, 42)
    res = _osc_zscore(cci, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 63-day Z-score base oscillator using closeadj
def f12osc_cci_zscore_63d_base_v111_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    cci = _cci(high * adj, low * adj, closeadj, 63)
    res = _osc_zscore(cci, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 126-day Z-score base oscillator using closeadj
def f12osc_cci_zscore_126d_base_v112_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    cci = _cci(high * adj, low * adj, closeadj, 126)
    res = _osc_zscore(cci, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 252-day Z-score base oscillator using closeadj
def f12osc_cci_zscore_252d_base_v113_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    cci = _cci(high * adj, low * adj, closeadj, 252)
    res = _osc_zscore(cci, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 3-day Z-score base oscillator
def f12osc_cci_zscore_3d_base_v114_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    cci = _cci(high, low, close, 3)
    res = _osc_zscore(cci, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 8-day Z-score base oscillator
def f12osc_cci_zscore_8d_base_v115_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    cci = _cci(high, low, close, 8)
    res = _osc_zscore(cci, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 34-day Z-score base oscillator using closeadj
def f12osc_cci_zscore_34d_base_v116_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    cci = _cci(high * adj, low * adj, closeadj, 34)
    res = _osc_zscore(cci, 34)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 55-day Z-score base oscillator using closeadj
def f12osc_cci_zscore_55d_base_v117_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    cci = _cci(high * adj, low * adj, closeadj, 55)
    res = _osc_zscore(cci, 55)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 89-day Z-score base oscillator using closeadj
def f12osc_cci_zscore_89d_base_v118_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    cci = _cci(high * adj, low * adj, closeadj, 89)
    res = _osc_zscore(cci, 89)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 144-day Z-score base oscillator using closeadj
def f12osc_cci_zscore_144d_base_v119_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    cci = _cci(high * adj, low * adj, closeadj, 144)
    res = _osc_zscore(cci, 144)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 233-day Z-score base oscillator using closeadj
def f12osc_cci_zscore_233d_base_v120_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    cci = _cci(high * adj, low * adj, closeadj, 233)
    res = _osc_zscore(cci, 233)
    return res.replace([np.inf, -np.inf], np.nan)

# Ultimate Oscillator Style Features (v121-v135)

# Ultimate Oscillator Style (7, 14, 28) base oscillator
def f12osc_ultimate_style_7_14_28_base_v121_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    def _avg(h, l, c, w):
        bp = c - _min(l, w)
        tr = _max(h, w) - _min(l, w)
        return _sma(bp, w) / _sma(tr, w).replace(0, np.nan)
    res = (4 * _avg(high, low, close, 7) + 2 * _avg(high, low, close, 14) + _avg(high, low, close, 28)) / 7
    return res.replace([np.inf, -np.inf], np.nan)

# Ultimate Oscillator Style (5, 10, 20) base oscillator
def f12osc_ultimate_style_5_10_20_base_v122_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    def _avg(h, l, c, w):
        bp = c - _min(l, w)
        tr = _max(h, w) - _min(l, w)
        return _sma(bp, w) / _sma(tr, w).replace(0, np.nan)
    res = (4 * _avg(high, low, close, 5) + 2 * _avg(high, low, close, 10) + _avg(high, low, close, 20)) / 7
    return res.replace([np.inf, -np.inf], np.nan)

# Ultimate Oscillator Style (10, 20, 40) base oscillator using closeadj
def f12osc_ultimate_style_10_20_40_base_v123_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    def _avg(h, l, c, w):
        bp = c - _min(l, w)
        tr = _max(h, w) - _min(l, w)
        return _sma(bp, w) / _sma(tr, w).replace(0, np.nan)
    res = (4 * _avg(high*adj, low*adj, closeadj, 10) + 2 * _avg(high*adj, low*adj, closeadj, 20) + _avg(high*adj, low*adj, closeadj, 40)) / 7
    return res.replace([np.inf, -np.inf], np.nan)

# Ultimate Oscillator Style (20, 40, 80) base oscillator using closeadj
def f12osc_ultimate_style_20_40_80_base_v124_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    def _avg(h, l, c, w):
        bp = c - _min(l, w)
        tr = _max(h, w) - _min(l, w)
        return _sma(bp, w) / _sma(tr, w).replace(0, np.nan)
    res = (4 * _avg(high*adj, low*adj, closeadj, 20) + 2 * _avg(high*adj, low*adj, closeadj, 40) + _avg(high*adj, low*adj, closeadj, 80)) / 7
    return res.replace([np.inf, -np.inf], np.nan)

# Ultimate Oscillator Style (40, 80, 160) base oscillator using closeadj
def f12osc_ultimate_style_40_80_160_base_v125_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    def _avg(h, l, c, w):
        bp = c - _min(l, w)
        tr = _max(h, w) - _min(l, w)
        return _sma(bp, w) / _sma(tr, w).replace(0, np.nan)
    res = (4 * _avg(high*adj, low*adj, closeadj, 40) + 2 * _avg(high*adj, low*adj, closeadj, 80) + _avg(high*adj, low*adj, closeadj, 160)) / 7
    return res.replace([np.inf, -np.inf], np.nan)

# Ultimate Oscillator Style (2, 4, 8) base oscillator
def f12osc_ultimate_style_2_4_8_base_v126_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    def _avg(h, l, c, w):
        bp = c - _min(l, w)
        tr = _max(h, w) - _min(l, w)
        return _sma(bp, w) / _sma(tr, w).replace(0, np.nan)
    res = (4 * _avg(high, low, close, 2) + 2 * _avg(high, low, close, 4) + _avg(high, low, close, 8)) / 7
    return res.replace([np.inf, -np.inf], np.nan)

# Ultimate Oscillator Style (63, 126, 252) base oscillator using closeadj
def f12osc_ultimate_style_63_126_252_base_v127_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    def _avg(h, l, c, w):
        bp = c - _min(l, w)
        tr = _max(h, w) - _min(l, w)
        return _sma(bp, w) / _sma(tr, w).replace(0, np.nan)
    res = (4 * _avg(high*adj, low*adj, closeadj, 63) + 2 * _avg(high*adj, low*adj, closeadj, 126) + _avg(high*adj, low*adj, closeadj, 252)) / 7
    return res.replace([np.inf, -np.inf], np.nan)

# Ultimate Oscillator Style (14, 28, 56) base oscillator using closeadj
def f12osc_ultimate_style_14_28_56_base_v128_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    def _avg(h, l, c, w):
        bp = c - _min(l, w)
        tr = _max(h, w) - _min(l, w)
        return _sma(bp, w) / _sma(tr, w).replace(0, np.nan)
    res = (4 * _avg(high*adj, low*adj, closeadj, 14) + 2 * _avg(high*adj, low*adj, closeadj, 28) + _avg(high*adj, low*adj, closeadj, 56)) / 7
    return res.replace([np.inf, -np.inf], np.nan)

# Ultimate Oscillator Style (3, 6, 12) base oscillator
def f12osc_ultimate_style_3_6_12_base_v129_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    def _avg(h, l, c, w):
        bp = c - _min(l, w)
        tr = _max(h, w) - _min(l, w)
        return _sma(bp, w) / _sma(tr, w).replace(0, np.nan)
    res = (4 * _avg(high, low, close, 3) + 2 * _avg(high, low, close, 6) + _avg(high, low, close, 12)) / 7
    return res.replace([np.inf, -np.inf], np.nan)

# Ultimate Oscillator Style (8, 16, 32) base oscillator using closeadj
def f12osc_ultimate_style_8_16_32_base_v130_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    def _avg(h, l, c, w):
        bp = c - _min(l, w)
        tr = _max(h, w) - _min(l, w)
        return _sma(bp, w) / _sma(tr, w).replace(0, np.nan)
    res = (4 * _avg(high*adj, low*adj, closeadj, 8) + 2 * _avg(high*adj, low*adj, closeadj, 16) + _avg(high*adj, low*adj, closeadj, 32)) / 7
    return res.replace([np.inf, -np.inf], np.nan)

# Ultimate Oscillator Style (12, 24, 48) base oscillator using closeadj
def f12osc_ultimate_style_12_24_48_base_v131_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    def _avg(h, l, c, w):
        bp = c - _min(l, w)
        tr = _max(h, w) - _min(l, w)
        return _sma(bp, w) / _sma(tr, w).replace(0, np.nan)
    res = (4 * _avg(high*adj, low*adj, closeadj, 12) + 2 * _avg(high*adj, low*adj, closeadj, 24) + _avg(high*adj, low*adj, closeadj, 48)) / 7
    return res.replace([np.inf, -np.inf], np.nan)

# Ultimate Oscillator Style (15, 30, 60) base oscillator using closeadj
def f12osc_ultimate_style_15_30_60_base_v132_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    def _avg(h, l, c, w):
        bp = c - _min(l, w)
        tr = _max(h, w) - _min(l, w)
        return _sma(bp, w) / _sma(tr, w).replace(0, np.nan)
    res = (4 * _avg(high*adj, low*adj, closeadj, 15) + 2 * _avg(high*adj, low*adj, closeadj, 30) + _avg(high*adj, low*adj, closeadj, 60)) / 7
    return res.replace([np.inf, -np.inf], np.nan)

# Ultimate Oscillator Style (18, 36, 72) base oscillator using closeadj
def f12osc_ultimate_style_18_36_72_base_v133_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    def _avg(h, l, c, w):
        bp = c - _min(l, w)
        tr = _max(h, w) - _min(l, w)
        return _sma(bp, w) / _sma(tr, w).replace(0, np.nan)
    res = (4 * _avg(high*adj, low*adj, closeadj, 18) + 2 * _avg(high*adj, low*adj, closeadj, 36) + _avg(high*adj, low*adj, closeadj, 72)) / 7
    return res.replace([np.inf, -np.inf], np.nan)

# Ultimate Oscillator Style (25, 50, 100) base oscillator using closeadj
def f12osc_ultimate_style_25_50_100_base_v134_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    def _avg(h, l, c, w):
        bp = c - _min(l, w)
        tr = _max(h, w) - _min(l, w)
        return _sma(bp, w) / _sma(tr, w).replace(0, np.nan)
    res = (4 * _avg(high*adj, low*adj, closeadj, 25) + 2 * _avg(high*adj, low*adj, closeadj, 50) + _avg(high*adj, low*adj, closeadj, 100)) / 7
    return res.replace([np.inf, -np.inf], np.nan)

# Ultimate Oscillator Style (30, 60, 120) base oscillator using closeadj
def f12osc_ultimate_style_30_60_120_base_v135_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    def _avg(h, l, c, w):
        bp = c - _min(l, w)
        tr = _max(h, w) - _min(l, w)
        return _sma(bp, w) / _sma(tr, w).replace(0, np.nan)
    res = (4 * _avg(high*adj, low*adj, closeadj, 30) + 2 * _avg(high*adj, low*adj, closeadj, 60) + _avg(high*adj, low*adj, closeadj, 120)) / 7
    return res.replace([np.inf, -np.inf], np.nan)

# Crossing and Divergence Proxy Features (v136-v150)

# RSI 14 crossing 50 proxy base feature
def f12osc_rsi14_cross_50_base_v136_signal(close: pd.Series) -> pd.Series:
    rsi = _rsi(close, 14)
    res = (rsi - 50) / 100.0
    return res.replace([np.inf, -np.inf], np.nan)

# Stoch 14 crossing 0.5 proxy base feature
def f12osc_stoch14_cross_50_base_v137_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch(high, low, close, 14)
    res = k - 0.5
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 20 crossing 0 proxy base feature
def f12osc_cci20_cross_0_base_v138_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    cci = _cci(high, low, close, 20)
    res = cci / 100.0
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence proxy: RSI 14 ROC minus Stoch 14 ROC
def f12osc_rsi14_stoch14_divergence_v139_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rsi_roc = _rsi(close, 14).diff(5)
    stoch_roc = _stoch(high, low, close, 14).diff(5)
    res = rsi_roc - stoch_roc
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence proxy: RSI 14 ROC minus Price ROC
def f12osc_rsi14_price_divergence_v140_signal(close: pd.Series) -> pd.Series:
    rsi_roc = _rsi(close, 14).diff(5)
    price_roc = close.pct_change(5)
    res = rsi_roc - price_roc
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence proxy: Stoch 14 ROC minus Price ROC
def f12osc_stoch14_price_divergence_v141_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    stoch_roc = _stoch(high, low, close, 14).diff(5)
    price_roc = close.pct_change(5)
    res = stoch_roc - price_roc
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence proxy: CCI 20 ROC minus Price ROC
def f12osc_cci20_price_divergence_v142_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    cci_roc = _cci(high, low, close, 20).diff(5)
    price_roc = close.pct_change(5)
    res = cci_roc - price_roc
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence proxy: RSI 21 ROC minus Price ROC
def f12osc_rsi21_price_divergence_v143_signal(close: pd.Series) -> pd.Series:
    rsi_roc = _rsi(close, 21).diff(5)
    price_roc = close.pct_change(5)
    res = rsi_roc - price_roc
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence proxy: Stoch 21 ROC minus Price ROC
def f12osc_stoch21_price_divergence_v144_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    stoch_roc = _stoch(high, low, close, 21).diff(5)
    price_roc = close.pct_change(5)
    res = stoch_roc - price_roc
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence proxy: CCI 40 ROC minus Price ROC using closeadj
def f12osc_cci40_price_divergence_v145_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    cci_roc = _cci(high * adj, low * adj, closeadj, 40).diff(21)
    price_roc = closeadj.pct_change(21)
    res = cci_roc - price_roc
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence proxy: RSI 63 ROC minus Price ROC using closeadj
def f12osc_rsi63_price_divergence_v146_signal(closeadj: pd.Series) -> pd.Series:
    rsi_roc = _rsi(closeadj, 63).diff(21)
    price_roc = closeadj.pct_change(21)
    res = rsi_roc - price_roc
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence proxy: Stoch 63 ROC minus Price ROC using closeadj
def f12osc_stoch63_price_divergence_v147_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    stoch_roc = _stoch(high * adj, low * adj, closeadj, 63).diff(21)
    price_roc = closeadj.pct_change(21)
    res = stoch_roc - price_roc
    return res.replace([np.inf, -np.inf], np.nan)

# Difference between RSI 14 and Stoch %K 14
def f12osc_rsi14_stoch_k_diff_v148_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rsi = _rsi(close, 14)
    stoch_k = _stoch(high, low, close, 14) * 100
    res = rsi - stoch_k
    return res.replace([np.inf, -np.inf], np.nan)

# Difference between RSI 21 and Stoch %K 21
def f12osc_rsi21_stoch_k_diff_v149_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rsi = _rsi(close, 21)
    stoch_k = _stoch(high, low, close, 21) * 100
    res = rsi - stoch_k
    return res.replace([np.inf, -np.inf], np.nan)

# Difference between RSI 63 and Stoch %K 63 using closeadj
def f12osc_rsi63_stoch_k_diff_v150_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    rsi = _rsi(closeadj, 63)
    stoch_k = _stoch(high * adj, low * adj, closeadj, 63) * 100
    res = rsi - stoch_k
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

BASE_NAMES = [f for f in globals() if f.startswith("f12osc_") and f.endswith("_signal")]

F12_OSCILLATOR_FAMILY_BASE_REGISTRY_076_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES)
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 500; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "high": np.random.randn(sz).cumsum()+110, "low": np.random.randn(sz).cumsum()+90, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F12_OSCILLATOR_FAMILY_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 076-150 OK")
