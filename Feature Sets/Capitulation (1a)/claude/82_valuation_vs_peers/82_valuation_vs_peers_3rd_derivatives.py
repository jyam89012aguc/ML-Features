"""
82_valuation_vs_peers — 3rd Derivatives (Features drv3_001-075)
Domain: rate of change of 2nd-derivative relative-valuation features — captures
        jerk / curvature of relative de-rating vs sector/industry peers.
Asset class: US equities | Daily valuation metrics (SF1-derived, daily frequency)
Target context: capitulation — absolute multi-year low / maximum distress

PEER-MEDIAN INPUT CONTRACT:
    Each function receives the ticker's own daily metric Series and a precomputed
    sector/industry peer-median Series of the same daily index named
    peer_median_<metric>  (e.g. peer_median_pe, peer_median_pb, peer_median_ps,
    peer_median_ev, peer_median_marketcap, peer_median_evebit, peer_median_evebitda,
    peer_median_divyield).  The pipeline computes these universe-wide sector/industry
    medians and passes them in.  All functions look strictly backward.

Each feature here computes a .diff(n)/slope/pct-change of a 2nd-derivative relative-to-peer
concept, giving the jerk or curvature of the cross-sectional valuation signal.

Inputs available (16 total):
    Own metrics:         pe, pb, ps, ev, marketcap, evebit, evebitda, divyield
    Peer-median series:  peer_median_pe, peer_median_pb, peer_median_ps,
                         peer_median_ev, peer_median_marketcap, peer_median_evebit,
                         peer_median_evebitda, peer_median_divyield
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_HALF  = 126
_TD_QTR   = 63
_TD_MON   = 21
_TD_WEEK  = 5
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero/near-zero denominator with NaN."""
    d = den.copy().astype(float)
    d[d.abs() < _EPS] = np.nan
    return num / d


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.abs().clip(lower=_EPS))


def _rel_ratio(own: pd.Series, peer: pd.Series) -> pd.Series:
    d = peer.copy().astype(float)
    d[d.abs() < _EPS] = np.nan
    return own / d


def _log_rel(own: pd.Series, peer: pd.Series) -> pd.Series:
    ratio = _rel_ratio(own, peer)
    return np.log(ratio.abs().clip(lower=_EPS)) * np.sign(ratio)


def _discount_flag(own: pd.Series, peer: pd.Series) -> pd.Series:
    return (own < peer).astype(float)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods (scalar per window)."""
    def _slope(x):
        n = len(x)
        if n < max(2, w // 2):
            return np.nan
        xi  = np.arange(n, dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        num  = ((xi - xi_m) * (x - x_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=False)


# ── 3rd-Derivative Feature Functions (drv3_001-025) ──────────────────────────

def vvp_drv3_001_pe_rel_ratio_5d_jerk(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """3rd-order 5-day difference of P/E relative ratio — jerk of weekly de-rating."""
    r = _rel_ratio(pe, peer_median_pe)
    return r.diff(5).diff(5).diff(5)


def vvp_drv3_002_log_pe_21d_triple_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """3rd-order 21-day difference of log(P/E/peer) — jerk of monthly log-relative velocity."""
    r = _log_rel(pe, peer_median_pe)
    return r.diff(21).diff(21).diff(21)


def vvp_drv3_003_pb_rel_ratio_accel_5d_diff(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5-day diff of the 21d acceleration of P/B relative ratio (jerk of P/B de-rating)."""
    r    = _rel_ratio(pb, peer_median_pb)
    accel = r.diff(21).diff(21)
    return accel.diff(5)


def vvp_drv3_004_ps_slope_accel_5d_diff(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """5-day diff of 5d-diff-of-63d-slope of P/S relative ratio (curvature of slope)."""
    r     = _rel_ratio(ps, peer_median_ps)
    slope = _linslope(r, _TD_QTR)
    return slope.diff(5).diff(5)


def vvp_drv3_005_evebitda_log_accel_5d_diff(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """5-day diff of 21d acceleration of log(EV/EBITDA/peer) — jerk of EV de-rating."""
    r    = _log_rel(evebitda, peer_median_evebitda)
    accel = r.diff(21).diff(5)
    return accel.diff(5)


def vvp_drv3_006_pe_frac_below_accel_5d_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of the 5d acceleration of 252-day below-peer fraction for P/E."""
    below = _discount_flag(pe, peer_median_pe)
    frac  = _rolling_mean(below, _TD_YEAR)
    return frac.diff(5).diff(5)


def vvp_drv3_007_pb_zscore_accel_5d_diff(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5-day diff of 21d velocity of 252d z-score of P/B relative ratio (jerk of z-score)."""
    r = _rel_ratio(pb, peer_median_pb)
    z = _zscore_rolling(r, _TD_YEAR)
    return z.diff(21).diff(5)


def vvp_drv3_008_log_pb_slope_accel(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5-day diff of the diff(5) of 63d-slope of log(P/B/peer) — slope curvature."""
    r     = _log_rel(pb, peer_median_pb)
    slope = _linslope(r, _TD_QTR)
    return slope.diff(5).diff(5)


def vvp_drv3_009_pe_zscore_accel_21d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """21-day diff of the 5d velocity of 252d z-score of P/E relative ratio."""
    r = _rel_ratio(pe, peer_median_pe)
    z = _zscore_rolling(r, _TD_YEAR)
    return z.diff(5).diff(21)


def vvp_drv3_010_ps_rel_ratio_jerk_21d(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """3rd-order 21-day difference of P/S relative ratio."""
    r = _rel_ratio(ps, peer_median_ps)
    return r.diff(21).diff(21).diff(21)


def vvp_drv3_011_composite_zscore_accel_5d(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series
) -> pd.Series:
    """5-day diff of 5d velocity of composite (PE/PB/PS) 252d z-score (composite jerk)."""
    z_pe = _zscore_rolling(_rel_ratio(pe, peer_median_pe), _TD_YEAR)
    z_pb = _zscore_rolling(_rel_ratio(pb, peer_median_pb), _TD_YEAR)
    z_ps = _zscore_rolling(_rel_ratio(ps, peer_median_ps), _TD_YEAR)
    composite = (z_pe + z_pb + z_ps) / 3.0
    return composite.diff(5).diff(5)


def vvp_drv3_012_evebit_accel_5d_diff(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """5-day diff of 21d acceleration of EV/EBIT relative ratio."""
    r    = _rel_ratio(evebit, peer_median_evebit)
    accel = r.diff(21).diff(21)
    return accel.diff(5)


def vvp_drv3_013_log_pe_ewm_accel(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of 5d velocity of EWM(21) of log(P/E/peer) — smooth log jerk."""
    r = _log_rel(pe, peer_median_pe)
    ewm = _ewm_mean(r, 21)
    return ewm.diff(5).diff(5)


def vvp_drv3_014_divyield_rel_jerk_5d(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """3rd-order 5-day difference of div-yield relative ratio (yield-advantage jerk)."""
    r = _rel_ratio(divyield, peer_median_divyield)
    return r.diff(5).diff(5).diff(5)


def vvp_drv3_015_pe_pctrank_accel_5d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of 5d velocity of 252-day pct-rank of P/E relative ratio (rank jerk)."""
    r    = _rel_ratio(pe, peer_median_pe)
    rank = r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(5).diff(5)


def vvp_drv3_016_pb_vs_mean_dev_accel(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5-day diff of 5d velocity of (P/B relative ratio minus 252d mean) — deviation jerk."""
    r   = _rel_ratio(pb, peer_median_pb)
    dev = r - _rolling_mean(r, _TD_YEAR)
    return dev.diff(5).diff(5)


def vvp_drv3_017_pe_rel_slope_curvature(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of 21d diff of 63d slope of P/E relative ratio (3rd-order slope change)."""
    r     = _rel_ratio(pe, peer_median_pe)
    slope = _linslope(r, _TD_QTR)
    return slope.diff(21).diff(5)


def vvp_drv3_018_ps_frac_below_accel(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """5-day diff of 5d velocity of 252-day below-peer fraction for P/S."""
    below = _discount_flag(ps, peer_median_ps)
    frac  = _rolling_mean(below, _TD_YEAR)
    return frac.diff(5).diff(5)


def vvp_drv3_019_log_evebitda_slope_curvature(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """5-day diff of 5d-diff of 63d-slope of log(EV/EBITDA/peer) (3rd-order slope)."""
    r     = _log_rel(evebitda, peer_median_evebitda)
    slope = _linslope(r, _TD_QTR)
    return slope.diff(5).diff(5)


def vvp_drv3_020_pe_derate_speed_accel(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of 5d-velocity of 21-day pct-change of P/E relative ratio (pct-rate jerk)."""
    r = _rel_ratio(pe, peer_median_pe)
    return r.pct_change(21).diff(5).diff(5)


def vvp_drv3_021_multi_discount_score_accel(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series
) -> pd.Series:
    """5-day diff of 5d velocity of multi-metric discount count (jerk of breadth widening)."""
    score = (
        _discount_flag(pe, peer_median_pe) +
        _discount_flag(pb, peer_median_pb) +
        _discount_flag(ps, peer_median_ps)
    )
    return score.diff(5).diff(5)


def vvp_drv3_022_log_rel_4m_ewm_accel(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series
) -> pd.Series:
    """5-day diff of 5d velocity of EWM(21) composite log-relative (jerk of composite signal)."""
    composite = (
        _log_rel(pe, peer_median_pe) +
        _log_rel(pb, peer_median_pb) +
        _log_rel(ps, peer_median_ps) +
        _log_rel(evebitda, peer_median_evebitda)
    ) / 4.0
    return _ewm_mean(composite, 21).diff(5).diff(5)


def vvp_drv3_023_pe_ath_dd_accel(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of 5d velocity of P/E-relative-ratio ATH drawdown (discount-depth jerk)."""
    r    = _rel_ratio(pe, peer_median_pe)
    peak = r.expanding(min_periods=1).max()
    dd   = _safe_div(r - peak, peak.abs())
    return dd.diff(5).diff(5)


def vvp_drv3_024_pb_log_rel_21d_triple_diff(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5-day diff of 21d diff of 5d diff of log(P/B/peer) — mixed-order log jerk."""
    r = _log_rel(pb, peer_median_pb)
    return r.diff(5).diff(21).diff(5)


def vvp_drv3_025_discount_persistence_accel(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series
) -> pd.Series:
    """5-day diff of 5d velocity of discount-persistence composite (PE/PB/PS) — jerk."""
    f_pe = _rolling_mean(_discount_flag(pe, peer_median_pe), _TD_YEAR)
    f_pb = _rolling_mean(_discount_flag(pb, peer_median_pb), _TD_YEAR)
    f_ps = _rolling_mean(_discount_flag(ps, peer_median_ps), _TD_YEAR)
    composite = (f_pe + f_pb + f_ps) / 3.0
    return composite.diff(5).diff(5)


# ── 3rd-Derivative Feature Functions (drv3_026-075) ──────────────────────────

# --- Group D3a (026-035): jerk of EWM-smoothed relative ratio features ---

def vvp_drv3_026_pe_rel_ewm21_5d_jerk(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of 5d diff of EWM(21) P/E relative ratio (EWM signal jerk)."""
    return _ewm_mean(_rel_ratio(pe, peer_median_pe), _TD_MON).diff(5).diff(5)


def vvp_drv3_027_pb_rel_ewm63_5d_jerk(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5-day diff of 5d diff of EWM(63) P/B relative ratio."""
    return _ewm_mean(_rel_ratio(pb, peer_median_pb), _TD_QTR).diff(5).diff(5)


def vvp_drv3_028_ps_rel_ewm21_21d_jerk(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """21-day diff of 5d diff of EWM(21) P/S relative ratio."""
    return _ewm_mean(_rel_ratio(ps, peer_median_ps), _TD_MON).diff(5).diff(21)


def vvp_drv3_029_log_pe_ewm21_jerk(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of 5d diff of EWM(21) log(P/E/peer) (log-relative signal jerk)."""
    return _ewm_mean(_log_rel(pe, peer_median_pe), _TD_MON).diff(5).diff(5)


def vvp_drv3_030_log_pb_ewm63_jerk(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5-day diff of 21d diff of EWM(63) log(P/B/peer) — mixed-order log jerk."""
    return _ewm_mean(_log_rel(pb, peer_median_pb), _TD_QTR).diff(21).diff(5)


def vvp_drv3_031_evebitda_rel_ewm21_jerk(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """5-day diff of 5d diff of EWM(21) EV/EBITDA relative ratio."""
    return _ewm_mean(_rel_ratio(evebitda, peer_median_evebitda), _TD_MON).diff(5).diff(5)


def vvp_drv3_032_evebit_rel_ewm21_jerk(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """5-day diff of 5d diff of EWM(21) EV/EBIT relative ratio."""
    return _ewm_mean(_rel_ratio(evebit, peer_median_evebit), _TD_MON).diff(5).diff(5)


def vvp_drv3_033_divyield_rel_ewm21_jerk(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """5-day diff of 5d diff of EWM(21) div-yield relative ratio."""
    return _ewm_mean(_rel_ratio(divyield, peer_median_divyield), _TD_MON).diff(5).diff(5)


def vvp_drv3_034_log_ps_ewm21_jerk(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """5-day diff of 5d diff of EWM(21) log(P/S/peer)."""
    return _ewm_mean(_log_rel(ps, peer_median_ps), _TD_MON).diff(5).diff(5)


def vvp_drv3_035_composite_ewm21_log_4m_jerk(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series
) -> pd.Series:
    """5d diff of 5d diff of EWM(21) composite log-relative (PE/PB/PS/EVEBITDA) — composite jerk."""
    composite = (
        _log_rel(pe, peer_median_pe) +
        _log_rel(pb, peer_median_pb) +
        _log_rel(ps, peer_median_ps) +
        _log_rel(evebitda, peer_median_evebitda)
    ) / 4.0
    return _ewm_mean(composite, _TD_MON).diff(5).diff(5)


# --- Group D3b (036-045): jerk of z-score features ---

def vvp_drv3_036_ps_zscore_252d_5d_jerk(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """5-day diff of 5d velocity of 252d z-score of P/S relative ratio."""
    return _zscore_rolling(_rel_ratio(ps, peer_median_ps), _TD_YEAR).diff(5).diff(5)


def vvp_drv3_037_evebitda_zscore_252d_5d_jerk(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """5-day diff of 5d velocity of 252d z-score of EV/EBITDA relative ratio."""
    return _zscore_rolling(_rel_ratio(evebitda, peer_median_evebitda), _TD_YEAR).diff(5).diff(5)


def vvp_drv3_038_evebit_zscore_252d_5d_jerk(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """5-day diff of 5d velocity of 252d z-score of EV/EBIT relative ratio."""
    return _zscore_rolling(_rel_ratio(evebit, peer_median_evebit), _TD_YEAR).diff(5).diff(5)


def vvp_drv3_039_log_pe_zscore_5d_jerk(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of 5d velocity of 252d z-score of log(P/E/peer)."""
    return _zscore_rolling(_log_rel(pe, peer_median_pe), _TD_YEAR).diff(5).diff(5)


def vvp_drv3_040_log_pb_zscore_5d_jerk(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5-day diff of 5d velocity of 252d z-score of log(P/B/peer)."""
    return _zscore_rolling(_log_rel(pb, peer_median_pb), _TD_YEAR).diff(5).diff(5)


def vvp_drv3_041_divyield_zscore_5d_jerk(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """5-day diff of 5d velocity of 252d z-score of div-yield relative ratio."""
    return _zscore_rolling(_rel_ratio(divyield, peer_median_divyield), _TD_YEAR).diff(5).diff(5)


def vvp_drv3_042_log_ps_zscore_5d_jerk(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """5-day diff of 5d velocity of 252d z-score of log(P/S/peer)."""
    return _zscore_rolling(_log_rel(ps, peer_median_ps), _TD_YEAR).diff(5).diff(5)


def vvp_drv3_043_pe_zscore_504d_5d_jerk(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of 5d velocity of 504d z-score of P/E relative ratio (2-year jerk)."""
    return _zscore_rolling(_rel_ratio(pe, peer_median_pe), _TD_2Y).diff(5).diff(5)


def vvp_drv3_044_composite_zscore_4m_5d_jerk(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    evebit: pd.Series, peer_median_evebit: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series
) -> pd.Series:
    """5d diff of 5d velocity of composite (PE/PB/EVEBIT/EVEBITDA) 252d z-score (jerk)."""
    z = (
        _zscore_rolling(_rel_ratio(pe, peer_median_pe), _TD_YEAR) +
        _zscore_rolling(_rel_ratio(pb, peer_median_pb), _TD_YEAR) +
        _zscore_rolling(_rel_ratio(evebit, peer_median_evebit), _TD_YEAR) +
        _zscore_rolling(_rel_ratio(evebitda, peer_median_evebitda), _TD_YEAR)
    ) / 4.0
    return z.diff(5).diff(5)


def vvp_drv3_045_log_evebitda_zscore_5d_jerk(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """5-day diff of 5d velocity of 252d z-score of log(EV/EBITDA/peer)."""
    return _zscore_rolling(_log_rel(evebitda, peer_median_evebitda), _TD_YEAR).diff(5).diff(5)


# --- Group D3c (046-055): jerk of percentile-rank features ---

def vvp_drv3_046_pb_pctrank_252d_5d_jerk(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5-day diff of 5d velocity of 252d pct-rank of P/B relative ratio (P/B rank jerk)."""
    r = _rel_ratio(pb, peer_median_pb)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).diff(5).diff(5)


def vvp_drv3_047_ps_pctrank_252d_5d_jerk(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """5-day diff of 5d velocity of 252d pct-rank of P/S relative ratio."""
    r = _rel_ratio(ps, peer_median_ps)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).diff(5).diff(5)


def vvp_drv3_048_evebitda_pctrank_252d_5d_jerk(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """5-day diff of 5d velocity of 252d pct-rank of EV/EBITDA relative ratio."""
    r = _rel_ratio(evebitda, peer_median_evebitda)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).diff(5).diff(5)


def vvp_drv3_049_divyield_pctrank_252d_5d_jerk(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """5-day diff of 5d velocity of 252d pct-rank of div-yield relative ratio."""
    r = _rel_ratio(divyield, peer_median_divyield)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).diff(5).diff(5)


def vvp_drv3_050_evebit_pctrank_252d_5d_jerk(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """5-day diff of 5d velocity of 252d pct-rank of EV/EBIT relative ratio."""
    r = _rel_ratio(evebit, peer_median_evebit)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).diff(5).diff(5)


def vvp_drv3_051_composite_pctrank_3m_5d_jerk(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series
) -> pd.Series:
    """5d diff of 5d velocity of composite (PE/PB/PS) 252d pct-rank (breadth rank jerk)."""
    def _rank252(s):
        return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    composite = (
        _rank252(_rel_ratio(pe, peer_median_pe)) +
        _rank252(_rel_ratio(pb, peer_median_pb)) +
        _rank252(_rel_ratio(ps, peer_median_ps))
    ) / 3.0
    return composite.diff(5).diff(5)


def vvp_drv3_052_pe_expanding_pctrank_5d_jerk(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5d diff of 5d velocity of expanding pct-rank of P/E relative ratio (rank jerk)."""
    r = _rel_ratio(pe, peer_median_pe)
    return r.expanding(min_periods=21).rank(pct=True).diff(5).diff(5)


def vvp_drv3_053_log_pe_pctrank_252d_5d_jerk(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5d diff of 5d velocity of 252d pct-rank of log(P/E/peer)."""
    r = _log_rel(pe, peer_median_pe)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).diff(5).diff(5)


def vvp_drv3_054_marketcap_rel_pctrank_5d_jerk(marketcap: pd.Series, peer_median_marketcap: pd.Series) -> pd.Series:
    """5d diff of 5d velocity of 252d pct-rank of market-cap relative ratio (size rank jerk)."""
    r = _rel_ratio(marketcap, peer_median_marketcap)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).diff(5).diff(5)


def vvp_drv3_055_pb_expanding_pctrank_5d_jerk(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5d diff of 5d velocity of expanding pct-rank of P/B relative ratio."""
    r = _rel_ratio(pb, peer_median_pb)
    return r.expanding(min_periods=21).rank(pct=True).diff(5).diff(5)


# --- Group D3d (056-065): jerk of discount-frequency and persistence features ---

def vvp_drv3_056_pe_frac_below_252d_5d_jerk(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5d diff of 5d velocity of 252d below-peer fraction for P/E."""
    return _rolling_mean(_discount_flag(pe, peer_median_pe), _TD_YEAR).diff(5).diff(5)


def vvp_drv3_057_pb_frac_below_252d_5d_jerk(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5d diff of 5d velocity of 252d below-peer fraction for P/B."""
    return _rolling_mean(_discount_flag(pb, peer_median_pb), _TD_YEAR).diff(5).diff(5)


def vvp_drv3_058_ps_frac_below_252d_5d_jerk(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """5d diff of 5d velocity of 252d below-peer fraction for P/S."""
    return _rolling_mean(_discount_flag(ps, peer_median_ps), _TD_YEAR).diff(5).diff(5)


def vvp_drv3_059_evebit_frac_below_252d_5d_jerk(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """5d diff of 5d velocity of 252d below-peer fraction for EV/EBIT."""
    return _rolling_mean(_discount_flag(evebit, peer_median_evebit), _TD_YEAR).diff(5).diff(5)


def vvp_drv3_060_evebitda_frac_below_252d_5d_jerk(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """5d diff of 5d velocity of 252d below-peer fraction for EV/EBITDA."""
    return _rolling_mean(_discount_flag(evebitda, peer_median_evebitda), _TD_YEAR).diff(5).diff(5)


def vvp_drv3_061_divyield_frac_above_peer_5d_jerk(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """5d diff of 5d velocity of 252d above-peer fraction for div yield (yield jerk)."""
    above = (divyield > peer_median_divyield).astype(float)
    return _rolling_mean(above, _TD_YEAR).diff(5).diff(5)


def vvp_drv3_062_multi_discount_score_5d_jerk(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series
) -> pd.Series:
    """5d diff of 5d velocity of multi-metric discount count (PE/PB/PS) — breadth jerk."""
    score = (
        _discount_flag(pe, peer_median_pe) +
        _discount_flag(pb, peer_median_pb) +
        _discount_flag(ps, peer_median_ps)
    )
    return score.diff(5).diff(5)


def vvp_drv3_063_discount_count_5m_5d_jerk(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series,
    evebit: pd.Series, peer_median_evebit: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series
) -> pd.Series:
    """5d diff of 5d velocity of 5-metric discount count — full-breadth de-rating jerk."""
    score = (
        _discount_flag(pe, peer_median_pe) +
        _discount_flag(pb, peer_median_pb) +
        _discount_flag(ps, peer_median_ps) +
        _discount_flag(evebit, peer_median_evebit) +
        _discount_flag(evebitda, peer_median_evebitda)
    )
    return score.diff(5).diff(5)


def vvp_drv3_064_pe_frac_below_63d_5d_jerk(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5d diff of 5d velocity of 63-day below-peer fraction for P/E."""
    return _rolling_mean(_discount_flag(pe, peer_median_pe), _TD_QTR).diff(5).diff(5)


def vvp_drv3_065_discount_persistence_4m_5d_jerk(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    evebit: pd.Series, peer_median_evebit: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series
) -> pd.Series:
    """5d diff of 5d velocity of 252d discount-persistence composite (PE/PB/EVEBIT/EVEBITDA)."""
    composite = (
        _rolling_mean(_discount_flag(pe, peer_median_pe), _TD_YEAR) +
        _rolling_mean(_discount_flag(pb, peer_median_pb), _TD_YEAR) +
        _rolling_mean(_discount_flag(evebit, peer_median_evebit), _TD_YEAR) +
        _rolling_mean(_discount_flag(evebitda, peer_median_evebitda), _TD_YEAR)
    ) / 4.0
    return composite.diff(5).diff(5)


# --- Group D3e (066-075): jerk of slope and drawdown features ---

def vvp_drv3_066_pe_rel_slope_63d_5d_jerk(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5d diff of 5d diff of 63d OLS slope of P/E relative ratio (slope jerk)."""
    return _linslope(_rel_ratio(pe, peer_median_pe), _TD_QTR).diff(5).diff(5)


def vvp_drv3_067_pb_rel_slope_63d_5d_jerk(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5d diff of 5d diff of 63d OLS slope of P/B relative ratio."""
    return _linslope(_rel_ratio(pb, peer_median_pb), _TD_QTR).diff(5).diff(5)


def vvp_drv3_068_ps_rel_slope_63d_5d_jerk(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """5d diff of 5d diff of 63d OLS slope of P/S relative ratio."""
    return _linslope(_rel_ratio(ps, peer_median_ps), _TD_QTR).diff(5).diff(5)


def vvp_drv3_069_evebitda_log_slope_5d_jerk(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """5d diff of 5d diff of 63d slope of log(EV/EBITDA/peer) (log-slope jerk)."""
    return _linslope(_log_rel(evebitda, peer_median_evebitda), _TD_QTR).diff(5).diff(5)


def vvp_drv3_070_pe_rel_slope_252d_5d_jerk(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5d diff of 5d diff of 252d OLS slope of P/E relative ratio (annual-slope jerk)."""
    return _linslope(_rel_ratio(pe, peer_median_pe), _TD_YEAR).diff(5).diff(5)


def vvp_drv3_071_pb_ath_dd_5d_jerk(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5d diff of 5d velocity of P/B relative-ratio ATH drawdown (discount-depth jerk)."""
    r    = _rel_ratio(pb, peer_median_pb)
    peak = r.expanding(min_periods=1).max()
    dd   = _safe_div(r - peak, peak.abs())
    return dd.diff(5).diff(5)


def vvp_drv3_072_evebitda_ath_dd_5d_jerk(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """5d diff of 5d velocity of EV/EBITDA relative-ratio ATH drawdown."""
    r    = _rel_ratio(evebitda, peer_median_evebitda)
    peak = r.expanding(min_periods=1).max()
    dd   = _safe_div(r - peak, peak.abs())
    return dd.diff(5).diff(5)


def vvp_drv3_073_pe_derate_pct_5d_jerk(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5d diff of 5d velocity of 21d pct-change of P/E relative ratio (pct de-rate jerk)."""
    return _rel_ratio(pe, peer_median_pe).pct_change(21).diff(5).diff(5)


def vvp_drv3_074_pb_derate_pct_5d_jerk(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5d diff of 5d velocity of 21d pct-change of P/B relative ratio."""
    return _rel_ratio(pb, peer_median_pb).pct_change(21).diff(5).diff(5)


def vvp_drv3_075_composite_derate_5d_jerk(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series
) -> pd.Series:
    """5d diff of 5d velocity of composite 63d excess de-rating (PE/PB/EVEBITDA) — jerk."""
    dr_pe  = pe.pct_change(63)  - peer_median_pe.pct_change(63)
    dr_pb  = pb.pct_change(63)  - peer_median_pb.pct_change(63)
    dr_evd = evebitda.pct_change(63) - peer_median_evebitda.pct_change(63)
    composite = (dr_pe + dr_pb + dr_evd) / 3.0
    return composite.diff(5).diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

VALUATION_VS_PEERS_REGISTRY_3RD_DERIVATIVES = {
    "vvp_drv3_001_pe_rel_ratio_5d_jerk":           {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv3_001_pe_rel_ratio_5d_jerk},
    "vvp_drv3_002_log_pe_21d_triple_diff":         {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv3_002_log_pe_21d_triple_diff},
    "vvp_drv3_003_pb_rel_ratio_accel_5d_diff":     {"inputs": ["pb", "peer_median_pb"],                                                                                                   "func": vvp_drv3_003_pb_rel_ratio_accel_5d_diff},
    "vvp_drv3_004_ps_slope_accel_5d_diff":         {"inputs": ["ps", "peer_median_ps"],                                                                                                   "func": vvp_drv3_004_ps_slope_accel_5d_diff},
    "vvp_drv3_005_evebitda_log_accel_5d_diff":     {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                       "func": vvp_drv3_005_evebitda_log_accel_5d_diff},
    "vvp_drv3_006_pe_frac_below_accel_5d_diff":    {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv3_006_pe_frac_below_accel_5d_diff},
    "vvp_drv3_007_pb_zscore_accel_5d_diff":        {"inputs": ["pb", "peer_median_pb"],                                                                                                   "func": vvp_drv3_007_pb_zscore_accel_5d_diff},
    "vvp_drv3_008_log_pb_slope_accel":             {"inputs": ["pb", "peer_median_pb"],                                                                                                   "func": vvp_drv3_008_log_pb_slope_accel},
    "vvp_drv3_009_pe_zscore_accel_21d":            {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv3_009_pe_zscore_accel_21d},
    "vvp_drv3_010_ps_rel_ratio_jerk_21d":          {"inputs": ["ps", "peer_median_ps"],                                                                                                   "func": vvp_drv3_010_ps_rel_ratio_jerk_21d},
    "vvp_drv3_011_composite_zscore_accel_5d":      {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps"],                                                   "func": vvp_drv3_011_composite_zscore_accel_5d},
    "vvp_drv3_012_evebit_accel_5d_diff":           {"inputs": ["evebit", "peer_median_evebit"],                                                                                           "func": vvp_drv3_012_evebit_accel_5d_diff},
    "vvp_drv3_013_log_pe_ewm_accel":              {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_drv3_013_log_pe_ewm_accel},
    "vvp_drv3_014_divyield_rel_jerk_5d":           {"inputs": ["divyield", "peer_median_divyield"],                                                                                       "func": vvp_drv3_014_divyield_rel_jerk_5d},
    "vvp_drv3_015_pe_pctrank_accel_5d":            {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv3_015_pe_pctrank_accel_5d},
    "vvp_drv3_016_pb_vs_mean_dev_accel":           {"inputs": ["pb", "peer_median_pb"],                                                                                                   "func": vvp_drv3_016_pb_vs_mean_dev_accel},
    "vvp_drv3_017_pe_rel_slope_curvature":         {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv3_017_pe_rel_slope_curvature},
    "vvp_drv3_018_ps_frac_below_accel":            {"inputs": ["ps", "peer_median_ps"],                                                                                                   "func": vvp_drv3_018_ps_frac_below_accel},
    "vvp_drv3_019_log_evebitda_slope_curvature":   {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                       "func": vvp_drv3_019_log_evebitda_slope_curvature},
    "vvp_drv3_020_pe_derate_speed_accel":          {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv3_020_pe_derate_speed_accel},
    "vvp_drv3_021_multi_discount_score_accel":     {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps"],                                                   "func": vvp_drv3_021_multi_discount_score_accel},
    "vvp_drv3_022_log_rel_4m_ewm_accel":          {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps", "evebitda", "peer_median_evebitda"],               "func": vvp_drv3_022_log_rel_4m_ewm_accel},
    "vvp_drv3_023_pe_ath_dd_accel":               {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_drv3_023_pe_ath_dd_accel},
    "vvp_drv3_024_pb_log_rel_21d_triple_diff":     {"inputs": ["pb", "peer_median_pb"],                                                                                                   "func": vvp_drv3_024_pb_log_rel_21d_triple_diff},
    "vvp_drv3_025_discount_persistence_accel":     {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps"],                                                   "func": vvp_drv3_025_discount_persistence_accel},
    "vvp_drv3_026_pe_rel_ewm21_5d_jerk":          {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_drv3_026_pe_rel_ewm21_5d_jerk},
    "vvp_drv3_027_pb_rel_ewm63_5d_jerk":          {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_drv3_027_pb_rel_ewm63_5d_jerk},
    "vvp_drv3_028_ps_rel_ewm21_21d_jerk":         {"inputs": ["ps", "peer_median_ps"],                                                                                                    "func": vvp_drv3_028_ps_rel_ewm21_21d_jerk},
    "vvp_drv3_029_log_pe_ewm21_jerk":             {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_drv3_029_log_pe_ewm21_jerk},
    "vvp_drv3_030_log_pb_ewm63_jerk":             {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_drv3_030_log_pb_ewm63_jerk},
    "vvp_drv3_031_evebitda_rel_ewm21_jerk":       {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                        "func": vvp_drv3_031_evebitda_rel_ewm21_jerk},
    "vvp_drv3_032_evebit_rel_ewm21_jerk":         {"inputs": ["evebit", "peer_median_evebit"],                                                                                            "func": vvp_drv3_032_evebit_rel_ewm21_jerk},
    "vvp_drv3_033_divyield_rel_ewm21_jerk":       {"inputs": ["divyield", "peer_median_divyield"],                                                                                        "func": vvp_drv3_033_divyield_rel_ewm21_jerk},
    "vvp_drv3_034_log_ps_ewm21_jerk":             {"inputs": ["ps", "peer_median_ps"],                                                                                                    "func": vvp_drv3_034_log_ps_ewm21_jerk},
    "vvp_drv3_035_composite_ewm21_log_4m_jerk":   {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps", "evebitda", "peer_median_evebitda"],               "func": vvp_drv3_035_composite_ewm21_log_4m_jerk},
    "vvp_drv3_036_ps_zscore_252d_5d_jerk":        {"inputs": ["ps", "peer_median_ps"],                                                                                                    "func": vvp_drv3_036_ps_zscore_252d_5d_jerk},
    "vvp_drv3_037_evebitda_zscore_252d_5d_jerk":  {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                        "func": vvp_drv3_037_evebitda_zscore_252d_5d_jerk},
    "vvp_drv3_038_evebit_zscore_252d_5d_jerk":    {"inputs": ["evebit", "peer_median_evebit"],                                                                                            "func": vvp_drv3_038_evebit_zscore_252d_5d_jerk},
    "vvp_drv3_039_log_pe_zscore_5d_jerk":         {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_drv3_039_log_pe_zscore_5d_jerk},
    "vvp_drv3_040_log_pb_zscore_5d_jerk":         {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_drv3_040_log_pb_zscore_5d_jerk},
    "vvp_drv3_041_divyield_zscore_5d_jerk":       {"inputs": ["divyield", "peer_median_divyield"],                                                                                        "func": vvp_drv3_041_divyield_zscore_5d_jerk},
    "vvp_drv3_042_log_ps_zscore_5d_jerk":         {"inputs": ["ps", "peer_median_ps"],                                                                                                    "func": vvp_drv3_042_log_ps_zscore_5d_jerk},
    "vvp_drv3_043_pe_zscore_504d_5d_jerk":        {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_drv3_043_pe_zscore_504d_5d_jerk},
    "vvp_drv3_044_composite_zscore_4m_5d_jerk":   {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "evebit", "peer_median_evebit", "evebitda", "peer_median_evebitda"],       "func": vvp_drv3_044_composite_zscore_4m_5d_jerk},
    "vvp_drv3_045_log_evebitda_zscore_5d_jerk":   {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                        "func": vvp_drv3_045_log_evebitda_zscore_5d_jerk},
    "vvp_drv3_046_pb_pctrank_252d_5d_jerk":       {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_drv3_046_pb_pctrank_252d_5d_jerk},
    "vvp_drv3_047_ps_pctrank_252d_5d_jerk":       {"inputs": ["ps", "peer_median_ps"],                                                                                                    "func": vvp_drv3_047_ps_pctrank_252d_5d_jerk},
    "vvp_drv3_048_evebitda_pctrank_252d_5d_jerk": {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                        "func": vvp_drv3_048_evebitda_pctrank_252d_5d_jerk},
    "vvp_drv3_049_divyield_pctrank_252d_5d_jerk": {"inputs": ["divyield", "peer_median_divyield"],                                                                                        "func": vvp_drv3_049_divyield_pctrank_252d_5d_jerk},
    "vvp_drv3_050_evebit_pctrank_252d_5d_jerk":   {"inputs": ["evebit", "peer_median_evebit"],                                                                                            "func": vvp_drv3_050_evebit_pctrank_252d_5d_jerk},
    "vvp_drv3_051_composite_pctrank_3m_5d_jerk":  {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps"],                                                   "func": vvp_drv3_051_composite_pctrank_3m_5d_jerk},
    "vvp_drv3_052_pe_expanding_pctrank_5d_jerk":  {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_drv3_052_pe_expanding_pctrank_5d_jerk},
    "vvp_drv3_053_log_pe_pctrank_252d_5d_jerk":   {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_drv3_053_log_pe_pctrank_252d_5d_jerk},
    "vvp_drv3_054_marketcap_rel_pctrank_5d_jerk": {"inputs": ["marketcap", "peer_median_marketcap"],                                                                                      "func": vvp_drv3_054_marketcap_rel_pctrank_5d_jerk},
    "vvp_drv3_055_pb_expanding_pctrank_5d_jerk":  {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_drv3_055_pb_expanding_pctrank_5d_jerk},
    "vvp_drv3_056_pe_frac_below_252d_5d_jerk":    {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_drv3_056_pe_frac_below_252d_5d_jerk},
    "vvp_drv3_057_pb_frac_below_252d_5d_jerk":    {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_drv3_057_pb_frac_below_252d_5d_jerk},
    "vvp_drv3_058_ps_frac_below_252d_5d_jerk":    {"inputs": ["ps", "peer_median_ps"],                                                                                                    "func": vvp_drv3_058_ps_frac_below_252d_5d_jerk},
    "vvp_drv3_059_evebit_frac_below_252d_5d_jerk":{"inputs": ["evebit", "peer_median_evebit"],                                                                                            "func": vvp_drv3_059_evebit_frac_below_252d_5d_jerk},
    "vvp_drv3_060_evebitda_frac_below_252d_5d_jerk": {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                     "func": vvp_drv3_060_evebitda_frac_below_252d_5d_jerk},
    "vvp_drv3_061_divyield_frac_above_peer_5d_jerk": {"inputs": ["divyield", "peer_median_divyield"],                                                                                     "func": vvp_drv3_061_divyield_frac_above_peer_5d_jerk},
    "vvp_drv3_062_multi_discount_score_5d_jerk":  {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps"],                                                   "func": vvp_drv3_062_multi_discount_score_5d_jerk},
    "vvp_drv3_063_discount_count_5m_5d_jerk":     {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps", "evebit", "peer_median_evebit", "evebitda", "peer_median_evebitda"], "func": vvp_drv3_063_discount_count_5m_5d_jerk},
    "vvp_drv3_064_pe_frac_below_63d_5d_jerk":     {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_drv3_064_pe_frac_below_63d_5d_jerk},
    "vvp_drv3_065_discount_persistence_4m_5d_jerk": {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "evebit", "peer_median_evebit", "evebitda", "peer_median_evebitda"],    "func": vvp_drv3_065_discount_persistence_4m_5d_jerk},
    "vvp_drv3_066_pe_rel_slope_63d_5d_jerk":      {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_drv3_066_pe_rel_slope_63d_5d_jerk},
    "vvp_drv3_067_pb_rel_slope_63d_5d_jerk":      {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_drv3_067_pb_rel_slope_63d_5d_jerk},
    "vvp_drv3_068_ps_rel_slope_63d_5d_jerk":      {"inputs": ["ps", "peer_median_ps"],                                                                                                    "func": vvp_drv3_068_ps_rel_slope_63d_5d_jerk},
    "vvp_drv3_069_evebitda_log_slope_5d_jerk":    {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                        "func": vvp_drv3_069_evebitda_log_slope_5d_jerk},
    "vvp_drv3_070_pe_rel_slope_252d_5d_jerk":     {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_drv3_070_pe_rel_slope_252d_5d_jerk},
    "vvp_drv3_071_pb_ath_dd_5d_jerk":             {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_drv3_071_pb_ath_dd_5d_jerk},
    "vvp_drv3_072_evebitda_ath_dd_5d_jerk":       {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                        "func": vvp_drv3_072_evebitda_ath_dd_5d_jerk},
    "vvp_drv3_073_pe_derate_pct_5d_jerk":         {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_drv3_073_pe_derate_pct_5d_jerk},
    "vvp_drv3_074_pb_derate_pct_5d_jerk":         {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_drv3_074_pb_derate_pct_5d_jerk},
    "vvp_drv3_075_composite_derate_5d_jerk":      {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "evebitda", "peer_median_evebitda"],                                        "func": vvp_drv3_075_composite_derate_5d_jerk},
}
