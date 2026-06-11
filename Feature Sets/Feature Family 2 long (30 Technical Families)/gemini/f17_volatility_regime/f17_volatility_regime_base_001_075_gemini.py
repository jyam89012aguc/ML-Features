# f17_volatility_regime_base_001_075_gemini.py
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

# --- Volatility Regime Score Features (001-025) ---

def f17vr_vol_regime_score_rs_5d_v001_signal(close: pd.Series) -> pd.Series:
    """Volatility regime score using returns standard deviation over a 5-day window."""
    vol = _get_vol_rs(close, 5)
    res = _vol_regime_score(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_rs_10d_v002_signal(close: pd.Series) -> pd.Series:
    """Volatility regime score using returns standard deviation over a 10-day window."""
    vol = _get_vol_rs(close, 10)
    res = _vol_regime_score(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_rs_21d_v003_signal(close: pd.Series) -> pd.Series:
    """Volatility regime score using returns standard deviation over a 21-day window."""
    vol = _get_vol_rs(close, 21)
    res = _vol_regime_score(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_rs_63d_v004_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility regime score using returns standard deviation over a 63-day window."""
    vol = _get_vol_rs(closeadj, 63)
    res = _vol_regime_score(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_rs_126d_v005_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility regime score using returns standard deviation over a 126-day window."""
    vol = _get_vol_rs(closeadj, 126)
    res = _vol_regime_score(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_pk_5d_v006_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Volatility regime score using Parkinson volatility over a 5-day window."""
    vol = _get_vol_pk(high, low, 5)
    res = _vol_regime_score(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_pk_10d_v007_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Volatility regime score using Parkinson volatility over a 10-day window."""
    vol = _get_vol_pk(high, low, 10)
    res = _vol_regime_score(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_pk_21d_v008_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Volatility regime score using Parkinson volatility over a 21-day window."""
    vol = _get_vol_pk(high, low, 21)
    res = _vol_regime_score(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_pk_63d_v009_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility regime score using Parkinson volatility over a 63-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_pk(high * adj, low * adj, 63)
    res = _vol_regime_score(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_pk_126d_v010_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility regime score using Parkinson volatility over a 126-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_pk(high * adj, low * adj, 126)
    res = _vol_regime_score(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_hl_5d_v011_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility regime score using High-Low range over a 5-day window."""
    vol = _get_vol_hl(high, low, close, 5)
    res = _vol_regime_score(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_hl_10d_v012_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility regime score using High-Low range over a 10-day window."""
    vol = _get_vol_hl(high, low, close, 10)
    res = _vol_regime_score(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_hl_21d_v013_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility regime score using High-Low range over a 21-day window."""
    vol = _get_vol_hl(high, low, close, 21)
    res = _vol_regime_score(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_hl_63d_v014_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility regime score using High-Low range over a 63-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_hl(high * adj, low * adj, closeadj, 63)
    res = _vol_regime_score(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_hl_126d_v015_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility regime score using High-Low range over a 126-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_hl(high * adj, low * adj, closeadj, 126)
    res = _vol_regime_score(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_gk_5d_v016_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility regime score using Garman-Klass volatility over a 5-day window."""
    vol = _get_vol_gk(high, low, close, 5)
    res = _vol_regime_score(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_gk_10d_v017_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility regime score using Garman-Klass volatility over a 10-day window."""
    vol = _get_vol_gk(high, low, close, 10)
    res = _vol_regime_score(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_gk_21d_v018_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility regime score using Garman-Klass volatility over a 21-day window."""
    vol = _get_vol_gk(high, low, close, 21)
    res = _vol_regime_score(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_gk_63d_v019_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility regime score using Garman-Klass volatility over a 63-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_gk(high * adj, low * adj, closeadj, 63)
    res = _vol_regime_score(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_gk_126d_v020_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility regime score using Garman-Klass volatility over a 126-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_gk(high * adj, low * adj, closeadj, 126)
    res = _vol_regime_score(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_tr_5d_v021_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility regime score using True Range volatility over a 5-day window."""
    vol = _get_vol_tr(high, low, close, 5)
    res = _vol_regime_score(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_tr_10d_v022_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility regime score using True Range volatility over a 10-day window."""
    vol = _get_vol_tr(high, low, close, 10)
    res = _vol_regime_score(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_tr_21d_v023_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility regime score using True Range volatility over a 21-day window."""
    vol = _get_vol_tr(high, low, close, 21)
    res = _vol_regime_score(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_tr_63d_v024_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility regime score using True Range volatility over a 63-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_tr(high * adj, low * adj, closeadj, 63)
    res = _vol_regime_score(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_tr_126d_v025_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility regime score using True Range volatility over a 126-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_tr(high * adj, low * adj, closeadj, 126)
    res = _vol_regime_score(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Volatility Shock Features (026-050) ---

def f17vr_vol_shock_rs_5d_v026_signal(close: pd.Series) -> pd.Series:
    """Volatility shock using returns standard deviation over a 5-day window."""
    vol = _get_vol_rs(close, 5)
    res = _vol_shock(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_rs_10d_v027_signal(close: pd.Series) -> pd.Series:
    """Volatility shock using returns standard deviation over a 10-day window."""
    vol = _get_vol_rs(close, 10)
    res = _vol_shock(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_rs_21d_v028_signal(close: pd.Series) -> pd.Series:
    """Volatility shock using returns standard deviation over a 21-day window."""
    vol = _get_vol_rs(close, 21)
    res = _vol_shock(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_rs_63d_v029_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility shock using returns standard deviation over a 63-day window."""
    vol = _get_vol_rs(closeadj, 63)
    res = _vol_shock(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_rs_126d_v030_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility shock using returns standard deviation over a 126-day window."""
    vol = _get_vol_rs(closeadj, 126)
    res = _vol_shock(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_pk_5d_v031_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Volatility shock using Parkinson volatility over a 5-day window."""
    vol = _get_vol_pk(high, low, 5)
    res = _vol_shock(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_pk_10d_v032_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Volatility shock using Parkinson volatility over a 10-day window."""
    vol = _get_vol_pk(high, low, 10)
    res = _vol_shock(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_pk_21d_v033_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Volatility shock using Parkinson volatility over a 21-day window."""
    vol = _get_vol_pk(high, low, 21)
    res = _vol_shock(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_pk_63d_v034_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility shock using Parkinson volatility over a 63-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_pk(high * adj, low * adj, 63)
    res = _vol_shock(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_pk_126d_v035_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility shock using Parkinson volatility over a 126-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_pk(high * adj, low * adj, 126)
    res = _vol_shock(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_hl_5d_v036_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility shock using High-Low range over a 5-day window."""
    vol = _get_vol_hl(high, low, close, 5)
    res = _vol_shock(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_hl_10d_v037_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility shock using High-Low range over a 10-day window."""
    vol = _get_vol_hl(high, low, close, 10)
    res = _vol_shock(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_hl_21d_v038_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility shock using High-Low range over a 21-day window."""
    vol = _get_vol_hl(high, low, close, 21)
    res = _vol_shock(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_hl_63d_v039_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility shock using High-Low range over a 63-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_hl(high * adj, low * adj, closeadj, 63)
    res = _vol_shock(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_hl_126d_v040_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility shock using High-Low range over a 126-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_hl(high * adj, low * adj, closeadj, 126)
    res = _vol_shock(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_gk_5d_v041_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility shock using Garman-Klass volatility over a 5-day window."""
    vol = _get_vol_gk(high, low, close, 5)
    res = _vol_shock(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_gk_10d_v042_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility shock using Garman-Klass volatility over a 10-day window."""
    vol = _get_vol_gk(high, low, close, 10)
    res = _vol_shock(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_gk_21d_v043_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility shock using Garman-Klass volatility over a 21-day window."""
    vol = _get_vol_gk(high, low, close, 21)
    res = _vol_shock(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_gk_63d_v044_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility shock using Garman-Klass volatility over a 63-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_gk(high * adj, low * adj, closeadj, 63)
    res = _vol_shock(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_gk_126d_v045_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility shock using Garman-Klass volatility over a 126-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_gk(high * adj, low * adj, closeadj, 126)
    res = _vol_shock(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_tr_5d_v046_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility shock using True Range volatility over a 5-day window."""
    vol = _get_vol_tr(high, low, close, 5)
    res = _vol_shock(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_tr_10d_v047_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility shock using True Range volatility over a 10-day window."""
    vol = _get_vol_tr(high, low, close, 10)
    res = _vol_shock(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_tr_21d_v048_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility shock using True Range volatility over a 21-day window."""
    vol = _get_vol_tr(high, low, close, 21)
    res = _vol_shock(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_tr_63d_v049_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility shock using True Range volatility over a 63-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_tr(high * adj, low * adj, closeadj, 63)
    res = _vol_shock(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_tr_126d_v050_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility shock using True Range volatility over a 126-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_tr(high * adj, low * adj, closeadj, 126)
    res = _vol_shock(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Volatility Drift Features (051-075) ---

def f17vr_vol_drift_rs_5d_v051_signal(close: pd.Series) -> pd.Series:
    """Volatility drift using returns standard deviation over a 5-day window."""
    vol = _get_vol_rs(close, 5)
    res = _vol_drift(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_rs_10d_v052_signal(close: pd.Series) -> pd.Series:
    """Volatility drift using returns standard deviation over a 10-day window."""
    vol = _get_vol_rs(close, 10)
    res = _vol_drift(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_rs_21d_v053_signal(close: pd.Series) -> pd.Series:
    """Volatility drift using returns standard deviation over a 21-day window."""
    vol = _get_vol_rs(close, 21)
    res = _vol_drift(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_rs_63d_v054_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility drift using returns standard deviation over a 63-day window."""
    vol = _get_vol_rs(closeadj, 63)
    res = _vol_drift(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_rs_126d_v055_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility drift using returns standard deviation over a 126-day window."""
    vol = _get_vol_rs(closeadj, 126)
    res = _vol_drift(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_pk_5d_v056_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Volatility drift using Parkinson volatility over a 5-day window."""
    vol = _get_vol_pk(high, low, 5)
    res = _vol_drift(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_pk_10d_v057_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Volatility drift using Parkinson volatility over a 10-day window."""
    vol = _get_vol_pk(high, low, 10)
    res = _vol_drift(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_pk_21d_v058_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Volatility drift using Parkinson volatility over a 21-day window."""
    vol = _get_vol_pk(high, low, 21)
    res = _vol_drift(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_pk_63d_v059_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility drift using Parkinson volatility over a 63-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_pk(high * adj, low * adj, 63)
    res = _vol_drift(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_pk_126d_v060_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility drift using Parkinson volatility over a 126-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_pk(high * adj, low * adj, 126)
    res = _vol_drift(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_hl_5d_v061_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility drift using High-Low range over a 5-day window."""
    vol = _get_vol_hl(high, low, close, 5)
    res = _vol_drift(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_hl_10d_v062_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility drift using High-Low range over a 10-day window."""
    vol = _get_vol_hl(high, low, close, 10)
    res = _vol_drift(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_hl_21d_v063_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility drift using High-Low range over a 21-day window."""
    vol = _get_vol_hl(high, low, close, 21)
    res = _vol_drift(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_hl_63d_v064_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility drift using High-Low range over a 63-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_hl(high * adj, low * adj, closeadj, 63)
    res = _vol_drift(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_hl_126d_v065_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility drift using High-Low range over a 126-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_hl(high * adj, low * adj, closeadj, 126)
    res = _vol_drift(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_gk_5d_v066_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility drift using Garman-Klass volatility over a 5-day window."""
    vol = _get_vol_gk(high, low, close, 5)
    res = _vol_drift(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_gk_10d_v067_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility drift using Garman-Klass volatility over a 10-day window."""
    vol = _get_vol_gk(high, low, close, 10)
    res = _vol_drift(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_gk_21d_v068_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility drift using Garman-Klass volatility over a 21-day window."""
    vol = _get_vol_gk(high, low, close, 21)
    res = _vol_drift(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_gk_63d_v069_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility drift using Garman-Klass volatility over a 63-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_gk(high * adj, low * adj, closeadj, 63)
    res = _vol_drift(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_gk_126d_v070_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility drift using Garman-Klass volatility over a 126-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_gk(high * adj, low * adj, closeadj, 126)
    res = _vol_drift(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_tr_5d_v071_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility drift using True Range volatility over a 5-day window."""
    vol = _get_vol_tr(high, low, close, 5)
    res = _vol_drift(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_tr_10d_v072_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility drift using True Range volatility over a 10-day window."""
    vol = _get_vol_tr(high, low, close, 10)
    res = _vol_drift(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_tr_21d_v073_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Volatility drift using True Range volatility over a 21-day window."""
    vol = _get_vol_tr(high, low, close, 21)
    res = _vol_drift(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_tr_63d_v074_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility drift using True Range volatility over a 63-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_tr(high * adj, low * adj, closeadj, 63)
    res = _vol_drift(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_tr_126d_v075_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility drift using True Range volatility over a 126-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_tr(high * adj, low * adj, closeadj, 126)
    res = _vol_drift(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Registry and Self-Test ---

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

FEATURE_NAMES = [f for f in globals() if f.startswith("f17vr_") and f.endswith("_signal")]

F17_VOLATILITY_REGIME_BASE_001_075_REGISTRY = {
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
    for n, c in F17_VOLATILITY_REGIME_BASE_001_075_REGISTRY.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 001_075 OK")
