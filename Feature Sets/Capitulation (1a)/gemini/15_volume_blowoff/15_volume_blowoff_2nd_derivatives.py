"""
15_volume_blowoff — 2nd Derivatives
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


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


# ── Feature functions ────────────────────────────────────────────────────────

# 25 features capturing acceleration of volume blowoff metrics
def vb_drv2_001_volume_spike_ratio_21d_velocity(volume: pd.Series) -> pd.Series:
    # Change in volume spike ratio
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    return v_rat.diff(5)


def vb_drv2_002_volume_zscore_252d_velocity(volume: pd.Series) -> pd.Series:
    v_avg = volume.rolling(252).mean()
    v_std = volume.rolling(252).std()
    z = (volume - v_avg) / v_std
    return z.diff(5)


def vb_drv2_003_volume_climax_intensity_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    ret = close.pct_change().abs()
    climax = v_rat * ret
    return climax.diff(5)


def vb_drv2_004_volume_acceleration_ratio_velocity(volume: pd.Series) -> pd.Series:
    # Rate of change of the volume acceleration ratio
    accel = _safe_div(_rolling_mean(volume, 5), _rolling_mean(volume, 21))
    return accel.diff(5)


def vb_drv2_005_dollar_volume_spike_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    dv_rat = _safe_div(dv, _rolling_median(dv, 63))
    return dv_rat.diff(5)


def vb_drv2_006_turnover_spike_velocity(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    to_rat = _safe_div(to, _rolling_median(to, 63))
    return to_rat.diff(5)


def vb_drv2_007_volume_cv_velocity(volume: pd.Series) -> pd.Series:
    cv = volume.rolling(63).std() / volume.rolling(63).mean()
    return cv.diff(5)


def vb_drv2_008_negative_volume_concentration_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    is_down = (close < close.shift(1))
    v_down = volume.where(is_down, 0).rolling(63).sum()
    v_total = volume.rolling(63).sum()
    conc = _safe_div(v_down, v_total)
    return conc.diff(5)


def vb_drv2_009_volume_climax_energy_velocity(volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 63))
    v_vol = volume.pct_change().rolling(21).std()
    energy = _safe_div(v_rat**2, v_vol)
    return energy.diff(5)


def vb_drv2_010_terminal_volume_flush_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    vs = _safe_div(volume, _rolling_median(volume, 63))
    is_down = (close < close.shift(1))
    streak = is_down.astype(int).groupby((is_down != is_down.shift()).cumsum()).cumsum()
    dist_h = (close.rolling(252).max() - close) / close.rolling(252).max()
    idx = vs * streak * dist_h
    return idx.diff(5)


def vb_drv2_011_volume_pct_rank_velocity(volume: pd.Series) -> pd.Series:
    rank = volume.expanding().rank(pct=True)
    return rank.diff(5)


def vb_drv2_012_volume_concentration_top5_velocity(volume: pd.Series) -> pd.Series:
    v_sort = volume.rolling(63).apply(lambda x: np.sort(x)[-5:].sum(), raw=True)
    v_total = volume.rolling(63).sum()
    conc = _safe_div(v_sort, v_total)
    return conc.diff(5)


def vb_drv2_013_mktcap_velocity_to_volume_velocity_accel(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    v_mc = np.log(close * sharesbas).diff(21)
    v_vol = np.log(volume + 1.0).diff(21)
    ratio = _safe_div(v_mc, v_vol)
    return ratio.diff(5)


def vb_drv2_014_volume_spike_freq_regime_velocity(volume: pd.Series) -> pd.Series:
    med = _rolling_median(volume, 252)
    is_spike = (volume > 2 * med).astype(int)
    f21 = is_spike.rolling(21).mean()
    f252 = is_spike.rolling(252).mean()
    rsi = _safe_div(f21, f252)
    return rsi.diff(5)


def vb_drv2_015_volume_trend_stability_velocity(volume: pd.Series) -> pd.Series:
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    r2 = volume.rolling(21).apply(_rsq, raw=True)
    return r2.diff(5)


def vb_drv2_016_volume_entropy_velocity(volume: pd.Series) -> pd.Series:
    def _ent(y):
        if len(y) == 0: return 0.0
        hist, _ = np.histogram(y, bins=10, density=True)
        p = hist[hist > 0]
        return -np.sum(p * np.log(p))
    e = volume.rolling(63).apply(_ent, raw=True)
    return e.diff(5)


def vb_drv2_017_cumulative_excess_volume_velocity(volume: pd.Series) -> pd.Series:
    med = _rolling_median(volume, 252)
    excess = (volume - med).clip(lower=0)
    ratio = _safe_div(excess.rolling(252).sum(), volume.rolling(252).sum())
    return ratio.diff(5)


def vb_drv2_018_volume_at_earnings_surprise_velocity(volume: pd.Series, surprise: pd.Series) -> pd.Series:
    ratio = _safe_div(volume, _rolling_median(volume, 63))
    val = ratio.where(surprise.abs() > 0).ffill()
    return val.diff(5)


def vb_drv2_019_mktcap_weighted_climax_velocity(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    v_spike = _safe_div(volume, _rolling_median(volume, 63))
    mc = close * sharesbas
    idx = v_spike * np.log(mc + _EPS)
    return idx.diff(5)


def vb_drv2_020_volume_oscillator_velocity(volume: pd.Series) -> pd.Series:
    v21 = volume.rolling(21).mean()
    v63 = volume.rolling(63).mean()
    osc = _safe_div(v21, v63) - 1.0
    return osc.diff(5)


def vb_drv2_021_volume_climax_decay_velocity(volume: pd.Series) -> pd.Series:
    ratio = _safe_div(volume, volume.rolling(63).max())
    return ratio.diff(5)


def vb_drv2_022_volume_to_range_expansion_velocity(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    v_spike = _safe_div(volume, _rolling_median(volume, 21))
    r = high - low
    r_spike = _safe_div(r, _rolling_median(r, 21))
    ratio = _safe_div(v_spike, r_spike)
    return ratio.diff(5)


def vb_drv2_023_vol_weighted_log_ret_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    lret = np.log(close / close.shift(1))
    v_norm = _safe_div(volume, volume.rolling(63).sum())
    vw_ret = (lret * v_norm).rolling(63).sum()
    return vw_ret.diff(5)


def vb_drv2_024_max_volume_spike_velocity(volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 63))
    mx = v_rat.rolling(63).max()
    return mx.diff(5)


def vb_drv2_025_volume_blowoff_composite_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vb_075_volume_blowoff_final_composite(close, volume)
    return score.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V15_V_REGISTRY = {
    "vb_drv2_001_volume_spike_ratio_21d_velocity": {"inputs": ["volume"], "func": vb_drv2_001_volume_spike_ratio_21d_velocity},
    "vb_drv2_002_volume_zscore_252d_velocity": {"inputs": ["volume"], "func": vb_drv2_002_volume_zscore_252d_velocity},
    "vb_drv2_003_volume_climax_intensity_velocity": {"inputs": ["close", "volume"], "func": vb_drv2_003_volume_climax_intensity_velocity},
    "vb_drv2_004_volume_acceleration_ratio_velocity": {"inputs": ["volume"], "func": vb_drv2_004_volume_acceleration_ratio_velocity},
    "vb_drv2_005_dollar_volume_spike_velocity": {"inputs": ["close", "volume"], "func": vb_drv2_005_dollar_volume_spike_velocity},
    "vb_drv2_006_turnover_spike_velocity": {"inputs": ["volume", "sharesbas"], "func": vb_drv2_006_turnover_spike_velocity},
    "vb_drv2_007_volume_cv_velocity": {"inputs": ["volume"], "func": vb_drv2_007_volume_cv_velocity},
    "vb_drv2_008_negative_volume_concentration_velocity": {"inputs": ["close", "volume"], "func": vb_drv2_008_negative_volume_concentration_velocity},
    "vb_drv2_009_volume_climax_energy_velocity": {"inputs": ["volume"], "func": vb_drv2_009_volume_climax_energy_velocity},
    "vb_drv2_010_terminal_volume_flush_velocity": {"inputs": ["close", "volume"], "func": vb_drv2_010_terminal_volume_flush_velocity},
    "vb_drv2_011_volume_pct_rank_velocity": {"inputs": ["volume"], "func": vb_drv2_011_volume_pct_rank_velocity},
    "vb_drv2_012_volume_concentration_top5_velocity": {"inputs": ["volume"], "func": vb_drv2_012_volume_concentration_top5_velocity},
    "vb_drv2_013_mktcap_velocity_to_volume_velocity_accel": {"inputs": ["close", "volume", "sharesbas"], "func": vb_drv2_013_mktcap_velocity_to_volume_velocity_accel},
    "vb_drv2_014_volume_spike_freq_regime_velocity": {"inputs": ["volume"], "func": vb_drv2_014_volume_spike_freq_regime_velocity},
    "vb_drv2_015_volume_trend_stability_velocity": {"inputs": ["volume"], "func": vb_drv2_015_volume_trend_stability_velocity},
    "vb_drv2_016_volume_entropy_velocity": {"inputs": ["volume"], "func": vb_drv2_016_volume_entropy_velocity},
    "vb_drv2_017_cumulative_excess_volume_velocity": {"inputs": ["volume"], "func": vb_drv2_017_cumulative_excess_volume_velocity},
    "vb_drv2_018_volume_at_earnings_surprise_velocity": {"inputs": ["volume", "surprise"], "func": vb_drv2_018_volume_at_earnings_surprise_velocity},
    "vb_drv2_019_mktcap_weighted_climax_velocity": {"inputs": ["close", "volume", "sharesbas"], "func": vb_drv2_019_mktcap_weighted_climax_velocity},
    "vb_drv2_020_volume_oscillator_velocity": {"inputs": ["volume"], "func": vb_drv2_020_volume_oscillator_velocity},
    "vb_drv2_021_volume_climax_decay_velocity": {"inputs": ["volume"], "func": vb_drv2_021_volume_climax_decay_velocity},
    "vb_drv2_022_volume_to_range_expansion_velocity": {"inputs": ["high", "low", "volume"], "func": vb_drv2_022_volume_to_range_expansion_velocity},
    "vb_drv2_023_vol_weighted_log_ret_velocity": {"inputs": ["close", "volume"], "func": vb_drv2_023_vol_weighted_log_ret_velocity},
    "vb_drv2_024_max_volume_spike_velocity": {"inputs": ["volume"], "func": vb_drv2_024_max_volume_spike_velocity},
    "vb_drv2_025_volume_blowoff_composite_velocity": {"inputs": ["close", "volume"], "func": vb_drv2_025_volume_blowoff_composite_velocity},
}
