"""
27_volatility_skewness — 3rd Derivatives
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


# ── Feature functions ────────────────────────────────────────────────────────

# 25 features capturing exhaustion/inflection of volatility skewness acceleration (jerk)
def vsk_drv3_001_return_skew_21d_jerk(close: pd.Series) -> pd.Series:
    # Rate of change of return skew velocity
    sk = close.pct_change().rolling(21).skew()
    vel = sk.diff(5)
    return vel.diff(5)


def vsk_drv3_002_down_up_skew_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    s = ret.rolling(252).std()
    dn_tail = (ret < -2 * s).astype(int).rolling(63).sum()
    up_tail = (ret > 2 * s).astype(int).rolling(63).sum()
    ratio = _safe_div(dn_tail, up_tail)
    vel = ratio.diff(5)
    return vel.diff(5)


def vsk_drv3_003_skewness_zscore_jerk(close: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(21).skew()
    z = (sk - sk.rolling(252).mean()) / (sk.rolling(252).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def vsk_drv3_004_vw_skew_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    v_rat = _safe_div(volume, _rolling_mean(volume, 21))
    weighted_ret = ret * v_rat
    sk = weighted_ret.rolling(21).skew()
    vel = sk.diff(5)
    return vel.diff(5)


def vsk_drv3_005_skew_drawdown_jerk(close: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(63).skew()
    h = close.rolling(252).max()
    dd = (h - close) / h
    val = sk * dd
    vel = val.diff(5)
    return vel.diff(5)


def vsk_drv3_006_panic_tail_intensity_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    sk = ret.rolling(63).skew()
    kt = ret.rolling(63).kurt()
    vol = ret.rolling(63).std()
    idx = _safe_div(sk * kt, vol + _EPS)
    vel = idx.diff(5)
    return vel.diff(5)


def vsk_drv3_007_skew_regime_shift_jerk(close: pd.Series) -> pd.Series:
    sk21 = close.pct_change().rolling(21).skew()
    sk252 = close.pct_change().rolling(252).skew()
    shift = sk21 - sk252
    vel = shift.diff(5)
    return vel.diff(5)


def vsk_drv3_008_skew_acceleration_jerk(close: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(21).skew()
    acc = sk.diff(5)
    vel = acc.diff(5)
    return vel.diff(5)


def vsk_drv3_009_skew_volume_div_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    sk_p = close.pct_change().rolling(63).skew()
    sk_v = volume.rolling(63).skew()
    div = sk_p - sk_v
    vel = div.diff(5)
    return vel.diff(5)


def vsk_drv3_010_joint_skew_kurt_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    idx = ret.rolling(63).skew() * ret.rolling(63).kurt()
    z = (idx - idx.rolling(252).mean()) / (idx.rolling(252).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def vsk_drv3_011_realized_asymmetry_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    idx = _safe_div(ret.rolling(21).median() - ret.rolling(21).mean(), ret.rolling(21).std())
    vel = idx.diff(5)
    return vel.diff(5)


def vsk_drv3_012_pearson_skewness_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    ps = 3 * _safe_div(ret.rolling(21).mean() - ret.rolling(21).median(), ret.rolling(21).std())
    vel = ps.diff(5)
    return vel.diff(5)


def vsk_drv3_013_tail_risk_expansion_jerk(close: pd.Series) -> pd.Series:
    sk21 = close.pct_change().rolling(21).skew()
    idx = _safe_div(sk21, sk21.rolling(252).mean().abs() + _EPS)
    vel = idx.diff(5)
    return vel.diff(5)


def vsk_drv3_014_dv_weighted_skew_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    v_rat = _safe_div(volume, volume.rolling(252).median())
    weighted_ret = ret.where(ret < 0, 0) * v_rat
    sk = weighted_ret.rolling(63).skew()
    vel = sk.diff(5)
    return vel.diff(5)


def vsk_drv3_015_skew_volatility_spread_jerk(close: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(21).skew()
    vol = close.pct_change().rolling(21).std() * np.sqrt(252)
    v_norm = (vol - vol.rolling(252).mean()) / (vol.rolling(252).std() + _EPS)
    spr = sk - v_norm
    vel = spr.diff(5)
    return vel.diff(5)


def vsk_drv3_016_panic_climax_velocity_jerk(close: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(21).skew()
    v_sk = sk.diff(5)
    dv = np.log(close).diff(5).abs()
    score = v_sk.clip(upper=0).abs() * dv
    vel = score.diff(5)
    return vel.diff(5)


def vsk_drv3_017_mktcap_skew_energy_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    ret = mc.pct_change()
    idx = (ret.rolling(63).skew()**2) * ret.rolling(63).std()
    vel = idx.diff(5)
    return vel.diff(5)


def vsk_drv3_018_skew_reversal_climax_jerk(close: pd.Series, low: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(21).skew()
    v_sk = sk.diff(5)
    c_low = _safe_div(close, low)
    vel = (v_sk * c_low).diff(5)
    return vel.diff(5)


def vsk_drv3_019_sustained_asymmetry_jerk(close: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(21).skew()
    q25 = sk.rolling(252).quantile(0.25)
    idx = (sk < q25).rolling(252).mean()
    vel = idx.diff(5)
    return vel.diff(5)


def vsk_drv3_020_skew_regime_break_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    brk = ret.rolling(21).skew() - ret.rolling(126).skew()
    vel = brk.diff(5)
    return vel.diff(5)


def vsk_drv3_021_cumulative_skew_energy_jerk(close: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(21).skew()
    energy = sk.cumsum() / (sk.abs().cumsum() + _EPS)
    vel = energy.diff(5)
    return vel.diff(5)


def vsk_drv3_022_final_vsk_fear_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vsk_150_vol_skew_final_fear_index(close, volume)
    vel = score.diff(5)
    return vel.diff(5)


def vsk_drv3_023_consecutive_neg_skew_jerk(close: pd.Series) -> pd.Series:
    sk = close.pct_change().rolling(21).skew()
    neg = (sk < 0).astype(int)
    dur = neg.groupby((neg == 0).cumsum()).cumsum()
    vel = dur.diff(5)
    return vel.diff(5)


def vsk_drv3_024_mktcap_skew_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    sk = mc.pct_change().rolling(63).skew()
    vel = sk.diff(5)
    return vel.diff(5)


def vcl_drv3_025_vol_skew_composite_jerk(close: pd.Series) -> pd.Series:
    score = vsk_075_volatility_skewness_final_composite(close)
    vel = score.diff(5)
    return vel.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V27_A_REGISTRY = {
    "vsk_drv3_001_return_skew_21d_jerk": {"inputs": ["close"], "func": vsk_drv3_001_return_skew_21d_jerk},
    "vsk_drv3_002_down_up_skew_jerk": {"inputs": ["close"], "func": vsk_drv3_002_down_up_skew_jerk},
    "vsk_drv3_003_skewness_zscore_jerk": {"inputs": ["close"], "func": vsk_drv3_003_skewness_zscore_jerk},
    "vsk_drv3_004_vw_skew_jerk": {"inputs": ["close", "volume"], "func": vsk_drv3_004_vw_skew_jerk},
    "vsk_drv3_005_skew_drawdown_jerk": {"inputs": ["close"], "func": vsk_drv3_005_skew_drawdown_jerk},
    "vsk_drv3_006_panic_tail_intensity_jerk": {"inputs": ["close"], "func": vsk_drv3_006_panic_tail_intensity_jerk},
    "vsk_drv3_007_skew_regime_shift_jerk": {"inputs": ["close"], "func": vsk_drv3_007_skew_regime_shift_jerk},
    "vsk_drv3_008_skew_acceleration_jerk": {"inputs": ["close"], "func": vsk_drv3_008_skew_acceleration_jerk},
    "vsk_drv3_009_skew_volume_div_jerk": {"inputs": ["close", "volume"], "func": vsk_drv3_009_skew_volume_div_jerk},
    "vsk_drv3_010_joint_skew_kurt_jerk": {"inputs": ["close"], "func": vsk_drv3_010_joint_skew_kurt_jerk},
    "vsk_drv3_011_realized_asymmetry_jerk": {"inputs": ["close"], "func": vsk_drv3_011_realized_asymmetry_jerk},
    "vsk_drv3_012_pearson_skewness_jerk": {"inputs": ["close"], "func": vsk_drv3_012_pearson_skewness_jerk},
    "vsk_drv3_013_tail_risk_expansion_jerk": {"inputs": ["close"], "func": vsk_drv3_013_tail_risk_expansion_jerk},
    "vsk_drv3_014_dv_weighted_skew_jerk": {"inputs": ["close", "volume"], "func": vsk_drv3_014_dv_weighted_skew_jerk},
    "vsk_drv3_015_skew_volatility_spread_jerk": {"inputs": ["close"], "func": vsk_drv3_015_skew_volatility_spread_jerk},
    "vsk_drv3_016_panic_climax_velocity_jerk": {"inputs": ["close"], "func": vsk_drv3_016_panic_climax_velocity_jerk},
    "vsk_drv3_017_mktcap_skew_energy_jerk": {"inputs": ["close", "sharesbas"], "func": vsk_drv3_017_mktcap_skew_energy_jerk},
    "vsk_drv3_018_skew_reversal_climax_jerk": {"inputs": ["close", "low"], "func": vsk_drv3_018_skew_reversal_climax_jerk},
    "vsk_drv3_019_sustained_asymmetry_jerk": {"inputs": ["close"], "func": vsk_drv3_019_sustained_asymmetry_jerk},
    "vsk_drv3_020_skew_regime_break_jerk": {"inputs": ["close"], "func": vsk_drv3_020_skew_regime_break_jerk},
    "vsk_drv3_021_cumulative_skew_energy_jerk": {"inputs": ["close"], "func": vsk_drv3_021_cumulative_skew_energy_jerk},
    "vsk_drv3_022_final_vsk_fear_jerk": {"inputs": ["close", "volume"], "func": vsk_drv3_022_final_vsk_fear_jerk},
    "vsk_drv3_023_consecutive_neg_skew_jerk": {"inputs": ["close"], "func": vsk_drv3_023_consecutive_neg_skew_jerk},
    "vsk_drv3_024_mktcap_skew_jerk": {"inputs": ["close", "sharesbas"], "func": vsk_drv3_024_mktcap_skew_jerk},
    "vsk_drv3_025_vol_skew_composite_jerk": {"inputs": ["close"], "func": vcl_drv3_025_vol_skew_composite_jerk},
}
