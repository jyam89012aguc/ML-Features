"""
81_valuation_vs_history — Extended Features 001-075
Domain: own-history valuation positioning — additional angles not in the base
        files: drawdown-from-trailing-peak, rolling-skew/kurtosis, MAD-based
        robust scores, slope/trend of multiples, streaks below thresholds,
        EWM range positions, cross-multiple dispersion, quantile depths.
Asset class: US equities | Daily-frequency Sharadar valuation fields —
        pe, pb, ps, ev, marketcap, evebit, evebitda, divyield
All feature functions are strictly backward-looking (rolling/expanding windows
over trailing data only). No negative shifts, no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_2Y = 504
_TD_3Y = 756
_TD_5Y = 1260
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _log_safe(s: pd.Series) -> pd.Series:
    """Natural log of a strictly-positive-clipped series."""
    return np.log(s.clip(lower=_EPS))


def _drawup_from_min(s: pd.Series, w: int) -> pd.Series:
    """Fractional rise of s above its trailing w-day minimum."""
    lo = _rolling_min(s, w)
    return _safe_div(s - lo, lo.abs())


def _drawdown_from_max(s: pd.Series, w: int) -> pd.Series:
    """Fractional fall of s below its trailing w-day maximum (<=0)."""
    hi = _rolling_max(s, w)
    return _safe_div(s - hi, hi.abs())


def _rolling_skew(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(3, w // 2)).skew()


def _rolling_kurt(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(4, w // 2)).kurt()


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


def _quantile_roll(s: pd.Series, w: int, q: float) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 2)).quantile(q)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Drawdown/draw-up from trailing extremes ---


def vvh_ext_001_pe_drawup_from_252d_min(pe: pd.Series) -> pd.Series:
    """Fractional rise of P/E above its trailing 252-day minimum."""
    return _drawup_from_min(pe, _TD_YEAR)


def vvh_ext_002_pe_drawup_from_756d_min(pe: pd.Series) -> pd.Series:
    """Fractional rise of P/E above its trailing 756-day (3-year) minimum."""
    return _drawup_from_min(pe, _TD_3Y)


def vvh_ext_003_pb_drawup_from_756d_min(pb: pd.Series) -> pd.Series:
    """Fractional rise of P/B above its trailing 756-day minimum."""
    return _drawup_from_min(pb, _TD_3Y)


def vvh_ext_004_ps_drawup_from_504d_min(ps: pd.Series) -> pd.Series:
    """Fractional rise of P/S above its trailing 504-day minimum."""
    return _drawup_from_min(ps, _TD_2Y)


def vvh_ext_005_pe_drawdown_from_252d_max(pe: pd.Series) -> pd.Series:
    """Fractional fall of P/E below its trailing 252-day maximum (multiple compression)."""
    return _drawdown_from_max(pe, _TD_YEAR)


def vvh_ext_006_pb_drawdown_from_504d_max(pb: pd.Series) -> pd.Series:
    """Fractional fall of P/B below its trailing 504-day maximum."""
    return _drawdown_from_max(pb, _TD_2Y)


def vvh_ext_007_ps_drawdown_from_252d_max(ps: pd.Series) -> pd.Series:
    """Fractional fall of P/S below its trailing 252-day maximum."""
    return _drawdown_from_max(ps, _TD_YEAR)


def vvh_ext_008_evebitda_drawdown_from_756d_max(evebitda: pd.Series) -> pd.Series:
    """Fractional fall of EV/EBITDA below its trailing 756-day maximum."""
    return _drawdown_from_max(evebitda, _TD_3Y)


def vvh_ext_009_marketcap_drawdown_from_252d_max(marketcap: pd.Series) -> pd.Series:
    """Fractional fall of market cap below its trailing 252-day maximum (price drawdown proxy)."""
    return _drawdown_from_max(marketcap, _TD_YEAR)


def vvh_ext_010_pe_drawdown_from_expanding_max(pe: pd.Series) -> pd.Series:
    """Fractional fall of P/E below its all-history expanding maximum."""
    peak = pe.expanding(min_periods=5).max()
    return _safe_div(pe - peak, peak.abs())


# --- Group B (011-020): Multiple-of-trailing-min (depth ratios) ---


def vvh_ext_011_pe_over_252d_min(pe: pd.Series) -> pd.Series:
    """P/E as a multiple of its trailing 252-day minimum (1 = at trough)."""
    return _safe_div(pe, _rolling_min(pe, _TD_YEAR))


def vvh_ext_012_pe_over_1260d_min(pe: pd.Series) -> pd.Series:
    """P/E as a multiple of its trailing 1260-day minimum."""
    return _safe_div(pe, _rolling_min(pe, _TD_5Y))


def vvh_ext_013_pb_over_252d_min(pb: pd.Series) -> pd.Series:
    """P/B as a multiple of its trailing 252-day minimum."""
    return _safe_div(pb, _rolling_min(pb, _TD_YEAR))


def vvh_ext_014_pb_over_1260d_min(pb: pd.Series) -> pd.Series:
    """P/B as a multiple of its trailing 1260-day minimum."""
    return _safe_div(pb, _rolling_min(pb, _TD_5Y))


def vvh_ext_015_ps_over_252d_min(ps: pd.Series) -> pd.Series:
    """P/S as a multiple of its trailing 252-day minimum."""
    return _safe_div(ps, _rolling_min(ps, _TD_YEAR))


def vvh_ext_016_evebitda_over_252d_min(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA as a multiple of its trailing 252-day minimum."""
    return _safe_div(evebitda, _rolling_min(evebitda, _TD_YEAR))


def vvh_ext_017_evebit_over_504d_min(evebit: pd.Series) -> pd.Series:
    """EV/EBIT as a multiple of its trailing 504-day minimum."""
    return _safe_div(evebit, _rolling_min(evebit, _TD_2Y))


def vvh_ext_018_pe_over_trailing_max_252d(pe: pd.Series) -> pd.Series:
    """P/E as a fraction of its trailing 252-day maximum (0..1, low = compressed)."""
    return _safe_div(pe, _rolling_max(pe, _TD_YEAR))


def vvh_ext_019_pb_over_trailing_max_1260d(pb: pd.Series) -> pd.Series:
    """P/B as a fraction of its trailing 1260-day maximum."""
    return _safe_div(pb, _rolling_max(pb, _TD_5Y))


def vvh_ext_020_marketcap_over_252d_min(marketcap: pd.Series) -> pd.Series:
    """Market cap as a multiple of its trailing 252-day minimum."""
    return _safe_div(marketcap, _rolling_min(marketcap, _TD_YEAR))


# --- Group C (021-030): Robust median/MAD z-scores ---


def vvh_ext_021_pe_robust_z_252d(pe: pd.Series) -> pd.Series:
    """Median/MAD robust z-score of P/E over trailing 252 days."""
    return _robust_z(pe, _TD_YEAR)


def vvh_ext_022_pe_robust_z_1260d(pe: pd.Series) -> pd.Series:
    """Median/MAD robust z-score of P/E over trailing 1260 days."""
    return _robust_z(pe, _TD_5Y)


def vvh_ext_023_pb_robust_z_252d(pb: pd.Series) -> pd.Series:
    """Median/MAD robust z-score of P/B over trailing 252 days."""
    return _robust_z(pb, _TD_YEAR)


def vvh_ext_024_pb_robust_z_504d(pb: pd.Series) -> pd.Series:
    """Median/MAD robust z-score of P/B over trailing 504 days."""
    return _robust_z(pb, _TD_2Y)


def vvh_ext_025_ps_robust_z_252d(ps: pd.Series) -> pd.Series:
    """Median/MAD robust z-score of P/S over trailing 252 days."""
    return _robust_z(ps, _TD_YEAR)


def vvh_ext_026_ps_robust_z_1260d(ps: pd.Series) -> pd.Series:
    """Median/MAD robust z-score of P/S over trailing 1260 days."""
    return _robust_z(ps, _TD_5Y)


def vvh_ext_027_evebitda_robust_z_252d(evebitda: pd.Series) -> pd.Series:
    """Median/MAD robust z-score of EV/EBITDA over trailing 252 days."""
    return _robust_z(evebitda, _TD_YEAR)


def vvh_ext_028_evebit_robust_z_252d(evebit: pd.Series) -> pd.Series:
    """Median/MAD robust z-score of EV/EBIT over trailing 252 days."""
    return _robust_z(evebit, _TD_YEAR)


def vvh_ext_029_divyield_robust_z_252d(divyield: pd.Series) -> pd.Series:
    """Median/MAD robust z-score of dividend yield over trailing 252 days."""
    return _robust_z(divyield, _TD_YEAR)


def vvh_ext_030_marketcap_robust_z_252d(marketcap: pd.Series) -> pd.Series:
    """Median/MAD robust z-score of market cap over trailing 252 days."""
    return _robust_z(marketcap, _TD_YEAR)


# --- Group D (031-040): Rolling skew / kurtosis of multiples ---


def vvh_ext_031_pe_rolling_skew_252d(pe: pd.Series) -> pd.Series:
    """Rolling 252-day skewness of P/E (distribution asymmetry of valuation)."""
    return _rolling_skew(pe, _TD_YEAR)


def vvh_ext_032_pe_rolling_kurt_252d(pe: pd.Series) -> pd.Series:
    """Rolling 252-day excess kurtosis of P/E (tail heaviness)."""
    return _rolling_kurt(pe, _TD_YEAR)


def vvh_ext_033_pb_rolling_skew_252d(pb: pd.Series) -> pd.Series:
    """Rolling 252-day skewness of P/B."""
    return _rolling_skew(pb, _TD_YEAR)


def vvh_ext_034_pb_rolling_kurt_252d(pb: pd.Series) -> pd.Series:
    """Rolling 252-day excess kurtosis of P/B."""
    return _rolling_kurt(pb, _TD_YEAR)


def vvh_ext_035_ps_rolling_skew_126d(ps: pd.Series) -> pd.Series:
    """Rolling 126-day skewness of P/S."""
    return _rolling_skew(ps, _TD_HALF)


def vvh_ext_036_evebitda_rolling_skew_252d(evebitda: pd.Series) -> pd.Series:
    """Rolling 252-day skewness of EV/EBITDA."""
    return _rolling_skew(evebitda, _TD_YEAR)


def vvh_ext_037_log_pe_rolling_skew_252d(pe: pd.Series) -> pd.Series:
    """Rolling 252-day skewness of log(P/E)."""
    return _rolling_skew(_log_safe(pe), _TD_YEAR)


def vvh_ext_038_pe_rolling_kurt_504d(pe: pd.Series) -> pd.Series:
    """Rolling 504-day excess kurtosis of P/E."""
    return _rolling_kurt(pe, _TD_2Y)


def vvh_ext_039_divyield_rolling_skew_252d(divyield: pd.Series) -> pd.Series:
    """Rolling 252-day skewness of dividend yield."""
    return _rolling_skew(divyield, _TD_YEAR)


def vvh_ext_040_marketcap_rolling_skew_252d(marketcap: pd.Series) -> pd.Series:
    """Rolling 252-day skewness of market cap."""
    return _rolling_skew(marketcap, _TD_YEAR)


# --- Group E (041-050): Trend / slope of valuation multiples ---


def vvh_ext_041_pe_slope_63d(pe: pd.Series) -> pd.Series:
    """Least-squares slope of P/E over trailing 63 days (per-day drift)."""
    return _slope(pe, _TD_QTR)


def vvh_ext_042_pe_slope_252d(pe: pd.Series) -> pd.Series:
    """Least-squares slope of P/E over trailing 252 days."""
    return _slope(pe, _TD_YEAR)


def vvh_ext_043_pb_slope_63d(pb: pd.Series) -> pd.Series:
    """Least-squares slope of P/B over trailing 63 days."""
    return _slope(pb, _TD_QTR)


def vvh_ext_044_pb_slope_252d(pb: pd.Series) -> pd.Series:
    """Least-squares slope of P/B over trailing 252 days."""
    return _slope(pb, _TD_YEAR)


def vvh_ext_045_ps_slope_126d(ps: pd.Series) -> pd.Series:
    """Least-squares slope of P/S over trailing 126 days."""
    return _slope(ps, _TD_HALF)


def vvh_ext_046_log_pe_slope_126d(pe: pd.Series) -> pd.Series:
    """Least-squares slope of log(P/E) over trailing 126 days (compounding drift)."""
    return _slope(_log_safe(pe), _TD_HALF)


def vvh_ext_047_evebitda_slope_63d(evebitda: pd.Series) -> pd.Series:
    """Least-squares slope of EV/EBITDA over trailing 63 days."""
    return _slope(evebitda, _TD_QTR)


def vvh_ext_048_marketcap_slope_63d(marketcap: pd.Series) -> pd.Series:
    """Least-squares slope of market cap over trailing 63 days."""
    return _slope(marketcap, _TD_QTR)


def vvh_ext_049_divyield_slope_126d(divyield: pd.Series) -> pd.Series:
    """Least-squares slope of dividend yield over trailing 126 days."""
    return _slope(divyield, _TD_HALF)


def vvh_ext_050_pe_slope_normalized_63d(pe: pd.Series) -> pd.Series:
    """63-day P/E slope normalized by trailing 63-day mean P/E (per-day percent drift)."""
    return _safe_div(_slope(pe, _TD_QTR), _rolling_mean(pe, _TD_QTR))


# --- Group F (051-060): Streaks below thresholds / cheap regimes ---


def vvh_ext_051_pe_consec_days_below_median_252d(pe: pd.Series) -> pd.Series:
    """Consecutive days P/E has been below its trailing 252-day median."""
    return _consec_streak(pe < _rolling_median(pe, _TD_YEAR))


def vvh_ext_052_pb_consec_days_below_median_252d(pb: pd.Series) -> pd.Series:
    """Consecutive days P/B has been below its trailing 252-day median."""
    return _consec_streak(pb < _rolling_median(pb, _TD_YEAR))


def vvh_ext_053_ps_consec_days_below_median_252d(ps: pd.Series) -> pd.Series:
    """Consecutive days P/S has been below its trailing 252-day median."""
    return _consec_streak(ps < _rolling_median(ps, _TD_YEAR))


def vvh_ext_054_pe_consec_days_below_q25_252d(pe: pd.Series) -> pd.Series:
    """Consecutive days P/E has been below its trailing 252-day 25th percentile."""
    return _consec_streak(pe < _quantile_roll(pe, _TD_YEAR, 0.25))


def vvh_ext_055_pb_consec_days_below_q10_252d(pb: pd.Series) -> pd.Series:
    """Consecutive days P/B has been below its trailing 252-day 10th percentile."""
    return _consec_streak(pb < _quantile_roll(pb, _TD_YEAR, 0.10))


def vvh_ext_056_evebitda_consec_days_below_median_252d(evebitda: pd.Series) -> pd.Series:
    """Consecutive days EV/EBITDA has been below its trailing 252-day median."""
    return _consec_streak(evebitda < _rolling_median(evebitda, _TD_YEAR))


def vvh_ext_057_pe_consec_days_at_252d_low(pe: pd.Series) -> pd.Series:
    """Consecutive days P/E has sat at its trailing 252-day minimum."""
    return _consec_streak(pe <= _rolling_min(pe, _TD_YEAR))


def vvh_ext_058_divyield_consec_days_above_median_252d(divyield: pd.Series) -> pd.Series:
    """Consecutive days dividend yield has been above its trailing 252-day median (cheap-income streak)."""
    return _consec_streak(divyield > _rolling_median(divyield, _TD_YEAR))


def vvh_ext_059_pe_max_below_median_streak_252d(pe: pd.Series) -> pd.Series:
    """Longest below-median P/E streak observed within the trailing 252 days."""
    streak = _consec_streak(pe < _rolling_median(pe, _TD_YEAR))
    return _rolling_max(streak, _TD_YEAR)


def vvh_ext_060_ps_consec_days_below_q25_504d(ps: pd.Series) -> pd.Series:
    """Consecutive days P/S has been below its trailing 504-day 25th percentile."""
    return _consec_streak(ps < _quantile_roll(ps, _TD_2Y, 0.25))


# --- Group G (061-068): EWM-smoothed range positions and deviations ---


def vvh_ext_061_pe_ewm63_rangepos_252d(pe: pd.Series) -> pd.Series:
    """Position of EWM(63)-smoothed P/E within its trailing 252-day min-max range."""
    sm = _ewm_mean(pe, _TD_QTR)
    lo = _rolling_min(sm, _TD_YEAR)
    hi = _rolling_max(sm, _TD_YEAR)
    return _safe_div(sm - lo, hi - lo)


def vvh_ext_062_pb_ewm63_rangepos_252d(pb: pd.Series) -> pd.Series:
    """Position of EWM(63)-smoothed P/B within its trailing 252-day min-max range."""
    sm = _ewm_mean(pb, _TD_QTR)
    lo = _rolling_min(sm, _TD_YEAR)
    hi = _rolling_max(sm, _TD_YEAR)
    return _safe_div(sm - lo, hi - lo)


def vvh_ext_063_pe_minus_ewm126(pe: pd.Series) -> pd.Series:
    """P/E minus its EWM(126) — deviation of current multiple from smoothed trend."""
    return pe - _ewm_mean(pe, _TD_HALF)


def vvh_ext_064_pe_over_ewm252(pe: pd.Series) -> pd.Series:
    """P/E as a fraction of its EWM(252) trend (below 1 = cheap vs smoothed history)."""
    return _safe_div(pe, _ewm_mean(pe, _TD_YEAR))


def vvh_ext_065_pb_over_ewm252(pb: pd.Series) -> pd.Series:
    """P/B as a fraction of its EWM(252) trend."""
    return _safe_div(pb, _ewm_mean(pb, _TD_YEAR))


def vvh_ext_066_ps_over_ewm126(ps: pd.Series) -> pd.Series:
    """P/S as a fraction of its EWM(126) trend."""
    return _safe_div(ps, _ewm_mean(ps, _TD_HALF))


def vvh_ext_067_evebitda_over_ewm252(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA as a fraction of its EWM(252) trend."""
    return _safe_div(evebitda, _ewm_mean(evebitda, _TD_YEAR))


def vvh_ext_068_marketcap_minus_ewm126(marketcap: pd.Series) -> pd.Series:
    """Market cap minus its EWM(126) — deviation from smoothed size trend."""
    return marketcap - _ewm_mean(marketcap, _TD_HALF)


# --- Group H (069-075): Quantile-depth, dispersion and cross-multiple composites ---


def vvh_ext_069_pe_depth_below_q10_252d(pe: pd.Series) -> pd.Series:
    """How far P/E sits below its trailing 252-day 10th percentile, scaled (>=0)."""
    q10 = _quantile_roll(pe, _TD_YEAR, 0.10)
    return _safe_div(q10 - pe, q10.abs()).clip(lower=0.0)


def vvh_ext_070_pb_depth_below_q10_252d(pb: pd.Series) -> pd.Series:
    """How far P/B sits below its trailing 252-day 10th percentile, scaled (>=0)."""
    q10 = _quantile_roll(pb, _TD_YEAR, 0.10)
    return _safe_div(q10 - pb, q10.abs()).clip(lower=0.0)


def vvh_ext_071_pe_coef_of_variation_252d(pe: pd.Series) -> pd.Series:
    """Coefficient of variation of P/E over trailing 252 days (std / mean)."""
    return _safe_div(_rolling_std(pe, _TD_YEAR), _rolling_mean(pe, _TD_YEAR))


def vvh_ext_072_pb_iqr_width_252d(pb: pd.Series) -> pd.Series:
    """Trailing 252-day inter-quartile width of P/B, scaled by its median."""
    iqr = _quantile_roll(pb, _TD_YEAR, 0.75) - _quantile_roll(pb, _TD_YEAR, 0.25)
    return _safe_div(iqr, _rolling_median(pb, _TD_YEAR))


def vvh_ext_073_cross_multiple_rank_dispersion_252d(pe: pd.Series, pb: pd.Series, ps: pd.Series) -> pd.Series:
    """Std-dev across PE/PB/PS 252-day percentile ranks (cheap-on-all vs mixed signal)."""
    r_pe = _rolling_rank_pct(pe, _TD_YEAR)
    r_pb = _rolling_rank_pct(pb, _TD_YEAR)
    r_ps = _rolling_rank_pct(ps, _TD_YEAR)
    frame = pd.concat([r_pe, r_pb, r_ps], axis=1)
    return frame.std(axis=1)


def vvh_ext_074_min_cross_multiple_rank_252d(pe: pd.Series, pb: pd.Series, ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Minimum 252-day percentile rank across PE/PB/PS/EV-EBITDA (cheapest single metric)."""
    r_pe = _rolling_rank_pct(pe, _TD_YEAR)
    r_pb = _rolling_rank_pct(pb, _TD_YEAR)
    r_ps = _rolling_rank_pct(ps, _TD_YEAR)
    r_ev = _rolling_rank_pct(evebitda, _TD_YEAR)
    frame = pd.concat([r_pe, r_pb, r_ps, r_ev], axis=1)
    return frame.min(axis=1)


def vvh_ext_075_extreme_cheapness_composite_252d(pe: pd.Series, pb: pd.Series, ps: pd.Series, divyield: pd.Series) -> pd.Series:
    """Capitulation cheapness composite: mean of (1-rank) for PE/PB/PS plus divyield rank, 252d.
    Higher = cheaper on price multiples and richer on yield simultaneously."""
    c_pe = 1.0 - _rolling_rank_pct(pe, _TD_YEAR)
    c_pb = 1.0 - _rolling_rank_pct(pb, _TD_YEAR)
    c_ps = 1.0 - _rolling_rank_pct(ps, _TD_YEAR)
    c_dy = _rolling_rank_pct(divyield, _TD_YEAR)
    return (c_pe + c_pb + c_ps + c_dy) / 4.0


# ── Registry ──────────────────────────────────────────────────────────────────

VALUATION_VS_HISTORY_EXTENDED_REGISTRY_001_075 = {
    "vvh_ext_001_pe_drawup_from_252d_min": {"inputs": ["pe"], "func": vvh_ext_001_pe_drawup_from_252d_min},
    "vvh_ext_002_pe_drawup_from_756d_min": {"inputs": ["pe"], "func": vvh_ext_002_pe_drawup_from_756d_min},
    "vvh_ext_003_pb_drawup_from_756d_min": {"inputs": ["pb"], "func": vvh_ext_003_pb_drawup_from_756d_min},
    "vvh_ext_004_ps_drawup_from_504d_min": {"inputs": ["ps"], "func": vvh_ext_004_ps_drawup_from_504d_min},
    "vvh_ext_005_pe_drawdown_from_252d_max": {"inputs": ["pe"], "func": vvh_ext_005_pe_drawdown_from_252d_max},
    "vvh_ext_006_pb_drawdown_from_504d_max": {"inputs": ["pb"], "func": vvh_ext_006_pb_drawdown_from_504d_max},
    "vvh_ext_007_ps_drawdown_from_252d_max": {"inputs": ["ps"], "func": vvh_ext_007_ps_drawdown_from_252d_max},
    "vvh_ext_008_evebitda_drawdown_from_756d_max": {"inputs": ["evebitda"], "func": vvh_ext_008_evebitda_drawdown_from_756d_max},
    "vvh_ext_009_marketcap_drawdown_from_252d_max": {"inputs": ["marketcap"], "func": vvh_ext_009_marketcap_drawdown_from_252d_max},
    "vvh_ext_010_pe_drawdown_from_expanding_max": {"inputs": ["pe"], "func": vvh_ext_010_pe_drawdown_from_expanding_max},
    "vvh_ext_011_pe_over_252d_min": {"inputs": ["pe"], "func": vvh_ext_011_pe_over_252d_min},
    "vvh_ext_012_pe_over_1260d_min": {"inputs": ["pe"], "func": vvh_ext_012_pe_over_1260d_min},
    "vvh_ext_013_pb_over_252d_min": {"inputs": ["pb"], "func": vvh_ext_013_pb_over_252d_min},
    "vvh_ext_014_pb_over_1260d_min": {"inputs": ["pb"], "func": vvh_ext_014_pb_over_1260d_min},
    "vvh_ext_015_ps_over_252d_min": {"inputs": ["ps"], "func": vvh_ext_015_ps_over_252d_min},
    "vvh_ext_016_evebitda_over_252d_min": {"inputs": ["evebitda"], "func": vvh_ext_016_evebitda_over_252d_min},
    "vvh_ext_017_evebit_over_504d_min": {"inputs": ["evebit"], "func": vvh_ext_017_evebit_over_504d_min},
    "vvh_ext_018_pe_over_trailing_max_252d": {"inputs": ["pe"], "func": vvh_ext_018_pe_over_trailing_max_252d},
    "vvh_ext_019_pb_over_trailing_max_1260d": {"inputs": ["pb"], "func": vvh_ext_019_pb_over_trailing_max_1260d},
    "vvh_ext_020_marketcap_over_252d_min": {"inputs": ["marketcap"], "func": vvh_ext_020_marketcap_over_252d_min},
    "vvh_ext_021_pe_robust_z_252d": {"inputs": ["pe"], "func": vvh_ext_021_pe_robust_z_252d},
    "vvh_ext_022_pe_robust_z_1260d": {"inputs": ["pe"], "func": vvh_ext_022_pe_robust_z_1260d},
    "vvh_ext_023_pb_robust_z_252d": {"inputs": ["pb"], "func": vvh_ext_023_pb_robust_z_252d},
    "vvh_ext_024_pb_robust_z_504d": {"inputs": ["pb"], "func": vvh_ext_024_pb_robust_z_504d},
    "vvh_ext_025_ps_robust_z_252d": {"inputs": ["ps"], "func": vvh_ext_025_ps_robust_z_252d},
    "vvh_ext_026_ps_robust_z_1260d": {"inputs": ["ps"], "func": vvh_ext_026_ps_robust_z_1260d},
    "vvh_ext_027_evebitda_robust_z_252d": {"inputs": ["evebitda"], "func": vvh_ext_027_evebitda_robust_z_252d},
    "vvh_ext_028_evebit_robust_z_252d": {"inputs": ["evebit"], "func": vvh_ext_028_evebit_robust_z_252d},
    "vvh_ext_029_divyield_robust_z_252d": {"inputs": ["divyield"], "func": vvh_ext_029_divyield_robust_z_252d},
    "vvh_ext_030_marketcap_robust_z_252d": {"inputs": ["marketcap"], "func": vvh_ext_030_marketcap_robust_z_252d},
    "vvh_ext_031_pe_rolling_skew_252d": {"inputs": ["pe"], "func": vvh_ext_031_pe_rolling_skew_252d},
    "vvh_ext_032_pe_rolling_kurt_252d": {"inputs": ["pe"], "func": vvh_ext_032_pe_rolling_kurt_252d},
    "vvh_ext_033_pb_rolling_skew_252d": {"inputs": ["pb"], "func": vvh_ext_033_pb_rolling_skew_252d},
    "vvh_ext_034_pb_rolling_kurt_252d": {"inputs": ["pb"], "func": vvh_ext_034_pb_rolling_kurt_252d},
    "vvh_ext_035_ps_rolling_skew_126d": {"inputs": ["ps"], "func": vvh_ext_035_ps_rolling_skew_126d},
    "vvh_ext_036_evebitda_rolling_skew_252d": {"inputs": ["evebitda"], "func": vvh_ext_036_evebitda_rolling_skew_252d},
    "vvh_ext_037_log_pe_rolling_skew_252d": {"inputs": ["pe"], "func": vvh_ext_037_log_pe_rolling_skew_252d},
    "vvh_ext_038_pe_rolling_kurt_504d": {"inputs": ["pe"], "func": vvh_ext_038_pe_rolling_kurt_504d},
    "vvh_ext_039_divyield_rolling_skew_252d": {"inputs": ["divyield"], "func": vvh_ext_039_divyield_rolling_skew_252d},
    "vvh_ext_040_marketcap_rolling_skew_252d": {"inputs": ["marketcap"], "func": vvh_ext_040_marketcap_rolling_skew_252d},
    "vvh_ext_041_pe_slope_63d": {"inputs": ["pe"], "func": vvh_ext_041_pe_slope_63d},
    "vvh_ext_042_pe_slope_252d": {"inputs": ["pe"], "func": vvh_ext_042_pe_slope_252d},
    "vvh_ext_043_pb_slope_63d": {"inputs": ["pb"], "func": vvh_ext_043_pb_slope_63d},
    "vvh_ext_044_pb_slope_252d": {"inputs": ["pb"], "func": vvh_ext_044_pb_slope_252d},
    "vvh_ext_045_ps_slope_126d": {"inputs": ["ps"], "func": vvh_ext_045_ps_slope_126d},
    "vvh_ext_046_log_pe_slope_126d": {"inputs": ["pe"], "func": vvh_ext_046_log_pe_slope_126d},
    "vvh_ext_047_evebitda_slope_63d": {"inputs": ["evebitda"], "func": vvh_ext_047_evebitda_slope_63d},
    "vvh_ext_048_marketcap_slope_63d": {"inputs": ["marketcap"], "func": vvh_ext_048_marketcap_slope_63d},
    "vvh_ext_049_divyield_slope_126d": {"inputs": ["divyield"], "func": vvh_ext_049_divyield_slope_126d},
    "vvh_ext_050_pe_slope_normalized_63d": {"inputs": ["pe"], "func": vvh_ext_050_pe_slope_normalized_63d},
    "vvh_ext_051_pe_consec_days_below_median_252d": {"inputs": ["pe"], "func": vvh_ext_051_pe_consec_days_below_median_252d},
    "vvh_ext_052_pb_consec_days_below_median_252d": {"inputs": ["pb"], "func": vvh_ext_052_pb_consec_days_below_median_252d},
    "vvh_ext_053_ps_consec_days_below_median_252d": {"inputs": ["ps"], "func": vvh_ext_053_ps_consec_days_below_median_252d},
    "vvh_ext_054_pe_consec_days_below_q25_252d": {"inputs": ["pe"], "func": vvh_ext_054_pe_consec_days_below_q25_252d},
    "vvh_ext_055_pb_consec_days_below_q10_252d": {"inputs": ["pb"], "func": vvh_ext_055_pb_consec_days_below_q10_252d},
    "vvh_ext_056_evebitda_consec_days_below_median_252d": {"inputs": ["evebitda"], "func": vvh_ext_056_evebitda_consec_days_below_median_252d},
    "vvh_ext_057_pe_consec_days_at_252d_low": {"inputs": ["pe"], "func": vvh_ext_057_pe_consec_days_at_252d_low},
    "vvh_ext_058_divyield_consec_days_above_median_252d": {"inputs": ["divyield"], "func": vvh_ext_058_divyield_consec_days_above_median_252d},
    "vvh_ext_059_pe_max_below_median_streak_252d": {"inputs": ["pe"], "func": vvh_ext_059_pe_max_below_median_streak_252d},
    "vvh_ext_060_ps_consec_days_below_q25_504d": {"inputs": ["ps"], "func": vvh_ext_060_ps_consec_days_below_q25_504d},
    "vvh_ext_061_pe_ewm63_rangepos_252d": {"inputs": ["pe"], "func": vvh_ext_061_pe_ewm63_rangepos_252d},
    "vvh_ext_062_pb_ewm63_rangepos_252d": {"inputs": ["pb"], "func": vvh_ext_062_pb_ewm63_rangepos_252d},
    "vvh_ext_063_pe_minus_ewm126": {"inputs": ["pe"], "func": vvh_ext_063_pe_minus_ewm126},
    "vvh_ext_064_pe_over_ewm252": {"inputs": ["pe"], "func": vvh_ext_064_pe_over_ewm252},
    "vvh_ext_065_pb_over_ewm252": {"inputs": ["pb"], "func": vvh_ext_065_pb_over_ewm252},
    "vvh_ext_066_ps_over_ewm126": {"inputs": ["ps"], "func": vvh_ext_066_ps_over_ewm126},
    "vvh_ext_067_evebitda_over_ewm252": {"inputs": ["evebitda"], "func": vvh_ext_067_evebitda_over_ewm252},
    "vvh_ext_068_marketcap_minus_ewm126": {"inputs": ["marketcap"], "func": vvh_ext_068_marketcap_minus_ewm126},
    "vvh_ext_069_pe_depth_below_q10_252d": {"inputs": ["pe"], "func": vvh_ext_069_pe_depth_below_q10_252d},
    "vvh_ext_070_pb_depth_below_q10_252d": {"inputs": ["pb"], "func": vvh_ext_070_pb_depth_below_q10_252d},
    "vvh_ext_071_pe_coef_of_variation_252d": {"inputs": ["pe"], "func": vvh_ext_071_pe_coef_of_variation_252d},
    "vvh_ext_072_pb_iqr_width_252d": {"inputs": ["pb"], "func": vvh_ext_072_pb_iqr_width_252d},
    "vvh_ext_073_cross_multiple_rank_dispersion_252d": {"inputs": ["pe", "pb", "ps"], "func": vvh_ext_073_cross_multiple_rank_dispersion_252d},
    "vvh_ext_074_min_cross_multiple_rank_252d": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vvh_ext_074_min_cross_multiple_rank_252d},
    "vvh_ext_075_extreme_cheapness_composite_252d": {"inputs": ["pe", "pb", "ps", "divyield"], "func": vvh_ext_075_extreme_cheapness_composite_252d},
}
