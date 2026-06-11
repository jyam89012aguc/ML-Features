"""
27_volatility_skewness — 2nd Derivatives
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


# ── Feature functions ────────────────────────────────────────────────────────

# 25 features capturing acceleration of volatility skewness metrics
def vsk_drv2_001_return_skew_21d_velocity(close: pd.Series) -> pd.Series:
    # Change in short-term return skewness
    sk = close.pct_change().rolling(21).skew()
    return sk.diff(5)


def vsk_drv2_002_down_up_skew_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    s = ret.rolling(252).std()
    dn_tail = (ret < -2 * s).astype(int).rolling(63).sum()
    up_tail = (ret > 2 * s).astype(int).rolling(63).sum()
    ratio = _safe_div(dn_tail, up_tail)
    return ratio.diff(5)


def vsk_drv2_003_skewness_zscore_velocity(close: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(21).skew()
    z = (sk - sk.rolling(252).mean()) / (sk.rolling(252).std() + _EPS)
    return z.diff(5)


def vsk_drv2_004_vw_skew_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    v_rat = _safe_div(volume, _rolling_mean(volume, 21))
    weighted_ret = ret * v_rat
    sk = weighted_ret.rolling(21).skew()
    return sk.diff(5)


def vsk_drv2_005_skew_drawdown_velocity(close: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(63).skew()
    h = close.rolling(252).max()
    dd = (h - close) / h
    return (sk * dd).diff(5)


def vsk_drv2_006_panic_tail_intensity_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    sk = ret.rolling(63).skew()
    kt = ret.rolling(63).kurt()
    vol = ret.rolling(63).std()
    idx = _safe_div(sk * kt, vol + _EPS)
    return idx.diff(5)


def vsk_drv2_007_skew_regime_shift_velocity(close: pd.Series) -> pd.Series:
    sk21 = close.pct_change().rolling(21).skew()
    sk252 = close.pct_change().rolling(252).skew()
    shift = sk21 - sk252
    return shift.diff(5)


def vsk_drv2_008_skew_acceleration_velocity(close: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(21).skew()
    acc = sk.diff(5)
    return acc.diff(5)


def vsk_drv2_009_skew_volume_div_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    sk_p = close.pct_change().rolling(63).skew()
    sk_v = volume.rolling(63).skew()
    div = sk_p - sk_v
    return div.diff(5)


def vsk_drv2_010_joint_skew_kurt_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    idx = ret.rolling(63).skew() * ret.rolling(63).kurt()
    z = (idx - idx.rolling(252).mean()) / (idx.rolling(252).std() + _EPS)
    return z.diff(5)


def vsk_drv2_011_realized_asymmetry_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    idx = _safe_div(ret.rolling(21).median() - ret.rolling(21).mean(), ret.rolling(21).std())
    return idx.diff(5)


def vsk_drv2_012_pearson_skewness_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    ps = 3 * _safe_div(ret.rolling(21).mean() - ret.rolling(21).median(), ret.rolling(21).std())
    return ps.diff(5)


def vsk_drv2_013_tail_risk_expansion_velocity(close: pd.Series) -> pd.Series:
    sk21 = close.pct_change().rolling(21).skew()
    idx = _safe_div(sk21, sk21.rolling(252).mean().abs())
    return idx.diff(5)


def vsk_drv2_014_dv_weighted_skew_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    v_rat = _safe_div(volume, volume.rolling(252).median())
    weighted_ret = ret.where(ret < 0, 0) * v_rat
    sk = weighted_ret.rolling(63).skew()
    return sk.diff(5)


def vsk_drv2_015_skew_volatility_spread_velocity(close: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(21).skew()
    vol = close.pct_change().rolling(21).std() * np.sqrt(252)
    v_norm = (vol - vol.rolling(252).mean()) / (vol.rolling(252).std() + _EPS)
    spr = sk - v_norm
    return spr.diff(5)


def vsk_drv2_016_panic_climax_velocity_accel(close: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(21).skew()
    v_sk = sk.diff(5)
    dv = np.log(close).diff(5).abs()
    score = v_sk.clip(upper=0).abs() * dv
    return score.diff(5)


def vsk_drv2_017_mktcap_skew_energy_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    ret = mc.pct_change()
    idx = (ret.rolling(63).skew()**2) * ret.rolling(63).std()
    return idx.diff(5)


def vsk_drv2_018_skew_reversal_climax_velocity(close: pd.Series, low: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(21).skew()
    v_sk = sk.diff(5)
    c_low = _safe_div(close, low)
    return (v_sk * c_low).diff(5)


def vsk_drv2_019_sustained_asymmetry_velocity(close: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(21).skew()
    q25 = sk.rolling(252).quantile(0.25)
    idx = (sk < q25).rolling(252).mean()
    return idx.diff(5)


def vsk_drv2_020_skew_regime_break_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    brk = ret.rolling(21).skew() - ret.rolling(126).skew()
    return brk.diff(5)


def vsk_drv2_021_cumulative_skew_energy_velocity(close: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(21).skew()
    energy = sk.cumsum() / (sk.abs().cumsum() + _EPS)
    return energy.diff(5)


def vsk_drv2_022_final_vsk_fear_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vsk_150_vol_skew_final_fear_index(close, volume)
    return score.diff(5)


def vsk_drv2_023_consecutive_neg_skew_velocity(close: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(21).skew()
    neg = (sk < 0).astype(int)
    dur = neg.groupby((neg == 0).cumsum()).cumsum()
    return dur.diff(5)


def vsk_drv2_024_mktcap_skew_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    sk = mc.pct_change().rolling(63).skew()
    return sk.diff(5)


def vsk_drv2_025_volatility_skewness_composite_velocity(close: pd.Series) -> pd.Series:
    score = vsk_075_volatility_skewness_final_composite(close)
    return score.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V27_V_REGISTRY = {
    "vsk_drv2_001_return_skew_21d_velocity": {"inputs": ["close"], "func": vsk_drv2_001_return_skew_21d_velocity},
    "vsk_drv2_002_down_up_skew_velocity": {"inputs": ["close"], "func": vsk_drv2_002_down_up_skew_velocity},
    "vsk_drv2_003_skewness_zscore_velocity": {"inputs": ["close"], "func": vsk_drv2_003_skewness_zscore_velocity},
    "vsk_drv2_004_vw_skew_velocity": {"inputs": ["close", "volume"], "func": vsk_drv2_004_vw_skew_velocity},
    "vsk_drv2_005_skew_drawdown_velocity": {"inputs": ["close"], "func": vsk_drv2_005_skew_drawdown_velocity},
    "vsk_drv2_006_panic_tail_intensity_velocity": {"inputs": ["close"], "func": vsk_drv2_006_panic_tail_intensity_velocity},
    "vsk_drv2_007_skew_regime_shift_velocity": {"inputs": ["close"], "func": vsk_drv2_007_skew_regime_shift_velocity},
    "vsk_drv2_008_skew_acceleration_velocity": {"inputs": ["close"], "func": vsk_drv2_008_skew_acceleration_velocity},
    "vsk_drv2_009_skew_volume_div_velocity": {"inputs": ["close", "volume"], "func": vsk_drv2_009_skew_volume_div_velocity},
    "vsk_drv2_010_joint_skew_kurt_velocity": {"inputs": ["close"], "func": vsk_drv2_010_joint_skew_kurt_velocity},
    "vsk_drv2_011_realized_asymmetry_velocity": {"inputs": ["close"], "func": vsk_drv2_011_realized_asymmetry_velocity},
    "vsk_drv2_012_pearson_skewness_velocity": {"inputs": ["close"], "func": vsk_drv2_012_pearson_skewness_velocity},
    "vsk_drv2_013_tail_risk_expansion_velocity": {"inputs": ["close"], "func": vsk_drv2_013_tail_risk_expansion_velocity},
    "vsk_drv2_014_dv_weighted_skew_velocity": {"inputs": ["close", "volume"], "func": vsk_drv2_014_dv_weighted_skew_velocity},
    "vsk_drv2_015_skew_volatility_spread_velocity": {"inputs": ["close"], "func": vsk_drv2_015_skew_volatility_spread_velocity},
    "vsk_drv2_016_panic_climax_velocity_accel": {"inputs": ["close"], "func": vsk_drv2_016_panic_climax_velocity_accel},
    "vsk_drv2_017_mktcap_skew_energy_velocity": {"inputs": ["close", "sharesbas"], "func": vsk_drv2_017_mktcap_skew_energy_velocity},
    "vsk_drv2_018_skew_reversal_climax_velocity": {"inputs": ["close", "low"], "func": vsk_drv2_018_skew_reversal_climax_velocity},
    "vsk_drv2_019_sustained_asymmetry_velocity": {"inputs": ["close"], "func": vsk_drv2_019_sustained_asymmetry_velocity},
    "vsk_drv2_020_skew_regime_break_velocity": {"inputs": ["close"], "func": vsk_drv2_020_skew_regime_break_velocity},
    "vsk_drv2_021_cumulative_skew_energy_velocity": {"inputs": ["close"], "func": vsk_drv2_021_cumulative_skew_energy_velocity},
    "vsk_drv2_022_final_vsk_fear_velocity": {"inputs": ["close", "volume"], "func": vsk_drv2_022_final_vsk_fear_velocity},
    "vsk_drv2_023_consecutive_neg_skew_velocity": {"inputs": ["close"], "func": vsk_drv2_023_consecutive_neg_skew_velocity},
    "vsk_drv2_024_mktcap_skew_velocity": {"inputs": ["close", "sharesbas"], "func": vsk_drv2_024_mktcap_skew_velocity},
    "vsk_drv2_025_volatility_skewness_composite_velocity": {"inputs": ["close"], "func": vsk_drv2_025_volatility_skewness_composite_velocity},
}
