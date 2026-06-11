"""
17_volume_climax — 2nd Derivatives
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

# 25 features capturing acceleration of volume climax metrics
def vcx_drv2_001_climax_ratio_252d_velocity(volume: pd.Series) -> pd.Series:
    # Rate of change of the single-day climax ratio
    h = volume.rolling(252).max().shift(1)
    rat = _safe_div(volume, h)
    return rat.diff(5)


def vcx_drv2_002_climax_zscore_velocity(volume: pd.Series) -> pd.Series:
    v_avg = volume.expanding().mean()
    v_std = volume.expanding().std()
    z = (volume - v_avg) / v_std
    return z.diff(5)


def vcx_drv2_003_climax_reversal_velocity(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    lw = (close - low).where(close > (high + low) / 2.0, 0)
    score = v_rat * _safe_div(lw, high - low)
    return score.diff(5)


def vcx_drv2_004_climax_exhaustion_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_mean(volume, 21))
    r_rat = _safe_div(close.pct_change().abs(), close.pct_change().abs().rolling(21).mean())
    idx = _safe_div(v_rat, r_rat)
    return idx.diff(5)


def vcx_drv2_005_mktcap_climax_velocity(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 252))
    mc = close * sharesbas
    dist = (mc.cummax() - mc) / mc.cummax()
    return (v_rat * dist).diff(5)


def vcx_drv2_006_climax_final_score_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    vs = _safe_div(volume, _rolling_median(volume, 21)) / 5.0
    ret = close.pct_change().abs() / (close.pct_change().rolling(21).std() + _EPS) / 5.0
    score = (0.7 * vs + 0.3 * ret)
    return score.diff(5)


def vcx_drv2_007_climax_volatility_spread_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    p_vol = close.pct_change().rolling(21).std()
    p_vol_rat = _safe_div(p_vol, p_vol.rolling(63).median())
    return (v_rat - p_vol_rat).diff(5)


def vcx_drv2_008_climax_concentration_velocity(volume: pd.Series) -> pd.Series:
    rat = _safe_div(volume, volume.rolling(21).sum())
    return rat.diff(5)


def vcx_drv2_009_climax_velocity_velocity(volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    return v_rat.diff(5).diff(5)


def vcx_drv2_010_climax_persistence_velocity(volume: pd.Series) -> pd.Series:
    med = _rolling_median(volume, 252)
    cnt = (volume > 3 * med).rolling(63).sum()
    return cnt.diff(5)


def vcx_drv2_011_turnover_climax_zscore_velocity(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    z = (to - to.rolling(252).mean()) / to.rolling(252).std()
    return z.diff(5)


def vcx_drv2_012_climax_reversal_efficiency_velocity(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 252))
    lw = (close - low).clip(lower=0) / close
    eff = _safe_div(lw, v_rat)
    return eff.diff(5)


def vcx_drv2_013_climax_oscillation_decay_velocity(volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    dec = v_rat.rolling(63).std() / v_rat.rolling(63).mean()
    return dec.diff(5)


def vcx_drv2_014_volume_climax_entropy_velocity(volume: pd.Series) -> pd.Series:
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y, bins=5, density=True)
        p = h[h > 0]
        return -np.sum(p * np.log(p))
    e_raw = volume.rolling(63).apply(_ent, raw=True)
    v_climax = volume.where(volume > 3 * _rolling_median(volume, 252), 0)
    e_climax = v_climax.rolling(63).apply(_ent, raw=True)
    ratio = _safe_div(e_climax, e_raw)
    return ratio.diff(5)


def vcx_drv2_015_mktcap_turnover_climax_velocity(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    to = _safe_div(volume, sharesbas)
    idx = mc * to
    z = (idx - idx.rolling(252).mean()) / idx.rolling(252).std()
    return z.diff(5)


def vcx_drv2_016_climax_spike_to_gap_velocity(volume: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 21))
    gap = (open - close.shift(1)).abs() / (close.shift(1) + _EPS)
    ratio = _safe_div(v_rat, gap + _EPS)
    return ratio.diff(5)


def vcx_drv2_017_terminal_climax_exhaustion_velocity(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    score = vcx_075_terminal_climax_exhaustion_score(close, volume, high, low)
    return score.diff(5)


def vcx_drv2_018_climax_magnitude_drift_velocity(volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 252))
    def _slope(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).slope
    sl = v_rat.rolling(63).apply(_slope, raw=True)
    return sl.diff(5)


def vcx_drv2_019_climax_to_vol_adjusted_depth_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    vs = _safe_div(volume, _rolling_median(volume, 63))
    h = close.rolling(252).max()
    dd = (h - close) / h
    vol = close.pct_change().rolling(21).std()
    score = vs * _safe_div(dd, vol)
    return score.diff(5)


def vcx_drv2_020_climax_reversal_trap_velocity(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    v_rat = _safe_div(volume, _rolling_median(volume, 63))
    pos = (close - low) / (high - low + _EPS)
    score = v_rat * (1.0 - pos)
    return score.diff(5)


def vcx_drv2_021_volume_climax_skew_velocity(volume: pd.Series) -> pd.Series:
    mx = volume.rolling(63).max()
    med = volume.rolling(63).median()
    skew = volume.rolling(63).skew()
    score = _safe_div(_safe_div(mx, med), skew.abs())
    return score.diff(5)


def vcx_drv2_022_climax_integral_ratio_velocity(volume: pd.Series) -> pd.Series:
    ratio = _safe_div(volume.rolling(5).sum(), volume.rolling(21).sum())
    return ratio.diff(5)


def vcx_drv2_023_final_volume_cap_climax_velocity(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    score = vcx_150_final_volume_capitulation_climax(close, volume, high, low)
    return score.diff(5)


def vcx_drv2_024_climax_at_ath_low_accel(close: pd.Series, volume: pd.Series) -> pd.Series:
    l = close.cummin()
    is_low = (close == l)
    v_rat = _safe_div(volume, _rolling_median(volume, 252))
    val = v_rat.where(is_low).ffill()
    return val.diff(5).diff(5)


def vcx_drv2_025_climax_impulse_velocity(volume: pd.Series) -> pd.Series:
    imp = _safe_div(volume, volume.shift(1)) - 1.0
    return imp.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V17_V_REGISTRY = {
    "vcx_drv2_001_climax_ratio_252d_velocity": {"inputs": ["volume"], "func": vcx_drv2_001_climax_ratio_252d_velocity},
    "vcx_drv2_002_climax_zscore_velocity": {"inputs": ["volume"], "func": vcx_drv2_002_climax_zscore_velocity},
    "vcx_drv2_003_climax_reversal_velocity": {"inputs": ["close", "high", "low", "volume"], "func": vcx_drv2_003_climax_reversal_velocity},
    "vcx_drv2_004_climax_exhaustion_velocity": {"inputs": ["close", "volume"], "func": vcx_drv2_004_climax_exhaustion_velocity},
    "vcx_drv2_005_mktcap_climax_velocity": {"inputs": ["close", "volume", "sharesbas"], "func": vcx_drv2_005_mktcap_climax_velocity},
    "vcx_drv2_006_climax_final_score_velocity": {"inputs": ["close", "volume"], "func": vcx_drv2_006_climax_final_score_velocity},
    "vcx_drv2_007_climax_volatility_spread_velocity": {"inputs": ["close", "volume"], "func": vcx_drv2_007_climax_volatility_spread_velocity},
    "vcx_drv2_008_climax_concentration_velocity": {"inputs": ["volume"], "func": vcx_drv2_008_climax_concentration_velocity},
    "vcx_drv2_009_climax_velocity_velocity": {"inputs": ["volume"], "func": vcx_drv2_009_climax_velocity_velocity},
    "vcx_drv2_010_climax_persistence_velocity": {"inputs": ["volume"], "func": vcx_drv2_010_climax_persistence_velocity},
    "vcx_drv2_011_turnover_climax_zscore_velocity": {"inputs": ["volume", "sharesbas"], "func": vcx_drv2_011_turnover_climax_zscore_velocity},
    "vcx_drv2_012_climax_reversal_efficiency_velocity": {"inputs": ["close", "volume", "high", "low"], "func": vcx_drv2_012_climax_reversal_efficiency_velocity},
    "vcx_drv2_013_climax_oscillation_decay_velocity": {"inputs": ["volume"], "func": vcx_drv2_013_climax_oscillation_decay_velocity},
    "vcx_drv2_014_volume_climax_entropy_velocity": {"inputs": ["volume"], "func": vcx_drv2_014_volume_climax_entropy_velocity},
    "vcx_drv2_015_mktcap_turnover_climax_velocity": {"inputs": ["close", "volume", "sharesbas"], "func": vcx_drv2_015_mktcap_turnover_climax_velocity},
    "vcx_drv2_016_climax_spike_to_gap_velocity": {"inputs": ["volume", "close", "open"], "func": vcx_drv2_016_climax_spike_to_gap_velocity},
    "vcx_drv2_017_terminal_climax_exhaustion_velocity": {"inputs": ["close", "volume", "high", "low"], "func": vcx_drv2_017_terminal_climax_exhaustion_velocity},
    "vcx_drv2_018_climax_magnitude_drift_velocity": {"inputs": ["volume"], "func": vcx_drv2_018_climax_magnitude_drift_velocity},
    "vcx_drv2_019_climax_to_vol_adjusted_depth_velocity": {"inputs": ["close", "volume"], "func": vcx_drv2_019_climax_to_vol_adjusted_depth_velocity},
    "vcx_drv2_020_climax_reversal_trap_velocity": {"inputs": ["close", "high", "low", "volume"], "func": vcx_drv2_020_climax_reversal_trap_velocity},
    "vcx_drv2_021_volume_climax_skew_velocity": {"inputs": ["volume"], "func": vcx_drv2_021_volume_climax_skew_velocity},
    "vcx_drv2_022_climax_integral_ratio_velocity": {"inputs": ["volume"], "func": vcx_drv2_022_climax_integral_ratio_velocity},
    "vcx_drv2_023_final_volume_cap_climax_velocity": {"inputs": ["close", "volume", "high", "low"], "func": vcx_drv2_023_final_volume_cap_climax_velocity},
    "vcx_drv2_024_climax_at_ath_low_accel": {"inputs": ["close", "volume"], "func": vcx_drv2_024_climax_at_ath_low_accel},
    "vcx_drv2_025_climax_impulse_velocity": {"inputs": ["volume"], "func": vcx_drv2_025_climax_impulse_velocity},
}
