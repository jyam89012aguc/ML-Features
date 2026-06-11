"""
79_ev_distortion — Base Features 076-200
Domain: enterprise-value vs equity-value distortion — extended feature set covering
        EV-based valuation spreads, ratio momentum, multi-window trend analysis,
        cross-multiple signals, and distress threshold analytics.

Inputs: daily-frequency Sharadar DAILY/METRICS valuation fields only.
        Canonical field names (lowercase): marketcap, ev, pe, pb, ps, evebit, evebitda, divyield.
        NO raw price/volume. NO quarterly forward-fill alignment helper needed — these are
        native daily-frequency series.

All feature functions are strictly backward-looking: no negative shifts, no forward fills
from future observations, no .iloc[i+n] look-ahead.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero/NaN denominator with NaN."""
    return num / den.replace(0, np.nan)


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


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods (scalar per window)."""
    def _slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi   = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        xv_m = x.mean()
        num  = ((xi - xi_m) * (x - xv_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        return np.nan if den == 0 else num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=False)


def _net_debt_wedge(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    return ev - marketcap


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): EV/marketcap ratio momentum and trend ---

def evd_076_ev_to_mktcap_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day first difference of EV/marketcap ratio (weekly velocity of distortion)."""
    ratio = _safe_div(ev, marketcap)
    return ratio.diff(5)


def evd_077_ev_to_mktcap_21d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day first difference of EV/marketcap ratio (monthly velocity)."""
    ratio = _safe_div(ev, marketcap)
    return ratio.diff(_TD_MON)


def evd_078_ev_to_mktcap_63d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day first difference of EV/marketcap ratio (quarterly velocity)."""
    ratio = _safe_div(ev, marketcap)
    return ratio.diff(_TD_QTR)


def evd_079_ev_to_mktcap_252d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day first difference of EV/marketcap ratio (annual velocity)."""
    ratio = _safe_div(ev, marketcap)
    return ratio.diff(_TD_YEAR)


def evd_080_ev_to_mktcap_5d_pct_change(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day percent change in EV/marketcap ratio."""
    ratio = _safe_div(ev, marketcap)
    return ratio.pct_change(5)


def evd_081_ev_to_mktcap_21d_pct_change(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day percent change in EV/marketcap ratio."""
    ratio = _safe_div(ev, marketcap)
    return ratio.pct_change(_TD_MON)


def evd_082_ev_to_mktcap_63d_pct_change(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day percent change in EV/marketcap ratio."""
    ratio = _safe_div(ev, marketcap)
    return ratio.pct_change(_TD_QTR)


def evd_083_ev_to_mktcap_21d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """OLS slope of EV/marketcap ratio over 21 days (linear trend direction)."""
    ratio = _safe_div(ev, marketcap)
    return _linslope(ratio, _TD_MON)


def evd_084_ev_to_mktcap_63d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """OLS slope of EV/marketcap ratio over 63 days."""
    ratio = _safe_div(ev, marketcap)
    return _linslope(ratio, _TD_QTR)


def evd_085_ev_to_mktcap_126d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """OLS slope of EV/marketcap ratio over 126 days."""
    ratio = _safe_div(ev, marketcap)
    return _linslope(ratio, _TD_HALF)


def evd_086_ev_to_mktcap_ratio_acceleration_21d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Second-difference of EV/marketcap ratio over 21 days (acceleration of distortion)."""
    ratio = _safe_div(ev, marketcap)
    return ratio.diff(5).diff(5)


def evd_087_wedge_to_mktcap_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of wedge/marketcap ratio (weekly leverage drift)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return ratio.diff(5)


def evd_088_wedge_to_mktcap_21d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day diff of wedge/marketcap ratio."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return ratio.diff(_TD_MON)


def evd_089_wedge_to_mktcap_63d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day diff of wedge/marketcap ratio."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return ratio.diff(_TD_QTR)


def evd_090_wedge_to_mktcap_21d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """OLS slope of wedge/marketcap ratio over 21 days."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return _linslope(ratio, _TD_MON)


# --- Group G (091-105): EV-based multiple trends and spreads vs equity ---

def evd_091_evebitda_21d_diff(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """21-day diff of EV/EBITDA multiple (enterprise multiple change)."""
    return evebitda.diff(_TD_MON)


def evd_092_evebitda_63d_diff(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """63-day diff of EV/EBITDA multiple."""
    return evebitda.diff(_TD_QTR)


def evd_093_evebitda_252d_diff(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """252-day diff of EV/EBITDA multiple."""
    return evebitda.diff(_TD_YEAR)


def evd_094_evebit_21d_diff(evebit: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day diff of EV/EBIT multiple."""
    return evebit.diff(_TD_MON)


def evd_095_evebit_63d_diff(evebit: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day diff of EV/EBIT multiple."""
    return evebit.diff(_TD_QTR)


def evd_096_evebitda_252d_max(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """252-day rolling max of EV/EBITDA (peak enterprise multiple in past year)."""
    return _rolling_max(evebitda, _TD_YEAR)


def evd_097_evebitda_252d_min(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """252-day rolling min of EV/EBITDA (trough enterprise multiple in past year)."""
    return _rolling_min(evebitda, _TD_YEAR)


def evd_098_evebitda_252d_range(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """252-day range of EV/EBITDA (max - min; compression bandwidth)."""
    return _rolling_max(evebitda, _TD_YEAR) - _rolling_min(evebitda, _TD_YEAR)


def evd_099_evebitda_position_in_252d_range(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA position within 252-day range (0=trough, 1=peak)."""
    hi  = _rolling_max(evebitda, _TD_YEAR)
    lo  = _rolling_min(evebitda, _TD_YEAR)
    return _safe_div(evebitda - lo, hi - lo)


def evd_100_evebit_position_in_252d_range(evebit: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EV/EBIT position within 252-day range."""
    hi  = _rolling_max(evebit, _TD_YEAR)
    lo  = _rolling_min(evebit, _TD_YEAR)
    return _safe_div(evebit - lo, hi - lo)


def evd_101_evebitda_pct_rank_1260d(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """5-year percentile rank of EV/EBITDA multiple."""
    return _rolling_rank_pct(evebitda, 1260)


def evd_102_evebit_pct_rank_1260d(evebit: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-year percentile rank of EV/EBIT multiple."""
    return _rolling_rank_pct(evebit, 1260)


def evd_103_evebitda_vs_21d_sma(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA deviation from its own 21-day SMA."""
    sma = _rolling_mean(evebitda, _TD_MON)
    return _safe_div(evebitda - sma, sma.replace(0, np.nan).abs())


def evd_104_evebitda_vs_252d_sma(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA deviation from its own 252-day SMA."""
    sma = _rolling_mean(evebitda, _TD_YEAR)
    return _safe_div(evebitda - sma, sma.replace(0, np.nan).abs())


def evd_105_evebit_21d_slope(evebit: pd.Series, marketcap: pd.Series) -> pd.Series:
    """OLS slope of EV/EBIT multiple over 21 days."""
    return _linslope(evebit, _TD_MON)


# --- Group H (106-120): Cross-metric and multi-ratio distortion signals ---

def evd_106_ev_to_mktcap_times_evebitda(ev: pd.Series, marketcap: pd.Series, evebitda: pd.Series) -> pd.Series:
    """EV/mktcap ratio multiplied by EV/EBITDA (compounded distortion index)."""
    ratio = _safe_div(ev, marketcap)
    return ratio * evebitda


def evd_107_wedge_ratio_times_evebitda(ev: pd.Series, marketcap: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Wedge/mktcap ratio multiplied by EV/EBITDA (leverage-amplified enterprise multiple)."""
    wedge_r = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return wedge_r * evebitda


def evd_108_ev_to_mktcap_ratio_vs_pe(ev: pd.Series, marketcap: pd.Series, pe: pd.Series) -> pd.Series:
    """EV/mktcap ratio times P/E (EV-inflated equity multiple compound)."""
    return _safe_div(ev, marketcap) * pe


def evd_109_evebitda_minus_pe_zscore_252d(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """252-day z-score of (EV/EBITDA - P/E) spread."""
    diff = evebitda - pe
    return _zscore_rolling(diff, _TD_YEAR)


def evd_110_evebitda_minus_pe_pct_rank_1260d(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """5-year pct-rank of EV/EBITDA minus P/E spread."""
    diff = evebitda - pe
    return _rolling_rank_pct(diff, 1260)


def evd_111_evebit_minus_pe_zscore_252d(evebit: pd.Series, pe: pd.Series) -> pd.Series:
    """252-day z-score of (EV/EBIT - P/E) spread."""
    diff = evebit - pe
    return _zscore_rolling(diff, _TD_YEAR)


def evd_112_evebitda_to_evebit_ratio(evebit: pd.Series, evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA divided by EV/EBIT: DA-implied spread (capex/amort burden proxy)."""
    return _safe_div(evebitda, evebit)


def evd_113_evebitda_to_evebit_zscore_252d(evebit: pd.Series, evebitda: pd.Series) -> pd.Series:
    """252-day z-score of EV/EBITDA-to-EV/EBIT ratio."""
    ratio = _safe_div(evebitda, evebit)
    return _zscore_rolling(ratio, _TD_YEAR)


def evd_114_pe_to_ev_ratio_combined(ev: pd.Series, marketcap: pd.Series, pe: pd.Series) -> pd.Series:
    """P/E divided by (EV/mktcap): equity earnings yield adjusted for leverage."""
    return _safe_div(pe, _safe_div(ev, marketcap))


def evd_115_ev_to_mktcap_ratio_times_pb(ev: pd.Series, marketcap: pd.Series, pb: pd.Series) -> pd.Series:
    """EV/mktcap multiplied by P/B: leverage-amplified book multiple."""
    return _safe_div(ev, marketcap) * pb


def evd_116_ev_to_mktcap_ratio_times_ps(ev: pd.Series, marketcap: pd.Series, ps: pd.Series) -> pd.Series:
    """EV/mktcap multiplied by P/S: leverage-amplified sales multiple."""
    return _safe_div(ev, marketcap) * ps


def evd_117_evebitda_expanding_zscore(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Expanding z-score of EV/EBITDA (how extreme vs all-time history)."""
    m  = evebitda.expanding(min_periods=5).mean()
    sd = evebitda.expanding(min_periods=5).std()
    return _safe_div(evebitda - m, sd)


def evd_118_evebit_expanding_zscore(evebit: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Expanding z-score of EV/EBIT."""
    m  = evebit.expanding(min_periods=5).mean()
    sd = evebit.expanding(min_periods=5).std()
    return _safe_div(evebit - m, sd)


def evd_119_mktcap_to_ev_below_threshold_pct_rank_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day pct-rank of marketcap/ev — extreme low rank signals option-like equity."""
    ratio = _safe_div(marketcap, ev)
    return _rolling_rank_pct(ratio, _TD_YEAR)


def evd_120_mktcap_to_ev_below_20pct_flag(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Binary flag: equity/EV below 20% (equity is less than 1/5 of enterprise)."""
    ratio = _safe_div(marketcap, ev)
    return (ratio < 0.2).astype(float)


# --- Group I (121-135): Window-variant and EWM cross-ratio signals ---

def evd_121_ev_to_mktcap_ewm_diff_21_63(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EWM(21) minus EWM(63) of EV/mktcap ratio (fast-slow trend gap)."""
    ratio = _safe_div(ev, marketcap)
    return _ewm_mean(ratio, _TD_MON) - _ewm_mean(ratio, _TD_QTR)


def evd_122_ev_to_mktcap_ewm_diff_63_252(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EWM(63) minus EWM(252) of EV/mktcap ratio (medium-slow trend gap)."""
    ratio = _safe_div(ev, marketcap)
    return _ewm_mean(ratio, _TD_QTR) - _ewm_mean(ratio, _TD_YEAR)


def evd_123_wedge_ewm_diff_21_63(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EWM(21) minus EWM(63) of wedge/mktcap ratio."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return _ewm_mean(ratio, _TD_MON) - _ewm_mean(ratio, _TD_QTR)


def evd_124_evebitda_ewm_diff_21_252(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """EWM(21) minus EWM(252) of EV/EBITDA (fast-annual enterprise multiple trend)."""
    return _ewm_mean(evebitda, _TD_MON) - _ewm_mean(evebitda, _TD_YEAR)


def evd_125_ev_to_mktcap_504d_avg(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """504-day rolling mean of EV/marketcap ratio (2-year average distortion)."""
    ratio = _safe_div(ev, marketcap)
    return _rolling_mean(ratio, 504)


def evd_126_ev_to_mktcap_756d_avg(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """756-day rolling mean of EV/marketcap ratio (3-year average distortion)."""
    ratio = _safe_div(ev, marketcap)
    return _rolling_mean(ratio, 756)


def evd_127_ev_to_mktcap_1260d_avg(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """1260-day rolling mean of EV/marketcap ratio (5-year average distortion)."""
    ratio = _safe_div(ev, marketcap)
    return _rolling_mean(ratio, 1260)


def evd_128_ev_to_mktcap_vs_504d_sma(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EV/mktcap deviation from 504-day SMA."""
    ratio = _safe_div(ev, marketcap)
    sma   = _rolling_mean(ratio, 504)
    return _safe_div(ratio - sma, sma)


def evd_129_ev_to_mktcap_vs_1260d_sma(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EV/mktcap deviation from 1260-day SMA."""
    ratio = _safe_div(ev, marketcap)
    sma   = _rolling_mean(ratio, 1260)
    return _safe_div(ratio - sma, sma)


def evd_130_ev_to_mktcap_median_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day rolling median of EV/mktcap ratio (robust central tendency)."""
    ratio = _safe_div(ev, marketcap)
    return _rolling_median(ratio, _TD_QTR)


def evd_131_ev_to_mktcap_median_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day rolling median of EV/mktcap ratio."""
    ratio = _safe_div(ev, marketcap)
    return _rolling_median(ratio, _TD_YEAR)


def evd_132_ev_to_mktcap_q95_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day 95th percentile of EV/mktcap ratio (tail distortion level)."""
    ratio = _safe_div(ev, marketcap)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.95)


def evd_133_ev_to_mktcap_q05_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day 5th percentile of EV/mktcap ratio (least distorted tail)."""
    ratio = _safe_div(ev, marketcap)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.05)


def evd_134_wedge_to_mktcap_q95_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day 95th percentile of wedge/mktcap (peak leverage tail)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.95)


def evd_135_wedge_to_mktcap_skew_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day rolling skewness of wedge/mktcap ratio (asymmetric leverage risk)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).skew()


# --- Group J (136-150): Composite, threshold, and stability signals ---

def evd_136_ev_to_mktcap_ratio_expanding_max(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Expanding maximum of EV/mktcap ratio (all-time peak distortion)."""
    ratio = _safe_div(ev, marketcap)
    return ratio.expanding(min_periods=1).max()


def evd_137_ev_to_mktcap_ratio_vs_expanding_max(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Current EV/mktcap vs its all-time max (fraction of worst-ever distortion)."""
    ratio = _safe_div(ev, marketcap)
    exp_max = ratio.expanding(min_periods=1).max()
    return _safe_div(ratio, exp_max)


def evd_138_mktcap_to_ev_expanding_zscore(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Expanding z-score of equity/EV share (how anomalously thin the equity slice is)."""
    ratio = _safe_div(marketcap, ev)
    m  = ratio.expanding(min_periods=5).mean()
    sd = ratio.expanding(min_periods=5).std()
    return _safe_div(ratio - m, sd)


def evd_139_ev_to_mktcap_above_2x_fraction_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Fraction of past 252 days where EV/mktcap > 2 (persistent double-debt distortion)."""
    ratio = _safe_div(ev, marketcap)
    flag  = (ratio > 2.0).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def evd_140_ev_to_mktcap_above_3x_fraction_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Fraction of past 252 days where EV/mktcap > 3 (extreme leverage persistence)."""
    ratio = _safe_div(ev, marketcap)
    flag  = (ratio > 3.0).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def evd_141_ev_to_mktcap_above_5x_fraction_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Fraction of past 252 days where EV/mktcap > 5 (near-zero equity fraction)."""
    ratio = _safe_div(ev, marketcap)
    flag  = (ratio > 5.0).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def evd_142_ev_to_mktcap_trend_up_fraction_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Fraction of past 63 days where EV/mktcap ratio rose day-over-day."""
    ratio = _safe_div(ev, marketcap)
    rising = (ratio.diff(1) > 0).astype(float)
    return _rolling_mean(rising, _TD_QTR)


def evd_143_ev_to_mktcap_trend_up_fraction_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Fraction of past 252 days where EV/mktcap ratio rose day-over-day."""
    ratio = _safe_div(ev, marketcap)
    rising = (ratio.diff(1) > 0).astype(float)
    return _rolling_mean(rising, _TD_YEAR)


def evd_144_divyield_times_ev_to_mktcap(ev: pd.Series, marketcap: pd.Series, divyield: pd.Series) -> pd.Series:
    """Dividend yield scaled by EV/mktcap (yield in context of leverage distortion)."""
    return divyield * _safe_div(ev, marketcap)


def evd_145_pb_times_ev_to_mktcap(ev: pd.Series, marketcap: pd.Series, pb: pd.Series) -> pd.Series:
    """P/B multiplied by EV/mktcap (leverage-adjusted book multiple)."""
    return pb * _safe_div(ev, marketcap)


def evd_146_ps_times_ev_to_mktcap(ev: pd.Series, marketcap: pd.Series, ps: pd.Series) -> pd.Series:
    """P/S multiplied by EV/mktcap (leverage-adjusted sales multiple)."""
    return ps * _safe_div(ev, marketcap)


def evd_147_ev_to_mktcap_std_21d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day rolling std of EV/mktcap ratio (short-term distortion volatility)."""
    ratio = _safe_div(ev, marketcap)
    return _rolling_std(ratio, _TD_MON)


def evd_148_ev_to_mktcap_std_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day rolling std of EV/mktcap ratio."""
    ratio = _safe_div(ev, marketcap)
    return _rolling_std(ratio, _TD_QTR)


def evd_149_ev_to_mktcap_cv_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day coefficient of variation of EV/mktcap (std/mean; instability measure)."""
    ratio = _safe_div(ev, marketcap)
    return _safe_div(_rolling_std(ratio, _TD_YEAR), _rolling_mean(ratio, _TD_YEAR).abs())


def evd_150_composite_ev_distortion_index(ev: pd.Series, marketcap: pd.Series, evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """Composite distortion index: equal-weight avg of z-scores of (ev/mktcap),
    (wedge/mktcap), and (evebitda/pe ratio) over 252 days."""
    z1 = _zscore_rolling(_safe_div(ev, marketcap), _TD_YEAR)
    z2 = _zscore_rolling(_safe_div(ev - marketcap, marketcap), _TD_YEAR)
    z3 = _zscore_rolling(_safe_div(evebitda, pe), _TD_YEAR)
    return (z1 + z2 + z3) / 3.0


# --- Group K (176-200): EWM extensions, slopes, cross-ratio stats, threshold trends ---

def evd_176_evebitda_ewm_21(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """21-day EWM of EV/EBITDA multiple (fast exponential trend of enterprise multiple)."""
    return _ewm_mean(evebitda, _TD_MON)


def evd_177_evebitda_ewm_63(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """63-day EWM of EV/EBITDA multiple (quarterly exponential trend)."""
    return _ewm_mean(evebitda, _TD_QTR)


def evd_178_evebit_ewm_21(evebit: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day EWM of EV/EBIT multiple."""
    return _ewm_mean(evebit, _TD_MON)


def evd_179_evebit_ewm_63(evebit: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day EWM of EV/EBIT multiple."""
    return _ewm_mean(evebit, _TD_QTR)


def evd_180_evebitda_63d_slope(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """OLS slope of EV/EBITDA multiple over 63 days (quarterly linear trend)."""
    return _linslope(evebitda, _TD_QTR)


def evd_181_evebit_63d_slope(evebit: pd.Series, marketcap: pd.Series) -> pd.Series:
    """OLS slope of EV/EBIT multiple over 63 days."""
    return _linslope(evebit, _TD_QTR)


def evd_182_evebitda_pct_rank_252d(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """252-day percentile rank of EV/EBITDA multiple (annual rank of enterprise multiple)."""
    return _rolling_rank_pct(evebitda, _TD_YEAR)


def evd_183_evebit_pct_rank_252d(evebit: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day percentile rank of EV/EBIT multiple."""
    return _rolling_rank_pct(evebit, _TD_YEAR)


def evd_184_ev_to_mktcap_126d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """OLS slope of EV/mktcap ratio over 126 days (semi-annual linear distortion trend)."""
    ratio = _safe_div(ev, marketcap)
    return _linslope(ratio, _TD_HALF)


def evd_185_wedge_to_mktcap_63d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """OLS slope of wedge/mktcap ratio over 63 days (quarterly leverage trend)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return _linslope(ratio, _TD_QTR)


def evd_186_wedge_to_mktcap_126d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """OLS slope of wedge/mktcap ratio over 126 days (semi-annual leverage trend)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return _linslope(ratio, _TD_HALF)


def evd_187_evebitda_to_pe_63d_avg(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """63-day rolling mean of EV/EBITDA-to-P/E ratio (quarterly multiple-gap average)."""
    ratio = _safe_div(evebitda, pe)
    return _rolling_mean(ratio, _TD_QTR)


def evd_188_evebitda_to_pe_126d_avg(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """126-day rolling mean of EV/EBITDA-to-P/E ratio (semi-annual multiple-gap average)."""
    ratio = _safe_div(evebitda, pe)
    return _rolling_mean(ratio, _TD_HALF)


def evd_189_evebit_to_pe_63d_avg(evebit: pd.Series, pe: pd.Series) -> pd.Series:
    """63-day rolling mean of EV/EBIT-to-P/E ratio (quarterly EBIT-based multiple gap)."""
    ratio = _safe_div(evebit, pe)
    return _rolling_mean(ratio, _TD_QTR)


def evd_190_evebitda_to_pe_expanding_zscore(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """Expanding z-score of EV/EBITDA-to-P/E ratio (all-history multiple-gap extremity)."""
    ratio = _safe_div(evebitda, pe)
    m  = ratio.expanding(min_periods=5).mean()
    sd = ratio.expanding(min_periods=5).std()
    return _safe_div(ratio - m, sd)


def evd_191_divyield_zscore_252d(ev: pd.Series, marketcap: pd.Series, divyield: pd.Series) -> pd.Series:
    """252-day z-score of dividend yield (yield extremity in EV-distortion context)."""
    return _zscore_rolling(divyield, _TD_YEAR)


def evd_192_divyield_times_wedge_ratio(ev: pd.Series, marketcap: pd.Series, divyield: pd.Series) -> pd.Series:
    """Dividend yield multiplied by wedge/mktcap (yield stressed by leverage ratio)."""
    wedge_r = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return divyield * wedge_r


def evd_193_pb_to_ev_to_mktcap_ratio(ev: pd.Series, marketcap: pd.Series, pb: pd.Series) -> pd.Series:
    """P/B divided by EV/mktcap (book multiple adjusted for leverage distortion)."""
    return _safe_div(pb, _safe_div(ev, marketcap))


def evd_194_ps_to_ev_to_mktcap_ratio(ev: pd.Series, marketcap: pd.Series, ps: pd.Series) -> pd.Series:
    """P/S divided by EV/mktcap (sales multiple adjusted for leverage distortion)."""
    return _safe_div(ps, _safe_div(ev, marketcap))


def evd_195_ev_to_mktcap_trend_dn_fraction_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Fraction of past 63 days where EV/mktcap ratio fell day-over-day."""
    ratio = _safe_div(ev, marketcap)
    falling = (ratio.diff(1) < 0).astype(float)
    return _rolling_mean(falling, _TD_QTR)


def evd_196_ev_to_mktcap_trend_dn_fraction_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Fraction of past 252 days where EV/mktcap ratio fell day-over-day."""
    ratio = _safe_div(ev, marketcap)
    falling = (ratio.diff(1) < 0).astype(float)
    return _rolling_mean(falling, _TD_YEAR)


def evd_197_evebitda_to_evebit_252d_avg(evebit: pd.Series, evebitda: pd.Series) -> pd.Series:
    """252-day rolling mean of EV/EBITDA-to-EV/EBIT ratio (annual DA-burden average)."""
    ratio = _safe_div(evebitda, evebit)
    return _rolling_mean(ratio, _TD_YEAR)


def evd_198_ev_to_mktcap_ratio_ewm_cross_21_252(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Binary flag: EWM(21) > EWM(252) of EV/mktcap (fast-trend above long-trend)."""
    ratio = _safe_div(ev, marketcap)
    return (_ewm_mean(ratio, _TD_MON) > _ewm_mean(ratio, _TD_YEAR)).astype(float)


def evd_199_wedge_to_mktcap_pct_rank_1260d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-year percentile rank of wedge/mktcap ratio (long-term leverage extremity)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return _rolling_rank_pct(ratio, 1260)


def evd_200_equity_share_trend_down_fraction_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Fraction of past 252 days where equity/EV share fell day-over-day (persistent erosion)."""
    ratio   = _safe_div(marketcap, ev)
    falling = (ratio.diff(1) < 0).astype(float)
    return _rolling_mean(falling, _TD_YEAR)


# ── Registry ──────────────────────────────────────────────────────────────────

EV_DISTORTION_REGISTRY_076_150 = {
    "evd_076_ev_to_mktcap_5d_diff":                     {"inputs": ["ev", "marketcap"],             "func": evd_076_ev_to_mktcap_5d_diff},
    "evd_077_ev_to_mktcap_21d_diff":                    {"inputs": ["ev", "marketcap"],             "func": evd_077_ev_to_mktcap_21d_diff},
    "evd_078_ev_to_mktcap_63d_diff":                    {"inputs": ["ev", "marketcap"],             "func": evd_078_ev_to_mktcap_63d_diff},
    "evd_079_ev_to_mktcap_252d_diff":                   {"inputs": ["ev", "marketcap"],             "func": evd_079_ev_to_mktcap_252d_diff},
    "evd_080_ev_to_mktcap_5d_pct_change":               {"inputs": ["ev", "marketcap"],             "func": evd_080_ev_to_mktcap_5d_pct_change},
    "evd_081_ev_to_mktcap_21d_pct_change":              {"inputs": ["ev", "marketcap"],             "func": evd_081_ev_to_mktcap_21d_pct_change},
    "evd_082_ev_to_mktcap_63d_pct_change":              {"inputs": ["ev", "marketcap"],             "func": evd_082_ev_to_mktcap_63d_pct_change},
    "evd_083_ev_to_mktcap_21d_slope":                   {"inputs": ["ev", "marketcap"],             "func": evd_083_ev_to_mktcap_21d_slope},
    "evd_084_ev_to_mktcap_63d_slope":                   {"inputs": ["ev", "marketcap"],             "func": evd_084_ev_to_mktcap_63d_slope},
    "evd_085_ev_to_mktcap_126d_slope":                  {"inputs": ["ev", "marketcap"],             "func": evd_085_ev_to_mktcap_126d_slope},
    "evd_086_ev_to_mktcap_ratio_acceleration_21d":      {"inputs": ["ev", "marketcap"],             "func": evd_086_ev_to_mktcap_ratio_acceleration_21d},
    "evd_087_wedge_to_mktcap_5d_diff":                  {"inputs": ["ev", "marketcap"],             "func": evd_087_wedge_to_mktcap_5d_diff},
    "evd_088_wedge_to_mktcap_21d_diff":                 {"inputs": ["ev", "marketcap"],             "func": evd_088_wedge_to_mktcap_21d_diff},
    "evd_089_wedge_to_mktcap_63d_diff":                 {"inputs": ["ev", "marketcap"],             "func": evd_089_wedge_to_mktcap_63d_diff},
    "evd_090_wedge_to_mktcap_21d_slope":                {"inputs": ["ev", "marketcap"],             "func": evd_090_wedge_to_mktcap_21d_slope},
    "evd_091_evebitda_21d_diff":                        {"inputs": ["ev", "evebitda"],              "func": evd_091_evebitda_21d_diff},
    "evd_092_evebitda_63d_diff":                        {"inputs": ["ev", "evebitda"],              "func": evd_092_evebitda_63d_diff},
    "evd_093_evebitda_252d_diff":                       {"inputs": ["ev", "evebitda"],              "func": evd_093_evebitda_252d_diff},
    "evd_094_evebit_21d_diff":                          {"inputs": ["evebit", "marketcap"],         "func": evd_094_evebit_21d_diff},
    "evd_095_evebit_63d_diff":                          {"inputs": ["evebit", "marketcap"],         "func": evd_095_evebit_63d_diff},
    "evd_096_evebitda_252d_max":                        {"inputs": ["ev", "evebitda"],              "func": evd_096_evebitda_252d_max},
    "evd_097_evebitda_252d_min":                        {"inputs": ["ev", "evebitda"],              "func": evd_097_evebitda_252d_min},
    "evd_098_evebitda_252d_range":                      {"inputs": ["ev", "evebitda"],              "func": evd_098_evebitda_252d_range},
    "evd_099_evebitda_position_in_252d_range":          {"inputs": ["ev", "evebitda"],              "func": evd_099_evebitda_position_in_252d_range},
    "evd_100_evebit_position_in_252d_range":            {"inputs": ["evebit", "marketcap"],         "func": evd_100_evebit_position_in_252d_range},
    "evd_101_evebitda_pct_rank_1260d":                  {"inputs": ["ev", "evebitda"],              "func": evd_101_evebitda_pct_rank_1260d},
    "evd_102_evebit_pct_rank_1260d":                    {"inputs": ["evebit", "marketcap"],         "func": evd_102_evebit_pct_rank_1260d},
    "evd_103_evebitda_vs_21d_sma":                      {"inputs": ["ev", "evebitda"],              "func": evd_103_evebitda_vs_21d_sma},
    "evd_104_evebitda_vs_252d_sma":                     {"inputs": ["ev", "evebitda"],              "func": evd_104_evebitda_vs_252d_sma},
    "evd_105_evebit_21d_slope":                         {"inputs": ["evebit", "marketcap"],         "func": evd_105_evebit_21d_slope},
    "evd_106_ev_to_mktcap_times_evebitda":              {"inputs": ["ev", "marketcap", "evebitda"], "func": evd_106_ev_to_mktcap_times_evebitda},
    "evd_107_wedge_ratio_times_evebitda":               {"inputs": ["ev", "marketcap", "evebitda"], "func": evd_107_wedge_ratio_times_evebitda},
    "evd_108_ev_to_mktcap_ratio_vs_pe":                 {"inputs": ["ev", "marketcap", "pe"],       "func": evd_108_ev_to_mktcap_ratio_vs_pe},
    "evd_109_evebitda_minus_pe_zscore_252d":            {"inputs": ["evebitda", "pe"],              "func": evd_109_evebitda_minus_pe_zscore_252d},
    "evd_110_evebitda_minus_pe_pct_rank_1260d":         {"inputs": ["evebitda", "pe"],              "func": evd_110_evebitda_minus_pe_pct_rank_1260d},
    "evd_111_evebit_minus_pe_zscore_252d":              {"inputs": ["evebit", "pe"],                "func": evd_111_evebit_minus_pe_zscore_252d},
    "evd_112_evebitda_to_evebit_ratio":                 {"inputs": ["evebit", "evebitda"],          "func": evd_112_evebitda_to_evebit_ratio},
    "evd_113_evebitda_to_evebit_zscore_252d":           {"inputs": ["evebit", "evebitda"],          "func": evd_113_evebitda_to_evebit_zscore_252d},
    "evd_114_pe_to_ev_ratio_combined":                  {"inputs": ["ev", "marketcap", "pe"],       "func": evd_114_pe_to_ev_ratio_combined},
    "evd_115_ev_to_mktcap_ratio_times_pb":              {"inputs": ["ev", "marketcap", "pb"],       "func": evd_115_ev_to_mktcap_ratio_times_pb},
    "evd_116_ev_to_mktcap_ratio_times_ps":              {"inputs": ["ev", "marketcap", "ps"],       "func": evd_116_ev_to_mktcap_ratio_times_ps},
    "evd_117_evebitda_expanding_zscore":                {"inputs": ["ev", "evebitda"],              "func": evd_117_evebitda_expanding_zscore},
    "evd_118_evebit_expanding_zscore":                  {"inputs": ["evebit", "marketcap"],         "func": evd_118_evebit_expanding_zscore},
    "evd_119_mktcap_to_ev_below_threshold_pct_rank_252d": {"inputs": ["ev", "marketcap"],          "func": evd_119_mktcap_to_ev_below_threshold_pct_rank_252d},
    "evd_120_mktcap_to_ev_below_20pct_flag":            {"inputs": ["ev", "marketcap"],             "func": evd_120_mktcap_to_ev_below_20pct_flag},
    "evd_121_ev_to_mktcap_ewm_diff_21_63":              {"inputs": ["ev", "marketcap"],             "func": evd_121_ev_to_mktcap_ewm_diff_21_63},
    "evd_122_ev_to_mktcap_ewm_diff_63_252":             {"inputs": ["ev", "marketcap"],             "func": evd_122_ev_to_mktcap_ewm_diff_63_252},
    "evd_123_wedge_ewm_diff_21_63":                     {"inputs": ["ev", "marketcap"],             "func": evd_123_wedge_ewm_diff_21_63},
    "evd_124_evebitda_ewm_diff_21_252":                 {"inputs": ["ev", "evebitda"],              "func": evd_124_evebitda_ewm_diff_21_252},
    "evd_125_ev_to_mktcap_504d_avg":                    {"inputs": ["ev", "marketcap"],             "func": evd_125_ev_to_mktcap_504d_avg},
    "evd_126_ev_to_mktcap_756d_avg":                    {"inputs": ["ev", "marketcap"],             "func": evd_126_ev_to_mktcap_756d_avg},
    "evd_127_ev_to_mktcap_1260d_avg":                   {"inputs": ["ev", "marketcap"],             "func": evd_127_ev_to_mktcap_1260d_avg},
    "evd_128_ev_to_mktcap_vs_504d_sma":                 {"inputs": ["ev", "marketcap"],             "func": evd_128_ev_to_mktcap_vs_504d_sma},
    "evd_129_ev_to_mktcap_vs_1260d_sma":                {"inputs": ["ev", "marketcap"],             "func": evd_129_ev_to_mktcap_vs_1260d_sma},
    "evd_130_ev_to_mktcap_median_63d":                  {"inputs": ["ev", "marketcap"],             "func": evd_130_ev_to_mktcap_median_63d},
    "evd_131_ev_to_mktcap_median_252d":                 {"inputs": ["ev", "marketcap"],             "func": evd_131_ev_to_mktcap_median_252d},
    "evd_132_ev_to_mktcap_q95_252d":                    {"inputs": ["ev", "marketcap"],             "func": evd_132_ev_to_mktcap_q95_252d},
    "evd_133_ev_to_mktcap_q05_252d":                    {"inputs": ["ev", "marketcap"],             "func": evd_133_ev_to_mktcap_q05_252d},
    "evd_134_wedge_to_mktcap_q95_252d":                 {"inputs": ["ev", "marketcap"],             "func": evd_134_wedge_to_mktcap_q95_252d},
    "evd_135_wedge_to_mktcap_skew_252d":                {"inputs": ["ev", "marketcap"],             "func": evd_135_wedge_to_mktcap_skew_252d},
    "evd_136_ev_to_mktcap_ratio_expanding_max":         {"inputs": ["ev", "marketcap"],             "func": evd_136_ev_to_mktcap_ratio_expanding_max},
    "evd_137_ev_to_mktcap_ratio_vs_expanding_max":      {"inputs": ["ev", "marketcap"],             "func": evd_137_ev_to_mktcap_ratio_vs_expanding_max},
    "evd_138_mktcap_to_ev_expanding_zscore":            {"inputs": ["ev", "marketcap"],             "func": evd_138_mktcap_to_ev_expanding_zscore},
    "evd_139_ev_to_mktcap_above_2x_fraction_252d":      {"inputs": ["ev", "marketcap"],             "func": evd_139_ev_to_mktcap_above_2x_fraction_252d},
    "evd_140_ev_to_mktcap_above_3x_fraction_252d":      {"inputs": ["ev", "marketcap"],             "func": evd_140_ev_to_mktcap_above_3x_fraction_252d},
    "evd_141_ev_to_mktcap_above_5x_fraction_252d":      {"inputs": ["ev", "marketcap"],             "func": evd_141_ev_to_mktcap_above_5x_fraction_252d},
    "evd_142_ev_to_mktcap_trend_up_fraction_63d":       {"inputs": ["ev", "marketcap"],             "func": evd_142_ev_to_mktcap_trend_up_fraction_63d},
    "evd_143_ev_to_mktcap_trend_up_fraction_252d":      {"inputs": ["ev", "marketcap"],             "func": evd_143_ev_to_mktcap_trend_up_fraction_252d},
    "evd_144_divyield_times_ev_to_mktcap":              {"inputs": ["ev", "marketcap", "divyield"], "func": evd_144_divyield_times_ev_to_mktcap},
    "evd_145_pb_times_ev_to_mktcap":                    {"inputs": ["ev", "marketcap", "pb"],       "func": evd_145_pb_times_ev_to_mktcap},
    "evd_146_ps_times_ev_to_mktcap":                    {"inputs": ["ev", "marketcap", "ps"],       "func": evd_146_ps_times_ev_to_mktcap},
    "evd_147_ev_to_mktcap_std_21d":                     {"inputs": ["ev", "marketcap"],             "func": evd_147_ev_to_mktcap_std_21d},
    "evd_148_ev_to_mktcap_std_63d":                     {"inputs": ["ev", "marketcap"],             "func": evd_148_ev_to_mktcap_std_63d},
    "evd_149_ev_to_mktcap_cv_252d":                     {"inputs": ["ev", "marketcap"],             "func": evd_149_ev_to_mktcap_cv_252d},
    "evd_150_composite_ev_distortion_index":            {"inputs": ["ev", "marketcap", "evebitda", "pe"], "func": evd_150_composite_ev_distortion_index},
    "evd_176_evebitda_ewm_21":                          {"inputs": ["ev", "evebitda"],              "func": evd_176_evebitda_ewm_21},
    "evd_177_evebitda_ewm_63":                          {"inputs": ["ev", "evebitda"],              "func": evd_177_evebitda_ewm_63},
    "evd_178_evebit_ewm_21":                            {"inputs": ["evebit", "marketcap"],         "func": evd_178_evebit_ewm_21},
    "evd_179_evebit_ewm_63":                            {"inputs": ["evebit", "marketcap"],         "func": evd_179_evebit_ewm_63},
    "evd_180_evebitda_63d_slope":                       {"inputs": ["ev", "evebitda"],              "func": evd_180_evebitda_63d_slope},
    "evd_181_evebit_63d_slope":                         {"inputs": ["evebit", "marketcap"],         "func": evd_181_evebit_63d_slope},
    "evd_182_evebitda_pct_rank_252d":                   {"inputs": ["ev", "evebitda"],              "func": evd_182_evebitda_pct_rank_252d},
    "evd_183_evebit_pct_rank_252d":                     {"inputs": ["evebit", "marketcap"],         "func": evd_183_evebit_pct_rank_252d},
    "evd_184_ev_to_mktcap_126d_slope":                  {"inputs": ["ev", "marketcap"],             "func": evd_184_ev_to_mktcap_126d_slope},
    "evd_185_wedge_to_mktcap_63d_slope":                {"inputs": ["ev", "marketcap"],             "func": evd_185_wedge_to_mktcap_63d_slope},
    "evd_186_wedge_to_mktcap_126d_slope":               {"inputs": ["ev", "marketcap"],             "func": evd_186_wedge_to_mktcap_126d_slope},
    "evd_187_evebitda_to_pe_63d_avg":                   {"inputs": ["evebitda", "pe"],              "func": evd_187_evebitda_to_pe_63d_avg},
    "evd_188_evebitda_to_pe_126d_avg":                  {"inputs": ["evebitda", "pe"],              "func": evd_188_evebitda_to_pe_126d_avg},
    "evd_189_evebit_to_pe_63d_avg":                     {"inputs": ["evebit", "pe"],                "func": evd_189_evebit_to_pe_63d_avg},
    "evd_190_evebitda_to_pe_expanding_zscore":          {"inputs": ["evebitda", "pe"],              "func": evd_190_evebitda_to_pe_expanding_zscore},
    "evd_191_divyield_zscore_252d":                     {"inputs": ["ev", "marketcap", "divyield"], "func": evd_191_divyield_zscore_252d},
    "evd_192_divyield_times_wedge_ratio":               {"inputs": ["ev", "marketcap", "divyield"], "func": evd_192_divyield_times_wedge_ratio},
    "evd_193_pb_to_ev_to_mktcap_ratio":                 {"inputs": ["ev", "marketcap", "pb"],       "func": evd_193_pb_to_ev_to_mktcap_ratio},
    "evd_194_ps_to_ev_to_mktcap_ratio":                 {"inputs": ["ev", "marketcap", "ps"],       "func": evd_194_ps_to_ev_to_mktcap_ratio},
    "evd_195_ev_to_mktcap_trend_dn_fraction_63d":       {"inputs": ["ev", "marketcap"],             "func": evd_195_ev_to_mktcap_trend_dn_fraction_63d},
    "evd_196_ev_to_mktcap_trend_dn_fraction_252d":      {"inputs": ["ev", "marketcap"],             "func": evd_196_ev_to_mktcap_trend_dn_fraction_252d},
    "evd_197_evebitda_to_evebit_252d_avg":              {"inputs": ["evebit", "evebitda"],          "func": evd_197_evebitda_to_evebit_252d_avg},
    "evd_198_ev_to_mktcap_ratio_ewm_cross_21_252":      {"inputs": ["ev", "marketcap"],             "func": evd_198_ev_to_mktcap_ratio_ewm_cross_21_252},
    "evd_199_wedge_to_mktcap_pct_rank_1260d":           {"inputs": ["ev", "marketcap"],             "func": evd_199_wedge_to_mktcap_pct_rank_1260d},
    "evd_200_equity_share_trend_down_fraction_252d":    {"inputs": ["ev", "marketcap"],             "func": evd_200_equity_share_trend_down_fraction_252d},
}
