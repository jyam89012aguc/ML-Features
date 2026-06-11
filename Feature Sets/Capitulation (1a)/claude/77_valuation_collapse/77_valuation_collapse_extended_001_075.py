"""
77_valuation_collapse — Extended Features 001-075
Domain: PE/PB/PS/EV-multiple compression to extremes — additional collapse variants:
        new lookback windows, range positions, half-year/quarterly drawdowns,
        velocity/acceleration of de-rating, fresh cross-multiple confluence.
Asset class: US equities | Sharadar DAILY/METRICS valuation fields (daily frequency):
    marketcap, ev, pe, pb, ps, evebit, evebitda, divyield
These are native daily-frequency series; no quarterly forward-fill alignment is needed.
All feature functions are backward-looking only — no negative shifts, no future info.

These are EXTENDED features in the valuation-collapse domain: net-new variants that
do NOT duplicate base_001_075, base_076_150, 2nd_derivatives or 3rd_derivatives.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_TD_2Y   = 504
_TD_3Y   = 756
_TD_5Y   = 1260
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; zero or NaN denominator -> NaN."""
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


def _range_position(s: pd.Series, w: int) -> pd.Series:
    """Position of s within its trailing w-day min-max range (0 = at the low)."""
    hi = _rolling_max(s, w)
    lo = _rolling_min(s, w)
    return _safe_div(s - lo, hi - lo)


def _drawdown_from_peak(s: pd.Series, w: int) -> pd.Series:
    """Fractional drawdown of positive s from its trailing w-day peak."""
    p = _positive_mask(s)
    peak = _rolling_max(p, w)
    return _safe_div(p - peak, peak)


def _consec_streak(cond: pd.Series, index: pd.Index) -> pd.Series:
    """Consecutive-row streak of True values (backward-looking)."""
    arr = cond.astype(int).values
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=index)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): New-window drawdowns (126d, 63d, 3y) ---

def vcl_ext_001_pe_drawdown_from_126d_peak(pe: pd.Series) -> pd.Series:
    """PE ratio drawdown from its trailing 126-day (half-year) peak."""
    return _drawdown_from_peak(pe, _TD_HALF)


def vcl_ext_002_pe_drawdown_from_63d_peak(pe: pd.Series) -> pd.Series:
    """PE ratio drawdown from its trailing 63-day (quarterly) peak."""
    return _drawdown_from_peak(pe, _TD_QTR)


def vcl_ext_003_pe_drawdown_from_756d_peak(pe: pd.Series) -> pd.Series:
    """PE ratio drawdown from its trailing 756-day (3-year) peak."""
    return _drawdown_from_peak(pe, _TD_3Y)


def vcl_ext_004_pb_drawdown_from_126d_peak(pb: pd.Series) -> pd.Series:
    """PB ratio drawdown from its trailing 126-day peak."""
    return _drawdown_from_peak(pb, _TD_HALF)


def vcl_ext_005_pb_drawdown_from_63d_peak(pb: pd.Series) -> pd.Series:
    """PB ratio drawdown from its trailing 63-day peak."""
    return _drawdown_from_peak(pb, _TD_QTR)


def vcl_ext_006_pb_drawdown_from_756d_peak(pb: pd.Series) -> pd.Series:
    """PB ratio drawdown from its trailing 756-day (3-year) peak."""
    return _drawdown_from_peak(pb, _TD_3Y)


def vcl_ext_007_ps_drawdown_from_126d_peak(ps: pd.Series) -> pd.Series:
    """PS ratio drawdown from its trailing 126-day peak."""
    return _drawdown_from_peak(ps, _TD_HALF)


def vcl_ext_008_ps_drawdown_from_63d_peak(ps: pd.Series) -> pd.Series:
    """PS ratio drawdown from its trailing 63-day peak."""
    return _drawdown_from_peak(ps, _TD_QTR)


def vcl_ext_009_evebitda_drawdown_from_126d_peak(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA drawdown from its trailing 126-day peak."""
    return _drawdown_from_peak(evebitda, _TD_HALF)


def vcl_ext_010_evebit_drawdown_from_126d_peak(evebit: pd.Series) -> pd.Series:
    """EV/EBIT drawdown from its trailing 126-day peak."""
    return _drawdown_from_peak(evebit, _TD_HALF)


def vcl_ext_011_marketcap_drawdown_from_252d_peak(marketcap: pd.Series) -> pd.Series:
    """Market cap drawdown from its trailing 252-day peak."""
    peak = _rolling_max(marketcap, _TD_YEAR)
    return _safe_div(marketcap - peak, peak)


def vcl_ext_012_marketcap_drawdown_from_expanding_peak(marketcap: pd.Series) -> pd.Series:
    """Market cap drawdown from its all-history expanding peak."""
    peak = _expanding_max(marketcap)
    return _safe_div(marketcap - peak, peak)


# --- Group B (013-024): Range positions across multiples and windows ---

def vcl_ext_013_pe_range_position_252d(pe: pd.Series) -> pd.Series:
    """Positive PE position within its 252-day min-max range (0 = at the low)."""
    return _range_position(_positive_mask(pe), _TD_YEAR)


def vcl_ext_014_pe_range_position_504d(pe: pd.Series) -> pd.Series:
    """Positive PE position within its 504-day min-max range."""
    return _range_position(_positive_mask(pe), _TD_2Y)


def vcl_ext_015_pb_range_position_252d(pb: pd.Series) -> pd.Series:
    """Positive PB position within its 252-day min-max range."""
    return _range_position(_positive_mask(pb), _TD_YEAR)


def vcl_ext_016_pb_range_position_504d(pb: pd.Series) -> pd.Series:
    """Positive PB position within its 504-day min-max range."""
    return _range_position(_positive_mask(pb), _TD_2Y)


def vcl_ext_017_ps_range_position_252d(ps: pd.Series) -> pd.Series:
    """Positive PS position within its 252-day min-max range."""
    return _range_position(_positive_mask(ps), _TD_YEAR)


def vcl_ext_018_ps_range_position_504d(ps: pd.Series) -> pd.Series:
    """Positive PS position within its 504-day min-max range."""
    return _range_position(_positive_mask(ps), _TD_2Y)


def vcl_ext_019_evebitda_range_position_252d(evebitda: pd.Series) -> pd.Series:
    """Positive EV/EBITDA position within its 252-day min-max range."""
    return _range_position(_positive_mask(evebitda), _TD_YEAR)


def vcl_ext_020_evebit_range_position_252d(evebit: pd.Series) -> pd.Series:
    """Positive EV/EBIT position within its 252-day min-max range."""
    return _range_position(_positive_mask(evebit), _TD_YEAR)


def vcl_ext_021_marketcap_range_position_252d(marketcap: pd.Series) -> pd.Series:
    """Market cap position within its 252-day min-max range."""
    return _range_position(marketcap, _TD_YEAR)


def vcl_ext_022_ev_range_position_252d(ev: pd.Series) -> pd.Series:
    """Positive EV position within its 252-day min-max range."""
    return _range_position(_positive_mask(ev), _TD_YEAR)


def vcl_ext_023_pe_range_position_63d(pe: pd.Series) -> pd.Series:
    """Positive PE position within its 63-day min-max range (short-horizon)."""
    return _range_position(_positive_mask(pe), _TD_QTR)


def vcl_ext_024_pb_range_position_126d(pb: pd.Series) -> pd.Series:
    """Positive PB position within its 126-day min-max range."""
    return _range_position(_positive_mask(pb), _TD_HALF)


# --- Group C (025-036): New rolling-low flags and percent-above-min variants ---

def vcl_ext_025_pe_at_504d_low(pe: pd.Series) -> pd.Series:
    """1 if positive PE is at or below its 504-day rolling minimum."""
    p = _positive_mask(pe)
    lo = _rolling_min(p, _TD_2Y)
    return (p <= lo + _EPS).astype(float)


def vcl_ext_026_pe_at_expanding_low(pe: pd.Series) -> pd.Series:
    """1 if positive PE is at its all-history expanding minimum."""
    p = _positive_mask(pe)
    lo = _expanding_min(p)
    return (p <= lo + _EPS).astype(float)


def vcl_ext_027_pb_at_252d_low(pb: pd.Series) -> pd.Series:
    """1 if positive PB is at or below its 252-day rolling minimum."""
    p = _positive_mask(pb)
    lo = _rolling_min(p, _TD_YEAR)
    return (p <= lo + _EPS).astype(float)


def vcl_ext_028_pb_at_504d_low(pb: pd.Series) -> pd.Series:
    """1 if positive PB is at or below its 504-day rolling minimum."""
    p = _positive_mask(pb)
    lo = _rolling_min(p, _TD_2Y)
    return (p <= lo + _EPS).astype(float)


def vcl_ext_029_ps_at_504d_low(ps: pd.Series) -> pd.Series:
    """1 if positive PS is at or below its 504-day rolling minimum."""
    p = _positive_mask(ps)
    lo = _rolling_min(p, _TD_2Y)
    return (p <= lo + _EPS).astype(float)


def vcl_ext_030_ps_at_expanding_low(ps: pd.Series) -> pd.Series:
    """1 if positive PS is at its all-history expanding minimum."""
    p = _positive_mask(ps)
    lo = _expanding_min(p)
    return (p <= lo + _EPS).astype(float)


def vcl_ext_031_evebitda_at_252d_low(evebitda: pd.Series) -> pd.Series:
    """1 if positive EV/EBITDA is at or below its 252-day rolling minimum."""
    p = _positive_mask(evebitda)
    lo = _rolling_min(p, _TD_YEAR)
    return (p <= lo + _EPS).astype(float)


def vcl_ext_032_pb_pct_above_504d_min(pb: pd.Series) -> pd.Series:
    """Percent by which positive PB exceeds its 504-day minimum (0 = at the low)."""
    p = _positive_mask(pb)
    lo = _rolling_min(p, _TD_2Y)
    return _safe_div(p - lo, lo)


def vcl_ext_033_pe_pct_above_504d_min(pe: pd.Series) -> pd.Series:
    """Percent by which positive PE exceeds its 504-day minimum."""
    p = _positive_mask(pe)
    lo = _rolling_min(p, _TD_2Y)
    return _safe_div(p - lo, lo)


def vcl_ext_034_ps_pct_above_504d_min(ps: pd.Series) -> pd.Series:
    """Percent by which positive PS exceeds its 504-day minimum."""
    p = _positive_mask(ps)
    lo = _rolling_min(p, _TD_2Y)
    return _safe_div(p - lo, lo)


def vcl_ext_035_evebitda_pct_above_252d_min(evebitda: pd.Series) -> pd.Series:
    """Percent by which positive EV/EBITDA exceeds its 252-day minimum."""
    p = _positive_mask(evebitda)
    lo = _rolling_min(p, _TD_YEAR)
    return _safe_div(p - lo, lo)


def vcl_ext_036_marketcap_at_252d_low(marketcap: pd.Series) -> pd.Series:
    """1 if market cap is at or below its 252-day rolling minimum."""
    lo = _rolling_min(marketcap, _TD_YEAR)
    return (marketcap <= lo + _EPS).astype(float)


# --- Group D (037-048): Compression magnitude / pct at new horizons ---

def vcl_ext_037_pe_compression_pct_126d(pe: pd.Series) -> pd.Series:
    """Percent compression in positive PE over 126 trading days."""
    p = _positive_mask(pe)
    return _safe_div(p - p.shift(_TD_HALF), p.shift(_TD_HALF))


def vcl_ext_038_pb_compression_pct_126d(pb: pd.Series) -> pd.Series:
    """Percent compression in positive PB over 126 trading days."""
    p = _positive_mask(pb)
    return _safe_div(p - p.shift(_TD_HALF), p.shift(_TD_HALF))


def vcl_ext_039_ps_compression_pct_126d(ps: pd.Series) -> pd.Series:
    """Percent compression in positive PS over 126 trading days."""
    p = _positive_mask(ps)
    return _safe_div(p - p.shift(_TD_HALF), p.shift(_TD_HALF))


def vcl_ext_040_pe_compression_pct_21d(pe: pd.Series) -> pd.Series:
    """Percent compression in positive PE over 21 trading days (monthly de-rating)."""
    p = _positive_mask(pe)
    return _safe_div(p - p.shift(_TD_MON), p.shift(_TD_MON))


def vcl_ext_041_pb_compression_pct_21d(pb: pd.Series) -> pd.Series:
    """Percent compression in positive PB over 21 trading days."""
    p = _positive_mask(pb)
    return _safe_div(p - p.shift(_TD_MON), p.shift(_TD_MON))


def vcl_ext_042_pe_compression_pct_504d(pe: pd.Series) -> pd.Series:
    """Percent compression in positive PE over 504 trading days (two-year de-rating)."""
    p = _positive_mask(pe)
    return _safe_div(p - p.shift(_TD_2Y), p.shift(_TD_2Y))


def vcl_ext_043_pb_compression_pct_252d(pb: pd.Series) -> pd.Series:
    """Percent compression in positive PB over 252 trading days (annual de-rating)."""
    p = _positive_mask(pb)
    return _safe_div(p - p.shift(_TD_YEAR), p.shift(_TD_YEAR))


def vcl_ext_044_evebitda_compression_pct_126d(evebitda: pd.Series) -> pd.Series:
    """Percent compression in positive EV/EBITDA over 126 trading days."""
    p = _positive_mask(evebitda)
    return _safe_div(p - p.shift(_TD_HALF), p.shift(_TD_HALF))


def vcl_ext_045_evebit_compression_pct_126d(evebit: pd.Series) -> pd.Series:
    """Percent compression in positive EV/EBIT over 126 trading days."""
    p = _positive_mask(evebit)
    return _safe_div(p - p.shift(_TD_HALF), p.shift(_TD_HALF))


def vcl_ext_046_ps_compression_magnitude_126d(ps: pd.Series) -> pd.Series:
    """Absolute drop in positive PS over 126 trading days."""
    p = _positive_mask(ps)
    return p - p.shift(_TD_HALF)


def vcl_ext_047_pe_compression_magnitude_126d(pe: pd.Series) -> pd.Series:
    """Absolute drop in positive PE over 126 trading days."""
    p = _positive_mask(pe)
    return p - p.shift(_TD_HALF)


def vcl_ext_048_marketcap_compression_pct_252d(marketcap: pd.Series) -> pd.Series:
    """Percent compression in market cap over 252 trading days."""
    return _safe_div(marketcap - marketcap.shift(_TD_YEAR), marketcap.shift(_TD_YEAR))


# --- Group E (049-060): Velocity, acceleration and de-rating streaks ---

def vcl_ext_049_pe_compression_speed_63d(pe: pd.Series) -> pd.Series:
    """Rate of PE decline: (PE_t - PE_{t-63}) / 63 (points per day, positive PE)."""
    p = _positive_mask(pe)
    return (p - p.shift(_TD_QTR)) / float(_TD_QTR)


def vcl_ext_050_pb_compression_speed_63d(pb: pd.Series) -> pd.Series:
    """Rate of PB decline over 63 days (points per day, positive PB)."""
    p = _positive_mask(pb)
    return (p - p.shift(_TD_QTR)) / float(_TD_QTR)


def vcl_ext_051_ps_compression_speed_21d(ps: pd.Series) -> pd.Series:
    """Rate of PS decline over 21 days (points per day, positive PS)."""
    p = _positive_mask(ps)
    return (p - p.shift(_TD_MON)) / float(_TD_MON)


def vcl_ext_052_pe_compression_accel_63d(pe: pd.Series) -> pd.Series:
    """PE compression acceleration: change in 63-day compression vs 63 days prior."""
    p = _positive_mask(pe)
    comp = p - p.shift(_TD_QTR)
    return comp - comp.shift(_TD_QTR)


def vcl_ext_053_pb_compression_accel_63d(pb: pd.Series) -> pd.Series:
    """PB compression acceleration: change in 63-day compression vs 63 days prior."""
    p = _positive_mask(pb)
    comp = p - p.shift(_TD_QTR)
    return comp - comp.shift(_TD_QTR)


def vcl_ext_054_ps_derating_velocity_ewm(ps: pd.Series) -> pd.Series:
    """EWM (span=21) of daily PS change — smoothed de-rating velocity."""
    p = _positive_mask(ps)
    return _ewm_mean(p.diff(1), _TD_MON)


def vcl_ext_055_evebitda_derating_velocity_ewm(evebitda: pd.Series) -> pd.Series:
    """EWM (span=21) of daily EV/EBITDA change — smoothed de-rating velocity."""
    p = _positive_mask(evebitda)
    return _ewm_mean(p.diff(1), _TD_MON)


def vcl_ext_056_pe_declining_days_streak(pe: pd.Series) -> pd.Series:
    """Consecutive days of declining positive PE (compression run length)."""
    p = _positive_mask(pe)
    return _consec_streak(p.diff(1) < 0, pe.index)


def vcl_ext_057_pb_declining_days_streak(pb: pd.Series) -> pd.Series:
    """Consecutive days of declining positive PB (compression run length)."""
    p = _positive_mask(pb)
    return _consec_streak(p.diff(1) < 0, pb.index)


def vcl_ext_058_ps_declining_days_streak(ps: pd.Series) -> pd.Series:
    """Consecutive days of declining positive PS (compression run length)."""
    p = _positive_mask(ps)
    return _consec_streak(p.diff(1) < 0, ps.index)


def vcl_ext_059_marketcap_declining_days_streak(marketcap: pd.Series) -> pd.Series:
    """Consecutive days of declining market cap (equity-destruction run length)."""
    return _consec_streak(marketcap.diff(1) < 0, marketcap.index)


def vcl_ext_060_pe_compression_streak_252d(pe: pd.Series) -> pd.Series:
    """Sum of negative daily PE changes over trailing 252 days (annual compression area)."""
    p = _positive_mask(pe)
    daily = p.diff(1)
    return _rolling_sum(daily.where(daily < 0, 0.0), _TD_YEAR)


# --- Group F (061-068): New z-score, rank, and EWM-gap variants ---

def vcl_ext_061_pe_zscore_504d(pe: pd.Series) -> pd.Series:
    """Rolling 504-day z-score of positive PE."""
    return _zscore_rolling(_positive_mask(pe), _TD_2Y)


def vcl_ext_062_pb_zscore_252d(pb: pd.Series) -> pd.Series:
    """Rolling 252-day z-score of positive PB."""
    return _zscore_rolling(_positive_mask(pb), _TD_YEAR)


def vcl_ext_063_ps_zscore_252d(ps: pd.Series) -> pd.Series:
    """Rolling 252-day z-score of positive PS."""
    return _zscore_rolling(_positive_mask(ps), _TD_YEAR)


def vcl_ext_064_evebitda_zscore_252d(evebitda: pd.Series) -> pd.Series:
    """Rolling 252-day z-score of positive EV/EBITDA."""
    return _zscore_rolling(_positive_mask(evebitda), _TD_YEAR)


def vcl_ext_065_pe_rolling_rank_pct_504d(pe: pd.Series) -> pd.Series:
    """Percentile rank of positive PE within trailing 504-day window."""
    return _rolling_rank_pct(_positive_mask(pe), _TD_2Y)


def vcl_ext_066_pb_rolling_rank_pct_504d(pb: pd.Series) -> pd.Series:
    """Percentile rank of positive PB within trailing 504-day window."""
    return _rolling_rank_pct(_positive_mask(pb), _TD_2Y)


def vcl_ext_067_marketcap_rolling_rank_pct_252d(marketcap: pd.Series) -> pd.Series:
    """Percentile rank of market cap within trailing 252-day window (low = collapse)."""
    return _rolling_rank_pct(marketcap, _TD_YEAR)


def vcl_ext_068_pb_ewm_deviation_21d(pb: pd.Series) -> pd.Series:
    """Deviation of positive PB from its 21-day EWM (short-term compression signal)."""
    p = _positive_mask(pb)
    return p - _ewm_mean(p, _TD_MON)


# --- Group G (069-075): Fresh cross-multiple confluence and composites ---

def vcl_ext_069_pe_ps_both_below_median_252d(pe: pd.Series, ps: pd.Series) -> pd.Series:
    """1 when both positive PE and PS are below their own 252-day rolling medians."""
    pe_p = _positive_mask(pe)
    ps_p = _positive_mask(ps)
    pe_lo = pe_p < _rolling_median(pe_p, _TD_YEAR)
    ps_lo = ps_p < _rolling_median(ps_p, _TD_YEAR)
    return (pe_lo & ps_lo).astype(float)


def vcl_ext_070_multiple_at_252d_low_count(pe: pd.Series, pb: pd.Series,
                                            ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Count of multiples (PE, PB, PS, EV/EBITDA) at their 252-day rolling low (0-4)."""
    def _at_low(s):
        p = _positive_mask(s)
        lo = _rolling_min(p, _TD_YEAR)
        return (p <= lo + _EPS).fillna(False).astype(float)
    return _at_low(pe) + _at_low(pb) + _at_low(ps) + _at_low(evebitda)


def vcl_ext_071_deep_distress_score(pe: pd.Series, pb: pd.Series, ps: pd.Series,
                                     evebitda: pd.Series) -> pd.Series:
    """Count of deep-distress thresholds breached: PE<5, PB<0.75, PS<0.5, EV/EBITDA<3 (0-4)."""
    s  = ((pe > 0) & (pe < 5)).astype(float)
    s += ((pb > 0) & (pb < 0.75)).astype(float)
    s += ((ps > 0) & (ps < 0.5)).astype(float)
    s += ((evebitda > 0) & (evebitda < 3)).astype(float)
    return s


def vcl_ext_072_all_multiples_compressing_flag(pe: pd.Series, pb: pd.Series,
                                                ps: pd.Series) -> pd.Series:
    """1 when PE, PB and PS are all below their levels 63 days ago (broad de-rating)."""
    pe_p = _positive_mask(pe)
    pb_p = _positive_mask(pb)
    ps_p = _positive_mask(ps)
    f = ((pe_p < pe_p.shift(_TD_QTR)) &
         (pb_p < pb_p.shift(_TD_QTR)) &
         (ps_p < ps_p.shift(_TD_QTR)))
    return f.astype(float)


def vcl_ext_073_negative_multiple_count_4way(pe: pd.Series, pb: pd.Series,
                                              evebit: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Count of negative multiples among PE, PB, EV/EBIT, EV/EBITDA (0-4)."""
    return ((pe < 0).astype(float) + (pb < 0).astype(float) +
            (evebit < 0).astype(float) + (evebitda < 0).astype(float))


def vcl_ext_074_composite_collapse_score_126d(pe: pd.Series, pb: pd.Series,
                                               ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Composite collapse score: average of 126-day drawdowns across PE/PB/PS/EV/EBITDA."""
    dd_pe = _drawdown_from_peak(pe, _TD_HALF)
    dd_pb = _drawdown_from_peak(pb, _TD_HALF)
    dd_ps = _drawdown_from_peak(ps, _TD_HALF)
    dd_ev = _drawdown_from_peak(evebitda, _TD_HALF)
    count = (dd_pe.notna().astype(float) + dd_pb.notna().astype(float) +
             dd_ps.notna().astype(float) + dd_ev.notna().astype(float))
    total = (dd_pe.fillna(0) + dd_pb.fillna(0) +
             dd_ps.fillna(0) + dd_ev.fillna(0))
    return _safe_div(total, count.replace(0, np.nan))


def vcl_ext_075_composite_range_position_score(pe: pd.Series, pb: pd.Series,
                                                ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """
    Composite range-position score: average of 252-day range positions across
    PE/PB/PS/EV/EBITDA. Near 0 = all multiples pinned at their annual lows.
    """
    rp_pe = _range_position(_positive_mask(pe), _TD_YEAR)
    rp_pb = _range_position(_positive_mask(pb), _TD_YEAR)
    rp_ps = _range_position(_positive_mask(ps), _TD_YEAR)
    rp_ev = _range_position(_positive_mask(evebitda), _TD_YEAR)
    count = (rp_pe.notna().astype(float) + rp_pb.notna().astype(float) +
             rp_ps.notna().astype(float) + rp_ev.notna().astype(float))
    total = (rp_pe.fillna(0) + rp_pb.fillna(0) +
             rp_ps.fillna(0) + rp_ev.fillna(0))
    return _safe_div(total, count.replace(0, np.nan))


# ── Registry ──────────────────────────────────────────────────────────────────

VALUATION_COLLAPSE_EXTENDED_REGISTRY_001_075 = {
    "vcl_ext_001_pe_drawdown_from_126d_peak": {"inputs": ["pe"], "func": vcl_ext_001_pe_drawdown_from_126d_peak},
    "vcl_ext_002_pe_drawdown_from_63d_peak": {"inputs": ["pe"], "func": vcl_ext_002_pe_drawdown_from_63d_peak},
    "vcl_ext_003_pe_drawdown_from_756d_peak": {"inputs": ["pe"], "func": vcl_ext_003_pe_drawdown_from_756d_peak},
    "vcl_ext_004_pb_drawdown_from_126d_peak": {"inputs": ["pb"], "func": vcl_ext_004_pb_drawdown_from_126d_peak},
    "vcl_ext_005_pb_drawdown_from_63d_peak": {"inputs": ["pb"], "func": vcl_ext_005_pb_drawdown_from_63d_peak},
    "vcl_ext_006_pb_drawdown_from_756d_peak": {"inputs": ["pb"], "func": vcl_ext_006_pb_drawdown_from_756d_peak},
    "vcl_ext_007_ps_drawdown_from_126d_peak": {"inputs": ["ps"], "func": vcl_ext_007_ps_drawdown_from_126d_peak},
    "vcl_ext_008_ps_drawdown_from_63d_peak": {"inputs": ["ps"], "func": vcl_ext_008_ps_drawdown_from_63d_peak},
    "vcl_ext_009_evebitda_drawdown_from_126d_peak": {"inputs": ["evebitda"], "func": vcl_ext_009_evebitda_drawdown_from_126d_peak},
    "vcl_ext_010_evebit_drawdown_from_126d_peak": {"inputs": ["evebit"], "func": vcl_ext_010_evebit_drawdown_from_126d_peak},
    "vcl_ext_011_marketcap_drawdown_from_252d_peak": {"inputs": ["marketcap"], "func": vcl_ext_011_marketcap_drawdown_from_252d_peak},
    "vcl_ext_012_marketcap_drawdown_from_expanding_peak": {"inputs": ["marketcap"], "func": vcl_ext_012_marketcap_drawdown_from_expanding_peak},
    "vcl_ext_013_pe_range_position_252d": {"inputs": ["pe"], "func": vcl_ext_013_pe_range_position_252d},
    "vcl_ext_014_pe_range_position_504d": {"inputs": ["pe"], "func": vcl_ext_014_pe_range_position_504d},
    "vcl_ext_015_pb_range_position_252d": {"inputs": ["pb"], "func": vcl_ext_015_pb_range_position_252d},
    "vcl_ext_016_pb_range_position_504d": {"inputs": ["pb"], "func": vcl_ext_016_pb_range_position_504d},
    "vcl_ext_017_ps_range_position_252d": {"inputs": ["ps"], "func": vcl_ext_017_ps_range_position_252d},
    "vcl_ext_018_ps_range_position_504d": {"inputs": ["ps"], "func": vcl_ext_018_ps_range_position_504d},
    "vcl_ext_019_evebitda_range_position_252d": {"inputs": ["evebitda"], "func": vcl_ext_019_evebitda_range_position_252d},
    "vcl_ext_020_evebit_range_position_252d": {"inputs": ["evebit"], "func": vcl_ext_020_evebit_range_position_252d},
    "vcl_ext_021_marketcap_range_position_252d": {"inputs": ["marketcap"], "func": vcl_ext_021_marketcap_range_position_252d},
    "vcl_ext_022_ev_range_position_252d": {"inputs": ["ev"], "func": vcl_ext_022_ev_range_position_252d},
    "vcl_ext_023_pe_range_position_63d": {"inputs": ["pe"], "func": vcl_ext_023_pe_range_position_63d},
    "vcl_ext_024_pb_range_position_126d": {"inputs": ["pb"], "func": vcl_ext_024_pb_range_position_126d},
    "vcl_ext_025_pe_at_504d_low": {"inputs": ["pe"], "func": vcl_ext_025_pe_at_504d_low},
    "vcl_ext_026_pe_at_expanding_low": {"inputs": ["pe"], "func": vcl_ext_026_pe_at_expanding_low},
    "vcl_ext_027_pb_at_252d_low": {"inputs": ["pb"], "func": vcl_ext_027_pb_at_252d_low},
    "vcl_ext_028_pb_at_504d_low": {"inputs": ["pb"], "func": vcl_ext_028_pb_at_504d_low},
    "vcl_ext_029_ps_at_504d_low": {"inputs": ["ps"], "func": vcl_ext_029_ps_at_504d_low},
    "vcl_ext_030_ps_at_expanding_low": {"inputs": ["ps"], "func": vcl_ext_030_ps_at_expanding_low},
    "vcl_ext_031_evebitda_at_252d_low": {"inputs": ["evebitda"], "func": vcl_ext_031_evebitda_at_252d_low},
    "vcl_ext_032_pb_pct_above_504d_min": {"inputs": ["pb"], "func": vcl_ext_032_pb_pct_above_504d_min},
    "vcl_ext_033_pe_pct_above_504d_min": {"inputs": ["pe"], "func": vcl_ext_033_pe_pct_above_504d_min},
    "vcl_ext_034_ps_pct_above_504d_min": {"inputs": ["ps"], "func": vcl_ext_034_ps_pct_above_504d_min},
    "vcl_ext_035_evebitda_pct_above_252d_min": {"inputs": ["evebitda"], "func": vcl_ext_035_evebitda_pct_above_252d_min},
    "vcl_ext_036_marketcap_at_252d_low": {"inputs": ["marketcap"], "func": vcl_ext_036_marketcap_at_252d_low},
    "vcl_ext_037_pe_compression_pct_126d": {"inputs": ["pe"], "func": vcl_ext_037_pe_compression_pct_126d},
    "vcl_ext_038_pb_compression_pct_126d": {"inputs": ["pb"], "func": vcl_ext_038_pb_compression_pct_126d},
    "vcl_ext_039_ps_compression_pct_126d": {"inputs": ["ps"], "func": vcl_ext_039_ps_compression_pct_126d},
    "vcl_ext_040_pe_compression_pct_21d": {"inputs": ["pe"], "func": vcl_ext_040_pe_compression_pct_21d},
    "vcl_ext_041_pb_compression_pct_21d": {"inputs": ["pb"], "func": vcl_ext_041_pb_compression_pct_21d},
    "vcl_ext_042_pe_compression_pct_504d": {"inputs": ["pe"], "func": vcl_ext_042_pe_compression_pct_504d},
    "vcl_ext_043_pb_compression_pct_252d": {"inputs": ["pb"], "func": vcl_ext_043_pb_compression_pct_252d},
    "vcl_ext_044_evebitda_compression_pct_126d": {"inputs": ["evebitda"], "func": vcl_ext_044_evebitda_compression_pct_126d},
    "vcl_ext_045_evebit_compression_pct_126d": {"inputs": ["evebit"], "func": vcl_ext_045_evebit_compression_pct_126d},
    "vcl_ext_046_ps_compression_magnitude_126d": {"inputs": ["ps"], "func": vcl_ext_046_ps_compression_magnitude_126d},
    "vcl_ext_047_pe_compression_magnitude_126d": {"inputs": ["pe"], "func": vcl_ext_047_pe_compression_magnitude_126d},
    "vcl_ext_048_marketcap_compression_pct_252d": {"inputs": ["marketcap"], "func": vcl_ext_048_marketcap_compression_pct_252d},
    "vcl_ext_049_pe_compression_speed_63d": {"inputs": ["pe"], "func": vcl_ext_049_pe_compression_speed_63d},
    "vcl_ext_050_pb_compression_speed_63d": {"inputs": ["pb"], "func": vcl_ext_050_pb_compression_speed_63d},
    "vcl_ext_051_ps_compression_speed_21d": {"inputs": ["ps"], "func": vcl_ext_051_ps_compression_speed_21d},
    "vcl_ext_052_pe_compression_accel_63d": {"inputs": ["pe"], "func": vcl_ext_052_pe_compression_accel_63d},
    "vcl_ext_053_pb_compression_accel_63d": {"inputs": ["pb"], "func": vcl_ext_053_pb_compression_accel_63d},
    "vcl_ext_054_ps_derating_velocity_ewm": {"inputs": ["ps"], "func": vcl_ext_054_ps_derating_velocity_ewm},
    "vcl_ext_055_evebitda_derating_velocity_ewm": {"inputs": ["evebitda"], "func": vcl_ext_055_evebitda_derating_velocity_ewm},
    "vcl_ext_056_pe_declining_days_streak": {"inputs": ["pe"], "func": vcl_ext_056_pe_declining_days_streak},
    "vcl_ext_057_pb_declining_days_streak": {"inputs": ["pb"], "func": vcl_ext_057_pb_declining_days_streak},
    "vcl_ext_058_ps_declining_days_streak": {"inputs": ["ps"], "func": vcl_ext_058_ps_declining_days_streak},
    "vcl_ext_059_marketcap_declining_days_streak": {"inputs": ["marketcap"], "func": vcl_ext_059_marketcap_declining_days_streak},
    "vcl_ext_060_pe_compression_streak_252d": {"inputs": ["pe"], "func": vcl_ext_060_pe_compression_streak_252d},
    "vcl_ext_061_pe_zscore_504d": {"inputs": ["pe"], "func": vcl_ext_061_pe_zscore_504d},
    "vcl_ext_062_pb_zscore_252d": {"inputs": ["pb"], "func": vcl_ext_062_pb_zscore_252d},
    "vcl_ext_063_ps_zscore_252d": {"inputs": ["ps"], "func": vcl_ext_063_ps_zscore_252d},
    "vcl_ext_064_evebitda_zscore_252d": {"inputs": ["evebitda"], "func": vcl_ext_064_evebitda_zscore_252d},
    "vcl_ext_065_pe_rolling_rank_pct_504d": {"inputs": ["pe"], "func": vcl_ext_065_pe_rolling_rank_pct_504d},
    "vcl_ext_066_pb_rolling_rank_pct_504d": {"inputs": ["pb"], "func": vcl_ext_066_pb_rolling_rank_pct_504d},
    "vcl_ext_067_marketcap_rolling_rank_pct_252d": {"inputs": ["marketcap"], "func": vcl_ext_067_marketcap_rolling_rank_pct_252d},
    "vcl_ext_068_pb_ewm_deviation_21d": {"inputs": ["pb"], "func": vcl_ext_068_pb_ewm_deviation_21d},
    "vcl_ext_069_pe_ps_both_below_median_252d": {"inputs": ["pe", "ps"], "func": vcl_ext_069_pe_ps_both_below_median_252d},
    "vcl_ext_070_multiple_at_252d_low_count": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_ext_070_multiple_at_252d_low_count},
    "vcl_ext_071_deep_distress_score": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_ext_071_deep_distress_score},
    "vcl_ext_072_all_multiples_compressing_flag": {"inputs": ["pe", "pb", "ps"], "func": vcl_ext_072_all_multiples_compressing_flag},
    "vcl_ext_073_negative_multiple_count_4way": {"inputs": ["pe", "pb", "evebit", "evebitda"], "func": vcl_ext_073_negative_multiple_count_4way},
    "vcl_ext_074_composite_collapse_score_126d": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_ext_074_composite_collapse_score_126d},
    "vcl_ext_075_composite_range_position_score": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_ext_075_composite_range_position_score},
}
