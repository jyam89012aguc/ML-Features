"""
31_volatility_apathy — Base Features 076–150
Domain: collapse of volatility to extreme lows
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

# 076-090: Statistical Apathy Profiles
def vapt_076_vol_apathy_pct_rank_252d(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    return v21.rolling(252).rank(pct=True)


def vapt_077_vol_apathy_zscore_ath(close: pd.Series) -> pd.Series:
    # Inverse z-score: (1/Vol) z-score (higher = more extreme low vol)
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    inv_v = 1.0 / (v21 + _EPS)
    return (inv_v - inv_v.expanding().mean()) / (inv_v.expanding().std() + _EPS)


def vapt_078_vol_apathy_persistence_63d(close: pd.Series) -> pd.Series:
    # Fraction of last 63 days with 21d vol < 252d minimum * 1.5
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    l252 = v21.rolling(252).min()
    return (v21 < 1.5 * l252).rolling(63).mean()


# 091-105: Apathy Threshold Counts and Timing
def vapt_091_days_since_lowest_vol_252d(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    idx = v21.rolling(252).apply(np.argmin, raw=True)
    return 252 - 1 - idx


def vapt_092_count_vol_downticks_21d(close: pd.Series) -> pd.Series:
    # Number of days in last 21 where 5d vol was less than previous day
    v5 = np.log(close / close.shift(1)).rolling(5).std()
    return (v5 < v5.shift(1)).rolling(21).sum()


# 106-125: Metric-Specific Apathy Accelerators
def vapt_106_mktcap_vol_apathy_velocity_63d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v21 = np.log(mc / mc.shift(1)).rolling(21).std()
    rat = _safe_div(v21, v21.rolling(252).median())
    return rat.diff(63) / np.log(mc + _EPS)


def vapt_107_turnover_vol_apathy_zscore_ath(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    v_to = to.pct_change().rolling(21).std()
    return (v_to - v_to.expanding().mean()) / (v_to.expanding().std() + _EPS)


# 126-140: Multi- Horizon Exhaustion Ratios
def vapt_126_vol_apathy_ratio_5d_to_63d(close: pd.Series) -> pd.Series:
    v5 = np.log(close / close.shift(1)).rolling(5).std()
    v63 = np.log(close / close.shift(1)).rolling(63).std()
    return _safe_div(v5, v63)


def vapt_127_vol_apathy_to_vol_ratio_252d(close: pd.Series) -> pd.Series:
    # (Rolling Avg Vol / Current Vol) / Volatility of Volatility
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v_pers = _safe_div(v21.rolling(252).mean(), v21)
    vov = v21.rolling(63).std()
    return _safe_div(v_pers, vov)


# 141-150: Final Apathy composites
def vapt_141_terminal_washout_index_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # (1 / Volatility Spike) * (1 / Volume Spike) * (1 / Price Velocity)
    v_rat = vapt_001_vol_apathy_ratio_21d(close)
    vol_rat = _safe_div(volume, volume.rolling(252).median())
    p_vel = np.log(close).diff(5).abs()
    return _safe_div(1.0, v_rat * vol_rat * p_vel + _EPS)


def vapt_142_vol_exhaustion_probability_63d(close: pd.Series) -> pd.Series:
    # Historical probability of 21d volatility staying below its median
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    med = v21.rolling(252).median()
    is_low = (v21 < med)
    persist = is_low & is_low.shift(1)
    return persist.rolling(63).sum() / (is_low.shift(1).rolling(63).sum() + _EPS)


def vapt_143_days_under_vol_floor_ath(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    avg = v21.expanding().mean()
    idx = pd.Series(np.arange(len(close)), index=close.index).where(v21 > avg).ffill()
    return pd.Series(np.arange(len(close)), index=close.index) - idx


def vapt_144_vol_apathy_to_mktcap_ratio(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    mc = close * sharesbas
    return _safe_div(v21, mc)


def vapt_145_vol_starvation_velocity_21d(close: pd.Series) -> pd.Series:
    v5 = np.log(close / close.shift(1)).rolling(5).std()
    q10 = v5.rolling(252).quantile(0.1)
    st = (v5 < q10).rolling(63).mean()
    return st.diff(21)


def vapt_146_consecutive_days_vol_decline(close: pd.Series) -> pd.Series:
    v5 = np.log(close / close.shift(1)).rolling(5).std()
    is_dec = (v5 < v5.shift(1)).astype(int)
    return is_dec.groupby((is_dec == 0).cumsum()).cumsum()


def vapt_147_vol_climax_to_apathy_spread_63d(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    mx = v.rolling(63).max()
    return (mx - v) / (mx + _EPS)


def vapt_148_vol_apathy_zscore_persistence_63d(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    z = (v21 - v21.rolling(252).mean()) / (v21.rolling(252).std() + _EPS)
    return z.rolling(63).mean()


def vapt_149_ratio_of_days_vol_lt_10pct_rank_252d(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    rank = v21.rolling(252).rank(pct=True)
    return (rank < 0.10).rolling(252).mean()


def vapt_150_vol_apathy_final_exhaustion_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    # (Low Vol Persistence) * (Price Range Compression) * (Volume Dry-up)
    v_per = (np.log(close / close.shift(1)).rolling(21).std() < _rolling_median(np.log(close / close.shift(1)).rolling(21).std(), 252)).rolling(63).mean()
    r = (close.rolling(21).max() - close.rolling(21).min()) / close.rolling(21).mean()
    v_dry = _safe_div(_rolling_median(volume, 252), volume)
    return v_per * (1.0 / (r + _EPS)) * v_dry


# ── Registry ──────────────────────────────────────────────────────────────────

V31_REGISTRY = {
    "vapt_076_vol_apathy_pct_rank_252d": {"inputs": ["close"], "func": vapt_076_vol_apathy_pct_rank_252d},
    "vapt_077_vol_apathy_zscore_ath": {"inputs": ["close"], "func": vapt_077_vol_apathy_zscore_ath},
    "vapt_078_vol_apathy_persistence_63d": {"inputs": ["close"], "func": vapt_078_vol_apathy_persistence_63d},
    "vapt_091_days_since_lowest_vol_252d": {"inputs": ["close"], "func": vapt_091_days_since_lowest_vol_252d},
    "vapt_092_count_vol_downticks_21d": {"inputs": ["close"], "func": vapt_092_count_vol_downticks_21d},
    "vapt_106_mktcap_vol_apathy_velocity_63d": {"inputs": ["close", "sharesbas", "volume"], "func": vapt_106_mktcap_vol_apathy_velocity_63d},
    "vapt_107_turnover_vol_apathy_zscore_ath": {"inputs": ["volume", "sharesbas"], "func": vapt_107_turnover_vol_apathy_zscore_ath},
    "vapt_126_vol_apathy_ratio_5d_to_63d": {"inputs": ["close"], "func": vapt_126_vol_apathy_ratio_5d_to_63d},
    "vapt_127_vol_apathy_to_vol_ratio_252d": {"inputs": ["close"], "func": vapt_127_vol_apathy_to_vol_ratio_252d},
    "vapt_141_terminal_washout_index_21d": {"inputs": ["close", "volume"], "func": vapt_141_terminal_washout_index_21d},
    "vapt_142_vol_exhaustion_probability_63d": {"inputs": ["close"], "func": vapt_142_vol_exhaustion_probability_63d},
    "vapt_143_days_under_vol_floor_ath": {"inputs": ["close"], "func": vapt_143_days_under_vol_floor_ath},
    "vapt_144_vol_apathy_to_mktcap_ratio": {"inputs": ["close", "sharesbas"], "func": vapt_144_vol_apathy_to_mktcap_ratio},
    "vapt_145_vol_starvation_velocity_21d": {"inputs": ["close"], "func": vapt_145_vol_starvation_velocity_21d},
    "vapt_146_consecutive_days_vol_decline": {"inputs": ["close"], "func": vapt_146_consecutive_days_vol_decline},
    "vapt_147_vol_climax_to_apathy_spread_63d": {"inputs": ["close"], "func": vapt_147_vol_climax_to_apathy_spread_63d},
    "vapt_148_vol_apathy_zscore_persistence_63d": {"inputs": ["close"], "func": vapt_148_vol_apathy_zscore_persistence_63d},
    "vapt_149_ratio_days_vol_lt_10pct_rank": {"inputs": ["close"], "func": vapt_149_ratio_of_days_vol_lt_10pct_rank_252d},
    "vapt_150_vol_apathy_final_exhaustion": {"inputs": ["close", "volume"], "func": vapt_150_vol_apathy_final_exhaustion_score},
}
