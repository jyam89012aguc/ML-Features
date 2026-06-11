"""
26_volatility_clustering — 2nd Derivatives
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

# 25 features capturing acceleration of volatility clustering metrics
def vcl_drv2_001_consecutive_high_vol_velocity(close: pd.Series) -> pd.Series:
    # Change in high-vol streak length
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    avg_v = v21.rolling(252).mean()
    above = (v21 > avg_v).astype(int)
    dur = above.groupby((above == 0).cumsum()).cumsum()
    return dur.diff(5)


def vcl_drv2_002_high_vol_freq_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    s = ret.rolling(252).std()
    extreme = (ret.abs() > 2 * s).astype(int)
    freq = extreme.rolling(63).mean()
    return freq.diff(5)


def vcl_drv2_003_vol_clustering_velocity(close: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    return ac.diff(5)


def vcl_drv2_004_count_vol_shocks_velocity(close: pd.Series) -> pd.Series:
    r = close.rolling(21).max() - close.rolling(21).min()
    med_r = r.rolling(252).median()
    cnt = (r > 2 * med_r).rolling(252).sum()
    return cnt.diff(5)


def vcl_drv2_005_range_persistence_velocity(high: pd.Series, low: pd.Series) -> pd.Series:
    r = (high - low) / ((high + low) / 2.0)
    per = _safe_div(r.rolling(21).mean(), r.rolling(252).median())
    return per.diff(5)


def vcl_drv2_006_vol_climax_duration_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    vp = (v21 > v21.rolling(252).mean()).rolling(63).mean()
    vol_p = (volume > volume.rolling(252).median()).rolling(63).mean()
    idx = vp * vol_p
    return idx.diff(5)


def vcl_drv2_007_vol_storm_intensity_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    mv = v21.rolling(63).mean()
    pv = (v21 > v21.rolling(252).mean()).rolling(63).mean()
    is_shock = (close.pct_change().abs() > 3 * close.pct_change().expanding().std())
    ds = pd.Series(np.arange(len(close)), index=close.index) - pd.Series(np.arange(len(close)), index=close.index).where(is_shock).ffill()
    idx = _safe_div(mv * pv, np.log(ds + 2.0))
    return idx.diff(5)


def vcl_drv2_008_vol_osc_clustering_velocity(close: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    z = (ac - ac.rolling(252).mean()) / (ac.rolling(252).std() + _EPS)
    return z.diff(5)


def vcl_drv2_009_vol_cluster_efficiency_velocity(close: pd.Series) -> pd.Series:
    net_m = (close / close.shift(63) - 1).abs()
    v = np.log(close / close.shift(1)).rolling(63).mean()
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    eff = _safe_div(net_m, v * ac + _EPS)
    return eff.diff(5)


def vcl_drv2_010_mktcap_vol_cluster_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    abs_ret = mc.pct_change().abs()
    ac = abs_ret.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    return ac.diff(5)


def vcl_drv2_011_vol_clustering_zscore_velocity(close: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    z = (ac - ac.expanding().mean()) / (ac.expanding().std() + _EPS)
    return z.diff(5)


def vcl_drv2_012_vol_cap_climax_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    vs = _safe_div(volume, volume.rolling(252).median())
    dd = (close.rolling(252).max() - close) / close.rolling(252).max()
    score = ac * vs * dd
    return score.diff(5)


def vcl_drv2_013_vol_cluster_regime_break_velocity(close: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac21 = abs_ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    ac63 = abs_ret.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    brk = ac21 - ac63
    return brk.diff(5)


def vcl_drv2_014_cumulative_cluster_energy_velocity(close: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    energy = ac.cumsum() / (ac.abs().cumsum() + _EPS)
    return energy.diff(5)


def vcl_drv2_015_vol_clustering_final_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    h = close.rolling(252).max()
    dist_h = (h - close) / h
    v = close.pct_change().rolling(21).std()
    score = ac * dist_h * v
    return score.diff(5)


def vcl_drv2_016_consecutive_extreme_range_velocity(high: pd.Series, low: pd.Series) -> pd.Series:
    r = high - low
    q90 = r.rolling(252).quantile(0.9)
    above = (r > q90).astype(int)
    dur = above.groupby((above == 0).cumsum()).cumsum()
    return dur.diff(5)


def vcl_drv2_017_vol_regime_switch_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    avg_v = v21.rolling(252).mean()
    cross = (v21 > avg_v) != (v21.shift(1) > avg_v.shift(1))
    cnt = cross.astype(int).rolling(252).sum()
    return cnt.diff(5)


def vcl_drv2_018_entropy_vol_cluster_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y[~np.isnan(y)], bins=5)
        p = h / (np.sum(h) + _EPS)
        return -np.sum(p[p > 0] * np.log(p[p > 0]))
    e = v.rolling(63).apply(_ent, raw=True)
    return e.diff(5)


def vcl_drv2_019_vw_vol_clustering_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    v_rat = _safe_div(volume, volume.rolling(63).mean())
    return (ac * v_rat).diff(5)


def vcl_drv2_020_vol_integral_spread_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change().abs()
    ratio = _safe_div(ret.rolling(63).sum() / 63.0, ret.rolling(252).sum() / 252.0)
    return ratio.diff(5)


def vcl_drv2_021_days_above_2sigma_range_velocity(high: pd.Series, low: pd.Series) -> pd.Series:
    r = high - low
    above = (r > r.rolling(252).mean() + 2 * r.rolling(252).std()).astype(int)
    cnt = above.rolling(63).sum()
    return cnt.diff(5)


def vcl_drv2_022_mktcap_turnover_cluster_div_velocity(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    def _ac(s): return s.pct_change().abs().rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    div = _ac(close * sharesbas) - _ac(_safe_div(volume, sharesbas))
    return div.diff(5)


def vcl_drv2_023_consecutive_high_clustering_velocity(close: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    is_high = (ac > ac.rolling(252).median()).astype(int)
    dur = is_high.groupby((is_high == 0).cumsum()).cumsum()
    return dur.diff(5)


def vcl_drv2_024_vol_cluster_reversal_velocity(close: pd.Series, low: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    score = ac.diff(5) * _safe_div(close, low)
    return score.diff(5)


def vcl_drv2_025_vol_clustering_decay_velocity(close: pd.Series) -> pd.Series:
    abs_ret = close.pct_change().abs()
    ac = abs_ret.rolling(21).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    def _slope(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), y).slope
    sl = ac.rolling(252).apply(_slope, raw=True)
    return sl.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V26_V_REGISTRY = {
    "vcl_drv2_001_consecutive_high_vol_velocity": {"inputs": ["close"], "func": vcl_drv2_001_consecutive_high_vol_velocity},
    "vcl_drv2_002_high_vol_freq_velocity": {"inputs": ["close"], "func": vcl_drv2_002_high_vol_freq_velocity},
    "vcl_drv2_003_vol_clustering_velocity": {"inputs": ["close"], "func": vcl_drv2_003_vol_clustering_velocity},
    "vcl_drv2_004_count_vol_shocks_velocity": {"inputs": ["close"], "func": vcl_drv2_004_count_vol_shocks_velocity},
    "vcl_drv2_005_range_persistence_velocity": {"inputs": ["high", "low"], "func": vcl_drv2_005_range_persistence_velocity},
    "vcl_drv2_006_vol_climax_duration_velocity": {"inputs": ["close", "volume"], "func": vcl_drv2_006_vol_climax_duration_velocity},
    "vcl_drv2_007_vol_storm_intensity_velocity": {"inputs": ["close"], "func": vcl_drv2_007_vol_storm_intensity_velocity},
    "vcl_drv2_008_vol_osc_clustering_velocity": {"inputs": ["close"], "func": vcl_drv2_008_vol_osc_clustering_velocity},
    "vcl_drv2_009_vol_cluster_efficiency_velocity": {"inputs": ["close"], "func": vcl_drv2_009_vol_cluster_efficiency_velocity},
    "vcl_drv2_010_mktcap_vol_cluster_velocity": {"inputs": ["close", "sharesbas"], "func": vcl_drv2_010_mktcap_vol_cluster_velocity},
    "vcl_drv2_011_vol_clustering_zscore_velocity": {"inputs": ["close"], "func": vcl_drv2_011_vol_clustering_zscore_velocity},
    "vcl_drv2_012_vol_cap_climax_velocity": {"inputs": ["close", "volume"], "func": vcl_drv2_012_vol_cap_climax_velocity},
    "vcl_drv2_013_vol_cluster_regime_break_velocity": {"inputs": ["close"], "func": vcl_drv2_013_vol_cluster_regime_break_velocity},
    "vcl_drv2_014_cumulative_cluster_energy_velocity": {"inputs": ["close"], "func": vcl_drv2_014_cumulative_cluster_energy_velocity},
    "vcl_drv2_015_vol_clustering_final_velocity": {"inputs": ["close", "volume"], "func": vcl_drv2_015_vol_clustering_final_velocity},
    "vcl_drv2_016_consecutive_extreme_range_velocity": {"inputs": ["high", "low"], "func": vcl_drv2_016_consecutive_extreme_range_velocity},
    "vcl_drv2_017_vol_regime_switch_velocity": {"inputs": ["close"], "func": vcl_drv2_017_vol_regime_switch_velocity},
    "vcl_drv2_018_entropy_vol_cluster_velocity": {"inputs": ["close"], "func": vcl_drv2_018_entropy_vol_cluster_velocity},
    "vcl_drv2_019_vw_vol_clustering_velocity": {"inputs": ["close", "volume"], "func": vcl_drv2_019_vw_vol_clustering_velocity},
    "vcl_drv2_020_vol_integral_spread_velocity": {"inputs": ["close"], "func": vcl_drv2_020_vol_integral_spread_velocity},
    "vcl_drv2_021_days_above_2sigma_range_velocity": {"inputs": ["high", "low"], "func": vcl_drv2_021_days_above_2sigma_range_velocity},
    "vcl_drv2_022_mktcap_turnover_cluster_div_velocity": {"inputs": ["close", "volume", "sharesbas"], "func": vcl_drv2_022_mktcap_turnover_cluster_div_velocity},
    "vcl_drv2_023_consecutive_high_clustering_velocity": {"inputs": ["close"], "func": vcl_drv2_023_consecutive_high_clustering_velocity},
    "vcl_drv2_024_vol_cluster_reversal_velocity": {"inputs": ["close", "low"], "func": vcl_drv2_024_vol_cluster_reversal_velocity},
    "vcl_drv2_025_vol_clustering_decay_velocity": {"inputs": ["close"], "func": vcl_drv2_025_vol_clustering_decay_velocity},
}
