"""
80_yield_distress — 3rd Derivatives (Features yld_drv3_001-075)
Domain: rate-of-change of 2nd-derivative yield-distress concepts — captures
        the jerk / convexity of yield spikes (acceleration of acceleration).
Inputs: daily-frequency Sharadar DAILY/METRICS valuation fields only.
  Canonical fields: pe, ps, pb, evebit, evebitda, divyield, marketcap, ev
  These are native daily-frequency series — no quarterly forward-fill needed.
Each feature computes .diff(n) or slope of a 2nd-derivative concept.
All features are strictly backward-looking; no forward information is used.
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
    Negative or near-zero multiples produce NaN.
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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods (scalar per window)."""
    def _slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi   = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        num  = ((xi - xi_m) * (x - x.mean())).sum()
        den  = ((xi - xi_m) ** 2).sum()
        return np.nan if den == 0 else num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=False)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def yld_drv3_001_earnings_yield_5d_diff_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of earnings yield) — yield-spike jerk."""
    return _to_yield(pe).diff(5).diff(5)


def yld_drv3_002_divyield_5d_diff_5d_diff(divyield: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of dividend yield) — dividend-yield jerk."""
    return divyield.diff(5).diff(5)


def yld_drv3_003_sales_yield_5d_diff_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of sales yield) — sales-yield jerk."""
    return _to_yield(ps).diff(5).diff(5)


def yld_drv3_004_book_yield_5d_diff_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of book yield) — book-yield jerk."""
    return _to_yield(pb).diff(5).diff(5)


def yld_drv3_005_ebitda_yield_5d_diff_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of EBITDA yield) — EBITDA-yield jerk."""
    return _to_yield(evebitda).diff(5).diff(5)


def yld_drv3_006_ebit_yield_5d_diff_5d_diff(evebit: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of EBIT yield) — EBIT-yield jerk."""
    return _to_yield(evebit).diff(5).diff(5)


def yld_drv3_007_earnings_yield_zscore_diff2(pe: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of earnings yield z-score) — z-score jerk."""
    return _zscore_rolling(_to_yield(pe), _TD_YEAR).diff(5).diff(5)


def yld_drv3_008_divyield_zscore_diff2(divyield: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of dividend yield z-score)."""
    return _zscore_rolling(divyield, _TD_YEAR).diff(5).diff(5)


def yld_drv3_009_earnings_yield_drawup_diff2(pe: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of earnings-yield 252d drawup) — drawup jerk."""
    ey     = _to_yield(pe)
    drawup = ey - _rolling_min(ey, _TD_YEAR)
    return drawup.diff(5).diff(5)


def yld_drv3_010_divyield_drawup_diff2(divyield: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of dividend-yield 252d drawup)."""
    drawup = divyield - _rolling_min(divyield, _TD_YEAR)
    return drawup.diff(5).diff(5)


def yld_drv3_011_earnings_yield_slope_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of earnings yield (slope-of-slope)."""
    return _linslope(_to_yield(pe), _TD_MON).diff(5)


def yld_drv3_012_divyield_slope_diff(divyield: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of dividend yield."""
    return _linslope(divyield, _TD_MON).diff(5)


def yld_drv3_013_earnings_yield_slope_of_slope_21d(pe: pd.Series) -> pd.Series:
    """21-day OLS slope of the (5-day-diff earnings yield) — slope of velocity."""
    vel = _to_yield(pe).diff(5)
    return _linslope(vel, _TD_MON)


def yld_drv3_014_divyield_slope_of_slope_21d(divyield: pd.Series) -> pd.Series:
    """21-day OLS slope of the (5-day-diff dividend yield)."""
    return _linslope(divyield.diff(5), _TD_MON)


def yld_drv3_015_composite_yield_zscore_diff2(pe: pd.Series, ps: pd.Series,
                                               pb: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of composite yield z-score) — composite jerk."""
    comp = (_to_yield(pe).fillna(0) + _to_yield(ps).fillna(0) +
            _to_yield(pb).fillna(0)) / 3.0
    return _zscore_rolling(comp, _TD_YEAR).diff(5).diff(5)


def yld_drv3_016_earnings_yield_pct_rank_diff2(pe: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of earnings yield percentile rank) — rank jerk."""
    return _rolling_rank_pct(_to_yield(pe), _TD_YEAR).diff(5).diff(5)


def yld_drv3_017_div_earnings_spread_diff2(divyield: pd.Series, pe: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of divyield-earnings yield spread) — payout jerk."""
    spread = divyield - _to_yield(pe)
    return spread.diff(5).diff(5)


def yld_drv3_018_earnings_yield_vol_21d_diff2(pe: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21d rolling std of earnings yield)."""
    return _rolling_std(_to_yield(pe), _TD_MON).diff(5).diff(5)


def yld_drv3_019_divyield_ewm21_dev_diff2(divyield: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of divyield deviation from 21d EMA)."""
    dev = divyield - _ewm_mean(divyield, _TD_MON)
    return dev.diff(5).diff(5)


def yld_drv3_020_sales_yield_expanding_zscore_diff2(ps: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of expanding z-score of sales yield)."""
    sy = _to_yield(ps)
    m  = sy.expanding(min_periods=5).mean()
    sd = sy.expanding(min_periods=5).std()
    ez = _safe_div(sy - m, sd)
    return ez.diff(5).diff(5)


def yld_drv3_021_earnings_yield_expanding_max_ratio_diff2(pe: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of earnings yield / expanding max ratio)."""
    ey    = _to_yield(pe)
    ratio = _safe_div(ey, ey.expanding(min_periods=1).max())
    return ratio.diff(5).diff(5)


def yld_drv3_022_ebitda_yield_pct_rank_diff2(evebitda: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of EBITDA yield percentile rank)."""
    return _rolling_rank_pct(_to_yield(evebitda), _TD_YEAR).diff(5).diff(5)


def yld_drv3_023_multi_yield_distress_composite_diff2(pe: pd.Series, ps: pd.Series,
                                                       pb: pd.Series, evebit: pd.Series,
                                                       evebitda: pd.Series,
                                                       divyield: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 6-yield distress composite z-score) — composite jerk."""
    zs = [
        _zscore_rolling(_to_yield(pe),       _TD_YEAR),
        _zscore_rolling(_to_yield(ps),       _TD_YEAR),
        _zscore_rolling(_to_yield(pb),       _TD_YEAR),
        _zscore_rolling(_to_yield(evebit),   _TD_YEAR),
        _zscore_rolling(_to_yield(evebitda), _TD_YEAR),
        _zscore_rolling(divyield,            _TD_YEAR),
    ]
    comp = pd.concat(zs, axis=1).mean(axis=1)
    return comp.diff(5).diff(5)


def yld_drv3_024_earnings_yield_slope_zscore_21d(pe: pd.Series) -> pd.Series:
    """Z-score (252-day) of the 21-day OLS slope of earnings yield (normalized slope)."""
    return _zscore_rolling(_linslope(_to_yield(pe), _TD_MON), _TD_YEAR)


def yld_drv3_025_divyield_slope_zscore_21d(divyield: pd.Series) -> pd.Series:
    """Z-score (252-day) of the 21-day OLS slope of dividend yield."""
    return _zscore_rolling(_linslope(divyield, _TD_MON), _TD_YEAR)


def yld_drv3_026_sales_yield_5d_diff_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of sales yield) — sales yield jerk."""
    return _to_yield(ps).diff(_TD_MON).diff(5)


def yld_drv3_027_book_yield_21d_diff_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of book yield) — book yield jerk."""
    return _to_yield(pb).diff(_TD_MON).diff(5)


def yld_drv3_028_ebit_yield_5d_diff_5d_diff(evebit: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of EBIT yield)."""
    return _to_yield(evebit).diff(5).diff(5)


def yld_drv3_029_ebitda_yield_21d_diff_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5-day diff of (21-day diff of EBITDA yield)."""
    return _to_yield(evebitda).diff(_TD_MON).diff(5)


def yld_drv3_030_earnings_yield_63d_diff_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of (63-day diff of earnings yield) — quarterly velocity jerk."""
    return _to_yield(pe).diff(_TD_QTR).diff(5)


def yld_drv3_031_divyield_63d_diff_5d_diff(divyield: pd.Series) -> pd.Series:
    """5-day diff of (63-day diff of dividend yield)."""
    return divyield.diff(_TD_QTR).diff(5)


def yld_drv3_032_sales_yield_pct_rank_diff2(ps: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252-day percentile rank of sales yield)."""
    return _rolling_rank_pct(_to_yield(ps), _TD_YEAR).diff(5).diff(5)


def yld_drv3_033_book_yield_pct_rank_diff2(pb: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252-day percentile rank of book yield)."""
    return _rolling_rank_pct(_to_yield(pb), _TD_YEAR).diff(5).diff(5)


def yld_drv3_034_ebit_yield_pct_rank_diff2(evebit: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252-day percentile rank of EBIT yield)."""
    return _rolling_rank_pct(_to_yield(evebit), _TD_YEAR).diff(5).diff(5)


def yld_drv3_035_sales_yield_zscore_diff2(ps: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252-day z-score of sales yield)."""
    return _zscore_rolling(_to_yield(ps), _TD_YEAR).diff(5).diff(5)


def yld_drv3_036_book_yield_zscore_diff2(pb: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252-day z-score of book yield)."""
    return _zscore_rolling(_to_yield(pb), _TD_YEAR).diff(5).diff(5)


def yld_drv3_037_ebit_yield_zscore_diff2(evebit: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 252-day z-score of EBIT yield)."""
    return _zscore_rolling(_to_yield(evebit), _TD_YEAR).diff(5).diff(5)


def yld_drv3_038_sales_yield_drawup_diff2(ps: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of sales-yield 252d drawup) — drawup jerk."""
    sy = _to_yield(ps)
    return (sy - _rolling_min(sy, _TD_YEAR)).diff(5).diff(5)


def yld_drv3_039_book_yield_drawup_diff2(pb: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of book-yield 252d drawup)."""
    by = _to_yield(pb)
    return (by - _rolling_min(by, _TD_YEAR)).diff(5).diff(5)


def yld_drv3_040_ebitda_yield_drawup_diff2(evebitda: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of EBITDA-yield 252d drawup)."""
    ey = _to_yield(evebitda)
    return (ey - _rolling_min(ey, _TD_YEAR)).diff(5).diff(5)


def yld_drv3_041_ebit_yield_drawup_diff2(evebit: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of EBIT-yield 252d drawup)."""
    ey = _to_yield(evebit)
    return (ey - _rolling_min(ey, _TD_YEAR)).diff(5).diff(5)


def yld_drv3_042_sales_yield_slope_diff2(ps: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21-day slope of sales yield)."""
    return _linslope(_to_yield(ps), _TD_MON).diff(5).diff(5)


def yld_drv3_043_book_yield_slope_diff2(pb: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21-day slope of book yield)."""
    return _linslope(_to_yield(pb), _TD_MON).diff(5).diff(5)


def yld_drv3_044_ebitda_yield_slope_diff2(evebitda: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21-day slope of EBITDA yield)."""
    return _linslope(_to_yield(evebitda), _TD_MON).diff(5).diff(5)


def yld_drv3_045_ebit_yield_slope_diff2(evebit: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21-day slope of EBIT yield)."""
    return _linslope(_to_yield(evebit), _TD_MON).diff(5).diff(5)


def yld_drv3_046_earnings_yield_slope_of_slope_63d(pe: pd.Series) -> pd.Series:
    """63-day OLS slope of the (5-day-diff earnings yield) — slope of velocity."""
    return _linslope(_to_yield(pe).diff(5), _TD_QTR)


def yld_drv3_047_divyield_slope_of_slope_63d(divyield: pd.Series) -> pd.Series:
    """63-day OLS slope of the (5-day-diff dividend yield)."""
    return _linslope(divyield.diff(5), _TD_QTR)


def yld_drv3_048_sales_yield_slope_of_slope_21d(ps: pd.Series) -> pd.Series:
    """21-day OLS slope of (5-day-diff sales yield) — velocity trend."""
    return _linslope(_to_yield(ps).diff(5), _TD_MON)


def yld_drv3_049_book_yield_slope_of_slope_21d(pb: pd.Series) -> pd.Series:
    """21-day OLS slope of (5-day-diff book yield)."""
    return _linslope(_to_yield(pb).diff(5), _TD_MON)


def yld_drv3_050_ebitda_yield_slope_of_slope_21d(evebitda: pd.Series) -> pd.Series:
    """21-day OLS slope of (5-day-diff EBITDA yield)."""
    return _linslope(_to_yield(evebitda).diff(5), _TD_MON)


def yld_drv3_051_earnings_yield_ewm21_dev_diff2(pe: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of earnings yield deviation from 21d EMA)."""
    ey = _to_yield(pe)
    return (ey - _ewm_mean(ey, _TD_MON)).diff(5).diff(5)


def yld_drv3_052_sales_yield_ewm21_dev_diff2(ps: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of sales yield deviation from 21d EMA)."""
    sy = _to_yield(ps)
    return (sy - _ewm_mean(sy, _TD_MON)).diff(5).diff(5)


def yld_drv3_053_book_yield_ewm63_dev_diff2(pb: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of book yield deviation from 63d EMA)."""
    by = _to_yield(pb)
    return (by - _ewm_mean(by, _TD_QTR)).diff(5).diff(5)


def yld_drv3_054_ebitda_yield_ewm63_dev_diff2(evebitda: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of EBITDA yield deviation from 63d EMA)."""
    ey = _to_yield(evebitda)
    return (ey - _ewm_mean(ey, _TD_QTR)).diff(5).diff(5)


def yld_drv3_055_earnings_yield_vol_63d_diff2(pe: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 63-day rolling std of earnings yield)."""
    return _rolling_std(_to_yield(pe), _TD_QTR).diff(5).diff(5)


def yld_drv3_056_divyield_vol_63d_diff2(divyield: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 63-day rolling std of dividend yield)."""
    return _rolling_std(divyield, _TD_QTR).diff(5).diff(5)


def yld_drv3_057_sales_yield_vol_21d_diff2(ps: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21-day rolling std of sales yield)."""
    return _rolling_std(_to_yield(ps), _TD_MON).diff(5).diff(5)


def yld_drv3_058_book_yield_vol_21d_diff2(pb: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21-day rolling std of book yield)."""
    return _rolling_std(_to_yield(pb), _TD_MON).diff(5).diff(5)


def yld_drv3_059_earnings_yield_slope_zscore_63d(pe: pd.Series) -> pd.Series:
    """Z-score (252-day) of the 63-day OLS slope of earnings yield."""
    return _zscore_rolling(_linslope(_to_yield(pe), _TD_QTR), _TD_YEAR)


def yld_drv3_060_sales_yield_slope_zscore_21d(ps: pd.Series) -> pd.Series:
    """Z-score (252-day) of the 21-day OLS slope of sales yield."""
    return _zscore_rolling(_linslope(_to_yield(ps), _TD_MON), _TD_YEAR)


def yld_drv3_061_book_yield_slope_zscore_21d(pb: pd.Series) -> pd.Series:
    """Z-score (252-day) of the 21-day OLS slope of book yield."""
    return _zscore_rolling(_linslope(_to_yield(pb), _TD_MON), _TD_YEAR)


def yld_drv3_062_ebitda_yield_slope_zscore_21d(evebitda: pd.Series) -> pd.Series:
    """Z-score (252-day) of the 21-day OLS slope of EBITDA yield."""
    return _zscore_rolling(_linslope(_to_yield(evebitda), _TD_MON), _TD_YEAR)


def yld_drv3_063_ebit_yield_slope_zscore_21d(evebit: pd.Series) -> pd.Series:
    """Z-score (252-day) of the 21-day OLS slope of EBIT yield."""
    return _zscore_rolling(_linslope(_to_yield(evebit), _TD_MON), _TD_YEAR)


def yld_drv3_064_composite_yield_zscore_diff2_21d(pe: pd.Series, ps: pd.Series,
                                                   pb: pd.Series) -> pd.Series:
    """21-day diff of (5-day diff of composite yield z-score) — longer jerk."""
    comp = (_to_yield(pe).fillna(0) + _to_yield(ps).fillna(0) +
            _to_yield(pb).fillna(0)) / 3.0
    return _zscore_rolling(comp, _TD_YEAR).diff(5).diff(_TD_MON)


def yld_drv3_065_div_earnings_spread_diff2_21d(divyield: pd.Series, pe: pd.Series) -> pd.Series:
    """21-day diff of (5-day diff of divyield-earnings spread) — payout jerk."""
    return (divyield - _to_yield(pe)).diff(5).diff(_TD_MON)


def yld_drv3_066_earnings_yield_expanding_pct_rank_diff2(pe: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of expanding pct rank of earnings yield)."""
    return _to_yield(pe).expanding(min_periods=5).rank(pct=True).diff(5).diff(5)


def yld_drv3_067_sales_yield_expanding_zscore_diff2_alt(ps: pd.Series) -> pd.Series:
    """5-day diff of (21d diff of expanding z-score of sales yield)."""
    sy = _to_yield(ps)
    ez = _safe_div(sy - sy.expanding(min_periods=5).mean(),
                   sy.expanding(min_periods=5).std())
    return ez.diff(_TD_MON).diff(5)


def yld_drv3_068_mcap_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of market cap) — collapse jerk."""
    return marketcap.diff(5).diff(5)


def yld_drv3_069_ev_5d_diff_5d_diff(ev: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of enterprise value)."""
    return ev.diff(5).diff(5)


def yld_drv3_070_ev_to_mcap_ratio_diff2(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of EV/marketcap ratio)."""
    return _safe_div(ev, marketcap).diff(5).diff(5)


def yld_drv3_071_earnings_yield_streak_rise_diff2(pe: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21-day rising-streak count of earnings yield)."""
    streak = _rolling_sum((_to_yield(pe).diff(1) > 0).astype(float), _TD_MON)
    return streak.diff(5).diff(5)


def yld_drv3_072_divyield_streak_rise_diff2(divyield: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of 21-day rising-streak count of dividend yield)."""
    streak = _rolling_sum((divyield.diff(1) > 0).astype(float), _TD_MON)
    return streak.diff(5).diff(5)


def yld_drv3_073_yield_dispersion_diff2(pe: pd.Series, ps: pd.Series,
                                         pb: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of cross-yield std) — dispersion jerk."""
    stack = pd.concat([_to_yield(pe), _to_yield(ps), _to_yield(pb)], axis=1)
    return stack.std(axis=1).diff(5).diff(5)


def yld_drv3_074_ebit_ebitda_spread_diff2(evebit: pd.Series, evebitda: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of EBIT-EBITDA yield spread)."""
    return (_to_yield(evebit) - _to_yield(evebitda)).diff(5).diff(5)


def yld_drv3_075_multi_yield_composite_slope_zscore(pe: pd.Series, ps: pd.Series,
                                                     pb: pd.Series, evebit: pd.Series,
                                                     evebitda: pd.Series,
                                                     divyield: pd.Series) -> pd.Series:
    """Z-score (252d) of 21d OLS slope of 6-yield distress composite (3rd-order speed)."""
    zs = [
        _zscore_rolling(_to_yield(pe),       _TD_YEAR),
        _zscore_rolling(_to_yield(ps),       _TD_YEAR),
        _zscore_rolling(_to_yield(pb),       _TD_YEAR),
        _zscore_rolling(_to_yield(evebit),   _TD_YEAR),
        _zscore_rolling(_to_yield(evebitda), _TD_YEAR),
        _zscore_rolling(divyield,            _TD_YEAR),
    ]
    comp = pd.concat(zs, axis=1).mean(axis=1)
    return _zscore_rolling(_linslope(comp, _TD_MON), _TD_YEAR)


# ── Registry ──────────────────────────────────────────────────────────────────

YIELD_DISTRESS_REGISTRY_3RD_DERIVATIVES = {
    "yld_drv3_001_earnings_yield_5d_diff_5d_diff":          {"inputs": ["pe"],                                           "func": yld_drv3_001_earnings_yield_5d_diff_5d_diff},
    "yld_drv3_002_divyield_5d_diff_5d_diff":                {"inputs": ["divyield"],                                     "func": yld_drv3_002_divyield_5d_diff_5d_diff},
    "yld_drv3_003_sales_yield_5d_diff_5d_diff":             {"inputs": ["ps"],                                           "func": yld_drv3_003_sales_yield_5d_diff_5d_diff},
    "yld_drv3_004_book_yield_5d_diff_5d_diff":              {"inputs": ["pb"],                                           "func": yld_drv3_004_book_yield_5d_diff_5d_diff},
    "yld_drv3_005_ebitda_yield_5d_diff_5d_diff":            {"inputs": ["evebitda"],                                     "func": yld_drv3_005_ebitda_yield_5d_diff_5d_diff},
    "yld_drv3_006_ebit_yield_5d_diff_5d_diff":              {"inputs": ["evebit"],                                       "func": yld_drv3_006_ebit_yield_5d_diff_5d_diff},
    "yld_drv3_007_earnings_yield_zscore_diff2":             {"inputs": ["pe"],                                           "func": yld_drv3_007_earnings_yield_zscore_diff2},
    "yld_drv3_008_divyield_zscore_diff2":                   {"inputs": ["divyield"],                                     "func": yld_drv3_008_divyield_zscore_diff2},
    "yld_drv3_009_earnings_yield_drawup_diff2":             {"inputs": ["pe"],                                           "func": yld_drv3_009_earnings_yield_drawup_diff2},
    "yld_drv3_010_divyield_drawup_diff2":                   {"inputs": ["divyield"],                                     "func": yld_drv3_010_divyield_drawup_diff2},
    "yld_drv3_011_earnings_yield_slope_diff":               {"inputs": ["pe"],                                           "func": yld_drv3_011_earnings_yield_slope_diff},
    "yld_drv3_012_divyield_slope_diff":                     {"inputs": ["divyield"],                                     "func": yld_drv3_012_divyield_slope_diff},
    "yld_drv3_013_earnings_yield_slope_of_slope_21d":       {"inputs": ["pe"],                                           "func": yld_drv3_013_earnings_yield_slope_of_slope_21d},
    "yld_drv3_014_divyield_slope_of_slope_21d":             {"inputs": ["divyield"],                                     "func": yld_drv3_014_divyield_slope_of_slope_21d},
    "yld_drv3_015_composite_yield_zscore_diff2":            {"inputs": ["pe", "ps", "pb"],                               "func": yld_drv3_015_composite_yield_zscore_diff2},
    "yld_drv3_016_earnings_yield_pct_rank_diff2":           {"inputs": ["pe"],                                           "func": yld_drv3_016_earnings_yield_pct_rank_diff2},
    "yld_drv3_017_div_earnings_spread_diff2":               {"inputs": ["divyield", "pe"],                               "func": yld_drv3_017_div_earnings_spread_diff2},
    "yld_drv3_018_earnings_yield_vol_21d_diff2":            {"inputs": ["pe"],                                           "func": yld_drv3_018_earnings_yield_vol_21d_diff2},
    "yld_drv3_019_divyield_ewm21_dev_diff2":                {"inputs": ["divyield"],                                     "func": yld_drv3_019_divyield_ewm21_dev_diff2},
    "yld_drv3_020_sales_yield_expanding_zscore_diff2":      {"inputs": ["ps"],                                           "func": yld_drv3_020_sales_yield_expanding_zscore_diff2},
    "yld_drv3_021_earnings_yield_expanding_max_ratio_diff2":{"inputs": ["pe"],                                           "func": yld_drv3_021_earnings_yield_expanding_max_ratio_diff2},
    "yld_drv3_022_ebitda_yield_pct_rank_diff2":             {"inputs": ["evebitda"],                                     "func": yld_drv3_022_ebitda_yield_pct_rank_diff2},
    "yld_drv3_023_multi_yield_distress_composite_diff2":    {"inputs": ["pe", "ps", "pb", "evebit", "evebitda", "divyield"], "func": yld_drv3_023_multi_yield_distress_composite_diff2},
    "yld_drv3_024_earnings_yield_slope_zscore_21d":         {"inputs": ["pe"],                                           "func": yld_drv3_024_earnings_yield_slope_zscore_21d},
    "yld_drv3_025_divyield_slope_zscore_21d":               {"inputs": ["divyield"],                                           "func": yld_drv3_025_divyield_slope_zscore_21d},
    "yld_drv3_026_sales_yield_5d_diff_5d_diff":             {"inputs": ["ps"],                                                 "func": yld_drv3_026_sales_yield_5d_diff_5d_diff},
    "yld_drv3_027_book_yield_21d_diff_5d_diff":             {"inputs": ["pb"],                                                 "func": yld_drv3_027_book_yield_21d_diff_5d_diff},
    "yld_drv3_028_ebit_yield_5d_diff_5d_diff":              {"inputs": ["evebit"],                                             "func": yld_drv3_028_ebit_yield_5d_diff_5d_diff},
    "yld_drv3_029_ebitda_yield_21d_diff_5d_diff":           {"inputs": ["evebitda"],                                           "func": yld_drv3_029_ebitda_yield_21d_diff_5d_diff},
    "yld_drv3_030_earnings_yield_63d_diff_5d_diff":         {"inputs": ["pe"],                                                 "func": yld_drv3_030_earnings_yield_63d_diff_5d_diff},
    "yld_drv3_031_divyield_63d_diff_5d_diff":               {"inputs": ["divyield"],                                           "func": yld_drv3_031_divyield_63d_diff_5d_diff},
    "yld_drv3_032_sales_yield_pct_rank_diff2":              {"inputs": ["ps"],                                                 "func": yld_drv3_032_sales_yield_pct_rank_diff2},
    "yld_drv3_033_book_yield_pct_rank_diff2":               {"inputs": ["pb"],                                                 "func": yld_drv3_033_book_yield_pct_rank_diff2},
    "yld_drv3_034_ebit_yield_pct_rank_diff2":               {"inputs": ["evebit"],                                             "func": yld_drv3_034_ebit_yield_pct_rank_diff2},
    "yld_drv3_035_sales_yield_zscore_diff2":                {"inputs": ["ps"],                                                 "func": yld_drv3_035_sales_yield_zscore_diff2},
    "yld_drv3_036_book_yield_zscore_diff2":                 {"inputs": ["pb"],                                                 "func": yld_drv3_036_book_yield_zscore_diff2},
    "yld_drv3_037_ebit_yield_zscore_diff2":                 {"inputs": ["evebit"],                                             "func": yld_drv3_037_ebit_yield_zscore_diff2},
    "yld_drv3_038_sales_yield_drawup_diff2":                {"inputs": ["ps"],                                                 "func": yld_drv3_038_sales_yield_drawup_diff2},
    "yld_drv3_039_book_yield_drawup_diff2":                 {"inputs": ["pb"],                                                 "func": yld_drv3_039_book_yield_drawup_diff2},
    "yld_drv3_040_ebitda_yield_drawup_diff2":               {"inputs": ["evebitda"],                                           "func": yld_drv3_040_ebitda_yield_drawup_diff2},
    "yld_drv3_041_ebit_yield_drawup_diff2":                 {"inputs": ["evebit"],                                             "func": yld_drv3_041_ebit_yield_drawup_diff2},
    "yld_drv3_042_sales_yield_slope_diff2":                 {"inputs": ["ps"],                                                 "func": yld_drv3_042_sales_yield_slope_diff2},
    "yld_drv3_043_book_yield_slope_diff2":                  {"inputs": ["pb"],                                                 "func": yld_drv3_043_book_yield_slope_diff2},
    "yld_drv3_044_ebitda_yield_slope_diff2":                {"inputs": ["evebitda"],                                           "func": yld_drv3_044_ebitda_yield_slope_diff2},
    "yld_drv3_045_ebit_yield_slope_diff2":                  {"inputs": ["evebit"],                                             "func": yld_drv3_045_ebit_yield_slope_diff2},
    "yld_drv3_046_earnings_yield_slope_of_slope_63d":       {"inputs": ["pe"],                                                 "func": yld_drv3_046_earnings_yield_slope_of_slope_63d},
    "yld_drv3_047_divyield_slope_of_slope_63d":             {"inputs": ["divyield"],                                           "func": yld_drv3_047_divyield_slope_of_slope_63d},
    "yld_drv3_048_sales_yield_slope_of_slope_21d":          {"inputs": ["ps"],                                                 "func": yld_drv3_048_sales_yield_slope_of_slope_21d},
    "yld_drv3_049_book_yield_slope_of_slope_21d":           {"inputs": ["pb"],                                                 "func": yld_drv3_049_book_yield_slope_of_slope_21d},
    "yld_drv3_050_ebitda_yield_slope_of_slope_21d":         {"inputs": ["evebitda"],                                           "func": yld_drv3_050_ebitda_yield_slope_of_slope_21d},
    "yld_drv3_051_earnings_yield_ewm21_dev_diff2":          {"inputs": ["pe"],                                                 "func": yld_drv3_051_earnings_yield_ewm21_dev_diff2},
    "yld_drv3_052_sales_yield_ewm21_dev_diff2":             {"inputs": ["ps"],                                                 "func": yld_drv3_052_sales_yield_ewm21_dev_diff2},
    "yld_drv3_053_book_yield_ewm63_dev_diff2":              {"inputs": ["pb"],                                                 "func": yld_drv3_053_book_yield_ewm63_dev_diff2},
    "yld_drv3_054_ebitda_yield_ewm63_dev_diff2":            {"inputs": ["evebitda"],                                           "func": yld_drv3_054_ebitda_yield_ewm63_dev_diff2},
    "yld_drv3_055_earnings_yield_vol_63d_diff2":            {"inputs": ["pe"],                                                 "func": yld_drv3_055_earnings_yield_vol_63d_diff2},
    "yld_drv3_056_divyield_vol_63d_diff2":                  {"inputs": ["divyield"],                                           "func": yld_drv3_056_divyield_vol_63d_diff2},
    "yld_drv3_057_sales_yield_vol_21d_diff2":               {"inputs": ["ps"],                                                 "func": yld_drv3_057_sales_yield_vol_21d_diff2},
    "yld_drv3_058_book_yield_vol_21d_diff2":                {"inputs": ["pb"],                                                 "func": yld_drv3_058_book_yield_vol_21d_diff2},
    "yld_drv3_059_earnings_yield_slope_zscore_63d":         {"inputs": ["pe"],                                                 "func": yld_drv3_059_earnings_yield_slope_zscore_63d},
    "yld_drv3_060_sales_yield_slope_zscore_21d":            {"inputs": ["ps"],                                                 "func": yld_drv3_060_sales_yield_slope_zscore_21d},
    "yld_drv3_061_book_yield_slope_zscore_21d":             {"inputs": ["pb"],                                                 "func": yld_drv3_061_book_yield_slope_zscore_21d},
    "yld_drv3_062_ebitda_yield_slope_zscore_21d":           {"inputs": ["evebitda"],                                           "func": yld_drv3_062_ebitda_yield_slope_zscore_21d},
    "yld_drv3_063_ebit_yield_slope_zscore_21d":             {"inputs": ["evebit"],                                             "func": yld_drv3_063_ebit_yield_slope_zscore_21d},
    "yld_drv3_064_composite_yield_zscore_diff2_21d":        {"inputs": ["pe", "ps", "pb"],                                     "func": yld_drv3_064_composite_yield_zscore_diff2_21d},
    "yld_drv3_065_div_earnings_spread_diff2_21d":           {"inputs": ["divyield", "pe"],                                     "func": yld_drv3_065_div_earnings_spread_diff2_21d},
    "yld_drv3_066_earnings_yield_expanding_pct_rank_diff2": {"inputs": ["pe"],                                                 "func": yld_drv3_066_earnings_yield_expanding_pct_rank_diff2},
    "yld_drv3_067_sales_yield_expanding_zscore_diff2_alt":  {"inputs": ["ps"],                                                 "func": yld_drv3_067_sales_yield_expanding_zscore_diff2_alt},
    "yld_drv3_068_mcap_5d_diff_5d_diff":                    {"inputs": ["marketcap"],                                          "func": yld_drv3_068_mcap_5d_diff_5d_diff},
    "yld_drv3_069_ev_5d_diff_5d_diff":                      {"inputs": ["ev"],                                                 "func": yld_drv3_069_ev_5d_diff_5d_diff},
    "yld_drv3_070_ev_to_mcap_ratio_diff2":                  {"inputs": ["ev", "marketcap"],                                    "func": yld_drv3_070_ev_to_mcap_ratio_diff2},
    "yld_drv3_071_earnings_yield_streak_rise_diff2":        {"inputs": ["pe"],                                                 "func": yld_drv3_071_earnings_yield_streak_rise_diff2},
    "yld_drv3_072_divyield_streak_rise_diff2":              {"inputs": ["divyield"],                                           "func": yld_drv3_072_divyield_streak_rise_diff2},
    "yld_drv3_073_yield_dispersion_diff2":                  {"inputs": ["pe", "ps", "pb"],                                     "func": yld_drv3_073_yield_dispersion_diff2},
    "yld_drv3_074_ebit_ebitda_spread_diff2":                {"inputs": ["evebit", "evebitda"],                                 "func": yld_drv3_074_ebit_ebitda_spread_diff2},
    "yld_drv3_075_multi_yield_composite_slope_zscore":      {"inputs": ["pe", "ps", "pb", "evebit", "evebitda", "divyield"],   "func": yld_drv3_075_multi_yield_composite_slope_zscore},
}
