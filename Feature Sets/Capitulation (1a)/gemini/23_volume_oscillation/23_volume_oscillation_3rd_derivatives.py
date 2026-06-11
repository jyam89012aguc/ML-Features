"""
23_volume_oscillation — 3rd Derivatives
Domain: rate of change of 2nd derivatives — captures exhaustion/inflection of acceleration
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

# 25 features capturing exhaustion/inflection of volume oscillation acceleration (jerk)
def vosc_drv3_001_pvo_12_26_jerk(volume: pd.Series) -> pd.Series:
    # Rate of change of PVO velocity
    ema12 = volume.ewm(span=12).mean()
    ema26 = volume.ewm(span=26).mean()
    pvo = 100 * _safe_div(ema12 - ema26, ema26)
    vel = pvo.diff(5)
    return vel.diff(5)


def vosc_drv3_002_volume_macd_jerk(volume: pd.Series) -> pd.Series:
    v21 = volume.ewm(span=21).mean()
    v63 = volume.ewm(span=63).mean()
    macd = _safe_div(v21 - v63, v63)
    vel = macd.diff(5)
    return vel.diff(5)


def vosc_drv3_003_pvo_histogram_jerk(volume: pd.Series) -> pd.Series:
    ema12 = volume.ewm(span=12).mean()
    ema26 = volume.ewm(span=26).mean()
    pvo = 100 * _safe_div(ema12 - ema26, ema26)
    sig = pvo.ewm(span=9).mean()
    hist = pvo - sig
    vel = hist.diff(5)
    return vel.diff(5)


def vosc_drv3_004_chaikin_oscillator_jerk(volume: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    ad = _safe_div((close - low) - (high - close), high - low) * volume
    ad_sum = ad.cumsum()
    co = ad_sum.ewm(span=3).mean() - ad_sum.ewm(span=10).mean()
    vel = co.diff(5)
    return vel.diff(5)


def vosc_drv3_005_volume_wave_intensity_jerk(volume: pd.Series) -> pd.Series:
    med = volume.rolling(63).median()
    v_avg = volume.rolling(63).mean()
    intens = (volume - med).abs().rolling(63).mean() / (v_avg + _EPS)
    vel = intens.diff(5)
    return vel.diff(5)


def vosc_drv3_006_vosc_stability_jerk(volume: pd.Series) -> pd.Series:
    pvo = 100 * _safe_div(volume.ewm(span=12).mean() - volume.ewm(span=26).mean(), volume.ewm(span=26).mean())
    sig = pvo.ewm(span=9).mean()
    hist = pvo - sig
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = hist.rolling(21).apply(_rsq, raw=True)
    vel = rs.diff(5)
    return vel.diff(5)


def vosc_drv3_007_vosc_regime_shift_jerk(volume: pd.Series) -> pd.Series:
    pvo = 100 * _safe_div(volume.ewm(span=12).mean() - volume.ewm(span=26).mean(), volume.ewm(span=26).mean())
    rsi = _safe_div(pvo.rolling(21).mean(), pvo.rolling(252).mean().abs())
    vel = rsi.diff(5)
    return vel.diff(5)


def vosc_drv3_008_vosc_climax_reversal_jerk(close: pd.Series, volume: pd.Series, low: pd.Series) -> pd.Series:
    pvo = 100 * _safe_div(volume.ewm(span=12).mean() - volume.ewm(span=26).mean(), volume.ewm(span=26).mean())
    score = pvo * _safe_div(close, low + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def vosc_drv3_009_vosc_momentum_div_jerk(volume: pd.Series) -> pd.Series:
    div = volume.pct_change(5) - volume.pct_change(21)
    vel = div.diff(5)
    return vel.diff(5)


def vosc_drv3_010_joint_pv_osc_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    pvo = 100 * _safe_div(volume.ewm(span=12).mean() - volume.ewm(span=26).mean(), volume.ewm(span=26).mean())
    ppo = 100 * _safe_div(close.ewm(span=12).mean() - close.ewm(span=26).mean(), close.ewm(span=26).mean())
    spr = pvo - ppo
    vel = spr.diff(5)
    return vel.diff(5)


def vosc_drv3_011_pvo_accel_jerk(volume: pd.Series) -> pd.Series:
    pvo = 100 * _safe_div(volume.ewm(span=12).mean() - volume.ewm(span=26).mean(), volume.ewm(span=26).mean())
    acc = pvo.diff(5)
    vel = acc.diff(5)
    return vel.diff(5)


def vosc_drv3_012_vosc_climax_intensity_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    pvo = 100 * _safe_div(volume.ewm(span=12).mean() - volume.ewm(span=26).mean(), volume.ewm(span=26).mean())
    rv = np.log(close).diff(5).abs()
    score = pvo * rv
    vel = score.diff(5)
    return vel.diff(5)


def vosc_drv3_013_vosc_exhaustion_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    pvo = 100 * _safe_div(volume.ewm(span=12).mean() - volume.ewm(span=26).mean(), volume.ewm(span=26).mean())
    h = close.rolling(252).max()
    dd = (h - close) / h
    idx = pvo * dd
    vel = idx.diff(5)
    return vel.diff(5)


def vosc_drv3_014_mktcap_vosc_jerk(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    cv = volume * np.log(mc + _EPS)
    v21 = cv.ewm(span=21).mean()
    v63 = cv.ewm(span=63).mean()
    macd = _safe_div(v21 - v63, v63)
    vel = macd.diff(5)
    return vel.diff(5)


def vosc_drv3_015_pvo_spread_short_long_jerk(volume: pd.Series) -> pd.Series:
    pvo_s = 100 * _safe_div(volume.ewm(span=12).mean() - volume.ewm(span=26).mean(), volume.ewm(span=26).mean())
    pvo_l = 100 * _safe_div(volume.ewm(span=63).mean() - volume.ewm(span=252).mean(), volume.ewm(span=252).mean())
    spr = pvo_s - pvo_l
    vel = spr.diff(5)
    return vel.diff(5)


def vosc_drv3_016_volume_jitter_jerk(volume: pd.Series) -> pd.Series:
    r = volume.rolling(21).max() - volume.rolling(21).min()
    jit = _safe_div(r, volume.rolling(21).mean())
    vel = jit.diff(5)
    return vel.diff(5)


def vosc_drv3_017_consecutive_vosc_inc_jerk(volume: pd.Series) -> pd.Series:
    macd = _safe_div(volume.ewm(span=21).mean() - volume.ewm(span=63).mean(), volume.ewm(span=63).mean())
    inc = (macd > macd.shift(1)).astype(int)
    dur = inc.groupby((inc == 0).cumsum()).cumsum()
    vel = dur.diff(5)
    return vel.diff(5)


def vosc_drv3_018_volume_wave_entropy_jerk(volume: pd.Series) -> pd.Series:
    pvo = 100 * _safe_div(volume.ewm(span=12).mean() - volume.ewm(span=26).mean(), volume.ewm(span=26).mean())
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y, bins=10, density=True)
        p = h[h > 0]
        return -np.sum(p * np.log(p))
    e = pvo.rolling(63).apply(_ent, raw=True)
    vel = e.diff(5)
    return vel.diff(5)


def vosc_drv3_019_vosc_final_composite_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vosc_075_volume_oscillation_final_composite(close, volume)
    vel = score.diff(5)
    return vel.diff(5)


def vosc_drv3_020_turnover_vosc_jerk(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    macd = _safe_div(to.ewm(span=21).mean() - to.ewm(span=63).mean(), to.ewm(span=63).mean())
    vel = macd.diff(5)
    return vel.diff(5)


def vosc_drv3_021_volume_cycle_period_jerk(volume: pd.Series) -> pd.Series:
    v_z = (volume - volume.rolling(252).mean()) / (volume.rolling(252).std() + _EPS)
    is_peak = (v_z > 2.0)
    idx = pd.Series(np.arange(len(volume)), index=volume.index).where(is_peak).ffill()
    gap = idx.diff().rolling(252).mean()
    vel = gap.diff(5)
    return vel.diff(5)


def vosc_drv3_022_vosc_reversal_jerk(volume: pd.Series) -> pd.Series:
    pvo = 100 * _safe_div(volume.ewm(span=12).mean() - volume.ewm(span=26).mean(), volume.ewm(span=26).mean())
    vel = pvo.diff(5).diff(5)
    return vel.diff(5)


def vosc_drv3_023_vosc_peak_proximity_jerk(volume: pd.Series) -> pd.Series:
    pvo = 100 * _safe_div(volume.ewm(span=12).mean() - volume.ewm(span=26).mean(), volume.ewm(span=26).mean())
    idx = pvo.rolling(252).apply(np.argmax, raw=True)
    dsp = 252 - 1 - idx
    vel = dsp.diff(5)
    return vel.diff(5)


def vosc_drv3_024_cumulative_vosc_energy_jerk(volume: pd.Series) -> pd.Series:
    pvo = 100 * _safe_div(volume.ewm(span=12).mean() - volume.ewm(span=26).mean(), volume.ewm(span=26).mean())
    energy = pvo.cumsum() / (pvo.abs().cumsum() + _EPS)
    vel = energy.diff(5)
    return vel.diff(5)


def vosc_drv3_025_vosc_velocity_to_vol_jerk(volume: pd.Series) -> pd.Series:
    macd = _safe_div(volume.ewm(span=21).mean() - volume.ewm(span=63).mean(), volume.ewm(span=63).mean())
    v = macd.diff(5)
    vol = volume.pct_change().rolling(21).std()
    ratio = _safe_div(v, vol)
    vel = ratio.diff(5)
    return vel.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V23_A_REGISTRY = {
    "vosc_drv3_001_pvo_12_26_jerk": {"inputs": ["volume"], "func": vosc_drv3_001_pvo_12_26_jerk},
    "vosc_drv3_002_volume_macd_jerk": {"inputs": ["volume"], "func": vosc_drv3_002_volume_macd_jerk},
    "vosc_drv3_003_pvo_histogram_jerk": {"inputs": ["volume"], "func": vosc_drv3_003_pvo_histogram_jerk},
    "vosc_drv3_004_chaikin_oscillator_jerk": {"inputs": ["volume", "high", "low", "close"], "func": vosc_drv3_004_chaikin_oscillator_jerk},
    "vosc_drv3_005_volume_wave_intensity_jerk": {"inputs": ["volume"], "func": vosc_drv3_005_volume_wave_intensity_jerk},
    "vosc_drv3_006_vosc_stability_jerk": {"inputs": ["volume"], "func": vosc_drv3_006_vosc_stability_jerk},
    "vosc_drv3_007_vosc_regime_shift_jerk": {"inputs": ["volume"], "func": vosc_drv3_007_vosc_regime_shift_jerk},
    "vosc_drv3_008_vosc_climax_reversal_jerk": {"inputs": ["close", "volume", "low"], "func": vosc_drv3_008_vosc_climax_reversal_jerk},
    "vosc_drv3_009_vosc_momentum_div_jerk": {"inputs": ["volume"], "func": vosc_drv3_009_vosc_momentum_div_jerk},
    "vosc_drv3_010_joint_pv_osc_jerk": {"inputs": ["close", "volume"], "func": vosc_drv3_010_joint_pv_osc_jerk},
    "vosc_drv3_011_pvo_accel_jerk": {"inputs": ["volume"], "func": vosc_drv3_011_pvo_accel_jerk},
    "vosc_drv3_012_vosc_climax_intensity_jerk": {"inputs": ["close", "volume"], "func": vosc_drv3_012_vosc_climax_intensity_jerk},
    "vosc_drv3_013_vosc_exhaustion_jerk": {"inputs": ["close", "volume"], "func": vosc_drv3_013_vosc_exhaustion_jerk},
    "vosc_drv3_014_mktcap_vosc_jerk": {"inputs": ["close", "volume", "sharesbas"], "func": vosc_drv3_014_mktcap_vosc_jerk},
    "vosc_drv3_015_pvo_spread_short_long_jerk": {"inputs": ["volume"], "func": vosc_drv3_015_pvo_spread_short_long_jerk},
    "vosc_drv3_016_volume_jitter_jerk": {"inputs": ["volume"], "func": vosc_drv3_016_volume_jitter_jerk},
    "vosc_drv3_017_consecutive_vosc_inc_jerk": {"inputs": ["volume"], "func": vosc_drv3_017_consecutive_vosc_inc_jerk},
    "vosc_drv3_018_volume_wave_entropy_jerk": {"inputs": ["volume"], "func": vosc_drv3_018_volume_wave_entropy_jerk},
    "vosc_drv3_019_vosc_final_composite_jerk": {"inputs": ["close", "volume"], "func": vosc_drv3_019_vosc_final_composite_jerk},
    "vosc_drv3_020_turnover_vosc_jerk": {"inputs": ["volume", "sharesbas"], "func": vosc_drv3_020_turnover_vosc_jerk},
    "vosc_drv3_021_volume_cycle_period_jerk": {"inputs": ["volume"], "func": vosc_drv3_021_volume_cycle_period_jerk},
    "vosc_drv3_022_vosc_reversal_jerk": {"inputs": ["volume"], "func": vosc_drv3_022_vosc_reversal_jerk},
    "vosc_drv3_023_vosc_peak_proximity_jerk": {"inputs": ["volume"], "func": vosc_drv3_023_vosc_peak_proximity_jerk},
    "vosc_drv3_024_cumulative_vosc_energy_jerk": {"inputs": ["volume"], "func": vosc_drv3_024_cumulative_vosc_energy_jerk},
    "vosc_drv3_025_vosc_velocity_to_vol_jerk": {"inputs": ["volume"], "func": vosc_drv3_025_vosc_velocity_to_vol_jerk},
}
