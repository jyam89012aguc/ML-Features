"""
16_volume_persistence — 3rd Derivatives
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

# 25 features capturing exhaustion/inflection of volume persistence acceleration (jerk)
def vp_drv3_001_volume_persistence_21d_jerk(volume: pd.Series) -> pd.Series:
    v_per = _safe_div(_rolling_mean(volume, 21), _rolling_median(volume, 252))
    vel = v_per.diff(5)
    return vel.diff(5)


def vp_drv3_002_volume_persistence_zscore_jerk(volume: pd.Series) -> pd.Series:
    v21 = _rolling_mean(volume, 21)
    z = (v21 - v21.rolling(252).mean()) / (v21.rolling(252).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def vp_drv3_003_high_volume_days_jerk(volume: pd.Series) -> pd.Series:
    med = _rolling_median(volume, 252)
    cnt = (volume > 1.5 * med).rolling(63).sum()
    vel = cnt.diff(5)
    return vel.diff(5)


def vp_drv3_004_volume_integral_spread_jerk(volume: pd.Series) -> pd.Series:
    v21 = volume.rolling(21).sum() / 21.0
    v252 = volume.rolling(252).sum() / 252.0
    ratio = _safe_div(v21, v252)
    vel = ratio.diff(5)
    return vel.diff(5)


def vp_drv3_005_turnover_persistence_jerk(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    per = _safe_div(_rolling_mean(to, 21), _rolling_median(to, 252))
    vel = per.diff(5)
    return vel.diff(5)


def vp_drv3_006_volume_heavy_base_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_per = _safe_div(_rolling_mean(volume, 21), _rolling_median(volume, 252))
    r = close.rolling(21).max() - close.rolling(21).min()
    comp = v_per * _safe_div(close.rolling(21).mean(), r)
    vel = comp.diff(5)
    return vel.diff(5)


def vp_drv3_007_volume_absorption_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_sum = volume.rolling(63).sum()
    r_abs = (close / close.shift(63) - 1).abs()
    ratio = _safe_div(v_sum, r_abs)
    vel = ratio.diff(5)
    return vel.diff(5)


def vp_drv3_008_volume_persistence_decay_jerk(volume: pd.Series) -> pd.Series:
    v = _safe_div(_rolling_mean(volume, 5), _rolling_median(volume, 252))
    def _slope(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).slope
    sl = v.rolling(63).apply(_slope, raw=True)
    vel = sl.diff(5)
    return vel.diff(5)


def vp_drv3_009_mktcap_volume_persistence_jerk(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    v_p = _safe_div(_rolling_mean(volume, 21), _rolling_median(volume, 252))
    mc = close * sharesbas
    m_p = _safe_div(_rolling_mean(mc, 21), _rolling_median(mc, 252))
    ratio = _safe_div(v_p, m_p)
    vel = ratio.diff(5)
    return vel.diff(5)


def vp_drv3_010_volume_floor_stability_jerk(volume: pd.Series) -> pd.Series:
    l21 = volume.rolling(21).min()
    score = _safe_div(1.0, l21.rolling(63).std() / (l21.rolling(63).mean() + _EPS))
    vel = score.diff(5)
    return vel.diff(5)


def vp_drv3_011_volume_to_price_persistence_div_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    vp = _safe_div(_rolling_mean(volume, 21), _rolling_median(volume, 252)).diff(21)
    pp = (close / close.shift(21) - 1).diff(21)
    div = vp - pp
    vel = div.diff(5)
    return vel.diff(5)


def vp_drv3_012_volume_integral_accel_jerk(volume: pd.Series) -> pd.Series:
    vi = volume.cumsum()
    acc = vi.diff(21).diff(21)
    vel = acc.diff(5)
    return vel.diff(5)


def vp_drv3_013_sustained_turnover_climax_jerk(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    per = _safe_div(_rolling_mean(to, 21), _rolling_median(to, 252))
    score = to * per
    vel = score.diff(5)
    return vel.diff(5)


def vp_drv3_014_volume_regime_stability_jerk(volume: pd.Series) -> pd.Series:
    v21 = _rolling_mean(volume, 21)
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    r2 = v21.rolling(63).apply(_rsq, raw=True)
    vel = r2.diff(5)
    return vel.diff(5)


def vp_drv3_015_sustained_high_volume_episode_jerk(volume: pd.Series) -> pd.Series:
    med = _rolling_median(volume, 252)
    is_high = (volume > 2 * med).astype(int)
    streak = is_high.groupby((is_high == 0).cumsum()).cumsum()
    cnt = (streak == 5).astype(int).rolling(252).sum()
    vel = cnt.diff(5)
    return vel.diff(5)


def vp_drv3_016_volume_integral_decay_jerk(volume: pd.Series) -> pd.Series:
    w = np.exp(-np.arange(252) / 63.0)[::-1]
    id = volume.rolling(252).apply(lambda x: np.sum(x * w), raw=True)
    vel = id.diff(5)
    return vel.diff(5)


def vp_drv3_017_heavy_selling_persistence_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    per = _safe_div(_rolling_mean(volume, 21), _rolling_median(volume, 252))
    dn_cnt = (close < close.shift(1)).astype(int).rolling(63).sum()
    idx = per * dn_cnt
    vel = idx.diff(5)
    return vel.diff(5)


def vp_drv3_018_volume_base_formation_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    per = _safe_div(_rolling_mean(volume, 21), _rolling_median(volume, 252))
    r = (close.rolling(63).max() - close.rolling(63).min()) / (close.rolling(63).mean() + _EPS)
    score = _safe_div(per, r + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def vp_drv3_019_sustained_climax_to_vol_jerk(volume: pd.Series) -> pd.Series:
    v_per = _safe_div(_rolling_mean(volume, 21), _rolling_median(volume, 252))
    v_vol = volume.pct_change().rolling(63).std()
    ratio = _safe_div(v_per, v_vol)
    vel = ratio.diff(5)
    return vel.diff(5)


def vp_drv3_020_volume_persistence_final_climax_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vp_150_volume_persistence_final_climax_index(close, volume)
    vel = score.diff(5)
    return vel.diff(5)


def vp_drv3_021_consecutive_volume_gt_median_jerk(volume: pd.Series) -> pd.Series:
    med = _rolling_median(volume, 252)
    above = (volume > med).astype(int)
    dur = above.groupby((above == 0).cumsum()).cumsum()
    vel = dur.diff(5)
    return vel.diff(5)


def vp_drv3_022_cumulative_excess_turnover_jerk(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    med = to.expanding().median()
    excess = (to - med).clip(lower=0).cumsum()
    vel = excess.diff(5)
    return vel.diff(5)


def vp_drv3_023_volume_persistence_regime_break_jerk(volume: pd.Series) -> pd.Series:
    p5 = _safe_div(_rolling_mean(volume, 5), _rolling_median(volume, 252))
    p63 = _safe_div(_rolling_mean(volume, 63), _rolling_median(volume, 252))
    break_val = p5 - p63
    vel = break_val.diff(5)
    return vel.diff(5)


def vp_drv3_024_inst_holder_persistence_jerk(inst_holders: pd.Series) -> pd.Series:
    score = _safe_div(_rolling_mean(inst_holders, 4), _rolling_std(inst_holders, 4) + _EPS)
    vel = score.diff(1)
    return vel.diff(1)


def vp_drv3_025_volume_persistence_composite_jerk(volume: pd.Series) -> pd.Series:
    p5 = _safe_div(_rolling_mean(volume, 5), _rolling_median(volume, 252))
    p21 = _safe_div(_rolling_mean(volume, 21), _rolling_median(volume, 252))
    p63 = _safe_div(_rolling_mean(volume, 63), _rolling_median(volume, 252))
    comp = (0.5 * p5 + 0.3 * p21 + 0.2 * p63)
    vel = comp.diff(5)
    return vel.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V16_A_REGISTRY = {
    "vp_drv3_001_volume_persistence_21d_jerk": {"inputs": ["volume"], "func": vp_drv3_001_volume_persistence_21d_jerk},
    "vp_drv3_002_volume_persistence_zscore_jerk": {"inputs": ["volume"], "func": vp_drv3_002_volume_persistence_zscore_jerk},
    "vp_drv3_003_high_volume_days_jerk": {"inputs": ["volume"], "func": vp_drv3_003_high_volume_days_jerk},
    "vp_drv3_004_volume_integral_spread_jerk": {"inputs": ["volume"], "func": vp_drv3_004_volume_integral_spread_jerk},
    "vp_drv3_005_turnover_persistence_jerk": {"inputs": ["volume", "sharesbas"], "func": vp_drv3_005_turnover_persistence_jerk},
    "vp_drv3_006_volume_heavy_base_jerk": {"inputs": ["close", "volume"], "func": vp_drv3_006_volume_heavy_base_jerk},
    "vp_drv3_007_volume_absorption_jerk": {"inputs": ["close", "volume"], "func": vp_drv3_007_volume_absorption_jerk},
    "vp_drv3_008_volume_persistence_decay_jerk": {"inputs": ["volume"], "func": vp_drv3_008_volume_persistence_decay_jerk},
    "vp_drv3_009_mktcap_volume_persistence_jerk": {"inputs": ["close", "volume", "sharesbas"], "func": vp_drv3_009_mktcap_volume_persistence_jerk},
    "vp_drv3_010_volume_floor_stability_jerk": {"inputs": ["volume"], "func": vp_drv3_010_volume_floor_stability_jerk},
    "vp_drv3_011_volume_to_price_persistence_div_jerk": {"inputs": ["close", "volume"], "func": vp_drv3_011_volume_to_price_persistence_div_jerk},
    "vp_drv3_012_volume_integral_accel_jerk": {"inputs": ["volume"], "func": vp_drv3_012_volume_integral_accel_jerk},
    "vp_drv3_013_sustained_turnover_climax_jerk": {"inputs": ["volume", "sharesbas"], "func": vp_drv3_013_sustained_turnover_climax_jerk},
    "vp_drv3_014_volume_regime_stability_jerk": {"inputs": ["volume"], "func": vp_drv3_014_volume_regime_stability_jerk},
    "vp_drv3_015_sustained_high_volume_episode_jerk": {"inputs": ["volume"], "func": vp_drv3_015_sustained_high_volume_episode_jerk},
    "vp_drv3_016_volume_integral_decay_jerk": {"inputs": ["volume"], "func": vp_drv3_016_volume_integral_decay_jerk},
    "vp_drv3_017_heavy_selling_persistence_jerk": {"inputs": ["close", "volume"], "func": vp_drv3_017_heavy_selling_persistence_jerk},
    "vp_drv3_018_volume_base_formation_jerk": {"inputs": ["close", "volume"], "func": vp_drv3_018_volume_base_formation_jerk},
    "vp_drv3_019_sustained_climax_to_vol_jerk": {"inputs": ["volume"], "func": vp_drv3_019_sustained_climax_to_vol_jerk},
    "vp_drv3_020_volume_persistence_final_climax_jerk": {"inputs": ["close", "volume"], "func": vp_drv3_020_volume_persistence_final_climax_jerk},
    "vp_drv3_021_consecutive_volume_gt_median_jerk": {"inputs": ["volume"], "func": vp_drv3_021_consecutive_volume_gt_median_jerk},
    "vp_drv3_022_cumulative_excess_turnover_jerk": {"inputs": ["volume", "sharesbas"], "func": vp_drv3_022_cumulative_excess_turnover_jerk},
    "vp_drv3_023_volume_persistence_regime_break_jerk": {"inputs": ["volume"], "func": vp_drv3_023_volume_persistence_regime_break_jerk},
    "vp_drv3_024_inst_holder_persistence_jerk": {"inputs": ["inst_holders"], "func": vp_drv3_024_inst_holder_persistence_jerk},
    "vp_drv3_025_volume_persistence_composite_jerk": {"inputs": ["volume"], "func": vp_drv3_025_volume_persistence_composite_jerk},
}
