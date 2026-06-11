"""
21_volume_concentration — 3rd Derivatives
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

# 25 features capturing exhaustion/inflection of volume concentration acceleration (jerk)
def vcc_drv3_001_volume_share_top1d_jerk(volume: pd.Series) -> pd.Series:
    c = _safe_div(volume.rolling(21).max(), volume.rolling(21).sum())
    vel = c.diff(5)
    return vel.diff(5)


def vcc_drv3_002_volume_share_top5d_jerk(volume: pd.Series) -> pd.Series:
    v_top5 = volume.rolling(63).apply(lambda x: np.sort(x)[-5:].sum(), raw=True)
    v_total = volume.rolling(63).sum()
    c = _safe_div(v_top5, v_total)
    vel = c.diff(5)
    return vel.diff(5)


def vcc_drv3_003_gini_coefficient_jerk(volume: pd.Series) -> pd.Series:
    def _gini(x):
        x = np.sort(x)
        n = len(x)
        return (np.sum((2 * np.arange(1, n + 1) - n - 1) * x)) / (n * np.sum(x) + _EPS)
    g = volume.rolling(63).apply(_gini, raw=True)
    vel = g.diff(5)
    return vel.diff(5)


def vcc_drv3_004_down_day_volume_share_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    v_dn = volume.where(close < close.shift(1), 0).rolling(63).sum()
    v_tot = volume.rolling(63).sum()
    ratio = _safe_div(v_dn, v_tot)
    vel = ratio.diff(5)
    return vel.diff(5)


def vcc_drv3_005_new_low_volume_share_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    l = close.rolling(252).min()
    v_low = volume.where(close == l, 0).rolling(252).sum()
    v_tot = volume.rolling(252).sum()
    ratio = _safe_div(v_low, v_tot)
    vel = ratio.diff(5)
    return vel.diff(5)


def vcc_drv3_006_volume_hhi_jerk(volume: pd.Series) -> pd.Series:
    v_sum = volume.rolling(63).sum()
    v_share = _safe_div(volume, v_sum)
    hhi = (v_share**2).rolling(63).sum()
    vel = hhi.diff(5)
    return vel.diff(5)


def vcc_drv3_007_dollar_volume_concentration_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    dv_top5 = dv.rolling(63).apply(lambda x: np.sort(x)[-5:].sum(), raw=True)
    dv_total = dv.rolling(63).sum()
    ratio = _safe_div(dv_top5, dv_total)
    vel = ratio.diff(5)
    return vel.diff(5)


def vcc_drv3_008_turnover_concentration_jerk(volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    to = _safe_div(volume, sharesbas)
    to_top5 = to.rolling(63).apply(lambda x: np.sort(x)[-5:].sum(), raw=True)
    to_total = to.rolling(63).sum()
    ratio = _safe_div(to_top5, to_total)
    vel = ratio.diff(5)
    return vel.diff(5)


def vcc_drv3_009_liquidation_cluster_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    vs = _safe_div(volume.rolling(21).max(), volume.rolling(21).sum())
    dd = (close.rolling(21).max() - close) / (close.rolling(21).max() + _EPS)
    idx = vs * dd
    vel = idx.diff(5)
    return vel.diff(5)


def vcc_drv3_010_concentration_oscillator_jerk(volume: pd.Series) -> pd.Series:
    c21 = _safe_div(volume.rolling(21).max(), volume.rolling(21).sum())
    c252 = _safe_div(volume.rolling(252).apply(lambda x: np.sort(x)[-10:].sum(), raw=True), volume.rolling(252).sum())
    ratio = _safe_div(c21, c252)
    vel = ratio.diff(5)
    return vel.diff(5)


def vcc_drv3_011_volume_entropy_concentration_jerk(volume: pd.Series) -> pd.Series:
    def _gini(x):
        x = np.sort(x)
        n = len(x)
        return (np.sum((2 * np.arange(1, n + 1) - n - 1) * x)) / (n * np.sum(x) + _EPS)
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y, bins=10, density=True)
        p = h[h > 0]
        return -np.sum(p * np.log(p))
    g = volume.rolling(63).apply(_gini, raw=True)
    e = volume.rolling(63).apply(_ent, raw=True)
    ratio = _safe_div(g, e + _EPS)
    vel = ratio.diff(5)
    return vel.diff(5)


def vcc_drv3_012_tail_volume_ratio_jerk(volume: pd.Series) -> pd.Series:
    ratio = _safe_div(volume.rolling(63).quantile(0.9), volume.rolling(63).mean())
    vel = ratio.diff(5)
    return vel.diff(5)


def vcc_drv3_013_climax_contribution_jerk(volume: pd.Series) -> pd.Series:
    ratio = _safe_div(volume.rolling(63).max(), volume.rolling(63).mean())
    vel = ratio.diff(5)
    return vel.diff(5)


def vcc_drv3_014_volume_skew_jerk(volume: pd.Series) -> pd.Series:
    sk = volume.rolling(63).skew()
    vel = sk.diff(5)
    return vel.diff(5)


def vcc_drv3_015_ratio_vol_red_candles_jerk(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    v_red = volume.where(close < open, 0).rolling(21).sum()
    v_total = volume.rolling(21).sum()
    ratio = _safe_div(v_red, v_total)
    vel = ratio.diff(5)
    return vel.diff(5)


def vcc_drv3_016_concentration_regime_jerk(volume: pd.Series) -> pd.Series:
    def _gini(x):
        x = np.sort(x)
        n = len(x)
        return (np.sum((2 * np.arange(1, n + 1) - n - 1) * x)) / (n * np.sum(x) + _EPS)
    g21 = volume.rolling(21).apply(_gini, raw=True)
    g252 = volume.rolling(252).apply(_gini, raw=True)
    ratio = _safe_div(g21, g252)
    vel = ratio.diff(5)
    return vel.diff(5)


def vcc_drv3_017_mktcap_weighted_conc_jerk(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    cv = volume * np.log(mc + _EPS)
    v_top5 = cv.rolling(63).apply(lambda x: np.sort(x)[-5:].sum() / (np.sum(x) + _EPS), raw=True)
    vel = v_top5.diff(5)
    return vel.diff(5)


def vcc_drv3_018_terminal_liquidation_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    def _gini(x):
        x = np.sort(x)
        n = len(x)
        return (np.sum((2 * np.arange(1, n + 1) - n - 1) * x)) / (n * np.sum(x) + _EPS)
    g = volume.rolling(21).apply(_gini, raw=True)
    ds = _safe_div(volume.where(close < close.shift(1), 0).rolling(21).sum(), volume.rolling(21).sum())
    prox = _safe_div(close, close.rolling(252).min())
    score = g * ds * (prox - 1.0).abs()
    vel = score.diff(5)
    return vel.diff(5)


def vcc_drv3_019_volume_kurtosis_jerk(volume: pd.Series) -> pd.Series:
    k = volume.rolling(63).kurt()
    vel = k.diff(5)
    return vel.diff(5)


def vcc_drv3_020_climax_volume_to_total_ath_jerk(volume: pd.Series) -> pd.Series:
    q99 = volume.expanding().quantile(0.99)
    ratio = _safe_div(volume.where(volume > q99, 0).cumsum(), volume.cumsum())
    vel = ratio.diff(5)
    return vel.diff(5)


def vcc_drv3_021_consecutive_high_conc_jerk(volume: pd.Series) -> pd.Series:
    def _gini(x):
        x = np.sort(x)
        n = len(x)
        return (np.sum((2 * np.arange(1, n + 1) - n - 1) * x)) / (n * np.sum(x) + _EPS)
    g = volume.rolling(63).apply(_gini, raw=True)
    is_high = (g > g.rolling(252).median()).astype(int)
    dur = is_high.groupby((is_high == 0).cumsum()).cumsum()
    vel = dur.diff(5)
    return vel.diff(5)


def vcc_drv3_022_ratio_vol_gap_downs_jerk(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    v_gap = volume.where(open < close.shift(1), 0).rolling(63).sum()
    v_total = volume.rolling(63).sum()
    ratio = _safe_div(v_gap, v_total)
    vel = ratio.diff(5)
    return vel.diff(5)


def vcc_drv3_023_cumulative_excess_conc_jerk(volume: pd.Series) -> pd.Series:
    def _gini(x):
        x = np.sort(x)
        n = len(x)
        return (np.sum((2 * np.arange(1, n + 1) - n - 1) * x)) / (n * np.sum(x) + _EPS)
    g = volume.rolling(63).apply(_gini, raw=True)
    med = g.expanding().median()
    excess = (g - med).clip(lower=0).cumsum()
    vel = excess.diff(5)
    return vel.diff(5)


def vcc_drv3_024_final_imbalance_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    from scipy.stats import linregress
    score = vcc_150_final_liquidation_imbalance_index(close, volume)
    vel = score.diff(5)
    return vel.diff(5)


def vcc_drv3_025_mktcap_to_volume_gini_jerk(close: pd.Series, volume: pd.Series, sharesbas: pd.Series) -> pd.Series:
    def _gini(x):
        x = np.sort(x)
        n = len(x)
        return (np.sum((2 * np.arange(1, n + 1) - n - 1) * x)) / (n * np.sum(x) + _EPS)
    mc = close * sharesbas
    g_p = volume.rolling(63).apply(_gini, raw=True)
    g_m = mc.rolling(63).apply(_gini, raw=True)
    ratio = _safe_div(g_p, g_m)
    vel = ratio.diff(5)
    return vel.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V21_A_REGISTRY = {
    "vcc_drv3_001_volume_share_top1d_jerk": {"inputs": ["volume"], "func": vcc_drv3_001_volume_share_top1d_jerk},
    "vcc_drv3_002_volume_share_top5d_jerk": {"inputs": ["volume"], "func": vcc_drv3_002_volume_share_top5d_jerk},
    "vcc_drv3_003_gini_coefficient_jerk": {"inputs": ["volume"], "func": vcc_drv3_003_gini_coefficient_jerk},
    "vcc_drv3_004_down_day_volume_share_jerk": {"inputs": ["close", "volume"], "func": vcc_drv3_004_down_day_volume_share_jerk},
    "vcc_drv3_005_new_low_volume_share_jerk": {"inputs": ["close", "volume"], "func": vcc_drv3_005_new_low_volume_share_jerk},
    "vcc_drv3_006_volume_hhi_jerk": {"inputs": ["volume"], "func": vcc_drv3_006_volume_hhi_jerk},
    "vcc_drv3_007_dollar_volume_concentration_jerk": {"inputs": ["close", "volume"], "func": vcc_drv3_007_dollar_volume_concentration_jerk},
    "vcc_drv3_008_turnover_concentration_jerk": {"inputs": ["volume", "sharesbas"], "func": vcc_drv3_008_turnover_concentration_jerk},
    "vcc_drv3_009_liquidation_cluster_jerk": {"inputs": ["close", "volume"], "func": vcc_drv3_009_liquidation_cluster_jerk},
    "vcc_drv3_010_concentration_oscillator_jerk": {"inputs": ["volume"], "func": vcc_drv3_010_concentration_oscillator_jerk},
    "vcc_drv3_011_volume_entropy_concentration_jerk": {"inputs": ["volume"], "func": vcc_drv3_011_volume_entropy_concentration_jerk},
    "vcc_drv3_012_tail_volume_ratio_jerk": {"inputs": ["volume"], "func": vcc_drv3_012_tail_volume_ratio_jerk},
    "vcc_drv3_013_climax_contribution_jerk": {"inputs": ["volume"], "func": vcc_drv3_013_climax_contribution_jerk},
    "vcc_drv3_014_volume_skew_jerk": {"inputs": ["volume"], "func": vcc_drv3_014_volume_skew_jerk},
    "vcc_drv3_015_ratio_vol_red_candles_jerk": {"inputs": ["open", "close", "volume"], "func": vcc_drv3_015_ratio_vol_red_candles_jerk},
    "vcc_drv3_016_concentration_regime_jerk": {"inputs": ["volume"], "func": vcc_drv3_016_concentration_regime_jerk},
    "vcc_drv3_017_mktcap_weighted_conc_jerk": {"inputs": ["close", "volume", "sharesbas"], "func": vcc_drv3_017_mktcap_weighted_conc_jerk},
    "vcc_drv3_018_terminal_liquidation_jerk": {"inputs": ["close", "volume"], "func": vcc_drv3_018_terminal_liquidation_jerk},
    "vcc_drv3_019_volume_kurtosis_jerk": {"inputs": ["volume"], "func": vcc_drv3_019_volume_kurtosis_jerk},
    "vcc_drv3_020_climax_volume_to_total_ath_jerk": {"inputs": ["volume"], "func": vcc_drv3_020_climax_volume_to_total_ath_jerk},
    "vcc_drv3_021_consecutive_high_conc_jerk": {"inputs": ["volume"], "func": vcc_drv3_021_consecutive_high_conc_jerk},
    "vcc_drv3_022_ratio_vol_gap_downs_jerk": {"inputs": ["close", "open", "volume"], "func": vcc_drv3_022_ratio_vol_gap_downs_jerk},
    "vcc_drv3_023_cumulative_excess_conc_jerk": {"inputs": ["volume"], "func": vcc_drv3_023_cumulative_excess_conc_jerk},
    "vcc_drv3_024_final_imbalance_jerk": {"inputs": ["close", "volume"], "func": vcc_drv3_024_final_imbalance_jerk},
    "vcc_drv3_025_mktcap_to_volume_gini_jerk": {"inputs": ["close", "volume", "sharesbas"], "func": vcc_drv3_025_mktcap_to_volume_gini_jerk},
}
