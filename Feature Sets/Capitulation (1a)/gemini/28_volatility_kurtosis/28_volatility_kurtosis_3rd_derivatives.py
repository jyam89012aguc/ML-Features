"""
28_volatility_kurtosis — 3rd Derivatives
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

# 25 features capturing exhaustion/inflection of volatility kurtosis acceleration (jerk)
def vkt_drv3_001_return_kurt_21d_jerk(close: pd.Series) -> pd.Series:
    # Rate of change of kurtosis velocity
    kt = close.pct_change().rolling(21).kurt()
    vel = kt.diff(5)
    return vel.diff(5)


def vkt_drv3_002_outlier_density_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    s = ret.rolling(252).std()
    m = ret.rolling(252).mean()
    is_outlier = (ret.abs() > m + 3 * s).astype(int)
    cnt = is_outlier.rolling(63).sum()
    vel = cnt.diff(5)
    return vel.diff(5)


def vkt_drv3_003_tail_to_body_ratio_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change().abs()
    ratio = _safe_div(ret.rolling(252).quantile(0.99), ret.rolling(252).median())
    vel = ratio.diff(5)
    return vel.diff(5)


def vkt_drv3_004_kurtosis_zscore_jerk(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(21).kurt()
    z = (kt - kt.rolling(252).mean()) / (kt.rolling(252).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def vkt_drv3_005_vw_kurt_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    v_rat = _safe_div(volume, volume.rolling(252).median())
    weighted_ret = ret * v_rat
    kt = weighted_ret.rolling(21).kurt()
    vel = kt.diff(5)
    return vel.diff(5)


def vkt_drv3_006_kurt_drawdown_jerk(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(63).kurt()
    h = close.rolling(252).max()
    dd = (h - close) / h
    val = kt * dd
    vel = val.diff(5)
    return vel.diff(5)


def vkt_drv3_007_climax_fat_tail_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    kt = ret.rolling(63).kurt()
    vol = ret.rolling(63).std()
    idx = _safe_div(kt, vol + _EPS)
    vel = idx.diff(5)
    return vel.diff(5)


def vkt_drv3_008_kurtosis_regime_shift_jerk(close: pd.Series) -> pd.Series:
    kt21 = close.pct_change().rolling(21).kurt()
    kt252 = close.pct_change().rolling(252).kurt()
    shift = kt21 - kt252
    vel = shift.diff(5)
    return vel.diff(5)


def vkt_drv3_009_kurtosis_gradient_jerk(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(21).kurt()
    def _slope(y):
        from scipy.stats import linregress
        if len(y) < 2: return 0.0
        return linregress(np.arange(len(y)), y).slope
    sl = kt.rolling(21).apply(_slope, raw=True)
    vel = sl.diff(5)
    return vel.diff(5)


def vkt_drv3_010_tail_integral_ratio_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    s = ret.rolling(252).std()
    outlier_val = ret.abs().where(ret.abs() > 2 * s, 0)
    ratio = _safe_div(outlier_val.rolling(63).sum(), outlier_val.rolling(252).sum())
    vel = ratio.diff(5)
    return vel.diff(5)


def vkt_drv3_011_kurtosis_oscillator_jerk(close: pd.Series) -> pd.Series:
    kt21 = close.pct_change().rolling(21).kurt()
    kt63 = close.pct_change().rolling(63).kurt()
    osc = _safe_div(kt21, kt63) - 1.0
    vel = osc.diff(5)
    return vel.diff(5)


def vkt_drv3_012_fat_tail_exhaustion_jerk(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(21).kurt()
    pv = np.log(close).diff(21).abs()
    score = _safe_div(kt, pv + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def vkt_drv3_013_mktcap_kurtosis_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    kt = mc.pct_change().rolling(63).kurt()
    vel = kt.diff(5)
    return vel.diff(5)


def vkt_drv3_014_kurtosis_reversal_climax_jerk(close: pd.Series, volume: pd.Series, low: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(21).kurt()
    v_rat = _safe_div(volume, volume.rolling(252).median())
    c_low = _safe_div(close, low)
    score = kt.diff(5) * v_rat * c_low
    vel = score.diff(5)
    return vel.diff(5)


def vsk_drv3_015_sustained_tail_density_jerk(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(21).kurt()
    q90 = kt.rolling(252).quantile(0.9)
    idx = (kt > q90).rolling(252).mean()
    vel = idx.diff(5)
    return vel.diff(5)


def vkt_drv3_016_ratio_kurt_to_dd_vel_jerk(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(21).kurt()
    dv = np.log(close).diff(21).abs()
    ratio = _safe_div(kt, dv + _EPS)
    vel = ratio.diff(5)
    return vel.diff(5)


def vkt_drv3_017_cumulative_kurt_energy_jerk(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(21).kurt()
    energy = kt.cumsum() / (kt.abs().cumsum() + _EPS)
    vel = energy.diff(5)
    return vel.diff(5)


def vkt_drv3_018_vkt_final_exhaustion_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    from scipy.stats import linregress
    score = vkt_150_vol_kurt_final_exhaustion_index(close, volume)
    vel = score.diff(5)
    return vel.diff(5)


def vkt_drv3_019_kurtosis_pct_rank_jerk(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(63).kurt()
    rank = kt.expanding().rank(pct=True)
    vel = rank.diff(5)
    return vel.diff(5)


def vkt_drv3_020_kurtosis_vol_corr_jerk(close: pd.Series) -> pd.Series:
    v = close.pct_change().rolling(21).std()
    k = close.pct_change().rolling(21).kurt()
    corr = v.rolling(63).corr(k)
    vel = corr.diff(5)
    return vel.diff(5)


def vkt_drv3_021_outlier_magnitude_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    s = ret.rolling(252).std()
    outliers = ret.abs().where(ret.abs() > 2 * s, 0)
    idx = outliers.rolling(63).mean()
    vel = idx.diff(5)
    return vel.diff(5)


def vkt_drv3_022_kurt_stability_jerk(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(21).kurt()
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = kt.rolling(21).apply(_rsq, raw=True)
    vel = rs.diff(5)
    return vel.diff(5)


def vkt_drv3_023_ratio_fat_tails_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    spread_95 = ret.rolling(252).quantile(0.95) - ret.rolling(252).quantile(0.05)
    spread_iqr = ret.rolling(252).quantile(0.75) - ret.rolling(252).quantile(0.25)
    ratio = _safe_div(spread_95, spread_iqr)
    vel = ratio.diff(5)
    return vel.diff(5)


def vkt_drv3_024_neg_outlier_vol_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    s = ret.rolling(252).std()
    is_neg_outlier = (ret < -3 * s)
    ratio = _safe_div(volume.where(is_neg_outlier, 0).rolling(63).sum(), volume.rolling(63).sum())
    vel = ratio.diff(5)
    return vel.diff(5)


def vkt_drv3_025_volatility_kurtosis_composite_jerk(close: pd.Series) -> pd.Series:
    score = vkt_075_volatility_kurtosis_final_composite(close)
    vel = score.diff(5)
    return vel.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V28_A_REGISTRY = {
    "vkt_drv3_001_return_kurt_21d_jerk": {"inputs": ["close"], "func": vkt_drv3_001_return_kurt_21d_jerk},
    "vkt_drv3_002_outlier_density_jerk": {"inputs": ["close"], "func": vkt_drv3_002_outlier_density_jerk},
    "vkt_drv3_003_tail_to_body_ratio_jerk": {"inputs": ["close"], "func": vkt_drv3_003_tail_to_body_ratio_jerk},
    "vkt_drv3_004_kurtosis_zscore_jerk": {"inputs": ["close"], "func": vkt_drv3_004_kurtosis_zscore_jerk},
    "vkt_drv3_005_vw_kurt_jerk": {"inputs": ["close", "volume"], "func": vkt_drv3_005_vw_kurt_jerk},
    "vkt_drv3_006_kurt_drawdown_jerk": {"inputs": ["close"], "func": vkt_drv3_006_kurt_drawdown_jerk},
    "vkt_drv3_007_climax_fat_tail_jerk": {"inputs": ["close"], "func": vkt_drv3_007_climax_fat_tail_jerk},
    "vkt_drv3_008_kurtosis_regime_shift_jerk": {"inputs": ["close"], "func": vkt_drv3_008_kurtosis_regime_shift_jerk},
    "vkt_drv3_009_kurtosis_gradient_jerk": {"inputs": ["close"], "func": vkt_drv3_009_kurtosis_gradient_jerk},
    "vkt_drv3_010_tail_integral_ratio_jerk": {"inputs": ["close"], "func": vkt_drv3_010_tail_integral_ratio_jerk},
    "vkt_drv3_011_kurtosis_oscillator_jerk": {"inputs": ["close"], "func": vkt_drv3_011_kurtosis_oscillator_jerk},
    "vkt_drv3_012_fat_tail_exhaustion_jerk": {"inputs": ["close"], "func": vkt_drv3_012_fat_tail_exhaustion_jerk},
    "vkt_drv3_013_mktcap_kurtosis_jerk": {"inputs": ["close", "sharesbas"], "func": vkt_drv3_013_mktcap_kurtosis_jerk},
    "vkt_drv3_014_kurtosis_reversal_climax_jerk": {"inputs": ["close", "volume", "low"], "func": vkt_drv3_014_kurtosis_reversal_climax_jerk},
    "vkt_drv3_015_sustained_tail_density_jerk": {"inputs": ["close"], "func": vsk_drv3_015_sustained_tail_density_jerk},
    "vkt_drv3_016_ratio_kurt_to_dd_vel_jerk": {"inputs": ["close"], "func": vkt_drv3_016_ratio_kurt_to_dd_vel_jerk},
    "vkt_drv3_017_cumulative_kurt_energy_jerk": {"inputs": ["close"], "func": vkt_drv3_017_cumulative_kurt_energy_jerk},
    "vkt_drv3_018_vkt_final_exhaustion_jerk": {"inputs": ["close", "volume"], "func": vkt_drv3_018_vkt_final_exhaustion_jerk},
    "vkt_drv3_019_kurtosis_pct_rank_jerk": {"inputs": ["close"], "func": vkt_drv3_019_kurtosis_pct_rank_jerk},
    "vkt_drv3_020_kurtosis_vol_corr_jerk": {"inputs": ["close"], "func": vkt_drv3_020_kurtosis_vol_corr_jerk},
    "vkt_drv3_021_outlier_magnitude_jerk": {"inputs": ["close"], "func": vkt_drv3_021_outlier_magnitude_jerk},
    "vkt_drv3_022_kurt_stability_jerk": {"inputs": ["close"], "func": vkt_drv3_022_kurt_stability_jerk},
    "vkt_drv3_023_ratio_fat_tails_jerk": {"inputs": ["close"], "func": vkt_drv3_023_ratio_fat_tails_jerk},
    "vkt_drv3_024_neg_outlier_vol_jerk": {"inputs": ["close", "volume"], "func": vkt_drv3_024_neg_outlier_vol_jerk},
    "vkt_drv3_025_volatility_kurtosis_composite_jerk": {"inputs": ["close"], "func": vkt_drv3_025_volatility_kurtosis_composite_jerk},
}
