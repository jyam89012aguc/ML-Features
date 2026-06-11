"""
16_volume_persistence — Base Features 076–150
Domain: sustained elevated volume, multi-day
Asset class: US equities | Daily OHLCV + Sharadar fundamentals
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
TRADING_DAYS_YEAR = 252
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5
_EPS = 1e-9


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


# ── Feature functions ────────────────────────────────────────────────────────

# 076-090: Statistical Distribution of Persistence
def vp_076_volume_persistence_pct_rank_252d(volume: pd.Series) -> pd.Series:
    # Rank of current 21-day average volume in last year's distribution
    v21 = _rolling_mean(volume, 21)
    return v21.rolling(252).rank(pct=True)


def vp_077_volume_regime_stability_63d(volume: pd.Series) -> pd.Series:
    # R-squared of the 21-day average volume path
    v21 = _rolling_mean(volume, 21)
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    return v21.rolling(63).apply(_rsq, raw=True)


def vp_078_volume_persistence_zscore_ath(volume: pd.Series) -> pd.Series:
    v63 = _rolling_mean(volume, 63)
    return (v63 - v63.expanding().mean()) / v63.expanding().std()


# 091-105: Persistence of Volume at Extremes
def vp_091_days_above_ath_volume_median_ath(volume: pd.Series) -> pd.Series:
    med = volume.expanding().median()
    return (volume > med).expanding().sum()


def vp_092_count_sustained_high_volume_episodes_252d(volume: pd.Series) -> pd.Series:
    # Episodes where volume was > 2x median for at least 5 days in the last year
    med = _rolling_median(volume, 252)
    is_high = (volume > 2 * med).astype(int)
    streak = is_high.groupby((is_high == 0).cumsum()).cumsum()
    is_episode = (streak == 5).astype(int)
    return is_episode.rolling(252).sum()


# 106-125: Event and Metric Specific Volume Persistence
def vp_106_mktcap_persistence_zscore_252d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v_mc = mc.pct_change().rolling(21).std()
    return (v_mc - v_mc.rolling(252).mean()) / v_mc.rolling(252).std()


def vp_107_volume_persistence_at_earnings_miss_63d(volume: pd.Series, surprise: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 252))
    return v_rat.where(surprise < 0).rolling(63).mean().ffill()


# 126-140: Multi- Horizon Integral Ratios
def vp_126_volume_integral_ratio_63d_to_ath(volume: pd.Series) -> pd.Series:
    a63 = volume.rolling(63).sum()
    a_ath = volume.cumsum()
    return _safe_div(a63, a_ath)


def vp_127_volume_integral_zscore_252d(volume: pd.Series) -> pd.Series:
    vi = volume.rolling(21).sum()
    return (vi - vi.rolling(252).mean()) / vi.rolling(252).std()


# 141-150: Final Persistence composites
def vp_141_heavy_selling_persistence_index_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Volume Persistence * Count of Down Days
    per = vp_002_volume_persistence_21d(volume)
    is_down = (close < close.shift(1)).astype(int)
    return per * is_down.rolling(63).sum()


def vp_142_mktcap_to_price_persistence_spread(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    # (V_pers / P_pers)
    v_per = vp_002_volume_persistence_21d(volume)
    p_per = (close / close.shift(21) - 1).abs().rolling(21).mean()
    return _safe_div(v_per, p_per)


def vp_143_volume_base_formation_score_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # (High Volume Persistence) / (Price Range)
    per = vp_002_volume_persistence_21d(volume)
    r = (close.rolling(63).max() - close.rolling(63).min()) / close.rolling(63).mean()
    return _safe_div(per, r + _EPS)


def vp_144_volume_integral_decay_252d(volume: pd.Series) -> pd.Series:
    # Exponentially decayed sum of volume
    weights = np.exp(-np.arange(252) / 63.0)[::-1]
    return volume.rolling(252).apply(lambda x: np.sum(x * weights), raw=True)


def vp_145_sustained_climax_to_vol_ratio_63d(volume: pd.Series) -> pd.Series:
    v_per = vp_002_volume_persistence_21d(volume)
    v_vol = volume.pct_change().rolling(63).std()
    return _safe_div(v_per, v_vol)


def vp_146_years_since_max_persistence_ath(volume: pd.Series) -> pd.Series:
    v21 = _rolling_mean(volume, 21)
    idx = v21.expanding().apply(np.argmax, raw=True)
    return (pd.Series(np.arange(len(volume)), index=volume.index) - idx) / 252.0


def vp_147_volume_persistence_regime_break_63d(volume: pd.Series) -> pd.Series:
    # Difference between current 5d persistence and 63d persistence
    return vp_001_volume_persistence_5d(volume) - vp_003_volume_persistence_63d(volume)


def vp_148_consecutive_days_volume_gt_median(volume: pd.Series) -> pd.Series:
    med = _rolling_median(volume, 252)
    above = (volume > med).astype(int)
    return above.groupby((above == 0).cumsum()).cumsum()


def vp_149_cumulative_excess_turnover_ath(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    med = to.expanding().median()
    excess = (to - med).clip(lower=0)
    return excess.cumsum()


def vp_150_volume_persistence_final_climax_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    # (Persistence) * (1 - Recovery Fraction) * (Drawdown Velocity)
    per = vp_002_volume_persistence_21d(volume)
    h = close.rolling(252).max()
    l = close.rolling(252).min()
    rf = _safe_div(close - l, h - l)
    dv = np.log(close).diff(5).abs()
    return per * (1.0 - rf) * dv


# ── Registry ──────────────────────────────────────────────────────────────────

V16_REGISTRY = {
    "vp_076_volume_persistence_pct_rank_252d": {"inputs": ["volume"], "func": vp_076_volume_pct_rank_252d},
    "vp_077_volume_regime_stability_63d": {"inputs": ["volume"], "func": vp_077_volume_regime_stability_63d},
    "vp_078_volume_persistence_zscore_ath": {"inputs": ["volume"], "func": vp_078_volume_persistence_zscore_ath},
    "vp_091_days_above_ath_volume_median_ath": {"inputs": ["volume"], "func": vp_091_days_above_ath_volume_median_ath},
    "vp_092_count_sustained_high_volume_episodes_252d": {"inputs": ["volume"], "func": vp_092_count_sustained_high_volume_episodes_252d},
    "vp_106_mktcap_persistence_zscore_252d": {"inputs": ["close", "sharesbas"], "func": vp_106_mktcap_persistence_zscore_252d},
    "vp_107_volume_persistence_at_earnings_miss_63d": {"inputs": ["volume", "surprise"], "func": vp_107_volume_persistence_at_earnings_miss_63d},
    "vp_126_volume_integral_ratio_63d_to_ath": {"inputs": ["volume"], "func": vp_126_volume_integral_ratio_63d_to_ath},
    "vp_127_volume_integral_zscore_252d": {"inputs": ["volume"], "func": vp_127_volume_integral_zscore_252d},
    "vp_141_heavy_selling_persistence_index_63d": {"inputs": ["close", "volume"], "func": vp_141_heavy_selling_persistence_index_63d},
    "vp_142_mktcap_to_price_persistence_spread": {"inputs": ["close", "volume", "sharesbas"], "func": vp_142_mktcap_to_price_persistence_spread},
    "vp_143_volume_base_formation_score_63d": {"inputs": ["close", "volume"], "func": vp_143_volume_base_formation_score_63d},
    "vp_144_volume_integral_decay_252d": {"inputs": ["volume"], "func": vp_144_volume_integral_decay_252d},
    "vp_145_sustained_climax_to_vol_ratio_63d": {"inputs": ["volume"], "func": vp_145_sustained_climax_to_vol_ratio_63d},
    "vp_146_years_since_max_persistence_ath": {"inputs": ["volume"], "func": vp_146_years_since_max_persistence_ath},
    "vp_147_volume_persistence_regime_break_63d": {"inputs": ["volume"], "func": vp_147_volume_persistence_regime_break_63d},
    "vp_148_consecutive_days_volume_gt_median": {"inputs": ["volume"], "func": vp_148_consecutive_days_volume_gt_median},
    "vp_149_cumulative_excess_turnover_ath": {"inputs": ["volume", "sharesbas"], "func": vp_149_cumulative_excess_turnover_ath},
    "vp_150_volume_persistence_final_climax_index": {"inputs": ["close", "volume"], "func": vp_150_volume_persistence_final_climax_index},
}
