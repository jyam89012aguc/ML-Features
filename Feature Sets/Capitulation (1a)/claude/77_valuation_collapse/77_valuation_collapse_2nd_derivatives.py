"""
77_valuation_collapse — 2nd Derivatives (Features drv2_001-075)
Domain: rate of change / velocity of base valuation-collapse features.
Inputs: Sharadar DAILY/METRICS valuation fields (daily frequency):
    marketcap, ev, pe, pb, ps, evebit, evebitda, divyield
These are native daily-frequency series (price moves daily; fundamental denominator
steps quarterly). No quarterly forward-fill alignment is needed here.
Each feature computes a .diff(n), slope, or pct-change of a base-feature concept.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def vcl_drv2_001_pe_dd_252d_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of PE's 252-day drawdown (velocity of PE de-rating)."""
    p    = _positive_mask(pe)
    peak = _rolling_max(p, _TD_YEAR)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_WEEK)


def vcl_drv2_002_pb_dd_252d_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of PB's 252-day drawdown (velocity of PB de-rating)."""
    p    = _positive_mask(pb)
    peak = _rolling_max(p, _TD_YEAR)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_WEEK)


def vcl_drv2_003_ps_dd_252d_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of PS's 252-day drawdown (velocity of PS de-rating)."""
    p    = _positive_mask(ps)
    peak = _rolling_max(p, _TD_YEAR)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_WEEK)


def vcl_drv2_004_evebitda_dd_252d_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5-day diff of EV/EBITDA 252-day drawdown (velocity of EV de-rating)."""
    p    = _positive_mask(evebitda)
    peak = _rolling_max(p, _TD_YEAR)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_WEEK)


def vcl_drv2_005_pe_dd_expanding_21d_diff(pe: pd.Series) -> pd.Series:
    """21-day diff of PE's all-history expanding-peak drawdown (monthly worsening pace)."""
    p    = _positive_mask(pe)
    peak = _expanding_max(p)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_MON)


def vcl_drv2_006_pb_dd_expanding_21d_diff(pb: pd.Series) -> pd.Series:
    """21-day diff of PB's expanding-peak drawdown."""
    p    = _positive_mask(pb)
    peak = _expanding_max(p)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_MON)


def vcl_drv2_007_pe_zscore_252d_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of 252-day PE z-score (acceleration of statistical extremity)."""
    p  = _positive_mask(pe)
    zs = _zscore_rolling(p, _TD_YEAR)
    return zs.diff(_TD_WEEK)


def vcl_drv2_008_pb_below_1_fraction_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of rolling fraction of days where PB < 1 (pace of distress deepening)."""
    flag = ((pb > 0) & (pb < 1.0)).astype(float)
    frac = _rolling_mean(flag, _TD_YEAR)
    return frac.diff(_TD_WEEK)


def vcl_drv2_009_distress_count_5d_diff(pe: pd.Series, pb: pd.Series,
                                          ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """5-day diff of distress-threshold count (PE<10, PB<1, PS<1, EV/EBITDA<5)."""
    count  = ((pe > 0) & (pe < 10)).astype(float)
    count += ((pb > 0) & (pb < 1.0)).astype(float)
    count += ((ps > 0) & (ps < 1.0)).astype(float)
    count += ((evebitda > 0) & (evebitda < 5)).astype(float)
    return count.diff(_TD_WEEK)


def vcl_drv2_010_pe_compression_speed_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of the 21-day PE compression speed (acceleration of de-rating)."""
    p     = _positive_mask(pe)
    speed = _safe_div(p - p.shift(_TD_MON), pd.Series(_TD_MON, index=p.index))
    return speed.diff(_TD_WEEK)


def vcl_drv2_011_composite_dd_21d_diff(pe: pd.Series, pb: pd.Series,
                                        ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """21-day diff of composite 252-day drawdown (monthly change in multi-multiple de-rating)."""
    def _dd252(s):
        p    = _positive_mask(s)
        peak = _rolling_max(p, _TD_YEAR)
        return _safe_div(p - peak, peak).fillna(0)
    combo = (_dd252(pe) + _dd252(pb) + _dd252(ps) + _dd252(evebitda)) / 4.0
    return combo.diff(_TD_MON)


def vcl_drv2_012_pb_low_position_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of PB's 252-day range position (speed of moving toward the low)."""
    p  = _positive_mask(pb)
    hi = _rolling_max(p, _TD_YEAR)
    lo = _rolling_min(p, _TD_YEAR)
    pos = _safe_div(p - lo, hi - lo)
    return pos.diff(_TD_WEEK)


def vcl_drv2_013_ps_low_position_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of PS's 252-day range position."""
    p  = _positive_mask(ps)
    hi = _rolling_max(p, _TD_YEAR)
    lo = _rolling_min(p, _TD_YEAR)
    pos = _safe_div(p - lo, hi - lo)
    return pos.diff(_TD_WEEK)


def vcl_drv2_014_marketcap_dd_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of market-cap 252-day drawdown (equity destruction velocity)."""
    peak = _rolling_max(marketcap, _TD_YEAR)
    dd   = _safe_div(marketcap - peak, peak)
    return dd.diff(_TD_WEEK)


def vcl_drv2_015_evebit_negative_frac_5d_diff(evebit: pd.Series) -> pd.Series:
    """5-day diff of 252-day fraction where EV/EBIT is negative (pace of EBIT loss)."""
    flag = (evebit < 0).astype(float)
    frac = _rolling_mean(flag, _TD_YEAR)
    return frac.diff(_TD_WEEK)


def vcl_drv2_016_pe_slope_21d_of_slope(pe: pd.Series) -> pd.Series:
    """21-day OLS slope of the 21-day PE slope (second derivative of PE trend)."""
    p     = _positive_mask(pe)
    slope = _linslope(p, _TD_MON)
    return _linslope(slope, _TD_MON)


def vcl_drv2_017_pb_compression_streak_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of rolling 63-day PB compression streak sum."""
    p      = _positive_mask(pb)
    neg_ch = p.diff(1).where(p.diff(1) < 0, 0.0)
    streak = _rolling_sum(neg_ch, _TD_QTR)
    return streak.diff(_TD_WEEK)


def vcl_drv2_018_evebitda_zscore_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5-day diff of 252-day EV/EBITDA z-score."""
    p  = _positive_mask(evebitda)
    zs = _zscore_rolling(p, _TD_YEAR)
    return zs.diff(_TD_WEEK)


def vcl_drv2_019_pe_pb_concordance_5d_diff(pe: pd.Series, pb: pd.Series) -> pd.Series:
    """5-day diff of joint PE+PB compression concordance fraction."""
    pe_dec = (pe.diff(1) < 0).astype(float)
    pb_dec = (pb.diff(1) < 0).astype(float)
    conc   = _rolling_mean(pe_dec * pb_dec, _TD_YEAR)
    return conc.diff(_TD_WEEK)


def vcl_drv2_020_negative_multiple_count_5d_diff(pe: pd.Series, evebit: pd.Series,
                                                   evebitda: pd.Series) -> pd.Series:
    """5-day diff of count of negative multiples (PE, EV/EBIT, EV/EBITDA)."""
    count = ((pe < 0).astype(float) + (evebit < 0).astype(float) +
             (evebitda < 0).astype(float))
    return count.diff(_TD_WEEK)


def vcl_drv2_021_pe_dd_504d_21d_diff(pe: pd.Series) -> pd.Series:
    """21-day diff of PE's 504-day drawdown."""
    p    = _positive_mask(pe)
    peak = _rolling_max(p, 504)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_MON)


def vcl_drv2_022_pb_ps_both_below1_5d_diff(pb: pd.Series, ps: pd.Series) -> pd.Series:
    """5-day diff of rolling 252-day fraction where both PB<1 and PS<1."""
    both = (((pb > 0) & (pb < 1.0)) & ((ps > 0) & (ps < 1.0))).astype(float)
    frac = _rolling_mean(both, _TD_YEAR)
    return frac.diff(_TD_WEEK)


def vcl_drv2_023_ev_to_marketcap_5d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """5-day diff of EV/marketcap ratio (change in leverage multiple)."""
    ratio = _safe_div(_positive_mask(ev), _positive_mask(marketcap))
    return ratio.diff(_TD_WEEK)


def vcl_drv2_024_ps_dd_expanding_21d_diff(ps: pd.Series) -> pd.Series:
    """21-day diff of PS's all-history expanding-peak drawdown."""
    p    = _positive_mask(ps)
    peak = _expanding_max(p)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_MON)


def vcl_drv2_025_weighted_distress_5d_diff(pe: pd.Series, pb: pd.Series,
                                            ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """5-day diff of the weighted distress score (0.3*PE<10 + 0.3*PB<1 + 0.2*PS<1 + 0.2*EVDA<5)."""
    s  = 0.3 * ((pe > 0) & (pe < 10)).astype(float)
    s += 0.3 * ((pb > 0) & (pb < 1.0)).astype(float)
    s += 0.2 * ((ps > 0) & (ps < 1.0)).astype(float)
    s += 0.2 * ((evebitda > 0) & (evebitda < 5)).astype(float)
    return s.diff(_TD_WEEK)


# ── 2nd-Derivative Feature Functions 026-075 ─────────────────────────────────

def vcl_drv2_026_evebit_dd_252d_5d_diff(evebit: pd.Series) -> pd.Series:
    """5-day diff of EV/EBIT 252-day drawdown (velocity of EV/EBIT de-rating)."""
    p    = _positive_mask(evebit)
    peak = _rolling_max(p, _TD_YEAR)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_WEEK)


def vcl_drv2_027_marketcap_dd_expanding_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of marketcap expanding-peak drawdown (velocity of equity destruction)."""
    peak = _expanding_max(marketcap)
    dd   = _safe_div(marketcap - peak, peak)
    return dd.diff(_TD_WEEK)


def vcl_drv2_028_pe_zscore_252d_21d_diff(pe: pd.Series) -> pd.Series:
    """21-day diff of PE 252-day z-score (monthly acceleration of statistical extremity)."""
    p  = _positive_mask(pe)
    zs = _zscore_rolling(p, _TD_YEAR)
    return zs.diff(_TD_MON)


def vcl_drv2_029_pb_zscore_252d_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of PB 252-day z-score (velocity of PB statistical extremity)."""
    p  = _positive_mask(pb)
    zs = _zscore_rolling(p, _TD_YEAR)
    return zs.diff(_TD_WEEK)


def vcl_drv2_030_ps_zscore_252d_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of PS 252-day z-score."""
    p  = _positive_mask(ps)
    zs = _zscore_rolling(p, _TD_YEAR)
    return zs.diff(_TD_WEEK)


def vcl_drv2_031_evebitda_dd_504d_21d_diff(evebitda: pd.Series) -> pd.Series:
    """21-day diff of EV/EBITDA 504-day drawdown."""
    p    = _positive_mask(evebitda)
    peak = _rolling_max(p, 504)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_MON)


def vcl_drv2_032_pe_low_position_252d_21d_diff(pe: pd.Series) -> pd.Series:
    """21-day diff of PE's 252-day range position (monthly speed toward the low)."""
    p   = _positive_mask(pe)
    hi  = _rolling_max(p, _TD_YEAR)
    lo  = _rolling_min(p, _TD_YEAR)
    pos = _safe_div(p - lo, hi - lo)
    return pos.diff(_TD_MON)


def vcl_drv2_033_marketcap_zscore_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of marketcap 252-day z-score."""
    zs = _zscore_rolling(marketcap, _TD_YEAR)
    return zs.diff(_TD_WEEK)


def vcl_drv2_034_divyield_5d_diff(divyield: pd.Series) -> pd.Series:
    """5-day diff of dividend yield (velocity of yield spike / price collapse)."""
    return divyield.diff(_TD_WEEK)


def vcl_drv2_035_divyield_21d_diff(divyield: pd.Series) -> pd.Series:
    """21-day diff of dividend yield (monthly pace of yield expansion)."""
    return divyield.diff(_TD_MON)


def vcl_drv2_036_ev_dd_252d_5d_diff(ev: pd.Series) -> pd.Series:
    """5-day diff of EV 252-day drawdown (velocity of enterprise value collapse)."""
    p    = _positive_mask(ev)
    peak = _rolling_max(p, _TD_YEAR)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_WEEK)


def vcl_drv2_037_pb_dd_504d_21d_diff(pb: pd.Series) -> pd.Series:
    """21-day diff of PB 504-day drawdown."""
    p    = _positive_mask(pb)
    peak = _rolling_max(p, 504)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_MON)


def vcl_drv2_038_ps_dd_504d_21d_diff(ps: pd.Series) -> pd.Series:
    """21-day diff of PS 504-day drawdown."""
    p    = _positive_mask(ps)
    peak = _rolling_max(p, 504)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_MON)


def vcl_drv2_039_evebit_negative_frac_21d_diff(evebit: pd.Series) -> pd.Series:
    """21-day diff of 252-day EV/EBIT negative fraction."""
    flag = (evebit < 0).astype(float)
    frac = _rolling_mean(flag, _TD_YEAR)
    return frac.diff(_TD_MON)


def vcl_drv2_040_pe_compression_streak_63d_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of 63-day PE compression streak sum."""
    p      = _positive_mask(pe)
    neg_ch = p.diff(1).where(p.diff(1) < 0, 0.0)
    streak = _rolling_sum(neg_ch, _TD_QTR)
    return streak.diff(_TD_WEEK)


def vcl_drv2_041_ps_compression_streak_252d_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of 252-day PS compression streak sum."""
    p      = _positive_mask(ps)
    neg_ch = p.diff(1).where(p.diff(1) < 0, 0.0)
    streak = _rolling_sum(neg_ch, _TD_YEAR)
    return streak.diff(_TD_WEEK)


def vcl_drv2_042_evebitda_below_5_frac_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5-day diff of 252-day fraction of EV/EBITDA<5 days."""
    flag = ((evebitda > 0) & (evebitda < 5)).astype(float)
    frac = _rolling_mean(flag, _TD_YEAR)
    return frac.diff(_TD_WEEK)


def vcl_drv2_043_pe_slope_21d_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of 21-day OLS PE slope (acceleration of compression trend)."""
    p     = _positive_mask(pe)
    slope = _linslope(p, _TD_MON)
    return slope.diff(_TD_WEEK)


def vcl_drv2_044_pb_slope_63d_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of 63-day OLS PB slope."""
    p     = _positive_mask(pb)
    slope = _linslope(p, _TD_QTR)
    return slope.diff(_TD_WEEK)


def vcl_drv2_045_ps_slope_63d_21d_diff(ps: pd.Series) -> pd.Series:
    """21-day diff of 63-day OLS PS slope."""
    p     = _positive_mask(ps)
    slope = _linslope(p, _TD_QTR)
    return slope.diff(_TD_MON)


def vcl_drv2_046_pe_dd_expanding_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of PE all-history expanding-peak drawdown."""
    p    = _positive_mask(pe)
    peak = _expanding_max(p)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_WEEK)


def vcl_drv2_047_evebit_dd_expanding_21d_diff(evebit: pd.Series) -> pd.Series:
    """21-day diff of EV/EBIT expanding-peak drawdown."""
    p    = _positive_mask(evebit)
    peak = _expanding_max(p)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_MON)


def vcl_drv2_048_pb_median_dev_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of PB deviation from its 252-day rolling median."""
    p  = _positive_mask(pb)
    md = _rolling_median(p, _TD_YEAR)
    return (p - md).diff(_TD_WEEK)


def vcl_drv2_049_pe_median_dev_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of PE deviation from its 252-day rolling median."""
    p  = _positive_mask(pe)
    md = _rolling_median(p, _TD_YEAR)
    return (p - md).diff(_TD_WEEK)


def vcl_drv2_050_composite_dd_5d_diff(pe: pd.Series, pb: pd.Series,
                                       ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """5-day diff of composite 252-day drawdown (weekly velocity of multi-multiple de-rating)."""
    def _dd252(s):
        p    = _positive_mask(s)
        peak = _rolling_max(p, _TD_YEAR)
        return _safe_div(p - peak, peak).fillna(0)
    combo = (_dd252(pe) + _dd252(pb) + _dd252(ps) + _dd252(evebitda)) / 4.0
    return combo.diff(_TD_WEEK)


def vcl_drv2_051_marketcap_compression_pct_63d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of 63-day marketcap pct compression."""
    pct = _safe_div(marketcap - marketcap.shift(_TD_QTR),
                    marketcap.shift(_TD_QTR).replace(0, np.nan))
    return pct.diff(_TD_WEEK)


def vcl_drv2_052_ev_zscore_252d_5d_diff(ev: pd.Series) -> pd.Series:
    """5-day diff of EV 252-day z-score."""
    p  = _positive_mask(ev)
    zs = _zscore_rolling(p, _TD_YEAR)
    return zs.diff(_TD_WEEK)


def vcl_drv2_053_pb_below_1_frac_21d_diff(pb: pd.Series) -> pd.Series:
    """21-day diff of fraction of PB<1 days in 252-day window."""
    flag = ((pb > 0) & (pb < 1.0)).astype(float)
    frac = _rolling_mean(flag, _TD_YEAR)
    return frac.diff(_TD_MON)


def vcl_drv2_054_ps_below_1_frac_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of 252-day fraction of PS<1 days."""
    flag = ((ps > 0) & (ps < 1.0)).astype(float)
    frac = _rolling_mean(flag, _TD_YEAR)
    return frac.diff(_TD_WEEK)


def vcl_drv2_055_evebit_compression_pct_252d_5d_diff(evebit: pd.Series) -> pd.Series:
    """5-day diff of 252-day EV/EBIT pct compression."""
    p   = _positive_mask(evebit)
    pct = _safe_div(p - p.shift(_TD_YEAR), p.shift(_TD_YEAR).replace(0, np.nan))
    return pct.diff(_TD_WEEK)


def vcl_drv2_056_evebitda_compression_pct_252d_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5-day diff of 252-day EV/EBITDA pct compression."""
    p   = _positive_mask(evebitda)
    pct = _safe_div(p - p.shift(_TD_YEAR), p.shift(_TD_YEAR).replace(0, np.nan))
    return pct.diff(_TD_WEEK)


def vcl_drv2_057_pe_compression_vol_63d_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of 63-day PE compression volatility (std of daily changes)."""
    p   = _positive_mask(pe)
    vol = _rolling_std(p.diff(1), _TD_QTR)
    return vol.diff(_TD_WEEK)


def vcl_drv2_058_pb_compression_vol_252d_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of 252-day PB compression volatility."""
    p   = _positive_mask(pb)
    vol = _rolling_std(p.diff(1), _TD_YEAR)
    return vol.diff(_TD_WEEK)


def vcl_drv2_059_pb_ps_concordance_21d_diff(pb: pd.Series, ps: pd.Series) -> pd.Series:
    """21-day diff of 252-day PB+PS joint compression concordance fraction."""
    pb_dec = (pb.diff(1) < 0).astype(float)
    ps_dec = (ps.diff(1) < 0).astype(float)
    conc   = _rolling_mean(pb_dec * ps_dec, _TD_YEAR)
    return conc.diff(_TD_MON)


def vcl_drv2_060_evebit_evebitda_spread_5d_diff(evebit: pd.Series, evebitda: pd.Series) -> pd.Series:
    """5-day diff of EV/EBIT minus EV/EBITDA spread (DA wedge velocity)."""
    spread = _positive_mask(evebit) - _positive_mask(evebitda)
    return spread.diff(_TD_WEEK)


def vcl_drv2_061_pe_pb_ratio_5d_diff(pe: pd.Series, pb: pd.Series) -> pd.Series:
    """5-day diff of PE/PB ratio (velocity of earnings vs book multiple divergence)."""
    ratio = _safe_div(_positive_mask(pe), _positive_mask(pb))
    return ratio.diff(_TD_WEEK)


def vcl_drv2_062_pb_ps_spread_5d_diff(pb: pd.Series, ps: pd.Series) -> pd.Series:
    """5-day diff of PB minus PS spread (velocity of book vs sales compression gap)."""
    spread = _positive_mask(pb) - _positive_mask(ps)
    return spread.diff(_TD_WEEK)


def vcl_drv2_063_marketcap_dd_504d_21d_diff(marketcap: pd.Series) -> pd.Series:
    """21-day diff of marketcap 504-day drawdown."""
    peak = _rolling_max(marketcap, 504)
    dd   = _safe_div(marketcap - peak, peak)
    return dd.diff(_TD_MON)


def vcl_drv2_064_divyield_zscore_252d_5d_diff(divyield: pd.Series) -> pd.Series:
    """5-day diff of 252-day divyield z-score."""
    zs = _zscore_rolling(divyield, _TD_YEAR)
    return zs.diff(_TD_WEEK)


def vcl_drv2_065_pe_ewm_deviation_21d_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of PE deviation from its 21-day EWM."""
    p = _positive_mask(pe)
    dev = p - _ewm_mean(p, _TD_MON)
    return dev.diff(_TD_WEEK)


def vcl_drv2_066_pb_rate_derating_126d_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of PB annualized 126-day de-rating rate."""
    p   = _positive_mask(pb)
    chg = p - p.shift(_TD_HALF)
    rate = _safe_div(chg * _TD_YEAR, pd.Series(_TD_HALF, index=p.index))
    return rate.diff(_TD_WEEK)


def vcl_drv2_067_evebitda_slope_63d_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5-day diff of 63-day OLS EV/EBITDA slope."""
    p     = _positive_mask(evebitda)
    slope = _linslope(p, _TD_QTR)
    return slope.diff(_TD_WEEK)


def vcl_drv2_068_ps_rate_derating_126d_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of PS annualized 126-day de-rating rate."""
    p    = _positive_mask(ps)
    chg  = p - p.shift(_TD_HALF)
    rate = _safe_div(chg * _TD_YEAR, pd.Series(_TD_HALF, index=p.index))
    return rate.diff(_TD_WEEK)


def vcl_drv2_069_pe_dd_1260d_21d_diff(pe: pd.Series) -> pd.Series:
    """21-day diff of PE 1260-day drawdown (monthly speed of 5-year de-rating)."""
    p    = _positive_mask(pe)
    peak = _rolling_max(p, 1260)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_MON)


def vcl_drv2_070_pb_dd_1260d_21d_diff(pb: pd.Series) -> pd.Series:
    """21-day diff of PB 1260-day drawdown."""
    p    = _positive_mask(pb)
    peak = _rolling_max(p, 1260)
    dd   = _safe_div(p - peak, peak)
    return dd.diff(_TD_MON)


def vcl_drv2_071_evebit_zscore_252d_5d_diff(evebit: pd.Series) -> pd.Series:
    """5-day diff of EV/EBIT 252-day z-score."""
    p  = _positive_mask(evebit)
    zs = _zscore_rolling(p, _TD_YEAR)
    return zs.diff(_TD_WEEK)


def vcl_drv2_072_ev_to_mktcap_21d_diff(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """21-day diff of EV/marketcap ratio (monthly change in leverage)."""
    ratio = _safe_div(_positive_mask(ev), _positive_mask(marketcap))
    return ratio.diff(_TD_MON)


def vcl_drv2_073_distress_count_21d_diff(pe: pd.Series, pb: pd.Series,
                                          ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """21-day diff of distress threshold count (monthly worsening of distress score)."""
    count  = ((pe > 0) & (pe < 10)).astype(float)
    count += ((pb > 0) & (pb < 1.0)).astype(float)
    count += ((ps > 0) & (ps < 1.0)).astype(float)
    count += ((evebitda > 0) & (evebitda < 5)).astype(float)
    return count.diff(_TD_MON)


def vcl_drv2_074_pb_compression_speed_21d_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of 21-day PB compression speed (acceleration of book de-rating)."""
    p     = _positive_mask(pb)
    speed = _safe_div(p - p.shift(_TD_MON), pd.Series(_TD_MON, index=p.index))
    return speed.diff(_TD_WEEK)


def vcl_drv2_075_ps_compression_speed_63d_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of 63-day PS compression speed."""
    p     = _positive_mask(ps)
    speed = _safe_div(p - p.shift(_TD_QTR), pd.Series(_TD_QTR, index=p.index))
    return speed.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VALUATION_COLLAPSE_REGISTRY_2ND_DERIVATIVES = {
    "vcl_drv2_001_pe_dd_252d_5d_diff": {"inputs": ["pe"], "func": vcl_drv2_001_pe_dd_252d_5d_diff},
    "vcl_drv2_002_pb_dd_252d_5d_diff": {"inputs": ["pb"], "func": vcl_drv2_002_pb_dd_252d_5d_diff},
    "vcl_drv2_003_ps_dd_252d_5d_diff": {"inputs": ["ps"], "func": vcl_drv2_003_ps_dd_252d_5d_diff},
    "vcl_drv2_004_evebitda_dd_252d_5d_diff": {"inputs": ["evebitda"], "func": vcl_drv2_004_evebitda_dd_252d_5d_diff},
    "vcl_drv2_005_pe_dd_expanding_21d_diff": {"inputs": ["pe"], "func": vcl_drv2_005_pe_dd_expanding_21d_diff},
    "vcl_drv2_006_pb_dd_expanding_21d_diff": {"inputs": ["pb"], "func": vcl_drv2_006_pb_dd_expanding_21d_diff},
    "vcl_drv2_007_pe_zscore_252d_5d_diff": {"inputs": ["pe"], "func": vcl_drv2_007_pe_zscore_252d_5d_diff},
    "vcl_drv2_008_pb_below_1_fraction_5d_diff": {"inputs": ["pb"], "func": vcl_drv2_008_pb_below_1_fraction_5d_diff},
    "vcl_drv2_009_distress_count_5d_diff": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_drv2_009_distress_count_5d_diff},
    "vcl_drv2_010_pe_compression_speed_5d_diff": {"inputs": ["pe"], "func": vcl_drv2_010_pe_compression_speed_5d_diff},
    "vcl_drv2_011_composite_dd_21d_diff": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_drv2_011_composite_dd_21d_diff},
    "vcl_drv2_012_pb_low_position_5d_diff": {"inputs": ["pb"], "func": vcl_drv2_012_pb_low_position_5d_diff},
    "vcl_drv2_013_ps_low_position_5d_diff": {"inputs": ["ps"], "func": vcl_drv2_013_ps_low_position_5d_diff},
    "vcl_drv2_014_marketcap_dd_252d_5d_diff": {"inputs": ["marketcap"], "func": vcl_drv2_014_marketcap_dd_252d_5d_diff},
    "vcl_drv2_015_evebit_negative_frac_5d_diff": {"inputs": ["evebit"], "func": vcl_drv2_015_evebit_negative_frac_5d_diff},
    "vcl_drv2_016_pe_slope_21d_of_slope": {"inputs": ["pe"], "func": vcl_drv2_016_pe_slope_21d_of_slope},
    "vcl_drv2_017_pb_compression_streak_5d_diff": {"inputs": ["pb"], "func": vcl_drv2_017_pb_compression_streak_5d_diff},
    "vcl_drv2_018_evebitda_zscore_5d_diff": {"inputs": ["evebitda"], "func": vcl_drv2_018_evebitda_zscore_5d_diff},
    "vcl_drv2_019_pe_pb_concordance_5d_diff": {"inputs": ["pe", "pb"], "func": vcl_drv2_019_pe_pb_concordance_5d_diff},
    "vcl_drv2_020_negative_multiple_count_5d_diff": {"inputs": ["pe", "evebit", "evebitda"], "func": vcl_drv2_020_negative_multiple_count_5d_diff},
    "vcl_drv2_021_pe_dd_504d_21d_diff": {"inputs": ["pe"], "func": vcl_drv2_021_pe_dd_504d_21d_diff},
    "vcl_drv2_022_pb_ps_both_below1_5d_diff": {"inputs": ["pb", "ps"], "func": vcl_drv2_022_pb_ps_both_below1_5d_diff},
    "vcl_drv2_023_ev_to_marketcap_5d_diff": {"inputs": ["ev", "marketcap"], "func": vcl_drv2_023_ev_to_marketcap_5d_diff},
    "vcl_drv2_024_ps_dd_expanding_21d_diff": {"inputs": ["ps"], "func": vcl_drv2_024_ps_dd_expanding_21d_diff},
    "vcl_drv2_025_weighted_distress_5d_diff": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_drv2_025_weighted_distress_5d_diff},
    "vcl_drv2_026_evebit_dd_252d_5d_diff": {"inputs": ["evebit"], "func": vcl_drv2_026_evebit_dd_252d_5d_diff},
    "vcl_drv2_027_marketcap_dd_expanding_5d_diff": {"inputs": ["marketcap"], "func": vcl_drv2_027_marketcap_dd_expanding_5d_diff},
    "vcl_drv2_028_pe_zscore_252d_21d_diff": {"inputs": ["pe"], "func": vcl_drv2_028_pe_zscore_252d_21d_diff},
    "vcl_drv2_029_pb_zscore_252d_5d_diff": {"inputs": ["pb"], "func": vcl_drv2_029_pb_zscore_252d_5d_diff},
    "vcl_drv2_030_ps_zscore_252d_5d_diff": {"inputs": ["ps"], "func": vcl_drv2_030_ps_zscore_252d_5d_diff},
    "vcl_drv2_031_evebitda_dd_504d_21d_diff": {"inputs": ["evebitda"], "func": vcl_drv2_031_evebitda_dd_504d_21d_diff},
    "vcl_drv2_032_pe_low_position_252d_21d_diff": {"inputs": ["pe"], "func": vcl_drv2_032_pe_low_position_252d_21d_diff},
    "vcl_drv2_033_marketcap_zscore_252d_5d_diff": {"inputs": ["marketcap"], "func": vcl_drv2_033_marketcap_zscore_252d_5d_diff},
    "vcl_drv2_034_divyield_5d_diff": {"inputs": ["divyield"], "func": vcl_drv2_034_divyield_5d_diff},
    "vcl_drv2_035_divyield_21d_diff": {"inputs": ["divyield"], "func": vcl_drv2_035_divyield_21d_diff},
    "vcl_drv2_036_ev_dd_252d_5d_diff": {"inputs": ["ev"], "func": vcl_drv2_036_ev_dd_252d_5d_diff},
    "vcl_drv2_037_pb_dd_504d_21d_diff": {"inputs": ["pb"], "func": vcl_drv2_037_pb_dd_504d_21d_diff},
    "vcl_drv2_038_ps_dd_504d_21d_diff": {"inputs": ["ps"], "func": vcl_drv2_038_ps_dd_504d_21d_diff},
    "vcl_drv2_039_evebit_negative_frac_21d_diff": {"inputs": ["evebit"], "func": vcl_drv2_039_evebit_negative_frac_21d_diff},
    "vcl_drv2_040_pe_compression_streak_63d_5d_diff": {"inputs": ["pe"], "func": vcl_drv2_040_pe_compression_streak_63d_5d_diff},
    "vcl_drv2_041_ps_compression_streak_252d_5d_diff": {"inputs": ["ps"], "func": vcl_drv2_041_ps_compression_streak_252d_5d_diff},
    "vcl_drv2_042_evebitda_below_5_frac_5d_diff": {"inputs": ["evebitda"], "func": vcl_drv2_042_evebitda_below_5_frac_5d_diff},
    "vcl_drv2_043_pe_slope_21d_5d_diff": {"inputs": ["pe"], "func": vcl_drv2_043_pe_slope_21d_5d_diff},
    "vcl_drv2_044_pb_slope_63d_5d_diff": {"inputs": ["pb"], "func": vcl_drv2_044_pb_slope_63d_5d_diff},
    "vcl_drv2_045_ps_slope_63d_21d_diff": {"inputs": ["ps"], "func": vcl_drv2_045_ps_slope_63d_21d_diff},
    "vcl_drv2_046_pe_dd_expanding_5d_diff": {"inputs": ["pe"], "func": vcl_drv2_046_pe_dd_expanding_5d_diff},
    "vcl_drv2_047_evebit_dd_expanding_21d_diff": {"inputs": ["evebit"], "func": vcl_drv2_047_evebit_dd_expanding_21d_diff},
    "vcl_drv2_048_pb_median_dev_5d_diff": {"inputs": ["pb"], "func": vcl_drv2_048_pb_median_dev_5d_diff},
    "vcl_drv2_049_pe_median_dev_5d_diff": {"inputs": ["pe"], "func": vcl_drv2_049_pe_median_dev_5d_diff},
    "vcl_drv2_050_composite_dd_5d_diff": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_drv2_050_composite_dd_5d_diff},
    "vcl_drv2_051_marketcap_compression_pct_63d_5d_diff": {"inputs": ["marketcap"], "func": vcl_drv2_051_marketcap_compression_pct_63d_5d_diff},
    "vcl_drv2_052_ev_zscore_252d_5d_diff": {"inputs": ["ev"], "func": vcl_drv2_052_ev_zscore_252d_5d_diff},
    "vcl_drv2_053_pb_below_1_frac_21d_diff": {"inputs": ["pb"], "func": vcl_drv2_053_pb_below_1_frac_21d_diff},
    "vcl_drv2_054_ps_below_1_frac_5d_diff": {"inputs": ["ps"], "func": vcl_drv2_054_ps_below_1_frac_5d_diff},
    "vcl_drv2_055_evebit_compression_pct_252d_5d_diff": {"inputs": ["evebit"], "func": vcl_drv2_055_evebit_compression_pct_252d_5d_diff},
    "vcl_drv2_056_evebitda_compression_pct_252d_5d_diff": {"inputs": ["evebitda"], "func": vcl_drv2_056_evebitda_compression_pct_252d_5d_diff},
    "vcl_drv2_057_pe_compression_vol_63d_5d_diff": {"inputs": ["pe"], "func": vcl_drv2_057_pe_compression_vol_63d_5d_diff},
    "vcl_drv2_058_pb_compression_vol_252d_5d_diff": {"inputs": ["pb"], "func": vcl_drv2_058_pb_compression_vol_252d_5d_diff},
    "vcl_drv2_059_pb_ps_concordance_21d_diff": {"inputs": ["pb", "ps"], "func": vcl_drv2_059_pb_ps_concordance_21d_diff},
    "vcl_drv2_060_evebit_evebitda_spread_5d_diff": {"inputs": ["evebit", "evebitda"], "func": vcl_drv2_060_evebit_evebitda_spread_5d_diff},
    "vcl_drv2_061_pe_pb_ratio_5d_diff": {"inputs": ["pe", "pb"], "func": vcl_drv2_061_pe_pb_ratio_5d_diff},
    "vcl_drv2_062_pb_ps_spread_5d_diff": {"inputs": ["pb", "ps"], "func": vcl_drv2_062_pb_ps_spread_5d_diff},
    "vcl_drv2_063_marketcap_dd_504d_21d_diff": {"inputs": ["marketcap"], "func": vcl_drv2_063_marketcap_dd_504d_21d_diff},
    "vcl_drv2_064_divyield_zscore_252d_5d_diff": {"inputs": ["divyield"], "func": vcl_drv2_064_divyield_zscore_252d_5d_diff},
    "vcl_drv2_065_pe_ewm_deviation_21d_5d_diff": {"inputs": ["pe"], "func": vcl_drv2_065_pe_ewm_deviation_21d_5d_diff},
    "vcl_drv2_066_pb_rate_derating_126d_5d_diff": {"inputs": ["pb"], "func": vcl_drv2_066_pb_rate_derating_126d_5d_diff},
    "vcl_drv2_067_evebitda_slope_63d_5d_diff": {"inputs": ["evebitda"], "func": vcl_drv2_067_evebitda_slope_63d_5d_diff},
    "vcl_drv2_068_ps_rate_derating_126d_5d_diff": {"inputs": ["ps"], "func": vcl_drv2_068_ps_rate_derating_126d_5d_diff},
    "vcl_drv2_069_pe_dd_1260d_21d_diff": {"inputs": ["pe"], "func": vcl_drv2_069_pe_dd_1260d_21d_diff},
    "vcl_drv2_070_pb_dd_1260d_21d_diff": {"inputs": ["pb"], "func": vcl_drv2_070_pb_dd_1260d_21d_diff},
    "vcl_drv2_071_evebit_zscore_252d_5d_diff": {"inputs": ["evebit"], "func": vcl_drv2_071_evebit_zscore_252d_5d_diff},
    "vcl_drv2_072_ev_to_mktcap_21d_diff": {"inputs": ["ev", "marketcap"], "func": vcl_drv2_072_ev_to_mktcap_21d_diff},
    "vcl_drv2_073_distress_count_21d_diff": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vcl_drv2_073_distress_count_21d_diff},
    "vcl_drv2_074_pb_compression_speed_21d_5d_diff": {"inputs": ["pb"], "func": vcl_drv2_074_pb_compression_speed_21d_5d_diff},
    "vcl_drv2_075_ps_compression_speed_63d_5d_diff": {"inputs": ["ps"], "func": vcl_drv2_075_ps_compression_speed_63d_5d_diff},
}
