# f14_momentum_divergence_base_001_075_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _ema(s, w):
    return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()

def _roc(s, w):
    return s.pct_change(w)

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

# --- RSI Divergence Base Features ---

# Divergence between 5d Price ROC and 5d RSI ROC
def f14md_f14_momentum_divergence_rsi_div_5d_v001_signal(close: pd.Series) -> pd.Series:
    p_roc = _roc(close, 5)
    m_roc = _roc(_rsi(close, 14), 5)
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 10d Price ROC and 10d RSI ROC
def f14md_f14_momentum_divergence_rsi_div_10d_v002_signal(close: pd.Series) -> pd.Series:
    p_roc = _roc(close, 10)
    m_roc = _roc(_rsi(close, 14), 10)
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 21d Price ROC and 21d RSI ROC
def f14md_f14_momentum_divergence_rsi_div_21d_v003_signal(close: pd.Series) -> pd.Series:
    p_roc = _roc(close, 21)
    m_roc = _roc(_rsi(close, 14), 21)
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 63d Price ROC and 63d RSI ROC
def f14md_f14_momentum_divergence_rsi_div_63d_v004_signal(closeadj: pd.Series) -> pd.Series:
    p_roc = _roc(closeadj, 63)
    m_roc = _roc(_rsi(closeadj, 14), 63)
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 126d Price ROC and 126d RSI ROC
def f14md_f14_momentum_divergence_rsi_div_126d_v005_signal(closeadj: pd.Series) -> pd.Series:
    p_roc = _roc(closeadj, 126)
    m_roc = _roc(_rsi(closeadj, 14), 126)
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of 14d RSI from its 21d mean
def f14md_f14_momentum_divergence_rsi_drift_21d_v006_signal(close: pd.Series) -> pd.Series:
    m = _rsi(close, 14)
    res = _mom_drift(m, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of 14d RSI from its 63d mean
def f14md_f14_momentum_divergence_rsi_drift_63d_v007_signal(closeadj: pd.Series) -> pd.Series:
    m = _rsi(closeadj, 14)
    res = _mom_drift(m, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of 14d RSI from its 126d mean
def f14md_f14_momentum_divergence_rsi_drift_126d_v008_signal(closeadj: pd.Series) -> pd.Series:
    m = _rsi(closeadj, 14)
    res = _mom_drift(m, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between 5d Price ROC and 5d RSI ROC over 21d
def f14md_f14_momentum_divergence_rsi_corr_5d_21w_v009_signal(close: pd.Series) -> pd.Series:
    p_roc = _roc(close, 5)
    m_roc = _roc(_rsi(close, 14), 5)
    res = _mom_corr(p_roc, m_roc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between 21d Price ROC and 21d RSI ROC over 63d
def f14md_f14_momentum_divergence_rsi_corr_21d_63w_v010_signal(closeadj: pd.Series) -> pd.Series:
    p_roc = _roc(closeadj, 21)
    m_roc = _roc(_rsi(closeadj, 14), 21)
    res = _mom_corr(p_roc, m_roc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# --- MACD Divergence Base Features ---

# Divergence between 5d Price ROC and 5d MACD ROC
def f14md_f14_momentum_divergence_macd_div_5d_v011_signal(close: pd.Series) -> pd.Series:
    p_roc = _roc(close, 5)
    m_roc = _roc(_macd(close), 5)
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 10d Price ROC and 10d MACD ROC
def f14md_f14_momentum_divergence_macd_div_10d_v012_signal(close: pd.Series) -> pd.Series:
    p_roc = _roc(close, 10)
    m_roc = _roc(_macd(close), 10)
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 21d Price ROC and 21d MACD ROC
def f14md_f14_momentum_divergence_macd_div_21d_v013_signal(close: pd.Series) -> pd.Series:
    p_roc = _roc(close, 21)
    m_roc = _roc(_macd(close), 21)
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 63d Price ROC and 63d MACD ROC
def f14md_f14_momentum_divergence_macd_div_63d_v014_signal(closeadj: pd.Series) -> pd.Series:
    p_roc = _roc(closeadj, 63)
    m_roc = _roc(_macd(closeadj), 63)
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 126d Price ROC and 126d MACD ROC
def f14md_f14_momentum_divergence_macd_div_126d_v015_signal(closeadj: pd.Series) -> pd.Series:
    p_roc = _roc(closeadj, 126)
    m_roc = _roc(_macd(closeadj), 126)
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of MACD from its 21d mean
def f14md_f14_momentum_divergence_macd_drift_21d_v016_signal(close: pd.Series) -> pd.Series:
    m = _macd(close)
    res = _mom_drift(m, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of MACD from its 63d mean
def f14md_f14_momentum_divergence_macd_drift_63d_v017_signal(closeadj: pd.Series) -> pd.Series:
    m = _macd(closeadj)
    res = _mom_drift(m, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of MACD from its 126d mean
def f14md_f14_momentum_divergence_macd_drift_126d_v018_signal(closeadj: pd.Series) -> pd.Series:
    m = _macd(closeadj)
    res = _mom_drift(m, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between 5d Price ROC and 5d MACD ROC over 21d
def f14md_f14_momentum_divergence_macd_corr_5d_21w_v019_signal(close: pd.Series) -> pd.Series:
    p_roc = _roc(close, 5)
    m_roc = _roc(_macd(close), 5)
    res = _mom_corr(p_roc, m_roc, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between 21d Price ROC and 21d MACD ROC over 63d
def f14md_f14_momentum_divergence_macd_corr_21d_63w_v020_signal(closeadj: pd.Series) -> pd.Series:
    p_roc = _roc(closeadj, 21)
    m_roc = _roc(_macd(closeadj), 21)
    res = _mom_corr(p_roc, m_roc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# --- ROC Divergence Base Features (Short vs Long) ---

# Divergence between 5d Price ROC and 21d Price ROC
def f14md_f14_momentum_divergence_roc_div_5d_21d_v021_signal(close: pd.Series) -> pd.Series:
    p_roc = _roc(close, 5)
    m_roc = _roc(close, 21)
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 10d Price ROC and 63d Price ROC
def f14md_f14_momentum_divergence_roc_div_10d_63d_v022_signal(closeadj: pd.Series) -> pd.Series:
    p_roc = _roc(closeadj, 10)
    m_roc = _roc(closeadj, 63)
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 21d Price ROC and 126d Price ROC
def f14md_f14_momentum_divergence_roc_div_21d_126d_v023_signal(closeadj: pd.Series) -> pd.Series:
    p_roc = _roc(closeadj, 21)
    m_roc = _roc(closeadj, 126)
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of 21d ROC from its 63d mean
def f14md_f14_momentum_divergence_roc_drift_21d_63w_v024_signal(closeadj: pd.Series) -> pd.Series:
    m = _roc(closeadj, 21)
    res = _mom_drift(m, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of 63d ROC from its 126d mean
def f14md_f14_momentum_divergence_roc_drift_63d_126w_v025_signal(closeadj: pd.Series) -> pd.Series:
    m = _roc(closeadj, 63)
    res = _mom_drift(m, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between 5d ROC and 21d ROC over 63d
def f14md_f14_momentum_divergence_roc_corr_5d_21d_63w_v026_signal(closeadj: pd.Series) -> pd.Series:
    p_roc = _roc(closeadj, 5)
    m_roc = _roc(closeadj, 21)
    res = _mom_corr(p_roc, m_roc, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between 21d ROC and 63d ROC over 126d
def f14md_f14_momentum_divergence_roc_corr_21d_63d_126w_v027_signal(closeadj: pd.Series) -> pd.Series:
    p_roc = _roc(closeadj, 21)
    m_roc = _roc(closeadj, 63)
    res = _mom_corr(p_roc, m_roc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# --- More RSI Variations (v028 - v040) ---

# Divergence between 5d Price ROC and 14d RSI
def f14md_f14_momentum_divergence_rsi_val_div_5d_v028_signal(close: pd.Series) -> pd.Series:
    p_roc = _roc(close, 5)
    m_roc = _rsi(close, 14) / 100.0 # Scaling RSI
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 21d Price ROC and 14d RSI
def f14md_f14_momentum_divergence_rsi_val_div_21d_v029_signal(close: pd.Series) -> pd.Series:
    p_roc = _roc(close, 21)
    m_roc = _rsi(close, 14) / 100.0
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 63d Price ROC and 14d RSI
def f14md_f14_momentum_divergence_rsi_val_div_63d_v030_signal(closeadj: pd.Series) -> pd.Series:
    p_roc = _roc(closeadj, 63)
    m_roc = _rsi(closeadj, 14) / 100.0
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between Price and RSI over 21d
def f14md_f14_momentum_divergence_price_rsi_corr_21w_v031_signal(close: pd.Series) -> pd.Series:
    res = _mom_corr(close, _rsi(close, 14), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between Price and RSI over 63d
def f14md_f14_momentum_divergence_price_rsi_corr_63w_v032_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_corr(closeadj, _rsi(closeadj, 14), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between Price and RSI over 126d
def f14md_f14_momentum_divergence_price_rsi_corr_126w_v033_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_corr(closeadj, _rsi(closeadj, 14), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of 7d RSI from its 21d mean
def f14md_f14_momentum_divergence_rsi7_drift_21d_v034_signal(close: pd.Series) -> pd.Series:
    res = _mom_drift(_rsi(close, 7), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of 21d RSI from its 63d mean
def f14md_f14_momentum_divergence_rsi21_drift_63d_v035_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_drift(_rsi(closeadj, 21), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 5d Price ROC and 5d RSI7 ROC
def f14md_f14_momentum_divergence_rsi7_div_5d_v036_signal(close: pd.Series) -> pd.Series:
    p_roc = _roc(close, 5)
    m_roc = _roc(_rsi(close, 7), 5)
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 21d Price ROC and 21d RSI21 ROC
def f14md_f14_momentum_divergence_rsi21_div_21d_v037_signal(close: pd.Series) -> pd.Series:
    p_roc = _roc(close, 21)
    m_roc = _roc(_rsi(close, 21), 21)
    res = _mom_div(p_roc, m_roc)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between 10d Price ROC and 10d RSI7 ROC over 42d
def f14md_f14_momentum_divergence_rsi7_corr_10d_42w_v038_signal(closeadj: pd.Series) -> pd.Series:
    p_roc = _roc(closeadj, 10)
    m_roc = _roc(_rsi(closeadj, 7), 10)
    res = _mom_corr(p_roc, m_roc, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between 21d Price ROC and 21d RSI21 ROC over 126d
def f14md_f14_momentum_divergence_rsi21_corr_21d_126w_v039_signal(closeadj: pd.Series) -> pd.Series:
    p_roc = _roc(closeadj, 21)
    m_roc = _roc(_rsi(closeadj, 21), 21)
    res = _mom_corr(p_roc, m_roc, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of RSI (fast/slow ratio) from its 63d mean
def f14md_f14_momentum_divergence_rsi_ratio_drift_63d_v040_signal(closeadj: pd.Series) -> pd.Series:
    m = _rsi(closeadj, 7) / _rsi(closeadj, 21).replace(0, np.nan)
    res = _mom_drift(m, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# --- More MACD Variations (v041 - v055) ---

# Divergence between 5d Price ROC and 5d MACD Signal ROC
def f14md_f14_momentum_divergence_macd_sig_div_5d_v041_signal(close: pd.Series) -> pd.Series:
    macd = _macd(close)
    signal = _ema(macd, 9)
    res = _mom_div(_roc(close, 5), _roc(signal, 5))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 21d Price ROC and 21d MACD Signal ROC
def f14md_f14_momentum_divergence_macd_sig_div_21d_v042_signal(close: pd.Series) -> pd.Series:
    macd = _macd(close)
    signal = _ema(macd, 9)
    res = _mom_div(_roc(close, 21), _roc(signal, 21))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 63d Price ROC and 63d MACD Signal ROC
def f14md_f14_momentum_divergence_macd_sig_div_63d_v043_signal(closeadj: pd.Series) -> pd.Series:
    macd = _macd(closeadj)
    signal = _ema(macd, 9)
    res = _mom_div(_roc(closeadj, 63), _roc(signal, 63))
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between MACD and its Signal over 21d
def f14md_f14_momentum_divergence_macd_sig_corr_21w_v044_signal(close: pd.Series) -> pd.Series:
    macd = _macd(close)
    signal = _ema(macd, 9)
    res = _mom_corr(macd, signal, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between MACD and its Signal over 63d
def f14md_f14_momentum_divergence_macd_sig_corr_63w_v045_signal(closeadj: pd.Series) -> pd.Series:
    macd = _macd(closeadj)
    signal = _ema(macd, 9)
    res = _mom_corr(macd, signal, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of MACD Histogram from its 21d mean
def f14md_f14_momentum_divergence_macd_hist_drift_21d_v046_signal(close: pd.Series) -> pd.Series:
    macd = _macd(close)
    signal = _ema(macd, 9)
    hist = macd - signal
    res = _mom_drift(hist, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of MACD Histogram from its 63d mean
def f14md_f14_momentum_divergence_macd_hist_drift_63d_v047_signal(closeadj: pd.Series) -> pd.Series:
    macd = _macd(closeadj)
    signal = _ema(macd, 9)
    hist = macd - signal
    res = _mom_drift(hist, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 5d Price ROC and 5d MACD Histogram ROC
def f14md_f14_momentum_divergence_macd_hist_div_5d_v048_signal(close: pd.Series) -> pd.Series:
    macd = _macd(close)
    signal = _ema(macd, 9)
    hist = macd - signal
    res = _mom_div(_roc(close, 5), _roc(hist, 5))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 21d Price ROC and 21d MACD Histogram ROC
def f14md_f14_momentum_divergence_macd_hist_div_21d_v049_signal(close: pd.Series) -> pd.Series:
    macd = _macd(close)
    signal = _ema(macd, 9)
    hist = macd - signal
    res = _mom_div(_roc(close, 21), _roc(hist, 21))
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between Price ROC and MACD Histogram ROC over 63d
def f14md_f14_momentum_divergence_macd_hist_corr_63w_v050_signal(closeadj: pd.Series) -> pd.Series:
    macd = _macd(closeadj)
    signal = _ema(macd, 9)
    hist = macd - signal
    res = _mom_corr(_roc(closeadj, 21), _roc(hist, 21), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of MACD (fast/slow) ratio from its 126d mean
def f14md_f14_momentum_divergence_macd_ratio_drift_126d_v051_signal(closeadj: pd.Series) -> pd.Series:
    m = _ema(closeadj, 12) / _ema(closeadj, 26).replace(0, np.nan)
    res = _mom_drift(m, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between Price and MACD Histogram over 126d
def f14md_f14_momentum_divergence_price_macd_hist_corr_126w_v052_signal(closeadj: pd.Series) -> pd.Series:
    macd = _macd(closeadj)
    signal = _ema(macd, 9)
    hist = macd - signal
    res = _mom_corr(closeadj, hist, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 10d Price ROC and 10d MACD (24, 52) ROC
def f14md_f14_momentum_divergence_macd_long_div_10d_v053_signal(close: pd.Series) -> pd.Series:
    m = _macd(close, fast=24, slow=52)
    res = _mom_div(_roc(close, 10), _roc(m, 10))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 63d Price ROC and 63d MACD (24, 52) ROC
def f14md_f14_momentum_divergence_macd_long_div_63d_v054_signal(closeadj: pd.Series) -> pd.Series:
    m = _macd(closeadj, fast=24, slow=52)
    res = _mom_div(_roc(closeadj, 63), _roc(m, 63))
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between 21d Price ROC and 21d MACD (24, 52) ROC over 252d
def f14md_f14_momentum_divergence_macd_long_corr_21d_252w_v055_signal(closeadj: pd.Series) -> pd.Series:
    m = _macd(closeadj, fast=24, slow=52)
    res = _mom_corr(_roc(closeadj, 21), _roc(m, 21), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# --- More ROC Variations (v056 - v075) ---

# Divergence between 1d Price ROC and 5d Price ROC
def f14md_f14_momentum_divergence_roc_div_1d_5d_v056_signal(close: pd.Series) -> pd.Series:
    res = _mom_div(_roc(close, 1), _roc(close, 5))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 5d Price ROC and 63d Price ROC
def f14md_f14_momentum_divergence_roc_div_5d_63d_v057_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_div(_roc(closeadj, 5), _roc(closeadj, 63))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 21d Price ROC and 252d Price ROC
def f14md_f14_momentum_divergence_roc_div_21d_252d_v058_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_div(_roc(closeadj, 21), _roc(closeadj, 252))
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of 5d ROC from its 21d mean
def f14md_f14_momentum_divergence_roc5_drift_21d_v059_signal(close: pd.Series) -> pd.Series:
    res = _mom_drift(_roc(close, 5), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of 126d ROC from its 252d mean
def f14md_f14_momentum_divergence_roc126_drift_252d_v060_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_drift(_roc(closeadj, 126), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between 1d ROC and 21d ROC over 21d
def f14md_f14_momentum_divergence_roc_corr_1d_21d_21w_v061_signal(close: pd.Series) -> pd.Series:
    res = _mom_corr(_roc(close, 1), _roc(close, 21), 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between 5d ROC and 126d ROC over 126d
def f14md_f14_momentum_divergence_roc_corr_5d_126d_126w_v062_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_corr(_roc(closeadj, 5), _roc(closeadj, 126), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 3d Price ROC and 15d Price ROC
def f14md_f14_momentum_divergence_roc_div_3d_15d_v063_signal(close: pd.Series) -> pd.Series:
    res = _mom_div(_roc(close, 3), _roc(close, 15))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 15d Price ROC and 45d Price ROC
def f14md_f14_momentum_divergence_roc_div_15d_45d_v064_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_div(_roc(closeadj, 15), _roc(closeadj, 45))
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of 45d ROC from its 90d mean
def f14md_f14_momentum_divergence_roc45_drift_90d_v065_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_drift(_roc(closeadj, 45), 90)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between 10d ROC and 40d ROC over 80d
def f14md_f14_momentum_divergence_roc_corr_10d_40d_80w_v066_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_corr(_roc(closeadj, 10), _roc(closeadj, 40), 80)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 1d Price ROC and 10d Price ROC
def f14md_f14_momentum_divergence_roc_div_1d_10d_v067_signal(close: pd.Series) -> pd.Series:
    res = _mom_div(_roc(close, 1), _roc(close, 10))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 10d Price ROC and 100d Price ROC
def f14md_f14_momentum_divergence_roc_div_10d_100d_v068_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_div(_roc(closeadj, 10), _roc(closeadj, 100))
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of 100d ROC from its 200d mean
def f14md_f14_momentum_divergence_roc100_drift_200d_v069_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_drift(_roc(closeadj, 100), 200)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between 20d ROC and 100d ROC over 200d
def f14md_f14_momentum_divergence_roc_corr_20d_100d_200w_v070_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_corr(_roc(closeadj, 20), _roc(closeadj, 100), 200)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 5d Price ROC and 20d Price ROC (alternate)
def f14md_f14_momentum_divergence_roc_div_5d_20d_v071_signal(close: pd.Series) -> pd.Series:
    res = _mom_div(_roc(close, 5), _roc(close, 20))
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 20d Price ROC and 60d Price ROC (alternate)
def f14md_f14_momentum_divergence_roc_div_20d_60d_v072_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_div(_roc(closeadj, 20), _roc(closeadj, 60))
    return res.replace([np.inf, -np.inf], np.nan)

# Drift of 60d ROC from its 120d mean (alternate)
def f14md_f14_momentum_divergence_roc60_drift_120d_v073_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_drift(_roc(closeadj, 60), 120)
    return res.replace([np.inf, -np.inf], np.nan)

# Correlation between 30d ROC and 90d ROC over 180d (alternate)
def f14md_f14_momentum_divergence_roc_corr_30d_90d_180w_v074_signal(closeadj: pd.Series) -> pd.Series:
    res = _mom_corr(_roc(closeadj, 30), _roc(closeadj, 90), 180)
    return res.replace([np.inf, -np.inf], np.nan)

# Divergence between 2d Price ROC and 8d Price ROC
def f14md_f14_momentum_divergence_roc_div_2d_8d_v075_signal(close: pd.Series) -> pd.Series:
    res = _mom_div(_roc(close, 2), _roc(close, 8))
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

BASE_NAMES = [f for f in globals() if f.startswith("f14md_") and f.endswith("_signal")]

F14_MOMENTUM_DIVERGENCE_BASE_REGISTRY_001_075 = {
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
    sz = 500; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F14_MOMENTUM_DIVERGENCE_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 001-075 OK")
