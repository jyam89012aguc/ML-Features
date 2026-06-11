"""
77_valuation_collapse — Base Features 076-200
Domain: PE/PB/PS/EV-multiple compression to extremes — extended collapse measures.
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
    """Return s where s > 0, else NaN."""
    return s.where(s > 0)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope of s over w periods (scalar return per window)."""
    def _slope(x):
        n = len(x)
        if n < max(2, w // 2):
            return np.nan
        xi = np.arange(n, dtype=float)
        xi_m = xi.mean()
        xm   = x.mean()
        num  = ((xi - xi_m) * (x - xm)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=False)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group G (076-088): PE deeper analytics ---

def vcl_076_pe_252d_low_position(pe: pd.Series) -> pd.Series:
    """PE position within its 252-day range: 0 = at the low, 1 = at the high."""
    p  = _positive_mask(pe)
    hi = _rolling_max(p, _TD_YEAR)
    lo = _rolling_min(p, _TD_YEAR)
    return _safe_div(p - lo, hi - lo)


def vcl_077_pe_504d_low_position(pe: pd.Series) -> pd.Series:
    """PE position within its 504-day range."""
    p  = _positive_mask(pe)
    hi = _rolling_max(p, 504)
    lo = _rolling_min(p, 504)
    return _safe_div(p - lo, hi - lo)


def vcl_078_pe_zscore_rolling_252d(pe: pd.Series) -> pd.Series:
    """Rolling 252-day z-score of positive PE (how many SDs below trailing mean)."""
    p = _positive_mask(pe)
    return _zscore_rolling(p, _TD_YEAR)


def vcl_079_pe_zscore_rolling_504d(pe: pd.Series) -> pd.Series:
    """Rolling 504-day z-score of positive PE."""
    p = _positive_mask(pe)
    return _zscore_rolling(p, 504)


def vcl_080_pe_median_deviation_252d(pe: pd.Series) -> pd.Series:
    """Deviation of PE from its 252-day rolling median (signed)."""
    p  = _positive_mask(pe)
    md = _rolling_median(p, _TD_YEAR)
    return p - md


def vcl_081_pe_below_median_flag_252d(pe: pd.Series) -> pd.Series:
    """Binary: positive PE is below its own 252-day rolling median."""
    p  = _positive_mask(pe)
    md = _rolling_median(p, _TD_YEAR)
    return (p < md).astype(float)


def vcl_082_pe_ath_drawdown_to_current_ratio(pe: pd.Series) -> pd.Series:
    """Current PE as a fraction of its all-history maximum PE."""
    p = _positive_mask(pe)
    return _safe_div(p, _expanding_max(p))


def vcl_083_pe_range_pct_1260d(pe: pd.Series) -> pd.Series:
    """PE position within its 1260-day (5-year) range."""
    p  = _positive_mask(pe)
    hi = _rolling_max(p, 1260)
    lo = _rolling_min(p, 1260)
    return _safe_div(p - lo, hi - lo)


def vcl_084_pe_negative_transition_flag(pe: pd.Series) -> pd.Series:
    """1 on the day PE flips from positive to negative (earnings collapse event)."""
    pos_prev = (pe.shift(1) > 0)
    neg_curr = (pe < 0)
    return (pos_prev & neg_curr).astype(float)


def vcl_085_pe_negative_to_positive_flag(pe: pd.Series) -> pd.Series:
    """1 on the day PE flips from negative to positive (earnings recovery event)."""
    neg_prev = (pe.shift(1) < 0)
    pos_curr = (pe > 0)
    return (neg_prev & pos_curr).astype(float)


def vcl_086_pe_below_5_fraction_504d(pe: pd.Series) -> pd.Series:
    """Fraction of last 504 days where PE was between 0 and 5."""
    flag = ((pe > 0) & (pe < 5)).astype(float)
    return _rolling_mean(flag, 504)


def vcl_087_pe_ewm_deviation_21d(pe: pd.Series) -> pd.Series:
    """Deviation of positive PE from its 21-day EWM (short-term compression signal)."""
    p = _positive_mask(pe)
    return p - _ewm_mean(p, _TD_MON)


def vcl_088_pe_slope_21d(pe: pd.Series) -> pd.Series:
    """OLS slope of positive PE over trailing 21 days (compression trend)."""
    p = _positive_mask(pe)
    return _linslope(p, _TD_MON)


# --- Group H (089-101): PB deeper analytics ---

def vcl_089_pb_252d_low_position(pb: pd.Series) -> pd.Series:
    """PB position within its 252-day range."""
    p  = _positive_mask(pb)
    hi = _rolling_max(p, _TD_YEAR)
    lo = _rolling_min(p, _TD_YEAR)
    return _safe_div(p - lo, hi - lo)


def vcl_090_pb_zscore_rolling_252d(pb: pd.Series) -> pd.Series:
    """Rolling 252-day z-score of positive PB."""
    p = _positive_mask(pb)
    return _zscore_rolling(p, _TD_YEAR)


def vcl_091_pb_zscore_rolling_1260d(pb: pd.Series) -> pd.Series:
    """Rolling 1260-day z-score of positive PB."""
    p = _positive_mask(pb)
    return _zscore_rolling(p, 1260)


def vcl_092_pb_ath_drawdown_ratio(pb: pd.Series) -> pd.Series:
    """Current PB as fraction of its all-history maximum."""
    p = _positive_mask(pb)
    return _safe_div(p, _expanding_max(p))


def vcl_093_pb_median_deviation_504d(pb: pd.Series) -> pd.Series:
    """Deviation of positive PB from its 504-day rolling median."""
    p  = _positive_mask(pb)
    md = _rolling_median(p, 504)
    return p - md


def vcl_094_pb_slope_63d(pb: pd.Series) -> pd.Series:
    """OLS slope of positive PB over trailing 63 days."""
    p = _positive_mask(pb)
    return _linslope(p, _TD_QTR)


def vcl_095_pb_below_0_5_fraction_252d(pb: pd.Series) -> pd.Series:
    """Fraction of last 252 days where PB was between 0 and 0.5."""
    flag = ((pb > 0) & (pb < 0.5)).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def vcl_096_pb_compression_pct_63d(pb: pd.Series) -> pd.Series:
    """Percent change in positive PB over 63 days."""
    p = _positive_mask(pb)
    return _safe_div(p - p.shift(_TD_QTR), p.shift(_TD_QTR).replace(0, np.nan))


def vcl_097_pb_at_252d_low_flag(pb: pd.Series) -> pd.Series:
    """1 if positive PB equals its 252-day rolling minimum."""
    p  = _positive_mask(pb)
    lo = _rolling_min(p, _TD_YEAR)
    return (p <= lo + _EPS).astype(float)


def vcl_098_pb_compression_volatility_252d(pb: pd.Series) -> pd.Series:
    """Std dev of daily PB changes over 252 days (compression instability)."""
    p = _positive_mask(pb)
    return _rolling_std(p.diff(1), _TD_YEAR)


def vcl_099_pb_ewm_vs_rolling_mean_252d(pb: pd.Series) -> pd.Series:
    """EWM(21) of PB minus rolling 252-day mean — trend vs history gap."""
    p = _positive_mask(pb)
    return _ewm_mean(p, _TD_MON) - _rolling_mean(p, _TD_YEAR)


def vcl_100_pb_1260d_low_position(pb: pd.Series) -> pd.Series:
    """PB position within its 1260-day (5-year) range."""
    p  = _positive_mask(pb)
    hi = _rolling_max(p, 1260)
    lo = _rolling_min(p, 1260)
    return _safe_div(p - lo, hi - lo)


def vcl_101_pb_rate_of_derating_126d(pb: pd.Series) -> pd.Series:
    """Annualized rate of PB change over 126 days (half-year de-rating speed)."""
    p = _positive_mask(pb)
    chg = p - p.shift(_TD_HALF)
    return _safe_div(chg * _TD_YEAR, pd.Series(_TD_HALF, index=p.index))


# --- Group I (102-113): PS deeper analytics ---

def vcl_102_ps_252d_low_position(ps: pd.Series) -> pd.Series:
    """PS position within its 252-day range."""
    p  = _positive_mask(ps)
    hi = _rolling_max(p, _TD_YEAR)
    lo = _rolling_min(p, _TD_YEAR)
    return _safe_div(p - lo, hi - lo)


def vcl_103_ps_zscore_rolling_252d(ps: pd.Series) -> pd.Series:
    """Rolling 252-day z-score of positive PS."""
    p = _positive_mask(ps)
    return _zscore_rolling(p, _TD_YEAR)


def vcl_104_ps_ath_drawdown_ratio(ps: pd.Series) -> pd.Series:
    """Current PS as fraction of its all-history maximum."""
    p = _positive_mask(ps)
    return _safe_div(p, _expanding_max(p))


def vcl_105_ps_slope_63d(ps: pd.Series) -> pd.Series:
    """OLS slope of positive PS over trailing 63 days."""
    p = _positive_mask(ps)
    return _linslope(p, _TD_QTR)


def vcl_106_ps_slope_252d(ps: pd.Series) -> pd.Series:
    """OLS slope of positive PS over trailing 252 days."""
    p = _positive_mask(ps)
    return _linslope(p, _TD_YEAR)


def vcl_107_ps_median_deviation_252d(ps: pd.Series) -> pd.Series:
    """Deviation of positive PS from its 252-day rolling median."""
    p  = _positive_mask(ps)
    md = _rolling_median(p, _TD_YEAR)
    return p - md


def vcl_108_ps_compression_streak_63d_count(ps: pd.Series) -> pd.Series:
    """Count of declining-PS days in trailing 63 days."""
    flag = (ps.diff(1) < 0).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def vcl_109_ps_below_0_5_fraction_252d(ps: pd.Series) -> pd.Series:
    """Fraction of last 252 days where PS was between 0 and 0.5."""
    flag = ((ps > 0) & (ps < 0.5)).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def vcl_110_ps_ewm_deviation_63d(ps: pd.Series) -> pd.Series:
    """Deviation of positive PS from its 63-day EWM."""
    p = _positive_mask(ps)
    return p - _ewm_mean(p, _TD_QTR)


def vcl_111_ps_1260d_low_position(ps: pd.Series) -> pd.Series:
    """PS position within its 1260-day range."""
    p  = _positive_mask(ps)
    hi = _rolling_max(p, 1260)
    lo = _rolling_min(p, 1260)
    return _safe_div(p - lo, hi - lo)


def vcl_112_ps_rate_of_derating_126d(ps: pd.Series) -> pd.Series:
    """Annualized rate of PS change over 126 days."""
    p = _positive_mask(ps)
    chg = p - p.shift(_TD_HALF)
    return _safe_div(chg * _TD_YEAR, pd.Series(_TD_HALF, index=p.index))


def vcl_113_ps_negative_flag(ps: pd.Series) -> pd.Series:
    """Binary: PS < 0 (negative revenue or data anomaly — flag for attention)."""
    return (ps < 0).astype(float)


# --- Group J (114-124): EV/EBIT & EV/EBITDA deeper analytics ---

def vcl_114_evebit_zscore_rolling_252d(evebit: pd.Series) -> pd.Series:
    """Rolling 252-day z-score of positive EV/EBIT."""
    p = _positive_mask(evebit)
    return _zscore_rolling(p, _TD_YEAR)


def vcl_115_evebit_252d_low_position(evebit: pd.Series) -> pd.Series:
    """EV/EBIT position within its 252-day range."""
    p  = _positive_mask(evebit)
    hi = _rolling_max(p, _TD_YEAR)
    lo = _rolling_min(p, _TD_YEAR)
    return _safe_div(p - lo, hi - lo)


def vcl_116_evebit_negative_transition_flag(evebit: pd.Series) -> pd.Series:
    """1 on day EV/EBIT flips from positive to negative (EBIT goes negative)."""
    return ((evebit.shift(1) > 0) & (evebit < 0)).astype(float)


def vcl_117_evebit_compression_pct_126d(evebit: pd.Series) -> pd.Series:
    """Percent compression in positive EV/EBIT over 126 days."""
    p = _positive_mask(evebit)
    return _safe_div(p - p.shift(_TD_HALF), p.shift(_TD_HALF).replace(0, np.nan))


def vcl_118_evebit_below_5_fraction_252d(evebit: pd.Series) -> pd.Series:
    """Fraction of last 252 days where EV/EBIT was between 0 and 5."""
    flag = ((evebit > 0) & (evebit < 5)).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def vcl_119_evebitda_zscore_rolling_252d(evebitda: pd.Series) -> pd.Series:
    """Rolling 252-day z-score of positive EV/EBITDA."""
    p = _positive_mask(evebitda)
    return _zscore_rolling(p, _TD_YEAR)


def vcl_120_evebitda_252d_low_position(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA position within its 252-day range."""
    p  = _positive_mask(evebitda)
    hi = _rolling_max(p, _TD_YEAR)
    lo = _rolling_min(p, _TD_YEAR)
    return _safe_div(p - lo, hi - lo)


def vcl_121_evebitda_1260d_low_position(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA position within its 1260-day (5-year) range."""
    p  = _positive_mask(evebitda)
    hi = _rolling_max(p, 1260)
    lo = _rolling_min(p, 1260)
    return _safe_div(p - lo, hi - lo)


def vcl_122_evebitda_compression_pct_252d(evebitda: pd.Series) -> pd.Series:
    """Percent compression in positive EV/EBITDA over 252 days."""
    p = _positive_mask(evebitda)
    return _safe_div(p - p.shift(_TD_YEAR), p.shift(_TD_YEAR).replace(0, np.nan))


def vcl_123_evebitda_slope_63d(evebitda: pd.Series) -> pd.Series:
    """OLS slope of positive EV/EBITDA over trailing 63 days."""
    p = _positive_mask(evebitda)
    return _linslope(p, _TD_QTR)


def vcl_124_evebitda_negative_transition_flag(evebitda: pd.Series) -> pd.Series:
    """1 on day EV/EBITDA flips from positive to negative."""
    return ((evebitda.shift(1) > 0) & (evebitda < 0)).astype(float)


# --- Group K (125-138): marketcap and EV collapse ---

def vcl_125_marketcap_drawdown_from_252d_peak(marketcap: pd.Series) -> pd.Series:
    """Market cap drawdown from 252-day peak."""
    peak = _rolling_max(marketcap, _TD_YEAR)
    return _safe_div(marketcap - peak, peak)


def vcl_126_marketcap_drawdown_from_504d_peak(marketcap: pd.Series) -> pd.Series:
    """Market cap drawdown from 504-day peak."""
    peak = _rolling_max(marketcap, 504)
    return _safe_div(marketcap - peak, peak)


def vcl_127_marketcap_drawdown_from_expanding_peak(marketcap: pd.Series) -> pd.Series:
    """Market cap drawdown from all-history expanding peak."""
    peak = _expanding_max(marketcap)
    return _safe_div(marketcap - peak, peak)


def vcl_128_ev_drawdown_from_252d_peak(ev: pd.Series) -> pd.Series:
    """Enterprise value drawdown from 252-day peak."""
    p    = _positive_mask(ev)
    peak = _rolling_max(p, _TD_YEAR)
    return _safe_div(p - peak, peak)


def vcl_129_ev_drawdown_from_expanding_peak(ev: pd.Series) -> pd.Series:
    """Enterprise value drawdown from all-history expanding peak."""
    p    = _positive_mask(ev)
    peak = _expanding_max(p)
    return _safe_div(p - peak, peak)


def vcl_130_marketcap_below_ev_flag(marketcap: pd.Series, ev: pd.Series) -> pd.Series:
    """Binary: market cap < EV (company has net debt exceeding equity value)."""
    return (marketcap < ev).astype(float)


def vcl_131_ev_to_marketcap_ratio(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EV / market cap (leverage multiple; >1 means net debt)."""
    return _safe_div(_positive_mask(ev), _positive_mask(marketcap))


def vcl_132_marketcap_zscore_rolling_252d(marketcap: pd.Series) -> pd.Series:
    """Rolling 252-day z-score of market cap."""
    return _zscore_rolling(marketcap, _TD_YEAR)


def vcl_133_marketcap_compression_pct_252d(marketcap: pd.Series) -> pd.Series:
    """Percent change in market cap over 252 days."""
    return _safe_div(marketcap - marketcap.shift(_TD_YEAR),
                     marketcap.shift(_TD_YEAR).replace(0, np.nan))


def vcl_134_ev_compression_pct_252d(ev: pd.Series) -> pd.Series:
    """Percent change in EV over 252 days (positive EV only)."""
    p = _positive_mask(ev)
    return _safe_div(p - p.shift(_TD_YEAR), p.shift(_TD_YEAR).replace(0, np.nan))


def vcl_135_marketcap_at_expanding_min(marketcap: pd.Series) -> pd.Series:
    """1 if market cap is at its all-history expanding minimum."""
    lo = _expanding_min(marketcap)
    return (marketcap <= lo + _EPS).astype(float)


def vcl_136_marketcap_252d_low_position(marketcap: pd.Series) -> pd.Series:
    """Market cap position within its 252-day range."""
    hi = _rolling_max(marketcap, _TD_YEAR)
    lo = _rolling_min(marketcap, _TD_YEAR)
    return _safe_div(marketcap - lo, hi - lo)


def vcl_137_divyield_spike_flag(divyield: pd.Series) -> pd.Series:
    """Binary: dividend yield > 10% (price crash inflating yield — distress proxy)."""
    return (divyield > 0.10).astype(float)


def vcl_138_divyield_compression_252d(divyield: pd.Series) -> pd.Series:
    """Change in dividend yield over 252 days (rising yield = price collapse proxy)."""
    return divyield - divyield.shift(_TD_YEAR)


# --- Group L (139-150): Advanced cross-multiple and composite collapse ---

def vcl_139_evebitda_pe_both_at_252d_low(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """Binary: both EV/EBITDA and PE at their respective 252-day lows."""
    ev_lo = _rolling_min(_positive_mask(evebitda), _TD_YEAR)
    pe_lo = _rolling_min(_positive_mask(pe), _TD_YEAR)
    ev_at = (_positive_mask(evebitda) <= ev_lo + _EPS).fillna(False)
    pe_at = (_positive_mask(pe) <= pe_lo + _EPS).fillna(False)
    return (ev_at & pe_at).astype(float)


def vcl_140_all_five_multiples_compressing_flag(pe: pd.Series, pb: pd.Series, ps: pd.Series,
                                                  evebit: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Binary: all 5 multiples declining over trailing 21 days simultaneously."""
    pe_d   = (pe.diff(_TD_MON) < 0)
    pb_d   = (pb.diff(_TD_MON) < 0)
    ps_d   = (ps.diff(_TD_MON) < 0)
    evb_d  = (evebit.diff(_TD_MON) < 0)
    evbd_d = (evebitda.diff(_TD_MON) < 0)
    return (pe_d & pb_d & ps_d & evb_d & evbd_d).astype(float)


def vcl_141_composite_multiple_level_score(pe: pd.Series, pb: pd.Series,
                                            ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Composite level score: z-score sum of PE, PB, PS, EV/EBITDA (all 252d z-scores)."""
    def _zs(s):
        p = _positive_mask(s)
        return _zscore_rolling(p, _TD_YEAR).fillna(0)
    return _zs(pe) + _zs(pb) + _zs(ps) + _zs(evebitda)


def vcl_142_pe_pb_ps_simultaneous_new_low_252d(pe: pd.Series, pb: pd.Series,
                                                 ps: pd.Series) -> pd.Series:
    """Count of PE, PB, PS simultaneously at their 252-day lows (0/1/2/3)."""
    def _at_low(s):
        p  = _positive_mask(s)
        lo = _rolling_min(p, _TD_YEAR)
        return (p <= lo + _EPS).fillna(False).astype(float)
    return _at_low(pe) + _at_low(pb) + _at_low(ps)


def vcl_143_marketcap_ev_drawdown_spread(marketcap: pd.Series, ev: pd.Series) -> pd.Series:
    """Difference between mktcap 252d drawdown and EV 252d drawdown (equity vs total)."""
    mc_peak = _rolling_max(marketcap, _TD_YEAR)
    ev_p    = _positive_mask(ev)
    ev_peak = _rolling_max(ev_p, _TD_YEAR)
    dd_mc   = _safe_div(marketcap - mc_peak, mc_peak)
    dd_ev   = _safe_div(ev_p - ev_peak, ev_peak)
    return dd_mc - dd_ev


def vcl_144_collapse_intensity_pe_relative_to_pb(pe: pd.Series, pb: pd.Series) -> pd.Series:
    """Ratio of PE's 252-day drawdown to PB's 252-day drawdown (earnings vs book de-rating)."""
    def _dd252(s):
        p    = _positive_mask(s)
        peak = _rolling_max(p, _TD_YEAR)
        return _safe_div(p - peak, peak)
    return _safe_div(_dd252(pe), _dd252(pb))


def vcl_145_distress_score_weighted(pe: pd.Series, pb: pd.Series, ps: pd.Series,
                                     evebitda: pd.Series) -> pd.Series:
    """Weighted distress score: 0.3*PE<10 + 0.3*PB<1 + 0.2*PS<1 + 0.2*EVEBITDA<5."""
    s  = 0.3 * ((pe > 0) & (pe < 10)).astype(float)
    s += 0.3 * ((pb > 0) & (pb < 1.0)).astype(float)
    s += 0.2 * ((ps > 0) & (ps < 1.0)).astype(float)
    s += 0.2 * ((evebitda > 0) & (evebitda < 5)).astype(float)
    return s


def vcl_146_pe_pb_compression_concordance_252d(pe: pd.Series, pb: pd.Series) -> pd.Series:
    """Fraction of last 252 days both PE and PB declined together (joint compression)."""
    pe_dec = (pe.diff(1) < 0).astype(float)
    pb_dec = (pb.diff(1) < 0).astype(float)
    both   = pe_dec * pb_dec
    return _rolling_mean(both, _TD_YEAR)


def vcl_147_multi_window_pe_low_flags(pe: pd.Series) -> pd.Series:
    """Count of windows (21/63/252/504/1260d) where PE is at rolling minimum (0-5)."""
    p = _positive_mask(pe)
    windows = [_TD_MON, _TD_QTR, _TD_YEAR, 504, 1260]
    total = pd.Series(0.0, index=pe.index)
    for w in windows:
        lo   = _rolling_min(p, w)
        flag = (p <= lo + _EPS).fillna(False).astype(float)
        total = total + flag
    return total


def vcl_148_evebit_evebitda_spread(evebit: pd.Series, evebitda: pd.Series) -> pd.Series:
    """EV/EBIT minus EV/EBITDA (positive values) — DA amortization wedge."""
    return _positive_mask(evebit) - _positive_mask(evebitda)


def vcl_149_negative_multiples_fraction_504d(pe: pd.Series, evebit: pd.Series,
                                              evebitda: pd.Series) -> pd.Series:
    """Avg fraction of last 504 days where any of PE, EV/EBIT, EV/EBITDA was negative."""
    any_neg = ((pe < 0) | (evebit < 0) | (evebitda < 0)).astype(float)
    return _rolling_mean(any_neg, 504)


def vcl_150_ultimate_collapse_score(pe: pd.Series, pb: pd.Series, ps: pd.Series,
                                     evebit: pd.Series, evebitda: pd.Series,
                                     marketcap: pd.Series) -> pd.Series:
    """Ultimate collapse score: sum of 252d drawdowns for PE/PB/PS/EV/EBITDA + mktcap dd."""
    def _dd252(s, positive_only=True):
        p    = _positive_mask(s) if positive_only else s
        peak = _rolling_max(p, _TD_YEAR)
        return _safe_div(p - peak, peak).fillna(0)

    scores = (_dd252(pe) + _dd252(pb) + _dd252(ps) +
              _dd252(evebit) + _dd252(evebitda) +
              _dd252(marketcap, positive_only=False))
    return scores


# ── Feature functions 176-200 ─────────────────────────────────────────────────

# --- Group O (176-188): EV/EBIT, EV/EBITDA, EV extended analytics ---

def vcl_176_evebit_slope_63d(evebit: pd.Series) -> pd.Series:
    """OLS slope of positive EV/EBIT over 63 days (compression trend)."""
    p = _positive_mask(evebit)
    return _linslope(p, _TD_QTR)


def vcl_177_evebit_slope_252d(evebit: pd.Series) -> pd.Series:
    """OLS slope of positive EV/EBIT over 252 days (annual compression trend)."""
    p = _positive_mask(evebit)
    return _linslope(p, _TD_YEAR)


def vcl_178_evebit_1260d_low_position(evebit: pd.Series) -> pd.Series:
    """EV/EBIT position within its 1260-day (5-year) range."""
    p  = _positive_mask(evebit)
    hi = _rolling_max(p, 1260)
    lo = _rolling_min(p, 1260)
    return _safe_div(p - lo, hi - lo)


def vcl_179_evebitda_slope_252d(evebitda: pd.Series) -> pd.Series:
    """OLS slope of positive EV/EBITDA over 252 days."""
    p = _positive_mask(evebitda)
    return _linslope(p, _TD_YEAR)


def vcl_180_evebitda_median_deviation_252d(evebitda: pd.Series) -> pd.Series:
    """Deviation of positive EV/EBITDA from its 252-day rolling median."""
    p  = _positive_mask(evebitda)
    md = _rolling_median(p, _TD_YEAR)
    return p - md


def vcl_181_evebit_ath_drawdown_ratio(evebit: pd.Series) -> pd.Series:
    """Current positive EV/EBIT as fraction of its all-history maximum."""
    p = _positive_mask(evebit)
    return _safe_div(p, _expanding_max(p))


def vcl_182_evebitda_ath_drawdown_ratio(evebitda: pd.Series) -> pd.Series:
    """Current positive EV/EBITDA as fraction of its all-history maximum."""
    p = _positive_mask(evebitda)
    return _safe_div(p, _expanding_max(p))


def vcl_183_evebit_below_10_fraction_252d(evebit: pd.Series) -> pd.Series:
    """Fraction of last 252 days where positive EV/EBIT was below 10."""
    flag = ((evebit > 0) & (evebit < 10)).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def vcl_184_evebitda_below_3_fraction_252d(evebitda: pd.Series) -> pd.Series:
    """Fraction of last 252 days where positive EV/EBITDA was below 3."""
    flag = ((evebitda > 0) & (evebitda < 3)).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def vcl_185_evebit_ewm_deviation_21d(evebit: pd.Series) -> pd.Series:
    """Deviation of positive EV/EBIT from its 21-day EWM."""
    p = _positive_mask(evebit)
    return p - _ewm_mean(p, _TD_MON)


def vcl_186_evebitda_ewm_deviation_63d(evebitda: pd.Series) -> pd.Series:
    """Deviation of positive EV/EBITDA from its 63-day EWM."""
    p = _positive_mask(evebitda)
    return p - _ewm_mean(p, _TD_QTR)


def vcl_187_evebit_compression_pct_63d(evebit: pd.Series) -> pd.Series:
    """Percent change in positive EV/EBIT over 63 days."""
    p = _positive_mask(evebit)
    return _safe_div(p - p.shift(_TD_QTR), p.shift(_TD_QTR).replace(0, np.nan))


def vcl_188_evebitda_compression_pct_63d(evebitda: pd.Series) -> pd.Series:
    """Percent change in positive EV/EBITDA over 63 days."""
    p = _positive_mask(evebitda)
    return _safe_div(p - p.shift(_TD_QTR), p.shift(_TD_QTR).replace(0, np.nan))


# --- Group P (189-200): Advanced cross-multiple, divyield, rolling rank ---

def vcl_189_evebit_rolling_rank_pct_252d(evebit: pd.Series) -> pd.Series:
    """Percentile rank of positive EV/EBIT within trailing 252-day window."""
    p = _positive_mask(evebit)
    return _rolling_rank_pct(p, _TD_YEAR)


def vcl_190_marketcap_rolling_rank_pct_252d(marketcap: pd.Series) -> pd.Series:
    """Percentile rank of market cap within trailing 252-day window (low = collapsed)."""
    return _rolling_rank_pct(marketcap, _TD_YEAR)


def vcl_191_pe_slope_63d(pe: pd.Series) -> pd.Series:
    """OLS slope of positive PE over 63 days (quarterly compression trend)."""
    p = _positive_mask(pe)
    return _linslope(p, _TD_QTR)


def vcl_192_pb_slope_252d(pb: pd.Series) -> pd.Series:
    """OLS slope of positive PB over 252 days (annual de-rating speed)."""
    p = _positive_mask(pb)
    return _linslope(p, _TD_YEAR)


def vcl_193_ps_slope_21d(ps: pd.Series) -> pd.Series:
    """OLS slope of positive PS over 21 days (short-term PS compression)."""
    p = _positive_mask(ps)
    return _linslope(p, _TD_MON)


def vcl_194_divyield_below_2pct_flag(divyield: pd.Series) -> pd.Series:
    """Binary: divyield > 0 and divyield < 0.02 (low yield = not yet in distress)."""
    return ((divyield > 0) & (divyield < 0.02)).astype(float)


def vcl_195_divyield_above_5pct_flag(divyield: pd.Series) -> pd.Series:
    """Binary: divyield > 0.05 (elevated yield signalling price distress)."""
    return (divyield > 0.05).astype(float)


def vcl_196_pe_pb_ps_evebitda_all_at_252d_low(pe: pd.Series, pb: pd.Series,
                                                ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Count of PE/PB/PS/EV/EBITDA simultaneously at their 252-day lows (0-4)."""
    def _at_lo(s):
        p  = _positive_mask(s)
        lo = _rolling_min(p, _TD_YEAR)
        return (p <= lo + _EPS).fillna(False).astype(float)
    return _at_lo(pe) + _at_lo(pb) + _at_lo(ps) + _at_lo(evebitda)


def vcl_197_pb_ps_drawdown_product(pb: pd.Series, ps: pd.Series) -> pd.Series:
    """Product of 252-day PB and PS drawdowns (joint collapse severity)."""
    dd_pb = _safe_div(_positive_mask(pb) - _rolling_max(_positive_mask(pb), _TD_YEAR),
                      _rolling_max(_positive_mask(pb), _TD_YEAR))
    dd_ps = _safe_div(_positive_mask(ps) - _rolling_max(_positive_mask(ps), _TD_YEAR),
                      _rolling_max(_positive_mask(ps), _TD_YEAR))
    return dd_pb * dd_ps


def vcl_198_evebitda_pe_ratio(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """EV/EBITDA divided by PE (both positive) — acquisition vs earnings multiple ratio."""
    return _safe_div(_positive_mask(evebitda), _positive_mask(pe))


def vcl_199_marketcap_ev_ratio(marketcap: pd.Series, ev: pd.Series) -> pd.Series:
    """Market cap divided by positive EV (equity fraction of enterprise value)."""
    return _safe_div(_positive_mask(marketcap), _positive_mask(ev))


def vcl_200_six_multiple_collapse_score(pe: pd.Series, pb: pd.Series, ps: pd.Series,
                                         evebit: pd.Series, evebitda: pd.Series,
                                         marketcap: pd.Series) -> pd.Series:
    """Rolling-rank composite: avg 252d pct-rank of PE/PB/PS/EV-EBIT/EV-EBITDA/mktcap (low = collapse)."""
    def _rp(s):
        p = _positive_mask(s) if s is not marketcap else s
        return _rolling_rank_pct(p, _TD_YEAR).fillna(0.5)
    scores = (_rp(pe) + _rp(pb) + _rp(ps) + _rp(evebit) + _rp(evebitda) + _rp(marketcap))
    return scores / 6.0


# ── Registry ──────────────────────────────────────────────────────────────────

VALUATION_COLLAPSE_REGISTRY_076_150 = {
    "vcl_076_pe_252d_low_position": {"inputs": ["pe"], "func": vcl_076_pe_252d_low_position},
    "vcl_077_pe_504d_low_position": {"inputs": ["pe"], "func": vcl_077_pe_504d_low_position},
    "vcl_078_pe_zscore_rolling_252d": {"inputs": ["pe"], "func": vcl_078_pe_zscore_rolling_252d},
    "vcl_079_pe_zscore_rolling_504d": {"inputs": ["pe"], "func": vcl_079_pe_zscore_rolling_504d},
    "vcl_080_pe_median_deviation_252d": {"inputs": ["pe"], "func": vcl_080_pe_median_deviation_252d},
    "vcl_081_pe_below_median_flag_252d": {"inputs": ["pe"], "func": vcl_081_pe_below_median_flag_252d},
    "vcl_082_pe_ath_drawdown_to_current_ratio": {"inputs": ["pe"], "func": vcl_082_pe_ath_drawdown_to_current_ratio},
    "vcl_083_pe_range_pct_1260d": {"inputs": ["pe"], "func": vcl_083_pe_range_pct_1260d},
    "vcl_084_pe_negative_transition_flag": {"inputs": ["pe"], "func": vcl_084_pe_negative_transition_flag},
    "vcl_085_pe_negative_to_positive_flag": {"inputs": ["pe"], "func": vcl_085_pe_negative_to_positive_flag},
    "vcl_086_pe_below_5_fraction_504d": {"inputs": ["pe"], "func": vcl_086_pe_below_5_fraction_504d},
    "vcl_087_pe_ewm_deviation_21d": {"inputs": ["pe"], "func": vcl_087_pe_ewm_deviation_21d},
    "vcl_088_pe_slope_21d": {"inputs": ["pe"], "func": vcl_088_pe_slope_21d},
    "vcl_089_pb_252d_low_position": {"inputs": ["pb"], "func": vcl_089_pb_252d_low_position},
    "vcl_090_pb_zscore_rolling_252d": {"inputs": ["pb"], "func": vcl_090_pb_zscore_rolling_252d},
    "vcl_091_pb_zscore_rolling_1260d": {"inputs": ["pb"], "func": vcl_091_pb_zscore_rolling_1260d},
    "vcl_092_pb_ath_drawdown_ratio": {"inputs": ["pb"], "func": vcl_092_pb_ath_drawdown_ratio},
    "vcl_093_pb_median_deviation_504d": {"inputs": ["pb"], "func": vcl_093_pb_median_deviation_504d},
    "vcl_094_pb_slope_63d": {"inputs": ["pb"], "func": vcl_094_pb_slope_63d},
    "vcl_095_pb_below_0_5_fraction_252d": {"inputs": ["pb"], "func": vcl_095_pb_below_0_5_fraction_252d},
    "vcl_096_pb_compression_pct_63d": {"inputs": ["pb"], "func": vcl_096_pb_compression_pct_63d},
    "vcl_097_pb_at_252d_low_flag": {"inputs": ["pb"], "func": vcl_097_pb_at_252d_low_flag},
    "vcl_098_pb_compression_volatility_252d": {"inputs": ["pb"], "func": vcl_098_pb_compression_volatility_252d},
    "vcl_099_pb_ewm_vs_rolling_mean_252d": {"inputs": ["pb"], "func": vcl_099_pb_ewm_vs_rolling_mean_252d},
    "vcl_100_pb_1260d_low_position": {"inputs": ["pb"], "func": vcl_100_pb_1260d_low_position},
    "vcl_101_pb_rate_of_derating_126d": {"inputs": ["pb"], "func": vcl_101_pb_rate_of_derating_126d},
    "vcl_102_ps_252d_low_position": {"inputs": ["ps"], "func": vcl_102_ps_252d_low_position},
    "vcl_103_ps_zscore_rolling_252d": {"inputs": ["ps"], "func": vcl_103_ps_zscore_rolling_252d},
    "vcl_104_ps_ath_drawdown_ratio": {"inputs": ["ps"], "func": vcl_104_ps_ath_drawdown_ratio},
    "vcl_105_ps_slope_63d": {"inputs": ["ps"], "func": vcl_105_ps_slope_63d},
    "vcl_106_ps_slope_252d": {"inputs": ["ps"], "func": vcl_106_ps_slope_252d},
    "vcl_107_ps_median_deviation_252d": {"inputs": ["ps"], "func": vcl_107_ps_median_deviation_252d},
    "vcl_108_ps_compression_streak_63d_count": {"inputs": ["ps"], "func": vcl_108_ps_compression_streak_63d_count},
    "vcl_109_ps_below_0_5_fraction_252d": {"inputs": ["ps"], "func": vcl_109_ps_below_0_5_fraction_252d},
    "vcl_110_ps_ewm_deviation_63d": {"inputs": ["ps"], "func": vcl_110_ps_ewm_deviation_63d},
    "vcl_111_ps_1260d_low_position": {"inputs": ["ps"], "func": vcl_111_ps_1260d_low_position},
    "vcl_112_ps_rate_of_derating_126d": {"inputs": ["ps"], "func": vcl_112_ps_rate_of_derating_126d},
    "vcl_113_ps_negative_flag": {"inputs": ["ps"], "func": vcl_113_ps_negative_flag},
    "vcl_114_evebit_zscore_rolling_252d": {"inputs": ["evebit"], "func": vcl_114_evebit_zscore_rolling_252d},
    "vcl_115_evebit_252d_low_position": {"inputs": ["evebit"], "func": vcl_115_evebit_252d_low_position},
    "vcl_116_evebit_negative_transition_flag": {"inputs": ["evebit"], "func": vcl_116_evebit_negative_transition_flag},
    "vcl_117_evebit_compression_pct_126d": {"inputs": ["evebit"], "func": vcl_117_evebit_compression_pct_126d},
    "vcl_118_evebit_below_5_fraction_252d": {"inputs": ["evebit"], "func": vcl_118_evebit_below_5_fraction_252d},
    "vcl_119_evebitda_zscore_rolling_252d": {"inputs": ["evebitda"], "func": vcl_119_evebitda_zscore_rolling_252d},
    "vcl_120_evebitda_252d_low_position": {"inputs": ["evebitda"], "func": vcl_120_evebitda_252d_low_position},
    "vcl_121_evebitda_1260d_low_position": {"inputs": ["evebitda"], "func": vcl_121_evebitda_1260d_low_position},
    "vcl_122_evebitda_compression_pct_252d": {"inputs": ["evebitda"], "func": vcl_122_evebitda_compression_pct_252d},
    "vcl_123_evebitda_slope_63d": {"inputs": ["evebitda"], "func": vcl_123_evebitda_slope_63d},
    "vcl_124_evebitda_negative_transition_flag": {"inputs": ["evebitda"], "func": vcl_124_evebitda_negative_transition_flag},
    "vcl_125_marketcap_drawdown_from_252d_peak": {"inputs": ["marketcap"], "func": vcl_125_marketcap_drawdown_from_252d_peak},
    "vcl_126_marketcap_drawdown_from_504d_peak": {"inputs": ["marketcap"], "func": vcl_126_marketcap_drawdown_from_504d_peak},
    "vcl_127_marketcap_drawdown_from_expanding_peak": {"inputs": ["marketcap"], "func": vcl_127_marketcap_drawdown_from_expanding_peak},
    "vcl_128_ev_drawdown_from_252d_peak": {"inputs": ["ev"], "func": vcl_128_ev_drawdown_from_252d_peak},
    "vcl_129_ev_drawdown_from_expanding_peak": {"inputs": ["ev"], "func": vcl_129_ev_drawdown_from_expanding_peak},
    "vcl_130_marketcap_below_ev_flag": {"inputs": ["marketcap", "ev"], "func": vcl_130_marketcap_below_ev_flag},
    "vcl_131_ev_to_marketcap_ratio": {"inputs": ["ev", "marketcap"], "func": vcl_131_ev_to_marketcap_ratio},
    "vcl_132_marketcap_zscore_rolling_252d": {"inputs": ["marketcap"], "func": vcl_132_marketcap_zscore_rolling_252d},
    "vcl_133_marketcap_compression_pct_252d": {"inputs": ["marketcap"], "func": vcl_133_marketcap_compression_pct_252d},
    "vcl_134_ev_compression_pct_252d": {"inputs": ["ev"], "func": vcl_134_ev_compression_pct_252d},
    "vcl_135_marketcap_at_expanding_min": {"inputs": ["marketcap"], "func": vcl_135_marketcap_at_expanding_min},
    "vcl_136_marketcap_252d_low_position": {"inputs": ["marketcap"], "func": vcl_136_marketcap_252d_low_position},
    "vcl_137_divyield_spike_flag": {"inputs": ["divyield"], "func": vcl_137_divyield_spike_flag},
    "vcl_138_divyield_compression_252d": {"inputs": ["divyield"], "func": vcl_138_divyield_compression_252d},
    "vcl_139_evebitda_pe_both_at_252d_low": {"inputs": ["evebitda", "pe"], "func": vcl_139_evebitda_pe_both_at_252d_low},
    "vcl_140_all_five_multiples_compressing_flag": {"inputs": ["pe", "pb", "ps", "evebit", "evebitda"], "func": vcl_140_all_five_multiples_compressing_flag},
    "vcl_141_composite_multiple_level_score": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_141_composite_multiple_level_score},
    "vcl_142_pe_pb_ps_simultaneous_new_low_252d": {"inputs": ["pe", "pb", "ps"], "func": vcl_142_pe_pb_ps_simultaneous_new_low_252d},
    "vcl_143_marketcap_ev_drawdown_spread": {"inputs": ["marketcap", "ev"], "func": vcl_143_marketcap_ev_drawdown_spread},
    "vcl_144_collapse_intensity_pe_relative_to_pb": {"inputs": ["pe", "pb"], "func": vcl_144_collapse_intensity_pe_relative_to_pb},
    "vcl_145_distress_score_weighted": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_145_distress_score_weighted},
    "vcl_146_pe_pb_compression_concordance_252d": {"inputs": ["pe", "pb"], "func": vcl_146_pe_pb_compression_concordance_252d},
    "vcl_147_multi_window_pe_low_flags": {"inputs": ["pe"], "func": vcl_147_multi_window_pe_low_flags},
    "vcl_148_evebit_evebitda_spread": {"inputs": ["evebit", "evebitda"], "func": vcl_148_evebit_evebitda_spread},
    "vcl_149_negative_multiples_fraction_504d": {"inputs": ["pe", "evebit", "evebitda"], "func": vcl_149_negative_multiples_fraction_504d},
    "vcl_150_ultimate_collapse_score": {"inputs": ["pe", "pb", "ps", "evebit", "evebitda", "marketcap"], "func": vcl_150_ultimate_collapse_score},
    "vcl_176_evebit_slope_63d": {"inputs": ["evebit"], "func": vcl_176_evebit_slope_63d},
    "vcl_177_evebit_slope_252d": {"inputs": ["evebit"], "func": vcl_177_evebit_slope_252d},
    "vcl_178_evebit_1260d_low_position": {"inputs": ["evebit"], "func": vcl_178_evebit_1260d_low_position},
    "vcl_179_evebitda_slope_252d": {"inputs": ["evebitda"], "func": vcl_179_evebitda_slope_252d},
    "vcl_180_evebitda_median_deviation_252d": {"inputs": ["evebitda"], "func": vcl_180_evebitda_median_deviation_252d},
    "vcl_181_evebit_ath_drawdown_ratio": {"inputs": ["evebit"], "func": vcl_181_evebit_ath_drawdown_ratio},
    "vcl_182_evebitda_ath_drawdown_ratio": {"inputs": ["evebitda"], "func": vcl_182_evebitda_ath_drawdown_ratio},
    "vcl_183_evebit_below_10_fraction_252d": {"inputs": ["evebit"], "func": vcl_183_evebit_below_10_fraction_252d},
    "vcl_184_evebitda_below_3_fraction_252d": {"inputs": ["evebitda"], "func": vcl_184_evebitda_below_3_fraction_252d},
    "vcl_185_evebit_ewm_deviation_21d": {"inputs": ["evebit"], "func": vcl_185_evebit_ewm_deviation_21d},
    "vcl_186_evebitda_ewm_deviation_63d": {"inputs": ["evebitda"], "func": vcl_186_evebitda_ewm_deviation_63d},
    "vcl_187_evebit_compression_pct_63d": {"inputs": ["evebit"], "func": vcl_187_evebit_compression_pct_63d},
    "vcl_188_evebitda_compression_pct_63d": {"inputs": ["evebitda"], "func": vcl_188_evebitda_compression_pct_63d},
    "vcl_189_evebit_rolling_rank_pct_252d": {"inputs": ["evebit"], "func": vcl_189_evebit_rolling_rank_pct_252d},
    "vcl_190_marketcap_rolling_rank_pct_252d": {"inputs": ["marketcap"], "func": vcl_190_marketcap_rolling_rank_pct_252d},
    "vcl_191_pe_slope_63d": {"inputs": ["pe"], "func": vcl_191_pe_slope_63d},
    "vcl_192_pb_slope_252d": {"inputs": ["pb"], "func": vcl_192_pb_slope_252d},
    "vcl_193_ps_slope_21d": {"inputs": ["ps"], "func": vcl_193_ps_slope_21d},
    "vcl_194_divyield_below_2pct_flag": {"inputs": ["divyield"], "func": vcl_194_divyield_below_2pct_flag},
    "vcl_195_divyield_above_5pct_flag": {"inputs": ["divyield"], "func": vcl_195_divyield_above_5pct_flag},
    "vcl_196_pe_pb_ps_evebitda_all_at_252d_low": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_196_pe_pb_ps_evebitda_all_at_252d_low},
    "vcl_197_pb_ps_drawdown_product": {"inputs": ["pb", "ps"], "func": vcl_197_pb_ps_drawdown_product},
    "vcl_198_evebitda_pe_ratio": {"inputs": ["evebitda", "pe"], "func": vcl_198_evebitda_pe_ratio},
    "vcl_199_marketcap_ev_ratio": {"inputs": ["marketcap", "ev"], "func": vcl_199_marketcap_ev_ratio},
    "vcl_200_six_multiple_collapse_score": {"inputs": ["pe", "pb", "ps", "evebit", "evebitda", "marketcap"], "func": vcl_200_six_multiple_collapse_score},
}
