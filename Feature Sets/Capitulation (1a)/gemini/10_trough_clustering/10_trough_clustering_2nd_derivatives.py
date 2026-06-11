"""
Trough Clustering — 2nd Derivatives
Domain: frequency and density of new lows
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

def tcl_drv2_001_minima_count_63d_velocity(close: pd.Series) -> pd.Series:
    """tcl_drv2_001_minima_count_63d_velocity feature"""
    mins = _find_local_minima(close, order=5)
    cnt = mins.rolling(63).sum()
    return cnt.diff(5)

def tcl_drv2_002_proximity_to_last_min_velocity(close: pd.Series) -> pd.Series:
    """tcl_drv2_002_proximity_to_last_min_velocity feature"""
    mins = _find_local_minima(close, order=5)
    levels = close.where(mins == 1).ffill()
    p = _safe_div(close, levels)
    return p.diff(5)

def tcl_drv2_003_support_level_persistence_velocity(close: pd.Series) -> pd.Series:
    """tcl_drv2_003_support_level_persistence_velocity feature"""
    mins = _find_local_minima(close, order=5)
    levels = close.where(mins == 1).ffill()
    near = (close / levels - 1).abs() < 0.02
    cnt = near.rolling(252).sum()
    return cnt.diff(5)

def tcl_drv2_004_trough_alignment_velocity(close: pd.Series) -> pd.Series:
    """tcl_drv2_004_trough_alignment_velocity feature"""
    mins = _find_local_minima(close, order=5)
    levels = close.where(mins == 1)
    s = levels.rolling(252).std() / close.rolling(252).mean()
    align = _safe_div(1.0, s)
    return align.diff(5)

def tcl_drv2_005_days_between_minima_velocity(close: pd.Series) -> pd.Series:
    """tcl_drv2_005_days_between_minima_velocity feature"""
    mins = _find_local_minima(close, order=5)
    indices = pd.Series(np.arange(len(close)), index=close.index).where(mins == 1).ffill()
    gap = indices.diff().rolling(252).mean()
    return gap.diff(5)

def tcl_drv2_006_minima_intensity_velocity(close: pd.Series) -> pd.Series:
    """tcl_drv2_006_minima_intensity_velocity feature"""
    mins = _find_local_minima(close, order=5)
    cnt = mins.rolling(63).sum()
    idx = pd.Series(np.arange(len(close)), index=close.index).where(mins == 1).ffill()
    dist_std = idx.diff().rolling(63).std()
    intensity = _safe_div(cnt, dist_std)
    return intensity.diff(5)

def tcl_drv2_007_trough_reclaim_velocity(close: pd.Series) -> pd.Series:
    """tcl_drv2_007_trough_reclaim_velocity feature"""
    mins = _find_local_minima(close, order=5)
    levels = close.where(mins == 1).ffill()
    reclaim = (close > levels.shift(1)) & (close.shift(1) < levels.shift(1))
    return reclaim.rolling(63).sum().diff(5)

def tcl_drv2_008_trough_capitulation_velocity(close: pd.Series) -> pd.Series:
    """tcl_drv2_008_trough_capitulation_velocity feature"""
    cnt = _find_local_minima(close, order=5).rolling(63).sum()
    prox = _safe_div(close, close.cummin())
    score = cnt * (1.0 / prox)
    return score.diff(5)

def tcl_drv2_009_minima_concentration_velocity(close: pd.Series) -> pd.Series:
    """tcl_drv2_009_minima_concentration_velocity feature"""
    mins = _find_local_minima(close, order=5)
    avg_min = close.where(mins == 1).rolling(63).mean()
    near = (close / avg_min - 1).abs() < 0.05
    conc = near.rolling(63).mean()
    return conc.diff(5)

def tcl_drv2_010_mktcap_minima_count_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """tcl_drv2_010_mktcap_minima_count_velocity feature"""
    mc = close * sharesbas
    mins = _find_local_minima(mc, order=5)
    return mins.rolling(252).sum().diff(5)

def tcl_drv2_011_trough_amplitude_vol_velocity(close: pd.Series) -> pd.Series:
    """tcl_drv2_011_trough_amplitude_vol_velocity feature"""
    mins = _find_local_minima(close, order=5)
    levels = close.where(mins == 1)
    v = levels.rolling(63).std()
    return v.diff(5)

def tcl_drv2_012_trough_renewal_velocity(close: pd.Series) -> pd.Series:
    """tcl_drv2_012_trough_renewal_velocity feature"""
    l63 = (close == close.rolling(63).min()).astype(int).rolling(63).sum()
    mins = _find_local_minima(close, order=5).rolling(63).sum()
    ratio = _safe_div(l63, mins)
    return ratio.diff(5)

def tcl_drv2_013_days_since_trough_cluster_velocity(close: pd.Series) -> pd.Series:
    """tcl_drv2_013_days_since_trough_cluster_velocity feature"""
    mins = _find_local_minima(close, order=5)
    dens = mins.rolling(21).sum()
    idx = dens.rolling(252).apply(np.argmax, raw=True)
    dstc = 252 - 1 - idx
    return dstc.diff(5)

def tcl_drv2_014_consecutive_trough_tests_velocity(close: pd.Series) -> pd.Series:
    """tcl_drv2_014_consecutive_trough_tests_velocity feature"""
    l = close.rolling(21).min()
    near = (close <= l * 1.01).astype(int)
    dur = near.groupby((near == 0).cumsum()).cumsum()
    return dur.diff(5)

def tcl_drv2_015_trough_cycle_persistence_velocity(close: pd.Series) -> pd.Series:
    """tcl_drv2_015_trough_cycle_persistence_velocity feature"""
    mins = _find_local_minima(close, order=5)
    curr = mins.rolling(63).mean()
    hist = mins.expanding().mean()
    idx = _safe_div(curr, hist)
    return idx.diff(5)

def tcl_drv2_016_terminal_bottoming_score_velocity(close: pd.Series) -> pd.Series:
    """tcl_drv2_016_terminal_bottoming_score_velocity feature"""
    cnt = _find_local_minima(close, order=5).rolling(63).sum()
    h = close.rolling(252).max()
    dist_h = (h - close) / h
    score = cnt * dist_h
    return score.diff(5)

def tcl_drv2_017_trough_vol_to_price_vol_velocity(close: pd.Series) -> pd.Series:
    """tcl_drv2_017_trough_vol_to_price_vol_velocity feature"""
    mins = _find_local_minima(close, order=5)
    t_vol = close.where(mins == 1).rolling(63).std()
    p_vol = close.rolling(63).std()
    ratio = _safe_div(t_vol, p_vol)
    return ratio.diff(5)

def tcl_drv2_018_minima_gap_vol_velocity(close: pd.Series) -> pd.Series:
    """tcl_drv2_018_minima_gap_vol_velocity feature"""
    mins = _find_local_minima(close, order=5)
    idx = pd.Series(np.arange(len(close)), index=close.index).where(mins == 1).ffill()
    v = idx.diff().rolling(252).std()
    return v.diff(5)

def tcl_drv2_019_revenue_ps_minima_velocity(revenue: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """tcl_drv2_019_revenue_ps_minima_velocity feature"""
    revps = _safe_div(revenue, sharesbas)
    mins = _find_local_minima(revps, order=2)
    return mins.expanding().sum().diff(1)

def tcl_drv2_020_equity_ps_minima_velocity(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """tcl_drv2_020_equity_ps_minima_velocity feature"""
    bvps = _safe_div(equity, sharesbas)
    mins = _find_local_minima(bvps, order=2)
    return mins.expanding().sum().diff(1)

def tcl_drv2_021_price_mktcap_overlap_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """tcl_drv2_021_price_mktcap_overlap_velocity feature"""
    m_p = _find_local_minima(close, order=5)
    m_mc = _find_local_minima(close * sharesbas, order=5)
    overlap = (m_p & m_mc).rolling(63).sum()
    return overlap.diff(5)

def tcl_drv2_022_trough_depth_rank_velocity(close: pd.Series) -> pd.Series:
    """tcl_drv2_022_trough_depth_rank_velocity feature"""
    mins = _find_local_minima(close, order=5)
    levels = close.where(mins == 1)
    rank = levels.expanding().rank(pct=True).ffill()
    return rank.diff(5)

def tcl_drv2_023_trough_cluster_tightness_velocity(close: pd.Series) -> pd.Series:
    """tcl_drv2_023_trough_cluster_tightness_velocity feature"""
    cnt = _find_local_minima(close, order=5).rolling(63).sum()
    levels = close.where(_find_local_minima(close, order=5) == 1)
    disp = levels.rolling(63).std()
    ratio = _safe_div(cnt, disp + _EPS)
    return ratio.diff(5)

def tcl_drv2_024_ratio_troughs_low_quartile_velocity(close: pd.Series) -> pd.Series:
    """tcl_drv2_024_ratio_troughs_low_quartile_velocity feature"""
    mins = _find_local_minima(close, order=5)
    q25 = close.rolling(252).quantile(0.25)
    ratio = _safe_div(((mins == 1) & (close < q25)).rolling(252).sum(), mins.rolling(252).sum())
    return ratio.diff(5)

def tcl_drv2_025_trough_final_exhaustion_velocity(close: pd.Series) -> pd.Series:
    """tcl_drv2_025_trough_final_exhaustion_velocity feature"""
    cnt = _find_local_minima(close, order=5).rolling(63).sum()
    is_min = _find_local_minima(close, order=3)
    idx = pd.Series(np.arange(len(close)), index=close.index).where(is_min == 1).ffill()
    dsl = pd.Series(np.arange(len(close)), index=close.index) - idx
    idx_val = _safe_div(cnt, dsl + 1)
    return idx_val.diff(5)

# ── Registry ──────────────────────────────────────────────────────────────────

V10_V_REGISTRY = {
    "tcl_drv2_001_minima_count_63d_velocity": {"inputs": ["close"], "func": tcl_drv2_001_minima_count_63d_velocity},
    "tcl_drv2_002_proximity_to_last_min_velocity": {"inputs": ["close"], "func": tcl_drv2_002_proximity_to_last_min_velocity},
    "tcl_drv2_003_support_level_persistence_velocity": {"inputs": ["close"], "func": tcl_drv2_003_support_level_persistence_velocity},
    "tcl_drv2_004_trough_alignment_velocity": {"inputs": ["close"], "func": tcl_drv2_004_trough_alignment_velocity},
    "tcl_drv2_005_days_between_minima_velocity": {"inputs": ["close"], "func": tcl_drv2_005_days_between_minima_velocity},
    "tcl_drv2_006_minima_intensity_velocity": {"inputs": ["close"], "func": tcl_drv2_006_minima_intensity_velocity},
    "tcl_drv2_007_trough_reclaim_velocity": {"inputs": ["close"], "func": tcl_drv2_007_trough_reclaim_velocity},
    "tcl_drv2_008_trough_capitulation_velocity": {"inputs": ["close"], "func": tcl_drv2_008_trough_capitulation_velocity},
    "tcl_drv2_009_minima_concentration_velocity": {"inputs": ["close"], "func": tcl_drv2_009_minima_concentration_velocity},
    "tcl_drv2_010_mktcap_minima_count_velocity": {"inputs": ["close", "sharesbas"], "func": tcl_drv2_010_mktcap_minima_count_velocity},
    "tcl_drv2_011_trough_amplitude_vol_velocity": {"inputs": ["close"], "func": tcl_drv2_011_trough_amplitude_vol_velocity},
    "tcl_drv2_012_trough_renewal_velocity": {"inputs": ["close"], "func": tcl_drv2_012_trough_renewal_velocity},
    "tcl_drv2_013_days_since_trough_cluster_velocity": {"inputs": ["close"], "func": tcl_drv2_013_days_since_trough_cluster_velocity},
    "tcl_drv2_014_consecutive_trough_tests_velocity": {"inputs": ["close"], "func": tcl_drv2_014_consecutive_trough_tests_velocity},
    "tcl_drv2_015_trough_cycle_persistence_velocity": {"inputs": ["close"], "func": tcl_drv2_015_trough_cycle_persistence_velocity},
    "tcl_drv2_016_terminal_bottoming_score_velocity": {"inputs": ["close"], "func": tcl_drv2_016_terminal_bottoming_score_velocity},
    "tcl_drv2_017_trough_vol_to_price_vol_velocity": {"inputs": ["close"], "func": tcl_drv2_017_trough_vol_to_price_vol_velocity},
    "tcl_drv2_018_minima_gap_vol_velocity": {"inputs": ["close"], "func": tcl_drv2_018_minima_gap_vol_velocity},
    "tcl_drv2_019_revenue_ps_minima_velocity": {"inputs": ["revenue", "sharesbas"], "func": tcl_drv2_019_revenue_ps_minima_velocity},
    "tcl_drv2_020_equity_ps_minima_velocity": {"inputs": ["equity", "sharesbas"], "func": tcl_drv2_020_equity_ps_minima_velocity},
    "tcl_drv2_021_price_mktcap_overlap_velocity": {"inputs": ["close", "sharesbas"], "func": tcl_drv2_021_price_mktcap_overlap_velocity},
    "tcl_drv2_022_trough_depth_rank_velocity": {"inputs": ["close"], "func": tcl_drv2_022_trough_depth_rank_velocity},
    "tcl_drv2_023_trough_cluster_tightness_velocity": {"inputs": ["close"], "func": tcl_drv2_023_trough_cluster_tightness_velocity},
    "tcl_drv2_024_ratio_troughs_low_quartile_velocity": {"inputs": ["close"], "func": tcl_drv2_024_ratio_troughs_low_quartile_velocity},
    "tcl_drv2_025_trough_final_exhaustion_velocity": {"inputs": ["close"], "func": tcl_drv2_025_trough_final_exhaustion_velocity},
}
