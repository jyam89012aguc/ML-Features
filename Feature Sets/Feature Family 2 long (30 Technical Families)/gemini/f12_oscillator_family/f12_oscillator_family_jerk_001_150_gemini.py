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

# RSI Jerk Features (v001-v030)

# RSI 2-day jerk oscillator
def f12osc_rsi_2d_jerk_v001_signal(close: pd.Series) -> pd.Series:
    res = _rsi(close, 2).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 3-day jerk oscillator
def f12osc_rsi_3d_jerk_v002_signal(close: pd.Series) -> pd.Series:
    res = _rsi(close, 3).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 5-day jerk oscillator
def f12osc_rsi_5d_jerk_v003_signal(close: pd.Series) -> pd.Series:
    res = _rsi(close, 5).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 8-day jerk oscillator
def f12osc_rsi_8d_jerk_v004_signal(close: pd.Series) -> pd.Series:
    res = _rsi(close, 8).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 14-day jerk oscillator
def f12osc_rsi_14d_jerk_v005_signal(close: pd.Series) -> pd.Series:
    res = _rsi(close, 14).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 21-day jerk oscillator
def f12osc_rsi_21d_jerk_v006_signal(close: pd.Series) -> pd.Series:
    res = _rsi(close, 21).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 34-day jerk oscillator using closeadj
def f12osc_rsi_34d_jerk_v007_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 34).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 55-day jerk oscillator using closeadj
def f12osc_rsi_55d_jerk_v008_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 55).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 89-day jerk oscillator using closeadj
def f12osc_rsi_89d_jerk_v009_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 89).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 144-day jerk oscillator using closeadj
def f12osc_rsi_144d_jerk_v010_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 144).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 233-day jerk oscillator using closeadj
def f12osc_rsi_233d_jerk_v011_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 233).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 10-day jerk oscillator
def f12osc_rsi_10d_jerk_v012_signal(close: pd.Series) -> pd.Series:
    res = _rsi(close, 10).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 20-day jerk oscillator
def f12osc_rsi_20d_jerk_v013_signal(close: pd.Series) -> pd.Series:
    res = _rsi(close, 20).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 50-day jerk oscillator using closeadj
def f12osc_rsi_50d_jerk_v014_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 50).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 100-day jerk oscillator using closeadj
def f12osc_rsi_100d_jerk_v015_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 100).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 150-day jerk oscillator using closeadj
def f12osc_rsi_150d_jerk_v016_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 150).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 200-day jerk oscillator using closeadj
def f12osc_rsi_200d_jerk_v017_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 200).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 250-day jerk oscillator using closeadj
def f12osc_rsi_250d_jerk_v018_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 250).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 7-day jerk oscillator
def f12osc_rsi_7d_jerk_v019_signal(close: pd.Series) -> pd.Series:
    res = _rsi(close, 7).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 9-day jerk oscillator
def f12osc_rsi_9d_jerk_v020_signal(close: pd.Series) -> pd.Series:
    res = _rsi(close, 9).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 12-day jerk oscillator
def f12osc_rsi_12d_jerk_v021_signal(close: pd.Series) -> pd.Series:
    res = _rsi(close, 12).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 18-day jerk oscillator
def f12osc_rsi_18d_jerk_v022_signal(close: pd.Series) -> pd.Series:
    res = _rsi(close, 18).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 25-day jerk oscillator using closeadj
def f12osc_rsi_25d_jerk_v023_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 25).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 30-day jerk oscillator using closeadj
def f12osc_rsi_30d_jerk_v024_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 30).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 40-day jerk oscillator using closeadj
def f12osc_rsi_40d_jerk_v025_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 40).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 60-day jerk oscillator using closeadj
def f12osc_rsi_60d_jerk_v026_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 60).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 70-day jerk oscillator using closeadj
def f12osc_rsi_70d_jerk_v027_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 70).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 80-day jerk oscillator using closeadj
def f12osc_rsi_80d_jerk_v028_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 80).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 90-day jerk oscillator using closeadj
def f12osc_rsi_90d_jerk_v029_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 90).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 110-day jerk oscillator using closeadj
def f12osc_rsi_110d_jerk_v030_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 110).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K Jerk Features (v031-v060)

# Stochastic %K 5-day jerk oscillator
def f12osc_stoch_k_5d_jerk_v031_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _stoch(high, low, close, 5).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 10-day jerk oscillator
def f12osc_stoch_k_10d_jerk_v032_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _stoch(high, low, close, 10).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 14-day jerk oscillator
def f12osc_stoch_k_14d_jerk_v033_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _stoch(high, low, close, 14).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 21-day jerk oscillator
def f12osc_stoch_k_21d_jerk_v034_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _stoch(high, low, close, 21).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 42-day jerk oscillator using closeadj
def f12osc_stoch_k_42d_jerk_v035_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 42).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 63-day jerk oscillator using closeadj
def f12osc_stoch_k_63d_jerk_v036_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 63).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 126-day jerk oscillator using closeadj
def f12osc_stoch_k_126d_jerk_v037_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 126).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 252-day jerk oscillator using closeadj
def f12osc_stoch_k_252d_jerk_v038_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 252).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 3-day jerk oscillator
def f12osc_stoch_k_3d_jerk_v039_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _stoch(high, low, close, 3).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 8-day jerk oscillator
def f12osc_stoch_k_8d_jerk_v040_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _stoch(high, low, close, 8).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 34-day jerk oscillator using closeadj
def f12osc_stoch_k_34d_jerk_v041_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 34).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 55-day jerk oscillator using closeadj
def f12osc_stoch_k_55d_jerk_v042_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 55).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 89-day jerk oscillator using closeadj
def f12osc_stoch_k_89d_jerk_v043_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 89).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 144-day jerk oscillator using closeadj
def f12osc_stoch_k_144d_jerk_v044_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 144).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 233-day jerk oscillator using closeadj
def f12osc_stoch_k_233d_jerk_v045_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 233).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 15-day jerk oscillator
def f12osc_stoch_k_15d_jerk_v046_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _stoch(high, low, close, 15).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 18-day jerk oscillator
def f12osc_stoch_k_18d_jerk_v047_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _stoch(high, low, close, 18).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 25-day jerk oscillator using closeadj
def f12osc_stoch_k_25d_jerk_v048_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 25).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 30-day jerk oscillator using closeadj
def f12osc_stoch_k_30d_jerk_v049_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 30).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 40-day jerk oscillator using closeadj
def f12osc_stoch_k_40d_jerk_v050_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 40).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 50-day jerk oscillator using closeadj
def f12osc_stoch_k_50d_jerk_v051_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 50).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 60-day jerk oscillator using closeadj
def f12osc_stoch_k_60d_jerk_v052_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 60).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 70-day jerk oscillator using closeadj
def f12osc_stoch_k_70d_jerk_v053_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 70).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 80-day jerk oscillator using closeadj
def f12osc_stoch_k_80d_jerk_v054_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 80).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 90-day jerk oscillator using closeadj
def f12osc_stoch_k_90d_jerk_v055_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 90).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 100-day jerk oscillator using closeadj
def f12osc_stoch_k_100d_jerk_v056_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 100).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 110-day jerk oscillator using closeadj
def f12osc_stoch_k_110d_jerk_v057_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 110).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 120-day jerk oscillator using closeadj
def f12osc_stoch_k_120d_jerk_v058_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 120).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 150-day jerk oscillator using closeadj
def f12osc_stoch_k_150d_jerk_v059_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 150).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 200-day jerk oscillator using closeadj
def f12osc_stoch_k_200d_jerk_v060_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 200).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D Jerk Features (v061-v090)

# Stochastic %D 5-day jerk oscillator
def f12osc_stoch_d_5d_jerk_v061_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch(high, low, close, 5)
    res = _sma(k, 3).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 10-day jerk oscillator
def f12osc_stoch_d_10d_jerk_v062_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch(high, low, close, 10)
    res = _sma(k, 3).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 14-day jerk oscillator
def f12osc_stoch_d_14d_jerk_v063_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch(high, low, close, 14)
    res = _sma(k, 3).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 21-day jerk oscillator
def f12osc_stoch_d_21d_jerk_v064_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch(high, low, close, 21)
    res = _sma(k, 3).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 42-day jerk oscillator using closeadj
def f12osc_stoch_d_42d_jerk_v065_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 42)
    res = _sma(k, 3).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 63-day jerk oscillator using closeadj
def f12osc_stoch_d_63d_jerk_v066_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 63)
    res = _sma(k, 3).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 126-day jerk oscillator using closeadj
def f12osc_stoch_d_126d_jerk_v067_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 126)
    res = _sma(k, 3).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 252-day jerk oscillator using closeadj
def f12osc_stoch_d_252d_jerk_v068_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 252)
    res = _sma(k, 3).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 3-day jerk oscillator
def f12osc_stoch_d_3d_jerk_v069_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch(high, low, close, 3)
    res = _sma(k, 3).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 8-day jerk oscillator
def f12osc_stoch_d_8d_jerk_v070_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch(high, low, close, 8)
    res = _sma(k, 3).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 34-day jerk oscillator using closeadj
def f12osc_stoch_d_34d_jerk_v071_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 34)
    res = _sma(k, 3).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 55-day jerk oscillator using closeadj
def f12osc_stoch_d_55d_jerk_v072_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 55)
    res = _sma(k, 3).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 89-day jerk oscillator using closeadj
def f12osc_stoch_d_89d_jerk_v073_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 89)
    res = _sma(k, 3).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 144-day jerk oscillator using closeadj
def f12osc_stoch_d_144d_jerk_v074_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 144)
    res = _sma(k, 3).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 233-day jerk oscillator using closeadj
def f12osc_stoch_d_233d_jerk_v075_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 233)
    res = _sma(k, 3).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 15-day jerk oscillator
def f12osc_stoch_d_15d_jerk_v076_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch(high, low, close, 15)
    res = _sma(k, 3).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 18-day jerk oscillator
def f12osc_stoch_d_18d_jerk_v077_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch(high, low, close, 18)
    res = _sma(k, 3).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 25-day jerk oscillator using closeadj
def f12osc_stoch_d_25d_jerk_v078_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 25)
    res = _sma(k, 3).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 30-day jerk oscillator using closeadj
def f12osc_stoch_d_30d_jerk_v079_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 30)
    res = _sma(k, 3).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 40-day jerk oscillator using closeadj
def f12osc_stoch_d_40d_jerk_v080_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 40)
    res = _sma(k, 3).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 50-day jerk oscillator using closeadj
def f12osc_stoch_d_50d_jerk_v081_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 50)
    res = _sma(k, 3).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 60-day jerk oscillator using closeadj
def f12osc_stoch_d_60d_jerk_v082_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 60)
    res = _sma(k, 3).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 70-day jerk oscillator using closeadj
def f12osc_stoch_d_70d_jerk_v083_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 70)
    res = _sma(k, 3).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 80-day jerk oscillator using closeadj
def f12osc_stoch_d_80d_jerk_v084_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 80)
    res = _sma(k, 3).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 90-day jerk oscillator using closeadj
def f12osc_stoch_d_90d_jerk_v085_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 90)
    res = _sma(k, 3).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 100-day jerk oscillator using closeadj
def f12osc_stoch_d_100d_jerk_v086_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 100)
    res = _sma(k, 3).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 110-day jerk oscillator using closeadj
def f12osc_stoch_d_110d_jerk_v087_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 110)
    res = _sma(k, 3).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 120-day jerk oscillator using closeadj
def f12osc_stoch_d_120d_jerk_v088_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 120)
    res = _sma(k, 3).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 150-day jerk oscillator using closeadj
def f12osc_stoch_d_150d_jerk_v089_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 150)
    res = _sma(k, 3).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 200-day jerk oscillator using closeadj
def f12osc_stoch_d_200d_jerk_v090_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 200)
    res = _sma(k, 3).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R Jerk Features (v091-v120)

# Williams %R 5-day jerk oscillator
def f12osc_williams_r_5d_jerk_v091_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _williams_r(high, low, close, 5).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 10-day jerk oscillator
def f12osc_williams_r_10d_jerk_v092_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _williams_r(high, low, close, 10).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 14-day jerk oscillator
def f12osc_williams_r_14d_jerk_v093_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _williams_r(high, low, close, 14).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 21-day jerk oscillator
def f12osc_williams_r_21d_jerk_v094_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _williams_r(high, low, close, 21).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 42-day jerk oscillator using closeadj
def f12osc_williams_r_42d_jerk_v095_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 42).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 63-day jerk oscillator using closeadj
def f12osc_williams_r_63d_jerk_v096_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 63).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 126-day jerk oscillator using closeadj
def f12osc_williams_r_126d_jerk_v097_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 126).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 252-day jerk oscillator using closeadj
def f12osc_williams_r_252d_jerk_v098_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 252).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 3-day jerk oscillator
def f12osc_williams_r_3d_jerk_v099_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _williams_r(high, low, close, 3).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 8-day jerk oscillator
def f12osc_williams_r_8d_jerk_v100_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _williams_r(high, low, close, 8).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 34-day jerk oscillator using closeadj
def f12osc_williams_r_34d_jerk_v101_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 34).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 55-day jerk oscillator using closeadj
def f12osc_williams_r_55d_jerk_v102_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 55).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 89-day jerk oscillator using closeadj
def f12osc_williams_r_89d_jerk_v103_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 89).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 144-day jerk oscillator using closeadj
def f12osc_williams_r_144d_jerk_v104_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 144).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 233-day jerk oscillator using closeadj
def f12osc_williams_r_233d_jerk_v105_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 233).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 7-day jerk oscillator
def f12osc_williams_r_7d_jerk_v106_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _williams_r(high, low, close, 7).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 12-day jerk oscillator
def f12osc_williams_r_12d_jerk_v107_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _williams_r(high, low, close, 12).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 18-day jerk oscillator
def f12osc_williams_r_18d_jerk_v108_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _williams_r(high, low, close, 18).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 25-day jerk oscillator using closeadj
def f12osc_williams_r_25d_jerk_v109_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 25).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 30-day jerk oscillator using closeadj
def f12osc_williams_r_30d_jerk_v110_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 30).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 40-day jerk oscillator using closeadj
def f12osc_williams_r_40d_jerk_v111_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 40).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 50-day jerk oscillator using closeadj
def f12osc_williams_r_50d_jerk_v112_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 50).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 60-day jerk oscillator using closeadj
def f12osc_williams_r_60d_jerk_v113_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 60).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 70-day jerk oscillator using closeadj
def f12osc_williams_r_70d_jerk_v114_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 70).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 80-day jerk oscillator using closeadj
def f12osc_williams_r_80d_jerk_v115_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 80).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 90-day jerk oscillator using closeadj
def f12osc_williams_r_90d_jerk_v116_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 90).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 100-day jerk oscillator using closeadj
def f12osc_williams_r_100d_jerk_v117_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 100).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 110-day jerk oscillator using closeadj
def f12osc_williams_r_110d_jerk_v118_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 110).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 120-day jerk oscillator using closeadj
def f12osc_williams_r_120d_jerk_v119_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 120).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 150-day jerk oscillator using closeadj
def f12osc_williams_r_150d_jerk_v120_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 150).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI Jerk Features (v121-v150)

# CCI 5-day jerk oscillator
def f12osc_cci_5d_jerk_v121_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _cci(high, low, close, 5).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 10-day jerk oscillator
def f12osc_cci_10d_jerk_v122_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _cci(high, low, close, 10).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 14-day jerk oscillator
def f12osc_cci_14d_jerk_v123_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _cci(high, low, close, 14).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 21-day jerk oscillator
def f12osc_cci_21d_jerk_v124_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _cci(high, low, close, 21).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 42-day jerk oscillator using closeadj
def f12osc_cci_42d_jerk_v125_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 42).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 63-day jerk oscillator using closeadj
def f12osc_cci_63d_jerk_v126_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 63).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 126-day jerk oscillator using closeadj
def f12osc_cci_126d_jerk_v127_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 126).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 252-day jerk oscillator using closeadj
def f12osc_cci_252d_jerk_v128_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 252).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 3-day jerk oscillator
def f12osc_cci_3d_jerk_v129_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _cci(high, low, close, 3).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 8-day jerk oscillator
def f12osc_cci_8d_jerk_v130_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _cci(high, low, close, 8).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 34-day jerk oscillator using closeadj
def f12osc_cci_34d_jerk_v131_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 34).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 55-day jerk oscillator using closeadj
def f12osc_cci_55d_jerk_v132_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 55).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 89-day jerk oscillator using closeadj
def f12osc_cci_89d_jerk_v133_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 89).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 144-day jerk oscillator using closeadj
def f12osc_cci_144d_jerk_v134_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 144).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 233-day jerk oscillator using closeadj
def f12osc_cci_233d_jerk_v135_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 233).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 15-day jerk oscillator
def f12osc_cci_15d_jerk_v136_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _cci(high, low, close, 15).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 18-day jerk oscillator
def f12osc_cci_18d_jerk_v137_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _cci(high, low, close, 18).pct_change(5).pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 25-day jerk oscillator using closeadj
def f12osc_cci_25d_jerk_v138_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 25).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 30-day jerk oscillator using closeadj
def f12osc_cci_30d_jerk_v139_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 30).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 40-day jerk oscillator using closeadj
def f12osc_cci_40d_jerk_v140_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 40).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 50-day jerk oscillator using closeadj
def f12osc_cci_50d_jerk_v141_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 50).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 60-day jerk oscillator using closeadj
def f12osc_cci_60d_jerk_v142_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 60).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 70-day jerk oscillator using closeadj
def f12osc_cci_70d_jerk_v143_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 70).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 80-day jerk oscillator using closeadj
def f12osc_cci_80d_jerk_v144_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 80).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 90-day jerk oscillator using closeadj
def f12osc_cci_90d_jerk_v145_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 90).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 100-day jerk oscillator using closeadj
def f12osc_cci_100d_jerk_v146_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 100).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 110-day jerk oscillator using closeadj
def f12osc_cci_110d_jerk_v147_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 110).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 120-day jerk oscillator using closeadj
def f12osc_cci_120d_jerk_v148_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 120).pct_change(21).pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 150-day jerk oscillator using closeadj
def f12osc_cci_150d_jerk_v149_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 150).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 200-day jerk oscillator using closeadj
def f12osc_cci_200d_jerk_v150_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 200).pct_change(63).pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

JERK_NAMES = [f for f in globals() if f.startswith("f12osc_") and f.endswith("_signal")]

F12_OSCILLATOR_FAMILY_JERK_REGISTRY_001_150 = {
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
    for n, c in F12_OSCILLATOR_FAMILY_JERK_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("jerk 001-150 OK")
