"""
13_drawdown_acceleration — 2nd Derivatives
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


def _calculate_accel(s: pd.Series, w: int) -> pd.Series:
    vel = s.diff(w) / w
    return vel.diff(w) / w


# ── Feature functions ────────────────────────────────────────────────────────

# 25 features capturing acceleration of drawdown acceleration metrics (jerk proxy)
def dacc_drv2_001_price_accel_5d_velocity(close: pd.Series) -> pd.Series:
    # Rate of change of 5-day acceleration
    a = _calculate_accel(np.log(close), 5)
    return a.diff(5)


def dacc_drv2_002_drawdown_accel_21d_velocity(close: pd.Series) -> pd.Series:
    h = close.rolling(252).max()
    dd = (close - h) / h
    a = _calculate_accel(dd, 5)
    return a.diff(5)


def dacc_drv2_003_sigma_accel_21d_velocity(close: pd.Series) -> pd.Series:
    a = _calculate_accel(np.log(close), 5)
    v = close.pct_change().rolling(21).std()
    sa = _safe_div(a, v)
    return sa.diff(5)


def dacc_drv2_004_accel_zscore_velocity(close: pd.Series) -> pd.Series:
    a = _calculate_accel(np.log(close), 5)
    z = (a - a.rolling(252).mean()) / a.rolling(252).std()
    return z.diff(5)


def dacc_drv2_005_mktcap_accel_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    a = _calculate_accel(np.log(mc), 21)
    return a.diff(5)


def dacc_drv2_006_accel_regime_shift_velocity(close: pd.Series) -> pd.Series:
    a5 = _calculate_accel(np.log(close), 5).abs()
    a63 = a5.rolling(63).mean()
    rsi = _safe_div(a5, a63)
    return rsi.diff(5)


def dacc_drv2_007_accel_to_velocity_ratio_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close).diff(5) / 5.0
    a = v.diff(5) / 5.0
    ratio = _safe_div(a, v.abs())
    return ratio.diff(5)


def dacc_drv2_008_acceleration_climax_velocity(close: pd.Series) -> pd.Series:
    a = _calculate_accel(np.log(close), 5).abs()
    v = close.pct_change().rolling(21).std()
    path_len = close.diff().abs().rolling(21).sum()
    eff = _safe_div((close - close.shift(21)).abs(), path_len)
    idx = a * v * (1.0 - eff)
    return idx.diff(5)


def dacc_drv2_009_ema_accel_velocity(close: pd.Series) -> pd.Series:
    ema = close.ewm(span=21).mean()
    a = _calculate_accel(np.log(ema), 5)
    return a.diff(5)


def dacc_drv2_010_accel_oscillation_velocity(close: pd.Series) -> pd.Series:
    a = _calculate_accel(np.log(close), 5)
    osc = _safe_div(a.rolling(63).std(), a.rolling(63).mean().abs())
    return osc.diff(5)


def dacc_drv2_011_ath_drawdown_accel_velocity(close: pd.Series) -> pd.Series:
    h = close.cummax()
    dist = (h - close) / h
    a = _calculate_accel(dist, 21)
    return a.diff(5)


def dacc_drv2_012_accel_persistence_prob_velocity(close: pd.Series) -> pd.Series:
    a = _calculate_accel(np.log(close), 1)
    neg = (a < 0)
    prob = (neg & neg.shift(1)).rolling(63).sum() / (neg.shift(1).rolling(63).sum() + _EPS)
    return prob.diff(5)


def dacc_drv2_013_terminal_accel_decay_velocity(close: pd.Series) -> pd.Series:
    a5 = _calculate_accel(np.log(close), 5)
    a21 = _calculate_accel(np.log(close), 21)
    score = a5 - a21
    return score.diff(5)


def dacc_drv2_014_underwater_area_accel_velocity(close: pd.Series) -> pd.Series:
    h = close.rolling(252).max()
    uw = (close - h) / h
    integral = uw.rolling(21).sum()
    a = _calculate_accel(integral, 21)
    return a.diff(5)


def dacc_drv2_015_accel_entropy_velocity(close: pd.Series) -> pd.Series:
    a = _calculate_accel(np.log(close), 5)
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y[~np.isnan(y)], bins=10)
        p = h / (np.sum(h) + _EPS)
        return -np.sum(p[p > 0] * np.log(p[p > 0]))
    e = a.rolling(63).apply(_ent, raw=True)
    return e.diff(5)


def dacc_drv2_016_accel_volatility_velocity(close: pd.Series) -> pd.Series:
    a = _calculate_accel(np.log(close), 1)
    v = a.rolling(63).std()
    return v.diff(5)


def dacc_drv2_017_accel_skewness_velocity(close: pd.Series) -> pd.Series:
    a = _calculate_accel(np.log(close), 5)
    return a.rolling(63).skew().diff(5)


def dacc_drv2_018_log_price_curvature_velocity(close: pd.Series) -> pd.Series:
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = np.log(close).rolling(63).apply(_poly2, raw=True)
    return curv.diff(5)


def dacc_drv2_019_mktcap_to_revenue_accel_velocity(close: pd.Series, sharesbas: pd.Series, revenue: pd.Series) -> pd.Series:
    a_mc = _calculate_accel(np.log(close * sharesbas), 21)
    a_rev = _calculate_accel(np.log(revenue + _EPS), 1)
    ratio = _safe_div(a_mc, a_rev)
    return ratio.diff(1)


def dacc_drv2_020_terminal_drawdown_accel_velocity(close: pd.Series) -> pd.Series:
    a5 = _calculate_accel(np.log(close), 5)
    return a5.diff(5)


def dacc_drv2_021_accel_energy_density_velocity(close: pd.Series) -> pd.Series:
    a = _calculate_accel(np.log(close), 5)
    v = close.pct_change().rolling(63).std()
    ed = _safe_div((a**2).rolling(63).mean(), v)
    return ed.diff(5)


def dacc_drv2_022_accel_jump_ratio_velocity(close: pd.Series) -> pd.Series:
    a = _calculate_accel(np.log(close), 1).abs()
    ratio = _safe_div(a, a.rolling(21).max())
    return ratio.diff(5)


def dacc_drv2_023_accel_normalized_depth_velocity(close: pd.Series) -> pd.Series:
    a = _calculate_accel(np.log(close), 5).abs()
    h = close.rolling(252).max()
    dd = (h - close) / h
    ratio = _safe_div(a, dd + _EPS)
    return ratio.diff(5)


def dacc_drv2_024_accel_autocorr_velocity(close: pd.Series) -> pd.Series:
    a = _calculate_accel(np.log(close), 5)
    ac = a.rolling(63).apply(lambda x: pd.Series(x).autocorr(lag=1), raw=True)
    return ac.diff(5)


def dacc_drv2_025_final_accel_composite_velocity(close: pd.Series) -> pd.Series:
    a5 = _calculate_accel(np.log(close), 5).abs()
    a21 = _calculate_accel(np.log(close), 21).abs()
    a63 = _calculate_accel(np.log(close), 63).abs()
    comp = (0.5 * a5 + 0.3 * a21 + 0.2 * a63)
    return comp.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V13_V_REGISTRY = {
    "dacc_drv2_001_price_accel_5d_velocity": {"inputs": ["close"], "func": dacc_drv2_001_price_accel_5d_velocity},
    "dacc_drv2_002_drawdown_accel_21d_velocity": {"inputs": ["close"], "func": dacc_drv2_002_drawdown_accel_21d_velocity},
    "dacc_drv2_003_sigma_accel_21d_velocity": {"inputs": ["close"], "func": dacc_drv2_003_sigma_accel_21d_velocity},
    "dacc_drv2_004_accel_zscore_velocity": {"inputs": ["close"], "func": dacc_drv2_004_accel_zscore_velocity},
    "dacc_drv2_005_mktcap_accel_velocity": {"inputs": ["close", "sharesbas"], "func": dacc_drv2_005_mktcap_accel_velocity},
    "dacc_drv2_006_accel_regime_shift_velocity": {"inputs": ["close"], "func": dacc_drv2_006_accel_regime_shift_velocity},
    "dacc_drv2_007_accel_to_velocity_ratio_velocity": {"inputs": ["close"], "func": dacc_drv2_007_accel_to_velocity_ratio_velocity},
    "dacc_drv2_008_acceleration_climax_velocity": {"inputs": ["close"], "func": dacc_drv2_008_acceleration_climax_velocity},
    "dacc_drv2_009_ema_accel_velocity": {"inputs": ["close"], "func": dacc_drv2_009_ema_accel_velocity},
    "dacc_drv2_010_accel_oscillation_velocity": {"inputs": ["close"], "func": dacc_drv2_010_accel_oscillation_velocity},
    "dacc_drv2_011_ath_drawdown_accel_velocity": {"inputs": ["close"], "func": dacc_drv2_011_ath_drawdown_accel_velocity},
    "dacc_drv2_012_accel_persistence_prob_velocity": {"inputs": ["close"], "func": dacc_drv2_012_accel_persistence_prob_velocity},
    "dacc_drv2_013_terminal_accel_decay_velocity": {"inputs": ["close"], "func": dacc_drv2_013_terminal_accel_decay_velocity},
    "dacc_drv2_014_underwater_area_accel_velocity": {"inputs": ["close"], "func": dacc_drv2_014_underwater_area_accel_velocity},
    "dacc_drv2_015_accel_entropy_velocity": {"inputs": ["close"], "func": dacc_drv2_015_accel_entropy_velocity},
    "dacc_drv2_016_accel_volatility_velocity": {"inputs": ["close"], "func": dacc_drv2_016_accel_volatility_velocity},
    "dacc_drv2_017_accel_skewness_velocity": {"inputs": ["close"], "func": dacc_drv2_017_accel_skewness_velocity},
    "dacc_drv2_018_log_price_curvature_velocity": {"inputs": ["close"], "func": dacc_drv2_018_log_price_curvature_velocity},
    "dacc_drv2_019_mktcap_to_revenue_accel_velocity": {"inputs": ["close", "sharesbas", "revenue"], "func": dacc_drv2_019_mktcap_to_revenue_accel_velocity},
    "dacc_drv2_020_terminal_drawdown_accel_velocity": {"inputs": ["close"], "func": dacc_drv2_020_terminal_drawdown_accel_velocity},
    "dacc_drv2_021_accel_energy_density_velocity": {"inputs": ["close"], "func": dacc_drv2_021_accel_energy_density_velocity},
    "dacc_drv2_022_accel_jump_ratio_velocity": {"inputs": ["close"], "func": dacc_drv2_022_accel_jump_ratio_velocity},
    "dacc_drv2_023_accel_normalized_depth_velocity": {"inputs": ["close"], "func": dacc_drv2_023_accel_normalized_depth_velocity},
    "dacc_drv2_024_accel_autocorr_velocity": {"inputs": ["close"], "func": dacc_drv2_024_accel_autocorr_velocity},
    "dacc_drv2_025_final_accel_composite_velocity": {"inputs": ["close"], "func": dacc_drv2_025_final_accel_composite_velocity},
}
