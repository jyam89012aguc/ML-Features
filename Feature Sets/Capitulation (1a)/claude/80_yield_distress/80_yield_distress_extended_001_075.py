"""
80_yield_distress — Extended Features 001-075
Domain: dividend / earnings yield spikes as price collapses (yield = 1/multiple) —
        additional yield-spike windows, streak/persistence counts, drawup variants,
        cross-yield divergence angles, acceleration-free composites, and breadth scores.
Inputs: daily-frequency Sharadar DAILY/METRICS valuation fields only.
        Canonical fields: pe, ps, pb, evebit, evebitda, divyield, marketcap, ev.
        These are native daily-frequency series — no quarterly forward-fill alignment needed.
All feature functions are strictly backward-looking; no forward information is used.
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


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(float)
    grp = (~cond.astype(bool)).cumsum()
    return c.groupby(grp).cumsum()


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Earnings-yield — new windows and transforms ---

def yld_ext_001_earnings_yield_vs_126d_max_ratio(pe: pd.Series) -> pd.Series:
    """Earnings yield as fraction of its 126-day rolling max (semi-annual spike recency)."""
    ey = _to_yield(pe)
    return _safe_div(ey, _rolling_max(ey, _TD_HALF))


def yld_ext_002_earnings_yield_vs_504d_max_ratio(pe: pd.Series) -> pd.Series:
    """Earnings yield as fraction of its 504-day rolling max (two-year spike recency)."""
    ey = _to_yield(pe)
    return _safe_div(ey, _rolling_max(ey, _TD_2Y))


def yld_ext_003_earnings_yield_zscore_126d(pe: pd.Series) -> pd.Series:
    """Z-score of earnings yield over trailing 126 days (semi-annual spike extremity)."""
    return _zscore_rolling(_to_yield(pe), _TD_HALF)


def yld_ext_004_earnings_yield_zscore_63d(pe: pd.Series) -> pd.Series:
    """Z-score of earnings yield over trailing 63 days (quarterly spike extremity)."""
    return _zscore_rolling(_to_yield(pe), _TD_QTR)


def yld_ext_005_earnings_yield_pct_rank_504d(pe: pd.Series) -> pd.Series:
    """Percentile rank of earnings yield within trailing 504-day window."""
    return _rolling_rank_pct(_to_yield(pe), _TD_2Y)


def yld_ext_006_earnings_yield_pct_rank_63d(pe: pd.Series) -> pd.Series:
    """Percentile rank of earnings yield within trailing 63-day window."""
    return _rolling_rank_pct(_to_yield(pe), _TD_QTR)


def yld_ext_007_earnings_yield_vs_10d_avg(pe: pd.Series) -> pd.Series:
    """Earnings yield minus its 10-day rolling mean (very short-term spike)."""
    ey = _to_yield(pe)
    return ey - _rolling_mean(ey, 10)


def yld_ext_008_earnings_yield_vs_63d_median(pe: pd.Series) -> pd.Series:
    """Earnings yield minus its 63-day rolling median (robust quarterly spike)."""
    ey = _to_yield(pe)
    return ey - _rolling_median(ey, _TD_QTR)


def yld_ext_009_earnings_yield_ewm21_dev(pe: pd.Series) -> pd.Series:
    """Earnings yield minus its 21-day EMA (fast EWM spike deviation)."""
    ey = _to_yield(pe)
    return ey - _ewm_mean(ey, _TD_MON)


def yld_ext_010_earnings_yield_21d_change(pe: pd.Series) -> pd.Series:
    """21-day change in earnings yield (monthly yield-spike velocity)."""
    return _to_yield(pe).diff(_TD_MON)


def yld_ext_011_earnings_yield_63d_change(pe: pd.Series) -> pd.Series:
    """63-day change in earnings yield (quarterly yield-spike velocity)."""
    return _to_yield(pe).diff(_TD_QTR)


def yld_ext_012_earnings_yield_252d_drawup(pe: pd.Series) -> pd.Series:
    """Earnings-yield drawup: current yield minus 252-day rolling minimum yield."""
    ey = _to_yield(pe)
    return ey - _rolling_min(ey, _TD_YEAR)


# --- Group B (013-022): Earnings-yield streaks and threshold persistence ---

def yld_ext_013_earnings_yield_rising_streak(pe: pd.Series) -> pd.Series:
    """Consecutive days the earnings yield has risen from the prior day."""
    return _consec_streak(_to_yield(pe).diff(1) > 0)


def yld_ext_014_earnings_yield_above_252d_avg_streak(pe: pd.Series) -> pd.Series:
    """Consecutive days earnings yield has stayed above its 252-day rolling mean."""
    ey = _to_yield(pe)
    return _consec_streak(ey > _rolling_mean(ey, _TD_YEAR))


def yld_ext_015_earnings_yield_above_q90_252d_streak(pe: pd.Series) -> pd.Series:
    """Consecutive days earnings yield has stayed above its 252-day 90th percentile."""
    ey = _to_yield(pe)
    q90 = ey.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    return _consec_streak(ey > q90)


def yld_ext_016_earnings_yield_above_15pct_fraction_252d(pe: pd.Series) -> pd.Series:
    """Fraction of past 252 days where earnings yield exceeded 15% (PE < ~6.7)."""
    flag = (_to_yield(pe) > 0.15).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def yld_ext_017_earnings_yield_above_25pct_fraction_252d(pe: pd.Series) -> pd.Series:
    """Fraction of past 252 days where earnings yield exceeded 25% (PE < 4)."""
    flag = (_to_yield(pe) > 0.25).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def yld_ext_018_earnings_yield_above_15pct_flag(pe: pd.Series) -> pd.Series:
    """Binary flag: earnings yield > 15% (deep distress earnings pricing)."""
    return (_to_yield(pe) > 0.15).astype(float)


def yld_ext_019_earnings_yield_count_rises_21d(pe: pd.Series) -> pd.Series:
    """Count of up-days in earnings yield within the trailing 21 days."""
    rising = (_to_yield(pe).diff(1) > 0).astype(float)
    return _rolling_sum(rising, _TD_MON)


def yld_ext_020_earnings_yield_count_rises_63d(pe: pd.Series) -> pd.Series:
    """Count of up-days in earnings yield within the trailing 63 days."""
    rising = (_to_yield(pe).diff(1) > 0).astype(float)
    return _rolling_sum(rising, _TD_QTR)


def yld_ext_021_earnings_yield_3x_252d_avg_flag(pe: pd.Series) -> pd.Series:
    """Binary flag: earnings yield > 3x its 252-day rolling mean (extreme spike)."""
    ey = _to_yield(pe)
    return (ey > 3.0 * _rolling_mean(ey, _TD_YEAR)).astype(float)


def yld_ext_022_earnings_yield_at_252d_max_flag(pe: pd.Series) -> pd.Series:
    """Binary flag: earnings yield equals its trailing 252-day maximum (fresh peak)."""
    ey = _to_yield(pe)
    return (ey >= _rolling_max(ey, _TD_YEAR) - _EPS).astype(float)


# --- Group C (023-032): Sales-yield and book-yield extended variants ---

def yld_ext_023_sales_yield_zscore_126d(ps: pd.Series) -> pd.Series:
    """Z-score of sales yield over trailing 126 days (semi-annual spike extremity)."""
    return _zscore_rolling(_to_yield(ps), _TD_HALF)


def yld_ext_024_sales_yield_pct_rank_1260d(ps: pd.Series) -> pd.Series:
    """Percentile rank of sales yield within trailing 1260-day (5-year) window."""
    return _rolling_rank_pct(_to_yield(ps), _TD_5Y)


def yld_ext_025_sales_yield_504d_drawup(ps: pd.Series) -> pd.Series:
    """Sales-yield drawup: current yield minus 504-day rolling minimum yield."""
    sy = _to_yield(ps)
    return sy - _rolling_min(sy, _TD_2Y)


def yld_ext_026_sales_yield_above_252d_avg_streak(ps: pd.Series) -> pd.Series:
    """Consecutive days sales yield has stayed above its 252-day rolling mean."""
    sy = _to_yield(ps)
    return _consec_streak(sy > _rolling_mean(sy, _TD_YEAR))


def yld_ext_027_sales_yield_63d_change(ps: pd.Series) -> pd.Series:
    """63-day change in sales yield (quarterly sales-yield-spike velocity)."""
    return _to_yield(ps).diff(_TD_QTR)


def yld_ext_028_sales_yield_vs_126d_avg(ps: pd.Series) -> pd.Series:
    """Sales yield minus its 126-day rolling mean (semi-annual spike)."""
    sy = _to_yield(ps)
    return sy - _rolling_mean(sy, _TD_HALF)


def yld_ext_029_book_yield_zscore_126d(pb: pd.Series) -> pd.Series:
    """Z-score of book yield over trailing 126 days (semi-annual discount extremity)."""
    return _zscore_rolling(_to_yield(pb), _TD_HALF)


def yld_ext_030_book_yield_504d_drawup(pb: pd.Series) -> pd.Series:
    """Book-yield drawup: current yield minus 504-day rolling minimum yield."""
    by = _to_yield(pb)
    return by - _rolling_min(by, _TD_2Y)


def yld_ext_031_book_yield_above_1_fraction_252d(pb: pd.Series) -> pd.Series:
    """Fraction of past 252 days where book yield exceeded 1 (PB < 1, below book)."""
    flag = (_to_yield(pb) > 1.0).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def yld_ext_032_book_yield_above_1_streak(pb: pd.Series) -> pd.Series:
    """Consecutive days book yield has stayed above 1 (persistent discount to book)."""
    return _consec_streak(_to_yield(pb) > 1.0)


# --- Group D (033-044): EBIT / EBITDA yield extended variants ---

def yld_ext_033_ebit_yield_zscore_126d(evebit: pd.Series) -> pd.Series:
    """Z-score of EBIT yield over trailing 126 days (semi-annual operating-yield extremity)."""
    return _zscore_rolling(_to_yield(evebit), _TD_HALF)


def yld_ext_034_ebit_yield_pct_rank_504d(evebit: pd.Series) -> pd.Series:
    """Percentile rank of EBIT yield within trailing 504-day window."""
    return _rolling_rank_pct(_to_yield(evebit), _TD_2Y)


def yld_ext_035_ebit_yield_504d_drawup(evebit: pd.Series) -> pd.Series:
    """EBIT-yield drawup: current yield minus 504-day rolling minimum yield."""
    ey = _to_yield(evebit)
    return ey - _rolling_min(ey, _TD_2Y)


def yld_ext_036_ebit_yield_vs_63d_avg(evebit: pd.Series) -> pd.Series:
    """EBIT yield minus its 63-day rolling mean (quarterly operating-yield spike)."""
    ey = _to_yield(evebit)
    return ey - _rolling_mean(ey, _TD_QTR)


def yld_ext_037_ebit_yield_above_252d_avg_streak(evebit: pd.Series) -> pd.Series:
    """Consecutive days EBIT yield has stayed above its 252-day rolling mean."""
    ey = _to_yield(evebit)
    return _consec_streak(ey > _rolling_mean(ey, _TD_YEAR))


def yld_ext_038_ebit_yield_above_33pct_flag(evebit: pd.Series) -> pd.Series:
    """Binary flag: EBIT yield > 33% (EV/EBIT < 3 — extreme operational discount)."""
    return (_to_yield(evebit) > 0.33).astype(float)


def yld_ext_039_ebitda_yield_zscore_126d(evebitda: pd.Series) -> pd.Series:
    """Z-score of EBITDA yield over trailing 126 days (semi-annual cash-yield extremity)."""
    return _zscore_rolling(_to_yield(evebitda), _TD_HALF)


def yld_ext_040_ebitda_yield_pct_rank_504d(evebitda: pd.Series) -> pd.Series:
    """Percentile rank of EBITDA yield within trailing 504-day window."""
    return _rolling_rank_pct(_to_yield(evebitda), _TD_2Y)


def yld_ext_041_ebitda_yield_504d_drawup(evebitda: pd.Series) -> pd.Series:
    """EBITDA-yield drawup: current yield minus 504-day rolling minimum yield."""
    ey = _to_yield(evebitda)
    return ey - _rolling_min(ey, _TD_2Y)


def yld_ext_042_ebitda_yield_vs_63d_avg(evebitda: pd.Series) -> pd.Series:
    """EBITDA yield minus its 63-day rolling mean (quarterly cash-yield spike)."""
    ey = _to_yield(evebitda)
    return ey - _rolling_mean(ey, _TD_QTR)


def yld_ext_043_ebitda_yield_above_252d_avg_streak(evebitda: pd.Series) -> pd.Series:
    """Consecutive days EBITDA yield has stayed above its 252-day rolling mean."""
    ey = _to_yield(evebitda)
    return _consec_streak(ey > _rolling_mean(ey, _TD_YEAR))


def yld_ext_044_ebitda_yield_above_33pct_flag(evebitda: pd.Series) -> pd.Series:
    """Binary flag: EBITDA yield > 33% (EV/EBITDA < 3 — extreme distress discount)."""
    return (_to_yield(evebitda) > 0.33).astype(float)


# --- Group E (045-056): Dividend-yield extended distress variants ---

def yld_ext_045_divyield_zscore_126d(divyield: pd.Series) -> pd.Series:
    """Z-score of dividend yield over trailing 126 days (semi-annual spike extremity)."""
    return _zscore_rolling(divyield, _TD_HALF)


def yld_ext_046_divyield_zscore_63d(divyield: pd.Series) -> pd.Series:
    """Z-score of dividend yield over trailing 63 days (quarterly spike extremity)."""
    return _zscore_rolling(divyield, _TD_QTR)


def yld_ext_047_divyield_pct_rank_504d(divyield: pd.Series) -> pd.Series:
    """Percentile rank of dividend yield within trailing 504-day window."""
    return _rolling_rank_pct(divyield, _TD_2Y)


def yld_ext_048_divyield_504d_drawup(divyield: pd.Series) -> pd.Series:
    """Dividend-yield drawup: current yield minus 504-day rolling minimum yield."""
    return divyield - _rolling_min(divyield, _TD_2Y)


def yld_ext_049_divyield_126d_drawup(divyield: pd.Series) -> pd.Series:
    """Dividend-yield drawup: current yield minus 126-day rolling minimum yield."""
    return divyield - _rolling_min(divyield, _TD_HALF)


def yld_ext_050_divyield_21d_change(divyield: pd.Series) -> pd.Series:
    """21-day change in dividend yield (monthly yield-spike velocity)."""
    return divyield.diff(_TD_MON)


def yld_ext_051_divyield_63d_change(divyield: pd.Series) -> pd.Series:
    """63-day change in dividend yield (quarterly yield-spike velocity)."""
    return divyield.diff(_TD_QTR)


def yld_ext_052_divyield_above_8pct_fraction_252d(divyield: pd.Series) -> pd.Series:
    """Fraction of past 252 days where dividend yield exceeded 8%."""
    return _rolling_mean((divyield > 0.08).astype(float), _TD_YEAR)


def yld_ext_053_divyield_above_12pct_flag(divyield: pd.Series) -> pd.Series:
    """Binary flag: dividend yield > 12% (acute yield-trap distress signal)."""
    return (divyield > 0.12).astype(float)


def yld_ext_054_divyield_above_252d_avg_streak(divyield: pd.Series) -> pd.Series:
    """Consecutive days dividend yield has stayed above its 252-day rolling mean."""
    return _consec_streak(divyield > _rolling_mean(divyield, _TD_YEAR))


def yld_ext_055_divyield_above_q90_252d_streak(divyield: pd.Series) -> pd.Series:
    """Consecutive days dividend yield has stayed above its 252-day 90th percentile."""
    q90 = divyield.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    return _consec_streak(divyield > q90)


def yld_ext_056_divyield_ewm21_dev(divyield: pd.Series) -> pd.Series:
    """Dividend yield minus its 21-day EMA (fast EWM spike deviation)."""
    return divyield - _ewm_mean(divyield, _TD_MON)


# --- Group F (057-066): Cross-yield divergence and spread variants ---

def yld_ext_057_div_vs_book_yield_spread(divyield: pd.Series, pb: pd.Series) -> pd.Series:
    """Dividend yield minus book yield (payout vs book-value backing)."""
    return divyield - _to_yield(pb)


def yld_ext_058_div_vs_ebit_yield_spread(divyield: pd.Series, evebit: pd.Series) -> pd.Series:
    """Dividend yield minus EBIT yield (payout vs operating-earnings coverage)."""
    return divyield - _to_yield(evebit)


def yld_ext_059_earnings_vs_sales_yield_spread(pe: pd.Series, ps: pd.Series) -> pd.Series:
    """Earnings yield minus sales yield (margin-implied gap between earnings and revenue)."""
    return _to_yield(pe) - _to_yield(ps)


def yld_ext_060_earnings_vs_book_yield_spread(pe: pd.Series, pb: pd.Series) -> pd.Series:
    """Earnings yield minus book yield (ROE-implied gap between earnings and book)."""
    return _to_yield(pe) - _to_yield(pb)


def yld_ext_061_div_to_ebitda_yield_ratio(divyield: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Ratio of dividend yield to EBITDA yield (payout vs cash-flow backing)."""
    return _safe_div(divyield, _to_yield(evebitda))


def yld_ext_062_earnings_to_ebit_yield_ratio(pe: pd.Series, evebit: pd.Series) -> pd.Series:
    """Ratio of earnings yield to EBIT yield (leverage / tax wedge proxy)."""
    return _safe_div(_to_yield(pe), _to_yield(evebit))


def yld_ext_063_div_minus_earnings_yield_zscore_252d(divyield: pd.Series, pe: pd.Series) -> pd.Series:
    """252-day z-score of the dividend-yield-minus-earnings-yield spread."""
    spread = divyield - _to_yield(pe)
    return _zscore_rolling(spread, _TD_YEAR)


def yld_ext_064_earnings_vs_sales_yield_spread_pct_rank_252d(pe: pd.Series, ps: pd.Series) -> pd.Series:
    """252-day percentile rank of the earnings-yield-minus-sales-yield spread."""
    return _rolling_rank_pct(_to_yield(pe) - _to_yield(ps), _TD_YEAR)


def yld_ext_065_payout_exceeds_earnings_flag(divyield: pd.Series, pe: pd.Series) -> pd.Series:
    """Binary flag: dividend yield exceeds earnings yield (payout above earnings — trap)."""
    return (divyield > _to_yield(pe)).astype(float)


def yld_ext_066_payout_exceeds_earnings_fraction_252d(divyield: pd.Series, pe: pd.Series) -> pd.Series:
    """Fraction of past 252 days where dividend yield exceeded earnings yield."""
    flag = (divyield > _to_yield(pe)).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


# --- Group G (067-075): Composite yield-distress and breadth scores ---

def yld_ext_067_composite_yield_5_avg(pe: pd.Series, ps: pd.Series, pb: pd.Series,
                                       evebit: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Simple average of earnings, sales, book, EBIT and EBITDA yields (5-way cheapness)."""
    parts = [_to_yield(pe), _to_yield(ps), _to_yield(pb),
             _to_yield(evebit), _to_yield(evebitda)]
    total = pd.Series(0.0, index=pe.index)
    for p in parts:
        total = total + p.fillna(0.0)
    return total / 5.0


def yld_ext_068_composite_yield_5_zscore_252d(pe: pd.Series, ps: pd.Series, pb: pd.Series,
                                                evebit: pd.Series, evebitda: pd.Series) -> pd.Series:
    """252-day z-score of the 5-way composite yield average."""
    parts = [_to_yield(pe), _to_yield(ps), _to_yield(pb),
             _to_yield(evebit), _to_yield(evebitda)]
    total = pd.Series(0.0, index=pe.index)
    for p in parts:
        total = total + p.fillna(0.0)
    return _zscore_rolling(total / 5.0, _TD_YEAR)


def yld_ext_069_yield_spike_breadth_3_q95(pe: pd.Series, ps: pd.Series, pb: pd.Series) -> pd.Series:
    """Count (0-3) of earnings/sales/book yields above their 252-day 95th percentile."""
    total = pd.Series(0.0, index=pe.index)
    for m in (pe, ps, pb):
        y = _to_yield(m)
        q95 = y.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.95)
        total = total + (y > q95).astype(float)
    return total


def yld_ext_070_yield_spike_breadth_4_zscore(pe: pd.Series, ps: pd.Series,
                                              evebit: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Count (0-4) of earnings/sales/EBIT/EBITDA yields with 252-day z-score above 2."""
    total = pd.Series(0.0, index=pe.index)
    for m in (pe, ps, evebit, evebitda):
        z = _zscore_rolling(_to_yield(m), _TD_YEAR)
        total = total + (z > 2.0).astype(float)
    return total


def yld_ext_071_yield_breadth_above_252d_avg_5(pe: pd.Series, ps: pd.Series, pb: pd.Series,
                                                evebit: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Count (0-5) of yields currently above their own 252-day rolling mean."""
    total = pd.Series(0.0, index=pe.index)
    for m in (pe, ps, pb, evebit, evebitda):
        y = _to_yield(m)
        total = total + (y > _rolling_mean(y, _TD_YEAR)).astype(float)
    return total


def yld_ext_072_earnings_yield_drawup_pct_rank_252d(pe: pd.Series) -> pd.Series:
    """252-day percentile rank of the earnings-yield 252-day drawup."""
    ey = _to_yield(pe)
    drawup = ey - _rolling_min(ey, _TD_YEAR)
    return _rolling_rank_pct(drawup, _TD_YEAR)


def yld_ext_073_divyield_capitulation_composite(divyield: pd.Series) -> pd.Series:
    """Dividend-yield capitulation composite: 252d pct-rank + |252d z-score|/3 clipped + drawup-flag."""
    rank = _rolling_rank_pct(divyield, _TD_YEAR)
    z = _zscore_rolling(divyield, _TD_YEAR).abs().clip(upper=3.0) / 3.0
    drawup = divyield - _rolling_min(divyield, _TD_YEAR)
    drawup_flag = (drawup > 0.05).astype(float)
    return rank.fillna(0.5) + z + drawup_flag


def yld_ext_074_earnings_yield_capitulation_composite(pe: pd.Series) -> pd.Series:
    """Earnings-yield capitulation composite: 252d pct-rank + |252d z-score|/3 clipped + extreme-flag."""
    ey = _to_yield(pe)
    rank = _rolling_rank_pct(ey, _TD_YEAR)
    z = _zscore_rolling(ey, _TD_YEAR).abs().clip(upper=3.0) / 3.0
    extreme = (ey > 0.20).astype(float)
    return rank.fillna(0.5) + z + extreme


def yld_ext_075_yield_distress_breadth_6_drawup(pe: pd.Series, ps: pd.Series, pb: pd.Series,
                                                 evebit: pd.Series, evebitda: pd.Series,
                                                 divyield: pd.Series) -> pd.Series:
    """Count (0-6) of yields whose 252-day drawup exceeds half their 252-day range."""
    total = pd.Series(0.0, index=pe.index)
    series = [_to_yield(pe), _to_yield(ps), _to_yield(pb),
              _to_yield(evebit), _to_yield(evebitda), divyield]
    for y in series:
        lo = _rolling_min(y, _TD_YEAR)
        hi = _rolling_max(y, _TD_YEAR)
        drawup = y - lo
        rng = hi - lo
        total = total + (drawup > 0.5 * rng).astype(float)
    return total


# ── Registry ──────────────────────────────────────────────────────────────────

YIELD_DISTRESS_EXTENDED_REGISTRY_001_075 = {
    "yld_ext_001_earnings_yield_vs_126d_max_ratio":          {"inputs": ["pe"], "func": yld_ext_001_earnings_yield_vs_126d_max_ratio},
    "yld_ext_002_earnings_yield_vs_504d_max_ratio":          {"inputs": ["pe"], "func": yld_ext_002_earnings_yield_vs_504d_max_ratio},
    "yld_ext_003_earnings_yield_zscore_126d":                {"inputs": ["pe"], "func": yld_ext_003_earnings_yield_zscore_126d},
    "yld_ext_004_earnings_yield_zscore_63d":                 {"inputs": ["pe"], "func": yld_ext_004_earnings_yield_zscore_63d},
    "yld_ext_005_earnings_yield_pct_rank_504d":              {"inputs": ["pe"], "func": yld_ext_005_earnings_yield_pct_rank_504d},
    "yld_ext_006_earnings_yield_pct_rank_63d":               {"inputs": ["pe"], "func": yld_ext_006_earnings_yield_pct_rank_63d},
    "yld_ext_007_earnings_yield_vs_10d_avg":                 {"inputs": ["pe"], "func": yld_ext_007_earnings_yield_vs_10d_avg},
    "yld_ext_008_earnings_yield_vs_63d_median":              {"inputs": ["pe"], "func": yld_ext_008_earnings_yield_vs_63d_median},
    "yld_ext_009_earnings_yield_ewm21_dev":                  {"inputs": ["pe"], "func": yld_ext_009_earnings_yield_ewm21_dev},
    "yld_ext_010_earnings_yield_21d_change":                 {"inputs": ["pe"], "func": yld_ext_010_earnings_yield_21d_change},
    "yld_ext_011_earnings_yield_63d_change":                 {"inputs": ["pe"], "func": yld_ext_011_earnings_yield_63d_change},
    "yld_ext_012_earnings_yield_252d_drawup":                {"inputs": ["pe"], "func": yld_ext_012_earnings_yield_252d_drawup},
    "yld_ext_013_earnings_yield_rising_streak":              {"inputs": ["pe"], "func": yld_ext_013_earnings_yield_rising_streak},
    "yld_ext_014_earnings_yield_above_252d_avg_streak":      {"inputs": ["pe"], "func": yld_ext_014_earnings_yield_above_252d_avg_streak},
    "yld_ext_015_earnings_yield_above_q90_252d_streak":      {"inputs": ["pe"], "func": yld_ext_015_earnings_yield_above_q90_252d_streak},
    "yld_ext_016_earnings_yield_above_15pct_fraction_252d":  {"inputs": ["pe"], "func": yld_ext_016_earnings_yield_above_15pct_fraction_252d},
    "yld_ext_017_earnings_yield_above_25pct_fraction_252d":  {"inputs": ["pe"], "func": yld_ext_017_earnings_yield_above_25pct_fraction_252d},
    "yld_ext_018_earnings_yield_above_15pct_flag":           {"inputs": ["pe"], "func": yld_ext_018_earnings_yield_above_15pct_flag},
    "yld_ext_019_earnings_yield_count_rises_21d":            {"inputs": ["pe"], "func": yld_ext_019_earnings_yield_count_rises_21d},
    "yld_ext_020_earnings_yield_count_rises_63d":            {"inputs": ["pe"], "func": yld_ext_020_earnings_yield_count_rises_63d},
    "yld_ext_021_earnings_yield_3x_252d_avg_flag":           {"inputs": ["pe"], "func": yld_ext_021_earnings_yield_3x_252d_avg_flag},
    "yld_ext_022_earnings_yield_at_252d_max_flag":           {"inputs": ["pe"], "func": yld_ext_022_earnings_yield_at_252d_max_flag},
    "yld_ext_023_sales_yield_zscore_126d":                   {"inputs": ["ps"], "func": yld_ext_023_sales_yield_zscore_126d},
    "yld_ext_024_sales_yield_pct_rank_1260d":                {"inputs": ["ps"], "func": yld_ext_024_sales_yield_pct_rank_1260d},
    "yld_ext_025_sales_yield_504d_drawup":                   {"inputs": ["ps"], "func": yld_ext_025_sales_yield_504d_drawup},
    "yld_ext_026_sales_yield_above_252d_avg_streak":         {"inputs": ["ps"], "func": yld_ext_026_sales_yield_above_252d_avg_streak},
    "yld_ext_027_sales_yield_63d_change":                    {"inputs": ["ps"], "func": yld_ext_027_sales_yield_63d_change},
    "yld_ext_028_sales_yield_vs_126d_avg":                   {"inputs": ["ps"], "func": yld_ext_028_sales_yield_vs_126d_avg},
    "yld_ext_029_book_yield_zscore_126d":                    {"inputs": ["pb"], "func": yld_ext_029_book_yield_zscore_126d},
    "yld_ext_030_book_yield_504d_drawup":                    {"inputs": ["pb"], "func": yld_ext_030_book_yield_504d_drawup},
    "yld_ext_031_book_yield_above_1_fraction_252d":          {"inputs": ["pb"], "func": yld_ext_031_book_yield_above_1_fraction_252d},
    "yld_ext_032_book_yield_above_1_streak":                 {"inputs": ["pb"], "func": yld_ext_032_book_yield_above_1_streak},
    "yld_ext_033_ebit_yield_zscore_126d":                    {"inputs": ["evebit"], "func": yld_ext_033_ebit_yield_zscore_126d},
    "yld_ext_034_ebit_yield_pct_rank_504d":                  {"inputs": ["evebit"], "func": yld_ext_034_ebit_yield_pct_rank_504d},
    "yld_ext_035_ebit_yield_504d_drawup":                    {"inputs": ["evebit"], "func": yld_ext_035_ebit_yield_504d_drawup},
    "yld_ext_036_ebit_yield_vs_63d_avg":                     {"inputs": ["evebit"], "func": yld_ext_036_ebit_yield_vs_63d_avg},
    "yld_ext_037_ebit_yield_above_252d_avg_streak":          {"inputs": ["evebit"], "func": yld_ext_037_ebit_yield_above_252d_avg_streak},
    "yld_ext_038_ebit_yield_above_33pct_flag":               {"inputs": ["evebit"], "func": yld_ext_038_ebit_yield_above_33pct_flag},
    "yld_ext_039_ebitda_yield_zscore_126d":                  {"inputs": ["evebitda"], "func": yld_ext_039_ebitda_yield_zscore_126d},
    "yld_ext_040_ebitda_yield_pct_rank_504d":                {"inputs": ["evebitda"], "func": yld_ext_040_ebitda_yield_pct_rank_504d},
    "yld_ext_041_ebitda_yield_504d_drawup":                  {"inputs": ["evebitda"], "func": yld_ext_041_ebitda_yield_504d_drawup},
    "yld_ext_042_ebitda_yield_vs_63d_avg":                   {"inputs": ["evebitda"], "func": yld_ext_042_ebitda_yield_vs_63d_avg},
    "yld_ext_043_ebitda_yield_above_252d_avg_streak":        {"inputs": ["evebitda"], "func": yld_ext_043_ebitda_yield_above_252d_avg_streak},
    "yld_ext_044_ebitda_yield_above_33pct_flag":             {"inputs": ["evebitda"], "func": yld_ext_044_ebitda_yield_above_33pct_flag},
    "yld_ext_045_divyield_zscore_126d":                      {"inputs": ["divyield"], "func": yld_ext_045_divyield_zscore_126d},
    "yld_ext_046_divyield_zscore_63d":                       {"inputs": ["divyield"], "func": yld_ext_046_divyield_zscore_63d},
    "yld_ext_047_divyield_pct_rank_504d":                    {"inputs": ["divyield"], "func": yld_ext_047_divyield_pct_rank_504d},
    "yld_ext_048_divyield_504d_drawup":                      {"inputs": ["divyield"], "func": yld_ext_048_divyield_504d_drawup},
    "yld_ext_049_divyield_126d_drawup":                      {"inputs": ["divyield"], "func": yld_ext_049_divyield_126d_drawup},
    "yld_ext_050_divyield_21d_change":                       {"inputs": ["divyield"], "func": yld_ext_050_divyield_21d_change},
    "yld_ext_051_divyield_63d_change":                       {"inputs": ["divyield"], "func": yld_ext_051_divyield_63d_change},
    "yld_ext_052_divyield_above_8pct_fraction_252d":         {"inputs": ["divyield"], "func": yld_ext_052_divyield_above_8pct_fraction_252d},
    "yld_ext_053_divyield_above_12pct_flag":                 {"inputs": ["divyield"], "func": yld_ext_053_divyield_above_12pct_flag},
    "yld_ext_054_divyield_above_252d_avg_streak":            {"inputs": ["divyield"], "func": yld_ext_054_divyield_above_252d_avg_streak},
    "yld_ext_055_divyield_above_q90_252d_streak":            {"inputs": ["divyield"], "func": yld_ext_055_divyield_above_q90_252d_streak},
    "yld_ext_056_divyield_ewm21_dev":                        {"inputs": ["divyield"], "func": yld_ext_056_divyield_ewm21_dev},
    "yld_ext_057_div_vs_book_yield_spread":                  {"inputs": ["divyield", "pb"], "func": yld_ext_057_div_vs_book_yield_spread},
    "yld_ext_058_div_vs_ebit_yield_spread":                  {"inputs": ["divyield", "evebit"], "func": yld_ext_058_div_vs_ebit_yield_spread},
    "yld_ext_059_earnings_vs_sales_yield_spread":            {"inputs": ["pe", "ps"], "func": yld_ext_059_earnings_vs_sales_yield_spread},
    "yld_ext_060_earnings_vs_book_yield_spread":             {"inputs": ["pe", "pb"], "func": yld_ext_060_earnings_vs_book_yield_spread},
    "yld_ext_061_div_to_ebitda_yield_ratio":                 {"inputs": ["divyield", "evebitda"], "func": yld_ext_061_div_to_ebitda_yield_ratio},
    "yld_ext_062_earnings_to_ebit_yield_ratio":              {"inputs": ["pe", "evebit"], "func": yld_ext_062_earnings_to_ebit_yield_ratio},
    "yld_ext_063_div_minus_earnings_yield_zscore_252d":      {"inputs": ["divyield", "pe"], "func": yld_ext_063_div_minus_earnings_yield_zscore_252d},
    "yld_ext_064_earnings_vs_sales_yield_spread_pct_rank_252d": {"inputs": ["pe", "ps"], "func": yld_ext_064_earnings_vs_sales_yield_spread_pct_rank_252d},
    "yld_ext_065_payout_exceeds_earnings_flag":              {"inputs": ["divyield", "pe"], "func": yld_ext_065_payout_exceeds_earnings_flag},
    "yld_ext_066_payout_exceeds_earnings_fraction_252d":     {"inputs": ["divyield", "pe"], "func": yld_ext_066_payout_exceeds_earnings_fraction_252d},
    "yld_ext_067_composite_yield_5_avg":                     {"inputs": ["pe", "ps", "pb", "evebit", "evebitda"], "func": yld_ext_067_composite_yield_5_avg},
    "yld_ext_068_composite_yield_5_zscore_252d":             {"inputs": ["pe", "ps", "pb", "evebit", "evebitda"], "func": yld_ext_068_composite_yield_5_zscore_252d},
    "yld_ext_069_yield_spike_breadth_3_q95":                 {"inputs": ["pe", "ps", "pb"], "func": yld_ext_069_yield_spike_breadth_3_q95},
    "yld_ext_070_yield_spike_breadth_4_zscore":              {"inputs": ["pe", "ps", "evebit", "evebitda"], "func": yld_ext_070_yield_spike_breadth_4_zscore},
    "yld_ext_071_yield_breadth_above_252d_avg_5":            {"inputs": ["pe", "ps", "pb", "evebit", "evebitda"], "func": yld_ext_071_yield_breadth_above_252d_avg_5},
    "yld_ext_072_earnings_yield_drawup_pct_rank_252d":       {"inputs": ["pe"], "func": yld_ext_072_earnings_yield_drawup_pct_rank_252d},
    "yld_ext_073_divyield_capitulation_composite":           {"inputs": ["divyield"], "func": yld_ext_073_divyield_capitulation_composite},
    "yld_ext_074_earnings_yield_capitulation_composite":     {"inputs": ["pe"], "func": yld_ext_074_earnings_yield_capitulation_composite},
    "yld_ext_075_yield_distress_breadth_6_drawup":           {"inputs": ["pe", "ps", "pb", "evebit", "evebitda", "divyield"], "func": yld_ext_075_yield_distress_breadth_6_drawup},
}
