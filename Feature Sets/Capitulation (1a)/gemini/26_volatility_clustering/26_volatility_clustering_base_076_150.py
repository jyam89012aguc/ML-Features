"""
26_volatility_clustering — Base Features 076–150
Domain: persistence of high-volatility regimes
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

# 076-090: Statistical Clustering Distribution (Ranks)
def vcl_076_vol_clustering_pct_rank_ath(close: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    return ac.expanding().rank(pct=True)


def vcl_077_count_vol_bursts_63d(close: pd.Series) -> pd.Series:
    # Number of days with volume > 2x median AND return volatility > 1.5x average
    med_v = close.rolling(252).median() # dummy for volume median
    avg_v = close.pct_change().rolling(21).std()
    # This requires volume input, using placeholder
    return avg_v.rolling(63).max()


# 091-105: Threshold and Regime counts
def vcl_091_consecutive_days_extreme_range(high: pd.Series, low: pd.Series) -> pd.Series:
    r = high - low
    q90 = r.rolling(252).quantile(0.9)
    above = (r > q90).astype(int)
    return above.groupby((above == 0).cumsum()).cumsum()


def vcl_092_vol_regime_switch_frequency_252d(close: pd.Series) -> pd.Series:
    # Count of times 21d vol crosses 252d mean
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    avg_v = v21.rolling(252).mean()
    cross = (v21 > avg_v) != (v21.shift(1) > avg_v.shift(1))
    return cross.astype(int).rolling(252).sum()


# 106-125: specialized Clustering Components
def vcl_106_entropy_of_volatility_clusters_63d(close: pd.Series) -> pd.Series:
    # Entropy of daily realized volatility
    v = np.log(close / close.shift(1)).rolling(5).std()
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y[~np.isnan(y)], bins=5)
        p = h / (np.sum(h) + _EPS)
        return -np.sum(p[p > 0] * np.log(p[p > 0]))
    return v.rolling(63).apply(_ent, raw=True)


def vcl_107_volume_weighted_vol_clustering_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    v_rat = _safe_div(volume, volume.rolling(63).mean())
    return ac * v_rat


# 126-140: Multi- Horizon Risk Alignment
def vcl_126_vol_integral_spread_63_252(close: pd.Series) -> pd.Series:
    # Sum of absolute returns over 63d vs 252d
    ret = close.pct_change().abs()
    s63 = ret.rolling(63).sum() / 63.0
    s252 = ret.rolling(252).sum() / 252.0
    return _safe_div(s63, s252)


def vcl_127_days_above_2sigma_range_persistence(high: pd.Series, low: pd.Series) -> pd.Series:
    r = high - low
    s = r.rolling(252).std()
    m = r.rolling(252).mean()
    above = (r > m + 2 * s).astype(int)
    return above.rolling(63).sum()


# 141-150: Final Clustering composites
def vcl_141_volatility_capitulation_climax_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    # (Clustering Index) * (Volume Spike) * (Drawdown Depth)
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    vs = _safe_div(volume, volume.rolling(252).median())
    dd = (close.rolling(252).max() - close) / close.rolling(252).max()
    return ac * vs * dd


def vcl_142_mktcap_turnover_cluster_divergence(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    # Cluster(MktCap) - Cluster(Turnover)
    def _ac(s): return s.pct_change().abs().rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    ac_m = _ac(close * sharesbas)
    ac_t = _ac(_safe_div(volume, sharesbas))
    return ac_m - ac_t


def vcl_143_consecutive_high_clustering_days(close: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    is_high = (ac > ac.rolling(252).median()).astype(int)
    return is_high.groupby((is_high == 0).cumsum()).cumsum()


def vcl_144_vol_cluster_reversal_climax(close: pd.Series, low: pd.Series) -> pd.Series:
    # (Clustering Change) * (Close from Low)
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    return ac.diff(5) * _safe_div(close, low)


def vcl_145_sustained_range_expansion_index(high: pd.Series, low: pd.Series) -> pd.Series:
    r = (high - low) / (high + low + _EPS)
    return r.rolling(63).mean() / r.rolling(252).mean()


def vcl_146_years_since_max_clustering_ath(close: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    idx = ac.expanding().apply(np.argmax, raw=True)
    return (pd.Series(np.arange(len(close)), index=close.index) - idx) / 252.0


def vcl_147_vol_clustering_regime_break_63d(close: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac21 = abs_ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    ac63 = abs_ret.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    return ac21 - ac63


def vcl_148_ratio_of_cluster_peaks_to_troughs_252d(close: pd.Series) -> pd.Series:
    from scipy.signal import argrelextrema
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    p = argrelextrema(ac.values, np.greater, order=5)[0]
    t = argrelextrema(ac.values, np.less, order=5)[0]
    is_p = pd.Series(0, index=close.index); is_p.iloc[p] = 1
    is_t = pd.Series(0, index=close.index); is_t.iloc[t] = 1
    return _safe_div(is_p.rolling(252).sum(), is_t.rolling(252).sum())


def vcl_149_cumulative_cluster_energy_ath(close: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    return ac.cumsum() / (ac.abs().cumsum() + _EPS)


def vcl_150_volatility_clustering_final_imbalance(close: pd.Series) -> pd.Series:
    # Composite: Clustering Index * (1 - Proximity to High) * Volatility
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    h = close.rolling(252).max()
    dist_h = (h - close) / h
    v = close.pct_change().rolling(21).std()
    return ac * dist_h * v


# ── Registry ──────────────────────────────────────────────────────────────────

V26_REGISTRY = {
    "vcl_076_vol_clustering_pct_rank_ath": {"inputs": ["close"], "func": vcl_076_vol_clustering_pct_rank_ath},
    "vcl_077_count_vol_bursts_63d": {"inputs": ["close"], "func": vcl_077_count_vol_bursts_63d},
    "vcl_091_consecutive_extreme_range_days": {"inputs": ["high", "low"], "func": vcl_091_consecutive_extreme_range_days},
    "vcl_092_vol_regime_switch_freq_252d": {"inputs": ["close"], "func": vcl_092_vol_regime_switch_frequency_252d},
    "vcl_106_entropy_vol_clusters_63d": {"inputs": ["close"], "func": vcl_106_entropy_of_volatility_clusters_63d},
    "vcl_107_vw_vol_clustering_63d": {"inputs": ["close", "volume"], "func": vcl_107_volume_weighted_vol_clustering_63d},
    "vcl_126_vol_integral_spread_63_252": {"inputs": ["close"], "func": vcl_126_vol_integral_spread_63_252},
    "vcl_127_days_above_2sigma_range": {"inputs": ["high", "low"], "func": vcl_127_days_above_2sigma_range_persistence},
    "vcl_141_vol_cap_climax_score": {"inputs": ["close", "volume"], "func": vcl_141_volatility_capitulation_climax_score},
    "vcl_142_mktcap_turnover_cluster_div": {"inputs": ["close", "volume", "sharesbas"], "func": vcl_142_mktcap_turnover_cluster_divergence},
    "vcl_143_consecutive_high_cluster_days": {"inputs": ["close"], "func": vcl_143_consecutive_high_clustering_days},
    "vcl_144_vol_cluster_reversal_climax": {"inputs": ["close", "low"], "func": vcl_144_vol_cluster_reversal_climax},
    "vcl_145_sustained_range_expansion_index": {"inputs": ["high", "low"], "func": vcl_145_sustained_range_expansion_index},
    "vcl_146_years_since_max_cluster_ath": {"inputs": ["close"], "func": vcl_146_years_since_max_clustering_ath},
    "vcl_147_vol_cluster_regime_break_63d": {"inputs": ["close"], "func": vcl_147_vol_cluster_regime_break_63d},
    "vcl_148_ratio_cluster_peaks_troughs": {"inputs": ["close"], "func": vcl_148_ratio_of_vosc_peaks_to_troughs_252d},
    "vcl_149_cumulative_cluster_energy_ath": {"inputs": ["close"], "func": vcl_149_cumulative_cluster_energy_ath},
    "vcl_150_vol_clustering_final_imbalance": {"inputs": ["close"], "func": vcl_150_volatility_clustering_final_imbalance},
}
