"""
79_ev_distortion — 2nd Derivatives (Features evd_drv2_001-075)
Domain: rate-of-change of base EV-distortion concepts — velocity, slope, and
        percent-change of the EV/marketcap ratio, wedge ratio, multiple spreads,
        and drawdown-divergence signals defined in the base files.

Inputs: daily-frequency Sharadar DAILY/METRICS valuation fields only.
        Canonical field names (lowercase): marketcap, ev, pe, pb, ps, evebit, evebitda, divyield.
        NO raw price/volume. NO quarterly forward-fill alignment helper needed.

All feature functions are strictly backward-looking: no negative shifts, no forward fills,
no .iloc[i+n] look-ahead. Each function computes a .diff(n), slope, or pct_change of a
base-layer concept.
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
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def evd_drv2_001_ev_to_mktcap_ratio_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of EV/mktcap ratio — velocity of distortion at weekly resolution."""
    ratio = _safe_div(ev, marketcap)
    return ratio.diff(5)


def evd_drv2_002_ev_to_mktcap_ratio_21d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day diff of EV/mktcap ratio — monthly drift in distortion level."""
    ratio = _safe_div(ev, marketcap)
    return ratio.diff(_TD_MON)


def evd_drv2_003_wedge_to_mktcap_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of wedge/mktcap ratio — weekly velocity of leverage build-up."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return ratio.diff(5)


def evd_drv2_004_wedge_to_mktcap_21d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day diff of wedge/mktcap ratio — monthly leverage drift."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return ratio.diff(_TD_MON)


def evd_drv2_005_mktcap_to_ev_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of equity/EV share — velocity of equity-slice erosion."""
    ratio = _safe_div(marketcap, ev)
    return ratio.diff(5)


def evd_drv2_006_mktcap_to_ev_21d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day diff of equity/EV share — monthly erosion of equity residual."""
    ratio = _safe_div(marketcap, ev)
    return ratio.diff(_TD_MON)


def evd_drv2_007_dd_divergence_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 252-day mktcap-vs-EV drawdown divergence (acceleration of split)."""
    mc_h  = _rolling_max(marketcap, _TD_YEAR)
    ev_h  = _rolling_max(ev, _TD_YEAR)
    mc_dd = _safe_div(marketcap - mc_h, mc_h)
    ev_dd = _safe_div(ev - ev_h, ev_h)
    div   = mc_dd - ev_dd
    return div.diff(5)


def evd_drv2_008_dd_divergence_21d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day diff of 252-day drawdown divergence (monthly acceleration of split)."""
    mc_h  = _rolling_max(marketcap, _TD_YEAR)
    ev_h  = _rolling_max(ev, _TD_YEAR)
    mc_dd = _safe_div(marketcap - mc_h, mc_h)
    ev_dd = _safe_div(ev - ev_h, ev_h)
    div   = mc_dd - ev_dd
    return div.diff(_TD_MON)


def evd_drv2_009_ev_to_mktcap_ratio_21d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """OLS slope of EV/mktcap ratio over 21 days (short-term linear trend of distortion)."""
    ratio = _safe_div(ev, marketcap)
    return _linslope(ratio, _TD_MON)


def evd_drv2_010_ev_to_mktcap_ratio_63d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """OLS slope of EV/mktcap ratio over 63 days (quarterly linear trend)."""
    ratio = _safe_div(ev, marketcap)
    return _linslope(ratio, _TD_QTR)


def evd_drv2_011_evebitda_vs_pe_ratio_5d_diff(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """5-day diff of EV/EBITDA-to-P/E ratio (velocity of enterprise vs equity multiple gap)."""
    ratio = _safe_div(evebitda, pe)
    return ratio.diff(5)


def evd_drv2_012_evebitda_vs_pe_ratio_21d_diff(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """21-day diff of EV/EBITDA-to-P/E ratio (monthly multiple gap drift)."""
    ratio = _safe_div(evebitda, pe)
    return ratio.diff(_TD_MON)


def evd_drv2_013_evebit_vs_pe_ratio_5d_diff(evebit: pd.Series, pe: pd.Series) -> pd.Series:
    """5-day diff of EV/EBIT-to-P/E ratio (EBIT-based velocity)."""
    ratio = _safe_div(evebit, pe)
    return ratio.diff(5)


def evd_drv2_014_log_ev_to_mktcap_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of log(EV/mktcap) — log-space velocity of distortion."""
    log_ratio = _log_safe(_safe_div(ev, marketcap).clip(lower=_EPS))
    return log_ratio.diff(5)


def evd_drv2_015_log_ev_to_mktcap_21d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day diff of log(EV/mktcap) — log-space monthly distortion velocity."""
    log_ratio = _log_safe(_safe_div(ev, marketcap).clip(lower=_EPS))
    return log_ratio.diff(_TD_MON)


def evd_drv2_016_ev_to_mktcap_zscore_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 252-day z-score of EV/mktcap (acceleration of statistical extremity)."""
    ratio = _safe_div(ev, marketcap)
    z     = _zscore_rolling(ratio, _TD_YEAR)
    return z.diff(5)


def evd_drv2_017_wedge_ratio_zscore_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 252-day z-score of wedge/mktcap (leverage extremity acceleration)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    z     = _zscore_rolling(ratio, _TD_YEAR)
    return z.diff(5)


def evd_drv2_018_mktcap_to_ev_21d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """OLS slope of equity/EV share over 21 days (trend in equity-residual shrinkage)."""
    ratio = _safe_div(marketcap, ev)
    return _linslope(ratio, _TD_MON)


def evd_drv2_019_mktcap_to_ev_63d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """OLS slope of equity/EV share over 63 days (quarterly slope of erosion)."""
    ratio = _safe_div(marketcap, ev)
    return _linslope(ratio, _TD_QTR)


def evd_drv2_020_ev_to_mktcap_5d_pct_change(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day percent change in EV/mktcap ratio (relative weekly velocity)."""
    ratio = _safe_div(ev, marketcap)
    return ratio.pct_change(5)


def evd_drv2_021_ev_to_mktcap_21d_pct_change(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day percent change in EV/mktcap ratio (relative monthly velocity)."""
    ratio = _safe_div(ev, marketcap)
    return ratio.pct_change(_TD_MON)


def evd_drv2_022_evebitda_21d_slope(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """OLS slope of EV/EBITDA over 21 days (short-term enterprise multiple trend)."""
    return _linslope(evebitda, _TD_MON)


def evd_drv2_023_composite_distortion_5d_diff(ev: pd.Series, marketcap: pd.Series, evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """5-day diff of composite distortion z-score (ev/mktcap z + wedge z + evebitda/pe z)/3."""
    z1 = _zscore_rolling(_safe_div(ev, marketcap), _TD_YEAR)
    z2 = _zscore_rolling(_safe_div(ev - marketcap, marketcap), _TD_YEAR)
    z3 = _zscore_rolling(_safe_div(evebitda, pe), _TD_YEAR)
    composite = (z1 + z2 + z3) / 3.0
    return composite.diff(5)


def evd_drv2_024_wedge_to_mktcap_pct_change_21d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day pct change of wedge/mktcap ratio (relative monthly leverage drift)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return ratio.pct_change(_TD_MON)


def evd_drv2_025_equity_share_21d_pct_change(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day pct change of equity/EV share (relative monthly erosion rate of equity residual)."""
    ratio = _safe_div(marketcap, ev)
    return ratio.pct_change(_TD_MON)


# ── 2nd-Derivative Feature Functions 026-075 ─────────────────────────────────

def evd_drv2_026_ev_to_mktcap_63d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day diff of EV/mktcap ratio — quarterly velocity of distortion."""
    ratio = _safe_div(ev, marketcap)
    return ratio.diff(_TD_QTR)


def evd_drv2_027_ev_to_mktcap_63d_pct_change(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day pct change of EV/mktcap ratio — relative quarterly velocity."""
    ratio = _safe_div(ev, marketcap)
    return ratio.pct_change(_TD_QTR)


def evd_drv2_028_wedge_to_mktcap_63d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day diff of wedge/mktcap ratio — quarterly leverage drift."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return ratio.diff(_TD_QTR)


def evd_drv2_029_wedge_to_mktcap_63d_pct_change(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day pct change of wedge/mktcap ratio — relative quarterly leverage drift."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return ratio.pct_change(_TD_QTR)


def evd_drv2_030_mktcap_to_ev_63d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day diff of equity/EV share — quarterly erosion of equity residual."""
    ratio = _safe_div(marketcap, ev)
    return ratio.diff(_TD_QTR)


def evd_drv2_031_mktcap_to_ev_63d_pct_change(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day pct change of equity/EV share — relative quarterly erosion rate."""
    ratio = _safe_div(marketcap, ev)
    return ratio.pct_change(_TD_QTR)


def evd_drv2_032_ev_to_mktcap_126d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """126-day diff of EV/mktcap ratio — semi-annual velocity of distortion."""
    ratio = _safe_div(ev, marketcap)
    return ratio.diff(_TD_HALF)


def evd_drv2_033_wedge_to_mktcap_126d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """126-day diff of wedge/mktcap ratio — semi-annual leverage drift."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return ratio.diff(_TD_HALF)


def evd_drv2_034_mktcap_to_ev_126d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """126-day diff of equity/EV share — semi-annual erosion of equity residual."""
    ratio = _safe_div(marketcap, ev)
    return ratio.diff(_TD_HALF)


def evd_drv2_035_log_ev_to_mktcap_63d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day diff of log(EV/mktcap) — log-space quarterly distortion velocity."""
    log_ratio = _log_safe(_safe_div(ev, marketcap).clip(lower=_EPS))
    return log_ratio.diff(_TD_QTR)


def evd_drv2_036_ev_to_mktcap_zscore_21d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day diff of 252-day z-score of EV/mktcap (monthly shift in statistical extremity)."""
    ratio = _safe_div(ev, marketcap)
    z     = _zscore_rolling(ratio, _TD_YEAR)
    return z.diff(_TD_MON)


def evd_drv2_037_wedge_ratio_zscore_21d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day diff of 252-day z-score of wedge/mktcap (monthly leverage extremity shift)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    z     = _zscore_rolling(ratio, _TD_YEAR)
    return z.diff(_TD_MON)


def evd_drv2_038_ev_to_mktcap_126d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """OLS slope of EV/mktcap ratio over 126 days (semi-annual linear distortion trend)."""
    ratio = _safe_div(ev, marketcap)
    return _linslope(ratio, _TD_HALF)


def evd_drv2_039_wedge_to_mktcap_63d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """OLS slope of wedge/mktcap ratio over 63 days (quarterly leverage slope)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return _linslope(ratio, _TD_QTR)


def evd_drv2_040_wedge_to_mktcap_126d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """OLS slope of wedge/mktcap ratio over 126 days (semi-annual leverage slope)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return _linslope(ratio, _TD_HALF)


def evd_drv2_041_mktcap_to_ev_126d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """OLS slope of equity/EV share over 126 days (semi-annual erosion slope)."""
    ratio = _safe_div(marketcap, ev)
    return _linslope(ratio, _TD_HALF)


def evd_drv2_042_evebitda_63d_slope(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """OLS slope of EV/EBITDA over 63 days (quarterly enterprise multiple trend)."""
    return _linslope(evebitda, _TD_QTR)


def evd_drv2_043_evebit_21d_slope(evebit: pd.Series, marketcap: pd.Series) -> pd.Series:
    """OLS slope of EV/EBIT over 21 days (short-term EBIT-multiple trend)."""
    return _linslope(evebit, _TD_MON)


def evd_drv2_044_evebit_63d_slope(evebit: pd.Series, marketcap: pd.Series) -> pd.Series:
    """OLS slope of EV/EBIT over 63 days (quarterly EBIT-multiple trend)."""
    return _linslope(evebit, _TD_QTR)


def evd_drv2_045_evebitda_vs_pe_ratio_63d_diff(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """63-day diff of EV/EBITDA-to-P/E ratio (quarterly multiple-gap drift)."""
    ratio = _safe_div(evebitda, pe)
    return ratio.diff(_TD_QTR)


def evd_drv2_046_evebit_vs_pe_ratio_21d_diff(evebit: pd.Series, pe: pd.Series) -> pd.Series:
    """21-day diff of EV/EBIT-to-P/E ratio (monthly EBIT multiple-gap drift)."""
    ratio = _safe_div(evebit, pe)
    return ratio.diff(_TD_MON)


def evd_drv2_047_evebit_vs_pe_ratio_63d_diff(evebit: pd.Series, pe: pd.Series) -> pd.Series:
    """63-day diff of EV/EBIT-to-P/E ratio (quarterly EBIT multiple-gap drift)."""
    ratio = _safe_div(evebit, pe)
    return ratio.diff(_TD_QTR)


def evd_drv2_048_evebitda_vs_pe_21d_slope(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """OLS slope of EV/EBITDA-to-P/E ratio over 21 days (short-term multiple-gap trend)."""
    ratio = _safe_div(evebitda, pe)
    return _linslope(ratio, _TD_MON)


def evd_drv2_049_evebit_vs_pe_21d_slope(evebit: pd.Series, pe: pd.Series) -> pd.Series:
    """OLS slope of EV/EBIT-to-P/E ratio over 21 days."""
    ratio = _safe_div(evebit, pe)
    return _linslope(ratio, _TD_MON)


def evd_drv2_050_dd_divergence_63d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day diff of 252-day drawdown divergence (quarterly acceleration of split)."""
    mc_h  = _rolling_max(marketcap, _TD_YEAR)
    ev_h  = _rolling_max(ev, _TD_YEAR)
    mc_dd = _safe_div(marketcap - mc_h, mc_h)
    ev_dd = _safe_div(ev - ev_h, ev_h)
    div   = mc_dd - ev_dd
    return div.diff(_TD_QTR)


def evd_drv2_051_ev_to_mktcap_ratio_5d_zscore_21d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day diff of 63-day z-score of EV/mktcap (monthly shift in quarterly extremity)."""
    ratio = _safe_div(ev, marketcap)
    z     = _zscore_rolling(ratio, _TD_QTR)
    return z.diff(_TD_MON)


def evd_drv2_052_wedge_ratio_zscore_63d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day diff of 252-day z-score of wedge/mktcap (quarterly extremity shift)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    z     = _zscore_rolling(ratio, _TD_YEAR)
    return z.diff(_TD_QTR)


def evd_drv2_053_mktcap_to_ev_zscore_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 252-day z-score of equity/EV share (weekly extremity acceleration)."""
    ratio = _safe_div(marketcap, ev)
    z     = _zscore_rolling(ratio, _TD_YEAR)
    return z.diff(5)


def evd_drv2_054_mktcap_to_ev_zscore_21d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day diff of 252-day z-score of equity/EV share (monthly extremity shift)."""
    ratio = _safe_div(marketcap, ev)
    z     = _zscore_rolling(ratio, _TD_YEAR)
    return z.diff(_TD_MON)


def evd_drv2_055_composite_distortion_21d_diff(ev: pd.Series, marketcap: pd.Series, evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """21-day diff of composite distortion z-score (monthly velocity of composite signal)."""
    z1 = _zscore_rolling(_safe_div(ev, marketcap), _TD_YEAR)
    z2 = _zscore_rolling(_safe_div(ev - marketcap, marketcap), _TD_YEAR)
    z3 = _zscore_rolling(_safe_div(evebitda, pe), _TD_YEAR)
    composite = (z1 + z2 + z3) / 3.0
    return composite.diff(_TD_MON)


def evd_drv2_056_ev_to_mktcap_5d_diff_ewm_21(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day EWM of 5-day EV/mktcap velocity (smoothed weekly distortion speed)."""
    ratio    = _safe_div(ev, marketcap)
    velocity = ratio.diff(5)
    return _ewm_mean(velocity, _TD_MON)


def evd_drv2_057_wedge_5d_diff_ewm_21(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day EWM of 5-day wedge/mktcap velocity (smoothed weekly leverage speed)."""
    ratio    = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    velocity = ratio.diff(5)
    return _ewm_mean(velocity, _TD_MON)


def evd_drv2_058_mktcap_to_ev_5d_diff_ewm_21(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day EWM of 5-day equity/EV velocity (smoothed weekly erosion speed)."""
    ratio    = _safe_div(marketcap, ev)
    velocity = ratio.diff(5)
    return _ewm_mean(velocity, _TD_MON)


def evd_drv2_059_ev_to_mktcap_21d_diff_ewm_63(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day EWM of 21-day EV/mktcap velocity (smoothed monthly distortion speed)."""
    ratio    = _safe_div(ev, marketcap)
    velocity = ratio.diff(_TD_MON)
    return _ewm_mean(velocity, _TD_QTR)


def evd_drv2_060_wedge_21d_diff_ewm_63(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day EWM of 21-day wedge/mktcap velocity (smoothed monthly leverage speed)."""
    ratio    = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    velocity = ratio.diff(_TD_MON)
    return _ewm_mean(velocity, _TD_QTR)


def evd_drv2_061_ev_to_mktcap_252d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day diff of EV/mktcap ratio — annual velocity of distortion."""
    ratio = _safe_div(ev, marketcap)
    return ratio.diff(_TD_YEAR)


def evd_drv2_062_wedge_to_mktcap_252d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day diff of wedge/mktcap ratio — annual leverage drift."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return ratio.diff(_TD_YEAR)


def evd_drv2_063_mktcap_to_ev_252d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day diff of equity/EV share — annual erosion of equity residual."""
    ratio = _safe_div(marketcap, ev)
    return ratio.diff(_TD_YEAR)


def evd_drv2_064_ev_to_mktcap_252d_pct_change(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day pct change of EV/mktcap ratio — relative annual velocity."""
    ratio = _safe_div(ev, marketcap)
    return ratio.pct_change(_TD_YEAR)


def evd_drv2_065_evebitda_252d_diff(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """252-day diff of EV/EBITDA multiple — annual enterprise multiple drift."""
    return evebitda.diff(_TD_YEAR)


def evd_drv2_066_evebit_252d_diff(evebit: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day diff of EV/EBIT multiple — annual EBIT multiple drift."""
    return evebit.diff(_TD_YEAR)


def evd_drv2_067_evebitda_pct_change_21d(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """21-day pct change of EV/EBITDA — relative monthly enterprise multiple velocity."""
    return evebitda.pct_change(_TD_MON)


def evd_drv2_068_evebit_pct_change_21d(evebit: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day pct change of EV/EBIT — relative monthly EBIT multiple velocity."""
    return evebit.pct_change(_TD_MON)


def evd_drv2_069_evebitda_pct_change_63d(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """63-day pct change of EV/EBITDA — relative quarterly enterprise multiple velocity."""
    return evebitda.pct_change(_TD_QTR)


def evd_drv2_070_evebit_pct_change_63d(evebit: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day pct change of EV/EBIT — relative quarterly EBIT multiple velocity."""
    return evebit.pct_change(_TD_QTR)


def evd_drv2_071_wedge_to_mktcap_5d_pct_change(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day pct change of wedge/mktcap ratio — relative weekly leverage velocity."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return ratio.pct_change(5)


def evd_drv2_072_mktcap_to_ev_5d_pct_change(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day pct change of equity/EV share — relative weekly erosion velocity."""
    ratio = _safe_div(marketcap, ev)
    return ratio.pct_change(5)


def evd_drv2_073_evebitda_to_pe_5d_diff(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """5-day diff of EV/EBITDA-to-P/E ratio — weekly velocity of multiple gap."""
    ratio = _safe_div(evebitda, pe)
    return ratio.diff(5)


def evd_drv2_074_evebitda_to_pe_pct_change_21d(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """21-day pct change of EV/EBITDA-to-P/E ratio — relative monthly multiple-gap velocity."""
    ratio = _safe_div(evebitda, pe)
    return ratio.pct_change(_TD_MON)


def evd_drv2_075_evebitda_to_evebit_5d_diff(evebit: pd.Series, evebitda: pd.Series) -> pd.Series:
    """5-day diff of EV/EBITDA-to-EV/EBIT ratio — weekly velocity of DA-burden spread."""
    ratio = _safe_div(evebitda, evebit)
    return ratio.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

EV_DISTORTION_REGISTRY_2ND_DERIVATIVES = {
    "evd_drv2_001_ev_to_mktcap_ratio_5d_diff":      {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_001_ev_to_mktcap_ratio_5d_diff},
    "evd_drv2_002_ev_to_mktcap_ratio_21d_diff":     {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_002_ev_to_mktcap_ratio_21d_diff},
    "evd_drv2_003_wedge_to_mktcap_5d_diff":         {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_003_wedge_to_mktcap_5d_diff},
    "evd_drv2_004_wedge_to_mktcap_21d_diff":        {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_004_wedge_to_mktcap_21d_diff},
    "evd_drv2_005_mktcap_to_ev_5d_diff":            {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_005_mktcap_to_ev_5d_diff},
    "evd_drv2_006_mktcap_to_ev_21d_diff":           {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_006_mktcap_to_ev_21d_diff},
    "evd_drv2_007_dd_divergence_5d_diff":           {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_007_dd_divergence_5d_diff},
    "evd_drv2_008_dd_divergence_21d_diff":          {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_008_dd_divergence_21d_diff},
    "evd_drv2_009_ev_to_mktcap_ratio_21d_slope":   {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_009_ev_to_mktcap_ratio_21d_slope},
    "evd_drv2_010_ev_to_mktcap_ratio_63d_slope":   {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_010_ev_to_mktcap_ratio_63d_slope},
    "evd_drv2_011_evebitda_vs_pe_ratio_5d_diff":   {"inputs": ["evebitda", "pe"],                         "func": evd_drv2_011_evebitda_vs_pe_ratio_5d_diff},
    "evd_drv2_012_evebitda_vs_pe_ratio_21d_diff":  {"inputs": ["evebitda", "pe"],                         "func": evd_drv2_012_evebitda_vs_pe_ratio_21d_diff},
    "evd_drv2_013_evebit_vs_pe_ratio_5d_diff":     {"inputs": ["evebit", "pe"],                           "func": evd_drv2_013_evebit_vs_pe_ratio_5d_diff},
    "evd_drv2_014_log_ev_to_mktcap_5d_diff":       {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_014_log_ev_to_mktcap_5d_diff},
    "evd_drv2_015_log_ev_to_mktcap_21d_diff":      {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_015_log_ev_to_mktcap_21d_diff},
    "evd_drv2_016_ev_to_mktcap_zscore_5d_diff":    {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_016_ev_to_mktcap_zscore_5d_diff},
    "evd_drv2_017_wedge_ratio_zscore_5d_diff":     {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_017_wedge_ratio_zscore_5d_diff},
    "evd_drv2_018_mktcap_to_ev_21d_slope":         {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_018_mktcap_to_ev_21d_slope},
    "evd_drv2_019_mktcap_to_ev_63d_slope":         {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_019_mktcap_to_ev_63d_slope},
    "evd_drv2_020_ev_to_mktcap_5d_pct_change":     {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_020_ev_to_mktcap_5d_pct_change},
    "evd_drv2_021_ev_to_mktcap_21d_pct_change":    {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_021_ev_to_mktcap_21d_pct_change},
    "evd_drv2_022_evebitda_21d_slope":             {"inputs": ["ev", "evebitda"],                         "func": evd_drv2_022_evebitda_21d_slope},
    "evd_drv2_023_composite_distortion_5d_diff":   {"inputs": ["ev", "marketcap", "evebitda", "pe"],      "func": evd_drv2_023_composite_distortion_5d_diff},
    "evd_drv2_024_wedge_to_mktcap_pct_change_21d": {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_024_wedge_to_mktcap_pct_change_21d},
    "evd_drv2_025_equity_share_21d_pct_change":    {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_025_equity_share_21d_pct_change},
    "evd_drv2_026_ev_to_mktcap_63d_diff":          {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_026_ev_to_mktcap_63d_diff},
    "evd_drv2_027_ev_to_mktcap_63d_pct_change":    {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_027_ev_to_mktcap_63d_pct_change},
    "evd_drv2_028_wedge_to_mktcap_63d_diff":       {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_028_wedge_to_mktcap_63d_diff},
    "evd_drv2_029_wedge_to_mktcap_63d_pct_change": {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_029_wedge_to_mktcap_63d_pct_change},
    "evd_drv2_030_mktcap_to_ev_63d_diff":          {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_030_mktcap_to_ev_63d_diff},
    "evd_drv2_031_mktcap_to_ev_63d_pct_change":    {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_031_mktcap_to_ev_63d_pct_change},
    "evd_drv2_032_ev_to_mktcap_126d_diff":         {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_032_ev_to_mktcap_126d_diff},
    "evd_drv2_033_wedge_to_mktcap_126d_diff":      {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_033_wedge_to_mktcap_126d_diff},
    "evd_drv2_034_mktcap_to_ev_126d_diff":         {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_034_mktcap_to_ev_126d_diff},
    "evd_drv2_035_log_ev_to_mktcap_63d_diff":      {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_035_log_ev_to_mktcap_63d_diff},
    "evd_drv2_036_ev_to_mktcap_zscore_21d_diff":   {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_036_ev_to_mktcap_zscore_21d_diff},
    "evd_drv2_037_wedge_ratio_zscore_21d_diff":    {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_037_wedge_ratio_zscore_21d_diff},
    "evd_drv2_038_ev_to_mktcap_126d_slope":        {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_038_ev_to_mktcap_126d_slope},
    "evd_drv2_039_wedge_to_mktcap_63d_slope":      {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_039_wedge_to_mktcap_63d_slope},
    "evd_drv2_040_wedge_to_mktcap_126d_slope":     {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_040_wedge_to_mktcap_126d_slope},
    "evd_drv2_041_mktcap_to_ev_126d_slope":        {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_041_mktcap_to_ev_126d_slope},
    "evd_drv2_042_evebitda_63d_slope":             {"inputs": ["ev", "evebitda"],                         "func": evd_drv2_042_evebitda_63d_slope},
    "evd_drv2_043_evebit_21d_slope":               {"inputs": ["evebit", "marketcap"],                    "func": evd_drv2_043_evebit_21d_slope},
    "evd_drv2_044_evebit_63d_slope":               {"inputs": ["evebit", "marketcap"],                    "func": evd_drv2_044_evebit_63d_slope},
    "evd_drv2_045_evebitda_vs_pe_ratio_63d_diff":  {"inputs": ["evebitda", "pe"],                         "func": evd_drv2_045_evebitda_vs_pe_ratio_63d_diff},
    "evd_drv2_046_evebit_vs_pe_ratio_21d_diff":    {"inputs": ["evebit", "pe"],                           "func": evd_drv2_046_evebit_vs_pe_ratio_21d_diff},
    "evd_drv2_047_evebit_vs_pe_ratio_63d_diff":    {"inputs": ["evebit", "pe"],                           "func": evd_drv2_047_evebit_vs_pe_ratio_63d_diff},
    "evd_drv2_048_evebitda_vs_pe_21d_slope":       {"inputs": ["evebitda", "pe"],                         "func": evd_drv2_048_evebitda_vs_pe_21d_slope},
    "evd_drv2_049_evebit_vs_pe_21d_slope":         {"inputs": ["evebit", "pe"],                           "func": evd_drv2_049_evebit_vs_pe_21d_slope},
    "evd_drv2_050_dd_divergence_63d_diff":         {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_050_dd_divergence_63d_diff},
    "evd_drv2_051_ev_to_mktcap_ratio_5d_zscore_21d_diff":  {"inputs": ["ev", "marketcap"],               "func": evd_drv2_051_ev_to_mktcap_ratio_5d_zscore_21d_diff},
    "evd_drv2_052_wedge_ratio_zscore_63d_diff":    {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_052_wedge_ratio_zscore_63d_diff},
    "evd_drv2_053_mktcap_to_ev_zscore_5d_diff":    {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_053_mktcap_to_ev_zscore_5d_diff},
    "evd_drv2_054_mktcap_to_ev_zscore_21d_diff":   {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_054_mktcap_to_ev_zscore_21d_diff},
    "evd_drv2_055_composite_distortion_21d_diff":  {"inputs": ["ev", "marketcap", "evebitda", "pe"],      "func": evd_drv2_055_composite_distortion_21d_diff},
    "evd_drv2_056_ev_to_mktcap_5d_diff_ewm_21":    {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_056_ev_to_mktcap_5d_diff_ewm_21},
    "evd_drv2_057_wedge_5d_diff_ewm_21":           {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_057_wedge_5d_diff_ewm_21},
    "evd_drv2_058_mktcap_to_ev_5d_diff_ewm_21":    {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_058_mktcap_to_ev_5d_diff_ewm_21},
    "evd_drv2_059_ev_to_mktcap_21d_diff_ewm_63":   {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_059_ev_to_mktcap_21d_diff_ewm_63},
    "evd_drv2_060_wedge_21d_diff_ewm_63":          {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_060_wedge_21d_diff_ewm_63},
    "evd_drv2_061_ev_to_mktcap_252d_diff":         {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_061_ev_to_mktcap_252d_diff},
    "evd_drv2_062_wedge_to_mktcap_252d_diff":      {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_062_wedge_to_mktcap_252d_diff},
    "evd_drv2_063_mktcap_to_ev_252d_diff":         {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_063_mktcap_to_ev_252d_diff},
    "evd_drv2_064_ev_to_mktcap_252d_pct_change":   {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_064_ev_to_mktcap_252d_pct_change},
    "evd_drv2_065_evebitda_252d_diff":             {"inputs": ["ev", "evebitda"],                         "func": evd_drv2_065_evebitda_252d_diff},
    "evd_drv2_066_evebit_252d_diff":               {"inputs": ["evebit", "marketcap"],                    "func": evd_drv2_066_evebit_252d_diff},
    "evd_drv2_067_evebitda_pct_change_21d":        {"inputs": ["ev", "evebitda"],                         "func": evd_drv2_067_evebitda_pct_change_21d},
    "evd_drv2_068_evebit_pct_change_21d":          {"inputs": ["evebit", "marketcap"],                    "func": evd_drv2_068_evebit_pct_change_21d},
    "evd_drv2_069_evebitda_pct_change_63d":        {"inputs": ["ev", "evebitda"],                         "func": evd_drv2_069_evebitda_pct_change_63d},
    "evd_drv2_070_evebit_pct_change_63d":          {"inputs": ["evebit", "marketcap"],                    "func": evd_drv2_070_evebit_pct_change_63d},
    "evd_drv2_071_wedge_to_mktcap_5d_pct_change":  {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_071_wedge_to_mktcap_5d_pct_change},
    "evd_drv2_072_mktcap_to_ev_5d_pct_change":     {"inputs": ["ev", "marketcap"],                        "func": evd_drv2_072_mktcap_to_ev_5d_pct_change},
    "evd_drv2_073_evebitda_to_pe_5d_diff":         {"inputs": ["evebitda", "pe"],                         "func": evd_drv2_073_evebitda_to_pe_5d_diff},
    "evd_drv2_074_evebitda_to_pe_pct_change_21d":  {"inputs": ["evebitda", "pe"],                         "func": evd_drv2_074_evebitda_to_pe_pct_change_21d},
    "evd_drv2_075_evebitda_to_evebit_5d_diff":     {"inputs": ["evebit", "evebitda"],                     "func": evd_drv2_075_evebitda_to_evebit_5d_diff},
}
