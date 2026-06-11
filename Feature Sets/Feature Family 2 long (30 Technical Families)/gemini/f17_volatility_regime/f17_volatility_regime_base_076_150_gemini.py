# f17_volatility_regime_base_076_150_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _std(s, w):
    return s.rolling(w, min_periods=min(w, 5)).std()

def _skew(s, w):
    return s.rolling(w, min_periods=min(w, 5)).skew()

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

def _get_vol_vv(close, w):
    """Calculates the volatility of volatility (VVIX-style)."""
    vol = _get_vol_rs(close, w)
    return _std(vol, w)

def _get_vol_sk(close, w):
    """Calculates the rolling skewness of returns."""
    return _skew(close.pct_change().replace([np.inf, -np.inf], 0), w).abs()

def _get_vol_pr(close, w):
    """Measures the persistence of high volatility regimes."""
    vol = _get_vol_rs(close, w)
    ma = _sma(vol, w * 2)
    return _sma((vol > ma).astype(float), w)

def _get_vol_hl(high, low, close, w):
    """Calculates the High-Low range normalized by the moving average of Close."""
    return _sma((high - low) / close.replace(0, np.nan), w)

# --- Volatility Regime Score Features (076-100) ---

def f17vr_vol_regime_score_vv_5d_v076_signal(close: pd.Series) -> pd.Series:
    """Volatility regime score of volatility-of-volatility over a 5-day window."""
    vol = _get_vol_vv(close, 5)
    res = _vol_regime_score(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_vv_10d_v077_signal(close: pd.Series) -> pd.Series:
    """Volatility regime score of volatility-of-volatility over a 10-day window."""
    vol = _get_vol_vv(close, 10)
    res = _vol_regime_score(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_vv_21d_v078_signal(close: pd.Series) -> pd.Series:
    """Volatility regime score of volatility-of-volatility over a 21-day window."""
    vol = _get_vol_vv(close, 21)
    res = _vol_regime_score(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_vv_63d_v079_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility regime score of volatility-of-volatility over a 63-day window."""
    vol = _get_vol_vv(closeadj, 63)
    res = _vol_regime_score(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_vv_126d_v080_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility regime score of volatility-of-volatility over a 126-day window."""
    vol = _get_vol_vv(closeadj, 126)
    res = _vol_regime_score(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_sk_5d_v081_signal(close: pd.Series) -> pd.Series:
    """Volatility regime score of absolute skewness over a 5-day window."""
    vol = _get_vol_sk(close, 5)
    res = _vol_regime_score(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_sk_10d_v082_signal(close: pd.Series) -> pd.Series:
    """Volatility regime score of absolute skewness over a 10-day window."""
    vol = _get_vol_sk(close, 10)
    res = _vol_regime_score(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_sk_21d_v083_signal(close: pd.Series) -> pd.Series:
    """Volatility regime score of absolute skewness over a 21-day window."""
    vol = _get_vol_sk(close, 21)
    res = _vol_regime_score(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_sk_63d_v084_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility regime score of absolute skewness over a 63-day window."""
    vol = _get_vol_sk(closeadj, 63)
    res = _vol_regime_score(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_sk_126d_v085_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility regime score of absolute skewness over a 126-day window."""
    vol = _get_vol_sk(closeadj, 126)
    res = _vol_regime_score(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_pr_5d_v086_signal(close: pd.Series) -> pd.Series:
    """Volatility regime score of vol-persistence over a 5-day window."""
    vol = _get_vol_pr(close, 5)
    res = _vol_regime_score(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_pr_10d_v087_signal(close: pd.Series) -> pd.Series:
    """Volatility regime score of vol-persistence over a 10-day window."""
    vol = _get_vol_pr(close, 10)
    res = _vol_regime_score(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_pr_21d_v088_signal(close: pd.Series) -> pd.Series:
    """Volatility regime score of vol-persistence over a 21-day window."""
    vol = _get_vol_pr(close, 21)
    res = _vol_regime_score(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_pr_63d_v089_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility regime score of vol-persistence over a 63-day window."""
    vol = _get_vol_pr(closeadj, 63)
    res = _vol_regime_score(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_pr_126d_v090_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility regime score of vol-persistence over a 126-day window."""
    vol = _get_vol_pr(closeadj, 126)
    res = _vol_regime_score(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_hl_252d_v091_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility regime score of High-Low range over a 252-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_hl(high * adj, low * adj, closeadj, 252)
    res = _vol_regime_score(vol, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_hl_504d_v092_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility regime score of High-Low range over a 504-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_hl(high * adj, low * adj, closeadj, 504)
    res = _vol_regime_score(vol, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_rs_252d_v093_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility regime score of returns standard deviation over a 252-day window."""
    vol = _get_vol_rs(closeadj, 252)
    res = _vol_regime_score(vol, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_rs_504d_v094_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility regime score of returns standard deviation over a 504-day window."""
    vol = _get_vol_rs(closeadj, 504)
    res = _vol_regime_score(vol, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_vv_252d_v095_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility regime score of vol-of-vol over a 252-day window."""
    vol = _get_vol_vv(closeadj, 252)
    res = _vol_regime_score(vol, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_sk_252d_v096_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility regime score of absolute skewness over a 252-day window."""
    vol = _get_vol_sk(closeadj, 252)
    res = _vol_regime_score(vol, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_pr_252d_v097_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility regime score of vol-persistence over a 252-day window."""
    vol = _get_vol_pr(closeadj, 252)
    res = _vol_regime_score(vol, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_vv_504d_v098_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility regime score of vol-of-vol over a 504-day window."""
    vol = _get_vol_vv(closeadj, 504)
    res = _vol_regime_score(vol, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_sk_504d_v099_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility regime score of absolute skewness over a 504-day window."""
    vol = _get_vol_sk(closeadj, 504)
    res = _vol_regime_score(vol, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_regime_score_pr_504d_v100_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility regime score of vol-persistence over a 504-day window."""
    vol = _get_vol_pr(closeadj, 504)
    res = _vol_regime_score(vol, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Volatility Shock Features (101-125) ---

def f17vr_vol_shock_vv_5d_v101_signal(close: pd.Series) -> pd.Series:
    """Volatility shock of vol-of-vol over a 5-day window."""
    vol = _get_vol_vv(close, 5)
    res = _vol_shock(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_vv_10d_v102_signal(close: pd.Series) -> pd.Series:
    """Volatility shock of vol-of-vol over a 10-day window."""
    vol = _get_vol_vv(close, 10)
    res = _vol_shock(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_vv_21d_v103_signal(close: pd.Series) -> pd.Series:
    """Volatility shock of vol-of-vol over a 21-day window."""
    vol = _get_vol_vv(close, 21)
    res = _vol_shock(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_vv_63d_v104_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility shock of vol-of-vol over a 63-day window."""
    vol = _get_vol_vv(closeadj, 63)
    res = _vol_shock(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_vv_126d_v105_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility shock of vol-of-vol over a 126-day window."""
    vol = _get_vol_vv(closeadj, 126)
    res = _vol_shock(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_sk_5d_v106_signal(close: pd.Series) -> pd.Series:
    """Volatility shock of absolute skewness over a 5-day window."""
    vol = _get_vol_sk(close, 5)
    res = _vol_shock(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_sk_10d_v107_signal(close: pd.Series) -> pd.Series:
    """Volatility shock of absolute skewness over a 10-day window."""
    vol = _get_vol_sk(close, 10)
    res = _vol_shock(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_sk_21d_v108_signal(close: pd.Series) -> pd.Series:
    """Volatility shock of absolute skewness over a 21-day window."""
    vol = _get_vol_sk(close, 21)
    res = _vol_shock(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_sk_63d_v109_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility shock of absolute skewness over a 63-day window."""
    vol = _get_vol_sk(closeadj, 63)
    res = _vol_shock(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_sk_126d_v110_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility shock of absolute skewness over a 126-day window."""
    vol = _get_vol_sk(closeadj, 126)
    res = _vol_shock(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_pr_5d_v111_signal(close: pd.Series) -> pd.Series:
    """Volatility shock of vol-persistence over a 5-day window."""
    vol = _get_vol_pr(close, 5)
    res = _vol_shock(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_pr_10d_v112_signal(close: pd.Series) -> pd.Series:
    """Volatility shock of vol-persistence over a 10-day window."""
    vol = _get_vol_pr(close, 10)
    res = _vol_shock(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_pr_21d_v113_signal(close: pd.Series) -> pd.Series:
    """Volatility shock of vol-persistence over a 21-day window."""
    vol = _get_vol_pr(close, 21)
    res = _vol_shock(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_pr_63d_v114_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility shock of vol-persistence over a 63-day window."""
    vol = _get_vol_pr(closeadj, 63)
    res = _vol_shock(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_pr_126d_v115_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility shock of vol-persistence over a 126-day window."""
    vol = _get_vol_pr(closeadj, 126)
    res = _vol_shock(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_hl_252d_v116_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility shock of High-Low range over a 252-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_hl(high * adj, low * adj, closeadj, 252)
    res = _vol_shock(vol, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_hl_504d_v117_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility shock of High-Low range over a 504-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_hl(high * adj, low * adj, closeadj, 504)
    res = _vol_shock(vol, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_rs_252d_v118_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility shock of returns standard deviation over a 252-day window."""
    vol = _get_vol_rs(closeadj, 252)
    res = _vol_shock(vol, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_rs_504d_v119_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility shock of returns standard deviation over a 504-day window."""
    vol = _get_vol_rs(closeadj, 504)
    res = _vol_shock(vol, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_vv_252d_v120_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility shock of vol-of-vol over a 252-day window."""
    vol = _get_vol_vv(closeadj, 252)
    res = _vol_shock(vol, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_sk_252d_v121_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility shock of absolute skewness over a 252-day window."""
    vol = _get_vol_sk(closeadj, 252)
    res = _vol_shock(vol, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_pr_252d_v122_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility shock of vol-persistence over a 252-day window."""
    vol = _get_vol_pr(closeadj, 252)
    res = _vol_shock(vol, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_vv_504d_v123_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility shock of vol-of-vol over a 504-day window."""
    vol = _get_vol_vv(closeadj, 504)
    res = _vol_shock(vol, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_sk_504d_v124_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility shock of absolute skewness over a 504-day window."""
    vol = _get_vol_sk(closeadj, 504)
    res = _vol_shock(vol, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_shock_pr_504d_v125_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility shock of vol-persistence over a 504-day window."""
    vol = _get_vol_pr(closeadj, 504)
    res = _vol_shock(vol, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Volatility Drift Features (126-150) ---

def f17vr_vol_drift_vv_5d_v126_signal(close: pd.Series) -> pd.Series:
    """Volatility drift of vol-of-vol over a 5-day window."""
    vol = _get_vol_vv(close, 5)
    res = _vol_drift(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_vv_10d_v127_signal(close: pd.Series) -> pd.Series:
    """Volatility drift of vol-of-vol over a 10-day window."""
    vol = _get_vol_vv(close, 10)
    res = _vol_drift(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_vv_21d_v128_signal(close: pd.Series) -> pd.Series:
    """Volatility drift of vol-of-vol over a 21-day window."""
    vol = _get_vol_vv(close, 21)
    res = _vol_drift(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_vv_63d_v129_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility drift of vol-of-vol over a 63-day window."""
    vol = _get_vol_vv(closeadj, 63)
    res = _vol_drift(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_vv_126d_v130_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility drift of vol-of-vol over a 126-day window."""
    vol = _get_vol_vv(closeadj, 126)
    res = _vol_drift(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_sk_5d_v131_signal(close: pd.Series) -> pd.Series:
    """Volatility drift of absolute skewness over a 5-day window."""
    vol = _get_vol_sk(close, 5)
    res = _vol_drift(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_sk_10d_v132_signal(close: pd.Series) -> pd.Series:
    """Volatility drift of absolute skewness over a 10-day window."""
    vol = _get_vol_sk(close, 10)
    res = _vol_drift(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_sk_21d_v133_signal(close: pd.Series) -> pd.Series:
    """Volatility drift of absolute skewness over a 21-day window."""
    vol = _get_vol_sk(close, 21)
    res = _vol_drift(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_sk_63d_v134_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility drift of absolute skewness over a 63-day window."""
    vol = _get_vol_sk(closeadj, 63)
    res = _vol_drift(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_sk_126d_v135_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility drift of absolute skewness over a 126-day window."""
    vol = _get_vol_sk(closeadj, 126)
    res = _vol_drift(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_pr_5d_v136_signal(close: pd.Series) -> pd.Series:
    """Volatility drift of vol-persistence over a 5-day window."""
    vol = _get_vol_pr(close, 5)
    res = _vol_drift(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_pr_10d_v137_signal(close: pd.Series) -> pd.Series:
    """Volatility drift of vol-persistence over a 10-day window."""
    vol = _get_vol_pr(close, 10)
    res = _vol_drift(vol, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_pr_21d_v138_signal(close: pd.Series) -> pd.Series:
    """Volatility drift of vol-persistence over a 21-day window."""
    vol = _get_vol_pr(close, 21)
    res = _vol_drift(vol, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_pr_63d_v139_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility drift of vol-persistence over a 63-day window."""
    vol = _get_vol_pr(closeadj, 63)
    res = _vol_drift(vol, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_pr_126d_v140_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility drift of vol-persistence over a 126-day window."""
    vol = _get_vol_pr(closeadj, 126)
    res = _vol_drift(vol, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_hl_252d_v141_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility drift of High-Low range over a 252-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_hl(high * adj, low * adj, closeadj, 252)
    res = _vol_drift(vol, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_hl_504d_v142_signal(high: pd.Series, low: pd.Series, close: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Volatility drift of High-Low range over a 504-day window."""
    adj = closeadj / close.replace(0, np.nan)
    vol = _get_vol_hl(high * adj, low * adj, closeadj, 504)
    res = _vol_drift(vol, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_rs_252d_v143_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility drift of returns standard deviation over a 252-day window."""
    vol = _get_vol_rs(closeadj, 252)
    res = _vol_drift(vol, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_rs_504d_v144_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility drift of returns standard deviation over a 504-day window."""
    vol = _get_vol_rs(closeadj, 504)
    res = _vol_drift(vol, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_vv_252d_v145_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility drift of vol-of-vol over a 252-day window."""
    vol = _get_vol_vv(closeadj, 252)
    res = _vol_drift(vol, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_sk_252d_v146_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility drift of absolute skewness over a 252-day window."""
    vol = _get_vol_sk(closeadj, 252)
    res = _vol_drift(vol, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_pr_252d_v147_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility drift of vol-persistence over a 252-day window."""
    vol = _get_vol_pr(closeadj, 252)
    res = _vol_drift(vol, 504)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_vv_504d_v148_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility drift of vol-of-vol over a 504-day window."""
    vol = _get_vol_vv(closeadj, 504)
    res = _vol_drift(vol, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_sk_504d_v149_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility drift of absolute skewness over a 504-day window."""
    vol = _get_vol_sk(closeadj, 504)
    res = _vol_drift(vol, 756)
    return res.replace([np.inf, -np.inf], np.nan)

def f17vr_vol_drift_pr_504d_v150_signal(closeadj: pd.Series) -> pd.Series:
    """Volatility drift of vol-persistence over a 504-day window."""
    vol = _get_vol_pr(closeadj, 504)
    res = _vol_drift(vol, 756)
    return res.replace([np.inf, -np.inf], np.nan)

# --- Registry and Self-Test ---

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "high", "low"]}

FEATURE_NAMES = [f for f in globals() if f.startswith("f17vr_") and f.endswith("_signal")]

F17_VOLATILITY_REGIME_BASE_076_150_REGISTRY = {
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
    for n, c in F17_VOLATILITY_REGIME_BASE_076_150_REGISTRY.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("base 076_150 OK")
