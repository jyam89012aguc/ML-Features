"""
22_volume_price_divergence — 2nd Derivatives
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


# ── Feature functions ────────────────────────────────────────────────────────

# 25 features capturing acceleration of volume-price divergence metrics
def vpd_drv2_001_vp_divergence_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    # Rate of change of the volume-price divergence intensity
    v_roc = volume.pct_change(5)
    p_roc = close.pct_change(5)
    div = (v_roc - p_roc).rolling(21).mean()
    return div.diff(5)


def vpd_drv2_002_absorption_ratio_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    v_rat = _safe_div(volume, _rolling_median(volume, 63))
    absorp = _safe_div(v_rat, ret.abs() + _EPS).where(ret < 0, 0).rolling(21).mean()
    return absorp.diff(5)


def vpd_drv2_003_volume_price_corr_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    c = close.rolling(21).corr(volume)
    return c.diff(5)


def vpd_drv2_004_obv_price_div_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.diff()
    obv = (np.sign(ret) * volume).cumsum()
    div = (obv / obv.expanding().max()) - (close / close.expanding().max())
    return div.diff(5)


def vpd_drv2_005_climax_to_range_div_velocity(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    r_rat = _safe_div(high - low, _rolling_median(high - low, 21))
    ratio = _safe_div(v_rat, r_rat)
    return ratio.diff(5)


def vpd_drv2_006_supply_surge_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    is_down = (close < close.shift(1))
    v_dn_pers = volume.where(is_down, 0).rolling(63).mean() / _rolling_median(volume, 252)
    l = close.rolling(252).min()
    score = v_dn_pers * (1.0 / _safe_div(close, l))
    return score.diff(5)


def vpd_drv2_007_demand_exhaustion_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    p_vel = np.log(close).diff(5).abs()
    v_up_rat = _safe_div(volume.where(close > close.shift(1), 0).rolling(21).mean(), volume.rolling(252).median())
    score = _safe_div(p_vel, v_up_rat + _EPS)
    return score.diff(5)


def vpd_drv2_008_vp_entropy_div_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y, bins=10, density=True)
        p = h[h > 0]
        return -np.sum(p * np.log(p))
    ve = volume.rolling(63).apply(_ent, raw=True)
    re = close.pct_change().rolling(63).apply(_ent, raw=True)
    return (ve - re).diff(5)


def vpd_drv2_009_climax_reversal_div_velocity(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 63))
    wick = _safe_div(close - low, high - low)
    score = (v_rat * (1.0 - wick)).where(close < close.shift(1), 0)
    return score.diff(5)


def vpd_drv2_010_vw_path_divergence_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_norm = _safe_div(volume, volume.rolling(63).sum())
    vw_lp = (np.log(close) * v_norm).rolling(63).sum()
    avg_lp = np.log(close).rolling(63).mean()
    return (vw_lp - avg_lp).diff(5)


def vpd_drv2_011_turnover_to_ret_accel_velocity(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    v_accel = volume.pct_change(5).diff(5)
    p_accel = close.pct_change(5).diff(5)
    ratio = _safe_div(v_accel, p_accel.abs() + _EPS)
    return ratio.diff(5)


def vpd_drv2_012_rejection_climax_velocity(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    h_rat = _safe_div(high - close, close)
    v_rat = _safe_div(volume, _rolling_median(volume, 63))
    return (h_rat * v_rat).diff(5)


def vpd_drv2_013_mktcap_vp_drift_div_velocity(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    m_drift = mc.diff(63) / mc.shift(63)
    v_drift = volume.rolling(21).mean().diff(63) / (volume.rolling(21).mean().shift(63) + _EPS)
    return (v_drift - m_drift).diff(5)


def vpd_drv2_014_volume_per_unit_dd_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume.rolling(63).mean(), _rolling_median(volume, 252))
    h = close.rolling(252).max()
    dd = (h - close) / h
    return _safe_div(v_rat, dd + _EPS).diff(5)


def vpd_drv2_015_joint_vp_osc_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_osc = _safe_div(volume.rolling(21).mean(), volume.rolling(63).mean())
    p_osc = _safe_div(close.rolling(21).mean(), close.rolling(63).mean())
    return (v_osc * p_osc).diff(5)


def vpd_drv2_016_spike_freq_div_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    med = _rolling_median(volume, 252)
    spike = (volume > 2 * med)
    s_dn = (spike & (close < close.shift(1))).rolling(63).sum()
    s_up = (spike & (close > close.shift(1))).rolling(63).sum()
    return _safe_div(s_dn, s_up).diff(5)


def vpd_drv2_017_relative_vbp_div_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    ma = close.rolling(20).mean()
    dist = (close - ma).abs() / ma
    v_rat = _safe_div(volume, _rolling_median(volume, 252))
    return (v_rat * dist).diff(5)


def vpd_drv2_018_climax_reclaim_div_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    l = close.rolling(21).min().shift(1)
    rec = (close > l) & (close.shift(1) < l)
    v_rat = _safe_div(volume, _rolling_median(volume, 63))
    return v_rat.where(rec).ffill().diff(5)


def vpd_drv2_019_force_price_div_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    fi = close.diff(1) * volume
    ma = close.rolling(50).mean()
    dist = (close - ma) / ma
    ratio = _safe_div(fi.rolling(21).mean(), dist.abs() + _EPS)
    return ratio.diff(5)


def vpd_drv2_020_vw_rsi_div_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    delta = close.diff()
    def _rsi(d, v=None):
        if v is None:
            g = d.where(d > 0, 0).rolling(14).mean()
            l = d.where(d < 0, 0).abs().rolling(14).mean()
        else:
            g = (d.where(d > 0, 0) * v).rolling(14).mean()
            l = (d.where(d < 0, 0).abs() * v).rolling(14).mean()
        return 100 - (100 / (1 + _safe_div(g, l)))
    div = _rsi(delta) - _rsi(delta, volume)
    return div.diff(5)


def vpd_drv2_021_consecutive_vp_div_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    cond = (volume > volume.shift(1)) & (close < close.shift(1))
    dur = cond.astype(int).groupby((cond == 0).cumsum()).cumsum()
    return dur.diff(5)


def vpd_drv2_022_vp_overlap_eff_velocity(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    net_p = (close - close.shift(63)).abs()
    v_range = (volume * (high - low)).rolling(63).sum()
    eff = _safe_div(net_p, v_range)
    return eff.diff(5)


def vpd_drv2_023_supply_demand_ratio_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_dn = volume.where(close < close.shift(1), 0).rolling(21).sum()
    v_up = volume.where(close > close.shift(1), 0).rolling(21).sum()
    ratio = _safe_div(v_dn, v_up)
    return ratio.diff(5)


def vpd_drv2_024_climax_retracement_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 63))
    l = close.rolling(252).min()
    h = close.rolling(252).max()
    rf = _safe_div(close - l, h - l)
    score = v_rat * (1.0 - rf)
    return score.diff(5)


def vpd_drv2_025_vp_divergence_composite_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vpd_075_volume_price_divergence_final_composite(close, volume)
    return score.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V22_V_REGISTRY = {
    "vpd_drv2_001_vp_divergence_velocity": {"inputs": ["close", "volume"], "func": vpd_drv2_001_vp_divergence_velocity},
    "vpd_drv2_002_absorption_ratio_velocity": {"inputs": ["close", "volume"], "func": vpd_drv2_002_absorption_ratio_velocity},
    "vpd_drv2_003_volume_price_corr_velocity": {"inputs": ["close", "volume"], "func": vpd_drv2_003_volume_price_corr_velocity},
    "vpd_drv2_004_obv_price_div_velocity": {"inputs": ["close", "volume"], "func": vpd_drv2_004_obv_price_div_velocity},
    "vpd_drv2_005_climax_to_range_div_velocity": {"inputs": ["high", "low", "volume"], "func": vpd_drv2_005_climax_to_range_div_velocity},
    "vpd_drv2_006_supply_surge_velocity": {"inputs": ["close", "volume"], "func": vpd_drv2_006_supply_surge_velocity},
    "vpd_drv2_007_demand_exhaustion_velocity": {"inputs": ["close", "volume"], "func": vpd_drv2_007_demand_exhaustion_velocity},
    "vpd_drv2_008_vp_entropy_div_velocity": {"inputs": ["close", "volume"], "func": vpd_drv2_008_vp_entropy_div_velocity},
    "vpd_drv2_009_climax_reversal_div_velocity": {"inputs": ["close", "volume", "high", "low"], "func": vpd_drv2_009_climax_reversal_div_velocity},
    "vpd_drv2_010_vw_path_divergence_velocity": {"inputs": ["close", "volume"], "func": vpd_drv2_010_vw_path_divergence_velocity},
    "vpd_drv2_011_turnover_to_ret_accel_velocity": {"inputs": ["close", "volume", "sharesbas"], "func": vpd_drv2_011_turnover_to_ret_accel_velocity},
    "vpd_drv2_012_rejection_climax_velocity": {"inputs": ["close", "high", "volume"], "func": vpd_drv2_012_rejection_climax_velocity},
    "vpd_drv2_013_mktcap_vp_drift_div_velocity": {"inputs": ["close", "volume", "sharesbas"], "func": vpd_drv2_013_mktcap_vp_drift_div_velocity},
    "vpd_drv2_014_volume_per_unit_dd_velocity": {"inputs": ["close", "volume"], "func": vpd_drv2_014_volume_per_unit_dd_velocity},
    "vpd_drv2_015_joint_vp_osc_velocity": {"inputs": ["close", "volume"], "func": vpd_drv2_015_joint_vp_osc_velocity},
    "vpd_drv2_016_spike_freq_div_velocity": {"inputs": ["close", "volume"], "func": vpd_drv2_016_spike_freq_div_velocity},
    "vpd_drv2_017_relative_vbp_div_velocity": {"inputs": ["close", "volume"], "func": vpd_drv2_017_relative_vbp_div_velocity},
    "vpd_drv2_018_climax_reclaim_div_velocity": {"inputs": ["close", "volume"], "func": vpd_drv2_018_climax_reclaim_div_velocity},
    "vpd_drv2_019_force_price_div_velocity": {"inputs": ["close", "volume"], "func": vpd_drv2_019_force_price_div_velocity},
    "vpd_drv2_020_vw_rsi_div_velocity": {"inputs": ["close", "volume"], "func": vpd_drv2_020_vw_rsi_div_velocity},
    "vpd_drv2_021_consecutive_vp_div_velocity": {"inputs": ["close", "volume"], "func": vpd_drv2_021_consecutive_vp_div_velocity},
    "vpd_drv2_022_vp_overlap_eff_velocity": {"inputs": ["close", "volume", "high", "low"], "func": vpd_drv2_022_vp_overlap_eff_velocity},
    "vpd_drv2_023_supply_demand_ratio_velocity": {"inputs": ["close", "volume"], "func": vpd_drv2_023_supply_demand_ratio_velocity},
    "vpd_drv2_024_climax_retracement_velocity": {"inputs": ["close", "volume"], "func": vpd_drv2_024_climax_retracement_velocity},
    "vpd_drv2_025_vp_divergence_composite_velocity": {"inputs": ["close", "volume"], "func": vpd_drv2_025_vp_divergence_composite_velocity},
}
