"""
80_yield_distress — Base Features 001-100
Domain: dividend / earnings yield spikes as price collapses (yield = 1/multiple)
Inputs: daily-frequency Sharadar DAILY/METRICS valuation fields only.
  Canonical fields: pe, ps, pb, evebit, evebitda, divyield, marketcap, ev
  These are native daily-frequency series — no quarterly forward-fill needed.
All feature functions are strictly backward-looking; no forward information is used.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_HALF  = 126
_TD_QTR   =  63
_TD_MON   =  21
_TD_WEEK  =   5
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero/near-zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _to_yield(multiple: pd.Series) -> pd.Series:
    """Convert a valuation multiple to a yield (1/multiple).
    Negative or near-zero multiples produce NaN to avoid sign-flipped distress
    signals. Only positive multiples give meaningful yields.
    """
    m = multiple.copy().astype(float)
    m[m.abs() < _EPS] = np.nan
    m[m < 0] = np.nan
    return 1.0 / m


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Raw earnings-yield level and spike measures ---

def yld_001_earnings_yield(pe: pd.Series) -> pd.Series:
    """Earnings yield = 1/PE; NaN when PE is negative or near-zero."""
    return _to_yield(pe)


def yld_002_earnings_yield_vs_21d_avg(pe: pd.Series) -> pd.Series:
    """Earnings yield minus its 21-day rolling mean (short-term spike)."""
    ey = _to_yield(pe)
    return ey - _rolling_mean(ey, _TD_MON)


def yld_003_earnings_yield_vs_63d_avg(pe: pd.Series) -> pd.Series:
    """Earnings yield minus its 63-day rolling mean (quarterly spike)."""
    ey = _to_yield(pe)
    return ey - _rolling_mean(ey, _TD_QTR)


def yld_004_earnings_yield_vs_252d_avg(pe: pd.Series) -> pd.Series:
    """Earnings yield minus its 252-day rolling mean (annual spike)."""
    ey = _to_yield(pe)
    return ey - _rolling_mean(ey, _TD_YEAR)


def yld_005_earnings_yield_21d_max_ratio(pe: pd.Series) -> pd.Series:
    """Earnings yield as fraction of its 21-day rolling max (recency of the spike)."""
    ey = _to_yield(pe)
    return _safe_div(ey, _rolling_max(ey, _TD_MON))


def yld_006_earnings_yield_252d_max_ratio(pe: pd.Series) -> pd.Series:
    """Earnings yield as fraction of its 252-day rolling max."""
    ey = _to_yield(pe)
    return _safe_div(ey, _rolling_max(ey, _TD_YEAR))


def yld_007_earnings_yield_expanding_max_ratio(pe: pd.Series) -> pd.Series:
    """Earnings yield vs expanding (all-history) maximum yield."""
    ey = _to_yield(pe)
    return _safe_div(ey, ey.expanding(min_periods=1).max())


def yld_008_earnings_yield_zscore_252d(pe: pd.Series) -> pd.Series:
    """Z-score of earnings yield over trailing 252 days."""
    return _zscore_rolling(_to_yield(pe), _TD_YEAR)


def yld_009_earnings_yield_zscore_504d(pe: pd.Series) -> pd.Series:
    """Z-score of earnings yield over trailing 504 days."""
    return _zscore_rolling(_to_yield(pe), 504)


def yld_010_earnings_yield_pct_rank_252d(pe: pd.Series) -> pd.Series:
    """Percentile rank of earnings yield within trailing 252-day window."""
    return _rolling_rank_pct(_to_yield(pe), _TD_YEAR)


def yld_011_earnings_yield_pct_rank_1260d(pe: pd.Series) -> pd.Series:
    """Percentile rank of earnings yield within trailing 1260-day (5-yr) window."""
    return _rolling_rank_pct(_to_yield(pe), 1260)


def yld_012_earnings_yield_expanding_pct_rank(pe: pd.Series) -> pd.Series:
    """Expanding percentile rank of earnings yield (all-history rank)."""
    return _to_yield(pe).expanding(min_periods=5).rank(pct=True)


# --- Group B (013-024): Sales-yield level and spike measures ---

def yld_013_sales_yield(ps: pd.Series) -> pd.Series:
    """Sales yield = 1/PS; NaN when PS is negative or near-zero."""
    return _to_yield(ps)


def yld_014_sales_yield_vs_21d_avg(ps: pd.Series) -> pd.Series:
    """Sales yield minus its 21-day rolling mean."""
    sy = _to_yield(ps)
    return sy - _rolling_mean(sy, _TD_MON)


def yld_015_sales_yield_vs_252d_avg(ps: pd.Series) -> pd.Series:
    """Sales yield minus its 252-day rolling mean."""
    sy = _to_yield(ps)
    return sy - _rolling_mean(sy, _TD_YEAR)


def yld_016_sales_yield_zscore_252d(ps: pd.Series) -> pd.Series:
    """Z-score of sales yield over trailing 252 days."""
    return _zscore_rolling(_to_yield(ps), _TD_YEAR)


def yld_017_sales_yield_pct_rank_252d(ps: pd.Series) -> pd.Series:
    """Percentile rank of sales yield within trailing 252-day window."""
    return _rolling_rank_pct(_to_yield(ps), _TD_YEAR)


def yld_018_sales_yield_expanding_max_ratio(ps: pd.Series) -> pd.Series:
    """Sales yield vs its expanding historical maximum."""
    sy = _to_yield(ps)
    return _safe_div(sy, sy.expanding(min_periods=1).max())


def yld_019_sales_yield_vs_63d_median(ps: pd.Series) -> pd.Series:
    """Sales yield minus its 63-day rolling median."""
    sy = _to_yield(ps)
    return sy - _rolling_median(sy, _TD_QTR)


def yld_020_sales_yield_252d_drawup(ps: pd.Series) -> pd.Series:
    """Sales-yield drawup: current yield minus 252-day rolling minimum yield."""
    sy = _to_yield(ps)
    return sy - _rolling_min(sy, _TD_YEAR)


def yld_021_sales_yield_zscore_1260d(ps: pd.Series) -> pd.Series:
    """Z-score of sales yield over trailing 1260 days (5-year context)."""
    return _zscore_rolling(_to_yield(ps), 1260)


def yld_022_sales_yield_expanding_zscore(ps: pd.Series) -> pd.Series:
    """Expanding z-score of sales yield (how extreme vs own full history)."""
    sy = _to_yield(ps)
    m  = sy.expanding(min_periods=5).mean()
    sd = sy.expanding(min_periods=5).std()
    return _safe_div(sy - m, sd)


def yld_023_sales_yield_above_2x_avg(ps: pd.Series) -> pd.Series:
    """Binary: sales yield is more than 2x its 252-day average (extreme spike)."""
    sy  = _to_yield(ps)
    avg = _rolling_mean(sy, _TD_YEAR)
    return (sy > 2.0 * avg).astype(float)


def yld_024_sales_yield_above_3x_avg(ps: pd.Series) -> pd.Series:
    """Binary: sales yield is more than 3x its 252-day average."""
    sy  = _to_yield(ps)
    avg = _rolling_mean(sy, _TD_YEAR)
    return (sy > 3.0 * avg).astype(float)


# --- Group C (025-036): Book-yield level and spike measures ---

def yld_025_book_yield(pb: pd.Series) -> pd.Series:
    """Book yield = 1/PB; NaN when PB is negative or near-zero."""
    return _to_yield(pb)


def yld_026_book_yield_vs_252d_avg(pb: pd.Series) -> pd.Series:
    """Book yield minus its 252-day rolling mean."""
    by = _to_yield(pb)
    return by - _rolling_mean(by, _TD_YEAR)


def yld_027_book_yield_zscore_252d(pb: pd.Series) -> pd.Series:
    """Z-score of book yield over trailing 252 days."""
    return _zscore_rolling(_to_yield(pb), _TD_YEAR)


def yld_028_book_yield_pct_rank_252d(pb: pd.Series) -> pd.Series:
    """Percentile rank of book yield within trailing 252-day window."""
    return _rolling_rank_pct(_to_yield(pb), _TD_YEAR)


def yld_029_book_yield_expanding_max_ratio(pb: pd.Series) -> pd.Series:
    """Book yield vs its expanding historical maximum."""
    by = _to_yield(pb)
    return _safe_div(by, by.expanding(min_periods=1).max())


def yld_030_book_yield_252d_drawup(pb: pd.Series) -> pd.Series:
    """Book-yield drawup: current yield minus 252-day rolling minimum."""
    by = _to_yield(pb)
    return by - _rolling_min(by, _TD_YEAR)


def yld_031_book_yield_above_1(pb: pd.Series) -> pd.Series:
    """Binary: book yield > 1.0 (i.e., PB < 1 — below book value)."""
    return (_to_yield(pb) > 1.0).astype(float)


def yld_032_book_yield_above_2(pb: pd.Series) -> pd.Series:
    """Binary: book yield > 2.0 (i.e., PB < 0.5 — severe discount to book)."""
    return (_to_yield(pb) > 2.0).astype(float)


def yld_033_book_yield_expanding_pct_rank(pb: pd.Series) -> pd.Series:
    """Expanding percentile rank of book yield."""
    return _to_yield(pb).expanding(min_periods=5).rank(pct=True)


def yld_034_book_yield_vs_63d_avg(pb: pd.Series) -> pd.Series:
    """Book yield minus its 63-day rolling mean."""
    by = _to_yield(pb)
    return by - _rolling_mean(by, _TD_QTR)


def yld_035_book_yield_ewm_deviation(pb: pd.Series) -> pd.Series:
    """Book yield minus 63-day EMA of book yield."""
    by = _to_yield(pb)
    return by - _ewm_mean(by, _TD_QTR)


def yld_036_book_yield_zscore_504d(pb: pd.Series) -> pd.Series:
    """Z-score of book yield over trailing 504 days (2-year context)."""
    return _zscore_rolling(_to_yield(pb), 504)


# --- Group D (037-048): EBIT and EBITDA yield measures ---

def yld_037_ebit_yield(evebit: pd.Series) -> pd.Series:
    """EBIT yield = 1/(EV/EBIT); NaN when EV/EBIT is negative or near-zero."""
    return _to_yield(evebit)


def yld_038_ebit_yield_vs_252d_avg(evebit: pd.Series) -> pd.Series:
    """EBIT yield minus its 252-day rolling mean."""
    ey = _to_yield(evebit)
    return ey - _rolling_mean(ey, _TD_YEAR)


def yld_039_ebit_yield_zscore_252d(evebit: pd.Series) -> pd.Series:
    """Z-score of EBIT yield over trailing 252 days."""
    return _zscore_rolling(_to_yield(evebit), _TD_YEAR)


def yld_040_ebit_yield_pct_rank_252d(evebit: pd.Series) -> pd.Series:
    """Percentile rank of EBIT yield within trailing 252-day window."""
    return _rolling_rank_pct(_to_yield(evebit), _TD_YEAR)


def yld_041_ebit_yield_expanding_max_ratio(evebit: pd.Series) -> pd.Series:
    """EBIT yield vs its expanding historical maximum."""
    ey = _to_yield(evebit)
    return _safe_div(ey, ey.expanding(min_periods=1).max())


def yld_042_ebit_yield_252d_drawup(evebit: pd.Series) -> pd.Series:
    """EBIT-yield drawup: current yield minus 252-day rolling minimum."""
    ey = _to_yield(evebit)
    return ey - _rolling_min(ey, _TD_YEAR)


def yld_043_ebitda_yield(evebitda: pd.Series) -> pd.Series:
    """EBITDA yield = 1/(EV/EBITDA); NaN when multiple is negative or near-zero."""
    return _to_yield(evebitda)


def yld_044_ebitda_yield_vs_252d_avg(evebitda: pd.Series) -> pd.Series:
    """EBITDA yield minus its 252-day rolling mean."""
    ey = _to_yield(evebitda)
    return ey - _rolling_mean(ey, _TD_YEAR)


def yld_045_ebitda_yield_zscore_252d(evebitda: pd.Series) -> pd.Series:
    """Z-score of EBITDA yield over trailing 252 days."""
    return _zscore_rolling(_to_yield(evebitda), _TD_YEAR)


def yld_046_ebitda_yield_pct_rank_252d(evebitda: pd.Series) -> pd.Series:
    """Percentile rank of EBITDA yield within trailing 252-day window."""
    return _rolling_rank_pct(_to_yield(evebitda), _TD_YEAR)


def yld_047_ebitda_yield_expanding_max_ratio(evebitda: pd.Series) -> pd.Series:
    """EBITDA yield vs its expanding historical maximum."""
    ey = _to_yield(evebitda)
    return _safe_div(ey, ey.expanding(min_periods=1).max())


def yld_048_ebitda_yield_expanding_zscore(evebitda: pd.Series) -> pd.Series:
    """Expanding z-score of EBITDA yield."""
    ey = _to_yield(evebitda)
    m  = ey.expanding(min_periods=5).mean()
    sd = ey.expanding(min_periods=5).std()
    return _safe_div(ey - m, sd)


# --- Group E (049-060): Dividend-yield distress measures ---

def yld_049_divyield_vs_21d_avg(divyield: pd.Series) -> pd.Series:
    """Dividend yield minus its 21-day rolling mean (short-term spike)."""
    return divyield - _rolling_mean(divyield, _TD_MON)


def yld_050_divyield_vs_252d_avg(divyield: pd.Series) -> pd.Series:
    """Dividend yield minus its 252-day rolling mean (annual spike)."""
    return divyield - _rolling_mean(divyield, _TD_YEAR)


def yld_051_divyield_zscore_252d(divyield: pd.Series) -> pd.Series:
    """Z-score of dividend yield over trailing 252 days."""
    return _zscore_rolling(divyield, _TD_YEAR)


def yld_052_divyield_pct_rank_252d(divyield: pd.Series) -> pd.Series:
    """Percentile rank of dividend yield within trailing 252-day window."""
    return _rolling_rank_pct(divyield, _TD_YEAR)


def yld_053_divyield_expanding_max_ratio(divyield: pd.Series) -> pd.Series:
    """Dividend yield vs its expanding historical maximum (trap proximity)."""
    return _safe_div(divyield, divyield.expanding(min_periods=1).max())


def yld_054_divyield_above_8pct(divyield: pd.Series) -> pd.Series:
    """Binary: dividend yield > 8% (market may be pricing a dividend cut)."""
    return (divyield > 0.08).astype(float)


def yld_055_divyield_above_10pct(divyield: pd.Series) -> pd.Series:
    """Binary: dividend yield > 10% (extreme yield-trap distress signal)."""
    return (divyield > 0.10).astype(float)


def yld_056_divyield_above_15pct(divyield: pd.Series) -> pd.Series:
    """Binary: dividend yield > 15% (near-certain pricing of a dividend cut)."""
    return (divyield > 0.15).astype(float)


def yld_057_divyield_252d_drawup(divyield: pd.Series) -> pd.Series:
    """Dividend-yield drawup: current yield minus 252-day rolling minimum."""
    return divyield - _rolling_min(divyield, _TD_YEAR)


def yld_058_divyield_pct_rank_1260d(divyield: pd.Series) -> pd.Series:
    """Percentile rank of dividend yield within trailing 5-year window."""
    return _rolling_rank_pct(divyield, 1260)


def yld_059_divyield_expanding_zscore(divyield: pd.Series) -> pd.Series:
    """Expanding z-score of dividend yield (how extreme vs own full history)."""
    m  = divyield.expanding(min_periods=5).mean()
    sd = divyield.expanding(min_periods=5).std()
    return _safe_div(divyield - m, sd)


def yld_060_divyield_consecutive_rise_21d(divyield: pd.Series) -> pd.Series:
    """Count of consecutive days dividend yield is rising within trailing 21 days."""
    rising = (divyield.diff(1) > 0).astype(float)
    return _rolling_sum(rising, _TD_MON)


# --- Group F (061-075): Cross-yield divergence and composite distress signals ---

def yld_061_div_vs_earnings_yield_spread(divyield: pd.Series, pe: pd.Series) -> pd.Series:
    """Dividend yield minus earnings yield (> 0 means payout exceeds earnings — trap)."""
    return divyield - _to_yield(pe)


def yld_062_div_earnings_payout_ratio_implied(divyield: pd.Series, pe: pd.Series) -> pd.Series:
    """Implied payout ratio: dividend yield / earnings yield (= divyield * PE)."""
    ey = _to_yield(pe)
    return _safe_div(divyield, ey)


def yld_063_div_vs_sales_yield_ratio(divyield: pd.Series, ps: pd.Series) -> pd.Series:
    """Ratio of dividend yield to sales yield (payout vs revenue backing)."""
    return _safe_div(divyield, _to_yield(ps))


def yld_064_earnings_vs_ebitda_yield_spread(pe: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Earnings yield minus EBITDA yield (gap measures leverage / D&A burden)."""
    return _to_yield(pe) - _to_yield(evebitda)


def yld_065_ebit_vs_ebitda_yield_spread(evebit: pd.Series, evebitda: pd.Series) -> pd.Series:
    """EBIT yield minus EBITDA yield (proxy for D&A intensity)."""
    return _to_yield(evebit) - _to_yield(evebitda)


def yld_066_composite_yield_avg(pe: pd.Series, ps: pd.Series, pb: pd.Series) -> pd.Series:
    """Simple average of earnings, sales and book yields (composite cheapness)."""
    return (_to_yield(pe).fillna(0) + _to_yield(ps).fillna(0) + _to_yield(pb).fillna(0)) / 3.0


def yld_067_composite_yield_zscore(pe: pd.Series, ps: pd.Series, pb: pd.Series) -> pd.Series:
    """Z-score of composite yield average over trailing 252 days."""
    comp = (_to_yield(pe).fillna(0) + _to_yield(ps).fillna(0) + _to_yield(pb).fillna(0)) / 3.0
    return _zscore_rolling(comp, _TD_YEAR)


def yld_068_earnings_yield_above_20pct(pe: pd.Series) -> pd.Series:
    """Binary: earnings yield > 20% (PE < 5 — market disbelieving earnings)."""
    return (_to_yield(pe) > 0.20).astype(float)


def yld_069_earnings_yield_above_33pct(pe: pd.Series) -> pd.Series:
    """Binary: earnings yield > 33% (PE < 3 — extreme distress pricing)."""
    return (_to_yield(pe) > 0.33).astype(float)


def yld_070_divyield_minus_ebitda_yield(divyield: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Dividend yield minus EBITDA yield (negative = EBITDA covers dividend)."""
    return divyield - _to_yield(evebitda)


def yld_071_yield_spike_breadth_3(pe: pd.Series, ps: pd.Series, pb: pd.Series) -> pd.Series:
    """Count (0-3) of yields above their 252-day 90th-percentile (spike breadth)."""
    ey  = _to_yield(pe)
    sy  = _to_yield(ps)
    by  = _to_yield(pb)
    q90e = ey.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    q90s = sy.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    q90b = by.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    return (
        (ey > q90e).astype(float) +
        (sy > q90s).astype(float) +
        (by > q90b).astype(float)
    )


def yld_072_yield_spike_breadth_5(pe: pd.Series, ps: pd.Series, pb: pd.Series,
                                   evebit: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Count (0-5) of yields above their 252-day 90th-percentile (wide-breadth)."""
    yields = [_to_yield(pe), _to_yield(ps), _to_yield(pb),
              _to_yield(evebit), _to_yield(evebitda)]
    total = pd.Series(0.0, index=pe.index)
    for y in yields:
        q90 = y.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
        total = total + (y > q90).astype(float)
    return total


def yld_073_ebit_yield_above_20pct(evebit: pd.Series) -> pd.Series:
    """Binary: EBIT yield > 20% (EV/EBIT < 5 — severe operational discount)."""
    return (_to_yield(evebit) > 0.20).astype(float)


def yld_074_divyield_2x_252d_avg(divyield: pd.Series) -> pd.Series:
    """Binary: dividend yield > 2x its 252-day average (yield trap signature)."""
    avg = _rolling_mean(divyield, _TD_YEAR)
    return (divyield > 2.0 * avg).astype(float)


def yld_075_earnings_yield_504d_drawup(pe: pd.Series) -> pd.Series:
    """Earnings-yield drawup: current yield minus 504-day rolling minimum yield."""
    ey = _to_yield(pe)
    return ey - _rolling_min(ey, 504)


# --- Group G-ext (151-175): Additional window / normalization variants ---

def yld_151_earnings_yield_126d_drawup(pe: pd.Series) -> pd.Series:
    """Earnings-yield drawup: current yield minus 126-day (half-year) rolling minimum."""
    ey = _to_yield(pe)
    return ey - _rolling_min(ey, _TD_HALF)


def yld_152_sales_yield_pct_rank_504d(ps: pd.Series) -> pd.Series:
    """Percentile rank of sales yield within trailing 504-day (2-year) window."""
    return _rolling_rank_pct(_to_yield(ps), 504)


def yld_153_book_yield_pct_rank_504d(pb: pd.Series) -> pd.Series:
    """Percentile rank of book yield within trailing 504-day window."""
    return _rolling_rank_pct(_to_yield(pb), 504)


def yld_154_ebitda_yield_zscore_504d(evebitda: pd.Series) -> pd.Series:
    """Z-score of EBITDA yield over trailing 504 days (2-year context)."""
    return _zscore_rolling(_to_yield(evebitda), 504)


def yld_155_ebit_yield_zscore_504d(evebit: pd.Series) -> pd.Series:
    """Z-score of EBIT yield over trailing 504 days."""
    return _zscore_rolling(_to_yield(evebit), 504)


def yld_156_divyield_vs_63d_avg(divyield: pd.Series) -> pd.Series:
    """Dividend yield minus its 63-day rolling mean (quarterly spike deviation)."""
    return divyield - _rolling_mean(divyield, _TD_QTR)


def yld_157_divyield_vs_126d_avg(divyield: pd.Series) -> pd.Series:
    """Dividend yield minus its 126-day rolling mean."""
    return divyield - _rolling_mean(divyield, _TD_HALF)


def yld_158_earnings_yield_63d_max_ratio(pe: pd.Series) -> pd.Series:
    """Earnings yield as fraction of its 63-day rolling maximum."""
    ey = _to_yield(pe)
    return _safe_div(ey, _rolling_max(ey, _TD_QTR))


def yld_159_sales_yield_126d_drawup(ps: pd.Series) -> pd.Series:
    """Sales-yield drawup: current yield minus 126-day rolling minimum."""
    sy = _to_yield(ps)
    return sy - _rolling_min(sy, _TD_HALF)


def yld_160_book_yield_126d_drawup(pb: pd.Series) -> pd.Series:
    """Book-yield drawup: current yield minus 126-day rolling minimum."""
    by = _to_yield(pb)
    return by - _rolling_min(by, _TD_HALF)


def yld_161_ebit_yield_expanding_pct_rank(evebit: pd.Series) -> pd.Series:
    """Expanding percentile rank of EBIT yield (all-history rank)."""
    return _to_yield(evebit).expanding(min_periods=5).rank(pct=True)


def yld_162_ebitda_yield_expanding_pct_rank(evebitda: pd.Series) -> pd.Series:
    """Expanding percentile rank of EBITDA yield (all-history rank)."""
    return _to_yield(evebitda).expanding(min_periods=5).rank(pct=True)


def yld_163_divyield_zscore_504d(divyield: pd.Series) -> pd.Series:
    """Z-score of dividend yield over trailing 504 days."""
    return _zscore_rolling(divyield, 504)


def yld_164_sales_yield_ewm63_dev(ps: pd.Series) -> pd.Series:
    """Sales yield minus its 63-day EMA (medium-term EWM deviation)."""
    sy = _to_yield(ps)
    return sy - _ewm_mean(sy, _TD_QTR)


def yld_165_ebit_yield_ewm63_dev(evebit: pd.Series) -> pd.Series:
    """EBIT yield minus its 63-day EMA."""
    ey = _to_yield(evebit)
    return ey - _ewm_mean(ey, _TD_QTR)


def yld_166_earnings_yield_above_50pct(pe: pd.Series) -> pd.Series:
    """Binary: earnings yield > 50% (PE < 2 — extreme distress / breakup valuation)."""
    return (_to_yield(pe) > 0.50).astype(float)


def yld_167_book_yield_above_3(pb: pd.Series) -> pd.Series:
    """Binary: book yield > 3.0 (PB < 0.33 — catastrophic discount to book)."""
    return (_to_yield(pb) > 3.0).astype(float)


def yld_168_divyield_above_20pct(divyield: pd.Series) -> pd.Series:
    """Binary: dividend yield > 20% (near-certain pricing of suspension)."""
    return (divyield > 0.20).astype(float)


def yld_169_ebitda_yield_above_20pct(evebitda: pd.Series) -> pd.Series:
    """Binary: EBITDA yield > 20% (EV/EBITDA < 5 — severe distress discount)."""
    return (_to_yield(evebitda) > 0.20).astype(float)


def yld_170_earnings_yield_vs_126d_avg(pe: pd.Series) -> pd.Series:
    """Earnings yield minus its 126-day rolling mean (half-year spike)."""
    ey = _to_yield(pe)
    return ey - _rolling_mean(ey, _TD_HALF)


def yld_171_sales_yield_zscore_504d(ps: pd.Series) -> pd.Series:
    """Z-score of sales yield over trailing 504 days."""
    return _zscore_rolling(_to_yield(ps), 504)


def yld_172_book_yield_zscore_1260d(pb: pd.Series) -> pd.Series:
    """Z-score of book yield over trailing 1260 days (5-year context)."""
    return _zscore_rolling(_to_yield(pb), 1260)


def yld_173_mcap_expanding_pct_rank(marketcap: pd.Series) -> pd.Series:
    """Expanding percentile rank of market cap (all-time size-collapse signal)."""
    return marketcap.expanding(min_periods=5).rank(pct=True)


def yld_174_ev_expanding_pct_rank(ev: pd.Series) -> pd.Series:
    """Expanding percentile rank of EV (all-time enterprise-value collapse)."""
    return ev.expanding(min_periods=5).rank(pct=True)


def yld_175_yield_spike_breadth_6(pe: pd.Series, ps: pd.Series, pb: pd.Series,
                                   evebit: pd.Series, evebitda: pd.Series,
                                   divyield: pd.Series) -> pd.Series:
    """Count (0-6) of all yields above their 252-day 95th-percentile (extreme breadth)."""
    yields = [_to_yield(pe), _to_yield(ps), _to_yield(pb),
              _to_yield(evebit), _to_yield(evebitda), divyield]
    total = pd.Series(0.0, index=pe.index)
    for y in yields:
        q95 = y.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.95)
        total = total + (y > q95).astype(float)
    return total


# ── Registry ──────────────────────────────────────────────────────────────────

YIELD_DISTRESS_REGISTRY_001_075 = {
    "yld_001_earnings_yield":                    {"inputs": ["pe"],                                     "func": yld_001_earnings_yield},
    "yld_002_earnings_yield_vs_21d_avg":         {"inputs": ["pe"],                                     "func": yld_002_earnings_yield_vs_21d_avg},
    "yld_003_earnings_yield_vs_63d_avg":         {"inputs": ["pe"],                                     "func": yld_003_earnings_yield_vs_63d_avg},
    "yld_004_earnings_yield_vs_252d_avg":        {"inputs": ["pe"],                                     "func": yld_004_earnings_yield_vs_252d_avg},
    "yld_005_earnings_yield_21d_max_ratio":      {"inputs": ["pe"],                                     "func": yld_005_earnings_yield_21d_max_ratio},
    "yld_006_earnings_yield_252d_max_ratio":     {"inputs": ["pe"],                                     "func": yld_006_earnings_yield_252d_max_ratio},
    "yld_007_earnings_yield_expanding_max_ratio":{"inputs": ["pe"],                                     "func": yld_007_earnings_yield_expanding_max_ratio},
    "yld_008_earnings_yield_zscore_252d":        {"inputs": ["pe"],                                     "func": yld_008_earnings_yield_zscore_252d},
    "yld_009_earnings_yield_zscore_504d":        {"inputs": ["pe"],                                     "func": yld_009_earnings_yield_zscore_504d},
    "yld_010_earnings_yield_pct_rank_252d":      {"inputs": ["pe"],                                     "func": yld_010_earnings_yield_pct_rank_252d},
    "yld_011_earnings_yield_pct_rank_1260d":     {"inputs": ["pe"],                                     "func": yld_011_earnings_yield_pct_rank_1260d},
    "yld_012_earnings_yield_expanding_pct_rank": {"inputs": ["pe"],                                     "func": yld_012_earnings_yield_expanding_pct_rank},
    "yld_013_sales_yield":                       {"inputs": ["ps"],                                     "func": yld_013_sales_yield},
    "yld_014_sales_yield_vs_21d_avg":            {"inputs": ["ps"],                                     "func": yld_014_sales_yield_vs_21d_avg},
    "yld_015_sales_yield_vs_252d_avg":           {"inputs": ["ps"],                                     "func": yld_015_sales_yield_vs_252d_avg},
    "yld_016_sales_yield_zscore_252d":           {"inputs": ["ps"],                                     "func": yld_016_sales_yield_zscore_252d},
    "yld_017_sales_yield_pct_rank_252d":         {"inputs": ["ps"],                                     "func": yld_017_sales_yield_pct_rank_252d},
    "yld_018_sales_yield_expanding_max_ratio":   {"inputs": ["ps"],                                     "func": yld_018_sales_yield_expanding_max_ratio},
    "yld_019_sales_yield_vs_63d_median":         {"inputs": ["ps"],                                     "func": yld_019_sales_yield_vs_63d_median},
    "yld_020_sales_yield_252d_drawup":           {"inputs": ["ps"],                                     "func": yld_020_sales_yield_252d_drawup},
    "yld_021_sales_yield_zscore_1260d":          {"inputs": ["ps"],                                     "func": yld_021_sales_yield_zscore_1260d},
    "yld_022_sales_yield_expanding_zscore":      {"inputs": ["ps"],                                     "func": yld_022_sales_yield_expanding_zscore},
    "yld_023_sales_yield_above_2x_avg":          {"inputs": ["ps"],                                     "func": yld_023_sales_yield_above_2x_avg},
    "yld_024_sales_yield_above_3x_avg":          {"inputs": ["ps"],                                     "func": yld_024_sales_yield_above_3x_avg},
    "yld_025_book_yield":                        {"inputs": ["pb"],                                     "func": yld_025_book_yield},
    "yld_026_book_yield_vs_252d_avg":            {"inputs": ["pb"],                                     "func": yld_026_book_yield_vs_252d_avg},
    "yld_027_book_yield_zscore_252d":            {"inputs": ["pb"],                                     "func": yld_027_book_yield_zscore_252d},
    "yld_028_book_yield_pct_rank_252d":          {"inputs": ["pb"],                                     "func": yld_028_book_yield_pct_rank_252d},
    "yld_029_book_yield_expanding_max_ratio":    {"inputs": ["pb"],                                     "func": yld_029_book_yield_expanding_max_ratio},
    "yld_030_book_yield_252d_drawup":            {"inputs": ["pb"],                                     "func": yld_030_book_yield_252d_drawup},
    "yld_031_book_yield_above_1":                {"inputs": ["pb"],                                     "func": yld_031_book_yield_above_1},
    "yld_032_book_yield_above_2":                {"inputs": ["pb"],                                     "func": yld_032_book_yield_above_2},
    "yld_033_book_yield_expanding_pct_rank":     {"inputs": ["pb"],                                     "func": yld_033_book_yield_expanding_pct_rank},
    "yld_034_book_yield_vs_63d_avg":             {"inputs": ["pb"],                                     "func": yld_034_book_yield_vs_63d_avg},
    "yld_035_book_yield_ewm_deviation":          {"inputs": ["pb"],                                     "func": yld_035_book_yield_ewm_deviation},
    "yld_036_book_yield_zscore_504d":            {"inputs": ["pb"],                                     "func": yld_036_book_yield_zscore_504d},
    "yld_037_ebit_yield":                        {"inputs": ["evebit"],                                 "func": yld_037_ebit_yield},
    "yld_038_ebit_yield_vs_252d_avg":            {"inputs": ["evebit"],                                 "func": yld_038_ebit_yield_vs_252d_avg},
    "yld_039_ebit_yield_zscore_252d":            {"inputs": ["evebit"],                                 "func": yld_039_ebit_yield_zscore_252d},
    "yld_040_ebit_yield_pct_rank_252d":          {"inputs": ["evebit"],                                 "func": yld_040_ebit_yield_pct_rank_252d},
    "yld_041_ebit_yield_expanding_max_ratio":    {"inputs": ["evebit"],                                 "func": yld_041_ebit_yield_expanding_max_ratio},
    "yld_042_ebit_yield_252d_drawup":            {"inputs": ["evebit"],                                 "func": yld_042_ebit_yield_252d_drawup},
    "yld_043_ebitda_yield":                      {"inputs": ["evebitda"],                               "func": yld_043_ebitda_yield},
    "yld_044_ebitda_yield_vs_252d_avg":          {"inputs": ["evebitda"],                               "func": yld_044_ebitda_yield_vs_252d_avg},
    "yld_045_ebitda_yield_zscore_252d":          {"inputs": ["evebitda"],                               "func": yld_045_ebitda_yield_zscore_252d},
    "yld_046_ebitda_yield_pct_rank_252d":        {"inputs": ["evebitda"],                               "func": yld_046_ebitda_yield_pct_rank_252d},
    "yld_047_ebitda_yield_expanding_max_ratio":  {"inputs": ["evebitda"],                               "func": yld_047_ebitda_yield_expanding_max_ratio},
    "yld_048_ebitda_yield_expanding_zscore":     {"inputs": ["evebitda"],                               "func": yld_048_ebitda_yield_expanding_zscore},
    "yld_049_divyield_vs_21d_avg":               {"inputs": ["divyield"],                               "func": yld_049_divyield_vs_21d_avg},
    "yld_050_divyield_vs_252d_avg":              {"inputs": ["divyield"],                               "func": yld_050_divyield_vs_252d_avg},
    "yld_051_divyield_zscore_252d":              {"inputs": ["divyield"],                               "func": yld_051_divyield_zscore_252d},
    "yld_052_divyield_pct_rank_252d":            {"inputs": ["divyield"],                               "func": yld_052_divyield_pct_rank_252d},
    "yld_053_divyield_expanding_max_ratio":      {"inputs": ["divyield"],                               "func": yld_053_divyield_expanding_max_ratio},
    "yld_054_divyield_above_8pct":               {"inputs": ["divyield"],                               "func": yld_054_divyield_above_8pct},
    "yld_055_divyield_above_10pct":              {"inputs": ["divyield"],                               "func": yld_055_divyield_above_10pct},
    "yld_056_divyield_above_15pct":              {"inputs": ["divyield"],                               "func": yld_056_divyield_above_15pct},
    "yld_057_divyield_252d_drawup":              {"inputs": ["divyield"],                               "func": yld_057_divyield_252d_drawup},
    "yld_058_divyield_pct_rank_1260d":           {"inputs": ["divyield"],                               "func": yld_058_divyield_pct_rank_1260d},
    "yld_059_divyield_expanding_zscore":         {"inputs": ["divyield"],                               "func": yld_059_divyield_expanding_zscore},
    "yld_060_divyield_consecutive_rise_21d":     {"inputs": ["divyield"],                               "func": yld_060_divyield_consecutive_rise_21d},
    "yld_061_div_vs_earnings_yield_spread":      {"inputs": ["divyield", "pe"],                         "func": yld_061_div_vs_earnings_yield_spread},
    "yld_062_div_earnings_payout_ratio_implied": {"inputs": ["divyield", "pe"],                         "func": yld_062_div_earnings_payout_ratio_implied},
    "yld_063_div_vs_sales_yield_ratio":          {"inputs": ["divyield", "ps"],                         "func": yld_063_div_vs_sales_yield_ratio},
    "yld_064_earnings_vs_ebitda_yield_spread":   {"inputs": ["pe", "evebitda"],                         "func": yld_064_earnings_vs_ebitda_yield_spread},
    "yld_065_ebit_vs_ebitda_yield_spread":       {"inputs": ["evebit", "evebitda"],                     "func": yld_065_ebit_vs_ebitda_yield_spread},
    "yld_066_composite_yield_avg":               {"inputs": ["pe", "ps", "pb"],                         "func": yld_066_composite_yield_avg},
    "yld_067_composite_yield_zscore":            {"inputs": ["pe", "ps", "pb"],                         "func": yld_067_composite_yield_zscore},
    "yld_068_earnings_yield_above_20pct":        {"inputs": ["pe"],                                     "func": yld_068_earnings_yield_above_20pct},
    "yld_069_earnings_yield_above_33pct":        {"inputs": ["pe"],                                     "func": yld_069_earnings_yield_above_33pct},
    "yld_070_divyield_minus_ebitda_yield":       {"inputs": ["divyield", "evebitda"],                   "func": yld_070_divyield_minus_ebitda_yield},
    "yld_071_yield_spike_breadth_3":             {"inputs": ["pe", "ps", "pb"],                         "func": yld_071_yield_spike_breadth_3},
    "yld_072_yield_spike_breadth_5":             {"inputs": ["pe", "ps", "pb", "evebit", "evebitda"],   "func": yld_072_yield_spike_breadth_5},
    "yld_073_ebit_yield_above_20pct":            {"inputs": ["evebit"],                                 "func": yld_073_ebit_yield_above_20pct},
    "yld_074_divyield_2x_252d_avg":              {"inputs": ["divyield"],                               "func": yld_074_divyield_2x_252d_avg},
    "yld_075_earnings_yield_504d_drawup":        {"inputs": ["pe"],                                     "func": yld_075_earnings_yield_504d_drawup},
    "yld_151_earnings_yield_126d_drawup":        {"inputs": ["pe"],                                     "func": yld_151_earnings_yield_126d_drawup},
    "yld_152_sales_yield_pct_rank_504d":         {"inputs": ["ps"],                                     "func": yld_152_sales_yield_pct_rank_504d},
    "yld_153_book_yield_pct_rank_504d":          {"inputs": ["pb"],                                     "func": yld_153_book_yield_pct_rank_504d},
    "yld_154_ebitda_yield_zscore_504d":          {"inputs": ["evebitda"],                               "func": yld_154_ebitda_yield_zscore_504d},
    "yld_155_ebit_yield_zscore_504d":            {"inputs": ["evebit"],                                 "func": yld_155_ebit_yield_zscore_504d},
    "yld_156_divyield_vs_63d_avg":               {"inputs": ["divyield"],                               "func": yld_156_divyield_vs_63d_avg},
    "yld_157_divyield_vs_126d_avg":              {"inputs": ["divyield"],                               "func": yld_157_divyield_vs_126d_avg},
    "yld_158_earnings_yield_63d_max_ratio":      {"inputs": ["pe"],                                     "func": yld_158_earnings_yield_63d_max_ratio},
    "yld_159_sales_yield_126d_drawup":           {"inputs": ["ps"],                                     "func": yld_159_sales_yield_126d_drawup},
    "yld_160_book_yield_126d_drawup":            {"inputs": ["pb"],                                     "func": yld_160_book_yield_126d_drawup},
    "yld_161_ebit_yield_expanding_pct_rank":     {"inputs": ["evebit"],                                 "func": yld_161_ebit_yield_expanding_pct_rank},
    "yld_162_ebitda_yield_expanding_pct_rank":   {"inputs": ["evebitda"],                               "func": yld_162_ebitda_yield_expanding_pct_rank},
    "yld_163_divyield_zscore_504d":              {"inputs": ["divyield"],                               "func": yld_163_divyield_zscore_504d},
    "yld_164_sales_yield_ewm63_dev":             {"inputs": ["ps"],                                     "func": yld_164_sales_yield_ewm63_dev},
    "yld_165_ebit_yield_ewm63_dev":              {"inputs": ["evebit"],                                 "func": yld_165_ebit_yield_ewm63_dev},
    "yld_166_earnings_yield_above_50pct":        {"inputs": ["pe"],                                     "func": yld_166_earnings_yield_above_50pct},
    "yld_167_book_yield_above_3":                {"inputs": ["pb"],                                     "func": yld_167_book_yield_above_3},
    "yld_168_divyield_above_20pct":              {"inputs": ["divyield"],                               "func": yld_168_divyield_above_20pct},
    "yld_169_ebitda_yield_above_20pct":          {"inputs": ["evebitda"],                               "func": yld_169_ebitda_yield_above_20pct},
    "yld_170_earnings_yield_vs_126d_avg":        {"inputs": ["pe"],                                     "func": yld_170_earnings_yield_vs_126d_avg},
    "yld_171_sales_yield_zscore_504d":           {"inputs": ["ps"],                                     "func": yld_171_sales_yield_zscore_504d},
    "yld_172_book_yield_zscore_1260d":           {"inputs": ["pb"],                                     "func": yld_172_book_yield_zscore_1260d},
    "yld_173_mcap_expanding_pct_rank":           {"inputs": ["marketcap"],                              "func": yld_173_mcap_expanding_pct_rank},
    "yld_174_ev_expanding_pct_rank":             {"inputs": ["ev"],                                     "func": yld_174_ev_expanding_pct_rank},
    "yld_175_yield_spike_breadth_6":             {"inputs": ["pe", "ps", "pb", "evebit", "evebitda", "divyield"], "func": yld_175_yield_spike_breadth_6},
}
