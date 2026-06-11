"""
Peak to Trough — 3rd Derivatives
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

def ptt_drv3_001_ptt_ratio_252d_jerk(close: pd.Series) -> pd.Series:
    """ptt_drv3_001_ptt_ratio_252d_jerk feature"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    r = _safe_div(h, l)
    vel = r.diff(5)
    return vel.diff(5)

def ptt_drv3_002_recovery_fraction_63d_jerk(close: pd.Series) -> pd.Series:
    """ptt_drv3_002_recovery_fraction_63d_jerk feature"""
    h = _rolling_max(close, 63)
    l = _rolling_min(close, 63)
    rf = _safe_div(close - l, h - l)
    vel = rf.diff(5)
    return vel.diff(5)

def ptt_drv3_003_drawdown_to_ptt_ratio_jerk(close: pd.Series) -> pd.Series:
    """ptt_drv3_003_drawdown_to_ptt_ratio_jerk feature"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    ratio = _safe_div(h - close, h - l)
    vel = ratio.diff(5)
    return vel.diff(5)

def ptt_drv3_004_days_since_trough_jerk(close: pd.Series) -> pd.Series:
    """ptt_drv3_004_days_since_trough_jerk feature"""
    l_idx = close.rolling(252).apply(np.argmin, raw=True)
    dst = 252 - 1 - l_idx
    vel = dst.diff(5)
    return vel.diff(5)

def ptt_drv3_005_mktcap_ptt_ratio_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ptt_drv3_005_mktcap_ptt_ratio_jerk feature"""
    mc = close * sharesbas
    r = _safe_div(_rolling_max(mc, 252), _rolling_min(mc, 252))
    vel = r.diff(5)
    return vel.diff(5)

def ptt_drv3_006_ptt_ratio_zscore_jerk(close: pd.Series) -> pd.Series:
    """ptt_drv3_006_ptt_ratio_zscore_jerk feature"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    r = _safe_div(h, l)
    z = (r - r.rolling(252).mean()) / r.rolling(252).std()
    vel = z.diff(5)
    return vel.diff(5)

def ptt_drv3_007_recovery_fraction_std_jerk(close: pd.Series) -> pd.Series:
    """ptt_drv3_007_recovery_fraction_std_jerk feature"""
    h = _rolling_max(close, 63)
    l = _rolling_min(close, 63)
    rf = _safe_div(close - l, h - l)
    vel = rf.rolling(63).std().diff(5)
    return vel.diff(5)

def ptt_drv3_008_ptt_volatility_adjusted_jerk(close: pd.Series) -> pd.Series:
    """ptt_drv3_008_ptt_volatility_adjusted_jerk feature"""
    r = _safe_div(_rolling_max(close, 252), _rolling_min(close, 252))
    v = close.pct_change().rolling(252).std()
    vel = _safe_div(r, v).diff(5)
    return vel.diff(5)

def ptt_drv3_009_current_to_midpoint_jerk(close: pd.Series) -> pd.Series:
    """ptt_drv3_009_current_to_midpoint_jerk feature"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    mid = (h + l) / 2.0
    vel = _safe_div(close, mid).diff(5)
    return vel.diff(5)

def ptt_drv3_010_trough_persistence_jerk(close: pd.Series) -> pd.Series:
    """ptt_drv3_010_trough_persistence_jerk feature"""
    l = _rolling_min(close, 252)
    cnt = (close <= l * 1.01).astype(int).rolling(252).sum()
    vel = cnt.diff(5)
    return vel.diff(5)

def ptt_drv3_011_ptt_ratio_expansion_jerk(close: pd.Series) -> pd.Series:
    """ptt_drv3_011_ptt_ratio_expansion_jerk feature"""
    r = _safe_div(_rolling_max(close, 63), _rolling_min(close, 63))
    idx = _safe_div(r, r.rolling(252).mean())
    vel = idx.diff(5)
    return vel.diff(5)

def ptt_drv3_012_recovery_velocity_score_jerk(close: pd.Series) -> pd.Series:
    """ptt_drv3_012_recovery_velocity_score_jerk feature"""
    h = _rolling_max(close, 63)
    l = _rolling_min(close, 63)
    rf = _safe_div(close - l, h - l)
    vol = close.pct_change().rolling(21).std()
    score = _safe_div(rf.diff(5), vol)
    vel = score.diff(5)
    return vel.diff(5)

def ptt_drv3_013_ptt_convexity_jerk(close: pd.Series) -> pd.Series:
    """ptt_drv3_013_ptt_convexity_jerk feature"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    dist = _safe_div(h - close, h - l)
    conv = dist.rolling(252).sum()
    vel = conv.diff(5)
    return vel.diff(5)

def ptt_drv3_014_dsp_dst_ratio_jerk(close: pd.Series) -> pd.Series:
    """ptt_drv3_014_dsp_dst_ratio_jerk feature"""
    h_idx = close.rolling(252).apply(np.argmax, raw=True)
    l_idx = close.rolling(252).apply(np.argmin, raw=True)
    ratio = _safe_div(252 - 1 - h_idx, 252 - 1 - l_idx)
    vel = ratio.diff(5)
    return vel.diff(5)

def ptt_drv3_015_recovery_fraction_log_drift_jerk(close: pd.Series) -> pd.Series:
    """ptt_drv3_015_recovery_fraction_log_drift_jerk feature"""
    h = _rolling_max(close, 63)
    l = _rolling_min(close, 63)
    rf = _safe_div(close - l, h - l)
    drift = np.log(rf + _EPS).diff(21)
    vel = drift.diff(5)
    return vel.diff(5)

def ptt_drv3_016_mktcap_recovery_efficiency_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ptt_drv3_016_mktcap_recovery_efficiency_jerk feature"""
    mc = close * sharesbas
    h = _rolling_max(mc, 252)
    l = _rolling_min(mc, 252)
    rf = _safe_div(mc - l, h - l)
    eff = _safe_div(rf, mc.pct_change().rolling(252).std())
    vel = eff.diff(5)
    return vel.diff(5)

def ptt_drv3_017_proximity_to_midpoint_spread_jerk(close: pd.Series) -> pd.Series:
    """ptt_drv3_017_proximity_to_midpoint_spread_jerk feature"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    s = (close - (h + l) / 2.0) / (h - l + _EPS)
    vel = s.diff(5)
    return vel.diff(5)

def ptt_drv3_018_recovery_fraction_entropy_jerk(close: pd.Series) -> pd.Series:
    """ptt_drv3_018_recovery_fraction_entropy_jerk feature"""
    h = _rolling_max(close, 63)
    l = _rolling_min(close, 63)
    rf = _safe_div(close - l, h - l)
    def _ent(y):
        hist, _ = np.histogram(y[~np.isnan(y)], bins=10, range=(0,1))
        p = hist / (np.sum(hist) + _EPS)
        p = p[p > 0]
        return -np.sum(p * np.log(p))
    e = rf.rolling(63).apply(_ent, raw=True)
    vel = e.diff(5)
    return vel.diff(5)

def ptt_drv3_019_ptt_cycle_amplitude_jerk(close: pd.Series) -> pd.Series:
    """ptt_drv3_019_ptt_cycle_amplitude_jerk feature"""
    r = _safe_div(_rolling_max(close, 252), _rolling_min(close, 252))
    amp = _safe_div(r, r.rolling(252 * 3).min())
    vel = amp.diff(5)
    return vel.diff(5)

def ptt_drv3_020_ptt_final_pain_score_jerk(close: pd.Series) -> pd.Series:
    """ptt_drv3_020_ptt_final_pain_score_jerk feature"""
    r = _safe_div(_rolling_max(close, 252), _rolling_min(close, 252))
    rf = _safe_div(close - _rolling_min(close, 252), _rolling_max(close, 252) - _rolling_min(close, 252))
    score = r * (1.0 - rf)
    vel = score.diff(5)
    return vel.diff(5)

def ptt_drv3_021_ptt_ratio_pct_rank_jerk(close: pd.Series) -> pd.Series:
    """ptt_drv3_021_ptt_ratio_pct_rank_jerk feature"""
    r = _safe_div(_rolling_max(close, 252), _rolling_min(close, 252))
    rank = r.expanding().rank(pct=True)
    vel = rank.diff(5)
    return vel.diff(5)

def ptt_drv3_022_recovery_fraction_zscore_jerk(close: pd.Series) -> pd.Series:
    """ptt_drv3_022_recovery_fraction_zscore_jerk feature"""
    h = _rolling_max(close, 252)
    l = _rolling_min(close, 252)
    rf = _safe_div(close - l, h - l)
    z = (rf - rf.rolling(252).mean()) / rf.rolling(252).std()
    vel = z.diff(5)
    return vel.diff(5)

def ptt_drv3_023_ptt_volatility_ratio_jerk(close: pd.Series) -> pd.Series:
    """ptt_drv3_023_ptt_volatility_ratio_jerk feature"""
    r = _safe_div(_rolling_max(close, 21), _rolling_min(close, 21))
    ratio = _safe_div(r.rolling(63).std(), r.rolling(63).mean())
    vel = ratio.diff(5)
    return vel.diff(5)

def ptt_drv3_024_pe_ptt_ratio_jerk(close: pd.Series, netinc: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ptt_drv3_024_pe_ptt_ratio_jerk feature"""
    pe = _safe_div(close * sharesbas, netinc)
    pe = pe.where(pe > 0)
    r = _safe_div(_rolling_max(pe, 252), _rolling_min(pe, 252))
    vel = r.diff(5)
    return vel.diff(5)

def ptt_drv3_025_revenue_ps_ptt_ratio_jerk(revenue: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ptt_drv3_025_revenue_ps_ptt_ratio_jerk feature"""
    revps = _safe_div(revenue, sharesbas)
    r = _safe_div(revps.cummax(), revps.cummin())
    vel = r.diff(5)
    return vel.diff(5)

# ── Registry ──────────────────────────────────────────────────────────────────

V07_A_REGISTRY = {
    "ptt_drv3_001_ptt_ratio_252d_jerk": {"inputs": ["close"], "func": ptt_drv3_001_ptt_ratio_252d_jerk},
    "ptt_drv3_002_recovery_fraction_63d_jerk": {"inputs": ["close"], "func": ptt_drv3_002_recovery_fraction_63d_jerk},
    "ptt_drv3_003_drawdown_to_ptt_ratio_jerk": {"inputs": ["close"], "func": ptt_drv3_003_drawdown_to_ptt_ratio_jerk},
    "ptt_drv3_004_days_since_trough_jerk": {"inputs": ["close"], "func": ptt_drv3_004_days_since_trough_jerk},
    "ptt_drv3_005_mktcap_ptt_ratio_jerk": {"inputs": ["close", "sharesbas"], "func": ptt_drv3_005_mktcap_ptt_ratio_jerk},
    "ptt_drv3_006_ptt_ratio_zscore_jerk": {"inputs": ["close"], "func": ptt_drv3_006_ptt_ratio_zscore_jerk},
    "ptt_drv3_007_recovery_fraction_std_jerk": {"inputs": ["close"], "func": ptt_drv3_007_recovery_fraction_std_jerk},
    "ptt_drv3_008_ptt_volatility_adjusted_jerk": {"inputs": ["close"], "func": ptt_drv3_008_ptt_volatility_adjusted_jerk},
    "ptt_drv3_009_current_to_midpoint_jerk": {"inputs": ["close"], "func": ptt_drv3_009_current_to_midpoint_jerk},
    "ptt_drv3_010_trough_persistence_jerk": {"inputs": ["close"], "func": ptt_drv3_010_trough_persistence_jerk},
    "ptt_drv3_011_ptt_ratio_expansion_jerk": {"inputs": ["close"], "func": ptt_drv3_011_ptt_ratio_expansion_jerk},
    "ptt_drv3_012_recovery_velocity_score_jerk": {"inputs": ["close"], "func": ptt_drv3_012_recovery_velocity_score_jerk},
    "ptt_drv3_013_ptt_convexity_jerk": {"inputs": ["close"], "func": ptt_drv3_013_ptt_convexity_jerk},
    "ptt_drv3_014_dsp_dst_ratio_jerk": {"inputs": ["close"], "func": ptt_drv3_014_dsp_dst_ratio_jerk},
    "ptt_drv3_015_recovery_fraction_log_drift_jerk": {"inputs": ["close"], "func": ptt_drv3_015_recovery_fraction_log_drift_jerk},
    "ptt_drv3_016_mktcap_recovery_efficiency_jerk": {"inputs": ["close", "sharesbas"], "func": ptt_drv3_016_mktcap_recovery_efficiency_jerk},
    "ptt_drv3_017_proximity_to_midpoint_spread_jerk": {"inputs": ["close"], "func": ptt_drv3_017_proximity_to_midpoint_spread_jerk},
    "ptt_drv3_018_recovery_fraction_entropy_jerk": {"inputs": ["close"], "func": ptt_drv3_018_recovery_fraction_entropy_jerk},
    "ptt_drv3_019_ptt_cycle_amplitude_jerk": {"inputs": ["close"], "func": ptt_drv3_019_ptt_cycle_amplitude_jerk},
    "ptt_drv3_020_ptt_final_pain_score_jerk": {"inputs": ["close"], "func": ptt_drv3_020_ptt_final_pain_score_jerk},
    "ptt_drv3_021_ptt_ratio_pct_rank_jerk": {"inputs": ["close"], "func": ptt_drv3_021_ptt_ratio_pct_rank_jerk},
    "ptt_drv3_022_recovery_fraction_zscore_jerk": {"inputs": ["close"], "func": ptt_drv3_022_recovery_fraction_zscore_jerk},
    "ptt_drv3_023_ptt_volatility_ratio_jerk": {"inputs": ["close"], "func": ptt_drv3_023_ptt_volatility_ratio_jerk},
    "ptt_drv3_024_pe_ptt_ratio_jerk": {"inputs": ["close", "netinc", "sharesbas"], "func": ptt_drv3_024_pe_ptt_ratio_jerk},
    "ptt_drv3_025_revenue_ps_ptt_ratio_jerk": {"inputs": ["revenue", "sharesbas"], "func": ptt_drv3_025_revenue_ps_ptt_ratio_jerk},
}
