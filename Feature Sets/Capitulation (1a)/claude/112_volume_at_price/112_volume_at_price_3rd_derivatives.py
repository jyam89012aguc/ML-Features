"""
112_volume_at_price — 3rd Derivatives (Features vap_drv3_001-025)
Domain: rate of change of 2nd-derivative VAP features — acceleration of VAP velocity
Captures acceleration of POC distance change, overhead supply build rate, VWAP drift speed
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9
_VAP_BINS = 20

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


def _vwap_window(close: pd.Series, volume: pd.Series, w: int) -> pd.Series:
    """Rolling VWAP over w periods."""
    cum_pv = _rolling_sum(close * volume, w)
    cum_v = _rolling_sum(volume, w)
    return _safe_div(cum_pv, cum_v)


def _vwap_std_window(close: pd.Series, volume: pd.Series, w: int) -> pd.Series:
    """Rolling volume-weighted standard deviation."""
    vwap = _vwap_window(close, volume, w)
    sq_dev = (close - vwap) ** 2
    cum_vsq = _rolling_sum(sq_dev * volume, w)
    cum_v = _rolling_sum(volume, w)
    var = _safe_div(cum_vsq, cum_v)
    return var.clip(lower=0.0).apply(lambda x: np.sqrt(x) if not np.isnan(x) else np.nan)


def _poc_window(close: pd.Series, volume: pd.Series, w: int, bins: int = _VAP_BINS) -> pd.Series:
    """Rolling POC price level."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    for i in range(n):
        start = max(0, i - w + 1)
        c_w = c_arr[start:i + 1]
        v_w = v_arr[start:i + 1]
        mask = ~(np.isnan(c_w) | np.isnan(v_w))
        c_w = c_w[mask]
        v_w = v_w[mask]
        if len(c_w) < max(2, w // 2):
            continue
        lo, hi = c_w.min(), c_w.max()
        if hi <= lo:
            result[i] = lo
            continue
        edges = np.linspace(lo, hi, bins + 1)
        hist_v = np.zeros(bins, dtype=float)
        for b in range(bins):
            mbk = (c_w >= edges[b]) & (c_w < edges[b + 1]) if b < bins - 1 else (c_w >= edges[b]) & (c_w <= edges[b + 1])
            hist_v[b] = v_w[mbk].sum()
        poc_bin = int(np.argmax(hist_v))
        result[i] = (edges[poc_bin] + edges[poc_bin + 1]) / 2.0
    return pd.Series(result, index=close.index)


def _overhead_vol_fraction(close: pd.Series, volume: pd.Series, w: int) -> pd.Series:
    """Fraction of trailing w-bar volume ABOVE current close."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    for i in range(n):
        start = max(0, i - w + 1)
        c_w = c_arr[start:i + 1]
        v_w = v_arr[start:i + 1]
        mask = ~(np.isnan(c_w) | np.isnan(v_w))
        c_w = c_w[mask]
        v_w = v_w[mask]
        if len(c_w) < max(2, w // 2):
            continue
        cur = c_arr[i]
        if np.isnan(cur):
            continue
        total = v_w.sum()
        if total == 0:
            continue
        result[i] = v_w[c_w > cur].sum() / total
    return pd.Series(result, index=close.index)


def _hvn_proximity(close: pd.Series, volume: pd.Series, w: int,
                   bins: int = _VAP_BINS, top_n: int = 3) -> pd.Series:
    """Distance from current price to nearest HVN (normalised)."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    for i in range(n):
        start = max(0, i - w + 1)
        c_w = c_arr[start:i + 1]
        v_w = v_arr[start:i + 1]
        mask = ~(np.isnan(c_w) | np.isnan(v_w))
        c_w = c_w[mask]
        v_w = v_w[mask]
        if len(c_w) < max(2, w // 2):
            continue
        cur = c_arr[i]
        if np.isnan(cur):
            continue
        lo, hi = c_w.min(), c_w.max()
        if hi <= lo:
            result[i] = 0.0
            continue
        edges = np.linspace(lo, hi, bins + 1)
        mids = (edges[:-1] + edges[1:]) / 2.0
        hist_v = np.zeros(bins, dtype=float)
        for b in range(bins):
            mbk = (c_w >= edges[b]) & (c_w < edges[b + 1]) if b < bins - 1 else (c_w >= edges[b]) & (c_w <= edges[b + 1])
            hist_v[b] = v_w[mbk].sum()
        top_idx = np.argsort(hist_v)[-top_n:]
        hvn_prices = mids[top_idx]
        dists = np.abs(hvn_prices - cur)
        result[i] = dists.min() / (hi - lo)
    return pd.Series(result, index=close.index)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def vap_drv3_001_poc_dist_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day POC distance (acceleration of POC pressure velocity)."""
    dist = _safe_div(close - _poc_window(close, volume, _TD_MON),
                     _poc_window(close, volume, _TD_MON).clip(lower=_EPS))
    vel = dist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vap_drv3_002_poc_dist_63d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day POC distance (acceleration of quarterly POC drift)."""
    dist = _safe_div(close - _poc_window(close, volume, _TD_QTR),
                     _poc_window(close, volume, _TD_QTR).clip(lower=_EPS))
    vel = dist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vap_drv3_003_poc_dist_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 63-day POC distance (jerk in monthly POC velocity)."""
    dist = _safe_div(close - _poc_window(close, volume, _TD_QTR),
                     _poc_window(close, volume, _TD_QTR).clip(lower=_EPS))
    vel21 = dist.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vap_drv3_004_overhead_frac_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day overhead fraction (acceleration of overhead supply change)."""
    vel = _overhead_vol_fraction(close, volume, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vap_drv3_005_overhead_frac_63d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day overhead fraction."""
    vel = _overhead_vol_fraction(close, volume, _TD_QTR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vap_drv3_006_overhead_frac_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 63-day overhead fraction."""
    vel21 = _overhead_vol_fraction(close, volume, _TD_QTR).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vap_drv3_007_vwap_dist_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day VWAP distance (acceleration of VWAP pressure)."""
    dist = _safe_div(close - _vwap_window(close, volume, _TD_MON),
                     _vwap_window(close, volume, _TD_MON).clip(lower=_EPS))
    vel = dist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vap_drv3_008_vwap_dist_63d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day VWAP distance."""
    dist = _safe_div(close - _vwap_window(close, volume, _TD_QTR),
                     _vwap_window(close, volume, _TD_QTR).clip(lower=_EPS))
    vel = dist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vap_drv3_009_vwap_dist_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 63-day VWAP distance."""
    dist = _safe_div(close - _vwap_window(close, volume, _TD_QTR),
                     _vwap_window(close, volume, _TD_QTR).clip(lower=_EPS))
    vel21 = dist.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vap_drv3_010_vwap_band_zscore_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day VWAP-band z-score."""
    vwap = _vwap_window(close, volume, _TD_MON)
    vstd = _vwap_std_window(close, volume, _TD_MON)
    z = _safe_div(close - vwap, vstd.clip(lower=_EPS))
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vap_drv3_011_vwap_band_zscore_63d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day VWAP-band z-score."""
    vwap = _vwap_window(close, volume, _TD_QTR)
    vstd = _vwap_std_window(close, volume, _TD_QTR)
    z = _safe_div(close - vwap, vstd.clip(lower=_EPS))
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vap_drv3_012_hvn_proximity_63d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day HVN proximity (acceleration of HVN drift)."""
    vel = _hvn_proximity(close, volume, _TD_QTR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vap_drv3_013_hvn_proximity_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day HVN proximity."""
    vel21 = _hvn_proximity(close, volume, _TD_QTR).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vap_drv3_014_poc_dist_252d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day POC distance."""
    dist = _safe_div(close - _poc_window(close, volume, _TD_YEAR),
                     _poc_window(close, volume, _TD_YEAR).clip(lower=_EPS))
    vel = dist.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vap_drv3_015_overhead_frac_252d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day overhead fraction."""
    vel = _overhead_vol_fraction(close, volume, _TD_YEAR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vap_drv3_016_poc_dist_21d_5d_diff_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day OLS slope of the 5-day velocity of 21-day POC distance."""
    dist = _safe_div(close - _poc_window(close, volume, _TD_MON),
                     _poc_window(close, volume, _TD_MON).clip(lower=_EPS))
    vel = dist.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vap_drv3_017_overhead_frac_21d_5d_diff_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day OLS slope of the 5-day velocity of 21-day overhead fraction."""
    vel = _overhead_vol_fraction(close, volume, _TD_MON).diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vap_drv3_018_vwap_dist_21d_5d_diff_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day OLS slope of the 5-day velocity of 21-day VWAP distance."""
    dist = _safe_div(close - _vwap_window(close, volume, _TD_MON),
                     _vwap_window(close, volume, _TD_MON).clip(lower=_EPS))
    vel = dist.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vap_drv3_019_vwap_dist_63d_5d_diff_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day OLS slope of the 5-day velocity of 63-day VWAP distance."""
    dist = _safe_div(close - _vwap_window(close, volume, _TD_QTR),
                     _vwap_window(close, volume, _TD_QTR).clip(lower=_EPS))
    vel = dist.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vap_drv3_020_overhead_frac_63d_5d_diff_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day OLS slope of the 5-day velocity of 63-day overhead fraction."""
    vel = _overhead_vol_fraction(close, volume, _TD_QTR).diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vap_drv3_021_poc_dist_252d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 252-day POC distance."""
    dist = _safe_div(close - _poc_window(close, volume, _TD_YEAR),
                     _poc_window(close, volume, _TD_YEAR).clip(lower=_EPS))
    vel21 = dist.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vap_drv3_022_overhead_frac_252d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 252-day overhead fraction."""
    vel21 = _overhead_vol_fraction(close, volume, _TD_YEAR).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def vap_drv3_023_vwap_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day VWAP level (acceleration of VWAP decline)."""
    vel = _vwap_window(close, volume, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vap_drv3_024_poc_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day POC price level (acceleration of POC decline)."""
    vel = _poc_window(close, volume, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vap_drv3_025_overhead_composite_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of composite overhead fraction (acceleration of avg overhead build)."""
    composite = (
        _overhead_vol_fraction(close, volume, _TD_MON) +
        _overhead_vol_fraction(close, volume, _TD_QTR) +
        _overhead_vol_fraction(close, volume, _TD_YEAR)
    ) / 3.0
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_AT_PRICE_REGISTRY_3RD_DERIVATIVES = {
    "vap_drv3_001_poc_dist_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vap_drv3_001_poc_dist_21d_5d_diff_5d_diff},
    "vap_drv3_002_poc_dist_63d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vap_drv3_002_poc_dist_63d_5d_diff_5d_diff},
    "vap_drv3_003_poc_dist_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vap_drv3_003_poc_dist_63d_21d_diff_5d_diff},
    "vap_drv3_004_overhead_frac_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vap_drv3_004_overhead_frac_21d_5d_diff_5d_diff},
    "vap_drv3_005_overhead_frac_63d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vap_drv3_005_overhead_frac_63d_5d_diff_5d_diff},
    "vap_drv3_006_overhead_frac_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vap_drv3_006_overhead_frac_63d_21d_diff_5d_diff},
    "vap_drv3_007_vwap_dist_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vap_drv3_007_vwap_dist_21d_5d_diff_5d_diff},
    "vap_drv3_008_vwap_dist_63d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vap_drv3_008_vwap_dist_63d_5d_diff_5d_diff},
    "vap_drv3_009_vwap_dist_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vap_drv3_009_vwap_dist_63d_21d_diff_5d_diff},
    "vap_drv3_010_vwap_band_zscore_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vap_drv3_010_vwap_band_zscore_21d_5d_diff_5d_diff},
    "vap_drv3_011_vwap_band_zscore_63d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vap_drv3_011_vwap_band_zscore_63d_5d_diff_5d_diff},
    "vap_drv3_012_hvn_proximity_63d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vap_drv3_012_hvn_proximity_63d_5d_diff_5d_diff},
    "vap_drv3_013_hvn_proximity_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vap_drv3_013_hvn_proximity_63d_21d_diff_5d_diff},
    "vap_drv3_014_poc_dist_252d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vap_drv3_014_poc_dist_252d_5d_diff_5d_diff},
    "vap_drv3_015_overhead_frac_252d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vap_drv3_015_overhead_frac_252d_5d_diff_5d_diff},
    "vap_drv3_016_poc_dist_21d_5d_diff_slope_21d": {"inputs": ["close", "volume"], "func": vap_drv3_016_poc_dist_21d_5d_diff_slope_21d},
    "vap_drv3_017_overhead_frac_21d_5d_diff_slope_21d": {"inputs": ["close", "volume"], "func": vap_drv3_017_overhead_frac_21d_5d_diff_slope_21d},
    "vap_drv3_018_vwap_dist_21d_5d_diff_slope_21d": {"inputs": ["close", "volume"], "func": vap_drv3_018_vwap_dist_21d_5d_diff_slope_21d},
    "vap_drv3_019_vwap_dist_63d_5d_diff_slope_21d": {"inputs": ["close", "volume"], "func": vap_drv3_019_vwap_dist_63d_5d_diff_slope_21d},
    "vap_drv3_020_overhead_frac_63d_5d_diff_slope_21d": {"inputs": ["close", "volume"], "func": vap_drv3_020_overhead_frac_63d_5d_diff_slope_21d},
    "vap_drv3_021_poc_dist_252d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vap_drv3_021_poc_dist_252d_21d_diff_5d_diff},
    "vap_drv3_022_overhead_frac_252d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vap_drv3_022_overhead_frac_252d_21d_diff_5d_diff},
    "vap_drv3_023_vwap_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vap_drv3_023_vwap_21d_5d_diff_5d_diff},
    "vap_drv3_024_poc_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vap_drv3_024_poc_21d_5d_diff_5d_diff},
    "vap_drv3_025_overhead_composite_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vap_drv3_025_overhead_composite_5d_diff_5d_diff},
}
