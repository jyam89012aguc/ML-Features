"""
77_valuation_collapse — Base Features 001-100
Domain: PE/PB/PS/EV-multiple compression to extremes — the COLLAPSE EVENT itself.
Inputs: Sharadar DAILY/METRICS valuation fields (daily frequency):
    marketcap, ev, pe, pb, ps, evebit, evebitda, divyield
These are native daily-frequency series (price moves daily; fundamental denominator
steps quarterly). No quarterly forward-fill alignment is needed here.
All feature functions are backward-looking only — no negative shifts, no future info.
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
    """Element-wise division; zero or NaN denominator → NaN."""
    d = den.replace(0, np.nan)
    return num / d


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _expanding_max(s: pd.Series) -> pd.Series:
    return s.expanding(min_periods=1).max()


def _expanding_min(s: pd.Series) -> pd.Series:
    return s.expanding(min_periods=1).min()


def _positive_mask(s: pd.Series) -> pd.Series:
    """Return s where s > 0, else NaN (guard for meaningful multiples)."""
    return s.where(s > 0)


def _negative_flag(s: pd.Series) -> pd.Series:
    """1.0 where s < 0 (negative multiple = distress signal), else 0."""
    return (s < 0).astype(float)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope of s over w periods (scalar return per window)."""
    def _slope(x):
        n = len(x)
        if n < max(2, w // 2):
            return np.nan
        xi   = np.arange(n, dtype=float)
        xi_m = xi.mean()
        xm   = x.mean()
        num  = ((xi - xi_m) * (x - xm)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=False)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): PE collapse — drawdown, thresholds, lows ---

def vcl_001_pe_drawdown_from_252d_peak(pe: pd.Series) -> pd.Series:
    """PE ratio drawdown from its trailing 252-day peak (only when PE positive)."""
    p = _positive_mask(pe)
    peak = _rolling_max(p, _TD_YEAR)
    return _safe_div(p - peak, peak)


def vcl_002_pe_drawdown_from_504d_peak(pe: pd.Series) -> pd.Series:
    """PE ratio drawdown from trailing 504-day peak."""
    p = _positive_mask(pe)
    peak = _rolling_max(p, 504)
    return _safe_div(p - peak, peak)


def vcl_003_pe_drawdown_from_1260d_peak(pe: pd.Series) -> pd.Series:
    """PE ratio drawdown from trailing 1260-day (5-year) peak."""
    p = _positive_mask(pe)
    peak = _rolling_max(p, 1260)
    return _safe_div(p - peak, peak)


def vcl_004_pe_drawdown_from_expanding_peak(pe: pd.Series) -> pd.Series:
    """PE ratio drawdown from all-history expanding peak."""
    p = _positive_mask(pe)
    peak = _expanding_max(p)
    return _safe_div(p - peak, peak)


def vcl_005_pe_below_5_flag(pe: pd.Series) -> pd.Series:
    """Binary: PE > 0 and PE < 5 (deep-value distress threshold)."""
    return ((pe > 0) & (pe < 5)).astype(float)


def vcl_006_pe_below_10_flag(pe: pd.Series) -> pd.Series:
    """Binary: PE > 0 and PE < 10."""
    return ((pe > 0) & (pe < 10)).astype(float)


def vcl_007_pe_negative_flag(pe: pd.Series) -> pd.Series:
    """Binary: PE < 0 (negative earnings — distress signal)."""
    return _negative_flag(pe)


def vcl_008_pe_at_252d_low(pe: pd.Series) -> pd.Series:
    """1 if current PE equals the 252-day rolling minimum (at a new 1-year low)."""
    p = _positive_mask(pe)
    lo = _rolling_min(p, _TD_YEAR)
    return (p <= lo + _EPS).astype(float)


def vcl_009_pe_at_1260d_low(pe: pd.Series) -> pd.Series:
    """1 if current positive PE is at or below the 5-year rolling minimum."""
    p = _positive_mask(pe)
    lo = _rolling_min(p, 1260)
    return (p <= lo + _EPS).astype(float)


def vcl_010_pe_pct_above_252d_min(pe: pd.Series) -> pd.Series:
    """Percent by which current PE exceeds its 252-day minimum (0 = at the low)."""
    p = _positive_mask(pe)
    lo = _rolling_min(p, _TD_YEAR)
    return _safe_div(p - lo, lo)


def vcl_011_pe_consecutive_compression_weeks(pe: pd.Series) -> pd.Series:
    """Rolling count of consecutive 5-day periods where PE declined (compression run)."""
    weekly_diff = pe.diff(_TD_WEEK)
    declining = (weekly_diff < 0).astype(float)
    # Rolling sum over 252 days — number of 5d windows where PE declined
    return _rolling_sum(declining, _TD_YEAR)


def vcl_012_pe_compression_magnitude_63d(pe: pd.Series) -> pd.Series:
    """Absolute drop in positive PE over 63 trading days (quarterly multiple compression)."""
    p = _positive_mask(pe)
    return p - p.shift(_TD_QTR)


# --- Group B (013-024): PB collapse ---

def vcl_013_pb_drawdown_from_252d_peak(pb: pd.Series) -> pd.Series:
    """PB ratio drawdown from trailing 252-day peak."""
    p = _positive_mask(pb)
    peak = _rolling_max(p, _TD_YEAR)
    return _safe_div(p - peak, peak)


def vcl_014_pb_drawdown_from_504d_peak(pb: pd.Series) -> pd.Series:
    """PB ratio drawdown from trailing 504-day peak."""
    p = _positive_mask(pb)
    peak = _rolling_max(p, 504)
    return _safe_div(p - peak, peak)


def vcl_015_pb_drawdown_from_expanding_peak(pb: pd.Series) -> pd.Series:
    """PB drawdown from all-history expanding peak."""
    p = _positive_mask(pb)
    peak = _expanding_max(p)
    return _safe_div(p - peak, peak)


def vcl_016_pb_below_1_flag(pb: pd.Series) -> pd.Series:
    """Binary: PB < 1 (trading below book value — classic distress threshold)."""
    return ((pb > 0) & (pb < 1.0)).astype(float)


def vcl_017_pb_below_0_75_flag(pb: pd.Series) -> pd.Series:
    """Binary: PB < 0.75 (deep distress — severe below-book territory)."""
    return ((pb > 0) & (pb < 0.75)).astype(float)


def vcl_018_pb_negative_flag(pb: pd.Series) -> pd.Series:
    """Binary: PB < 0 (negative book value — extreme financial stress)."""
    return _negative_flag(pb)


def vcl_019_pb_at_1260d_low(pb: pd.Series) -> pd.Series:
    """1 if positive PB is at or below its 5-year rolling minimum."""
    p = _positive_mask(pb)
    lo = _rolling_min(p, 1260)
    return (p <= lo + _EPS).astype(float)


def vcl_020_pb_pct_above_252d_min(pb: pd.Series) -> pd.Series:
    """Percent by which PB exceeds its 252-day minimum."""
    p = _positive_mask(pb)
    lo = _rolling_min(p, _TD_YEAR)
    return _safe_div(p - lo, lo)


def vcl_021_pb_compression_magnitude_63d(pb: pd.Series) -> pd.Series:
    """Absolute drop in positive PB over 63 trading days."""
    p = _positive_mask(pb)
    return p - p.shift(_TD_QTR)


def vcl_022_pb_compression_magnitude_252d(pb: pd.Series) -> pd.Series:
    """Absolute drop in positive PB over 252 trading days (annual de-rating)."""
    p = _positive_mask(pb)
    return p - p.shift(_TD_YEAR)


def vcl_023_pb_below_1_consecutive_days(pb: pd.Series) -> pd.Series:
    """Rolling 252-day count of days where PB < 1 (persistence of distress)."""
    flag = ((pb > 0) & (pb < 1.0)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def vcl_024_pb_below_1_fraction_252d(pb: pd.Series) -> pd.Series:
    """Fraction of last 252 days where PB < 1."""
    flag = ((pb > 0) & (pb < 1.0)).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


# --- Group C (025-036): PS collapse ---

def vcl_025_ps_drawdown_from_252d_peak(ps: pd.Series) -> pd.Series:
    """PS ratio drawdown from trailing 252-day peak."""
    p = _positive_mask(ps)
    peak = _rolling_max(p, _TD_YEAR)
    return _safe_div(p - peak, peak)


def vcl_026_ps_drawdown_from_504d_peak(ps: pd.Series) -> pd.Series:
    """PS ratio drawdown from trailing 504-day peak."""
    p = _positive_mask(ps)
    peak = _rolling_max(p, 504)
    return _safe_div(p - peak, peak)


def vcl_027_ps_drawdown_from_1260d_peak(ps: pd.Series) -> pd.Series:
    """PS ratio drawdown from trailing 1260-day peak."""
    p = _positive_mask(ps)
    peak = _rolling_max(p, 1260)
    return _safe_div(p - peak, peak)


def vcl_028_ps_drawdown_from_expanding_peak(ps: pd.Series) -> pd.Series:
    """PS drawdown from all-history expanding peak."""
    p = _positive_mask(ps)
    peak = _expanding_max(p)
    return _safe_div(p - peak, peak)


def vcl_029_ps_below_1_flag(ps: pd.Series) -> pd.Series:
    """Binary: PS < 1 (price below annual revenue — deep-value territory)."""
    return ((ps > 0) & (ps < 1.0)).astype(float)


def vcl_030_ps_below_0_5_flag(ps: pd.Series) -> pd.Series:
    """Binary: PS < 0.5 (extreme price-to-sales compression)."""
    return ((ps > 0) & (ps < 0.5)).astype(float)


def vcl_031_ps_at_252d_low(ps: pd.Series) -> pd.Series:
    """1 if current PS is at its 252-day rolling minimum."""
    p = _positive_mask(ps)
    lo = _rolling_min(p, _TD_YEAR)
    return (p <= lo + _EPS).astype(float)


def vcl_032_ps_compression_magnitude_252d(ps: pd.Series) -> pd.Series:
    """Absolute drop in positive PS over 252 days."""
    p = _positive_mask(ps)
    return p - p.shift(_TD_YEAR)


def vcl_033_ps_compression_pct_63d(ps: pd.Series) -> pd.Series:
    """Percent compression in positive PS over 63 trading days."""
    p = _positive_mask(ps)
    return _safe_div(p - p.shift(_TD_QTR), p.shift(_TD_QTR).replace(0, np.nan))


def vcl_034_ps_compression_pct_252d(ps: pd.Series) -> pd.Series:
    """Percent compression in positive PS over 252 trading days."""
    p = _positive_mask(ps)
    return _safe_div(p - p.shift(_TD_YEAR), p.shift(_TD_YEAR).replace(0, np.nan))


def vcl_035_ps_below_1_fraction_504d(ps: pd.Series) -> pd.Series:
    """Fraction of last 504 days where PS < 1."""
    flag = ((ps > 0) & (ps < 1.0)).astype(float)
    return _rolling_mean(flag, 504)


def vcl_036_ps_pct_above_252d_min(ps: pd.Series) -> pd.Series:
    """Percent by which PS exceeds its 252-day minimum."""
    p = _positive_mask(ps)
    lo = _rolling_min(p, _TD_YEAR)
    return _safe_div(p - lo, lo)


# --- Group D (037-048): EV/EBIT and EV/EBITDA collapse ---

def vcl_037_evebit_drawdown_from_252d_peak(evebit: pd.Series) -> pd.Series:
    """EV/EBIT drawdown from 252-day peak (positive values only)."""
    p = _positive_mask(evebit)
    peak = _rolling_max(p, _TD_YEAR)
    return _safe_div(p - peak, peak)


def vcl_038_evebit_negative_flag(evebit: pd.Series) -> pd.Series:
    """Binary: EV/EBIT < 0 (negative EBIT = operating losses — distress signal)."""
    return _negative_flag(evebit)


def vcl_039_evebit_below_5_flag(evebit: pd.Series) -> pd.Series:
    """Binary: EV/EBIT > 0 and EV/EBIT < 5 (severe compression threshold)."""
    return ((evebit > 0) & (evebit < 5)).astype(float)


def vcl_040_evebit_below_10_flag(evebit: pd.Series) -> pd.Series:
    """Binary: EV/EBIT > 0 and EV/EBIT < 10."""
    return ((evebit > 0) & (evebit < 10)).astype(float)


def vcl_041_evebit_at_252d_low(evebit: pd.Series) -> pd.Series:
    """1 if positive EV/EBIT is at its 252-day rolling minimum."""
    p = _positive_mask(evebit)
    lo = _rolling_min(p, _TD_YEAR)
    return (p <= lo + _EPS).astype(float)


def vcl_042_evebit_compression_pct_252d(evebit: pd.Series) -> pd.Series:
    """Percent compression in positive EV/EBIT over 252 days."""
    p = _positive_mask(evebit)
    return _safe_div(p - p.shift(_TD_YEAR), p.shift(_TD_YEAR).replace(0, np.nan))


def vcl_043_evebit_negative_fraction_252d(evebit: pd.Series) -> pd.Series:
    """Fraction of last 252 days where EV/EBIT was negative."""
    flag = (evebit < 0).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def vcl_044_evebitda_drawdown_from_252d_peak(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA drawdown from 252-day peak (positive values only)."""
    p = _positive_mask(evebitda)
    peak = _rolling_max(p, _TD_YEAR)
    return _safe_div(p - peak, peak)


def vcl_045_evebitda_drawdown_from_504d_peak(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA drawdown from 504-day peak."""
    p = _positive_mask(evebitda)
    peak = _rolling_max(p, 504)
    return _safe_div(p - peak, peak)


def vcl_046_evebitda_below_5_flag(evebitda: pd.Series) -> pd.Series:
    """Binary: EV/EBITDA > 0 and EV/EBITDA < 5 (extreme compression)."""
    return ((evebitda > 0) & (evebitda < 5)).astype(float)


def vcl_047_evebitda_below_3_flag(evebitda: pd.Series) -> pd.Series:
    """Binary: EV/EBITDA > 0 and EV/EBITDA < 3 (near-liquidation valuation)."""
    return ((evebitda > 0) & (evebitda < 3)).astype(float)


def vcl_048_evebitda_negative_flag(evebitda: pd.Series) -> pd.Series:
    """Binary: EV/EBITDA < 0 (negative EBITDA — severe distress)."""
    return _negative_flag(evebitda)


# --- Group E (049-060): Cross-multiple cheapness agreement and spread ---

def vcl_049_pb_ps_both_below_1_flag(pb: pd.Series, ps: pd.Series) -> pd.Series:
    """Binary: both PB < 1 and PS < 1 simultaneously (dual distress agreement)."""
    return (((pb > 0) & (pb < 1.0)) & ((ps > 0) & (ps < 1.0))).astype(float)


def vcl_050_pe_pb_both_distressed_flag(pe: pd.Series, pb: pd.Series) -> pd.Series:
    """Binary: PE > 0 & PE < 10 and PB > 0 & PB < 1 (earnings + book distress)."""
    pe_dist = (pe > 0) & (pe < 10)
    pb_dist = (pb > 0) & (pb < 1.0)
    return (pe_dist & pb_dist).astype(float)


def vcl_051_triple_distress_flag(pe: pd.Series, pb: pd.Series, ps: pd.Series) -> pd.Series:
    """Binary: PE < 10, PB < 1, and PS < 1 all simultaneously (triple agreement)."""
    pe_d = (pe > 0) & (pe < 10)
    pb_d = (pb > 0) & (pb < 1.0)
    ps_d = (ps > 0) & (ps < 1.0)
    return (pe_d & pb_d & ps_d).astype(float)


def vcl_052_distress_score_count(pe: pd.Series, pb: pd.Series, ps: pd.Series,
                                  evebitda: pd.Series) -> pd.Series:
    """Count of distress thresholds breached: PE<10, PB<1, PS<1, EV/EBITDA<5 (0-4)."""
    s  = ((pe > 0) & (pe < 10)).astype(float)
    s += ((pb > 0) & (pb < 1.0)).astype(float)
    s += ((ps > 0) & (ps < 1.0)).astype(float)
    s += ((evebitda > 0) & (evebitda < 5)).astype(float)
    return s


def vcl_053_pe_pb_ratio(pe: pd.Series, pb: pd.Series) -> pd.Series:
    """PE / PB ratio (both positive) — measures relative cheapness dimension."""
    return _safe_div(_positive_mask(pe), _positive_mask(pb))


def vcl_054_pb_ps_spread(pb: pd.Series, ps: pd.Series) -> pd.Series:
    """PB minus PS (both positive) — spread compression indicator."""
    return _positive_mask(pb) - _positive_mask(ps)


def vcl_055_evebitda_pe_spread(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """EV/EBITDA minus PE (both positive) — acquisition vs earnings multiple gap."""
    return _positive_mask(evebitda) - _positive_mask(pe)


def vcl_056_multiples_drawdown_avg_pe_pb_ps(pe: pd.Series, pb: pd.Series,
                                              ps: pd.Series) -> pd.Series:
    """Average 252-day drawdown across PE, PB, PS (equally weighted de-rating)."""
    dd_pe = _safe_div(_positive_mask(pe) - _rolling_max(_positive_mask(pe), _TD_YEAR),
                      _rolling_max(_positive_mask(pe), _TD_YEAR))
    dd_pb = _safe_div(_positive_mask(pb) - _rolling_max(_positive_mask(pb), _TD_YEAR),
                      _rolling_max(_positive_mask(pb), _TD_YEAR))
    dd_ps = _safe_div(_positive_mask(ps) - _rolling_max(_positive_mask(ps), _TD_YEAR),
                      _rolling_max(_positive_mask(ps), _TD_YEAR))
    count = dd_pe.notna().astype(float) + dd_pb.notna().astype(float) + dd_ps.notna().astype(float)
    total = dd_pe.fillna(0) + dd_pb.fillna(0) + dd_ps.fillna(0)
    return _safe_div(total, count.replace(0, np.nan))


def vcl_057_any_multiple_negative_flag(pe: pd.Series, evebit: pd.Series,
                                        evebitda: pd.Series) -> pd.Series:
    """Binary: at least one of PE, EV/EBIT, EV/EBITDA is negative."""
    return ((pe < 0) | (evebit < 0) | (evebitda < 0)).astype(float)


def vcl_058_negative_multiple_count(pe: pd.Series, evebit: pd.Series,
                                     evebitda: pd.Series) -> pd.Series:
    """Count of negative multiples among PE, EV/EBIT, EV/EBITDA (0-3)."""
    return ((pe < 0).astype(float) + (evebit < 0).astype(float) +
            (evebitda < 0).astype(float))


def vcl_059_pe_to_ps_compression_ratio(pe: pd.Series, ps: pd.Series) -> pd.Series:
    """Ratio of PE's 252-day drawdown to PS's 252-day drawdown (relative compression)."""
    dd_pe = _safe_div(_positive_mask(pe) - _rolling_max(_positive_mask(pe), _TD_YEAR),
                      _rolling_max(_positive_mask(pe), _TD_YEAR))
    dd_ps = _safe_div(_positive_mask(ps) - _rolling_max(_positive_mask(ps), _TD_YEAR),
                      _rolling_max(_positive_mask(ps), _TD_YEAR))
    return _safe_div(dd_pe, dd_ps)


def vcl_060_evebitda_pb_joint_low_flag(evebitda: pd.Series, pb: pd.Series) -> pd.Series:
    """Binary: EV/EBITDA < 5 AND PB < 1 simultaneously."""
    return (((evebitda > 0) & (evebitda < 5)) & ((pb > 0) & (pb < 1.0))).astype(float)


# --- Group F (061-075): Speed and velocity of multiple compression ---

def vcl_061_pe_compression_speed_21d(pe: pd.Series) -> pd.Series:
    """Rate of PE decline: (PE_t - PE_{t-21}) / 21 (points per day, positive PE only)."""
    p = _positive_mask(pe)
    return _safe_div(p - p.shift(_TD_MON), pd.Series(_TD_MON, index=p.index))


def vcl_062_pb_compression_speed_21d(pb: pd.Series) -> pd.Series:
    """Rate of PB decline over 21 days (points per day)."""
    p = _positive_mask(pb)
    return _safe_div(p - p.shift(_TD_MON), pd.Series(_TD_MON, index=p.index))


def vcl_063_ps_compression_speed_63d(ps: pd.Series) -> pd.Series:
    """Rate of PS decline over 63 days (points per day)."""
    p = _positive_mask(ps)
    return _safe_div(p - p.shift(_TD_QTR), pd.Series(_TD_QTR, index=p.index))


def vcl_064_evebitda_compression_speed_63d(evebitda: pd.Series) -> pd.Series:
    """Rate of EV/EBITDA decline over 63 days."""
    p = _positive_mask(evebitda)
    return _safe_div(p - p.shift(_TD_QTR), pd.Series(_TD_QTR, index=p.index))


def vcl_065_pe_derating_velocity_ewm(pe: pd.Series) -> pd.Series:
    """EWM (span=21) of daily PE change — smoothed de-rating velocity."""
    p = _positive_mask(pe)
    return _ewm_mean(p.diff(1), _TD_MON)


def vcl_066_pb_derating_velocity_ewm(pb: pd.Series) -> pd.Series:
    """EWM (span=21) of daily PB change — smoothed de-rating velocity."""
    p = _positive_mask(pb)
    return _ewm_mean(p.diff(1), _TD_MON)


def vcl_067_pe_rolling_min_drawdown_252d(pe: pd.Series) -> pd.Series:
    """Minimum 252-day PE relative to expanding all-time-high PE (deepest de-rating)."""
    p = _positive_mask(pe)
    lo_252 = _rolling_min(p, _TD_YEAR)
    ath_pe = _expanding_max(p)
    return _safe_div(lo_252 - ath_pe, ath_pe)


def vcl_068_pb_rolling_min_drawdown_252d(pb: pd.Series) -> pd.Series:
    """Minimum 252-day PB relative to expanding all-time-high PB."""
    p = _positive_mask(pb)
    lo_252 = _rolling_min(p, _TD_YEAR)
    ath_pb = _expanding_max(p)
    return _safe_div(lo_252 - ath_pb, ath_pb)


def vcl_069_pe_compression_streak_63d(pe: pd.Series) -> pd.Series:
    """Sum of daily PE changes that are negative over trailing 63 days (compression area)."""
    p = _positive_mask(pe)
    daily_chg = p.diff(1)
    neg_chg = daily_chg.where(daily_chg < 0, 0.0)
    return _rolling_sum(neg_chg, _TD_QTR)


def vcl_070_pb_compression_streak_63d(pb: pd.Series) -> pd.Series:
    """Sum of daily PB negative changes over trailing 63 days."""
    p = _positive_mask(pb)
    daily_chg = p.diff(1)
    neg_chg = daily_chg.where(daily_chg < 0, 0.0)
    return _rolling_sum(neg_chg, _TD_QTR)


def vcl_071_ps_compression_streak_252d(ps: pd.Series) -> pd.Series:
    """Sum of daily PS negative changes over trailing 252 days."""
    p = _positive_mask(ps)
    daily_chg = p.diff(1)
    neg_chg = daily_chg.where(daily_chg < 0, 0.0)
    return _rolling_sum(neg_chg, _TD_YEAR)


def vcl_072_evebitda_at_expanding_min(evebitda: pd.Series) -> pd.Series:
    """1 if positive EV/EBITDA is at its all-history expanding minimum."""
    p = _positive_mask(evebitda)
    lo = _expanding_min(p)
    return (p <= lo + _EPS).astype(float)


def vcl_073_pe_compression_volatility_63d(pe: pd.Series) -> pd.Series:
    """Std dev of daily PE changes over 63 days (compression noise / instability)."""
    p = _positive_mask(pe)
    return _rolling_std(p.diff(1), _TD_QTR)


def vcl_074_pb_ps_compression_agreement_252d(pb: pd.Series, ps: pd.Series) -> pd.Series:
    """Fraction of last 252 days where both PB and PS were declining (joint compression)."""
    pb_dec = (pb.diff(1) < 0).astype(float)
    ps_dec = (ps.diff(1) < 0).astype(float)
    both   = (pb_dec * ps_dec)
    return _rolling_mean(both, _TD_YEAR)


def vcl_075_composite_collapse_score(pe: pd.Series, pb: pd.Series,
                                      ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Composite collapse score: avg of normalized 252-day drawdowns across PE/PB/PS/EV/EBITDA."""
    def _dd252(s):
        p = _positive_mask(s)
        peak = _rolling_max(p, _TD_YEAR)
        return _safe_div(p - peak, peak)

    dd_pe  = _dd252(pe)
    dd_pb  = _dd252(pb)
    dd_ps  = _dd252(ps)
    dd_ev  = _dd252(evebitda)
    count  = (dd_pe.notna().astype(float) + dd_pb.notna().astype(float) +
              dd_ps.notna().astype(float) + dd_ev.notna().astype(float))
    total  = (dd_pe.fillna(0) + dd_pb.fillna(0) +
              dd_ps.fillna(0) + dd_ev.fillna(0))
    return _safe_div(total, count.replace(0, np.nan))


# ── Feature functions 151-175 ─────────────────────────────────────────────────

# --- Group M (151-162): divyield, marketcap, ev extended ---

def vcl_151_divyield_zscore_rolling_252d(divyield: pd.Series) -> pd.Series:
    """Rolling 252-day z-score of dividend yield (extreme yield = price collapse signal)."""
    return _zscore_rolling(divyield, _TD_YEAR)


def vcl_152_divyield_at_expanding_max(divyield: pd.Series) -> pd.Series:
    """1 if divyield is at its all-history expanding maximum (yield spike = distress)."""
    hi = divyield.expanding(min_periods=1).max()
    return (divyield >= hi - _EPS).astype(float)


def vcl_153_divyield_252d_range_position(divyield: pd.Series) -> pd.Series:
    """Dividend yield position within its 252-day range (high = collapsed price)."""
    hi = _rolling_max(divyield, _TD_YEAR)
    lo = _rolling_min(divyield, _TD_YEAR)
    return _safe_div(divyield - lo, hi - lo)


def vcl_154_marketcap_below_5pct_ath_flag(marketcap: pd.Series) -> pd.Series:
    """1 if marketcap is within 5% of its all-history expanding minimum."""
    lo = marketcap.expanding(min_periods=1).min()
    return (marketcap <= lo * 1.05).astype(float)


def vcl_155_ev_at_252d_low_flag(ev: pd.Series) -> pd.Series:
    """1 if positive EV is at its 252-day rolling minimum."""
    p  = _positive_mask(ev)
    lo = _rolling_min(p, _TD_YEAR)
    return (p <= lo + _EPS).astype(float)


def vcl_156_ev_zscore_rolling_252d(ev: pd.Series) -> pd.Series:
    """Rolling 252-day z-score of positive EV (statistical extremity of EV collapse)."""
    p = _positive_mask(ev)
    return _zscore_rolling(p, _TD_YEAR)


def vcl_157_ev_compression_pct_63d(ev: pd.Series) -> pd.Series:
    """Percent change in positive EV over 63 trading days (quarterly EV collapse)."""
    p = _positive_mask(ev)
    return _safe_div(p - p.shift(_TD_QTR), p.shift(_TD_QTR).replace(0, np.nan))


def vcl_158_marketcap_compression_pct_63d(marketcap: pd.Series) -> pd.Series:
    """Percent change in market cap over 63 trading days."""
    return _safe_div(marketcap - marketcap.shift(_TD_QTR),
                     marketcap.shift(_TD_QTR).replace(0, np.nan))


def vcl_159_marketcap_compression_streak_252d(marketcap: pd.Series) -> pd.Series:
    """Sum of negative daily marketcap changes over 252 days (equity destruction mass)."""
    neg_chg = marketcap.diff(1).where(marketcap.diff(1) < 0, 0.0)
    return _rolling_sum(neg_chg, _TD_YEAR)


def vcl_160_ev_slope_63d(ev: pd.Series) -> pd.Series:
    """OLS slope of positive EV over 63 days (EV compression trend)."""
    p = _positive_mask(ev)
    return _linslope(p, _TD_QTR)


def vcl_161_divyield_ewm_deviation_21d(divyield: pd.Series) -> pd.Series:
    """Deviation of divyield from its 21-day EWM (short-term yield spike detection)."""
    return divyield - _ewm_mean(divyield, _TD_MON)


def vcl_162_ev_504d_low_position(ev: pd.Series) -> pd.Series:
    """Positive EV position within its 504-day range."""
    p  = _positive_mask(ev)
    hi = _rolling_max(p, 504)
    lo = _rolling_min(p, 504)
    return _safe_div(p - lo, hi - lo)


# --- Group N (163-175): rolling-rank, EWM, and multi-window distress ---

def vcl_163_pe_rolling_rank_pct_252d(pe: pd.Series) -> pd.Series:
    """Percentile rank of positive PE within trailing 252-day window (low = collapse)."""
    p = _positive_mask(pe)
    return _rolling_rank_pct(p, _TD_YEAR)


def vcl_164_pb_rolling_rank_pct_252d(pb: pd.Series) -> pd.Series:
    """Percentile rank of positive PB within trailing 252-day window."""
    p = _positive_mask(pb)
    return _rolling_rank_pct(p, _TD_YEAR)


def vcl_165_ps_rolling_rank_pct_252d(ps: pd.Series) -> pd.Series:
    """Percentile rank of positive PS within trailing 252-day window."""
    p = _positive_mask(ps)
    return _rolling_rank_pct(p, _TD_YEAR)


def vcl_166_evebitda_rolling_rank_pct_252d(evebitda: pd.Series) -> pd.Series:
    """Percentile rank of positive EV/EBITDA within trailing 252-day window."""
    p = _positive_mask(evebitda)
    return _rolling_rank_pct(p, _TD_YEAR)


def vcl_167_pe_ewm_vs_rolling_mean_252d(pe: pd.Series) -> pd.Series:
    """EWM(21) of PE minus rolling 252-day mean (recent vs historical PE gap)."""
    p = _positive_mask(pe)
    return _ewm_mean(p, _TD_MON) - _rolling_mean(p, _TD_YEAR)


def vcl_168_ps_ewm_deviation_21d(ps: pd.Series) -> pd.Series:
    """Deviation of positive PS from its 21-day EWM (short-term PS compression signal)."""
    p = _positive_mask(ps)
    return p - _ewm_mean(p, _TD_MON)


def vcl_169_evebit_compression_streak_63d(evebit: pd.Series) -> pd.Series:
    """Sum of negative daily EV/EBIT changes over 63 days (positive EV/EBIT only)."""
    p      = _positive_mask(evebit)
    neg_ch = p.diff(1).where(p.diff(1) < 0, 0.0)
    return _rolling_sum(neg_ch, _TD_QTR)


def vcl_170_evebitda_compression_streak_63d(evebitda: pd.Series) -> pd.Series:
    """Sum of negative daily EV/EBITDA changes over 63 days (positive values only)."""
    p      = _positive_mask(evebitda)
    neg_ch = p.diff(1).where(p.diff(1) < 0, 0.0)
    return _rolling_sum(neg_ch, _TD_QTR)


def vcl_171_multi_window_pb_low_flags(pb: pd.Series) -> pd.Series:
    """Count of windows (21/63/252/504/1260d) where positive PB is at rolling minimum (0-5)."""
    p = _positive_mask(pb)
    windows = [_TD_MON, _TD_QTR, _TD_YEAR, 504, 1260]
    total = pd.Series(0.0, index=pb.index)
    for w in windows:
        lo   = _rolling_min(p, w)
        flag = (p <= lo + _EPS).fillna(False).astype(float)
        total = total + flag
    return total


def vcl_172_pe_pb_ps_evebit_distress_score(pe: pd.Series, pb: pd.Series,
                                             ps: pd.Series, evebit: pd.Series) -> pd.Series:
    """Count of distress flags: PE<10, PB<1, PS<1, EV/EBIT<5 (0-4)."""
    s  = ((pe > 0) & (pe < 10)).astype(float)
    s += ((pb > 0) & (pb < 1.0)).astype(float)
    s += ((ps > 0) & (ps < 1.0)).astype(float)
    s += ((evebit > 0) & (evebit < 5)).astype(float)
    return s


def vcl_173_ps_compression_volatility_63d(ps: pd.Series) -> pd.Series:
    """Std dev of daily PS changes over 63 days (PS compression instability)."""
    p = _positive_mask(ps)
    return _rolling_std(p.diff(1), _TD_QTR)


def vcl_174_pb_below_0_5_fraction_504d(pb: pd.Series) -> pd.Series:
    """Fraction of last 504 days where positive PB was below 0.5 (deep distress persistence)."""
    flag = ((pb > 0) & (pb < 0.5)).astype(float)
    return _rolling_mean(flag, 504)


def vcl_175_evebitda_below_5_fraction_504d(evebitda: pd.Series) -> pd.Series:
    """Fraction of last 504 days where positive EV/EBITDA was below 5."""
    flag = ((evebitda > 0) & (evebitda < 5)).astype(float)
    return _rolling_mean(flag, 504)


# ── Registry ──────────────────────────────────────────────────────────────────

VALUATION_COLLAPSE_REGISTRY_001_075 = {
    "vcl_001_pe_drawdown_from_252d_peak": {"inputs": ["pe"], "func": vcl_001_pe_drawdown_from_252d_peak},
    "vcl_002_pe_drawdown_from_504d_peak": {"inputs": ["pe"], "func": vcl_002_pe_drawdown_from_504d_peak},
    "vcl_003_pe_drawdown_from_1260d_peak": {"inputs": ["pe"], "func": vcl_003_pe_drawdown_from_1260d_peak},
    "vcl_004_pe_drawdown_from_expanding_peak": {"inputs": ["pe"], "func": vcl_004_pe_drawdown_from_expanding_peak},
    "vcl_005_pe_below_5_flag": {"inputs": ["pe"], "func": vcl_005_pe_below_5_flag},
    "vcl_006_pe_below_10_flag": {"inputs": ["pe"], "func": vcl_006_pe_below_10_flag},
    "vcl_007_pe_negative_flag": {"inputs": ["pe"], "func": vcl_007_pe_negative_flag},
    "vcl_008_pe_at_252d_low": {"inputs": ["pe"], "func": vcl_008_pe_at_252d_low},
    "vcl_009_pe_at_1260d_low": {"inputs": ["pe"], "func": vcl_009_pe_at_1260d_low},
    "vcl_010_pe_pct_above_252d_min": {"inputs": ["pe"], "func": vcl_010_pe_pct_above_252d_min},
    "vcl_011_pe_consecutive_compression_weeks": {"inputs": ["pe"], "func": vcl_011_pe_consecutive_compression_weeks},
    "vcl_012_pe_compression_magnitude_63d": {"inputs": ["pe"], "func": vcl_012_pe_compression_magnitude_63d},
    "vcl_013_pb_drawdown_from_252d_peak": {"inputs": ["pb"], "func": vcl_013_pb_drawdown_from_252d_peak},
    "vcl_014_pb_drawdown_from_504d_peak": {"inputs": ["pb"], "func": vcl_014_pb_drawdown_from_504d_peak},
    "vcl_015_pb_drawdown_from_expanding_peak": {"inputs": ["pb"], "func": vcl_015_pb_drawdown_from_expanding_peak},
    "vcl_016_pb_below_1_flag": {"inputs": ["pb"], "func": vcl_016_pb_below_1_flag},
    "vcl_017_pb_below_0_75_flag": {"inputs": ["pb"], "func": vcl_017_pb_below_0_75_flag},
    "vcl_018_pb_negative_flag": {"inputs": ["pb"], "func": vcl_018_pb_negative_flag},
    "vcl_019_pb_at_1260d_low": {"inputs": ["pb"], "func": vcl_019_pb_at_1260d_low},
    "vcl_020_pb_pct_above_252d_min": {"inputs": ["pb"], "func": vcl_020_pb_pct_above_252d_min},
    "vcl_021_pb_compression_magnitude_63d": {"inputs": ["pb"], "func": vcl_021_pb_compression_magnitude_63d},
    "vcl_022_pb_compression_magnitude_252d": {"inputs": ["pb"], "func": vcl_022_pb_compression_magnitude_252d},
    "vcl_023_pb_below_1_consecutive_days": {"inputs": ["pb"], "func": vcl_023_pb_below_1_consecutive_days},
    "vcl_024_pb_below_1_fraction_252d": {"inputs": ["pb"], "func": vcl_024_pb_below_1_fraction_252d},
    "vcl_025_ps_drawdown_from_252d_peak": {"inputs": ["ps"], "func": vcl_025_ps_drawdown_from_252d_peak},
    "vcl_026_ps_drawdown_from_504d_peak": {"inputs": ["ps"], "func": vcl_026_ps_drawdown_from_504d_peak},
    "vcl_027_ps_drawdown_from_1260d_peak": {"inputs": ["ps"], "func": vcl_027_ps_drawdown_from_1260d_peak},
    "vcl_028_ps_drawdown_from_expanding_peak": {"inputs": ["ps"], "func": vcl_028_ps_drawdown_from_expanding_peak},
    "vcl_029_ps_below_1_flag": {"inputs": ["ps"], "func": vcl_029_ps_below_1_flag},
    "vcl_030_ps_below_0_5_flag": {"inputs": ["ps"], "func": vcl_030_ps_below_0_5_flag},
    "vcl_031_ps_at_252d_low": {"inputs": ["ps"], "func": vcl_031_ps_at_252d_low},
    "vcl_032_ps_compression_magnitude_252d": {"inputs": ["ps"], "func": vcl_032_ps_compression_magnitude_252d},
    "vcl_033_ps_compression_pct_63d": {"inputs": ["ps"], "func": vcl_033_ps_compression_pct_63d},
    "vcl_034_ps_compression_pct_252d": {"inputs": ["ps"], "func": vcl_034_ps_compression_pct_252d},
    "vcl_035_ps_below_1_fraction_504d": {"inputs": ["ps"], "func": vcl_035_ps_below_1_fraction_504d},
    "vcl_036_ps_pct_above_252d_min": {"inputs": ["ps"], "func": vcl_036_ps_pct_above_252d_min},
    "vcl_037_evebit_drawdown_from_252d_peak": {"inputs": ["evebit"], "func": vcl_037_evebit_drawdown_from_252d_peak},
    "vcl_038_evebit_negative_flag": {"inputs": ["evebit"], "func": vcl_038_evebit_negative_flag},
    "vcl_039_evebit_below_5_flag": {"inputs": ["evebit"], "func": vcl_039_evebit_below_5_flag},
    "vcl_040_evebit_below_10_flag": {"inputs": ["evebit"], "func": vcl_040_evebit_below_10_flag},
    "vcl_041_evebit_at_252d_low": {"inputs": ["evebit"], "func": vcl_041_evebit_at_252d_low},
    "vcl_042_evebit_compression_pct_252d": {"inputs": ["evebit"], "func": vcl_042_evebit_compression_pct_252d},
    "vcl_043_evebit_negative_fraction_252d": {"inputs": ["evebit"], "func": vcl_043_evebit_negative_fraction_252d},
    "vcl_044_evebitda_drawdown_from_252d_peak": {"inputs": ["evebitda"], "func": vcl_044_evebitda_drawdown_from_252d_peak},
    "vcl_045_evebitda_drawdown_from_504d_peak": {"inputs": ["evebitda"], "func": vcl_045_evebitda_drawdown_from_504d_peak},
    "vcl_046_evebitda_below_5_flag": {"inputs": ["evebitda"], "func": vcl_046_evebitda_below_5_flag},
    "vcl_047_evebitda_below_3_flag": {"inputs": ["evebitda"], "func": vcl_047_evebitda_below_3_flag},
    "vcl_048_evebitda_negative_flag": {"inputs": ["evebitda"], "func": vcl_048_evebitda_negative_flag},
    "vcl_049_pb_ps_both_below_1_flag": {"inputs": ["pb", "ps"], "func": vcl_049_pb_ps_both_below_1_flag},
    "vcl_050_pe_pb_both_distressed_flag": {"inputs": ["pe", "pb"], "func": vcl_050_pe_pb_both_distressed_flag},
    "vcl_051_triple_distress_flag": {"inputs": ["pe", "pb", "ps"], "func": vcl_051_triple_distress_flag},
    "vcl_052_distress_score_count": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_052_distress_score_count},
    "vcl_053_pe_pb_ratio": {"inputs": ["pe", "pb"], "func": vcl_053_pe_pb_ratio},
    "vcl_054_pb_ps_spread": {"inputs": ["pb", "ps"], "func": vcl_054_pb_ps_spread},
    "vcl_055_evebitda_pe_spread": {"inputs": ["evebitda", "pe"], "func": vcl_055_evebitda_pe_spread},
    "vcl_056_multiples_drawdown_avg_pe_pb_ps": {"inputs": ["pe", "pb", "ps"], "func": vcl_056_multiples_drawdown_avg_pe_pb_ps},
    "vcl_057_any_multiple_negative_flag": {"inputs": ["pe", "evebit", "evebitda"], "func": vcl_057_any_multiple_negative_flag},
    "vcl_058_negative_multiple_count": {"inputs": ["pe", "evebit", "evebitda"], "func": vcl_058_negative_multiple_count},
    "vcl_059_pe_to_ps_compression_ratio": {"inputs": ["pe", "ps"], "func": vcl_059_pe_to_ps_compression_ratio},
    "vcl_060_evebitda_pb_joint_low_flag": {"inputs": ["evebitda", "pb"], "func": vcl_060_evebitda_pb_joint_low_flag},
    "vcl_061_pe_compression_speed_21d": {"inputs": ["pe"], "func": vcl_061_pe_compression_speed_21d},
    "vcl_062_pb_compression_speed_21d": {"inputs": ["pb"], "func": vcl_062_pb_compression_speed_21d},
    "vcl_063_ps_compression_speed_63d": {"inputs": ["ps"], "func": vcl_063_ps_compression_speed_63d},
    "vcl_064_evebitda_compression_speed_63d": {"inputs": ["evebitda"], "func": vcl_064_evebitda_compression_speed_63d},
    "vcl_065_pe_derating_velocity_ewm": {"inputs": ["pe"], "func": vcl_065_pe_derating_velocity_ewm},
    "vcl_066_pb_derating_velocity_ewm": {"inputs": ["pb"], "func": vcl_066_pb_derating_velocity_ewm},
    "vcl_067_pe_rolling_min_drawdown_252d": {"inputs": ["pe"], "func": vcl_067_pe_rolling_min_drawdown_252d},
    "vcl_068_pb_rolling_min_drawdown_252d": {"inputs": ["pb"], "func": vcl_068_pb_rolling_min_drawdown_252d},
    "vcl_069_pe_compression_streak_63d": {"inputs": ["pe"], "func": vcl_069_pe_compression_streak_63d},
    "vcl_070_pb_compression_streak_63d": {"inputs": ["pb"], "func": vcl_070_pb_compression_streak_63d},
    "vcl_071_ps_compression_streak_252d": {"inputs": ["ps"], "func": vcl_071_ps_compression_streak_252d},
    "vcl_072_evebitda_at_expanding_min": {"inputs": ["evebitda"], "func": vcl_072_evebitda_at_expanding_min},
    "vcl_073_pe_compression_volatility_63d": {"inputs": ["pe"], "func": vcl_073_pe_compression_volatility_63d},
    "vcl_074_pb_ps_compression_agreement_252d": {"inputs": ["pb", "ps"], "func": vcl_074_pb_ps_compression_agreement_252d},
    "vcl_075_composite_collapse_score": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_075_composite_collapse_score},
    "vcl_151_divyield_zscore_rolling_252d": {"inputs": ["divyield"], "func": vcl_151_divyield_zscore_rolling_252d},
    "vcl_152_divyield_at_expanding_max": {"inputs": ["divyield"], "func": vcl_152_divyield_at_expanding_max},
    "vcl_153_divyield_252d_range_position": {"inputs": ["divyield"], "func": vcl_153_divyield_252d_range_position},
    "vcl_154_marketcap_below_5pct_ath_flag": {"inputs": ["marketcap"], "func": vcl_154_marketcap_below_5pct_ath_flag},
    "vcl_155_ev_at_252d_low_flag": {"inputs": ["ev"], "func": vcl_155_ev_at_252d_low_flag},
    "vcl_156_ev_zscore_rolling_252d": {"inputs": ["ev"], "func": vcl_156_ev_zscore_rolling_252d},
    "vcl_157_ev_compression_pct_63d": {"inputs": ["ev"], "func": vcl_157_ev_compression_pct_63d},
    "vcl_158_marketcap_compression_pct_63d": {"inputs": ["marketcap"], "func": vcl_158_marketcap_compression_pct_63d},
    "vcl_159_marketcap_compression_streak_252d": {"inputs": ["marketcap"], "func": vcl_159_marketcap_compression_streak_252d},
    "vcl_160_ev_slope_63d": {"inputs": ["ev"], "func": vcl_160_ev_slope_63d},
    "vcl_161_divyield_ewm_deviation_21d": {"inputs": ["divyield"], "func": vcl_161_divyield_ewm_deviation_21d},
    "vcl_162_ev_504d_low_position": {"inputs": ["ev"], "func": vcl_162_ev_504d_low_position},
    "vcl_163_pe_rolling_rank_pct_252d": {"inputs": ["pe"], "func": vcl_163_pe_rolling_rank_pct_252d},
    "vcl_164_pb_rolling_rank_pct_252d": {"inputs": ["pb"], "func": vcl_164_pb_rolling_rank_pct_252d},
    "vcl_165_ps_rolling_rank_pct_252d": {"inputs": ["ps"], "func": vcl_165_ps_rolling_rank_pct_252d},
    "vcl_166_evebitda_rolling_rank_pct_252d": {"inputs": ["evebitda"], "func": vcl_166_evebitda_rolling_rank_pct_252d},
    "vcl_167_pe_ewm_vs_rolling_mean_252d": {"inputs": ["pe"], "func": vcl_167_pe_ewm_vs_rolling_mean_252d},
    "vcl_168_ps_ewm_deviation_21d": {"inputs": ["ps"], "func": vcl_168_ps_ewm_deviation_21d},
    "vcl_169_evebit_compression_streak_63d": {"inputs": ["evebit"], "func": vcl_169_evebit_compression_streak_63d},
    "vcl_170_evebitda_compression_streak_63d": {"inputs": ["evebitda"], "func": vcl_170_evebitda_compression_streak_63d},
    "vcl_171_multi_window_pb_low_flags": {"inputs": ["pb"], "func": vcl_171_multi_window_pb_low_flags},
    "vcl_172_pe_pb_ps_evebit_distress_score": {"inputs": ["pe", "pb", "ps", "evebit"], "func": vcl_172_pe_pb_ps_evebit_distress_score},
    "vcl_173_ps_compression_volatility_63d": {"inputs": ["ps"], "func": vcl_173_ps_compression_volatility_63d},
    "vcl_174_pb_below_0_5_fraction_504d": {"inputs": ["pb"], "func": vcl_174_pb_below_0_5_fraction_504d},
    "vcl_175_evebitda_below_5_fraction_504d": {"inputs": ["evebitda"], "func": vcl_175_evebitda_below_5_fraction_504d},
}
