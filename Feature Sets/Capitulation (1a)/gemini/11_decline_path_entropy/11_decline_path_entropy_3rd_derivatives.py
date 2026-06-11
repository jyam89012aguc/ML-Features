"""
11_decline_path_entropy — 3rd Derivatives
Domain: rate of change of 2nd derivatives — captures exhaustion/inflection of acceleration
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

# 25 features capturing exhaustion/inflection of entropy acceleration (jerk)
def dpe_drv3_001_return_entropy_63d_jerk(close: pd.Series) -> pd.Series:
    e = close.pct_change().rolling(63).apply(_calculate_entropy, raw=False)
    vel = e.diff(5)
    return vel.diff(5)


def dpe_drv3_002_efficiency_ratio_252d_jerk(close: pd.Series) -> pd.Series:
    net_move = (close - close.shift(252)).abs()
    path_len = close.diff().abs().rolling(252).sum()
    er = _safe_div(net_move, path_len)
    vel = er.diff(5)
    return vel.diff(5)


def dpe_drv3_003_drawdown_entropy_63d_jerk(close: pd.Series) -> pd.Series:
    h = close.rolling(252).max()
    uw = (close - h) / h
    e = uw.rolling(63).apply(_calculate_entropy, raw=False)
    vel = e.diff(5)
    return vel.diff(5)


def dpe_drv3_004_zigzag_index_63d_jerk(close: pd.Series) -> pd.Series:
    h = close.rolling(252).max()
    uw = (close - h) / h
    duw = uw.diff()
    sign_change = (np.sign(duw) != np.sign(duw.shift(1))).astype(int)
    zz = sign_change.rolling(63).sum()
    vel = zz.diff(5)
    return vel.diff(5)


def dpe_drv3_005_vol_entropy_jerk(volume: pd.Series) -> pd.Series:
    ve = volume.rolling(63).apply(_calculate_entropy, raw=False)
    vel = ve.diff(5)
    return vel.diff(5)


def dpe_drv3_006_complexity_composite_jerk(close: pd.Series) -> pd.Series:
    re = close.pct_change().rolling(21).apply(_calculate_entropy, raw=False)
    er = _safe_div((close - close.shift(21)).abs(), close.diff().abs().rolling(21).sum())
    comp = (re + (1.0 - er)) / 2.0
    vel = comp.diff(5)
    return vel.diff(5)


def dpe_drv3_007_entropy_regime_shift_jerk(close: pd.Series) -> pd.Series:
    e21 = close.pct_change().rolling(21).apply(_calculate_entropy, raw=False)
    e252 = close.pct_change().rolling(252).apply(_calculate_entropy, raw=False)
    rsi = _safe_div(e21, e252)
    vel = rsi.diff(5)
    return vel.diff(5)


def dpe_drv3_008_information_gain_jerk(close: pd.Series) -> pd.Series:
    e = close.pct_change().rolling(21).apply(_calculate_entropy, raw=False)
    gain = e.diff(21)
    vel = gain.diff(5)
    return vel.diff(5)


def dpe_drv3_009_mktcap_path_entropy_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    ret = mc.pct_change()
    mce = ret.rolling(63).apply(_calculate_entropy, raw=False)
    vel = mce.diff(5)
    return vel.diff(5)


def dpe_drv3_010_entropy_to_vol_ratio_jerk(close: pd.Series) -> pd.Series:
    e = close.pct_change().rolling(63).apply(_calculate_entropy, raw=False)
    v = close.pct_change().rolling(63).std()
    ratio = _safe_div(e, v)
    vel = ratio.diff(5)
    return vel.diff(5)


def dpe_drv3_011_entropy_climax_jerk(close: pd.Series) -> pd.Series:
    e = close.pct_change().rolling(21).apply(_calculate_entropy, raw=False)
    v = close.pct_change().rolling(21).std()
    path_len = close.diff().abs().rolling(21).sum()
    er = _safe_div((close - close.shift(21)).abs(), path_len)
    score = e * v * (1.0 / (er + _EPS))
    vel = score.diff(5)
    return vel.diff(5)


def dpe_drv3_012_entropy_regime_stability_jerk(close: pd.Series) -> pd.Series:
    e = close.pct_change().rolling(21).apply(_calculate_entropy, raw=False)
    def _rsq(y):
        from scipy.stats import linregress
        if len(y) < 2: return 0.0
        return linregress(np.arange(len(y)), y).rvalue**2
    rs = e.rolling(63).apply(_rsq, raw=True)
    vel = rs.diff(5)
    return vel.diff(5)


def dpe_drv3_013_entropy_volatility_jerk(close: pd.Series) -> pd.Series:
    e = close.pct_change().rolling(21).apply(_calculate_entropy, raw=False)
    ev = e.rolling(63).std()
    vel = ev.diff(5)
    return vel.diff(5)


def dpe_drv3_014_permutation_entropy_jerk(close: pd.Series) -> pd.Series:
    p = np.sign(close.diff()).rolling(21).apply(_calculate_entropy, raw=False)
    vel = p.diff(5)
    return vel.diff(5)


def dpe_drv3_015_sample_entropy_jerk(close: pd.Series) -> pd.Series:
    ret = close.pct_change()
    def _joint_ent(y):
        if len(y) < 2: return 0.0
        y1, y2 = y[:-1], y[1:]
        h, _, _ = np.histogram2d(y1, y2, bins=5)
        p = h.flatten() / (np.sum(h) + _EPS)
        return -np.sum(p[p > 0] * np.log(p[p > 0]))
    se = ret.rolling(63).apply(_joint_ent, raw=True)
    vel = se.diff(5)
    return vel.diff(5)


def dpe_drv3_016_joint_entropy_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    pe = close.pct_change().rolling(63).apply(_calculate_entropy, raw=False)
    ve = volume.rolling(63).apply(_calculate_entropy, raw=False)
    je = (pe / pe.rolling(252).mean()) + (ve / ve.rolling(252).mean())
    vel = je.diff(5)
    return vel.diff(5)


def dpe_drv3_017_entropy_divergence_jerk(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    pe = close.pct_change().rolling(63).apply(_calculate_entropy, raw=False)
    mce = (close * sharesbas).pct_change().rolling(63).apply(_calculate_entropy, raw=False)
    div = pe - mce
    vel = div.diff(5)
    return vel.diff(5)


def dpe_drv3_018_path_curviness_jerk(close: pd.Series) -> pd.Series:
    d2 = close.diff().diff().abs()
    cv = d2.rolling(21).sum() / close.rolling(21).mean()
    vel = cv.diff(5)
    return vel.diff(5)


def dpe_drv3_019_entropy_weighted_avg_jerk(close: pd.Series) -> pd.Series:
    e21 = close.pct_change().rolling(21).apply(_calculate_entropy, raw=False)
    e63 = close.pct_change().rolling(63).apply(_calculate_entropy, raw=False)
    ewa = (0.7 * e21 + 0.3 * e63)
    vel = ewa.diff(5)
    return vel.diff(5)


def dpe_drv3_020_final_chaos_index_jerk(close: pd.Series, volume: pd.Series) -> pd.Series:
    re = close.pct_change().rolling(63).apply(_calculate_entropy, raw=False)
    ve = volume.rolling(63).apply(_calculate_entropy, raw=False)
    er = _safe_div((close - close.shift(63)).abs(), close.diff().abs().rolling(63).sum())
    ci = (re + ve) * (1.0 - er)
    vel = ci.diff(5)
    return vel.diff(5)


def dpe_drv3_021_underwater_area_entropy_jerk(close: pd.Series) -> pd.Series:
    h = close.rolling(252).max()
    uw = (close - h) / h
    integral = uw.rolling(21).sum()
    uae = integral.rolling(63).apply(_calculate_entropy, raw=False)
    vel = uae.diff(5)
    return vel.diff(5)


def dpe_drv3_022_entropy_of_volatility_jerk(close: pd.Series) -> pd.Series:
    v = close.pct_change().rolling(10).std()
    ev = v.rolling(63).apply(_calculate_entropy, raw=False)
    vel = ev.diff(5)
    return vel.diff(5)


def dpe_drv3_023_path_smoothness_jerk(close: pd.Series) -> pd.Series:
    h = close.rolling(252).max()
    uw = (close - h) / h
    zz = (np.sign(uw.diff()) != np.sign(uw.diff().shift(1))).astype(int).rolling(63).sum()
    er = _safe_div((close - close.shift(252)).abs(), close.diff().abs().rolling(252).sum())
    ps = _safe_div(er, zz + 1)
    vel = ps.diff(5)
    return vel.diff(5)


def dpe_drv3_024_revenue_ps_entropy_jerk(revenue: pd.Series, sharesbas: pd.Series) -> pd.Series:
    revps = _safe_div(revenue, sharesbas)
    ret = revps.pct_change()
    e = ret.expanding().apply(_calculate_entropy, raw=False)
    vel = e.diff(1)
    return vel.diff(1)


def dpe_drv3_025_entropy_normalized_duration_jerk(close: pd.Series) -> pd.Series:
    e = close.pct_change().rolling(21).apply(_calculate_entropy, raw=False)
    cummax = close.cummax()
    high_indices = pd.Series(np.arange(len(close)), index=close.index).where(close == cummax).ffill()
    dsh = pd.Series(np.arange(len(close)), index=close.index) - high_indices
    en = _safe_div(e, np.log(dsh + 2))
    vel = en.diff(5)
    return vel.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V11_A_REGISTRY = {
    "dpe_drv3_001_return_entropy_63d_jerk": {"inputs": ["close"], "func": dpe_drv3_001_return_entropy_63d_jerk},
    "dpe_drv3_002_efficiency_ratio_252d_jerk": {"inputs": ["close"], "func": dpe_drv3_002_efficiency_ratio_252d_jerk},
    "dpe_drv3_003_drawdown_entropy_63d_jerk": {"inputs": ["close"], "func": dpe_drv3_003_drawdown_entropy_63d_jerk},
    "dpe_drv3_004_zigzag_index_63d_jerk": {"inputs": ["close"], "func": dpe_drv3_004_zigzag_index_63d_jerk},
    "dpe_drv3_005_vol_entropy_jerk": {"inputs": ["volume"], "func": dpe_drv3_005_vol_entropy_jerk},
    "dpe_drv3_006_complexity_composite_jerk": {"inputs": ["close"], "func": dpe_drv3_006_complexity_composite_jerk},
    "dpe_drv3_007_entropy_regime_shift_jerk": {"inputs": ["close"], "func": dpe_drv3_007_entropy_regime_shift_jerk},
    "dpe_drv3_008_information_gain_jerk": {"inputs": ["close"], "func": dpe_drv3_008_information_gain_jerk},
    "dpe_drv3_009_mktcap_path_entropy_jerk": {"inputs": ["close", "sharesbas"], "func": dpe_drv3_009_mktcap_path_entropy_jerk},
    "dpe_drv3_010_entropy_to_vol_ratio_jerk": {"inputs": ["close"], "func": dpe_drv3_010_entropy_to_vol_ratio_jerk},
    "dpe_drv3_011_entropy_climax_jerk": {"inputs": ["close"], "func": dpe_drv3_011_entropy_climax_jerk},
    "dpe_drv3_012_entropy_regime_stability_jerk": {"inputs": ["close"], "func": dpe_drv3_012_entropy_regime_stability_jerk},
    "dpe_drv3_013_entropy_volatility_jerk": {"inputs": ["close"], "func": dpe_drv3_013_entropy_volatility_jerk},
    "dpe_drv3_014_permutation_entropy_jerk": {"inputs": ["close"], "func": dpe_drv3_014_permutation_entropy_jerk},
    "dpe_drv3_015_sample_entropy_jerk": {"inputs": ["close"], "func": dpe_drv3_015_sample_entropy_jerk},
    "dpe_drv3_016_joint_entropy_jerk": {"inputs": ["close", "volume"], "func": dpe_drv3_016_joint_entropy_jerk},
    "dpe_drv3_017_entropy_divergence_jerk": {"inputs": ["close", "sharesbas"], "func": dpe_drv3_017_entropy_divergence_jerk},
    "dpe_drv3_018_path_curviness_jerk": {"inputs": ["close"], "func": dpe_drv3_018_path_curviness_jerk},
    "dpe_drv3_019_entropy_weighted_avg_jerk": {"inputs": ["close"], "func": dpe_drv3_019_entropy_weighted_avg_jerk},
    "dpe_drv3_020_final_chaos_index_jerk": {"inputs": ["close", "volume"], "func": dpe_drv3_020_final_chaos_index_jerk},
    "dpe_drv3_021_underwater_area_entropy_jerk": {"inputs": ["close"], "func": dpe_drv3_021_underwater_area_entropy_jerk},
    "dpe_drv3_022_entropy_of_volatility_jerk": {"inputs": ["close"], "func": dpe_drv3_022_entropy_of_volatility_jerk},
    "dpe_drv3_023_path_smoothness_jerk": {"inputs": ["close"], "func": dpe_drv3_023_path_smoothness_jerk},
    "dpe_drv3_024_revenue_ps_entropy_jerk": {"inputs": ["revenue", "sharesbas"], "func": dpe_drv3_024_revenue_ps_entropy_jerk},
    "dpe_drv3_025_entropy_normalized_duration_jerk": {"inputs": ["close"], "func": dpe_drv3_025_entropy_normalized_duration_jerk},
}
