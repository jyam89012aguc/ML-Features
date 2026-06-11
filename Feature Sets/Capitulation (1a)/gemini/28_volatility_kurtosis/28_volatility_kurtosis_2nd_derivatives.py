"""
28_volatility_kurtosis — 2nd Derivatives
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


# ── Feature functions ────────────────────────────────────────────────────────

# 25 features capturing acceleration of volatility kurtosis metrics
def vkt_drv2_001_return_kurt_21d_velocity(close: pd.Series) -> pd.Series:
    # Change in short-term return kurtosis
    kt = close.pct_change().rolling(21).kurt()
    return kt.diff(5)


def vkt_drv2_002_outlier_density_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    s = ret.rolling(252).std()
    m = ret.rolling(252).mean()
    is_outlier = (ret.abs() > m + 3 * s).astype(int)
    cnt = is_outlier.rolling(63).sum()
    return cnt.diff(5)


def vkt_drv2_003_tail_to_body_ratio_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change().abs()
    ratio = _safe_div(ret.rolling(252).quantile(0.99), ret.rolling(252).median())
    return ratio.diff(5)


def vkt_drv2_004_kurtosis_zscore_velocity(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(21).kurt()
    z = (kt - kt.rolling(252).mean()) / (kt.rolling(252).std() + _EPS)
    return z.diff(5)


def vkt_drv2_005_vw_kurt_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    v_rat = _safe_div(volume, volume.rolling(252).median())
    weighted_ret = ret * v_rat
    kt = weighted_ret.rolling(21).kurt()
    return kt.diff(5)


def vkt_drv2_006_kurt_drawdown_velocity(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(63).kurt()
    h = close.rolling(252).max()
    dd = (h - close) / h
    return (kt * dd).diff(5)


def vkt_drv2_007_climax_fat_tail_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    kt = ret.rolling(63).kurt()
    vol = ret.rolling(63).std()
    idx = _safe_div(kt, vol + _EPS)
    return idx.diff(5)


def vkt_drv2_008_kurtosis_regime_shift_velocity(close: pd.Series) -> pd.Series:
    kt21 = close.pct_change().rolling(21).kurt()
    kt252 = close.pct_change().rolling(252).kurt()
    shift = kt21 - kt252
    return shift.diff(5)


def vkt_drv2_009_kurtosis_gradient_velocity(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(21).kurt()
    def _slope(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).slope
    sl = kt.rolling(21).apply(_slope, raw=True)
    return sl.diff(5)


def vkt_drv2_010_tail_integral_ratio_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    s = ret.rolling(252).std()
    outlier_val = ret.abs().where(ret.abs() > 2 * s, 0)
    ratio = _safe_div(outlier_val.rolling(63).sum(), outlier_val.rolling(252).sum())
    return ratio.diff(5)


def vkt_drv2_011_kurtosis_oscillator_velocity(close: pd.Series) -> pd.Series:
    kt21 = close.pct_change().rolling(21).kurt()
    kt63 = close.pct_change().rolling(63).kurt()
    osc = _safe_div(kt21, kt63) - 1.0
    return osc.diff(5)


def vkt_drv2_012_fat_tail_exhaustion_velocity(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(21).kurt()
    pv = np.log(close).diff(21).abs()
    score = _safe_div(kt, pv + _EPS)
    return score.diff(5)


def vkt_drv2_013_mktcap_kurtosis_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    kt = mc.pct_change().rolling(63).kurt()
    return kt.diff(5)


def vkt_drv2_014_kurtosis_reversal_climax_velocity(close: pd.Series, volume: pd.Series, low: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(21).kurt()
    v_rat = _safe_div(volume, volume.rolling(252).median())
    c_low = _safe_div(close, low)
    score = kt.diff(5) * v_rat * c_low
    return score.diff(5)


def vkt_drv2_015_sustained_tail_density_velocity(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(21).kurt()
    q90 = kt.rolling(252).quantile(0.9)
    idx = (kt > q90).rolling(252).mean()
    return idx.diff(5)


def vkt_drv2_016_ratio_kurt_to_dd_vel_velocity(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(21).kurt()
    dv = np.log(close).diff(21).abs()
    ratio = _safe_div(kt, dv + _EPS)
    return ratio.diff(5)


def vkt_drv2_017_cumulative_kurt_energy_velocity(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(21).kurt()
    energy = kt.cumsum() / (kt.abs().cumsum() + _EPS)
    return energy.diff(5)


def vkt_drv2_018_vkt_final_exhaustion_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vkt_150_vol_kurt_final_exhaustion_index(close, volume)
    return score.diff(5)


def vkt_drv2_019_kurtosis_pct_rank_velocity(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(63).kurt()
    rank = kt.expanding().rank(pct=True)
    return rank.diff(5)


def vkt_drv2_020_kurtosis_vol_corr_velocity(close: pd.Series) -> pd.Series:
    v = close.pct_change().rolling(21).std()
    k = close.pct_change().rolling(21).kurt()
    corr = v.rolling(63).corr(k)
    return corr.diff(5)


def vkt_drv2_021_outlier_magnitude_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    s = ret.rolling(252).std()
    outliers = ret.abs().where(ret.abs() > 2 * s, 0)
    idx = outliers.rolling(63).mean()
    return idx.diff(5)


def vkt_drv2_022_kurt_stability_velocity(close: pd.Series) -> pd.Series:
    kt = close.pct_change().rolling(21).kurt()
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = kt.rolling(21).apply(_rsq, raw=True)
    return rs.diff(5)


def vkt_drv2_023_ratio_fat_tails_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    spread_95 = ret.rolling(252).quantile(0.95) - ret.rolling(252).quantile(0.05)
    spread_iqr = ret.rolling(252).quantile(0.75) - ret.rolling(252).quantile(0.25)
    ratio = _safe_div(spread_95, spread_iqr)
    return ratio.diff(5)


def vkt_drv2_024_neg_outlier_vol_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    ret = close.pct_change()
    s = ret.rolling(252).std()
    is_neg_outlier = (ret < -3 * s)
    ratio = _safe_div(volume.where(is_neg_outlier, 0).rolling(63).sum(), volume.rolling(63).sum())
    return ratio.diff(5)


def vkt_drv2_025_volatility_kurtosis_composite_velocity(close: pd.Series) -> pd.Series:
    score = vkt_075_volatility_kurtosis_final_composite(close)
    return score.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V28_V_REGISTRY = {
    "vkt_drv2_001_return_kurt_21d_velocity": {"inputs": ["close"], "func": vkt_drv2_001_return_kurt_21d_velocity},
    "vkt_drv2_002_outlier_density_velocity": {"inputs": ["close"], "func": vkt_drv2_002_outlier_density_velocity},
    "vkt_drv2_003_tail_to_body_ratio_velocity": {"inputs": ["close"], "func": vkt_drv2_003_tail_to_body_ratio_velocity},
    "vkt_drv2_004_kurtosis_zscore_velocity": {"inputs": ["close"], "func": vkt_drv2_004_kurtosis_zscore_velocity},
    "vkt_drv2_005_vw_kurt_velocity": {"inputs": ["close", "volume"], "func": vkt_drv2_005_vw_kurt_velocity},
    "vkt_drv2_006_kurt_drawdown_velocity": {"inputs": ["close"], "func": vkt_drv2_006_kurt_drawdown_velocity},
    "vkt_drv2_007_climax_fat_tail_velocity": {"inputs": ["close"], "func": vkt_drv2_007_climax_fat_tail_velocity},
    "vkt_drv2_008_kurtosis_regime_shift_velocity": {"inputs": ["close"], "func": vkt_drv2_008_kurtosis_regime_shift_velocity},
    "vkt_drv2_009_kurtosis_gradient_velocity": {"inputs": ["close"], "func": vkt_drv2_009_kurtosis_gradient_velocity},
    "vkt_drv2_010_tail_integral_ratio_velocity": {"inputs": ["close"], "func": vkt_drv2_010_tail_integral_ratio_velocity},
    "vkt_drv2_011_kurtosis_oscillator_velocity": {"inputs": ["close"], "func": vkt_drv2_011_kurtosis_oscillator_velocity},
    "vkt_drv2_012_fat_tail_exhaustion_velocity": {"inputs": ["close"], "func": vkt_drv2_012_fat_tail_exhaustion_velocity},
    "vkt_drv2_013_mktcap_kurtosis_velocity": {"inputs": ["close", "sharesbas"], "func": vkt_drv2_013_mktcap_kurtosis_velocity},
    "vkt_drv2_014_kurtosis_reversal_climax_velocity": {"inputs": ["close", "volume", "low"], "func": vkt_drv2_014_kurtosis_reversal_climax_velocity},
    "vkt_drv2_015_sustained_tail_density_velocity": {"inputs": ["close"], "func": vkt_drv2_015_sustained_tail_density_velocity},
    "vkt_drv2_016_ratio_kurt_to_dd_vel_velocity": {"inputs": ["close"], "func": vkt_drv2_016_ratio_kurt_to_dd_vel_velocity},
    "vkt_drv2_017_cumulative_kurt_energy_velocity": {"inputs": ["close"], "func": vkt_drv2_017_cumulative_kurt_energy_velocity},
    "vkt_drv2_018_vkt_final_exhaustion_velocity": {"inputs": ["close", "volume"], "func": vkt_drv2_018_vkt_final_exhaustion_velocity},
    "vkt_drv2_019_kurtosis_pct_rank_velocity": {"inputs": ["close"], "func": vkt_drv2_019_kurtosis_pct_rank_velocity},
    "vkt_drv2_020_kurtosis_vol_corr_velocity": {"inputs": ["close"], "func": vkt_drv2_020_kurtosis_vol_corr_velocity},
    "vkt_drv2_021_outlier_magnitude_velocity": {"inputs": ["close"], "func": vkt_drv2_021_outlier_magnitude_velocity},
    "vkt_drv2_022_kurt_stability_velocity": {"inputs": ["close"], "func": vkt_drv2_022_kurt_stability_velocity},
    "vkt_drv2_023_ratio_fat_tails_velocity": {"inputs": ["close"], "func": vkt_drv2_023_ratio_fat_tails_velocity},
    "vkt_drv2_024_neg_outlier_vol_velocity": {"inputs": ["close", "volume"], "func": vkt_drv2_024_neg_outlier_vol_velocity},
    "vkt_drv2_025_volatility_kurtosis_composite_velocity": {"inputs": ["close"], "func": vkt_drv2_025_volatility_kurtosis_composite_velocity},
}
