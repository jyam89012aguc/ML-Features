"""
79_ev_distortion — 3rd Derivatives (Features evd_drv3_001-075)
Domain: second-order rate-of-change of EV-distortion concepts — acceleration of the
        velocity signals produced by the 2nd-derivative layer. Captures convexity,
        curvature, and jerk in EV/equity distortion dynamics.

Inputs: daily-frequency Sharadar DAILY/METRICS valuation fields only.
        Canonical field names (lowercase): marketcap, ev, pe, pb, ps, evebit, evebitda, divyield.
        NO raw price/volume. NO quarterly forward-fill alignment helper needed.

All feature functions are strictly backward-looking: no negative shifts, no forward fills,
no .iloc[i+n] look-ahead. Each function computes a second diff / diff-of-slope / diff-of-pct-change
of a 2nd-derivative concept, or the slope/zscore of a 2nd-derivative series.
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def evd_drv3_001_ev_to_mktcap_ratio_5d_diff2(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Second 5-day diff of EV/mktcap ratio (acceleration: diff of 5d velocity)."""
    ratio = _safe_div(ev, marketcap)
    return ratio.diff(5).diff(5)


def evd_drv3_002_ev_to_mktcap_ratio_21d_diff2(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Second 21-day diff of EV/mktcap ratio (monthly acceleration of distortion)."""
    ratio = _safe_div(ev, marketcap)
    return ratio.diff(_TD_MON).diff(_TD_MON)


def evd_drv3_003_wedge_to_mktcap_5d_diff2(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Second 5-day diff of wedge/mktcap ratio (acceleration of leverage build-up)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return ratio.diff(5).diff(5)


def evd_drv3_004_wedge_to_mktcap_21d_diff2(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Second 21-day diff of wedge/mktcap ratio (monthly leverage acceleration)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return ratio.diff(_TD_MON).diff(_TD_MON)


def evd_drv3_005_mktcap_to_ev_5d_diff2(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Second 5-day diff of equity/EV share (acceleration of equity-slice erosion)."""
    ratio = _safe_div(marketcap, ev)
    return ratio.diff(5).diff(5)


def evd_drv3_006_mktcap_to_ev_21d_diff2(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Second 21-day diff of equity/EV share (monthly acceleration of erosion)."""
    ratio = _safe_div(marketcap, ev)
    return ratio.diff(_TD_MON).diff(_TD_MON)


def evd_drv3_007_dd_divergence_5d_diff2(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day drawdown divergence (jerk in equity-vs-EV split)."""
    mc_h  = _rolling_max(marketcap, _TD_YEAR)
    ev_h  = _rolling_max(ev, _TD_YEAR)
    mc_dd = _safe_div(marketcap - mc_h, mc_h)
    ev_dd = _safe_div(ev - ev_h, ev_h)
    div   = mc_dd - ev_dd
    return div.diff(5).diff(5)


def evd_drv3_008_ev_to_mktcap_ratio_5d_diff_21d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day OLS slope of 5-day velocity series (trend in velocity of distortion)."""
    ratio    = _safe_div(ev, marketcap)
    velocity = ratio.diff(5)
    return _linslope(velocity, _TD_MON)


def evd_drv3_009_ev_to_mktcap_ratio_5d_diff_63d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day OLS slope of 5-day velocity series (quarterly trend in velocity)."""
    ratio    = _safe_div(ev, marketcap)
    velocity = ratio.diff(5)
    return _linslope(velocity, _TD_QTR)


def evd_drv3_010_wedge_5d_diff_21d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day OLS slope of 5-day wedge/mktcap velocity (trend in leverage velocity)."""
    ratio    = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    velocity = ratio.diff(5)
    return _linslope(velocity, _TD_MON)


def evd_drv3_011_evebitda_vs_pe_ratio_5d_diff2(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """Second 5-day diff of EV/EBITDA-to-P/E ratio (acceleration of multiple-gap velocity)."""
    ratio = _safe_div(evebitda, pe)
    return ratio.diff(5).diff(5)


def evd_drv3_012_evebitda_vs_pe_ratio_5d_diff_21d_slope(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """21-day slope of 5-day velocity of EV/EBITDA-to-P/E ratio."""
    ratio    = _safe_div(evebitda, pe)
    velocity = ratio.diff(5)
    return _linslope(velocity, _TD_MON)


def evd_drv3_013_log_ev_to_mktcap_5d_diff2(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Second 5-day diff of log(EV/mktcap) (log-space acceleration of distortion)."""
    log_ratio = _log_safe(_safe_div(ev, marketcap).clip(lower=_EPS))
    return log_ratio.diff(5).diff(5)


def evd_drv3_014_ev_to_mktcap_zscore_5d_diff2(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day z-score of EV/mktcap (acceleration of statistical extremity)."""
    ratio = _safe_div(ev, marketcap)
    z     = _zscore_rolling(ratio, _TD_YEAR)
    return z.diff(5).diff(5)


def evd_drv3_015_wedge_zscore_5d_diff2(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day z-score of wedge/mktcap (leverage extremity jerk)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    z     = _zscore_rolling(ratio, _TD_YEAR)
    return z.diff(5).diff(5)


def evd_drv3_016_mktcap_to_ev_5d_diff_21d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day slope of 5-day velocity of equity/EV share (trend in erosion velocity)."""
    ratio    = _safe_div(marketcap, ev)
    velocity = ratio.diff(5)
    return _linslope(velocity, _TD_MON)


def evd_drv3_017_ev_to_mktcap_ratio_21d_pct_change_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 21-day pct-change of EV/mktcap (acceleration of relative monthly velocity)."""
    ratio = _safe_div(ev, marketcap)
    pct   = ratio.pct_change(_TD_MON)
    return pct.diff(5)


def evd_drv3_018_wedge_21d_pct_change_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 21-day pct-change of wedge/mktcap (monthly leverage-velocity jerk)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    pct   = ratio.pct_change(_TD_MON)
    return pct.diff(5)


def evd_drv3_019_equity_share_21d_pct_change_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 21-day pct-change of equity/EV share (erosion-rate jerk)."""
    ratio = _safe_div(marketcap, ev)
    pct   = ratio.pct_change(_TD_MON)
    return pct.diff(5)


def evd_drv3_020_composite_distortion_5d_diff2(ev: pd.Series, marketcap: pd.Series, evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """Second 5-day diff of composite distortion z-score (jerk of distortion acceleration)."""
    z1 = _zscore_rolling(_safe_div(ev, marketcap), _TD_YEAR)
    z2 = _zscore_rolling(_safe_div(ev - marketcap, marketcap), _TD_YEAR)
    z3 = _zscore_rolling(_safe_div(evebitda, pe), _TD_YEAR)
    composite = (z1 + z2 + z3) / 3.0
    return composite.diff(5).diff(5)


def evd_drv3_021_ev_to_mktcap_velocity_zscore_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day z-score of 5-day EV/mktcap velocity (how extreme is the current velocity)."""
    ratio    = _safe_div(ev, marketcap)
    velocity = ratio.diff(5)
    return _zscore_rolling(velocity, _TD_QTR)


def evd_drv3_022_wedge_velocity_zscore_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day z-score of 5-day wedge/mktcap velocity."""
    ratio    = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    velocity = ratio.diff(5)
    return _zscore_rolling(velocity, _TD_QTR)


def evd_drv3_023_mktcap_to_ev_velocity_zscore_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day z-score of 5-day equity/EV velocity (how extreme is the erosion speed)."""
    ratio    = _safe_div(marketcap, ev)
    velocity = ratio.diff(5)
    return _zscore_rolling(velocity, _TD_QTR)


def evd_drv3_024_ev_to_mktcap_velocity_pct_rank_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day pct-rank of 5-day EV/mktcap velocity (extreme velocity rank)."""
    ratio    = _safe_div(ev, marketcap)
    velocity = ratio.diff(5)
    return _rolling_rank_pct(velocity, _TD_YEAR)


def evd_drv3_025_dd_divergence_velocity_zscore_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day z-score of 5-day velocity of 252d drawdown divergence."""
    mc_h  = _rolling_max(marketcap, _TD_YEAR)
    ev_h  = _rolling_max(ev, _TD_YEAR)
    mc_dd = _safe_div(marketcap - mc_h, mc_h)
    ev_dd = _safe_div(ev - ev_h, ev_h)
    div   = mc_dd - ev_dd
    velocity = div.diff(5)
    return _zscore_rolling(velocity, _TD_QTR)


# ── 3rd-Derivative Feature Functions 026-075 ─────────────────────────────────

def evd_drv3_026_ev_to_mktcap_ratio_63d_diff2(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Second 63-day diff of EV/mktcap ratio (quarterly acceleration of distortion)."""
    ratio = _safe_div(ev, marketcap)
    return ratio.diff(_TD_QTR).diff(_TD_QTR)


def evd_drv3_027_wedge_to_mktcap_63d_diff2(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Second 63-day diff of wedge/mktcap ratio (quarterly acceleration of leverage)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    return ratio.diff(_TD_QTR).diff(_TD_QTR)


def evd_drv3_028_mktcap_to_ev_63d_diff2(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Second 63-day diff of equity/EV share (quarterly acceleration of erosion)."""
    ratio = _safe_div(marketcap, ev)
    return ratio.diff(_TD_QTR).diff(_TD_QTR)


def evd_drv3_029_ev_to_mktcap_ratio_5d_diff_126d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """126-day OLS slope of 5-day EV/mktcap velocity (semi-annual trend in velocity)."""
    ratio    = _safe_div(ev, marketcap)
    velocity = ratio.diff(5)
    return _linslope(velocity, _TD_HALF)


def evd_drv3_030_wedge_5d_diff_63d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day OLS slope of 5-day wedge/mktcap velocity (quarterly leverage velocity trend)."""
    ratio    = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    velocity = ratio.diff(5)
    return _linslope(velocity, _TD_QTR)


def evd_drv3_031_mktcap_to_ev_5d_diff_63d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day OLS slope of 5-day equity/EV velocity (quarterly erosion-velocity trend)."""
    ratio    = _safe_div(marketcap, ev)
    velocity = ratio.diff(5)
    return _linslope(velocity, _TD_QTR)


def evd_drv3_032_ev_to_mktcap_21d_diff_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of EV/mktcap (jerk of monthly distortion speed)."""
    ratio    = _safe_div(ev, marketcap)
    velocity = ratio.diff(_TD_MON)
    return velocity.diff(5)


def evd_drv3_033_wedge_21d_diff_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of wedge/mktcap (jerk of monthly leverage speed)."""
    ratio    = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    velocity = ratio.diff(_TD_MON)
    return velocity.diff(5)


def evd_drv3_034_mktcap_to_ev_21d_diff_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of equity/EV share (jerk of monthly erosion speed)."""
    ratio    = _safe_div(marketcap, ev)
    velocity = ratio.diff(_TD_MON)
    return velocity.diff(5)


def evd_drv3_035_evebitda_vs_pe_ratio_21d_diff_5d_diff(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of EV/EBITDA-to-P/E (jerk of monthly multiple-gap)."""
    ratio    = _safe_div(evebitda, pe)
    velocity = ratio.diff(_TD_MON)
    return velocity.diff(5)


def evd_drv3_036_evebit_vs_pe_ratio_5d_diff2(evebit: pd.Series, pe: pd.Series) -> pd.Series:
    """Second 5-day diff of EV/EBIT-to-P/E ratio (acceleration of EBIT multiple-gap velocity)."""
    ratio = _safe_div(evebit, pe)
    return ratio.diff(5).diff(5)


def evd_drv3_037_log_ev_to_mktcap_21d_diff_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of log(EV/mktcap) (log-space monthly velocity jerk)."""
    log_ratio = _log_safe(_safe_div(ev, marketcap).clip(lower=_EPS))
    velocity  = log_ratio.diff(_TD_MON)
    return velocity.diff(5)


def evd_drv3_038_ev_to_mktcap_zscore_63d_diff2(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Second 63-day diff of 252-day z-score of EV/mktcap (quarterly acceleration of extremity)."""
    ratio = _safe_div(ev, marketcap)
    z     = _zscore_rolling(ratio, _TD_YEAR)
    return z.diff(_TD_QTR).diff(_TD_QTR)


def evd_drv3_039_wedge_zscore_21d_diff2(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Second 21-day diff of 252-day z-score of wedge/mktcap (monthly acceleration of leverage extremity)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    z     = _zscore_rolling(ratio, _TD_YEAR)
    return z.diff(_TD_MON).diff(_TD_MON)


def evd_drv3_040_mktcap_to_ev_zscore_5d_diff2(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day z-score of equity/EV share (extremity jerk)."""
    ratio = _safe_div(marketcap, ev)
    z     = _zscore_rolling(ratio, _TD_YEAR)
    return z.diff(5).diff(5)


def evd_drv3_041_ev_to_mktcap_velocity_zscore_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day z-score of 5-day EV/mktcap velocity (annual extremity of weekly speed)."""
    ratio    = _safe_div(ev, marketcap)
    velocity = ratio.diff(5)
    return _zscore_rolling(velocity, _TD_YEAR)


def evd_drv3_042_wedge_velocity_zscore_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day z-score of 5-day wedge/mktcap velocity (annual extremity of leverage speed)."""
    ratio    = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    velocity = ratio.diff(5)
    return _zscore_rolling(velocity, _TD_YEAR)


def evd_drv3_043_mktcap_to_ev_velocity_zscore_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day z-score of 5-day equity/EV velocity (annual extremity of erosion speed)."""
    ratio    = _safe_div(marketcap, ev)
    velocity = ratio.diff(5)
    return _zscore_rolling(velocity, _TD_YEAR)


def evd_drv3_044_ev_to_mktcap_velocity_pct_rank_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day pct-rank of 5-day EV/mktcap velocity (quarterly rank of distortion speed)."""
    ratio    = _safe_div(ev, marketcap)
    velocity = ratio.diff(5)
    return _rolling_rank_pct(velocity, _TD_QTR)


def evd_drv3_045_wedge_velocity_pct_rank_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day pct-rank of 5-day wedge/mktcap velocity (annual rank of leverage speed)."""
    ratio    = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    velocity = ratio.diff(5)
    return _rolling_rank_pct(velocity, _TD_YEAR)


def evd_drv3_046_ev_to_mktcap_21d_diff_21d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day OLS slope of 21-day EV/mktcap velocity (trend of monthly distortion speed)."""
    ratio    = _safe_div(ev, marketcap)
    velocity = ratio.diff(_TD_MON)
    return _linslope(velocity, _TD_MON)


def evd_drv3_047_wedge_21d_diff_21d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day OLS slope of 21-day wedge/mktcap velocity (trend of monthly leverage speed)."""
    ratio    = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    velocity = ratio.diff(_TD_MON)
    return _linslope(velocity, _TD_MON)


def evd_drv3_048_mktcap_to_ev_21d_diff_21d_slope(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day OLS slope of 21-day equity/EV velocity (trend of monthly erosion speed)."""
    ratio    = _safe_div(marketcap, ev)
    velocity = ratio.diff(_TD_MON)
    return _linslope(velocity, _TD_MON)


def evd_drv3_049_evebitda_5d_diff_21d_slope(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """21-day OLS slope of 5-day EV/EBITDA velocity (trend in weekly enterprise-multiple speed)."""
    velocity = evebitda.diff(5)
    return _linslope(velocity, _TD_MON)


def evd_drv3_050_evebit_5d_diff_21d_slope(evebit: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day OLS slope of 5-day EV/EBIT velocity (trend in weekly EBIT-multiple speed)."""
    velocity = evebit.diff(5)
    return _linslope(velocity, _TD_MON)


def evd_drv3_051_ev_to_mktcap_63d_diff_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 63-day velocity of EV/mktcap (jerk of quarterly distortion speed)."""
    ratio    = _safe_div(ev, marketcap)
    velocity = ratio.diff(_TD_QTR)
    return velocity.diff(5)


def evd_drv3_052_wedge_63d_diff_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 63-day velocity of wedge/mktcap (jerk of quarterly leverage speed)."""
    ratio    = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    velocity = ratio.diff(_TD_QTR)
    return velocity.diff(5)


def evd_drv3_053_mktcap_to_ev_63d_diff_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 63-day velocity of equity/EV share (jerk of quarterly erosion speed)."""
    ratio    = _safe_div(marketcap, ev)
    velocity = ratio.diff(_TD_QTR)
    return velocity.diff(5)


def evd_drv3_054_ev_to_mktcap_63d_pct_change_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 63-day pct-change of EV/mktcap (jerk of relative quarterly velocity)."""
    ratio = _safe_div(ev, marketcap)
    pct   = ratio.pct_change(_TD_QTR)
    return pct.diff(5)


def evd_drv3_055_wedge_63d_pct_change_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 63-day pct-change of wedge/mktcap (jerk of relative quarterly leverage velocity)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    pct   = ratio.pct_change(_TD_QTR)
    return pct.diff(5)


def evd_drv3_056_composite_distortion_63d_diff_5d_diff(ev: pd.Series, marketcap: pd.Series, evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """5-day diff of 63-day velocity of composite distortion (jerk of quarterly composite speed)."""
    z1 = _zscore_rolling(_safe_div(ev, marketcap), _TD_YEAR)
    z2 = _zscore_rolling(_safe_div(ev - marketcap, marketcap), _TD_YEAR)
    z3 = _zscore_rolling(_safe_div(evebitda, pe), _TD_YEAR)
    composite = (z1 + z2 + z3) / 3.0
    velocity  = composite.diff(_TD_QTR)
    return velocity.diff(5)


def evd_drv3_057_ev_to_mktcap_21d_slope_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS slope of EV/mktcap (rate of change of linear distortion trend)."""
    ratio = _safe_div(ev, marketcap)
    slope = _linslope(ratio, _TD_MON)
    return slope.diff(5)


def evd_drv3_058_wedge_21d_slope_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS slope of wedge/mktcap (jerk of leverage linear trend)."""
    ratio = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    slope = _linslope(ratio, _TD_MON)
    return slope.diff(5)


def evd_drv3_059_mktcap_to_ev_21d_slope_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS slope of equity/EV share (jerk of erosion linear trend)."""
    ratio = _safe_div(marketcap, ev)
    slope = _linslope(ratio, _TD_MON)
    return slope.diff(5)


def evd_drv3_060_ev_to_mktcap_63d_slope_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 63-day OLS slope of EV/mktcap (jerk of quarterly linear distortion trend)."""
    ratio = _safe_div(ev, marketcap)
    slope = _linslope(ratio, _TD_QTR)
    return slope.diff(5)


def evd_drv3_061_dd_divergence_21d_diff_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of 252d drawdown divergence (jerk of monthly split speed)."""
    mc_h  = _rolling_max(marketcap, _TD_YEAR)
    ev_h  = _rolling_max(ev, _TD_YEAR)
    mc_dd = _safe_div(marketcap - mc_h, mc_h)
    ev_dd = _safe_div(ev - ev_h, ev_h)
    div   = mc_dd - ev_dd
    velocity = div.diff(_TD_MON)
    return velocity.diff(5)


def evd_drv3_062_dd_divergence_velocity_zscore_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day z-score of 5-day velocity of 252d drawdown divergence (annual extremity of split speed)."""
    mc_h  = _rolling_max(marketcap, _TD_YEAR)
    ev_h  = _rolling_max(ev, _TD_YEAR)
    mc_dd = _safe_div(marketcap - mc_h, mc_h)
    ev_dd = _safe_div(ev - ev_h, ev_h)
    div   = mc_dd - ev_dd
    velocity = div.diff(5)
    return _zscore_rolling(velocity, _TD_YEAR)


def evd_drv3_063_evebitda_vs_pe_5d_diff2(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """Second 5-day diff of EV/EBITDA-to-P/E ratio (acceleration of multiple-gap velocity)."""
    ratio = _safe_div(evebitda, pe)
    return ratio.diff(5).diff(5)


def evd_drv3_064_evebitda_vs_pe_21d_diff_5d_diff(evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of EV/EBITDA-to-P/E (jerk of monthly multiple-gap speed)."""
    ratio    = _safe_div(evebitda, pe)
    velocity = ratio.diff(_TD_MON)
    return velocity.diff(5)


def evd_drv3_065_evebit_vs_pe_21d_diff_5d_diff(evebit: pd.Series, pe: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of EV/EBIT-to-P/E (jerk of monthly EBIT gap speed)."""
    ratio    = _safe_div(evebit, pe)
    velocity = ratio.diff(_TD_MON)
    return velocity.diff(5)


def evd_drv3_066_ev_to_mktcap_5d_diff_zscore_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day z-score of 5-day EV/mktcap velocity (quarterly extremity of weekly distortion speed)."""
    ratio    = _safe_div(ev, marketcap)
    velocity = ratio.diff(5)
    return _zscore_rolling(velocity, _TD_QTR)


def evd_drv3_067_wedge_5d_diff_zscore_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day z-score of 5-day wedge/mktcap velocity (annual extremity of weekly leverage speed)."""
    ratio    = _safe_div(_net_debt_wedge(ev, marketcap), marketcap)
    velocity = ratio.diff(5)
    return _zscore_rolling(velocity, _TD_YEAR)


def evd_drv3_068_mktcap_to_ev_21d_diff_zscore_63d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """63-day z-score of 21-day equity/EV velocity (quarterly extremity of monthly erosion speed)."""
    ratio    = _safe_div(marketcap, ev)
    velocity = ratio.diff(_TD_MON)
    return _zscore_rolling(velocity, _TD_QTR)


def evd_drv3_069_ev_to_mktcap_21d_diff_zscore_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """252-day z-score of 21-day EV/mktcap velocity (annual extremity of monthly distortion speed)."""
    ratio    = _safe_div(ev, marketcap)
    velocity = ratio.diff(_TD_MON)
    return _zscore_rolling(velocity, _TD_YEAR)


def evd_drv3_070_evebitda_5d_diff2(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Second 5-day diff of EV/EBITDA (acceleration of weekly enterprise multiple velocity)."""
    return evebitda.diff(5).diff(5)


def evd_drv3_071_evebit_5d_diff2(evebit: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Second 5-day diff of EV/EBIT (acceleration of weekly EBIT multiple velocity)."""
    return evebit.diff(5).diff(5)


def evd_drv3_072_evebitda_21d_diff_5d_diff(ev: pd.Series, evebitda: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of EV/EBITDA (jerk of monthly enterprise multiple speed)."""
    velocity = evebitda.diff(_TD_MON)
    return velocity.diff(5)


def evd_drv3_073_evebit_21d_diff_5d_diff(evebit: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 21-day velocity of EV/EBIT (jerk of monthly EBIT multiple speed)."""
    velocity = evebit.diff(_TD_MON)
    return velocity.diff(5)


def evd_drv3_074_evebitda_to_evebit_5d_diff_21d_slope(evebit: pd.Series, evebitda: pd.Series) -> pd.Series:
    """21-day OLS slope of 5-day velocity of EV/EBITDA-to-EV/EBIT ratio (trend in DA-burden speed)."""
    ratio    = _safe_div(evebitda, evebit)
    velocity = ratio.diff(5)
    return _linslope(velocity, _TD_MON)


def evd_drv3_075_composite_distortion_velocity_zscore_63d(ev: pd.Series, marketcap: pd.Series, evebitda: pd.Series, pe: pd.Series) -> pd.Series:
    """63-day z-score of 5-day velocity of composite distortion (quarterly extremity of composite speed)."""
    z1 = _zscore_rolling(_safe_div(ev, marketcap), _TD_YEAR)
    z2 = _zscore_rolling(_safe_div(ev - marketcap, marketcap), _TD_YEAR)
    z3 = _zscore_rolling(_safe_div(evebitda, pe), _TD_YEAR)
    composite = (z1 + z2 + z3) / 3.0
    velocity  = composite.diff(5)
    return _zscore_rolling(velocity, _TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

EV_DISTORTION_REGISTRY_3RD_DERIVATIVES = {
    "evd_drv3_001_ev_to_mktcap_ratio_5d_diff2":               {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_001_ev_to_mktcap_ratio_5d_diff2},
    "evd_drv3_002_ev_to_mktcap_ratio_21d_diff2":              {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_002_ev_to_mktcap_ratio_21d_diff2},
    "evd_drv3_003_wedge_to_mktcap_5d_diff2":                  {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_003_wedge_to_mktcap_5d_diff2},
    "evd_drv3_004_wedge_to_mktcap_21d_diff2":                 {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_004_wedge_to_mktcap_21d_diff2},
    "evd_drv3_005_mktcap_to_ev_5d_diff2":                     {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_005_mktcap_to_ev_5d_diff2},
    "evd_drv3_006_mktcap_to_ev_21d_diff2":                    {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_006_mktcap_to_ev_21d_diff2},
    "evd_drv3_007_dd_divergence_5d_diff2":                    {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_007_dd_divergence_5d_diff2},
    "evd_drv3_008_ev_to_mktcap_ratio_5d_diff_21d_slope":      {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_008_ev_to_mktcap_ratio_5d_diff_21d_slope},
    "evd_drv3_009_ev_to_mktcap_ratio_5d_diff_63d_slope":      {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_009_ev_to_mktcap_ratio_5d_diff_63d_slope},
    "evd_drv3_010_wedge_5d_diff_21d_slope":                   {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_010_wedge_5d_diff_21d_slope},
    "evd_drv3_011_evebitda_vs_pe_ratio_5d_diff2":             {"inputs": ["evebitda", "pe"],                         "func": evd_drv3_011_evebitda_vs_pe_ratio_5d_diff2},
    "evd_drv3_012_evebitda_vs_pe_ratio_5d_diff_21d_slope":    {"inputs": ["evebitda", "pe"],                         "func": evd_drv3_012_evebitda_vs_pe_ratio_5d_diff_21d_slope},
    "evd_drv3_013_log_ev_to_mktcap_5d_diff2":                 {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_013_log_ev_to_mktcap_5d_diff2},
    "evd_drv3_014_ev_to_mktcap_zscore_5d_diff2":              {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_014_ev_to_mktcap_zscore_5d_diff2},
    "evd_drv3_015_wedge_zscore_5d_diff2":                     {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_015_wedge_zscore_5d_diff2},
    "evd_drv3_016_mktcap_to_ev_5d_diff_21d_slope":            {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_016_mktcap_to_ev_5d_diff_21d_slope},
    "evd_drv3_017_ev_to_mktcap_ratio_21d_pct_change_5d_diff": {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_017_ev_to_mktcap_ratio_21d_pct_change_5d_diff},
    "evd_drv3_018_wedge_21d_pct_change_5d_diff":              {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_018_wedge_21d_pct_change_5d_diff},
    "evd_drv3_019_equity_share_21d_pct_change_5d_diff":       {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_019_equity_share_21d_pct_change_5d_diff},
    "evd_drv3_020_composite_distortion_5d_diff2":             {"inputs": ["ev", "marketcap", "evebitda", "pe"],      "func": evd_drv3_020_composite_distortion_5d_diff2},
    "evd_drv3_021_ev_to_mktcap_velocity_zscore_63d":          {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_021_ev_to_mktcap_velocity_zscore_63d},
    "evd_drv3_022_wedge_velocity_zscore_63d":                 {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_022_wedge_velocity_zscore_63d},
    "evd_drv3_023_mktcap_to_ev_velocity_zscore_63d":          {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_023_mktcap_to_ev_velocity_zscore_63d},
    "evd_drv3_024_ev_to_mktcap_velocity_pct_rank_252d":       {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_024_ev_to_mktcap_velocity_pct_rank_252d},
    "evd_drv3_025_dd_divergence_velocity_zscore_63d":         {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_025_dd_divergence_velocity_zscore_63d},
    "evd_drv3_026_ev_to_mktcap_ratio_63d_diff2":             {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_026_ev_to_mktcap_ratio_63d_diff2},
    "evd_drv3_027_wedge_to_mktcap_63d_diff2":                {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_027_wedge_to_mktcap_63d_diff2},
    "evd_drv3_028_mktcap_to_ev_63d_diff2":                   {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_028_mktcap_to_ev_63d_diff2},
    "evd_drv3_029_ev_to_mktcap_ratio_5d_diff_126d_slope":    {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_029_ev_to_mktcap_ratio_5d_diff_126d_slope},
    "evd_drv3_030_wedge_5d_diff_63d_slope":                  {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_030_wedge_5d_diff_63d_slope},
    "evd_drv3_031_mktcap_to_ev_5d_diff_63d_slope":           {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_031_mktcap_to_ev_5d_diff_63d_slope},
    "evd_drv3_032_ev_to_mktcap_21d_diff_5d_diff":            {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_032_ev_to_mktcap_21d_diff_5d_diff},
    "evd_drv3_033_wedge_21d_diff_5d_diff":                   {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_033_wedge_21d_diff_5d_diff},
    "evd_drv3_034_mktcap_to_ev_21d_diff_5d_diff":            {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_034_mktcap_to_ev_21d_diff_5d_diff},
    "evd_drv3_035_evebitda_vs_pe_ratio_21d_diff_5d_diff":    {"inputs": ["evebitda", "pe"],                         "func": evd_drv3_035_evebitda_vs_pe_ratio_21d_diff_5d_diff},
    "evd_drv3_036_evebit_vs_pe_ratio_5d_diff2":              {"inputs": ["evebit", "pe"],                           "func": evd_drv3_036_evebit_vs_pe_ratio_5d_diff2},
    "evd_drv3_037_log_ev_to_mktcap_21d_diff_5d_diff":        {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_037_log_ev_to_mktcap_21d_diff_5d_diff},
    "evd_drv3_038_ev_to_mktcap_zscore_63d_diff2":            {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_038_ev_to_mktcap_zscore_63d_diff2},
    "evd_drv3_039_wedge_zscore_21d_diff2":                   {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_039_wedge_zscore_21d_diff2},
    "evd_drv3_040_mktcap_to_ev_zscore_5d_diff2":             {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_040_mktcap_to_ev_zscore_5d_diff2},
    "evd_drv3_041_ev_to_mktcap_velocity_zscore_252d":        {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_041_ev_to_mktcap_velocity_zscore_252d},
    "evd_drv3_042_wedge_velocity_zscore_252d":               {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_042_wedge_velocity_zscore_252d},
    "evd_drv3_043_mktcap_to_ev_velocity_zscore_252d":        {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_043_mktcap_to_ev_velocity_zscore_252d},
    "evd_drv3_044_ev_to_mktcap_velocity_pct_rank_63d":       {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_044_ev_to_mktcap_velocity_pct_rank_63d},
    "evd_drv3_045_wedge_velocity_pct_rank_252d":             {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_045_wedge_velocity_pct_rank_252d},
    "evd_drv3_046_ev_to_mktcap_21d_diff_21d_slope":          {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_046_ev_to_mktcap_21d_diff_21d_slope},
    "evd_drv3_047_wedge_21d_diff_21d_slope":                 {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_047_wedge_21d_diff_21d_slope},
    "evd_drv3_048_mktcap_to_ev_21d_diff_21d_slope":          {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_048_mktcap_to_ev_21d_diff_21d_slope},
    "evd_drv3_049_evebitda_5d_diff_21d_slope":               {"inputs": ["ev", "evebitda"],                         "func": evd_drv3_049_evebitda_5d_diff_21d_slope},
    "evd_drv3_050_evebit_5d_diff_21d_slope":                 {"inputs": ["evebit", "marketcap"],                    "func": evd_drv3_050_evebit_5d_diff_21d_slope},
    "evd_drv3_051_ev_to_mktcap_63d_diff_5d_diff":            {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_051_ev_to_mktcap_63d_diff_5d_diff},
    "evd_drv3_052_wedge_63d_diff_5d_diff":                   {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_052_wedge_63d_diff_5d_diff},
    "evd_drv3_053_mktcap_to_ev_63d_diff_5d_diff":            {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_053_mktcap_to_ev_63d_diff_5d_diff},
    "evd_drv3_054_ev_to_mktcap_63d_pct_change_5d_diff":      {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_054_ev_to_mktcap_63d_pct_change_5d_diff},
    "evd_drv3_055_wedge_63d_pct_change_5d_diff":             {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_055_wedge_63d_pct_change_5d_diff},
    "evd_drv3_056_composite_distortion_63d_diff_5d_diff":    {"inputs": ["ev", "marketcap", "evebitda", "pe"],      "func": evd_drv3_056_composite_distortion_63d_diff_5d_diff},
    "evd_drv3_057_ev_to_mktcap_21d_slope_5d_diff":           {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_057_ev_to_mktcap_21d_slope_5d_diff},
    "evd_drv3_058_wedge_21d_slope_5d_diff":                  {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_058_wedge_21d_slope_5d_diff},
    "evd_drv3_059_mktcap_to_ev_21d_slope_5d_diff":           {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_059_mktcap_to_ev_21d_slope_5d_diff},
    "evd_drv3_060_ev_to_mktcap_63d_slope_5d_diff":           {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_060_ev_to_mktcap_63d_slope_5d_diff},
    "evd_drv3_061_dd_divergence_21d_diff_5d_diff":           {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_061_dd_divergence_21d_diff_5d_diff},
    "evd_drv3_062_dd_divergence_velocity_zscore_252d":       {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_062_dd_divergence_velocity_zscore_252d},
    "evd_drv3_063_evebitda_vs_pe_5d_diff2":                  {"inputs": ["evebitda", "pe"],                         "func": evd_drv3_063_evebitda_vs_pe_5d_diff2},
    "evd_drv3_064_evebitda_vs_pe_21d_diff_5d_diff":          {"inputs": ["evebitda", "pe"],                         "func": evd_drv3_064_evebitda_vs_pe_21d_diff_5d_diff},
    "evd_drv3_065_evebit_vs_pe_21d_diff_5d_diff":            {"inputs": ["evebit", "pe"],                           "func": evd_drv3_065_evebit_vs_pe_21d_diff_5d_diff},
    "evd_drv3_066_ev_to_mktcap_5d_diff_zscore_63d":          {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_066_ev_to_mktcap_5d_diff_zscore_63d},
    "evd_drv3_067_wedge_5d_diff_zscore_252d":                {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_067_wedge_5d_diff_zscore_252d},
    "evd_drv3_068_mktcap_to_ev_21d_diff_zscore_63d":         {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_068_mktcap_to_ev_21d_diff_zscore_63d},
    "evd_drv3_069_ev_to_mktcap_21d_diff_zscore_252d":        {"inputs": ["ev", "marketcap"],                        "func": evd_drv3_069_ev_to_mktcap_21d_diff_zscore_252d},
    "evd_drv3_070_evebitda_5d_diff2":                        {"inputs": ["ev", "evebitda"],                         "func": evd_drv3_070_evebitda_5d_diff2},
    "evd_drv3_071_evebit_5d_diff2":                          {"inputs": ["evebit", "marketcap"],                    "func": evd_drv3_071_evebit_5d_diff2},
    "evd_drv3_072_evebitda_21d_diff_5d_diff":                {"inputs": ["ev", "evebitda"],                         "func": evd_drv3_072_evebitda_21d_diff_5d_diff},
    "evd_drv3_073_evebit_21d_diff_5d_diff":                  {"inputs": ["evebit", "marketcap"],                    "func": evd_drv3_073_evebit_21d_diff_5d_diff},
    "evd_drv3_074_evebitda_to_evebit_5d_diff_21d_slope":     {"inputs": ["evebit", "evebitda"],                     "func": evd_drv3_074_evebitda_to_evebit_5d_diff_21d_slope},
    "evd_drv3_075_composite_distortion_velocity_zscore_63d": {"inputs": ["ev", "marketcap", "evebitda", "pe"],      "func": evd_drv3_075_composite_distortion_velocity_zscore_63d},
}
