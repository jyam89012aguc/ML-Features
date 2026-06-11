"""
23_volume_oscillation — 2nd Derivatives
Domain: rate of change of base features — captures acceleration of decline/distress
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


# ── Feature functions ────────────────────────────────────────────────────────

# 25 features capturing acceleration of volume oscillation metrics
def vosc_drv2_001_pvo_12_26_velocity(volume: pd.Series) -> pd.Series:
    # Change in PVO
    ema12 = volume.ewm(span=12).mean()
    ema26 = volume.ewm(span=26).mean()
    pvo = 100 * _safe_div(ema12 - ema26, ema26)
    return pvo.diff(5)


def vosc_drv2_002_volume_macd_velocity(volume: pd.Series) -> pd.Series:
    v21 = volume.ewm(span=21).mean()
    v63 = volume.ewm(span=63).mean()
    macd = _safe_div(v21 - v63, v63)
    return macd.diff(5)


def vosc_drv2_003_pvo_histogram_velocity(volume: pd.Series) -> pd.Series:
    ema12 = volume.ewm(span=12).mean()
    ema26 = volume.ewm(span=26).mean()
    pvo = 100 * _safe_div(ema12 - ema26, ema26)
    sig = pvo.ewm(span=9).mean()
    hist = pvo - sig
    return hist.diff(5)


def vosc_drv2_004_chaikin_oscillator_velocity(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ad = _safe_div((close - low) - (high - close), high - low) * volume
    ad_sum = ad.cumsum()
    co = ad_sum.ewm(span=3).mean() - ad_sum.ewm(span=10).mean()
    return co.diff(5)


def vosc_drv2_005_volume_wave_intensity_velocity(volume: pd.Series) -> pd.Series:
    med = volume.rolling(63).median()
    v_avg = volume.rolling(63).mean()
    intens = (volume - med).abs().rolling(63).mean() / (v_avg + _EPS)
    return intens.diff(5)


def vosc_drv2_006_vosc_stability_velocity(volume: pd.Series) -> pd.Series:
    ema12 = volume.ewm(span=12).mean()
    ema26 = volume.ewm(span=26).mean()
    pvo = 100 * _safe_div(ema12 - ema26, ema26)
    sig = pvo.ewm(span=9).mean()
    hist = pvo - sig
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = hist.rolling(21).apply(_rsq, raw=True)
    return rs.diff(5)


def vosc_drv2_007_vosc_regime_shift_velocity(volume: pd.Series) -> pd.Series:
    ema12 = volume.ewm(span=12).mean()
    ema26 = volume.ewm(span=26).mean()
    pvo = 100 * _safe_div(ema12 - ema26, ema26)
    rsi = _safe_div(pvo.rolling(21).mean(), pvo.rolling(252).mean().abs())
    return rsi.diff(5)


def vosc_drv2_008_vosc_climax_reversal_velocity(close: pd.Series, volume: pd.Series, low: pd.Series) -> pd.Series:
    ema12 = volume.ewm(span=12).mean()
    ema26 = volume.ewm(span=26).mean()
    pvo = 100 * _safe_div(ema12 - ema26, ema26)
    score = pvo * _safe_div(close, low)
    return score.diff(5)


def vosc_drv2_009_vosc_momentum_div_velocity(volume: pd.Series) -> pd.Series:
    div = volume.pct_change(5) - volume.pct_change(21)
    return div.diff(5)


def vosc_drv2_010_joint_pv_osc_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    ema12_v = volume.ewm(span=12).mean()
    ema26_v = volume.ewm(span=26).mean()
    pvo = 100 * _safe_div(ema12_v - ema26_v, ema26_v)
    ema12_p = close.ewm(span=12).mean()
    ema26_p = close.ewm(span=26).mean()
    ppo = 100 * _safe_div(ema12_p - ema26_p, ema26_p)
    spr = pvo - ppo
    return spr.diff(5)


def vosc_drv2_011_pvo_accel_velocity(volume: pd.Series) -> pd.Series:
    pvo = 100 * _safe_div(volume.ewm(span=12).mean() - volume.ewm(span=26).mean(), volume.ewm(span=26).mean())
    acc = pvo.diff(5)
    return acc.diff(5)


def vosc_drv2_012_vosc_climax_intensity_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    pvo = 100 * _safe_div(volume.ewm(span=12).mean() - volume.ewm(span=26).mean(), volume.ewm(span=26).mean())
    rv = np.log(close).diff(5).abs()
    score = pvo * rv
    return score.diff(5)


def vosc_drv2_013_vosc_exhaustion_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    pvo = 100 * _safe_div(volume.ewm(span=12).mean() - volume.ewm(span=26).mean(), volume.ewm(span=26).mean())
    h = close.rolling(252).max()
    dd = (h - close) / h
    idx = pvo * dd
    return idx.diff(5)


def vosc_drv2_014_mktcap_vosc_velocity(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    cv = volume * np.log(mc + _EPS)
    v21 = cv.ewm(span=21).mean()
    v63 = cv.ewm(span=63).mean()
    macd = _safe_div(v21 - v63, v63)
    return macd.diff(5)


def vosc_drv2_015_pvo_spread_short_long_velocity(volume: pd.Series) -> pd.Series:
    ema12 = volume.ewm(span=12).mean()
    ema26 = volume.ewm(span=26).mean()
    pvo_s = 100 * _safe_div(ema12 - ema26, ema26)
    ema63 = volume.ewm(span=63).mean()
    ema252 = volume.ewm(span=252).mean()
    pvo_l = 100 * _safe_div(ema63 - ema252, ema252)
    return (pvo_s - pvo_l).diff(5)


def vosc_drv2_016_volume_jitter_velocity(volume: pd.Series) -> pd.Series:
    r = volume.rolling(21).max() - volume.rolling(21).min()
    jit = _safe_div(r, volume.rolling(21).mean())
    return jit.diff(5)


def vosc_drv2_017_consecutive_vosc_inc_velocity(volume: pd.Series) -> pd.Series:
    v21 = volume.ewm(span=21).mean()
    v63 = volume.ewm(span=63).mean()
    macd = _safe_div(v21 - v63, v63)
    inc = (macd > macd.shift(1)).astype(int)
    dur = inc.groupby((inc == 0).cumsum()).cumsum()
    return dur.diff(5)


def vosc_drv2_018_volume_wave_entropy_velocity(volume: pd.Series) -> pd.Series:
    def _pvo(v):
        e12 = v.ewm(span=12).mean()
        e26 = v.ewm(span=26).mean()
        return 100 * _safe_div(e12 - e26, e26)
    pvo = _pvo(volume)
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y, bins=10, density=True)
        p = h[h > 0]
        return -np.sum(p * np.log(p))
    e = pvo.rolling(63).apply(_ent, raw=True)
    return e.diff(5)


def vosc_drv2_019_vosc_final_composite_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vosc_075_volume_oscillation_final_composite(close, volume)
    return score.diff(5)


def vosc_drv2_020_turnover_vosc_velocity(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    ema21 = to.ewm(span=21).mean()
    ema63 = to.ewm(span=63).mean()
    macd = _safe_div(ema21 - ema63, ema63)
    return macd.diff(5)


def vosc_drv2_021_volume_cycle_period_velocity(volume: pd.Series) -> pd.Series:
    v_z = (volume - volume.rolling(252).mean()) / volume.rolling(252).std()
    is_peak = (v_z > 2.0)
    idx = pd.Series(np.arange(len(volume)), index=volume.index).where(is_peak).ffill()
    gap = idx.diff().rolling(252).mean()
    return gap.diff(5)


def vosc_drv2_022_vosc_reversal_velocity(volume: pd.Series) -> pd.Series:
    # 5d change in PVO
    pvo = 100 * _safe_div(volume.ewm(span=12).mean() - volume.ewm(span=26).mean(), volume.ewm(span=26).mean())
    return pvo.diff(5).diff(5)


def vosc_drv2_023_vosc_peak_proximity_velocity(volume: pd.Series) -> pd.Series:
    pvo = 100 * _safe_div(volume.ewm(span=12).mean() - volume.ewm(span=26).mean(), volume.ewm(span=26).mean())
    idx = pvo.rolling(252).apply(np.argmax, raw=True)
    dsp = 252 - 1 - idx
    return dsp.diff(5)


def vosc_drv2_024_cumulative_vosc_energy_velocity(volume: pd.Series) -> pd.Series:
    pvo = 100 * _safe_div(volume.ewm(span=12).mean() - volume.ewm(span=26).mean(), volume.ewm(span=26).mean())
    energy = pvo.cumsum() / (pvo.abs().cumsum() + _EPS)
    return energy.diff(5)


def vosc_drv2_025_vosc_velocity_to_vol_accel(volume: pd.Series) -> pd.Series:
    macd = _safe_div(volume.ewm(span=21).mean() - volume.ewm(span=63).mean(), volume.ewm(span=63).mean())
    v = macd.diff(5)
    vol = volume.pct_change().rolling(21).std()
    ratio = _safe_div(v, vol)
    return ratio.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V23_V_REGISTRY = {
    "vosc_drv2_001_pvo_12_26_velocity": {"inputs": ["volume"], "func": vosc_drv2_001_pvo_12_26_velocity},
    "vosc_drv2_002_volume_macd_velocity": {"inputs": ["volume"], "func": vosc_drv2_002_volume_macd_velocity},
    "vosc_drv2_003_pvo_histogram_velocity": {"inputs": ["volume"], "func": vosc_drv2_003_pvo_histogram_velocity},
    "vosc_drv2_004_chaikin_oscillator_velocity": {"inputs": ["volume", "high", "low", "close"], "func": vosc_drv2_004_chaikin_oscillator_velocity},
    "vosc_drv2_005_volume_wave_intensity_velocity": {"inputs": ["volume"], "func": vosc_drv2_005_volume_wave_intensity_velocity},
    "vosc_drv2_006_vosc_stability_velocity": {"inputs": ["volume"], "func": vosc_drv2_006_vosc_stability_velocity},
    "vosc_drv2_007_vosc_regime_shift_velocity": {"inputs": ["volume"], "func": vosc_drv2_007_vosc_regime_shift_velocity},
    "vosc_drv2_008_vosc_climax_reversal_velocity": {"inputs": ["close", "volume", "low"], "func": vosc_drv2_008_vosc_climax_reversal_velocity},
    "vosc_drv2_009_vosc_momentum_div_velocity": {"inputs": ["volume"], "func": vosc_drv2_009_vosc_momentum_div_velocity},
    "vosc_drv2_010_joint_pv_osc_velocity": {"inputs": ["close", "volume"], "func": vosc_drv2_010_joint_pv_osc_velocity},
    "vosc_drv2_011_pvo_accel_velocity": {"inputs": ["volume"], "func": vosc_drv2_011_pvo_accel_velocity},
    "vosc_drv2_012_vosc_climax_intensity_velocity": {"inputs": ["close", "volume"], "func": vosc_drv2_012_vosc_climax_intensity_velocity},
    "vosc_drv2_013_vosc_exhaustion_velocity": {"inputs": ["close", "volume"], "func": vosc_drv2_013_vosc_exhaustion_velocity},
    "vosc_drv2_014_mktcap_vosc_velocity": {"inputs": ["close", "volume", "sharesbas"], "func": vosc_drv2_014_mktcap_vosc_velocity},
    "vosc_drv2_015_pvo_spread_short_long_velocity": {"inputs": ["volume"], "func": vosc_drv2_015_pvo_spread_short_long_velocity},
    "vosc_drv2_016_volume_jitter_velocity": {"inputs": ["volume"], "func": vosc_drv2_016_volume_jitter_velocity},
    "vosc_drv2_017_consecutive_vosc_inc_velocity": {"inputs": ["volume"], "func": vosc_drv2_017_consecutive_vosc_inc_velocity},
    "vosc_drv2_018_volume_wave_entropy_velocity": {"inputs": ["volume"], "func": vosc_drv2_018_volume_wave_entropy_velocity},
    "vosc_drv2_019_vosc_final_composite_velocity": {"inputs": ["close", "volume"], "func": vosc_drv2_019_vosc_final_composite_velocity},
    "vosc_drv2_020_turnover_vosc_velocity": {"inputs": ["volume", "sharesbas"], "func": vosc_drv2_020_turnover_vosc_velocity},
    "vosc_drv2_021_volume_cycle_period_velocity": {"inputs": ["volume"], "func": vosc_drv2_021_volume_cycle_period_velocity},
    "vosc_drv2_022_vosc_reversal_velocity": {"inputs": ["volume"], "func": vosc_drv2_022_vosc_reversal_velocity},
    "vosc_drv2_023_vosc_peak_proximity_velocity": {"inputs": ["volume"], "func": vosc_drv2_023_vosc_peak_proximity_velocity},
    "vosc_drv2_024_cumulative_vosc_energy_velocity": {"inputs": ["volume"], "func": vosc_drv2_024_cumulative_vosc_energy_velocity},
    "vosc_drv2_025_vosc_velocity_to_vol_accel": {"inputs": ["volume"], "func": vosc_drv2_025_vosc_velocity_to_vol_accel},
}
