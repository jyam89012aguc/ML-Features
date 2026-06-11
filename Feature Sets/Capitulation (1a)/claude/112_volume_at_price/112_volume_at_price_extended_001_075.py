"""
112_volume_at_price — Extended Features 001-075
Domain: Volume-at-price deeper variants — finer-resolution VAP histograms (30/50 bins),
        80% and 90% value-area variants, price-to-volume decile analysis,
        HVN gap analysis, volume-weighted price quantiles, multi-timeframe entropy,
        VWAP-distance cross-series, and cross-window composite distress scores
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
_VAP_BINS_FINE = 30
_VAP_BINS_ULTRA = 50

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


def _vwap_decile_position(close: pd.Series, volume: pd.Series, w: int) -> pd.Series:
    """Volume-weighted decile position of current price in trailing w-bar distribution (0-9)."""
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
        # fraction of volume at or below current price
        frac_below = v_w[c_w <= cur].sum() / total
        result[i] = frac_below * 9.0  # 0 to 9 scale
    return pd.Series(result, index=close.index)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Fine-resolution (30-bin) POC distance variants ---

def vap_ext_001_poc_dist_21d_fine(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day POC distance using 30-bin fine-resolution histogram."""
    poc = _poc_window(close, volume, _TD_MON, bins=_VAP_BINS_FINE)
    return _safe_div(close - poc, poc.clip(lower=_EPS))


def vap_ext_002_poc_dist_63d_fine(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day POC distance using 30-bin fine-resolution histogram."""
    poc = _poc_window(close, volume, _TD_QTR, bins=_VAP_BINS_FINE)
    return _safe_div(close - poc, poc.clip(lower=_EPS))


def vap_ext_003_poc_dist_252d_fine(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day POC distance using 30-bin fine-resolution histogram."""
    poc = _poc_window(close, volume, _TD_YEAR, bins=_VAP_BINS_FINE)
    return _safe_div(close - poc, poc.clip(lower=_EPS))


def vap_ext_004_poc_dist_63d_ultra(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day POC distance using 50-bin ultra-fine histogram."""
    poc = _poc_window(close, volume, _TD_QTR, bins=_VAP_BINS_ULTRA)
    return _safe_div(close - poc, poc.clip(lower=_EPS))


def vap_ext_005_poc_below_flag_63d_fine(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary: price below 63-day POC (fine 30-bin resolution)."""
    poc = _poc_window(close, volume, _TD_QTR, bins=_VAP_BINS_FINE)
    return (close < poc).astype(float)


def vap_ext_006_poc_dist_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """126-day POC distance with fine 30-bin histogram."""
    poc = _poc_window(close, volume, _TD_HALF, bins=_VAP_BINS_FINE)
    return _safe_div(close - poc, poc.clip(lower=_EPS))


def vap_ext_007_poc_fine_vs_coarse_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Difference between fine (30-bin) and coarse (20-bin) 63-day POC estimates."""
    poc_fine = _poc_window(close, volume, _TD_QTR, bins=_VAP_BINS_FINE)
    poc_coarse = _poc_window(close, volume, _TD_QTR, bins=_VAP_BINS)
    return _safe_div(poc_fine - poc_coarse, poc_coarse.clip(lower=_EPS))


def vap_ext_008_poc_dist_21d_pct_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day POC distance vs 126-day history."""
    dist = _safe_div(close - _poc_window(close, volume, _TD_MON),
                     _poc_window(close, volume, _TD_MON).clip(lower=_EPS))
    return dist.rolling(_TD_HALF, min_periods=_TD_QTR).rank(pct=True)


def vap_ext_009_poc_dist_63d_pct_rank_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day POC distance vs 126-day history."""
    dist = _safe_div(close - _poc_window(close, volume, _TD_QTR),
                     _poc_window(close, volume, _TD_QTR).clip(lower=_EPS))
    return dist.rolling(_TD_HALF, min_periods=_TD_QTR).rank(pct=True)


def vap_ext_010_poc_dist_252d_zscore_expanding(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding z-score of 252-day POC distance."""
    dist = _safe_div(close - _poc_window(close, volume, _TD_YEAR),
                     _poc_window(close, volume, _TD_YEAR).clip(lower=_EPS))
    m = dist.expanding(min_periods=_TD_QTR).mean()
    s = dist.expanding(min_periods=_TD_QTR).std()
    return _safe_div(dist - m, s)


# --- Group B (011-020): 80% and 90% value-area variants ---

def vap_ext_011_below_va80_low_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: price below 80% value-area low (63-day window)."""
    va_lo, _ = _value_area_bounds(close, volume, _TD_QTR, va_frac=0.80)
    return (close < va_lo).astype(float)


def vap_ext_012_below_va90_low_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: price below 90% value-area low (63-day window)."""
    va_lo, _ = _value_area_bounds(close, volume, _TD_QTR, va_frac=0.90)
    return (close < va_lo).astype(float)


def vap_ext_013_va80_low_dist_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance below 80%-VA low (63-day), normalised by VA-low price."""
    va_lo, _ = _value_area_bounds(close, volume, _TD_QTR, va_frac=0.80)
    return _safe_div((va_lo - close).clip(lower=0.0), va_lo.clip(lower=_EPS))


def vap_ext_014_va90_low_dist_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance below 90%-VA low (63-day), normalised by VA-low price."""
    va_lo, _ = _value_area_bounds(close, volume, _TD_QTR, va_frac=0.90)
    return _safe_div((va_lo - close).clip(lower=0.0), va_lo.clip(lower=_EPS))


def vap_ext_015_below_va80_low_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: price below 80% value-area low (252-day window)."""
    va_lo, _ = _value_area_bounds(close, volume, _TD_YEAR, va_frac=0.80)
    return (close < va_lo).astype(float)


def vap_ext_016_va80_width_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Width of 80%-value-area (63-day) normalised by close."""
    va_lo, va_hi = _value_area_bounds(close, volume, _TD_QTR, va_frac=0.80)
    return _safe_div(va_hi - va_lo, close.clip(lower=_EPS))


def vap_ext_017_va90_width_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Width of 90%-value-area (252-day) normalised by close."""
    va_lo, va_hi = _value_area_bounds(close, volume, _TD_YEAR, va_frac=0.90)
    return _safe_div(va_hi - va_lo, close.clip(lower=_EPS))


def vap_ext_018_price_position_in_va80_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price position within 80%-VA (63-day): 0=at low, 1=at high."""
    va_lo, va_hi = _value_area_bounds(close, volume, _TD_QTR, va_frac=0.80)
    width = (va_hi - va_lo).replace(0, np.nan)
    return ((close - va_lo) / width).clip(lower=0.0, upper=1.0)


def vap_ext_019_va70_vs_va90_width_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 70%-VA width to 90%-VA width (measure of volume profile spikiness)."""
    va70_lo, va70_hi = _value_area_bounds(close, volume, _TD_QTR, va_frac=0.70)
    va90_lo, va90_hi = _value_area_bounds(close, volume, _TD_QTR, va_frac=0.90)
    w70 = va70_hi - va70_lo
    w90 = (va90_hi - va90_lo).replace(0, np.nan)
    return _safe_div(w70, w90)


def vap_ext_020_below_all_va_lows_70_80_90(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary: price below 70%, 80%, AND 90% VA-lows simultaneously (63-day)."""
    va70_lo, _ = _value_area_bounds(close, volume, _TD_QTR, va_frac=0.70)
    va80_lo, _ = _value_area_bounds(close, volume, _TD_QTR, va_frac=0.80)
    va90_lo, _ = _value_area_bounds(close, volume, _TD_QTR, va_frac=0.90)
    return ((close < va70_lo) & (close < va80_lo) & (close < va90_lo)).astype(float)


# --- Group C (021-030): Volume decile analysis ---

def vap_ext_021_vol_decile_pos_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted decile position in 21-day window (0=bottom, 9=top)."""
    return _vwap_decile_position(close, volume, _TD_MON)


def vap_ext_022_vol_decile_pos_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted decile position in 63-day window."""
    return _vwap_decile_position(close, volume, _TD_QTR)


def vap_ext_023_vol_decile_pos_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted decile position in 252-day window."""
    return _vwap_decile_position(close, volume, _TD_YEAR)


def vap_ext_024_vol_decile_below2_63d_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: price in lowest 2 deciles of 63-day volume-weighted distribution."""
    return (_vwap_decile_position(close, volume, _TD_QTR) < 2.0).astype(float)


def vap_ext_025_vol_decile_below1_252d_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: price in lowest 1 decile of 252-day volume-weighted distribution."""
    return (_vwap_decile_position(close, volume, _TD_YEAR) < 1.0).astype(float)


def vap_ext_026_vol_decile_pos_63d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day decile position vs 252-day history."""
    s = _vwap_decile_position(close, volume, _TD_QTR)
    return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vap_ext_027_vol_decile_spread_21d_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Difference of 21-day decile position vs 252-day decile position."""
    return _vwap_decile_position(close, volume, _TD_MON) - _vwap_decile_position(close, volume, _TD_YEAR)


def vap_ext_028_vol_decile_pos_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day decile position (velocity of decile shift)."""
    return _vwap_decile_position(close, volume, _TD_MON).diff(_TD_WEEK)


def vap_ext_029_vol_decile_pos_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day decile position."""
    return _vwap_decile_position(close, volume, _TD_QTR).diff(_TD_MON)


def vap_ext_030_vol_decile_pos_252d_min_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day minimum of the 252-day decile position."""
    return _rolling_min(_vwap_decile_position(close, volume, _TD_YEAR), _TD_MON)


# --- Group D (031-040): HVN gap and node-cluster features ---

def vap_ext_031_hvn_gap_above_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume gap (LVN) above current price in 63-day VAP — fraction of range between
    current price and next HVN that has below-average volume (structural weakness above)."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    bins = _VAP_BINS_FINE
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
            mbk = (c_w >= edges[b]) & (c_w < edges[b + 1]) if b < bins - 1 else (c_w >= edges[b]) & (c_w <= edges[b + 1])
            hist_v[b] = v_w[mbk].sum()
        avg_v = hist_v.mean()
        # bins above current price
        above_mask = mids > cur
        if not above_mask.any():
            result[i] = 0.0
            continue
        above_hist = hist_v[above_mask]
        # fraction of above-price bins that are LVN (below avg)
        lvn_count = (above_hist < avg_v).sum()
        result[i] = lvn_count / above_mask.sum()
    return pd.Series(result, index=close.index)


def vap_ext_032_hvn_gap_below_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of below-price bins that are LVN in 63-day VAP (thin support floor)."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    bins = _VAP_BINS_FINE
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
            mbk = (c_w >= edges[b]) & (c_w < edges[b + 1]) if b < bins - 1 else (c_w >= edges[b]) & (c_w <= edges[b + 1])
            hist_v[b] = v_w[mbk].sum()
        avg_v = hist_v.mean()
        below_mask = mids < cur
        if not below_mask.any():
            result[i] = 0.0
            continue
        below_hist = hist_v[below_mask]
        lvn_count = (below_hist < avg_v).sum()
        result[i] = lvn_count / below_mask.sum()
    return pd.Series(result, index=close.index)


def vap_ext_033_hvn_gap_asymmetry_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """LVN asymmetry above minus below (positive = more gap above = more overhead weakness)."""
    return vap_ext_031_hvn_gap_above_63d(close, volume) - vap_ext_032_hvn_gap_below_63d(close, volume)


def vap_ext_034_poc_fine_30bin_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of fine (30-bin) 63-day POC distance vs 252-day history."""
    dist = _safe_div(close - _poc_window(close, volume, _TD_QTR, bins=_VAP_BINS_FINE),
                     _poc_window(close, volume, _TD_QTR, bins=_VAP_BINS_FINE).clip(lower=_EPS))
    return dist.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vap_ext_035_hvn_above_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of top-5 HVN nodes ABOVE current price in 252-day window."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    bins = _VAP_BINS
    w = _TD_YEAR
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
            mbk = (c_w >= edges[b]) & (c_w < edges[b + 1]) if b < bins - 1 else (c_w >= edges[b]) & (c_w <= edges[b + 1])
            hist_v[b] = v_w[mbk].sum()
        top_idx = np.argsort(hist_v)[-top_n:]
        result[i] = float((mids[top_idx] > cur).sum())
    return pd.Series(result, index=close.index)


def vap_ext_036_hvn_below_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of top-5 HVN nodes BELOW current price in 252-day window."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    bins = _VAP_BINS
    w = _TD_YEAR
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
            mbk = (c_w >= edges[b]) & (c_w < edges[b + 1]) if b < bins - 1 else (c_w >= edges[b]) & (c_w <= edges[b + 1])
            hist_v[b] = v_w[mbk].sum()
        top_idx = np.argsort(hist_v)[-top_n:]
        result[i] = float((mids[top_idx] < cur).sum())
    return pd.Series(result, index=close.index)


def vap_ext_037_hvn_above_below_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of HVN-above-count to HVN-below-count (252-day) — >1 = more overhead HVNs."""
    above = vap_ext_035_hvn_above_count_252d(close, volume)
    below = vap_ext_036_hvn_below_count_252d(close, volume).replace(0, np.nan)
    return _safe_div(above, below)


def vap_ext_038_hvn_proximity_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance to nearest HVN in 21-day window."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    bins = _VAP_BINS
    w = _TD_MON
    top_n = 3
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


def vap_ext_039_hvn_concentration_top3_vs_top5_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of volume in top-3 HVN bins vs top-5 HVN bins (63-day)."""
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
        sorted_v = np.sort(hist_v)[::-1]
        top3 = sorted_v[:3].sum()
        top5 = sorted_v[:5].sum()
        if top5 == 0:
            continue
        result[i] = top3 / top5
    return pd.Series(result, index=close.index)


def vap_ext_040_hvn_proximity_252d_pct_rank_expanding(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252-day HVN proximity."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    bins = _VAP_BINS
    w = _TD_YEAR
    top_n = 3
    hvn_arr = np.full(n, np.nan)
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
            hvn_arr[i] = 0.0
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
        hvn_arr[i] = dists.min() / (hi - lo)
    s = pd.Series(hvn_arr, index=close.index)
    return s.expanding(min_periods=_TD_QTR).rank(pct=True)


# --- Group E (041-055): VWAP cross-series and additional window features ---

def vap_ext_041_vwap_dist_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance of close from 5-day VWAP, normalised by VWAP."""
    vwap = _vwap_window(close, volume, _TD_WEEK)
    return _safe_div(close - vwap, vwap.clip(lower=_EPS))


def vap_ext_042_vwap_dist_5d_pct_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 5-day VWAP distance vs 63-day history."""
    dist = _safe_div(close - _vwap_window(close, volume, _TD_WEEK),
                     _vwap_window(close, volume, _TD_WEEK).clip(lower=_EPS))
    return dist.rolling(_TD_QTR, min_periods=_TD_MON).rank(pct=True)


def vap_ext_043_vwap_band_zscore_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of close relative to 126-day VWAP ± volume-weighted std."""
    vwap = _vwap_window(close, volume, _TD_HALF)
    vstd = _vwap_std_window(close, volume, _TD_HALF)
    return _safe_div(close - vwap, vstd.clip(lower=_EPS))


def vap_ext_044_vwap_band_below_2std_flag_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: close more than 2 VWAP-std below 252-day VWAP."""
    vwap = _vwap_window(close, volume, _TD_YEAR)
    vstd = _vwap_std_window(close, volume, _TD_YEAR)
    return (close < vwap - 2.0 * vstd).astype(float)


def vap_ext_045_vwap_band_below_3std_flag_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: close more than 3 VWAP-std below 63-day VWAP (deep panic)."""
    vwap = _vwap_window(close, volume, _TD_QTR)
    vstd = _vwap_std_window(close, volume, _TD_QTR)
    return (close < vwap - 3.0 * vstd).astype(float)


def vap_ext_046_vwap_dist_high_21d(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance of daily HIGH from 21-day VWAP (measures intraday reach toward VWAP)."""
    vwap = _vwap_window(close, volume, _TD_MON)
    return _safe_div(high - vwap, vwap.clip(lower=_EPS))


def vap_ext_047_vwap_dist_low_21d(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance of daily LOW from 21-day VWAP (negative = low probed below VWAP)."""
    vwap = _vwap_window(close, volume, _TD_MON)
    return _safe_div(low - vwap, vwap.clip(lower=_EPS))


def vap_ext_048_vwap_dist_252d_zscore_expanding(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding z-score of 252-day VWAP distance."""
    dist = _safe_div(close - _vwap_window(close, volume, _TD_YEAR),
                     _vwap_window(close, volume, _TD_YEAR).clip(lower=_EPS))
    m = dist.expanding(min_periods=_TD_QTR).mean()
    s = dist.expanding(min_periods=_TD_QTR).std()
    return _safe_div(dist - m, s)


def vap_ext_049_vwap_std_63d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day VWAP std (volatility of volume-weighted price) vs 252-day history."""
    vstd = _vwap_std_window(close, volume, _TD_QTR)
    return vstd.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vap_ext_050_vwap_dist_21d_in_252d_count_below_neg5pct(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in 252 days where 21-day VWAP distance < -5%."""
    dist = _safe_div(close - _vwap_window(close, volume, _TD_MON),
                     _vwap_window(close, volume, _TD_MON).clip(lower=_EPS))
    return _rolling_sum((dist < -0.05).astype(float), _TD_YEAR)


def vap_ext_051_vwap_63d_consec_below_21d_vwap(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days 63-day VWAP has been below 21-day VWAP (bearish term structure)."""
    v21 = _vwap_window(close, volume, _TD_MON)
    v63 = _vwap_window(close, volume, _TD_QTR)
    cond = v63 < v21
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def vap_ext_052_vwap_dist_21d_vs_63d_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day to 63-day VWAP distance (short-term vs medium-term VWAP pressure)."""
    d21 = _safe_div(close - _vwap_window(close, volume, _TD_MON),
                    _vwap_window(close, volume, _TD_MON).clip(lower=_EPS))
    d63 = _safe_div(close - _vwap_window(close, volume, _TD_QTR),
                    _vwap_window(close, volume, _TD_QTR).clip(lower=_EPS))
    return _safe_div(d21, d63.abs().clip(lower=_EPS))


def vap_ext_053_overhead_frac_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """126-day overhead supply fraction."""
    return _overhead_vol_fraction(close, volume, _TD_HALF)


def vap_ext_054_overhead_frac_126d_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 126-day overhead fraction vs 252-day history."""
    s = _overhead_vol_fraction(close, volume, _TD_HALF)
    return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vap_ext_055_overhead_frac_all4_avg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average of 21d, 63d, 126d, 252d overhead supply fractions (4-window composite)."""
    return (
        _overhead_vol_fraction(close, volume, _TD_MON) +
        _overhead_vol_fraction(close, volume, _TD_QTR) +
        _overhead_vol_fraction(close, volume, _TD_HALF) +
        _overhead_vol_fraction(close, volume, _TD_YEAR)
    ) / 4.0


# --- Group F (056-065): Multi-window entropy and concentration ---

def vap_ext_056_vap_entropy_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Shannon entropy of 21-day VAP histogram."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    bins = _VAP_BINS
    w = _TD_MON
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
            result[i] = -np.where(p > 0, p * np.log(p), 0.0).sum()
    return pd.Series(result, index=close.index)


def vap_ext_057_vap_entropy_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Shannon entropy of 126-day VAP histogram."""
    n = len(close)
    result = np.full(n, np.nan)
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    bins = _VAP_BINS
    w = _TD_HALF
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
            result[i] = -np.where(p > 0, p * np.log(p), 0.0).sum()
    return pd.Series(result, index=close.index)


def vap_ext_058_vap_entropy_ratio_63d_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 63-day entropy to 252-day entropy (profile concentration comparison)."""
    n = len(close)
    def _entropy_for_w(c_arr, v_arr, i, w, bins):
        start = max(0, i - w + 1)
        c_w = c_arr[start:i + 1]
        v_w = v_arr[start:i + 1]
        mask = ~(np.isnan(c_w) | np.isnan(v_w))
        c_w = c_w[mask]
        v_w = v_w[mask]
        if len(c_w) < max(2, w // 2):
            return np.nan
        lo, hi = c_w.min(), c_w.max()
        if hi <= lo:
            return 0.0
        edges = np.linspace(lo, hi, bins + 1)
        hist_v = np.zeros(bins, dtype=float)
        for b in range(bins):
            mbk = (c_w >= edges[b]) & (c_w < edges[b + 1]) if b < bins - 1 else (c_w >= edges[b]) & (c_w <= edges[b + 1])
            hist_v[b] = v_w[mbk].sum()
        total = hist_v.sum()
        if total == 0:
            return np.nan
        p = hist_v / total
        with np.errstate(divide='ignore', invalid='ignore'):
            return -np.where(p > 0, p * np.log(p), 0.0).sum()
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    result = np.full(n, np.nan)
    for i in range(n):
        e63 = _entropy_for_w(c_arr, v_arr, i, _TD_QTR, _VAP_BINS)
        e252 = _entropy_for_w(c_arr, v_arr, i, _TD_YEAR, _VAP_BINS)
        if e252 is not None and not np.isnan(e252) and e252 != 0:
            result[i] = e63 / e252
    return pd.Series(result, index=close.index)


def vap_ext_059_hvn_vol_concentration_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of total 252-day volume in the single highest-volume bin."""
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


def vap_ext_060_vap_concentration_ratio_63d_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 63-day max-bin concentration to 252-day max-bin concentration."""
    n = len(close)
    def _max_conc(c_arr, v_arr, i, w, bins):
        start = max(0, i - w + 1)
        c_w = c_arr[start:i + 1]
        v_w = v_arr[start:i + 1]
        mask = ~(np.isnan(c_w) | np.isnan(v_w))
        c_w = c_w[mask]
        v_w = v_w[mask]
        if len(c_w) < max(2, w // 2):
            return np.nan
        lo, hi = c_w.min(), c_w.max()
        if hi <= lo:
            return 1.0
        edges = np.linspace(lo, hi, bins + 1)
        hist_v = np.zeros(bins, dtype=float)
        for b in range(bins):
            mbk = (c_w >= edges[b]) & (c_w < edges[b + 1]) if b < bins - 1 else (c_w >= edges[b]) & (c_w <= edges[b + 1])
            hist_v[b] = v_w[mbk].sum()
        total = hist_v.sum()
        if total == 0:
            return np.nan
        return hist_v.max() / total
    c_arr = close.values.astype(float)
    v_arr = volume.values.astype(float)
    result = np.full(n, np.nan)
    for i in range(n):
        c63 = _max_conc(c_arr, v_arr, i, _TD_QTR, _VAP_BINS)
        c252 = _max_conc(c_arr, v_arr, i, _TD_YEAR, _VAP_BINS)
        if c252 is not None and not np.isnan(c252) and c252 != 0:
            result[i] = c63 / c252
    return pd.Series(result, index=close.index)


# --- Group G (061-075): Cross-feature composite distress and regime scores ---

def vap_ext_061_vap_distress_score_5dim(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-dimension VAP distress: overhead_252d + below_va90_63d + vwap_band_z_63d_neg
    + poc_dist_252d_neg + decile_pos_252d_inv — composite of the deepest features."""
    oh252 = _overhead_vol_fraction(close, volume, _TD_YEAR)
    va90_lo, _ = _value_area_bounds(close, volume, _TD_QTR, va_frac=0.90)
    below_va90 = (close < va90_lo).astype(float)
    vwap63 = _vwap_window(close, volume, _TD_QTR)
    vstd63 = _vwap_std_window(close, volume, _TD_QTR)
    z63_neg = (-_safe_div(close - vwap63, vstd63.clip(lower=_EPS))).clip(lower=0.0) / 3.0
    poc252 = _poc_window(close, volume, _TD_YEAR)
    poc_dist_neg = (-_safe_div(close - poc252, poc252.clip(lower=_EPS))).clip(lower=0.0)
    decile_inv = 1.0 - _vwap_decile_position(close, volume, _TD_YEAR) / 9.0
    return oh252 + below_va90 + z63_neg + poc_dist_neg + decile_inv


def vap_ext_062_vap_distress_score_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 5-dim VAP distress score vs 252-day history."""
    score = vap_ext_061_vap_distress_score_5dim(close, volume)
    return score.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vap_ext_063_overhead_frac_21d_vs_63d_acceleration(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of (21d overhead - 63d overhead) — is overhead supply building faster short term?"""
    spread = _overhead_vol_fraction(close, volume, _TD_MON) - _overhead_vol_fraction(close, volume, _TD_QTR)
    return spread.diff(_TD_WEEK)


def vap_ext_064_poc_dist_trend_coherence_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Correlation of 21-day POC distance and 63-day POC distance over 63-day window."""
    d21 = _safe_div(close - _poc_window(close, volume, _TD_MON),
                    _poc_window(close, volume, _TD_MON).clip(lower=_EPS))
    d63 = _safe_div(close - _poc_window(close, volume, _TD_QTR),
                    _poc_window(close, volume, _TD_QTR).clip(lower=_EPS))
    return d21.rolling(_TD_QTR, min_periods=_TD_MON).corr(d63)


def vap_ext_065_vwap_poc_distance_spread_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """VWAP distance minus POC distance (63-day): divergence between mean-volume and peak-volume anchor."""
    vwap_dist = _safe_div(close - _vwap_window(close, volume, _TD_QTR),
                          _vwap_window(close, volume, _TD_QTR).clip(lower=_EPS))
    poc_dist = _safe_div(close - _poc_window(close, volume, _TD_QTR),
                         _poc_window(close, volume, _TD_QTR).clip(lower=_EPS))
    return vwap_dist - poc_dist


def vap_ext_066_all_distress_signals_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary: price below 63d VA-low AND below 252d POC AND 252d overhead > 0.75."""
    va_lo_63, _ = _value_area_bounds(close, volume, _TD_QTR)
    poc252 = _poc_window(close, volume, _TD_YEAR)
    oh252 = _overhead_vol_fraction(close, volume, _TD_YEAR)
    return ((close < va_lo_63) & (close < poc252) & (oh252 > 0.75)).astype(float)


def vap_ext_067_va_low_63d_expanding_min(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding minimum of 63-day VA-low price (has support ever been this low?)."""
    va_lo, _ = _value_area_bounds(close, volume, _TD_QTR)
    return va_lo.expanding(min_periods=_TD_QTR).min()


def vap_ext_068_poc_63d_expanding_min(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding minimum of 63-day POC price level."""
    poc = _poc_window(close, volume, _TD_QTR)
    return poc.expanding(min_periods=_TD_QTR).min()


def vap_ext_069_overhead_frac_63d_decay_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM-decayed (21-day span) version of 63-day overhead fraction."""
    s = _overhead_vol_fraction(close, volume, _TD_QTR)
    return _ewm_mean(s, _TD_MON)


def vap_ext_070_overhead_frac_21d_max_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day maximum of the 21-day overhead supply fraction."""
    s = _overhead_vol_fraction(close, volume, _TD_MON)
    return _rolling_max(s, _TD_YEAR)


def vap_ext_071_vwap_dist_21d_max_abs_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day maximum absolute value of 21-day VWAP distance (extreme dislocation ever reached)."""
    dist = _safe_div(close - _vwap_window(close, volume, _TD_MON),
                     _vwap_window(close, volume, _TD_MON).clip(lower=_EPS)).abs()
    return _rolling_max(dist, _TD_YEAR)


def vap_ext_072_poc_dist_21d_consec_neg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days 21-day POC distance is negative (price persistently below POC)."""
    dist = _safe_div(close - _poc_window(close, volume, _TD_MON),
                     _poc_window(close, volume, _TD_MON).clip(lower=_EPS))
    cond = dist < 0
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def vap_ext_073_vwap_dist_63d_consec_neg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days 63-day VWAP distance is negative."""
    dist = _safe_div(close - _vwap_window(close, volume, _TD_QTR),
                     _vwap_window(close, volume, _TD_QTR).clip(lower=_EPS))
    cond = dist < 0
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def vap_ext_074_below_vol_frac_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 252-day volume BELOW current price (how thin is the volume floor?)."""
    return 1.0 - _overhead_vol_fraction(close, volume, _TD_YEAR)


def vap_ext_075_vap_ultimate_distress_composite(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ultimate VAP capitulation composite: normalised sum of overhead_252d, poc_dist_252d (neg clipped),
    vwap_dist_252d (neg clipped), below_va90_252d flag, and below_decile1_252d flag.
    Higher = deeper multi-dimensional VAP distress."""
    oh = _overhead_vol_fraction(close, volume, _TD_YEAR)
    poc252 = _poc_window(close, volume, _TD_YEAR)
    poc_dist = _safe_div(close - poc252, poc252.clip(lower=_EPS))
    poc_neg = (-poc_dist).clip(lower=0.0)
    vwap252 = _vwap_window(close, volume, _TD_YEAR)
    vwap_dist = _safe_div(close - vwap252, vwap252.clip(lower=_EPS))
    vwap_neg = (-vwap_dist).clip(lower=0.0)
    va90_lo, _ = _value_area_bounds(close, volume, _TD_YEAR, va_frac=0.90)
    below_va90 = (close < va90_lo).astype(float)
    decile_inv = (1.0 - _vwap_decile_position(close, volume, _TD_YEAR) / 9.0).clip(lower=0.0)
    return oh + poc_neg + vwap_neg + below_va90 + decile_inv


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_AT_PRICE_EXTENDED_REGISTRY_001_075 = {
    "vap_ext_001_poc_dist_21d_fine": {"inputs": ["close", "volume"], "func": vap_ext_001_poc_dist_21d_fine},
    "vap_ext_002_poc_dist_63d_fine": {"inputs": ["close", "volume"], "func": vap_ext_002_poc_dist_63d_fine},
    "vap_ext_003_poc_dist_252d_fine": {"inputs": ["close", "volume"], "func": vap_ext_003_poc_dist_252d_fine},
    "vap_ext_004_poc_dist_63d_ultra": {"inputs": ["close", "volume"], "func": vap_ext_004_poc_dist_63d_ultra},
    "vap_ext_005_poc_below_flag_63d_fine": {"inputs": ["close", "volume"], "func": vap_ext_005_poc_below_flag_63d_fine},
    "vap_ext_006_poc_dist_126d": {"inputs": ["close", "volume"], "func": vap_ext_006_poc_dist_126d},
    "vap_ext_007_poc_fine_vs_coarse_63d": {"inputs": ["close", "volume"], "func": vap_ext_007_poc_fine_vs_coarse_63d},
    "vap_ext_008_poc_dist_21d_pct_rank_126d": {"inputs": ["close", "volume"], "func": vap_ext_008_poc_dist_21d_pct_rank_126d},
    "vap_ext_009_poc_dist_63d_pct_rank_126d": {"inputs": ["close", "volume"], "func": vap_ext_009_poc_dist_63d_pct_rank_126d},
    "vap_ext_010_poc_dist_252d_zscore_expanding": {"inputs": ["close", "volume"], "func": vap_ext_010_poc_dist_252d_zscore_expanding},
    "vap_ext_011_below_va80_low_63d": {"inputs": ["close", "volume"], "func": vap_ext_011_below_va80_low_63d},
    "vap_ext_012_below_va90_low_63d": {"inputs": ["close", "volume"], "func": vap_ext_012_below_va90_low_63d},
    "vap_ext_013_va80_low_dist_63d": {"inputs": ["close", "volume"], "func": vap_ext_013_va80_low_dist_63d},
    "vap_ext_014_va90_low_dist_63d": {"inputs": ["close", "volume"], "func": vap_ext_014_va90_low_dist_63d},
    "vap_ext_015_below_va80_low_252d": {"inputs": ["close", "volume"], "func": vap_ext_015_below_va80_low_252d},
    "vap_ext_016_va80_width_63d": {"inputs": ["close", "volume"], "func": vap_ext_016_va80_width_63d},
    "vap_ext_017_va90_width_252d": {"inputs": ["close", "volume"], "func": vap_ext_017_va90_width_252d},
    "vap_ext_018_price_position_in_va80_63d": {"inputs": ["close", "volume"], "func": vap_ext_018_price_position_in_va80_63d},
    "vap_ext_019_va70_vs_va90_width_ratio_63d": {"inputs": ["close", "volume"], "func": vap_ext_019_va70_vs_va90_width_ratio_63d},
    "vap_ext_020_below_all_va_lows_70_80_90": {"inputs": ["close", "volume"], "func": vap_ext_020_below_all_va_lows_70_80_90},
    "vap_ext_021_vol_decile_pos_21d": {"inputs": ["close", "volume"], "func": vap_ext_021_vol_decile_pos_21d},
    "vap_ext_022_vol_decile_pos_63d": {"inputs": ["close", "volume"], "func": vap_ext_022_vol_decile_pos_63d},
    "vap_ext_023_vol_decile_pos_252d": {"inputs": ["close", "volume"], "func": vap_ext_023_vol_decile_pos_252d},
    "vap_ext_024_vol_decile_below2_63d_flag": {"inputs": ["close", "volume"], "func": vap_ext_024_vol_decile_below2_63d_flag},
    "vap_ext_025_vol_decile_below1_252d_flag": {"inputs": ["close", "volume"], "func": vap_ext_025_vol_decile_below1_252d_flag},
    "vap_ext_026_vol_decile_pos_63d_pct_rank_252d": {"inputs": ["close", "volume"], "func": vap_ext_026_vol_decile_pos_63d_pct_rank_252d},
    "vap_ext_027_vol_decile_spread_21d_252d": {"inputs": ["close", "volume"], "func": vap_ext_027_vol_decile_spread_21d_252d},
    "vap_ext_028_vol_decile_pos_21d_5d_diff": {"inputs": ["close", "volume"], "func": vap_ext_028_vol_decile_pos_21d_5d_diff},
    "vap_ext_029_vol_decile_pos_63d_21d_diff": {"inputs": ["close", "volume"], "func": vap_ext_029_vol_decile_pos_63d_21d_diff},
    "vap_ext_030_vol_decile_pos_252d_min_21d": {"inputs": ["close", "volume"], "func": vap_ext_030_vol_decile_pos_252d_min_21d},
    "vap_ext_031_hvn_gap_above_63d": {"inputs": ["close", "volume"], "func": vap_ext_031_hvn_gap_above_63d},
    "vap_ext_032_hvn_gap_below_63d": {"inputs": ["close", "volume"], "func": vap_ext_032_hvn_gap_below_63d},
    "vap_ext_033_hvn_gap_asymmetry_63d": {"inputs": ["close", "volume"], "func": vap_ext_033_hvn_gap_asymmetry_63d},
    "vap_ext_034_poc_fine_30bin_pct_rank_252d": {"inputs": ["close", "volume"], "func": vap_ext_034_poc_fine_30bin_pct_rank_252d},
    "vap_ext_035_hvn_above_count_252d": {"inputs": ["close", "volume"], "func": vap_ext_035_hvn_above_count_252d},
    "vap_ext_036_hvn_below_count_252d": {"inputs": ["close", "volume"], "func": vap_ext_036_hvn_below_count_252d},
    "vap_ext_037_hvn_above_below_ratio_252d": {"inputs": ["close", "volume"], "func": vap_ext_037_hvn_above_below_ratio_252d},
    "vap_ext_038_hvn_proximity_21d": {"inputs": ["close", "volume"], "func": vap_ext_038_hvn_proximity_21d},
    "vap_ext_039_hvn_concentration_top3_vs_top5_63d": {"inputs": ["close", "volume"], "func": vap_ext_039_hvn_concentration_top3_vs_top5_63d},
    "vap_ext_040_hvn_proximity_252d_pct_rank_expanding": {"inputs": ["close", "volume"], "func": vap_ext_040_hvn_proximity_252d_pct_rank_expanding},
    "vap_ext_041_vwap_dist_5d": {"inputs": ["close", "volume"], "func": vap_ext_041_vwap_dist_5d},
    "vap_ext_042_vwap_dist_5d_pct_rank_63d": {"inputs": ["close", "volume"], "func": vap_ext_042_vwap_dist_5d_pct_rank_63d},
    "vap_ext_043_vwap_band_zscore_126d": {"inputs": ["close", "volume"], "func": vap_ext_043_vwap_band_zscore_126d},
    "vap_ext_044_vwap_band_below_2std_flag_252d": {"inputs": ["close", "volume"], "func": vap_ext_044_vwap_band_below_2std_flag_252d},
    "vap_ext_045_vwap_band_below_3std_flag_63d": {"inputs": ["close", "volume"], "func": vap_ext_045_vwap_band_below_3std_flag_63d},
    "vap_ext_046_vwap_dist_high_21d": {"inputs": ["close", "high", "volume"], "func": vap_ext_046_vwap_dist_high_21d},
    "vap_ext_047_vwap_dist_low_21d": {"inputs": ["close", "low", "volume"], "func": vap_ext_047_vwap_dist_low_21d},
    "vap_ext_048_vwap_dist_252d_zscore_expanding": {"inputs": ["close", "volume"], "func": vap_ext_048_vwap_dist_252d_zscore_expanding},
    "vap_ext_049_vwap_std_63d_pct_rank_252d": {"inputs": ["close", "volume"], "func": vap_ext_049_vwap_std_63d_pct_rank_252d},
    "vap_ext_050_vwap_dist_21d_in_252d_count_below_neg5pct": {"inputs": ["close", "volume"], "func": vap_ext_050_vwap_dist_21d_in_252d_count_below_neg5pct},
    "vap_ext_051_vwap_63d_consec_below_21d_vwap": {"inputs": ["close", "volume"], "func": vap_ext_051_vwap_63d_consec_below_21d_vwap},
    "vap_ext_052_vwap_dist_21d_vs_63d_ratio": {"inputs": ["close", "volume"], "func": vap_ext_052_vwap_dist_21d_vs_63d_ratio},
    "vap_ext_053_overhead_frac_126d": {"inputs": ["close", "volume"], "func": vap_ext_053_overhead_frac_126d},
    "vap_ext_054_overhead_frac_126d_pct_rank_252d": {"inputs": ["close", "volume"], "func": vap_ext_054_overhead_frac_126d_pct_rank_252d},
    "vap_ext_055_overhead_frac_all4_avg": {"inputs": ["close", "volume"], "func": vap_ext_055_overhead_frac_all4_avg},
    "vap_ext_056_vap_entropy_21d": {"inputs": ["close", "volume"], "func": vap_ext_056_vap_entropy_21d},
    "vap_ext_057_vap_entropy_126d": {"inputs": ["close", "volume"], "func": vap_ext_057_vap_entropy_126d},
    "vap_ext_058_vap_entropy_ratio_63d_252d": {"inputs": ["close", "volume"], "func": vap_ext_058_vap_entropy_ratio_63d_252d},
    "vap_ext_059_hvn_vol_concentration_252d": {"inputs": ["close", "volume"], "func": vap_ext_059_hvn_vol_concentration_252d},
    "vap_ext_060_vap_concentration_ratio_63d_252d": {"inputs": ["close", "volume"], "func": vap_ext_060_vap_concentration_ratio_63d_252d},
    "vap_ext_061_vap_distress_score_5dim": {"inputs": ["close", "volume"], "func": vap_ext_061_vap_distress_score_5dim},
    "vap_ext_062_vap_distress_score_pct_rank_252d": {"inputs": ["close", "volume"], "func": vap_ext_062_vap_distress_score_pct_rank_252d},
    "vap_ext_063_overhead_frac_21d_vs_63d_acceleration": {"inputs": ["close", "volume"], "func": vap_ext_063_overhead_frac_21d_vs_63d_acceleration},
    "vap_ext_064_poc_dist_trend_coherence_63d": {"inputs": ["close", "volume"], "func": vap_ext_064_poc_dist_trend_coherence_63d},
    "vap_ext_065_vwap_poc_distance_spread_63d": {"inputs": ["close", "volume"], "func": vap_ext_065_vwap_poc_distance_spread_63d},
    "vap_ext_066_all_distress_signals_flag": {"inputs": ["close", "volume"], "func": vap_ext_066_all_distress_signals_flag},
    "vap_ext_067_va_low_63d_expanding_min": {"inputs": ["close", "volume"], "func": vap_ext_067_va_low_63d_expanding_min},
    "vap_ext_068_poc_63d_expanding_min": {"inputs": ["close", "volume"], "func": vap_ext_068_poc_63d_expanding_min},
    "vap_ext_069_overhead_frac_63d_decay_21d": {"inputs": ["close", "volume"], "func": vap_ext_069_overhead_frac_63d_decay_21d},
    "vap_ext_070_overhead_frac_21d_max_252d": {"inputs": ["close", "volume"], "func": vap_ext_070_overhead_frac_21d_max_252d},
    "vap_ext_071_vwap_dist_21d_max_abs_252d": {"inputs": ["close", "volume"], "func": vap_ext_071_vwap_dist_21d_max_abs_252d},
    "vap_ext_072_poc_dist_21d_consec_neg": {"inputs": ["close", "volume"], "func": vap_ext_072_poc_dist_21d_consec_neg},
    "vap_ext_073_vwap_dist_63d_consec_neg": {"inputs": ["close", "volume"], "func": vap_ext_073_vwap_dist_63d_consec_neg},
    "vap_ext_074_below_vol_frac_252d": {"inputs": ["close", "volume"], "func": vap_ext_074_below_vol_frac_252d},
    "vap_ext_075_vap_ultimate_distress_composite": {"inputs": ["close", "volume"], "func": vap_ext_075_vap_ultimate_distress_composite},
}
