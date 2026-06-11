"""
26_volatility_clustering — 3rd Derivatives
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

# 25 features capturing exhaustion/inflection of volatility clustering acceleration (jerk)
def vcl_drv3_001_consecutive_high_vol_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    avg_v = v21.rolling(252).mean()
    above = (v21 > avg_v).astype(int)
    dur = above.groupby((above == 0).cumsum()).cumsum()
    vel = dur.diff(5)
    return vel.diff(5)


def vcl_drv3_002_high_vol_freq_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    s = ret.rolling(252).std()
    extreme = (ret.abs() > 2 * s).astype(int)
    freq = extreme.rolling(63).mean()
    vel = freq.diff(5)
    return vel.diff(5)


def vcl_drv3_003_vol_clustering_jerk(close: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    vel = ac.diff(5)
    return vel.diff(5)


def vcl_drv3_004_count_vol_shocks_jerk(close: pd.Series) -> pd.Series:
    r = close.rolling(21).max() - close.rolling(21).min()
    med_r = r.rolling(252).median()
    cnt = (r > 2 * med_r).rolling(252).sum()
    vel = cnt.diff(5)
    return vel.diff(5)


def vcl_drv3_005_range_persistence_jerk(high: pd.Series, low: pd.Series) -> pd.Series:
    r = (high - low) / ((high + low) / 2.0)
    per = _safe_div(r.rolling(21).mean(), r.rolling(252).median())
    vel = per.diff(5)
    return vel.diff(5)


def vcl_drv3_006_vol_climax_duration_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    vp = (v21 > v21.rolling(252).mean()).rolling(63).mean()
    vol_p = (volume > volume.rolling(252).median()).rolling(63).mean()
    idx = vp * vol_p
    vel = idx.diff(5)
    return vel.diff(5)


def vcl_drv3_007_vol_storm_intensity_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    mv = v21.rolling(63).mean()
    pv = (v21 > v21.rolling(252).mean()).rolling(63).mean()
    is_shock = (close.pct_change().abs() > 3 * close.pct_change().expanding().std())
    ds = pd.Series(np.arange(len(close)), index=close.index) - pd.Series(np.arange(len(close)), index=close.index).where(is_shock).ffill()
    idx = _safe_div(mv * pv, np.log(ds + 2.0))
    vel = idx.diff(5)
    return vel.diff(5)


def vcl_drv3_008_vol_osc_clustering_jerk(close: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    z = (ac - ac.rolling(252).mean()) / (ac.rolling(252).std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def vcl_drv3_009_vol_cluster_efficiency_jerk(close: pd.Series) -> pd.Series:
    net_m = (close / close.shift(63) - 1).abs()
    v = np.log(close / close.shift(1)).rolling(63).mean()
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    eff = _safe_div(net_m, v * ac + _EPS)
    vel = eff.diff(5)
    return vel.diff(5)


def vcl_drv3_010_mktcap_vol_cluster_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    abs_ret = mc.pct_change().abs()
    ac = abs_ret.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    vel = ac.diff(5)
    return vel.diff(5)


def vcl_drv3_011_vol_clustering_zscore_jerk(close: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    z = (ac - ac.expanding().mean()) / (ac.expanding().std() + _EPS)
    vel = z.diff(5)
    return vel.diff(5)


def vcl_drv3_012_vol_cap_climax_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    vs = _safe_div(volume, volume.rolling(252).median())
    dd = (close.rolling(252).max() - close) / (close.rolling(252).max() + _EPS)
    score = ac * vs * dd
    vel = score.diff(5)
    return vel.diff(5)


def vcl_drv3_013_vol_cluster_regime_break_jerk(close: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac21 = abs_ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    ac63 = abs_ret.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    brk = ac21 - ac63
    vel = brk.diff(5)
    return vel.diff(5)


def vcl_drv3_014_cumulative_cluster_energy_jerk(close: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    energy = ac.cumsum() / (ac.abs().cumsum() + _EPS)
    vel = energy.diff(5)
    return vel.diff(5)


def vcl_drv3_015_vol_clustering_final_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    h = close.rolling(252).max()
    dist_h = (h - close) / (h + _EPS)
    v = close.pct_change().rolling(21).std()
    score = ac * dist_h * v
    vel = score.diff(5)
    return vel.diff(5)


def vcl_drv3_016_consecutive_extreme_range_jerk(high: pd.Series, low: pd.Series) -> pd.Series:
    r = high - low
    q90 = r.rolling(252).quantile(0.9)
    above = (r > q90).astype(int)
    dur = above.groupby((above == 0).cumsum()).cumsum()
    vel = dur.diff(5)
    return vel.diff(5)


def vcl_drv3_017_vol_regime_switch_jerk(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    avg_v = v21.rolling(252).mean()
    cross = (v21 > avg_v) != (v21.shift(1) > avg_v.shift(1))
    cnt = cross.astype(int).rolling(252).sum()
    vel = cnt.diff(5)
    return vel.diff(5)


def vcl_drv3_018_entropy_vol_cluster_jerk(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y[~np.isnan(y)], bins=5)
        p = h / (np.sum(h) + _EPS)
        return -np.sum(p[p > 0] * np.log(p[p > 0]))
    e = v.rolling(63).apply(_ent, raw=True)
    vel = e.diff(5)
    return vel.diff(5)


def vcl_drv3_019_vw_vol_clustering_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    v_rat = _safe_div(volume, volume.rolling(63).mean())
    score = ac * v_rat
    vel = score.diff(5)
    return vel.diff(5)


def vcl_drv3_020_vol_integral_spread_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change().abs()
    ratio = _safe_div(ret.rolling(63).sum() / 63.0, ret.rolling(252).sum() / 252.0)
    vel = ratio.diff(5)
    return vel.diff(5)


def vcl_drv3_021_days_above_2sigma_range_jerk(high: pd.Series, low: pd.Series) -> pd.Series:
    r = high - low
    above = (r > r.rolling(252).mean() + 2 * r.rolling(252).std()).astype(int)
    cnt = above.rolling(63).sum()
    vel = cnt.diff(5)
    return vel.diff(5)


def vcl_drv3_022_mktcap_turnover_cluster_div_jerk(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    def _ac(s): return s.pct_change().abs().rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    div = _ac(close * sharesbas) - _ac(_safe_div(volume, sharesbas))
    vel = div.diff(5)
    return vel.diff(5)


def vcl_drv3_023_consecutive_high_clustering_jerk(close: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    is_high = (ac > ac.rolling(252).median()).astype(int)
    dur = is_high.groupby((is_high == 0).cumsum()).cumsum()
    vel = dur.diff(5)
    return vel.diff(5)


def vcl_drv3_024_vol_cluster_reversal_jerk(close: pd.Series, low: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    score = ac.diff(5) * _safe_div(close, low + _EPS)
    vel = score.diff(5)
    return vel.diff(5)


def vcl_drv3_025_vol_clustering_decay_jerk(close: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    def _slope(y):
        from scipy.stats import linregress
        if len(y) < 2: return 0.0
        return linregress(np.arange(len(y)), y).slope
    sl = ac.rolling(252).apply(_slope, raw=True)
    vel = sl.diff(5)
    return vel.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V26_A_REGISTRY = {
    "vcl_drv3_001_consecutive_high_vol_jerk": {"inputs": ["close"], "func": vcl_drv3_001_consecutive_high_vol_jerk},
    "vcl_drv3_002_high_vol_freq_jerk": {"inputs": ["close"], "func": vcl_drv3_002_high_vol_freq_jerk},
    "vcl_drv3_003_vol_clustering_jerk": {"inputs": ["close"], "func": vcl_drv3_003_vol_clustering_jerk},
    "vcl_drv3_004_count_vol_shocks_jerk": {"inputs": ["close"], "func": vcl_drv3_004_count_vol_shocks_jerk},
    "vcl_drv3_005_range_persistence_jerk": {"inputs": ["high", "low"], "func": vcl_drv3_005_range_persistence_jerk},
    "vcl_drv3_006_vol_climax_duration_jerk": {"inputs": ["close", "volume"], "func": vcl_drv3_006_vol_climax_duration_jerk},
    "vcl_drv3_007_vol_storm_intensity_jerk": {"inputs": ["close"], "func": vcl_drv3_007_vol_storm_intensity_jerk},
    "vcl_drv3_008_vol_osc_clustering_jerk": {"inputs": ["close"], "func": vcl_drv3_008_vol_osc_clustering_jerk},
    "vcl_drv3_009_vol_cluster_efficiency_jerk": {"inputs": ["close"], "func": vcl_drv3_009_vol_cluster_efficiency_jerk},
    "vcl_drv3_010_mktcap_vol_cluster_jerk": {"inputs": ["close", "sharesbas"], "func": vcl_drv3_010_mktcap_vol_cluster_jerk},
    "vcl_drv3_011_vol_clustering_zscore_jerk": {"inputs": ["close"], "func": vcl_drv3_011_vol_clustering_zscore_jerk},
    "vcl_drv3_012_vol_cap_climax_jerk": {"inputs": ["close", "volume"], "func": vcl_drv3_012_vol_cap_climax_jerk},
    "vcl_drv3_013_vol_cluster_regime_break_jerk": {"inputs": ["close"], "func": vcl_drv3_013_vol_cluster_regime_break_jerk},
    "vcl_drv3_014_cumulative_cluster_energy_jerk": {"inputs": ["close"], "func": vcl_drv3_014_cumulative_cluster_energy_jerk},
    "vcl_drv3_015_vol_clustering_final_jerk": {"inputs": ["close", "volume"], "func": vcl_drv3_015_vol_clustering_final_jerk},
    "vcl_drv3_016_consecutive_extreme_range_jerk": {"inputs": ["high", "low"], "func": vcl_drv3_016_consecutive_extreme_range_jerk},
    "vcl_drv3_017_vol_regime_switch_jerk": {"inputs": ["close"], "func": vcl_drv3_017_vol_regime_switch_jerk},
    "vcl_drv3_018_entropy_vol_cluster_jerk": {"inputs": ["close"], "func": vcl_drv3_018_entropy_vol_cluster_jerk},
    "vcl_drv3_019_vw_vol_clustering_jerk": {"inputs": ["close", "volume"], "func": vcl_drv3_019_vw_vol_clustering_jerk},
    "vcl_drv3_020_vol_integral_spread_jerk": {"inputs": ["close"], "func": vcl_drv3_020_vol_integral_spread_jerk},
    "vcl_drv3_021_days_above_2sigma_range_jerk": {"inputs": ["high", "low"], "func": vcl_drv3_021_days_above_2sigma_range_jerk},
    "vcl_drv3_022_mktcap_turnover_cluster_div_jerk": {"inputs": ["close", "volume", "sharesbas"], "func": vcl_drv3_022_mktcap_turnover_cluster_div_jerk},
    "vcl_drv3_023_consecutive_high_clustering_jerk": {"inputs": ["close"], "func": vcl_drv3_023_consecutive_high_clustering_jerk},
    "vcl_drv3_024_vol_cluster_reversal_jerk": {"inputs": ["close", "low"], "func": vcl_drv3_024_vol_cluster_reversal_jerk},
    "vcl_drv3_025_vol_clustering_decay_jerk": {"inputs": ["close"], "func": vcl_drv3_025_vol_clustering_decay_jerk},
}
