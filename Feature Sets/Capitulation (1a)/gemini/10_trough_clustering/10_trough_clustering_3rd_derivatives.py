"""
Trough Clustering — 3rd Derivatives
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

def tcl_drv3_001_minima_count_63d_jerk(close: pd.Series) -> pd.Series:
    """tcl_drv3_001_minima_count_63d_jerk feature"""
    mins = _find_local_minima(close, order=5)
    cnt = mins.rolling(63).sum()
    vel = cnt.diff(5)
    return vel.diff(5)

def tcl_drv3_002_proximity_to_last_min_jerk(close: pd.Series) -> pd.Series:
    """tcl_drv3_002_proximity_to_last_min_jerk feature"""
    mins = _find_local_minima(close, order=5)
    levels = close.where(mins == 1).ffill()
    p = _safe_div(close, levels)
    vel = p.diff(5)
    return vel.diff(5)

def tcl_drv3_003_support_level_persistence_jerk(close: pd.Series) -> pd.Series:
    """tcl_drv3_003_support_level_persistence_jerk feature"""
    mins = _find_local_minima(close, order=5)
    levels = close.where(mins == 1).ffill()
    near = (close / levels - 1).abs() < 0.02
    cnt = near.rolling(252).sum()
    vel = cnt.diff(5)
    return vel.diff(5)

def tcl_drv3_004_trough_alignment_jerk(close: pd.Series) -> pd.Series:
    """tcl_drv3_004_trough_alignment_jerk feature"""
    mins = _find_local_minima(close, order=5)
    levels = close.where(mins == 1)
    s = levels.rolling(252).std() / (close.rolling(252).mean() + _EPS)
    align = _safe_div(1.0, s)
    vel = align.diff(5)
    return vel.diff(5)

def tcl_drv3_005_days_between_minima_jerk(close: pd.Series) -> pd.Series:
    """tcl_drv3_005_days_between_minima_jerk feature"""
    mins = _find_local_minima(close, order=5)
    indices = pd.Series(np.arange(len(close)), index=close.index).where(mins == 1).ffill()
    gap = indices.diff().rolling(252).mean()
    vel = gap.diff(5)
    return vel.diff(5)

def tcl_drv3_006_minima_intensity_jerk(close: pd.Series) -> pd.Series:
    """tcl_drv3_006_minima_intensity_jerk feature"""
    mins = _find_local_minima(close, order=5)
    cnt = mins.rolling(63).sum()
    idx = pd.Series(np.arange(len(close)), index=close.index).where(mins == 1).ffill()
    dist_std = idx.diff().rolling(63).std()
    intensity = _safe_div(cnt, dist_std)
    vel = intensity.diff(5)
    return vel.diff(5)

def tcl_drv3_007_trough_reclaim_jerk(close: pd.Series) -> pd.Series:
    """tcl_drv3_007_trough_reclaim_jerk feature"""
    mins = _find_local_minima(close, order=5)
    levels = close.where(mins == 1).ffill()
    reclaim = (close > levels.shift(1)) & (close.shift(1) < levels.shift(1))
    vel = reclaim.rolling(63).sum().diff(5)
    return vel.diff(5)

def tcl_drv3_008_trough_capitulation_jerk(close: pd.Series) -> pd.Series:
    """tcl_drv3_008_trough_capitulation_jerk feature"""
    cnt = _find_local_minima(close, order=5).rolling(63).sum()
    prox = _safe_div(close, close.cummin())
    score = cnt * (1.0 / prox)
    vel = score.diff(5)
    return vel.diff(5)

def tcl_drv3_009_minima_concentration_jerk(close: pd.Series) -> pd.Series:
    """tcl_drv3_009_minima_concentration_jerk feature"""
    mins = _find_local_minima(close, order=5)
    avg_min = close.where(mins == 1).rolling(63).mean()
    near = (close / avg_min - 1).abs() < 0.05
    conc = near.rolling(63).mean()
    vel = conc.diff(5)
    return vel.diff(5)

def tcl_drv3_010_mktcap_minima_count_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """tcl_drv3_010_mktcap_minima_count_jerk feature"""
    mc = close * sharesbas
    mins = _find_local_minima(mc, order=5)
    vel = mins.rolling(252).sum().diff(5)
    return vel.diff(5)

def tcl_drv3_011_trough_amplitude_vol_jerk(close: pd.Series) -> pd.Series:
    """tcl_drv3_011_trough_amplitude_vol_jerk feature"""
    mins = _find_local_minima(close, order=5)
    levels = close.where(mins == 1)
    v = levels.rolling(63).std()
    vel = v.diff(5)
    return vel.diff(5)

def tcl_drv3_012_trough_renewal_jerk(close: pd.Series) -> pd.Series:
    """tcl_drv3_012_trough_renewal_jerk feature"""
    l63 = (close == close.rolling(63).min()).astype(int).rolling(63).sum()
    mins = _find_local_minima(close, order=5).rolling(63).sum()
    ratio = _safe_div(l63, mins)
    vel = ratio.diff(5)
    return vel.diff(5)

def tcl_drv3_013_days_since_trough_cluster_jerk(close: pd.Series) -> pd.Series:
    """tcl_drv3_013_days_since_trough_cluster_jerk feature"""
    mins = _find_local_minima(close, order=5)
    dens = mins.rolling(21).sum()
    idx = dens.rolling(252).apply(np.argmax, raw=True)
    dstc = 252 - 1 - idx
    vel = dstc.diff(5)
    return vel.diff(5)

def tcl_drv3_014_consecutive_trough_tests_jerk(close: pd.Series) -> pd.Series:
    """tcl_drv3_014_consecutive_trough_tests_jerk feature"""
    l = close.rolling(21).min()
    near = (close <= l * 1.01).astype(int)
    dur = near.groupby((near == 0).cumsum()).cumsum()
    vel = dur.diff(5)
    return vel.diff(5)

def tcl_drv3_015_trough_cycle_persistence_jerk(close: pd.Series) -> pd.Series:
    """tcl_drv3_015_trough_cycle_persistence_jerk feature"""
    mins = _find_local_minima(close, order=5)
    curr = mins.rolling(63).mean()
    hist = mins.expanding().mean()
    idx = _safe_div(curr, hist)
    vel = idx.diff(5)
    return vel.diff(5)

def tcl_drv3_016_terminal_bottoming_score_jerk(close: pd.Series) -> pd.Series:
    """tcl_drv3_016_terminal_bottoming_score_jerk feature"""
    cnt = _find_local_minima(close, order=5).rolling(63).sum()
    h = close.rolling(252).max()
    dist_h = (h - close) / h
    score = cnt * dist_h
    vel = score.diff(5)
    return vel.diff(5)

def tcl_drv3_017_trough_vol_to_price_vol_jerk(close: pd.Series) -> pd.Series:
    """tcl_drv3_017_trough_vol_to_price_vol_jerk feature"""
    mins = _find_local_minima(close, order=5)
    t_vol = close.where(mins == 1).rolling(63).std()
    p_vol = close.rolling(63).std()
    ratio = _safe_div(t_vol, p_vol)
    vel = ratio.diff(5)
    return vel.diff(5)

def tcl_drv3_018_minima_gap_vol_jerk(close: pd.Series) -> pd.Series:
    """tcl_drv3_018_minima_gap_vol_jerk feature"""
    mins = _find_local_minima(close, order=5)
    idx = pd.Series(np.arange(len(close)), index=close.index).where(mins == 1).ffill()
    v = idx.diff().rolling(252).std()
    vel = v.diff(5)
    return vel.diff(5)

def tcl_drv3_019_revenue_ps_minima_jerk(revenue: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """tcl_drv3_019_revenue_ps_minima_jerk feature"""
    revps = _safe_div(revenue, sharesbas)
    mins = _find_local_minima(revps, order=2)
    vel = mins.expanding().sum().diff(1)
    return vel.diff(1)

def tcl_drv3_020_equity_ps_minima_jerk(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """tcl_drv3_020_equity_ps_minima_jerk feature"""
    bvps = _safe_div(equity, sharesbas)
    mins = _find_local_minima(bvps, order=2)
    vel = mins.expanding().sum().diff(1)
    return vel.diff(1)

def tcl_drv3_021_price_mktcap_overlap_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """tcl_drv3_021_price_mktcap_overlap_jerk feature"""
    m_p = _find_local_minima(close, order=5)
    m_mc = _find_local_minima(close * sharesbas, order=5)
    overlap = (m_p & m_mc).rolling(63).sum()
    vel = overlap.diff(5)
    return vel.diff(5)

def tcl_drv3_022_trough_depth_rank_jerk(close: pd.Series) -> pd.Series:
    """tcl_drv3_022_trough_depth_rank_jerk feature"""
    mins = _find_local_minima(close, order=5)
    levels = close.where(mins == 1)
    rank = levels.expanding().rank(pct=True).ffill()
    vel = rank.diff(5)
    return vel.diff(5)

def tcl_drv3_023_trough_cluster_tightness_jerk(close: pd.Series) -> pd.Series:
    """tcl_drv3_023_trough_cluster_tightness_jerk feature"""
    cnt = _find_local_minima(close, order=5).rolling(63).sum()
    levels = close.where(_find_local_minima(close, order=5) == 1)
    disp = levels.rolling(63).std()
    ratio = _safe_div(cnt, disp + _EPS)
    vel = ratio.diff(5)
    return vel.diff(5)

def tcl_drv3_024_ratio_troughs_low_quartile_jerk(close: pd.Series) -> pd.Series:
    """tcl_drv3_024_ratio_troughs_low_quartile_jerk feature"""
    mins = _find_local_minima(close, order=5)
    q25 = close.rolling(252).quantile(0.25)
    ratio = _safe_div(((mins == 1) & (close < q25)).rolling(252).sum(), mins.rolling(252).sum())
    vel = ratio.diff(5)
    return vel.diff(5)

def tcl_drv3_025_trough_final_exhaustion_jerk(close: pd.Series) -> pd.Series:
    """tcl_drv3_025_trough_final_exhaustion_jerk feature"""
    cnt = _find_local_minima(close, order=5).rolling(63).sum()
    is_min = _find_local_minima(close, order=3)
    idx = pd.Series(np.arange(len(close)), index=close.index).where(is_min == 1).ffill()
    dsl = pd.Series(np.arange(len(close)), index=close.index) - idx
    idx_val = _safe_div(cnt, dsl + 1)
    vel = idx_val.diff(5)
    return vel.diff(5)

# ── Registry ──────────────────────────────────────────────────────────────────

V10_A_REGISTRY = {
    "tcl_drv3_001_minima_count_63d_jerk": {"inputs": ["close"], "func": tcl_drv3_001_minima_count_63d_jerk},
    "tcl_drv3_002_proximity_to_last_min_jerk": {"inputs": ["close"], "func": tcl_drv3_002_proximity_to_last_min_jerk},
    "tcl_drv3_003_support_level_persistence_jerk": {"inputs": ["close"], "func": tcl_drv3_003_support_level_persistence_jerk},
    "tcl_drv3_004_trough_alignment_jerk": {"inputs": ["close"], "func": tcl_drv3_004_trough_alignment_jerk},
    "tcl_drv3_005_days_between_minima_jerk": {"inputs": ["close"], "func": tcl_drv3_005_days_between_minima_jerk},
    "tcl_drv3_006_minima_intensity_jerk": {"inputs": ["close"], "func": tcl_drv3_006_minima_intensity_jerk},
    "tcl_drv3_007_trough_reclaim_jerk": {"inputs": ["close"], "func": tcl_drv3_007_trough_reclaim_jerk},
    "tcl_drv3_008_trough_capitulation_jerk": {"inputs": ["close"], "func": tcl_drv3_008_trough_capitulation_jerk},
    "tcl_drv3_009_minima_concentration_jerk": {"inputs": ["close"], "func": tcl_drv3_009_minima_concentration_jerk},
    "tcl_drv3_010_mktcap_minima_count_jerk": {"inputs": ["close", "sharesbas"], "func": tcl_drv3_010_mktcap_minima_count_jerk},
    "tcl_drv3_011_trough_amplitude_vol_jerk": {"inputs": ["close"], "func": tcl_drv3_011_trough_amplitude_vol_jerk},
    "tcl_drv3_012_trough_renewal_jerk": {"inputs": ["close"], "func": tcl_drv3_012_trough_renewal_jerk},
    "tcl_drv3_013_days_since_trough_cluster_jerk": {"inputs": ["close"], "func": tcl_drv3_013_days_since_trough_cluster_jerk},
    "tcl_drv3_014_consecutive_trough_tests_jerk": {"inputs": ["close"], "func": tcl_drv3_014_consecutive_trough_tests_jerk},
    "tcl_drv3_015_trough_cycle_persistence_jerk": {"inputs": ["close"], "func": tcl_drv3_015_trough_cycle_persistence_jerk},
    "tcl_drv3_016_terminal_bottoming_score_jerk": {"inputs": ["close"], "func": tcl_drv3_016_terminal_bottoming_score_jerk},
    "tcl_drv3_017_trough_vol_to_price_vol_jerk": {"inputs": ["close"], "func": tcl_drv3_017_trough_vol_to_price_vol_jerk},
    "tcl_drv3_018_minima_gap_vol_jerk": {"inputs": ["close"], "func": tcl_drv3_018_minima_gap_vol_jerk},
    "tcl_drv3_019_revenue_ps_minima_jerk": {"inputs": ["revenue", "sharesbas"], "func": tcl_drv3_019_revenue_ps_minima_jerk},
    "tcl_drv3_020_equity_ps_minima_jerk": {"inputs": ["equity", "sharesbas"], "func": tcl_drv3_020_equity_ps_minima_jerk},
    "tcl_drv3_021_price_mktcap_overlap_jerk": {"inputs": ["close", "sharesbas"], "func": tcl_drv3_021_price_mktcap_overlap_jerk},
    "tcl_drv3_022_trough_depth_rank_jerk": {"inputs": ["close"], "func": tcl_drv3_022_trough_depth_rank_jerk},
    "tcl_drv3_023_trough_cluster_tightness_jerk": {"inputs": ["close"], "func": tcl_drv3_023_trough_cluster_tightness_jerk},
    "tcl_drv3_024_ratio_troughs_low_quartile_jerk": {"inputs": ["close"], "func": tcl_drv3_024_ratio_troughs_low_quartile_jerk},
    "tcl_drv3_025_trough_final_exhaustion_jerk": {"inputs": ["close"], "func": tcl_drv3_025_trough_final_exhaustion_jerk},
}
