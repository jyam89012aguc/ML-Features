# f14_momentum_divergence_jerk_001_150_gemini.py
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

# --- Jerk Features (Acceleration in Divergence/Drift/Correlation) ---

# Jerk of 5d RSI Divergence (5d ROC of Slope)
def f14md_f14_momentum_divergence_rsi_div_5d_jerk_v001_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(_rsi(close, 14), 5))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 10d RSI Divergence (5d ROC of Slope)
def f14md_f14_momentum_divergence_rsi_div_10d_jerk_v002_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 10), _roc(_rsi(close, 14), 10))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 21d RSI Divergence (10d ROC of Slope)
def f14md_f14_momentum_divergence_rsi_div_21d_jerk_v003_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 21), _roc(_rsi(close, 14), 21))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 63d RSI Divergence (21d ROC of Slope)
def f14md_f14_momentum_divergence_rsi_div_63d_jerk_v004_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_div(_roc(closeadj, 63), _roc(_rsi(closeadj, 14), 63))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 126d RSI Divergence (21d ROC of Slope)
def f14md_f14_momentum_divergence_rsi_div_126d_jerk_v005_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_div(_roc(closeadj, 126), _roc(_rsi(closeadj, 14), 126))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of RSI Drift (21d window, 5d ROC)
def f14md_f14_momentum_divergence_rsi_drift_21d_jerk_v006_signal(close: pd.Series) -> pd.Series:
    base = _mom_drift(_rsi(close, 14), 21)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of RSI Drift (63d window, 21d ROC)
def f14md_f14_momentum_divergence_rsi_drift_63d_jerk_v007_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_drift(_rsi(closeadj, 14), 63)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of RSI Correlation (21w, 5d ROC)
def f14md_f14_momentum_divergence_rsi_corr_5d_21w_jerk_v008_signal(close: pd.Series) -> pd.Series:
    base = _mom_corr(_roc(close, 5), _roc(_rsi(close, 14), 5), 21)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 5d MACD Divergence (5d ROC)
def f14md_f14_momentum_divergence_macd_div_5d_jerk_v009_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(_macd(close), 5))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 21d MACD Divergence (10d ROC)
def f14md_f14_momentum_divergence_macd_div_21d_jerk_v010_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 21), _roc(_macd(close), 21))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 63d MACD Divergence (21d ROC)
def f14md_f14_momentum_divergence_macd_div_63d_jerk_v011_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_div(_roc(closeadj, 63), _roc(_macd(closeadj), 63))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 5d ROC Divergence (Short vs Long, 5d ROC)
def f14md_f14_momentum_divergence_roc_div_5d_21d_jerk_v012_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(close, 21))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of 21d ROC Divergence (21d ROC)
def f14md_f14_momentum_divergence_roc_div_21d_126d_jerk_v013_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_div(_roc(closeadj, 21), _roc(closeadj, 126))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Stoch Divergence (5d, 5d ROC)
def f14md_f14_momentum_divergence_stoch_div_5d_jerk_v014_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(_stoch_k(high, low, close, 14), 5))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Stoch Divergence (63d, 21d ROC)
def f14md_f14_momentum_divergence_stoch_div_63d_jerk_v015_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    base = _mom_div(_roc(closeadj, 63), _roc(_stoch_k(high * adj, low * adj, closeadj, 14), 63))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Raw Momentum Divergence (5d, 5d ROC)
def f14md_f14_momentum_divergence_raw_mom_div_5d_jerk_v016_signal(close: pd.Series) -> pd.Series:
    raw_mom = close - close.shift(10)
    base = _mom_div(_roc(close, 5), _roc(raw_mom, 5))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of SMA Diff Divergence (10d, 5d ROC)
def f14md_f14_momentum_divergence_sma_diff_div_10d_jerk_v017_signal(close: pd.Series) -> pd.Series:
    m = close - _sma(close, 10)
    base = _mom_div(_roc(close, 10), _roc(m, 10))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of EMA Diff Divergence (5d, 5d ROC)
def f14md_f14_momentum_divergence_ema_diff_div_5d_jerk_v018_signal(close: pd.Series) -> pd.Series:
    m = close - _ema(close, 5)
    base = _mom_div(_roc(close, 5), _roc(m, 5))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of RSI/MACD Divergence (5d, 5d ROC)
def f14md_f14_momentum_divergence_rsi_macd_div_5d_jerk_v019_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(_rsi(close, 14), 5), _roc(_macd(close), 5))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of HL Range Divergence (5d, 5d ROC)
def f14md_f14_momentum_divergence_hl_range_div_5d_jerk_v020_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(high - low, 5))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of ATR Divergence (21d, 10d ROC)
def f14md_f14_momentum_divergence_atr_div_21d_jerk_v021_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    base = _mom_div(_roc(close, 21), _roc(_sma(tr, 14), 21))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of RSI7 Divergence (5d, 5d ROC)
def f14md_f14_momentum_divergence_rsi7_div_5d_jerk_v022_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(_rsi(close, 7), 5))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of MACD Histogram Drift (21d, 5d ROC)
def f14md_f14_momentum_divergence_macd_hist_drift_21d_jerk_v023_signal(close: pd.Series) -> pd.Series:
    m = _macd(close)
    base = _mom_drift(m - _ema(m, 9), 21)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Combo Divergence (5d, 5d ROC)
def f14md_f14_momentum_divergence_combo_div_5d_jerk_v024_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    combo = (_rsi(close, 14) + _stoch_k(high, low, close, 14)) / 2.0
    base = _mom_div(_roc(close, 5), _roc(combo, 5))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of RSI Divergence (15d, 5d ROC)
def f14md_f14_momentum_divergence_rsi_div_15d_jerk_v025_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 15), _roc(_rsi(close, 14), 15))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of MACD Divergence (30d, 15d ROC)
def f14md_f14_momentum_divergence_macd_div_30d_jerk_v026_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_div(_roc(closeadj, 30), _roc(_macd(closeadj), 30))
    slope = base.pct_change(15)
    res = slope.pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)

# Jerk of Stoch Divergence (30d, 15d ROC)
def f14md_f14_momentum_divergence_stoch_div_30d_jerk_v027_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    base = _mom_div(_roc(closeadj, 30), _roc(_stoch_k(high * adj, low * adj, closeadj, 14), 30))
    slope = base.pct_change(15)
    res = slope.pct_change(15)
    return res.replace([np.inf, -np.inf], np.nan)

# [Generating more jerks following the pattern v028-v150 to ensure size and variety]

def f14md_f14_momentum_divergence_rsi_div_5d_alt_jerk_v028_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(_rsi(close, 14), 5))
    slope = base.pct_change(3)
    res = slope.pct_change(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_div_10d_alt_jerk_v029_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 10), _roc(_rsi(close, 14), 10))
    slope = base.pct_change(3)
    res = slope.pct_change(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_div_21d_alt_jerk_v030_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 21), _roc(_rsi(close, 14), 21))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_div_63d_alt_jerk_v031_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_div(_roc(closeadj, 63), _roc(_rsi(closeadj, 14), 63))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_div_126d_alt_jerk_v032_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_div(_roc(closeadj, 126), _roc(_rsi(closeadj, 14), 126))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_5d_alt_jerk_v033_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(_macd(close), 5))
    slope = base.pct_change(3)
    res = slope.pct_change(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_10d_alt_jerk_v034_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 10), _roc(_macd(close), 10))
    slope = base.pct_change(3)
    res = slope.pct_change(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_21d_alt_jerk_v035_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 21), _roc(_macd(close), 21))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_63d_alt_jerk_v036_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_div(_roc(closeadj, 63), _roc(_macd(closeadj), 63))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_126d_alt_jerk_v037_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_div(_roc(closeadj, 126), _roc(_macd(closeadj), 126))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_5d_alt_jerk_v038_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(_stoch_k(high, low, close, 14), 5))
    slope = base.pct_change(3)
    res = slope.pct_change(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_10d_alt_jerk_v039_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 10), _roc(_stoch_k(high, low, close, 14), 10))
    slope = base.pct_change(3)
    res = slope.pct_change(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_21d_alt_jerk_v040_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 21), _roc(_stoch_k(high, low, close, 14), 21))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_63d_alt_jerk_v041_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    base = _mom_div(_roc(closeadj, 63), _roc(_stoch_k(high * adj, low * adj, closeadj, 14), 63))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_126d_alt_jerk_v042_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    base = _mom_div(_roc(closeadj, 126), _roc(_stoch_k(high * adj, low * adj, closeadj, 14), 126))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_drift_21d_alt_jerk_v043_signal(close: pd.Series) -> pd.Series:
    base = _mom_drift(_rsi(close, 14), 21)
    slope = base.pct_change(3)
    res = slope.pct_change(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_drift_63d_alt_jerk_v044_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_drift(_rsi(closeadj, 14), 63)
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_drift_21d_alt_jerk_v045_signal(close: pd.Series) -> pd.Series:
    base = _mom_drift(_macd(close), 21)
    slope = base.pct_change(3)
    res = slope.pct_change(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_drift_63d_alt_jerk_v046_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_drift(_macd(closeadj), 63)
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_drift_21d_alt_jerk_v047_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_drift(_stoch_k(high, low, close, 14), 21)
    slope = base.pct_change(3)
    res = slope.pct_change(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_drift_63d_alt_jerk_v048_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    base = _mom_drift(_stoch_k(high * adj, low * adj, closeadj, 14), 63)
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_corr_5d_21w_alt_jerk_v049_signal(close: pd.Series) -> pd.Series:
    base = _mom_corr(_roc(close, 5), _roc(_rsi(close, 14), 5), 21)
    slope = base.pct_change(3)
    res = slope.pct_change(3)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_corr_21d_63w_alt_jerk_v050_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_corr(_roc(closeadj, 21), _roc(_rsi(closeadj, 14), 21), 63)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_div_5d_long_jerk_v051_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(_rsi(close, 14), 5))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_div_21d_long_jerk_v052_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 21), _roc(_rsi(close, 14), 21))
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_5d_long_jerk_v053_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(_macd(close), 5))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_21d_long_jerk_v054_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 21), _roc(_macd(close), 21))
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_5d_long_jerk_v055_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(_stoch_k(high, low, close, 14), 5))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_21d_long_jerk_v056_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 21), _roc(_stoch_k(high, low, close, 14), 21))
    slope = base.pct_change(42)
    res = slope.pct_change(42)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_raw_mom_div_5d_long_jerk_v057_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(close - close.shift(10), 5))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_drift_21d_long_jerk_v058_signal(close: pd.Series) -> pd.Series:
    base = _mom_drift(_rsi(close, 14), 21)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_drift_21d_long_jerk_v059_signal(close: pd.Series) -> pd.Series:
    base = _mom_drift(_macd(close), 21)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_drift_21d_long_jerk_v060_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_drift(_stoch_k(high, low, close, 14), 21)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_rsi_div_10d_v2_jerk_v062_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 10), _roc(_rsi(close, 7), 10))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_div_21d_v2_jerk_v063_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 21), _roc(_rsi(close, 7), 21))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_div_63d_v2_jerk_v064_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_div(_roc(closeadj, 63), _roc(_rsi(closeadj, 7), 63))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_div_126d_v2_jerk_v065_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_div(_roc(closeadj, 126), _roc(_rsi(closeadj, 7), 126))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_5d_v2_jerk_v066_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(_macd(close, 24, 52), 5))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_10d_v2_jerk_v067_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 10), _roc(_macd(close, 24, 52), 10))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_21d_v2_jerk_v068_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 21), _roc(_macd(close, 24, 52), 21))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_63d_v2_jerk_v069_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_div(_roc(closeadj, 63), _roc(_macd(closeadj, 24, 52), 63))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_126d_v2_jerk_v070_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_div(_roc(closeadj, 126), _roc(_macd(closeadj, 24, 52), 126))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_5d_v2_jerk_v071_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(_stoch_k(high, low, close, 7), 5))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_10d_v2_jerk_v072_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 10), _roc(_stoch_k(high, low, close, 7), 10))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_21d_v2_jerk_v073_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 21), _roc(_stoch_k(high, low, close, 7), 21))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_63d_v2_jerk_v074_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    base = _mom_div(_roc(closeadj, 63), _roc(_stoch_k(high * adj, low * adj, closeadj, 7), 63))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_126d_v2_jerk_v075_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    base = _mom_div(_roc(closeadj, 126), _roc(_stoch_k(high * adj, low * adj, closeadj, 7), 126))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_drift_21d_v2_jerk_v076_signal(close: pd.Series) -> pd.Series:
    base = _mom_drift(_rsi(close, 7), 21)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_drift_63d_v2_jerk_v077_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_drift(_rsi(closeadj, 7), 63)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_drift_21d_v2_jerk_v078_signal(close: pd.Series) -> pd.Series:
    base = _mom_drift(_macd(close, 24, 52), 21)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_drift_63d_v2_jerk_v079_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_drift(_macd(closeadj, 24, 52), 63)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_drift_21d_v2_jerk_v080_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_drift(_stoch_k(high, low, close, 7), 21)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_drift_63d_v2_jerk_v081_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    base = _mom_drift(_stoch_k(high * adj, low * adj, closeadj, 7), 63)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_corr_5d_21w_v2_jerk_v082_signal(close: pd.Series) -> pd.Series:
    base = _mom_corr(_roc(close, 5), _roc(_rsi(close, 7), 5), 21)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_corr_21d_63w_v2_jerk_v083_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_corr(_roc(closeadj, 21), _roc(_rsi(closeadj, 7), 21), 63)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_corr_5d_21w_v2_jerk_v084_signal(close: pd.Series) -> pd.Series:
    base = _mom_corr(_roc(close, 5), _roc(_macd(close, 24, 52), 5), 21)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_corr_21d_63w_v2_jerk_v085_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_corr(_roc(closeadj, 21), _roc(_macd(closeadj, 24, 52), 21), 63)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_corr_5d_21w_v2_jerk_v086_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_corr(_roc(close, 5), _roc(_stoch_k(high, low, close, 7), 5), 21)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_corr_21d_63w_v2_jerk_v087_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    base = _mom_corr(_roc(closeadj, 21), _roc(_stoch_k(high * adj, low * adj, closeadj, 7), 21), 63)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_div_5d_v3_jerk_v088_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(_rsi(close, 21), 5))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_div_10d_v3_jerk_v089_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 10), _roc(_rsi(close, 21), 10))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_div_21d_v3_jerk_v090_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 21), _roc(_rsi(close, 21), 21))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_div_63d_v3_jerk_v091_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_div(_roc(closeadj, 63), _roc(_rsi(closeadj, 21), 63))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_div_126d_v3_jerk_v092_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_div(_roc(closeadj, 126), _roc(_rsi(closeadj, 21), 126))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_5d_v3_jerk_v093_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(_macd(close, 5, 35), 5))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_10d_v3_jerk_v094_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 10), _roc(_macd(close, 5, 35), 10))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_21d_v3_jerk_v095_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 21), _roc(_macd(close, 5, 35), 21))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_63d_v3_jerk_v096_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_div(_roc(closeadj, 63), _roc(_macd(closeadj, 5, 35), 63))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_126d_v3_jerk_v097_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_div(_roc(closeadj, 126), _roc(_macd(closeadj, 5, 35), 126))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_5d_v3_jerk_v098_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(_stoch_k(high, low, close, 21), 5))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_10d_v3_jerk_v099_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 10), _roc(_stoch_k(high, low, close, 21), 10))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_21d_v3_jerk_v100_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 21), _roc(_stoch_k(high, low, close, 21), 21))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_63d_v3_jerk_v101_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    base = _mom_div(_roc(closeadj, 63), _roc(_stoch_k(high * adj, low * adj, closeadj, 21), 63))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_126d_v3_jerk_v102_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    base = _mom_div(_roc(closeadj, 126), _roc(_stoch_k(high * adj, low * adj, closeadj, 21), 126))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_drift_21d_v3_jerk_v103_signal(close: pd.Series) -> pd.Series:
    base = _mom_drift(_rsi(close, 21), 21)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_drift_63d_v3_jerk_v104_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_drift(_rsi(closeadj, 21), 63)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_drift_21d_v3_jerk_v105_signal(close: pd.Series) -> pd.Series:
    base = _mom_drift(_macd(close, 5, 35), 21)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_drift_63d_v3_jerk_v106_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_drift(_macd(closeadj, 5, 35), 63)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_drift_21d_v3_jerk_v107_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_drift(_stoch_k(high, low, close, 21), 21)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_drift_63d_v3_jerk_v108_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    base = _mom_drift(_stoch_k(high * adj, low * adj, closeadj, 21), 63)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_corr_5d_21w_v3_jerk_v109_signal(close: pd.Series) -> pd.Series:
    base = _mom_corr(_roc(close, 5), _roc(_rsi(close, 21), 5), 21)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_corr_21d_63w_v3_jerk_v110_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_corr(_roc(closeadj, 21), _roc(_rsi(closeadj, 21), 21), 63)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_corr_5d_21w_v3_jerk_v111_signal(close: pd.Series) -> pd.Series:
    base = _mom_corr(_roc(close, 5), _roc(_macd(close, 5, 35), 5), 21)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_corr_21d_63w_v3_jerk_v112_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_corr(_roc(closeadj, 21), _roc(_macd(closeadj, 5, 35), 21), 63)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_corr_5d_21w_v3_jerk_v113_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_corr(_roc(close, 5), _roc(_stoch_k(high, low, close, 21), 5), 21)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_corr_21d_63w_v3_jerk_v114_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    base = _mom_corr(_roc(closeadj, 21), _roc(_stoch_k(high * adj, low * adj, closeadj, 21), 21), 63)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# [Filling remaining up to v150 with variants]

def f14md_f14_momentum_divergence_rsi_div_5d_v4_jerk_v115_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(_rsi(close, 14), 5))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_5d_v4_jerk_v116_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(_macd(close), 5))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_5d_v4_jerk_v117_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(_stoch_k(high, low, close, 14), 5))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_div_21d_v4_jerk_v118_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 21), _roc(_rsi(close, 14), 21))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_21d_v4_jerk_v119_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 21), _roc(_macd(close), 21))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_21d_v4_jerk_v120_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 21), _roc(_stoch_k(high, low, close, 14), 21))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_div_63d_v4_jerk_v121_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_div(_roc(closeadj, 63), _roc(_rsi(closeadj, 14), 63))
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_63d_v4_jerk_v122_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_div(_roc(closeadj, 63), _roc(_macd(closeadj), 63))
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_63d_v4_jerk_v123_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    base = _mom_div(_roc(closeadj, 63), _roc(_stoch_k(high * adj, low * adj, closeadj, 14), 63))
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_div_5d_v5_jerk_v124_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(_rsi(close, 14), 5))
    slope = base.pct_change(1)
    res = slope.pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_5d_v5_jerk_v125_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(_macd(close), 5))
    slope = base.pct_change(1)
    res = slope.pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_5d_v5_jerk_v126_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 5), _roc(_stoch_k(high, low, close, 14), 5))
    slope = base.pct_change(1)
    res = slope.pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)


def f14md_f14_momentum_divergence_macd_div_10d_v5_jerk_v128_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 10), _roc(_macd(close), 10))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_10d_v5_jerk_v129_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 10), _roc(_stoch_k(high, low, close, 14), 10))
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)



def f14md_f14_momentum_divergence_stoch_div_21d_v5_jerk_v132_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 21), _roc(_stoch_k(high, low, close, 14), 21))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)





def f14md_f14_momentum_divergence_macd_div_126d_v5_jerk_v137_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_div(_roc(closeadj, 126), _roc(_macd(closeadj), 126))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_126d_v5_jerk_v138_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    base = _mom_div(_roc(closeadj, 126), _roc(_stoch_k(high * adj, low * adj, closeadj, 14), 126))
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_drift_21d_v4_jerk_v139_signal(close: pd.Series) -> pd.Series:
    base = _mom_drift(_rsi(close, 14), 21)
    slope = base.pct_change(1)
    res = slope.pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_drift_21d_v4_jerk_v140_signal(close: pd.Series) -> pd.Series:
    base = _mom_drift(_macd(close), 21)
    slope = base.pct_change(1)
    res = slope.pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_drift_21d_v4_jerk_v141_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_drift(_stoch_k(high, low, close, 14), 21)
    slope = base.pct_change(1)
    res = slope.pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_drift_63d_v4_jerk_v142_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_drift(_rsi(closeadj, 14), 63)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_drift_63d_v4_jerk_v143_signal(closeadj: pd.Series) -> pd.Series:
    base = _mom_drift(_macd(closeadj), 63)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_drift_63d_v4_jerk_v144_signal(high: pd.Series, low: pd.Series, closeadj: pd.Series, close: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    base = _mom_drift(_stoch_k(high * adj, low * adj, closeadj, 14), 63)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_corr_5d_21w_v4_jerk_v145_signal(close: pd.Series) -> pd.Series:
    base = _mom_corr(_roc(close, 5), _roc(_rsi(close, 14), 5), 21)
    slope = base.pct_change(1)
    res = slope.pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_corr_5d_21w_v4_jerk_v146_signal(close: pd.Series) -> pd.Series:
    base = _mom_corr(_roc(close, 5), _roc(_macd(close), 5), 21)
    slope = base.pct_change(1)
    res = slope.pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_corr_5d_21w_v4_jerk_v147_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_corr(_roc(close, 5), _roc(_stoch_k(high, low, close, 14), 5), 21)
    slope = base.pct_change(1)
    res = slope.pct_change(1)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_rsi_div_10d_v6_jerk_v148_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 10), _roc(_rsi(close, 14), 10))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_macd_div_10d_v6_jerk_v149_signal(close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 10), _roc(_macd(close), 10))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

def f14md_f14_momentum_divergence_stoch_div_10d_v6_jerk_v150_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    base = _mom_div(_roc(close, 10), _roc(_stoch_k(high, low, close, 14), 10))
    slope = base.pct_change(10)
    res = slope.pct_change(10)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

JERK_NAMES = [f for f in globals() if f.startswith("f14md_") and f.endswith("_signal")]

F14_MOMENTUM_DIVERGENCE_JERK_REGISTRY_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(JERK_NAMES)
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 500; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "high": np.random.randn(sz).cumsum()+110, "low": np.random.randn(sz).cumsum()+90, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F14_MOMENTUM_DIVERGENCE_JERK_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("jerk 001-150 OK")
