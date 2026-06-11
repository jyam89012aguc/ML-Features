"""
37_range_expansion — Extended 2nd Derivatives (Features extdrv2_001-025)
Domain: rate of change of extended base range-expansion concepts (from
        extended_001_075) — velocity of NR21/WR21 regimes, TR-excess in ATR
        units, down-range component ratios, gap-adjusted ranges, HL-vs-CC
        divergence, range-at-new-low scores, opening-range ratios,
        range-of-ranges dispersion, and volume-confirmed expansion metrics.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
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
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range: max of H-L, |H-prevC|, |L-prevC|."""
    prev_c = close.shift(1)
    return pd.concat([
        high - low,
        (high - prev_c).abs(),
        (low  - prev_c).abs(),
    ], axis=1).max(axis=1)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi   = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        num  = ((xi - xi_m) * (x - x_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        return np.nan if den == 0 else num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Extended 2nd-Derivative Feature Functions ────────────────────────────────
# Each function re-implements the underlying extended-base concept inline,
# then takes its rate of change via 5d/21d diff, pct_change, or OLS slope.

def rex_extdrv2_001_nr21_count_63d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 63-day NR21-count (velocity of deep-contraction clustering)."""
    hl    = high - low
    min21 = hl.rolling(21, min_periods=11).min()
    flag  = (hl <= min21).astype(float)
    cnt   = _rolling_sum(flag, _TD_QTR)
    return cnt.diff(_TD_WEEK)


def rex_extdrv2_002_wr21_count_63d_21d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day WR21-count (monthly velocity of wide-range 21-bar clustering)."""
    hl    = high - low
    max21 = hl.rolling(21, min_periods=11).max()
    flag  = (hl >= max21).astype(float)
    cnt   = _rolling_sum(flag, _TD_QTR)
    return cnt.diff(_TD_MON)


def rex_extdrv2_003_hl_zscore_126d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 126-day HL z-score (short-term velocity of semi-annual range extremity)."""
    hl = high - low
    m  = _rolling_mean(hl, _TD_HALF)
    s  = _rolling_std(hl, _TD_HALF)
    z  = _safe_div(hl - m, s)
    return z.diff(_TD_WEEK)


def rex_extdrv2_004_tr_excess_atr21_units_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of TR-excess-above-ATR21 in ATR21 units (velocity of expansion magnitude)."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    base = _safe_div(tr - atr, atr)
    return base.diff(_TD_WEEK)


def rex_extdrv2_005_tr_excess_atr63_units_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of clipped TR-excess-above-ATR63 in ATR63 units (monthly expansion drift)."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_QTR)
    base = _safe_div(tr - atr, atr).clip(lower=0)
    return base.diff(_TD_MON)


def rex_extdrv2_006_down_range_vs_tr_ratio_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of downside-TR-fraction (velocity of bearish range component shift)."""
    prev_c    = close.shift(1)
    tr        = _tr(close, high, low)
    down_comp = (prev_c - low).clip(lower=0)
    base      = _safe_div(down_comp, tr)
    return base.diff(_TD_WEEK)


def rex_extdrv2_007_down_range_21d_avg_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day average downside TR fraction (short-term bearish drift velocity)."""
    prev_c    = close.shift(1)
    tr        = _tr(close, high, low)
    down_frac = _safe_div((prev_c - low).clip(lower=0), tr)
    base      = _rolling_mean(down_frac, _TD_MON)
    return base.diff(_TD_WEEK)


def rex_extdrv2_008_down_vs_up_range_ratio_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 21-day avg down-component / up-component ratio (monthly bear/bull balance shift)."""
    prev_c    = close.shift(1)
    tr        = _tr(close, high, low)
    down_frac = _safe_div((prev_c - low).clip(lower=0), tr)
    up_frac   = _safe_div((high - prev_c).clip(lower=0), tr)
    base      = _safe_div(_rolling_mean(down_frac, _TD_MON), _rolling_mean(up_frac, _TD_MON))
    return base.diff(_TD_MON)


def rex_extdrv2_009_hl_vs_cc_ratio_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of HL/|CC| ratio (velocity of intraday-vs-overnight range divergence)."""
    hl   = high - low
    cc   = (close - close.shift(1)).abs().replace(0, np.nan)
    base = _safe_div(hl, cc)
    return base.diff(_TD_WEEK)


def rex_extdrv2_010_cc_range_zscore_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day z-score of close-to-close absolute change (CC velocity)."""
    cc   = (close - close.shift(1)).abs()
    m    = _rolling_mean(cc, _TD_MON)
    s    = _rolling_std(cc, _TD_MON)
    base = _safe_div(cc - m, s)
    return base.diff(_TD_WEEK)


def rex_extdrv2_011_range_at_new_low_score_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of range-at-new-low distress score (velocity of capitulation composite)."""
    tr    = _tr(close, high, low)
    atr   = _rolling_mean(tr, _TD_MON)
    ratio = _safe_div(tr, atr)
    lo63  = _rolling_min(close, _TD_QTR)
    hi63  = _rolling_max(close, _TD_QTR)
    rng   = (hi63 - lo63).replace(0, np.nan)
    pos   = ((close - lo63) / rng).clip(0, 1)
    base  = ratio * (1 - pos)
    return base.diff(_TD_WEEK)


def rex_extdrv2_012_range_at_new_low_score_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of range-at-new-low distress score (monthly velocity of capitulation intensity)."""
    tr    = _tr(close, high, low)
    atr   = _rolling_mean(tr, _TD_MON)
    ratio = _safe_div(tr, atr)
    lo63  = _rolling_min(close, _TD_QTR)
    hi63  = _rolling_max(close, _TD_QTR)
    rng   = (hi63 - lo63).replace(0, np.nan)
    pos   = ((close - lo63) / rng).clip(0, 1)
    base  = ratio * (1 - pos)
    return base.diff(_TD_MON)


def rex_extdrv2_013_open_to_low_ratio_atr21_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of (Open-Low)/ATR21 (velocity of downside opening-range expansion)."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    base = _safe_div((open - low).clip(lower=0), atr)
    return base.diff(_TD_WEEK)


def rex_extdrv2_014_open_to_low_21d_avg_slope(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope of 21-day avg (Open-Low)/ATR21 over trailing 63 days (trend in persistent downside ORE)."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    r    = _safe_div((open - low).clip(lower=0), atr)
    base = _rolling_mean(r, _TD_MON)
    return _linslope(base, _TD_QTR)


def rex_extdrv2_015_gap_down_magnitude_avg_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day avg gap-down magnitude (velocity of overnight downside gap regime)."""
    prev_c = close.shift(1)
    gap_dn = (prev_c - open).clip(lower=0)
    base   = _rolling_mean(gap_dn, _TD_MON)
    return base.diff(_TD_WEEK)


def rex_extdrv2_016_overnight_gap_ratio_atr21_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of overnight gap / ATR21 ratio (velocity of gap contribution to vol)."""
    gap  = (open - close.shift(1)).abs()
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    base = _safe_div(gap, atr)
    return base.diff(_TD_WEEK)


def rex_extdrv2_017_range_of_ranges_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day range-of-ranges (velocity of TR dispersion spread)."""
    tr   = _tr(close, high, low)
    base = _rolling_max(tr, _TD_MON) - _rolling_min(tr, _TD_MON)
    return base.diff(_TD_WEEK)


def rex_extdrv2_018_ror_63d_norm_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day normalized range-of-ranges (monthly drift in TR dispersion)."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_QTR)
    ror  = _rolling_max(tr, _TD_QTR) - _rolling_min(tr, _TD_QTR)
    base = _safe_div(ror, atr)
    return base.diff(_TD_MON)


def rex_extdrv2_019_vol_surge_on_expansion_ratio_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of vol-on-expansion / vol-on-non-expansion ratio (velocity of volume differentiation)."""
    tr      = _tr(close, high, low)
    atr     = _rolling_mean(tr, _TD_MON)
    is_exp  = tr > atr
    v_exp   = volume.where(is_exp,  np.nan).rolling(_TD_MON, min_periods=1).mean()
    v_no    = volume.where(~is_exp, np.nan).rolling(_TD_MON, min_periods=1).mean()
    base    = _safe_div(v_exp, v_no)
    return base.diff(_TD_WEEK)


def rex_extdrv2_020_vol_weighted_tr_zscore_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day volume-weighted TR z-score (velocity of VW-TR extremity)."""
    tr   = _tr(close, high, low)
    vwtr = _safe_div(tr * volume, _rolling_mean(volume, _TD_QTR))
    m    = _rolling_mean(vwtr, _TD_QTR)
    s    = _rolling_std(vwtr, _TD_QTR)
    base = _safe_div(vwtr - m, s)
    return base.diff(_TD_WEEK)


def rex_extdrv2_021_bearish_expansion_down_zscore_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of bearish-expansion downside z-score (velocity of downside range extremity)."""
    prev_c    = close.shift(1)
    down_comp = (prev_c - low).clip(lower=0)
    m    = _rolling_mean(down_comp, _TD_QTR)
    s    = _rolling_std(down_comp, _TD_QTR)
    base = _safe_div(down_comp - m, s)
    return base.diff(_TD_WEEK)


def rex_extdrv2_022_close_lower_half_expansion_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day count of bearish expansion days (monthly drift in bearish pressure count)."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    mid  = (high + low) / 2.0
    flag = ((tr > atr) & (close < mid)).astype(float)
    base = _rolling_sum(flag, _TD_QTR)
    return base.diff(_TD_MON)


def rex_extdrv2_023_tr_pct_rank_126d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 126-day TR percentile rank (velocity of semi-annual rank movement)."""
    tr   = _tr(close, high, low)
    base = tr.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)
    return base.diff(_TD_WEEK)


def rex_extdrv2_024_high_vol_bearish_score_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of high-vol bearish expansion composite score (velocity of capitulation intensity)."""
    tr     = _tr(close, high, low)
    atr    = _rolling_mean(tr, _TD_MON)
    avg_v  = _rolling_mean(volume, _TD_MON)
    hl     = (high - low).replace(0, np.nan)
    pos    = (close - low) / hl
    tr_r   = _safe_div(tr, atr)
    vol_r  = _safe_div(volume, avg_v)
    bear_r = (1 - pos.clip(0, 1))
    base   = tr_r * vol_r * bear_r
    return base.diff(_TD_WEEK)


def rex_extdrv2_025_hl_minus_cc_avg_in_atr_slope(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of 21-day avg (HL minus |CC|)/ATR21 over trailing 63 days (trend in intraday excess)."""
    hl   = high - low
    cc   = (close - close.shift(1)).abs()
    diff = (hl - cc).clip(lower=0)
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    base = _safe_div(_rolling_mean(diff, _TD_MON), atr)
    return _linslope(base, _TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

RANGE_EXPANSION_EXTENDED_REGISTRY_2ND_DERIVATIVES = {
    "rex_extdrv2_001_nr21_count_63d_5d_diff": {"inputs": ["high", "low"], "func": rex_extdrv2_001_nr21_count_63d_5d_diff},
    "rex_extdrv2_002_wr21_count_63d_21d_diff": {"inputs": ["high", "low"], "func": rex_extdrv2_002_wr21_count_63d_21d_diff},
    "rex_extdrv2_003_hl_zscore_126d_5d_diff": {"inputs": ["high", "low"], "func": rex_extdrv2_003_hl_zscore_126d_5d_diff},
    "rex_extdrv2_004_tr_excess_atr21_units_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv2_004_tr_excess_atr21_units_5d_diff},
    "rex_extdrv2_005_tr_excess_atr63_units_21d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv2_005_tr_excess_atr63_units_21d_diff},
    "rex_extdrv2_006_down_range_vs_tr_ratio_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv2_006_down_range_vs_tr_ratio_5d_diff},
    "rex_extdrv2_007_down_range_21d_avg_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv2_007_down_range_21d_avg_5d_diff},
    "rex_extdrv2_008_down_vs_up_range_ratio_21d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv2_008_down_vs_up_range_ratio_21d_diff},
    "rex_extdrv2_009_hl_vs_cc_ratio_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv2_009_hl_vs_cc_ratio_5d_diff},
    "rex_extdrv2_010_cc_range_zscore_21d_5d_diff": {"inputs": ["close"], "func": rex_extdrv2_010_cc_range_zscore_21d_5d_diff},
    "rex_extdrv2_011_range_at_new_low_score_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv2_011_range_at_new_low_score_5d_diff},
    "rex_extdrv2_012_range_at_new_low_score_21d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv2_012_range_at_new_low_score_21d_diff},
    "rex_extdrv2_013_open_to_low_ratio_atr21_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": rex_extdrv2_013_open_to_low_ratio_atr21_5d_diff},
    "rex_extdrv2_014_open_to_low_21d_avg_slope": {"inputs": ["close", "high", "low", "open"], "func": rex_extdrv2_014_open_to_low_21d_avg_slope},
    "rex_extdrv2_015_gap_down_magnitude_avg_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": rex_extdrv2_015_gap_down_magnitude_avg_5d_diff},
    "rex_extdrv2_016_overnight_gap_ratio_atr21_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": rex_extdrv2_016_overnight_gap_ratio_atr21_5d_diff},
    "rex_extdrv2_017_range_of_ranges_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv2_017_range_of_ranges_21d_5d_diff},
    "rex_extdrv2_018_ror_63d_norm_21d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv2_018_ror_63d_norm_21d_diff},
    "rex_extdrv2_019_vol_surge_on_expansion_ratio_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": rex_extdrv2_019_vol_surge_on_expansion_ratio_5d_diff},
    "rex_extdrv2_020_vol_weighted_tr_zscore_63d_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": rex_extdrv2_020_vol_weighted_tr_zscore_63d_5d_diff},
    "rex_extdrv2_021_bearish_expansion_down_zscore_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv2_021_bearish_expansion_down_zscore_5d_diff},
    "rex_extdrv2_022_close_lower_half_expansion_63d_21d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv2_022_close_lower_half_expansion_63d_21d_diff},
    "rex_extdrv2_023_tr_pct_rank_126d_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv2_023_tr_pct_rank_126d_5d_diff},
    "rex_extdrv2_024_high_vol_bearish_score_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": rex_extdrv2_024_high_vol_bearish_score_5d_diff},
    "rex_extdrv2_025_hl_minus_cc_avg_in_atr_slope": {"inputs": ["close", "high", "low"], "func": rex_extdrv2_025_hl_minus_cc_avg_in_atr_slope},
}
