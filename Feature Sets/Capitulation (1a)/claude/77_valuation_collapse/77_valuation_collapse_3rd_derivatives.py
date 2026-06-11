"""
77_valuation_collapse — 3rd Derivatives (Features drv3_001-075)
Domain: acceleration of rate-of-change of valuation-collapse features.
Inputs: Sharadar DAILY/METRICS valuation fields (daily frequency):
    marketcap, ev, pe, pb, ps, evebit, evebitda, divyield
These are native daily-frequency series (price moves daily; fundamental denominator
steps quarterly). No quarterly forward-fill alignment is needed here.
Each feature computes a .diff(n) or slope of a 2nd-derivative concept,
i.e. the third derivative of the underlying valuation-multiple series.
All features are backward-looking only — no negative shifts, no future info.
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


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _expanding_max(s: pd.Series) -> pd.Series:
    return s.expanding(min_periods=1).max()


def _positive_mask(s: pd.Series) -> pd.Series:
    """Return s where s > 0, else NaN."""
    return s.where(s > 0)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope of s over w periods."""
    def _slope(x):
        n = len(x)
        if n < max(2, w // 2):
            return np.nan
        xi   = np.arange(n, dtype=float)
        xi_m = xi.mean()
        xm   = x.mean()
        num  = ((xi - xi_m) * (x - xm)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=False)


# ── Helper: 2nd-derivative building blocks (self-contained, no cross-file import) ─

def _pe_dd_252d_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of PE 252d drawdown (2nd derivative building block)."""
    p    = _positive_mask(pe)
    peak = _rolling_max(p, _TD_YEAR)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_WEEK)


def _pb_dd_252d_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of PB 252d drawdown."""
    p    = _positive_mask(pb)
    peak = _rolling_max(p, _TD_YEAR)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_WEEK)


def _ps_dd_252d_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of PS 252d drawdown."""
    p    = _positive_mask(ps)
    peak = _rolling_max(p, _TD_YEAR)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_WEEK)


def _evebitda_dd_252d_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5-day diff of EV/EBITDA 252d drawdown."""
    p    = _positive_mask(evebitda)
    peak = _rolling_max(p, _TD_YEAR)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_WEEK)


def _distress_count(pe, pb, ps, evebitda):
    """Count of distress-threshold breaches (0-4)."""
    c  = ((pe > 0) & (pe < 10)).astype(float)
    c += ((pb > 0) & (pb < 1.0)).astype(float)
    c += ((ps > 0) & (ps < 1.0)).astype(float)
    c += ((evebitda > 0) & (evebitda < 5)).astype(float)
    return c


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def vcl_drv3_001_pe_dd_252d_5d_diff_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of the 5-day-diff of PE's 252-day drawdown (jerk of PE de-rating)."""
    vel = _pe_dd_252d_5d_diff(pe)
    return vel.diff(_TD_WEEK)


def vcl_drv3_002_pb_dd_252d_5d_diff_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of the 5-day-diff of PB's 252-day drawdown."""
    vel = _pb_dd_252d_5d_diff(pb)
    return vel.diff(_TD_WEEK)


def vcl_drv3_003_ps_dd_252d_5d_diff_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of the 5-day-diff of PS's 252-day drawdown."""
    vel = _ps_dd_252d_5d_diff(ps)
    return vel.diff(_TD_WEEK)


def vcl_drv3_004_evebitda_dd_252d_5d_diff_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5-day diff of the 5-day-diff of EV/EBITDA's 252-day drawdown."""
    vel = _evebitda_dd_252d_5d_diff(evebitda)
    return vel.diff(_TD_WEEK)


def vcl_drv3_005_pe_dd_velocity_slope_21d(pe: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5d-PE-drawdown-diff series (trend in de-rating velocity)."""
    vel = _pe_dd_252d_5d_diff(pe)
    return _linslope(vel, _TD_MON)


def vcl_drv3_006_pb_dd_velocity_slope_21d(pb: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5d-PB-drawdown-diff series."""
    vel = _pb_dd_252d_5d_diff(pb)
    return _linslope(vel, _TD_MON)


def vcl_drv3_007_pe_dd_velocity_ewm_diff_5d(pe: pd.Series) -> pd.Series:
    """5-day diff of the EWM(21) of PE drawdown velocity (smoothed acceleration)."""
    vel = _pe_dd_252d_5d_diff(pe)
    smooth = _ewm_mean(vel, _TD_MON)
    return smooth.diff(_TD_WEEK)


def vcl_drv3_008_pb_dd_velocity_ewm_diff_5d(pb: pd.Series) -> pd.Series:
    """5-day diff of the EWM(21) of PB drawdown velocity."""
    vel = _pb_dd_252d_5d_diff(pb)
    smooth = _ewm_mean(vel, _TD_MON)
    return smooth.diff(_TD_WEEK)


def vcl_drv3_009_ps_dd_velocity_ewm_diff_5d(ps: pd.Series) -> pd.Series:
    """5-day diff of the EWM(21) of PS drawdown velocity."""
    vel = _ps_dd_252d_5d_diff(ps)
    smooth = _ewm_mean(vel, _TD_MON)
    return smooth.diff(_TD_WEEK)


def vcl_drv3_010_distress_count_5d_diff_5d_diff(pe: pd.Series, pb: pd.Series,
                                                   ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """5-day diff of the 5-day-diff of distress threshold count (jerk of distress)."""
    cnt = _distress_count(pe, pb, ps, evebitda)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_011_pe_zscore_velocity_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of the 5-day-diff of PE's 252d z-score (acceleration of extremity)."""
    p   = _positive_mask(pe)
    zs  = _zscore_rolling(p, _TD_YEAR)
    vel = zs.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_012_pb_low_position_accel_5d(pb: pd.Series) -> pd.Series:
    """5-day diff of the 5d-diff of PB's 252-day range position (jerk toward low)."""
    p   = _positive_mask(pb)
    hi  = _rolling_max(p, _TD_YEAR)
    lo  = _rolling_min(p, _TD_YEAR)
    pos = _safe_div(p - lo, hi - lo)
    vel = pos.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_013_pe_compression_speed_accel_5d(pe: pd.Series) -> pd.Series:
    """5-day diff of the 5-day-diff of PE's 21-day compression speed."""
    p     = _positive_mask(pe)
    speed = _safe_div(p - p.shift(_TD_MON), pd.Series(_TD_MON, index=p.index))
    vel   = speed.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_014_composite_dd_velocity_slope_21d(pe: pd.Series, pb: pd.Series,
                                                    ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the composite 252d-drawdown 5d-velocity."""
    def _dd252(s):
        p    = _positive_mask(s)
        peak = _rolling_max(p, _TD_YEAR)
        return _safe_div(p - peak, peak).fillna(0)
    combo = (_dd252(pe) + _dd252(pb) + _dd252(ps) + _dd252(evebitda)) / 4.0
    vel   = combo.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vcl_drv3_015_marketcap_dd_velocity_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of the 5-day-diff of market-cap 252d drawdown."""
    peak = _rolling_max(marketcap, _TD_YEAR)
    dd   = _safe_div(marketcap - peak, peak)
    vel  = dd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_016_pb_below_1_frac_accel_5d(pb: pd.Series) -> pd.Series:
    """5-day diff of 5d-diff of fraction of PB<1 days (jerk of distress persistence)."""
    flag = ((pb > 0) & (pb < 1.0)).astype(float)
    frac = _rolling_mean(flag, _TD_YEAR)
    vel  = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_017_evebit_neg_frac_accel_5d(evebit: pd.Series) -> pd.Series:
    """5-day diff of 5d-diff of EV/EBIT negative fraction (jerk of EBIT loss pace)."""
    flag = (evebit < 0).astype(float)
    frac = _rolling_mean(flag, _TD_YEAR)
    vel  = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_018_pe_slope_of_slope_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope-of-slope of PE (third derivative trend)."""
    p        = _positive_mask(pe)
    slope1   = _linslope(p, _TD_MON)
    slope2   = _linslope(slope1, _TD_MON)
    return slope2.diff(_TD_WEEK)


def vcl_drv3_019_pb_compression_streak_accel_5d(pb: pd.Series) -> pd.Series:
    """5-day diff of the 5d-diff of 63-day PB compression streak sum."""
    p      = _positive_mask(pb)
    neg_ch = p.diff(1).where(p.diff(1) < 0, 0.0)
    streak = _rolling_sum(neg_ch, _TD_QTR)
    vel    = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_020_pe_pb_concordance_accel_5d(pe: pd.Series, pb: pd.Series) -> pd.Series:
    """5-day diff of the 5d-diff of PE+PB joint compression concordance fraction."""
    pe_dec = (pe.diff(1) < 0).astype(float)
    pb_dec = (pb.diff(1) < 0).astype(float)
    conc   = _rolling_mean(pe_dec * pb_dec, _TD_YEAR)
    vel    = conc.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_021_evebitda_zscore_accel_5d(evebitda: pd.Series) -> pd.Series:
    """5-day diff of the 5d-diff of EV/EBITDA 252d z-score."""
    p   = _positive_mask(evebitda)
    zs  = _zscore_rolling(p, _TD_YEAR)
    vel = zs.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_022_ps_dd_velocity_slope_21d(ps: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5d-PS-drawdown-diff (trend in PS de-rating velocity)."""
    vel = _ps_dd_252d_5d_diff(ps)
    return _linslope(vel, _TD_MON)


def vcl_drv3_023_weighted_distress_accel_5d(pe: pd.Series, pb: pd.Series,
                                              ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """5-day diff of the 5d-diff of the weighted distress score (jerk of weighted distress)."""
    s  = 0.3 * ((pe > 0) & (pe < 10)).astype(float)
    s += 0.3 * ((pb > 0) & (pb < 1.0)).astype(float)
    s += 0.2 * ((ps > 0) & (ps < 1.0)).astype(float)
    s += 0.2 * ((evebitda > 0) & (evebitda < 5)).astype(float)
    vel = s.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_024_ev_to_mktcap_velocity_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of the 5d-diff of EV/mktcap ratio (jerk of leverage change)."""
    ratio = _safe_div(_positive_mask(ev), _positive_mask(marketcap))
    vel   = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_025_composite_dd_jerk_ewm(pe: pd.Series, pb: pd.Series,
                                         ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """EWM(5) of composite-dd 5d-velocity 5d-diff (smoothed multi-multiple jerk)."""
    def _dd252(s):
        p    = _positive_mask(s)
        peak = _rolling_max(p, _TD_YEAR)
        return _safe_div(p - peak, peak).fillna(0)
    combo  = (_dd252(pe) + _dd252(pb) + _dd252(ps) + _dd252(evebitda)) / 4.0
    vel    = combo.diff(_TD_WEEK)
    accel  = vel.diff(_TD_WEEK)
    return _ewm_mean(accel, _TD_WEEK)


# ── Additional 2nd-derivative building blocks for drv3_026-075 ───────────────

def _evebit_dd_252d_5d_diff(evebit: pd.Series) -> pd.Series:
    """5-day diff of EV/EBIT 252d drawdown (2nd-deriv block)."""
    p    = _positive_mask(evebit)
    peak = _rolling_max(p, _TD_YEAR)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_WEEK)


def _marketcap_dd_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of marketcap 252d drawdown (2nd-deriv block)."""
    peak = _rolling_max(marketcap, _TD_YEAR)
    dd   = _safe_div(marketcap - peak, peak)
    return dd.diff(_TD_WEEK)


def _divyield_5d_diff(divyield: pd.Series) -> pd.Series:
    """5-day diff of divyield (2nd-deriv block)."""
    return divyield.diff(_TD_WEEK)


def _ev_dd_252d_5d_diff(ev: pd.Series) -> pd.Series:
    """5-day diff of EV 252d drawdown (2nd-deriv block)."""
    p    = _positive_mask(ev)
    peak = _rolling_max(p, _TD_YEAR)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_WEEK)


def _composite_dd_5d_diff(pe, pb, ps, evebitda):
    """5-day diff of composite 252d drawdown (2nd-deriv block)."""
    def _dd(s):
        p    = _positive_mask(s)
        peak = _rolling_max(p, _TD_YEAR)
        return _safe_div(p - peak, peak).fillna(0)
    return ((_dd(pe) + _dd(pb) + _dd(ps) + _dd(evebitda)) / 4.0).diff(_TD_WEEK)


# ── 3rd-Derivative Feature Functions 026-075 ─────────────────────────────────

def vcl_drv3_026_evebit_dd_252d_5d_diff_5d_diff(evebit: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of EV/EBIT 252d drawdown (jerk of EV/EBIT de-rating)."""
    vel = _evebit_dd_252d_5d_diff(evebit)
    return vel.diff(_TD_WEEK)


def vcl_drv3_027_marketcap_dd_252d_accel_5d(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of marketcap 252d drawdown (jerk of equity collapse)."""
    vel = _marketcap_dd_252d_5d_diff(marketcap)
    return vel.diff(_TD_WEEK)


def vcl_drv3_028_divyield_5d_diff_5d_diff(divyield: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of divyield (jerk of yield spike)."""
    vel = _divyield_5d_diff(divyield)
    return vel.diff(_TD_WEEK)


def vcl_drv3_029_ev_dd_252d_accel_5d(ev: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of EV 252d drawdown."""
    vel = _ev_dd_252d_5d_diff(ev)
    return vel.diff(_TD_WEEK)


def vcl_drv3_030_pb_zscore_252d_accel_5d(pb: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of PB 252d z-score."""
    p   = _positive_mask(pb)
    zs  = _zscore_rolling(p, _TD_YEAR)
    vel = zs.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_031_ps_zscore_252d_accel_5d(ps: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of PS 252d z-score."""
    p   = _positive_mask(ps)
    zs  = _zscore_rolling(p, _TD_YEAR)
    vel = zs.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_032_evebit_zscore_accel_5d(evebit: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of EV/EBIT 252d z-score."""
    p   = _positive_mask(evebit)
    zs  = _zscore_rolling(p, _TD_YEAR)
    vel = zs.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_033_pe_dd_expanding_accel_5d(pe: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of PE expanding-peak drawdown."""
    p    = _positive_mask(pe)
    peak = _expanding_max(p)
    dd   = _safe_div(p - peak, peak)
    vel  = dd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_034_ps_dd_expanding_accel_5d(ps: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of PS expanding-peak drawdown."""
    p    = _positive_mask(ps)
    peak = _expanding_max(p)
    dd   = _safe_div(p - peak, peak)
    vel  = dd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_035_evebit_dd_velocity_slope_21d(evebit: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 5d-EV/EBIT-drawdown-diff (trend in EV/EBIT de-rating velocity)."""
    vel = _evebit_dd_252d_5d_diff(evebit)
    return _linslope(vel, _TD_MON)


def vcl_drv3_036_marketcap_dd_velocity_slope_21d(marketcap: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 5d-marketcap-drawdown-diff."""
    vel = _marketcap_dd_252d_5d_diff(marketcap)
    return _linslope(vel, _TD_MON)


def vcl_drv3_037_divyield_velocity_slope_21d(divyield: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 5d-divyield-diff (trend in yield spike velocity)."""
    vel = _divyield_5d_diff(divyield)
    return _linslope(vel, _TD_MON)


def vcl_drv3_038_ev_dd_velocity_slope_21d(ev: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 5d-EV-drawdown-diff."""
    vel = _ev_dd_252d_5d_diff(ev)
    return _linslope(vel, _TD_MON)


def vcl_drv3_039_composite_dd_accel_ewm(pe: pd.Series, pb: pd.Series,
                                         ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """EWM(5) of composite-dd 5d-velocity 5d-diff (smoothed jerk — wider multi-multiple)."""
    vel   = _composite_dd_5d_diff(pe, pb, ps, evebitda)
    accel = vel.diff(_TD_WEEK)
    return _ewm_mean(accel, _TD_WEEK)


def vcl_drv3_040_pe_slope_21d_accel_5d(pe: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of 21-day PE OLS slope."""
    p     = _positive_mask(pe)
    slope = _linslope(p, _TD_MON)
    vel   = slope.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_041_pb_slope_63d_accel_5d(pb: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of 63-day PB OLS slope."""
    p     = _positive_mask(pb)
    slope = _linslope(p, _TD_QTR)
    vel   = slope.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_042_ps_low_position_accel_5d(ps: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of PS 252d range position."""
    p   = _positive_mask(ps)
    hi  = _rolling_max(p, _TD_YEAR)
    lo  = _rolling_min(p, _TD_YEAR)
    pos = _safe_div(p - lo, hi - lo)
    vel = pos.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_043_evebitda_slope_63d_accel_5d(evebitda: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of 63-day EV/EBITDA OLS slope."""
    p     = _positive_mask(evebitda)
    slope = _linslope(p, _TD_QTR)
    vel   = slope.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_044_pb_below_1_frac_accel_21d(pb: pd.Series) -> pd.Series:
    """21-day diff of 5d-diff of PB<1 fraction (monthly acceleration of distress persistence)."""
    flag = ((pb > 0) & (pb < 1.0)).astype(float)
    frac = _rolling_mean(flag, _TD_YEAR)
    vel  = frac.diff(_TD_WEEK)
    return vel.diff(_TD_MON)


def vcl_drv3_045_evebit_neg_frac_accel_21d(evebit: pd.Series) -> pd.Series:
    """21-day diff of 5d-diff of EV/EBIT negative fraction."""
    flag = (evebit < 0).astype(float)
    frac = _rolling_mean(flag, _TD_YEAR)
    vel  = frac.diff(_TD_WEEK)
    return vel.diff(_TD_MON)


def vcl_drv3_046_distress_count_accel_21d(pe: pd.Series, pb: pd.Series,
                                           ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """21-day diff of 5d-diff of distress count (monthly jerk of distress breaches)."""
    cnt = _distress_count(pe, pb, ps, evebitda)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_MON)


def vcl_drv3_047_pe_dd_504d_accel_5d(pe: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of PE 504-day drawdown."""
    p    = _positive_mask(pe)
    peak = _rolling_max(p, 504)
    dd   = _safe_div(p - peak, peak)
    vel  = dd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_048_pb_dd_504d_accel_5d(pb: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of PB 504-day drawdown."""
    p    = _positive_mask(pb)
    peak = _rolling_max(p, 504)
    dd   = _safe_div(p - peak, peak)
    vel  = dd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_049_ps_dd_504d_accel_5d(ps: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of PS 504-day drawdown."""
    p    = _positive_mask(ps)
    peak = _rolling_max(p, 504)
    dd   = _safe_div(p - peak, peak)
    vel  = dd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_050_evebitda_dd_504d_accel_5d(evebitda: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of EV/EBITDA 504-day drawdown."""
    p    = _positive_mask(evebitda)
    peak = _rolling_max(p, 504)
    dd   = _safe_div(p - peak, peak)
    vel  = dd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_051_pe_compression_streak_63d_accel_5d(pe: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of 63-day PE compression streak sum."""
    p      = _positive_mask(pe)
    neg_ch = p.diff(1).where(p.diff(1) < 0, 0.0)
    streak = _rolling_sum(neg_ch, _TD_QTR)
    vel    = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_052_ps_compression_streak_252d_accel_5d(ps: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of 252-day PS compression streak sum."""
    p      = _positive_mask(ps)
    neg_ch = p.diff(1).where(p.diff(1) < 0, 0.0)
    streak = _rolling_sum(neg_ch, _TD_YEAR)
    vel    = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_053_evebitda_below_5_frac_accel_5d(evebitda: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of 252-day EV/EBITDA<5 fraction."""
    flag = ((evebitda > 0) & (evebitda < 5)).astype(float)
    frac = _rolling_mean(flag, _TD_YEAR)
    vel  = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_054_ev_to_mktcap_accel_5d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of EV/mktcap ratio."""
    ratio = _safe_div(_positive_mask(ev), _positive_mask(marketcap))
    vel   = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_055_divyield_5d_diff_slope_21d(divyield: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 5d-divyield-diff (trend in yield spike acceleration)."""
    vel = _divyield_5d_diff(divyield)
    return _linslope(vel, _TD_MON)


def vcl_drv3_056_pe_compression_speed_slope_21d(pe: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 5d-diff of 21d PE compression speed."""
    p     = _positive_mask(pe)
    speed = _safe_div(p - p.shift(_TD_MON), pd.Series(_TD_MON, index=p.index))
    vel   = speed.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vcl_drv3_057_pb_compression_speed_slope_21d(pb: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 5d-diff of 21d PB compression speed."""
    p     = _positive_mask(pb)
    speed = _safe_div(p - p.shift(_TD_MON), pd.Series(_TD_MON, index=p.index))
    vel   = speed.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vcl_drv3_058_marketcap_zscore_accel_5d(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of marketcap 252d z-score."""
    zs  = _zscore_rolling(marketcap, _TD_YEAR)
    vel = zs.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_059_pe_pb_concordance_slope_21d(pe: pd.Series, pb: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 5d-diff of PE+PB concordance fraction."""
    pe_dec = (pe.diff(1) < 0).astype(float)
    pb_dec = (pb.diff(1) < 0).astype(float)
    conc   = _rolling_mean(pe_dec * pb_dec, _TD_YEAR)
    vel    = conc.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vcl_drv3_060_ps_dd_252d_accel_ewm(ps: pd.Series) -> pd.Series:
    """EWM(5) of PS-dd-velocity 5d-diff (smoothed jerk of PS de-rating)."""
    vel   = _ps_dd_252d_5d_diff(ps)
    accel = vel.diff(_TD_WEEK)
    return _ewm_mean(accel, _TD_WEEK)


def vcl_drv3_061_pe_dd_velocity_ewm_slope_21d(pe: pd.Series) -> pd.Series:
    """OLS slope over 21 days of EWM(21)-smoothed PE-dd-velocity."""
    vel    = _pe_dd_252d_5d_diff(pe)
    smooth = _ewm_mean(vel, _TD_MON)
    return _linslope(smooth, _TD_MON)


def vcl_drv3_062_pb_dd_velocity_ewm_slope_21d(pb: pd.Series) -> pd.Series:
    """OLS slope over 21 days of EWM(21)-smoothed PB-dd-velocity."""
    vel    = _pb_dd_252d_5d_diff(pb)
    smooth = _ewm_mean(vel, _TD_MON)
    return _linslope(smooth, _TD_MON)


def vcl_drv3_063_evebit_dd_velocity_ewm_diff_5d(evebit: pd.Series) -> pd.Series:
    """5-day diff of EWM(21) of EV/EBIT-dd-velocity."""
    vel    = _evebit_dd_252d_5d_diff(evebit)
    smooth = _ewm_mean(vel, _TD_MON)
    return smooth.diff(_TD_WEEK)


def vcl_drv3_064_marketcap_dd_velocity_ewm_diff_5d(marketcap: pd.Series) -> pd.Series:
    """5-day diff of EWM(21) of marketcap-dd-velocity."""
    vel    = _marketcap_dd_252d_5d_diff(marketcap)
    smooth = _ewm_mean(vel, _TD_MON)
    return smooth.diff(_TD_WEEK)


def vcl_drv3_065_ev_dd_velocity_ewm_diff_5d(ev: pd.Series) -> pd.Series:
    """5-day diff of EWM(21) of EV-dd-velocity."""
    vel    = _ev_dd_252d_5d_diff(ev)
    smooth = _ewm_mean(vel, _TD_MON)
    return smooth.diff(_TD_WEEK)


def vcl_drv3_066_pb_ps_both_below1_frac_accel_5d(pb: pd.Series, ps: pd.Series) -> pd.Series:
    """5-day diff of 5d-diff of 252d fraction of both PB<1 and PS<1 days."""
    both = (((pb > 0) & (pb < 1.0)) & ((ps > 0) & (ps < 1.0))).astype(float)
    frac = _rolling_mean(both, _TD_YEAR)
    vel  = frac.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_067_evebitda_median_dev_accel_5d(evebitda: pd.Series) -> pd.Series:
    """5-day diff of 5d-diff of EV/EBITDA deviation from 252d rolling median."""
    p   = _positive_mask(evebitda)
    md  = _rolling_median(p, _TD_YEAR)
    dev = p - md
    vel = dev.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_068_pe_median_dev_accel_5d(pe: pd.Series) -> pd.Series:
    """5-day diff of 5d-diff of PE deviation from 252d rolling median."""
    p   = _positive_mask(pe)
    md  = _rolling_median(p, _TD_YEAR)
    dev = p - md
    vel = dev.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_069_composite_dd_velocity_ewm_slope(pe: pd.Series, pb: pd.Series,
                                                   ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """OLS slope over 21d of EWM(21) of composite-dd 5d-velocity."""
    vel    = _composite_dd_5d_diff(pe, pb, ps, evebitda)
    smooth = _ewm_mean(vel, _TD_MON)
    return _linslope(smooth, _TD_MON)


def vcl_drv3_070_evebitda_dd_expanding_accel_5d(evebitda: pd.Series) -> pd.Series:
    """5-day diff of 5d-diff of EV/EBITDA expanding-peak drawdown."""
    p    = _positive_mask(evebitda)
    peak = _expanding_max(p)
    dd   = _safe_div(p - peak, peak)
    vel  = dd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_071_ps_slope_21d_accel_5d(ps: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of 21-day PS OLS slope."""
    p     = _positive_mask(ps)
    slope = _linslope(p, _TD_MON)
    vel   = slope.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_072_evebit_slope_63d_accel_5d(evebit: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of 63-day EV/EBIT OLS slope."""
    p     = _positive_mask(evebit)
    slope = _linslope(p, _TD_QTR)
    vel   = slope.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_073_pb_compression_vol_252d_accel_5d(pb: pd.Series) -> pd.Series:
    """5-day diff of 5-day-diff of 252d PB compression volatility."""
    p   = _positive_mask(pb)
    vol = _rolling_std(p.diff(1), _TD_YEAR)
    vel = vol.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcl_drv3_074_weighted_distress_slope_21d(pe: pd.Series, pb: pd.Series,
                                              ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """OLS slope over 21 days of 5d-diff of weighted distress score."""
    s  = 0.3 * ((pe > 0) & (pe < 10)).astype(float)
    s += 0.3 * ((pb > 0) & (pb < 1.0)).astype(float)
    s += 0.2 * ((ps > 0) & (ps < 1.0)).astype(float)
    s += 0.2 * ((evebitda > 0) & (evebitda < 5)).astype(float)
    vel = s.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vcl_drv3_075_six_dd_jerk_composite(pe: pd.Series, pb: pd.Series, ps: pd.Series,
                                        evebit: pd.Series, evebitda: pd.Series,
                                        marketcap: pd.Series) -> pd.Series:
    """EWM(5) of 5d-accel of avg 252d-drawdown across PE/PB/PS/EV-EBIT/EV-EBITDA/mktcap."""
    def _dd(s, pos=True):
        p    = _positive_mask(s) if pos else s
        peak = _rolling_max(p, _TD_YEAR)
        return _safe_div(p - peak, peak).fillna(0)
    combo = (_dd(pe) + _dd(pb) + _dd(ps) + _dd(evebit) + _dd(evebitda) + _dd(marketcap, False)) / 6.0
    vel   = combo.diff(_TD_WEEK)
    accel = vel.diff(_TD_WEEK)
    return _ewm_mean(accel, _TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VALUATION_COLLAPSE_REGISTRY_3RD_DERIVATIVES = {
    "vcl_drv3_001_pe_dd_252d_5d_diff_5d_diff": {"inputs": ["pe"], "func": vcl_drv3_001_pe_dd_252d_5d_diff_5d_diff},
    "vcl_drv3_002_pb_dd_252d_5d_diff_5d_diff": {"inputs": ["pb"], "func": vcl_drv3_002_pb_dd_252d_5d_diff_5d_diff},
    "vcl_drv3_003_ps_dd_252d_5d_diff_5d_diff": {"inputs": ["ps"], "func": vcl_drv3_003_ps_dd_252d_5d_diff_5d_diff},
    "vcl_drv3_004_evebitda_dd_252d_5d_diff_5d_diff": {"inputs": ["evebitda"], "func": vcl_drv3_004_evebitda_dd_252d_5d_diff_5d_diff},
    "vcl_drv3_005_pe_dd_velocity_slope_21d": {"inputs": ["pe"], "func": vcl_drv3_005_pe_dd_velocity_slope_21d},
    "vcl_drv3_006_pb_dd_velocity_slope_21d": {"inputs": ["pb"], "func": vcl_drv3_006_pb_dd_velocity_slope_21d},
    "vcl_drv3_007_pe_dd_velocity_ewm_diff_5d": {"inputs": ["pe"], "func": vcl_drv3_007_pe_dd_velocity_ewm_diff_5d},
    "vcl_drv3_008_pb_dd_velocity_ewm_diff_5d": {"inputs": ["pb"], "func": vcl_drv3_008_pb_dd_velocity_ewm_diff_5d},
    "vcl_drv3_009_ps_dd_velocity_ewm_diff_5d": {"inputs": ["ps"], "func": vcl_drv3_009_ps_dd_velocity_ewm_diff_5d},
    "vcl_drv3_010_distress_count_5d_diff_5d_diff": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_drv3_010_distress_count_5d_diff_5d_diff},
    "vcl_drv3_011_pe_zscore_velocity_5d_diff": {"inputs": ["pe"], "func": vcl_drv3_011_pe_zscore_velocity_5d_diff},
    "vcl_drv3_012_pb_low_position_accel_5d": {"inputs": ["pb"], "func": vcl_drv3_012_pb_low_position_accel_5d},
    "vcl_drv3_013_pe_compression_speed_accel_5d": {"inputs": ["pe"], "func": vcl_drv3_013_pe_compression_speed_accel_5d},
    "vcl_drv3_014_composite_dd_velocity_slope_21d": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_drv3_014_composite_dd_velocity_slope_21d},
    "vcl_drv3_015_marketcap_dd_velocity_5d_diff": {"inputs": ["marketcap"], "func": vcl_drv3_015_marketcap_dd_velocity_5d_diff},
    "vcl_drv3_016_pb_below_1_frac_accel_5d": {"inputs": ["pb"], "func": vcl_drv3_016_pb_below_1_frac_accel_5d},
    "vcl_drv3_017_evebit_neg_frac_accel_5d": {"inputs": ["evebit"], "func": vcl_drv3_017_evebit_neg_frac_accel_5d},
    "vcl_drv3_018_pe_slope_of_slope_5d_diff": {"inputs": ["pe"], "func": vcl_drv3_018_pe_slope_of_slope_5d_diff},
    "vcl_drv3_019_pb_compression_streak_accel_5d": {"inputs": ["pb"], "func": vcl_drv3_019_pb_compression_streak_accel_5d},
    "vcl_drv3_020_pe_pb_concordance_accel_5d": {"inputs": ["pe", "pb"], "func": vcl_drv3_020_pe_pb_concordance_accel_5d},
    "vcl_drv3_021_evebitda_zscore_accel_5d": {"inputs": ["evebitda"], "func": vcl_drv3_021_evebitda_zscore_accel_5d},
    "vcl_drv3_022_ps_dd_velocity_slope_21d": {"inputs": ["ps"], "func": vcl_drv3_022_ps_dd_velocity_slope_21d},
    "vcl_drv3_023_weighted_distress_accel_5d": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_drv3_023_weighted_distress_accel_5d},
    "vcl_drv3_024_ev_to_mktcap_velocity_5d_diff": {"inputs": ["ev", "marketcap"], "func": vcl_drv3_024_ev_to_mktcap_velocity_5d_diff},
    "vcl_drv3_025_composite_dd_jerk_ewm": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_drv3_025_composite_dd_jerk_ewm},
    "vcl_drv3_026_evebit_dd_252d_5d_diff_5d_diff": {"inputs": ["evebit"], "func": vcl_drv3_026_evebit_dd_252d_5d_diff_5d_diff},
    "vcl_drv3_027_marketcap_dd_252d_accel_5d": {"inputs": ["marketcap"], "func": vcl_drv3_027_marketcap_dd_252d_accel_5d},
    "vcl_drv3_028_divyield_5d_diff_5d_diff": {"inputs": ["divyield"], "func": vcl_drv3_028_divyield_5d_diff_5d_diff},
    "vcl_drv3_029_ev_dd_252d_accel_5d": {"inputs": ["ev"], "func": vcl_drv3_029_ev_dd_252d_accel_5d},
    "vcl_drv3_030_pb_zscore_252d_accel_5d": {"inputs": ["pb"], "func": vcl_drv3_030_pb_zscore_252d_accel_5d},
    "vcl_drv3_031_ps_zscore_252d_accel_5d": {"inputs": ["ps"], "func": vcl_drv3_031_ps_zscore_252d_accel_5d},
    "vcl_drv3_032_evebit_zscore_accel_5d": {"inputs": ["evebit"], "func": vcl_drv3_032_evebit_zscore_accel_5d},
    "vcl_drv3_033_pe_dd_expanding_accel_5d": {"inputs": ["pe"], "func": vcl_drv3_033_pe_dd_expanding_accel_5d},
    "vcl_drv3_034_ps_dd_expanding_accel_5d": {"inputs": ["ps"], "func": vcl_drv3_034_ps_dd_expanding_accel_5d},
    "vcl_drv3_035_evebit_dd_velocity_slope_21d": {"inputs": ["evebit"], "func": vcl_drv3_035_evebit_dd_velocity_slope_21d},
    "vcl_drv3_036_marketcap_dd_velocity_slope_21d": {"inputs": ["marketcap"], "func": vcl_drv3_036_marketcap_dd_velocity_slope_21d},
    "vcl_drv3_037_divyield_velocity_slope_21d": {"inputs": ["divyield"], "func": vcl_drv3_037_divyield_velocity_slope_21d},
    "vcl_drv3_038_ev_dd_velocity_slope_21d": {"inputs": ["ev"], "func": vcl_drv3_038_ev_dd_velocity_slope_21d},
    "vcl_drv3_039_composite_dd_accel_ewm": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_drv3_039_composite_dd_accel_ewm},
    "vcl_drv3_040_pe_slope_21d_accel_5d": {"inputs": ["pe"], "func": vcl_drv3_040_pe_slope_21d_accel_5d},
    "vcl_drv3_041_pb_slope_63d_accel_5d": {"inputs": ["pb"], "func": vcl_drv3_041_pb_slope_63d_accel_5d},
    "vcl_drv3_042_ps_low_position_accel_5d": {"inputs": ["ps"], "func": vcl_drv3_042_ps_low_position_accel_5d},
    "vcl_drv3_043_evebitda_slope_63d_accel_5d": {"inputs": ["evebitda"], "func": vcl_drv3_043_evebitda_slope_63d_accel_5d},
    "vcl_drv3_044_pb_below_1_frac_accel_21d": {"inputs": ["pb"], "func": vcl_drv3_044_pb_below_1_frac_accel_21d},
    "vcl_drv3_045_evebit_neg_frac_accel_21d": {"inputs": ["evebit"], "func": vcl_drv3_045_evebit_neg_frac_accel_21d},
    "vcl_drv3_046_distress_count_accel_21d": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_drv3_046_distress_count_accel_21d},
    "vcl_drv3_047_pe_dd_504d_accel_5d": {"inputs": ["pe"], "func": vcl_drv3_047_pe_dd_504d_accel_5d},
    "vcl_drv3_048_pb_dd_504d_accel_5d": {"inputs": ["pb"], "func": vcl_drv3_048_pb_dd_504d_accel_5d},
    "vcl_drv3_049_ps_dd_504d_accel_5d": {"inputs": ["ps"], "func": vcl_drv3_049_ps_dd_504d_accel_5d},
    "vcl_drv3_050_evebitda_dd_504d_accel_5d": {"inputs": ["evebitda"], "func": vcl_drv3_050_evebitda_dd_504d_accel_5d},
    "vcl_drv3_051_pe_compression_streak_63d_accel_5d": {"inputs": ["pe"], "func": vcl_drv3_051_pe_compression_streak_63d_accel_5d},
    "vcl_drv3_052_ps_compression_streak_252d_accel_5d": {"inputs": ["ps"], "func": vcl_drv3_052_ps_compression_streak_252d_accel_5d},
    "vcl_drv3_053_evebitda_below_5_frac_accel_5d": {"inputs": ["evebitda"], "func": vcl_drv3_053_evebitda_below_5_frac_accel_5d},
    "vcl_drv3_054_ev_to_mktcap_accel_5d": {"inputs": ["ev", "marketcap"], "func": vcl_drv3_054_ev_to_mktcap_accel_5d},
    "vcl_drv3_055_divyield_5d_diff_slope_21d": {"inputs": ["divyield"], "func": vcl_drv3_055_divyield_5d_diff_slope_21d},
    "vcl_drv3_056_pe_compression_speed_slope_21d": {"inputs": ["pe"], "func": vcl_drv3_056_pe_compression_speed_slope_21d},
    "vcl_drv3_057_pb_compression_speed_slope_21d": {"inputs": ["pb"], "func": vcl_drv3_057_pb_compression_speed_slope_21d},
    "vcl_drv3_058_marketcap_zscore_accel_5d": {"inputs": ["marketcap"], "func": vcl_drv3_058_marketcap_zscore_accel_5d},
    "vcl_drv3_059_pe_pb_concordance_slope_21d": {"inputs": ["pe", "pb"], "func": vcl_drv3_059_pe_pb_concordance_slope_21d},
    "vcl_drv3_060_ps_dd_252d_accel_ewm": {"inputs": ["ps"], "func": vcl_drv3_060_ps_dd_252d_accel_ewm},
    "vcl_drv3_061_pe_dd_velocity_ewm_slope_21d": {"inputs": ["pe"], "func": vcl_drv3_061_pe_dd_velocity_ewm_slope_21d},
    "vcl_drv3_062_pb_dd_velocity_ewm_slope_21d": {"inputs": ["pb"], "func": vcl_drv3_062_pb_dd_velocity_ewm_slope_21d},
    "vcl_drv3_063_evebit_dd_velocity_ewm_diff_5d": {"inputs": ["evebit"], "func": vcl_drv3_063_evebit_dd_velocity_ewm_diff_5d},
    "vcl_drv3_064_marketcap_dd_velocity_ewm_diff_5d": {"inputs": ["marketcap"], "func": vcl_drv3_064_marketcap_dd_velocity_ewm_diff_5d},
    "vcl_drv3_065_ev_dd_velocity_ewm_diff_5d": {"inputs": ["ev"], "func": vcl_drv3_065_ev_dd_velocity_ewm_diff_5d},
    "vcl_drv3_066_pb_ps_both_below1_frac_accel_5d": {"inputs": ["pb", "ps"], "func": vcl_drv3_066_pb_ps_both_below1_frac_accel_5d},
    "vcl_drv3_067_evebitda_median_dev_accel_5d": {"inputs": ["evebitda"], "func": vcl_drv3_067_evebitda_median_dev_accel_5d},
    "vcl_drv3_068_pe_median_dev_accel_5d": {"inputs": ["pe"], "func": vcl_drv3_068_pe_median_dev_accel_5d},
    "vcl_drv3_069_composite_dd_velocity_ewm_slope": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_drv3_069_composite_dd_velocity_ewm_slope},
    "vcl_drv3_070_evebitda_dd_expanding_accel_5d": {"inputs": ["evebitda"], "func": vcl_drv3_070_evebitda_dd_expanding_accel_5d},
    "vcl_drv3_071_ps_slope_21d_accel_5d": {"inputs": ["ps"], "func": vcl_drv3_071_ps_slope_21d_accel_5d},
    "vcl_drv3_072_evebit_slope_63d_accel_5d": {"inputs": ["evebit"], "func": vcl_drv3_072_evebit_slope_63d_accel_5d},
    "vcl_drv3_073_pb_compression_vol_252d_accel_5d": {"inputs": ["pb"], "func": vcl_drv3_073_pb_compression_vol_252d_accel_5d},
    "vcl_drv3_074_weighted_distress_slope_21d": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_drv3_074_weighted_distress_slope_21d},
    "vcl_drv3_075_six_dd_jerk_composite": {"inputs": ["pe", "pb", "ps", "evebit", "evebitda", "marketcap"], "func": vcl_drv3_075_six_dd_jerk_composite},
}
