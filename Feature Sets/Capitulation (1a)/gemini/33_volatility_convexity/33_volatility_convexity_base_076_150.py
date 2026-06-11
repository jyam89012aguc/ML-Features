"""
33_volatility_convexity — Base Features 076–150
Domain: curvature of the volatility path, parabolic fear
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

# 076-090: Statistical Distribution of Vol Convexity (Ranks)
def vcvx_076_vol_curvature_pct_rank_ath(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y):
        if len(y) < 3: return 0.0
        return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v21.rolling(63).apply(_poly2, raw=True).abs()
    return curv.expanding().rank(pct=True)


def vcvx_077_vol_area_ratio_zscore_252d(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    ratio = _safe_div(v.rolling(63).sum(), v.rolling(63).max() * 63)
    return (ratio - ratio.rolling(252).mean()) / (ratio.rolling(252).std() + _EPS)


# 091-105: Climax Convexity Threshold Counts
def vcvx_091_count_extreme_curvature_days_252d(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(63).apply(_poly2, raw=True).abs()
    threshold = curv.rolling(252).mean() + 2 * curv.rolling(252).std()
    return (curv > threshold).rolling(252).sum()


def vcvx_092_consecutive_days_convex_vol(close: pd.Series) -> pd.Series:
    # Days in a row where vol curvature is positive
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(21).apply(_poly2, raw=True)
    is_convex = (curv > 0).astype(int)
    return is_convex.groupby((is_convex == 0).cumsum()).cumsum()


# 106-125: specialized Vol-Path Geometry accelerators
def vcvx_106_vol_curvature_velocity_21d(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(63).apply(_poly2, raw=True)
    return curv.diff(21)


def vcvx_107_vol_area_drift_63d(close: pd.Series) -> pd.Series:
    # Slope of the volatility area ratio
    v = np.log(close / close.shift(1)).rolling(21).std()
    ratio = _safe_div(v.rolling(21).sum(), v.rolling(21).max() * 21)
    def _slope(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).slope
    return ratio.rolling(63).apply(_slope, raw=True)


# 126-140: Multi-Horizon Integral Geometry
def vcvx_126_vol_area_ratio_spread_21_252(close: pd.Series) -> pd.Series:
    def _ar(w):
        v = np.log(close / close.shift(1)).rolling(5).std()
        return _safe_div(v.rolling(w).sum(), v.rolling(w).max() * w)
    return _ar(21) - _ar(252)


def vcvx_127_vol_curvature_to_accel_divergence(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(63).apply(_poly2, raw=True).abs()
    accel = v.diff(21).diff(21).abs()
    return curv - accel


# 141-150: Final Convexity composites
def vcvx_141_vol_parabolic_blowoff_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    # (Curvature) * (Volume Spike) / (Efficiency)
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(63).apply(_poly2, raw=True).abs()
    vs = _safe_div(volume, volume.rolling(252).median())
    net_m = (close / close.shift(21) - 1).abs()
    path = close.diff().abs().rolling(21).sum()
    eff = _safe_div(net_m, path)
    return (curv * vs) / (eff + _EPS)


def vcvx_142_mktcap_vol_convexity_index_63d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v = np.log(mc / mc.shift(1)).rolling(21).std()
    area = v.rolling(63).sum()
    max_v = v.rolling(63).max()
    return _safe_div(area, max_v * 63)


def vcvx_143_consecutive_days_increasing_vol_curv(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(63).apply(_poly2, raw=True).abs()
    inc = (curv > curv.shift(1)).astype(int)
    return inc.groupby((inc == 0).cumsum()).cumsum()


def vcvx_144_vol_curvature_reversal_climax(close: pd.Series, low: pd.Series) -> pd.Series:
    # (Curvature Change) * (Close from Low)
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(63).apply(_poly2, raw=True).abs()
    return curv.diff(5) * _safe_div(close, low)


def vcvx_145_sustained_convex_vol_regime_index(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(63).apply(_poly2, raw=True)
    return (curv > 0).rolling(252).mean()


def vcvx_146_years_since_max_curvature_ath(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(63).apply(_poly2, raw=True).abs()
    idx = curv.expanding().apply(np.argmax, raw=True)
    return (pd.Series(np.arange(len(close)), index=close.index) - idx) / 252.0


def vcvx_147_vol_area_ratio_regime_break_63d(close: pd.Series) -> pd.Series:
    def _ar(w):
        v = np.log(close / close.shift(1)).rolling(5).std()
        return _safe_div(v.rolling(w).sum(), v.rolling(w).max() * w)
    return _ar(21) - _ar(126)


def vcvx_148_ratio_of_curv_peaks_to_troughs_252d(close: pd.Series) -> pd.Series:
    from scipy.signal import argrelextrema
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(63).apply(_poly2, raw=True).abs()
    p = argrelextrema(curv.values, np.greater, order=5)[0]
    t = argrelextrema(curv.values, np.less, order=5)[0]
    is_p = pd.Series(0, index=close.index); is_p.iloc[p] = 1
    is_t = pd.Series(0, index=close.index); is_t.iloc[t] = 1
    return _safe_div(is_p.rolling(252).sum(), is_t.rolling(252).sum())


def vcvx_149_cumulative_curv_energy_ath(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(63).apply(_poly2, raw=True).abs()
    return curv.cumsum() / (curv.abs().cumsum() + _EPS)


def vcvx_150_vol_convexity_final_exhaustion(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Composite: Curvature * (1 - Recovery Fraction) * Volume Persistence
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(63).apply(_poly2, raw=True).abs()
    l = close.rolling(252).min()
    h = close.rolling(252).max()
    rf = _safe_div(close - l, h - l)
    vp = _safe_div(volume.rolling(21).mean(), volume.rolling(252).median())
    return curv * (1.0 - rf) * vp


# ── Registry ──────────────────────────────────────────────────────────────────

V33_REGISTRY = {
    "vcvx_076_vol_curvature_pct_rank_ath": {"inputs": ["close"], "func": vcvx_076_vol_curvature_pct_rank_ath},
    "vcvx_077_vol_area_ratio_zscore_252d": {"inputs": ["close"], "func": vcvx_077_vol_area_ratio_zscore_252d},
    "vcvx_091_count_extreme_curvature_days": {"inputs": ["close"], "func": vcvx_091_count_extreme_curvature_days_252d},
    "vcvx_092_consecutive_convex_vol_days": {"inputs": ["close"], "func": vcvx_092_consecutive_days_convex_vol},
    "vcvx_106_vol_curvature_velocity_21d": {"inputs": ["close"], "func": vcvx_106_vol_curvature_velocity_21d},
    "vcvx_107_vol_area_drift_63d": {"inputs": ["close"], "func": vcvx_107_vol_area_drift_63d},
    "vcvx_126_vol_area_ratio_spread_21_252": {"inputs": ["close"], "func": vcvx_126_vol_area_ratio_spread_21_252},
    "vcvx_127_vol_curv_to_accel_div": {"inputs": ["close"], "func": vcvx_127_vol_curvature_to_accel_divergence},
    "vcvx_141_vol_parabolic_blowoff_score": {"inputs": ["close", "volume"], "func": vcvx_141_vol_parabolic_blowoff_score},
    "vcvx_142_mktcap_vol_conv_index": {"inputs": ["close", "sharesbas"], "func": vcvx_142_mktcap_vol_convexity_index_63d},
    "vcvx_143_consecutive_inc_vol_curv": {"inputs": ["close"], "func": vcvx_143_consecutive_days_increasing_vol_curv},
    "vcvx_144_vol_curv_reversal_climax": {"inputs": ["close", "low"], "func": vcvx_144_vol_curvature_reversal_climax},
    "vcvx_145_sustained_convex_regime": {"inputs": ["close"], "func": vcvx_145_sustained_convex_vol_regime_index},
    "vcvx_146_years_since_max_curvature": {"inputs": ["close"], "func": vcvx_146_years_since_max_curvature_ath},
    "vcvx_147_vol_area_regime_break_63d": {"inputs": ["close"], "func": vcvx_147_vol_area_ratio_regime_break_63d},
    "vcvx_148_ratio_curv_peaks_troughs": {"inputs": ["close"], "func": vcvx_148_ratio_of_curv_peaks_to_troughs_252d},
    "vcvx_149_cumulative_curv_energy_ath": {"inputs": ["close"], "func": vcvx_149_cumulative_curv_energy_ath},
    "vcvx_150_vol_conv_final_exhaustion": {"inputs": ["close", "volume"], "func": vcvx_150_vol_convexity_final_exhaustion},
}
