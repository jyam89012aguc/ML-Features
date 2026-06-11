"""
79_ev_distortion — Extended Features 001-075
Domain: enterprise-value vs equity-value distortion — additional EV/marketcap ratio
        windows, net-debt-wedge dynamics, drawdown-divergence variants, EV-multiple gap
        angles, equity-slice erosion streaks, and composite distortion scores.
Inputs: daily-frequency Sharadar DAILY/METRICS valuation fields only.
        Canonical field names (lowercase): marketcap, ev, pe, pb, ps, evebit, evebitda, divyield.
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
    """Element-wise division; replaces zero denominator with NaN."""
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


def _net_debt_wedge(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """ev - marketcap = implied net debt + minority interest + preferred."""
    return ev - marketcap


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(float)
    grp = (~cond.astype(bool)).cumsum()
    return c.groupby(grp).cumsum()


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): EV/marketcap ratio — new windows and transforms ---

def evd_ext_001_ev_to_mktcap_10d_avg(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """10-day rolling mean of EV/marketcap ratio (bi-weekly smoothed distortion)."""
    return _rolling_mean(_safe_div(ev, marketcap), 10)


def evd_ext_002_ev_to_mktcap_504d_avg(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """504-day rolling mean of EV/marketcap ratio (two-year average distortion)."""
    return _rolling_mean(_safe_div(ev, marketcap), _TD_2Y)


def evd_ext_003_ev_to_mktcap_median_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day rolling median of EV/marketcap ratio (robust central distortion)."""
    return _rolling_median(_safe_div(ev, marketcap), _TD_YEAR)


def evd_ext_004_ev_to_mktcap_zscore_126d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """126-day z-score of EV/marketcap ratio (semi-annual statistical extremity)."""
    return _zscore_rolling(_safe_div(ev, marketcap), _TD_HALF)


def evd_ext_005_ev_to_mktcap_zscore_504d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """504-day z-score of EV/marketcap ratio (two-year statistical extremity)."""
    return _zscore_rolling(_safe_div(ev, marketcap), _TD_2Y)


def evd_ext_006_ev_to_mktcap_pct_rank_504d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """504-day percentile rank of EV/marketcap ratio."""
    return _rolling_rank_pct(_safe_div(ev, marketcap), _TD_2Y)


def evd_ext_007_ev_to_mktcap_pct_rank_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day percentile rank of EV/marketcap ratio (quarterly distortion rank)."""
    return _rolling_rank_pct(_safe_div(ev, marketcap), _TD_QTR)


def evd_ext_008_ev_to_mktcap_drawup_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EV/marketcap ratio minus its 252-day rolling minimum (distortion drawup)."""
    ratio = _safe_div(ev, marketcap)
    return ratio - _rolling_min(ratio, _TD_YEAR)


def evd_ext_009_ev_to_mktcap_vs_252d_max(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EV/marketcap ratio as fraction of its 252-day rolling maximum."""
    ratio = _safe_div(ev, marketcap)
    return _safe_div(ratio, _rolling_max(ratio, _TD_YEAR))


def evd_ext_010_log_ev_to_mktcap_252d_avg(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day rolling mean of log EV/marketcap ratio (linearized smoothed distortion)."""
    return _rolling_mean(_log_safe(_safe_div(ev, marketcap)), _TD_YEAR)


def evd_ext_011_ev_to_mktcap_126d_change(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """126-day change in EV/marketcap ratio (semi-annual distortion drift)."""
    return _safe_div(ev, marketcap).diff(_TD_HALF)


def evd_ext_012_ev_to_mktcap_252d_change(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day change in EV/marketcap ratio (annual distortion drift)."""
    return _safe_div(ev, marketcap).diff(_TD_YEAR)


# --- Group B (013-024): Net-debt wedge dynamics and streaks ---

def evd_ext_013_wedge_to_ev_252d_avg(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day rolling mean of wedge/EV ratio (annual debt fraction of enterprise)."""
    return _rolling_mean(_safe_div(_net_debt_wedge(ev, marketcap), ev), _TD_YEAR)


def evd_ext_014_wedge_to_ev_zscore_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day z-score of wedge/EV ratio (debt-fraction statistical extremity)."""
    return _zscore_rolling(_safe_div(_net_debt_wedge(ev, marketcap), ev), _TD_YEAR)


def evd_ext_015_wedge_to_ev_pct_rank_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day percentile rank of wedge/EV ratio."""
    return _rolling_rank_pct(_safe_div(_net_debt_wedge(ev, marketcap), ev), _TD_YEAR)


def evd_ext_016_wedge_abs_252d_max(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day rolling maximum of the absolute net-debt wedge (peak dollar debt burden)."""
    return _rolling_max(_net_debt_wedge(ev, marketcap), _TD_YEAR)


def evd_ext_017_wedge_to_mktcap_21d_change(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day change in wedge/marketcap ratio (monthly leverage drift)."""
    return _safe_div(_net_debt_wedge(ev, marketcap), marketcap).diff(_TD_MON)


def evd_ext_018_wedge_to_mktcap_63d_change(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day change in wedge/marketcap ratio (quarterly leverage drift)."""
    return _safe_div(_net_debt_wedge(ev, marketcap), marketcap).diff(_TD_QTR)


def evd_ext_019_wedge_pos_streak(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Consecutive days enterprise value has exceeded marketcap (positive net debt)."""
    return _consec_streak(ev > marketcap)


def evd_ext_020_wedge_to_mktcap_above_1_flag(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Binary flag: wedge/marketcap > 1 (net debt exceeds equity value)."""
    return (_safe_div(_net_debt_wedge(ev, marketcap), marketcap) > 1.0).astype(float)


def evd_ext_021_wedge_to_mktcap_above_1_fraction_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Fraction of past 252 days where wedge/marketcap exceeded 1."""
    flag = (_safe_div(_net_debt_wedge(ev, marketcap), marketcap) > 1.0).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def evd_ext_022_wedge_to_mktcap_drawup_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Wedge/marketcap ratio minus its 252-day rolling minimum (leverage drawup)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return ratio - _rolling_min(ratio, _TD_YEAR)


def evd_ext_023_wedge_to_mktcap_vol_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day rolling std of wedge/marketcap ratio (annual leverage instability)."""
    return _rolling_std(_safe_div(_net_debt_wedge(ev, marketcap), marketcap), _TD_YEAR)


def evd_ext_024_wedge_to_mktcap_504d_max(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """504-day rolling maximum of wedge/marketcap ratio (worst two-year leverage)."""
    return _rolling_max(_safe_div(_net_debt_wedge(ev, marketcap), marketcap), _TD_2Y)


# --- Group C (025-036): EV vs marketcap drawdown divergence variants ---

def evd_ext_025_dd_divergence_126d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Marketcap dd minus EV dd over 126 days (semi-annual divergence)."""
    mc_h = _rolling_max(marketcap, _TD_HALF)
    ev_h = _rolling_max(ev, _TD_HALF)
    return _safe_div(marketcap - mc_h, mc_h) - _safe_div(ev - ev_h, ev_h)


def evd_ext_026_dd_divergence_21d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Marketcap dd minus EV dd over 21 days (monthly divergence)."""
    mc_h = _rolling_max(marketcap, _TD_MON)
    ev_h = _rolling_max(ev, _TD_MON)
    return _safe_div(marketcap - mc_h, mc_h) - _safe_div(ev - ev_h, ev_h)


def evd_ext_027_dd_divergence_756d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Marketcap dd minus EV dd over 756 days (three-year divergence)."""
    mc_h = _rolling_max(marketcap, _TD_3Y)
    ev_h = _rolling_max(ev, _TD_3Y)
    return _safe_div(marketcap - mc_h, mc_h) - _safe_div(ev - ev_h, ev_h)


def evd_ext_028_dd_divergence_ratio_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Ratio of marketcap 252-day dd to EV 252-day dd (equity falls how many x EV)."""
    mc_h = _rolling_max(marketcap, _TD_YEAR)
    ev_h = _rolling_max(ev, _TD_YEAR)
    return _safe_div(_safe_div(marketcap - mc_h, mc_h), _safe_div(ev - ev_h, ev_h))


def evd_ext_029_dd_divergence_zscore_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day z-score of the 252-day EV-vs-equity dd divergence."""
    mc_h = _rolling_max(marketcap, _TD_YEAR)
    ev_h = _rolling_max(ev, _TD_YEAR)
    div = _safe_div(marketcap - mc_h, mc_h) - _safe_div(ev - ev_h, ev_h)
    return _zscore_rolling(div, _TD_QTR)


def evd_ext_030_dd_divergence_pct_rank_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day percentile rank of the 252-day EV-vs-equity dd divergence."""
    mc_h = _rolling_max(marketcap, _TD_YEAR)
    ev_h = _rolling_max(ev, _TD_YEAR)
    div = _safe_div(marketcap - mc_h, mc_h) - _safe_div(ev - ev_h, ev_h)
    return _rolling_rank_pct(div, _TD_YEAR)


def evd_ext_031_mktcap_dd_from_504d_high(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Marketcap drawdown from its 504-day high (two-year equity destruction)."""
    h = _rolling_max(marketcap, _TD_2Y)
    return _safe_div(marketcap - h, h)


def evd_ext_032_ev_dd_from_504d_high(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EV drawdown from its 504-day high (two-year enterprise destruction)."""
    h = _rolling_max(ev, _TD_2Y)
    return _safe_div(ev - h, h)


def evd_ext_033_equity_dd_excess_over_ev_log(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Log-space 252-day drawdown of marketcap minus log-space EV drawdown."""
    mc_pk = _rolling_max(marketcap, _TD_YEAR)
    ev_pk = _rolling_max(ev, _TD_YEAR)
    mc_log_dd = _log_safe(marketcap) - _log_safe(mc_pk)
    ev_log_dd = _log_safe(ev) - _log_safe(ev_pk)
    return mc_log_dd - ev_log_dd


def evd_ext_034_mktcap_falls_ev_holds_flag(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Flag: marketcap down >10% over 63d while EV down <5% (equity-only collapse)."""
    mc_chg = marketcap.pct_change(_TD_QTR)
    ev_chg = ev.pct_change(_TD_QTR)
    return ((mc_chg < -0.10) & (ev_chg > -0.05)).astype(float)


def evd_ext_035_mktcap_falls_ev_holds_fraction_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day fraction of days marketcap down >10% over 63d while EV down <5%."""
    mc_chg = marketcap.pct_change(_TD_QTR)
    ev_chg = ev.pct_change(_TD_QTR)
    flag = ((mc_chg < -0.10) & (ev_chg > -0.05)).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def evd_ext_036_dd_divergence_ewm_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day EWM of the 252-day EV-vs-equity dd divergence (smoothed divergence trend)."""
    mc_h = _rolling_max(marketcap, _TD_YEAR)
    ev_h = _rolling_max(ev, _TD_YEAR)
    div = _safe_div(marketcap - mc_h, mc_h) - _safe_div(ev - ev_h, ev_h)
    return _ewm_mean(div, _TD_QTR)


# --- Group D (037-048): EV-multiple vs equity-multiple gap variants ---

def evd_ext_037_evebitda_minus_ps(evebitda: pd.Series, ps: pd.Series) -> pd.Series:
    """EV/EBITDA minus P/S: enterprise-earnings vs equity-sales multiple gap."""
    return evebitda - ps


def evd_ext_038_evebit_minus_pb(evebit: pd.Series, pb: pd.Series) -> pd.Series:
    """EV/EBIT minus P/B: operating-earnings vs book-value multiple gap."""
    return evebit - pb


def evd_ext_039_evebitda_to_ps_ratio(evebitda: pd.Series, ps: pd.Series) -> pd.Series:
    """EV/EBITDA divided by P/S (enterprise-earnings vs equity-sales multiple ratio)."""
    return _safe_div(evebitda, ps)


def evd_ext_040_evebit_to_evebitda_ratio(evebit: pd.Series, evebitda: pd.Series) -> pd.Series:
    """EV/EBIT divided by EV/EBITDA (D&A burden embedded in enterprise multiple)."""
    return _safe_div(evebit, evebitda)


def evd_ext_041_evebitda_to_pe_63d_avg(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """63-day rolling mean of EV/EBITDA-to-P/E ratio (quarterly multiple gap)."""
    return _rolling_mean(_safe_div(evebitda, pe), _TD_QTR)


def evd_ext_042_evebitda_to_pe_pct_rank_504d(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """504-day percentile rank of EV/EBITDA-to-P/E ratio."""
    return _rolling_rank_pct(_safe_div(evebitda, pe), _TD_2Y)


def evd_ext_043_evebit_to_pe_zscore_126d(evebit: pd.Series, pe: pd.Series) -> pd.Series:
    """126-day z-score of EV/EBIT-to-P/E ratio (semi-annual multiple-gap extremity)."""
    return _zscore_rolling(_safe_div(evebit, pe), _TD_HALF)


def evd_ext_044_evebitda_to_pe_drawup_252d(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """EV/EBITDA-to-P/E ratio minus its 252-day rolling minimum (multiple-gap drawup)."""
    ratio = _safe_div(evebitda, pe)
    return ratio - _rolling_min(ratio, _TD_YEAR)


def evd_ext_045_evebitda_pe_gap_252d_change(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """252-day change in the raw EV/EBITDA - P/E spread."""
    return (evebitda - pe).diff(_TD_YEAR)


def evd_ext_046_pe_minus_evebitda_252d_avg(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """252-day rolling mean of P/E minus EV/EBITDA (equity-cheap-vs-enterprise gap)."""
    return _rolling_mean(pe - evebitda, _TD_YEAR)


def evd_ext_047_evebit_ath_drawdown_zscore_252d(evebit: pd.Series, pe: pd.Series) -> pd.Series:
    """252-day z-score of EV/EBIT drawdown from its all-time high."""
    h = evebit.expanding(min_periods=1).max()
    dd = _safe_div(evebit - h, h.replace(0, np.nan).abs())
    return _zscore_rolling(dd, _TD_YEAR)


def evd_ext_048_multiple_gap_evebitda_pe_vol_252d(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """252-day rolling std of the EV/EBITDA - P/E spread (multiple-gap instability)."""
    return _rolling_std(evebitda - pe, _TD_YEAR)


# --- Group E (049-060): Equity-slice erosion and thin-equity persistence ---

def evd_ext_049_equity_share_streak_below_30pct(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Consecutive days the equity/EV share has stayed below 30%."""
    return _consec_streak(_safe_div(marketcap, ev) < 0.30)


def evd_ext_050_equity_share_streak_below_10pct(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Consecutive days the equity/EV share has stayed below 10% (deep subordination)."""
    return _consec_streak(_safe_div(marketcap, ev) < 0.10)


def evd_ext_051_equity_share_below_20pct_fraction_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Fraction of past 252 days where equity/EV share was below 20%."""
    flag = (_safe_div(marketcap, ev) < 0.20).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def evd_ext_052_equity_share_below_50pct_fraction_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Fraction of past 252 days where equity/EV share was below 50%."""
    flag = (_safe_div(marketcap, ev) < 0.50).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def evd_ext_053_equity_share_126d_drawdown(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Equity/EV share drawdown from its 126-day rolling peak (slice erosion depth)."""
    ratio = _safe_div(marketcap, ev)
    pk = _rolling_max(ratio, _TD_HALF)
    return _safe_div(ratio - pk, pk)


def evd_ext_054_equity_share_252d_drawdown(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Equity/EV share drawdown from its 252-day rolling peak."""
    ratio = _safe_div(marketcap, ev)
    pk = _rolling_max(ratio, _TD_YEAR)
    return _safe_div(ratio - pk, pk)


def evd_ext_055_equity_share_decay_42d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """42-day change in equity/EV share (two-month slice erosion rate)."""
    return _safe_div(marketcap, ev).diff(42)


def evd_ext_056_equity_share_decay_126d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """126-day change in equity/EV share (semi-annual slice erosion rate)."""
    return _safe_div(marketcap, ev).diff(_TD_HALF)


def evd_ext_057_equity_share_pct_rank_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day percentile rank of equity/EV share (low rank = thin residual equity)."""
    return _rolling_rank_pct(_safe_div(marketcap, ev), _TD_YEAR)


def evd_ext_058_equity_share_vs_252d_avg(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Equity/EV share deviation from its own 252-day rolling mean."""
    ratio = _safe_div(marketcap, ev)
    avg = _rolling_mean(ratio, _TD_YEAR)
    return _safe_div(ratio - avg, avg)


def evd_ext_059_equity_share_zscore_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day z-score of equity/EV share (statistical thinness of residual equity)."""
    return _zscore_rolling(_safe_div(marketcap, ev), _TD_YEAR)


def evd_ext_060_equity_share_neg_decay_streak(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Consecutive days the 21-day change in equity/EV share has stayed negative."""
    return _consec_streak(_safe_div(marketcap, ev).diff(_TD_MON) < 0)


# --- Group F (061-068): EWM signals and trend-gap variants ---

def evd_ext_061_ewm_ev_to_mktcap_5(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day EWM of EV/marketcap ratio (very fast distortion signal)."""
    return _ewm_mean(_safe_div(ev, marketcap), _TD_WEEK)


def evd_ext_062_ewm_ev_to_mktcap_504(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """504-day EWM of EV/marketcap ratio (two-year slow distortion trend)."""
    return _ewm_mean(_safe_div(ev, marketcap), _TD_2Y)


def evd_ext_063_ev_to_mktcap_ewm_diff_5_63(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EWM(5) minus EWM(63) of EV/marketcap ratio (fast-quarterly trend gap)."""
    ratio = _safe_div(ev, marketcap)
    return _ewm_mean(ratio, _TD_WEEK) - _ewm_mean(ratio, _TD_QTR)


def evd_ext_064_ev_to_mktcap_ewm_diff_63_252(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EWM(63) minus EWM(252) of EV/marketcap ratio (quarterly-annual trend gap)."""
    ratio = _safe_div(ev, marketcap)
    return _ewm_mean(ratio, _TD_QTR) - _ewm_mean(ratio, _TD_YEAR)


def evd_ext_065_ewm_wedge_ratio_252(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day EWM of wedge/marketcap ratio (annual leverage trend)."""
    return _ewm_mean(_safe_div(_net_debt_wedge(ev, marketcap), marketcap), _TD_YEAR)


def evd_ext_066_wedge_ratio_ewm_diff_21_126(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EWM(21) minus EWM(126) of wedge/marketcap ratio (fast-semi-annual leverage gap)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return _ewm_mean(ratio, _TD_MON) - _ewm_mean(ratio, _TD_HALF)


def evd_ext_067_ev_to_mktcap_vs_own_126d_sma(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EV/marketcap ratio deviation from its own 126-day SMA."""
    ratio = _safe_div(ev, marketcap)
    sma = _rolling_mean(ratio, _TD_HALF)
    return _safe_div(ratio - sma, sma)


def evd_ext_068_ev_to_mktcap_vs_own_504d_sma(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EV/marketcap ratio deviation from its own 504-day SMA."""
    ratio = _safe_div(ev, marketcap)
    sma = _rolling_mean(ratio, _TD_2Y)
    return _safe_div(ratio - sma, sma)


# --- Group G (069-075): Composite distortion and breadth scores ---

def evd_ext_069_ev_to_mktcap_above_2x_fraction_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Fraction of past 252 days where EV/marketcap exceeded 2 (persistent debt dominance)."""
    flag = (_safe_div(ev, marketcap) > 2.0).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def evd_ext_070_ev_to_mktcap_above_6x_flag(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Binary flag: EV/marketcap > 6 (equity is a near-vanishing residual)."""
    return (_safe_div(ev, marketcap) > 6.0).astype(float)


def evd_ext_071_distortion_breadth_score(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Count (0-3) of EV/marketcap ratio above its 63/126/252-day 90th percentiles."""
    ratio = _safe_div(ev, marketcap)
    total = pd.Series(0.0, index=marketcap.index)
    for w in (_TD_QTR, _TD_HALF, _TD_YEAR):
        q = ratio.rolling(w, min_periods=max(1, w // 2)).quantile(0.90)
        total = total + (ratio > q).astype(float)
    return total


def evd_ext_072_composite_distortion_score_126d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """126-day composite distortion: avg of z-scores of (ev/mktcap) and (wedge/mktcap)."""
    z1 = _zscore_rolling(_safe_div(ev, marketcap), _TD_HALF)
    z2 = _zscore_rolling(_safe_div(_net_debt_wedge(ev, marketcap), marketcap), _TD_HALF)
    return (z1 + z2) / 2.0


def evd_ext_073_composite_distortion_score_504d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """504-day composite distortion: avg of z-scores of (ev/mktcap) and (wedge/mktcap)."""
    z1 = _zscore_rolling(_safe_div(ev, marketcap), _TD_2Y)
    z2 = _zscore_rolling(_safe_div(_net_debt_wedge(ev, marketcap), marketcap), _TD_2Y)
    return (z1 + z2) / 2.0


def evd_ext_074_distortion_capitulation_composite(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Capitulation composite: ev/mktcap 252d pct-rank + (1 - equity/EV share) + |z|/3 clipped."""
    ratio = _safe_div(ev, marketcap)
    rank = _rolling_rank_pct(ratio, _TD_YEAR)
    eq_share = _safe_div(marketcap, ev).clip(lower=0.0, upper=1.0)
    z = _zscore_rolling(ratio, _TD_YEAR).abs().clip(upper=3.0) / 3.0
    return rank.fillna(0.5) + (1.0 - eq_share.fillna(0.5)) + z


def evd_ext_075_wedge_distortion_acceleration_free_score(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Composite leverage stress: wedge/EV pct-rank plus wedge/marketcap 252d z-score clipped."""
    wedge_ev_rank = _rolling_rank_pct(_safe_div(_net_debt_wedge(ev, marketcap), ev), _TD_YEAR)
    wedge_mc_z = _zscore_rolling(_safe_div(_net_debt_wedge(ev, marketcap), marketcap), _TD_YEAR)
    return wedge_ev_rank.fillna(0.5) + wedge_mc_z.clip(lower=-3.0, upper=3.0) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

EV_DISTORTION_EXTENDED_REGISTRY_001_075 = {
    "evd_ext_001_ev_to_mktcap_10d_avg":                   {"inputs": ["ev", "marketcap"], "func": evd_ext_001_ev_to_mktcap_10d_avg},
    "evd_ext_002_ev_to_mktcap_504d_avg":                  {"inputs": ["ev", "marketcap"], "func": evd_ext_002_ev_to_mktcap_504d_avg},
    "evd_ext_003_ev_to_mktcap_median_252d":               {"inputs": ["ev", "marketcap"], "func": evd_ext_003_ev_to_mktcap_median_252d},
    "evd_ext_004_ev_to_mktcap_zscore_126d":               {"inputs": ["ev", "marketcap"], "func": evd_ext_004_ev_to_mktcap_zscore_126d},
    "evd_ext_005_ev_to_mktcap_zscore_504d":               {"inputs": ["ev", "marketcap"], "func": evd_ext_005_ev_to_mktcap_zscore_504d},
    "evd_ext_006_ev_to_mktcap_pct_rank_504d":             {"inputs": ["ev", "marketcap"], "func": evd_ext_006_ev_to_mktcap_pct_rank_504d},
    "evd_ext_007_ev_to_mktcap_pct_rank_63d":              {"inputs": ["ev", "marketcap"], "func": evd_ext_007_ev_to_mktcap_pct_rank_63d},
    "evd_ext_008_ev_to_mktcap_drawup_252d":               {"inputs": ["ev", "marketcap"], "func": evd_ext_008_ev_to_mktcap_drawup_252d},
    "evd_ext_009_ev_to_mktcap_vs_252d_max":               {"inputs": ["ev", "marketcap"], "func": evd_ext_009_ev_to_mktcap_vs_252d_max},
    "evd_ext_010_log_ev_to_mktcap_252d_avg":              {"inputs": ["ev", "marketcap"], "func": evd_ext_010_log_ev_to_mktcap_252d_avg},
    "evd_ext_011_ev_to_mktcap_126d_change":               {"inputs": ["ev", "marketcap"], "func": evd_ext_011_ev_to_mktcap_126d_change},
    "evd_ext_012_ev_to_mktcap_252d_change":               {"inputs": ["ev", "marketcap"], "func": evd_ext_012_ev_to_mktcap_252d_change},
    "evd_ext_013_wedge_to_ev_252d_avg":                   {"inputs": ["ev", "marketcap"], "func": evd_ext_013_wedge_to_ev_252d_avg},
    "evd_ext_014_wedge_to_ev_zscore_252d":                {"inputs": ["ev", "marketcap"], "func": evd_ext_014_wedge_to_ev_zscore_252d},
    "evd_ext_015_wedge_to_ev_pct_rank_252d":              {"inputs": ["ev", "marketcap"], "func": evd_ext_015_wedge_to_ev_pct_rank_252d},
    "evd_ext_016_wedge_abs_252d_max":                     {"inputs": ["ev", "marketcap"], "func": evd_ext_016_wedge_abs_252d_max},
    "evd_ext_017_wedge_to_mktcap_21d_change":             {"inputs": ["ev", "marketcap"], "func": evd_ext_017_wedge_to_mktcap_21d_change},
    "evd_ext_018_wedge_to_mktcap_63d_change":             {"inputs": ["ev", "marketcap"], "func": evd_ext_018_wedge_to_mktcap_63d_change},
    "evd_ext_019_wedge_pos_streak":                       {"inputs": ["ev", "marketcap"], "func": evd_ext_019_wedge_pos_streak},
    "evd_ext_020_wedge_to_mktcap_above_1_flag":           {"inputs": ["ev", "marketcap"], "func": evd_ext_020_wedge_to_mktcap_above_1_flag},
    "evd_ext_021_wedge_to_mktcap_above_1_fraction_252d":  {"inputs": ["ev", "marketcap"], "func": evd_ext_021_wedge_to_mktcap_above_1_fraction_252d},
    "evd_ext_022_wedge_to_mktcap_drawup_252d":            {"inputs": ["ev", "marketcap"], "func": evd_ext_022_wedge_to_mktcap_drawup_252d},
    "evd_ext_023_wedge_to_mktcap_vol_252d":               {"inputs": ["ev", "marketcap"], "func": evd_ext_023_wedge_to_mktcap_vol_252d},
    "evd_ext_024_wedge_to_mktcap_504d_max":               {"inputs": ["ev", "marketcap"], "func": evd_ext_024_wedge_to_mktcap_504d_max},
    "evd_ext_025_dd_divergence_126d":                     {"inputs": ["ev", "marketcap"], "func": evd_ext_025_dd_divergence_126d},
    "evd_ext_026_dd_divergence_21d":                      {"inputs": ["ev", "marketcap"], "func": evd_ext_026_dd_divergence_21d},
    "evd_ext_027_dd_divergence_756d":                     {"inputs": ["ev", "marketcap"], "func": evd_ext_027_dd_divergence_756d},
    "evd_ext_028_dd_divergence_ratio_252d":               {"inputs": ["ev", "marketcap"], "func": evd_ext_028_dd_divergence_ratio_252d},
    "evd_ext_029_dd_divergence_zscore_63d":               {"inputs": ["ev", "marketcap"], "func": evd_ext_029_dd_divergence_zscore_63d},
    "evd_ext_030_dd_divergence_pct_rank_252d":            {"inputs": ["ev", "marketcap"], "func": evd_ext_030_dd_divergence_pct_rank_252d},
    "evd_ext_031_mktcap_dd_from_504d_high":               {"inputs": ["ev", "marketcap"], "func": evd_ext_031_mktcap_dd_from_504d_high},
    "evd_ext_032_ev_dd_from_504d_high":                   {"inputs": ["ev", "marketcap"], "func": evd_ext_032_ev_dd_from_504d_high},
    "evd_ext_033_equity_dd_excess_over_ev_log":           {"inputs": ["ev", "marketcap"], "func": evd_ext_033_equity_dd_excess_over_ev_log},
    "evd_ext_034_mktcap_falls_ev_holds_flag":             {"inputs": ["ev", "marketcap"], "func": evd_ext_034_mktcap_falls_ev_holds_flag},
    "evd_ext_035_mktcap_falls_ev_holds_fraction_252d":    {"inputs": ["ev", "marketcap"], "func": evd_ext_035_mktcap_falls_ev_holds_fraction_252d},
    "evd_ext_036_dd_divergence_ewm_63d":                  {"inputs": ["ev", "marketcap"], "func": evd_ext_036_dd_divergence_ewm_63d},
    "evd_ext_037_evebitda_minus_ps":                      {"inputs": ["evebitda", "ps"],  "func": evd_ext_037_evebitda_minus_ps},
    "evd_ext_038_evebit_minus_pb":                        {"inputs": ["evebit", "pb"],    "func": evd_ext_038_evebit_minus_pb},
    "evd_ext_039_evebitda_to_ps_ratio":                   {"inputs": ["evebitda", "ps"],  "func": evd_ext_039_evebitda_to_ps_ratio},
    "evd_ext_040_evebit_to_evebitda_ratio":               {"inputs": ["evebit", "evebitda"], "func": evd_ext_040_evebit_to_evebitda_ratio},
    "evd_ext_041_evebitda_to_pe_63d_avg":                 {"inputs": ["evebitda", "pe"],  "func": evd_ext_041_evebitda_to_pe_63d_avg},
    "evd_ext_042_evebitda_to_pe_pct_rank_504d":           {"inputs": ["evebitda", "pe"],  "func": evd_ext_042_evebitda_to_pe_pct_rank_504d},
    "evd_ext_043_evebit_to_pe_zscore_126d":               {"inputs": ["evebit", "pe"],    "func": evd_ext_043_evebit_to_pe_zscore_126d},
    "evd_ext_044_evebitda_to_pe_drawup_252d":             {"inputs": ["evebitda", "pe"],  "func": evd_ext_044_evebitda_to_pe_drawup_252d},
    "evd_ext_045_evebitda_pe_gap_252d_change":            {"inputs": ["evebitda", "pe"],  "func": evd_ext_045_evebitda_pe_gap_252d_change},
    "evd_ext_046_pe_minus_evebitda_252d_avg":             {"inputs": ["evebitda", "pe"],  "func": evd_ext_046_pe_minus_evebitda_252d_avg},
    "evd_ext_047_evebit_ath_drawdown_zscore_252d":        {"inputs": ["evebit", "pe"],    "func": evd_ext_047_evebit_ath_drawdown_zscore_252d},
    "evd_ext_048_multiple_gap_evebitda_pe_vol_252d":      {"inputs": ["evebitda", "pe"],  "func": evd_ext_048_multiple_gap_evebitda_pe_vol_252d},
    "evd_ext_049_equity_share_streak_below_30pct":        {"inputs": ["ev", "marketcap"], "func": evd_ext_049_equity_share_streak_below_30pct},
    "evd_ext_050_equity_share_streak_below_10pct":        {"inputs": ["ev", "marketcap"], "func": evd_ext_050_equity_share_streak_below_10pct},
    "evd_ext_051_equity_share_below_20pct_fraction_252d": {"inputs": ["ev", "marketcap"], "func": evd_ext_051_equity_share_below_20pct_fraction_252d},
    "evd_ext_052_equity_share_below_50pct_fraction_252d": {"inputs": ["ev", "marketcap"], "func": evd_ext_052_equity_share_below_50pct_fraction_252d},
    "evd_ext_053_equity_share_126d_drawdown":             {"inputs": ["ev", "marketcap"], "func": evd_ext_053_equity_share_126d_drawdown},
    "evd_ext_054_equity_share_252d_drawdown":             {"inputs": ["ev", "marketcap"], "func": evd_ext_054_equity_share_252d_drawdown},
    "evd_ext_055_equity_share_decay_42d":                 {"inputs": ["ev", "marketcap"], "func": evd_ext_055_equity_share_decay_42d},
    "evd_ext_056_equity_share_decay_126d":                {"inputs": ["ev", "marketcap"], "func": evd_ext_056_equity_share_decay_126d},
    "evd_ext_057_equity_share_pct_rank_252d":             {"inputs": ["ev", "marketcap"], "func": evd_ext_057_equity_share_pct_rank_252d},
    "evd_ext_058_equity_share_vs_252d_avg":               {"inputs": ["ev", "marketcap"], "func": evd_ext_058_equity_share_vs_252d_avg},
    "evd_ext_059_equity_share_zscore_252d":               {"inputs": ["ev", "marketcap"], "func": evd_ext_059_equity_share_zscore_252d},
    "evd_ext_060_equity_share_neg_decay_streak":          {"inputs": ["ev", "marketcap"], "func": evd_ext_060_equity_share_neg_decay_streak},
    "evd_ext_061_ewm_ev_to_mktcap_5":                     {"inputs": ["ev", "marketcap"], "func": evd_ext_061_ewm_ev_to_mktcap_5},
    "evd_ext_062_ewm_ev_to_mktcap_504":                   {"inputs": ["ev", "marketcap"], "func": evd_ext_062_ewm_ev_to_mktcap_504},
    "evd_ext_063_ev_to_mktcap_ewm_diff_5_63":             {"inputs": ["ev", "marketcap"], "func": evd_ext_063_ev_to_mktcap_ewm_diff_5_63},
    "evd_ext_064_ev_to_mktcap_ewm_diff_63_252":           {"inputs": ["ev", "marketcap"], "func": evd_ext_064_ev_to_mktcap_ewm_diff_63_252},
    "evd_ext_065_ewm_wedge_ratio_252":                    {"inputs": ["ev", "marketcap"], "func": evd_ext_065_ewm_wedge_ratio_252},
    "evd_ext_066_wedge_ratio_ewm_diff_21_126":            {"inputs": ["ev", "marketcap"], "func": evd_ext_066_wedge_ratio_ewm_diff_21_126},
    "evd_ext_067_ev_to_mktcap_vs_own_126d_sma":           {"inputs": ["ev", "marketcap"], "func": evd_ext_067_ev_to_mktcap_vs_own_126d_sma},
    "evd_ext_068_ev_to_mktcap_vs_own_504d_sma":           {"inputs": ["ev", "marketcap"], "func": evd_ext_068_ev_to_mktcap_vs_own_504d_sma},
    "evd_ext_069_ev_to_mktcap_above_2x_fraction_252d":    {"inputs": ["ev", "marketcap"], "func": evd_ext_069_ev_to_mktcap_above_2x_fraction_252d},
    "evd_ext_070_ev_to_mktcap_above_6x_flag":             {"inputs": ["ev", "marketcap"], "func": evd_ext_070_ev_to_mktcap_above_6x_flag},
    "evd_ext_071_distortion_breadth_score":               {"inputs": ["ev", "marketcap"], "func": evd_ext_071_distortion_breadth_score},
    "evd_ext_072_composite_distortion_score_126d":        {"inputs": ["ev", "marketcap"], "func": evd_ext_072_composite_distortion_score_126d},
    "evd_ext_073_composite_distortion_score_504d":        {"inputs": ["ev", "marketcap"], "func": evd_ext_073_composite_distortion_score_504d},
    "evd_ext_074_distortion_capitulation_composite":      {"inputs": ["ev", "marketcap"], "func": evd_ext_074_distortion_capitulation_composite},
    "evd_ext_075_wedge_distortion_acceleration_free_score": {"inputs": ["ev", "marketcap"], "func": evd_ext_075_wedge_distortion_acceleration_free_score},
}
