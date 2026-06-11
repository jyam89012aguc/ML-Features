"""
Drawdown Duration — 3rd Derivatives
Domain: time spent in drawdown, days since high
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

def ddur_drv3_001_days_since_252d_high_jerk(close: pd.Series) -> pd.Series:
    """ddur_drv3_001_days_since_252d_high_jerk"""
    vel = _days_since_high(close, 252).diff(5)
    return vel.diff(5)

def ddur_drv3_002_days_since_ath_jerk(close: pd.Series) -> pd.Series:
    """ddur_drv3_002_days_since_ath_jerk"""
    vel = _days_since_expanding_high(close).diff(5)
    return vel.diff(5)

def ddur_drv3_003_consecutive_days_under_ath_jerk(close: pd.Series) -> pd.Series:
    """ddur_drv3_003_consecutive_days_under_ath_jerk"""
    h = close.cummax()
    under = (close < h).astype(int)
    dur = under.groupby((under == 0).cumsum()).cumsum()
    vel = dur.diff(5)
    return vel.diff(5)

def ddur_drv3_004_days_since_last_new_low_ath_jerk(close: pd.Series) -> pd.Series:
    """ddur_drv3_004_days_since_last_new_low_ath_jerk"""
    l = close.cummin()
    dsl = pd.Series(np.arange(len(close)), index=close.index) - pd.Series(np.arange(len(close)), index=close.index).where(close == l).ffill()
    vel = dsl.diff(5)
    return vel.diff(5)

def ddur_drv3_005_drawdown_age_index_jerk(close: pd.Series) -> pd.Series:
    """ddur_drv3_005_drawdown_age_index_jerk"""
    d21 = _days_since_high(close, 21)
    d63 = _days_since_high(close, 63)
    d252 = _days_since_high(close, 252)
    idx = (d21 + d63 + d252) / 3.0
    vel = idx.diff(5)
    return vel.diff(5)

def ddur_drv3_006_days_since_ebitda_ath_jerk(ebitda: pd.Series) -> pd.Series:
    """ddur_drv3_006_days_since_ebitda_ath_jerk"""
    vel = _days_since_expanding_high(ebitda).diff(5)
    return vel.diff(5)

def ddur_drv3_007_days_since_mktcap_ath_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ddur_drv3_007_days_since_mktcap_ath_jerk"""
    mc = close * sharesbas
    vel = _days_since_expanding_high(mc).diff(5)
    return vel.diff(5)

def ddur_drv3_008_days_since_revenue_ps_ath_jerk(revenue: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ddur_drv3_008_days_since_revenue_ps_ath_jerk"""
    revps = revenue / sharesbas
    vel = _days_since_expanding_high(revps).diff(5)
    return vel.diff(5)

def ddur_drv3_009_days_under_ma_200_jerk(close: pd.Series) -> pd.Series:
    """ddur_drv3_009_days_under_ma_200_jerk"""
    ma = close.rolling(200).mean()
    under = (close < ma).astype(int)
    dur = under.groupby((under == 0).cumsum()).cumsum()
    vel = dur.diff(5)
    return vel.diff(5)

def ddur_drv3_010_days_since_high_vol_adjusted_jerk(close: pd.Series) -> pd.Series:
    """ddur_drv3_010_days_since_high_vol_adjusted_jerk"""
    dsh = _days_since_high(close, 252)
    vol = close.pct_change().rolling(21).std() * np.sqrt(252)
    vel = (dsh * vol).diff(5)
    return vel.diff(5)

def ddur_drv3_011_days_since_ath_to_dsl_ratio_jerk(close: pd.Series) -> pd.Series:
    """ddur_drv3_011_days_since_ath_to_dsl_ratio_jerk"""
    dsh = _days_since_expanding_high(close)
    l = close.cummin()
    dsl = pd.Series(np.arange(len(close)), index=close.index) - pd.Series(np.arange(len(close)), index=close.index).where(close == l).ffill()
    ratio = _safe_div(dsh, dsl)
    vel = ratio.diff(5)
    return vel.diff(5)

def ddur_drv3_012_integral_of_drawdown_depth_252d_jerk(close: pd.Series) -> pd.Series:
    """ddur_drv3_012_integral_of_drawdown_depth_252d_jerk"""
    h = close.rolling(252).max()
    dd = (h - close) / h
    integral = dd.rolling(252).sum()
    vel = integral.diff(5)
    return vel.diff(5)

def ddur_drv3_013_days_spent_in_capitulation_zone_252d_jerk(close: pd.Series) -> pd.Series:
    """ddur_drv3_013_days_spent_in_capitulation_zone_252d_jerk"""
    l = close.rolling(252).min()
    days = (close <= l * 1.1).rolling(252).sum()
    vel = days.diff(5)
    return vel.diff(5)

def ddur_drv3_014_days_since_last_share_issuance_jerk(sharesbas: pd.Series) -> pd.Series:
    """ddur_drv3_014_days_since_last_share_issuance_jerk"""
    diff = sharesbas.diff()
    indices = pd.Series(np.arange(len(sharesbas)), index=sharesbas.index).where(diff > 0).ffill()
    dsl = pd.Series(np.arange(len(sharesbas)), index=sharesbas.index) - indices
    vel = dsl.diff(5)
    return vel.diff(5)

def ddur_drv3_015_days_since_last_insider_buy_jerk(insider_buys: pd.Series) -> pd.Series:
    """ddur_drv3_015_days_since_last_insider_buy_jerk"""
    indices = pd.Series(np.arange(len(insider_buys)), index=insider_buys.index).where(insider_buys > 0).ffill()
    dsl = pd.Series(np.arange(len(insider_buys)), index=insider_buys.index) - indices
    vel = dsl.diff(5)
    return vel.diff(5)

def ddur_drv3_016_days_since_last_negative_surprise_jerk(surprise: pd.Series) -> pd.Series:
    """ddur_drv3_016_days_since_last_negative_surprise_jerk"""
    indices = pd.Series(np.arange(len(surprise)), index=surprise.index).where(surprise < 0).ffill()
    dsl = pd.Series(np.arange(len(surprise)), index=surprise.index) - indices
    vel = dsl.diff(5)
    return vel.diff(5)

def ddur_drv3_017_duration_decay_index_jerk(close: pd.Series) -> pd.Series:
    """ddur_drv3_017_duration_decay_index_jerk"""
    dsh = _days_since_high(close, 252)
    decay = np.exp(-dsh / 252.0)
    vel = decay.diff(5)
    return vel.diff(5)

def ddur_drv3_018_days_since_sma_200_high_jerk(close: pd.Series) -> pd.Series:
    """ddur_drv3_018_days_since_sma_200_high_jerk"""
    ma = close.rolling(200).mean()
    vel = _days_since_high(ma, 252).diff(5)
    return vel.diff(5)

def ddur_drv3_019_days_since_ath_norm_by_vol_jerk(close: pd.Series) -> pd.Series:
    """ddur_drv3_019_days_since_ath_norm_by_vol_jerk"""
    dsh = _days_since_expanding_high(close)
    vol = close.pct_change().expanding().std() * np.sqrt(252)
    vel = (dsh * vol).diff(5)
    return vel.diff(5)

def ddur_drv3_020_days_since_high_normalized_252d_jerk(close: pd.Series) -> pd.Series:
    """ddur_drv3_020_days_since_high_normalized_252d_jerk"""
    vel = (_days_since_high(close, 252) / 252.0).diff(5)
    return vel.diff(5)

def ddur_drv3_021_days_under_minus_20_pct_252d_high_jerk(close: pd.Series) -> pd.Series:
    """ddur_drv3_021_days_under_minus_20_pct_252d_high_jerk"""
    h = close.rolling(252).max()
    under = (close < h * 0.8).rolling(252).sum()
    vel = under.diff(5)
    return vel.diff(5)

def ddur_drv3_022_days_since_last_52w_low_jerk(close: pd.Series) -> pd.Series:
    """ddur_drv3_022_days_since_last_52w_low_jerk"""
    vel = _days_since_high(-close, 252).diff(5)
    return vel.diff(5)

def ddur_drv3_023_days_since_ath_composite_score_jerk(close: pd.Series) -> pd.Series:
    """ddur_drv3_023_days_since_ath_composite_score_jerk"""
    dsh = _days_since_expanding_high(close)
    d252 = _days_since_high(close, 252)
    score = (0.7 * dsh + 0.3 * d252)
    vel = score.diff(5)
    return vel.diff(5)

def ddur_drv3_024_days_since_pb_ratio_ath_jerk(close: pd.Series, equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ddur_drv3_024_days_since_pb_ratio_ath_jerk"""
    pb = close / (equity / sharesbas)
    vel = _days_since_expanding_high(pb).diff(5)
    return vel.diff(5)

def ddur_drv3_025_days_since_ev_revenue_ath_jerk(close: pd.Series, sharesbas: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series) -> pd.Series:
    """ddur_drv3_025_days_since_ev_revenue_ath_jerk"""
    ev = (close * sharesbas) + debt - cashnequiv
    ratio = ev / revenue
    vel = _days_since_expanding_high(ratio).diff(5)
    return vel.diff(5)

# ── Registry ──────────────────────────────────────────────────────────────────

V02_A_REGISTRY = {
    "ddur_drv3_001_days_since_252d_high_jerk": {"inputs": ["close"], "func": ddur_drv3_001_days_since_252d_high_jerk},
    "ddur_drv3_002_days_since_ath_jerk": {"inputs": ["close"], "func": ddur_drv3_002_days_since_ath_jerk},
    "ddur_drv3_003_consecutive_days_under_ath_jerk": {"inputs": ["close"], "func": ddur_drv3_003_consecutive_days_under_ath_jerk},
    "ddur_drv3_004_days_since_last_new_low_ath_jerk": {"inputs": ["close"], "func": ddur_drv3_004_days_since_last_new_low_ath_jerk},
    "ddur_drv3_005_drawdown_age_index_jerk": {"inputs": ["close"], "func": ddur_drv3_005_drawdown_age_index_jerk},
    "ddur_drv3_006_days_since_ebitda_ath_jerk": {"inputs": ["ebitda"], "func": ddur_drv3_006_days_since_ebitda_ath_jerk},
    "ddur_drv3_007_days_since_mktcap_ath_jerk": {"inputs": ["close", "sharesbas"], "func": ddur_drv3_007_days_since_mktcap_ath_jerk},
    "ddur_drv3_008_days_since_revenue_ps_ath_jerk": {"inputs": ["revenue", "sharesbas"], "func": ddur_drv3_008_days_since_revenue_ps_ath_jerk},
    "ddur_drv3_009_days_under_ma_200_jerk": {"inputs": ["close"], "func": ddur_drv3_009_days_under_ma_200_jerk},
    "ddur_drv3_010_days_since_high_vol_adjusted_jerk": {"inputs": ["close"], "func": ddur_drv3_010_days_since_high_vol_adjusted_jerk},
    "ddur_drv3_011_days_since_ath_to_dsl_ratio_jerk": {"inputs": ["close"], "func": ddur_drv3_011_days_since_ath_to_dsl_ratio_jerk},
    "ddur_drv3_012_integral_of_drawdown_depth_252d_jerk": {"inputs": ["close"], "func": ddur_drv3_012_integral_of_drawdown_depth_252d_jerk},
    "ddur_drv3_013_days_spent_in_capitulation_zone_252d_jerk": {"inputs": ["close"], "func": ddur_drv3_013_days_spent_in_capitulation_zone_252d_jerk},
    "ddur_drv3_014_days_since_last_share_issuance_jerk": {"inputs": ["sharesbas"], "func": ddur_drv3_014_days_since_last_share_issuance_jerk},
    "ddur_drv3_015_days_since_last_insider_buy_jerk": {"inputs": ["insider_buys"], "func": ddur_drv3_015_days_since_last_insider_buy_jerk},
    "ddur_drv3_016_days_since_last_negative_surprise_jerk": {"inputs": ["surprise"], "func": ddur_drv3_016_days_since_last_negative_surprise_jerk},
    "ddur_drv3_017_duration_decay_index_jerk": {"inputs": ["close"], "func": ddur_drv3_017_duration_decay_index_jerk},
    "ddur_drv3_018_days_since_sma_200_high_jerk": {"inputs": ["close"], "func": ddur_drv3_018_days_since_sma_200_high_jerk},
    "ddur_drv3_019_days_since_ath_norm_by_vol_jerk": {"inputs": ["close"], "func": ddur_drv3_019_days_since_ath_norm_by_vol_jerk},
    "ddur_drv3_020_days_since_high_normalized_252d_jerk": {"inputs": ["close"], "func": ddur_drv3_020_days_since_high_normalized_252d_jerk},
    "ddur_drv3_021_days_under_minus_20_pct_252d_high_jerk": {"inputs": ["close"], "func": ddur_drv3_021_days_under_minus_20_pct_252d_high_jerk},
    "ddur_drv3_022_days_since_last_52w_low_jerk": {"inputs": ["close"], "func": ddur_drv3_022_days_since_last_52w_low_jerk},
    "ddur_drv3_023_days_since_ath_composite_score_jerk": {"inputs": ["close"], "func": ddur_drv3_023_days_since_ath_composite_score_jerk},
    "ddur_drv3_024_days_since_pb_ratio_ath_jerk": {"inputs": ["close", "equity", "sharesbas"], "func": ddur_drv3_024_days_since_pb_ratio_ath_jerk},
    "ddur_drv3_025_days_since_ev_revenue_ath_jerk": {"inputs": ["close", "sharesbas", "debt", "cashnequiv", "revenue"], "func": ddur_drv3_025_days_since_ev_revenue_ath_jerk},
}
