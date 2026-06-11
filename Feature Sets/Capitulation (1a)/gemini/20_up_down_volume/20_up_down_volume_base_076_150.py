"""
20_up_down_volume — Base Features 076–150
Domain: volume on down days vs up days
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

# 076-090: Statistical Distribution of Up/Down Ratios
def udv_076_up_down_volume_ratio_pct_rank_ath(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_up = volume.where(close > close.shift(1), 0).rolling(63).sum()
    v_dn = volume.where(close < close.shift(1), 0).rolling(63).sum()
    ratio = _safe_div(v_up, v_dn)
    return ratio.expanding().rank(pct=True)


def udv_077_down_volume_concentration_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    is_down = (close < close.shift(1))
    v_down = volume.where(is_down, 0).rolling(21).sum()
    v_total = volume.rolling(21).sum()
    conc = _safe_div(v_down, v_total)
    return (conc - conc.rolling(252).mean()) / conc.rolling(252).std()


def udv_078_up_down_volume_volatility_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Std Dev of Up-Volume / Std Dev of Down-Volume
    v_up = volume.where(close > close.shift(1))
    v_dn = volume.where(close < close.shift(1))
    return _safe_div(v_up.rolling(63).std(), v_dn.rolling(63).std())


# 091-105: Pressure Inflection points
def udv_091_pressure_shift_index_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Change in (Down Volume / Total Volume) over last 21 days
    v_dn_rat = _safe_div(volume.where(close < close.shift(1), 0).rolling(21).sum(), volume.rolling(21).sum())
    return v_dn_rat.diff(21)


def udv_092_count_extreme_down_volume_days_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Days with negative return AND volume > 3x median
    med = volume.rolling(252).median()
    is_climax_dn = (close < close.shift(1)) & (volume > 3 * med)
    return is_climax_dn.astype(int).rolling(252).sum()


# 106-125: Specialized Force and Momentum components
def udv_106_normalized_force_index_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # (Close - Prev) * (Volume / Median)
    fi = close.diff(1) * _safe_div(volume, volume.rolling(252).median())
    return fi.rolling(63).mean()


def udv_107_volume_weighted_rsi_14(close: pd.Series, volume: pd.Series) -> pd.Series:
    delta = close.diff()
    v_gain = (delta.where(delta > 0, 0) * volume).rolling(14).mean()
    v_loss = (delta.where(delta < 0, 0).abs() * volume).rolling(14).mean()
    rs = _safe_div(v_gain, v_loss)
    return 100 - (100 / (1 + rs))


# 126-140: Multi-Metric Flow Ratios
def udv_126_mktcap_ud_spread_zscore_252d(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v_sig = np.sign(mc.diff()) * volume
    return (v_sig - v_sig.rolling(252).mean()) / v_sig.rolling(252).std()


def udv_127_obv_slope_to_volume_trend_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Slope of OBV / Slope of Volume (Is the 'quality' of volume trend confirming price?)
    def _slope(y):
        from scipy.stats import linregress
        if len(y) < 2: return 0.0
        return linregress(np.arange(len(y)), y).slope
    ret = close.diff()
    obv = (np.sign(ret) * volume).cumsum()
    os = _slope(obv.rolling(63).mean())
    vs = _slope(volume.rolling(63).mean())
    return _safe_div(pd.Series(os), pd.Series(vs)).iloc[0]


# 141-150: Final Up/Down composites
def udv_141_buying_exhaustion_score_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # (Up Volume Ratio) / (Return Velocity) -> looking for buyers failing to push price
    is_up = (close > close.shift(1))
    v_up_rat = _safe_div(volume.where(is_up, 0).rolling(21).mean(), volume.rolling(252).median())
    p_vel = np.log(close).diff(5).abs()
    return _safe_div(v_up_rat, p_vel + _EPS)


def udv_142_down_volume_energy_index_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    # (Down Volume / Total)^2 * Drawdown Velocity
    v_dn = volume.where(close < close.shift(1), 0).rolling(63).sum()
    v_tot = volume.rolling(63).sum()
    ratio = _safe_div(v_dn, v_tot)
    p_vel = np.log(close).diff(21).abs()
    return (ratio**2) * p_vel


def udv_143_consecutive_days_up_volume_expansion(close: pd.Series, volume: pd.Series) -> pd.Series:
    is_up = (close > close.shift(1))
    v_inc = (volume > volume.shift(1))
    cond = (is_up & v_inc).astype(int)
    return cond.groupby((cond == 0).cumsum()).cumsum()


def udv_144_volume_reversal_climax_score_63d(close: pd.Series, volume: pd.Series, low: pd.Series) -> pd.Series:
    # (Volume Spike) * (Close from Low ratio) on Down Days
    is_down = (close < close.shift(1))
    v_rat = _safe_div(volume, volume.rolling(252).median())
    c_low = _safe_div(close, low)
    return (v_rat * c_low).where(is_down).ffill()


def udv_145_mktcap_down_volume_persistence_63d(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    is_down = (mc < mc.shift(1))
    return volume.where(is_down, 0).rolling(63).mean() / volume.rolling(252).median()


def udv_146_ratio_of_up_to_down_vol_at_support_tests(close: pd.Series, volume: pd.Series) -> pd.Series:
    l = close.rolling(252).min()
    near = (close <= l * 1.03)
    v_up = volume.where((close > close.shift(1)) & near, 0).rolling(252).sum()
    v_dn = volume.where((close < close.shift(1)) & near, 0).rolling(252).sum()
    return _safe_div(v_up, v_dn)


def udv_147_days_since_up_volume_climax_ath(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_up = volume.where(close > close.shift(1), 0)
    idx = v_up.expanding().apply(np.argmax, raw=True)
    return pd.Series(np.arange(len(volume)), index=volume.index) - idx


def udv_148_volume_pressure_oscillator_21_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    vp = _safe_div(volume.where(close < close.shift(1), 0).rolling(21).sum(), volume.rolling(21).sum())
    vp_long = _safe_div(volume.where(close < close.shift(1), 0).rolling(63).sum(), volume.rolling(63).sum())
    return vp - vp_long


def udv_149_cumulative_obv_energy_ath(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.diff()
    v_sig = np.sign(ret) * volume
    return v_sig.cumsum() / (volume.cumsum() + _EPS)


def udv_150_up_down_volume_final_imbalance_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Composite: (Down Volume / Total) * (1 - Proximity to High) * Volatility
    v_dn_rat = _safe_div(volume.where(close < close.shift(1), 0).rolling(63).sum(), volume.rolling(63).sum())
    h = close.rolling(252).max()
    dist_h = (h - close) / h
    vol = close.pct_change().rolling(21).std()
    return v_dn_rat * dist_h * vol


# ── Registry ──────────────────────────────────────────────────────────────────

V20_REGISTRY = {
    "udv_076_up_down_volume_ratio_pct_rank_ath": {"inputs": ["close", "volume"], "func": udv_076_up_down_volume_ratio_pct_rank_ath},
    "udv_077_down_volume_concentration_zscore_252d": {"inputs": ["close", "volume"], "func": udv_077_down_volume_concentration_zscore_252d},
    "udv_078_up_down_volume_volatility_ratio_63d": {"inputs": ["close", "volume"], "func": udv_078_up_down_volume_volatility_ratio_63d},
    "udv_091_pressure_shift_index_21d": {"inputs": ["close", "volume"], "func": udv_091_pressure_shift_index_21d},
    "udv_092_count_extreme_down_volume_days_252d": {"inputs": ["close", "volume"], "func": udv_092_count_extreme_down_volume_days_252d},
    "udv_106_normalized_force_index_63d": {"inputs": ["close", "volume"], "func": udv_106_normalized_force_index_63d},
    "udv_107_volume_weighted_rsi_14": {"inputs": ["close", "volume"], "func": udv_107_volume_weighted_rsi_14},
    "udv_126_mktcap_ud_spread_zscore_252d": {"inputs": ["close", "volume", "sharesbas"], "func": udv_126_mktcap_ud_spread_zscore_252d},
    "udv_127_obv_to_volume_trend_ratio_63d": {"inputs": ["close", "volume"], "func": udv_127_obv_slope_to_volume_trend_ratio_63d},
    "udv_141_buying_exhaustion_score_21d": {"inputs": ["close", "volume"], "func": udv_141_buying_exhaustion_score_21d},
    "udv_142_down_volume_energy_index_63d": {"inputs": ["close", "volume"], "func": udv_142_down_volume_energy_index_63d},
    "udv_143_consecutive_up_volume_expansion_days": {"inputs": ["close", "volume"], "func": udv_143_consecutive_days_up_volume_expansion},
    "udv_144_volume_reversal_climax_score_63d": {"inputs": ["close", "volume", "low"], "func": udv_144_volume_reversal_climax_score_63d},
    "udv_145_mktcap_down_volume_persistence_63d": {"inputs": ["close", "volume", "sharesbas"], "func": udv_145_mktcap_down_volume_persistence_63d},
    "udv_146_ratio_ud_vol_at_support_tests": {"inputs": ["close", "volume"], "func": udv_146_ratio_of_up_to_down_vol_at_support_tests},
    "udv_147_days_since_up_volume_climax_ath": {"inputs": ["close", "volume"], "func": udv_147_days_since_up_volume_climax_ath},
    "udv_148_volume_pressure_oscillator_21_63": {"inputs": ["close", "volume"], "func": udv_148_volume_pressure_oscillator_21_63},
    "udv_149_cumulative_obv_energy_ath": {"inputs": ["close", "volume"], "func": udv_149_cumulative_obv_energy_ath},
    "udv_150_up_down_volume_final_imbalance_index": {"inputs": ["close", "volume"], "func": udv_150_up_down_volume_final_imbalance_index},
}
