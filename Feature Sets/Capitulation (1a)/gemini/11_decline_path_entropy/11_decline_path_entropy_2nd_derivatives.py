"""
11_decline_path_entropy — 2nd Derivatives
Domain: rate of change of base features — captures acceleration of decline/distress
Asset class: US equities | Daily OHLCV + Sharadar fundamentals
"""
import numpy as np
import pandas as pd
from scipy.stats import entropy

# ── Utility helpers ──────────────────────────────────────────────────────────
TRADING_DAYS_YEAR = 252
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5
_EPS = 1e-9


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _calculate_entropy(s: pd.Series, bins: int = 10) -> float:
    if s.isna().all(): return np.nan
    counts, _ = np.histogram(s.dropna(), bins=bins, density=True)
    return entropy(counts + _EPS)


# ── Feature functions ────────────────────────────────────────────────────────

# 25 features capturing acceleration of entropy and path complexity metrics
def dpe_drv2_001_return_entropy_63d_velocity(close: pd.Series) -> pd.Series:
    e = close.pct_change().rolling(63).apply(_calculate_entropy, raw=False)
    return e.diff(5)


def dpe_drv2_002_efficiency_ratio_252d_velocity(close: pd.Series) -> pd.Series:
    net_move = (close - close.shift(252)).abs()
    path_len = close.diff().abs().rolling(252).sum()
    er = _safe_div(net_move, path_len)
    return er.diff(5)


def dpe_drv2_003_drawdown_entropy_63d_velocity(close: pd.Series) -> pd.Series:
    h = close.rolling(252).max()
    uw = (close - h) / h
    e = uw.rolling(63).apply(_calculate_entropy, raw=False)
    return e.diff(5)


def dpe_drv2_004_zigzag_index_63d_velocity(close: pd.Series) -> pd.Series:
    h = close.rolling(252).max()
    uw = (close - h) / h
    duw = uw.diff()
    sign_change = (np.sign(duw) != np.sign(duw.shift(1))).astype(int)
    zz = sign_change.rolling(63).sum()
    return zz.diff(5)


def dpe_drv2_005_vol_entropy_velocity(volume: pd.Series) -> pd.Series:
    ve = volume.rolling(63).apply(_calculate_entropy, raw=False)
    return ve.diff(5)


def dpe_drv2_006_complexity_composite_velocity(close: pd.Series) -> pd.Series:
    re = close.pct_change().rolling(21).apply(_calculate_entropy, raw=False)
    er = _safe_div((close - close.shift(21)).abs(), close.diff().abs().rolling(21).sum())
    comp = (re + (1.0 - er)) / 2.0
    return comp.diff(5)


def dpe_drv2_007_entropy_regime_shift_velocity(close: pd.Series) -> pd.Series:
    e21 = close.pct_change().rolling(21).apply(_calculate_entropy, raw=False)
    e252 = close.pct_change().rolling(252).apply(_calculate_entropy, raw=False)
    rsi = _safe_div(e21, e252)
    return rsi.diff(5)


def dpe_drv2_008_information_gain_velocity(close: pd.Series) -> pd.Series:
    e = close.pct_change().rolling(21).apply(_calculate_entropy, raw=False)
    gain = e.diff(21)
    return gain.diff(5)


def dpe_drv2_009_mktcap_path_entropy_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    ret = mc.pct_change()
    mce = ret.rolling(63).apply(_calculate_entropy, raw=False)
    return mce.diff(5)


def dpe_drv2_010_entropy_to_vol_ratio_velocity(close: pd.Series) -> pd.Series:
    e = close.pct_change().rolling(63).apply(_calculate_entropy, raw=False)
    v = close.pct_change().rolling(63).std()
    ratio = _safe_div(e, v)
    return ratio.diff(5)


def dpe_drv2_011_entropy_climax_velocity(close: pd.Series) -> pd.Series:
    e = close.pct_change().rolling(21).apply(_calculate_entropy, raw=False)
    v = close.pct_change().rolling(21).std()
    path_len = close.diff().abs().rolling(21).sum()
    er = _safe_div((close - close.shift(21)).abs(), path_len)
    score = e * v * (1.0 / (er + _EPS))
    return score.diff(5)


def dpe_drv2_012_entropy_regime_stability_velocity(close: pd.Series) -> pd.Series:
    e = close.pct_change().rolling(21).apply(_calculate_entropy, raw=False)
    def _rsq(y):
        from scipy.stats import linregress
        if len(y) < 2: return 0.0
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = e.rolling(63).apply(_rsq, raw=True)
    return rs.diff(5)


def dpe_drv2_013_entropy_volatility_velocity(close: pd.Series) -> pd.Series:
    e = close.pct_change().rolling(21).apply(_calculate_entropy, raw=False)
    ev = e.rolling(63).std()
    return ev.diff(5)


def dpe_drv2_014_permutation_entropy_velocity(close: pd.Series) -> pd.Series:
    p = np.sign(close.diff()).rolling(21).apply(_calculate_entropy, raw=False)
    return p.diff(5)


def dpe_drv2_015_sample_entropy_velocity(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    def _joint_ent(y):
        if len(y) < 2: return 0.0
        y1, y2 = y[:-1], y[1:]
        h, _, _ = np.histogram2d(y1, y2, bins=5)
        p = h.flatten() / (np.sum(h) + _EPS)
        return -np.sum(p[p > 0] * np.log(p[p > 0]))
    se = ret.rolling(63).apply(_joint_ent, raw=True)
    return se.diff(5)


def dpe_drv2_016_joint_entropy_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    pe = close.pct_change().rolling(63).apply(_calculate_entropy, raw=False)
    ve = volume.rolling(63).apply(_calculate_entropy, raw=False)
    je = (pe / pe.rolling(252).mean()) + (ve / ve.rolling(252).mean())
    return je.diff(5)


def dpe_drv2_017_entropy_divergence_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    pe = close.pct_change().rolling(63).apply(_calculate_entropy, raw=False)
    mce = (close * sharesbas).pct_change().rolling(63).apply(_calculate_entropy, raw=False)
    div = pe - mce
    return div.diff(5)


def dpe_drv2_018_path_curviness_velocity(close: pd.Series) -> pd.Series:
    d2 = close.diff().diff().abs()
    cv = d2.rolling(21).sum() / close.rolling(21).mean()
    return cv.diff(5)


def dpe_drv2_019_entropy_weighted_avg_velocity(close: pd.Series) -> pd.Series:
    e21 = close.pct_change().rolling(21).apply(_calculate_entropy, raw=False)
    e63 = close.pct_change().rolling(63).apply(_calculate_entropy, raw=False)
    ewa = (0.7 * e21 + 0.3 * e63)
    return ewa.diff(5)


def dpe_drv2_020_final_chaos_index_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    re = close.pct_change().rolling(63).apply(_calculate_entropy, raw=False)
    ve = volume.rolling(63).apply(_calculate_entropy, raw=False)
    er = _safe_div((close - close.shift(63)).abs(), close.diff().abs().rolling(63).sum())
    ci = (re + ve) * (1.0 - er)
    return ci.diff(5)


def dpe_drv2_021_underwater_area_entropy_velocity(close: pd.Series) -> pd.Series:
    h = close.rolling(252).max()
    uw = (close - h) / h
    integral = uw.rolling(21).sum()
    uae = integral.rolling(63).apply(_calculate_entropy, raw=False)
    return uae.diff(5)


def dpe_drv2_022_entropy_of_volatility_velocity(close: pd.Series) -> pd.Series:
    v = close.pct_change().rolling(10).std()
    ev = v.rolling(63).apply(_calculate_entropy, raw=False)
    return ev.diff(5)


def dpe_drv2_023_path_smoothness_velocity(close: pd.Series) -> pd.Series:
    h = close.rolling(252).max()
    uw = (close - h) / h
    zz = (np.sign(uw.diff()) != np.sign(uw.diff().shift(1))).astype(int).rolling(63).sum()
    er = _safe_div((close - close.shift(252)).abs(), close.diff().abs().rolling(252).sum())
    ps = _safe_div(er, zz + 1)
    return ps.diff(5)


def dpe_drv2_024_revenue_ps_entropy_velocity(revenue: pd.Series, sharesbas: pd.Series) -> pd.Series:
    revps = _safe_div(revenue, sharesbas)
    ret = revps.pct_change()
    e = ret.expanding().apply(_calculate_entropy, raw=False)
    return e.diff(1)


def dpe_drv2_025_entropy_normalized_duration_velocity(close: pd.Series) -> pd.Series:
    e = close.pct_change().rolling(21).apply(_calculate_entropy, raw=False)
    cummax = close.cummax()
    high_indices = pd.Series(np.arange(len(close)), index=close.index).where(close == cummax).ffill()
    dsh = pd.Series(np.arange(len(close)), index=close.index) - high_indices
    en = _safe_div(e, np.log(dsh + 2))
    return en.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V11_V_REGISTRY = {
    "dpe_drv2_001_return_entropy_63d_velocity": {"inputs": ["close"], "func": dpe_drv2_001_return_entropy_63d_velocity},
    "dpe_drv2_002_efficiency_ratio_252d_velocity": {"inputs": ["close"], "func": dpe_drv2_002_efficiency_ratio_252d_velocity},
    "dpe_drv2_003_drawdown_entropy_63d_velocity": {"inputs": ["close"], "func": dpe_drv2_003_drawdown_entropy_63d_velocity},
    "dpe_drv2_004_zigzag_index_63d_velocity": {"inputs": ["close"], "func": dpe_drv2_004_zigzag_index_63d_velocity},
    "dpe_drv2_005_vol_entropy_velocity": {"inputs": ["volume"], "func": dpe_drv2_005_vol_entropy_velocity},
    "dpe_drv2_006_complexity_composite_velocity": {"inputs": ["close"], "func": dpe_drv2_006_complexity_composite_velocity},
    "dpe_drv2_007_entropy_regime_shift_velocity": {"inputs": ["close"], "func": dpe_drv2_007_entropy_regime_shift_velocity},
    "dpe_drv2_008_information_gain_velocity": {"inputs": ["close"], "func": dpe_drv2_008_information_gain_velocity},
    "dpe_drv2_009_mktcap_path_entropy_velocity": {"inputs": ["close", "sharesbas"], "func": dpe_drv2_009_mktcap_path_entropy_velocity},
    "dpe_drv2_010_entropy_to_vol_ratio_velocity": {"inputs": ["close"], "func": dpe_drv2_010_entropy_to_vol_ratio_velocity},
    "dpe_drv2_011_entropy_climax_velocity": {"inputs": ["close"], "func": dpe_drv2_011_entropy_climax_velocity},
    "dpe_drv2_012_entropy_regime_stability_velocity": {"inputs": ["close"], "func": dpe_drv2_012_entropy_regime_stability_velocity},
    "dpe_drv2_013_entropy_volatility_velocity": {"inputs": ["close"], "func": dpe_drv2_013_entropy_volatility_velocity},
    "dpe_drv2_014_permutation_entropy_velocity": {"inputs": ["close"], "func": dpe_drv2_014_permutation_entropy_velocity},
    "dpe_drv2_015_sample_entropy_velocity": {"inputs": ["close"], "func": dpe_drv2_015_sample_entropy_velocity},
    "dpe_drv2_016_joint_entropy_velocity": {"inputs": ["close", "volume"], "func": dpe_drv2_016_joint_entropy_velocity},
    "dpe_drv2_017_entropy_divergence_velocity": {"inputs": ["close", "sharesbas"], "func": dpe_drv2_017_entropy_divergence_velocity},
    "dpe_drv2_018_path_curviness_velocity": {"inputs": ["close"], "func": dpe_drv2_018_path_curviness_velocity},
    "dpe_drv2_019_entropy_weighted_avg_velocity": {"inputs": ["close"], "func": dpe_drv2_019_entropy_weighted_avg_velocity},
    "dpe_drv2_020_final_chaos_index_velocity": {"inputs": ["close", "volume"], "func": dpe_drv2_020_final_chaos_index_velocity},
    "dpe_drv2_021_underwater_area_entropy_velocity": {"inputs": ["close"], "func": dpe_drv2_021_underwater_area_entropy_velocity},
    "dpe_drv2_022_entropy_of_volatility_velocity": {"inputs": ["close"], "func": dpe_drv2_022_entropy_of_volatility_velocity},
    "dpe_drv2_023_path_smoothness_velocity": {"inputs": ["close"], "func": dpe_drv2_023_path_smoothness_velocity},
    "dpe_drv2_024_revenue_ps_entropy_velocity": {"inputs": ["revenue", "sharesbas"], "func": dpe_drv2_024_revenue_ps_entropy_velocity},
    "dpe_drv2_025_entropy_normalized_duration_velocity": {"inputs": ["close"], "func": dpe_drv2_025_entropy_normalized_duration_velocity},
}
