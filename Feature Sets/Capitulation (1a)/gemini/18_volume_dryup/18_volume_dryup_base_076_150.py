"""
18_volume_dryup — Base Features 076–150
Domain: volume collapse / exhaustion of selling
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

# 076-090: Statistical Dry-Up Profiles
def vdry_076_volume_dryup_pct_rank_252d(volume: pd.Series) -> pd.Series:
    return volume.rolling(252).rank(pct=True)


def vdry_077_volume_apathy_zscore_252d(volume: pd.Series) -> pd.Series:
    # Z-score of (1/Volume) -> higher = more extreme dry-up
    inv_v = 1.0 / (volume + 1.0)
    return (inv_v - inv_v.rolling(252).mean()) / inv_v.rolling(252).std()


def vdry_078_volume_dryup_persistence_63d(volume: pd.Series) -> pd.Series:
    # Fraction of last 63 days with volume below 252d minimum * 1.5
    l252 = volume.rolling(252).min()
    return (volume < 1.5 * l252).rolling(63).mean()


# 091-105: Dry-Up Threshold Counts and Timing
def vdry_091_days_since_lowest_volume_252d(volume: pd.Series) -> pd.Series:
    idx = volume.rolling(252).apply(np.argmin, raw=True)
    return 252 - 1 - idx


def vdry_092_count_volume_downticks_21d(volume: pd.Series) -> pd.Series:
    # Number of days in last 21 where volume was less than previous day
    return (volume < volume.shift(1)).rolling(21).sum()


# 106-125: Metric-Specific Dry-Up Accelerators
def vdry_106_mktcap_dryup_velocity_63d(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v_rat = _safe_div(volume, _rolling_median(volume, 252))
    return v_rat.diff(63) / np.log(mc + _EPS)


def vdry_107_turnover_dryup_zscore_ath(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    return (to - to.expanding().mean()) / to.expanding().std()


# 126-140: Multi- Horizon Exhaustion Ratios
def vdry_126_volume_dryup_ratio_5d_to_63d(volume: pd.Series) -> pd.Series:
    v5 = _rolling_mean(volume, 5)
    v63 = _rolling_mean(volume, 63)
    return _safe_div(v5, v63)


def vdry_127_volume_dryup_to_vol_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # (Rolling Avg Volume / Current Volume) / Price Volatility
    v_pers = _safe_div(_rolling_mean(volume, 252), volume)
    p_vol = close.pct_change().rolling(252).std()
    return _safe_div(v_pers, p_vol)


# 141-150: Final Dry-Up composites
def vdry_141_terminal_apathy_index_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # (1 / Volume Spike) * (1 / Price Velocity)
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    p_vel = np.log(close).diff(5).abs()
    return _safe_div(1.0, v_rat * p_vel + _EPS)


def vdry_142_volume_exhaustion_probability_63d(volume: pd.Series) -> pd.Series:
    # Historical probability of volume staying low
    is_low = (volume < _rolling_median(volume, 252))
    persist = is_low & is_low.shift(1)
    return persist.rolling(63).sum() / (is_low.shift(1).rolling(63).sum() + _EPS)


def vdry_143_days_under_volume_floor_ath(volume: pd.Series) -> pd.Series:
    # Days since volume was last above its expanding average
    avg = volume.expanding().mean()
    above = (volume > avg)
    idx = pd.Series(np.arange(len(volume)), index=volume.index).where(above).ffill()
    return pd.Series(np.arange(len(volume)), index=volume.index) - idx


def vdry_144_volume_dryup_to_mktcap_ratio(volume: pd.Series, close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    return _safe_div(volume, mc)


def vdry_145_volume_starvation_velocity_21d(volume: pd.Series) -> pd.Series:
    # Change in starvation index
    q10 = volume.rolling(252).quantile(0.1)
    st = (volume < q10).rolling(63).mean()
    return st.diff(21)


def vdry_146_consecutive_days_volume_decline(volume: pd.Series) -> pd.Series:
    is_dec = (volume < volume.shift(1)).astype(int)
    return is_dec.groupby((is_dec == 0).cumsum()).cumsum()


def vdry_147_volume_climax_to_dryup_spread_63d(volume: pd.Series) -> pd.Series:
    mx = volume.rolling(63).max()
    curr = volume
    return (mx - curr) / mx


def vdry_148_volume_dryup_zscore_persistence_63d(volume: pd.Series) -> pd.Series:
    z = (volume - _rolling_mean(volume, 252)) / (volume.rolling(252).std() + _EPS)
    return z.rolling(63).mean()


def vdry_149_ratio_of_days_volume_lt_10pct_rank_252d(volume: pd.Series) -> pd.Series:
    rank = volume.rolling(252).rank(pct=True)
    return (rank < 0.10).rolling(252).mean()


def vdry_150_volume_dryup_final_exhaustion_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    # (Low Volume Persistence) * (Price Range Compression)
    v_per = (volume < _rolling_median(volume, 252)).rolling(63).mean()
    r = (close.rolling(21).max() - close.rolling(21).min()) / close.rolling(21).mean()
    return _safe_div(v_per, r + _EPS)


# ── Registry ──────────────────────────────────────────────────────────────────

V18_REGISTRY = {
    "vdry_076_volume_dryup_pct_rank_252d": {"inputs": ["volume"], "func": vdry_076_volume_dryup_pct_rank_252d},
    "vdry_077_volume_apathy_zscore_252d": {"inputs": ["volume"], "func": vdry_077_volume_apathy_zscore_252d},
    "vdry_078_volume_dryup_persistence_63d": {"inputs": ["volume"], "func": vdry_078_volume_dryup_persistence_63d},
    "vdry_091_days_since_lowest_volume_252d": {"inputs": ["volume"], "func": vdry_091_days_since_lowest_volume_252d},
    "vdry_092_count_volume_downticks_21d": {"inputs": ["volume"], "func": vdry_092_count_volume_downticks_21d},
    "vdry_106_mktcap_dryup_velocity_63d": {"inputs": ["close", "volume", "sharesbas"], "func": vdry_106_mktcap_dryup_velocity_63d},
    "vdry_107_turnover_dryup_zscore_ath": {"inputs": ["volume", "sharesbas"], "func": vdry_107_turnover_dryup_zscore_ath},
    "vdry_126_volume_dryup_ratio_5d_to_63d": {"inputs": ["volume"], "func": vdry_126_volume_dryup_ratio_5d_to_63d},
    "vdry_127_volume_dryup_to_vol_ratio_252d": {"inputs": ["close", "volume"], "func": vdry_127_volume_dryup_to_vol_ratio_252d},
    "vdry_141_terminal_apathy_index_21d": {"inputs": ["close", "volume"], "func": vdry_141_terminal_apathy_index_21d},
    "vdry_142_volume_exhaustion_probability_63d": {"inputs": ["volume"], "func": vdry_142_volume_exhaustion_probability_63d},
    "vdry_143_days_under_volume_floor_ath": {"inputs": ["volume"], "func": vdry_143_days_under_volume_floor_ath},
    "vdry_144_volume_dryup_to_mktcap_ratio": {"inputs": ["volume", "close", "sharesbas"], "func": vdry_144_volume_dryup_to_mktcap_ratio},
    "vdry_145_volume_starvation_velocity_21d": {"inputs": ["volume"], "func": vdry_145_volume_starvation_velocity_21d},
    "vdry_146_consecutive_days_volume_decline": {"inputs": ["volume"], "func": vdry_146_consecutive_days_volume_decline},
    "vdry_147_volume_climax_to_dryup_spread_63d": {"inputs": ["volume"], "func": vdry_147_volume_climax_to_dryup_spread_63d},
    "vdry_148_volume_dryup_zscore_persistence_63d": {"inputs": ["volume"], "func": vdry_148_volume_dryup_zscore_persistence_63d},
    "vdry_149_ratio_of_days_volume_lt_10pct_rank_252d": {"inputs": ["volume"], "func": vdry_149_ratio_of_days_volume_lt_10pct_rank_252d},
    "vdry_150_volume_dryup_final_exhaustion_score": {"inputs": ["close", "volume"], "func": vdry_150_volume_dryup_final_exhaustion_score},
}
