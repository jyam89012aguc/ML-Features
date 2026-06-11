"""
21_volume_concentration — Base Features 076–150
Domain: share of volume in worst N days
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


# ── Feature functions ────────────────────────────────────────────────────────

# 076-090: Higher-Order Concentration stats
def vcc_076_volume_gini_ath(volume: pd.Series) -> pd.Series:
    def _gini(x):
        x = np.sort(x)
        n = len(x)
        return (np.sum((2 * np.arange(1, n + 1) - n - 1) * x)) / (n * np.sum(x) + _EPS)
    return volume.expanding().apply(_gini, raw=True)


def vcc_077_volume_concentration_volatility_63d(volume: pd.Series) -> pd.Series:
    # Std dev of the top-5 volume share
    v_top5 = volume.rolling(63).apply(lambda x: np.sort(x)[-5:].sum() / (np.sum(x) + _EPS), raw=True)
    return v_top5.rolling(63).std()


def vcc_078_volume_tail_density_zscore_252d(volume: pd.Series) -> pd.Series:
    # Z-score of (90th percentile / 50th percentile)
    rat = _safe_div(volume.rolling(63).quantile(0.9), volume.rolling(63).median())
    return (rat - rat.rolling(252).mean()) / rat.rolling(252).std()


# 091-105: Proximity to Concentration Peaks
def vcc_091_days_since_peak_volume_share_252d(volume: pd.Series) -> pd.Series:
    c = _safe_div(volume, volume.rolling(252).sum())
    idx = c.rolling(252).apply(np.argmax, raw=True)
    return 252 - 1 - idx


def vcc_092_count_concentration_surges_252d(volume: pd.Series) -> pd.Series:
    # Number of times 5-day volume share > 2x its 252-day median
    c5 = _safe_div(volume.rolling(5).sum(), volume.rolling(252).sum())
    return (c5 > 2 * c5.rolling(252).median()).rolling(252).sum()


# 106-125: Metric-Specific Concentration Accelerators
def vcc_106_mktcap_concentration_velocity_63d(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    cv = volume * mc
    v_top5 = cv.rolling(63).apply(lambda x: np.sort(x)[-5:].sum() / (np.sum(x) + _EPS), raw=True)
    return v_top5.diff(63)


def vcc_107_turnover_gini_ath(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    def _gini(x):
        x = np.sort(x)
        n = len(x)
        return (np.sum((2 * np.arange(1, n + 1) - n - 1) * x)) / (n * np.sum(x) + _EPS)
    return to.expanding().apply(_gini, raw=True)


# 126-140: Multi- Horizon Flow Inequalities
def vcc_126_volume_concentration_spread_21_252(volume: pd.Series) -> pd.Series:
    def _gini(x):
        x = np.sort(x)
        n = len(x)
        return (np.sum((2 * np.arange(1, n + 1) - n - 1) * x)) / (n * np.sum(x) + _EPS)
    g21 = volume.rolling(21).apply(_gini, raw=True)
    g252 = volume.rolling(252).apply(_gini, raw=True)
    return g21 - g252


def vcc_127_climax_volume_to_total_ath_ratio(volume: pd.Series) -> pd.Series:
    # Volume on days > 99th percentile / Total Volume so far
    q99 = volume.expanding().quantile(0.99)
    v_climax = volume.where(volume > q99, 0).cumsum()
    return _safe_div(v_climax, volume.cumsum())


# 141-150: Final Concentration composites
def vcc_141_terminal_liquidation_score_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # (Gini Index) * (Down Day Share) * (1 - Proximity to Low)
    def _gini(x):
        x = np.sort(x)
        n = len(x)
        return (np.sum((2 * np.arange(1, n + 1) - n - 1) * x)) / (n * np.sum(x) + _EPS)
    g = volume.rolling(21).apply(_gini, raw=True)
    ds = _safe_div(volume.where(close < close.shift(1), 0).rolling(21).sum(), volume.rolling(21).sum())
    prox = _safe_div(close, close.rolling(252).min())
    return g * ds * (prox - 1.0).abs()


def vcc_142_volume_hhi_zscore_252d(volume: pd.Series) -> pd.Series:
    v_sum = volume.rolling(63).sum()
    v_share = _safe_div(volume, v_sum)
    hhi = (v_share**2).rolling(63).sum()
    return (hhi - hhi.rolling(252).mean()) / hhi.rolling(252).std()


def vcc_143_consecutive_days_with_extreme_kurtosis(volume: pd.Series) -> pd.Series:
    k = volume.rolling(63).kurt()
    is_high = (k > k.rolling(252).quantile(0.9))
    return is_high.astype(int).groupby((is_high == 0).cumsum()).cumsum()


def vcc_144_volume_share_velocity_21d(volume: pd.Series) -> pd.Series:
    s5 = vcc_002_volume_share_top_5d_63d(volume)
    return s5.diff(21)


def vcc_145_mktcap_to_volume_gini_ratio(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    def _gini(x):
        x = np.sort(x)
        n = len(x)
        return (np.sum((2 * np.arange(1, n + 1) - n - 1) * x)) / (n * np.sum(x) + _EPS)
    mc = close * sharesbas
    g_p = volume.rolling(63).apply(_gini, raw=True)
    g_m = mc.rolling(63).apply(_gini, raw=True)
    return _safe_div(g_p, g_m)


def vcc_146_years_since_max_gini_ath(volume: pd.Series) -> pd.Series:
    def _gini(x):
        x = np.sort(x)
        n = len(x)
        return (np.sum((2 * np.arange(1, n + 1) - n - 1) * x)) / (n * np.sum(x) + _EPS)
    g = volume.rolling(63).apply(_gini, raw=True)
    idx = g.expanding().apply(np.argmax, raw=True)
    return (pd.Series(np.arange(len(volume)), index=volume.index) - idx) / 252.0


def vcc_147_volume_climax_to_entropy_ratio_63d(volume: pd.Series) -> pd.Series:
    mx = volume.rolling(63).max()
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y, bins=10, density=True)
        p = h[h > 0]
        return -np.sum(p * np.log(p))
    e = volume.rolling(63).apply(_ent, raw=True)
    return _safe_div(mx / volume.rolling(63).mean(), e + _EPS)


def vcc_148_ratio_of_volume_in_gap_downs_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    v_gap = volume.where(open < close.shift(1), 0).rolling(63).sum()
    v_total = volume.rolling(63).sum()
    return _safe_div(v_gap, v_total)


def vcc_149_cumulative_excess_concentration_ath(volume: pd.Series) -> pd.Series:
    def _gini(x):
        x = np.sort(x)
        n = len(x)
        return (np.sum((2 * np.arange(1, n + 1) - n - 1) * x)) / (n * np.sum(x) + _EPS)
    g = volume.rolling(63).apply(_gini, raw=True)
    med = g.expanding().median()
    excess = (g - med).clip(lower=0)
    return excess.cumsum()


def vcc_150_final_liquidation_imbalance_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Composite: Gini * Down Volume Share * Volatility Rank
    def _gini(x):
        x = np.sort(x)
        n = len(x)
        return (np.sum((2 * np.arange(1, n + 1) - n - 1) * x)) / (n * np.sum(x) + _EPS)
    g = volume.rolling(63).apply(_gini, raw=True)
    ds = _safe_div(volume.where(close < close.shift(1), 0).rolling(63).sum(), volume.rolling(63).sum())
    vr = close.pct_change().rolling(21).std().expanding().rank(pct=True)
    return g * ds * vr


# ── Registry ──────────────────────────────────────────────────────────────────

V21_REGISTRY = {
    "vcc_076_volume_gini_ath": {"inputs": ["volume"], "func": vcc_076_volume_gini_ath},
    "vcc_077_volume_concentration_volatility_63d": {"inputs": ["volume"], "func": vcc_077_volume_concentration_volatility_63d},
    "vcc_078_volume_tail_density_zscore_252d": {"inputs": ["volume"], "func": vcc_078_volume_tail_density_zscore_252d},
    "vcc_091_days_since_peak_volume_share_252d": {"inputs": ["volume"], "func": vcc_091_days_since_peak_volume_share_252d},
    "vcc_092_count_concentration_surges_252d": {"inputs": ["volume"], "func": vcc_092_count_concentration_surges_252d},
    "vcc_106_mktcap_concentration_velocity_63d": {"inputs": ["close", "volume", "sharesbas"], "func": vcc_106_mktcap_concentration_velocity_63d},
    "vcc_107_turnover_gini_ath": {"inputs": ["volume", "sharesbas"], "func": vcc_107_turnover_gini_ath},
    "vcc_126_volume_concentration_spread_21_252": {"inputs": ["volume"], "func": vcc_126_volume_concentration_spread_21_252},
    "vcc_127_climax_volume_to_total_ath_ratio": {"inputs": ["volume"], "func": vcc_127_climax_volume_to_total_ath_ratio},
    "vcc_141_terminal_liquidation_score_21d": {"inputs": ["close", "volume"], "func": vcc_141_terminal_liquidation_score_21d},
    "vcc_142_volume_hhi_zscore_252d": {"inputs": ["volume"], "func": vcc_142_volume_hhi_zscore_252d},
    "vcc_143_consecutive_extreme_kurtosis_days": {"inputs": ["volume"], "func": vcc_143_consecutive_days_with_extreme_kurtosis},
    "vcc_144_volume_share_velocity_21d": {"inputs": ["volume"], "func": vcc_144_volume_share_velocity_21d},
    "vcc_145_mktcap_to_volume_gini_ratio": {"inputs": ["close", "volume", "sharesbas"], "func": vcc_145_mktcap_to_volume_gini_ratio},
    "vcc_146_years_since_max_gini_ath": {"inputs": ["volume"], "func": vcc_146_years_since_max_gini_ath},
    "vcc_147_volume_climax_to_entropy_ratio_63d": {"inputs": ["volume"], "func": vcc_147_volume_climax_to_entropy_ratio_63d},
    "vcc_148_ratio_vol_gap_downs_63d": {"inputs": ["close", "open", "volume"], "func": vcc_148_ratio_of_volume_in_gap_downs_63d},
    "vcc_149_cumulative_excess_concentration_ath": {"inputs": ["volume"], "func": vcc_149_cumulative_excess_concentration_ath},
    "vcc_150_final_liquidation_imbalance_index": {"inputs": ["close", "volume"], "func": vcc_150_final_liquidation_imbalance_index},
}
