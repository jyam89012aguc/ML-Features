"""
22_volume_price_divergence — Base Features 076–150
Domain: volume rising while price falls
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

# 076-090: Statistical Distribution of Divergence
def vpd_076_vp_divergence_pct_rank_ath(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Rank of the 21-day VP divergence in history
    v_roc = volume.pct_change(5)
    p_roc = close.pct_change(5)
    div = (v_roc - p_roc)
    return div.expanding().rank(pct=True)


def vpd_077_absorption_ratio_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Volume spike / Price move magnitude
    ret = close.pct_change()
    v_rat = _safe_div(volume, _rolling_median(volume, 63))
    absorp = _safe_div(v_rat, ret.abs() + _EPS)
    return (absorp - absorp.rolling(252).mean()) / absorp.rolling(252).std()


# 091-105: Convergence/Divergence Inflection
def vpd_091_correlation_regime_shift_index_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Corr(21d) - Corr(252d)
    c21 = close.rolling(21).corr(volume)
    c252 = close.rolling(252).corr(volume)
    return c21 - c252


def vpd_092_days_since_peak_supply_surge_ath(close: pd.Series, volume: pd.Series) -> pd.Series:
    is_down = (close < close.shift(1))
    surge = volume.where(is_down, 0).rolling(63).mean() / _rolling_median(volume, 252)
    idx = surge.expanding().apply(np.argmax, raw=True)
    return pd.Series(np.arange(len(volume)), index=volume.index) - idx


# 106-125: Specialized Flow Ratios (Volume-Price interactions)
def vpd_106_force_price_divergence_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Force Index / Price Distance from MA
    fi = close.diff(1) * volume
    ma = close.rolling(50).mean()
    dist = (close - ma) / ma
    return _safe_div(fi.rolling(21).mean(), dist.abs() + _EPS)


def vpd_107_volume_weighted_rsi_divergence_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Standard RSI - Volume Weighted RSI
    delta = close.diff()
    gain = delta.where(delta > 0, 0).rolling(14).mean()
    loss = delta.where(delta < 0, 0).abs().rolling(14).mean()
    rsi = 100 - (100 / (1 + _safe_div(gain, loss)))
    
    v_gain = (delta.where(delta > 0, 0) * volume).rolling(14).mean()
    v_loss = (delta.where(delta < 0, 0).abs() * volume).rolling(14).mean()
    vw_rsi = 100 - (100 / (1 + _safe_div(v_gain, v_loss)))
    return rsi - vw_rsi


# 126-140: Multi-Metric Flow Imbalances
def vpd_126_obv_slope_to_price_slope_divergence(close: pd.Series, volume: pd.Series) -> pd.Series:
    from scipy.stats import linregress
    def _slope(y):
        if len(y) < 2: return 0.0
        return linregress(np.arange(len(y)), y).slope
    obv = (np.sign(close.diff()) * volume).cumsum()
    os = obv.rolling(63).apply(_slope, raw=True) / obv.abs().rolling(63).mean()
    ps = close.rolling(63).apply(_slope, raw=True) / close.rolling(63).mean()
    return os - ps


def vpd_127_turnover_to_range_divergence_ratio(volume: pd.Series, high: pd.Series, low: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    r = (high - low) / ((high + low) / 2.0)
    return _safe_div(to.rolling(21).mean(), r.rolling(21).mean())


# 141-150: Final Divergence composites
def vpd_141_demand_collapse_index_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # (Price ROC) * (1 / Up Volume)
    p_roc = close.pct_change(5).abs()
    is_up = (close > close.shift(1))
    v_up = volume.where(is_up, 0).rolling(21).mean() / _rolling_median(volume, 252)
    return _safe_div(p_roc, v_up + _EPS)


def vpd_142_mktcap_supply_surge_velocity(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    is_down = (mc < mc.shift(1))
    surge = volume.where(is_down, 0).rolling(21).mean() / _rolling_median(volume, 252)
    return surge.diff(5)


def vpd_143_consecutive_days_volume_up_price_down(close: pd.Series, volume: pd.Series) -> pd.Series:
    cond = (volume > volume.shift(1)) & (close < close.shift(1))
    return cond.astype(int).groupby((cond == 0).cumsum()).cumsum()


def vpd_144_volume_price_overlap_efficiency_63d(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    # Net Price Move / Sum(Volume * Range)
    net_p = (close - close.shift(63)).abs()
    v_range = (volume * (high - low)).rolling(63).sum()
    return _safe_div(net_p, v_range)


def vpd_145_ath_drawdown_volume_drift_divergence(close: pd.Series, volume: pd.Series) -> pd.Series:
    h = close.cummax()
    dd = (h - close) / h
    v_drift = volume.rolling(21).mean().diff(21) / volume.rolling(21).mean().shift(21)
    return v_drift - dd.diff(21)


def vpd_146_years_since_max_vp_divergence_ath(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_roc = volume.pct_change(5)
    p_roc = close.pct_change(5)
    div = (v_roc - p_roc)
    idx = div.expanding().apply(np.argmax, raw=True)
    return (pd.Series(np.arange(len(volume)), index=volume.index) - idx) / 252.0


def vpd_147_volume_climax_to_retracement_divergence(close: pd.Series, volume: pd.Series) -> pd.Series:
    # (Volume Spike) * (1 - Recovery Fraction)
    v_rat = _safe_div(volume, _rolling_median(volume, 63))
    l = close.rolling(252).min()
    h = close.rolling(252).max()
    rf = _safe_div(close - l, h - l)
    return v_rat * (1.0 - rf)


def vpd_148_ratio_of_supply_to_demand_volume_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_dn = volume.where(close < close.shift(1), 0).rolling(21).sum()
    v_up = volume.where(close > close.shift(1), 0).rolling(21).sum()
    return _safe_div(v_dn, v_up)


def vpd_149_joint_vp_entropy_divergence_zscore(close: pd.Series, volume: pd.Series) -> pd.Series:
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y[~np.isnan(y)], bins=5, density=True)
        p = h[h > 0]
        return -np.sum(p * np.log(p))
    ve = volume.rolling(63).apply(_ent, raw=True)
    re = close.pct_change().rolling(63).apply(_ent, raw=True)
    div = ve - re
    return (div - div.rolling(252).mean()) / div.rolling(252).std()


def vpd_150_volume_price_divergence_final_exhaustion(close: pd.Series, volume: pd.Series) -> pd.Series:
    # (Down Volume Share) * (Price Velocity) * (1 / Up Volume Persistence)
    v_dn_rat = _safe_div(volume.where(close < close.shift(1), 0).rolling(63).sum(), volume.rolling(63).sum())
    p_vel = np.log(close).diff(21).abs()
    up_pers = (close > close.shift(1)).rolling(63).mean()
    return (v_dn_rat * p_vel) / (up_pers + _EPS)


# ── Registry ──────────────────────────────────────────────────────────────────

V22_REGISTRY = {
    "vpd_076_vp_divergence_pct_rank_ath": {"inputs": ["close", "volume"], "func": vpd_076_vp_divergence_pct_rank_ath},
    "vpd_077_absorption_ratio_zscore_252d": {"inputs": ["close", "volume"], "func": vpd_077_absorption_ratio_zscore_252d},
    "vpd_091_correlation_regime_shift_63d": {"inputs": ["close", "volume"], "func": vpd_091_correlation_regime_shift_index_63d},
    "vpd_092_days_since_peak_supply_surge_ath": {"inputs": ["close", "volume"], "func": vpd_092_days_since_peak_supply_surge_ath},
    "vpd_106_force_price_divergence_63d": {"inputs": ["close", "volume"], "func": vpd_106_force_price_divergence_63d},
    "vpd_107_vw_rsi_divergence_21d": {"inputs": ["close", "volume"], "func": vpd_107_volume_weighted_rsi_divergence_21d},
    "vpd_126_obv_price_slope_divergence": {"inputs": ["close", "volume"], "func": vpd_126_obv_slope_to_price_slope_divergence},
    "vpd_127_turnover_range_divergence_ratio": {"inputs": ["volume", "high", "low", "sharesbas"], "func": vpd_127_turnover_to_range_divergence_ratio},
    "vpd_141_demand_collapse_index_21d": {"inputs": ["close", "volume"], "func": vpd_141_demand_collapse_index_21d},
    "vpd_142_mktcap_supply_surge_velocity": {"inputs": ["close", "volume", "sharesbas"], "func": vpd_142_mktcap_supply_surge_velocity},
    "vpd_143_consecutive_vp_div_days": {"inputs": ["close", "volume"], "func": vpd_143_consecutive_days_volume_up_price_down},
    "vpd_144_vp_overlap_efficiency_63d": {"inputs": ["close", "volume", "high", "low"], "func": vpd_144_volume_price_overlap_efficiency_63d},
    "vpd_145_ath_dd_volume_drift_div": {"inputs": ["close", "volume"], "func": vpd_145_ath_drawdown_volume_drift_divergence},
    "vpd_146_years_since_max_vp_div_ath": {"inputs": ["close", "volume"], "func": vpd_146_years_since_max_vp_divergence_ath},
    "vpd_147_climax_retracement_divergence": {"inputs": ["close", "volume"], "func": vpd_147_volume_climax_to_retracement_divergence},
    "vpd_148_ratio_supply_demand_volume_21d": {"inputs": ["close", "volume"], "func": vpd_148_ratio_of_supply_to_demand_volume_21d},
    "vpd_149_joint_vp_entropy_div_zscore": {"inputs": ["close", "volume"], "func": vpd_149_joint_vp_entropy_divergence_zscore},
    "vpd_150_vp_divergence_final_exhaustion": {"inputs": ["close", "volume"], "func": vpd_150_volume_price_divergence_final_exhaustion},
}
