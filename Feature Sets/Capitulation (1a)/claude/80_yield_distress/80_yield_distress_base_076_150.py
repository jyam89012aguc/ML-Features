"""
80_yield_distress — Base Features 076-200
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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group G (076-088): Multi-window yield drawup measures ---

def yld_076_earnings_yield_756d_drawup(pe: pd.Series) -> pd.Series:
    """Earnings-yield drawup: current yield minus 756-day (3-yr) rolling minimum."""
    ey = _to_yield(pe)
    return ey - _rolling_min(ey, 756)


def yld_077_earnings_yield_1260d_drawup(pe: pd.Series) -> pd.Series:
    """Earnings-yield drawup: current yield minus 1260-day (5-yr) rolling minimum."""
    ey = _to_yield(pe)
    return ey - _rolling_min(ey, 1260)


def yld_078_earnings_yield_expanding_drawup(pe: pd.Series) -> pd.Series:
    """Earnings-yield drawup vs all-time minimum (expanding historical trough)."""
    ey = _to_yield(pe)
    return ey - ey.expanding(min_periods=1).min()


def yld_079_sales_yield_504d_drawup(ps: pd.Series) -> pd.Series:
    """Sales-yield drawup: current yield minus 504-day rolling minimum."""
    sy = _to_yield(ps)
    return sy - _rolling_min(sy, 504)


def yld_080_sales_yield_756d_drawup(ps: pd.Series) -> pd.Series:
    """Sales-yield drawup: current yield minus 756-day rolling minimum."""
    sy = _to_yield(ps)
    return sy - _rolling_min(sy, 756)


def yld_081_sales_yield_expanding_drawup(ps: pd.Series) -> pd.Series:
    """Sales-yield drawup vs all-time minimum."""
    sy = _to_yield(ps)
    return sy - sy.expanding(min_periods=1).min()


def yld_082_book_yield_504d_drawup(pb: pd.Series) -> pd.Series:
    """Book-yield drawup: current yield minus 504-day rolling minimum."""
    by = _to_yield(pb)
    return by - _rolling_min(by, 504)


def yld_083_book_yield_expanding_drawup(pb: pd.Series) -> pd.Series:
    """Book-yield drawup vs all-time minimum."""
    by = _to_yield(pb)
    return by - by.expanding(min_periods=1).min()


def yld_084_ebitda_yield_504d_drawup(evebitda: pd.Series) -> pd.Series:
    """EBITDA-yield drawup: current yield minus 504-day rolling minimum."""
    ey = _to_yield(evebitda)
    return ey - _rolling_min(ey, 504)


def yld_085_ebitda_yield_756d_drawup(evebitda: pd.Series) -> pd.Series:
    """EBITDA-yield drawup: current yield minus 756-day rolling minimum."""
    ey = _to_yield(evebitda)
    return ey - _rolling_min(ey, 756)


def yld_086_ebit_yield_504d_drawup(evebit: pd.Series) -> pd.Series:
    """EBIT-yield drawup: current yield minus 504-day rolling minimum."""
    ey = _to_yield(evebit)
    return ey - _rolling_min(ey, 504)


def yld_087_divyield_504d_drawup(divyield: pd.Series) -> pd.Series:
    """Dividend-yield drawup: current yield minus 504-day rolling minimum."""
    return divyield - _rolling_min(divyield, 504)


def yld_088_divyield_expanding_drawup(divyield: pd.Series) -> pd.Series:
    """Dividend-yield drawup vs all-time minimum."""
    return divyield - divyield.expanding(min_periods=1).min()


# --- Group H (089-100): Rolling OLS slope of yield series ---

def yld_089_earnings_yield_21d_slope(pe: pd.Series) -> pd.Series:
    """OLS slope of earnings yield over trailing 21 days (short-term speed)."""
    return _linslope(_to_yield(pe), _TD_MON)


def yld_090_earnings_yield_63d_slope(pe: pd.Series) -> pd.Series:
    """OLS slope of earnings yield over trailing 63 days."""
    return _linslope(_to_yield(pe), _TD_QTR)


def yld_091_earnings_yield_252d_slope(pe: pd.Series) -> pd.Series:
    """OLS slope of earnings yield over trailing 252 days."""
    return _linslope(_to_yield(pe), _TD_YEAR)


def yld_092_divyield_21d_slope(divyield: pd.Series) -> pd.Series:
    """OLS slope of dividend yield over trailing 21 days."""
    return _linslope(divyield, _TD_MON)


def yld_093_divyield_63d_slope(divyield: pd.Series) -> pd.Series:
    """OLS slope of dividend yield over trailing 63 days."""
    return _linslope(divyield, _TD_QTR)


def yld_094_sales_yield_21d_slope(ps: pd.Series) -> pd.Series:
    """OLS slope of sales yield over trailing 21 days."""
    return _linslope(_to_yield(ps), _TD_MON)


def yld_095_book_yield_21d_slope(pb: pd.Series) -> pd.Series:
    """OLS slope of book yield over trailing 21 days."""
    return _linslope(_to_yield(pb), _TD_MON)


def yld_096_ebit_yield_21d_slope(evebit: pd.Series) -> pd.Series:
    """OLS slope of EBIT yield over trailing 21 days."""
    return _linslope(_to_yield(evebit), _TD_MON)


def yld_097_ebitda_yield_21d_slope(evebitda: pd.Series) -> pd.Series:
    """OLS slope of EBITDA yield over trailing 21 days."""
    return _linslope(_to_yield(evebitda), _TD_MON)


def yld_098_earnings_yield_slope_accel_ratio(pe: pd.Series) -> pd.Series:
    """Ratio of 21-day slope to 63-day slope of earnings yield (slope acceleration)."""
    return _safe_div(_linslope(_to_yield(pe), _TD_MON),
                     _linslope(_to_yield(pe), _TD_QTR).abs() + _EPS)


def yld_099_divyield_slope_zscore_252d(divyield: pd.Series) -> pd.Series:
    """Z-score of 21-day dividend yield slope over trailing 252 days."""
    slope = _linslope(divyield, _TD_MON)
    return _zscore_rolling(slope, _TD_YEAR)


def yld_100_composite_yield_21d_slope(pe: pd.Series, ps: pd.Series, pb: pd.Series) -> pd.Series:
    """Average 21-day slope across earnings, sales and book yields."""
    s1 = _linslope(_to_yield(pe), _TD_MON)
    s2 = _linslope(_to_yield(ps), _TD_MON)
    s3 = _linslope(_to_yield(pb), _TD_MON)
    return (s1.fillna(0) + s2.fillna(0) + s3.fillna(0)) / 3.0


# --- Group I (101-112): Consecutive rising-yield streaks ---

def yld_101_earnings_yield_streak_rise_21d(pe: pd.Series) -> pd.Series:
    """Days earnings yield rose (daily diff > 0) within trailing 21 days."""
    ey = _to_yield(pe)
    return _rolling_sum((ey.diff(1) > 0).astype(float), _TD_MON)


def yld_102_earnings_yield_streak_rise_63d(pe: pd.Series) -> pd.Series:
    """Days earnings yield rose within trailing 63 days."""
    ey = _to_yield(pe)
    return _rolling_sum((ey.diff(1) > 0).astype(float), _TD_QTR)


def yld_103_sales_yield_streak_rise_21d(ps: pd.Series) -> pd.Series:
    """Days sales yield rose within trailing 21 days."""
    sy = _to_yield(ps)
    return _rolling_sum((sy.diff(1) > 0).astype(float), _TD_MON)


def yld_104_book_yield_streak_rise_21d(pb: pd.Series) -> pd.Series:
    """Days book yield rose within trailing 21 days."""
    by = _to_yield(pb)
    return _rolling_sum((by.diff(1) > 0).astype(float), _TD_MON)


def yld_105_divyield_streak_rise_63d(divyield: pd.Series) -> pd.Series:
    """Days dividend yield rose within trailing 63 days."""
    return _rolling_sum((divyield.diff(1) > 0).astype(float), _TD_QTR)


def yld_106_ebit_yield_streak_rise_21d(evebit: pd.Series) -> pd.Series:
    """Days EBIT yield rose within trailing 21 days."""
    ey = _to_yield(evebit)
    return _rolling_sum((ey.diff(1) > 0).astype(float), _TD_MON)


def yld_107_ebitda_yield_streak_rise_21d(evebitda: pd.Series) -> pd.Series:
    """Days EBITDA yield rose within trailing 21 days."""
    ey = _to_yield(evebitda)
    return _rolling_sum((ey.diff(1) > 0).astype(float), _TD_MON)


def yld_108_multi_yield_rise_breadth_21d(pe: pd.Series, ps: pd.Series,
                                          pb: pd.Series, divyield: pd.Series) -> pd.Series:
    """Average fraction of days each of 4 yields rose over trailing 21 days."""
    series = [_to_yield(pe), _to_yield(ps), _to_yield(pb), divyield]
    fracs  = [_rolling_sum((s.diff(1) > 0).astype(float), _TD_MON) / _TD_MON
              for s in series]
    return sum(fracs) / 4.0


def yld_109_earnings_yield_above_median_63d(pe: pd.Series) -> pd.Series:
    """Fraction of last 63 days earnings yield exceeded its 63-day median."""
    ey  = _to_yield(pe)
    med = _rolling_median(ey, _TD_QTR)
    return _rolling_sum((ey > med).astype(float), _TD_QTR) / _TD_QTR


def yld_110_divyield_above_median_63d(divyield: pd.Series) -> pd.Series:
    """Fraction of last 63 days dividend yield exceeded its 63-day median."""
    med = _rolling_median(divyield, _TD_QTR)
    return _rolling_sum((divyield > med).astype(float), _TD_QTR) / _TD_QTR


def yld_111_earnings_yield_days_above_20pct_21d(pe: pd.Series) -> pd.Series:
    """Days earnings yield > 20% within trailing 21 days."""
    return _rolling_sum((_to_yield(pe) > 0.20).astype(float), _TD_MON)


def yld_112_divyield_days_above_8pct_63d(divyield: pd.Series) -> pd.Series:
    """Days dividend yield > 8% within trailing 63 days."""
    return _rolling_sum((divyield > 0.08).astype(float), _TD_QTR)


# --- Group J (113-124): EWM and momentum-based yield measures ---

def yld_113_earnings_yield_ewm21_dev(pe: pd.Series) -> pd.Series:
    """Earnings yield minus its 21-day EMA (short-term EWM deviation)."""
    ey = _to_yield(pe)
    return ey - _ewm_mean(ey, _TD_MON)


def yld_114_earnings_yield_ewm63_dev(pe: pd.Series) -> pd.Series:
    """Earnings yield minus its 63-day EMA."""
    ey = _to_yield(pe)
    return ey - _ewm_mean(ey, _TD_QTR)


def yld_115_earnings_yield_ewm_crossover(pe: pd.Series) -> pd.Series:
    """21-day EMA minus 63-day EMA of earnings yield (yield-EMA crossover)."""
    ey = _to_yield(pe)
    return _ewm_mean(ey, _TD_MON) - _ewm_mean(ey, _TD_QTR)


def yld_116_divyield_ewm21_dev(divyield: pd.Series) -> pd.Series:
    """Dividend yield minus its 21-day EMA."""
    return divyield - _ewm_mean(divyield, _TD_MON)


def yld_117_divyield_ewm_crossover(divyield: pd.Series) -> pd.Series:
    """21-day EMA minus 63-day EMA of dividend yield."""
    return _ewm_mean(divyield, _TD_MON) - _ewm_mean(divyield, _TD_QTR)


def yld_118_sales_yield_ewm21_dev(ps: pd.Series) -> pd.Series:
    """Sales yield minus its 21-day EMA."""
    sy = _to_yield(ps)
    return sy - _ewm_mean(sy, _TD_MON)


def yld_119_book_yield_ewm63_dev(pb: pd.Series) -> pd.Series:
    """Book yield minus its 63-day EMA."""
    by = _to_yield(pb)
    return by - _ewm_mean(by, _TD_QTR)


def yld_120_ebitda_yield_ewm63_dev(evebitda: pd.Series) -> pd.Series:
    """EBITDA yield minus its 63-day EMA."""
    ey = _to_yield(evebitda)
    return ey - _ewm_mean(ey, _TD_QTR)


def yld_121_earnings_yield_5d_pct_change(pe: pd.Series) -> pd.Series:
    """5-day percent change in earnings yield (rapid spike rate)."""
    ey = _to_yield(pe)
    return _safe_div(ey - ey.shift(5), ey.shift(5).abs() + _EPS)


def yld_122_divyield_5d_pct_change(divyield: pd.Series) -> pd.Series:
    """5-day percent change in dividend yield."""
    return _safe_div(divyield - divyield.shift(5), divyield.shift(5).abs() + _EPS)


def yld_123_divyield_21d_pct_change(divyield: pd.Series) -> pd.Series:
    """21-day percent change in dividend yield (monthly spike rate)."""
    return _safe_div(divyield - divyield.shift(_TD_MON),
                     divyield.shift(_TD_MON).abs() + _EPS)


def yld_124_earnings_yield_63d_pct_change(pe: pd.Series) -> pd.Series:
    """63-day percent change in earnings yield (quarterly spike rate)."""
    ey = _to_yield(pe)
    return _safe_div(ey - ey.shift(_TD_QTR), ey.shift(_TD_QTR).abs() + _EPS)


# --- Group K (125-136): Yield vs EV/marketcap structural measures ---

def yld_125_ev_to_mcap_ratio(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EV / market cap ratio (leverage lift on enterprise value vs equity)."""
    return _safe_div(ev, marketcap)


def yld_126_ev_to_mcap_zscore_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Z-score of EV/marketcap ratio over trailing 252 days."""
    ratio = _safe_div(ev, marketcap)
    return _zscore_rolling(ratio, _TD_YEAR)


def yld_127_earnings_yield_times_mcap(pe: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Earnings yield times log(marketcap) — yield adjusted for size context."""
    ey = _to_yield(pe)
    lmc = np.log(marketcap.clip(lower=_EPS))
    return ey * lmc


def yld_128_divyield_times_mcap_log(divyield: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Dividend yield times log(marketcap)."""
    return divyield * np.log(marketcap.clip(lower=_EPS))


def yld_129_ebitda_yield_ev_normalized(evebitda: pd.Series, ev: pd.Series) -> pd.Series:
    """EBITDA yield scaled by log(EV) to normalize for enterprise size."""
    ey  = _to_yield(evebitda)
    lev = np.log(ev.clip(lower=_EPS))
    return ey * lev


def yld_130_mcap_pct_rank_252d(marketcap: pd.Series) -> pd.Series:
    """Percentile rank of marketcap within trailing 252 days (size collapse signal)."""
    return _rolling_rank_pct(marketcap, _TD_YEAR)


def yld_131_mcap_vs_252d_avg(marketcap: pd.Series) -> pd.Series:
    """Market cap deviation from 252-day average (% collapse)."""
    avg = _rolling_mean(marketcap, _TD_YEAR)
    return _safe_div(marketcap - avg, avg)


def yld_132_mcap_zscore_252d(marketcap: pd.Series) -> pd.Series:
    """Z-score of marketcap over trailing 252 days."""
    return _zscore_rolling(marketcap, _TD_YEAR)


def yld_133_ev_pct_rank_252d(ev: pd.Series) -> pd.Series:
    """Percentile rank of EV within trailing 252 days."""
    return _rolling_rank_pct(ev, _TD_YEAR)


def yld_134_ev_vs_252d_avg(ev: pd.Series) -> pd.Series:
    """EV deviation from 252-day average (%)."""
    avg = _rolling_mean(ev, _TD_YEAR)
    return _safe_div(ev - avg, avg)


def yld_135_earnings_yield_vs_book_yield_ratio(pe: pd.Series, pb: pd.Series) -> pd.Series:
    """Earnings yield divided by book yield (ROE proxy from market-implied yields)."""
    return _safe_div(_to_yield(pe), _to_yield(pb))


def yld_136_sales_yield_vs_book_yield_ratio(ps: pd.Series, pb: pd.Series) -> pd.Series:
    """Sales yield divided by book yield (asset-turn proxy from yields)."""
    return _safe_div(_to_yield(ps), _to_yield(pb))


# --- Group L (137-150): Yield-trap and distress composite scores ---

def yld_137_yield_trap_score(divyield: pd.Series, pe: pd.Series) -> pd.Series:
    """Yield trap score: divyield > earnings yield AND divyield z-score > 1.5."""
    ey      = _to_yield(pe)
    dz      = _zscore_rolling(divyield, _TD_YEAR)
    trap    = ((divyield > ey) & (dz > 1.5)).astype(float)
    return trap


def yld_138_earnings_yield_vol_21d(pe: pd.Series) -> pd.Series:
    """21-day rolling std of earnings yield (yield volatility)."""
    return _rolling_std(_to_yield(pe), _TD_MON)


def yld_139_earnings_yield_vol_63d(pe: pd.Series) -> pd.Series:
    """63-day rolling std of earnings yield."""
    return _rolling_std(_to_yield(pe), _TD_QTR)


def yld_140_divyield_vol_63d(divyield: pd.Series) -> pd.Series:
    """63-day rolling std of dividend yield."""
    return _rolling_std(divyield, _TD_QTR)


def yld_141_ebitda_yield_vol_63d(evebitda: pd.Series) -> pd.Series:
    """63-day rolling std of EBITDA yield."""
    return _rolling_std(_to_yield(evebitda), _TD_QTR)


def yld_142_earnings_yield_skew_252d(pe: pd.Series) -> pd.Series:
    """Skewness of earnings yield over trailing 252 days (positive = right-tail spikes)."""
    return _to_yield(pe).rolling(_TD_YEAR, min_periods=_TD_QTR).skew()


def yld_143_divyield_skew_252d(divyield: pd.Series) -> pd.Series:
    """Skewness of dividend yield over trailing 252 days."""
    return divyield.rolling(_TD_YEAR, min_periods=_TD_QTR).skew()


def yld_144_earnings_yield_q95_252d(pe: pd.Series) -> pd.Series:
    """95th-percentile of earnings yield over trailing 252 days (tail distress level)."""
    return _to_yield(pe).rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.95)


def yld_145_divyield_q95_252d(divyield: pd.Series) -> pd.Series:
    """95th-percentile of dividend yield over trailing 252 days."""
    return divyield.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.95)


def yld_146_earnings_yield_q95_vs_current(pe: pd.Series) -> pd.Series:
    """Earnings yield vs its trailing 252-day 95th-percentile (how close to tail)."""
    ey  = _to_yield(pe)
    q95 = ey.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.95)
    return _safe_div(ey, q95)


def yld_147_divyield_q95_vs_current(divyield: pd.Series) -> pd.Series:
    """Dividend yield vs its trailing 252-day 95th-percentile."""
    q95 = divyield.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.95)
    return _safe_div(divyield, q95)


def yld_148_multi_yield_distress_composite(pe: pd.Series, ps: pd.Series,
                                            pb: pd.Series, evebit: pd.Series,
                                            evebitda: pd.Series,
                                            divyield: pd.Series) -> pd.Series:
    """Composite distress score: average z-score across all 6 yields (252d window)."""
    zs = [
        _zscore_rolling(_to_yield(pe),      _TD_YEAR),
        _zscore_rolling(_to_yield(ps),      _TD_YEAR),
        _zscore_rolling(_to_yield(pb),      _TD_YEAR),
        _zscore_rolling(_to_yield(evebit),  _TD_YEAR),
        _zscore_rolling(_to_yield(evebitda),_TD_YEAR),
        _zscore_rolling(divyield,           _TD_YEAR),
    ]
    stack = pd.concat(zs, axis=1)
    return stack.mean(axis=1)


def yld_149_yield_dispersion_252d(pe: pd.Series, ps: pd.Series,
                                   pb: pd.Series) -> pd.Series:
    """Std dev of earnings/sales/book yields at each point (yield dispersion)."""
    stack = pd.concat([_to_yield(pe), _to_yield(ps), _to_yield(pb)], axis=1)
    return stack.std(axis=1)


def yld_150_earnings_yield_recovery_from_min(pe: pd.Series) -> pd.Series:
    """Earnings yield % above its expanding all-time minimum (recovery signal)."""
    ey  = _to_yield(pe)
    mn  = ey.expanding(min_periods=1).min()
    return _safe_div(ey - mn, mn.abs() + _EPS)


# --- Group M (176-200): Advanced volatility, quantile, and cross-yield measures ---

def yld_176_earnings_yield_vol_252d(pe: pd.Series) -> pd.Series:
    """252-day rolling std of earnings yield (annual yield volatility)."""
    return _rolling_std(_to_yield(pe), _TD_YEAR)


def yld_177_sales_yield_vol_21d(ps: pd.Series) -> pd.Series:
    """21-day rolling std of sales yield."""
    return _rolling_std(_to_yield(ps), _TD_MON)


def yld_178_book_yield_vol_21d(pb: pd.Series) -> pd.Series:
    """21-day rolling std of book yield."""
    return _rolling_std(_to_yield(pb), _TD_MON)


def yld_179_ebit_yield_vol_63d(evebit: pd.Series) -> pd.Series:
    """63-day rolling std of EBIT yield."""
    return _rolling_std(_to_yield(evebit), _TD_QTR)


def yld_180_divyield_vol_21d(divyield: pd.Series) -> pd.Series:
    """21-day rolling std of dividend yield."""
    return _rolling_std(divyield, _TD_MON)


def yld_181_earnings_yield_q05_252d(pe: pd.Series) -> pd.Series:
    """5th-percentile of earnings yield over trailing 252 days (cheapness floor)."""
    return _to_yield(pe).rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.05)


def yld_182_earnings_yield_q75_252d(pe: pd.Series) -> pd.Series:
    """75th-percentile of earnings yield over trailing 252 days."""
    return _to_yield(pe).rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)


def yld_183_divyield_q75_252d(divyield: pd.Series) -> pd.Series:
    """75th-percentile of dividend yield over trailing 252 days."""
    return divyield.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)


def yld_184_sales_yield_skew_252d(ps: pd.Series) -> pd.Series:
    """Skewness of sales yield over trailing 252 days."""
    return _to_yield(ps).rolling(_TD_YEAR, min_periods=_TD_QTR).skew()


def yld_185_book_yield_skew_252d(pb: pd.Series) -> pd.Series:
    """Skewness of book yield over trailing 252 days."""
    return _to_yield(pb).rolling(_TD_YEAR, min_periods=_TD_QTR).skew()


def yld_186_ebitda_yield_vs_book_yield_ratio(evebitda: pd.Series, pb: pd.Series) -> pd.Series:
    """EBITDA yield divided by book yield (cash-generation vs asset backing)."""
    return _safe_div(_to_yield(evebitda), _to_yield(pb))


def yld_187_ebit_yield_vs_earnings_yield_ratio(evebit: pd.Series, pe: pd.Series) -> pd.Series:
    """EBIT yield divided by earnings yield (pre/post-tax gap proxy)."""
    return _safe_div(_to_yield(evebit), _to_yield(pe))


def yld_188_div_vs_ebit_yield_ratio(divyield: pd.Series, evebit: pd.Series) -> pd.Series:
    """Dividend yield divided by EBIT yield (payout vs operating-earnings backing)."""
    return _safe_div(divyield, _to_yield(evebit))


def yld_189_composite_yield_pct_rank_252d(pe: pd.Series, ps: pd.Series,
                                           pb: pd.Series) -> pd.Series:
    """Percentile rank of composite (earnings+sales+book) yield within 252 days."""
    comp = (_to_yield(pe).fillna(0) + _to_yield(ps).fillna(0) +
            _to_yield(pb).fillna(0)) / 3.0
    return _rolling_rank_pct(comp, _TD_YEAR)


def yld_190_earnings_yield_126d_slope(pe: pd.Series) -> pd.Series:
    """OLS slope of earnings yield over trailing 126 days (half-year trend)."""
    return _linslope(_to_yield(pe), _TD_HALF)


def yld_191_divyield_126d_slope(divyield: pd.Series) -> pd.Series:
    """OLS slope of dividend yield over trailing 126 days."""
    return _linslope(divyield, _TD_HALF)


def yld_192_sales_yield_63d_slope(ps: pd.Series) -> pd.Series:
    """OLS slope of sales yield over trailing 63 days."""
    return _linslope(_to_yield(ps), _TD_QTR)


def yld_193_book_yield_63d_slope(pb: pd.Series) -> pd.Series:
    """OLS slope of book yield over trailing 63 days."""
    return _linslope(_to_yield(pb), _TD_QTR)


def yld_194_ebitda_yield_63d_slope(evebitda: pd.Series) -> pd.Series:
    """OLS slope of EBITDA yield over trailing 63 days."""
    return _linslope(_to_yield(evebitda), _TD_QTR)


def yld_195_ebit_yield_63d_slope(evebit: pd.Series) -> pd.Series:
    """OLS slope of EBIT yield over trailing 63 days."""
    return _linslope(_to_yield(evebit), _TD_QTR)


def yld_196_mcap_expanding_zscore(marketcap: pd.Series) -> pd.Series:
    """Expanding z-score of market cap (how extreme vs own all-time history)."""
    m  = marketcap.expanding(min_periods=5).mean()
    sd = marketcap.expanding(min_periods=5).std()
    return _safe_div(marketcap - m, sd)


def yld_197_ev_expanding_zscore(ev: pd.Series) -> pd.Series:
    """Expanding z-score of enterprise value."""
    m  = ev.expanding(min_periods=5).mean()
    sd = ev.expanding(min_periods=5).std()
    return _safe_div(ev - m, sd)


def yld_198_earnings_yield_days_above_33pct_63d(pe: pd.Series) -> pd.Series:
    """Days earnings yield > 33% within trailing 63 days."""
    return _rolling_sum((_to_yield(pe) > 0.33).astype(float), _TD_QTR)


def yld_199_divyield_days_above_10pct_63d(divyield: pd.Series) -> pd.Series:
    """Days dividend yield > 10% within trailing 63 days."""
    return _rolling_sum((divyield > 0.10).astype(float), _TD_QTR)


def yld_200_yield_distress_composite_pct_rank(pe: pd.Series, ps: pd.Series,
                                               pb: pd.Series, evebit: pd.Series,
                                               evebitda: pd.Series,
                                               divyield: pd.Series) -> pd.Series:
    """Percentile rank of 6-yield average z-score composite (252-day window)."""
    zs = [
        _zscore_rolling(_to_yield(pe),       _TD_YEAR),
        _zscore_rolling(_to_yield(ps),       _TD_YEAR),
        _zscore_rolling(_to_yield(pb),       _TD_YEAR),
        _zscore_rolling(_to_yield(evebit),   _TD_YEAR),
        _zscore_rolling(_to_yield(evebitda), _TD_YEAR),
        _zscore_rolling(divyield,            _TD_YEAR),
    ]
    comp = pd.concat(zs, axis=1).mean(axis=1)
    return _rolling_rank_pct(comp, _TD_YEAR)


# ── Registry ──────────────────────────────────────────────────────────────────

YIELD_DISTRESS_REGISTRY_076_150 = {
    "yld_076_earnings_yield_756d_drawup":         {"inputs": ["pe"],                                                               "func": yld_076_earnings_yield_756d_drawup},
    "yld_077_earnings_yield_1260d_drawup":         {"inputs": ["pe"],                                                               "func": yld_077_earnings_yield_1260d_drawup},
    "yld_078_earnings_yield_expanding_drawup":     {"inputs": ["pe"],                                                               "func": yld_078_earnings_yield_expanding_drawup},
    "yld_079_sales_yield_504d_drawup":             {"inputs": ["ps"],                                                               "func": yld_079_sales_yield_504d_drawup},
    "yld_080_sales_yield_756d_drawup":             {"inputs": ["ps"],                                                               "func": yld_080_sales_yield_756d_drawup},
    "yld_081_sales_yield_expanding_drawup":        {"inputs": ["ps"],                                                               "func": yld_081_sales_yield_expanding_drawup},
    "yld_082_book_yield_504d_drawup":              {"inputs": ["pb"],                                                               "func": yld_082_book_yield_504d_drawup},
    "yld_083_book_yield_expanding_drawup":         {"inputs": ["pb"],                                                               "func": yld_083_book_yield_expanding_drawup},
    "yld_084_ebitda_yield_504d_drawup":            {"inputs": ["evebitda"],                                                         "func": yld_084_ebitda_yield_504d_drawup},
    "yld_085_ebitda_yield_756d_drawup":            {"inputs": ["evebitda"],                                                         "func": yld_085_ebitda_yield_756d_drawup},
    "yld_086_ebit_yield_504d_drawup":              {"inputs": ["evebit"],                                                           "func": yld_086_ebit_yield_504d_drawup},
    "yld_087_divyield_504d_drawup":                {"inputs": ["divyield"],                                                         "func": yld_087_divyield_504d_drawup},
    "yld_088_divyield_expanding_drawup":           {"inputs": ["divyield"],                                                         "func": yld_088_divyield_expanding_drawup},
    "yld_089_earnings_yield_21d_slope":            {"inputs": ["pe"],                                                               "func": yld_089_earnings_yield_21d_slope},
    "yld_090_earnings_yield_63d_slope":            {"inputs": ["pe"],                                                               "func": yld_090_earnings_yield_63d_slope},
    "yld_091_earnings_yield_252d_slope":           {"inputs": ["pe"],                                                               "func": yld_091_earnings_yield_252d_slope},
    "yld_092_divyield_21d_slope":                  {"inputs": ["divyield"],                                                         "func": yld_092_divyield_21d_slope},
    "yld_093_divyield_63d_slope":                  {"inputs": ["divyield"],                                                         "func": yld_093_divyield_63d_slope},
    "yld_094_sales_yield_21d_slope":               {"inputs": ["ps"],                                                               "func": yld_094_sales_yield_21d_slope},
    "yld_095_book_yield_21d_slope":                {"inputs": ["pb"],                                                               "func": yld_095_book_yield_21d_slope},
    "yld_096_ebit_yield_21d_slope":                {"inputs": ["evebit"],                                                           "func": yld_096_ebit_yield_21d_slope},
    "yld_097_ebitda_yield_21d_slope":              {"inputs": ["evebitda"],                                                         "func": yld_097_ebitda_yield_21d_slope},
    "yld_098_earnings_yield_slope_accel_ratio":    {"inputs": ["pe"],                                                               "func": yld_098_earnings_yield_slope_accel_ratio},
    "yld_099_divyield_slope_zscore_252d":          {"inputs": ["divyield"],                                                         "func": yld_099_divyield_slope_zscore_252d},
    "yld_100_composite_yield_21d_slope":           {"inputs": ["pe", "ps", "pb"],                                                   "func": yld_100_composite_yield_21d_slope},
    "yld_101_earnings_yield_streak_rise_21d":      {"inputs": ["pe"],                                                               "func": yld_101_earnings_yield_streak_rise_21d},
    "yld_102_earnings_yield_streak_rise_63d":      {"inputs": ["pe"],                                                               "func": yld_102_earnings_yield_streak_rise_63d},
    "yld_103_sales_yield_streak_rise_21d":         {"inputs": ["ps"],                                                               "func": yld_103_sales_yield_streak_rise_21d},
    "yld_104_book_yield_streak_rise_21d":          {"inputs": ["pb"],                                                               "func": yld_104_book_yield_streak_rise_21d},
    "yld_105_divyield_streak_rise_63d":            {"inputs": ["divyield"],                                                         "func": yld_105_divyield_streak_rise_63d},
    "yld_106_ebit_yield_streak_rise_21d":          {"inputs": ["evebit"],                                                           "func": yld_106_ebit_yield_streak_rise_21d},
    "yld_107_ebitda_yield_streak_rise_21d":        {"inputs": ["evebitda"],                                                         "func": yld_107_ebitda_yield_streak_rise_21d},
    "yld_108_multi_yield_rise_breadth_21d":        {"inputs": ["pe", "ps", "pb", "divyield"],                                       "func": yld_108_multi_yield_rise_breadth_21d},
    "yld_109_earnings_yield_above_median_63d":     {"inputs": ["pe"],                                                               "func": yld_109_earnings_yield_above_median_63d},
    "yld_110_divyield_above_median_63d":           {"inputs": ["divyield"],                                                         "func": yld_110_divyield_above_median_63d},
    "yld_111_earnings_yield_days_above_20pct_21d": {"inputs": ["pe"],                                                               "func": yld_111_earnings_yield_days_above_20pct_21d},
    "yld_112_divyield_days_above_8pct_63d":        {"inputs": ["divyield"],                                                         "func": yld_112_divyield_days_above_8pct_63d},
    "yld_113_earnings_yield_ewm21_dev":            {"inputs": ["pe"],                                                               "func": yld_113_earnings_yield_ewm21_dev},
    "yld_114_earnings_yield_ewm63_dev":            {"inputs": ["pe"],                                                               "func": yld_114_earnings_yield_ewm63_dev},
    "yld_115_earnings_yield_ewm_crossover":        {"inputs": ["pe"],                                                               "func": yld_115_earnings_yield_ewm_crossover},
    "yld_116_divyield_ewm21_dev":                  {"inputs": ["divyield"],                                                         "func": yld_116_divyield_ewm21_dev},
    "yld_117_divyield_ewm_crossover":              {"inputs": ["divyield"],                                                         "func": yld_117_divyield_ewm_crossover},
    "yld_118_sales_yield_ewm21_dev":               {"inputs": ["ps"],                                                               "func": yld_118_sales_yield_ewm21_dev},
    "yld_119_book_yield_ewm63_dev":                {"inputs": ["pb"],                                                               "func": yld_119_book_yield_ewm63_dev},
    "yld_120_ebitda_yield_ewm63_dev":              {"inputs": ["evebitda"],                                                         "func": yld_120_ebitda_yield_ewm63_dev},
    "yld_121_earnings_yield_5d_pct_change":        {"inputs": ["pe"],                                                               "func": yld_121_earnings_yield_5d_pct_change},
    "yld_122_divyield_5d_pct_change":              {"inputs": ["divyield"],                                                         "func": yld_122_divyield_5d_pct_change},
    "yld_123_divyield_21d_pct_change":             {"inputs": ["divyield"],                                                         "func": yld_123_divyield_21d_pct_change},
    "yld_124_earnings_yield_63d_pct_change":       {"inputs": ["pe"],                                                               "func": yld_124_earnings_yield_63d_pct_change},
    "yld_125_ev_to_mcap_ratio":                    {"inputs": ["ev", "marketcap"],                                                  "func": yld_125_ev_to_mcap_ratio},
    "yld_126_ev_to_mcap_zscore_252d":              {"inputs": ["ev", "marketcap"],                                                  "func": yld_126_ev_to_mcap_zscore_252d},
    "yld_127_earnings_yield_times_mcap":           {"inputs": ["pe", "marketcap"],                                                  "func": yld_127_earnings_yield_times_mcap},
    "yld_128_divyield_times_mcap_log":             {"inputs": ["divyield", "marketcap"],                                            "func": yld_128_divyield_times_mcap_log},
    "yld_129_ebitda_yield_ev_normalized":          {"inputs": ["evebitda", "ev"],                                                   "func": yld_129_ebitda_yield_ev_normalized},
    "yld_130_mcap_pct_rank_252d":                  {"inputs": ["marketcap"],                                                        "func": yld_130_mcap_pct_rank_252d},
    "yld_131_mcap_vs_252d_avg":                    {"inputs": ["marketcap"],                                                        "func": yld_131_mcap_vs_252d_avg},
    "yld_132_mcap_zscore_252d":                    {"inputs": ["marketcap"],                                                        "func": yld_132_mcap_zscore_252d},
    "yld_133_ev_pct_rank_252d":                    {"inputs": ["ev"],                                                               "func": yld_133_ev_pct_rank_252d},
    "yld_134_ev_vs_252d_avg":                      {"inputs": ["ev"],                                                               "func": yld_134_ev_vs_252d_avg},
    "yld_135_earnings_yield_vs_book_yield_ratio":  {"inputs": ["pe", "pb"],                                                         "func": yld_135_earnings_yield_vs_book_yield_ratio},
    "yld_136_sales_yield_vs_book_yield_ratio":     {"inputs": ["ps", "pb"],                                                         "func": yld_136_sales_yield_vs_book_yield_ratio},
    "yld_137_yield_trap_score":                    {"inputs": ["divyield", "pe"],                                                   "func": yld_137_yield_trap_score},
    "yld_138_earnings_yield_vol_21d":              {"inputs": ["pe"],                                                               "func": yld_138_earnings_yield_vol_21d},
    "yld_139_earnings_yield_vol_63d":              {"inputs": ["pe"],                                                               "func": yld_139_earnings_yield_vol_63d},
    "yld_140_divyield_vol_63d":                    {"inputs": ["divyield"],                                                         "func": yld_140_divyield_vol_63d},
    "yld_141_ebitda_yield_vol_63d":                {"inputs": ["evebitda"],                                                         "func": yld_141_ebitda_yield_vol_63d},
    "yld_142_earnings_yield_skew_252d":            {"inputs": ["pe"],                                                               "func": yld_142_earnings_yield_skew_252d},
    "yld_143_divyield_skew_252d":                  {"inputs": ["divyield"],                                                         "func": yld_143_divyield_skew_252d},
    "yld_144_earnings_yield_q95_252d":             {"inputs": ["pe"],                                                               "func": yld_144_earnings_yield_q95_252d},
    "yld_145_divyield_q95_252d":                   {"inputs": ["divyield"],                                                         "func": yld_145_divyield_q95_252d},
    "yld_146_earnings_yield_q95_vs_current":       {"inputs": ["pe"],                                                               "func": yld_146_earnings_yield_q95_vs_current},
    "yld_147_divyield_q95_vs_current":             {"inputs": ["divyield"],                                                         "func": yld_147_divyield_q95_vs_current},
    "yld_148_multi_yield_distress_composite":      {"inputs": ["pe", "ps", "pb", "evebit", "evebitda", "divyield"],                 "func": yld_148_multi_yield_distress_composite},
    "yld_149_yield_dispersion_252d":               {"inputs": ["pe", "ps", "pb"],                                                   "func": yld_149_yield_dispersion_252d},
    "yld_150_earnings_yield_recovery_from_min":    {"inputs": ["pe"],                                                               "func": yld_150_earnings_yield_recovery_from_min},
    "yld_176_earnings_yield_vol_252d":             {"inputs": ["pe"],                                                               "func": yld_176_earnings_yield_vol_252d},
    "yld_177_sales_yield_vol_21d":                 {"inputs": ["ps"],                                                               "func": yld_177_sales_yield_vol_21d},
    "yld_178_book_yield_vol_21d":                  {"inputs": ["pb"],                                                               "func": yld_178_book_yield_vol_21d},
    "yld_179_ebit_yield_vol_63d":                  {"inputs": ["evebit"],                                                           "func": yld_179_ebit_yield_vol_63d},
    "yld_180_divyield_vol_21d":                    {"inputs": ["divyield"],                                                         "func": yld_180_divyield_vol_21d},
    "yld_181_earnings_yield_q05_252d":             {"inputs": ["pe"],                                                               "func": yld_181_earnings_yield_q05_252d},
    "yld_182_earnings_yield_q75_252d":             {"inputs": ["pe"],                                                               "func": yld_182_earnings_yield_q75_252d},
    "yld_183_divyield_q75_252d":                   {"inputs": ["divyield"],                                                         "func": yld_183_divyield_q75_252d},
    "yld_184_sales_yield_skew_252d":               {"inputs": ["ps"],                                                               "func": yld_184_sales_yield_skew_252d},
    "yld_185_book_yield_skew_252d":                {"inputs": ["pb"],                                                               "func": yld_185_book_yield_skew_252d},
    "yld_186_ebitda_yield_vs_book_yield_ratio":    {"inputs": ["evebitda", "pb"],                                                   "func": yld_186_ebitda_yield_vs_book_yield_ratio},
    "yld_187_ebit_yield_vs_earnings_yield_ratio":  {"inputs": ["evebit", "pe"],                                                     "func": yld_187_ebit_yield_vs_earnings_yield_ratio},
    "yld_188_div_vs_ebit_yield_ratio":             {"inputs": ["divyield", "evebit"],                                               "func": yld_188_div_vs_ebit_yield_ratio},
    "yld_189_composite_yield_pct_rank_252d":       {"inputs": ["pe", "ps", "pb"],                                                   "func": yld_189_composite_yield_pct_rank_252d},
    "yld_190_earnings_yield_126d_slope":           {"inputs": ["pe"],                                                               "func": yld_190_earnings_yield_126d_slope},
    "yld_191_divyield_126d_slope":                 {"inputs": ["divyield"],                                                         "func": yld_191_divyield_126d_slope},
    "yld_192_sales_yield_63d_slope":               {"inputs": ["ps"],                                                               "func": yld_192_sales_yield_63d_slope},
    "yld_193_book_yield_63d_slope":                {"inputs": ["pb"],                                                               "func": yld_193_book_yield_63d_slope},
    "yld_194_ebitda_yield_63d_slope":              {"inputs": ["evebitda"],                                                         "func": yld_194_ebitda_yield_63d_slope},
    "yld_195_ebit_yield_63d_slope":                {"inputs": ["evebit"],                                                           "func": yld_195_ebit_yield_63d_slope},
    "yld_196_mcap_expanding_zscore":               {"inputs": ["marketcap"],                                                        "func": yld_196_mcap_expanding_zscore},
    "yld_197_ev_expanding_zscore":                 {"inputs": ["ev"],                                                               "func": yld_197_ev_expanding_zscore},
    "yld_198_earnings_yield_days_above_33pct_63d": {"inputs": ["pe"],                                                               "func": yld_198_earnings_yield_days_above_33pct_63d},
    "yld_199_divyield_days_above_10pct_63d":       {"inputs": ["divyield"],                                                         "func": yld_199_divyield_days_above_10pct_63d},
    "yld_200_yield_distress_composite_pct_rank":   {"inputs": ["pe", "ps", "pb", "evebit", "evebitda", "divyield"],                 "func": yld_200_yield_distress_composite_pct_rank},
}
