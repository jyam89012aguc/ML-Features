"""
16_volume_persistence — 2nd Derivatives
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

# 25 features capturing acceleration of volume persistence metrics
def vp_drv2_001_volume_persistence_21d_velocity(volume: pd.Series) -> pd.Series:
    v_per = _safe_div(_rolling_mean(volume, 21), _rolling_median(volume, 252))
    return v_per.diff(5)


def vp_drv2_002_volume_persistence_zscore_velocity(volume: pd.Series) -> pd.Series:
    v21 = _rolling_mean(volume, 21)
    z = (v21 - v21.rolling(252).mean()) / v21.rolling(252).std()
    return z.diff(5)


def vp_drv2_003_high_volume_days_velocity(volume: pd.Series) -> pd.Series:
    med = _rolling_median(volume, 252)
    cnt = (volume > 1.5 * med).rolling(63).sum()
    return cnt.diff(5)


def vp_drv2_004_volume_integral_spread_velocity(volume: pd.Series) -> pd.Series:
    v21 = volume.rolling(21).sum() / 21.0
    v252 = volume.rolling(252).sum() / 252.0
    ratio = _safe_div(v21, v252)
    return ratio.diff(5)


def vp_drv2_005_turnover_persistence_velocity(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    per = _safe_div(_rolling_mean(to, 21), _rolling_median(to, 252))
    return per.diff(5)


def vp_drv2_006_volume_heavy_base_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_per = _safe_div(_rolling_mean(volume, 21), _rolling_median(volume, 252))
    r = close.rolling(21).max() - close.rolling(21).min()
    comp = v_per * _safe_div(close.rolling(21).mean(), r)
    return comp.diff(5)


def vp_drv2_007_volume_absorption_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_sum = volume.rolling(63).sum()
    r_abs = (close / close.shift(63) - 1).abs()
    ratio = _safe_div(v_sum, r_abs)
    return ratio.diff(5)


def vp_drv2_008_volume_persistence_decay_velocity(volume: pd.Series) -> pd.Series:
    v = _safe_div(_rolling_mean(volume, 5), _rolling_median(volume, 252))
    def _slope(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).slope
    sl = v.rolling(63).apply(_slope, raw=True)
    return sl.diff(5)


def vp_drv2_009_mktcap_volume_persistence_velocity(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    v_p = _safe_div(_rolling_mean(volume, 21), _rolling_median(volume, 252))
    mc = close * sharesbas
    m_p = _safe_div(_rolling_mean(mc, 21), _rolling_median(mc, 252))
    ratio = _safe_div(v_p, m_p)
    return ratio.diff(5)


def vp_drv2_010_volume_floor_stability_velocity(volume: pd.Series) -> pd.Series:
    l21 = volume.rolling(21).min()
    score = _safe_div(1.0, l21.rolling(63).std() / l21.rolling(63).mean())
    return score.diff(5)


def vp_drv2_011_volume_to_price_persistence_div_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    vp = _safe_div(_rolling_mean(volume, 21), _rolling_median(volume, 252)).diff(21)
    pp = (close / close.shift(21) - 1).diff(21)
    div = vp - pp
    return div.diff(5)


def vp_drv2_012_volume_integral_accel_velocity(volume: pd.Series) -> pd.Series:
    vi = volume.cumsum()
    acc = vi.diff(21).diff(21)
    return acc.diff(5)


def vp_drv2_013_sustained_turnover_climax_velocity(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    per = _safe_div(_rolling_mean(to, 21), _rolling_median(to, 252))
    score = to * per
    return score.diff(5)


def vp_drv2_014_volume_regime_stability_velocity(volume: pd.Series) -> pd.Series:
    v21 = _rolling_mean(volume, 21)
    def _rsq(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    r2 = v21.rolling(63).apply(_rsq, raw=True)
    return r2.diff(5)


def vp_drv2_015_sustained_high_volume_episode_velocity(volume: pd.Series) -> pd.Series:
    med = _rolling_median(volume, 252)
    is_high = (volume > 2 * med).astype(int)
    streak = is_high.groupby((is_high == 0).cumsum()).cumsum()
    cnt = (streak == 5).astype(int).rolling(252).sum()
    return cnt.diff(5)


def vp_drv2_016_volume_integral_decay_velocity(volume: pd.Series) -> pd.Series:
    w = np.exp(-np.arange(252) / 63.0)[::-1]
    id = volume.rolling(252).apply(lambda x: np.sum(x * w), raw=True)
    return id.diff(5)


def vp_drv2_017_heavy_selling_persistence_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    per = _safe_div(_rolling_mean(volume, 21), _rolling_median(volume, 252))
    dn_cnt = (close < close.shift(1)).astype(int).rolling(63).sum()
    idx = per * dn_cnt
    return idx.diff(5)


def vp_drv2_018_volume_base_formation_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    per = _safe_div(_rolling_mean(volume, 21), _rolling_median(volume, 252))
    r = (close.rolling(63).max() - close.rolling(63).min()) / close.rolling(63).mean()
    score = _safe_div(per, r + _EPS)
    return score.diff(5)


def vp_drv2_019_sustained_climax_to_vol_velocity(volume: pd.Series) -> pd.Series:
    v_per = _safe_div(_rolling_mean(volume, 21), _rolling_median(volume, 252))
    v_vol = volume.pct_change().rolling(63).std()
    ratio = _safe_div(v_per, v_vol)
    return ratio.diff(5)


def vp_drv2_020_volume_persistence_final_climax_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vp_150_volume_persistence_final_climax_index(close, volume)
    return score.diff(5)


def vp_drv2_021_consecutive_volume_gt_median_velocity(volume: pd.Series) -> pd.Series:
    med = _rolling_median(volume, 252)
    above = (volume > med).astype(int)
    dur = above.groupby((above == 0).cumsum()).cumsum()
    return dur.diff(5)


def vp_drv2_022_cumulative_excess_turnover_velocity(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    med = to.expanding().median()
    excess = (to - med).clip(lower=0).cumsum()
    return excess.diff(5)


def vp_drv2_023_volume_persistence_regime_break_velocity(volume: pd.Series) -> pd.Series:
    p5 = _safe_div(_rolling_mean(volume, 5), _rolling_median(volume, 252))
    p63 = _safe_div(_rolling_mean(volume, 63), _rolling_median(volume, 252))
    break_val = p5 - p63
    return break_val.diff(5)


def vp_drv2_024_inst_holder_persistence_velocity(inst_holders: pd.Series) -> pd.Series:
    score = _safe_div(_rolling_mean(inst_holders, 4), _rolling_std(inst_holders, 4))
    return score.diff(1)


def vp_drv2_025_volume_persistence_composite_velocity(volume: pd.Series) -> pd.Series:
    p5 = _safe_div(_rolling_mean(volume, 5), _rolling_median(volume, 252))
    p21 = _safe_div(_rolling_mean(volume, 21), _rolling_median(volume, 252))
    p63 = _safe_div(_rolling_mean(volume, 63), _rolling_median(volume, 252))
    comp = (0.5 * p5 + 0.3 * p21 + 0.2 * p63)
    return comp.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V16_V_REGISTRY = {
    "vp_drv2_001_volume_persistence_21d_velocity": {"inputs": ["volume"], "func": vp_drv2_001_volume_persistence_21d_velocity},
    "vp_drv2_002_volume_persistence_zscore_velocity": {"inputs": ["volume"], "func": vp_drv2_002_volume_persistence_zscore_velocity},
    "vp_drv2_003_high_volume_days_velocity": {"inputs": ["volume"], "func": vp_drv2_003_high_volume_days_velocity},
    "vp_drv2_004_volume_integral_spread_velocity": {"inputs": ["volume"], "func": vp_drv2_004_volume_integral_spread_velocity},
    "vp_drv2_005_turnover_persistence_velocity": {"inputs": ["volume", "sharesbas"], "func": vp_drv2_005_turnover_persistence_velocity},
    "vp_drv2_006_volume_heavy_base_velocity": {"inputs": ["close", "volume"], "func": vp_drv2_006_volume_heavy_base_velocity},
    "vp_drv2_007_volume_absorption_velocity": {"inputs": ["close", "volume"], "func": vp_drv2_007_volume_absorption_velocity},
    "vp_drv2_008_volume_persistence_decay_velocity": {"inputs": ["volume"], "func": vp_drv2_008_volume_persistence_decay_velocity},
    "vp_drv2_009_mktcap_volume_persistence_velocity": {"inputs": ["close", "volume", "sharesbas"], "func": vp_drv2_009_mktcap_volume_persistence_velocity},
    "vp_drv2_010_volume_floor_stability_velocity": {"inputs": ["volume"], "func": vp_drv2_010_volume_floor_stability_velocity},
    "vp_drv2_011_volume_to_price_persistence_div_velocity": {"inputs": ["close", "volume"], "func": vp_drv2_011_volume_to_price_persistence_div_velocity},
    "vp_drv2_012_volume_integral_accel_velocity": {"inputs": ["volume"], "func": vp_drv2_012_volume_integral_accel_velocity},
    "vp_drv2_013_sustained_turnover_climax_velocity": {"inputs": ["volume", "sharesbas"], "func": vp_drv2_013_sustained_turnover_climax_velocity},
    "vp_drv2_014_volume_regime_stability_velocity": {"inputs": ["volume"], "func": vp_drv2_014_volume_regime_stability_velocity},
    "vp_drv2_015_sustained_high_volume_episode_velocity": {"inputs": ["volume"], "func": vp_drv2_015_sustained_high_volume_episode_velocity},
    "vp_drv2_016_volume_integral_decay_velocity": {"inputs": ["volume"], "func": vp_drv2_016_volume_integral_decay_velocity},
    "vp_drv2_017_heavy_selling_persistence_velocity": {"inputs": ["close", "volume"], "func": vp_drv2_017_heavy_selling_persistence_velocity},
    "vp_drv2_018_volume_base_formation_velocity": {"inputs": ["close", "volume"], "func": vp_drv2_018_volume_base_formation_velocity},
    "vp_drv2_019_sustained_climax_to_vol_velocity": {"inputs": ["volume"], "func": vp_drv2_019_sustained_climax_to_vol_velocity},
    "vp_drv2_020_volume_persistence_final_climax_velocity": {"inputs": ["close", "volume"], "func": vp_drv2_020_volume_persistence_final_climax_velocity},
    "vp_drv2_021_consecutive_volume_gt_median_velocity": {"inputs": ["volume"], "func": vp_drv2_021_consecutive_volume_gt_median_velocity},
    "vp_drv2_022_cumulative_excess_turnover_velocity": {"inputs": ["volume", "sharesbas"], "func": vp_drv2_022_cumulative_excess_turnover_velocity},
    "vp_drv2_023_volume_persistence_regime_break_velocity": {"inputs": ["volume"], "func": vp_drv2_023_volume_persistence_regime_break_velocity},
    "vp_drv2_024_inst_holder_persistence_velocity": {"inputs": ["inst_holders"], "func": vp_drv2_024_inst_holder_persistence_velocity},
    "vp_drv2_025_volume_persistence_composite_velocity": {"inputs": ["volume"], "func": vp_drv2_025_volume_persistence_composite_velocity},
}
