"""
23_volume_oscillation — Base Features 076–150
Domain: cycles of volume expansion and contraction
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

# 076-090: Statistical Distribution of Oscillations
def vosc_076_pvo_pct_rank_ath(volume: pd.Series) -> pd.Series:
    ema12 = volume.ewm(span=12).mean()
    ema26 = volume.ewm(span=26).mean()
    pvo = 100 * _safe_div(ema12 - ema26, ema26)
    return pvo.expanding().rank(pct=True)


def vosc_077_pvo_zscore_252d(volume: pd.Series) -> pd.Series:
    ema12 = volume.ewm(span=12).mean()
    ema26 = volume.ewm(span=26).mean()
    pvo = 100 * _safe_div(ema12 - ema26, ema26)
    return (pvo - pvo.rolling(252).mean()) / pvo.rolling(252).std()


# 091-105: Oscillation Inflection and Momentum
def vosc_091_vosc_regime_stability_63d(volume: pd.Series) -> pd.Series:
    # R-squared of the volume MACD line
    ema21 = volume.ewm(span=21).mean()
    ema63 = volume.ewm(span=63).mean()
    macd = _safe_div(ema21 - ema63, ema63)
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    return macd.rolling(63).apply(_rsq, raw=True)


def vosc_092_days_since_vosc_peak_252d(volume: pd.Series) -> pd.Series:
    ema21 = volume.ewm(span=21).mean()
    ema63 = volume.ewm(span=63).mean()
    macd = _safe_div(ema21 - ema63, ema63)
    idx = macd.rolling(252).apply(np.argmax, raw=True)
    return 252 - 1 - idx


# 106-125: Event and Metric Specific Volume Oscillators
def vosc_106_mktcap_pvo_divergence_63d(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    # PVO(Volume) - PVO(MarketCap * Volume)
    def _pvo(v):
        e12 = v.ewm(span=12).mean()
        e26 = v.ewm(span=26).mean()
        return 100 * _safe_div(e12 - e26, e26)
    pvo_v = _pvo(volume)
    pvo_mc = _pvo(close * sharesbas * volume)
    return pvo_v - pvo_mc


def vosc_107_vosc_at_earnings_miss_63d(volume: pd.Series, surprise: pd.Series) -> pd.Series:
    ema21 = volume.ewm(span=21).mean()
    ema63 = volume.ewm(span=63).mean()
    macd = _safe_div(ema21 - ema63, ema63)
    return macd.where(surprise < 0).ffill()


# 126-140: Multi- Horizon Flow Ratios
def vosc_126_pvo_spread_short_long(volume: pd.Series) -> pd.Series:
    pvo_s = vosc_031_pvo_12_26(volume)
    ema63 = volume.ewm(span=63).mean()
    ema252 = volume.ewm(span=252).mean()
    pvo_l = 100 * _safe_div(ema63 - ema252, ema252)
    return pvo_s - pvo_l


def vosc_127_vosc_velocity_to_vol_ratio(volume: pd.Series) -> pd.Series:
    ema21 = volume.ewm(span=21).mean()
    ema63 = volume.ewm(span=63).mean()
    macd = _safe_div(ema21 - ema63, ema63)
    v = macd.diff(5)
    vol = volume.pct_change().rolling(21).std()
    return _safe_div(v, vol)


# 141-150: Final Oscillation composites
def vosc_141_volume_climax_oscillation_index(close: pd.Series, volume: pd.Series) -> pd.Series:
    # (PVO Histogram) * (Return Velocity)
    pvo = vosc_031_pvo_12_26(volume)
    sig = pvo.ewm(span=9).mean()
    hist = pvo - sig
    rv = np.log(close).diff(5).abs()
    return hist * rv


def vosc_142_mktcap_vosc_zscore_252d(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    cv = volume * np.log(mc + _EPS)
    ema21 = cv.ewm(span=21).mean()
    ema63 = cv.ewm(span=63).mean()
    macd = _safe_div(ema21 - ema63, ema63)
    return (macd - macd.rolling(252).mean()) / macd.rolling(252).std()


def vosc_143_consecutive_days_pvo_above_zero(volume: pd.Series) -> pd.Series:
    pvo = vosc_031_pvo_12_26(volume)
    above = (pvo > 0).astype(int)
    return above.groupby((above == 0).cumsum()).cumsum()


def vosc_144_vosc_reversal_climax_score(close: pd.Series, volume: pd.Series, low: pd.Series) -> pd.Series:
    pvo = vosc_031_pvo_12_26(volume)
    c_low = _safe_div(close, low)
    return pvo.diff(5) * c_low


def vosc_145_sustained_oscillation_climax_ratio(volume: pd.Series) -> pd.Series:
    # Mean(PVO) / Std(PVO)
    pvo = vosc_031_pvo_12_26(volume)
    return _safe_div(pvo.rolling(63).mean(), pvo.rolling(63).std())


def vosc_146_years_since_max_vosc_ath(volume: pd.Series) -> pd.Series:
    ema21 = volume.ewm(span=21).mean()
    ema63 = volume.ewm(span=63).mean()
    macd = _safe_div(ema21 - ema63, ema63)
    idx = macd.expanding().apply(np.argmax, raw=True)
    return (pd.Series(np.arange(len(volume)), index=volume.index) - idx) / 252.0


def vosc_147_pvo_trend_acceleration_21d(volume: pd.Series) -> pd.Series:
    pvo = vosc_031_pvo_12_26(volume)
    return pvo.diff(5).diff(5)


def vosc_148_ratio_of_vosc_peaks_to_troughs_252d(volume: pd.Series) -> pd.Series:
    from scipy.signal import argrelextrema
    ema21 = volume.ewm(span=21).mean()
    ema63 = volume.ewm(span=63).mean()
    macd = _safe_div(ema21 - ema63, ema63)
    p = argrelextrema(macd.values, np.greater, order=5)[0]
    t = argrelextrema(macd.values, np.less, order=5)[0]
    is_p = pd.Series(0, index=volume.index); is_p.iloc[p] = 1
    is_t = pd.Series(0, index=volume.index); is_t.iloc[t] = 1
    return _safe_div(is_p.rolling(252).sum(), is_t.rolling(252).sum())


def vosc_149_cumulative_vosc_energy_ath(volume: pd.Series) -> pd.Series:
    pvo = vosc_031_pvo_12_26(volume)
    return pvo.cumsum() / (pvo.abs().cumsum() + _EPS)


def vosc_150_volume_oscillation_final_imbalance(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Composite: PVO * (1 - Proximity to High) * Volatility
    pvo = vosc_031_pvo_12_26(volume) / 100.0
    h = close.rolling(252).max()
    dist_h = (h - close) / h
    vol = close.pct_change().rolling(21).std()
    return pvo * dist_h * vol


# ── Registry ──────────────────────────────────────────────────────────────────

V23_REGISTRY = {
    "vosc_076_pvo_pct_rank_ath": {"inputs": ["volume"], "func": vosc_076_pvo_pct_rank_ath},
    "vosc_077_pvo_zscore_252d": {"inputs": ["volume"], "func": vosc_077_pvo_zscore_252d},
    "vosc_091_vosc_regime_stability_63d": {"inputs": ["volume"], "func": vosc_091_vosc_regime_stability_63d},
    "vosc_092_days_since_vosc_peak_252d": {"inputs": ["volume"], "func": vosc_092_days_since_vosc_peak_252d},
    "vosc_106_mktcap_pvo_divergence_63d": {"inputs": ["close", "volume", "sharesbas"], "func": vosc_106_mktcap_pvo_divergence_63d},
    "vosc_107_vosc_at_earnings_miss_63d": {"inputs": ["volume", "surprise"], "func": vosc_107_vosc_at_earnings_miss_63d},
    "vosc_126_pvo_spread_short_long": {"inputs": ["volume"], "func": vosc_126_pvo_spread_short_long},
    "vosc_127_vosc_velocity_to_vol_ratio": {"inputs": ["volume"], "func": vosc_127_vosc_velocity_to_vol_ratio},
    "vosc_141_volume_climax_oscillation_index": {"inputs": ["close", "volume"], "func": vosc_141_volume_climax_oscillation_index},
    "vosc_142_mktcap_vosc_zscore_252d": {"inputs": ["close", "volume", "sharesbas"], "func": vosc_142_mktcap_vosc_zscore_252d},
    "vosc_143_consecutive_pvo_above_zero": {"inputs": ["volume"], "func": vosc_143_consecutive_days_pvo_above_zero},
    "vosc_144_vosc_reversal_climax_score": {"inputs": ["close", "volume", "low"], "func": vosc_144_vosc_reversal_climax_score},
    "vosc_145_sustained_oscillation_climax_ratio": {"inputs": ["volume"], "func": vosc_145_sustained_oscillation_climax_ratio},
    "vosc_146_years_since_max_vosc_ath": {"inputs": ["volume"], "func": vosc_146_years_since_max_vosc_ath},
    "vosc_147_pvo_trend_acceleration_21d": {"inputs": ["volume"], "func": vosc_147_pvo_trend_acceleration_21d},
    "vosc_148_ratio_vosc_peaks_troughs": {"inputs": ["volume"], "func": vosc_148_ratio_of_vosc_peaks_to_troughs_252d},
    "vosc_149_cumulative_vosc_energy_ath": {"inputs": ["volume"], "func": vosc_149_cumulative_vosc_energy_ath},
    "vosc_150_volume_oscillation_final_imbalance": {"inputs": ["close", "volume"], "func": vosc_150_volume_oscillation_final_imbalance},
}
