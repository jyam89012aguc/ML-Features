"""
20_up_down_volume — 3rd Derivatives
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

# 25 features capturing exhaustion/inflection of up/down volume acceleration (jerk)
def udv_drv3_001_up_down_ratio_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    is_up = (close > close.shift(1))
    is_down = (close < close.shift(1))
    v_up = volume.where(is_up, 0).rolling(21).sum()
    v_down = volume.where(is_down, 0).rolling(21).sum()
    ratio = _safe_div(v_up, v_down)
    vel = ratio.diff(5)
    return vel.diff(5)


def udv_drv3_002_force_index_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    fi = close.diff(1) * volume
    v_fi = fi.rolling(13).mean()
    vel = v_fi.diff(5)
    return vel.diff(5)


def udv_drv3_003_down_volume_zscore_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    is_down = (close < close.shift(1))
    v_dn = volume.where(is_down, 0)
    z = (v_dn - v_dn.rolling(252).mean()) / (v_dn.rolling(252).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def udv_drv3_004_volume_pressure_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_dn = volume.where(close < close.shift(1), 0).rolling(63).sum()
    v_tot = volume.rolling(63).sum()
    h = close.rolling(252).max()
    dd = (h - close) / h
    idx = _safe_div(v_dn, v_tot) * dd
    vel = idx.diff(5)
    return vel.diff(5)


def udv_drv3_005_obv_efficiency_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.diff()
    obv = (np.sign(ret) * volume).cumsum()
    net = obv.diff(63).abs()
    sum_v = volume.rolling(63).sum()
    eff = _safe_div(net, sum_v)
    vel = eff.diff(5)
    return vel.diff(5)


def udv_drv3_006_selling_exhaustion_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    is_down = (close < close.shift(1))
    v_dn_rat = _safe_div(volume.where(is_down, 0).rolling(21).mean(), volume.rolling(252).median())
    p_vel = np.log(close).diff(5).abs()
    score = _safe_div(v_dn_rat, p_vel + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def udv_drv3_007_down_volume_accel_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_dn = volume.where(close < close.shift(1), 0)
    accel = _safe_div(v_dn.rolling(5).mean(), v_dn.rolling(21).mean())
    vel = accel.diff(5)
    return vel.diff(5)


def udv_drv3_008_up_down_vol_spread_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.diff()
    v_sig = np.sign(ret) * volume
    spr = _safe_div(v_sig, volume)
    vel = spr.diff(5)
    return vel.diff(5)


def vtr_drv3_009_up_volume_persistence_jerk(close: pd.Series) -> pd.Series:
    p = (close > close.shift(1)).rolling(63).mean()
    vel = p.diff(5)
    return vel.diff(5)


def udv_drv3_010_vwap_ud_spread_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_up = volume.where(close > close.shift(1), 0)
    v_dn = volume.where(close < close.shift(1), 0)
    p_up = close.where(close > close.shift(1), 0)
    p_dn = close.where(close < close.shift(1), 0)
    vwap_up = _safe_div((v_up * p_up).rolling(252).sum(), v_up.rolling(252).sum())
    vwap_dn = _safe_div((v_dn * p_dn).rolling(252).sum(), v_dn.rolling(252).sum())
    spr = _safe_div(vwap_up - vwap_dn, close + _EPS)
    vel = spr.diff(5)
    return vel.diff(5)


def udv_drv3_011_pressure_oscillator_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_dn = volume.where(close < close.shift(1), 0)
    v_tot = volume
    vp_short = _safe_div(v_dn.rolling(21).sum(), v_tot.rolling(21).sum())
    vp_long = _safe_div(v_dn.rolling(63).sum(), v_tot.rolling(63).sum())
    osc = vp_short - vp_long
    vel = osc.diff(5)
    return vel.diff(5)


def udv_drv3_012_up_down_entropy_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y[~np.isnan(y)], bins=5, density=True)
        p = h[h > 0]
        return -np.sum(p * np.log(p))
    v_up = volume.where(close > close.shift(1), 0)
    v_dn = volume.where(close < close.shift(1), 0)
    ratio = _safe_div(v_up.rolling(63).apply(_ent, raw=True), v_dn.rolling(63).apply(_ent, raw=True))
    vel = ratio.diff(5)
    return vel.diff(5)


def udv_drv3_013_mktcap_ud_spread_jerk(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v_sig = np.sign(mc.diff()) * volume
    z = (v_sig - v_sig.rolling(252).mean()) / (v_sig.rolling(252).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def udv_drv3_014_buying_exhaustion_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    is_up = (close > close.shift(1))
    v_up_rat = _safe_div(volume.where(is_up, 0).rolling(21).mean(), volume.rolling(252).median())
    p_vel = np.log(close).diff(5).abs()
    score = _safe_div(v_up_rat, p_vel + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def udv_drv3_015_down_volume_energy_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_dn = volume.where(close < close.shift(1), 0).rolling(63).sum()
    v_tot = volume.rolling(63).sum()
    ratio = _safe_div(v_dn, v_tot)
    p_vel = np.log(close).diff(21).abs()
    idx = (ratio**2) * p_vel
    vel = idx.diff(5)
    return vel.diff(5)


def udv_drv3_016_volume_reversal_climax_jerk(close: pd.Series, volume: pd.Series, low: pd.Series) -> pd.Series:
    is_down = (close < close.shift(1))
    v_rat = _safe_div(volume, volume.rolling(252).median())
    c_low = _safe_div(close, low + _EPS)
    score = (v_rat * c_low).where(is_down).ffill()
    vel = score.diff(5)
    return vel.diff(5)


def udv_drv3_017_mktcap_down_volume_persistence_jerk(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    is_down = (mc < mc.shift(1))
    per = volume.where(is_down, 0).rolling(63).mean() / (volume.rolling(252).median() + _EPS)
    vel = per.diff(5)
    return vel.diff(5)


def udv_drv3_018_consecutive_up_volume_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    is_up = (close > close.shift(1))
    v_inc = (volume > volume.shift(1))
    cond = (is_up & v_inc).astype(int)
    dur = cond.groupby((cond == 0).cumsum()).cumsum()
    vel = dur.diff(5)
    return vel.diff(5)


def udv_drv3_019_up_down_volume_vol_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_up = volume.where(close > close.shift(1))
    v_dn = volume.where(close < close.shift(1))
    ratio = _safe_div(v_up.rolling(63).std(), v_dn.rolling(63).std())
    vel = ratio.diff(5)
    return vel.diff(5)


def udv_drv3_020_pressure_shift_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_dn_rat = _safe_div(volume.where(close < close.shift(1), 0).rolling(21).sum(), volume.rolling(21).sum())
    vel = v_dn_rat.diff(21).diff(5)
    return vel.diff(5)


def udv_drv3_021_obv_to_vol_trend_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.diff()
    obv = (np.sign(ret) * volume).cumsum()
    os = obv.diff(21)
    vs = volume.rolling(21).sum()
    ratio = _safe_div(os, vs)
    vel = ratio.diff(5)
    return vel.diff(5)


def udv_drv3_022_ratio_vol_new_low_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    l = close.rolling(252).min()
    is_low = (close == l)
    v_low = volume.where(is_low, 0).rolling(252).sum()
    v_tot = volume.rolling(252).sum()
    ratio = _safe_div(v_low, v_tot)
    vel = ratio.diff(5)
    return vel.diff(5)


def udv_drv3_023_climax_day_dir_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    mx_idx = volume.rolling(63).apply(np.argmax, raw=True)
    ret = close.diff()
    val = np.sign(ret.iloc[mx_idx.astype(int)])
    vel = val.diff(5)
    return vel.diff(5)


def udv_drv3_024_down_volume_concentration_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_dn = volume.where(close < close.shift(1), 0).rolling(21).sum()
    v_tot = volume.rolling(21).sum()
    conc = _safe_div(v_dn, v_tot)
    vel = conc.diff(5)
    return vel.diff(5)


def udv_drv3_025_up_down_volume_final_composite_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = udv_150_up_down_volume_final_imbalance_index(close, volume)
    vel = score.diff(5)
    return vel.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V20_A_REGISTRY = {
    "udv_drv3_001_up_down_ratio_jerk": {"inputs": ["close", "volume"], "func": udv_drv3_001_up_down_ratio_jerk},
    "udv_drv3_002_force_index_jerk": {"inputs": ["close", "volume"], "func": udv_drv3_002_force_index_jerk},
    "udv_drv3_003_down_volume_zscore_jerk": {"inputs": ["close", "volume"], "func": udv_drv3_003_down_volume_zscore_jerk},
    "udv_drv3_004_volume_pressure_jerk": {"inputs": ["close", "volume"], "func": udv_drv3_004_volume_pressure_jerk},
    "udv_drv3_005_obv_efficiency_jerk": {"inputs": ["close", "volume"], "func": udv_drv3_005_obv_efficiency_jerk},
    "udv_drv3_006_selling_exhaustion_jerk": {"inputs": ["close", "volume"], "func": udv_drv3_006_selling_exhaustion_jerk},
    "udv_drv3_007_down_volume_accel_jerk": {"inputs": ["close", "volume"], "func": udv_drv3_007_down_volume_accel_jerk},
    "udv_drv3_008_up_down_vol_spread_jerk": {"inputs": ["close", "volume"], "func": udv_drv3_008_up_down_vol_spread_jerk},
    "udv_drv3_010_vwap_ud_spread_jerk": {"inputs": ["close", "volume"], "func": udv_drv3_010_vwap_ud_spread_jerk},
    "udv_drv3_011_pressure_oscillator_jerk": {"inputs": ["close", "volume"], "func": udv_drv3_011_pressure_oscillator_jerk},
    "udv_drv3_012_up_down_entropy_jerk": {"inputs": ["close", "volume"], "func": udv_drv3_012_up_down_entropy_jerk},
    "udv_drv3_013_mktcap_ud_spread_jerk": {"inputs": ["close", "volume", "sharesbas"], "func": udv_drv3_013_mktcap_ud_spread_jerk},
    "udv_drv3_014_buying_exhaustion_jerk": {"inputs": ["close", "volume"], "func": udv_drv3_014_buying_exhaustion_jerk},
    "udv_drv3_015_down_volume_energy_jerk": {"inputs": ["close", "volume"], "func": udv_drv3_015_down_volume_energy_jerk},
    "udv_drv3_016_volume_reversal_climax_jerk": {"inputs": ["close", "volume", "low"], "func": udv_drv3_016_volume_reversal_climax_jerk},
    "udv_drv3_017_mktcap_down_volume_persistence_jerk": {"inputs": ["close", "volume", "sharesbas"], "func": udv_drv3_017_mktcap_down_volume_persistence_jerk},
    "udv_drv3_018_consecutive_up_volume_jerk": {"inputs": ["close", "volume"], "func": udv_drv3_018_consecutive_up_volume_jerk},
    "udv_drv3_019_up_down_volume_vol_jerk": {"inputs": ["close", "volume"], "func": udv_drv3_019_up_down_volume_vol_jerk},
    "udv_drv3_020_pressure_shift_jerk": {"inputs": ["close", "volume"], "func": udv_drv3_020_pressure_shift_jerk},
    "udv_drv3_021_obv_to_vol_trend_jerk": {"inputs": ["close", "volume"], "func": udv_drv3_021_obv_to_vol_trend_jerk},
    "udv_drv3_022_ratio_vol_new_low_jerk": {"inputs": ["close", "volume"], "func": udv_drv3_022_ratio_vol_new_low_jerk},
    "udv_drv3_023_climax_day_dir_jerk": {"inputs": ["close", "volume"], "func": udv_drv3_023_climax_day_dir_jerk},
    "udv_drv3_024_down_volume_concentration_jerk": {"inputs": ["close", "volume"], "func": udv_drv3_024_down_volume_concentration_jerk},
    "udv_drv3_025_up_down_volume_final_composite_jerk": {"inputs": ["close", "volume"], "func": udv_drv3_025_up_down_volume_final_composite_jerk},
}
