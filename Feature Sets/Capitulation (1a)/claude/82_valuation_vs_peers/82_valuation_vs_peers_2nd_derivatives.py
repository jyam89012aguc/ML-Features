"""
82_valuation_vs_peers — 2nd Derivatives (Features drv2_001-075)
Domain: rate of change of base relative-valuation features — captures acceleration of
        relative de-rating vs sector/industry peers.
Asset class: US equities | Daily valuation metrics (SF1-derived, daily frequency)
Target context: capitulation — absolute multi-year low / maximum distress

PEER-MEDIAN INPUT CONTRACT:
    Each function receives the ticker's own daily metric Series and a precomputed
    sector/industry peer-median Series of the same daily index named
    peer_median_<metric>  (e.g. peer_median_pe, peer_median_pb, peer_median_ps,
    peer_median_ev, peer_median_marketcap, peer_median_evebit, peer_median_evebitda,
    peer_median_divyield).  The pipeline computes these universe-wide sector/industry
    medians and passes them in.  All functions look strictly backward.

Each feature here computes a .diff(n)/slope/pct-change of a base relative-to-peer
concept (e.g. ratio, log-ratio, gap, discount fraction), giving the velocity or
acceleration of the cross-sectional valuation signal.

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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


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
        xi = np.arange(n, dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        num  = ((xi - xi_m) * (x - x_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=False)


# ── 2nd-Derivative Feature Functions (drv2_001-025) ──────────────────────────

def vvp_drv2_001_pe_rel_ratio_5d_accel(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """2nd difference (5d) of P/E relative ratio — acceleration of weekly de-rating velocity."""
    r = _rel_ratio(pe, peer_median_pe)
    return r.diff(5).diff(5)


def vvp_drv2_002_log_pe_21d_diff_diff5(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of the 21-day diff of log(P/E/peer) — acceleration of monthly log-velocity."""
    r = _log_rel(pe, peer_median_pe)
    return r.diff(21).diff(5)


def vvp_drv2_003_pb_rel_ratio_21d_accel(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """2nd difference (21d) of P/B relative ratio — monthly acceleration."""
    r = _rel_ratio(pb, peer_median_pb)
    return r.diff(21).diff(21)


def vvp_drv2_004_ps_rel_ratio_5d_diff_of_slope63(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """5-day diff of the 63-day OLS slope of P/S relative ratio — slope-velocity."""
    r = _rel_ratio(ps, peer_median_ps)
    slope = _linslope(r, _TD_QTR)
    return slope.diff(5)


def vvp_drv2_005_evebitda_rel_ratio_21d_diff_diff5(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in EV/EBITDA relative ratio (acceleration of EV de-rating)."""
    r = _rel_ratio(evebitda, peer_median_evebitda)
    return r.diff(21).diff(5)


def vvp_drv2_006_pe_frac_below_peer_252d_5d_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of 252-day below-peer fraction for P/E (pace of rising discount frequency)."""
    below = _discount_flag(pe, peer_median_pe)
    frac  = _rolling_mean(below, _TD_YEAR)
    return frac.diff(5)


def vvp_drv2_007_pb_frac_below_peer_252d_21d_diff(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """21-day diff of 252-day P/B below-peer fraction (monthly acceleration of discount duration)."""
    below = _discount_flag(pb, peer_median_pb)
    frac  = _rolling_mean(below, _TD_YEAR)
    return frac.diff(21)


def vvp_drv2_008_log_pb_slope_diff5(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5-day diff of 63-day OLS slope of log(P/B/peer) — acceleration of log-relative trend."""
    r = _log_rel(pb, peer_median_pb)
    slope = _linslope(r, _TD_QTR)
    return slope.diff(5)


def vvp_drv2_009_pe_zscore_252d_5d_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of 252d z-score of P/E relative ratio (velocity of statistical extremity)."""
    r = _rel_ratio(pe, peer_median_pe)
    z = _zscore_rolling(r, _TD_YEAR)
    return z.diff(5)


def vvp_drv2_010_pb_zscore_252d_21d_diff(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """21-day diff of 252d z-score of P/B relative ratio (monthly velocity of z-score)."""
    r = _rel_ratio(pb, peer_median_pb)
    z = _zscore_rolling(r, _TD_YEAR)
    return z.diff(21)


def vvp_drv2_011_ps_rel_ratio_63d_diff_diff21(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """21-day diff of the 63-day change in P/S relative ratio (quarterly momentum velocity)."""
    r = _rel_ratio(ps, peer_median_ps)
    return r.diff(63).diff(21)


def vvp_drv2_012_pe_pctrank_252d_5d_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of 252-day rolling pct-rank of P/E relative ratio (rank shift pace)."""
    r = _rel_ratio(pe, peer_median_pe)
    rank = r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return rank.diff(5)


def vvp_drv2_013_evebit_rel_ratio_21d_accel(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """2nd difference (21d) of EV/EBIT relative ratio — monthly acceleration."""
    r = _rel_ratio(evebit, peer_median_evebit)
    return r.diff(21).diff(21)


def vvp_drv2_014_log_pe_ewm21_5d_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of EWM(21) of log(P/E/peer) — smooth short-run log-velocity."""
    r = _log_rel(pe, peer_median_pe)
    return _ewm_mean(r, 21).diff(5)


def vvp_drv2_015_divyield_rel_ratio_21d_diff_diff5(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """5-day diff of 21-day diff in div-yield relative ratio (acceleration of yield-advantage shift)."""
    r = _rel_ratio(divyield, peer_median_divyield)
    return r.diff(21).diff(5)


def vvp_drv2_016_composite_zscore_3m_5d_diff(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series
) -> pd.Series:
    """5-day diff of composite (PE/PB/PS) 252d z-score (velocity of composite discount extremity)."""
    z_pe = _zscore_rolling(_rel_ratio(pe, peer_median_pe), _TD_YEAR)
    z_pb = _zscore_rolling(_rel_ratio(pb, peer_median_pb), _TD_YEAR)
    z_ps = _zscore_rolling(_rel_ratio(ps, peer_median_ps), _TD_YEAR)
    composite = (z_pe + z_pb + z_ps) / 3.0
    return composite.diff(5)


def vvp_drv2_017_pe_rel_ratio_slope_63d_21d_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """21-day diff of 63d OLS slope of P/E relative ratio (change in slope = curvature)."""
    r     = _rel_ratio(pe, peer_median_pe)
    slope = _linslope(r, _TD_QTR)
    return slope.diff(21)


def vvp_drv2_018_pb_rel_ratio_vs_mean_5d_diff(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5-day diff of (P/B relative ratio minus its 252-day mean) — velocity of deviation."""
    r    = _rel_ratio(pb, peer_median_pb)
    dev  = r - _rolling_mean(r, _TD_YEAR)
    return dev.diff(5)


def vvp_drv2_019_ps_rel_ratio_vs_mean_21d_diff(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """21-day diff of (P/S relative ratio minus its 252-day mean)."""
    r   = _rel_ratio(ps, peer_median_ps)
    dev = r - _rolling_mean(r, _TD_YEAR)
    return dev.diff(21)


def vvp_drv2_020_pe_derate_speed_21d_5d_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of the 21-day pct-change of P/E relative ratio (acceleration of pct de-rate)."""
    r = _rel_ratio(pe, peer_median_pe)
    return r.pct_change(21).diff(5)


def vvp_drv2_021_multi_discount_score_5d_diff(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series
) -> pd.Series:
    """5-day diff of multi-metric discount count (PE/PB/PS) — velocity of breadth widening."""
    score = (
        _discount_flag(pe, peer_median_pe) +
        _discount_flag(pb, peer_median_pb) +
        _discount_flag(ps, peer_median_ps)
    )
    return score.diff(5)


def vvp_drv2_022_log_evebitda_slope_diff5(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """5-day diff of 63d slope of log(EV/EBITDA/peer) (acceleration of log-trend)."""
    r     = _log_rel(evebitda, peer_median_evebitda)
    slope = _linslope(r, _TD_QTR)
    return slope.diff(5)


def vvp_drv2_023_pe_rel_ratio_ath_dd_5d_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of P/E-relative-ratio ATH drawdown (velocity of discount deepening from peak)."""
    r    = _rel_ratio(pe, peer_median_pe)
    peak = r.expanding(min_periods=1).max()
    dd   = _safe_div(r - peak, peak.abs())
    return dd.diff(5)


def vvp_drv2_024_evebitda_frac_below_peer_5d_diff(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """5-day diff of 252-day below-peer fraction for EV/EBITDA (pace of discount frequency rise)."""
    below = _discount_flag(evebitda, peer_median_evebitda)
    frac  = _rolling_mean(below, _TD_YEAR)
    return frac.diff(5)


def vvp_drv2_025_log_rel_all_4_ewm_5d_diff(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series
) -> pd.Series:
    """5-day diff of EWM(21) composite log-relative (PE/PB/PS/EVEBITDA) velocity."""
    composite = (
        _log_rel(pe, peer_median_pe) +
        _log_rel(pb, peer_median_pb) +
        _log_rel(ps, peer_median_ps) +
        _log_rel(evebitda, peer_median_evebitda)
    ) / 4.0
    return _ewm_mean(composite, 21).diff(5)


# ── 2nd-Derivative Feature Functions (drv2_026-075) ──────────────────────────

# --- Group D2a (026-035): 21d diff of EWM-smoothed relative ratios ---

def vvp_drv2_026_pe_rel_ewm21_21d_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """21-day diff of EWM(21) of P/E relative ratio (monthly velocity of smooth signal)."""
    return _ewm_mean(_rel_ratio(pe, peer_median_pe), _TD_MON).diff(21)


def vvp_drv2_027_pb_rel_ewm63_5d_diff(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5-day diff of EWM(63) of P/B relative ratio (short-run velocity of quarterly-smooth)."""
    return _ewm_mean(_rel_ratio(pb, peer_median_pb), _TD_QTR).diff(5)


def vvp_drv2_028_ps_rel_ewm21_5d_diff(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """5-day diff of EWM(21) of P/S relative ratio."""
    return _ewm_mean(_rel_ratio(ps, peer_median_ps), _TD_MON).diff(5)


def vvp_drv2_029_evebit_rel_ewm21_5d_diff(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """5-day diff of EWM(21) of EV/EBIT relative ratio."""
    return _ewm_mean(_rel_ratio(evebit, peer_median_evebit), _TD_MON).diff(5)


def vvp_drv2_030_divyield_rel_ewm21_21d_diff(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """21-day diff of EWM(21) of div-yield relative ratio (monthly yield-advantage velocity)."""
    return _ewm_mean(_rel_ratio(divyield, peer_median_divyield), _TD_MON).diff(21)


def vvp_drv2_031_log_pe_ewm63_5d_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of EWM(63) of log(P/E/peer) — quarterly-smooth log velocity."""
    return _ewm_mean(_log_rel(pe, peer_median_pe), _TD_QTR).diff(5)


def vvp_drv2_032_log_pb_ewm21_21d_diff(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """21-day diff of EWM(21) of log(P/B/peer)."""
    return _ewm_mean(_log_rel(pb, peer_median_pb), _TD_MON).diff(21)


def vvp_drv2_033_evebitda_rel_ewm63_21d_diff(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """21-day diff of EWM(63) of EV/EBITDA relative ratio."""
    return _ewm_mean(_rel_ratio(evebitda, peer_median_evebitda), _TD_QTR).diff(21)


def vvp_drv2_034_log_ps_ewm21_5d_diff(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """5-day diff of EWM(21) of log(P/S/peer)."""
    return _ewm_mean(_log_rel(ps, peer_median_ps), _TD_MON).diff(5)


def vvp_drv2_035_marketcap_rel_ewm63_5d_diff(marketcap: pd.Series, peer_median_marketcap: pd.Series) -> pd.Series:
    """5-day diff of EWM(63) of market-cap relative ratio (size-relative velocity)."""
    return _ewm_mean(_rel_ratio(marketcap, peer_median_marketcap), _TD_QTR).diff(5)


# --- Group D2b (036-045): diff of rolling median of relative ratio ---

def vvp_drv2_036_pe_rel_median63_5d_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of 63-day rolling median of P/E relative ratio."""
    return _rolling_median(_rel_ratio(pe, peer_median_pe), _TD_QTR).diff(5)


def vvp_drv2_037_pb_rel_median252_5d_diff(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5-day diff of 252-day rolling median of P/B relative ratio."""
    return _rolling_median(_rel_ratio(pb, peer_median_pb), _TD_YEAR).diff(5)


def vvp_drv2_038_ps_rel_median63_21d_diff(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """21-day diff of 63-day rolling median of P/S relative ratio."""
    return _rolling_median(_rel_ratio(ps, peer_median_ps), _TD_QTR).diff(21)


def vvp_drv2_039_evebitda_rel_median252_21d_diff(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """21-day diff of 252-day rolling median of EV/EBITDA relative ratio."""
    return _rolling_median(_rel_ratio(evebitda, peer_median_evebitda), _TD_YEAR).diff(21)


def vvp_drv2_040_divyield_rel_median63_5d_diff(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """5-day diff of 63-day rolling median of div-yield relative ratio."""
    return _rolling_median(_rel_ratio(divyield, peer_median_divyield), _TD_QTR).diff(5)


# --- Group D2c (041-050): diff of z-score at alternate windows ---

def vvp_drv2_041_ps_zscore_252d_5d_diff(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """5-day diff of 252d z-score of P/S relative ratio."""
    return _zscore_rolling(_rel_ratio(ps, peer_median_ps), _TD_YEAR).diff(5)


def vvp_drv2_042_evebitda_zscore_252d_21d_diff(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """21-day diff of 252d z-score of EV/EBITDA relative ratio."""
    return _zscore_rolling(_rel_ratio(evebitda, peer_median_evebitda), _TD_YEAR).diff(21)


def vvp_drv2_043_evebit_zscore_252d_5d_diff(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """5-day diff of 252d z-score of EV/EBIT relative ratio."""
    return _zscore_rolling(_rel_ratio(evebit, peer_median_evebit), _TD_YEAR).diff(5)


def vvp_drv2_044_log_pe_zscore_252d_21d_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """21-day diff of 252d z-score of log(P/E/peer) — monthly velocity of log z-score."""
    return _zscore_rolling(_log_rel(pe, peer_median_pe), _TD_YEAR).diff(21)


def vvp_drv2_045_log_pb_zscore_252d_5d_diff(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5-day diff of 252d z-score of log(P/B/peer)."""
    return _zscore_rolling(_log_rel(pb, peer_median_pb), _TD_YEAR).diff(5)


def vvp_drv2_046_divyield_zscore_252d_5d_diff(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """5-day diff of 252d z-score of div-yield relative ratio."""
    return _zscore_rolling(_rel_ratio(divyield, peer_median_divyield), _TD_YEAR).diff(5)


def vvp_drv2_047_pe_zscore_504d_5d_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of 504d z-score of P/E relative ratio (2-year z-score velocity)."""
    return _zscore_rolling(_rel_ratio(pe, peer_median_pe), _TD_2Y).diff(5)


def vvp_drv2_048_composite_zscore_4m_21d_diff(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    evebit: pd.Series, peer_median_evebit: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series
) -> pd.Series:
    """21-day diff of composite (PE/PB/EVEBIT/EVEBITDA) 252d z-score (4-metric velocity)."""
    z = (
        _zscore_rolling(_rel_ratio(pe, peer_median_pe), _TD_YEAR) +
        _zscore_rolling(_rel_ratio(pb, peer_median_pb), _TD_YEAR) +
        _zscore_rolling(_rel_ratio(evebit, peer_median_evebit), _TD_YEAR) +
        _zscore_rolling(_rel_ratio(evebitda, peer_median_evebitda), _TD_YEAR)
    ) / 4.0
    return z.diff(21)


def vvp_drv2_049_log_ps_zscore_252d_5d_diff(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """5-day diff of 252d z-score of log(P/S/peer)."""
    return _zscore_rolling(_log_rel(ps, peer_median_ps), _TD_YEAR).diff(5)


def vvp_drv2_050_log_evebitda_zscore_252d_5d_diff(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """5-day diff of 252d z-score of log(EV/EBITDA/peer)."""
    return _zscore_rolling(_log_rel(evebitda, peer_median_evebitda), _TD_YEAR).diff(5)


# --- Group D2d (051-060): diff of percentile-rank features ---

def vvp_drv2_051_pb_pctrank_252d_5d_diff(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5-day diff of 252d pct-rank of P/B relative ratio (P/B rank shift pace)."""
    r = _rel_ratio(pb, peer_median_pb)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).diff(5)


def vvp_drv2_052_ps_pctrank_252d_21d_diff(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """21-day diff of 252d pct-rank of P/S relative ratio."""
    r = _rel_ratio(ps, peer_median_ps)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).diff(21)


def vvp_drv2_053_evebitda_pctrank_252d_5d_diff(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """5-day diff of 252d pct-rank of EV/EBITDA relative ratio."""
    r = _rel_ratio(evebitda, peer_median_evebitda)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).diff(5)


def vvp_drv2_054_divyield_pctrank_252d_5d_diff(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """5-day diff of 252d pct-rank of div-yield relative ratio."""
    r = _rel_ratio(divyield, peer_median_divyield)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).diff(5)


def vvp_drv2_055_evebit_pctrank_252d_21d_diff(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """21-day diff of 252d pct-rank of EV/EBIT relative ratio."""
    r = _rel_ratio(evebit, peer_median_evebit)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).diff(21)


def vvp_drv2_056_composite_pctrank_3m_5d_diff(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series
) -> pd.Series:
    """5-day diff of composite (PE/PB/PS) 252d pct-rank (velocity of breadth-rank)."""
    def _rank252(s):
        return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    composite = (
        _rank252(_rel_ratio(pe, peer_median_pe)) +
        _rank252(_rel_ratio(pb, peer_median_pb)) +
        _rank252(_rel_ratio(ps, peer_median_ps))
    ) / 3.0
    return composite.diff(5)


def vvp_drv2_057_pe_expanding_pctrank_5d_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of expanding pct-rank of P/E relative ratio."""
    r = _rel_ratio(pe, peer_median_pe)
    return r.expanding(min_periods=21).rank(pct=True).diff(5)


def vvp_drv2_058_pb_expanding_pctrank_5d_diff(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5-day diff of expanding pct-rank of P/B relative ratio."""
    r = _rel_ratio(pb, peer_median_pb)
    return r.expanding(min_periods=21).rank(pct=True).diff(5)


def vvp_drv2_059_log_pe_pctrank_252d_21d_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """21-day diff of 252d pct-rank of log(P/E/peer)."""
    r = _log_rel(pe, peer_median_pe)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).diff(21)


def vvp_drv2_060_marketcap_rel_pctrank_252d_5d_diff(marketcap: pd.Series, peer_median_marketcap: pd.Series) -> pd.Series:
    """5-day diff of 252d pct-rank of market-cap relative ratio (size-rank velocity)."""
    r = _rel_ratio(marketcap, peer_median_marketcap)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).diff(5)


# --- Group D2e (061-075): diff of discount flags, persistence, and drawdown features ---

def vvp_drv2_061_ps_frac_below_peer_252d_5d_diff(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """5-day diff of 252-day below-peer fraction for P/S."""
    return _rolling_mean(_discount_flag(ps, peer_median_ps), _TD_YEAR).diff(5)


def vvp_drv2_062_evebit_frac_below_peer_252d_21d_diff(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """21-day diff of 252-day below-peer fraction for EV/EBIT."""
    return _rolling_mean(_discount_flag(evebit, peer_median_evebit), _TD_YEAR).diff(21)


def vvp_drv2_063_divyield_frac_above_peer_252d_5d_diff(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """5-day diff of 252-day above-peer fraction for div yield (yield-advantage momentum)."""
    above = (divyield > peer_median_divyield).astype(float)
    return _rolling_mean(above, _TD_YEAR).diff(5)


def vvp_drv2_064_pe_frac_below_63d_5d_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of 63-day below-peer fraction for P/E (short-window discount frequency vel.)."""
    return _rolling_mean(_discount_flag(pe, peer_median_pe), _TD_QTR).diff(5)


def vvp_drv2_065_pb_frac_below_63d_5d_diff(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5-day diff of 63-day below-peer fraction for P/B."""
    return _rolling_mean(_discount_flag(pb, peer_median_pb), _TD_QTR).diff(5)


def vvp_drv2_066_multi_discount_score_21d_diff(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series
) -> pd.Series:
    """21-day diff of multi-metric discount count (PE/PB/PS) — monthly breadth velocity."""
    score = (
        _discount_flag(pe, peer_median_pe) +
        _discount_flag(pb, peer_median_pb) +
        _discount_flag(ps, peer_median_ps)
    )
    return score.diff(21)


def vvp_drv2_067_discount_count_5m_5d_diff(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series,
    evebit: pd.Series, peer_median_evebit: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series
) -> pd.Series:
    """5-day diff of 5-metric discount count (velocity of full-breadth de-rating)."""
    score = (
        _discount_flag(pe, peer_median_pe) +
        _discount_flag(pb, peer_median_pb) +
        _discount_flag(ps, peer_median_ps) +
        _discount_flag(evebit, peer_median_evebit) +
        _discount_flag(evebitda, peer_median_evebitda)
    )
    return score.diff(5)


def vvp_drv2_068_pb_rel_ratio_ath_dd_5d_diff(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """5-day diff of P/B relative-ratio ATH drawdown (velocity of P/B discount deepening)."""
    r    = _rel_ratio(pb, peer_median_pb)
    peak = r.expanding(min_periods=1).max()
    dd   = _safe_div(r - peak, peak.abs())
    return dd.diff(5)


def vvp_drv2_069_evebitda_rel_ratio_ath_dd_5d_diff(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """5-day diff of EV/EBITDA relative-ratio ATH drawdown."""
    r    = _rel_ratio(evebitda, peer_median_evebitda)
    peak = r.expanding(min_periods=1).max()
    dd   = _safe_div(r - peak, peak.abs())
    return dd.diff(5)


def vvp_drv2_070_pe_rel_vs_mean_21d_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """21-day diff of (P/E relative ratio minus its 252-day mean)."""
    r = _rel_ratio(pe, peer_median_pe)
    return (r - _rolling_mean(r, _TD_YEAR)).diff(21)


def vvp_drv2_071_evebit_rel_vs_mean_5d_diff(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """5-day diff of (EV/EBIT relative ratio minus its 252-day mean)."""
    r = _rel_ratio(evebit, peer_median_evebit)
    return (r - _rolling_mean(r, _TD_YEAR)).diff(5)


def vvp_drv2_072_divyield_rel_vs_mean_5d_diff(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """5-day diff of (div-yield relative ratio minus its 252-day mean)."""
    r = _rel_ratio(divyield, peer_median_divyield)
    return (r - _rolling_mean(r, _TD_YEAR)).diff(5)


def vvp_drv2_073_log_pe_linslope_63d_5d_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of 63d OLS slope of log(P/E/peer) (log-slope acceleration)."""
    return _linslope(_log_rel(pe, peer_median_pe), _TD_QTR).diff(5)


def vvp_drv2_074_pe_derate_speed_63d_5d_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day diff of 63-day pct-change of P/E relative ratio (quarterly de-rate acceleration)."""
    return _rel_ratio(pe, peer_median_pe).pct_change(63).diff(5)


def vvp_drv2_075_pb_derate_speed_63d_21d_diff(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """21-day diff of 63-day pct-change of P/B relative ratio."""
    return _rel_ratio(pb, peer_median_pb).pct_change(63).diff(21)


# ── Registry ──────────────────────────────────────────────────────────────────

VALUATION_VS_PEERS_REGISTRY_2ND_DERIVATIVES = {
    "vvp_drv2_001_pe_rel_ratio_5d_accel":            {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv2_001_pe_rel_ratio_5d_accel},
    "vvp_drv2_002_log_pe_21d_diff_diff5":            {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv2_002_log_pe_21d_diff_diff5},
    "vvp_drv2_003_pb_rel_ratio_21d_accel":           {"inputs": ["pb", "peer_median_pb"],                                                                                                   "func": vvp_drv2_003_pb_rel_ratio_21d_accel},
    "vvp_drv2_004_ps_rel_ratio_5d_diff_of_slope63":  {"inputs": ["ps", "peer_median_ps"],                                                                                                   "func": vvp_drv2_004_ps_rel_ratio_5d_diff_of_slope63},
    "vvp_drv2_005_evebitda_rel_ratio_21d_diff_diff5":{"inputs": ["evebitda", "peer_median_evebitda"],                                                                                       "func": vvp_drv2_005_evebitda_rel_ratio_21d_diff_diff5},
    "vvp_drv2_006_pe_frac_below_peer_252d_5d_diff":  {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv2_006_pe_frac_below_peer_252d_5d_diff},
    "vvp_drv2_007_pb_frac_below_peer_252d_21d_diff": {"inputs": ["pb", "peer_median_pb"],                                                                                                   "func": vvp_drv2_007_pb_frac_below_peer_252d_21d_diff},
    "vvp_drv2_008_log_pb_slope_diff5":               {"inputs": ["pb", "peer_median_pb"],                                                                                                   "func": vvp_drv2_008_log_pb_slope_diff5},
    "vvp_drv2_009_pe_zscore_252d_5d_diff":           {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv2_009_pe_zscore_252d_5d_diff},
    "vvp_drv2_010_pb_zscore_252d_21d_diff":          {"inputs": ["pb", "peer_median_pb"],                                                                                                   "func": vvp_drv2_010_pb_zscore_252d_21d_diff},
    "vvp_drv2_011_ps_rel_ratio_63d_diff_diff21":     {"inputs": ["ps", "peer_median_ps"],                                                                                                   "func": vvp_drv2_011_ps_rel_ratio_63d_diff_diff21},
    "vvp_drv2_012_pe_pctrank_252d_5d_diff":          {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv2_012_pe_pctrank_252d_5d_diff},
    "vvp_drv2_013_evebit_rel_ratio_21d_accel":       {"inputs": ["evebit", "peer_median_evebit"],                                                                                           "func": vvp_drv2_013_evebit_rel_ratio_21d_accel},
    "vvp_drv2_014_log_pe_ewm21_5d_diff":             {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv2_014_log_pe_ewm21_5d_diff},
    "vvp_drv2_015_divyield_rel_ratio_21d_diff_diff5":{"inputs": ["divyield", "peer_median_divyield"],                                                                                       "func": vvp_drv2_015_divyield_rel_ratio_21d_diff_diff5},
    "vvp_drv2_016_composite_zscore_3m_5d_diff":      {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps"],                                                   "func": vvp_drv2_016_composite_zscore_3m_5d_diff},
    "vvp_drv2_017_pe_rel_ratio_slope_63d_21d_diff":  {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv2_017_pe_rel_ratio_slope_63d_21d_diff},
    "vvp_drv2_018_pb_rel_ratio_vs_mean_5d_diff":     {"inputs": ["pb", "peer_median_pb"],                                                                                                   "func": vvp_drv2_018_pb_rel_ratio_vs_mean_5d_diff},
    "vvp_drv2_019_ps_rel_ratio_vs_mean_21d_diff":    {"inputs": ["ps", "peer_median_ps"],                                                                                                   "func": vvp_drv2_019_ps_rel_ratio_vs_mean_21d_diff},
    "vvp_drv2_020_pe_derate_speed_21d_5d_diff":      {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv2_020_pe_derate_speed_21d_5d_diff},
    "vvp_drv2_021_multi_discount_score_5d_diff":     {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps"],                                                   "func": vvp_drv2_021_multi_discount_score_5d_diff},
    "vvp_drv2_022_log_evebitda_slope_diff5":         {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                       "func": vvp_drv2_022_log_evebitda_slope_diff5},
    "vvp_drv2_023_pe_rel_ratio_ath_dd_5d_diff":      {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv2_023_pe_rel_ratio_ath_dd_5d_diff},
    "vvp_drv2_024_evebitda_frac_below_peer_5d_diff": {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                       "func": vvp_drv2_024_evebitda_frac_below_peer_5d_diff},
    "vvp_drv2_025_log_rel_all_4_ewm_5d_diff":        {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps", "evebitda", "peer_median_evebitda"],              "func": vvp_drv2_025_log_rel_all_4_ewm_5d_diff},
    "vvp_drv2_026_pe_rel_ewm21_21d_diff":            {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv2_026_pe_rel_ewm21_21d_diff},
    "vvp_drv2_027_pb_rel_ewm63_5d_diff":             {"inputs": ["pb", "peer_median_pb"],                                                                                                   "func": vvp_drv2_027_pb_rel_ewm63_5d_diff},
    "vvp_drv2_028_ps_rel_ewm21_5d_diff":             {"inputs": ["ps", "peer_median_ps"],                                                                                                   "func": vvp_drv2_028_ps_rel_ewm21_5d_diff},
    "vvp_drv2_029_evebit_rel_ewm21_5d_diff":         {"inputs": ["evebit", "peer_median_evebit"],                                                                                           "func": vvp_drv2_029_evebit_rel_ewm21_5d_diff},
    "vvp_drv2_030_divyield_rel_ewm21_21d_diff":      {"inputs": ["divyield", "peer_median_divyield"],                                                                                       "func": vvp_drv2_030_divyield_rel_ewm21_21d_diff},
    "vvp_drv2_031_log_pe_ewm63_5d_diff":             {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv2_031_log_pe_ewm63_5d_diff},
    "vvp_drv2_032_log_pb_ewm21_21d_diff":            {"inputs": ["pb", "peer_median_pb"],                                                                                                   "func": vvp_drv2_032_log_pb_ewm21_21d_diff},
    "vvp_drv2_033_evebitda_rel_ewm63_21d_diff":      {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                       "func": vvp_drv2_033_evebitda_rel_ewm63_21d_diff},
    "vvp_drv2_034_log_ps_ewm21_5d_diff":             {"inputs": ["ps", "peer_median_ps"],                                                                                                   "func": vvp_drv2_034_log_ps_ewm21_5d_diff},
    "vvp_drv2_035_marketcap_rel_ewm63_5d_diff":      {"inputs": ["marketcap", "peer_median_marketcap"],                                                                                     "func": vvp_drv2_035_marketcap_rel_ewm63_5d_diff},
    "vvp_drv2_036_pe_rel_median63_5d_diff":          {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv2_036_pe_rel_median63_5d_diff},
    "vvp_drv2_037_pb_rel_median252_5d_diff":         {"inputs": ["pb", "peer_median_pb"],                                                                                                   "func": vvp_drv2_037_pb_rel_median252_5d_diff},
    "vvp_drv2_038_ps_rel_median63_21d_diff":         {"inputs": ["ps", "peer_median_ps"],                                                                                                   "func": vvp_drv2_038_ps_rel_median63_21d_diff},
    "vvp_drv2_039_evebitda_rel_median252_21d_diff":  {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                       "func": vvp_drv2_039_evebitda_rel_median252_21d_diff},
    "vvp_drv2_040_divyield_rel_median63_5d_diff":    {"inputs": ["divyield", "peer_median_divyield"],                                                                                       "func": vvp_drv2_040_divyield_rel_median63_5d_diff},
    "vvp_drv2_041_ps_zscore_252d_5d_diff":           {"inputs": ["ps", "peer_median_ps"],                                                                                                   "func": vvp_drv2_041_ps_zscore_252d_5d_diff},
    "vvp_drv2_042_evebitda_zscore_252d_21d_diff":    {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                       "func": vvp_drv2_042_evebitda_zscore_252d_21d_diff},
    "vvp_drv2_043_evebit_zscore_252d_5d_diff":       {"inputs": ["evebit", "peer_median_evebit"],                                                                                           "func": vvp_drv2_043_evebit_zscore_252d_5d_diff},
    "vvp_drv2_044_log_pe_zscore_252d_21d_diff":      {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv2_044_log_pe_zscore_252d_21d_diff},
    "vvp_drv2_045_log_pb_zscore_252d_5d_diff":       {"inputs": ["pb", "peer_median_pb"],                                                                                                   "func": vvp_drv2_045_log_pb_zscore_252d_5d_diff},
    "vvp_drv2_046_divyield_zscore_252d_5d_diff":     {"inputs": ["divyield", "peer_median_divyield"],                                                                                       "func": vvp_drv2_046_divyield_zscore_252d_5d_diff},
    "vvp_drv2_047_pe_zscore_504d_5d_diff":           {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv2_047_pe_zscore_504d_5d_diff},
    "vvp_drv2_048_composite_zscore_4m_21d_diff":     {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "evebit", "peer_median_evebit", "evebitda", "peer_median_evebitda"],      "func": vvp_drv2_048_composite_zscore_4m_21d_diff},
    "vvp_drv2_049_log_ps_zscore_252d_5d_diff":       {"inputs": ["ps", "peer_median_ps"],                                                                                                   "func": vvp_drv2_049_log_ps_zscore_252d_5d_diff},
    "vvp_drv2_050_log_evebitda_zscore_252d_5d_diff": {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                       "func": vvp_drv2_050_log_evebitda_zscore_252d_5d_diff},
    "vvp_drv2_051_pb_pctrank_252d_5d_diff":          {"inputs": ["pb", "peer_median_pb"],                                                                                                   "func": vvp_drv2_051_pb_pctrank_252d_5d_diff},
    "vvp_drv2_052_ps_pctrank_252d_21d_diff":         {"inputs": ["ps", "peer_median_ps"],                                                                                                   "func": vvp_drv2_052_ps_pctrank_252d_21d_diff},
    "vvp_drv2_053_evebitda_pctrank_252d_5d_diff":    {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                       "func": vvp_drv2_053_evebitda_pctrank_252d_5d_diff},
    "vvp_drv2_054_divyield_pctrank_252d_5d_diff":    {"inputs": ["divyield", "peer_median_divyield"],                                                                                       "func": vvp_drv2_054_divyield_pctrank_252d_5d_diff},
    "vvp_drv2_055_evebit_pctrank_252d_21d_diff":     {"inputs": ["evebit", "peer_median_evebit"],                                                                                           "func": vvp_drv2_055_evebit_pctrank_252d_21d_diff},
    "vvp_drv2_056_composite_pctrank_3m_5d_diff":     {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps"],                                                   "func": vvp_drv2_056_composite_pctrank_3m_5d_diff},
    "vvp_drv2_057_pe_expanding_pctrank_5d_diff":     {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv2_057_pe_expanding_pctrank_5d_diff},
    "vvp_drv2_058_pb_expanding_pctrank_5d_diff":     {"inputs": ["pb", "peer_median_pb"],                                                                                                   "func": vvp_drv2_058_pb_expanding_pctrank_5d_diff},
    "vvp_drv2_059_log_pe_pctrank_252d_21d_diff":     {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv2_059_log_pe_pctrank_252d_21d_diff},
    "vvp_drv2_060_marketcap_rel_pctrank_252d_5d_diff": {"inputs": ["marketcap", "peer_median_marketcap"],                                                                                   "func": vvp_drv2_060_marketcap_rel_pctrank_252d_5d_diff},
    "vvp_drv2_061_ps_frac_below_peer_252d_5d_diff":  {"inputs": ["ps", "peer_median_ps"],                                                                                                   "func": vvp_drv2_061_ps_frac_below_peer_252d_5d_diff},
    "vvp_drv2_062_evebit_frac_below_peer_252d_21d_diff": {"inputs": ["evebit", "peer_median_evebit"],                                                                                      "func": vvp_drv2_062_evebit_frac_below_peer_252d_21d_diff},
    "vvp_drv2_063_divyield_frac_above_peer_252d_5d_diff": {"inputs": ["divyield", "peer_median_divyield"],                                                                                 "func": vvp_drv2_063_divyield_frac_above_peer_252d_5d_diff},
    "vvp_drv2_064_pe_frac_below_63d_5d_diff":        {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv2_064_pe_frac_below_63d_5d_diff},
    "vvp_drv2_065_pb_frac_below_63d_5d_diff":        {"inputs": ["pb", "peer_median_pb"],                                                                                                   "func": vvp_drv2_065_pb_frac_below_63d_5d_diff},
    "vvp_drv2_066_multi_discount_score_21d_diff":    {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps"],                                                   "func": vvp_drv2_066_multi_discount_score_21d_diff},
    "vvp_drv2_067_discount_count_5m_5d_diff":        {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps", "evebit", "peer_median_evebit", "evebitda", "peer_median_evebitda"], "func": vvp_drv2_067_discount_count_5m_5d_diff},
    "vvp_drv2_068_pb_rel_ratio_ath_dd_5d_diff":      {"inputs": ["pb", "peer_median_pb"],                                                                                                   "func": vvp_drv2_068_pb_rel_ratio_ath_dd_5d_diff},
    "vvp_drv2_069_evebitda_rel_ratio_ath_dd_5d_diff": {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                     "func": vvp_drv2_069_evebitda_rel_ratio_ath_dd_5d_diff},
    "vvp_drv2_070_pe_rel_vs_mean_21d_diff":          {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv2_070_pe_rel_vs_mean_21d_diff},
    "vvp_drv2_071_evebit_rel_vs_mean_5d_diff":       {"inputs": ["evebit", "peer_median_evebit"],                                                                                           "func": vvp_drv2_071_evebit_rel_vs_mean_5d_diff},
    "vvp_drv2_072_divyield_rel_vs_mean_5d_diff":     {"inputs": ["divyield", "peer_median_divyield"],                                                                                       "func": vvp_drv2_072_divyield_rel_vs_mean_5d_diff},
    "vvp_drv2_073_log_pe_linslope_63d_5d_diff":      {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv2_073_log_pe_linslope_63d_5d_diff},
    "vvp_drv2_074_pe_derate_speed_63d_5d_diff":      {"inputs": ["pe", "peer_median_pe"],                                                                                                   "func": vvp_drv2_074_pe_derate_speed_63d_5d_diff},
    "vvp_drv2_075_pb_derate_speed_63d_21d_diff":     {"inputs": ["pb", "peer_median_pb"],                                                                                                   "func": vvp_drv2_075_pb_derate_speed_63d_21d_diff},
}
