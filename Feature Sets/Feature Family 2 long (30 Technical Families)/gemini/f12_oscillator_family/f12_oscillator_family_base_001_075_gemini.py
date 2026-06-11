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

# RSI Base Features (v001-v015)

# RSI 2-day base oscillator
def f12osc_rsi_2d_base_v001_signal(close: pd.Series) -> pd.Series:
    res = _rsi(close, 2)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 3-day base oscillator
def f12osc_rsi_3d_base_v002_signal(close: pd.Series) -> pd.Series:
    res = _rsi(close, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 5-day base oscillator
def f12osc_rsi_5d_base_v003_signal(close: pd.Series) -> pd.Series:
    res = _rsi(close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 8-day base oscillator
def f12osc_rsi_8d_base_v004_signal(close: pd.Series) -> pd.Series:
    res = _rsi(close, 8)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 14-day base oscillator
def f12osc_rsi_14d_base_v005_signal(close: pd.Series) -> pd.Series:
    res = _rsi(close, 14)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 21-day base oscillator
def f12osc_rsi_21d_base_v006_signal(close: pd.Series) -> pd.Series:
    res = _rsi(close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 34-day base oscillator using closeadj
def f12osc_rsi_34d_base_v007_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 34)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 55-day base oscillator using closeadj
def f12osc_rsi_55d_base_v008_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 55)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 89-day base oscillator using closeadj
def f12osc_rsi_89d_base_v009_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 89)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 144-day base oscillator using closeadj
def f12osc_rsi_144d_base_v010_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 144)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 233-day base oscillator using closeadj
def f12osc_rsi_233d_base_v011_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 233)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 10-day base oscillator
def f12osc_rsi_10d_base_v012_signal(close: pd.Series) -> pd.Series:
    res = _rsi(close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 20-day base oscillator
def f12osc_rsi_20d_base_v013_signal(close: pd.Series) -> pd.Series:
    res = _rsi(close, 20)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 50-day base oscillator using closeadj
def f12osc_rsi_50d_base_v014_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 50)
    return res.replace([np.inf, -np.inf], np.nan)

# RSI 100-day base oscillator using closeadj
def f12osc_rsi_100d_base_v015_signal(closeadj: pd.Series) -> pd.Series:
    res = _rsi(closeadj, 100)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K Base Features (v016-v030)

# Stochastic %K 5-day base oscillator
def f12osc_stoch_k_5d_base_v016_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _stoch(high, low, close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 10-day base oscillator
def f12osc_stoch_k_10d_base_v017_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _stoch(high, low, close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 14-day base oscillator
def f12osc_stoch_k_14d_base_v018_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _stoch(high, low, close, 14)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 21-day base oscillator
def f12osc_stoch_k_21d_base_v019_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _stoch(high, low, close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 42-day base oscillator using closeadj
def f12osc_stoch_k_42d_base_v020_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 63-day base oscillator using closeadj
def f12osc_stoch_k_63d_base_v021_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 126-day base oscillator using closeadj
def f12osc_stoch_k_126d_base_v022_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 252-day base oscillator using closeadj
def f12osc_stoch_k_252d_base_v023_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 3-day base oscillator
def f12osc_stoch_k_3d_base_v024_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _stoch(high, low, close, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 8-day base oscillator
def f12osc_stoch_k_8d_base_v025_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _stoch(high, low, close, 8)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 34-day base oscillator using closeadj
def f12osc_stoch_k_34d_base_v026_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 34)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 55-day base oscillator using closeadj
def f12osc_stoch_k_55d_base_v027_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 55)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 89-day base oscillator using closeadj
def f12osc_stoch_k_89d_base_v028_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 89)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 144-day base oscillator using closeadj
def f12osc_stoch_k_144d_base_v029_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 144)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %K 233-day base oscillator using closeadj
def f12osc_stoch_k_233d_base_v030_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _stoch(high * adj, low * adj, closeadj, 233)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D Base Features (v031-v045)

# Stochastic %D 5-day base oscillator
def f12osc_stoch_d_5d_base_v031_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch(high, low, close, 5)
    res = _sma(k, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 10-day base oscillator
def f12osc_stoch_d_10d_base_v032_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch(high, low, close, 10)
    res = _sma(k, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 14-day base oscillator
def f12osc_stoch_d_14d_base_v033_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch(high, low, close, 14)
    res = _sma(k, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 21-day base oscillator
def f12osc_stoch_d_21d_base_v034_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch(high, low, close, 21)
    res = _sma(k, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 42-day base oscillator using closeadj
def f12osc_stoch_d_42d_base_v035_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 42)
    res = _sma(k, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 63-day base oscillator using closeadj
def f12osc_stoch_d_63d_base_v036_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 63)
    res = _sma(k, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 126-day base oscillator using closeadj
def f12osc_stoch_d_126d_base_v037_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 126)
    res = _sma(k, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 252-day base oscillator using closeadj
def f12osc_stoch_d_252d_base_v038_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 252)
    res = _sma(k, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 3-day base oscillator
def f12osc_stoch_d_3d_base_v039_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch(high, low, close, 3)
    res = _sma(k, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 8-day base oscillator
def f12osc_stoch_d_8d_base_v040_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    k = _stoch(high, low, close, 8)
    res = _sma(k, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 34-day base oscillator using closeadj
def f12osc_stoch_d_34d_base_v041_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 34)
    res = _sma(k, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 55-day base oscillator using closeadj
def f12osc_stoch_d_55d_base_v042_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 55)
    res = _sma(k, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 89-day base oscillator using closeadj
def f12osc_stoch_d_89d_base_v043_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 89)
    res = _sma(k, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 144-day base oscillator using closeadj
def f12osc_stoch_d_144d_base_v044_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 144)
    res = _sma(k, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Stochastic %D 233-day base oscillator using closeadj
def f12osc_stoch_d_233d_base_v045_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    k = _stoch(high * adj, low * adj, closeadj, 233)
    res = _sma(k, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R Base Features (v046-v060)

# Williams %R 5-day base oscillator
def f12osc_williams_r_5d_base_v046_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _williams_r(high, low, close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 10-day base oscillator
def f12osc_williams_r_10d_base_v047_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _williams_r(high, low, close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 14-day base oscillator
def f12osc_williams_r_14d_base_v048_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _williams_r(high, low, close, 14)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 21-day base oscillator
def f12osc_williams_r_21d_base_v049_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _williams_r(high, low, close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 42-day base oscillator using closeadj
def f12osc_williams_r_42d_base_v050_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 63-day base oscillator using closeadj
def f12osc_williams_r_63d_base_v051_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 126-day base oscillator using closeadj
def f12osc_williams_r_126d_base_v052_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 252-day base oscillator using closeadj
def f12osc_williams_r_252d_base_v053_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 3-day base oscillator
def f12osc_williams_r_3d_base_v054_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _williams_r(high, low, close, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 8-day base oscillator
def f12osc_williams_r_8d_base_v055_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _williams_r(high, low, close, 8)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 34-day base oscillator using closeadj
def f12osc_williams_r_34d_base_v056_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 34)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 55-day base oscillator using closeadj
def f12osc_williams_r_55d_base_v057_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 55)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 89-day base oscillator using closeadj
def f12osc_williams_r_89d_base_v058_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 89)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 144-day base oscillator using closeadj
def f12osc_williams_r_144d_base_v059_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 144)
    return res.replace([np.inf, -np.inf], np.nan)

# Williams %R 233-day base oscillator using closeadj
def f12osc_williams_r_233d_base_v060_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _williams_r(high * adj, low * adj, closeadj, 233)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI Base Features (v061-v075)

# CCI 5-day base oscillator
def f12osc_cci_5d_base_v061_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _cci(high, low, close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 10-day base oscillator
def f12osc_cci_10d_base_v062_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _cci(high, low, close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 14-day base oscillator
def f12osc_cci_14d_base_v063_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _cci(high, low, close, 14)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 21-day base oscillator
def f12osc_cci_21d_base_v064_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _cci(high, low, close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 42-day base oscillator using closeadj
def f12osc_cci_42d_base_v065_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 63-day base oscillator using closeadj
def f12osc_cci_63d_base_v066_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 126-day base oscillator using closeadj
def f12osc_cci_126d_base_v067_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 252-day base oscillator using closeadj
def f12osc_cci_252d_base_v068_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 3-day base oscillator
def f12osc_cci_3d_base_v069_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _cci(high, low, close, 3)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 8-day base oscillator
def f12osc_cci_8d_base_v070_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    res = _cci(high, low, close, 8)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 34-day base oscillator using closeadj
def f12osc_cci_34d_base_v071_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 34)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 55-day base oscillator using closeadj
def f12osc_cci_55d_base_v072_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 55)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 89-day base oscillator using closeadj
def f12osc_cci_89d_base_v073_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 89)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 144-day base oscillator using closeadj
def f12osc_cci_144d_base_v074_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 144)
    return res.replace([np.inf, -np.inf], np.nan)

# CCI 233-day base oscillator using closeadj
def f12osc_cci_233d_base_v075_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    adj = closeadj / close.replace(0, np.nan)
    res = _cci(high * adj, low * adj, closeadj, 233)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

BASE_NAMES = [f for f in globals() if f.startswith("f12osc_") and f.endswith("_signal")]

F12_OSCILLATOR_FAMILY_BASE_REGISTRY_001_075 = {
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
    for n, c in F12_OSCILLATOR_FAMILY_BASE_REGISTRY_001_075.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 001-075 OK")
