"""
112_volume_at_price — Base Features 001-075
Domain: Volume-at-price structure — VAP histogram, point-of-control distance,
        value-area positioning, overhead supply fraction, VWAP-band distances,
        high-volume-node proximity
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
_VAP_BINS = 20   # default price bins for VAP histogram

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
    """
    Rolling point-of-control (POC): price level with highest volume over trailing w bars.
    Returns the mid-price of the highest-volume bin at each bar.
    NaN-safe: drops NaN rows before histogram.
    """
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)

    for i in range(n):
        start = max(0, i - w + 1)
        c_w = c_arr[start:i + 1]
        v_w = v_arr[start:i + 1]
        # drop NaNs
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
            if b < bins - 1:
                mask_b = (c_w >= edges[b]) & (c_w < edges[b + 1])
            else:
                mask_b = (c_w >= edges[b]) & (c_w <= edges[b + 1])
            hist_v[b] = v_w[mask_b].sum()
        poc_bin = int(np.argmax(hist_v))
        result[i] = (edges[poc_bin] + edges[poc_bin + 1]) / 2.0

    return pd.Series(result, index=close.index)


def _value_area_bounds(close: pd.Series, volume: pd.Series, w: int,
                       va_frac: float = 0.70, bins: int = _VAP_BINS):
    """
    Rolling value-area high/low: price band capturing va_frac (~70%) of volume.
    Returns (va_low Series, va_high Series).
    """
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
            if b < bins - 1:
                mask_b = (c_w >= edges[b]) & (c_w < edges[b + 1])
            else:
                mask_b = (c_w >= edges[b]) & (c_w <= edges[b + 1])
            hist_v[b] = v_w[mask_b].sum()
        total_vol = hist_v.sum()
        if total_vol == 0:
            continue
        target = total_vol * va_frac
        poc_bin = int(np.argmax(hist_v))
        included = [poc_bin]
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


def _overhead_vol_fraction(close: pd.Series, volume: pd.Series, w: int,
                           bins: int = _VAP_BINS) -> pd.Series:
    """
    Fraction of trailing w-bar volume transacted ABOVE the current close price.
    Represents trapped buyers / overhead supply.
    """
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
        above = v_w[c_w > cur].sum()
        result[i] = above / total

    return pd.Series(result, index=close.index)


def _hvn_proximity(close: pd.Series, volume: pd.Series, w: int,
                   bins: int = _VAP_BINS, top_n: int = 3) -> pd.Series:
    """
    Distance from current price to nearest high-volume node (top_n bins by volume).
    Returns absolute distance normalised by price range of the window.
    """
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
            if b < bins - 1:
                mask_b = (c_w >= edges[b]) & (c_w < edges[b + 1])
            else:
                mask_b = (c_w >= edges[b]) & (c_w <= edges[b + 1])
            hist_v[b] = v_w[mask_b].sum()
        top_idx = np.argsort(hist_v)[-top_n:]
        hvn_prices = mids[top_idx]
        dists = np.abs(hvn_prices - cur)
        result[i] = dists.min() / (hi - lo)

    return pd.Series(result, index=close.index)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): POC distance at multiple windows ---

def vap_001_poc_dist_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance of current price from 21-day POC, normalised by POC price."""
    poc = _poc_window(close, volume, _TD_MON)
    return _safe_div(close - poc, poc.clip(lower=_EPS))


def vap_002_poc_dist_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance of current price from 63-day POC, normalised by POC price."""
    poc = _poc_window(close, volume, _TD_QTR)
    return _safe_div(close - poc, poc.clip(lower=_EPS))


def vap_003_poc_dist_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance of current price from 126-day POC, normalised by POC price."""
    poc = _poc_window(close, volume, _TD_HALF)
    return _safe_div(close - poc, poc.clip(lower=_EPS))


def vap_004_poc_dist_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance of current price from 252-day POC, normalised by POC price."""
    poc = _poc_window(close, volume, _TD_YEAR)
    return _safe_div(close - poc, poc.clip(lower=_EPS))


def vap_005_poc_dist_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance of current price from 5-day POC, normalised by POC price."""
    poc = _poc_window(close, volume, _TD_WEEK)
    return _safe_div(close - poc, poc.clip(lower=_EPS))


def vap_006_poc_below_flag_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: current price is below the 21-day POC (below high-volume support)."""
    poc = _poc_window(close, volume, _TD_MON)
    return (close < poc).astype(float)


def vap_007_poc_below_flag_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: current price is below the 63-day POC."""
    poc = _poc_window(close, volume, _TD_QTR)
    return (close < poc).astype(float)


def vap_008_poc_below_flag_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: current price is below the 252-day POC."""
    poc = _poc_window(close, volume, _TD_YEAR)
    return (close < poc).astype(float)


def vap_009_poc_dist_63d_abs(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Absolute distance of current price from 63-day POC (unsigned)."""
    poc = _poc_window(close, volume, _TD_QTR)
    return (close - poc).abs()


def vap_010_poc_dist_252d_abs(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Absolute distance of current price from 252-day POC (unsigned)."""
    poc = _poc_window(close, volume, _TD_YEAR)
    return (close - poc).abs()


def vap_011_poc_dist_21d_signed_norm_atr(close: pd.Series, high: pd.Series,
                                          low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day POC distance normalised by 21-day ATR (ATR-units)."""
    poc = _poc_window(close, volume, _TD_MON)
    atr = _rolling_mean(high - low, _TD_MON).clip(lower=_EPS)
    return _safe_div(close - poc, atr)


def vap_012_poc_dist_63d_signed_norm_atr(close: pd.Series, high: pd.Series,
                                          low: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day POC distance normalised by 63-day ATR (ATR-units)."""
    poc = _poc_window(close, volume, _TD_QTR)
    atr = _rolling_mean(high - low, _TD_QTR).clip(lower=_EPS)
    return _safe_div(close - poc, atr)


def vap_013_poc_trend_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day difference of the 21-day POC level (is POC drifting lower?)."""
    poc = _poc_window(close, volume, _TD_MON)
    return poc.diff(_TD_WEEK)


def vap_014_poc_trend_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day difference of the 63-day POC level."""
    poc = _poc_window(close, volume, _TD_QTR)
    return poc.diff(_TD_MON)


def vap_015_poc_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of the 63-day POC distance (252-day lookback)."""
    dist = _safe_div(close - _poc_window(close, volume, _TD_QTR),
                     _poc_window(close, volume, _TD_QTR).clip(lower=_EPS))
    return dist.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group B (016-030): Value-area position features ---

def vap_016_below_value_area_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: current price is below the 21-day value-area low."""
    va_lo, _ = _value_area_bounds(close, volume, _TD_MON)
    return (close < va_lo).astype(float)


def vap_017_below_value_area_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: current price is below the 63-day value-area low."""
    va_lo, _ = _value_area_bounds(close, volume, _TD_QTR)
    return (close < va_lo).astype(float)


def vap_018_below_value_area_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: current price is below the 252-day value-area low."""
    va_lo, _ = _value_area_bounds(close, volume, _TD_YEAR)
    return (close < va_lo).astype(float)


def vap_019_va_low_dist_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance below 21-day value-area low, normalised by VA-low price (0 when above)."""
    va_lo, _ = _value_area_bounds(close, volume, _TD_MON)
    return _safe_div((va_lo - close).clip(lower=0.0), va_lo.clip(lower=_EPS))


def vap_020_va_low_dist_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance below 63-day value-area low, normalised by VA-low price."""
    va_lo, _ = _value_area_bounds(close, volume, _TD_QTR)
    return _safe_div((va_lo - close).clip(lower=0.0), va_lo.clip(lower=_EPS))


def vap_021_va_low_dist_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance below 252-day value-area low, normalised by VA-low price."""
    va_lo, _ = _value_area_bounds(close, volume, _TD_YEAR)
    return _safe_div((va_lo - close).clip(lower=0.0), va_lo.clip(lower=_EPS))


def vap_022_va_width_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Width of 21-day value area (VA-high minus VA-low) normalised by close."""
    va_lo, va_hi = _value_area_bounds(close, volume, _TD_MON)
    return _safe_div(va_hi - va_lo, close.clip(lower=_EPS))


def vap_023_va_width_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Width of 63-day value area normalised by close."""
    va_lo, va_hi = _value_area_bounds(close, volume, _TD_QTR)
    return _safe_div(va_hi - va_lo, close.clip(lower=_EPS))


def vap_024_va_width_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Width of 252-day value area normalised by close."""
    va_lo, va_hi = _value_area_bounds(close, volume, _TD_YEAR)
    return _safe_div(va_hi - va_lo, close.clip(lower=_EPS))


def vap_025_price_in_va_flag_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: current price is inside the 63-day value area."""
    va_lo, va_hi = _value_area_bounds(close, volume, _TD_QTR)
    return ((close >= va_lo) & (close <= va_hi)).astype(float)


def vap_026_price_position_in_va_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Position of current price within the 63-day value area (0=at VA-low, 1=at VA-high)."""
    va_lo, va_hi = _value_area_bounds(close, volume, _TD_QTR)
    width = (va_hi - va_lo).replace(0, np.nan)
    pos = (close - va_lo) / width
    return pos.clip(lower=0.0, upper=1.0)


def vap_027_price_position_in_va_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Position of current price within the 252-day value area (0=VA-low, 1=VA-high)."""
    va_lo, va_hi = _value_area_bounds(close, volume, _TD_YEAR)
    width = (va_hi - va_lo).replace(0, np.nan)
    pos = (close - va_lo) / width
    return pos.clip(lower=0.0, upper=1.0)


def vap_028_va_low_trend_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of the 63-day VA-low (is support eroding?)."""
    va_lo, _ = _value_area_bounds(close, volume, _TD_QTR)
    return va_lo.diff(_TD_MON)


def vap_029_va_high_trend_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of the 63-day VA-high (ceiling drift)."""
    _, va_hi = _value_area_bounds(close, volume, _TD_QTR)
    return va_hi.diff(_TD_MON)


def vap_030_consec_days_below_va_low_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days current price has been below the 63-day value-area low."""
    va_lo, _ = _value_area_bounds(close, volume, _TD_QTR)
    cond = close < va_lo
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


# --- Group C (031-045): Overhead supply fraction (trapped-buyer proxy) ---

def vap_031_overhead_vol_frac_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of trailing 21-day volume transacted ABOVE current price (overhead supply)."""
    return _overhead_vol_fraction(close, volume, _TD_MON)


def vap_032_overhead_vol_frac_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of trailing 63-day volume transacted ABOVE current price."""
    return _overhead_vol_fraction(close, volume, _TD_QTR)


def vap_033_overhead_vol_frac_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of trailing 126-day volume transacted ABOVE current price."""
    return _overhead_vol_fraction(close, volume, _TD_HALF)


def vap_034_overhead_vol_frac_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of trailing 252-day volume transacted ABOVE current price."""
    return _overhead_vol_fraction(close, volume, _TD_YEAR)


def vap_035_overhead_vol_frac_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of trailing 5-day volume transacted ABOVE current price."""
    return _overhead_vol_fraction(close, volume, _TD_WEEK)


def vap_036_overhead_frac_21d_flag_high(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: 21-day overhead supply fraction > 0.70 (heavy overhead)."""
    return (_overhead_vol_fraction(close, volume, _TD_MON) > 0.70).astype(float)


def vap_037_overhead_frac_63d_flag_high(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: 63-day overhead supply fraction > 0.70."""
    return (_overhead_vol_fraction(close, volume, _TD_QTR) > 0.70).astype(float)


def vap_038_overhead_frac_252d_flag_extreme(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: 252-day overhead supply fraction > 0.85 (extreme trapped-buyer situation)."""
    return (_overhead_vol_fraction(close, volume, _TD_YEAR) > 0.85).astype(float)


def vap_039_overhead_frac_63d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 63-day overhead fraction relative to its 252-day distribution."""
    s = _overhead_vol_fraction(close, volume, _TD_QTR)
    m = _rolling_mean(s, _TD_YEAR)
    sd = _rolling_std(s, _TD_YEAR)
    return _safe_div(s - m, sd)


def vap_040_overhead_frac_21d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day overhead fraction vs 252-day history."""
    s = _overhead_vol_fraction(close, volume, _TD_MON)
    return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vap_041_overhead_frac_63d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day overhead fraction vs 252-day history."""
    s = _overhead_vol_fraction(close, volume, _TD_QTR)
    return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vap_042_overhead_frac_trend_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day overhead fraction (is overhead supply growing?)."""
    return _overhead_vol_fraction(close, volume, _TD_MON).diff(_TD_WEEK)


def vap_043_overhead_frac_trend_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day overhead fraction."""
    return _overhead_vol_fraction(close, volume, _TD_QTR).diff(_TD_MON)


def vap_044_below_vol_frac_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of trailing 63-day volume transacted BELOW current price (support cushion)."""
    return 1.0 - _overhead_vol_fraction(close, volume, _TD_QTR)


def vap_045_overhead_frac_max_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day maximum of 21-day overhead fraction (peak overhead in recent quarter)."""
    s = _overhead_vol_fraction(close, volume, _TD_MON)
    return _rolling_max(s, _TD_QTR)


# --- Group D (046-060): VWAP-band distances ---

def vap_046_vwap_dist_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance of close from 21-day VWAP, normalised by VWAP."""
    vwap = _vwap_window(close, volume, _TD_MON)
    return _safe_div(close - vwap, vwap.clip(lower=_EPS))


def vap_047_vwap_dist_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance of close from 63-day VWAP, normalised by VWAP."""
    vwap = _vwap_window(close, volume, _TD_QTR)
    return _safe_div(close - vwap, vwap.clip(lower=_EPS))


def vap_048_vwap_dist_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance of close from 126-day VWAP, normalised by VWAP."""
    vwap = _vwap_window(close, volume, _TD_HALF)
    return _safe_div(close - vwap, vwap.clip(lower=_EPS))


def vap_049_vwap_dist_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance of close from 252-day VWAP, normalised by VWAP."""
    vwap = _vwap_window(close, volume, _TD_YEAR)
    return _safe_div(close - vwap, vwap.clip(lower=_EPS))


def vap_050_vwap_below_flag_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: close is below 21-day VWAP."""
    return (close < _vwap_window(close, volume, _TD_MON)).astype(float)


def vap_051_vwap_below_flag_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: close is below 63-day VWAP."""
    return (close < _vwap_window(close, volume, _TD_QTR)).astype(float)


def vap_052_vwap_below_flag_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: close is below 252-day VWAP."""
    return (close < _vwap_window(close, volume, _TD_YEAR)).astype(float)


def vap_053_vwap_band_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of close relative to 21-day VWAP ± 1 volume-weighted std."""
    vwap = _vwap_window(close, volume, _TD_MON)
    vstd = _vwap_std_window(close, volume, _TD_MON)
    return _safe_div(close - vwap, vstd.clip(lower=_EPS))


def vap_054_vwap_band_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of close relative to 63-day VWAP ± volume-weighted std."""
    vwap = _vwap_window(close, volume, _TD_QTR)
    vstd = _vwap_std_window(close, volume, _TD_QTR)
    return _safe_div(close - vwap, vstd.clip(lower=_EPS))


def vap_055_vwap_band_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of close relative to 252-day VWAP ± volume-weighted std."""
    vwap = _vwap_window(close, volume, _TD_YEAR)
    vstd = _vwap_std_window(close, volume, _TD_YEAR)
    return _safe_div(close - vwap, vstd.clip(lower=_EPS))


def vap_056_vwap_dist_63d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day VWAP distance vs 252-day history."""
    dist = _safe_div(close - _vwap_window(close, volume, _TD_QTR),
                     _vwap_window(close, volume, _TD_QTR).clip(lower=_EPS))
    return dist.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vap_057_all_vwap_below_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: close is below 21d, 63d, and 252d VWAP simultaneously."""
    b21 = close < _vwap_window(close, volume, _TD_MON)
    b63 = close < _vwap_window(close, volume, _TD_QTR)
    b252 = close < _vwap_window(close, volume, _TD_YEAR)
    return (b21 & b63 & b252).astype(float)


def vap_058_vwap_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day VWAP (is the volume-weighted mean price declining?)."""
    return _vwap_window(close, volume, _TD_MON).diff(_TD_WEEK)


def vap_059_vwap_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day VWAP."""
    return _vwap_window(close, volume, _TD_QTR).diff(_TD_MON)


def vap_060_vwap_dist_21d_consec_below(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days close has been below 21-day VWAP."""
    cond = close < _vwap_window(close, volume, _TD_MON)
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


# --- Group E (061-075): HVN proximity features ---

def vap_061_hvn_proximity_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance from current price to nearest high-volume node in 21-day window (normalised)."""
    return _hvn_proximity(close, volume, _TD_MON)


def vap_062_hvn_proximity_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance from current price to nearest HVN in 63-day window (normalised)."""
    return _hvn_proximity(close, volume, _TD_QTR)


def vap_063_hvn_proximity_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance from current price to nearest HVN in 252-day window (normalised)."""
    return _hvn_proximity(close, volume, _TD_YEAR)


def vap_064_hvn_proximity_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance from current price to nearest HVN in 126-day window (normalised)."""
    return _hvn_proximity(close, volume, _TD_HALF)


def vap_065_at_hvn_flag_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: price is within 2% of the nearest 63-day HVN."""
    return (_hvn_proximity(close, volume, _TD_QTR) < 0.02).astype(float)


def vap_066_below_hvn_dist_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Signed distance below the nearest 63-day HVN (negative means below, clipped)."""
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
        mids = (edges[:-1] + edges[1:]) / 2.0
        hist_v = np.zeros(bins, dtype=float)
        for b in range(bins):
            if b < bins - 1:
                mbk = (c_w >= edges[b]) & (c_w < edges[b + 1])
            else:
                mbk = (c_w >= edges[b]) & (c_w <= edges[b + 1])
            hist_v[b] = v_w[mbk].sum()
        top_idx = np.argmax(hist_v)
        hvn_price = mids[top_idx]
        result[i] = (cur - hvn_price) / (hi - lo)
    return pd.Series(result, index=close.index)


def vap_067_hvn_proximity_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day HVN proximity vs 252-day history (low rank = far from HVN)."""
    s = _hvn_proximity(close, volume, _TD_QTR)
    return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vap_068_hvn_above_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of top-5 HVN nodes that are ABOVE current price in 63-day window."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    bins = _VAP_BINS
    w = _TD_QTR
    top_n = 5
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
            if b < bins - 1:
                mbk = (c_w >= edges[b]) & (c_w < edges[b + 1])
            else:
                mbk = (c_w >= edges[b]) & (c_w <= edges[b + 1])
            hist_v[b] = v_w[mbk].sum()
        top_idx = np.argsort(hist_v)[-top_n:]
        hvn_prices = mids[top_idx]
        result[i] = float((hvn_prices > cur).sum())
    return pd.Series(result, index=close.index)


def vap_069_hvn_below_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of top-5 HVN nodes that are BELOW current price in 63-day window."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    bins = _VAP_BINS
    w = _TD_QTR
    top_n = 5
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
            if b < bins - 1:
                mbk = (c_w >= edges[b]) & (c_w < edges[b + 1])
            else:
                mbk = (c_w >= edges[b]) & (c_w <= edges[b + 1])
            hist_v[b] = v_w[mbk].sum()
        top_idx = np.argsort(hist_v)[-top_n:]
        hvn_prices = mids[top_idx]
        result[i] = float((hvn_prices < cur).sum())
    return pd.Series(result, index=close.index)


def vap_070_hvn_vol_concentration_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of total 63-day volume concentrated in the single highest-volume bin."""
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
            if b < bins - 1:
                mbk = (c_w >= edges[b]) & (c_w < edges[b + 1])
            else:
                mbk = (c_w >= edges[b]) & (c_w <= edges[b + 1])
            hist_v[b] = v_w[mbk].sum()
        total = hist_v.sum()
        if total == 0:
            continue
        result[i] = hist_v.max() / total
    return pd.Series(result, index=close.index)


def vap_071_vap_entropy_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Shannon entropy of the 63-day VAP histogram (low entropy = concentrated distribution)."""
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
            result[i] = 0.0
            continue
        edges = np.linspace(lo, hi, bins + 1)
        hist_v = np.zeros(bins, dtype=float)
        for b in range(bins):
            if b < bins - 1:
                mbk = (c_w >= edges[b]) & (c_w < edges[b + 1])
            else:
                mbk = (c_w >= edges[b]) & (c_w <= edges[b + 1])
            hist_v[b] = v_w[mbk].sum()
        total = hist_v.sum()
        if total == 0:
            continue
        p = hist_v / total
        with np.errstate(divide='ignore', invalid='ignore'):
            ent = -np.where(p > 0, p * np.log(p), 0.0).sum()
        result[i] = ent
    return pd.Series(result, index=close.index)


def vap_072_vap_skew_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted price skewness of 63-day VAP histogram."""
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


def vap_073_vap_kurtosis_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Excess kurtosis of the 63-day volume-weighted price distribution."""
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
        if len(c_w) < max(4, w // 2):
            continue
        total = v_w.sum()
        if total == 0:
            continue
        mean = (c_w * v_w).sum() / total
        var = ((c_w - mean) ** 2 * v_w).sum() / total
        if var <= 0:
            result[i] = 0.0
            continue
        kurt = ((c_w - mean) ** 4 * v_w).sum() / total / (var ** 2) - 3.0
        result[i] = kurt
    return pd.Series(result, index=close.index)


def vap_074_poc_distance_expanding(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance from current price to expanding (all-history) POC, normalised by POC."""
    poc = _poc_window(close, volume, len(close))
    return _safe_div(close - poc, poc.clip(lower=_EPS))


def vap_075_vwap_dist_252d_pct_rank(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 252-day VWAP distance vs expanding history."""
    dist = _safe_div(close - _vwap_window(close, volume, _TD_YEAR),
                     _vwap_window(close, volume, _TD_YEAR).clip(lower=_EPS))
    return dist.expanding(min_periods=_TD_QTR).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_AT_PRICE_REGISTRY_001_075 = {
    "vap_001_poc_dist_21d": {"inputs": ["close", "volume"], "func": vap_001_poc_dist_21d},
    "vap_002_poc_dist_63d": {"inputs": ["close", "volume"], "func": vap_002_poc_dist_63d},
    "vap_003_poc_dist_126d": {"inputs": ["close", "volume"], "func": vap_003_poc_dist_126d},
    "vap_004_poc_dist_252d": {"inputs": ["close", "volume"], "func": vap_004_poc_dist_252d},
    "vap_005_poc_dist_5d": {"inputs": ["close", "volume"], "func": vap_005_poc_dist_5d},
    "vap_006_poc_below_flag_21d": {"inputs": ["close", "volume"], "func": vap_006_poc_below_flag_21d},
    "vap_007_poc_below_flag_63d": {"inputs": ["close", "volume"], "func": vap_007_poc_below_flag_63d},
    "vap_008_poc_below_flag_252d": {"inputs": ["close", "volume"], "func": vap_008_poc_below_flag_252d},
    "vap_009_poc_dist_63d_abs": {"inputs": ["close", "volume"], "func": vap_009_poc_dist_63d_abs},
    "vap_010_poc_dist_252d_abs": {"inputs": ["close", "volume"], "func": vap_010_poc_dist_252d_abs},
    "vap_011_poc_dist_21d_signed_norm_atr": {"inputs": ["close", "high", "low", "volume"], "func": vap_011_poc_dist_21d_signed_norm_atr},
    "vap_012_poc_dist_63d_signed_norm_atr": {"inputs": ["close", "high", "low", "volume"], "func": vap_012_poc_dist_63d_signed_norm_atr},
    "vap_013_poc_trend_21d": {"inputs": ["close", "volume"], "func": vap_013_poc_trend_21d},
    "vap_014_poc_trend_63d": {"inputs": ["close", "volume"], "func": vap_014_poc_trend_63d},
    "vap_015_poc_pct_rank_252d": {"inputs": ["close", "volume"], "func": vap_015_poc_pct_rank_252d},
    "vap_016_below_value_area_21d": {"inputs": ["close", "volume"], "func": vap_016_below_value_area_21d},
    "vap_017_below_value_area_63d": {"inputs": ["close", "volume"], "func": vap_017_below_value_area_63d},
    "vap_018_below_value_area_252d": {"inputs": ["close", "volume"], "func": vap_018_below_value_area_252d},
    "vap_019_va_low_dist_21d": {"inputs": ["close", "volume"], "func": vap_019_va_low_dist_21d},
    "vap_020_va_low_dist_63d": {"inputs": ["close", "volume"], "func": vap_020_va_low_dist_63d},
    "vap_021_va_low_dist_252d": {"inputs": ["close", "volume"], "func": vap_021_va_low_dist_252d},
    "vap_022_va_width_21d": {"inputs": ["close", "volume"], "func": vap_022_va_width_21d},
    "vap_023_va_width_63d": {"inputs": ["close", "volume"], "func": vap_023_va_width_63d},
    "vap_024_va_width_252d": {"inputs": ["close", "volume"], "func": vap_024_va_width_252d},
    "vap_025_price_in_va_flag_63d": {"inputs": ["close", "volume"], "func": vap_025_price_in_va_flag_63d},
    "vap_026_price_position_in_va_63d": {"inputs": ["close", "volume"], "func": vap_026_price_position_in_va_63d},
    "vap_027_price_position_in_va_252d": {"inputs": ["close", "volume"], "func": vap_027_price_position_in_va_252d},
    "vap_028_va_low_trend_63d": {"inputs": ["close", "volume"], "func": vap_028_va_low_trend_63d},
    "vap_029_va_high_trend_63d": {"inputs": ["close", "volume"], "func": vap_029_va_high_trend_63d},
    "vap_030_consec_days_below_va_low_63d": {"inputs": ["close", "volume"], "func": vap_030_consec_days_below_va_low_63d},
    "vap_031_overhead_vol_frac_21d": {"inputs": ["close", "volume"], "func": vap_031_overhead_vol_frac_21d},
    "vap_032_overhead_vol_frac_63d": {"inputs": ["close", "volume"], "func": vap_032_overhead_vol_frac_63d},
    "vap_033_overhead_vol_frac_126d": {"inputs": ["close", "volume"], "func": vap_033_overhead_vol_frac_126d},
    "vap_034_overhead_vol_frac_252d": {"inputs": ["close", "volume"], "func": vap_034_overhead_vol_frac_252d},
    "vap_035_overhead_vol_frac_5d": {"inputs": ["close", "volume"], "func": vap_035_overhead_vol_frac_5d},
    "vap_036_overhead_frac_21d_flag_high": {"inputs": ["close", "volume"], "func": vap_036_overhead_frac_21d_flag_high},
    "vap_037_overhead_frac_63d_flag_high": {"inputs": ["close", "volume"], "func": vap_037_overhead_frac_63d_flag_high},
    "vap_038_overhead_frac_252d_flag_extreme": {"inputs": ["close", "volume"], "func": vap_038_overhead_frac_252d_flag_extreme},
    "vap_039_overhead_frac_63d_zscore_252d": {"inputs": ["close", "volume"], "func": vap_039_overhead_frac_63d_zscore_252d},
    "vap_040_overhead_frac_21d_pct_rank_252d": {"inputs": ["close", "volume"], "func": vap_040_overhead_frac_21d_pct_rank_252d},
    "vap_041_overhead_frac_63d_pct_rank_252d": {"inputs": ["close", "volume"], "func": vap_041_overhead_frac_63d_pct_rank_252d},
    "vap_042_overhead_frac_trend_21d": {"inputs": ["close", "volume"], "func": vap_042_overhead_frac_trend_21d},
    "vap_043_overhead_frac_trend_63d": {"inputs": ["close", "volume"], "func": vap_043_overhead_frac_trend_63d},
    "vap_044_below_vol_frac_63d": {"inputs": ["close", "volume"], "func": vap_044_below_vol_frac_63d},
    "vap_045_overhead_frac_max_63d": {"inputs": ["close", "volume"], "func": vap_045_overhead_frac_max_63d},
    "vap_046_vwap_dist_21d": {"inputs": ["close", "volume"], "func": vap_046_vwap_dist_21d},
    "vap_047_vwap_dist_63d": {"inputs": ["close", "volume"], "func": vap_047_vwap_dist_63d},
    "vap_048_vwap_dist_126d": {"inputs": ["close", "volume"], "func": vap_048_vwap_dist_126d},
    "vap_049_vwap_dist_252d": {"inputs": ["close", "volume"], "func": vap_049_vwap_dist_252d},
    "vap_050_vwap_below_flag_21d": {"inputs": ["close", "volume"], "func": vap_050_vwap_below_flag_21d},
    "vap_051_vwap_below_flag_63d": {"inputs": ["close", "volume"], "func": vap_051_vwap_below_flag_63d},
    "vap_052_vwap_below_flag_252d": {"inputs": ["close", "volume"], "func": vap_052_vwap_below_flag_252d},
    "vap_053_vwap_band_zscore_21d": {"inputs": ["close", "volume"], "func": vap_053_vwap_band_zscore_21d},
    "vap_054_vwap_band_zscore_63d": {"inputs": ["close", "volume"], "func": vap_054_vwap_band_zscore_63d},
    "vap_055_vwap_band_zscore_252d": {"inputs": ["close", "volume"], "func": vap_055_vwap_band_zscore_252d},
    "vap_056_vwap_dist_63d_pct_rank_252d": {"inputs": ["close", "volume"], "func": vap_056_vwap_dist_63d_pct_rank_252d},
    "vap_057_all_vwap_below_flag": {"inputs": ["close", "volume"], "func": vap_057_all_vwap_below_flag},
    "vap_058_vwap_slope_21d": {"inputs": ["close", "volume"], "func": vap_058_vwap_slope_21d},
    "vap_059_vwap_slope_63d": {"inputs": ["close", "volume"], "func": vap_059_vwap_slope_63d},
    "vap_060_vwap_dist_21d_consec_below": {"inputs": ["close", "volume"], "func": vap_060_vwap_dist_21d_consec_below},
    "vap_061_hvn_proximity_21d": {"inputs": ["close", "volume"], "func": vap_061_hvn_proximity_21d},
    "vap_062_hvn_proximity_63d": {"inputs": ["close", "volume"], "func": vap_062_hvn_proximity_63d},
    "vap_063_hvn_proximity_252d": {"inputs": ["close", "volume"], "func": vap_063_hvn_proximity_252d},
    "vap_064_hvn_proximity_126d": {"inputs": ["close", "volume"], "func": vap_064_hvn_proximity_126d},
    "vap_065_at_hvn_flag_63d": {"inputs": ["close", "volume"], "func": vap_065_at_hvn_flag_63d},
    "vap_066_below_hvn_dist_63d": {"inputs": ["close", "volume"], "func": vap_066_below_hvn_dist_63d},
    "vap_067_hvn_proximity_pct_rank_252d": {"inputs": ["close", "volume"], "func": vap_067_hvn_proximity_pct_rank_252d},
    "vap_068_hvn_above_count_63d": {"inputs": ["close", "volume"], "func": vap_068_hvn_above_count_63d},
    "vap_069_hvn_below_count_63d": {"inputs": ["close", "volume"], "func": vap_069_hvn_below_count_63d},
    "vap_070_hvn_vol_concentration_63d": {"inputs": ["close", "volume"], "func": vap_070_hvn_vol_concentration_63d},
    "vap_071_vap_entropy_63d": {"inputs": ["close", "volume"], "func": vap_071_vap_entropy_63d},
    "vap_072_vap_skew_63d": {"inputs": ["close", "volume"], "func": vap_072_vap_skew_63d},
    "vap_073_vap_kurtosis_63d": {"inputs": ["close", "volume"], "func": vap_073_vap_kurtosis_63d},
    "vap_074_poc_distance_expanding": {"inputs": ["close", "volume"], "func": vap_074_poc_distance_expanding},
    "vap_075_vwap_dist_252d_pct_rank": {"inputs": ["close", "volume"], "func": vap_075_vwap_dist_252d_pct_rank},
}
