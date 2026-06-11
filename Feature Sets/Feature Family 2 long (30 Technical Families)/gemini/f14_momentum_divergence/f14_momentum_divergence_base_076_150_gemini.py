# f14_momentum_divergence_base_076_150_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _ema(s, w):
    return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()

def _roc(s, w):
    return s.pct_change(w)

def _min(s, w):
    return s.rolling(w, min_periods=min(w, 5)).min()

def _max(s, w):
    return s.rolling(w, min_periods=min(w, 5)).max()

def _stoch_k(h, l, c, w):
    low_min = _min(l, w)
    high_max = _max(h, w)
    return 100 * (c - low_min) / (high_max - low_min).replace(0, np.nan)

def _rsi(s, w):
    delta = s.diff()
    gain = (delta.where(delta > 0, 0)).rolling(w).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(w).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))

def _macd(s, fast=12, slow=26):
    return _ema(s, fast) - _ema(s, slow)

def _mom_div(price_roc, mom_roc):
    return (price_roc - mom_roc) / mom_roc.abs().replace(0, np.nan)

def _mom_drift(mom, w):
    return (mom - mom.rolling(w).mean()) / mom.rolling(w).std().replace(0, np.nan)

def _mom_corr(price_roc, mom_roc, w):
    return price_roc.rolling(w).corr(mom_roc)

# --- Stochastic Divergence Features (v076 - v090) ---

# Divergence between 5d Price ROC and 5d Stochastic K ROC
def f14md_f14_momentum_divergence_stoch_div_5d_v076_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p_roc = _roc(close, 5)
    m_roc = _roc(_stoch_k(high, low, close, 14), 5)
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 21d Price ROC and 21d Stochastic K ROC
def f14md_f14_momentum_divergence_stoch_div_21d_v077_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p_roc = _roc(close, 21)
    m_roc = _roc(_stoch_k(high, low, close, 14), 21)
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 63d Price ROC and 63d Stochastic K ROC
def f14md_f14_momentum_divergence_stoch_div_63d_v078_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    p_roc = _roc(closeadj, 63)
    m_roc = _roc(_stoch_k(high * adj, low * adj, closeadj, 14), 63)
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of 14d Stochastic K from its 21d mean
def f14md_f14_momentum_divergence_stoch_drift_21d_v079_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    m = _stoch_k(high, low, close, 14)
    res = _mom_drift(m, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of 14d Stochastic K from its 63d mean
def f14md_f14_momentum_divergence_stoch_drift_63d_v080_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    m = _stoch_k(high * adj, low * adj, closeadj, 14)
    res = _mom_drift(m, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between 5d Price ROC and 5d Stoch K ROC over 21d
def f14md_f14_momentum_divergence_stoch_corr_5d_21w_v081_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p_roc = _roc(close, 5)
    m_roc = _roc(_stoch_k(high, low, close, 14), 5)
    res = _mom_corr(p_roc, m_roc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between 21d Price ROC and 21d Stoch K ROC over 63d
def f14md_f14_momentum_divergence_stoch_corr_21d_63w_v082_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    p_roc = _roc(closeadj, 21)
    m_roc = _roc(_stoch_k(high * adj, low * adj, closeadj, 14), 21)
    res = _mom_corr(p_roc, m_roc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 10d Price ROC and 10d Stochastic D (3-period SMA of K) ROC
def f14md_f14_momentum_divergence_stoch_d_div_10d_v083_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch_k(high, low, close, 14)
    d = _sma(k, 3)
    res = _mom_div(_roc(close, 10), _roc(d, 10))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 63d Price ROC and 63d Stochastic D ROC
def f14md_f14_momentum_divergence_stoch_d_div_63d_v084_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch_k(high * adj, low * adj, closeadj, 14)
    d = _sma(k, 3)
    res = _mom_div(_roc(closeadj, 63), _roc(d, 63))
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of Stochastic D from its 126d mean
def f14md_f14_momentum_divergence_stoch_d_drift_126d_v085_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch_k(high * adj, low * adj, closeadj, 14)
    d = _sma(k, 3)
    res = _mom_drift(d, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between Price and Stochastic K over 126d
def f14md_f14_momentum_divergence_price_stoch_corr_126w_v086_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch_k(high * adj, low * adj, closeadj, 14)
    res = _mom_corr(closeadj, k, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 5d Price ROC and 5d Stoch K (7-period) ROC
def f14md_f14_momentum_divergence_stoch7_div_5d_v087_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p_roc = _roc(close, 5)
    m_roc = _roc(_stoch_k(high, low, close, 7), 5)
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 21d Price ROC and 21d Stoch K (21-period) ROC
def f14md_f14_momentum_divergence_stoch21_div_21d_v088_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p_roc = _roc(close, 21)
    m_roc = _roc(_stoch_k(high, low, close, 21), 21)
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of 21-period Stochastic K from its 63d mean
def f14md_f14_momentum_divergence_stoch21_drift_63d_v089_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    m = _stoch_k(high * adj, low * adj, closeadj, 21)
    res = _mom_drift(m, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between 21d Price ROC and 21d Stoch K (21-period) ROC over 126d
def f14md_f14_momentum_divergence_stoch21_corr_21d_126w_v090_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    p_roc = _roc(closeadj, 21)
    m_roc = _roc(_stoch_k(high * adj, low * adj, closeadj, 21), 21)
    res = _mom_corr(p_roc, m_roc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Raw Momentum Divergence (v091 - v105) ---

# Divergence between 5d Price ROC and 5d (Close - Close[10]) ROC
def f14md_f14_momentum_divergence_raw_mom_div_5d_v091_signal(close: pd.Series) -> pd.Series:
    raw_mom = close - close.shift(10)
    res = _mom_div(_roc(close, 5), _roc(raw_mom, 5))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 21d Price ROC and 21d (Close - Close[21]) ROC
def f14md_f14_momentum_divergence_raw_mom_div_21d_v092_signal(close: pd.Series) -> pd.Series:
    raw_mom = close - close.shift(21)
    res = _mom_div(_roc(close, 21), _roc(raw_mom, 21))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 63d Price ROC and 63d (Closeadj - Closeadj[63]) ROC
def f14md_f14_momentum_divergence_raw_mom_div_63d_v093_signal(closeadj: pd.Series) -> pd.Series:
    raw_mom = closeadj - closeadj.shift(63)
    res = _mom_div(_roc(closeadj, 63), _roc(raw_mom, 63))
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of (Close - Close[10]) from its 21d mean
def f14md_f14_momentum_divergence_raw_mom_drift_21d_v094_signal(close: pd.Series) -> pd.Series:
    raw_mom = close - close.shift(10)
    res = _mom_drift(raw_mom, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of (Closeadj - Closeadj[63]) from its 126d mean
def f14md_f14_momentum_divergence_raw_mom_drift_126d_v095_signal(closeadj: pd.Series) -> pd.Series:
    raw_mom = closeadj - closeadj.shift(63)
    res = _mom_drift(raw_mom, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between 5d Price ROC and 5d (Close - Close[10]) ROC over 21d
def f14md_f14_momentum_divergence_raw_mom_corr_5d_21w_v096_signal(close: pd.Series) -> pd.Series:
    raw_mom = close - close.shift(10)
    res = _mom_corr(_roc(close, 5), _roc(raw_mom, 5), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between 21d Price ROC and 21d (Closeadj - Closeadj[21]) ROC over 63d
def f14md_f14_momentum_divergence_raw_mom_corr_21d_63w_v097_signal(closeadj: pd.Series) -> pd.Series:
    raw_mom = closeadj - closeadj.shift(21)
    res = _mom_corr(_roc(closeadj, 21), _roc(raw_mom, 21), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 10d Price ROC and 10d (Close - SMA(Close, 10)) ROC
def f14md_f14_momentum_divergence_sma_diff_div_10d_v098_signal(close: pd.Series) -> pd.Series:
    m = close - _sma(close, 10)
    res = _mom_div(_roc(close, 10), _roc(m, 10))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 63d Price ROC and 63d (Closeadj - SMA(Closeadj, 63)) ROC
def f14md_f14_momentum_divergence_sma_diff_div_63d_v099_signal(closeadj: pd.Series) -> pd.Series:
    m = closeadj - _sma(closeadj, 63)
    res = _mom_div(_roc(closeadj, 63), _roc(m, 63))
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of (Closeadj - SMA(Closeadj, 252)) from its 252d mean
def f14md_f14_momentum_divergence_sma_diff_drift_252d_v100_signal(closeadj: pd.Series) -> pd.Series:
    m = closeadj - _sma(closeadj, 252)
    res = _mom_drift(m, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between Price and (Closeadj - SMA(Closeadj, 63)) over 63d
def f14md_f14_momentum_divergence_price_sma_diff_corr_63w_v101_signal(closeadj: pd.Series) -> pd.Series:
    m = closeadj - _sma(closeadj, 63)
    res = _mom_corr(closeadj, m, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 5d Price ROC and 5d (Close - EMA(Close, 5)) ROC
def f14md_f14_momentum_divergence_ema_diff_div_5d_v102_signal(close: pd.Series) -> pd.Series:
    m = close - _ema(close, 5)
    res = _mom_div(_roc(close, 5), _roc(m, 5))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 21d Price ROC and 21d (Closeadj - EMA(Closeadj, 21)) ROC
def f14md_f14_momentum_divergence_ema_diff_div_21d_v103_signal(closeadj: pd.Series) -> pd.Series:
    m = closeadj - _ema(closeadj, 21)
    res = _mom_div(_roc(closeadj, 21), _roc(m, 21))
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of (Closeadj - EMA(Closeadj, 63)) from its 126d mean
def f14md_f14_momentum_divergence_ema_diff_drift_126d_v104_signal(closeadj: pd.Series) -> pd.Series:
    m = closeadj - _ema(closeadj, 63)
    res = _mom_drift(m, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between Price and (Closeadj - EMA(Closeadj, 126)) over 126d
def f14md_f14_momentum_divergence_price_ema_diff_corr_126w_v105_signal(closeadj: pd.Series) -> pd.Series:
    m = closeadj - _ema(closeadj, 126)
    res = _mom_corr(closeadj, m, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Multi-Indicator Divergence (v106 - v120) ---

# Divergence between RSI ROC and MACD ROC
def f14md_f14_momentum_divergence_rsi_macd_div_5d_v106_signal(close: pd.Series) -> pd.Series:
    r_roc = _roc(_rsi(close, 14), 5)
    m_roc = _roc(_macd(close), 5)
    res = _mom_div(r_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between RSI ROC and Stoch K ROC
def f14md_f14_momentum_divergence_rsi_stoch_div_21d_v107_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    r_roc = _roc(_rsi(close, 14), 21)
    s_roc = _roc(_stoch_k(high, low, close, 14), 21)
    res = _mom_div(r_roc, s_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between MACD ROC and Stoch K ROC
def f14md_f14_momentum_divergence_macd_stoch_div_63d_v108_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    m_roc = _roc(_macd(closeadj), 63)
    s_roc = _roc(_stoch_k(high * adj, low * adj, closeadj, 14), 63)
    res = _mom_div(m_roc, s_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between RSI and MACD over 63d
def f14md_f14_momentum_divergence_rsi_macd_corr_63w_v109_signal(closeadj: pd.Series) -> pd.Series:
    r = _rsi(closeadj, 14)
    m = _macd(closeadj)
    res = _mom_corr(r, m, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between RSI and Stoch K over 126d
def f14md_f14_momentum_divergence_rsi_stoch_corr_126w_v110_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    r = _rsi(closeadj, 14)
    s = _stoch_k(high * adj, low * adj, closeadj, 14)
    res = _mom_corr(r, s, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of (RSI - 50) from its 21d mean
def f14md_f14_momentum_divergence_rsi_center_drift_21d_v111_signal(close: pd.Series) -> pd.Series:
    m = _rsi(close, 14) - 50
    res = _mom_drift(m, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of (Stoch K - 50) from its 63d mean
def f14md_f14_momentum_divergence_stoch_center_drift_63d_v112_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    m = _stoch_k(high * adj, low * adj, closeadj, 14) - 50
    res = _mom_drift(m, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 5d Price ROC and 5d (RSI + Stoch K) ROC
def f14md_f14_momentum_divergence_combo_div_5d_v113_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    combo = (_rsi(close, 14) + _stoch_k(high, low, close, 14)) / 2.0
    res = _mom_div(_roc(close, 5), _roc(combo, 5))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 21d Price ROC and 21d (RSI + Stoch K) ROC
def f14md_f14_momentum_divergence_combo_div_21d_v114_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    combo = (_rsi(close, 14) + _stoch_k(high, low, close, 14)) / 2.0
    res = _mom_div(_roc(close, 21), _roc(combo, 21))
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of (RSI + Stoch K) from its 126d mean
def f14md_f14_momentum_divergence_combo_drift_126d_v115_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    combo = (_rsi(closeadj, 14) + _stoch_k(high * adj, low * adj, closeadj, 14)) / 2.0
    res = _mom_drift(combo, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between Price ROC and (RSI + Stoch K) ROC over 63d
def f14md_f14_momentum_divergence_combo_corr_63w_v116_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    p_roc = _roc(closeadj, 21)
    combo_roc = _roc((_rsi(closeadj, 14) + _stoch_k(high * adj, low * adj, closeadj, 14)) / 2.0, 21)
    res = _mom_corr(p_roc, combo_roc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 10d Price ROC and 10d (MACD / Price) ROC
def f14md_f14_momentum_divergence_norm_macd_div_10d_v117_signal(close: pd.Series) -> pd.Series:
    m = _macd(close) / close.replace(0, np.nan)
    res = _mom_div(_roc(close, 10), _roc(m, 10))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 63d Price ROC and 63d (MACD / Price) ROC
def f14md_f14_momentum_divergence_norm_macd_div_63d_v118_signal(closeadj: pd.Series) -> pd.Series:
    m = _macd(closeadj) / closeadj.replace(0, np.nan)
    res = _mom_div(_roc(closeadj, 63), _roc(m, 63))
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of (MACD / Price) from its 252d mean
def f14md_f14_momentum_divergence_norm_macd_drift_252d_v119_signal(closeadj: pd.Series) -> pd.Series:
    m = _macd(closeadj) / closeadj.replace(0, np.nan)
    res = _mom_drift(m, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between Price and (MACD / Price) over 252d
def f14md_f14_momentum_divergence_price_norm_macd_corr_252w_v120_signal(closeadj: pd.Series) -> pd.Series:
    m = _macd(closeadj) / closeadj.replace(0, np.nan)
    res = _mom_corr(closeadj, m, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# --- High/Low Range Divergence (v121 - v135) ---

# Divergence between 5d Price ROC and 5d High-Low Range ROC
def f14md_f14_momentum_divergence_hl_range_div_5d_v121_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    hl = high - low
    res = _mom_div(_roc(close, 5), _roc(hl, 5))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 21d Price ROC and 21d High-Low Range ROC
def f14md_f14_momentum_divergence_hl_range_div_21d_v122_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    hl = high - low
    res = _mom_div(_roc(close, 21), _roc(hl, 21))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 63d Price ROC and 63d High-Low Range ROC
def f14md_f14_momentum_divergence_hl_range_div_63d_v123_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    hl = (high - low) * adj
    res = _mom_div(_roc(closeadj, 63), _roc(hl, 63))
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of High-Low Range from its 21d mean
def f14md_f14_momentum_divergence_hl_range_drift_21d_v124_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    hl = high - low
    res = _mom_drift(hl, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of High-Low Range from its 126d mean
def f14md_f14_momentum_divergence_hl_range_drift_126d_v125_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    hl = (high - low) * adj
    res = _mom_drift(hl, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between Price ROC and High-Low Range ROC over 63d
def f14md_f14_momentum_divergence_hl_range_corr_63w_v126_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    p_roc = _roc(closeadj, 21)
    hl_roc = _roc((high - low) * adj, 21)
    res = _mom_corr(p_roc, hl_roc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 5d Price ROC and 5d ATR ROC
def f14md_f14_momentum_divergence_atr_div_5d_v127_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = _sma(tr, 14)
    res = _mom_div(_roc(close, 5), _roc(atr, 5))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 21d Price ROC and 21d ATR ROC
def f14md_f14_momentum_divergence_atr_div_21d_v128_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = _sma(tr, 14)
    res = _mom_div(_roc(close, 21), _roc(atr, 21))
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of ATR from its 63d mean
def f14md_f14_momentum_divergence_atr_drift_63d_v129_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr = _sma(tr, 14)
    res = _mom_drift(atr, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between Price ROC and ATR ROC over 126d
def f14md_f14_momentum_divergence_atr_corr_126w_v130_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    tr = pd.concat([(high-low)*adj, (high*adj - closeadj.shift(1)).abs(), (low*adj - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    atr = _sma(tr, 14)
    res = _mom_corr(_roc(closeadj, 21), _roc(atr, 21), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 5d Price ROC and 5d (High-Close) ROC
def f14md_f14_momentum_divergence_high_close_div_5d_v131_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    m = high - close
    res = _mom_div(_roc(close, 5), _roc(m, 5))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 21d Price ROC and 21d (Close-Low) ROC
def f14md_f14_momentum_divergence_close_low_div_21d_v132_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    m = close - low
    res = _mom_div(_roc(close, 21), _roc(m, 21))
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of (High-Close) from its 63d mean
def f14md_f14_momentum_divergence_high_close_drift_63d_v133_signal(high: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    m = (high * adj) - closeadj
    res = _mom_drift(m, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of (Close-Low) from its 126d mean
def f14md_f14_momentum_divergence_close_low_drift_126d_v134_signal(low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    m = closeadj - (low * adj)
    res = _mom_drift(m, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between Price ROC and (High-Low) ROC over 252d
def f14md_f14_momentum_divergence_hl_range_corr_252w_v135_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _mom_corr(_roc(closeadj, 63), _roc((high - low) * adj, 63), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# --- More Raw Momentum Variants (v136 - v150) ---

# Divergence between 5d Price ROC and 5d (Close - Close[5]) ROC
def f14md_f14_momentum_divergence_raw5_div_5d_v136_signal(close: pd.Series) -> pd.Series:
    raw_mom = close - close.shift(5)
    res = _mom_div(_roc(close, 5), _roc(raw_mom, 5))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 21d Price ROC and 21d (Close - Close[21]) ROC (alternate)

# Divergence between 63d Price ROC and 63d (Closeadj - Closeadj[63]) ROC (alternate)

# Drift of (Closeadj - Closeadj[126]) from its 252d mean
def f14md_f14_momentum_divergence_raw126_drift_252d_v139_signal(closeadj: pd.Series) -> pd.Series:
    raw_mom = closeadj - closeadj.shift(126)
    res = _mom_drift(raw_mom, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between 21d Price ROC and 21d (Closeadj - Closeadj[126]) ROC over 126d
def f14md_f14_momentum_divergence_raw126_corr_21d_126w_v140_signal(closeadj: pd.Series) -> pd.Series:
    raw_mom = closeadj - closeadj.shift(126)
    res = _mom_corr(_roc(closeadj, 21), _roc(raw_mom, 21), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 10d Price ROC and 10d (EMA(Close, 5) - EMA(Close, 20)) ROC
def f14md_f14_momentum_divergence_ema_cross_div_10d_v141_signal(close: pd.Series) -> pd.Series:
    m = _ema(close, 5) - _ema(close, 20)
    res = _mom_div(_roc(close, 10), _roc(m, 10))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 63d Price ROC and 63d (EMA(Closeadj, 20) - EMA(Closeadj, 60)) ROC
def f14md_f14_momentum_divergence_ema_cross_div_63d_v142_signal(closeadj: pd.Series) -> pd.Series:
    m = _ema(closeadj, 20) - _ema(closeadj, 60)
    res = _mom_div(_roc(closeadj, 63), _roc(m, 63))
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of (EMA(Closeadj, 50) - EMA(Closeadj, 200)) from its 200d mean
def f14md_f14_momentum_divergence_ema_cross_drift_200d_v143_signal(closeadj: pd.Series) -> pd.Series:
    m = _ema(closeadj, 50) - _ema(closeadj, 200)
    res = _mom_drift(m, 200)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between Price and (EMA(Closeadj, 20) - EMA(Closeadj, 60)) over 120d
def f14md_f14_momentum_divergence_price_ema_cross_corr_120w_v144_signal(closeadj: pd.Series) -> pd.Series:
    m = _ema(closeadj, 20) - _ema(closeadj, 60)
    res = _mom_corr(closeadj, m, 120)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 5d Price ROC and 5d (Close / SMA(Close, 20)) ROC
def f14md_f14_momentum_divergence_ma_ratio_div_5d_v145_signal(close: pd.Series) -> pd.Series:
    m = close / _sma(close, 20).replace(0, np.nan)
    res = _mom_div(_roc(close, 5), _roc(m, 5))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 21d Price ROC and 21d (Closeadj / SMA(Closeadj, 63)) ROC
def f14md_f14_momentum_divergence_ma_ratio_div_21d_v146_signal(closeadj: pd.Series) -> pd.Series:
    m = closeadj / _sma(closeadj, 63).replace(0, np.nan)
    res = _mom_div(_roc(closeadj, 21), _roc(m, 21))
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of (Closeadj / SMA(Closeadj, 252)) from its 252d mean
def f14md_f14_momentum_divergence_ma_ratio_drift_252d_v147_signal(closeadj: pd.Series) -> pd.Series:
    m = closeadj / _sma(closeadj, 252).replace(0, np.nan)
    res = _mom_drift(m, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between Price ROC and (Closeadj / SMA(Closeadj, 63)) ROC over 63d
def f14md_f14_momentum_divergence_ma_ratio_corr_63w_v148_signal(closeadj: pd.Series) -> pd.Series:
    p_roc = _roc(closeadj, 21)
    m_roc = _roc(closeadj / _sma(closeadj, 63).replace(0, np.nan), 21)
    res = _mom_corr(p_roc, m_roc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 3d Price ROC and 3d (High / Low) ROC
def f14md_f14_momentum_divergence_hl_ratio_div_3d_v149_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    m = high / low.replace(0, np.nan)
    res = _mom_div(_roc(close, 3), _roc(m, 3))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 21d Price ROC and 21d (High / Low) ROC
def f14md_f14_momentum_divergence_hl_ratio_div_21d_v150_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    m = high / low.replace(0, np.nan)
    res = _mom_div(_roc(close, 21), _roc(m, 21))
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

BASE_NAMES = [f for f in globals() if f.startswith("f14md_") and f.endswith("_signal")]

F14_MOMENTUM_DIVERGENCE_BASE_REGISTRY_076_150 = {
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
    for n, c in F14_MOMENTUM_DIVERGENCE_BASE_REGISTRY_076_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 076-150 OK")
