# f17_volatility_regime_slope_001_150_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _std(s, w):
    return s.rolling(w, min_periods=min(w, 5)).std()

def _vol_regime_score(vol, w):
    """Calculates the relative position of current volatility within its recent range."""
    return (vol - vol.rolling(w).min()) / (vol.rolling(w).max() - vol.rolling(w).min()).replace(0, np.nan)

def _vol_shock(vol, w):
    """Measures the ratio of current volatility to its moving average."""
    return vol / vol.rolling(w).mean().replace(0, np.nan)

def _vol_drift(vol, w):
    """Calculates the normalized change in volatility relative to its rolling standard deviation."""
    return (vol - vol.shift(w)) / vol.rolling(w).std().replace(0, np.nan)

def _get_vol_rs(close, w):
    """Returns the standard rolling volatility of returns."""
    return _std(close.pct_change().replace([np.inf, -np.inf], 0), w)

def _get_vol_pk(high, low, w):
    """Calculates the Parkinson volatility estimator based on High and Low prices."""
    return np.sqrt((1 / (4 * np.log(2))) * _sma(np.log(high / low.replace(0, np.nan))**2, w))

def _get_vol_hl(high, low, close, w):
    """Calculates the High-Low range normalized by the moving average of Close."""
    return _sma((high - low) / close.replace(0, np.nan), w)

def _get_vol_gk(high, low, close, w):
    """Calculates the Garman-Klass volatility estimator."""
    c_prev = close.shift(1)
    res = 0.5 * np.log(high / low.replace(0, np.nan))**2 - (2 * np.log(2) - 1) * np.log(close / c_prev.replace(0, np.nan))**2
    return np.sqrt(_sma(res.replace([np.inf, -np.inf], 0), w))

def _get_vol_tr(high, low, close, w):
    """Calculates the True Range based volatility normalized by Close."""
    cp = close.shift(1)
    tr = pd.concat([high - low, (high - cp).abs(), (low - cp).abs()], axis=1).max(axis=1)
    return _sma(tr / close.replace(0, np.nan), w)

def _get_vol_vv(close, w):
    """Calculates the volatility of volatility (VVIX-style)."""
    vol = _get_vol_rs(close, w)
    return _std(vol, w)

def _get_vol_sk(close, w):
    """Calculates the rolling skewness of returns."""
    return close.pct_change().rolling(w, min_periods=min(w, 5)).skew().abs()

def _get_vol_pr(close, w):
    """Measures the persistence of high volatility regimes."""
    vol = _get_vol_rs(close, w)
    ma = _sma(vol, w * 2)
    return _sma((vol > ma).astype(float), w)

# --- Volatility Regime Slope Features ---

# Helpers for window-based ROC
def _roc_s(s): return s.pct_change(5)
def _roc_m(s): return s.pct_change(21)
def _roc_l(s): return s.pct_change(63)

# 001-025: Regime Score Slopes (RS, PK, HL, GK, TR)
def f17vr_slope_v001_signal(close: pd.Series) -> pd.Series:
    """Slope of 5d RS vol regime score."""
    return _roc_s(_vol_regime_score(_get_vol_rs(close, 5), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v002_signal(close: pd.Series) -> pd.Series:
    """Slope of 10d RS vol regime score."""
    return _roc_s(_vol_regime_score(_get_vol_rs(close, 10), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v003_signal(close: pd.Series) -> pd.Series:
    """Slope of 21d RS vol regime score."""
    return _roc_s(_vol_regime_score(_get_vol_rs(close, 21), 42)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v004_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 63d RS vol regime score."""
    return _roc_m(_vol_regime_score(_get_vol_rs(closeadj, 63), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v005_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 126d RS vol regime score."""
    return _roc_m(_vol_regime_score(_get_vol_rs(closeadj, 126), 252)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v006_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope of 5d PK vol regime score."""
    return _roc_s(_vol_regime_score(_get_vol_pk(high, low, 5), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v007_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope of 10d PK vol regime score."""
    return _roc_s(_vol_regime_score(_get_vol_pk(high, low, 10), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v008_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope of 21d PK vol regime score."""
    return _roc_s(_vol_regime_score(_get_vol_pk(high, low, 21), 42)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v009_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 63d PK vol regime score."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_regime_score(_get_vol_pk(high * adj, low * adj, 63), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v010_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 126d PK vol regime score."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_regime_score(_get_vol_pk(high * adj, low * adj, 126), 252)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v011_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 5d HL vol regime score."""
    return _roc_s(_vol_regime_score(_get_vol_hl(high, low, close, 5), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v012_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 10d HL vol regime score."""
    return _roc_s(_vol_regime_score(_get_vol_hl(high, low, close, 10), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v013_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 21d HL vol regime score."""
    return _roc_s(_vol_regime_score(_get_vol_hl(high, low, close, 21), 42)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v014_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 63d HL vol regime score."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_regime_score(_get_vol_hl(high * adj, low * adj, closeadj, 63), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v015_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 126d HL vol regime score."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_regime_score(_get_vol_hl(high * adj, low * adj, closeadj, 126), 252)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v016_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 5d GK vol regime score."""
    return _roc_s(_vol_regime_score(_get_vol_gk(high, low, close, 5), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v017_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 10d GK vol regime score."""
    return _roc_s(_vol_regime_score(_get_vol_gk(high, low, close, 10), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v018_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 21d GK vol regime score."""
    return _roc_s(_vol_regime_score(_get_vol_gk(high, low, close, 21), 42)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v019_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 63d GK vol regime score."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_regime_score(_get_vol_gk(high * adj, low * adj, closeadj, 63), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v020_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 126d GK vol regime score."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_regime_score(_get_vol_gk(high * adj, low * adj, closeadj, 126), 252)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v021_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 5d TR vol regime score."""
    return _roc_s(_vol_regime_score(_get_vol_tr(high, low, close, 5), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v022_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 10d TR vol regime score."""
    return _roc_s(_vol_regime_score(_get_vol_tr(high, low, close, 10), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v023_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 21d TR vol regime score."""
    return _roc_s(_vol_regime_score(_get_vol_tr(high, low, close, 21), 42)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v024_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 63d TR vol regime score."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_regime_score(_get_vol_tr(high * adj, low * adj, closeadj, 63), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v025_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 126d TR vol regime score."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_regime_score(_get_vol_tr(high * adj, low * adj, closeadj, 126), 252)).replace([np.inf, -np.inf], np.nan)

# 026-050: Vol Shock Slopes
def f17vr_slope_v026_signal(close: pd.Series) -> pd.Series:
    """Slope of 5d RS vol shock."""
    return _roc_s(_vol_shock(_get_vol_rs(close, 5), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v027_signal(close: pd.Series) -> pd.Series:
    """Slope of 10d RS vol shock."""
    return _roc_s(_vol_shock(_get_vol_rs(close, 10), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v028_signal(close: pd.Series) -> pd.Series:
    """Slope of 21d RS vol shock."""
    return _roc_s(_vol_shock(_get_vol_rs(close, 21), 42)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v029_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 63d RS vol shock."""
    return _roc_m(_vol_shock(_get_vol_rs(closeadj, 63), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v030_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 126d RS vol shock."""
    return _roc_m(_vol_shock(_get_vol_rs(closeadj, 126), 252)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v031_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope of 5d PK vol shock."""
    return _roc_s(_vol_shock(_get_vol_pk(high, low, 5), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v032_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope of 10d PK vol shock."""
    return _roc_s(_vol_shock(_get_vol_pk(high, low, 10), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v033_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope of 21d PK vol shock."""
    return _roc_s(_vol_shock(_get_vol_pk(high, low, 21), 42)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v034_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 63d PK vol shock."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_shock(_get_vol_pk(high * adj, low * adj, 63), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v035_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 126d PK vol shock."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_shock(_get_vol_pk(high * adj, low * adj, 126), 252)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v036_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 5d HL vol shock."""
    return _roc_s(_vol_shock(_get_vol_hl(high, low, close, 5), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v037_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 10d HL vol shock."""
    return _roc_s(_vol_shock(_get_vol_hl(high, low, close, 10), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v038_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 21d HL vol shock."""
    return _roc_s(_vol_shock(_get_vol_hl(high, low, close, 21), 42)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v039_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 63d HL vol shock."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_shock(_get_vol_hl(high * adj, low * adj, closeadj, 63), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v040_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 126d HL vol shock."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_shock(_get_vol_hl(high * adj, low * adj, closeadj, 126), 252)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v041_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 5d GK vol shock."""
    return _roc_s(_vol_shock(_get_vol_gk(high, low, close, 5), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v042_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 10d GK vol shock."""
    return _roc_s(_vol_shock(_get_vol_gk(high, low, close, 10), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v043_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 21d GK vol shock."""
    return _roc_s(_vol_shock(_get_vol_gk(high, low, close, 21), 42)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v044_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 63d GK vol shock."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_shock(_get_vol_gk(high * adj, low * adj, closeadj, 63), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v045_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 126d GK vol shock."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_shock(_get_vol_gk(high * adj, low * adj, closeadj, 126), 252)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v046_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 5d TR vol shock."""
    return _roc_s(_vol_shock(_get_vol_tr(high, low, close, 5), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v047_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 10d TR vol shock."""
    return _roc_s(_vol_shock(_get_vol_tr(high, low, close, 10), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v048_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 21d TR vol shock."""
    return _roc_s(_vol_shock(_get_vol_tr(high, low, close, 21), 42)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v049_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 63d TR vol shock."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_shock(_get_vol_tr(high * adj, low * adj, closeadj, 63), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v050_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 126d TR vol shock."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_shock(_get_vol_tr(high * adj, low * adj, closeadj, 126), 252)).replace([np.inf, -np.inf], np.nan)

# 051-075: Vol Drift Slopes
def f17vr_slope_v051_signal(close: pd.Series) -> pd.Series:
    """Slope of 5d RS vol drift."""
    return _roc_s(_vol_drift(_get_vol_rs(close, 5), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v052_signal(close: pd.Series) -> pd.Series:
    """Slope of 10d RS vol drift."""
    return _roc_s(_vol_drift(_get_vol_rs(close, 10), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v053_signal(close: pd.Series) -> pd.Series:
    """Slope of 21d RS vol drift."""
    return _roc_s(_vol_drift(_get_vol_rs(close, 21), 42)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v054_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 63d RS vol drift."""
    return _roc_m(_vol_drift(_get_vol_rs(closeadj, 63), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v055_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 126d RS vol drift."""
    return _roc_m(_vol_drift(_get_vol_rs(closeadj, 126), 252)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v056_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope of 5d PK vol drift."""
    return _roc_s(_vol_drift(_get_vol_pk(high, low, 5), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v057_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope of 10d PK vol drift."""
    return _roc_s(_vol_drift(_get_vol_pk(high, low, 10), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v058_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope of 21d PK vol drift."""
    return _roc_s(_vol_drift(_get_vol_pk(high, low, 21), 42)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v059_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 63d PK vol drift."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_drift(_get_vol_pk(high * adj, low * adj, 63), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v060_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 126d PK vol drift."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_drift(_get_vol_pk(high * adj, low * adj, 126), 252)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v061_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 5d HL vol drift."""
    return _roc_s(_vol_drift(_get_vol_hl(high, low, close, 5), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v062_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 10d HL vol drift."""
    return _roc_s(_vol_drift(_get_vol_hl(high, low, close, 10), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v063_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 21d HL vol drift."""
    return _roc_s(_vol_drift(_get_vol_hl(high, low, close, 21), 42)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v064_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 63d HL vol drift."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_drift(_get_vol_hl(high * adj, low * adj, closeadj, 63), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v065_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 126d HL vol drift."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_drift(_get_vol_hl(high * adj, low * adj, closeadj, 126), 252)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v066_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 5d GK vol drift."""
    return _roc_s(_vol_drift(_get_vol_gk(high, low, close, 5), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v067_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 10d GK vol drift."""
    return _roc_s(_vol_drift(_get_vol_gk(high, low, close, 10), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v068_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 21d GK vol drift."""
    return _roc_s(_vol_drift(_get_vol_gk(high, low, close, 21), 42)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v069_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 63d GK vol drift."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_drift(_get_vol_gk(high * adj, low * adj, closeadj, 63), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v070_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 126d GK vol drift."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_drift(_get_vol_gk(high * adj, low * adj, closeadj, 126), 252)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v071_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 5d TR vol drift."""
    return _roc_s(_vol_drift(_get_vol_tr(high, low, close, 5), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v072_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 10d TR vol drift."""
    return _roc_s(_vol_drift(_get_vol_tr(high, low, close, 10), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v073_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 21d TR vol drift."""
    return _roc_s(_vol_drift(_get_vol_tr(high, low, close, 21), 42)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v074_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 63d TR vol drift."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_drift(_get_vol_tr(high * adj, low * adj, closeadj, 63), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v075_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 126d TR vol drift."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_drift(_get_vol_tr(high * adj, low * adj, closeadj, 126), 252)).replace([np.inf, -np.inf], np.nan)

# 076-100: VV Slopes
def f17vr_slope_v076_signal(close: pd.Series) -> pd.Series:
    """Slope of 5d VV vol regime score."""
    return _roc_s(_vol_regime_score(_get_vol_vv(close, 5), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v077_signal(close: pd.Series) -> pd.Series:
    """Slope of 10d VV vol shock."""
    return _roc_s(_vol_shock(_get_vol_vv(close, 10), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v078_signal(close: pd.Series) -> pd.Series:
    """Slope of 21d VV vol drift."""
    return _roc_s(_vol_drift(_get_vol_vv(close, 21), 42)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v079_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 63d VV vol regime score."""
    return _roc_m(_vol_regime_score(_get_vol_vv(closeadj, 63), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v080_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 126d VV vol shock."""
    return _roc_m(_vol_shock(_get_vol_vv(closeadj, 126), 252)).replace([np.inf, -np.inf], np.nan)

# 081-090: SK Slopes
def f17vr_slope_v081_signal(close: pd.Series) -> pd.Series:
    """Slope of 5d SK vol regime score."""
    return _roc_s(_vol_regime_score(_get_vol_sk(close, 5), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v082_signal(close: pd.Series) -> pd.Series:
    """Slope of 10d SK vol shock."""
    return _roc_s(_vol_shock(_get_vol_sk(close, 10), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v083_signal(close: pd.Series) -> pd.Series:
    """Slope of 21d SK vol drift."""
    return _roc_s(_vol_drift(_get_vol_sk(close, 21), 42)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v084_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 63d SK vol regime score."""
    return _roc_m(_vol_regime_score(_get_vol_sk(closeadj, 63), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v085_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 126d SK vol shock."""
    return _roc_m(_vol_shock(_get_vol_sk(closeadj, 126), 252)).replace([np.inf, -np.inf], np.nan)

# 086-095: PR Slopes
def f17vr_slope_v086_signal(close: pd.Series) -> pd.Series:
    """Slope of 5d PR vol regime score."""
    return _roc_s(_vol_regime_score(_get_vol_pr(close, 5), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v087_signal(close: pd.Series) -> pd.Series:
    """Slope of 10d PR vol shock."""
    return _roc_s(_vol_shock(_get_vol_pr(close, 10), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v088_signal(close: pd.Series) -> pd.Series:
    """Slope of 21d PR vol drift."""
    return _roc_s(_vol_drift(_get_vol_pr(close, 21), 42)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v089_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 63d PR vol regime score."""
    return _roc_m(_vol_regime_score(_get_vol_pr(closeadj, 63), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v090_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 126d PR vol shock."""
    return _roc_m(_vol_shock(_get_vol_pr(closeadj, 126), 252)).replace([np.inf, -np.inf], np.nan)

# 091-100: Long Window Slopes
def f17vr_slope_v091_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 252d HL vol regime score."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_l(_vol_regime_score(_get_vol_hl(high * adj, low * adj, closeadj, 252), 504)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v092_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 504d HL vol shock."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_l(_vol_shock(_get_vol_hl(high * adj, low * adj, closeadj, 504), 756)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v093_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 252d RS vol drift."""
    return _roc_l(_vol_drift(_get_vol_rs(closeadj, 252), 504)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v094_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 504d RS vol regime score."""
    return _roc_l(_vol_regime_score(_get_vol_rs(closeadj, 504), 756)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v095_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 252d VV vol shock."""
    return _roc_l(_vol_shock(_get_vol_vv(closeadj, 252), 504)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v096_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 504d SK vol drift."""
    return _roc_l(_vol_drift(_get_vol_sk(closeadj, 504), 756)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v097_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 252d PR vol regime score."""
    return _roc_l(_vol_regime_score(_get_vol_pr(closeadj, 252), 504)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v098_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 504d VV vol shock."""
    return _roc_l(_vol_shock(_get_vol_vv(closeadj, 504), 756)).replace([np.inf, -np.inf], np.nan)


def f17vr_slope_v100_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 504d PR vol shock."""
    return _roc_l(_vol_shock(_get_vol_pr(closeadj, 504), 756)).replace([np.inf, -np.inf], np.nan)

# Fill remaining 101-150 with variations
def f17vr_slope_v101_signal(close: pd.Series) -> pd.Series:
    """Slope of 5d RS vol shock (v2)."""
    return _roc_s(_vol_shock(_get_vol_rs(close, 5), 10)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v102_signal(close: pd.Series) -> pd.Series:
    """Slope of 10d RS vol drift (v2)."""
    return _roc_s(_vol_drift(_get_vol_rs(close, 10), 10)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v103_signal(close: pd.Series) -> pd.Series:
    """Slope of 21d RS vol regime score (v2)."""
    return _roc_s(_vol_regime_score(_get_vol_rs(close, 21), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v104_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 63d RS vol shock (v2)."""
    return _roc_m(_vol_shock(_get_vol_rs(closeadj, 63), 63)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v105_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 126d RS vol drift (v2)."""
    return _roc_m(_vol_drift(_get_vol_rs(closeadj, 126), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v106_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope of 5d PK vol shock (v2)."""
    return _roc_s(_vol_shock(_get_vol_pk(high, low, 5), 10)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v107_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope of 10d PK vol drift (v2)."""
    return _roc_s(_vol_drift(_get_vol_pk(high, low, 10), 10)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v108_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Slope of 21d PK vol regime score (v2)."""
    return _roc_s(_vol_regime_score(_get_vol_pk(high, low, 21), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v109_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 63d PK vol shock (v2)."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_shock(_get_vol_pk(high * adj, low * adj, 63), 63)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v110_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 126d PK vol drift (v2)."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_drift(_get_vol_pk(high * adj, low * adj, 126), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v111_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 5d HL vol shock (v2)."""
    return _roc_s(_vol_shock(_get_vol_hl(high, low, close, 5), 10)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v112_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 10d HL vol drift (v2)."""
    return _roc_s(_vol_drift(_get_vol_hl(high, low, close, 10), 10)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v113_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 21d HL vol regime score (v2)."""
    return _roc_s(_vol_regime_score(_get_vol_hl(high, low, close, 21), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v114_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 63d HL vol shock (v2)."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_shock(_get_vol_hl(high * adj, low * adj, closeadj, 63), 63)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v115_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 126d HL vol drift (v2)."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_drift(_get_vol_hl(high * adj, low * adj, closeadj, 126), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v116_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 5d GK vol shock (v2)."""
    return _roc_s(_vol_shock(_get_vol_gk(high, low, close, 5), 10)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v117_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 10d GK vol drift (v2)."""
    return _roc_s(_vol_drift(_get_vol_gk(high, low, close, 10), 10)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v118_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 21d GK vol regime score (v2)."""
    return _roc_s(_vol_regime_score(_get_vol_gk(high, low, close, 21), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v119_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 63d GK vol shock (v2)."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_shock(_get_vol_gk(high * adj, low * adj, closeadj, 63), 63)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v120_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 126d GK vol drift (v2)."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_drift(_get_vol_gk(high * adj, low * adj, closeadj, 126), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v121_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 5d TR vol shock (v2)."""
    return _roc_s(_vol_shock(_get_vol_tr(high, low, close, 5), 10)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v122_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 10d TR vol drift (v2)."""
    return _roc_s(_vol_drift(_get_vol_tr(high, low, close, 10), 10)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v123_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of 21d TR vol regime score (v2)."""
    return _roc_s(_vol_regime_score(_get_vol_tr(high, low, close, 21), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v124_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 63d TR vol shock (v2)."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_shock(_get_vol_tr(high * adj, low * adj, closeadj, 63), 63)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v125_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 126d TR vol drift (v2)."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_m(_vol_drift(_get_vol_tr(high * adj, low * adj, closeadj, 126), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v126_signal(close: pd.Series) -> pd.Series:
    """Slope of 5d VV vol shock (v2)."""
    return _roc_s(_vol_shock(_get_vol_vv(close, 5), 10)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v127_signal(close: pd.Series) -> pd.Series:
    """Slope of 10d VV vol drift (v2)."""
    return _roc_s(_vol_drift(_get_vol_vv(close, 10), 10)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v128_signal(close: pd.Series) -> pd.Series:
    """Slope of 21d VV vol regime score (v2)."""
    return _roc_s(_vol_regime_score(_get_vol_vv(close, 21), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v129_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 63d VV vol shock (v2)."""
    return _roc_m(_vol_shock(_get_vol_vv(closeadj, 63), 63)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v130_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 126d VV vol drift (v2)."""
    return _roc_m(_vol_drift(_get_vol_vv(closeadj, 126), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v131_signal(close: pd.Series) -> pd.Series:
    """Slope of 5d SK vol shock (v2)."""
    return _roc_s(_vol_shock(_get_vol_sk(close, 5), 10)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v132_signal(close: pd.Series) -> pd.Series:
    """Slope of 10d SK vol drift (v2)."""
    return _roc_s(_vol_drift(_get_vol_sk(close, 10), 10)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v133_signal(close: pd.Series) -> pd.Series:
    """Slope of 21d SK vol regime score (v2)."""
    return _roc_s(_vol_regime_score(_get_vol_sk(close, 21), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v134_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 63d SK vol shock (v2)."""
    return _roc_m(_vol_shock(_get_vol_sk(closeadj, 63), 63)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v135_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 126d SK vol drift (v2)."""
    return _roc_m(_vol_drift(_get_vol_sk(closeadj, 126), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v136_signal(close: pd.Series) -> pd.Series:
    """Slope of 5d PR vol shock (v2)."""
    return _roc_s(_vol_shock(_get_vol_pr(close, 5), 10)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v137_signal(close: pd.Series) -> pd.Series:
    """Slope of 10d PR vol drift (v2)."""
    return _roc_s(_vol_drift(_get_vol_pr(close, 10), 10)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v138_signal(close: pd.Series) -> pd.Series:
    """Slope of 21d PR vol regime score (v2)."""
    return _roc_s(_vol_regime_score(_get_vol_pr(close, 21), 21)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v139_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 63d PR vol shock (v2)."""
    return _roc_m(_vol_shock(_get_vol_pr(closeadj, 63), 63)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v140_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 126d PR vol drift (v2)."""
    return _roc_m(_vol_drift(_get_vol_pr(closeadj, 126), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v141_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 252d HL vol shock (v2)."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_l(_vol_shock(_get_vol_hl(high * adj, low * adj, closeadj, 252), 252)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v142_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Slope of 504d HL vol drift (v2)."""
    adj = closeadj / close.replace(0, np.nan)
    return _roc_l(_vol_drift(_get_vol_hl(high * adj, low * adj, closeadj, 504), 504)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v143_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 252d RS vol regime score (v2)."""
    return _roc_l(_vol_regime_score(_get_vol_rs(closeadj, 252), 252)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v144_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 504d RS vol shock (v2)."""
    return _roc_l(_vol_shock(_get_vol_rs(closeadj, 504), 504)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v145_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 252d VV vol drift (v2)."""
    return _roc_l(_vol_drift(_get_vol_vv(closeadj, 252), 252)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v146_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 504d SK vol regime score (v2)."""
    return _roc_l(_vol_regime_score(_get_vol_sk(closeadj, 504), 504)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v147_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 252d PR vol shock (v2)."""
    return _roc_l(_vol_shock(_get_vol_pr(closeadj, 252), 252)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v148_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 504d VV vol drift (v2)."""
    return _roc_l(_vol_drift(_get_vol_vv(closeadj, 504), 504)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v149_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 252d RS vol regime score (v3)."""
    return _roc_l(_vol_regime_score(_get_vol_rs(closeadj, 252), 126)).replace([np.inf, -np.inf], np.nan)

def f17vr_slope_v150_signal(closeadj: pd.Series) -> pd.Series:
    """Slope of 504d PR vol drift (v2)."""
    return _roc_l(_vol_drift(_get_vol_pr(closeadj, 504), 504)).replace([np.inf, -np.inf], np.nan)

# --- Registry and Self-Test ---

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

FEATURE_NAMES = [f for f in globals() if f.startswith("f17vr_") and f.endswith("_signal")]

F17_VOLATILITY_REGIME_SLOPE_001_150_REGISTRY = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(FEATURE_NAMES)
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 500; d = pd.DataFrame({
        "close": np.random.randn(sz).cumsum()+100, 
        "closeadj": np.random.randn(sz).cumsum()+100, 
        "high": np.random.randn(sz).cumsum()+110, 
        "low": np.random.randn(sz).cumsum()+90, 
        "ticker": ["T"]*sz, 
        "date": pd.date_range("2020-01-01", periods=sz)
    })
    for n, c in F17_VOLATILITY_REGIME_SLOPE_001_150_REGISTRY.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("slope 001_150 OK")
