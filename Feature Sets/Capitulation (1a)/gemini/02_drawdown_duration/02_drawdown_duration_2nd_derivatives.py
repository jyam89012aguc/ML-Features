"""
Drawdown Duration — 2nd Derivatives
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

def ddur_drv2_001_days_since_252d_high_velocity(close: pd.Series) -> pd.Series:
    """ddur_drv2_001_days_since_252d_high_velocity"""
    return _days_since_high(close, 252).diff(5)

def ddur_drv2_002_days_since_ath_velocity(close: pd.Series) -> pd.Series:
    """ddur_drv2_002_days_since_ath_velocity"""
    return _days_since_expanding_high(close).diff(5)

def ddur_drv2_003_consecutive_days_under_ath_accel(close: pd.Series) -> pd.Series:
    """ddur_drv2_003_consecutive_days_under_ath_accel"""
    h = close.cummax()
    under = (close < h).astype(int)
    dur = under.groupby((under == 0).cumsum()).cumsum()
    return dur.diff(5)

def ddur_drv2_004_days_since_last_new_low_ath_velocity(close: pd.Series) -> pd.Series:
    """ddur_drv2_004_days_since_last_new_low_ath_velocity"""
    l = close.cummin()
    is_low = (close == l)
    indices = pd.Series(np.arange(len(close)), index=close.index).where(is_low).ffill()
    dsl = pd.Series(np.arange(len(close)), index=close.index) - indices
    return dsl.diff(5)

def ddur_drv2_005_drawdown_age_index_velocity(close: pd.Series) -> pd.Series:
    """ddur_drv2_005_drawdown_age_index_velocity"""
    d21 = _days_since_high(close, 21)
    d63 = _days_since_high(close, 63)
    d252 = _days_since_high(close, 252)
    idx = (d21 + d63 + d252) / 3.0
    return idx.diff(5)

def ddur_drv2_006_days_since_ebitda_ath_velocity(ebitda: pd.Series) -> pd.Series:
    """ddur_drv2_006_days_since_ebitda_ath_velocity"""
    return _days_since_expanding_high(ebitda).diff(5)

def ddur_drv2_007_days_since_mktcap_ath_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ddur_drv2_007_days_since_mktcap_ath_velocity"""
    mc = close * sharesbas
    return _days_since_expanding_high(mc).diff(5)

def ddur_drv2_008_days_since_revenue_ps_ath_velocity(revenue: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ddur_drv2_008_days_since_revenue_ps_ath_velocity"""
    revps = revenue / sharesbas
    return _days_since_expanding_high(revps).diff(5)

def ddur_drv2_009_days_under_ma_200_accel(close: pd.Series) -> pd.Series:
    """ddur_drv2_009_days_under_ma_200_accel"""
    ma = close.rolling(200).mean()
    under = (close < ma).astype(int)
    dur = under.groupby((under == 0).cumsum()).cumsum()
    return dur.diff(5)

def ddur_drv2_010_days_since_high_vol_adjusted_accel(close: pd.Series) -> pd.Series:
    """ddur_drv2_010_days_since_high_vol_adjusted_accel"""
    dsh = _days_since_high(close, 252)
    vol = close.pct_change().rolling(21).std() * np.sqrt(252)
    return (dsh * vol).diff(5)

def ddur_drv2_011_days_since_ath_to_dsl_ratio_chg(close: pd.Series) -> pd.Series:
    """ddur_drv2_011_days_since_ath_to_dsl_ratio_chg"""
    dsh = _days_since_expanding_high(close)
    l = close.cummin()
    dsl = pd.Series(np.arange(len(close)), index=close.index) - pd.Series(np.arange(len(close)), index=close.index).where(close == l).ffill()
    ratio = _safe_div(dsh, dsl)
    return ratio.diff(5)

def ddur_drv2_012_integral_of_drawdown_depth_252d_velocity(close: pd.Series) -> pd.Series:
    """ddur_drv2_012_integral_of_drawdown_depth_252d_velocity"""
    h = close.rolling(252).max()
    dd = (h - close) / h
    integral = dd.rolling(252).sum()
    return integral.diff(5)

def ddur_drv2_013_days_spent_in_capitulation_zone_252d_velocity(close: pd.Series) -> pd.Series:
    """ddur_drv2_013_days_spent_in_capitulation_zone_252d_velocity"""
    l = close.rolling(252).min()
    days = (close <= l * 1.1).rolling(252).sum()
    return days.diff(5)

def ddur_drv2_014_days_since_last_share_issuance_velocity(sharesbas: pd.Series) -> pd.Series:
    """ddur_drv2_014_days_since_last_share_issuance_velocity"""
    diff = sharesbas.diff()
    indices = pd.Series(np.arange(len(sharesbas)), index=sharesbas.index).where(diff > 0).ffill()
    dsl = pd.Series(np.arange(len(sharesbas)), index=sharesbas.index) - indices
    return dsl.diff(5)

def ddur_drv2_015_days_since_last_insider_buy_velocity(insider_buys: pd.Series) -> pd.Series:
    """ddur_drv2_015_days_since_last_insider_buy_velocity"""
    indices = pd.Series(np.arange(len(insider_buys)), index=insider_buys.index).where(insider_buys > 0).ffill()
    dsl = pd.Series(np.arange(len(insider_buys)), index=insider_buys.index) - indices
    return dsl.diff(5)

def ddur_drv2_016_days_since_last_negative_surprise_velocity(surprise: pd.Series) -> pd.Series:
    """ddur_drv2_016_days_since_last_negative_surprise_velocity"""
    indices = pd.Series(np.arange(len(surprise)), index=surprise.index).where(surprise < 0).ffill()
    dsl = pd.Series(np.arange(len(surprise)), index=surprise.index) - indices
    return dsl.diff(5)

def ddur_drv2_017_duration_decay_index_velocity(close: pd.Series) -> pd.Series:
    """ddur_drv2_017_duration_decay_index_velocity"""
    dsh = _days_since_high(close, 252)
    decay = np.exp(-dsh / 252.0)
    return decay.diff(5)

def ddur_drv2_018_days_since_sma_200_high_velocity(close: pd.Series) -> pd.Series:
    """ddur_drv2_018_days_since_sma_200_high_velocity"""
    ma = close.rolling(200).mean()
    return _days_since_high(ma, 252).diff(5)

def ddur_drv2_019_days_since_ath_norm_by_vol_velocity(close: pd.Series) -> pd.Series:
    """ddur_drv2_019_days_since_ath_norm_by_vol_velocity"""
    dsh = _days_since_expanding_high(close)
    vol = close.pct_change().expanding().std() * np.sqrt(252)
    return (dsh * vol).diff(5)

def ddur_drv2_020_days_since_high_normalized_252d_velocity(close: pd.Series) -> pd.Series:
    """ddur_drv2_020_days_since_high_normalized_252d_velocity"""
    return (_days_since_high(close, 252) / 252.0).diff(5)

def ddur_drv2_021_days_under_minus_20_pct_252d_high_velocity(close: pd.Series) -> pd.Series:
    """ddur_drv2_021_days_under_minus_20_pct_252d_high_velocity"""
    h = close.rolling(252).max()
    under = (close < h * 0.8).rolling(252).sum()
    return under.diff(5)

def ddur_drv2_022_days_since_last_52w_low_velocity(close: pd.Series) -> pd.Series:
    """ddur_drv2_022_days_since_last_52w_low_velocity"""
    return _days_since_high(-close, 252).diff(5)

def ddur_drv2_023_days_since_ath_composite_score_velocity(close: pd.Series) -> pd.Series:
    """ddur_drv2_023_days_since_ath_composite_score_velocity"""
    dsh = _days_since_expanding_high(close)
    d252 = _days_since_high(close, 252)
    score = (0.7 * dsh + 0.3 * d252)
    return score.diff(5)

def ddur_drv2_024_days_since_pb_ratio_ath_velocity(close: pd.Series, equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ddur_drv2_024_days_since_pb_ratio_ath_velocity"""
    pb = close / (equity / sharesbas)
    return _days_since_expanding_high(pb).diff(5)

def ddur_drv2_025_days_since_ev_revenue_ath_velocity(close: pd.Series, sharesbas: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series) -> pd.Series:
    """ddur_drv2_025_days_since_ev_revenue_ath_velocity"""
    ev = (close * sharesbas) + debt - cashnequiv
    ratio = ev / revenue
    return _days_since_expanding_high(ratio).diff(5)

# ── Registry ──────────────────────────────────────────────────────────────────

V02_V_REGISTRY = {
    "ddur_drv2_001_days_since_252d_high_velocity": {"inputs": ["close"], "func": ddur_drv2_001_days_since_252d_high_velocity},
    "ddur_drv2_002_days_since_ath_velocity": {"inputs": ["close"], "func": ddur_drv2_002_days_since_ath_velocity},
    "ddur_drv2_003_consecutive_days_under_ath_accel": {"inputs": ["close"], "func": ddur_drv2_003_consecutive_days_under_ath_accel},
    "ddur_drv2_004_days_since_last_new_low_ath_velocity": {"inputs": ["close"], "func": ddur_drv2_004_days_since_last_new_low_ath_velocity},
    "ddur_drv2_005_drawdown_age_index_velocity": {"inputs": ["close"], "func": ddur_drv2_005_drawdown_age_index_velocity},
    "ddur_drv2_006_days_since_ebitda_ath_velocity": {"inputs": ["ebitda"], "func": ddur_drv2_006_days_since_ebitda_ath_velocity},
    "ddur_drv2_007_days_since_mktcap_ath_velocity": {"inputs": ["close", "sharesbas"], "func": ddur_drv2_007_days_since_mktcap_ath_velocity},
    "ddur_drv2_008_days_since_revenue_ps_ath_velocity": {"inputs": ["revenue", "sharesbas"], "func": ddur_drv2_008_days_since_revenue_ps_ath_velocity},
    "ddur_drv2_009_days_under_ma_200_accel": {"inputs": ["close"], "func": ddur_drv2_009_days_under_ma_200_accel},
    "ddur_drv2_010_days_since_high_vol_adjusted_accel": {"inputs": ["close"], "func": ddur_drv2_010_days_since_high_vol_adjusted_accel},
    "ddur_drv2_011_days_since_ath_to_dsl_ratio_chg": {"inputs": ["close"], "func": ddur_drv2_011_days_since_ath_to_dsl_ratio_chg},
    "ddur_drv2_012_integral_of_drawdown_depth_252d_velocity": {"inputs": ["close"], "func": ddur_drv2_012_integral_of_drawdown_depth_252d_velocity},
    "ddur_drv2_013_days_spent_in_capitulation_zone_252d_velocity": {"inputs": ["close"], "func": ddur_drv2_013_days_spent_in_capitulation_zone_252d_velocity},
    "ddur_drv2_014_days_since_last_share_issuance_velocity": {"inputs": ["sharesbas"], "func": ddur_drv2_014_days_since_last_share_issuance_velocity},
    "ddur_drv2_015_days_since_last_insider_buy_velocity": {"inputs": ["insider_buys"], "func": ddur_drv2_015_days_since_last_insider_buy_velocity},
    "ddur_drv2_016_days_since_last_negative_surprise_velocity": {"inputs": ["surprise"], "func": ddur_drv2_016_days_since_last_negative_surprise_velocity},
    "ddur_drv2_017_duration_decay_index_velocity": {"inputs": ["close"], "func": ddur_drv2_017_duration_decay_index_velocity},
    "ddur_drv2_018_days_since_sma_200_high_velocity": {"inputs": ["close"], "func": ddur_drv2_018_days_since_sma_200_high_velocity},
    "ddur_drv2_019_days_since_ath_norm_by_vol_velocity": {"inputs": ["close"], "func": ddur_drv2_019_days_since_ath_norm_by_vol_velocity},
    "ddur_drv2_020_days_since_high_normalized_252d_velocity": {"inputs": ["close"], "func": ddur_drv2_020_days_since_high_normalized_252d_velocity},
    "ddur_drv2_021_days_under_minus_20_pct_252d_high_velocity": {"inputs": ["close"], "func": ddur_drv2_021_days_under_minus_20_pct_252d_high_velocity},
    "ddur_drv2_022_days_since_last_52w_low_velocity": {"inputs": ["close"], "func": ddur_drv2_022_days_since_last_52w_low_velocity},
    "ddur_drv2_023_days_since_ath_composite_score_velocity": {"inputs": ["close"], "func": ddur_drv2_023_days_since_ath_composite_score_velocity},
    "ddur_drv2_024_days_since_pb_ratio_ath_velocity": {"inputs": ["close", "equity", "sharesbas"], "func": ddur_drv2_024_days_since_pb_ratio_ath_velocity},
    "ddur_drv2_025_days_since_ev_revenue_ath_velocity": {"inputs": ["close", "sharesbas", "debt", "cashnequiv", "revenue"], "func": ddur_drv2_025_days_since_ev_revenue_ath_velocity},
}
