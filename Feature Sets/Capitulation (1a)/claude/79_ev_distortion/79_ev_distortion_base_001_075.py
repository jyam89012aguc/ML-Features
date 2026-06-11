"""
79_ev_distortion — Base Features 001-100
Domain: enterprise-value vs equity-value distortion — the gap and ratio between EV and
        market-cap, the implied net-debt wedge, equity shrinking as a residual of EV,
        EV-based vs equity-based multiple divergence, and drawdown divergence between
        EV and market-cap.

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


def _net_debt_wedge(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """ev - marketcap = implied net debt + minority interest + preferred."""
    return ev - marketcap


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): EV/MarketCap ratio and its levels ---

def evd_001_ev_to_mktcap_ratio(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Raw EV-to-market-cap ratio (>1 signals positive net debt; distress when ratio soars)."""
    return _safe_div(ev, marketcap)


def evd_002_mktcap_to_ev_ratio(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Equity-to-EV ratio (marketcap/ev); shrinks toward zero as equity becomes residual."""
    return _safe_div(marketcap, ev)


def evd_003_log_ev_to_mktcap_ratio(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Log of EV/marketcap ratio; linearizes the distortion signal."""
    ratio = _safe_div(ev, marketcap)
    return _log_safe(ratio.clip(lower=_EPS))


def evd_004_ev_to_mktcap_21d_avg(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day rolling mean of EV/marketcap ratio (smoothed monthly distortion)."""
    ratio = _safe_div(ev, marketcap)
    return _rolling_mean(ratio, _TD_MON)


def evd_005_ev_to_mktcap_63d_avg(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day rolling mean of EV/marketcap ratio (smoothed quarterly distortion)."""
    ratio = _safe_div(ev, marketcap)
    return _rolling_mean(ratio, _TD_QTR)


def evd_006_ev_to_mktcap_252d_avg(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day rolling mean of EV/marketcap ratio (annual average distortion)."""
    ratio = _safe_div(ev, marketcap)
    return _rolling_mean(ratio, _TD_YEAR)


def evd_007_ev_to_mktcap_expanding_avg(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Expanding (all-history) mean of EV/marketcap ratio."""
    ratio = _safe_div(ev, marketcap)
    return ratio.expanding(min_periods=1).mean()


def evd_008_ev_to_mktcap_252d_max(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day rolling maximum of EV/marketcap ratio (peak distortion in past year)."""
    ratio = _safe_div(ev, marketcap)
    return _rolling_max(ratio, _TD_YEAR)


def evd_009_ev_to_mktcap_252d_min(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day rolling minimum of EV/marketcap ratio (least distorted in past year)."""
    ratio = _safe_div(ev, marketcap)
    return _rolling_min(ratio, _TD_YEAR)


def evd_010_ev_to_mktcap_zscore_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day z-score of EV/marketcap ratio (how extreme vs own annual history)."""
    ratio = _safe_div(ev, marketcap)
    return _zscore_rolling(ratio, _TD_YEAR)


def evd_011_ev_to_mktcap_zscore_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day z-score of EV/marketcap ratio."""
    ratio = _safe_div(ev, marketcap)
    return _zscore_rolling(ratio, _TD_QTR)


def evd_012_ev_to_mktcap_expanding_zscore(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Expanding z-score of EV/marketcap ratio (all-history statistical extremity)."""
    ratio = _safe_div(ev, marketcap)
    m  = ratio.expanding(min_periods=5).mean()
    sd = ratio.expanding(min_periods=5).std()
    return _safe_div(ratio - m, sd)


def evd_013_ev_to_mktcap_pct_rank_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day percentile rank of EV/marketcap ratio."""
    ratio = _safe_div(ev, marketcap)
    return _rolling_rank_pct(ratio, _TD_YEAR)


def evd_014_ev_to_mktcap_pct_rank_1260d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """1260-day (5-year) percentile rank of EV/marketcap ratio."""
    ratio = _safe_div(ev, marketcap)
    return _rolling_rank_pct(ratio, 1260)


def evd_015_mktcap_to_ev_expanding_min(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Expanding minimum of equity-to-EV share (how thin has the equity slice been)."""
    ratio = _safe_div(marketcap, ev)
    return ratio.expanding(min_periods=1).min()


# --- Group B (016-030): Net-debt wedge (EV - marketcap) levels ---

def evd_016_net_debt_wedge_abs(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Absolute net-debt wedge: ev - marketcap (raw dollar size of debt burden)."""
    return _net_debt_wedge(ev, marketcap)


def evd_017_wedge_to_mktcap_ratio(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Wedge relative to marketcap: (ev - marketcap) / marketcap (leverage in cap terms)."""
    wedge = _net_debt_wedge(ev, marketcap)
    return _safe_div(wedge, marketcap)


def evd_018_wedge_to_ev_ratio(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Wedge relative to EV: (ev - marketcap) / ev (debt fraction of total enterprise)."""
    wedge = _net_debt_wedge(ev, marketcap)
    return _safe_div(wedge, ev)


def evd_019_wedge_to_mktcap_21d_avg(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day average of wedge/marketcap ratio."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return _rolling_mean(ratio, _TD_MON)


def evd_020_wedge_to_mktcap_63d_avg(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day average of wedge/marketcap ratio."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return _rolling_mean(ratio, _TD_QTR)


def evd_021_wedge_to_mktcap_252d_avg(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day average of wedge/marketcap ratio."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return _rolling_mean(ratio, _TD_YEAR)


def evd_022_wedge_to_mktcap_252d_max(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day max of wedge/marketcap ratio (worst leverage in the past year)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return _rolling_max(ratio, _TD_YEAR)


def evd_023_wedge_to_mktcap_zscore_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day z-score of wedge/marketcap ratio."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return _zscore_rolling(ratio, _TD_YEAR)


def evd_024_wedge_to_mktcap_pct_rank_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day percentile rank of wedge/marketcap ratio."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return _rolling_rank_pct(ratio, _TD_YEAR)


def evd_025_wedge_expanding_max(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Expanding max of wedge/marketcap ratio (historical peak leverage)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return ratio.expanding(min_periods=1).max()


def evd_026_wedge_to_mktcap_expanding_zscore(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Expanding z-score of wedge/marketcap ratio."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    m  = ratio.expanding(min_periods=5).mean()
    sd = ratio.expanding(min_periods=5).std()
    return _safe_div(ratio - m, sd)


def evd_027_log_wedge_to_mktcap(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Log of (1 + wedge/marketcap): log-space leverage measure (guards negative wedge)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return np.log1p(ratio.clip(lower=-1 + _EPS))


def evd_028_wedge_pos_flag(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Binary flag: 1 if ev > marketcap (positive net debt); 0 otherwise."""
    return (ev > marketcap).astype(float)


def evd_029_wedge_pos_fraction_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Fraction of past 252 days where ev > marketcap."""
    flag = evd_028_wedge_pos_flag(ev, marketcap)
    return _rolling_mean(flag, _TD_YEAR)


def evd_030_wedge_pos_fraction_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Fraction of past 63 days where ev > marketcap."""
    flag = evd_028_wedge_pos_flag(ev, marketcap)
    return _rolling_mean(flag, _TD_QTR)


# --- Group C (031-045): EV vs marketcap drawdown divergence ---

def evd_031_mktcap_dd_from_252d_high(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Marketcap drawdown from 252-day marketcap high."""
    h = _rolling_max(marketcap, _TD_YEAR)
    return _safe_div(marketcap - h, h)


def evd_032_ev_dd_from_252d_high(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EV drawdown from 252-day EV high."""
    h = _rolling_max(ev, _TD_YEAR)
    return _safe_div(ev - h, h)


def evd_033_dd_divergence_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Marketcap dd minus EV dd over 252 days (equity falls faster than EV = distress)."""
    mktcap_dd = evd_031_mktcap_dd_from_252d_high(ev, marketcap)
    ev_dd     = evd_032_ev_dd_from_252d_high(ev, marketcap)
    return mktcap_dd - ev_dd


def evd_034_dd_divergence_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Marketcap dd minus EV dd over 63 days."""
    mc_h = _rolling_max(marketcap, _TD_QTR)
    ev_h = _rolling_max(ev, _TD_QTR)
    mc_dd = _safe_div(marketcap - mc_h, mc_h)
    ev_dd = _safe_div(ev - ev_h, ev_h)
    return mc_dd - ev_dd


def evd_035_dd_divergence_504d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Marketcap dd minus EV dd over 504 days."""
    mc_h = _rolling_max(marketcap, 504)
    ev_h = _rolling_max(ev, 504)
    mc_dd = _safe_div(marketcap - mc_h, mc_h)
    ev_dd = _safe_div(ev - ev_h, ev_h)
    return mc_dd - ev_dd


def evd_036_mktcap_dd_from_ath(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Marketcap drawdown from all-time marketcap high."""
    h = marketcap.expanding(min_periods=1).max()
    return _safe_div(marketcap - h, h)


def evd_037_ev_dd_from_ath(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EV drawdown from all-time EV high."""
    h = ev.expanding(min_periods=1).max()
    return _safe_div(ev - h, h)


def evd_038_dd_divergence_ath(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """ATH marketcap dd minus ATH EV dd (equity wipeout vs enterprise wipeout)."""
    return evd_036_mktcap_dd_from_ath(ev, marketcap) - evd_037_ev_dd_from_ath(ev, marketcap)


def evd_039_mktcap_dd_zscore_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day z-score of marketcap dd (equity-only statistical extremity)."""
    dd = evd_031_mktcap_dd_from_252d_high(ev, marketcap)
    return _zscore_rolling(dd, _TD_YEAR)


def evd_040_ev_dd_zscore_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day z-score of EV dd (enterprise-level statistical extremity)."""
    dd = evd_032_ev_dd_from_252d_high(ev, marketcap)
    return _zscore_rolling(dd, _TD_YEAR)


def evd_041_dd_divergence_zscore_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day z-score of the EV-vs-equity dd divergence."""
    div = evd_033_dd_divergence_252d(ev, marketcap)
    return _zscore_rolling(div, _TD_YEAR)


def evd_042_mktcap_dd_rank_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day percentile rank of marketcap dd."""
    dd = evd_031_mktcap_dd_from_252d_high(ev, marketcap)
    return _rolling_rank_pct(dd, _TD_YEAR)


def evd_043_ev_recovery_while_mktcap_down(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Flag: EV improving (diff > 0) while marketcap worsening (diff < 0) — distress signal."""
    ev_up  = (ev.diff(5)  > 0).astype(float)
    mc_dn  = (marketcap.diff(5) < 0).astype(float)
    return ev_up * mc_dn


def evd_044_ev_recovery_while_mktcap_down_fraction_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day fraction of days where EV rises while marketcap falls."""
    flag = evd_043_ev_recovery_while_mktcap_down(ev, marketcap)
    return _rolling_mean(flag, _TD_QTR)


def evd_045_ev_recovery_while_mktcap_down_fraction_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day fraction of days where EV rises while marketcap falls."""
    flag = evd_043_ev_recovery_while_mktcap_down(ev, marketcap)
    return _rolling_mean(flag, _TD_YEAR)


# --- Group D (046-060): Multiple divergence (EV-based vs equity-based) ---

def evd_046_evebitda_vs_pe_ratio(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """EV/EBITDA divided by P/E: enterprise multiple vs equity multiple divergence."""
    return _safe_div(evebitda, pe)


def evd_047_evebit_vs_pe_ratio(evebit: pd.Series, pe: pd.Series) -> pd.Series:
    """EV/EBIT divided by P/E: EBIT-based enterprise vs equity multiple spread."""
    return _safe_div(evebit, pe)


def evd_048_evebitda_vs_pe_diff(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """EV/EBITDA minus P/E: raw multiple spread (enterprise premium over equity)."""
    return evebitda - pe


def evd_049_evebit_vs_pe_diff(evebit: pd.Series, pe: pd.Series) -> pd.Series:
    """EV/EBIT minus P/E: raw EBIT-multiple spread."""
    return evebit - pe


def evd_050_evebitda_to_pe_zscore_252d(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """252-day z-score of EV/EBITDA-to-P/E ratio."""
    ratio = _safe_div(evebitda, pe)
    return _zscore_rolling(ratio, _TD_YEAR)


def evd_051_evebit_to_pe_zscore_252d(evebit: pd.Series, pe: pd.Series) -> pd.Series:
    """252-day z-score of EV/EBIT-to-P/E ratio."""
    ratio = _safe_div(evebit, pe)
    return _zscore_rolling(ratio, _TD_YEAR)


def evd_052_evebitda_to_pe_252d_avg(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """252-day rolling mean of EV/EBITDA-to-P/E ratio."""
    ratio = _safe_div(evebitda, pe)
    return _rolling_mean(ratio, _TD_YEAR)


def evd_053_evebitda_to_pe_pct_rank_252d(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """252-day percentile rank of EV/EBITDA-to-P/E ratio."""
    ratio = _safe_div(evebitda, pe)
    return _rolling_rank_pct(ratio, _TD_YEAR)


def evd_054_pe_to_evebitda_ratio(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """P/E divided by EV/EBITDA: inverse ratio (equity cheap vs enterprise)."""
    return _safe_div(pe, evebitda)


def evd_055_evebitda_zscore_252d(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """252-day z-score of raw EV/EBITDA level."""
    return _zscore_rolling(evebitda, _TD_YEAR)


def evd_056_evebit_zscore_252d(evebit: pd.Series, pe: pd.Series) -> pd.Series:
    """252-day z-score of raw EV/EBIT level."""
    return _zscore_rolling(evebit, _TD_YEAR)


def evd_057_pe_zscore_252d(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """252-day z-score of raw P/E level (equity-multiple context)."""
    return _zscore_rolling(pe, _TD_YEAR)


def evd_058_multiple_gap_evebitda_pe_pct_rank_252d(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """252-day pct-rank of the raw EV/EBITDA - P/E spread."""
    diff = evebitda - pe
    return _rolling_rank_pct(diff, _TD_YEAR)


def evd_059_evebitda_ath_drawdown(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """EV/EBITDA drawdown from all-time high (enterprise multiple compression)."""
    h = evebitda.expanding(min_periods=1).max()
    return _safe_div(evebitda - h, h.replace(0, np.nan).abs())


def evd_060_evebit_ath_drawdown(evebit: pd.Series, pe: pd.Series) -> pd.Series:
    """EV/EBIT drawdown from all-time high."""
    h = evebit.expanding(min_periods=1).max()
    return _safe_div(evebit - h, h.replace(0, np.nan).abs())


# --- Group E (061-075): Equity-as-option, composite distortion, and EWM signals ---

def evd_061_equity_option_proxy(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Equity-option proxy: max(marketcap/ev, 0) as a ratio bounded at zero."""
    ratio = _safe_div(marketcap, ev)
    return ratio.clip(lower=0)


def evd_062_equity_option_decay_21d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day change in equity/EV share (rate of equity-slice erosion)."""
    ratio = _safe_div(marketcap, ev)
    return ratio.diff(_TD_MON)


def evd_063_equity_option_decay_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day change in equity/EV share."""
    ratio = _safe_div(marketcap, ev)
    return ratio.diff(_TD_QTR)


def evd_064_equity_option_decay_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day change in equity/EV share."""
    ratio = _safe_div(marketcap, ev)
    return ratio.diff(_TD_YEAR)


def evd_065_ewm_ev_to_mktcap_21(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day EWM of EV/marketcap ratio (fast signal for trend)."""
    ratio = _safe_div(ev, marketcap)
    return _ewm_mean(ratio, _TD_MON)


def evd_066_ewm_ev_to_mktcap_63(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day EWM of EV/marketcap ratio."""
    ratio = _safe_div(ev, marketcap)
    return _ewm_mean(ratio, _TD_QTR)


def evd_067_ewm_ev_to_mktcap_252(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day EWM of EV/marketcap ratio (slow trend)."""
    ratio = _safe_div(ev, marketcap)
    return _ewm_mean(ratio, _TD_YEAR)


def evd_068_ewm_wedge_ratio_21(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day EWM of wedge/marketcap ratio."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return _ewm_mean(ratio, _TD_MON)


def evd_069_ewm_wedge_ratio_63(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day EWM of wedge/marketcap ratio."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return _ewm_mean(ratio, _TD_QTR)


def evd_070_composite_distortion_score(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Composite distortion: z-score of (ev/mktcap ratio) + z-score of (wedge/mktcap ratio), scaled."""
    z1 = _zscore_rolling(_safe_div(ev, marketcap), _TD_YEAR)
    z2 = _zscore_rolling(_safe_div(_net_debt_wedge(ev, marketcap), marketcap), _TD_YEAR)
    return (z1 + z2) / 2.0


def evd_071_ev_to_mktcap_vs_own_21d_sma(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EV/mktcap ratio deviation from its own 21-day SMA."""
    ratio = _safe_div(ev, marketcap)
    sma   = _rolling_mean(ratio, _TD_MON)
    return _safe_div(ratio - sma, sma)


def evd_072_ev_to_mktcap_vs_own_252d_sma(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EV/mktcap ratio deviation from its own 252-day SMA."""
    ratio = _safe_div(ev, marketcap)
    sma   = _rolling_mean(ratio, _TD_YEAR)
    return _safe_div(ratio - sma, sma)


def evd_073_wedge_ratio_vol_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day rolling std of wedge/marketcap ratio (instability of leverage ratio)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return _rolling_std(ratio, _TD_YEAR)


def evd_074_equity_share_below_threshold_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Fraction of past 252 days where equity/EV share < 0.3 (thin equity residual)."""
    ratio = _safe_div(marketcap, ev)
    flag  = (ratio < 0.3).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def evd_075_equity_share_below_threshold_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Fraction of past 63 days where equity/EV share < 0.3."""
    ratio = _safe_div(marketcap, ev)
    flag  = (ratio < 0.3).astype(float)
    return _rolling_mean(flag, _TD_QTR)


# --- Group F (151-175): Additional windows, distributional stats, cross-ratio, and composite ---

def evd_151_ev_to_mktcap_ratio_10d_avg(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """10-day rolling mean of EV/marketcap ratio (bi-weekly smoothed distortion)."""
    ratio = _safe_div(ev, marketcap)
    return _rolling_mean(ratio, 10)


def evd_152_ev_to_mktcap_ratio_126d_avg(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """126-day rolling mean of EV/marketcap ratio (semi-annual average distortion)."""
    ratio = _safe_div(ev, marketcap)
    return _rolling_mean(ratio, _TD_HALF)


def evd_153_wedge_to_mktcap_126d_avg(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """126-day rolling mean of wedge/marketcap ratio (semi-annual leverage average)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return _rolling_mean(ratio, _TD_HALF)


def evd_154_wedge_to_ev_126d_avg(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """126-day rolling mean of wedge/EV ratio (semi-annual debt fraction of enterprise)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), ev)
    return _rolling_mean(ratio, _TD_HALF)


def evd_155_ev_to_mktcap_ratio_vol_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day rolling std of EV/marketcap ratio (quarterly distortion volatility)."""
    ratio = _safe_div(ev, marketcap)
    return _rolling_std(ratio, _TD_QTR)


def evd_156_wedge_to_mktcap_vol_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day rolling std of wedge/marketcap ratio (quarterly leverage instability)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return _rolling_std(ratio, _TD_QTR)


def evd_157_ev_to_mktcap_ratio_skew_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day rolling skewness of EV/mktcap ratio (tail asymmetry of distortion)."""
    ratio = _safe_div(ev, marketcap)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).skew()


def evd_158_wedge_to_mktcap_q05_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day 5th percentile of wedge/mktcap (best-case leverage tail)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.05)


def evd_159_ev_to_mktcap_range_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day range of EV/mktcap ratio (max - min; annual distortion bandwidth)."""
    ratio = _safe_div(ev, marketcap)
    return _rolling_max(ratio, _TD_YEAR) - _rolling_min(ratio, _TD_YEAR)


def evd_160_ev_to_mktcap_pos_in_252d_range(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EV/mktcap position within 252-day range (0=trough, 1=peak distortion)."""
    ratio = _safe_div(ev, marketcap)
    hi = _rolling_max(ratio, _TD_YEAR)
    lo = _rolling_min(ratio, _TD_YEAR)
    return _safe_div(ratio - lo, hi - lo)


def evd_161_equity_share_q05_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day 5th percentile of equity/EV share (thinnest residual equity tail)."""
    ratio = _safe_div(marketcap, ev)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.05)


def evd_162_equity_share_q95_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day 95th percentile of equity/EV share (fattest residual equity tail)."""
    ratio = _safe_div(marketcap, ev)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.95)


def evd_163_wedge_pos_fraction_126d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Fraction of past 126 days where ev > marketcap (semi-annual positive net debt)."""
    flag = (ev > marketcap).astype(float)
    return _rolling_mean(flag, _TD_HALF)


def evd_164_ev_to_mktcap_above_4x_fraction_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Fraction of past 252 days where EV/mktcap > 4 (near-zero equity persistence)."""
    ratio = _safe_div(ev, marketcap)
    flag  = (ratio > 4.0).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def evd_165_mktcap_to_ev_below_10pct_flag(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Binary flag: equity/EV below 10% (deeply subordinated equity)."""
    ratio = _safe_div(marketcap, ev)
    return (ratio < 0.1).astype(float)


def evd_166_mktcap_to_ev_below_10pct_fraction_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Fraction of past 252 days where equity/EV < 10% (persistent deep subordination)."""
    flag = evd_165_mktcap_to_ev_below_10pct_flag(ev, marketcap)
    return _rolling_mean(flag, _TD_YEAR)


def evd_167_evebitda_to_pe_ewm_diff_21_63(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """EWM(21) minus EWM(63) of EV/EBITDA-to-P/E ratio (fast-slow multiple-gap trend)."""
    ratio = _safe_div(evebitda, pe)
    return _ewm_mean(ratio, _TD_MON) - _ewm_mean(ratio, _TD_QTR)


def evd_168_evebit_to_pe_21d_avg(evebit: pd.Series, pe: pd.Series) -> pd.Series:
    """21-day rolling mean of EV/EBIT-to-P/E ratio (smoothed EBIT multiple gap)."""
    ratio = _safe_div(evebit, pe)
    return _rolling_mean(ratio, _TD_MON)


def evd_169_evebitda_to_evebit_pct_rank_252d(evebit: pd.Series, evebitda: pd.Series) -> pd.Series:
    """252-day pct-rank of EV/EBITDA-to-EV/EBIT ratio (DA-burden extremity rank)."""
    ratio = _safe_div(evebitda, evebit)
    return _rolling_rank_pct(ratio, _TD_YEAR)


def evd_170_log_wedge_to_ev(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Log of (1 + wedge/EV): log-space debt-fraction of enterprise."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), ev)
    return np.log1p(ratio.clip(lower=-1 + _EPS))


def evd_171_ev_to_mktcap_ewm_126(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """126-day EWM of EV/marketcap ratio (semi-annual slow signal)."""
    ratio = _safe_div(ev, marketcap)
    return _ewm_mean(ratio, _TD_HALF)


def evd_172_wedge_to_mktcap_ewm_126(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """126-day EWM of wedge/marketcap ratio."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return _ewm_mean(ratio, _TD_HALF)


def evd_173_ev_to_mktcap_ewm_diff_21_126(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EWM(21) minus EWM(126) of EV/mktcap ratio (fast-semi-annual trend gap)."""
    ratio = _safe_div(ev, marketcap)
    return _ewm_mean(ratio, _TD_MON) - _ewm_mean(ratio, _TD_HALF)


def evd_174_ev_to_mktcap_vs_own_63d_sma(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """EV/mktcap ratio deviation from its own 63-day SMA."""
    ratio = _safe_div(ev, marketcap)
    sma   = _rolling_mean(ratio, _TD_QTR)
    return _safe_div(ratio - sma, sma)


def evd_175_composite_distortion_score_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day composite distortion: avg of z-scores of (ev/mktcap) and (wedge/mktcap)."""
    z1 = _zscore_rolling(_safe_div(ev, marketcap), _TD_QTR)
    z2 = _zscore_rolling(_safe_div(_net_debt_wedge(ev, marketcap), marketcap), _TD_QTR)
    return (z1 + z2) / 2.0


# ── Registry ──────────────────────────────────────────────────────────────────

EV_DISTORTION_REGISTRY_001_075 = {
    "evd_001_ev_to_mktcap_ratio":                       {"inputs": ["ev", "marketcap"], "func": evd_001_ev_to_mktcap_ratio},
    "evd_002_mktcap_to_ev_ratio":                       {"inputs": ["ev", "marketcap"], "func": evd_002_mktcap_to_ev_ratio},
    "evd_003_log_ev_to_mktcap_ratio":                   {"inputs": ["ev", "marketcap"], "func": evd_003_log_ev_to_mktcap_ratio},
    "evd_004_ev_to_mktcap_21d_avg":                     {"inputs": ["ev", "marketcap"], "func": evd_004_ev_to_mktcap_21d_avg},
    "evd_005_ev_to_mktcap_63d_avg":                     {"inputs": ["ev", "marketcap"], "func": evd_005_ev_to_mktcap_63d_avg},
    "evd_006_ev_to_mktcap_252d_avg":                    {"inputs": ["ev", "marketcap"], "func": evd_006_ev_to_mktcap_252d_avg},
    "evd_007_ev_to_mktcap_expanding_avg":               {"inputs": ["ev", "marketcap"], "func": evd_007_ev_to_mktcap_expanding_avg},
    "evd_008_ev_to_mktcap_252d_max":                    {"inputs": ["ev", "marketcap"], "func": evd_008_ev_to_mktcap_252d_max},
    "evd_009_ev_to_mktcap_252d_min":                    {"inputs": ["ev", "marketcap"], "func": evd_009_ev_to_mktcap_252d_min},
    "evd_010_ev_to_mktcap_zscore_252d":                 {"inputs": ["ev", "marketcap"], "func": evd_010_ev_to_mktcap_zscore_252d},
    "evd_011_ev_to_mktcap_zscore_63d":                  {"inputs": ["ev", "marketcap"], "func": evd_011_ev_to_mktcap_zscore_63d},
    "evd_012_ev_to_mktcap_expanding_zscore":            {"inputs": ["ev", "marketcap"], "func": evd_012_ev_to_mktcap_expanding_zscore},
    "evd_013_ev_to_mktcap_pct_rank_252d":               {"inputs": ["ev", "marketcap"], "func": evd_013_ev_to_mktcap_pct_rank_252d},
    "evd_014_ev_to_mktcap_pct_rank_1260d":              {"inputs": ["ev", "marketcap"], "func": evd_014_ev_to_mktcap_pct_rank_1260d},
    "evd_015_mktcap_to_ev_expanding_min":               {"inputs": ["ev", "marketcap"], "func": evd_015_mktcap_to_ev_expanding_min},
    "evd_016_net_debt_wedge_abs":                       {"inputs": ["ev", "marketcap"], "func": evd_016_net_debt_wedge_abs},
    "evd_017_wedge_to_mktcap_ratio":                    {"inputs": ["ev", "marketcap"], "func": evd_017_wedge_to_mktcap_ratio},
    "evd_018_wedge_to_ev_ratio":                        {"inputs": ["ev", "marketcap"], "func": evd_018_wedge_to_ev_ratio},
    "evd_019_wedge_to_mktcap_21d_avg":                  {"inputs": ["ev", "marketcap"], "func": evd_019_wedge_to_mktcap_21d_avg},
    "evd_020_wedge_to_mktcap_63d_avg":                  {"inputs": ["ev", "marketcap"], "func": evd_020_wedge_to_mktcap_63d_avg},
    "evd_021_wedge_to_mktcap_252d_avg":                 {"inputs": ["ev", "marketcap"], "func": evd_021_wedge_to_mktcap_252d_avg},
    "evd_022_wedge_to_mktcap_252d_max":                 {"inputs": ["ev", "marketcap"], "func": evd_022_wedge_to_mktcap_252d_max},
    "evd_023_wedge_to_mktcap_zscore_252d":              {"inputs": ["ev", "marketcap"], "func": evd_023_wedge_to_mktcap_zscore_252d},
    "evd_024_wedge_to_mktcap_pct_rank_252d":            {"inputs": ["ev", "marketcap"], "func": evd_024_wedge_to_mktcap_pct_rank_252d},
    "evd_025_wedge_expanding_max":                      {"inputs": ["ev", "marketcap"], "func": evd_025_wedge_expanding_max},
    "evd_026_wedge_to_mktcap_expanding_zscore":         {"inputs": ["ev", "marketcap"], "func": evd_026_wedge_to_mktcap_expanding_zscore},
    "evd_027_log_wedge_to_mktcap":                      {"inputs": ["ev", "marketcap"], "func": evd_027_log_wedge_to_mktcap},
    "evd_028_wedge_pos_flag":                           {"inputs": ["ev", "marketcap"], "func": evd_028_wedge_pos_flag},
    "evd_029_wedge_pos_fraction_252d":                  {"inputs": ["ev", "marketcap"], "func": evd_029_wedge_pos_fraction_252d},
    "evd_030_wedge_pos_fraction_63d":                   {"inputs": ["ev", "marketcap"], "func": evd_030_wedge_pos_fraction_63d},
    "evd_031_mktcap_dd_from_252d_high":                 {"inputs": ["ev", "marketcap"], "func": evd_031_mktcap_dd_from_252d_high},
    "evd_032_ev_dd_from_252d_high":                     {"inputs": ["ev", "marketcap"], "func": evd_032_ev_dd_from_252d_high},
    "evd_033_dd_divergence_252d":                       {"inputs": ["ev", "marketcap"], "func": evd_033_dd_divergence_252d},
    "evd_034_dd_divergence_63d":                        {"inputs": ["ev", "marketcap"], "func": evd_034_dd_divergence_63d},
    "evd_035_dd_divergence_504d":                       {"inputs": ["ev", "marketcap"], "func": evd_035_dd_divergence_504d},
    "evd_036_mktcap_dd_from_ath":                       {"inputs": ["ev", "marketcap"], "func": evd_036_mktcap_dd_from_ath},
    "evd_037_ev_dd_from_ath":                           {"inputs": ["ev", "marketcap"], "func": evd_037_ev_dd_from_ath},
    "evd_038_dd_divergence_ath":                        {"inputs": ["ev", "marketcap"], "func": evd_038_dd_divergence_ath},
    "evd_039_mktcap_dd_zscore_252d":                    {"inputs": ["ev", "marketcap"], "func": evd_039_mktcap_dd_zscore_252d},
    "evd_040_ev_dd_zscore_252d":                        {"inputs": ["ev", "marketcap"], "func": evd_040_ev_dd_zscore_252d},
    "evd_041_dd_divergence_zscore_252d":                {"inputs": ["ev", "marketcap"], "func": evd_041_dd_divergence_zscore_252d},
    "evd_042_mktcap_dd_rank_252d":                      {"inputs": ["ev", "marketcap"], "func": evd_042_mktcap_dd_rank_252d},
    "evd_043_ev_recovery_while_mktcap_down":            {"inputs": ["ev", "marketcap"], "func": evd_043_ev_recovery_while_mktcap_down},
    "evd_044_ev_recovery_while_mktcap_down_fraction_63d":  {"inputs": ["ev", "marketcap"], "func": evd_044_ev_recovery_while_mktcap_down_fraction_63d},
    "evd_045_ev_recovery_while_mktcap_down_fraction_252d": {"inputs": ["ev", "marketcap"], "func": evd_045_ev_recovery_while_mktcap_down_fraction_252d},
    "evd_046_evebitda_vs_pe_ratio":                     {"inputs": ["evebitda", "pe"], "func": evd_046_evebitda_vs_pe_ratio},
    "evd_047_evebit_vs_pe_ratio":                       {"inputs": ["evebit", "pe"],   "func": evd_047_evebit_vs_pe_ratio},
    "evd_048_evebitda_vs_pe_diff":                      {"inputs": ["evebitda", "pe"], "func": evd_048_evebitda_vs_pe_diff},
    "evd_049_evebit_vs_pe_diff":                        {"inputs": ["evebit", "pe"],   "func": evd_049_evebit_vs_pe_diff},
    "evd_050_evebitda_to_pe_zscore_252d":               {"inputs": ["evebitda", "pe"], "func": evd_050_evebitda_to_pe_zscore_252d},
    "evd_051_evebit_to_pe_zscore_252d":                 {"inputs": ["evebit", "pe"],   "func": evd_051_evebit_to_pe_zscore_252d},
    "evd_052_evebitda_to_pe_252d_avg":                  {"inputs": ["evebitda", "pe"], "func": evd_052_evebitda_to_pe_252d_avg},
    "evd_053_evebitda_to_pe_pct_rank_252d":             {"inputs": ["evebitda", "pe"], "func": evd_053_evebitda_to_pe_pct_rank_252d},
    "evd_054_pe_to_evebitda_ratio":                     {"inputs": ["evebitda", "pe"], "func": evd_054_pe_to_evebitda_ratio},
    "evd_055_evebitda_zscore_252d":                     {"inputs": ["evebitda", "pe"], "func": evd_055_evebitda_zscore_252d},
    "evd_056_evebit_zscore_252d":                       {"inputs": ["evebit", "pe"],   "func": evd_056_evebit_zscore_252d},
    "evd_057_pe_zscore_252d":                           {"inputs": ["evebitda", "pe"], "func": evd_057_pe_zscore_252d},
    "evd_058_multiple_gap_evebitda_pe_pct_rank_252d":   {"inputs": ["evebitda", "pe"], "func": evd_058_multiple_gap_evebitda_pe_pct_rank_252d},
    "evd_059_evebitda_ath_drawdown":                    {"inputs": ["evebitda", "pe"], "func": evd_059_evebitda_ath_drawdown},
    "evd_060_evebit_ath_drawdown":                      {"inputs": ["evebit", "pe"],   "func": evd_060_evebit_ath_drawdown},
    "evd_061_equity_option_proxy":                      {"inputs": ["ev", "marketcap"], "func": evd_061_equity_option_proxy},
    "evd_062_equity_option_decay_21d":                  {"inputs": ["ev", "marketcap"], "func": evd_062_equity_option_decay_21d},
    "evd_063_equity_option_decay_63d":                  {"inputs": ["ev", "marketcap"], "func": evd_063_equity_option_decay_63d},
    "evd_064_equity_option_decay_252d":                 {"inputs": ["ev", "marketcap"], "func": evd_064_equity_option_decay_252d},
    "evd_065_ewm_ev_to_mktcap_21":                      {"inputs": ["ev", "marketcap"], "func": evd_065_ewm_ev_to_mktcap_21},
    "evd_066_ewm_ev_to_mktcap_63":                      {"inputs": ["ev", "marketcap"], "func": evd_066_ewm_ev_to_mktcap_63},
    "evd_067_ewm_ev_to_mktcap_252":                     {"inputs": ["ev", "marketcap"], "func": evd_067_ewm_ev_to_mktcap_252},
    "evd_068_ewm_wedge_ratio_21":                       {"inputs": ["ev", "marketcap"], "func": evd_068_ewm_wedge_ratio_21},
    "evd_069_ewm_wedge_ratio_63":                       {"inputs": ["ev", "marketcap"], "func": evd_069_ewm_wedge_ratio_63},
    "evd_070_composite_distortion_score":               {"inputs": ["ev", "marketcap"], "func": evd_070_composite_distortion_score},
    "evd_071_ev_to_mktcap_vs_own_21d_sma":             {"inputs": ["ev", "marketcap"], "func": evd_071_ev_to_mktcap_vs_own_21d_sma},
    "evd_072_ev_to_mktcap_vs_own_252d_sma":            {"inputs": ["ev", "marketcap"], "func": evd_072_ev_to_mktcap_vs_own_252d_sma},
    "evd_073_wedge_ratio_vol_252d":                     {"inputs": ["ev", "marketcap"], "func": evd_073_wedge_ratio_vol_252d},
    "evd_074_equity_share_below_threshold_252d":        {"inputs": ["ev", "marketcap"], "func": evd_074_equity_share_below_threshold_252d},
    "evd_075_equity_share_below_threshold_63d":         {"inputs": ["ev", "marketcap"], "func": evd_075_equity_share_below_threshold_63d},
    "evd_151_ev_to_mktcap_ratio_10d_avg":               {"inputs": ["ev", "marketcap"], "func": evd_151_ev_to_mktcap_ratio_10d_avg},
    "evd_152_ev_to_mktcap_ratio_126d_avg":              {"inputs": ["ev", "marketcap"], "func": evd_152_ev_to_mktcap_ratio_126d_avg},
    "evd_153_wedge_to_mktcap_126d_avg":                 {"inputs": ["ev", "marketcap"], "func": evd_153_wedge_to_mktcap_126d_avg},
    "evd_154_wedge_to_ev_126d_avg":                     {"inputs": ["ev", "marketcap"], "func": evd_154_wedge_to_ev_126d_avg},
    "evd_155_ev_to_mktcap_ratio_vol_63d":               {"inputs": ["ev", "marketcap"], "func": evd_155_ev_to_mktcap_ratio_vol_63d},
    "evd_156_wedge_to_mktcap_vol_63d":                  {"inputs": ["ev", "marketcap"], "func": evd_156_wedge_to_mktcap_vol_63d},
    "evd_157_ev_to_mktcap_ratio_skew_252d":             {"inputs": ["ev", "marketcap"], "func": evd_157_ev_to_mktcap_ratio_skew_252d},
    "evd_158_wedge_to_mktcap_q05_252d":                 {"inputs": ["ev", "marketcap"], "func": evd_158_wedge_to_mktcap_q05_252d},
    "evd_159_ev_to_mktcap_range_252d":                  {"inputs": ["ev", "marketcap"], "func": evd_159_ev_to_mktcap_range_252d},
    "evd_160_ev_to_mktcap_pos_in_252d_range":           {"inputs": ["ev", "marketcap"], "func": evd_160_ev_to_mktcap_pos_in_252d_range},
    "evd_161_equity_share_q05_252d":                    {"inputs": ["ev", "marketcap"], "func": evd_161_equity_share_q05_252d},
    "evd_162_equity_share_q95_252d":                    {"inputs": ["ev", "marketcap"], "func": evd_162_equity_share_q95_252d},
    "evd_163_wedge_pos_fraction_126d":                  {"inputs": ["ev", "marketcap"], "func": evd_163_wedge_pos_fraction_126d},
    "evd_164_ev_to_mktcap_above_4x_fraction_252d":      {"inputs": ["ev", "marketcap"], "func": evd_164_ev_to_mktcap_above_4x_fraction_252d},
    "evd_165_mktcap_to_ev_below_10pct_flag":            {"inputs": ["ev", "marketcap"], "func": evd_165_mktcap_to_ev_below_10pct_flag},
    "evd_166_mktcap_to_ev_below_10pct_fraction_252d":   {"inputs": ["ev", "marketcap"], "func": evd_166_mktcap_to_ev_below_10pct_fraction_252d},
    "evd_167_evebitda_to_pe_ewm_diff_21_63":            {"inputs": ["evebitda", "pe"],  "func": evd_167_evebitda_to_pe_ewm_diff_21_63},
    "evd_168_evebit_to_pe_21d_avg":                     {"inputs": ["evebit", "pe"],    "func": evd_168_evebit_to_pe_21d_avg},
    "evd_169_evebitda_to_evebit_pct_rank_252d":         {"inputs": ["evebit", "evebitda"], "func": evd_169_evebitda_to_evebit_pct_rank_252d},
    "evd_170_log_wedge_to_ev":                          {"inputs": ["ev", "marketcap"], "func": evd_170_log_wedge_to_ev},
    "evd_171_ev_to_mktcap_ewm_126":                     {"inputs": ["ev", "marketcap"], "func": evd_171_ev_to_mktcap_ewm_126},
    "evd_172_wedge_to_mktcap_ewm_126":                  {"inputs": ["ev", "marketcap"], "func": evd_172_wedge_to_mktcap_ewm_126},
    "evd_173_ev_to_mktcap_ewm_diff_21_126":             {"inputs": ["ev", "marketcap"], "func": evd_173_ev_to_mktcap_ewm_diff_21_126},
    "evd_174_ev_to_mktcap_vs_own_63d_sma":              {"inputs": ["ev", "marketcap"], "func": evd_174_ev_to_mktcap_vs_own_63d_sma},
    "evd_175_composite_distortion_score_63d":           {"inputs": ["ev", "marketcap"], "func": evd_175_composite_distortion_score_63d},
}
