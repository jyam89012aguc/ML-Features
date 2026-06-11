"""
82_valuation_vs_peers — Extended Features 001-075
Domain: cross-sectional valuation vs sector/industry peer medians — additional
        angles not in the base files: relative-ratio drawdowns and draw-ups,
        robust z-scores, slope/trend of the relative ratio, discount streaks,
        skew/kurtosis of the relative ratio, gap-to-MAD scores, cross-multiple
        dispersion and composite peer-discount capitulation scores.
Asset class: US equities | Daily valuation metrics (SF1-derived, daily frequency)
Target context: capitulation — absolute multi-year low / maximum distress
All feature functions are strictly backward-looking. No forward information.

PEER-MEDIAN INPUT CONTRACT:
    Each function receives the ticker's own daily metric Series and a precomputed
    sector/industry peer-median Series of the same daily index named
    peer_median_<metric>  (e.g. peer_median_pe, peer_median_pb, peer_median_ps,
    peer_median_ev, peer_median_marketcap, peer_median_evebit,
    peer_median_evebitda, peer_median_divyield).  The pipeline computes these
    universe-wide sector/industry medians and passes them in.  These inputs are
    already daily-aligned to the ticker's own metric index — no forward-fill is
    performed here; functions consume them on the shared daily index directly.

Inputs available (16 total):
    Own metrics:         pe, pb, ps, ev, marketcap, evebit, evebitda, divyield
    Peer-median series:  peer_median_pe, peer_median_pb, peer_median_ps,
                         peer_median_ev, peer_median_marketcap, peer_median_evebit,
                         peer_median_evebitda, peer_median_divyield
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_2Y = 504
_TD_3Y = 756
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


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


def _robust_z(s: pd.Series, w: int) -> pd.Series:
    """Median/MAD robust z-score over trailing window w."""
    med = _rolling_median(s, w)
    mad = (s - med).abs().rolling(w, min_periods=max(1, w // 2)).median()
    return _safe_div(s - med, mad * 1.4826)


def _slope(s: pd.Series, w: int) -> pd.Series:
    """Least-squares slope of s over trailing window w (per-day change)."""
    x = np.arange(w, dtype=float)
    x = x - x.mean()
    denom = float((x * x).sum())

    def _fit(arr):
        y = np.asarray(arr, dtype=float)
        if np.isnan(y).any():
            return np.nan
        return float((x * (y - y.mean())).sum() / denom)

    return s.rolling(w, min_periods=w).apply(_fit, raw=True)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def _rolling_skew(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(3, w // 2)).skew()


def _rolling_kurt(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(4, w // 2)).kurt()


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Relative-ratio drawdowns and draw-ups ---


def vvp_ext_001_pe_rel_drawup_from_252d_min(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Rise of P/E-to-peer ratio above its trailing 252-day minimum."""
    r = _rel_ratio(pe, peer_median_pe)
    return _safe_div(r - _rolling_min(r, _TD_YEAR), _rolling_min(r, _TD_YEAR).abs())


def vvp_ext_002_pb_rel_drawup_from_252d_min(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Rise of P/B-to-peer ratio above its trailing 252-day minimum."""
    r = _rel_ratio(pb, peer_median_pb)
    return _safe_div(r - _rolling_min(r, _TD_YEAR), _rolling_min(r, _TD_YEAR).abs())


def vvp_ext_003_ps_rel_drawup_from_504d_min(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """Rise of P/S-to-peer ratio above its trailing 504-day minimum."""
    r = _rel_ratio(ps, peer_median_ps)
    return _safe_div(r - _rolling_min(r, _TD_2Y), _rolling_min(r, _TD_2Y).abs())


def vvp_ext_004_evebitda_rel_drawup_from_252d_min(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """Rise of EV/EBITDA-to-peer ratio above its trailing 252-day minimum."""
    r = _rel_ratio(evebitda, peer_median_evebitda)
    return _safe_div(r - _rolling_min(r, _TD_YEAR), _rolling_min(r, _TD_YEAR).abs())


def vvp_ext_005_pe_rel_drawdown_from_252d_max(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Fall of P/E-to-peer ratio below its trailing 252-day maximum (<=0)."""
    r = _rel_ratio(pe, peer_median_pe)
    return _safe_div(r - _rolling_max(r, _TD_YEAR), _rolling_max(r, _TD_YEAR).abs())


def vvp_ext_006_pb_rel_drawdown_from_504d_max(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Fall of P/B-to-peer ratio below its trailing 504-day maximum (<=0)."""
    r = _rel_ratio(pb, peer_median_pb)
    return _safe_div(r - _rolling_max(r, _TD_2Y), _rolling_max(r, _TD_2Y).abs())


def vvp_ext_007_ps_rel_drawdown_from_252d_max(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """Fall of P/S-to-peer ratio below its trailing 252-day maximum (<=0)."""
    r = _rel_ratio(ps, peer_median_ps)
    return _safe_div(r - _rolling_max(r, _TD_YEAR), _rolling_max(r, _TD_YEAR).abs())


def vvp_ext_008_evebit_rel_drawdown_from_252d_max(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """Fall of EV/EBIT-to-peer ratio below its trailing 252-day maximum (<=0)."""
    r = _rel_ratio(evebit, peer_median_evebit)
    return _safe_div(r - _rolling_max(r, _TD_YEAR), _rolling_max(r, _TD_YEAR).abs())


def vvp_ext_009_evebitda_rel_drawdown_from_756d_max(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """Fall of EV/EBITDA-to-peer ratio below its trailing 756-day maximum (<=0)."""
    r = _rel_ratio(evebitda, peer_median_evebitda)
    return _safe_div(r - _rolling_max(r, _TD_3Y), _rolling_max(r, _TD_3Y).abs())


def vvp_ext_010_pe_rel_drawdown_from_expanding_max(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Fall of P/E-to-peer ratio below its all-history expanding maximum (<=0)."""
    r = _rel_ratio(pe, peer_median_pe)
    peak = r.expanding(min_periods=21).max()
    return _safe_div(r - peak, peak.abs())


# --- Group B (011-020): Relative-ratio multiple-of-trailing-min ---


def vvp_ext_011_pe_rel_over_252d_min(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """P/E-to-peer ratio as a multiple of its trailing 252-day minimum."""
    r = _rel_ratio(pe, peer_median_pe)
    return _safe_div(r, _rolling_min(r, _TD_YEAR))


def vvp_ext_012_pb_rel_over_252d_min(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """P/B-to-peer ratio as a multiple of its trailing 252-day minimum."""
    r = _rel_ratio(pb, peer_median_pb)
    return _safe_div(r, _rolling_min(r, _TD_YEAR))


def vvp_ext_013_ps_rel_over_252d_min(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """P/S-to-peer ratio as a multiple of its trailing 252-day minimum."""
    r = _rel_ratio(ps, peer_median_ps)
    return _safe_div(r, _rolling_min(r, _TD_YEAR))


def vvp_ext_014_evebitda_rel_over_504d_min(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA-to-peer ratio as a multiple of its trailing 504-day minimum."""
    r = _rel_ratio(evebitda, peer_median_evebitda)
    return _safe_div(r, _rolling_min(r, _TD_2Y))


def vvp_ext_015_pe_rel_over_252d_max(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """P/E-to-peer ratio as a fraction of its trailing 252-day maximum (0..1)."""
    r = _rel_ratio(pe, peer_median_pe)
    return _safe_div(r, _rolling_max(r, _TD_YEAR))


def vvp_ext_016_pb_rel_over_252d_max(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """P/B-to-peer ratio as a fraction of its trailing 252-day maximum (0..1)."""
    r = _rel_ratio(pb, peer_median_pb)
    return _safe_div(r, _rolling_max(r, _TD_YEAR))


def vvp_ext_017_evebit_rel_over_252d_min(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """EV/EBIT-to-peer ratio as a multiple of its trailing 252-day minimum."""
    r = _rel_ratio(evebit, peer_median_evebit)
    return _safe_div(r, _rolling_min(r, _TD_YEAR))


def vvp_ext_018_marketcap_rel_over_252d_min(marketcap: pd.Series, peer_median_marketcap: pd.Series) -> pd.Series:
    """Market-cap-to-peer ratio as a multiple of its trailing 252-day minimum."""
    r = _rel_ratio(marketcap, peer_median_marketcap)
    return _safe_div(r, _rolling_min(r, _TD_YEAR))


def vvp_ext_019_pe_rel_range_position_252d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """P/E-to-peer ratio position within its trailing 252-day min-max range."""
    r = _rel_ratio(pe, peer_median_pe)
    lo = _rolling_min(r, _TD_YEAR)
    hi = _rolling_max(r, _TD_YEAR)
    return _safe_div(r - lo, hi - lo)


def vvp_ext_020_pb_rel_range_position_504d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """P/B-to-peer ratio position within its trailing 504-day min-max range."""
    r = _rel_ratio(pb, peer_median_pb)
    lo = _rolling_min(r, _TD_2Y)
    hi = _rolling_max(r, _TD_2Y)
    return _safe_div(r - lo, hi - lo)


# --- Group C (021-030): Robust median/MAD z-scores of the relative ratio ---


def vvp_ext_021_pe_rel_robust_z_252d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Median/MAD robust z-score of P/E-to-peer ratio over 252 days."""
    return _robust_z(_rel_ratio(pe, peer_median_pe), _TD_YEAR)


def vvp_ext_022_pb_rel_robust_z_252d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Median/MAD robust z-score of P/B-to-peer ratio over 252 days."""
    return _robust_z(_rel_ratio(pb, peer_median_pb), _TD_YEAR)


def vvp_ext_023_ps_rel_robust_z_252d(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """Median/MAD robust z-score of P/S-to-peer ratio over 252 days."""
    return _robust_z(_rel_ratio(ps, peer_median_ps), _TD_YEAR)


def vvp_ext_024_evebitda_rel_robust_z_252d(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """Median/MAD robust z-score of EV/EBITDA-to-peer ratio over 252 days."""
    return _robust_z(_rel_ratio(evebitda, peer_median_evebitda), _TD_YEAR)


def vvp_ext_025_evebit_rel_robust_z_252d(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """Median/MAD robust z-score of EV/EBIT-to-peer ratio over 252 days."""
    return _robust_z(_rel_ratio(evebit, peer_median_evebit), _TD_YEAR)


def vvp_ext_026_pe_rel_robust_z_504d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Median/MAD robust z-score of P/E-to-peer ratio over 504 days."""
    return _robust_z(_rel_ratio(pe, peer_median_pe), _TD_2Y)


def vvp_ext_027_log_pe_rel_robust_z_252d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Median/MAD robust z-score of log(P/E / peer) over 252 days."""
    return _robust_z(_log_rel(pe, peer_median_pe), _TD_YEAR)


def vvp_ext_028_log_pb_rel_robust_z_252d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Median/MAD robust z-score of log(P/B / peer) over 252 days."""
    return _robust_z(_log_rel(pb, peer_median_pb), _TD_YEAR)


def vvp_ext_029_divyield_rel_robust_z_252d(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """Median/MAD robust z-score of div-yield-to-peer ratio over 252 days."""
    return _robust_z(_rel_ratio(divyield, peer_median_divyield), _TD_YEAR)


def vvp_ext_030_marketcap_rel_robust_z_252d(marketcap: pd.Series, peer_median_marketcap: pd.Series) -> pd.Series:
    """Median/MAD robust z-score of market-cap-to-peer ratio over 252 days."""
    return _robust_z(_rel_ratio(marketcap, peer_median_marketcap), _TD_YEAR)


# --- Group D (031-040): Slope / trend of the relative ratio ---


def vvp_ext_031_pe_rel_slope_63d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Least-squares slope of P/E-to-peer ratio over trailing 63 days."""
    return _slope(_rel_ratio(pe, peer_median_pe), _TD_QTR)


def vvp_ext_032_pe_rel_slope_252d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Least-squares slope of P/E-to-peer ratio over trailing 252 days."""
    return _slope(_rel_ratio(pe, peer_median_pe), _TD_YEAR)


def vvp_ext_033_pb_rel_slope_63d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Least-squares slope of P/B-to-peer ratio over trailing 63 days."""
    return _slope(_rel_ratio(pb, peer_median_pb), _TD_QTR)


def vvp_ext_034_ps_rel_slope_126d(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """Least-squares slope of P/S-to-peer ratio over trailing 126 days."""
    return _slope(_rel_ratio(ps, peer_median_ps), _TD_HALF)


def vvp_ext_035_evebitda_rel_slope_63d(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """Least-squares slope of EV/EBITDA-to-peer ratio over trailing 63 days."""
    return _slope(_rel_ratio(evebitda, peer_median_evebitda), _TD_QTR)


def vvp_ext_036_log_pe_rel_slope_126d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Least-squares slope of log(P/E / peer) over trailing 126 days."""
    return _slope(_log_rel(pe, peer_median_pe), _TD_HALF)


def vvp_ext_037_pe_gap_slope_63d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Least-squares slope of the additive P/E gap (own minus peer) over trailing 63 days."""
    return _slope(_gap(pe, peer_median_pe), _TD_QTR)


def vvp_ext_038_pb_gap_slope_126d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Least-squares slope of the additive P/B gap over trailing 126 days."""
    return _slope(_gap(pb, peer_median_pb), _TD_HALF)


def vvp_ext_039_divyield_rel_slope_126d(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """Least-squares slope of div-yield-to-peer ratio over trailing 126 days."""
    return _slope(_rel_ratio(divyield, peer_median_divyield), _TD_HALF)


def vvp_ext_040_pe_rel_slope_normalized_63d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """63-day slope of P/E relative ratio normalized by its 63-day mean (per-day percent drift)."""
    r = _rel_ratio(pe, peer_median_pe)
    return _safe_div(_slope(r, _TD_QTR), _rolling_mean(r, _TD_QTR))


# --- Group E (041-052): Discount streaks and time-since-extreme ---


def vvp_ext_041_pe_consec_days_discount(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Consecutive days P/E has traded below peer median."""
    return _consec_streak(pe < peer_median_pe)


def vvp_ext_042_pb_consec_days_discount(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Consecutive days P/B has traded below peer median."""
    return _consec_streak(pb < peer_median_pb)


def vvp_ext_043_ps_consec_days_discount(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """Consecutive days P/S has traded below peer median."""
    return _consec_streak(ps < peer_median_ps)


def vvp_ext_044_evebitda_consec_days_discount(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """Consecutive days EV/EBITDA has traded below peer median."""
    return _consec_streak(evebitda < peer_median_evebitda)


def vvp_ext_045_pe_consec_days_deep_discount(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Consecutive days P/E has been below 70% of peer median (deep discount streak)."""
    return _consec_streak(pe < 0.70 * peer_median_pe)


def vvp_ext_046_pb_consec_days_deep_discount(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Consecutive days P/B has been below 70% of peer median (deep discount streak)."""
    return _consec_streak(pb < 0.70 * peer_median_pb)


def vvp_ext_047_pe_max_discount_streak_252d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Longest below-peer P/E streak observed within the trailing 252 days."""
    return _rolling_max(_consec_streak(pe < peer_median_pe), _TD_YEAR)


def vvp_ext_048_divyield_consec_days_yield_premium(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """Consecutive days dividend yield has exceeded peer median (yield-premium streak)."""
    return _consec_streak(divyield > peer_median_divyield)


def vvp_ext_049_pe_days_since_last_premium(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Trading days since P/E last traded above peer median (length of current discount run)."""
    premium = (pe > peer_median_pe).astype(float)
    idx = pd.Series(np.arange(len(premium), dtype=float), index=premium.index)
    last = idx.where(premium == 1.0).ffill()
    out = (idx - last).where(~pe.isna(), np.nan)
    return out


def vvp_ext_050_pe_rel_consec_days_below_252d_median(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Consecutive days the P/E relative ratio has been below its own trailing 252-day median."""
    r = _rel_ratio(pe, peer_median_pe)
    return _consec_streak(r < _rolling_median(r, _TD_YEAR))


def vvp_ext_051_pb_rel_consec_days_below_252d_median(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Consecutive days the P/B relative ratio has been below its own trailing 252-day median."""
    r = _rel_ratio(pb, peer_median_pb)
    return _consec_streak(r < _rolling_median(r, _TD_YEAR))


def vvp_ext_052_ps_rel_consec_days_at_252d_low(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """Consecutive days the P/S relative ratio has sat at its trailing 252-day minimum."""
    r = _rel_ratio(ps, peer_median_ps)
    return _consec_streak(r <= _rolling_min(r, _TD_YEAR))


# --- Group F (053-062): Skew / kurtosis / dispersion of the relative ratio ---


def vvp_ext_053_pe_rel_rolling_skew_252d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Rolling 252-day skewness of the P/E relative ratio."""
    return _rolling_skew(_rel_ratio(pe, peer_median_pe), _TD_YEAR)


def vvp_ext_054_pe_rel_rolling_kurt_252d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Rolling 252-day excess kurtosis of the P/E relative ratio."""
    return _rolling_kurt(_rel_ratio(pe, peer_median_pe), _TD_YEAR)


def vvp_ext_055_pb_rel_rolling_skew_252d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Rolling 252-day skewness of the P/B relative ratio."""
    return _rolling_skew(_rel_ratio(pb, peer_median_pb), _TD_YEAR)


def vvp_ext_056_ps_rel_rolling_skew_126d(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """Rolling 126-day skewness of the P/S relative ratio."""
    return _rolling_skew(_rel_ratio(ps, peer_median_ps), _TD_HALF)


def vvp_ext_057_evebitda_rel_rolling_skew_252d(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """Rolling 252-day skewness of the EV/EBITDA relative ratio."""
    return _rolling_skew(_rel_ratio(evebitda, peer_median_evebitda), _TD_YEAR)


def vvp_ext_058_pe_rel_coef_of_variation_252d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Coefficient of variation of the P/E relative ratio over trailing 252 days."""
    r = _rel_ratio(pe, peer_median_pe)
    return _safe_div(_rolling_std(r, _TD_YEAR), _rolling_mean(r, _TD_YEAR))


def vvp_ext_059_pb_rel_coef_of_variation_252d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Coefficient of variation of the P/B relative ratio over trailing 252 days."""
    r = _rel_ratio(pb, peer_median_pb)
    return _safe_div(_rolling_std(r, _TD_YEAR), _rolling_mean(r, _TD_YEAR))


def vvp_ext_060_pe_rel_iqr_width_252d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Trailing 252-day inter-quartile width of the P/E relative ratio, scaled by its median."""
    r = _rel_ratio(pe, peer_median_pe)
    q75 = r.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).quantile(0.75)
    q25 = r.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).quantile(0.25)
    return _safe_div(q75 - q25, _rolling_median(r, _TD_YEAR))


def vvp_ext_061_evebitda_rel_rolling_kurt_252d(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """Rolling 252-day excess kurtosis of the EV/EBITDA relative ratio."""
    return _rolling_kurt(_rel_ratio(evebitda, peer_median_evebitda), _TD_YEAR)


def vvp_ext_062_divyield_rel_rolling_skew_252d(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """Rolling 252-day skewness of the div-yield relative ratio."""
    return _rolling_skew(_rel_ratio(divyield, peer_median_divyield), _TD_YEAR)


# --- Group G (063-068): Gap normalized by trailing dispersion ---


def vvp_ext_063_pe_gap_over_252d_mad(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Current P/E gap (own-peer) divided by its trailing 252-day median absolute deviation."""
    g = _gap(pe, peer_median_pe)
    med = _rolling_median(g, _TD_YEAR)
    mad = (g - med).abs().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).median()
    return _safe_div(g, mad * 1.4826)


def vvp_ext_064_pb_gap_over_252d_mad(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Current P/B gap divided by its trailing 252-day median absolute deviation."""
    g = _gap(pb, peer_median_pb)
    med = _rolling_median(g, _TD_YEAR)
    mad = (g - med).abs().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).median()
    return _safe_div(g, mad * 1.4826)


def vvp_ext_065_ps_gap_over_252d_std(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """Current P/S gap divided by its trailing 252-day standard deviation."""
    g = _gap(ps, peer_median_ps)
    return _safe_div(g, _rolling_std(g, _TD_YEAR))


def vvp_ext_066_evebitda_gap_over_252d_std(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """Current EV/EBITDA gap divided by its trailing 252-day standard deviation."""
    g = _gap(evebitda, peer_median_evebitda)
    return _safe_div(g, _rolling_std(g, _TD_YEAR))


def vvp_ext_067_pe_gap_minus_252d_min(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Current P/E gap minus its trailing 252-day minimum gap (distance above the gap floor)."""
    g = _gap(pe, peer_median_pe)
    return g - _rolling_min(g, _TD_YEAR)


def vvp_ext_068_pb_gap_ewm126(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """EWM(126)-smoothed additive P/B gap (own minus peer median)."""
    return _ewm_mean(_gap(pb, peer_median_pb), _TD_HALF)


# --- Group H (069-075): Cross-multiple peer-discount composites ---


def vvp_ext_069_count_metrics_below_70pct_peer(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series,
) -> pd.Series:
    """Count of PE/PB/PS/EV-EBITDA multiples trading below 70% of peer median (0-4 deep-discount score)."""
    return (
        (pe < 0.70 * peer_median_pe).astype(float)
        + (pb < 0.70 * peer_median_pb).astype(float)
        + (ps < 0.70 * peer_median_ps).astype(float)
        + (evebitda < 0.70 * peer_median_evebitda).astype(float)
    )


def vvp_ext_070_min_cross_multiple_rel_ratio(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series,
) -> pd.Series:
    """Minimum relative ratio across PE/PB/PS (cheapest single multiple vs peers)."""
    frame = pd.concat([
        _rel_ratio(pe, peer_median_pe),
        _rel_ratio(pb, peer_median_pb),
        _rel_ratio(ps, peer_median_ps),
    ], axis=1)
    return frame.min(axis=1)


def vvp_ext_071_cross_multiple_rel_ratio_dispersion(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series,
) -> pd.Series:
    """Std-dev across PE/PB/PS relative ratios (consistency of peer discount)."""
    frame = pd.concat([
        _rel_ratio(pe, peer_median_pe),
        _rel_ratio(pb, peer_median_pb),
        _rel_ratio(ps, peer_median_ps),
    ], axis=1)
    return frame.std(axis=1)


def vvp_ext_072_mean_cross_multiple_log_rel(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series,
) -> pd.Series:
    """Mean signed log-relative across PE/PB/PS/EV-EBITDA (negative = broad peer discount)."""
    return (
        _log_rel(pe, peer_median_pe)
        + _log_rel(pb, peer_median_pb)
        + _log_rel(ps, peer_median_ps)
        + _log_rel(evebitda, peer_median_evebitda)
    ) / 4.0


def vvp_ext_073_frac_metrics_below_peer_63d(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series,
) -> pd.Series:
    """63-day mean of the count of PE/PB/PS metrics below peer median (smoothed discount breadth)."""
    score = (
        _discount_flag(pe, peer_median_pe)
        + _discount_flag(pb, peer_median_pb)
        + _discount_flag(ps, peer_median_ps)
    )
    return _rolling_mean(score, _TD_QTR)


def vvp_ext_074_all_metrics_extreme_discount_streak(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series,
) -> pd.Series:
    """Consecutive days ALL of PE/PB/PS simultaneously traded below peer median."""
    all_below = (
        (pe < peer_median_pe) & (pb < peer_median_pb) & (ps < peer_median_ps)
    )
    return _consec_streak(all_below)


def vvp_ext_075_peer_discount_capitulation_composite(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series,
    divyield: pd.Series, peer_median_divyield: pd.Series,
) -> pd.Series:
    """Peer-discount capitulation composite: mean of 252d rel-ratio pct-ranks for PE/PB/PS
    plus inverted div-yield rel-ratio rank. Low score = deeply cheap and high-yielding vs peers."""
    def _rank252(s):
        return s.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    r_pe = _rank252(_rel_ratio(pe, peer_median_pe))
    r_pb = _rank252(_rel_ratio(pb, peer_median_pb))
    r_ps = _rank252(_rel_ratio(ps, peer_median_ps))
    r_dy = 1.0 - _rank252(_rel_ratio(divyield, peer_median_divyield))
    return (r_pe + r_pb + r_ps + r_dy) / 4.0


# ── Registry ──────────────────────────────────────────────────────────────────

VALUATION_VS_PEERS_EXTENDED_REGISTRY_001_075 = {
    "vvp_ext_001_pe_rel_drawup_from_252d_min": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_001_pe_rel_drawup_from_252d_min},
    "vvp_ext_002_pb_rel_drawup_from_252d_min": {"inputs": ["pb", "peer_median_pb"], "func": vvp_ext_002_pb_rel_drawup_from_252d_min},
    "vvp_ext_003_ps_rel_drawup_from_504d_min": {"inputs": ["ps", "peer_median_ps"], "func": vvp_ext_003_ps_rel_drawup_from_504d_min},
    "vvp_ext_004_evebitda_rel_drawup_from_252d_min": {"inputs": ["evebitda", "peer_median_evebitda"], "func": vvp_ext_004_evebitda_rel_drawup_from_252d_min},
    "vvp_ext_005_pe_rel_drawdown_from_252d_max": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_005_pe_rel_drawdown_from_252d_max},
    "vvp_ext_006_pb_rel_drawdown_from_504d_max": {"inputs": ["pb", "peer_median_pb"], "func": vvp_ext_006_pb_rel_drawdown_from_504d_max},
    "vvp_ext_007_ps_rel_drawdown_from_252d_max": {"inputs": ["ps", "peer_median_ps"], "func": vvp_ext_007_ps_rel_drawdown_from_252d_max},
    "vvp_ext_008_evebit_rel_drawdown_from_252d_max": {"inputs": ["evebit", "peer_median_evebit"], "func": vvp_ext_008_evebit_rel_drawdown_from_252d_max},
    "vvp_ext_009_evebitda_rel_drawdown_from_756d_max": {"inputs": ["evebitda", "peer_median_evebitda"], "func": vvp_ext_009_evebitda_rel_drawdown_from_756d_max},
    "vvp_ext_010_pe_rel_drawdown_from_expanding_max": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_010_pe_rel_drawdown_from_expanding_max},
    "vvp_ext_011_pe_rel_over_252d_min": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_011_pe_rel_over_252d_min},
    "vvp_ext_012_pb_rel_over_252d_min": {"inputs": ["pb", "peer_median_pb"], "func": vvp_ext_012_pb_rel_over_252d_min},
    "vvp_ext_013_ps_rel_over_252d_min": {"inputs": ["ps", "peer_median_ps"], "func": vvp_ext_013_ps_rel_over_252d_min},
    "vvp_ext_014_evebitda_rel_over_504d_min": {"inputs": ["evebitda", "peer_median_evebitda"], "func": vvp_ext_014_evebitda_rel_over_504d_min},
    "vvp_ext_015_pe_rel_over_252d_max": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_015_pe_rel_over_252d_max},
    "vvp_ext_016_pb_rel_over_252d_max": {"inputs": ["pb", "peer_median_pb"], "func": vvp_ext_016_pb_rel_over_252d_max},
    "vvp_ext_017_evebit_rel_over_252d_min": {"inputs": ["evebit", "peer_median_evebit"], "func": vvp_ext_017_evebit_rel_over_252d_min},
    "vvp_ext_018_marketcap_rel_over_252d_min": {"inputs": ["marketcap", "peer_median_marketcap"], "func": vvp_ext_018_marketcap_rel_over_252d_min},
    "vvp_ext_019_pe_rel_range_position_252d": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_019_pe_rel_range_position_252d},
    "vvp_ext_020_pb_rel_range_position_504d": {"inputs": ["pb", "peer_median_pb"], "func": vvp_ext_020_pb_rel_range_position_504d},
    "vvp_ext_021_pe_rel_robust_z_252d": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_021_pe_rel_robust_z_252d},
    "vvp_ext_022_pb_rel_robust_z_252d": {"inputs": ["pb", "peer_median_pb"], "func": vvp_ext_022_pb_rel_robust_z_252d},
    "vvp_ext_023_ps_rel_robust_z_252d": {"inputs": ["ps", "peer_median_ps"], "func": vvp_ext_023_ps_rel_robust_z_252d},
    "vvp_ext_024_evebitda_rel_robust_z_252d": {"inputs": ["evebitda", "peer_median_evebitda"], "func": vvp_ext_024_evebitda_rel_robust_z_252d},
    "vvp_ext_025_evebit_rel_robust_z_252d": {"inputs": ["evebit", "peer_median_evebit"], "func": vvp_ext_025_evebit_rel_robust_z_252d},
    "vvp_ext_026_pe_rel_robust_z_504d": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_026_pe_rel_robust_z_504d},
    "vvp_ext_027_log_pe_rel_robust_z_252d": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_027_log_pe_rel_robust_z_252d},
    "vvp_ext_028_log_pb_rel_robust_z_252d": {"inputs": ["pb", "peer_median_pb"], "func": vvp_ext_028_log_pb_rel_robust_z_252d},
    "vvp_ext_029_divyield_rel_robust_z_252d": {"inputs": ["divyield", "peer_median_divyield"], "func": vvp_ext_029_divyield_rel_robust_z_252d},
    "vvp_ext_030_marketcap_rel_robust_z_252d": {"inputs": ["marketcap", "peer_median_marketcap"], "func": vvp_ext_030_marketcap_rel_robust_z_252d},
    "vvp_ext_031_pe_rel_slope_63d": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_031_pe_rel_slope_63d},
    "vvp_ext_032_pe_rel_slope_252d": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_032_pe_rel_slope_252d},
    "vvp_ext_033_pb_rel_slope_63d": {"inputs": ["pb", "peer_median_pb"], "func": vvp_ext_033_pb_rel_slope_63d},
    "vvp_ext_034_ps_rel_slope_126d": {"inputs": ["ps", "peer_median_ps"], "func": vvp_ext_034_ps_rel_slope_126d},
    "vvp_ext_035_evebitda_rel_slope_63d": {"inputs": ["evebitda", "peer_median_evebitda"], "func": vvp_ext_035_evebitda_rel_slope_63d},
    "vvp_ext_036_log_pe_rel_slope_126d": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_036_log_pe_rel_slope_126d},
    "vvp_ext_037_pe_gap_slope_63d": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_037_pe_gap_slope_63d},
    "vvp_ext_038_pb_gap_slope_126d": {"inputs": ["pb", "peer_median_pb"], "func": vvp_ext_038_pb_gap_slope_126d},
    "vvp_ext_039_divyield_rel_slope_126d": {"inputs": ["divyield", "peer_median_divyield"], "func": vvp_ext_039_divyield_rel_slope_126d},
    "vvp_ext_040_pe_rel_slope_normalized_63d": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_040_pe_rel_slope_normalized_63d},
    "vvp_ext_041_pe_consec_days_discount": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_041_pe_consec_days_discount},
    "vvp_ext_042_pb_consec_days_discount": {"inputs": ["pb", "peer_median_pb"], "func": vvp_ext_042_pb_consec_days_discount},
    "vvp_ext_043_ps_consec_days_discount": {"inputs": ["ps", "peer_median_ps"], "func": vvp_ext_043_ps_consec_days_discount},
    "vvp_ext_044_evebitda_consec_days_discount": {"inputs": ["evebitda", "peer_median_evebitda"], "func": vvp_ext_044_evebitda_consec_days_discount},
    "vvp_ext_045_pe_consec_days_deep_discount": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_045_pe_consec_days_deep_discount},
    "vvp_ext_046_pb_consec_days_deep_discount": {"inputs": ["pb", "peer_median_pb"], "func": vvp_ext_046_pb_consec_days_deep_discount},
    "vvp_ext_047_pe_max_discount_streak_252d": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_047_pe_max_discount_streak_252d},
    "vvp_ext_048_divyield_consec_days_yield_premium": {"inputs": ["divyield", "peer_median_divyield"], "func": vvp_ext_048_divyield_consec_days_yield_premium},
    "vvp_ext_049_pe_days_since_last_premium": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_049_pe_days_since_last_premium},
    "vvp_ext_050_pe_rel_consec_days_below_252d_median": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_050_pe_rel_consec_days_below_252d_median},
    "vvp_ext_051_pb_rel_consec_days_below_252d_median": {"inputs": ["pb", "peer_median_pb"], "func": vvp_ext_051_pb_rel_consec_days_below_252d_median},
    "vvp_ext_052_ps_rel_consec_days_at_252d_low": {"inputs": ["ps", "peer_median_ps"], "func": vvp_ext_052_ps_rel_consec_days_at_252d_low},
    "vvp_ext_053_pe_rel_rolling_skew_252d": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_053_pe_rel_rolling_skew_252d},
    "vvp_ext_054_pe_rel_rolling_kurt_252d": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_054_pe_rel_rolling_kurt_252d},
    "vvp_ext_055_pb_rel_rolling_skew_252d": {"inputs": ["pb", "peer_median_pb"], "func": vvp_ext_055_pb_rel_rolling_skew_252d},
    "vvp_ext_056_ps_rel_rolling_skew_126d": {"inputs": ["ps", "peer_median_ps"], "func": vvp_ext_056_ps_rel_rolling_skew_126d},
    "vvp_ext_057_evebitda_rel_rolling_skew_252d": {"inputs": ["evebitda", "peer_median_evebitda"], "func": vvp_ext_057_evebitda_rel_rolling_skew_252d},
    "vvp_ext_058_pe_rel_coef_of_variation_252d": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_058_pe_rel_coef_of_variation_252d},
    "vvp_ext_059_pb_rel_coef_of_variation_252d": {"inputs": ["pb", "peer_median_pb"], "func": vvp_ext_059_pb_rel_coef_of_variation_252d},
    "vvp_ext_060_pe_rel_iqr_width_252d": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_060_pe_rel_iqr_width_252d},
    "vvp_ext_061_evebitda_rel_rolling_kurt_252d": {"inputs": ["evebitda", "peer_median_evebitda"], "func": vvp_ext_061_evebitda_rel_rolling_kurt_252d},
    "vvp_ext_062_divyield_rel_rolling_skew_252d": {"inputs": ["divyield", "peer_median_divyield"], "func": vvp_ext_062_divyield_rel_rolling_skew_252d},
    "vvp_ext_063_pe_gap_over_252d_mad": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_063_pe_gap_over_252d_mad},
    "vvp_ext_064_pb_gap_over_252d_mad": {"inputs": ["pb", "peer_median_pb"], "func": vvp_ext_064_pb_gap_over_252d_mad},
    "vvp_ext_065_ps_gap_over_252d_std": {"inputs": ["ps", "peer_median_ps"], "func": vvp_ext_065_ps_gap_over_252d_std},
    "vvp_ext_066_evebitda_gap_over_252d_std": {"inputs": ["evebitda", "peer_median_evebitda"], "func": vvp_ext_066_evebitda_gap_over_252d_std},
    "vvp_ext_067_pe_gap_minus_252d_min": {"inputs": ["pe", "peer_median_pe"], "func": vvp_ext_067_pe_gap_minus_252d_min},
    "vvp_ext_068_pb_gap_ewm126": {"inputs": ["pb", "peer_median_pb"], "func": vvp_ext_068_pb_gap_ewm126},
    "vvp_ext_069_count_metrics_below_70pct_peer": {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps", "evebitda", "peer_median_evebitda"], "func": vvp_ext_069_count_metrics_below_70pct_peer},
    "vvp_ext_070_min_cross_multiple_rel_ratio": {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps"], "func": vvp_ext_070_min_cross_multiple_rel_ratio},
    "vvp_ext_071_cross_multiple_rel_ratio_dispersion": {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps"], "func": vvp_ext_071_cross_multiple_rel_ratio_dispersion},
    "vvp_ext_072_mean_cross_multiple_log_rel": {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps", "evebitda", "peer_median_evebitda"], "func": vvp_ext_072_mean_cross_multiple_log_rel},
    "vvp_ext_073_frac_metrics_below_peer_63d": {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps"], "func": vvp_ext_073_frac_metrics_below_peer_63d},
    "vvp_ext_074_all_metrics_extreme_discount_streak": {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps"], "func": vvp_ext_074_all_metrics_extreme_discount_streak},
    "vvp_ext_075_peer_discount_capitulation_composite": {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps", "divyield", "peer_median_divyield"], "func": vvp_ext_075_peer_discount_capitulation_composite},
}
