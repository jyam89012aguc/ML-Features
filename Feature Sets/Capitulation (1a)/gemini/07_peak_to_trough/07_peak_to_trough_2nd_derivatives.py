"""
Peak to Trough — 2nd Derivatives
Domain: amplitude of high to low swings
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, _EPS)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).min()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).sum()

def _ewm_mean(s: pd.Series, w: int) -> pd.Series:
    return s.ewm(span=w, min_periods=1).mean()

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))

def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change().fillna(0)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).median()

# Domain Specific Additions
def _days_since_high(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).apply(lambda x: len(x) - 1 - np.argmax(x), raw=True)

def _days_since_expanding_high(s: pd.Series) -> pd.Series:
    cummax = s.cummax()
    new_highs = (s == cummax)
    high_indices = pd.Series(np.arange(len(s)), index=s.index).where(new_highs).ffill()
    return pd.Series(np.arange(len(s)), index=s.index) - high_indices

def _pct_change(s: pd.Series, periods: int = 1) -> pd.Series:
    prev = s.shift(periods)
    return _safe_div(s - prev, prev.abs())

# ── Feature functions ────────────────────────────────────────────────────────

def ptt_drv2_001_ptt_ratio_252d_velocity(close: pd.Series) -> pd.Series:
    """ptt_drv2_001_ptt_ratio_252d_velocity feature"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    r = _safe_div(h, l)
    return r.diff(5)

def ptt_drv2_002_recovery_fraction_63d_velocity(close: pd.Series) -> pd.Series:
    """ptt_drv2_002_recovery_fraction_63d_velocity feature"""
    h = _rolling_max(close, 63)
    l = _rolling_min(close, 63)
    rf = _safe_div(close - l, h - l)
    return rf.diff(5)

def ptt_drv2_003_drawdown_to_ptt_ratio_velocity(close: pd.Series) -> pd.Series:
    """ptt_drv2_003_drawdown_to_ptt_ratio_velocity feature"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    ratio = _safe_div(h - close, h - l)
    return ratio.diff(5)

def ptt_drv2_004_days_since_trough_velocity(close: pd.Series) -> pd.Series:
    """ptt_drv2_004_days_since_trough_velocity feature"""
    l_idx = close.rolling(252).apply(np.argmin, raw=True)
    dst = 252 - 1 - l_idx
    return dst.diff(5)

def ptt_drv2_005_mktcap_ptt_ratio_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ptt_drv2_005_mktcap_ptt_ratio_velocity feature"""
    mc = close * sharesbas
    r = _safe_div(_rolling_max(mc, 252), _rolling_min(mc, 252))
    return r.diff(5)

def ptt_drv2_006_ptt_ratio_zscore_velocity(close: pd.Series) -> pd.Series:
    """ptt_drv2_006_ptt_ratio_zscore_velocity feature"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    r = _safe_div(h, l)
    z = (r - r.rolling(252).mean()) / r.rolling(252).std()
    return z.diff(5)

def ptt_drv2_007_recovery_fraction_std_velocity(close: pd.Series) -> pd.Series:
    """ptt_drv2_007_recovery_fraction_std_velocity feature"""
    h = _rolling_max(close, 63)
    l = _rolling_min(close, 63)
    rf = _safe_div(close - l, h - l)
    return rf.rolling(63).std().diff(5)

def ptt_drv2_008_ptt_volatility_adjusted_velocity(close: pd.Series) -> pd.Series:
    """ptt_drv2_008_ptt_volatility_adjusted_velocity feature"""
    r = _safe_div(_rolling_max(close, 252), _rolling_min(close, 252))
    v = close.pct_change().rolling(252).std()
    return _safe_div(r, v).diff(5)

def ptt_drv2_009_current_to_midpoint_velocity(close: pd.Series) -> pd.Series:
    """ptt_drv2_009_current_to_midpoint_velocity feature"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    mid = (h + l) / 2.0
    return _safe_div(close, mid).diff(5)

def ptt_drv2_010_trough_persistence_velocity(close: pd.Series) -> pd.Series:
    """ptt_drv2_010_trough_persistence_velocity feature"""
    l = _rolling_min(close, 252)
    cnt = (close <= l * 1.01).astype(int).rolling(252).sum()
    return cnt.diff(5)

def ptt_drv2_011_ptt_ratio_expansion_velocity(close: pd.Series) -> pd.Series:
    """ptt_drv2_011_ptt_ratio_expansion_velocity feature"""
    r = _safe_div(_rolling_max(close, 63), _rolling_min(close, 63))
    idx = _safe_div(r, r.rolling(252).mean())
    return idx.diff(5)

def ptt_drv2_012_recovery_velocity_score_accel(close: pd.Series) -> pd.Series:
    """ptt_drv2_012_recovery_velocity_score_accel feature"""
    h = _rolling_max(close, 63)
    l = _rolling_min(close, 63)
    rf = _safe_div(close - l, h - l)
    vol = close.pct_change().rolling(21).std()
    score = _safe_div(rf.diff(5), vol)
    return score.diff(5)

def ptt_drv2_013_ptt_convexity_velocity(close: pd.Series) -> pd.Series:
    """ptt_drv2_013_ptt_convexity_velocity feature"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    dist = _safe_div(h - close, h - l)
    conv = dist.rolling(252).sum()
    return conv.diff(5)

def ptt_drv2_014_dsp_dst_ratio_velocity(close: pd.Series) -> pd.Series:
    """ptt_drv2_014_dsp_dst_ratio_velocity feature"""
    h_idx = close.rolling(252).apply(np.argmax, raw=True)
    l_idx = close.rolling(252).apply(np.argmin, raw=True)
    ratio = _safe_div(252 - 1 - h_idx, 252 - 1 - l_idx)
    return ratio.diff(5)

def ptt_drv2_015_recovery_fraction_log_drift_velocity(close: pd.Series) -> pd.Series:
    """ptt_drv2_015_recovery_fraction_log_drift_velocity feature"""
    h = _rolling_max(close, 63)
    l = _rolling_min(close, 63)
    rf = _safe_div(close - l, h - l)
    drift = np.log(rf + _EPS).diff(21)
    return drift.diff(5)

def ptt_drv2_016_mktcap_recovery_efficiency_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ptt_drv2_016_mktcap_recovery_efficiency_velocity feature"""
    mc = close * sharesbas
    h = _rolling_max(mc, 252)
    l = _rolling_min(mc, 252)
    rf = _safe_div(mc - l, h - l)
    eff = _safe_div(rf, mc.pct_change().rolling(252).std())
    return eff.diff(5)

def ptt_drv2_017_proximity_to_midpoint_spread_velocity(close: pd.Series) -> pd.Series:
    """ptt_drv2_017_proximity_to_midpoint_spread_velocity feature"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    s = (close - (h + l) / 2.0) / (h - l + _EPS)
    return s.diff(5)

def ptt_drv2_018_recovery_fraction_entropy_velocity(close: pd.Series) -> pd.Series:
    """ptt_drv2_018_recovery_fraction_entropy_velocity feature"""
    h = _rolling_max(close, 63)
    l = _rolling_min(close, 63)
    rf = _safe_div(close - l, h - l)
    def _ent(y):
        hist, _ = np.histogram(y[~np.isnan(y)], bins=10, range=(0,1))
        p = hist / (np.sum(hist) + _EPS)
        p = p[p > 0]
        return -np.sum(p * np.log(p))
    e = rf.rolling(63).apply(_ent, raw=True)
    return e.diff(5)

def ptt_drv2_019_ptt_cycle_amplitude_velocity(close: pd.Series) -> pd.Series:
    """ptt_drv2_019_ptt_cycle_amplitude_velocity feature"""
    r = _safe_div(_rolling_max(close, 252), _rolling_min(close, 252))
    amp = _safe_div(r, r.rolling(252 * 3).min())
    return amp.diff(5)

def ptt_drv2_020_ptt_final_pain_score_velocity(close: pd.Series) -> pd.Series:
    """ptt_drv2_020_ptt_final_pain_score_velocity feature"""
    r = _safe_div(_rolling_max(close, 252), _rolling_min(close, 252))
    rf = _safe_div(close - _rolling_min(close, 252), _rolling_max(close, 252) - _rolling_min(close, 252))
    score = r * (1.0 - rf)
    return score.diff(5)

def ptt_drv2_021_ptt_ratio_pct_rank_velocity(close: pd.Series) -> pd.Series:
    """ptt_drv2_021_ptt_ratio_pct_rank_velocity feature"""
    r = _safe_div(_rolling_max(close, 252), _rolling_min(close, 252))
    rank = r.expanding().rank(pct=True)
    return rank.diff(5)

def ptt_drv2_022_recovery_fraction_zscore_velocity(close: pd.Series) -> pd.Series:
    """ptt_drv2_022_recovery_fraction_zscore_velocity feature"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    rf = _safe_div(close - l, h - l)
    z = (rf - rf.rolling(252).mean()) / rf.rolling(252).std()
    return z.diff(5)

def ptt_drv2_023_ptt_volatility_ratio_velocity(close: pd.Series) -> pd.Series:
    """ptt_drv2_023_ptt_volatility_ratio_velocity feature"""
    r = _safe_div(_rolling_max(close, 21), _rolling_min(close, 21))
    ratio = _safe_div(r.rolling(63).std(), r.rolling(63).mean())
    return ratio.diff(5)

def ptt_drv2_024_pe_ptt_ratio_velocity(close: pd.Series, netinc: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ptt_drv2_024_pe_ptt_ratio_velocity feature"""
    pe = _safe_div(close * sharesbas, netinc)
    pe = pe.where(pe > 0)
    r = _safe_div(_rolling_max(pe, 252), _rolling_min(pe, 252))
    return r.diff(5)

def ptt_drv2_025_revenue_ps_ptt_ratio_velocity(revenue: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ptt_drv2_025_revenue_ps_ptt_ratio_velocity feature"""
    revps = _safe_div(revenue, sharesbas)
    r = _safe_div(revps.cummax(), revps.cummin())
    return r.diff(5)

# ── Registry ──────────────────────────────────────────────────────────────────

V07_V_REGISTRY = {
    "ptt_drv2_001_ptt_ratio_252d_velocity": {"inputs": ["close"], "func": ptt_drv2_001_ptt_ratio_252d_velocity},
    "ptt_drv2_002_recovery_fraction_63d_velocity": {"inputs": ["close"], "func": ptt_drv2_002_recovery_fraction_63d_velocity},
    "ptt_drv2_003_drawdown_to_ptt_ratio_velocity": {"inputs": ["close"], "func": ptt_drv2_003_drawdown_to_ptt_ratio_velocity},
    "ptt_drv2_004_days_since_trough_velocity": {"inputs": ["close"], "func": ptt_drv2_004_days_since_trough_velocity},
    "ptt_drv2_005_mktcap_ptt_ratio_velocity": {"inputs": ["close", "sharesbas"], "func": ptt_drv2_005_mktcap_ptt_ratio_velocity},
    "ptt_drv2_006_ptt_ratio_zscore_velocity": {"inputs": ["close"], "func": ptt_drv2_006_ptt_ratio_zscore_velocity},
    "ptt_drv2_007_recovery_fraction_std_velocity": {"inputs": ["close"], "func": ptt_drv2_007_recovery_fraction_std_velocity},
    "ptt_drv2_008_ptt_volatility_adjusted_velocity": {"inputs": ["close"], "func": ptt_drv2_008_ptt_volatility_adjusted_velocity},
    "ptt_drv2_009_current_to_midpoint_velocity": {"inputs": ["close"], "func": ptt_drv2_009_current_to_midpoint_velocity},
    "ptt_drv2_010_trough_persistence_velocity": {"inputs": ["close"], "func": ptt_drv2_010_trough_persistence_velocity},
    "ptt_drv2_011_ptt_ratio_expansion_velocity": {"inputs": ["close"], "func": ptt_drv2_011_ptt_ratio_expansion_velocity},
    "ptt_drv2_012_recovery_velocity_score_accel": {"inputs": ["close"], "func": ptt_drv2_012_recovery_velocity_score_accel},
    "ptt_drv2_013_ptt_convexity_velocity": {"inputs": ["close"], "func": ptt_drv2_013_ptt_convexity_velocity},
    "ptt_drv2_014_dsp_dst_ratio_velocity": {"inputs": ["close"], "func": ptt_drv2_014_dsp_dst_ratio_velocity},
    "ptt_drv2_015_recovery_fraction_log_drift_velocity": {"inputs": ["close"], "func": ptt_drv2_015_recovery_fraction_log_drift_velocity},
    "ptt_drv2_016_mktcap_recovery_efficiency_velocity": {"inputs": ["close", "sharesbas"], "func": ptt_drv2_016_mktcap_recovery_efficiency_velocity},
    "ptt_drv2_017_proximity_to_midpoint_spread_velocity": {"inputs": ["close"], "func": ptt_drv2_017_proximity_to_midpoint_spread_velocity},
    "ptt_drv2_018_recovery_fraction_entropy_velocity": {"inputs": ["close"], "func": ptt_drv2_018_recovery_fraction_entropy_velocity},
    "ptt_drv2_019_ptt_cycle_amplitude_velocity": {"inputs": ["close"], "func": ptt_drv2_019_ptt_cycle_amplitude_velocity},
    "ptt_drv2_020_ptt_final_pain_score_velocity": {"inputs": ["close"], "func": ptt_drv2_020_ptt_final_pain_score_velocity},
    "ptt_drv2_021_ptt_ratio_pct_rank_velocity": {"inputs": ["close"], "func": ptt_drv2_021_ptt_ratio_pct_rank_velocity},
    "ptt_drv2_022_recovery_fraction_zscore_velocity": {"inputs": ["close"], "func": ptt_drv2_022_recovery_fraction_zscore_velocity},
    "ptt_drv2_023_ptt_volatility_ratio_velocity": {"inputs": ["close"], "func": ptt_drv2_023_ptt_volatility_ratio_velocity},
    "ptt_drv2_024_pe_ptt_ratio_velocity": {"inputs": ["close", "netinc", "sharesbas"], "func": ptt_drv2_024_pe_ptt_ratio_velocity},
    "ptt_drv2_025_revenue_ps_ptt_ratio_velocity": {"inputs": ["revenue", "sharesbas"], "func": ptt_drv2_025_revenue_ps_ptt_ratio_velocity},
}
