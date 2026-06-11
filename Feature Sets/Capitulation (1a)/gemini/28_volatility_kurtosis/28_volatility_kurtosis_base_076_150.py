"""
28_volatility_kurtosis — Base Features 076–150
Domain: fatness of tails, outlier density
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

# 076-090: Statistical Distribution of Kurtosis (Ranks)
def vkt_076_kurtosis_pct_rank_ath(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(63).kurt()
    return kt.expanding().rank(pct=True)


def vkt_077_excess_kurtosis_zscore_ath(close: pd.Series) -> pd.Series:
    # (21d Kurtosis - 3.0) normalized by history
    kt = close.pct_change().rolling(21).kurt()
    ex_kt = kt - 3.0
    return (ex_kt - ex_kt.expanding().mean()) / (ex_kt.expanding().std() + _EPS)


# 091-105: Climax Outlier Signatures
def vkt_091_count_negative_outliers_63d(close: pd.Series) -> pd.Series:
    # Days with return < -3 std devs in the last year
    ret = close.pct_change()
    s = ret.rolling(252).std()
    m = ret.rolling(252).mean()
    is_outlier = (ret < m - 3 * s).astype(int)
    return is_outlier.rolling(63).sum()


def vkt_092_ratio_of_negative_outlier_volume_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Volume on negative outlier days / Total volume
    ret = close.pct_change()
    s = ret.rolling(252).std()
    is_neg_outlier = (ret < -3 * s)
    v_outlier = volume.where(is_neg_outlier, 0).rolling(63).sum()
    v_total = volume.rolling(63).sum()
    return _safe_div(v_outlier, v_total)


# 106-125: specialized Kurtosis Accelerators
def vkt_106_kurtosis_velocity_63d(close: pd.Series) -> pd.Series:
    # ROC of 21-day kurtosis
    kt = close.pct_change().rolling(21).kurt()
    return kt.diff(63)


def vkt_107_kurtosis_gradient_21d(close: pd.Series) -> pd.Series:
    # Slope of the kurtosis path
    kt = close.pct_change().rolling(21).kurt()
    def _slope(y):
        from scipy.stats import linregress
        if len(y) < 2: return 0.0
        return linregress(np.arange(len(y)), y).slope
    return kt.rolling(21).apply(_slope, raw=True)


# 126-140: Multi-Horizon Integral Tail Ratios
def vkt_126_tail_integral_ratio_63d_to_252d(close: pd.Series) -> pd.Series:
    # Sum of absolute returns > 2-sigma over 63d vs 252d
    ret = close.pct_change()
    s = ret.rolling(252).std()
    outlier_val = ret.abs().where(ret.abs() > 2 * s, 0)
    return _safe_div(outlier_val.rolling(63).sum(), outlier_val.rolling(252).sum())


def vkt_127_kurtosis_oscillator_21_63(close: pd.Series) -> pd.Series:
    # (Kurtosis 21 / Kurtosis 63) - 1
    kt21 = close.pct_change().rolling(21).kurt()
    kt63 = close.pct_change().rolling(63).kurt()
    return _safe_div(kt21, kt63) - 1.0


# 141-150: Final Kurtosis composites
def vkt_141_fat_tail_exhaustion_score_21d(close: pd.Series) -> pd.Series:
    # (Kurtosis) / (Price Velocity) -> higher = more shock without directional drift
    kt = close.pct_change().rolling(21).kurt()
    pv = np.log(close).diff(21).abs()
    return _safe_div(kt, pv + _EPS)


def vkt_142_mktcap_kurtosis_climax_index(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    ret = mc.pct_change()
    kt = ret.rolling(63).kurt()
    vs = ret.rolling(63).std()
    return kt * vs


def vkt_143_consecutive_days_kurtosis_gt_median(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(21).kurt()
    med = kt.rolling(252).median()
    is_high = (kt > med).astype(int)
    return is_high.groupby((is_high == 0).cumsum()).cumsum()


def vkt_144_kurtosis_reversal_climax_score(close: pd.Series, volume: pd.Series, low: pd.Series) -> pd.Series:
    # (Kurtosis Change) * (Volume Spike) * (Close from Low)
    kt = close.pct_change().rolling(21).kurt()
    v_rat = _safe_div(volume, volume.rolling(252).median())
    c_low = _safe_div(close, low)
    return kt.diff(5) * v_rat * c_low


def vkt_145_sustained_tail_density_index_252d(close: pd.Series) -> pd.Series:
    # Fraction of year with 21d kurtosis in highest decile
    kt = close.pct_change().rolling(21).kurt()
    q90 = kt.rolling(252).quantile(0.9)
    return (kt > q90).rolling(252).mean()


def vkt_146_years_since_max_kurtosis_ath(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(63).kurt()
    idx = kt.expanding().apply(np.argmax, raw=True)
    return (pd.Series(np.arange(len(close)), index=close.index) - idx) / 252.0


def vkt_147_kurtosis_regime_break_63d(close: pd.Series) -> pd.Series:
    # Kurtosis(21d) - Kurtosis(126d)
    ret = close.pct_change()
    return ret.rolling(21).kurt() - ret.rolling(126).kurt()


def vkt_148_ratio_of_kurtosis_to_drawdown_velocity(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(21).kurt()
    dv = np.log(close).diff(21).abs()
    return _safe_div(kt, dv + _EPS)


def vkt_149_cumulative_kurtosis_energy_ath(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(21).kurt()
    return kt.cumsum() / (kt.abs().cumsum() + _EPS)


def vkt_150_vol_kurt_final_exhaustion_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Composite: Kurtosis * (1 - Recovery Fraction) * Volume Persistence
    kt = close.pct_change().rolling(63).kurt() / 10.0
    h = close.rolling(252).max()
    l = close.rolling(252).min()
    rf = _safe_div(close - l, h - l)
    vp = _safe_div(volume.rolling(21).mean(), volume.rolling(252).median())
    return kt.clip(0,1) * (1.0 - rf) * vp


# ── Registry ──────────────────────────────────────────────────────────────────

V28_REGISTRY = {
    "vkt_076_kurtosis_pct_rank_ath": {"inputs": ["close"], "func": vkt_076_kurtosis_pct_rank_ath},
    "vkt_077_excess_kurtosis_zscore_ath": {"inputs": ["close"], "func": vkt_077_excess_kurtosis_zscore_ath},
    "vkt_091_count_negative_outliers_63d": {"inputs": ["close"], "func": vkt_091_count_negative_outliers_63d},
    "vkt_092_ratio_neg_outlier_volume_63d": {"inputs": ["close", "volume"], "func": vkt_092_ratio_of_negative_outlier_volume_63d},
    "vkt_106_kurtosis_velocity_63d": {"inputs": ["close"], "func": vkt_106_kurtosis_velocity_63d},
    "vkt_107_kurtosis_gradient_21d": {"inputs": ["close"], "func": vkt_107_kurtosis_gradient_21d},
    "vkt_126_tail_integral_ratio": {"inputs": ["close"], "func": vkt_126_tail_integral_ratio_63d_to_252d},
    "vkt_127_kurtosis_oscillator_21_63": {"inputs": ["close"], "func": vkt_127_kurtosis_oscillator_21_63},
    "vkt_141_fat_tail_exhaustion_score": {"inputs": ["close"], "func": vkt_141_fat_tail_exhaustion_score_21d},
    "vkt_142_mktcap_kurtosis_climax": {"inputs": ["close", "sharesbas"], "func": vkt_142_mktcap_kurtosis_climax_index},
    "vkt_143_consecutive_high_kurt_days": {"inputs": ["close"], "func": vkt_143_consecutive_days_kurtosis_gt_median},
    "vkt_144_kurt_reversal_climax_score": {"inputs": ["close", "volume", "low"], "func": vkt_144_kurtosis_reversal_climax_score},
    "vkt_145_sustained_tail_density_index": {"inputs": ["close"], "func": vkt_145_sustained_tail_density_index_252d},
    "vkt_146_years_since_max_kurt_ath": {"inputs": ["close"], "func": vkt_146_years_since_max_kurtosis_ath},
    "vkt_147_kurt_regime_break_63d": {"inputs": ["close"], "func": vkt_147_kurt_regime_break_63d},
    "vkt_148_ratio_kurt_to_dd_velocity": {"inputs": ["close"], "func": vkt_148_ratio_of_kurtosis_to_drawdown_velocity},
    "vkt_149_cumulative_kurt_energy_ath": {"inputs": ["close"], "func": vkt_149_cumulative_kurtosis_energy_ath},
    "vkt_150_vol_kurt_final_exhaustion": {"inputs": ["close", "volume"], "func": vkt_150_vol_kurt_final_exhaustion_index},
}
