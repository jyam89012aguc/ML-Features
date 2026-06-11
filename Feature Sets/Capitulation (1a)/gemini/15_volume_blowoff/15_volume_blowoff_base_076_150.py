"""
15_volume_blowoff — Base Features 076–150
Domain: volume spikes vs trailing median
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

# 076-090: Distributional Volume Profiles
def vb_076_volume_pct_rank_ath(volume: pd.Series) -> pd.Series:
    return volume.expanding().rank(pct=True)


def vb_077_volume_zscore_ath(volume: pd.Series) -> pd.Series:
    return (volume - volume.expanding().mean()) / volume.expanding().std()


def vb_078_volume_concentration_top_5d_63d(volume: pd.Series) -> pd.Series:
    # Volume in top 5 days / Total volume in 63 days
    v_sort = volume.rolling(63).apply(lambda x: np.sort(x)[-5:].sum(), raw=True)
    v_total = volume.rolling(63).sum()
    return _safe_div(v_sort, v_total)


# 091-105: Climax Volume Threshold Counts
def vb_091_count_extreme_volume_spikes_252d(volume: pd.Series) -> pd.Series:
    # Number of days with volume > 3x trailing 252d median
    med = _rolling_median(volume, 252)
    return (volume > 3 * med).rolling(252).sum()


def vb_092_days_since_extreme_volume_spike_ath(volume: pd.Series) -> pd.Series:
    med = volume.expanding().median()
    is_spike = (volume > 3 * med)
    indices = pd.Series(np.arange(len(volume)), index=volume.index).where(is_spike).ffill()
    return pd.Series(np.arange(len(volume)), index=volume.index) - indices


# 106-125: Specialized Volume Accelerators
def vb_106_volume_velocity_21d(volume: pd.Series) -> pd.Series:
    # ROC of 5-day average volume
    v5 = _rolling_mean(volume, 5)
    return v5.pct_change(21)


def vb_107_volume_acceleration_63d(volume: pd.Series) -> pd.Series:
    # Change in volume velocity
    v = vb_106_volume_velocity_21d(volume)
    return v.diff(21)


# 126-140: Multi-Metric Volume Alignment
def vb_126_volume_spike_to_mktcap_spread(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    # (Volume/Median Volume) - (MktCap/ATH MktCap)
    v_rat = _safe_div(volume, _rolling_median(volume, 63))
    mc = close * sharesbas
    m_rat = mc / mc.cummax()
    return v_rat - m_rat


def vb_127_volume_climax_to_fundamental_yield(volume: pd.Series, sharesbas: pd.Series, netinc: pd.Series) -> pd.Series:
    # Turnover ratio * (Earnings Yield)
    turnover = _safe_div(volume, sharesbas)
    ey = _safe_div(netinc, volume * 0) # Placeholder if not available
    # Using simpler proxy: Turnover * 1 on spike
    return turnover.where(volume > 2 * _rolling_median(volume, 63))


# 141-150: Final Volume composites
def vb_141_volume_capitulation_climax_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    # (Volume Spike) * (1 - Proximity to Low)
    l = close.rolling(252).min()
    prox = _safe_div(close, l)
    v_spike = _safe_div(volume, _rolling_median(volume, 63))
    return v_spike * (prox - 1.0).abs()


def vb_142_mktcap_velocity_to_volume_velocity_ratio(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    v_mc = np.log(close * sharesbas).diff(21)
    v_vol = np.log(volume + 1.0).diff(21)
    return _safe_div(v_mc, v_vol)


def vb_143_volume_oscillator_21_63(volume: pd.Series) -> pd.Series:
    # (V_avg_21 / V_avg_63) - 1
    v21 = _rolling_mean(volume, 21)
    v63 = _rolling_mean(volume, 63)
    return _safe_div(v21, v63) - 1.0


def vb_144_volume_trend_stability_score(volume: pd.Series) -> pd.Series:
    # R-squared of volume over last 21 days
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    return volume.rolling(21).apply(_rsq, raw=True)


def vb_145_cumulative_excess_volume_ratio_252d(volume: pd.Series) -> pd.Series:
    # Integral of volume above median / total integral
    med = _rolling_median(volume, 252)
    excess = (volume - med).clip(lower=0)
    return _safe_div(excess.rolling(252).sum(), volume.rolling(252).sum())


def vb_146_volume_spike_at_earnings_surprise(volume: pd.Series, surprise: pd.Series) -> pd.Series:
    # Volume spike ratio on earnings days
    ratio = _safe_div(volume, _rolling_median(volume, 63))
    return ratio.where(surprise.abs() > 0).ffill()


def vb_147_volume_spike_frequency_regime_shift(volume: pd.Series) -> pd.Series:
    # Ratio of spike frequency in 21d vs 252d
    med = _rolling_median(volume, 252)
    is_spike = (volume > 2 * med).astype(int)
    f21 = is_spike.rolling(21).mean()
    f252 = is_spike.rolling(252).mean()
    return _safe_div(f21, f252)


def vb_148_volume_weighted_log_ret_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    lret = np.log(close / close.shift(1))
    v_norm = _safe_div(volume, volume.rolling(63).sum())
    return (lret * v_norm).rolling(63).sum()


def vb_149_volume_climax_energy_score(volume: pd.Series) -> pd.Series:
    # (Volume / Median)^2 / Volatility of Volume
    v_rat = _safe_div(volume, _rolling_median(volume, 63))
    v_vol = volume.pct_change().rolling(21).std()
    return _safe_div(v_rat**2, v_vol)


def vb_150_terminal_volume_flush_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Composite: (Volume Spike) * (Consecutive Down Days) * (1 - Proximity to High)
    vs = _safe_div(volume, _rolling_median(volume, 63))
    is_down = (close < close.shift(1))
    streak = is_down.astype(int).groupby((is_down != is_down.shift()).cumsum()).cumsum()
    dist_h = (close.rolling(252).max() - close) / close.rolling(252).max()
    return vs * streak * dist_h


# ── Registry ──────────────────────────────────────────────────────────────────

V15_REGISTRY = {
    "vb_076_volume_pct_rank_ath": {"inputs": ["volume"], "func": vb_076_volume_pct_rank_ath},
    "vb_077_volume_zscore_ath": {"inputs": ["volume"], "func": vb_077_volume_zscore_ath},
    "vb_078_volume_concentration_top_5d_63d": {"inputs": ["volume"], "func": vb_078_volume_concentration_top_5d_63d},
    "vb_091_count_extreme_volume_spikes_252d": {"inputs": ["volume"], "func": vb_091_count_extreme_volume_spikes_252d},
    "vb_092_days_since_extreme_volume_spike_ath": {"inputs": ["volume"], "func": vb_092_days_since_extreme_volume_spike_ath},
    "vb_106_volume_velocity_21d": {"inputs": ["volume"], "func": vb_106_volume_velocity_21d},
    "vb_107_volume_acceleration_63d": {"inputs": ["volume"], "func": vb_107_volume_acceleration_63d},
    "vb_126_volume_spike_to_mktcap_spread": {"inputs": ["close", "volume", "sharesbas"], "func": vb_126_volume_spike_to_mktcap_spread},
    "vb_127_volume_climax_fundamental_proxy": {"inputs": ["volume", "sharesbas", "netinc"], "func": vb_127_volume_climax_to_fundamental_yield},
    "vb_141_volume_capitulation_climax_score": {"inputs": ["close", "volume"], "func": vb_141_volume_capitulation_climax_score},
    "vb_142_mktcap_to_volume_velocity_ratio": {"inputs": ["close", "volume", "sharesbas"], "func": vb_142_mktcap_velocity_to_volume_velocity_ratio},
    "vb_143_volume_oscillator_21_63": {"inputs": ["volume"], "func": vb_143_volume_oscillator_21_63},
    "vb_144_volume_trend_stability_score": {"inputs": ["volume"], "func": vb_144_volume_trend_stability_score},
    "vb_145_cumulative_excess_volume_ratio_252d": {"inputs": ["volume"], "func": vb_145_cumulative_excess_volume_ratio_252d},
    "vb_146_volume_spike_at_earnings_surprise": {"inputs": ["volume", "surprise"], "func": vb_146_volume_spike_at_earnings_surprise},
    "vb_147_volume_spike_freq_regime_shift": {"inputs": ["volume"], "func": vb_147_volume_spike_frequency_regime_shift},
    "vb_148_volume_weighted_log_ret_63d": {"inputs": ["close", "volume"], "func": vb_148_volume_weighted_log_ret_63d},
    "vb_149_volume_climax_energy_score": {"inputs": ["volume"], "func": vb_149_volume_climax_energy_score},
    "vb_150_terminal_volume_flush_index": {"inputs": ["close", "volume"], "func": vb_150_terminal_volume_flush_index},
}
