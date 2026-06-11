"""
37_range_expansion — Extended 3rd Derivatives (Features extdrv3_001-025)
Domain: rate of change of extended 2nd-derivative concepts — acceleration of
        velocity in NR21/WR21 regime dynamics, TR-excess-in-ATR velocity,
        down-range component drift, HL-vs-CC divergence shift, range-at-new-low
        momentum, opening-range velocity, range-of-ranges dispersion curvature,
        and volume-confirmed expansion jerk.
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


# ── Extended 3rd-Derivative Feature Functions ────────────────────────────────
# Each function re-implements the underlying 2nd-derivative concept inline,
# then takes a further diff/slope (second diff, slope-of-slope, or diff-of-slope).

def rex_extdrv3_001_nr21_count_63d_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day NR21-count velocity (acceleration of deep-contraction clustering)."""
    hl    = high - low
    min21 = hl.rolling(21, min_periods=11).min()
    flag  = (hl <= min21).astype(float)
    cnt   = _rolling_sum(flag, _TD_QTR)
    vel   = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_extdrv3_002_wr21_count_63d_21d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of 63-day WR21-count (jerk in wide-range 21-bar clustering)."""
    hl    = high - low
    max21 = hl.rolling(21, min_periods=11).max()
    flag  = (hl >= max21).astype(float)
    cnt   = _rolling_sum(flag, _TD_QTR)
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rex_extdrv3_003_hl_zscore_126d_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 126-day HL z-score (acceleration of semi-annual range extremity velocity)."""
    hl  = high - low
    m   = _rolling_mean(hl, _TD_HALF)
    s   = _rolling_std(hl, _TD_HALF)
    z   = _safe_div(hl - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_extdrv3_004_tr_excess_atr21_units_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of TR-excess-in-ATR21-units (acceleration of expansion magnitude velocity)."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    base = _safe_div(tr - atr, atr)
    vel  = base.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_extdrv3_005_tr_excess_atr63_units_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in TR-excess-above-ATR63 (jerk in medium-term expansion drift)."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_QTR)
    base = _safe_div(tr - atr, atr).clip(lower=0)
    vel  = base.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def rex_extdrv3_006_down_range_vs_tr_ratio_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of downside-TR-fraction (acceleration of bearish range component shift)."""
    prev_c    = close.shift(1)
    tr        = _tr(close, high, low)
    down_comp = (prev_c - low).clip(lower=0)
    base      = _safe_div(down_comp, tr)
    vel       = base.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_extdrv3_007_down_range_21d_avg_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day avg downside TR fraction (acceleration of sustained bearish drift)."""
    prev_c    = close.shift(1)
    tr        = _tr(close, high, low)
    down_frac = _safe_div((prev_c - low).clip(lower=0), tr)
    base      = _rolling_mean(down_frac, _TD_MON)
    vel       = base.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_extdrv3_008_down_vs_up_range_ratio_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in down/up-range ratio (jerk in bear/bull balance)."""
    prev_c    = close.shift(1)
    tr        = _tr(close, high, low)
    down_frac = _safe_div((prev_c - low).clip(lower=0), tr)
    up_frac   = _safe_div((high - prev_c).clip(lower=0), tr)
    base      = _safe_div(_rolling_mean(down_frac, _TD_MON), _rolling_mean(up_frac, _TD_MON))
    vel21     = base.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rex_extdrv3_009_hl_vs_cc_ratio_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of HL/|CC| ratio (acceleration of intraday-vs-overnight divergence)."""
    hl   = high - low
    cc   = (close - close.shift(1)).abs().replace(0, np.nan)
    base = _safe_div(hl, cc)
    vel  = base.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_extdrv3_010_cc_zscore_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day CC z-score (acceleration of close-to-close extremity velocity)."""
    cc   = (close - close.shift(1)).abs()
    m    = _rolling_mean(cc, _TD_MON)
    s    = _rolling_std(cc, _TD_MON)
    base = _safe_div(cc - m, s)
    vel  = base.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_extdrv3_011_range_at_new_low_score_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of range-at-new-low distress score (acceleration of capitulation composite)."""
    tr    = _tr(close, high, low)
    atr   = _rolling_mean(tr, _TD_MON)
    ratio = _safe_div(tr, atr)
    lo63  = _rolling_min(close, _TD_QTR)
    hi63  = _rolling_max(close, _TD_QTR)
    rng   = (hi63 - lo63).replace(0, np.nan)
    pos   = ((close - lo63) / rng).clip(0, 1)
    base  = ratio * (1 - pos)
    vel   = base.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_extdrv3_012_range_at_new_low_score_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in range-at-new-low distress score (jerk in capitulation monthly trend)."""
    tr    = _tr(close, high, low)
    atr   = _rolling_mean(tr, _TD_MON)
    ratio = _safe_div(tr, atr)
    lo63  = _rolling_min(close, _TD_QTR)
    hi63  = _rolling_max(close, _TD_QTR)
    rng   = (hi63 - lo63).replace(0, np.nan)
    pos   = ((close - lo63) / rng).clip(0, 1)
    base  = ratio * (1 - pos)
    vel21 = base.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def rex_extdrv3_013_open_to_low_ratio_atr21_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of (Open-Low)/ATR21 (acceleration of downside opening-range expansion velocity)."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    base = _safe_div((open - low).clip(lower=0), atr)
    vel  = base.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_extdrv3_014_open_to_low_21d_avg_slope_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day avg (Open-Low)/ATR21 over 63d (acceleration of ORE trend)."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    r    = _safe_div((open - low).clip(lower=0), atr)
    base = _rolling_mean(r, _TD_MON)
    slp  = _linslope(base, _TD_QTR)
    return slp.diff(_TD_WEEK)


def rex_extdrv3_015_gap_down_magnitude_avg_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day avg gap-down magnitude (acceleration of overnight gap regime)."""
    prev_c = close.shift(1)
    gap_dn = (prev_c - open).clip(lower=0)
    base   = _rolling_mean(gap_dn, _TD_MON)
    vel    = base.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_extdrv3_016_overnight_gap_ratio_atr21_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of overnight gap / ATR21 (acceleration of gap-to-vol contribution)."""
    gap  = (open - close.shift(1)).abs()
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    base = _safe_div(gap, atr)
    vel  = base.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_extdrv3_017_range_of_ranges_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day range-of-ranges (acceleration of TR dispersion spread)."""
    tr   = _tr(close, high, low)
    base = _rolling_max(tr, _TD_MON) - _rolling_min(tr, _TD_MON)
    vel  = base.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_extdrv3_018_ror_63d_norm_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day normalized range-of-ranges (jerk in dispersion monthly drift)."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_QTR)
    ror  = _rolling_max(tr, _TD_QTR) - _rolling_min(tr, _TD_QTR)
    base = _safe_div(ror, atr)
    vel  = base.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def rex_extdrv3_019_vol_surge_expansion_ratio_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of vol-on-expansion / vol-on-non-expansion ratio (acceleration of vol differentiation)."""
    tr      = _tr(close, high, low)
    atr     = _rolling_mean(tr, _TD_MON)
    is_exp  = tr > atr
    v_exp   = volume.where(is_exp,  np.nan).rolling(_TD_MON, min_periods=1).mean()
    v_no    = volume.where(~is_exp, np.nan).rolling(_TD_MON, min_periods=1).mean()
    base    = _safe_div(v_exp, v_no)
    vel     = base.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_extdrv3_020_vol_weighted_tr_zscore_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day volume-weighted TR z-score (acceleration of VW-TR extremity)."""
    tr   = _tr(close, high, low)
    vwtr = _safe_div(tr * volume, _rolling_mean(volume, _TD_QTR))
    m    = _rolling_mean(vwtr, _TD_QTR)
    s    = _rolling_std(vwtr, _TD_QTR)
    base = _safe_div(vwtr - m, s)
    vel  = base.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_extdrv3_021_bearish_expansion_down_zscore_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of bearish-expansion downside z-score (acceleration of downside range extremity)."""
    prev_c    = close.shift(1)
    down_comp = (prev_c - low).clip(lower=0)
    m    = _rolling_mean(down_comp, _TD_QTR)
    s    = _rolling_std(down_comp, _TD_QTR)
    base = _safe_div(down_comp - m, s)
    vel  = base.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_extdrv3_022_close_lower_half_expansion_63d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day bearish expansion count (jerk in bearish pressure count)."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    mid  = (high + low) / 2.0
    flag = ((tr > atr) & (close < mid)).astype(float)
    base = _rolling_sum(flag, _TD_QTR)
    vel  = base.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def rex_extdrv3_023_tr_pct_rank_126d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 126-day TR percentile rank (acceleration of semi-annual rank velocity)."""
    tr   = _tr(close, high, low)
    base = tr.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)
    vel  = base.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_extdrv3_024_high_vol_bearish_score_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of high-vol bearish expansion composite (acceleration of capitulation intensity)."""
    tr     = _tr(close, high, low)
    atr    = _rolling_mean(tr, _TD_MON)
    avg_v  = _rolling_mean(volume, _TD_MON)
    hl     = (high - low).replace(0, np.nan)
    pos    = (close - low) / hl
    tr_r   = _safe_div(tr, atr)
    vol_r  = _safe_div(volume, avg_v)
    bear_r = (1 - pos.clip(0, 1))
    base   = tr_r * vol_r * bear_r
    vel    = base.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_extdrv3_025_hl_minus_cc_avg_in_atr_slope_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day avg (HL minus |CC|)/ATR21 over 63d (jerk in intraday excess trend)."""
    hl   = high - low
    cc   = (close - close.shift(1)).abs()
    diff = (hl - cc).clip(lower=0)
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    base = _safe_div(_rolling_mean(diff, _TD_MON), atr)
    slp  = _linslope(base, _TD_QTR)
    return slp.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

RANGE_EXPANSION_EXTENDED_REGISTRY_3RD_DERIVATIVES = {
    "rex_extdrv3_001_nr21_count_63d_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": rex_extdrv3_001_nr21_count_63d_5d_diff_5d_diff},
    "rex_extdrv3_002_wr21_count_63d_21d_diff_5d_diff": {"inputs": ["high", "low"], "func": rex_extdrv3_002_wr21_count_63d_21d_diff_5d_diff},
    "rex_extdrv3_003_hl_zscore_126d_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": rex_extdrv3_003_hl_zscore_126d_5d_diff_5d_diff},
    "rex_extdrv3_004_tr_excess_atr21_units_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv3_004_tr_excess_atr21_units_5d_diff_5d_diff},
    "rex_extdrv3_005_tr_excess_atr63_units_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv3_005_tr_excess_atr63_units_21d_diff_5d_diff},
    "rex_extdrv3_006_down_range_vs_tr_ratio_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv3_006_down_range_vs_tr_ratio_5d_diff_5d_diff},
    "rex_extdrv3_007_down_range_21d_avg_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv3_007_down_range_21d_avg_5d_diff_5d_diff},
    "rex_extdrv3_008_down_vs_up_range_ratio_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv3_008_down_vs_up_range_ratio_21d_diff_5d_diff},
    "rex_extdrv3_009_hl_vs_cc_ratio_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv3_009_hl_vs_cc_ratio_5d_diff_5d_diff},
    "rex_extdrv3_010_cc_zscore_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": rex_extdrv3_010_cc_zscore_21d_5d_diff_5d_diff},
    "rex_extdrv3_011_range_at_new_low_score_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv3_011_range_at_new_low_score_5d_diff_5d_diff},
    "rex_extdrv3_012_range_at_new_low_score_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv3_012_range_at_new_low_score_21d_diff_5d_diff},
    "rex_extdrv3_013_open_to_low_ratio_atr21_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": rex_extdrv3_013_open_to_low_ratio_atr21_5d_diff_5d_diff},
    "rex_extdrv3_014_open_to_low_21d_avg_slope_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": rex_extdrv3_014_open_to_low_21d_avg_slope_5d_diff},
    "rex_extdrv3_015_gap_down_magnitude_avg_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": rex_extdrv3_015_gap_down_magnitude_avg_5d_diff_5d_diff},
    "rex_extdrv3_016_overnight_gap_ratio_atr21_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": rex_extdrv3_016_overnight_gap_ratio_atr21_5d_diff_5d_diff},
    "rex_extdrv3_017_range_of_ranges_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv3_017_range_of_ranges_21d_5d_diff_5d_diff},
    "rex_extdrv3_018_ror_63d_norm_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv3_018_ror_63d_norm_21d_diff_5d_diff},
    "rex_extdrv3_019_vol_surge_expansion_ratio_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": rex_extdrv3_019_vol_surge_expansion_ratio_5d_diff_5d_diff},
    "rex_extdrv3_020_vol_weighted_tr_zscore_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": rex_extdrv3_020_vol_weighted_tr_zscore_5d_diff_5d_diff},
    "rex_extdrv3_021_bearish_expansion_down_zscore_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv3_021_bearish_expansion_down_zscore_5d_diff_5d_diff},
    "rex_extdrv3_022_close_lower_half_expansion_63d_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv3_022_close_lower_half_expansion_63d_21d_diff_5d_diff},
    "rex_extdrv3_023_tr_pct_rank_126d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv3_023_tr_pct_rank_126d_5d_diff_5d_diff},
    "rex_extdrv3_024_high_vol_bearish_score_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": rex_extdrv3_024_high_vol_bearish_score_5d_diff_5d_diff},
    "rex_extdrv3_025_hl_minus_cc_avg_in_atr_slope_5d_diff": {"inputs": ["close", "high", "low"], "func": rex_extdrv3_025_hl_minus_cc_avg_in_atr_slope_5d_diff},
}
