"""
17_volume_climax — 3rd Derivatives
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

# 25 features capturing exhaustion/inflection of volume climax acceleration (jerk)
def vcx_drv3_001_climax_ratio_252d_jerk(volume: pd.Series) -> pd.Series:
    # Rate of change of volume climax velocity
    h = volume.rolling(252).max().shift(1)
    rat = _safe_div(volume, h)
    vel = rat.diff(5)
    return vel.diff(5)


def vcx_drv3_002_climax_zscore_jerk(volume: pd.Series) -> pd.Series:
    v_avg = volume.expanding().mean()
    v_std = volume.expanding().std()
    z = (volume - v_avg) / (v_std + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def vcx_drv3_003_climax_reversal_jerk(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    lw = (close - low).where(close > (high + low) / 2.0, 0)
    score = v_rat * _safe_div(lw, high - low + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def vcx_drv3_004_climax_exhaustion_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_mean(volume, 21))
    r_rat = _safe_div(close.pct_change().abs(), close.pct_change().abs().rolling(21).mean() + _EPS)
    idx = _safe_div(v_rat, r_rat)
    vel = idx.diff(5)
    return vel.diff(5)


def vcx_drv3_005_mktcap_climax_jerk(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 252))
    mc = close * sharesbas
    dist = (mc.cummax() - mc) / (mc.cummax() + _EPS)
    vel = (v_rat * dist).diff(5)
    return vel.diff(5)


def vcx_drv3_006_climax_final_score_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    vs = _safe_div(volume, _rolling_median(volume, 21)) / 5.0
    ret = close.pct_change().abs() / (close.pct_change().rolling(21).std() + _EPS) / 5.0
    score = (0.7 * vs + 0.3 * ret)
    vel = score.diff(5)
    return vel.diff(5)


def vcx_drv3_007_climax_volatility_spread_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    p_vol = close.pct_change().rolling(21).std()
    p_vol_rat = _safe_div(p_vol, p_vol.rolling(63).median())
    vel = (v_rat - p_vol_rat).diff(5)
    return vel.diff(5)


def vcx_drv3_008_climax_concentration_jerk(volume: pd.Series) -> pd.Series:
    rat = _safe_div(volume, volume.rolling(21).sum())
    vel = rat.diff(5)
    return vel.diff(5)


def vcx_drv3_009_climax_velocity_jerk(volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    vel = v_rat.diff(5)
    accel = vel.diff(5)
    return accel.diff(5)


def vcx_drv3_010_climax_persistence_jerk(volume: pd.Series) -> pd.Series:
    med = _rolling_median(volume, 252)
    cnt = (volume > 3 * med).rolling(63).sum()
    vel = cnt.diff(5)
    return vel.diff(5)


def vcx_drv3_011_turnover_climax_zscore_jerk(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    z = (to - to.rolling(252).mean()) / (to.rolling(252).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def vcx_drv3_012_climax_reversal_efficiency_jerk(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 252))
    lw = (close - low).clip(lower=0) / (close + _EPS)
    eff = _safe_div(lw, v_rat)
    vel = eff.diff(5)
    return vel.diff(5)


def vcx_drv3_013_climax_oscillation_decay_jerk(volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    dec = v_rat.rolling(63).std() / (v_rat.rolling(63).mean() + _EPS)
    vel = dec.diff(5)
    return vel.diff(5)


def vcx_drv3_014_volume_climax_entropy_jerk(volume: pd.Series) -> pd.Series:
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y, bins=5, density=True)
        p = h / (np.sum(h) + _EPS)
        return -np.sum(p[p > 0] * np.log(p[p > 0]))
    e_raw = volume.rolling(63).apply(_ent, raw=True)
    v_climax = volume.where(volume > 3 * _rolling_median(volume, 252), 0)
    e_climax = v_climax.rolling(63).apply(_ent, raw=True)
    ratio = _safe_div(e_climax, e_raw)
    vel = ratio.diff(5)
    return vel.diff(5)


def vcx_drv3_015_mktcap_turnover_climax_jerk(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    to = _safe_div(volume, sharesbas)
    idx = mc * to
    z = (idx - idx.rolling(252).mean()) / (idx.rolling(252).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def vcx_drv3_016_climax_spike_to_gap_jerk(volume: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    gap = (open - close.shift(1)).abs() / (close.shift(1) + _EPS)
    ratio = _safe_div(v_rat, gap + _EPS)
    vel = ratio.diff(5)
    return vel.diff(5)


def vcx_drv3_017_terminal_climax_exhaustion_jerk(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    from scipy.stats import linregress
    v_rat = _safe_div(volume, _rolling_median(volume, 63))
    path_len = close.diff().abs().rolling(21).sum()
    jag = _safe_div(path_len, (close - close.shift(21)).abs())
    wick = _safe_div(close - low, high - low)
    score = v_rat * jag * wick
    vel = score.diff(5)
    return vel.diff(5)


def vcx_drv3_018_climax_magnitude_drift_jerk(volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 252))
    def _slope(y):
        from scipy.stats import linregress
        if len(y) < 2: return 0.0
        return linregress(np.arange(len(y)), y).slope
    sl = v_rat.rolling(63).apply(_slope, raw=True)
    vel = sl.diff(5)
    return vel.diff(5)


def vcx_drv3_019_climax_to_vol_adjusted_depth_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    vs = _safe_div(volume, _rolling_median(volume, 63))
    h = close.rolling(252).max()
    dd = (h - close) / h
    vol = close.pct_change().rolling(21).std()
    score = vs * _safe_div(dd, vol + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def vcx_drv3_020_climax_reversal_trap_jerk(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 63))
    pos = _safe_div(close - low, high - low)
    score = v_rat * (1.0 - pos)
    vel = score.diff(5)
    return vel.diff(5)


def vcx_drv3_021_volume_climax_skew_jerk(volume: pd.Series) -> pd.Series:
    mx = volume.rolling(63).max()
    med = volume.rolling(63).median()
    skew = volume.rolling(63).skew()
    score = _safe_div(_safe_div(mx, med), skew.abs() + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def vcx_drv3_022_climax_integral_ratio_jerk(volume: pd.Series) -> pd.Series:
    ratio = _safe_div(volume.rolling(5).sum(), volume.rolling(21).sum())
    vel = ratio.diff(5)
    return vel.diff(5)


def vcx_drv3_023_final_volume_cap_climax_jerk(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    vs = _safe_div(volume, _rolling_median(volume, 63))
    rev = _safe_div(close - low, high - low + _EPS)
    dd = _safe_div(close.rolling(252).max() - close, close.rolling(252).max())
    score = vs * rev * dd
    vel = score.diff(5)
    return vel.diff(5)


def vcx_drv3_024_climax_at_ath_low_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    l = close.cummin()
    is_low = (close == l)
    v_rat = _safe_div(volume, _rolling_median(volume, 252))
    val = v_rat.where(is_low).ffill()
    accel = val.diff(5).diff(5)
    return accel.diff(5)


def vcx_drv3_025_climax_impulse_jerk(volume: pd.Series) -> pd.Series:
    imp = _safe_div(volume, volume.shift(1)) - 1.0
    vel = imp.diff(5)
    return vel.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V17_A_REGISTRY = {
    "vcx_drv3_001_climax_ratio_252d_jerk": {"inputs": ["volume"], "func": vcx_drv3_001_climax_ratio_252d_jerk},
    "vcx_drv3_002_climax_zscore_jerk": {"inputs": ["volume"], "func": vcx_drv3_002_climax_zscore_jerk},
    "vcx_drv3_003_climax_reversal_jerk": {"inputs": ["close", "high", "low", "volume"], "func": vcx_drv3_003_climax_reversal_jerk},
    "vcx_drv3_004_climax_exhaustion_jerk": {"inputs": ["close", "volume"], "func": vcx_drv3_004_climax_exhaustion_jerk},
    "vcx_drv3_005_mktcap_climax_jerk": {"inputs": ["close", "volume", "sharesbas"], "func": vcx_drv3_005_mktcap_climax_jerk},
    "vcx_drv3_006_climax_final_score_jerk": {"inputs": ["close", "volume"], "func": vcx_drv3_006_climax_final_score_jerk},
    "vcx_drv3_007_climax_volatility_spread_jerk": {"inputs": ["close", "volume"], "func": vcx_drv3_007_climax_volatility_spread_jerk},
    "vcx_drv3_008_climax_concentration_jerk": {"inputs": ["volume"], "func": vcx_drv3_008_climax_concentration_jerk},
    "vcx_drv3_009_climax_velocity_jerk": {"inputs": ["volume"], "func": vcx_drv3_009_climax_velocity_jerk},
    "vcx_drv3_010_climax_persistence_jerk": {"inputs": ["volume"], "func": vcx_drv3_010_climax_persistence_jerk},
    "vcx_drv3_011_turnover_climax_zscore_jerk": {"inputs": ["volume", "sharesbas"], "func": vcx_drv3_011_turnover_climax_zscore_jerk},
    "vcx_drv3_012_climax_reversal_efficiency_jerk": {"inputs": ["close", "volume", "high", "low"], "func": vcx_drv3_012_climax_reversal_efficiency_jerk},
    "vcx_drv3_013_climax_oscillation_decay_jerk": {"inputs": ["volume"], "func": vcx_drv3_013_climax_oscillation_decay_jerk},
    "vcx_drv3_014_volume_climax_entropy_jerk": {"inputs": ["volume"], "func": vcx_drv3_014_volume_climax_entropy_jerk},
    "vcx_drv3_015_mktcap_turnover_climax_jerk": {"inputs": ["close", "volume", "sharesbas"], "func": vcx_drv3_015_mktcap_turnover_climax_jerk},
    "vcx_drv3_016_climax_spike_to_gap_jerk": {"inputs": ["volume", "close", "open"], "func": vcx_drv3_016_climax_spike_to_gap_jerk},
    "vcx_drv3_017_terminal_climax_exhaustion_jerk": {"inputs": ["close", "volume", "high", "low"], "func": vcx_drv3_017_terminal_climax_exhaustion_jerk},
    "vcx_drv3_018_climax_magnitude_drift_jerk": {"inputs": ["volume"], "func": vcx_drv3_018_climax_magnitude_drift_jerk},
    "vcx_drv3_019_climax_to_vol_adjusted_depth_jerk": {"inputs": ["close", "volume"], "func": vcx_drv3_019_climax_to_vol_adjusted_depth_jerk},
    "vcx_drv3_020_climax_reversal_trap_jerk": {"inputs": ["close", "high", "low", "volume"], "func": vcx_drv3_020_climax_reversal_trap_jerk},
    "vcx_drv3_021_volume_climax_skew_jerk": {"inputs": ["volume"], "func": vcx_drv3_021_volume_climax_skew_jerk},
    "vcx_drv3_022_climax_integral_ratio_jerk": {"inputs": ["volume"], "func": vcx_drv3_022_climax_integral_ratio_jerk},
    "vcx_drv3_023_final_volume_cap_climax_jerk": {"inputs": ["close", "volume", "high", "low"], "func": vcx_drv3_023_final_volume_cap_climax_jerk},
    "vcx_drv3_024_climax_at_ath_low_jerk": {"inputs": ["close", "volume"], "func": vcx_drv3_024_climax_at_ath_low_jerk},
    "vcx_drv3_025_climax_impulse_jerk": {"inputs": ["volume"], "func": vcx_drv3_025_climax_impulse_jerk},
}
