"""
27_volatility_skewness — Base Features 076–150
Domain: asymmetry of return distribution, panic tail
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

# 076-090: Higher-Order Asymmetry (L-Skewness and Pearsons)
def vsk_076_pearson_skewness_21d(close: pd.Series) -> pd.Series:
    # 3 * (Mean - Median) / Std
    ret = close.pct_change()
    return 3 * _safe_div(ret.rolling(21).mean() - ret.rolling(21).median(), ret.rolling(21).std())


def vsk_077_med_abs_dev_skewness_63d(close: pd.Series) -> pd.Series:
    # (Mean - Median) / MAD
    ret = close.pct_change()
    def _mad(y): return np.median(np.abs(y - np.median(y)))
    mad = ret.rolling(63).apply(_mad, raw=True)
    return _safe_div(ret.rolling(63).mean() - ret.rolling(63).median(), mad)


def vsk_078_skewness_oscillator_21_252(close: pd.Series) -> pd.Series:
    sk21 = close.pct_change().rolling(21).skew()
    sk252 = close.pct_change().rolling(252).skew()
    return sk21 - sk252


# 091-105: Climax Tail Signatures (Tail-Risk focus)
def vsk_091_tail_risk_expansion_index_63d(close: pd.Series) -> pd.Series:
    # Ratio of current 21d skew to the average skew of the last year
    sk21 = close.pct_change().rolling(21).skew()
    return _safe_div(sk21, sk21.rolling(252).mean().abs())


def vsk_092_count_extreme_skew_days_252d(close: pd.Series) -> pd.Series:
    # Days where daily skew < -2x history
    sk = close.pct_change().rolling(21).skew()
    threshold = sk.rolling(252).mean() - 2 * sk.rolling(252).std()
    return (sk < threshold).rolling(252).sum()


# 106-125: Specialized Flow Skews (Volume-Return interaction)
def vsk_106_downside_volume_weighted_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    v_rat = _safe_div(volume, volume.rolling(252).median())
    # Weighted returns (emphasizing down days)
    weighted_ret = ret.where(ret < 0, 0) * v_rat
    return weighted_ret.rolling(63).skew()


def vsk_107_turnover_skew_ath(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    return to.expanding().skew()


# 126-140: Multi-Horizon Risk Imbalance
def vsk_126_skew_to_kurtosis_ratio_63d(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    sk = ret.rolling(63).skew()
    kt = ret.rolling(63).kurt()
    return _safe_div(sk, kt + _EPS)


def vsk_127_skew_volatility_spread_21d(close: pd.Series) -> pd.Series:
    # Skewness - Realized Vol (standardized)
    sk = close.pct_change().rolling(21).skew()
    vol = close.pct_change().rolling(21).std() * np.sqrt(252)
    v_norm = (vol - vol.rolling(252).mean()) / (vol.rolling(252).std() + _EPS)
    return sk - v_norm


# 141-150: Final Skewness composites
def vsk_141_panic_climax_velocity_score_21d(close: pd.Series) -> pd.Series:
    # (Negative Skew ROC) * (Drawdown Velocity)
    sk = close.pct_change().rolling(21).skew()
    v_sk = sk.diff(5)
    dv = np.log(close).diff(5).abs()
    return v_sk.clip(upper=0).abs() * dv


def vsk_142_mktcap_skew_energy_index_63d(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    ret = mc.pct_change()
    sk = ret.rolling(63).skew()
    vol = ret.rolling(63).std()
    return (sk**2) * vol


def vsk_143_consecutive_days_with_expanding_neg_skew(close: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(21).skew()
    inc = (sk < sk.shift(1)) & (sk < 0)
    return inc.astype(int).groupby((inc == 0).cumsum()).cumsum()


def vsk_144_skew_reversal_climax_score_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(21).skew()
    v_sk = sk.diff(5)
    c_low = _safe_div(close, low)
    return v_sk * c_low


def vsk_145_sustained_asymmetry_index_252d(close: pd.Series) -> pd.Series:
    # Fraction of year with 21d skew in lowest quartile
    sk = close.pct_change().rolling(21).skew()
    q25 = sk.rolling(252).quantile(0.25)
    return (sk < q25).rolling(252).mean()


def vsk_146_years_since_max_negative_skew_ath(close: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(63).skew()
    idx = sk.expanding().apply(np.argmin, raw=True)
    return (pd.Series(np.arange(len(close)), index=close.index) - idx) / 252.0


def vsk_147_skew_regime_break_63d(close: pd.Series) -> pd.Series:
    # Skew(21d) - Skew(126d)
    ret = close.pct_change()
    return ret.rolling(21).skew() - ret.rolling(126).skew()


def vsk_148_ratio_of_negative_skews_to_peaks_252d(close: pd.Series) -> pd.Series:
    # Frequency of being < -1.0 skew vs Frequency of being > 1.0 skew
    sk = close.pct_change().rolling(21).skew()
    neg = (sk < -1.0).rolling(252).sum()
    pos = (sk > 1.0).rolling(252).sum()
    return _safe_div(neg, pos)


def vsk_149_cumulative_skew_energy_ath(close: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(21).skew()
    return sk.cumsum() / (sk.abs().cumsum() + _EPS)


def vsk_150_vol_skew_final_fear_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Composite: (1 - Skewness) * (Volume Spike) * (Drawdown Depth)
    sk = close.pct_change().rolling(21).skew()
    vs = _safe_div(volume, volume.rolling(252).median())
    dd = (close.rolling(252).max() - close) / close.rolling(252).max()
    return (1.0 - sk.clip(-1,1)) * vs * dd


# ── Registry ──────────────────────────────────────────────────────────────────

V27_REGISTRY = {
    "vsk_076_pearson_skewness_21d": {"inputs": ["close"], "func": vsk_076_pearson_skewness_21d},
    "vsk_077_med_abs_dev_skewness_63d": {"inputs": ["close"], "func": vsk_077_med_abs_dev_skewness_63d},
    "vsk_078_skewness_oscillator_21_252": {"inputs": ["close"], "func": vsk_078_skewness_oscillator_21_252},
    "vsk_091_tail_risk_expansion_index_63d": {"inputs": ["close"], "func": vsk_091_tail_risk_expansion_index_63d},
    "vsk_092_count_extreme_skew_days_252d": {"inputs": ["close"], "func": vsk_092_count_extreme_skew_days_252d},
    "vsk_106_dv_weighted_skew_63d": {"inputs": ["close", "volume"], "func": vsk_106_downside_volume_weighted_skew_63d},
    "vsk_107_turnover_skew_ath": {"inputs": ["volume", "sharesbas"], "func": vsk_107_turnover_skew_ath},
    "vsk_126_skew_to_kurtosis_ratio_63d": {"inputs": ["close"], "func": vsk_126_skew_to_kurtosis_ratio_63d},
    "vsk_127_skew_volatility_spread_21d": {"inputs": ["close"], "func": vsk_127_skew_volatility_spread_21d},
    "vsk_141_panic_climax_velocity_score": {"inputs": ["close"], "func": vsk_141_panic_climax_velocity_score_21d},
    "vsk_142_mktcap_skew_energy_index_63d": {"inputs": ["close", "sharesbas"], "func": vsk_142_mktcap_skew_energy_index_63d},
    "vsk_143_consecutive_neg_skew_expansion": {"inputs": ["close"], "func": vsk_143_consecutive_days_with_expanding_neg_skew},
    "vsk_144_skew_reversal_climax_score": {"inputs": ["close", "low"], "func": vsk_144_skew_reversal_climax_score_63d},
    "vsk_145_sustained_asymmetry_index_252d": {"inputs": ["close"], "func": vsk_145_sustained_asymmetry_index_252d},
    "vsk_146_years_since_max_neg_skew_ath": {"inputs": ["close"], "func": vsk_146_years_since_max_negative_skew_ath},
    "vsk_147_skew_regime_break_63d": {"inputs": ["close"], "func": vsk_147_skew_regime_break_63d},
    "vsk_148_ratio_neg_skews_to_peaks": {"inputs": ["close"], "func": vsk_148_ratio_of_negative_skews_to_peaks_252d},
    "vsk_149_cumulative_skew_energy_ath": {"inputs": ["close"], "func": vsk_149_cumulative_skew_energy_ath},
    "vsk_150_vol_skew_final_fear_index": {"inputs": ["close", "volume"], "func": vsk_150_vol_skew_final_fear_index},
}
