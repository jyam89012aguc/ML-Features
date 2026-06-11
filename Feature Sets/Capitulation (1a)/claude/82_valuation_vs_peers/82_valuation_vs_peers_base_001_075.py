"""
82_valuation_vs_peers — Base Features 001-100
Domain: multiples vs sector/industry peer medians (cross-sectional valuation)
Asset class: US equities | Daily valuation metrics (SF1-derived, daily frequency)
Target context: capitulation — absolute multi-year low / maximum distress

PEER-MEDIAN INPUT CONTRACT:
    Each function receives the ticker's own daily metric Series and a precomputed
    sector/industry peer-median Series of the same daily index named
    peer_median_<metric>  (e.g. peer_median_pe, peer_median_pb, peer_median_ps,
    peer_median_ev, peer_median_marketcap, peer_median_evebit, peer_median_evebitda,
    peer_median_divyield).  The pipeline computes these universe-wide sector/industry
    medians and passes them in.  All functions look strictly backward.

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
    """Log of absolute value; preserves sign for ratio series."""
    return np.log(s.abs().clip(lower=_EPS))


def _rel_ratio(own: pd.Series, peer: pd.Series) -> pd.Series:
    """Own / peer-median ratio; NaN where either is near-zero."""
    return _safe_div(own, peer)


def _log_rel(own: pd.Series, peer: pd.Series) -> pd.Series:
    """Log(own / peer) — signed log-ratio of multiples."""
    ratio = _rel_ratio(own, peer)
    return np.log(ratio.abs().clip(lower=_EPS)) * np.sign(ratio)


def _gap(own: pd.Series, peer: pd.Series) -> pd.Series:
    """Absolute additive gap: own - peer."""
    return own - peer


def _discount_flag(own: pd.Series, peer: pd.Series) -> pd.Series:
    """1 if own < peer (trading at discount), 0 otherwise."""
    return (own < peer).astype(float)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Raw relative-valuation ratios by metric ---

def vvp_001_pe_ratio_to_peer(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """P/E ratio relative to sector peer median (own / peer)."""
    return _rel_ratio(pe, peer_median_pe)


def vvp_002_pb_ratio_to_peer(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """P/B ratio relative to sector peer median (own / peer)."""
    return _rel_ratio(pb, peer_median_pb)


def vvp_003_ps_ratio_to_peer(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """P/S ratio relative to sector peer median (own / peer)."""
    return _rel_ratio(ps, peer_median_ps)


def vvp_004_evebit_ratio_to_peer(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """EV/EBIT ratio relative to sector peer median (own / peer)."""
    return _rel_ratio(evebit, peer_median_evebit)


def vvp_005_evebitda_ratio_to_peer(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA ratio relative to sector peer median (own / peer)."""
    return _rel_ratio(evebitda, peer_median_evebitda)


def vvp_006_marketcap_ratio_to_peer(marketcap: pd.Series, peer_median_marketcap: pd.Series) -> pd.Series:
    """Market cap relative to peer median (size relative)."""
    return _rel_ratio(marketcap, peer_median_marketcap)


def vvp_007_ev_ratio_to_peer(ev: pd.Series, peer_median_ev: pd.Series) -> pd.Series:
    """EV relative to peer median EV (enterprise size relative)."""
    return _rel_ratio(ev, peer_median_ev)


def vvp_008_divyield_ratio_to_peer(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """Dividend yield relative to peer median (own / peer; >1 means higher yield)."""
    return _rel_ratio(divyield, peer_median_divyield)


# --- Group B (009-016): Log-ratios (signed log-relative-valuation) ---

def vvp_009_log_pe_vs_peer(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Signed log-ratio of P/E to peer median (negative = discount)."""
    return _log_rel(pe, peer_median_pe)


def vvp_010_log_pb_vs_peer(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Signed log-ratio of P/B to peer median."""
    return _log_rel(pb, peer_median_pb)


def vvp_011_log_ps_vs_peer(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """Signed log-ratio of P/S to peer median."""
    return _log_rel(ps, peer_median_ps)


def vvp_012_log_evebitda_vs_peer(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """Signed log-ratio of EV/EBITDA to peer median."""
    return _log_rel(evebitda, peer_median_evebitda)


def vvp_013_log_evebit_vs_peer(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """Signed log-ratio of EV/EBIT to peer median."""
    return _log_rel(evebit, peer_median_evebit)


def vvp_014_log_divyield_vs_peer(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """Signed log-ratio of div yield to peer median (positive = higher yield than peers)."""
    return _log_rel(divyield, peer_median_divyield)


# --- Group C (015-022): Absolute additive gaps ---

def vvp_015_pe_gap_vs_peer(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Additive P/E gap (own minus peer median)."""
    return _gap(pe, peer_median_pe)


def vvp_016_pb_gap_vs_peer(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Additive P/B gap (own minus peer median)."""
    return _gap(pb, peer_median_pb)


def vvp_017_ps_gap_vs_peer(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """Additive P/S gap (own minus peer median)."""
    return _gap(ps, peer_median_ps)


def vvp_018_evebitda_gap_vs_peer(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """Additive EV/EBITDA gap (own minus peer median)."""
    return _gap(evebitda, peer_median_evebitda)


def vvp_019_evebit_gap_vs_peer(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """Additive EV/EBIT gap (own minus peer median)."""
    return _gap(evebit, peer_median_evebit)


def vvp_020_divyield_gap_vs_peer(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """Additive dividend yield gap (own minus peer median; positive = higher yield)."""
    return _gap(divyield, peer_median_divyield)


# --- Group D (021-030): Discount flags and discount depth ---

def vvp_021_pe_discount_flag(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """1 if stock P/E < peer median (trading at P/E discount to peers)."""
    return _discount_flag(pe, peer_median_pe)


def vvp_022_pb_discount_flag(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """1 if stock P/B < peer median (trading at P/B discount)."""
    return _discount_flag(pb, peer_median_pb)


def vvp_023_ps_discount_flag(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """1 if stock P/S < peer median (trading at P/S discount)."""
    return _discount_flag(ps, peer_median_ps)


def vvp_024_evebitda_discount_flag(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """1 if stock EV/EBITDA < peer median."""
    return _discount_flag(evebitda, peer_median_evebitda)


def vvp_025_evebit_discount_flag(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """1 if stock EV/EBIT < peer median."""
    return _discount_flag(evebit, peer_median_evebit)


def vvp_026_multi_metric_discount_score(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series
) -> pd.Series:
    """Count of price multiples (PE/PB/PS) where ticker < peer median (0-3 score)."""
    return (
        _discount_flag(pe, peer_median_pe) +
        _discount_flag(pb, peer_median_pb) +
        _discount_flag(ps, peer_median_ps)
    )


def vvp_027_ev_discount_flag(ev: pd.Series, peer_median_ev: pd.Series) -> pd.Series:
    """1 if stock EV < peer median EV (smaller enterprise than peers)."""
    return _discount_flag(ev, peer_median_ev)


def vvp_028_pe_discount_depth(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Depth of P/E discount: (own - peer) / |peer|, clipped to <=0."""
    gap = _gap(pe, peer_median_pe)
    depth = _safe_div(gap, peer_median_pe.abs())
    return depth.clip(upper=0.0)


def vvp_029_pb_discount_depth(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Depth of P/B discount: (own - peer) / |peer|, clipped to <=0."""
    gap = _gap(pb, peer_median_pb)
    depth = _safe_div(gap, peer_median_pb.abs())
    return depth.clip(upper=0.0)


def vvp_030_ps_discount_depth(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """Depth of P/S discount: (own - peer) / |peer|, clipped to <=0."""
    gap = _gap(ps, peer_median_ps)
    depth = _safe_div(gap, peer_median_ps.abs())
    return depth.clip(upper=0.0)


# --- Group E (031-040): Rolling time-spent-below-peer metrics ---

def vvp_031_pe_frac_below_peer_63d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days where P/E < peer median."""
    below = _discount_flag(pe, peer_median_pe)
    return _rolling_mean(below, _TD_QTR)


def vvp_032_pe_frac_below_peer_252d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where P/E < peer median."""
    below = _discount_flag(pe, peer_median_pe)
    return _rolling_mean(below, _TD_YEAR)


def vvp_033_pb_frac_below_peer_63d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days where P/B < peer median."""
    below = _discount_flag(pb, peer_median_pb)
    return _rolling_mean(below, _TD_QTR)


def vvp_034_pb_frac_below_peer_252d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where P/B < peer median."""
    below = _discount_flag(pb, peer_median_pb)
    return _rolling_mean(below, _TD_YEAR)


def vvp_035_ps_frac_below_peer_252d(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where P/S < peer median."""
    below = _discount_flag(ps, peer_median_ps)
    return _rolling_mean(below, _TD_YEAR)


def vvp_036_evebitda_frac_below_peer_252d(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where EV/EBITDA < peer median."""
    below = _discount_flag(evebitda, peer_median_evebitda)
    return _rolling_mean(below, _TD_YEAR)


def vvp_037_all_multiples_discount_frac_252d(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series
) -> pd.Series:
    """Fraction of 252 days where ALL three multiples (PE/PB/PS) are below peer."""
    all_below = (
        _discount_flag(pe, peer_median_pe) *
        _discount_flag(pb, peer_median_pb) *
        _discount_flag(ps, peer_median_ps)
    )
    return _rolling_mean(all_below, _TD_YEAR)


def vvp_038_pe_frac_below_peer_504d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Fraction of trailing 504 days where P/E < peer median."""
    below = _discount_flag(pe, peer_median_pe)
    return _rolling_mean(below, _TD_2Y)


def vvp_039_pb_frac_below_peer_504d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Fraction of trailing 504 days where P/B < peer median."""
    below = _discount_flag(pb, peer_median_pb)
    return _rolling_mean(below, _TD_2Y)


def vvp_040_divyield_frac_above_peer_252d(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where div yield > peer median (yield advantage)."""
    above = (divyield > peer_median_divyield).astype(float)
    return _rolling_mean(above, _TD_YEAR)


# --- Group F (041-050): Rolling mean of the relative-ratio over various windows ---

def vvp_041_pe_rel_ratio_mean_63d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """63-day rolling mean of P/E-to-peer ratio (sustained relative cheapness)."""
    return _rolling_mean(_rel_ratio(pe, peer_median_pe), _TD_QTR)


def vvp_042_pe_rel_ratio_mean_252d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """252-day rolling mean of P/E-to-peer ratio."""
    return _rolling_mean(_rel_ratio(pe, peer_median_pe), _TD_YEAR)


def vvp_043_pb_rel_ratio_mean_252d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """252-day rolling mean of P/B-to-peer ratio."""
    return _rolling_mean(_rel_ratio(pb, peer_median_pb), _TD_YEAR)


def vvp_044_ps_rel_ratio_mean_252d(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """252-day rolling mean of P/S-to-peer ratio."""
    return _rolling_mean(_rel_ratio(ps, peer_median_ps), _TD_YEAR)


def vvp_045_evebitda_rel_ratio_mean_252d(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """252-day rolling mean of EV/EBITDA-to-peer ratio."""
    return _rolling_mean(_rel_ratio(evebitda, peer_median_evebitda), _TD_YEAR)


def vvp_046_log_pe_vs_peer_mean_63d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """63-day rolling mean of log P/E-to-peer (smoother relative cheapness signal)."""
    return _rolling_mean(_log_rel(pe, peer_median_pe), _TD_QTR)


def vvp_047_log_pb_vs_peer_mean_252d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """252-day rolling mean of log P/B-to-peer."""
    return _rolling_mean(_log_rel(pb, peer_median_pb), _TD_YEAR)


def vvp_048_log_ps_vs_peer_mean_252d(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """252-day rolling mean of log P/S-to-peer."""
    return _rolling_mean(_log_rel(ps, peer_median_ps), _TD_YEAR)


def vvp_049_pe_rel_ratio_mean_504d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """504-day rolling mean of P/E-to-peer ratio (long-run relative valuation)."""
    return _rolling_mean(_rel_ratio(pe, peer_median_pe), _TD_2Y)


def vvp_050_evebit_rel_ratio_mean_252d(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """252-day rolling mean of EV/EBIT-to-peer ratio."""
    return _rolling_mean(_rel_ratio(evebit, peer_median_evebit), _TD_YEAR)


# --- Group G (051-060): Z-score of relative ratio (how extreme is current discount?) ---

def vvp_051_pe_rel_ratio_zscore_252d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Z-score of P/E relative ratio over trailing 252 days (extremity of discount)."""
    r = _rel_ratio(pe, peer_median_pe)
    return _zscore_rolling(r, _TD_YEAR)


def vvp_052_pb_rel_ratio_zscore_252d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Z-score of P/B relative ratio over trailing 252 days."""
    r = _rel_ratio(pb, peer_median_pb)
    return _zscore_rolling(r, _TD_YEAR)


def vvp_053_ps_rel_ratio_zscore_252d(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """Z-score of P/S relative ratio over trailing 252 days."""
    r = _rel_ratio(ps, peer_median_ps)
    return _zscore_rolling(r, _TD_YEAR)


def vvp_054_evebitda_rel_ratio_zscore_252d(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """Z-score of EV/EBITDA relative ratio over trailing 252 days."""
    r = _rel_ratio(evebitda, peer_median_evebitda)
    return _zscore_rolling(r, _TD_YEAR)


def vvp_055_pe_rel_ratio_zscore_504d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Z-score of P/E relative ratio over trailing 504-day window."""
    r = _rel_ratio(pe, peer_median_pe)
    return _zscore_rolling(r, _TD_2Y)


def vvp_056_log_pe_zscore_252d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Z-score of log(P/E / peer) over trailing 252 days."""
    r = _log_rel(pe, peer_median_pe)
    return _zscore_rolling(r, _TD_YEAR)


def vvp_057_log_pb_zscore_252d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Z-score of log(P/B / peer) over trailing 252 days."""
    r = _log_rel(pb, peer_median_pb)
    return _zscore_rolling(r, _TD_YEAR)


def vvp_058_log_ps_zscore_252d(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """Z-score of log(P/S / peer) over trailing 252 days."""
    r = _log_rel(ps, peer_median_ps)
    return _zscore_rolling(r, _TD_YEAR)


def vvp_059_evebit_rel_zscore_252d(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """Z-score of EV/EBIT-to-peer ratio over 252 days."""
    r = _rel_ratio(evebit, peer_median_evebit)
    return _zscore_rolling(r, _TD_YEAR)


def vvp_060_composite_zscore_3metric(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series
) -> pd.Series:
    """Average 252d z-score of PE/PB/PS relative ratios (composite discount extremity)."""
    z_pe = _zscore_rolling(_rel_ratio(pe, peer_median_pe), _TD_YEAR)
    z_pb = _zscore_rolling(_rel_ratio(pb, peer_median_pb), _TD_YEAR)
    z_ps = _zscore_rolling(_rel_ratio(ps, peer_median_ps), _TD_YEAR)
    return (z_pe + z_pb + z_ps) / 3.0


# --- Group H (061-070): Expanding percentile rank of relative ratio ---

def vvp_061_pe_rel_ratio_expanding_pctrank(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Expanding percentile rank of P/E-to-peer ratio (0=cheapest ever vs peers)."""
    r = _rel_ratio(pe, peer_median_pe)
    return r.expanding(min_periods=21).rank(pct=True)


def vvp_062_pb_rel_ratio_expanding_pctrank(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Expanding percentile rank of P/B-to-peer ratio."""
    r = _rel_ratio(pb, peer_median_pb)
    return r.expanding(min_periods=21).rank(pct=True)


def vvp_063_ps_rel_ratio_expanding_pctrank(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """Expanding percentile rank of P/S-to-peer ratio."""
    r = _rel_ratio(ps, peer_median_ps)
    return r.expanding(min_periods=21).rank(pct=True)


def vvp_064_evebitda_rel_ratio_expanding_pctrank(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """Expanding percentile rank of EV/EBITDA-to-peer ratio."""
    r = _rel_ratio(evebitda, peer_median_evebitda)
    return r.expanding(min_periods=21).rank(pct=True)


def vvp_065_pe_rel_ratio_252d_pctrank(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """252-day rolling percentile rank of P/E-to-peer ratio."""
    r = _rel_ratio(pe, peer_median_pe)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vvp_066_pb_rel_ratio_252d_pctrank(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """252-day rolling percentile rank of P/B-to-peer ratio."""
    r = _rel_ratio(pb, peer_median_pb)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vvp_067_ps_rel_ratio_504d_pctrank(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """504-day rolling percentile rank of P/S-to-peer ratio (2-year rank)."""
    r = _rel_ratio(ps, peer_median_ps)
    return r.rolling(_TD_2Y, min_periods=_TD_HALF).rank(pct=True)


def vvp_068_log_pe_252d_pctrank(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """252-day rolling percentile rank of log(P/E / peer)."""
    r = _log_rel(pe, peer_median_pe)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vvp_069_divyield_rel_ratio_252d_pctrank(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """252-day rolling percentile rank of div-yield-to-peer ratio (high = rich yield vs peers)."""
    r = _rel_ratio(divyield, peer_median_divyield)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vvp_070_composite_pctrank_4metric(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series
) -> pd.Series:
    """Mean 252d pct-rank across PE/PB/EV-EBITDA/PS relative ratios (composite cheapness rank)."""
    def _rank252(s):
        return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    r_pe = _rank252(_rel_ratio(pe, peer_median_pe))
    r_pb = _rank252(_rel_ratio(pb, peer_median_pb))
    r_ev = _rank252(_rel_ratio(evebitda, peer_median_evebitda))
    r_ps = _rank252(_rel_ratio(ps, peer_median_ps))
    return (r_pe + r_pb + r_ev + r_ps) / 4.0


# --- Group I (071-075): Relative-discount drawdown and extremes ---

def vvp_071_pe_rel_ratio_ath_drawdown(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Drawdown of P/E relative ratio from its expanding max (how much discount deepened)."""
    r = _rel_ratio(pe, peer_median_pe)
    peak = r.expanding(min_periods=1).max()
    return _safe_div(r - peak, peak.abs())


def vvp_072_pb_rel_ratio_252d_drawdown(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Drawdown of P/B relative ratio from its 252-day max."""
    r = _rel_ratio(pb, peer_median_pb)
    peak = _rolling_max(r, _TD_YEAR)
    return _safe_div(r - peak, peak.abs())


def vvp_073_ps_rel_ratio_ath_min(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """Expanding all-time minimum of P/S relative ratio (absolute cheapest ever vs peers)."""
    r = _rel_ratio(ps, peer_median_ps)
    return r.expanding(min_periods=1).min()


def vvp_074_pe_rel_ratio_distance_from_252d_min(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Distance of current P/E relative ratio above its 252-day min (how far above the floor)."""
    r = _rel_ratio(pe, peer_median_pe)
    floor = _rolling_min(r, _TD_YEAR)
    return r - floor


def vvp_075_multi_metric_extreme_discount_flag(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series
) -> pd.Series:
    """1 if all four multiples (PE/PB/PS/EVEBITDA) simultaneously trade below peer medians."""
    return (
        _discount_flag(pe, peer_median_pe) *
        _discount_flag(pb, peer_median_pb) *
        _discount_flag(ps, peer_median_ps) *
        _discount_flag(evebitda, peer_median_evebitda)
    )


# --- Group R (151-160): EWM relative ratio at alternate spans ---

def vvp_151_pe_rel_ratio_ewm126(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """EWM(126) of P/E relative ratio (half-year smoothed relative valuation)."""
    return _ewm_mean(_rel_ratio(pe, peer_median_pe), _TD_HALF)


def vvp_152_pb_rel_ratio_ewm126(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """EWM(126) of P/B relative ratio (half-year smoothed)."""
    return _ewm_mean(_rel_ratio(pb, peer_median_pb), _TD_HALF)


def vvp_153_ps_rel_ratio_ewm126(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """EWM(126) of P/S relative ratio (half-year smoothed)."""
    return _ewm_mean(_rel_ratio(ps, peer_median_ps), _TD_HALF)


def vvp_154_evebitda_rel_ratio_ewm126(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """EWM(126) of EV/EBITDA relative ratio (half-year smoothed)."""
    return _ewm_mean(_rel_ratio(evebitda, peer_median_evebitda), _TD_HALF)


def vvp_155_log_pe_ewm63(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """EWM(63) of log(P/E/peer) — quarterly smoothed log-relative."""
    return _ewm_mean(_log_rel(pe, peer_median_pe), _TD_QTR)


def vvp_156_log_evebit_ewm21(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """EWM(21) of log(EV/EBIT/peer) (short-run log-relative smoothing)."""
    return _ewm_mean(_log_rel(evebit, peer_median_evebit), _TD_MON)


def vvp_157_marketcap_rel_ratio_ewm63(marketcap: pd.Series, peer_median_marketcap: pd.Series) -> pd.Series:
    """EWM(63) of market-cap relative ratio (smooth quarterly size relative)."""
    return _ewm_mean(_rel_ratio(marketcap, peer_median_marketcap), _TD_QTR)


def vvp_158_ev_rel_ratio_ewm63(ev: pd.Series, peer_median_ev: pd.Series) -> pd.Series:
    """EWM(63) of EV relative ratio (smooth quarterly enterprise-size relative)."""
    return _ewm_mean(_rel_ratio(ev, peer_median_ev), _TD_QTR)


def vvp_159_divyield_rel_ratio_ewm63(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """EWM(63) of div-yield relative ratio (smooth quarterly yield advantage)."""
    return _ewm_mean(_rel_ratio(divyield, peer_median_divyield), _TD_QTR)


def vvp_160_log_divyield_ewm21(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """EWM(21) of log(divyield/peer) — short-run smoothed log yield-relative."""
    return _ewm_mean(_log_rel(divyield, peer_median_divyield), _TD_MON)


# --- Group S (161-166): Median-based rolling central tendency of relative ratios ---

def vvp_161_pe_rel_ratio_rolling_median_63d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """63-day rolling median of P/E relative ratio (robust central tendency)."""
    return _rolling_median(_rel_ratio(pe, peer_median_pe), _TD_QTR)


def vvp_162_pb_rel_ratio_rolling_median_252d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """252-day rolling median of P/B relative ratio."""
    return _rolling_median(_rel_ratio(pb, peer_median_pb), _TD_YEAR)


def vvp_163_ps_rel_ratio_rolling_median_63d(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """63-day rolling median of P/S relative ratio."""
    return _rolling_median(_rel_ratio(ps, peer_median_ps), _TD_QTR)


def vvp_164_evebitda_rel_ratio_rolling_median_252d(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """252-day rolling median of EV/EBITDA relative ratio."""
    return _rolling_median(_rel_ratio(evebitda, peer_median_evebitda), _TD_YEAR)


def vvp_165_evebit_rel_ratio_rolling_median_63d(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """63-day rolling median of EV/EBIT relative ratio."""
    return _rolling_median(_rel_ratio(evebit, peer_median_evebit), _TD_QTR)


def vvp_166_divyield_rel_ratio_rolling_median_252d(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """252-day rolling median of div-yield relative ratio."""
    return _rolling_median(_rel_ratio(divyield, peer_median_divyield), _TD_YEAR)


# --- Group T (167-171): Relative ratio vs rolling median (deviation from robust center) ---

def vvp_167_pe_rel_ratio_vs_median_63d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Current P/E relative ratio minus its 63-day rolling median."""
    r = _rel_ratio(pe, peer_median_pe)
    return r - _rolling_median(r, _TD_QTR)


def vvp_168_pb_rel_ratio_vs_median_252d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Current P/B relative ratio minus its 252-day rolling median."""
    r = _rel_ratio(pb, peer_median_pb)
    return r - _rolling_median(r, _TD_YEAR)


def vvp_169_ps_rel_ratio_vs_median_252d(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """Current P/S relative ratio minus its 252-day rolling median."""
    r = _rel_ratio(ps, peer_median_ps)
    return r - _rolling_median(r, _TD_YEAR)


def vvp_170_evebitda_rel_ratio_vs_median_63d(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """Current EV/EBITDA relative ratio minus its 63-day rolling median."""
    r = _rel_ratio(evebitda, peer_median_evebitda)
    return r - _rolling_median(r, _TD_QTR)


def vvp_171_divyield_rel_ratio_vs_median_63d(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """Current div-yield relative ratio minus its 63-day rolling median."""
    r = _rel_ratio(divyield, peer_median_divyield)
    return r - _rolling_median(r, _TD_QTR)


# --- Group U (172-175): Size-relative and composite cross-multiple features ---

def vvp_172_marketcap_rel_ratio_zscore_252d(marketcap: pd.Series, peer_median_marketcap: pd.Series) -> pd.Series:
    """Z-score of market-cap relative ratio over 252 days (size dislocation vs peers)."""
    return _zscore_rolling(_rel_ratio(marketcap, peer_median_marketcap), _TD_YEAR)


def vvp_173_ev_rel_ratio_zscore_252d(ev: pd.Series, peer_median_ev: pd.Series) -> pd.Series:
    """Z-score of EV relative ratio over 252 days (enterprise-size dislocation vs peers)."""
    return _zscore_rolling(_rel_ratio(ev, peer_median_ev), _TD_YEAR)


def vvp_174_log_pe_vs_median_63d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Current log(P/E/peer) minus its 63-day rolling median (robust log-relative deviation)."""
    r = _log_rel(pe, peer_median_pe)
    return r - _rolling_median(r, _TD_QTR)


def vvp_175_composite_ewm21_log_rel_5metric(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series,
    evebit: pd.Series, peer_median_evebit: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series
) -> pd.Series:
    """EWM(21) of mean log-relative for 5 multiples (PE/PB/PS/EVEBIT/EVEBITDA)."""
    composite = (
        _log_rel(pe, peer_median_pe) +
        _log_rel(pb, peer_median_pb) +
        _log_rel(ps, peer_median_ps) +
        _log_rel(evebit, peer_median_evebit) +
        _log_rel(evebitda, peer_median_evebitda)
    ) / 5.0
    return _ewm_mean(composite, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

VALUATION_VS_PEERS_REGISTRY_001_075 = {
    "vvp_001_pe_ratio_to_peer":                    {"inputs": ["pe", "peer_median_pe"],                                                                               "func": vvp_001_pe_ratio_to_peer},
    "vvp_002_pb_ratio_to_peer":                    {"inputs": ["pb", "peer_median_pb"],                                                                               "func": vvp_002_pb_ratio_to_peer},
    "vvp_003_ps_ratio_to_peer":                    {"inputs": ["ps", "peer_median_ps"],                                                                               "func": vvp_003_ps_ratio_to_peer},
    "vvp_004_evebit_ratio_to_peer":                {"inputs": ["evebit", "peer_median_evebit"],                                                                        "func": vvp_004_evebit_ratio_to_peer},
    "vvp_005_evebitda_ratio_to_peer":              {"inputs": ["evebitda", "peer_median_evebitda"],                                                                    "func": vvp_005_evebitda_ratio_to_peer},
    "vvp_006_marketcap_ratio_to_peer":             {"inputs": ["marketcap", "peer_median_marketcap"],                                                                  "func": vvp_006_marketcap_ratio_to_peer},
    "vvp_007_ev_ratio_to_peer":                    {"inputs": ["ev", "peer_median_ev"],                                                                               "func": vvp_007_ev_ratio_to_peer},
    "vvp_008_divyield_ratio_to_peer":              {"inputs": ["divyield", "peer_median_divyield"],                                                                    "func": vvp_008_divyield_ratio_to_peer},
    "vvp_009_log_pe_vs_peer":                      {"inputs": ["pe", "peer_median_pe"],                                                                               "func": vvp_009_log_pe_vs_peer},
    "vvp_010_log_pb_vs_peer":                      {"inputs": ["pb", "peer_median_pb"],                                                                               "func": vvp_010_log_pb_vs_peer},
    "vvp_011_log_ps_vs_peer":                      {"inputs": ["ps", "peer_median_ps"],                                                                               "func": vvp_011_log_ps_vs_peer},
    "vvp_012_log_evebitda_vs_peer":                {"inputs": ["evebitda", "peer_median_evebitda"],                                                                    "func": vvp_012_log_evebitda_vs_peer},
    "vvp_013_log_evebit_vs_peer":                  {"inputs": ["evebit", "peer_median_evebit"],                                                                        "func": vvp_013_log_evebit_vs_peer},
    "vvp_014_log_divyield_vs_peer":                {"inputs": ["divyield", "peer_median_divyield"],                                                                    "func": vvp_014_log_divyield_vs_peer},
    "vvp_015_pe_gap_vs_peer":                      {"inputs": ["pe", "peer_median_pe"],                                                                               "func": vvp_015_pe_gap_vs_peer},
    "vvp_016_pb_gap_vs_peer":                      {"inputs": ["pb", "peer_median_pb"],                                                                               "func": vvp_016_pb_gap_vs_peer},
    "vvp_017_ps_gap_vs_peer":                      {"inputs": ["ps", "peer_median_ps"],                                                                               "func": vvp_017_ps_gap_vs_peer},
    "vvp_018_evebitda_gap_vs_peer":                {"inputs": ["evebitda", "peer_median_evebitda"],                                                                    "func": vvp_018_evebitda_gap_vs_peer},
    "vvp_019_evebit_gap_vs_peer":                  {"inputs": ["evebit", "peer_median_evebit"],                                                                        "func": vvp_019_evebit_gap_vs_peer},
    "vvp_020_divyield_gap_vs_peer":                {"inputs": ["divyield", "peer_median_divyield"],                                                                    "func": vvp_020_divyield_gap_vs_peer},
    "vvp_021_pe_discount_flag":                    {"inputs": ["pe", "peer_median_pe"],                                                                               "func": vvp_021_pe_discount_flag},
    "vvp_022_pb_discount_flag":                    {"inputs": ["pb", "peer_median_pb"],                                                                               "func": vvp_022_pb_discount_flag},
    "vvp_023_ps_discount_flag":                    {"inputs": ["ps", "peer_median_ps"],                                                                               "func": vvp_023_ps_discount_flag},
    "vvp_024_evebitda_discount_flag":              {"inputs": ["evebitda", "peer_median_evebitda"],                                                                    "func": vvp_024_evebitda_discount_flag},
    "vvp_025_evebit_discount_flag":                {"inputs": ["evebit", "peer_median_evebit"],                                                                        "func": vvp_025_evebit_discount_flag},
    "vvp_026_multi_metric_discount_score":         {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps"],                               "func": vvp_026_multi_metric_discount_score},
    "vvp_027_ev_discount_flag":                    {"inputs": ["ev", "peer_median_ev"],                                                                               "func": vvp_027_ev_discount_flag},
    "vvp_028_pe_discount_depth":                   {"inputs": ["pe", "peer_median_pe"],                                                                               "func": vvp_028_pe_discount_depth},
    "vvp_029_pb_discount_depth":                   {"inputs": ["pb", "peer_median_pb"],                                                                               "func": vvp_029_pb_discount_depth},
    "vvp_030_ps_discount_depth":                   {"inputs": ["ps", "peer_median_ps"],                                                                               "func": vvp_030_ps_discount_depth},
    "vvp_031_pe_frac_below_peer_63d":              {"inputs": ["pe", "peer_median_pe"],                                                                               "func": vvp_031_pe_frac_below_peer_63d},
    "vvp_032_pe_frac_below_peer_252d":             {"inputs": ["pe", "peer_median_pe"],                                                                               "func": vvp_032_pe_frac_below_peer_252d},
    "vvp_033_pb_frac_below_peer_63d":              {"inputs": ["pb", "peer_median_pb"],                                                                               "func": vvp_033_pb_frac_below_peer_63d},
    "vvp_034_pb_frac_below_peer_252d":             {"inputs": ["pb", "peer_median_pb"],                                                                               "func": vvp_034_pb_frac_below_peer_252d},
    "vvp_035_ps_frac_below_peer_252d":             {"inputs": ["ps", "peer_median_ps"],                                                                               "func": vvp_035_ps_frac_below_peer_252d},
    "vvp_036_evebitda_frac_below_peer_252d":       {"inputs": ["evebitda", "peer_median_evebitda"],                                                                    "func": vvp_036_evebitda_frac_below_peer_252d},
    "vvp_037_all_multiples_discount_frac_252d":    {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps"],                               "func": vvp_037_all_multiples_discount_frac_252d},
    "vvp_038_pe_frac_below_peer_504d":             {"inputs": ["pe", "peer_median_pe"],                                                                               "func": vvp_038_pe_frac_below_peer_504d},
    "vvp_039_pb_frac_below_peer_504d":             {"inputs": ["pb", "peer_median_pb"],                                                                               "func": vvp_039_pb_frac_below_peer_504d},
    "vvp_040_divyield_frac_above_peer_252d":       {"inputs": ["divyield", "peer_median_divyield"],                                                                    "func": vvp_040_divyield_frac_above_peer_252d},
    "vvp_041_pe_rel_ratio_mean_63d":               {"inputs": ["pe", "peer_median_pe"],                                                                               "func": vvp_041_pe_rel_ratio_mean_63d},
    "vvp_042_pe_rel_ratio_mean_252d":              {"inputs": ["pe", "peer_median_pe"],                                                                               "func": vvp_042_pe_rel_ratio_mean_252d},
    "vvp_043_pb_rel_ratio_mean_252d":              {"inputs": ["pb", "peer_median_pb"],                                                                               "func": vvp_043_pb_rel_ratio_mean_252d},
    "vvp_044_ps_rel_ratio_mean_252d":              {"inputs": ["ps", "peer_median_ps"],                                                                               "func": vvp_044_ps_rel_ratio_mean_252d},
    "vvp_045_evebitda_rel_ratio_mean_252d":        {"inputs": ["evebitda", "peer_median_evebitda"],                                                                    "func": vvp_045_evebitda_rel_ratio_mean_252d},
    "vvp_046_log_pe_vs_peer_mean_63d":             {"inputs": ["pe", "peer_median_pe"],                                                                               "func": vvp_046_log_pe_vs_peer_mean_63d},
    "vvp_047_log_pb_vs_peer_mean_252d":            {"inputs": ["pb", "peer_median_pb"],                                                                               "func": vvp_047_log_pb_vs_peer_mean_252d},
    "vvp_048_log_ps_vs_peer_mean_252d":            {"inputs": ["ps", "peer_median_ps"],                                                                               "func": vvp_048_log_ps_vs_peer_mean_252d},
    "vvp_049_pe_rel_ratio_mean_504d":              {"inputs": ["pe", "peer_median_pe"],                                                                               "func": vvp_049_pe_rel_ratio_mean_504d},
    "vvp_050_evebit_rel_ratio_mean_252d":          {"inputs": ["evebit", "peer_median_evebit"],                                                                        "func": vvp_050_evebit_rel_ratio_mean_252d},
    "vvp_051_pe_rel_ratio_zscore_252d":            {"inputs": ["pe", "peer_median_pe"],                                                                               "func": vvp_051_pe_rel_ratio_zscore_252d},
    "vvp_052_pb_rel_ratio_zscore_252d":            {"inputs": ["pb", "peer_median_pb"],                                                                               "func": vvp_052_pb_rel_ratio_zscore_252d},
    "vvp_053_ps_rel_ratio_zscore_252d":            {"inputs": ["ps", "peer_median_ps"],                                                                               "func": vvp_053_ps_rel_ratio_zscore_252d},
    "vvp_054_evebitda_rel_ratio_zscore_252d":      {"inputs": ["evebitda", "peer_median_evebitda"],                                                                    "func": vvp_054_evebitda_rel_ratio_zscore_252d},
    "vvp_055_pe_rel_ratio_zscore_504d":            {"inputs": ["pe", "peer_median_pe"],                                                                               "func": vvp_055_pe_rel_ratio_zscore_504d},
    "vvp_056_log_pe_zscore_252d":                  {"inputs": ["pe", "peer_median_pe"],                                                                               "func": vvp_056_log_pe_zscore_252d},
    "vvp_057_log_pb_zscore_252d":                  {"inputs": ["pb", "peer_median_pb"],                                                                               "func": vvp_057_log_pb_zscore_252d},
    "vvp_058_log_ps_zscore_252d":                  {"inputs": ["ps", "peer_median_ps"],                                                                               "func": vvp_058_log_ps_zscore_252d},
    "vvp_059_evebit_rel_zscore_252d":              {"inputs": ["evebit", "peer_median_evebit"],                                                                        "func": vvp_059_evebit_rel_zscore_252d},
    "vvp_060_composite_zscore_3metric":            {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps"],                               "func": vvp_060_composite_zscore_3metric},
    "vvp_061_pe_rel_ratio_expanding_pctrank":      {"inputs": ["pe", "peer_median_pe"],                                                                               "func": vvp_061_pe_rel_ratio_expanding_pctrank},
    "vvp_062_pb_rel_ratio_expanding_pctrank":      {"inputs": ["pb", "peer_median_pb"],                                                                               "func": vvp_062_pb_rel_ratio_expanding_pctrank},
    "vvp_063_ps_rel_ratio_expanding_pctrank":      {"inputs": ["ps", "peer_median_ps"],                                                                               "func": vvp_063_ps_rel_ratio_expanding_pctrank},
    "vvp_064_evebitda_rel_ratio_expanding_pctrank":{"inputs": ["evebitda", "peer_median_evebitda"],                                                                    "func": vvp_064_evebitda_rel_ratio_expanding_pctrank},
    "vvp_065_pe_rel_ratio_252d_pctrank":           {"inputs": ["pe", "peer_median_pe"],                                                                               "func": vvp_065_pe_rel_ratio_252d_pctrank},
    "vvp_066_pb_rel_ratio_252d_pctrank":           {"inputs": ["pb", "peer_median_pb"],                                                                               "func": vvp_066_pb_rel_ratio_252d_pctrank},
    "vvp_067_ps_rel_ratio_504d_pctrank":           {"inputs": ["ps", "peer_median_ps"],                                                                               "func": vvp_067_ps_rel_ratio_504d_pctrank},
    "vvp_068_log_pe_252d_pctrank":                 {"inputs": ["pe", "peer_median_pe"],                                                                               "func": vvp_068_log_pe_252d_pctrank},
    "vvp_069_divyield_rel_ratio_252d_pctrank":     {"inputs": ["divyield", "peer_median_divyield"],                                                                    "func": vvp_069_divyield_rel_ratio_252d_pctrank},
    "vvp_070_composite_pctrank_4metric":           {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "evebitda", "peer_median_evebitda", "ps", "peer_median_ps"], "func": vvp_070_composite_pctrank_4metric},
    "vvp_071_pe_rel_ratio_ath_drawdown":           {"inputs": ["pe", "peer_median_pe"],                                                                               "func": vvp_071_pe_rel_ratio_ath_drawdown},
    "vvp_072_pb_rel_ratio_252d_drawdown":          {"inputs": ["pb", "peer_median_pb"],                                                                               "func": vvp_072_pb_rel_ratio_252d_drawdown},
    "vvp_073_ps_rel_ratio_ath_min":                {"inputs": ["ps", "peer_median_ps"],                                                                               "func": vvp_073_ps_rel_ratio_ath_min},
    "vvp_074_pe_rel_ratio_distance_from_252d_min": {"inputs": ["pe", "peer_median_pe"],                                                                               "func": vvp_074_pe_rel_ratio_distance_from_252d_min},
    "vvp_075_multi_metric_extreme_discount_flag":  {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps", "evebitda", "peer_median_evebitda"], "func": vvp_075_multi_metric_extreme_discount_flag},
    "vvp_151_pe_rel_ratio_ewm126":                 {"inputs": ["pe", "peer_median_pe"],                                                                                                                                                   "func": vvp_151_pe_rel_ratio_ewm126},
    "vvp_152_pb_rel_ratio_ewm126":                 {"inputs": ["pb", "peer_median_pb"],                                                                                                                                                   "func": vvp_152_pb_rel_ratio_ewm126},
    "vvp_153_ps_rel_ratio_ewm126":                 {"inputs": ["ps", "peer_median_ps"],                                                                                                                                                   "func": vvp_153_ps_rel_ratio_ewm126},
    "vvp_154_evebitda_rel_ratio_ewm126":           {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                                                                       "func": vvp_154_evebitda_rel_ratio_ewm126},
    "vvp_155_log_pe_ewm63":                        {"inputs": ["pe", "peer_median_pe"],                                                                                                                                                   "func": vvp_155_log_pe_ewm63},
    "vvp_156_log_evebit_ewm21":                    {"inputs": ["evebit", "peer_median_evebit"],                                                                                                                                           "func": vvp_156_log_evebit_ewm21},
    "vvp_157_marketcap_rel_ratio_ewm63":           {"inputs": ["marketcap", "peer_median_marketcap"],                                                                                                                                     "func": vvp_157_marketcap_rel_ratio_ewm63},
    "vvp_158_ev_rel_ratio_ewm63":                  {"inputs": ["ev", "peer_median_ev"],                                                                                                                                                   "func": vvp_158_ev_rel_ratio_ewm63},
    "vvp_159_divyield_rel_ratio_ewm63":            {"inputs": ["divyield", "peer_median_divyield"],                                                                                                                                       "func": vvp_159_divyield_rel_ratio_ewm63},
    "vvp_160_log_divyield_ewm21":                  {"inputs": ["divyield", "peer_median_divyield"],                                                                                                                                       "func": vvp_160_log_divyield_ewm21},
    "vvp_161_pe_rel_ratio_rolling_median_63d":     {"inputs": ["pe", "peer_median_pe"],                                                                                                                                                   "func": vvp_161_pe_rel_ratio_rolling_median_63d},
    "vvp_162_pb_rel_ratio_rolling_median_252d":    {"inputs": ["pb", "peer_median_pb"],                                                                                                                                                   "func": vvp_162_pb_rel_ratio_rolling_median_252d},
    "vvp_163_ps_rel_ratio_rolling_median_63d":     {"inputs": ["ps", "peer_median_ps"],                                                                                                                                                   "func": vvp_163_ps_rel_ratio_rolling_median_63d},
    "vvp_164_evebitda_rel_ratio_rolling_median_252d": {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                                                                    "func": vvp_164_evebitda_rel_ratio_rolling_median_252d},
    "vvp_165_evebit_rel_ratio_rolling_median_63d": {"inputs": ["evebit", "peer_median_evebit"],                                                                                                                                           "func": vvp_165_evebit_rel_ratio_rolling_median_63d},
    "vvp_166_divyield_rel_ratio_rolling_median_252d": {"inputs": ["divyield", "peer_median_divyield"],                                                                                                                                    "func": vvp_166_divyield_rel_ratio_rolling_median_252d},
    "vvp_167_pe_rel_ratio_vs_median_63d":          {"inputs": ["pe", "peer_median_pe"],                                                                                                                                                   "func": vvp_167_pe_rel_ratio_vs_median_63d},
    "vvp_168_pb_rel_ratio_vs_median_252d":         {"inputs": ["pb", "peer_median_pb"],                                                                                                                                                   "func": vvp_168_pb_rel_ratio_vs_median_252d},
    "vvp_169_ps_rel_ratio_vs_median_252d":         {"inputs": ["ps", "peer_median_ps"],                                                                                                                                                   "func": vvp_169_ps_rel_ratio_vs_median_252d},
    "vvp_170_evebitda_rel_ratio_vs_median_63d":    {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                                                                       "func": vvp_170_evebitda_rel_ratio_vs_median_63d},
    "vvp_171_divyield_rel_ratio_vs_median_63d":    {"inputs": ["divyield", "peer_median_divyield"],                                                                                                                                       "func": vvp_171_divyield_rel_ratio_vs_median_63d},
    "vvp_172_marketcap_rel_ratio_zscore_252d":     {"inputs": ["marketcap", "peer_median_marketcap"],                                                                                                                                     "func": vvp_172_marketcap_rel_ratio_zscore_252d},
    "vvp_173_ev_rel_ratio_zscore_252d":            {"inputs": ["ev", "peer_median_ev"],                                                                                                                                                   "func": vvp_173_ev_rel_ratio_zscore_252d},
    "vvp_174_log_pe_vs_median_63d":                {"inputs": ["pe", "peer_median_pe"],                                                                                                                                                   "func": vvp_174_log_pe_vs_median_63d},
    "vvp_175_composite_ewm21_log_rel_5metric":     {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps", "evebit", "peer_median_evebit", "evebitda", "peer_median_evebitda"],                             "func": vvp_175_composite_ewm21_log_rel_5metric},
}
