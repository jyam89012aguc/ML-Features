"""
33_volatility_convexity — 2nd Derivatives
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

# 25 features capturing acceleration of volatility convexity metrics
def vcvx_drv2_001_vol_curvature_21d_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    def _poly2(y):
        if len(y) < 3: return 0.0
        return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(21).apply(_poly2, raw=True)
    return curv.diff(5)


def vcvx_drv2_002_vol_area_ratio_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    area = v.rolling(63).sum()
    max_v = v.rolling(63).max()
    ratio = _safe_div(area, max_v * 63)
    return ratio.diff(5)


def vcvx_drv2_003_vol_bow_factor_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    bow = v.rolling(63).median() - v.rolling(63).mean()
    return bow.diff(5)


def vcvx_drv2_004_parabolic_fear_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(63).apply(_poly2, raw=True).abs()
    accel = v.diff(5).diff(5).abs()
    h = close.rolling(252).max()
    dd = (h - close) / h
    score = curv * accel * dd
    return score.diff(5)


def vcvx_drv2_005_vol_v_shape_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    def _vscore(y):
        mid = len(y) // 2
        from scipy.stats import linregress
        s1 = linregress(np.arange(mid), y[:mid]).slope
        s2 = linregress(np.arange(mid), y[mid:]).slope
        return s2 - s1
    vs = v.rolling(21).apply(_vscore, raw=True)
    return vs.diff(5)


def vcvx_drv2_006_vol_conv_regime_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    def _curv(w):
        def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
        return v.rolling(w).apply(_poly2, raw=True).abs()
    ratio = _safe_div(_curv(21), _curv(63))
    return ratio.diff(5)


def vcvx_drv2_007_vol_jitter_conv_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    cv = v.rolling(21).std() / (v.rolling(21).mean() + _EPS)
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = cv.rolling(21).apply(_poly2, raw=True)
    return curv.diff(5)


def vcvx_drv2_008_vw_vol_curvature_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    v_norm = _safe_div(volume, volume.rolling(63).mean())
    wv = v * v_norm
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = wv.rolling(63).apply(_poly2, raw=True)
    return curv.diff(5)


def vcvx_drv2_009_vol_path_efficiency_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    net = (v - v.shift(63)).abs()
    path = v.diff().abs().rolling(63).sum()
    eff = _safe_div(net, path)
    return eff.diff(5)


def vcvx_drv2_010_mktcap_vol_curvature_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v = np.log(mc / mc.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(63).apply(_poly2, raw=True)
    return curv.diff(5)


def vcvx_drv2_011_vol_decay_conv_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(5).std()
    def _decay(y):
        from scipy.stats import linregress
        return linregress(np.arange(len(y)), np.log(y + _EPS)).slope
    dec = v.rolling(63).apply(_decay, raw=True)
    return dec.diff(5)


def vcvx_drv2_012_vol_curv_entropy_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(63).apply(_poly2, raw=True).abs()
    def _ent(y):
        if len(y) == 0: return 0.0
        h, _ = np.histogram(y[~np.isnan(y)], bins=5)
        p = h / (np.sum(h) + _EPS)
        return -np.sum(p[p > 0] * np.log(p[p > 0]))
    e = curv.rolling(63).apply(_ent, raw=True)
    return e.diff(5)


def vcvx_drv2_013_joint_vol_range_curv_velocity(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    r = (high - low) / close
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    vc = v.rolling(63).apply(_poly2, raw=True)
    rc = r.rolling(63).apply(_poly2, raw=True)
    idx = vc * rc
    return idx.diff(5)


def vcvx_drv2_014_vol_conv_final_exhaustion_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    score = vcvx_150_vol_convexity_final_exhaustion(close, volume)
    return score.diff(5)


def vcvx_drv2_015_vol_curvature_rank_velocity(close: pd.Series) -> pd.Series:
    v21 = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v21.rolling(63).apply(_poly2, raw=True).abs()
    rank = curv.expanding().rank(pct=True)
    return rank.diff(5)


def vcvx_drv2_016_consecutive_convex_vol_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(21).apply(_poly2, raw=True)
    is_convex = (curv > 0).astype(int)
    dur = is_convex.groupby((is_convex == 0).cumsum()).cumsum()
    return dur.diff(5)


def vcvx_drv2_017_vol_area_ratio_zscore_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    ratio = _safe_div(v.rolling(63).sum(), v.rolling(63).max() * 63)
    z = (ratio - ratio.rolling(252).mean()) / (ratio.rolling(252).std() + _EPS)
    return z.diff(5)


def vcvx_drv2_018_vol_accel_curv_ratio_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    a = v.diff(5).diff(5).abs()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(63).apply(_poly2, raw=True).abs()
    ratio = _safe_div(a, curv)
    return ratio.diff(5)


def vcvx_drv2_019_mktcap_vol_area_velocity(close: pd.Series, sharesbas: pd.Series) -> pd.Series:
    mc = close * sharesbas
    v = np.log(mc / mc.shift(1)).rolling(21).std()
    area = _safe_div(v.rolling(252).sum(), v.rolling(252).max() * 252)
    return area.diff(5)


def vcvx_drv2_020_vol_parabolic_blowoff_velocity(close: pd.Series, volume: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(63).apply(_poly2, raw=True).abs()
    vs = _safe_div(volume, volume.rolling(252).median())
    net_m = (close / close.shift(21) - 1).abs()
    path = close.diff().abs().rolling(21).sum()
    eff = _safe_div(net_m, path)
    score = (curv * vs) / (eff + _EPS)
    return score.diff(5)


def vcvx_drv2_021_consecutive_inc_vol_curv_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(63).apply(_poly2, raw=True).abs()
    inc = (curv > curv.shift(1)).astype(int)
    dur = inc.groupby((inc == 0).cumsum()).cumsum()
    return dur.diff(5)


def vcvx_drv2_022_vol_curv_reversal_velocity(close: pd.Series, low: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(63).apply(_poly2, raw=True).abs()
    score = curv.diff(5) * _safe_div(close, low)
    return score.diff(5)


def vcvx_drv2_023_vol_area_regime_break_velocity(close: pd.Series) -> pd.Series:
    def _ar(w):
        v = np.log(close / close.shift(1)).rolling(5).std()
        return _safe_div(v.rolling(w).sum(), v.rolling(w).max() * w)
    brk = _ar(21) - _ar(126)
    return brk.diff(5)


def vcvx_drv2_024_cumulative_curv_energy_velocity(close: pd.Series) -> pd.Series:
    v = np.log(close / close.shift(1)).rolling(21).std()
    def _poly2(y): return np.polyfit(np.arange(len(y)), y, 2)[0]
    curv = v.rolling(63).apply(_poly2, raw=True).abs()
    energy = curv.cumsum() / (curv.abs().cumsum() + _EPS)
    return energy.diff(5)


def vcvx_drv2_025_vol_conv_final_composite_velocity(close: pd.Series) -> pd.Series:
    score = vcvx_075_vol_convexity_final_composite(close)
    return score.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

V33_V_REGISTRY = {
    "vcvx_drv2_001_vol_curvature_21d_velocity": {"inputs": ["close"], "func": vcvx_drv2_001_vol_curvature_21d_velocity},
    "vcvx_drv2_002_vol_area_ratio_velocity": {"inputs": ["close"], "func": vcvx_drv2_002_vol_area_ratio_velocity},
    "vcvx_drv2_003_vol_bow_factor_velocity": {"inputs": ["close"], "func": vcvx_drv2_003_vol_bow_factor_velocity},
    "vcvx_drv2_004_parabolic_fear_velocity": {"inputs": ["close"], "func": vcvx_drv2_004_parabolic_fear_velocity},
    "vcvx_drv2_005_vol_v_shape_velocity": {"inputs": ["close"], "func": vcvx_drv2_005_vol_v_shape_velocity},
    "vcvx_drv2_006_vol_conv_regime_velocity": {"inputs": ["close"], "func": vcvx_drv2_006_vol_conv_regime_velocity},
    "vcvx_drv2_007_vol_jitter_conv_velocity": {"inputs": ["close"], "func": vcvx_drv2_007_vol_jitter_conv_velocity},
    "vcvx_drv2_008_vw_vol_curvature_velocity": {"inputs": ["close", "volume"], "func": vcvx_drv2_008_vw_vol_curvature_velocity},
    "vcvx_drv2_009_vol_path_efficiency_velocity": {"inputs": ["close"], "func": vcvx_drv2_009_vol_path_efficiency_velocity},
    "vcvx_drv2_010_mktcap_vol_curvature_velocity": {"inputs": ["close", "sharesbas"], "func": vcvx_drv2_010_mktcap_vol_curvature_velocity},
    "vcvx_drv2_011_vol_decay_conv_velocity": {"inputs": ["close"], "func": vcvx_drv2_011_vol_decay_conv_velocity},
    "vcvx_drv2_012_vol_curv_entropy_velocity": {"inputs": ["close"], "func": vcvx_drv2_012_vol_curv_entropy_velocity},
    "vcvx_drv2_013_joint_vol_range_curv_velocity": {"inputs": ["high", "low", "close"], "func": vcvx_drv2_013_joint_vol_range_curv_velocity},
    "vcvx_drv2_014_vol_conv_final_exhaustion_velocity": {"inputs": ["close", "volume"], "func": vcvx_drv2_014_vol_conv_final_exhaustion_velocity},
    "vcvx_drv2_015_vol_curvature_rank_velocity": {"inputs": ["close"], "func": vcvx_drv2_015_vol_curvature_rank_velocity},
    "vcvx_drv2_016_consecutive_convex_vol_velocity": {"inputs": ["close"], "func": vcvx_drv2_016_consecutive_convex_vol_velocity},
    "vcvx_drv2_017_vol_area_ratio_zscore_velocity": {"inputs": ["close"], "func": vcvx_drv2_017_vol_area_ratio_zscore_velocity},
    "vcvx_drv2_018_vol_accel_curv_ratio_velocity": {"inputs": ["close"], "func": vcvx_drv2_018_vol_accel_curv_ratio_velocity},
    "vcvx_drv2_019_mktcap_vol_area_velocity": {"inputs": ["close", "sharesbas"], "func": vcvx_drv2_019_mktcap_vol_area_velocity},
    "vcvx_drv2_020_vol_parabolic_blowoff_velocity": {"inputs": ["close", "volume"], "func": vcvx_drv2_020_vol_parabolic_blowoff_velocity},
    "vcvx_drv2_021_consecutive_inc_vol_curv_velocity": {"inputs": ["close"], "func": vcvx_drv2_021_consecutive_inc_vol_curv_velocity},
    "vcvx_drv2_022_vol_curv_reversal_velocity": {"inputs": ["close", "low"], "func": vcvx_drv2_022_vol_curv_reversal_velocity},
    "vcvx_drv2_023_vol_area_regime_break_velocity": {"inputs": ["close"], "func": vcvx_drv2_023_vol_area_regime_break_velocity},
    "vcvx_drv2_024_cumulative_curv_energy_velocity": {"inputs": ["close"], "func": vcvx_drv2_024_cumulative_curv_energy_velocity},
    "vcvx_drv2_025_vol_conv_final_composite_velocity": {"inputs": ["close"], "func": vcvx_drv2_025_vol_conv_final_composite_velocity},
}
