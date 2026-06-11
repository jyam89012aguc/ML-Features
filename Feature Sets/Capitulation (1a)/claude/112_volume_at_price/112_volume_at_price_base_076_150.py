"""
112_volume_at_price — Base Features 076-150
Domain: Volume-at-price structure — VAP histogram variants, value-area dynamics,
        VWAP composite features, multi-window overhead supply, volume-profile
        divergence, bin-level volume imbalance, and cross-window comparisons
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
    """Element-wise division; replaces zero denominator with NaN."""
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _vwap_window(close: pd.Series, volume: pd.Series, w: int) -> pd.Series:
    """Rolling VWAP over w periods."""
    cum_pv = _rolling_sum(close * volume, w)
    cum_v = _rolling_sum(volume, w)
    return _safe_div(cum_pv, cum_v)


def _vwap_std_window(close: pd.Series, volume: pd.Series, w: int) -> pd.Series:
    """Rolling volume-weighted standard deviation of price over w periods."""
    vwap = _vwap_window(close, volume, w)
    sq_dev = (close - vwap) ** 2
    cum_vsq = _rolling_sum(sq_dev * volume, w)
    cum_v = _rolling_sum(volume, w)
    var = _safe_div(cum_vsq, cum_v)
    return var.clip(lower=0.0).apply(lambda x: np.sqrt(x) if not np.isnan(x) else np.nan)


def _poc_window(close: pd.Series, volume: pd.Series, w: int, bins: int = _VAP_BINS) -> pd.Series:
    """Rolling POC price level over trailing w bars."""
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


def _value_area_bounds(close: pd.Series, volume: pd.Series, w: int,
                       va_frac: float = 0.70, bins: int = _VAP_BINS):
    """Rolling value-area (low, high) capturing va_frac of volume."""
    n = len(close)
    va_lo = np.full(n, np.nan)
    va_hi = np.full(n, np.nan)
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
            va_lo[i] = lo
            va_hi[i] = hi
            continue
        edges = np.linspace(lo, hi, bins + 1)
        hist_v = np.zeros(bins, dtype=float)
        for b in range(bins):
            mbk = (c_w >= edges[b]) & (c_w < edges[b + 1]) if b < bins - 1 else (c_w >= edges[b]) & (c_w <= edges[b + 1])
            hist_v[b] = v_w[mbk].sum()
        total_vol = hist_v.sum()
        if total_vol == 0:
            continue
        target = total_vol * va_frac
        poc_bin = int(np.argmax(hist_v))
        accumulated = hist_v[poc_bin]
        lo_ptr = poc_bin
        hi_ptr = poc_bin
        while accumulated < target:
            lo_cand = lo_ptr - 1 if lo_ptr > 0 else -1
            hi_cand = hi_ptr + 1 if hi_ptr < bins - 1 else -1
            lo_vol = hist_v[lo_cand] if lo_cand >= 0 else 0.0
            hi_vol = hist_v[hi_cand] if hi_cand >= 0 else 0.0
            if lo_cand < 0 and hi_cand < 0:
                break
            if lo_vol >= hi_vol and lo_cand >= 0:
                lo_ptr = lo_cand
                accumulated += lo_vol
            elif hi_cand >= 0:
                hi_ptr = hi_cand
                accumulated += hi_vol
            else:
                lo_ptr = lo_cand
                accumulated += lo_vol
        va_lo[i] = edges[lo_ptr]
        va_hi[i] = edges[hi_ptr + 1]
    return pd.Series(va_lo, index=close.index), pd.Series(va_hi, index=close.index)


def _overhead_vol_fraction(close: pd.Series, volume: pd.Series, w: int) -> pd.Series:
    """Fraction of trailing w-bar volume transacted ABOVE current close."""
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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Multi-resolution VAP comparisons ---

def vap_076_poc_dist_21d_vs_252d_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day POC distance to 252-day POC distance (short vs long term divergence)."""
    d21 = _safe_div(close - _poc_window(close, volume, _TD_MON),
                    _poc_window(close, volume, _TD_MON).clip(lower=_EPS))
    d252 = _safe_div(close - _poc_window(close, volume, _TD_YEAR),
                     _poc_window(close, volume, _TD_YEAR).clip(lower=_EPS))
    return _safe_div(d21, d252.abs().clip(lower=_EPS))


def vap_077_vwap_dist_spread_21d_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Spread between 21-day and 252-day VWAP distances (term structure of VWAP pressure)."""
    d21 = _safe_div(close - _vwap_window(close, volume, _TD_MON),
                    _vwap_window(close, volume, _TD_MON).clip(lower=_EPS))
    d252 = _safe_div(close - _vwap_window(close, volume, _TD_YEAR),
                     _vwap_window(close, volume, _TD_YEAR).clip(lower=_EPS))
    return d21 - d252


def vap_078_overhead_frac_spread_21d_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Difference: 252-day overhead fraction minus 21-day overhead fraction."""
    return _overhead_vol_fraction(close, volume, _TD_YEAR) - _overhead_vol_fraction(close, volume, _TD_MON)


def vap_079_poc_21d_below_poc_252d_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: 21-day POC is below 252-day POC (short-term gravity shifted lower)."""
    poc21 = _poc_window(close, volume, _TD_MON)
    poc252 = _poc_window(close, volume, _TD_YEAR)
    return (poc21 < poc252).astype(float)


def vap_080_poc_63d_below_poc_252d_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: 63-day POC is below 252-day POC."""
    poc63 = _poc_window(close, volume, _TD_QTR)
    poc252 = _poc_window(close, volume, _TD_YEAR)
    return (poc63 < poc252).astype(float)


def vap_081_va_low_63d_below_va_low_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: 63-day VA-low is below 252-day VA-low (support deterioration)."""
    va_lo_63, _ = _value_area_bounds(close, volume, _TD_QTR)
    va_lo_252, _ = _value_area_bounds(close, volume, _TD_YEAR)
    return (va_lo_63 < va_lo_252).astype(float)


def vap_082_all_poc_below_price_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: POC at all three windows (21d, 63d, 252d) are all above current price."""
    poc21 = _poc_window(close, volume, _TD_MON)
    poc63 = _poc_window(close, volume, _TD_QTR)
    poc252 = _poc_window(close, volume, _TD_YEAR)
    return ((close < poc21) & (close < poc63) & (close < poc252)).astype(float)


def vap_083_all_vwap_overhead_above_70pct(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: overhead supply > 70% at 21d, 63d, AND 252d simultaneously."""
    o21 = _overhead_vol_fraction(close, volume, _TD_MON)
    o63 = _overhead_vol_fraction(close, volume, _TD_QTR)
    o252 = _overhead_vol_fraction(close, volume, _TD_YEAR)
    return ((o21 > 0.70) & (o63 > 0.70) & (o252 > 0.70)).astype(float)


def vap_084_poc_21d_distance_from_252d_poc(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance between 21-day and 252-day POC, normalised by 252d POC."""
    poc21 = _poc_window(close, volume, _TD_MON)
    poc252 = _poc_window(close, volume, _TD_YEAR)
    return _safe_div(poc21 - poc252, poc252.clip(lower=_EPS))


def vap_085_va_width_ratio_21d_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day VA width to 252-day VA width (short-term volume compression)."""
    va_lo_21, va_hi_21 = _value_area_bounds(close, volume, _TD_MON)
    va_lo_252, va_hi_252 = _value_area_bounds(close, volume, _TD_YEAR)
    w21 = va_hi_21 - va_lo_21
    w252 = (va_hi_252 - va_lo_252).replace(0, np.nan)
    return _safe_div(w21, w252)


def vap_086_overhead_frac_all3_avg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average of 21d, 63d, 252d overhead supply fractions (composite overhead pressure)."""
    o21 = _overhead_vol_fraction(close, volume, _TD_MON)
    o63 = _overhead_vol_fraction(close, volume, _TD_QTR)
    o252 = _overhead_vol_fraction(close, volume, _TD_YEAR)
    return (o21 + o63 + o252) / 3.0


def vap_087_vwap_21d_vs_63d_spread(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day VWAP minus 63-day VWAP, normalised by 63-day VWAP."""
    v21 = _vwap_window(close, volume, _TD_MON)
    v63 = _vwap_window(close, volume, _TD_QTR)
    return _safe_div(v21 - v63, v63.clip(lower=_EPS))


def vap_088_vwap_63d_vs_252d_spread(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day VWAP minus 252-day VWAP, normalised by 252-day VWAP."""
    v63 = _vwap_window(close, volume, _TD_QTR)
    v252 = _vwap_window(close, volume, _TD_YEAR)
    return _safe_div(v63 - v252, v252.clip(lower=_EPS))


def vap_089_price_below_all_va_lows_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: close is below VA-low at 21d, 63d, and 252d simultaneously."""
    va_lo_21, _ = _value_area_bounds(close, volume, _TD_MON)
    va_lo_63, _ = _value_area_bounds(close, volume, _TD_QTR)
    va_lo_252, _ = _value_area_bounds(close, volume, _TD_YEAR)
    return ((close < va_lo_21) & (close < va_lo_63) & (close < va_lo_252)).astype(float)


def vap_090_poc_cluster_spread_21_63_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max minus min of 21d/63d/252d POC prices, normalised by 252d POC."""
    poc21 = _poc_window(close, volume, _TD_MON)
    poc63 = _poc_window(close, volume, _TD_QTR)
    poc252 = _poc_window(close, volume, _TD_YEAR)
    combined = pd.concat([poc21, poc63, poc252], axis=1)
    spread = combined.max(axis=1) - combined.min(axis=1)
    return _safe_div(spread, poc252.clip(lower=_EPS))


# --- Group G (091-105): Volume-profile imbalance and cross-bin features ---

def vap_091_lower_half_vol_frac_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63-day volume in the lower half of the price range."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    w = _TD_QTR
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
            result[i] = 0.5
            continue
        mid = (lo + hi) / 2.0
        total = v_w.sum()
        if total == 0:
            continue
        result[i] = v_w[c_w <= mid].sum() / total
    return pd.Series(result, index=close.index)


def vap_092_lower_quartile_vol_frac_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63-day volume in the lowest quartile of the price range."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    w = _TD_QTR
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
            result[i] = 1.0
            continue
        q25 = lo + (hi - lo) * 0.25
        total = v_w.sum()
        if total == 0:
            continue
        result[i] = v_w[c_w <= q25].sum() / total
    return pd.Series(result, index=close.index)


def vap_093_upper_quartile_vol_frac_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63-day volume in the highest quartile of the price range."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    w = _TD_QTR
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
            result[i] = 0.0
            continue
        q75 = lo + (hi - lo) * 0.75
        total = v_w.sum()
        if total == 0:
            continue
        result[i] = v_w[c_w >= q75].sum() / total
    return pd.Series(result, index=close.index)


def vap_094_lower_half_vol_frac_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 252-day volume in the lower half of the price range."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    w = _TD_YEAR
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
            result[i] = 0.5
            continue
        mid = (lo + hi) / 2.0
        total = v_w.sum()
        if total == 0:
            continue
        result[i] = v_w[c_w <= mid].sum() / total
    return pd.Series(result, index=close.index)


def vap_095_vol_imbalance_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume imbalance: (lower_half_frac - upper_half_frac) for 63-day window."""
    lower = vap_091_lower_half_vol_frac_63d(close, volume)
    return 2.0 * lower - 1.0


def vap_096_vol_imbalance_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume imbalance: (lower_half_frac - upper_half_frac) for 252-day window."""
    lower = vap_094_lower_half_vol_frac_252d(close, volume)
    return 2.0 * lower - 1.0


def vap_097_vol_weighted_mean_price_pct_rank(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day VWAP vs 252-day rolling VWAP distribution."""
    vwap63 = _vwap_window(close, volume, _TD_QTR)
    return vwap63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vap_098_price_to_vol_weighted_mean_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of current close to 63-day VWAP."""
    return _safe_div(close, _vwap_window(close, volume, _TD_QTR).clip(lower=_EPS))


def vap_099_poc_vol_fraction_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of total 63-day volume in the POC bin (concentration at the mode)."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    bins = _VAP_BINS
    w = _TD_QTR
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
            result[i] = 1.0
            continue
        edges = np.linspace(lo, hi, bins + 1)
        hist_v = np.zeros(bins, dtype=float)
        for b in range(bins):
            mbk = (c_w >= edges[b]) & (c_w < edges[b + 1]) if b < bins - 1 else (c_w >= edges[b]) & (c_w <= edges[b + 1])
            hist_v[b] = v_w[mbk].sum()
        total = hist_v.sum()
        if total == 0:
            continue
        result[i] = hist_v.max() / total
    return pd.Series(result, index=close.index)


def vap_100_low_volume_node_below_flag_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: current price is within a Low-Volume Node (bottom 3 bins) in 63-day VAP."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    bins = _VAP_BINS
    w = _TD_QTR
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
        hist_v = np.zeros(bins, dtype=float)
        for b in range(bins):
            mbk = (c_w >= edges[b]) & (c_w < edges[b + 1]) if b < bins - 1 else (c_w >= edges[b]) & (c_w <= edges[b + 1])
            hist_v[b] = v_w[mbk].sum()
        lvn_idx = np.argsort(hist_v)[:3]
        in_lvn = False
        for b in lvn_idx:
            if edges[b] <= cur <= edges[b + 1]:
                in_lvn = True
                break
        result[i] = 1.0 if in_lvn else 0.0
    return pd.Series(result, index=close.index)


def vap_101_vap_modal_price_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day VAP modal price (POC) level, un-normalised."""
    return _poc_window(close, volume, _TD_MON)


def vap_102_vap_modal_price_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day VAP modal price (POC) level, un-normalised."""
    return _poc_window(close, volume, _TD_QTR)


def vap_103_vap_modal_price_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day VAP modal price (POC) level, un-normalised."""
    return _poc_window(close, volume, _TD_YEAR)


def vap_104_poc_as_pct_of_52w_high(close: pd.Series, high: pd.Series,
                                    volume: pd.Series) -> pd.Series:
    """63-day POC expressed as fraction of 252-day rolling high (POC in range context)."""
    poc63 = _poc_window(close, volume, _TD_QTR)
    hi252 = _rolling_max(high, _TD_YEAR)
    return _safe_div(poc63, hi252.clip(lower=_EPS))


def vap_105_poc_as_pct_of_52w_low(close: pd.Series, low: pd.Series,
                                   volume: pd.Series) -> pd.Series:
    """63-day POC expressed relative to 252-day rolling low."""
    poc63 = _poc_window(close, volume, _TD_QTR)
    lo252 = _rolling_min(low, _TD_YEAR)
    return _safe_div(poc63 - lo252, lo252.clip(lower=_EPS))


# --- Group H (106-120): VWAP band and momentum features ---

def vap_106_vwap_21d_slope_pct_rank(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 5-day slope of 21-day VWAP vs 252-day history of that slope."""
    slope = _vwap_window(close, volume, _TD_MON).diff(_TD_WEEK)
    return slope.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vap_107_vwap_63d_slope_pct_rank(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day slope of 63-day VWAP vs 252-day history."""
    slope = _vwap_window(close, volume, _TD_QTR).diff(_TD_MON)
    return slope.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vap_108_vwap_band_zscore_21d_pct_rank(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day VWAP-band z-score vs 252-day history."""
    vwap = _vwap_window(close, volume, _TD_MON)
    vstd = _vwap_std_window(close, volume, _TD_MON)
    z = _safe_div(close - vwap, vstd.clip(lower=_EPS))
    return z.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vap_109_vwap_band_zscore_63d_pct_rank(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day VWAP-band z-score vs 252-day history."""
    vwap = _vwap_window(close, volume, _TD_QTR)
    vstd = _vwap_std_window(close, volume, _TD_QTR)
    z = _safe_div(close - vwap, vstd.clip(lower=_EPS))
    return z.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vap_110_vwap_21d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day VWAP distance (normalised) vs its own 252-day distribution."""
    dist = _safe_div(close - _vwap_window(close, volume, _TD_MON),
                     _vwap_window(close, volume, _TD_MON).clip(lower=_EPS))
    m = _rolling_mean(dist, _TD_YEAR)
    s = _rolling_std(dist, _TD_YEAR)
    return _safe_div(dist - m, s)


def vap_111_vwap_below_all3_consec_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days close has been below all three VWAPs (21d, 63d, 252d)."""
    cond = (
        (close < _vwap_window(close, volume, _TD_MON)) &
        (close < _vwap_window(close, volume, _TD_QTR)) &
        (close < _vwap_window(close, volume, _TD_YEAR))
    )
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def vap_112_vwap_std_expanding_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding-history z-score of the 21-day VWAP band z-score."""
    vwap = _vwap_window(close, volume, _TD_MON)
    vstd = _vwap_std_window(close, volume, _TD_MON)
    z = _safe_div(close - vwap, vstd.clip(lower=_EPS))
    m_exp = z.expanding(min_periods=_TD_QTR).mean()
    s_exp = z.expanding(min_periods=_TD_QTR).std()
    return _safe_div(z - m_exp, s_exp)


def vap_113_vwap_dist_21d_min_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day minimum of the 21-day VWAP distance."""
    dist = _safe_div(close - _vwap_window(close, volume, _TD_MON),
                     _vwap_window(close, volume, _TD_MON).clip(lower=_EPS))
    return _rolling_min(dist, _TD_QTR)


def vap_114_vwap_dist_63d_min_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252-day minimum of the 63-day VWAP distance."""
    dist = _safe_div(close - _vwap_window(close, volume, _TD_QTR),
                     _vwap_window(close, volume, _TD_QTR).clip(lower=_EPS))
    return _rolling_min(dist, _TD_YEAR)


def vap_115_overhead_frac_consec_above70_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days 21-day overhead supply fraction > 0.70."""
    cond = _overhead_vol_fraction(close, volume, _TD_MON) > 0.70
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def vap_116_overhead_frac_consec_above70_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days 63-day overhead supply fraction > 0.70."""
    cond = _overhead_vol_fraction(close, volume, _TD_QTR) > 0.70
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def vap_117_overhead_frac_21d_new_high_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: today's 21-day overhead fraction is the highest in 21 days."""
    s = _overhead_vol_fraction(close, volume, _TD_MON)
    prev_max = s.shift(1).rolling(_TD_MON, min_periods=1).max()
    return (s > prev_max).astype(float)


def vap_118_poc_pct_rank_expanding(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 63-day POC distance."""
    dist = _safe_div(close - _poc_window(close, volume, _TD_QTR),
                     _poc_window(close, volume, _TD_QTR).clip(lower=_EPS))
    return dist.expanding(min_periods=_TD_QTR).rank(pct=True)


def vap_119_vwap_21d_new_low_63d_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: today's 21-day VWAP distance is the most negative in 63 days."""
    dist = _safe_div(close - _vwap_window(close, volume, _TD_MON),
                     _vwap_window(close, volume, _TD_MON).clip(lower=_EPS))
    prev_min = dist.shift(1).rolling(_TD_QTR, min_periods=1).min()
    return (dist < prev_min).astype(float)


def vap_120_overhead_frac_trend_crossover_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: 21d overhead fraction > 63d overhead fraction (short-term worse than medium)."""
    o21 = _overhead_vol_fraction(close, volume, _TD_MON)
    o63 = _overhead_vol_fraction(close, volume, _TD_QTR)
    return (o21 > o63).astype(float)


# --- Group I (121-135): Volume-weighted price stats and VAP normalised features ---

def vap_121_vol_weighted_close_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day VWAP level vs 252-day VWAP level distribution."""
    vwap21 = _vwap_window(close, volume, _TD_MON)
    return vwap21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vap_122_vap_entropy_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Shannon entropy of the 252-day VAP histogram."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    bins = _VAP_BINS
    w = _TD_YEAR
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
            result[i] = 0.0
            continue
        edges = np.linspace(lo, hi, bins + 1)
        hist_v = np.zeros(bins, dtype=float)
        for b in range(bins):
            mbk = (c_w >= edges[b]) & (c_w < edges[b + 1]) if b < bins - 1 else (c_w >= edges[b]) & (c_w <= edges[b + 1])
            hist_v[b] = v_w[mbk].sum()
        total = hist_v.sum()
        if total == 0:
            continue
        p = hist_v / total
        with np.errstate(divide='ignore', invalid='ignore'):
            ent = -np.where(p > 0, p * np.log(p), 0.0).sum()
        result[i] = ent
    return pd.Series(result, index=close.index)


def vap_123_vap_entropy_63d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day VAP entropy vs 252-day history."""
    # Inline entropy calculation to keep file self-contained
    n = len(close)
    ent_vals = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    bins = _VAP_BINS
    w = _TD_QTR
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
            ent_vals[i] = 0.0
            continue
        edges = np.linspace(lo, hi, bins + 1)
        hist_v = np.zeros(bins, dtype=float)
        for b in range(bins):
            mbk = (c_w >= edges[b]) & (c_w < edges[b + 1]) if b < bins - 1 else (c_w >= edges[b]) & (c_w <= edges[b + 1])
            hist_v[b] = v_w[mbk].sum()
        total = hist_v.sum()
        if total == 0:
            continue
        p = hist_v / total
        with np.errstate(divide='ignore', invalid='ignore'):
            ent_vals[i] = -np.where(p > 0, p * np.log(p), 0.0).sum()
    ent = pd.Series(ent_vals, index=close.index)
    return ent.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vap_124_vap_skew_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted price skewness over 252-day window."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    w = _TD_YEAR
    for i in range(n):
        start = max(0, i - w + 1)
        c_w = c_arr[start:i + 1]
        v_w = v_arr[start:i + 1]
        mask = ~(np.isnan(c_w) | np.isnan(v_w))
        c_w = c_w[mask]
        v_w = v_w[mask]
        if len(c_w) < max(3, w // 2):
            continue
        total = v_w.sum()
        if total == 0:
            continue
        mean = (c_w * v_w).sum() / total
        var = ((c_w - mean) ** 2 * v_w).sum() / total
        if var <= 0:
            result[i] = 0.0
            continue
        skew = ((c_w - mean) ** 3 * v_w).sum() / total / (var ** 1.5)
        result[i] = skew
    return pd.Series(result, index=close.index)


def vap_125_vap_skew_63d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day VAP skewness vs 252-day history."""
    n = len(close)
    result_arr = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    w = _TD_QTR
    skew_vals = np.full(n, np.nan)
    for i in range(n):
        start = max(0, i - w + 1)
        c_w = c_arr[start:i + 1]
        v_w = v_arr[start:i + 1]
        mask = ~(np.isnan(c_w) | np.isnan(v_w))
        c_w = c_w[mask]
        v_w = v_w[mask]
        if len(c_w) < max(3, w // 2):
            continue
        total = v_w.sum()
        if total == 0:
            continue
        mean = (c_w * v_w).sum() / total
        var = ((c_w - mean) ** 2 * v_w).sum() / total
        if var <= 0:
            skew_vals[i] = 0.0
            continue
        skew_vals[i] = ((c_w - mean) ** 3 * v_w).sum() / total / (var ** 1.5)
    skew_s = pd.Series(skew_vals, index=close.index)
    return skew_s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vap_126_overhead_frac_21d_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day overhead fraction vs its 63-day rolling distribution."""
    s = _overhead_vol_fraction(close, volume, _TD_MON)
    m = _rolling_mean(s, _TD_QTR)
    sd = _rolling_std(s, _TD_QTR)
    return _safe_div(s - m, sd)


def vap_127_below_va_low_21d_in_63d_count(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in trailing 63 days where close < 21-day VA-low."""
    va_lo, _ = _value_area_bounds(close, volume, _TD_MON)
    flag = (close < va_lo).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def vap_128_below_va_low_63d_in_252d_count(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in trailing 252 days where close < 63-day VA-low."""
    va_lo, _ = _value_area_bounds(close, volume, _TD_QTR)
    flag = (close < va_lo).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def vap_129_poc_new_low_63d_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: today's 21-day POC is at its 63-day low (POC eroding)."""
    poc = _poc_window(close, volume, _TD_MON)
    prev_min = poc.shift(1).rolling(_TD_QTR, min_periods=1).min()
    return (poc < prev_min).astype(float)


def vap_130_vwap_dist_21d_in_63d_count_below_neg2pct(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in 63 days where 21-day VWAP distance < -2% (persistent pressure below VWAP)."""
    dist = _safe_div(close - _vwap_window(close, volume, _TD_MON),
                     _vwap_window(close, volume, _TD_MON).clip(lower=_EPS))
    flag = (dist < -0.02).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def vap_131_poc_distance_63d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 63-day POC distance vs its 252-day distribution."""
    dist = _safe_div(close - _poc_window(close, volume, _TD_QTR),
                     _poc_window(close, volume, _TD_QTR).clip(lower=_EPS))
    m = _rolling_mean(dist, _TD_YEAR)
    s = _rolling_std(dist, _TD_YEAR)
    return _safe_div(dist - m, s)


def vap_132_va_low_63d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day VA-low price level vs 252-day history."""
    va_lo, _ = _value_area_bounds(close, volume, _TD_QTR)
    return va_lo.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vap_133_vwap_std_21d_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day VWAP std to 63-day VWAP std (short-term price spread vs medium)."""
    std21 = _vwap_std_window(close, volume, _TD_MON)
    std63 = _vwap_std_window(close, volume, _TD_QTR)
    return _safe_div(std21, std63.clip(lower=_EPS))


def vap_134_vol_wtd_median_dist_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance of close from volume-weighted approximate median price over 63 days."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    w = _TD_QTR
    for i in range(n):
        start = max(0, i - w + 1)
        c_w = c_arr[start:i + 1]
        v_w = v_arr[start:i + 1]
        mask = ~(np.isnan(c_w) | np.isnan(v_w))
        c_w = c_w[mask]
        v_w = v_w[mask]
        if len(c_w) < max(2, w // 2):
            continue
        total = v_w.sum()
        if total == 0:
            continue
        idx_sort = np.argsort(c_w)
        c_sorted = c_w[idx_sort]
        v_sorted = v_w[idx_sort]
        cumvol = np.cumsum(v_sorted)
        median_idx = np.searchsorted(cumvol, total * 0.5)
        median_idx = min(median_idx, len(c_sorted) - 1)
        vw_median = c_sorted[median_idx]
        cur = c_arr[i]
        if not np.isnan(cur) and vw_median != 0:
            result[i] = (cur - vw_median) / vw_median
    return pd.Series(result, index=close.index)


def vap_135_poc_distance_21d_new_low_252d_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: today's 21-day POC distance is the most negative in 252 days."""
    dist = _safe_div(close - _poc_window(close, volume, _TD_MON),
                     _poc_window(close, volume, _TD_MON).clip(lower=_EPS))
    prev_min = dist.shift(1).rolling(_TD_YEAR, min_periods=1).min()
    return (dist < prev_min).astype(float)


# --- Group J (136-150): Composite and cross-feature distress indicators ---

def vap_136_vap_distress_composite_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: overhead_frac_21d + |vwap_dist_21d| + |poc_dist_21d|."""
    oh = _overhead_vol_fraction(close, volume, _TD_MON)
    vd = _safe_div(close - _vwap_window(close, volume, _TD_MON),
                   _vwap_window(close, volume, _TD_MON).clip(lower=_EPS)).abs()
    pd_ = _safe_div(close - _poc_window(close, volume, _TD_MON),
                    _poc_window(close, volume, _TD_MON).clip(lower=_EPS)).abs()
    return oh + vd + pd_


def vap_137_vap_distress_composite_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: overhead_frac_63d + |vwap_dist_63d| + |poc_dist_63d|."""
    oh = _overhead_vol_fraction(close, volume, _TD_QTR)
    vd = _safe_div(close - _vwap_window(close, volume, _TD_QTR),
                   _vwap_window(close, volume, _TD_QTR).clip(lower=_EPS)).abs()
    pd_ = _safe_div(close - _poc_window(close, volume, _TD_QTR),
                    _poc_window(close, volume, _TD_QTR).clip(lower=_EPS)).abs()
    return oh + vd + pd_


def vap_138_vap_distress_composite_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: overhead_frac_252d + |vwap_dist_252d| + |poc_dist_252d|."""
    oh = _overhead_vol_fraction(close, volume, _TD_YEAR)
    vd = _safe_div(close - _vwap_window(close, volume, _TD_YEAR),
                   _vwap_window(close, volume, _TD_YEAR).clip(lower=_EPS)).abs()
    pd_ = _safe_div(close - _poc_window(close, volume, _TD_YEAR),
                    _poc_window(close, volume, _TD_YEAR).clip(lower=_EPS)).abs()
    return oh + vd + pd_


def vap_139_all_overhead_above_80pct_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: all three overhead fractions (21d, 63d, 252d) exceed 0.80."""
    o21 = _overhead_vol_fraction(close, volume, _TD_MON)
    o63 = _overhead_vol_fraction(close, volume, _TD_QTR)
    o252 = _overhead_vol_fraction(close, volume, _TD_YEAR)
    return ((o21 > 0.80) & (o63 > 0.80) & (o252 > 0.80)).astype(float)


def vap_140_poc_declining_streak_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days the 21-day POC has been declining."""
    poc = _poc_window(close, volume, _TD_MON)
    cond = poc.diff(1) < 0
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def vap_141_vwap_63d_declining_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days the 63-day VWAP has been declining."""
    vwap = _vwap_window(close, volume, _TD_QTR)
    cond = vwap.diff(1) < 0
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def vap_142_overhead_frac_63d_max_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day maximum of the 63-day overhead supply fraction."""
    s = _overhead_vol_fraction(close, volume, _TD_QTR)
    return _rolling_max(s, _TD_YEAR)


def vap_143_overhead_frac_21d_min_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day minimum of the 21-day overhead supply fraction."""
    s = _overhead_vol_fraction(close, volume, _TD_MON)
    return _rolling_min(s, _TD_QTR)


def vap_144_price_to_vwap_252d_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of current close to 252-day VWAP (raw price dislocation)."""
    return _safe_div(close, _vwap_window(close, volume, _TD_YEAR).clip(lower=_EPS))


def vap_145_poc_dist_252d_expanding_min(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding minimum of the 252-day POC distance (how deep has it ever gotten?)."""
    dist = _safe_div(close - _poc_window(close, volume, _TD_YEAR),
                     _poc_window(close, volume, _TD_YEAR).clip(lower=_EPS))
    return dist.expanding(min_periods=_TD_QTR).min()


def vap_146_vwap_band_below_2std_flag_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: close is more than 2 VWAP-std below the 21-day VWAP."""
    vwap = _vwap_window(close, volume, _TD_MON)
    vstd = _vwap_std_window(close, volume, _TD_MON)
    return (close < vwap - 2.0 * vstd).astype(float)


def vap_147_vwap_band_below_2std_flag_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: close is more than 2 VWAP-std below the 63-day VWAP."""
    vwap = _vwap_window(close, volume, _TD_QTR)
    vstd = _vwap_std_window(close, volume, _TD_QTR)
    return (close < vwap - 2.0 * vstd).astype(float)


def vap_148_vwap_band_below_3std_flag_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: close is more than 3 VWAP-std below the 21-day VWAP (extreme)."""
    vwap = _vwap_window(close, volume, _TD_MON)
    vstd = _vwap_std_window(close, volume, _TD_MON)
    return (close < vwap - 3.0 * vstd).astype(float)


def vap_149_poc_distance_21d_in_63d_count_below_neg5pct(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in 63-day window where 21-day POC distance < -5%."""
    dist = _safe_div(close - _poc_window(close, volume, _TD_MON),
                     _poc_window(close, volume, _TD_MON).clip(lower=_EPS))
    flag = (dist < -0.05).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def vap_150_vap_capitulation_composite(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Capitulation composite: overhead_frac_252d + below_va_low_252d + vwap_band_zscore_252d_neg.
    Higher = more extreme VAP-based distress."""
    oh = _overhead_vol_fraction(close, volume, _TD_YEAR)
    va_lo, _ = _value_area_bounds(close, volume, _TD_YEAR)
    below_va = (close < va_lo).astype(float)
    vwap = _vwap_window(close, volume, _TD_YEAR)
    vstd = _vwap_std_window(close, volume, _TD_YEAR)
    z = _safe_div(close - vwap, vstd.clip(lower=_EPS))
    z_neg = (-z).clip(lower=0.0) / 3.0
    return oh + below_va + z_neg


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_AT_PRICE_REGISTRY_076_150 = {
    "vap_076_poc_dist_21d_vs_252d_ratio": {"inputs": ["close", "volume"], "func": vap_076_poc_dist_21d_vs_252d_ratio},
    "vap_077_vwap_dist_spread_21d_252d": {"inputs": ["close", "volume"], "func": vap_077_vwap_dist_spread_21d_252d},
    "vap_078_overhead_frac_spread_21d_252d": {"inputs": ["close", "volume"], "func": vap_078_overhead_frac_spread_21d_252d},
    "vap_079_poc_21d_below_poc_252d_flag": {"inputs": ["close", "volume"], "func": vap_079_poc_21d_below_poc_252d_flag},
    "vap_080_poc_63d_below_poc_252d_flag": {"inputs": ["close", "volume"], "func": vap_080_poc_63d_below_poc_252d_flag},
    "vap_081_va_low_63d_below_va_low_252d": {"inputs": ["close", "volume"], "func": vap_081_va_low_63d_below_va_low_252d},
    "vap_082_all_poc_below_price_flag": {"inputs": ["close", "volume"], "func": vap_082_all_poc_below_price_flag},
    "vap_083_all_vwap_overhead_above_70pct": {"inputs": ["close", "volume"], "func": vap_083_all_vwap_overhead_above_70pct},
    "vap_084_poc_21d_distance_from_252d_poc": {"inputs": ["close", "volume"], "func": vap_084_poc_21d_distance_from_252d_poc},
    "vap_085_va_width_ratio_21d_252d": {"inputs": ["close", "volume"], "func": vap_085_va_width_ratio_21d_252d},
    "vap_086_overhead_frac_all3_avg": {"inputs": ["close", "volume"], "func": vap_086_overhead_frac_all3_avg},
    "vap_087_vwap_21d_vs_63d_spread": {"inputs": ["close", "volume"], "func": vap_087_vwap_21d_vs_63d_spread},
    "vap_088_vwap_63d_vs_252d_spread": {"inputs": ["close", "volume"], "func": vap_088_vwap_63d_vs_252d_spread},
    "vap_089_price_below_all_va_lows_flag": {"inputs": ["close", "volume"], "func": vap_089_price_below_all_va_lows_flag},
    "vap_090_poc_cluster_spread_21_63_252": {"inputs": ["close", "volume"], "func": vap_090_poc_cluster_spread_21_63_252},
    "vap_091_lower_half_vol_frac_63d": {"inputs": ["close", "volume"], "func": vap_091_lower_half_vol_frac_63d},
    "vap_092_lower_quartile_vol_frac_63d": {"inputs": ["close", "volume"], "func": vap_092_lower_quartile_vol_frac_63d},
    "vap_093_upper_quartile_vol_frac_63d": {"inputs": ["close", "volume"], "func": vap_093_upper_quartile_vol_frac_63d},
    "vap_094_lower_half_vol_frac_252d": {"inputs": ["close", "volume"], "func": vap_094_lower_half_vol_frac_252d},
    "vap_095_vol_imbalance_63d": {"inputs": ["close", "volume"], "func": vap_095_vol_imbalance_63d},
    "vap_096_vol_imbalance_252d": {"inputs": ["close", "volume"], "func": vap_096_vol_imbalance_252d},
    "vap_097_vol_weighted_mean_price_pct_rank": {"inputs": ["close", "volume"], "func": vap_097_vol_weighted_mean_price_pct_rank},
    "vap_098_price_to_vol_weighted_mean_ratio": {"inputs": ["close", "volume"], "func": vap_098_price_to_vol_weighted_mean_ratio},
    "vap_099_poc_vol_fraction_63d": {"inputs": ["close", "volume"], "func": vap_099_poc_vol_fraction_63d},
    "vap_100_low_volume_node_below_flag_63d": {"inputs": ["close", "volume"], "func": vap_100_low_volume_node_below_flag_63d},
    "vap_101_vap_modal_price_21d": {"inputs": ["close", "volume"], "func": vap_101_vap_modal_price_21d},
    "vap_102_vap_modal_price_63d": {"inputs": ["close", "volume"], "func": vap_102_vap_modal_price_63d},
    "vap_103_vap_modal_price_252d": {"inputs": ["close", "volume"], "func": vap_103_vap_modal_price_252d},
    "vap_104_poc_as_pct_of_52w_high": {"inputs": ["close", "high", "volume"], "func": vap_104_poc_as_pct_of_52w_high},
    "vap_105_poc_as_pct_of_52w_low": {"inputs": ["close", "low", "volume"], "func": vap_105_poc_as_pct_of_52w_low},
    "vap_106_vwap_21d_slope_pct_rank": {"inputs": ["close", "volume"], "func": vap_106_vwap_21d_slope_pct_rank},
    "vap_107_vwap_63d_slope_pct_rank": {"inputs": ["close", "volume"], "func": vap_107_vwap_63d_slope_pct_rank},
    "vap_108_vwap_band_zscore_21d_pct_rank": {"inputs": ["close", "volume"], "func": vap_108_vwap_band_zscore_21d_pct_rank},
    "vap_109_vwap_band_zscore_63d_pct_rank": {"inputs": ["close", "volume"], "func": vap_109_vwap_band_zscore_63d_pct_rank},
    "vap_110_vwap_21d_zscore_252d": {"inputs": ["close", "volume"], "func": vap_110_vwap_21d_zscore_252d},
    "vap_111_vwap_below_all3_consec_days": {"inputs": ["close", "volume"], "func": vap_111_vwap_below_all3_consec_days},
    "vap_112_vwap_std_expanding_zscore_21d": {"inputs": ["close", "volume"], "func": vap_112_vwap_std_expanding_zscore_21d},
    "vap_113_vwap_dist_21d_min_63d": {"inputs": ["close", "volume"], "func": vap_113_vwap_dist_21d_min_63d},
    "vap_114_vwap_dist_63d_min_252d": {"inputs": ["close", "volume"], "func": vap_114_vwap_dist_63d_min_252d},
    "vap_115_overhead_frac_consec_above70_21d": {"inputs": ["close", "volume"], "func": vap_115_overhead_frac_consec_above70_21d},
    "vap_116_overhead_frac_consec_above70_63d": {"inputs": ["close", "volume"], "func": vap_116_overhead_frac_consec_above70_63d},
    "vap_117_overhead_frac_21d_new_high_21d": {"inputs": ["close", "volume"], "func": vap_117_overhead_frac_21d_new_high_21d},
    "vap_118_poc_pct_rank_expanding": {"inputs": ["close", "volume"], "func": vap_118_poc_pct_rank_expanding},
    "vap_119_vwap_21d_new_low_63d_flag": {"inputs": ["close", "volume"], "func": vap_119_vwap_21d_new_low_63d_flag},
    "vap_120_overhead_frac_trend_crossover_flag": {"inputs": ["close", "volume"], "func": vap_120_overhead_frac_trend_crossover_flag},
    "vap_121_vol_weighted_close_pct_rank_252d": {"inputs": ["close", "volume"], "func": vap_121_vol_weighted_close_pct_rank_252d},
    "vap_122_vap_entropy_252d": {"inputs": ["close", "volume"], "func": vap_122_vap_entropy_252d},
    "vap_123_vap_entropy_63d_pct_rank_252d": {"inputs": ["close", "volume"], "func": vap_123_vap_entropy_63d_pct_rank_252d},
    "vap_124_vap_skew_252d": {"inputs": ["close", "volume"], "func": vap_124_vap_skew_252d},
    "vap_125_vap_skew_63d_pct_rank_252d": {"inputs": ["close", "volume"], "func": vap_125_vap_skew_63d_pct_rank_252d},
    "vap_126_overhead_frac_21d_zscore_63d": {"inputs": ["close", "volume"], "func": vap_126_overhead_frac_21d_zscore_63d},
    "vap_127_below_va_low_21d_in_63d_count": {"inputs": ["close", "volume"], "func": vap_127_below_va_low_21d_in_63d_count},
    "vap_128_below_va_low_63d_in_252d_count": {"inputs": ["close", "volume"], "func": vap_128_below_va_low_63d_in_252d_count},
    "vap_129_poc_new_low_63d_flag": {"inputs": ["close", "volume"], "func": vap_129_poc_new_low_63d_flag},
    "vap_130_vwap_dist_21d_in_63d_count_below_neg2pct": {"inputs": ["close", "volume"], "func": vap_130_vwap_dist_21d_in_63d_count_below_neg2pct},
    "vap_131_poc_distance_63d_zscore_252d": {"inputs": ["close", "volume"], "func": vap_131_poc_distance_63d_zscore_252d},
    "vap_132_va_low_63d_pct_rank_252d": {"inputs": ["close", "volume"], "func": vap_132_va_low_63d_pct_rank_252d},
    "vap_133_vwap_std_21d_ratio_63d": {"inputs": ["close", "volume"], "func": vap_133_vwap_std_21d_ratio_63d},
    "vap_134_vol_wtd_median_dist_63d": {"inputs": ["close", "volume"], "func": vap_134_vol_wtd_median_dist_63d},
    "vap_135_poc_distance_21d_new_low_252d_flag": {"inputs": ["close", "volume"], "func": vap_135_poc_distance_21d_new_low_252d_flag},
    "vap_136_vap_distress_composite_21d": {"inputs": ["close", "volume"], "func": vap_136_vap_distress_composite_21d},
    "vap_137_vap_distress_composite_63d": {"inputs": ["close", "volume"], "func": vap_137_vap_distress_composite_63d},
    "vap_138_vap_distress_composite_252d": {"inputs": ["close", "volume"], "func": vap_138_vap_distress_composite_252d},
    "vap_139_all_overhead_above_80pct_flag": {"inputs": ["close", "volume"], "func": vap_139_all_overhead_above_80pct_flag},
    "vap_140_poc_declining_streak_21d": {"inputs": ["close", "volume"], "func": vap_140_poc_declining_streak_21d},
    "vap_141_vwap_63d_declining_streak": {"inputs": ["close", "volume"], "func": vap_141_vwap_63d_declining_streak},
    "vap_142_overhead_frac_63d_max_252d": {"inputs": ["close", "volume"], "func": vap_142_overhead_frac_63d_max_252d},
    "vap_143_overhead_frac_21d_min_63d": {"inputs": ["close", "volume"], "func": vap_143_overhead_frac_21d_min_63d},
    "vap_144_price_to_vwap_252d_ratio": {"inputs": ["close", "volume"], "func": vap_144_price_to_vwap_252d_ratio},
    "vap_145_poc_dist_252d_expanding_min": {"inputs": ["close", "volume"], "func": vap_145_poc_dist_252d_expanding_min},
    "vap_146_vwap_band_below_2std_flag_21d": {"inputs": ["close", "volume"], "func": vap_146_vwap_band_below_2std_flag_21d},
    "vap_147_vwap_band_below_2std_flag_63d": {"inputs": ["close", "volume"], "func": vap_147_vwap_band_below_2std_flag_63d},
    "vap_148_vwap_band_below_3std_flag_21d": {"inputs": ["close", "volume"], "func": vap_148_vwap_band_below_3std_flag_21d},
    "vap_149_poc_distance_21d_in_63d_count_below_neg5pct": {"inputs": ["close", "volume"], "func": vap_149_poc_distance_21d_in_63d_count_below_neg5pct},
    "vap_150_vap_capitulation_composite": {"inputs": ["close", "volume"], "func": vap_150_vap_capitulation_composite},
}
