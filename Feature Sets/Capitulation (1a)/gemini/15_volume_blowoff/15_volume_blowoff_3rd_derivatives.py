"""
15_volume_blowoff — 3rd Derivatives
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


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


# ── Feature functions ────────────────────────────────────────────────────────

# 25 features capturing exhaustion/inflection of volume blowoff acceleration (jerk)
def vb_drv3_001_volume_spike_ratio_21d_jerk(volume: pd.Series) -> pd.Series:
    # Rate of change of volume spike ratio velocity
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    vel = v_rat.diff(5)
    return vel.diff(5)


def vb_drv3_002_volume_zscore_252d_jerk(volume: pd.Series) -> pd.Series:
    v_avg = volume.rolling(252).mean()
    v_std = volume.rolling(252).std()
    z = (volume - v_avg) / (v_std + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def vb_drv3_003_volume_climax_intensity_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    ret = close.pct_change().abs()
    climax = v_rat * ret
    vel = climax.diff(5)
    return vel.diff(5)


def vb_drv3_004_volume_acceleration_ratio_jerk(volume: pd.Series) -> pd.Series:
    accel = _safe_div(_rolling_mean(volume, 5), _rolling_mean(volume, 21))
    vel = accel.diff(5)
    return vel.diff(5)


def vb_drv3_005_dollar_volume_spike_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    dv_rat = _safe_div(dv, _rolling_median(dv, 63))
    vel = dv_rat.diff(5)
    return vel.diff(5)


def vb_drv3_006_turnover_spike_jerk(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    to_rat = _safe_div(to, _rolling_median(to, 63))
    vel = to_rat.diff(5)
    return vel.diff(5)


def vb_drv3_007_volume_cv_jerk(volume: pd.Series) -> pd.Series:
    cv = volume.rolling(63).std() / (volume.rolling(63).mean() + _EPS)
    vel = cv.diff(5)
    return vel.diff(5)


def vb_drv3_008_negative_volume_concentration_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    is_down = (close < close.shift(1))
    v_down = volume.where(is_down, 0).rolling(63).sum()
    v_total = volume.rolling(63).sum()
    conc = _safe_div(v_down, v_total)
    vel = conc.diff(5)
    return vel.diff(5)


def vb_drv3_009_volume_climax_energy_jerk(volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 63))
    v_vol = volume.pct_change().rolling(21).std()
    energy = _safe_div(v_rat**2, v_vol)
    vel = energy.diff(5)
    return vel.diff(5)


def vb_drv3_010_terminal_volume_flush_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    vs = _safe_div(volume, _rolling_median(volume, 63))
    is_down = (close < close.shift(1))
    streak = is_down.astype(int).groupby((is_down != is_down.shift()).cumsum()).cumsum()
    dist_h = (close.rolling(252).max() - close) / (close.rolling(252).max() + _EPS)
    idx = vs * streak * dist_h
    vel = idx.diff(5)
    return vel.diff(5)


def vb_drv3_011_volume_pct_rank_jerk(volume: pd.Series) -> pd.Series:
    rank = volume.expanding().rank(pct=True)
    vel = rank.diff(5)
    return vel.diff(5)


def vb_drv3_012_volume_concentration_top5_jerk(volume: pd.Series) -> pd.Series:
    v_sort = volume.rolling(63).apply(lambda x: np.sort(x)[-5:].sum(), raw=True)
    v_total = volume.rolling(63).sum()
    conc = _safe_div(v_sort, v_total)
    vel = conc.diff(5)
    return vel.diff(5)


def vb_drv3_013_mktcap_velocity_to_volume_velocity_jerk(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    v_mc = np.log(close * sharesbas).diff(21)
    v_vol = np.log(volume + 1.0).diff(21)
    ratio = _safe_div(v_mc, v_vol)
    vel = ratio.diff(5)
    return vel.diff(5)


def vb_drv3_014_volume_spike_freq_regime_jerk(volume: pd.Series) -> pd.Series:
    med = _rolling_median(volume, 252)
    is_spike = (volume > 2 * med).astype(int)
    f21 = is_spike.rolling(21).mean()
    f252 = is_spike.rolling(252).mean()
    rsi = _safe_div(f21, f252)
    vel = rsi.diff(5)
    return vel.diff(5)


def vb_drv3_015_volume_trend_stability_jerk(volume: pd.Series) -> pd.Series:
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    r2 = volume.rolling(21).apply(_rsq, raw=True)
    vel = r2.diff(5)
    return vel.diff(5)


def vb_drv3_016_volume_entropy_jerk(volume: pd.Series) -> pd.Series:
    def _ent(y):
        if len(y) == 0: return 0.0
        hist, _ = np.histogram(y, bins=10, density=True)
        p = hist[hist > 0]
        return -np.sum(p * np.log(p))
    e = volume.rolling(63).apply(_ent, raw=True)
    vel = e.diff(5)
    return vel.diff(5)


def vb_drv3_017_cumulative_excess_volume_jerk(volume: pd.Series) -> pd.Series:
    med = _rolling_median(volume, 252)
    excess = (volume - med).clip(lower=0)
    ratio = _safe_div(excess.rolling(252).sum(), volume.rolling(252).sum())
    vel = ratio.diff(5)
    return vel.diff(5)


def vb_drv3_018_volume_at_earnings_surprise_jerk(volume: pd.Series, surprise: pd.Series) -> pd.Series:
    ratio = _safe_div(volume, _rolling_median(volume, 63))
    val = ratio.where(surprise.abs() > 0).ffill()
    vel = val.diff(5)
    return vel.diff(5)


def vb_drv3_019_mktcap_weighted_climax_jerk(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    v_spike = _safe_div(volume, _rolling_median(volume, 63))
    mc = close * sharesbas
    idx = v_spike * np.log(mc + _EPS)
    vel = idx.diff(5)
    return vel.diff(5)


def vb_drv3_020_volume_oscillator_jerk(volume: pd.Series) -> pd.Series:
    v21 = volume.rolling(21).mean()
    v63 = volume.rolling(63).mean()
    osc = _safe_div(v21, v63) - 1.0
    vel = osc.diff(5)
    return vel.diff(5)


def vb_drv3_021_volume_climax_decay_jerk(volume: pd.Series) -> pd.Series:
    ratio = _safe_div(volume, volume.rolling(63).max())
    vel = ratio.diff(5)
    return vel.diff(5)


def vb_drv3_022_volume_to_range_expansion_jerk(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    v_spike = _safe_div(volume, _rolling_median(volume, 21))
    r = high - low
    r_spike = _safe_div(r, _rolling_median(r, 21))
    ratio = _safe_div(v_spike, r_spike)
    vel = ratio.diff(5)
    return vel.diff(5)


def vb_drv3_023_vol_weighted_log_ret_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    lret = np.log(close / close.shift(1))
    v_norm = _safe_div(volume, volume.rolling(63).sum())
    vw_ret = (lret * v_norm).rolling(63).sum()
    vel = vw_ret.diff(5)
    return vel.diff(5)


def vb_drv3_024_max_volume_spike_jerk(volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 63))
    mx = v_rat.rolling(63).max()
    vel = mx.diff(5)
    return vel.diff(5)


def vb_drv3_025_volume_blowoff_composite_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vb_075_volume_blowoff_final_composite(close, volume)
    vel = score.diff(5)
    return vel.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V15_A_REGISTRY = {
    "vb_drv3_001_volume_spike_ratio_21d_jerk": {"inputs": ["volume"], "func": vb_drv3_001_volume_spike_ratio_21d_jerk},
    "vb_drv3_002_volume_zscore_252d_jerk": {"inputs": ["volume"], "func": vb_drv3_002_volume_zscore_252d_jerk},
    "vb_drv3_003_volume_climax_intensity_jerk": {"inputs": ["close", "volume"], "func": vb_drv3_003_volume_climax_intensity_jerk},
    "vb_drv3_004_volume_acceleration_ratio_jerk": {"inputs": ["volume"], "func": vb_drv3_004_volume_acceleration_ratio_jerk},
    "vb_drv3_005_dollar_volume_spike_jerk": {"inputs": ["close", "volume"], "func": vb_drv3_005_dollar_volume_spike_jerk},
    "vb_drv3_006_turnover_spike_jerk": {"inputs": ["volume", "sharesbas"], "func": vb_drv3_006_turnover_spike_jerk},
    "vb_drv3_007_volume_cv_jerk": {"inputs": ["volume"], "func": vb_drv3_007_volume_cv_jerk},
    "vb_drv3_008_negative_volume_concentration_jerk": {"inputs": ["close", "volume"], "func": vb_drv3_008_negative_volume_concentration_jerk},
    "vb_drv3_009_volume_climax_energy_jerk": {"inputs": ["volume"], "func": vb_drv3_009_volume_climax_energy_jerk},
    "vb_drv3_010_terminal_volume_flush_jerk": {"inputs": ["close", "volume"], "func": vb_drv3_010_terminal_volume_flush_jerk},
    "vb_drv3_011_volume_pct_rank_jerk": {"inputs": ["volume"], "func": vb_drv3_011_volume_pct_rank_jerk},
    "vb_drv3_012_volume_concentration_top5_jerk": {"inputs": ["volume"], "func": vb_drv3_012_volume_concentration_top5_jerk},
    "vb_drv3_013_mktcap_velocity_to_volume_velocity_jerk": {"inputs": ["close", "volume", "sharesbas"], "func": vb_drv3_013_mktcap_velocity_to_volume_velocity_jerk},
    "vb_drv3_014_volume_spike_freq_regime_jerk": {"inputs": ["volume"], "func": vb_drv3_014_volume_spike_freq_regime_jerk},
    "vb_drv3_015_volume_trend_stability_jerk": {"inputs": ["volume"], "func": vb_drv3_015_volume_trend_stability_jerk},
    "vb_drv3_016_volume_entropy_jerk": {"inputs": ["volume"], "func": vb_drv3_016_volume_entropy_jerk},
    "vb_drv3_017_cumulative_excess_volume_jerk": {"inputs": ["volume"], "func": vb_drv3_017_cumulative_excess_volume_jerk},
    "vb_drv3_018_volume_at_earnings_surprise_jerk": {"inputs": ["volume", "surprise"], "func": vb_drv3_018_volume_at_earnings_surprise_jerk},
    "vb_drv3_019_mktcap_weighted_climax_jerk": {"inputs": ["close", "volume", "sharesbas"], "func": vb_drv3_019_mktcap_weighted_climax_jerk},
    "vb_drv3_020_volume_oscillator_jerk": {"inputs": ["volume"], "func": vb_drv3_020_volume_oscillator_jerk},
    "vb_drv3_021_volume_climax_decay_jerk": {"inputs": ["volume"], "func": vb_drv3_021_volume_climax_decay_jerk},
    "vb_drv3_022_volume_to_range_expansion_jerk": {"inputs": ["high", "low", "volume"], "func": vb_drv3_022_volume_to_range_expansion_jerk},
    "vb_drv3_023_vol_weighted_log_ret_jerk": {"inputs": ["close", "volume"], "func": vb_drv3_023_vol_weighted_log_ret_jerk},
    "vb_drv3_024_max_volume_spike_jerk": {"inputs": ["volume"], "func": vb_drv3_024_max_volume_spike_jerk},
    "vb_drv3_025_volume_blowoff_composite_jerk": {"inputs": ["close", "volume"], "func": vb_drv3_025_volume_blowoff_composite_jerk},
}
