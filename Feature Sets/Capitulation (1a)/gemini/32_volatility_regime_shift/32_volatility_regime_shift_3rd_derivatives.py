"""
32_volatility_regime_shift — 3rd Derivatives
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

# 25 features capturing exhaustion/inflection of volatility regime shift acceleration (jerk)
def vrs_drv3_001_vol_regime_ratio_jerk(close: pd.Series) -> pd.Series:
    # Rate of change of vol regime ratio velocity
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = np.log(close / close.shift(1)).rolling(252).std()
    ratio = _safe_div(v21, v252)
    vel = ratio.diff(5)
    return vel.diff(5)


def vrs_drv3_002_vol_spread_zscore_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = np.log(close / close.shift(1)).rolling(252).std()
    spr = v21 - v252
    z = (spr - spr.rolling(252).mean()) / (spr.rolling(252).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def vrs_drv3_003_high_vol_state_persistence_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    med = v21.rolling(252).median()
    is_high = (v21 > med)
    prob = (is_high & is_high.shift(1)).rolling(63).sum() / (is_high.shift(1).rolling(63).sum() + _EPS)
    vel = prob.diff(5)
    return vel.diff(5)


def vrs_drv3_004_vol_regime_switch_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    avg_v = v21.rolling(252).mean()
    cross = (v21 > avg_v) != (v21.shift(1) > avg_v.shift(1))
    cnt = cross.astype(int).rolling(252).sum()
    vel = cnt.diff(5)
    return vel.diff(5)


def vrs_drv3_005_atr_regime_ratio_jerk(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    ratio = _safe_div(tr.rolling(21).mean(), tr.rolling(252).mean())
    vel = ratio.diff(5)
    return vel.diff(5)


def vrs_drv3_006_vol_character_break_jerk(close: pd.Series) -> pd.Series:
    v5 = np.log(close / close.shift(1)).rolling(5).std()
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    idx = _safe_div(v5, v21)
    vel = idx.diff(5)
    return vel.diff(5)


def vrs_drv3_007_vol_shock_regime_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    s = ret.rolling(252).std()
    freq = (ret.abs() > 2 * s).astype(int).rolling(63).mean()
    vel = freq.diff(5)
    return vel.diff(5)


def vrs_drv3_008_vol_regime_stability_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    def _rsq(y):
        if len(y) < 2: return 0.0
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = v21.rolling(63).apply(_rsq, raw=True)
    vel = rs.diff(5)
    return vel.diff(5)


def vrs_drv3_009_joint_vp_regime_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    vr = _safe_div(np.log(close / close.shift(1)).rolling(21).std(), np.log(close / close.shift(1)).rolling(252).std())
    vor = _safe_div(volume.rolling(21).mean(), volume.rolling(252).median())
    idx = vr * np.log(vor + _EPS)
    vel = idx.diff(5)
    return vel.diff(5)


def vrs_drv3_010_mktcap_regime_shift_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v21 = np.log(mc / mc.shift(1)).rolling(21).std()
    v252 = np.log(mc / mc.shift(1)).rolling(252).std()
    ratio = _safe_div(v21, v252)
    vel = ratio.diff(5)
    return vel.diff(5)


def vrs_drv3_011_regime_norm_dd_velocity_jerk(close: pd.Series) -> pd.Series:
    pv = np.log(close).diff(21).abs()
    vr = _safe_div(np.log(close / close.shift(1)).rolling(21).std(), np.log(close / close.shift(1)).rolling(252).std())
    idx = _safe_div(pv, vr + _EPS)
    vel = idx.diff(5)
    return vel.diff(5)


def vrs_drv3_012_vol_regime_final_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vrs_075_vol_regime_shift_final_composite(close)
    vel = score.diff(5)
    return vel.diff(5)


def vrs_drv3_013_vol_regime_ratio_pct_rank_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = np.log(close / close.shift(1)).rolling(252).std()
    ratio = _safe_div(v21, v252)
    rank = ratio.expanding().rank(pct=True)
    vel = rank.diff(5)
    return vel.diff(5)


def vrs_drv3_014_vol_entropy_regime_jerk(close: pd.Series) -> pd.Series:
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y, bins=10, density=True)
        p = h / (np.sum(h) + _EPS)
        return -np.sum(p[p > 0] * np.log(p[p > 0]))
    ret = close.pct_change()
    e21 = ret.rolling(21).apply(_ent, raw=True)
    e252 = ret.rolling(252).apply(_ent, raw=True)
    ratio = _safe_div(e21, e252)
    vel = ratio.diff(5)
    return vel.diff(5)


def vrs_drv3_015_turnover_regime_shift_jerk(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    tr = _safe_div(to.rolling(21).mean(), to.rolling(252).median())
    z = (tr - tr.rolling(252).mean()) / (tr.rolling(252).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def vrs_drv3_016_vol_clustering_regime_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change().abs()
    ac21 = ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    ac252 = ret.rolling(252).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    ratio = _safe_div(ac21, ac252)
    vel = ratio.diff(5)
    return vel.diff(5)


def vrs_drv3_017_vol_breakaway_energy_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = np.log(close / close.shift(1)).rolling(252).std()
    vr = _safe_div(v21, v252)
    va = v21.diff(5).diff(5).abs()
    score = (vr**2) * va
    vel = score.diff(5)
    return vel.diff(5)


def vrs_drv3_018_consecutive_regime_expanding_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = v21.rolling(252).mean()
    ratio = _safe_div(v21, v252)
    inc = (ratio > ratio.shift(1)) & (ratio > 1.0)
    dur = inc.astype(int).groupby((inc == 0).cumsum()).cumsum()
    vel = dur.diff(5)
    return vel.diff(5)


def vrs_drv3_019_regime_reversal_climax_jerk(close: pd.Series, low: pd.Series) -> pd.Series:
    vr = _safe_div(np.log(close / close.shift(1)).rolling(21).std(), np.log(close / close.shift(1)).rolling(252).std())
    score = vr.diff(5) * _safe_div(close, low + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def vrs_drv3_020_sustained_hi_vol_regime_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252_avg = v21.rolling(252).mean()
    idx = (v21 > 1.5 * v252_avg).rolling(252).mean()
    vel = idx.diff(5)
    return vel.diff(5)


def vrs_drv3_021_vol_regime_skew_div_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(5).std()
    v252 = v21.rolling(252).mean()
    ratio = _safe_div(v21, v252)
    div = ratio.rolling(63).skew() - ratio.rolling(252).skew()
    vel = div.diff(5)
    return vel.diff(5)


def vrs_drv3_022_cumulative_regime_energy_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = v21.rolling(252).mean()
    ratio = _safe_div(v21, v252)
    energy = ratio.cumsum() / (ratio.abs().cumsum() + _EPS)
    vel = energy.diff(5)
    return vel.diff(5)


def vrs_drv3_023_regime_weighted_fear_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    vr = _safe_div(np.log(close / close.shift(1)).rolling(21).std(), np.log(close / close.shift(1)).rolling(252).std())
    vs = _safe_div(volume, volume.rolling(252).median())
    h = close.rolling(252).max()
    l = close.rolling(252).min()
    rf = _safe_div(close - l, h - l)
    score = vr * vs * (1.0 - rf)
    vel = score.diff(5)
    return vel.diff(5)


def vrs_drv3_024_vix_proxy_regime_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    v252 = np.log(close / close.shift(1)).rolling(252).std()
    ratio = _safe_div(v21, v252)
    z = (ratio - ratio.rolling(252).mean()) / (ratio.rolling(252).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def vrs_drv3_025_mktcap_regime_energy_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v21 = np.log(mc / mc.shift(1)).rolling(21).std()
    v252 = np.log(mc / mc.shift(1)).rolling(252).std()
    idx = _safe_div(v21, v252) * v21.diff(21)
    vel = idx.diff(5)
    return vel.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V32_A_REGISTRY = {
    "vrs_drv3_001_vol_regime_ratio_jerk": {"inputs": ["close"], "func": vrs_drv3_001_vol_regime_ratio_jerk},
    "vrs_drv3_002_vol_spread_zscore_jerk": {"inputs": ["close"], "func": vrs_drv3_002_vol_spread_zscore_jerk},
    "vrs_drv3_003_high_vol_state_persistence_jerk": {"inputs": ["close"], "func": vrs_drv3_003_high_vol_state_persistence_jerk},
    "vrs_drv3_004_vol_regime_switch_jerk": {"inputs": ["close"], "func": vrs_drv3_004_vol_regime_switch_jerk},
    "vrs_drv3_005_atr_regime_ratio_jerk": {"inputs": ["high", "low", "close"], "func": vrs_drv3_005_atr_regime_ratio_jerk},
    "vrs_drv3_006_vol_character_break_jerk": {"inputs": ["close"], "func": vrs_drv3_006_vol_character_break_jerk},
    "vrs_drv3_007_vol_shock_regime_jerk": {"inputs": ["close"], "func": vrs_drv3_007_vol_shock_regime_jerk},
    "vrs_drv3_008_vol_regime_stability_jerk": {"inputs": ["close"], "func": vrs_drv3_008_vol_regime_stability_jerk},
    "vrs_drv3_009_joint_vp_regime_jerk": {"inputs": ["close", "volume"], "func": vrs_drv3_009_joint_vp_regime_jerk},
    "vrs_drv3_010_mktcap_regime_shift_jerk": {"inputs": ["close", "sharesbas"], "func": vrs_drv3_010_mktcap_regime_shift_jerk},
    "vrs_drv3_011_regime_norm_dd_velocity_jerk": {"inputs": ["close"], "func": vrs_drv3_011_regime_norm_dd_velocity_jerk},
    "vrs_drv3_012_vol_regime_final_jerk": {"inputs": ["close", "volume"], "func": vrs_drv3_012_vol_regime_final_jerk},
    "vrs_drv3_013_vol_regime_ratio_pct_rank_jerk": {"inputs": ["close"], "func": vrs_drv3_013_vol_regime_ratio_pct_rank_jerk},
    "vrs_drv3_014_vol_entropy_regime_jerk": {"inputs": ["close"], "func": vrs_drv3_014_vol_entropy_regime_jerk},
    "vrs_drv3_015_turnover_regime_shift_jerk": {"inputs": ["volume", "sharesbas"], "func": vrs_drv3_015_turnover_regime_shift_jerk},
    "vrs_drv3_016_vol_clustering_regime_jerk": {"inputs": ["close"], "func": vrs_drv3_016_vol_clustering_regime_jerk},
    "vrs_drv3_017_vol_breakaway_energy_jerk": {"inputs": ["close"], "func": vrs_drv3_017_vol_breakaway_energy_jerk},
    "vrs_drv3_018_consecutive_regime_expanding_jerk": {"inputs": ["close"], "func": vrs_drv3_018_consecutive_regime_expanding_jerk},
    "vrs_drv3_019_regime_reversal_climax_jerk": {"inputs": ["close", "low"], "func": vrs_drv3_019_regime_reversal_climax_jerk},
    "vrs_drv3_020_sustained_hi_vol_regime_jerk": {"inputs": ["close"], "func": vrs_drv3_020_sustained_hi_vol_regime_jerk},
    "vrs_drv3_021_vol_regime_skew_div_jerk": {"inputs": ["close"], "func": vrs_drv3_021_vol_regime_skew_div_jerk},
    "vrs_drv3_022_cumulative_regime_energy_jerk": {"inputs": ["close"], "func": vrs_drv3_022_cumulative_regime_energy_jerk},
    "vrs_drv3_023_regime_weighted_fear_jerk": {"inputs": ["close", "volume"], "func": vrs_drv3_023_regime_weighted_fear_jerk},
    "vrs_drv3_024_vix_proxy_regime_jerk": {"inputs": ["close"], "func": vrs_drv3_024_vix_proxy_regime_jerk},
    "vrs_drv3_025_mktcap_regime_energy_jerk": {"inputs": ["close", "sharesbas"], "func": vrs_drv3_025_mktcap_regime_energy_jerk},
}
