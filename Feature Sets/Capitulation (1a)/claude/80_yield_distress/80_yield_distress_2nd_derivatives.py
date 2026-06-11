"""
80_yield_distress — 2nd Derivatives (Features yld_drv2_001-075)
Domain: rate-of-change of base yield-distress concepts — captures acceleration of
        yield spikes as price collapses.
Inputs: daily-frequency Sharadar DAILY/METRICS valuation fields only.
  Canonical fields: pe, ps, pb, evebit, evebitda, divyield, marketcap, ev
  These are native daily-frequency series — no quarterly forward-fill needed.
Each feature computes .diff(n), slope, or pct-change of a base-feature concept.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def yld_drv2_001_earnings_yield_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day first difference of earnings yield (velocity of yield spike)."""
    return _to_yield(pe).diff(5)


def yld_drv2_002_earnings_yield_21d_diff(pe: pd.Series) -> pd.Series:
    """21-day first difference of earnings yield (monthly velocity of spike)."""
    return _to_yield(pe).diff(_TD_MON)


def yld_drv2_003_divyield_5d_diff(divyield: pd.Series) -> pd.Series:
    """5-day first difference of dividend yield (short-term spike velocity)."""
    return divyield.diff(5)


def yld_drv2_004_divyield_21d_diff(divyield: pd.Series) -> pd.Series:
    """21-day first difference of dividend yield (monthly spike velocity)."""
    return divyield.diff(_TD_MON)


def yld_drv2_005_sales_yield_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day first difference of sales yield."""
    return _to_yield(ps).diff(5)


def yld_drv2_006_book_yield_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day first difference of book yield."""
    return _to_yield(pb).diff(5)


def yld_drv2_007_ebitda_yield_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5-day first difference of EBITDA yield."""
    return _to_yield(evebitda).diff(5)


def yld_drv2_008_earnings_yield_zscore_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of 252-day z-score of earnings yield (speed of statistical extremity)."""
    return _zscore_rolling(_to_yield(pe), _TD_YEAR).diff(5)


def yld_drv2_009_divyield_zscore_5d_diff(divyield: pd.Series) -> pd.Series:
    """5-day diff of 252-day z-score of dividend yield."""
    return _zscore_rolling(divyield, _TD_YEAR).diff(5)


def yld_drv2_010_earnings_yield_pct_rank_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of 252-day percentile rank of earnings yield."""
    return _rolling_rank_pct(_to_yield(pe), _TD_YEAR).diff(5)


def yld_drv2_011_earnings_yield_drawup_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of earnings-yield drawup from 252-day minimum (spike acceleration)."""
    ey = _to_yield(pe)
    drawup = ey - _rolling_min(ey, _TD_YEAR)
    return drawup.diff(5)


def yld_drv2_012_divyield_drawup_5d_diff(divyield: pd.Series) -> pd.Series:
    """5-day diff of dividend-yield drawup from 252-day minimum."""
    drawup = divyield - _rolling_min(divyield, _TD_YEAR)
    return drawup.diff(5)


def yld_drv2_013_earnings_yield_21d_slope_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS slope of earnings yield (slope acceleration)."""
    return _linslope(_to_yield(pe), _TD_MON).diff(5)


def yld_drv2_014_divyield_21d_slope_5d_diff(divyield: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS slope of dividend yield."""
    return _linslope(divyield, _TD_MON).diff(5)


def yld_drv2_015_div_earnings_spread_5d_diff(divyield: pd.Series, pe: pd.Series) -> pd.Series:
    """5-day diff of (divyield - earnings yield) spread (payout unsustainability rate)."""
    spread = divyield - _to_yield(pe)
    return spread.diff(5)


def yld_drv2_016_composite_yield_zscore_5d_diff(pe: pd.Series, ps: pd.Series,
                                                  pb: pd.Series) -> pd.Series:
    """5-day diff of composite (earnings+sales+book) yield z-score."""
    comp = (_to_yield(pe).fillna(0) + _to_yield(ps).fillna(0) +
            _to_yield(pb).fillna(0)) / 3.0
    return _zscore_rolling(comp, _TD_YEAR).diff(5)


def yld_drv2_017_earnings_yield_expanding_pct_rank_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of expanding percentile rank of earnings yield."""
    rank = _to_yield(pe).expanding(min_periods=5).rank(pct=True)
    return rank.diff(5)


def yld_drv2_018_divyield_streak_21d_5d_diff(divyield: pd.Series) -> pd.Series:
    """5-day diff of count of days divyield rose within trailing 21 days."""
    streak = divyield.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda x: float((pd.Series(x).diff(1) > 0).sum()), raw=False)
    return streak.diff(5)


def yld_drv2_019_sales_yield_expanding_zscore_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of expanding z-score of sales yield."""
    sy = _to_yield(ps)
    m  = sy.expanding(min_periods=5).mean()
    sd = sy.expanding(min_periods=5).std()
    ez = _safe_div(sy - m, sd)
    return ez.diff(5)


def yld_drv2_020_ebitda_yield_pct_rank_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5-day diff of 252-day percentile rank of EBITDA yield."""
    return _rolling_rank_pct(_to_yield(evebitda), _TD_YEAR).diff(5)


def yld_drv2_021_earnings_yield_vol_21d_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of 21-day rolling std of earnings yield (volatility of spike)."""
    return _rolling_std(_to_yield(pe), _TD_MON).diff(5)


def yld_drv2_022_divyield_ewm21_dev_5d_diff(divyield: pd.Series) -> pd.Series:
    """5-day diff of divyield deviation from its 21-day EMA."""
    dev = divyield - _ewm_mean(divyield, _TD_MON)
    return dev.diff(5)


def yld_drv2_023_earnings_yield_expanding_max_ratio_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of earnings yield vs expanding historical max (ATH-proximity rate)."""
    ey    = _to_yield(pe)
    ratio = _safe_div(ey, ey.expanding(min_periods=1).max())
    return ratio.diff(5)


def yld_drv2_024_ebit_yield_drawup_21d_diff(evebit: pd.Series) -> pd.Series:
    """21-day diff of EBIT-yield drawup from 252-day minimum."""
    ey = _to_yield(evebit)
    drawup = ey - _rolling_min(ey, _TD_YEAR)
    return drawup.diff(_TD_MON)


def yld_drv2_025_multi_yield_distress_composite_5d_diff(pe: pd.Series, ps: pd.Series,
                                                          pb: pd.Series, evebit: pd.Series,
                                                          evebitda: pd.Series,
                                                          divyield: pd.Series) -> pd.Series:
    """5-day diff of 6-yield average z-score composite (acceleration of distress)."""
    zs = [
        _zscore_rolling(_to_yield(pe),       _TD_YEAR),
        _zscore_rolling(_to_yield(ps),       _TD_YEAR),
        _zscore_rolling(_to_yield(pb),       _TD_YEAR),
        _zscore_rolling(_to_yield(evebit),   _TD_YEAR),
        _zscore_rolling(_to_yield(evebitda), _TD_YEAR),
        _zscore_rolling(divyield,            _TD_YEAR),
    ]
    comp = pd.concat(zs, axis=1).mean(axis=1)
    return comp.diff(5)


def yld_drv2_026_earnings_yield_21d_diff(pe: pd.Series) -> pd.Series:
    """21-day diff of earnings yield velocity (5d diff) — monthly acceleration."""
    return _to_yield(pe).diff(5).diff(_TD_MON)


def yld_drv2_027_divyield_63d_diff(divyield: pd.Series) -> pd.Series:
    """63-day first difference of dividend yield (quarterly velocity)."""
    return divyield.diff(_TD_QTR)


def yld_drv2_028_sales_yield_21d_diff(ps: pd.Series) -> pd.Series:
    """21-day first difference of sales yield (monthly velocity)."""
    return _to_yield(ps).diff(_TD_MON)


def yld_drv2_029_book_yield_21d_diff(pb: pd.Series) -> pd.Series:
    """21-day first difference of book yield."""
    return _to_yield(pb).diff(_TD_MON)


def yld_drv2_030_ebit_yield_5d_diff(evebit: pd.Series) -> pd.Series:
    """5-day first difference of EBIT yield (short-term velocity)."""
    return _to_yield(evebit).diff(5)


def yld_drv2_031_ebitda_yield_21d_diff(evebitda: pd.Series) -> pd.Series:
    """21-day first difference of EBITDA yield."""
    return _to_yield(evebitda).diff(_TD_MON)


def yld_drv2_032_earnings_yield_63d_diff(pe: pd.Series) -> pd.Series:
    """63-day first difference of earnings yield (quarterly velocity)."""
    return _to_yield(pe).diff(_TD_QTR)


def yld_drv2_033_divyield_pct_rank_5d_diff(divyield: pd.Series) -> pd.Series:
    """5-day diff of 252-day percentile rank of dividend yield."""
    return _rolling_rank_pct(divyield, _TD_YEAR).diff(5)


def yld_drv2_034_sales_yield_pct_rank_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of 252-day percentile rank of sales yield."""
    return _rolling_rank_pct(_to_yield(ps), _TD_YEAR).diff(5)


def yld_drv2_035_book_yield_pct_rank_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of 252-day percentile rank of book yield."""
    return _rolling_rank_pct(_to_yield(pb), _TD_YEAR).diff(5)


def yld_drv2_036_ebit_yield_pct_rank_5d_diff(evebit: pd.Series) -> pd.Series:
    """5-day diff of 252-day percentile rank of EBIT yield."""
    return _rolling_rank_pct(_to_yield(evebit), _TD_YEAR).diff(5)


def yld_drv2_037_sales_yield_zscore_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of 252-day z-score of sales yield."""
    return _zscore_rolling(_to_yield(ps), _TD_YEAR).diff(5)


def yld_drv2_038_book_yield_zscore_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of 252-day z-score of book yield."""
    return _zscore_rolling(_to_yield(pb), _TD_YEAR).diff(5)


def yld_drv2_039_ebit_yield_zscore_5d_diff(evebit: pd.Series) -> pd.Series:
    """5-day diff of 252-day z-score of EBIT yield."""
    return _zscore_rolling(_to_yield(evebit), _TD_YEAR).diff(5)


def yld_drv2_040_earnings_yield_drawup_21d_diff(pe: pd.Series) -> pd.Series:
    """21-day diff of earnings-yield 252d drawup (monthly acceleration of drawup)."""
    ey = _to_yield(pe)
    return (ey - _rolling_min(ey, _TD_YEAR)).diff(_TD_MON)


def yld_drv2_041_divyield_drawup_21d_diff(divyield: pd.Series) -> pd.Series:
    """21-day diff of dividend-yield 252d drawup."""
    return (divyield - _rolling_min(divyield, _TD_YEAR)).diff(_TD_MON)


def yld_drv2_042_sales_yield_drawup_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of sales-yield 252d drawup."""
    sy = _to_yield(ps)
    return (sy - _rolling_min(sy, _TD_YEAR)).diff(5)


def yld_drv2_043_book_yield_drawup_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of book-yield 252d drawup."""
    by = _to_yield(pb)
    return (by - _rolling_min(by, _TD_YEAR)).diff(5)


def yld_drv2_044_ebitda_yield_drawup_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5-day diff of EBITDA-yield 252d drawup."""
    ey = _to_yield(evebitda)
    return (ey - _rolling_min(ey, _TD_YEAR)).diff(5)


def yld_drv2_045_earnings_yield_21d_slope_21d_diff(pe: pd.Series) -> pd.Series:
    """21-day diff of 21-day OLS slope of earnings yield (longer slope acceleration)."""
    return _linslope(_to_yield(pe), _TD_MON).diff(_TD_MON)


def yld_drv2_046_divyield_63d_slope_5d_diff(divyield: pd.Series) -> pd.Series:
    """5-day diff of 63-day OLS slope of dividend yield."""
    return _linslope(divyield, _TD_QTR).diff(5)


def yld_drv2_047_sales_yield_21d_slope_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS slope of sales yield."""
    return _linslope(_to_yield(ps), _TD_MON).diff(5)


def yld_drv2_048_book_yield_21d_slope_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS slope of book yield."""
    return _linslope(_to_yield(pb), _TD_MON).diff(5)


def yld_drv2_049_ebitda_yield_21d_slope_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS slope of EBITDA yield."""
    return _linslope(_to_yield(evebitda), _TD_MON).diff(5)


def yld_drv2_050_ebit_yield_21d_slope_5d_diff(evebit: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS slope of EBIT yield."""
    return _linslope(_to_yield(evebit), _TD_MON).diff(5)


def yld_drv2_051_earnings_yield_ewm21_dev_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of earnings yield deviation from 21-day EMA."""
    ey = _to_yield(pe)
    return (ey - _ewm_mean(ey, _TD_MON)).diff(5)


def yld_drv2_052_sales_yield_ewm21_dev_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of sales yield deviation from 21-day EMA."""
    sy = _to_yield(ps)
    return (sy - _ewm_mean(sy, _TD_MON)).diff(5)


def yld_drv2_053_book_yield_ewm63_dev_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of book yield deviation from 63-day EMA."""
    by = _to_yield(pb)
    return (by - _ewm_mean(by, _TD_QTR)).diff(5)


def yld_drv2_054_ebitda_yield_ewm63_dev_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5-day diff of EBITDA yield deviation from 63-day EMA."""
    ey = _to_yield(evebitda)
    return (ey - _ewm_mean(ey, _TD_QTR)).diff(5)


def yld_drv2_055_earnings_yield_ewm_crossover_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of (21d EMA minus 63d EMA) of earnings yield."""
    ey = _to_yield(pe)
    return (_ewm_mean(ey, _TD_MON) - _ewm_mean(ey, _TD_QTR)).diff(5)


def yld_drv2_056_divyield_ewm_crossover_5d_diff(divyield: pd.Series) -> pd.Series:
    """5-day diff of (21d EMA minus 63d EMA) of dividend yield."""
    return (_ewm_mean(divyield, _TD_MON) - _ewm_mean(divyield, _TD_QTR)).diff(5)


def yld_drv2_057_earnings_yield_vol_63d_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of 63-day rolling std of earnings yield."""
    return _rolling_std(_to_yield(pe), _TD_QTR).diff(5)


def yld_drv2_058_divyield_vol_63d_5d_diff(divyield: pd.Series) -> pd.Series:
    """5-day diff of 63-day rolling std of dividend yield."""
    return _rolling_std(divyield, _TD_QTR).diff(5)


def yld_drv2_059_sales_yield_vol_21d_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of 21-day rolling std of sales yield."""
    return _rolling_std(_to_yield(ps), _TD_MON).diff(5)


def yld_drv2_060_book_yield_vol_21d_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of 21-day rolling std of book yield."""
    return _rolling_std(_to_yield(pb), _TD_MON).diff(5)


def yld_drv2_061_earnings_yield_pct_change_21d(pe: pd.Series) -> pd.Series:
    """21-day percent change in earnings yield (monthly spike rate)."""
    ey = _to_yield(pe)
    return _safe_div(ey - ey.shift(_TD_MON), ey.shift(_TD_MON).abs() + _EPS)


def yld_drv2_062_sales_yield_pct_change_5d(ps: pd.Series) -> pd.Series:
    """5-day percent change in sales yield."""
    sy = _to_yield(ps)
    return _safe_div(sy - sy.shift(5), sy.shift(5).abs() + _EPS)


def yld_drv2_063_book_yield_pct_change_5d(pb: pd.Series) -> pd.Series:
    """5-day percent change in book yield."""
    by = _to_yield(pb)
    return _safe_div(by - by.shift(5), by.shift(5).abs() + _EPS)


def yld_drv2_064_ebit_yield_pct_change_5d(evebit: pd.Series) -> pd.Series:
    """5-day percent change in EBIT yield."""
    ey = _to_yield(evebit)
    return _safe_div(ey - ey.shift(5), ey.shift(5).abs() + _EPS)


def yld_drv2_065_ebitda_yield_pct_change_5d(evebitda: pd.Series) -> pd.Series:
    """5-day percent change in EBITDA yield."""
    ey = _to_yield(evebitda)
    return _safe_div(ey - ey.shift(5), ey.shift(5).abs() + _EPS)


def yld_drv2_066_mcap_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day first difference of market cap (collapse velocity)."""
    return marketcap.diff(5)


def yld_drv2_067_ev_5d_diff(ev: pd.Series) -> pd.Series:
    """5-day first difference of enterprise value."""
    return ev.diff(5)


def yld_drv2_068_ev_to_mcap_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of EV/marketcap ratio (leverage-lift velocity)."""
    return _safe_div(ev, marketcap).diff(5)


def yld_drv2_069_earnings_yield_streak_rise_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of 21-day rising-streak count of earnings yield."""
    streak = _rolling_sum((_to_yield(pe).diff(1) > 0).astype(float), _TD_MON)
    return streak.diff(5)


def yld_drv2_070_divyield_streak_rise_5d_diff(divyield: pd.Series) -> pd.Series:
    """5-day diff of 21-day rising-streak count of dividend yield."""
    streak = _rolling_sum((divyield.diff(1) > 0).astype(float), _TD_MON)
    return streak.diff(5)


def yld_drv2_071_composite_yield_avg_5d_diff(pe: pd.Series, ps: pd.Series,
                                              pb: pd.Series) -> pd.Series:
    """5-day diff of composite (earnings+sales+book) yield average."""
    comp = (_to_yield(pe).fillna(0) + _to_yield(ps).fillna(0) +
            _to_yield(pb).fillna(0)) / 3.0
    return comp.diff(5)


def yld_drv2_072_div_earnings_spread_21d_diff(divyield: pd.Series, pe: pd.Series) -> pd.Series:
    """21-day diff of (divyield - earnings yield) spread."""
    return (divyield - _to_yield(pe)).diff(_TD_MON)


def yld_drv2_073_ebit_ebitda_spread_5d_diff(evebit: pd.Series, evebitda: pd.Series) -> pd.Series:
    """5-day diff of (EBIT yield - EBITDA yield) spread."""
    return (_to_yield(evebit) - _to_yield(evebitda)).diff(5)


def yld_drv2_074_yield_dispersion_5d_diff(pe: pd.Series, ps: pd.Series,
                                           pb: pd.Series) -> pd.Series:
    """5-day diff of cross-yield std (earnings/sales/book dispersion velocity)."""
    stack = pd.concat([_to_yield(pe), _to_yield(ps), _to_yield(pb)], axis=1)
    return stack.std(axis=1).diff(5)


def yld_drv2_075_earnings_yield_expanding_zscore_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of expanding z-score of earnings yield."""
    ey = _to_yield(pe)
    m  = ey.expanding(min_periods=5).mean()
    sd = ey.expanding(min_periods=5).std()
    return _safe_div(ey - m, sd).diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

YIELD_DISTRESS_REGISTRY_2ND_DERIVATIVES = {
    "yld_drv2_001_earnings_yield_5d_diff":                   {"inputs": ["pe"],                                           "func": yld_drv2_001_earnings_yield_5d_diff},
    "yld_drv2_002_earnings_yield_21d_diff":                  {"inputs": ["pe"],                                           "func": yld_drv2_002_earnings_yield_21d_diff},
    "yld_drv2_003_divyield_5d_diff":                         {"inputs": ["divyield"],                                     "func": yld_drv2_003_divyield_5d_diff},
    "yld_drv2_004_divyield_21d_diff":                        {"inputs": ["divyield"],                                     "func": yld_drv2_004_divyield_21d_diff},
    "yld_drv2_005_sales_yield_5d_diff":                      {"inputs": ["ps"],                                           "func": yld_drv2_005_sales_yield_5d_diff},
    "yld_drv2_006_book_yield_5d_diff":                       {"inputs": ["pb"],                                           "func": yld_drv2_006_book_yield_5d_diff},
    "yld_drv2_007_ebitda_yield_5d_diff":                     {"inputs": ["evebitda"],                                     "func": yld_drv2_007_ebitda_yield_5d_diff},
    "yld_drv2_008_earnings_yield_zscore_5d_diff":            {"inputs": ["pe"],                                           "func": yld_drv2_008_earnings_yield_zscore_5d_diff},
    "yld_drv2_009_divyield_zscore_5d_diff":                  {"inputs": ["divyield"],                                     "func": yld_drv2_009_divyield_zscore_5d_diff},
    "yld_drv2_010_earnings_yield_pct_rank_5d_diff":          {"inputs": ["pe"],                                           "func": yld_drv2_010_earnings_yield_pct_rank_5d_diff},
    "yld_drv2_011_earnings_yield_drawup_5d_diff":            {"inputs": ["pe"],                                           "func": yld_drv2_011_earnings_yield_drawup_5d_diff},
    "yld_drv2_012_divyield_drawup_5d_diff":                  {"inputs": ["divyield"],                                     "func": yld_drv2_012_divyield_drawup_5d_diff},
    "yld_drv2_013_earnings_yield_21d_slope_5d_diff":         {"inputs": ["pe"],                                           "func": yld_drv2_013_earnings_yield_21d_slope_5d_diff},
    "yld_drv2_014_divyield_21d_slope_5d_diff":               {"inputs": ["divyield"],                                     "func": yld_drv2_014_divyield_21d_slope_5d_diff},
    "yld_drv2_015_div_earnings_spread_5d_diff":              {"inputs": ["divyield", "pe"],                               "func": yld_drv2_015_div_earnings_spread_5d_diff},
    "yld_drv2_016_composite_yield_zscore_5d_diff":           {"inputs": ["pe", "ps", "pb"],                               "func": yld_drv2_016_composite_yield_zscore_5d_diff},
    "yld_drv2_017_earnings_yield_expanding_pct_rank_5d_diff":{"inputs": ["pe"],                                           "func": yld_drv2_017_earnings_yield_expanding_pct_rank_5d_diff},
    "yld_drv2_018_divyield_streak_21d_5d_diff":              {"inputs": ["divyield"],                                     "func": yld_drv2_018_divyield_streak_21d_5d_diff},
    "yld_drv2_019_sales_yield_expanding_zscore_5d_diff":     {"inputs": ["ps"],                                           "func": yld_drv2_019_sales_yield_expanding_zscore_5d_diff},
    "yld_drv2_020_ebitda_yield_pct_rank_5d_diff":            {"inputs": ["evebitda"],                                     "func": yld_drv2_020_ebitda_yield_pct_rank_5d_diff},
    "yld_drv2_021_earnings_yield_vol_21d_5d_diff":           {"inputs": ["pe"],                                           "func": yld_drv2_021_earnings_yield_vol_21d_5d_diff},
    "yld_drv2_022_divyield_ewm21_dev_5d_diff":               {"inputs": ["divyield"],                                     "func": yld_drv2_022_divyield_ewm21_dev_5d_diff},
    "yld_drv2_023_earnings_yield_expanding_max_ratio_5d_diff":{"inputs": ["pe"],                                          "func": yld_drv2_023_earnings_yield_expanding_max_ratio_5d_diff},
    "yld_drv2_024_ebit_yield_drawup_21d_diff":               {"inputs": ["evebit"],                                       "func": yld_drv2_024_ebit_yield_drawup_21d_diff},
    "yld_drv2_025_multi_yield_distress_composite_5d_diff":   {"inputs": ["pe", "ps", "pb", "evebit", "evebitda", "divyield"], "func": yld_drv2_025_multi_yield_distress_composite_5d_diff},
    "yld_drv2_026_earnings_yield_21d_diff":                  {"inputs": ["pe"],                                           "func": yld_drv2_026_earnings_yield_21d_diff},
    "yld_drv2_027_divyield_63d_diff":                        {"inputs": ["divyield"],                                     "func": yld_drv2_027_divyield_63d_diff},
    "yld_drv2_028_sales_yield_21d_diff":                     {"inputs": ["ps"],                                           "func": yld_drv2_028_sales_yield_21d_diff},
    "yld_drv2_029_book_yield_21d_diff":                      {"inputs": ["pb"],                                           "func": yld_drv2_029_book_yield_21d_diff},
    "yld_drv2_030_ebit_yield_5d_diff":                       {"inputs": ["evebit"],                                       "func": yld_drv2_030_ebit_yield_5d_diff},
    "yld_drv2_031_ebitda_yield_21d_diff":                    {"inputs": ["evebitda"],                                     "func": yld_drv2_031_ebitda_yield_21d_diff},
    "yld_drv2_032_earnings_yield_63d_diff":                  {"inputs": ["pe"],                                           "func": yld_drv2_032_earnings_yield_63d_diff},
    "yld_drv2_033_divyield_pct_rank_5d_diff":                {"inputs": ["divyield"],                                     "func": yld_drv2_033_divyield_pct_rank_5d_diff},
    "yld_drv2_034_sales_yield_pct_rank_5d_diff":             {"inputs": ["ps"],                                           "func": yld_drv2_034_sales_yield_pct_rank_5d_diff},
    "yld_drv2_035_book_yield_pct_rank_5d_diff":              {"inputs": ["pb"],                                           "func": yld_drv2_035_book_yield_pct_rank_5d_diff},
    "yld_drv2_036_ebit_yield_pct_rank_5d_diff":              {"inputs": ["evebit"],                                       "func": yld_drv2_036_ebit_yield_pct_rank_5d_diff},
    "yld_drv2_037_sales_yield_zscore_5d_diff":               {"inputs": ["ps"],                                           "func": yld_drv2_037_sales_yield_zscore_5d_diff},
    "yld_drv2_038_book_yield_zscore_5d_diff":                {"inputs": ["pb"],                                           "func": yld_drv2_038_book_yield_zscore_5d_diff},
    "yld_drv2_039_ebit_yield_zscore_5d_diff":                {"inputs": ["evebit"],                                       "func": yld_drv2_039_ebit_yield_zscore_5d_diff},
    "yld_drv2_040_earnings_yield_drawup_21d_diff":           {"inputs": ["pe"],                                           "func": yld_drv2_040_earnings_yield_drawup_21d_diff},
    "yld_drv2_041_divyield_drawup_21d_diff":                 {"inputs": ["divyield"],                                     "func": yld_drv2_041_divyield_drawup_21d_diff},
    "yld_drv2_042_sales_yield_drawup_5d_diff":               {"inputs": ["ps"],                                           "func": yld_drv2_042_sales_yield_drawup_5d_diff},
    "yld_drv2_043_book_yield_drawup_5d_diff":                {"inputs": ["pb"],                                           "func": yld_drv2_043_book_yield_drawup_5d_diff},
    "yld_drv2_044_ebitda_yield_drawup_5d_diff":              {"inputs": ["evebitda"],                                     "func": yld_drv2_044_ebitda_yield_drawup_5d_diff},
    "yld_drv2_045_earnings_yield_21d_slope_21d_diff":        {"inputs": ["pe"],                                           "func": yld_drv2_045_earnings_yield_21d_slope_21d_diff},
    "yld_drv2_046_divyield_63d_slope_5d_diff":               {"inputs": ["divyield"],                                     "func": yld_drv2_046_divyield_63d_slope_5d_diff},
    "yld_drv2_047_sales_yield_21d_slope_5d_diff":            {"inputs": ["ps"],                                           "func": yld_drv2_047_sales_yield_21d_slope_5d_diff},
    "yld_drv2_048_book_yield_21d_slope_5d_diff":             {"inputs": ["pb"],                                           "func": yld_drv2_048_book_yield_21d_slope_5d_diff},
    "yld_drv2_049_ebitda_yield_21d_slope_5d_diff":           {"inputs": ["evebitda"],                                     "func": yld_drv2_049_ebitda_yield_21d_slope_5d_diff},
    "yld_drv2_050_ebit_yield_21d_slope_5d_diff":             {"inputs": ["evebit"],                                       "func": yld_drv2_050_ebit_yield_21d_slope_5d_diff},
    "yld_drv2_051_earnings_yield_ewm21_dev_5d_diff":         {"inputs": ["pe"],                                           "func": yld_drv2_051_earnings_yield_ewm21_dev_5d_diff},
    "yld_drv2_052_sales_yield_ewm21_dev_5d_diff":            {"inputs": ["ps"],                                           "func": yld_drv2_052_sales_yield_ewm21_dev_5d_diff},
    "yld_drv2_053_book_yield_ewm63_dev_5d_diff":             {"inputs": ["pb"],                                           "func": yld_drv2_053_book_yield_ewm63_dev_5d_diff},
    "yld_drv2_054_ebitda_yield_ewm63_dev_5d_diff":           {"inputs": ["evebitda"],                                     "func": yld_drv2_054_ebitda_yield_ewm63_dev_5d_diff},
    "yld_drv2_055_earnings_yield_ewm_crossover_5d_diff":     {"inputs": ["pe"],                                           "func": yld_drv2_055_earnings_yield_ewm_crossover_5d_diff},
    "yld_drv2_056_divyield_ewm_crossover_5d_diff":           {"inputs": ["divyield"],                                     "func": yld_drv2_056_divyield_ewm_crossover_5d_diff},
    "yld_drv2_057_earnings_yield_vol_63d_5d_diff":           {"inputs": ["pe"],                                           "func": yld_drv2_057_earnings_yield_vol_63d_5d_diff},
    "yld_drv2_058_divyield_vol_63d_5d_diff":                 {"inputs": ["divyield"],                                     "func": yld_drv2_058_divyield_vol_63d_5d_diff},
    "yld_drv2_059_sales_yield_vol_21d_5d_diff":              {"inputs": ["ps"],                                           "func": yld_drv2_059_sales_yield_vol_21d_5d_diff},
    "yld_drv2_060_book_yield_vol_21d_5d_diff":               {"inputs": ["pb"],                                           "func": yld_drv2_060_book_yield_vol_21d_5d_diff},
    "yld_drv2_061_earnings_yield_pct_change_21d":            {"inputs": ["pe"],                                           "func": yld_drv2_061_earnings_yield_pct_change_21d},
    "yld_drv2_062_sales_yield_pct_change_5d":                {"inputs": ["ps"],                                           "func": yld_drv2_062_sales_yield_pct_change_5d},
    "yld_drv2_063_book_yield_pct_change_5d":                 {"inputs": ["pb"],                                           "func": yld_drv2_063_book_yield_pct_change_5d},
    "yld_drv2_064_ebit_yield_pct_change_5d":                 {"inputs": ["evebit"],                                       "func": yld_drv2_064_ebit_yield_pct_change_5d},
    "yld_drv2_065_ebitda_yield_pct_change_5d":               {"inputs": ["evebitda"],                                     "func": yld_drv2_065_ebitda_yield_pct_change_5d},
    "yld_drv2_066_mcap_5d_diff":                             {"inputs": ["marketcap"],                                    "func": yld_drv2_066_mcap_5d_diff},
    "yld_drv2_067_ev_5d_diff":                               {"inputs": ["ev"],                                           "func": yld_drv2_067_ev_5d_diff},
    "yld_drv2_068_ev_to_mcap_5d_diff":                       {"inputs": ["ev", "marketcap"],                              "func": yld_drv2_068_ev_to_mcap_5d_diff},
    "yld_drv2_069_earnings_yield_streak_rise_5d_diff":       {"inputs": ["pe"],                                           "func": yld_drv2_069_earnings_yield_streak_rise_5d_diff},
    "yld_drv2_070_divyield_streak_rise_5d_diff":             {"inputs": ["divyield"],                                     "func": yld_drv2_070_divyield_streak_rise_5d_diff},
    "yld_drv2_071_composite_yield_avg_5d_diff":              {"inputs": ["pe", "ps", "pb"],                               "func": yld_drv2_071_composite_yield_avg_5d_diff},
    "yld_drv2_072_div_earnings_spread_21d_diff":             {"inputs": ["divyield", "pe"],                               "func": yld_drv2_072_div_earnings_spread_21d_diff},
    "yld_drv2_073_ebit_ebitda_spread_5d_diff":               {"inputs": ["evebit", "evebitda"],                           "func": yld_drv2_073_ebit_ebitda_spread_5d_diff},
    "yld_drv2_074_yield_dispersion_5d_diff":                 {"inputs": ["pe", "ps", "pb"],                               "func": yld_drv2_074_yield_dispersion_5d_diff},
    "yld_drv2_075_earnings_yield_expanding_zscore_5d_diff":  {"inputs": ["pe"],                                           "func": yld_drv2_075_earnings_yield_expanding_zscore_5d_diff},
}
