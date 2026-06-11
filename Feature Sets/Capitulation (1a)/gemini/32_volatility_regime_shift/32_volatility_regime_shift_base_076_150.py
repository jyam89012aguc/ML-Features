"""
32_volatility_regime_shift — Base Features 076–150
Domain: transitions between low-vol and high-vol states
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

# 076-090: Statistical Regime Distribution (Ranks)
def vrs_076_vol_regime_ratio_pct_rank_ath(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = np.log(close / close.shift(1)).rolling(252).std()
    ratio = _safe_div(v21, v252)
    return ratio.expanding().rank(pct=True)


def vrs_077_vol_entropy_regime_shift_63d(close: pd.Series) -> pd.Series:
    # Entropy(21d returns) / Entropy(252d returns)
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y[~np.isnan(y)], bins=10, density=True)
        p = h / (np.sum(h) + _EPS)
        return -np.sum(p[p > 0] * np.log(p[p > 0]))
    ret = close.pct_change()
    e21 = ret.rolling(21).apply(_ent, raw=True)
    e252 = ret.rolling(252).apply(_ent, raw=True)
    return _safe_div(e21, e252)


# 091-105: Threshold-Based Regime Switches
def vrs_091_count_regime_breakouts_252d(close: pd.Series) -> pd.Series:
    # Number of times 5d vol > 2x 252d avg vol
    v5 = np.log(close / close.shift(1)).rolling(5).std()
    avg_v = np.log(close / close.shift(1)).rolling(252).std()
    return (v5 > 2 * avg_v).astype(int).rolling(252).sum()


def vrs_092_days_since_vol_regime_peak_ath(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = v21.rolling(252).mean()
    ratio = _safe_div(v21, v252)
    idx = ratio.expanding().apply(np.argmax, raw=True)
    return pd.Series(np.arange(len(close)), index=close.index) - idx


# 106-125: specialized character change metrics
def vrs_106_vol_velocity_regime_spread(close: pd.Series) -> pd.Series:
    # Vol Velocity(21d) - Vol Velocity(252d)
    v = np.log(close / close.shift(1)).rolling(5).std()
    vv21 = v.diff(21)
    vv252 = v.diff(252)
    return vv21 - vv252


def vrs_107_turnover_regime_shift_zscore_252d(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    tr = _safe_div(to.rolling(21).mean(), to.rolling(252).median())
    return (tr - tr.rolling(252).mean()) / (tr.rolling(252).std() + _EPS)


# 126-140: Multi- Horizon Resistance Regimes
def vrs_126_vol_clustering_regime_velocity_63d(close: pd.Series) -> pd.Series:
    ret = close.pct_change().abs()
    ac = ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    return ac.diff(63)


def vrs_127_range_expansion_regime_index_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    r = (high - low) / close
    r21 = r.rolling(21).mean()
    r252 = r.rolling(252).mean()
    return _safe_div(r21, r252)


# 141-150: Final Regime Shift composites
def vrs_141_volatility_breakaway_energy_score(close: pd.Series) -> pd.Series:
    # (Vol Ratio)^2 * (Vol Acceleration)
    vr = vrs_001_vol_regime_ratio_21_252(close).abs()
    v = np.log(close / close.shift(1)).rolling(21).std()
    va = v.diff(5).diff(5).abs()
    return (vr**2) * va


def vrs_142_mktcap_regime_energy_index_63d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v21 = np.log(mc / mc.shift(1)).rolling(21).std()
    v252 = np.log(mc / mc.shift(1)).rolling(252).std()
    return _safe_div(v21, v252) * v21.diff(21)


def vrs_143_consecutive_days_vol_regime_expanding(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = v21.rolling(252).mean()
    ratio = _safe_div(v21, v252)
    inc = (ratio > ratio.shift(1)) & (ratio > 1.0)
    return inc.astype(int).groupby((inc == 0).cumsum()).cumsum()


def vrs_144_regime_reversal_climax_score_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    # (Regime Ratio Change) * (Close from Low)
    vr = _safe_div(np.log(close / close.shift(1)).rolling(21).std(), np.log(close / close.shift(1)).rolling(252).std())
    return vr.diff(5) * _safe_div(close, low)


def vrs_145_sustained_high_vol_regime_index_252d(close: pd.Series) -> pd.Series:
    # Fraction of year where 21d vol > 1.5x 252d mean
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252_avg = v21.rolling(252).mean()
    return (v21 > 1.5 * v252_avg).rolling(252).mean()


def vrs_146_years_since_max_regime_ratio_ath(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = v21.rolling(252).mean()
    ratio = _safe_div(v21, v252)
    idx = ratio.expanding().apply(np.argmax, raw=True)
    return (pd.Series(np.arange(len(close)), index=close.index) - idx) / 252.0


def vrs_147_vol_regime_skew_divergence_63d(close: pd.Series) -> pd.Series:
    # Skew(Vol Ratio 21d) - Skew(Vol Ratio 252d)
    v21 = np.log(close / close.shift(1)).rolling(5).std()
    v252 = v21.rolling(252).mean()
    ratio = _safe_div(v21, v252)
    return ratio.rolling(63).skew() - ratio.rolling(252).skew()


def vrs_148_ratio_of_regime_peaks_to_troughs_252d(close: pd.Series) -> pd.Series:
    from scipy.signal import argrelextrema
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = v21.rolling(252).mean()
    ratio = _safe_div(v21, v252)
    p = argrelextrema(ratio.values, np.greater, order=5)[0]
    t = argrelextrema(ratio.values, np.less, order=5)[0]
    is_p = pd.Series(0, index=close.index); is_p.iloc[p] = 1
    is_t = pd.Series(0, index=close.index); is_t.iloc[t] = 1
    return _safe_div(is_p.rolling(252).sum(), is_t.rolling(252).sum())


def vrs_149_cumulative_regime_energy_ath(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = v21.rolling(252).mean()
    ratio = _safe_div(v21, v252)
    return ratio.cumsum() / (ratio.abs().cumsum() + _EPS)


def vrs_150_vol_regime_final_exhaustion_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Composite: (Regime Ratio) * (1 - Recovery Fraction) * Volume Persistence
    vr = _safe_div(np.log(close / close.shift(1)).rolling(21).std(), np.log(close / close.shift(1)).rolling(252).std())
    h = close.rolling(252).max()
    l = close.rolling(252).min()
    rf = _safe_div(close - l, h - l)
    vp = _safe_div(volume.rolling(21).mean(), volume.rolling(252).median())
    return vr * (1.0 - rf) * vp


# ── Registry ──────────────────────────────────────────────────────────────────

V32_REGISTRY = {
    "vrs_076_vol_regime_ratio_pct_rank_ath": {"inputs": ["close"], "func": vrs_076_vol_regime_ratio_pct_rank_ath},
    "vrs_077_vol_entropy_regime_shift_63d": {"inputs": ["close"], "func": vrs_077_vol_entropy_regime_shift_63d},
    "vrs_091_count_regime_breakouts_252d": {"inputs": ["close"], "func": vrs_091_count_regime_breakouts_252d},
    "vrs_092_days_since_vol_regime_peak": {"inputs": ["close"], "func": vrs_092_days_since_vol_regime_peak_ath},
    "vrs_106_vol_velocity_regime_spread": {"inputs": ["close"], "func": vrs_106_vol_velocity_regime_spread},
    "vrs_107_turnover_regime_shift_zscore": {"inputs": ["volume", "sharesbas"], "func": vrs_107_turnover_regime_shift_zscore_252d},
    "vrs_126_vol_cluster_regime_velocity": {"inputs": ["close"], "func": vrs_126_vol_clustering_regime_velocity_63d},
    "vrs_127_range_expansion_regime_index": {"inputs": ["high", "low", "close"], "func": vrs_127_range_expansion_regime_index_63d},
    "vrs_141_vol_breakaway_energy_score": {"inputs": ["close"], "func": vrs_141_volatility_breakaway_energy_score},
    "vrs_142_mktcap_regime_energy_index": {"inputs": ["close", "sharesbas"], "func": vrs_142_mktcap_regime_energy_index_63d},
    "vrs_143_consecutive_regime_expanding_days": {"inputs": ["close"], "func": vrs_143_consecutive_days_vol_regime_expanding},
    "vrs_144_regime_reversal_climax_score": {"inputs": ["close", "low"], "func": vrs_144_regime_reversal_climax_score_63d},
    "vrs_145_sustained_hi_vol_regime_index": {"inputs": ["close"], "func": vrs_145_sustained_high_vol_regime_index_252d},
    "vrs_146_years_since_max_regime_ratio": {"inputs": ["close"], "func": vrs_146_years_since_max_regime_ratio_ath},
    "vrs_147_vol_regime_skew_div_63d": {"inputs": ["close"], "func": vrs_147_vol_regime_skew_divergence_63d},
    "vrs_148_ratio_regime_peaks_troughs": {"inputs": ["close"], "func": vrs_148_ratio_of_regime_peaks_to_troughs_252d},
    "vrs_149_cumulative_regime_energy_ath": {"inputs": ["close"], "func": vrs_149_cumulative_regime_energy_ath},
    "vrs_150_vol_regime_final_exhaustion": {"inputs": ["close", "volume"], "func": vrs_150_vol_regime_final_exhaustion_index},
}
