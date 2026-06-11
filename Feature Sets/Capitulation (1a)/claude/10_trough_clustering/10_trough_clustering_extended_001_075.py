"""
10_trough_clustering — Extended Features ext_001-075
Domain: density of local minima, repeated bottoms — additional depth.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features backward-looking only; no forward information.
Net-new vs existing 200: histogram entropy of trough-price distribution;
distinct cluster counting; retest depth below support; quadruple-bottom patterns;
EWM-volume at troughs; trough-age exponential weighting; inter-trough returns;
absolute support-floor level; volume entropy; trough IQR/skewness/kurtosis;
open-to-low gap at trough; candle-shadow metrics on trough bars; HL-midpoint
distance from floor; basing low skewness; support hold fraction; z-score and
pct-rank transforms on novel composite windows; cross-timeframe density ratios
at windows 3/7/15/30-bar (not covered by existing 5/10/21/63-bar set);
support-break depth z-score; volume-weighted trough-price at 504d; and
trough-cluster volume entropy.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()

def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()

def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()

def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()

def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))

def _local_min_flag(low: pd.Series, w: int) -> pd.Series:
    """Backward-only local-minimum flag: low[t] == rolling_min(low,w)[t]."""
    rmin = low.rolling(w, min_periods=max(1, w // 2)).min()
    return (low <= rmin + _EPS).astype(float)

# ── Extended scalar helpers (raw=True, return scalar) ────────────────────────

def _entropy_raw(x, n_bins=10):
    if len(x) < 2:
        return np.nan
    rng = np.max(x) - np.min(x)
    if rng < _EPS:
        return 0.0
    counts, _ = np.histogram(x, bins=n_bins)
    tot = counts.sum()
    if tot == 0:
        return np.nan
    probs = counts[counts > 0] / tot
    return float(-np.sum(probs * np.log(probs + _EPS)))

def _trough_skew_raw(x):
    if len(x) < 3:
        return np.nan
    mn = np.min(x)
    near = x[x <= mn * 1.05 + _EPS]
    if len(near) < 3:
        return np.nan
    m = np.mean(near); s = np.std(near)
    if s < _EPS:
        return 0.0
    return float(np.mean(((near - m) / s) ** 3))

def _trough_kurt_raw(x):
    if len(x) < 4:
        return np.nan
    mn = np.min(x)
    near = x[x <= mn * 1.05 + _EPS]
    if len(near) < 4:
        return np.nan
    m = np.mean(near); s = np.std(near)
    if s < _EPS:
        return np.nan
    return float(np.mean(((near - m) / s) ** 4) - 3.0)

def _distinct_clusters_raw(x, band_pct):
    if len(x) < 2:
        return np.nan
    mn = np.min(x)
    pts = np.sort(x[x <= mn * (1.0 + band_pct) + _EPS])
    if len(pts) == 0:
        return 0.0
    clusters = 1; anchor = pts[0]
    for p in pts[1:]:
        if p > anchor * (1.0 + band_pct) + _EPS:
            clusters += 1; anchor = p
    return float(clusters)

def _retest_depth_raw(x, band_pct):
    if len(x) < 2:
        return np.nan
    mn = np.min(x)
    support = mn * (1.0 + band_pct)
    below = x[x < support - _EPS]
    if len(below) == 0:
        return 0.0
    return float(np.mean((support - below) / (support + _EPS)))

def _support_hold_frac_raw(x, band_pct=0.03):
    if len(x) < 2:
        return np.nan
    mn = np.min(x)
    in_band = x[x <= mn * (1.0 + band_pct) + _EPS]
    if len(in_band) == 0:
        return np.nan
    hold = float(np.sum(in_band > mn + _EPS))
    return hold / len(in_band)

def _quad_bottom_raw(x, band_pct=0.02, min_sep=5):
    if len(x) < 20:
        return np.nan
    mn = np.min(x)
    idxs = np.where(x <= mn * (1.0 + band_pct) + _EPS)[0]
    if len(idxs) < 2:
        return 0.0
    groups = [idxs[0]]
    for i in idxs[1:]:
        if i - groups[-1] >= min_sep:
            groups.append(i)
    return float(len(groups))

def _inter_trough_return_raw(x):
    if len(x) < 4:
        return np.nan
    mn = np.min(x)
    idxs = np.where(x <= mn * 1.03 + _EPS)[0]
    if len(idxs) < 2:
        return np.nan
    prices = x[idxs]
    rets = np.abs(np.diff(prices) / (prices[:-1] + _EPS))
    return float(np.mean(rets))

def _trough_iqr_norm_raw(x):
    if len(x) < 4:
        return np.nan
    mn = np.min(x)
    near = x[x <= mn * 1.05 + _EPS]
    if len(near) < 4:
        return np.nan
    iqr = float(np.percentile(near, 75) - np.percentile(near, 25))
    if mn < _EPS:
        return np.nan
    return iqr / mn

def _last_trough_bars_ago_raw(x):
    if len(x) == 0:
        return np.nan
    mn = np.min(x)
    idxs = np.where(x <= mn * 1.01 + _EPS)[0]
    if len(idxs) == 0:
        return np.nan
    return float(len(x) - 1 - idxs[-1])

def _age_decay_count_raw(x, halflife):
    n = len(x)
    ages = np.arange(n - 1, -1, -1, dtype=float)
    weights = np.exp(-ages / halflife)
    return float(np.sum(x * weights))

def _vol_entropy_raw(x, n_bins=8):
    if len(x) < 2:
        return np.nan
    total = np.sum(x)
    if total < _EPS:
        return np.nan
    counts, _ = np.histogram(x, bins=n_bins)
    tot = counts.sum()
    probs = counts[counts > 0] / tot
    return float(-np.sum(probs * np.log(probs + _EPS)))

def _max_nontrough_run_raw(x):
    if len(x) < 2:
        return np.nan
    best = cur = 0
    for v in x:
        if v < 0.5:
            cur += 1; best = max(best, cur)
        else:
            cur = 0
    return float(best)

def _full_skew_raw(x):
    if len(x) < 3:
        return np.nan
    m = np.mean(x); s = np.std(x)
    if s < _EPS:
        return 0.0
    return float(np.mean(((x - m) / s) ** 3))

def _trough_spacing_std_raw(x):
    idxs = np.where(x > 0.5)[0]
    if len(idxs) < 3:
        return np.nan
    gaps = np.diff(idxs.astype(float))
    return float(np.std(gaps))

# ── Feature functions ext_001-075 ─────────────────────────────────────────────

# --- Group A (001-010): Local-min density at windows NOT in existing 200 ---
# Existing covers: 5-bar (many), 10-bar, 21-bar, 63-bar local-min flags.
# We add: 3-bar, 7-bar, 15-bar, 30-bar.

def tcl_ext_001_local_min_count_3bar_21d(low: pd.Series) -> pd.Series:
    """Count of 3-bar local-min flags within trailing 21 days."""
    return _rolling_sum(_local_min_flag(low, 3), _TD_MON)

def tcl_ext_002_local_min_count_3bar_63d(low: pd.Series) -> pd.Series:
    """Count of 3-bar local-min flags within trailing 63 days."""
    return _rolling_sum(_local_min_flag(low, 3), _TD_QTR)

def tcl_ext_003_local_min_count_3bar_252d(low: pd.Series) -> pd.Series:
    """Count of 3-bar local-min flags within trailing 252 days."""
    return _rolling_sum(_local_min_flag(low, 3), _TD_YEAR)

def tcl_ext_004_local_min_count_7bar_63d(low: pd.Series) -> pd.Series:
    """Count of 7-bar local-min flags within trailing 63 days."""
    return _rolling_sum(_local_min_flag(low, 7), _TD_QTR)

def tcl_ext_005_local_min_count_7bar_252d(low: pd.Series) -> pd.Series:
    """Count of 7-bar local-min flags within trailing 252 days."""
    return _rolling_sum(_local_min_flag(low, 7), _TD_YEAR)

def tcl_ext_006_local_min_count_15bar_126d(low: pd.Series) -> pd.Series:
    """Count of 15-bar local-min flags within trailing 126 days."""
    return _rolling_sum(_local_min_flag(low, 15), _TD_HALF)

def tcl_ext_007_local_min_count_15bar_252d(low: pd.Series) -> pd.Series:
    """Count of 15-bar local-min flags within trailing 252 days."""
    return _rolling_sum(_local_min_flag(low, 15), _TD_YEAR)

def tcl_ext_008_local_min_count_30bar_126d(low: pd.Series) -> pd.Series:
    """Count of 30-bar local-min flags within trailing 126 days."""
    return _rolling_sum(_local_min_flag(low, 30), _TD_HALF)

def tcl_ext_009_local_min_count_30bar_252d(low: pd.Series) -> pd.Series:
    """Count of 30-bar local-min flags within trailing 252 days."""
    return _rolling_sum(_local_min_flag(low, 30), _TD_YEAR)

def tcl_ext_010_local_min_3bar_vs_30bar_ratio_63d(low: pd.Series) -> pd.Series:
    """Ratio of 3-bar to 30-bar local-min counts in 63d (micro vs macro density)."""
    c3  = _rolling_sum(_local_min_flag(low, 3),  _TD_QTR)
    c30 = _rolling_sum(_local_min_flag(low, 30), _TD_QTR)
    return _safe_div(c3, c30)

# --- Group B (011-019): Trough-price histogram entropy, skewness, kurtosis, IQR ---

def tcl_ext_011_trough_price_entropy_63d(low: pd.Series) -> pd.Series:
    """Shannon entropy of low-price histogram in 63d (dispersed vs clustered)."""
    return low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _entropy_raw, raw=True)

def tcl_ext_012_trough_price_entropy_252d(low: pd.Series) -> pd.Series:
    """Shannon entropy of low-price histogram in 252d."""
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _entropy_raw, raw=True)

def tcl_ext_013_trough_price_skewness_126d(low: pd.Series) -> pd.Series:
    """Skewness of trough prices (near 5% of 126d min) — tail asymmetry."""
    return low.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        _trough_skew_raw, raw=True)

def tcl_ext_014_trough_price_skewness_252d(low: pd.Series) -> pd.Series:
    """Skewness of trough prices (near 5% of 252d min)."""
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _trough_skew_raw, raw=True)

def tcl_ext_015_trough_price_kurtosis_252d(low: pd.Series) -> pd.Series:
    """Excess kurtosis of trough prices in 252d (peakedness of support cluster)."""
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _trough_kurt_raw, raw=True)

def tcl_ext_016_trough_price_iqr_norm_63d(low: pd.Series) -> pd.Series:
    """IQR of near-trough prices / window min in 63d (robust basing spread)."""
    return low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _trough_iqr_norm_raw, raw=True)

def tcl_ext_017_trough_price_iqr_norm_252d(low: pd.Series) -> pd.Series:
    """IQR of near-trough prices / window min in 252d."""
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _trough_iqr_norm_raw, raw=True)

def tcl_ext_018_basing_low_skewness_252d(low: pd.Series) -> pd.Series:
    """Skewness of full 252d low distribution (negative = fat left tail / capitulation)."""
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _full_skew_raw, raw=True)

def tcl_ext_019_trough_entropy_zscore_252d(low: pd.Series) -> pd.Series:
    """Z-score of 63d trough-price entropy vs its 252d rolling mean/std."""
    ent = low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _entropy_raw, raw=True)
    return _safe_div(ent - _rolling_mean(ent, _TD_YEAR), _rolling_std(ent, _TD_YEAR))

# --- Group C (020-028): Distinct cluster count and support zone strength ---

def tcl_ext_020_trough_price_q10_norm_252d(low: pd.Series) -> pd.Series:
    """
    10th percentile of 252d lows normalized by the 252d minimum.
    Measures where the deepest price cluster sits relative to the floor.
    Higher = bulk of lows cluster well above the absolute minimum.
    """
    def _q10(x):
        if len(x) < 4: return np.nan
        mn = np.min(x)
        if mn < _EPS: return np.nan
        return float(np.percentile(x, 10) / mn)
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_q10, raw=True)

def tcl_ext_021_trough_price_q90_norm_252d(low: pd.Series) -> pd.Series:
    """
    90th percentile of 252d lows normalized by the 252d minimum.
    High ratio = wide spread of lows (scattered); low = tight clustering.
    """
    def _q90(x):
        if len(x) < 4: return np.nan
        mn = np.min(x)
        if mn < _EPS: return np.nan
        return float(np.percentile(x, 90) / mn)
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_q90, raw=True)

def tcl_ext_022_trough_price_q10_norm_126d(low: pd.Series) -> pd.Series:
    """10th percentile of 126d lows normalized by the 126d minimum."""
    def _q10(x):
        if len(x) < 4: return np.nan
        mn = np.min(x)
        if mn < _EPS: return np.nan
        return float(np.percentile(x, 10) / mn)
    return low.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(_q10, raw=True)

def tcl_ext_023_support_hold_frac_63d(low: pd.Series) -> pd.Series:
    """Fraction of support-band touches where low holds above absolute minimum (63d)."""
    return low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _support_hold_frac_raw, raw=True)

def tcl_ext_024_support_hold_frac_252d(low: pd.Series) -> pd.Series:
    """Fraction of support-band touches where low holds above absolute minimum (252d)."""
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _support_hold_frac_raw, raw=True)

def tcl_ext_025_retest_depth_1pct_63d(low: pd.Series) -> pd.Series:
    """Mean fractional depth below 1%-support band on breach days in 63d."""
    def _rd(x): return _retest_depth_raw(x, 0.01)
    return low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_rd, raw=True)

def tcl_ext_026_retest_depth_3pct_252d(low: pd.Series) -> pd.Series:
    """Mean fractional depth below 3%-support band on breach days in 252d."""
    def _rd(x): return _retest_depth_raw(x, 0.03)
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_rd, raw=True)

def tcl_ext_027_support_zone_abs_level_252d(low: pd.Series) -> pd.Series:
    """Absolute price of the 252d rolling minimum (support floor in $ terms)."""
    return _rolling_min(low, _TD_YEAR)

def tcl_ext_028_support_zone_abs_level_126d(low: pd.Series) -> pd.Series:
    """Absolute price of the 126d rolling minimum."""
    return _rolling_min(low, _TD_HALF)

# --- Group D (029-037): Quadruple-bottom and multi-touch at novel separations ---

def tcl_ext_029_quad_bottom_score_63d(low: pd.Series) -> pd.Series:
    """Count distinct trough-touch groups (2% band, 3-bar sep) in 63d."""
    def _qb(x): return _quad_bottom_raw(x, 0.02, 3)
    return low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_qb, raw=True)

def tcl_ext_030_quad_bottom_score_126d(low: pd.Series) -> pd.Series:
    """Count distinct trough-touch groups (2% band, 5-bar sep) in 126d."""
    def _qb(x): return _quad_bottom_raw(x, 0.02, 5)
    return low.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(_qb, raw=True)

def tcl_ext_031_quad_bottom_score_252d(low: pd.Series) -> pd.Series:
    """Count distinct trough-touch groups (3% band, 5-bar sep) in 252d."""
    def _qb(x): return _quad_bottom_raw(x, 0.03, 5)
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_qb, raw=True)

def tcl_ext_032_multi_touch_ge3_flag_126d(low: pd.Series) -> pd.Series:
    """Binary: 1 if quad_bottom_score_126d >= 3 (triple+ confirmed)."""
    return (tcl_ext_030_quad_bottom_score_126d(low) >= 3.0).astype(float)

def tcl_ext_033_multi_touch_ge4_flag_252d(low: pd.Series) -> pd.Series:
    """Binary: 1 if quad_bottom_score_252d >= 4 (quadruple confirmed)."""
    return (tcl_ext_031_quad_bottom_score_252d(low) >= 4.0).astype(float)

def tcl_ext_034_trough_price_std_vs_mean_126d(low: pd.Series) -> pd.Series:
    """
    Std of ALL 126d lows divided by their mean (full-window CV, not just near-trough).
    Distinct from existing trough_price_cv_63d/252d which restricts to bars
    within 3% of the minimum. This uses the entire 126d low distribution.
    """
    return _safe_div(_rolling_std(low, _TD_HALF), _rolling_mean(low, _TD_HALF))

def tcl_ext_035_triple_bottom_sep10_126d(low: pd.Series) -> pd.Series:
    """Binary: >=3 touch groups (2% band, 10-bar sep) in 126d."""
    def _tb10(x):
        s = _quad_bottom_raw(x, 0.02, 10)
        return np.nan if np.isnan(s) else float(s >= 3.0)
    return low.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(_tb10, raw=True)

def tcl_ext_036_touch_acceleration_126d(low: pd.Series) -> pd.Series:
    """Difference: quad_bottom_score_63d minus score from prior 63d (acceleration)."""
    s126 = tcl_ext_030_quad_bottom_score_126d(low)
    s63  = tcl_ext_029_quad_bottom_score_63d(low)
    return s63 - s126.shift(_TD_QTR).fillna(0.0)

def tcl_ext_037_close_multi_touch_252d(close: pd.Series) -> pd.Series:
    """Count distinct close-price trough groups (2% band, 5-bar sep) in 252d."""
    def _qbc(x): return _quad_bottom_raw(x, 0.02, 5)
    return close.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_qbc, raw=True)

# --- Group E (038-047): Trough age, exponential recency, inter-trough returns ---

def tcl_ext_038_trough_age_decay_count_63d(low: pd.Series) -> pd.Series:
    """Exp-decay weighted trough count 63d: weight=exp(-age/21), recent > old."""
    flag = _local_min_flag(low, 5)
    def _aw(x): return _age_decay_count_raw(x, _TD_MON)
    return flag.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_aw, raw=True)

def tcl_ext_039_trough_age_decay_count_252d(low: pd.Series) -> pd.Series:
    """Exp-decay weighted trough count 252d: weight=exp(-age/63)."""
    flag = _local_min_flag(low, 5)
    def _aw(x): return _age_decay_count_raw(x, _TD_QTR)
    return flag.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_aw, raw=True)

def tcl_ext_040_last_trough_bars_ago_63d(low: pd.Series) -> pd.Series:
    """Bars from end of 63d window to most recent trough touch (recency in bars)."""
    return low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _last_trough_bars_ago_raw, raw=True)

def tcl_ext_041_last_trough_bars_ago_252d(low: pd.Series) -> pd.Series:
    """Bars from end of 252d window to most recent trough touch."""
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _last_trough_bars_ago_raw, raw=True)

def tcl_ext_042_inter_trough_return_126d(low: pd.Series) -> pd.Series:
    """Mean abs return between successive trough prices in 126d."""
    return low.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        _inter_trough_return_raw, raw=True)

def tcl_ext_043_inter_trough_return_252d(low: pd.Series) -> pd.Series:
    """Mean abs return between successive trough prices in 252d."""
    return low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _inter_trough_return_raw, raw=True)

def tcl_ext_044_close_age_decay_count_252d(close: pd.Series) -> pd.Series:
    """Exp-decay close-based trough count 252d: weight=exp(-age/63)."""
    flag = _local_min_flag(close, 5)
    def _aw(x): return _age_decay_count_raw(x, _TD_QTR)
    return flag.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_aw, raw=True)

def tcl_ext_045_trough_recency_linear_7bar_63d(low: pd.Series) -> pd.Series:
    """Linear recency score: 7-bar flag weighted by position/window in 63d."""
    flag = _local_min_flag(low, 7)
    def _lw(x):
        n = len(x)
        weights = np.arange(1, n + 1, dtype=float) / n
        return float(np.sum(x * weights))
    return flag.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_lw, raw=True)

def tcl_ext_046_max_inter_trough_gap_7bar_63d(low: pd.Series) -> pd.Series:
    """Maximum gap between consecutive 7-bar trough flags in 63d."""
    flag = _local_min_flag(low, 7)
    def _mg(x):
        idxs = np.where(x > 0.5)[0]
        if len(idxs) < 2: return np.nan
        return float(np.max(np.diff(idxs.astype(float))))
    return flag.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_mg, raw=True)

def tcl_ext_047_trough_spacing_std_7bar_252d(low: pd.Series) -> pd.Series:
    """Std of gap between consecutive 7-bar trough flags in 252d."""
    flag = _local_min_flag(low, 7)
    return flag.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _trough_spacing_std_raw, raw=True)

# --- Group F (048-056): Volume entropy, EWM-volume at troughs, novel combos ---

def tcl_ext_048_volume_ewm_at_troughs_63d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM(span=21) of volume masked to local-min days (smoothed trough volume)."""
    return _ewm_mean(_local_min_flag(low, 5) * volume, _TD_MON)

def tcl_ext_049_volume_ewm_at_troughs_126d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """EWM(span=63) of volume on local-min days."""
    return _ewm_mean(_local_min_flag(low, 5) * volume, _TD_QTR)

def tcl_ext_050_volume_entropy_63d(volume: pd.Series) -> pd.Series:
    """Shannon entropy of volume distribution in 63d."""
    return volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _vol_entropy_raw, raw=True)

def tcl_ext_051_volume_entropy_252d(volume: pd.Series) -> pd.Series:
    """Shannon entropy of volume distribution in 252d."""
    return volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _vol_entropy_raw, raw=True)

def tcl_ext_052_volume_concentration_near_low_126d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 126d volume in bars within 2% of 126d low."""
    rmin = _rolling_min(low, _TD_HALF)
    near = (low <= rmin * 1.02 + _EPS).astype(float)
    return _safe_div(_rolling_sum(near * volume, _TD_HALF), _rolling_sum(volume, _TD_HALF))

def tcl_ext_053_high_vol_trough_fraction_63d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of trough days with above-average (rolling mean) volume in 63d."""
    flag    = _local_min_flag(low, 5)
    vol_avg = _rolling_mean(volume, _TD_QTR)
    both    = flag * (volume >= vol_avg).astype(float)
    cnt_t   = _rolling_sum(flag, _TD_QTR).replace(0, np.nan)
    return _rolling_sum(both, _TD_QTR) / cnt_t

def tcl_ext_054_vwap_trough_price_504d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted avg low within 3% of 504d low (2yr support floor VWAP)."""
    rmin = low.rolling(504, min_periods=252).min()
    near = (low <= rmin * 1.03 + _EPS).astype(float)
    wt   = near * volume
    return _safe_div(
        _rolling_sum(wt * low, 504),
        _rolling_sum(wt, 504)
    )

def tcl_ext_055_trough_vol_spike_score_252d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean z-score of volume on local-min days vs 252d distribution (climax selling)."""
    flag    = _local_min_flag(low, 5)
    vol_z   = _safe_div(volume - _rolling_mean(volume, _TD_YEAR),
                        _rolling_std(volume, _TD_YEAR))
    cnt     = _rolling_sum(flag, _TD_YEAR).replace(0, np.nan)
    return _rolling_sum(vol_z * flag, _TD_YEAR) / cnt

def tcl_ext_056_trough_cluster_vol_entropy_252d(low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume entropy restricted to bars within 3% of 252d low (climax vs diffuse)."""
    rmin    = _rolling_min(low, _TD_YEAR)
    near    = (low <= rmin * 1.03 + _EPS).astype(float)
    tvol    = near * volume
    return tvol.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _vol_entropy_raw, raw=True)

# --- Group G (057-064): Open/midpoint/shadow metrics on trough bars ---

def tcl_ext_057_open_to_low_gap_at_trough_63d(low: pd.Series, open: pd.Series) -> pd.Series:
    """Mean (open-low).clip(0)/open on local-min days in 63d (gap-down on trough bar)."""
    flag     = _local_min_flag(low, 5)
    gap_norm = _safe_div((open - low).clip(lower=0.0), open.replace(0, np.nan))
    return _rolling_mean(gap_norm * flag, _TD_QTR)

def tcl_ext_058_open_to_low_gap_at_trough_252d(low: pd.Series, open: pd.Series) -> pd.Series:
    """Mean (open-low).clip(0)/open on local-min days in 252d."""
    flag     = _local_min_flag(low, 5)
    gap_norm = _safe_div((open - low).clip(lower=0.0), open.replace(0, np.nan))
    return _rolling_mean(gap_norm * flag, _TD_YEAR)

def tcl_ext_059_hl_midpoint_vs_252d_low_63d(low: pd.Series, high: pd.Series) -> pd.Series:
    """Mean (midpoint - 252d_floor) / 252d_floor in 63d (bars' midpoint distance from floor)."""
    mid   = (high + low) / 2.0
    floor = _rolling_min(low, _TD_YEAR)
    return _rolling_mean(_safe_div(mid - floor, floor), _TD_QTR)

def tcl_ext_060_hl_midpoint_vs_252d_low_21d(low: pd.Series, high: pd.Series) -> pd.Series:
    """Mean (midpoint - 252d_floor) / 252d_floor in 21d."""
    mid   = (high + low) / 2.0
    floor = _rolling_min(low, _TD_YEAR)
    return _rolling_mean(_safe_div(mid - floor, floor), _TD_MON)

def tcl_ext_061_candle_body_on_trough_bars_252d(
        low: pd.Series, open: pd.Series, close: pd.Series) -> pd.Series:
    """Mean |close-open|/low on trough bars in 252d (body size at capitulation)."""
    flag     = _local_min_flag(low, 5)
    body_pct = _safe_div((close - open).abs(), low.replace(0, np.nan))
    return _rolling_mean(body_pct * flag, _TD_YEAR)

def tcl_ext_062_upper_shadow_at_trough_252d(
        low: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Mean upper shadow (high-close).clip(0)/low on trough bars in 252d."""
    flag       = _local_min_flag(low, 5)
    shadow_pct = _safe_div((high - close).clip(lower=0.0), low.replace(0, np.nan))
    return _rolling_mean(shadow_pct * flag, _TD_YEAR)

def tcl_ext_063_lower_shadow_at_trough_252d(
        low: pd.Series, open: pd.Series, close: pd.Series) -> pd.Series:
    """Mean lower shadow (min(open,close)-low).clip(0)/low on trough bars in 252d."""
    flag       = _local_min_flag(low, 5)
    body_bot   = pd.concat([open, close], axis=1).min(axis=1)
    shadow_pct = _safe_div((body_bot - low).clip(lower=0.0), low.replace(0, np.nan))
    return _rolling_mean(shadow_pct * flag, _TD_YEAR)

def tcl_ext_064_close_vs_hl_mid_at_trough_252d(
        low: pd.Series, high: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (close-midpoint)/(high-low) on trough bars in 252d (close position in range)."""
    flag = _local_min_flag(low, 5)
    mid  = (high + low) / 2.0
    rng  = (high - low).replace(0, np.nan)
    pos  = (close - mid) / rng
    return _rolling_mean(pos * flag, _TD_YEAR)

# --- Group H (065-070): Statistical transforms at novel windows ---

def tcl_ext_065_local_min_7bar_zscore_252d(low: pd.Series) -> pd.Series:
    """Z-score of 63d 7-bar local-min count vs its 252d rolling mean/std."""
    cnt = _rolling_sum(_local_min_flag(low, 7), _TD_QTR)
    return _safe_div(cnt - _rolling_mean(cnt, _TD_YEAR), _rolling_std(cnt, _TD_YEAR))

def tcl_ext_066_troughs_2pct_126d_pctrank_252d(low: pd.Series) -> pd.Series:
    """Pct-rank of 126d within-2pct trough count within 252d rolling history."""
    def _cnt(x):
        if len(x) == 0: return np.nan
        mn = np.min(x)
        return float(np.sum(x <= mn * 1.02 + _EPS))
    cnt = low.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(_cnt, raw=True)
    return cnt.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)

def tcl_ext_067_retest_depth_zscore_252d(low: pd.Series) -> pd.Series:
    """Z-score of 63d retest-depth-below-3pct-support vs 252d history."""
    depth = low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda x: _retest_depth_raw(x, 0.03), raw=True)
    return _safe_div(depth - _rolling_mean(depth, _TD_YEAR), _rolling_std(depth, _TD_YEAR))

def tcl_ext_068_trough_iqr_pctrank_252d(low: pd.Series) -> pd.Series:
    """Pct-rank of 63d trough IQR (normalized) within 252d rolling distribution."""
    iqr = low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _trough_iqr_norm_raw, raw=True)
    return iqr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)

def tcl_ext_069_local_min_30bar_pctrank_252d(low: pd.Series) -> pd.Series:
    """Pct-rank of 126d 30-bar local-min count within 252d history."""
    cnt = _rolling_sum(_local_min_flag(low, 30), _TD_HALF)
    return cnt.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)

def tcl_ext_070_trough_count_3bar_pctrank_252d(low: pd.Series) -> pd.Series:
    """Pct-rank of 63d 3-bar local-min count within 252d history."""
    cnt = _rolling_sum(_local_min_flag(low, 3), _TD_QTR)
    return cnt.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)

# --- Group I (071-075): Cross-timeframe and basing structure features ---

def tcl_ext_071_local_min_7bar_vs_21bar_ratio_252d(low: pd.Series) -> pd.Series:
    """Ratio of 7-bar to 21-bar local-min counts in 252d (fine vs coarse density)."""
    c7  = _rolling_sum(_local_min_flag(low, 7),  _TD_YEAR)
    c21 = _rolling_sum(_local_min_flag(low, 21), _TD_YEAR)
    return _safe_div(c7, c21)

def tcl_ext_072_max_nontrough_run_63d(low: pd.Series) -> pd.Series:
    """Max consecutive non-trough bars in 63d (longest gap without basing activity)."""
    flag = _local_min_flag(low, 5)
    return flag.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _max_nontrough_run_raw, raw=True)

def tcl_ext_073_trough_count_504d_3pct(low: pd.Series) -> pd.Series:
    """Count of bars within 3% of 504d low (2yr support cluster density)."""
    def _cnt(x):
        if len(x) == 0: return np.nan
        mn = np.min(x)
        return float(np.sum(x <= mn * 1.03 + _EPS))
    return low.rolling(504, min_periods=252).apply(_cnt, raw=True)

def tcl_ext_074_trough_count_3bar_vs_30bar_pctrank(low: pd.Series) -> pd.Series:
    """Pct-rank of (3-bar / 30-bar count ratio in 63d) within 252d history."""
    ratio = tcl_ext_010_local_min_3bar_vs_30bar_ratio_63d(low)
    return ratio.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)

def tcl_ext_075_trough_vol_ratio_trough_nontrough_126d(
        low: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio mean volume on trough days vs non-trough days in 126d."""
    flag    = _local_min_flag(low, 5)
    nonflag = 1.0 - flag
    cnt_t   = _rolling_sum(flag,    _TD_HALF).replace(0, np.nan)
    cnt_n   = _rolling_sum(nonflag, _TD_HALF).replace(0, np.nan)
    mean_t  = _rolling_sum(flag    * volume, _TD_HALF) / cnt_t
    mean_n  = _rolling_sum(nonflag * volume, _TD_HALF) / cnt_n
    return _safe_div(mean_t, mean_n)

# ── Registry ──────────────────────────────────────────────────────────────────

TROUGH_CLUSTERING_EXTENDED_REGISTRY_001_075 = {
    "tcl_ext_001_local_min_count_3bar_21d":          {"inputs": ["low"],                    "func": tcl_ext_001_local_min_count_3bar_21d},
    "tcl_ext_002_local_min_count_3bar_63d":          {"inputs": ["low"],                    "func": tcl_ext_002_local_min_count_3bar_63d},
    "tcl_ext_003_local_min_count_3bar_252d":         {"inputs": ["low"],                    "func": tcl_ext_003_local_min_count_3bar_252d},
    "tcl_ext_004_local_min_count_7bar_63d":          {"inputs": ["low"],                    "func": tcl_ext_004_local_min_count_7bar_63d},
    "tcl_ext_005_local_min_count_7bar_252d":         {"inputs": ["low"],                    "func": tcl_ext_005_local_min_count_7bar_252d},
    "tcl_ext_006_local_min_count_15bar_126d":        {"inputs": ["low"],                    "func": tcl_ext_006_local_min_count_15bar_126d},
    "tcl_ext_007_local_min_count_15bar_252d":        {"inputs": ["low"],                    "func": tcl_ext_007_local_min_count_15bar_252d},
    "tcl_ext_008_local_min_count_30bar_126d":        {"inputs": ["low"],                    "func": tcl_ext_008_local_min_count_30bar_126d},
    "tcl_ext_009_local_min_count_30bar_252d":        {"inputs": ["low"],                    "func": tcl_ext_009_local_min_count_30bar_252d},
    "tcl_ext_010_local_min_3bar_vs_30bar_ratio_63d": {"inputs": ["low"],                    "func": tcl_ext_010_local_min_3bar_vs_30bar_ratio_63d},
    "tcl_ext_011_trough_price_entropy_63d":          {"inputs": ["low"],                    "func": tcl_ext_011_trough_price_entropy_63d},
    "tcl_ext_012_trough_price_entropy_252d":         {"inputs": ["low"],                    "func": tcl_ext_012_trough_price_entropy_252d},
    "tcl_ext_013_trough_price_skewness_126d":        {"inputs": ["low"],                    "func": tcl_ext_013_trough_price_skewness_126d},
    "tcl_ext_014_trough_price_skewness_252d":        {"inputs": ["low"],                    "func": tcl_ext_014_trough_price_skewness_252d},
    "tcl_ext_015_trough_price_kurtosis_252d":        {"inputs": ["low"],                    "func": tcl_ext_015_trough_price_kurtosis_252d},
    "tcl_ext_016_trough_price_iqr_norm_63d":         {"inputs": ["low"],                    "func": tcl_ext_016_trough_price_iqr_norm_63d},
    "tcl_ext_017_trough_price_iqr_norm_252d":        {"inputs": ["low"],                    "func": tcl_ext_017_trough_price_iqr_norm_252d},
    "tcl_ext_018_basing_low_skewness_252d":          {"inputs": ["low"],                    "func": tcl_ext_018_basing_low_skewness_252d},
    "tcl_ext_019_trough_entropy_zscore_252d":        {"inputs": ["low"],                    "func": tcl_ext_019_trough_entropy_zscore_252d},
    "tcl_ext_020_trough_price_q10_norm_252d":        {"inputs": ["low"],                    "func": tcl_ext_020_trough_price_q10_norm_252d},
    "tcl_ext_021_trough_price_q90_norm_252d":        {"inputs": ["low"],                    "func": tcl_ext_021_trough_price_q90_norm_252d},
    "tcl_ext_022_trough_price_q10_norm_126d":        {"inputs": ["low"],                    "func": tcl_ext_022_trough_price_q10_norm_126d},
    "tcl_ext_023_support_hold_frac_63d":             {"inputs": ["low"],                    "func": tcl_ext_023_support_hold_frac_63d},
    "tcl_ext_024_support_hold_frac_252d":            {"inputs": ["low"],                    "func": tcl_ext_024_support_hold_frac_252d},
    "tcl_ext_025_retest_depth_1pct_63d":             {"inputs": ["low"],                    "func": tcl_ext_025_retest_depth_1pct_63d},
    "tcl_ext_026_retest_depth_3pct_252d":            {"inputs": ["low"],                    "func": tcl_ext_026_retest_depth_3pct_252d},
    "tcl_ext_027_support_zone_abs_level_252d":       {"inputs": ["low"],                    "func": tcl_ext_027_support_zone_abs_level_252d},
    "tcl_ext_028_support_zone_abs_level_126d":       {"inputs": ["low"],                    "func": tcl_ext_028_support_zone_abs_level_126d},
    "tcl_ext_029_quad_bottom_score_63d":             {"inputs": ["low"],                    "func": tcl_ext_029_quad_bottom_score_63d},
    "tcl_ext_030_quad_bottom_score_126d":            {"inputs": ["low"],                    "func": tcl_ext_030_quad_bottom_score_126d},
    "tcl_ext_031_quad_bottom_score_252d":            {"inputs": ["low"],                    "func": tcl_ext_031_quad_bottom_score_252d},
    "tcl_ext_032_multi_touch_ge3_flag_126d":         {"inputs": ["low"],                    "func": tcl_ext_032_multi_touch_ge3_flag_126d},
    "tcl_ext_033_multi_touch_ge4_flag_252d":         {"inputs": ["low"],                    "func": tcl_ext_033_multi_touch_ge4_flag_252d},
    "tcl_ext_034_trough_price_std_vs_mean_126d":     {"inputs": ["low"],                    "func": tcl_ext_034_trough_price_std_vs_mean_126d},
    "tcl_ext_035_triple_bottom_sep10_126d":          {"inputs": ["low"],                    "func": tcl_ext_035_triple_bottom_sep10_126d},
    "tcl_ext_036_touch_acceleration_126d":           {"inputs": ["low"],                    "func": tcl_ext_036_touch_acceleration_126d},
    "tcl_ext_037_close_multi_touch_252d":            {"inputs": ["close"],                  "func": tcl_ext_037_close_multi_touch_252d},
    "tcl_ext_038_trough_age_decay_count_63d":        {"inputs": ["low"],                    "func": tcl_ext_038_trough_age_decay_count_63d},
    "tcl_ext_039_trough_age_decay_count_252d":       {"inputs": ["low"],                    "func": tcl_ext_039_trough_age_decay_count_252d},
    "tcl_ext_040_last_trough_bars_ago_63d":          {"inputs": ["low"],                    "func": tcl_ext_040_last_trough_bars_ago_63d},
    "tcl_ext_041_last_trough_bars_ago_252d":         {"inputs": ["low"],                    "func": tcl_ext_041_last_trough_bars_ago_252d},
    "tcl_ext_042_inter_trough_return_126d":          {"inputs": ["low"],                    "func": tcl_ext_042_inter_trough_return_126d},
    "tcl_ext_043_inter_trough_return_252d":          {"inputs": ["low"],                    "func": tcl_ext_043_inter_trough_return_252d},
    "tcl_ext_044_close_age_decay_count_252d":        {"inputs": ["close"],                  "func": tcl_ext_044_close_age_decay_count_252d},
    "tcl_ext_045_trough_recency_linear_7bar_63d":    {"inputs": ["low"],                    "func": tcl_ext_045_trough_recency_linear_7bar_63d},
    "tcl_ext_046_max_inter_trough_gap_7bar_63d":     {"inputs": ["low"],                    "func": tcl_ext_046_max_inter_trough_gap_7bar_63d},
    "tcl_ext_047_trough_spacing_std_7bar_252d":      {"inputs": ["low"],                    "func": tcl_ext_047_trough_spacing_std_7bar_252d},
    "tcl_ext_048_volume_ewm_at_troughs_63d":         {"inputs": ["low", "volume"],          "func": tcl_ext_048_volume_ewm_at_troughs_63d},
    "tcl_ext_049_volume_ewm_at_troughs_126d":        {"inputs": ["low", "volume"],          "func": tcl_ext_049_volume_ewm_at_troughs_126d},
    "tcl_ext_050_volume_entropy_63d":                {"inputs": ["volume"],                 "func": tcl_ext_050_volume_entropy_63d},
    "tcl_ext_051_volume_entropy_252d":               {"inputs": ["volume"],                 "func": tcl_ext_051_volume_entropy_252d},
    "tcl_ext_052_volume_concentration_near_low_126d":{"inputs": ["low", "volume"],          "func": tcl_ext_052_volume_concentration_near_low_126d},
    "tcl_ext_053_high_vol_trough_fraction_63d":      {"inputs": ["low", "volume"],          "func": tcl_ext_053_high_vol_trough_fraction_63d},
    "tcl_ext_054_vwap_trough_price_504d":            {"inputs": ["low", "volume"],          "func": tcl_ext_054_vwap_trough_price_504d},
    "tcl_ext_055_trough_vol_spike_score_252d":       {"inputs": ["low", "volume"],          "func": tcl_ext_055_trough_vol_spike_score_252d},
    "tcl_ext_056_trough_cluster_vol_entropy_252d":   {"inputs": ["low", "volume"],          "func": tcl_ext_056_trough_cluster_vol_entropy_252d},
    "tcl_ext_057_open_to_low_gap_at_trough_63d":     {"inputs": ["low", "open"],            "func": tcl_ext_057_open_to_low_gap_at_trough_63d},
    "tcl_ext_058_open_to_low_gap_at_trough_252d":    {"inputs": ["low", "open"],            "func": tcl_ext_058_open_to_low_gap_at_trough_252d},
    "tcl_ext_059_hl_midpoint_vs_252d_low_63d":       {"inputs": ["low", "high"],            "func": tcl_ext_059_hl_midpoint_vs_252d_low_63d},
    "tcl_ext_060_hl_midpoint_vs_252d_low_21d":       {"inputs": ["low", "high"],            "func": tcl_ext_060_hl_midpoint_vs_252d_low_21d},
    "tcl_ext_061_candle_body_on_trough_bars_252d":   {"inputs": ["low", "open", "close"],   "func": tcl_ext_061_candle_body_on_trough_bars_252d},
    "tcl_ext_062_upper_shadow_at_trough_252d":       {"inputs": ["low", "high", "close"],   "func": tcl_ext_062_upper_shadow_at_trough_252d},
    "tcl_ext_063_lower_shadow_at_trough_252d":       {"inputs": ["low", "open", "close"],   "func": tcl_ext_063_lower_shadow_at_trough_252d},
    "tcl_ext_064_close_vs_hl_mid_at_trough_252d":    {"inputs": ["low", "high", "close"],   "func": tcl_ext_064_close_vs_hl_mid_at_trough_252d},
    "tcl_ext_065_local_min_7bar_zscore_252d":        {"inputs": ["low"],                    "func": tcl_ext_065_local_min_7bar_zscore_252d},
    "tcl_ext_066_troughs_2pct_126d_pctrank_252d":    {"inputs": ["low"],                    "func": tcl_ext_066_troughs_2pct_126d_pctrank_252d},
    "tcl_ext_067_retest_depth_zscore_252d":          {"inputs": ["low"],                    "func": tcl_ext_067_retest_depth_zscore_252d},
    "tcl_ext_068_trough_iqr_pctrank_252d":           {"inputs": ["low"],                    "func": tcl_ext_068_trough_iqr_pctrank_252d},
    "tcl_ext_069_local_min_30bar_pctrank_252d":      {"inputs": ["low"],                    "func": tcl_ext_069_local_min_30bar_pctrank_252d},
    "tcl_ext_070_trough_count_3bar_pctrank_252d":    {"inputs": ["low"],                    "func": tcl_ext_070_trough_count_3bar_pctrank_252d},
    "tcl_ext_071_local_min_7bar_vs_21bar_ratio_252d":{"inputs": ["low"],                    "func": tcl_ext_071_local_min_7bar_vs_21bar_ratio_252d},
    "tcl_ext_072_max_nontrough_run_63d":             {"inputs": ["low"],                    "func": tcl_ext_072_max_nontrough_run_63d},
    "tcl_ext_073_trough_count_504d_3pct":            {"inputs": ["low"],                    "func": tcl_ext_073_trough_count_504d_3pct},
    "tcl_ext_074_trough_count_3bar_vs_30bar_pctrank":{"inputs": ["low"],                    "func": tcl_ext_074_trough_count_3bar_vs_30bar_pctrank},
    "tcl_ext_075_trough_vol_ratio_trough_nontrough_126d": {"inputs": ["low", "volume"],     "func": tcl_ext_075_trough_vol_ratio_trough_nontrough_126d},
}
