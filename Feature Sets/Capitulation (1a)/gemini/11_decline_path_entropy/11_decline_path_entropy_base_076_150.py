"""
11_decline_path_entropy — Base Features 076–150
Domain: smooth-vs-jagged structure of the fall
Asset class: US equities | Daily OHLCV + Sharadar fundamentals
"""
import numpy as np
import pandas as pd
from scipy.stats import entropy

# ── Utility helpers ──────────────────────────────────────────────────────────
TRADING_DAYS_YEAR = 252
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5
_EPS = 1e-9


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _calculate_entropy(s: pd.Series, bins: int = 10) -> float:
    if s.isna().all(): return np.nan
    counts, _ = np.histogram(s.dropna(), bins=bins, density=True)
    return entropy(counts + _EPS)


# ── Feature functions ────────────────────────────────────────────────────────

# 076-090: Higher-Order Entropy Stats
def dpe_076_entropy_volatility_63d(close: pd.Series) -> pd.Series:
    # Std dev of daily entropy values (how unstable is the chaos?)
    ret = close.pct_change()
    e = ret.rolling(21).apply(_calculate_entropy, raw=False)
    return e.rolling(63).std()


def dpe_077_entropy_of_volatility_63d(close: pd.Series) -> pd.Series:
    # Entropy of the volatility series
    v = close.pct_change().rolling(10).std()
    return v.rolling(63).apply(_calculate_entropy, raw=False)


def dpe_078_entropy_gradient_63d(close: pd.Series) -> pd.Series:
    # Linear slope of entropy changes
    e = close.pct_change().rolling(21).apply(_calculate_entropy, raw=False)
    def _slope(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).slope
    return e.rolling(63).apply(_slope, raw=True)


# 091-105: Permutation and Sample Entropy Proxies
def dpe_091_permutation_entropy_proxy_21d(close: pd.Series) -> pd.Series:
    # Simplified: Entropy of ordinal patterns (Up/Down/Flat)
    ret = close.diff()
    patterns = np.sign(ret)
    return patterns.rolling(21).apply(_calculate_entropy, raw=False)


def dpe_092_sample_entropy_proxy_63d(close: pd.Series) -> pd.Series:
    # Complexity of return sequences (1-day vs 2-day joint entropy proxy)
    ret = close.pct_change()
    def _joint_ent(y):
        if len(y) < 2: return 0.0
        y1 = y[:-1]
        y2 = y[1:]
        hist, _, _ = np.histogram2d(y1, y2, bins=5)
        p = hist.flatten() / np.sum(hist)
        p = p[p > 0]
        return -np.sum(p * np.log(p))
    return ret.rolling(63).apply(_joint_ent, raw=True)


# 106-125: Structural Disruption (Entropy Peaks at Troughs)
def dpe_106_entropy_at_local_minima_63d(close: pd.Series) -> pd.Series:
    from scipy.signal import argrelextrema
    e = close.pct_change().rolling(21).apply(_calculate_entropy, raw=False)
    is_min = pd.Series(0, index=close.index)
    idx = argrelextrema(close.values, np.less, order=5)[0]
    is_min.iloc[idx] = 1
    return e.where(is_min == 1).ffill()


def dpe_107_entropy_to_range_efficiency_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    # Entropy / Efficiency Ratio
    e = dpe_002_return_entropy_63d(close)
    er = _safe_div((close - close.shift(63)).abs(), (high - low).rolling(63).sum())
    return _safe_div(e, er)


# 126-140: Multi-Metric Information Flow
def dpe_126_entropy_divergence_price_mktcap_63d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    pe = close.pct_change().rolling(63).apply(_calculate_entropy, raw=False)
    mce = (close * sharesbas).pct_change().rolling(63).apply(_calculate_entropy, raw=False)
    return pe - mce


def dpe_127_entropy_of_ath_drawdown_path(close: pd.Series) -> pd.Series:
    h = close.cummax()
    uw = (close - h) / h
    return uw.expanding().apply(_calculate_entropy, raw=False)


# 141-150: Final Entropy composites
def dpe_141_entropy_climax_score_21d(close: pd.Series) -> pd.Series:
    # Entropy * Volatility * (1 / Efficiency)
    e = dpe_001_return_entropy_21d(close)
    v = close.pct_change().rolling(21).std()
    er = dpe_016_efficiency_ratio_21d(close)
    return e * v * (1.0 / (er + _EPS))


def dpe_142_entropy_regime_stability_score(close: pd.Series) -> pd.Series:
    # R-squared of entropy path (high = steady chaos expansion)
    e = close.pct_change().rolling(21).apply(_calculate_entropy, raw=False)
    def _rsq(y):
        from scipy.stats import linregress
        if len(y) < 2: return 0.0
        return linregress(np.arange(len(y)), y).rvalue**2
    return e.rolling(63).apply(_rsq, raw=True)


def dpe_143_consecutive_days_with_high_entropy(close: pd.Series) -> pd.Series:
    e = dpe_001_return_entropy_21d(close)
    q90 = e.rolling(252).quantile(0.9)
    high_e = (e > q90).astype(int)
    return high_e.groupby((high_e == 0).cumsum()).cumsum()


def dpe_144_entropy_normalized_by_ath_duration(close: pd.Series) -> pd.Series:
    e = dpe_001_return_entropy_21d(close)
    cummax = close.cummax()
    is_high = (close == cummax)
    high_indices = pd.Series(np.arange(len(close)), index=close.index).where(is_high).ffill()
    dsh = pd.Series(np.arange(len(close)), index=close.index) - high_indices
    return _safe_div(e, np.log(dsh + 2)) # Log scale duration


def dpe_145_mktcap_efficiency_ratio_252d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    net_move = (mc - mc.shift(252)).abs()
    path_len = mc.diff().abs().rolling(252).sum()
    return _safe_div(net_move, path_len)


def dpe_146_entropy_of_gap_returns_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    gap_ret = (open - close.shift(1)) / close.shift(1)
    return gap_ret.rolling(63).apply(_calculate_entropy, raw=False)


def dpe_147_entropy_of_intra_returns_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    intra_ret = (close - open) / open
    return intra_ret.rolling(63).apply(_calculate_entropy, raw=False)


def dpe_148_entropy_spread_short_long_term(close: pd.Series) -> pd.Series:
    return dpe_001_return_entropy_21d(close) - dpe_003_return_entropy_252d(close)


def dpe_149_entropy_weighted_average_63d(close: pd.Series) -> pd.Series:
    e21 = dpe_001_return_entropy_21d(close)
    e63 = dpe_002_return_entropy_63d(close)
    return (0.7 * e21 + 0.3 * e63)


def dpe_150_final_chaos_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Composite: (Return Entropy + Vol Entropy) * (1 - Path Efficiency)
    re = dpe_002_return_entropy_63d(close)
    ve = volume.rolling(63).apply(_calculate_entropy, raw=False)
    er = dpe_017_efficiency_ratio_63d(close)
    return (re + ve) * (1.0 - er)


# ── Registry ──────────────────────────────────────────────────────────────────

V11_REGISTRY = {
    "dpe_076_entropy_volatility_63d": {"inputs": ["close"], "func": dpe_076_entropy_volatility_63d},
    "dpe_077_entropy_of_volatility_63d": {"inputs": ["close"], "func": dpe_077_entropy_of_volatility_63d},
    "dpe_078_entropy_gradient_63d": {"inputs": ["close"], "func": dpe_078_entropy_gradient_63d},
    "dpe_091_permutation_entropy_proxy_21d": {"inputs": ["close"], "func": dpe_091_permutation_entropy_proxy_21d},
    "dpe_092_sample_entropy_proxy_63d": {"inputs": ["close"], "func": dpe_092_sample_entropy_proxy_63d},
    "dpe_106_entropy_at_local_minima_63d": {"inputs": ["close"], "func": dpe_106_entropy_at_local_minima_63d},
    "dpe_107_entropy_to_range_efficiency_63d": {"inputs": ["close", "high", "low"], "func": dpe_107_entropy_to_range_efficiency_63d},
    "dpe_126_entropy_divergence_price_mktcap_63d": {"inputs": ["close", "sharesbas"], "func": dpe_126_entropy_divergence_price_mktcap_63d},
    "dpe_127_entropy_of_ath_drawdown_path": {"inputs": ["close"], "func": dpe_127_entropy_of_ath_drawdown_path},
    "dpe_141_entropy_climax_score_21d": {"inputs": ["close"], "func": dpe_141_entropy_climax_score_21d},
    "dpe_142_entropy_regime_stability_score": {"inputs": ["close"], "func": dpe_142_entropy_regime_stability_score},
    "dpe_143_consecutive_days_with_high_entropy": {"inputs": ["close"], "func": dpe_143_consecutive_days_with_high_entropy},
    "dpe_144_entropy_normalized_by_ath_duration": {"inputs": ["close"], "func": dpe_144_entropy_normalized_by_ath_duration},
    "dpe_145_mktcap_efficiency_ratio_252d": {"inputs": ["close", "sharesbas"], "func": dpe_145_mktcap_efficiency_ratio_252d},
    "dpe_146_entropy_of_gap_returns_63d": {"inputs": ["close", "open"], "func": dpe_146_entropy_of_gap_returns_63d},
    "dpe_147_entropy_of_intra_returns_63d": {"inputs": ["open", "close"], "func": dpe_147_entropy_of_intra_returns_63d},
    "dpe_148_entropy_spread_short_long_term": {"inputs": ["close"], "func": dpe_148_entropy_spread_short_long_term},
    "dpe_149_entropy_weighted_average_63d": {"inputs": ["close"], "func": dpe_149_entropy_weighted_average_63d},
    "dpe_150_final_chaos_index": {"inputs": ["close", "volume"], "func": dpe_150_final_chaos_index},
}
