"""
32_volatility_regime_shift — 2nd Derivatives
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

# 25 features capturing acceleration of volatility regime shift metrics
def vrs_drv2_001_vol_regime_ratio_velocity(close: pd.Series) -> pd.Series:
    # Change in the short/long vol ratio
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = np.log(close / close.shift(1)).rolling(252).std()
    ratio = _safe_div(v21, v252)
    return ratio.diff(5)


def vrs_drv2_002_vol_spread_zscore_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = np.log(close / close.shift(1)).rolling(252).std()
    spr = v21 - v252
    z = (spr - spr.rolling(252).mean()) / (spr.rolling(252).std() + _EPS)
    return z.diff(5)


def vrs_drv2_003_high_vol_state_persistence_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    med = v21.rolling(252).median()
    is_high = (v21 > med)
    prob = (is_high & is_high.shift(1)).rolling(63).sum() / (is_high.shift(1).rolling(63).sum() + _EPS)
    return prob.diff(5)


def vrs_drv2_004_vol_regime_switch_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    avg_v = v21.rolling(252).mean()
    cross = (v21 > avg_v) != (v21.shift(1) > avg_v.shift(1))
    cnt = cross.astype(int).rolling(252).sum()
    return cnt.diff(5)


def vrs_drv2_005_atr_regime_ratio_velocity(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    ratio = _safe_div(tr.rolling(21).mean(), tr.rolling(252).mean())
    return ratio.diff(5)


def vrs_drv2_006_vol_character_break_velocity(close: pd.Series) -> pd.Series:
    v5 = np.log(close / close.shift(1)).rolling(5).std()
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    idx = _safe_div(v5, v21)
    return idx.diff(5)


def vrs_drv2_007_vol_shock_regime_velocity_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    s = ret.rolling(252).std()
    freq = (ret.abs() > 2 * s).astype(int).rolling(63).mean()
    return freq.diff(5)


def vrs_drv2_008_vol_regime_stability_accel(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = v21.rolling(63).apply(_rsq, raw=True)
    return rs.diff(5)


def vrs_drv2_009_joint_vp_regime_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    vr = _safe_div(np.log(close / close.shift(1)).rolling(21).std(), np.log(close / close.shift(1)).rolling(252).std())
    vor = _safe_div(volume.rolling(21).mean(), volume.rolling(252).median())
    idx = vr * np.log(vor + _EPS)
    return idx.diff(5)


def vrs_drv2_010_mktcap_regime_shift_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v21 = np.log(mc / mc.shift(1)).rolling(21).std()
    v252 = np.log(mc / mc.shift(1)).rolling(252).std()
    ratio = _safe_div(v21, v252)
    return ratio.diff(5)


def vrs_drv2_011_regime_norm_dd_velocity_velocity(close: pd.Series) -> pd.Series:
    pv = np.log(close).diff(21).abs()
    vr = _safe_div(np.log(close / close.shift(1)).rolling(21).std(), np.log(close / close.shift(1)).rolling(252).std())
    idx = _safe_div(pv, vr + _EPS)
    return idx.diff(5)


def vrs_drv2_012_vol_regime_final_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vrs_075_vol_regime_shift_final_composite(close)
    return score.diff(5)


def vrs_drv2_013_vol_regime_ratio_pct_rank_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = np.log(close / close.shift(1)).rolling(252).std()
    ratio = _safe_div(v21, v252)
    rank = ratio.expanding().rank(pct=True)
    return rank.diff(5)


def vrs_drv2_014_vol_entropy_regime_velocity(close: pd.Series) -> pd.Series:
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y[~np.isnan(y)], bins=10, density=True)
        p = h / (np.sum(h) + _EPS)
        return -np.sum(p[p > 0] * np.log(p[p > 0]))
    ret = close.pct_change()
    e21 = ret.rolling(21).apply(_ent, raw=True)
    e252 = ret.rolling(252).apply(_ent, raw=True)
    ratio = _safe_div(e21, e252)
    return ratio.diff(5)


def vrs_drv2_015_turnover_regime_shift_velocity(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    tr = _safe_div(to.rolling(21).mean(), to.rolling(252).median())
    z = (tr - tr.rolling(252).mean()) / (tr.rolling(252).std() + _EPS)
    return z.diff(5)


def vrs_drv2_016_vol_clustering_regime_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change().abs()
    ac21 = ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    ac252 = ret.rolling(252).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    ratio = _safe_div(ac21, ac252)
    return ratio.diff(5)


def vrs_drv2_017_vol_breakaway_energy_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = np.log(close / close.shift(1)).rolling(252).std()
    vr = _safe_div(v21, v252)
    va = v21.diff(5).diff(5).abs()
    score = (vr**2) * va
    return score.diff(5)


def vrs_drv2_018_consecutive_regime_expanding_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = v21.rolling(252).mean()
    ratio = _safe_div(v21, v252)
    inc = (ratio > ratio.shift(1)) & (ratio > 1.0)
    dur = inc.astype(int).groupby((inc == 0).cumsum()).cumsum()
    return dur.diff(5)


def vrs_drv2_019_regime_reversal_climax_velocity(close: pd.Series, low: pd.Series) -> pd.Series:
    vr = _safe_div(np.log(close / close.shift(1)).rolling(21).std(), np.log(close / close.shift(1)).rolling(252).std())
    score = vr.diff(5) * _safe_div(close, low)
    return score.diff(5)


def vrs_drv2_020_sustained_hi_vol_regime_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252_avg = v21.rolling(252).mean()
    idx = (v21 > 1.5 * v252_avg).rolling(252).mean()
    return idx.diff(5)


def vrs_drv2_021_vol_regime_skew_div_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(5).std()
    v252 = v21.rolling(252).mean()
    ratio = _safe_div(v21, v252)
    div = ratio.rolling(63).skew() - ratio.rolling(252).skew()
    return div.diff(5)


def vrs_drv2_022_cumulative_regime_energy_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = v21.rolling(252).mean()
    ratio = _safe_div(v21, v252)
    energy = ratio.cumsum() / (ratio.abs().cumsum() + _EPS)
    return energy.diff(5)


def vrs_drv2_023_regime_weighted_fear_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    vr = _safe_div(np.log(close / close.shift(1)).rolling(21).std(), np.log(close / close.shift(1)).rolling(252).std())
    vs = _safe_div(volume, volume.rolling(252).median())
    h = close.rolling(252).max()
    l = close.rolling(252).min()
    rf = _safe_div(close - l, h - l)
    score = vr * vs * (1.0 - rf)
    return score.diff(5)


def vrs_drv2_024_vix_proxy_regime_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = np.log(close / close.shift(1)).rolling(252).std()
    ratio = _safe_div(v21, v252)
    z = (ratio - ratio.rolling(252).mean()) / (ratio.rolling(252).std() + _EPS)
    return z.diff(5)


def vrs_drv2_025_mktcap_regime_energy_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v21 = np.log(mc / mc.shift(1)).rolling(21).std()
    v252 = np.log(mc / mc.shift(1)).rolling(252).std()
    idx = _safe_div(v21, v252) * v21.diff(21)
    return idx.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V32_V_REGISTRY = {
    "vrs_drv2_001_vol_regime_ratio_velocity": {"inputs": ["close"], "func": vrs_drv2_001_vol_regime_ratio_velocity},
    "vrs_drv2_002_vol_spread_zscore_velocity": {"inputs": ["close"], "func": vrs_drv2_002_vol_spread_zscore_velocity},
    "vrs_drv2_003_high_vol_state_persistence_velocity": {"inputs": ["close"], "func": vrs_drv2_003_high_vol_state_persistence_velocity},
    "vrs_drv2_004_vol_regime_switch_velocity": {"inputs": ["close"], "func": vrs_drv2_004_vol_regime_switch_velocity},
    "vrs_drv2_005_atr_regime_ratio_velocity": {"inputs": ["high", "low", "close"], "func": vrs_drv2_005_atr_regime_ratio_velocity},
    "vrs_drv2_006_vol_character_break_velocity": {"inputs": ["close"], "func": vrs_drv2_006_vol_character_break_velocity},
    "vrs_drv2_007_vol_shock_regime_velocity_velocity": {"inputs": ["close"], "func": vrs_drv2_007_vol_shock_regime_velocity_velocity},
    "vrs_drv2_008_vol_regime_stability_accel": {"inputs": ["close"], "func": vrs_drv2_008_vol_regime_stability_accel},
    "vrs_drv2_009_joint_vp_regime_velocity": {"inputs": ["close", "volume"], "func": vrs_drv2_009_joint_vp_regime_velocity},
    "vrs_drv2_010_mktcap_vol_regime_shift_velocity": {"inputs": ["close", "sharesbas"], "func": vrs_drv2_010_mktcap_vol_regime_shift_velocity},
    "vrs_drv2_011_regime_norm_dd_velocity_velocity": {"inputs": ["close"], "func": vrs_drv2_011_regime_norm_dd_velocity_velocity},
    "vrs_drv2_012_vol_regime_final_velocity": {"inputs": ["close", "volume"], "func": vrs_drv2_012_vol_regime_final_velocity},
    "vrs_drv2_013_vol_regime_ratio_pct_rank_velocity": {"inputs": ["close"], "func": vrs_drv2_013_vol_regime_ratio_pct_rank_velocity},
    "vrs_drv2_014_vol_entropy_regime_velocity": {"inputs": ["close"], "func": vrs_drv2_014_vol_entropy_regime_velocity},
    "vrs_drv2_015_turnover_regime_shift_velocity": {"inputs": ["volume", "sharesbas"], "func": vrs_drv2_015_turnover_regime_shift_velocity},
    "vrs_drv2_016_vol_clustering_regime_velocity": {"inputs": ["close"], "func": vrs_drv2_016_vol_clustering_regime_velocity},
    "vrs_drv2_017_vol_breakaway_energy_velocity": {"inputs": ["close"], "func": vrs_drv2_017_vol_breakaway_energy_velocity},
    "vrs_drv2_018_consecutive_regime_expanding_velocity": {"inputs": ["close"], "func": vrs_drv2_018_consecutive_regime_expanding_velocity},
    "vrs_drv2_019_regime_reversal_climax_velocity": {"inputs": ["close", "low"], "func": vrs_drv2_019_regime_reversal_climax_velocity},
    "vrs_drv2_020_sustained_hi_vol_regime_velocity": {"inputs": ["close"], "func": vrs_drv2_020_sustained_hi_vol_regime_velocity},
    "vrs_drv2_021_vol_regime_skew_div_velocity": {"inputs": ["close"], "func": vrs_drv2_021_vol_regime_skew_div_velocity},
    "vrs_drv2_022_cumulative_regime_energy_velocity": {"inputs": ["close"], "func": vrs_drv2_022_cumulative_regime_energy_velocity},
    "vrs_drv2_023_regime_weighted_fear_velocity": {"inputs": ["close", "volume"], "func": vrs_drv2_023_regime_weighted_fear_velocity},
    "vrs_drv2_024_vix_proxy_regime_velocity": {"inputs": ["close"], "func": vrs_drv2_024_vix_proxy_regime_velocity},
    "vrs_drv2_025_mktcap_regime_energy_velocity": {"inputs": ["close", "sharesbas"], "func": vrs_drv2_025_mktcap_regime_energy_velocity},
}
