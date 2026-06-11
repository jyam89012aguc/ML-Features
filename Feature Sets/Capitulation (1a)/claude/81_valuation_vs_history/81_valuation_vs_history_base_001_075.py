"""
81_valuation_vs_history — Base Features 001-100
Domain: statistical positioning of current valuation multiples relative to the
        ticker's own trailing distribution (own-history percentile, z-score,
        range position, distance from trailing min/max, cheapness counts, etc.)
Inputs: daily-frequency Sharadar DAILY/METRICS valuation fields only —
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
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _range_pos(s: pd.Series, w: int) -> pd.Series:
    """Position within rolling range: (s - min) / (max - min)."""
    lo = _rolling_min(s, w)
    hi = _rolling_max(s, w)
    return _safe_div(s - lo, hi - lo)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Percentile rank of PE vs own trailing history ---

def vvh_001_pe_pctrank_252d(pe: pd.Series) -> pd.Series:
    """Percentile rank of current P/E within trailing 252-day window."""
    return _rolling_rank_pct(pe, _TD_YEAR)


def vvh_002_pe_pctrank_504d(pe: pd.Series) -> pd.Series:
    """Percentile rank of current P/E within trailing 504-day (2-year) window."""
    return _rolling_rank_pct(pe, _TD_2Y)


def vvh_003_pe_pctrank_756d(pe: pd.Series) -> pd.Series:
    """Percentile rank of current P/E within trailing 756-day (3-year) window."""
    return _rolling_rank_pct(pe, _TD_3Y)


def vvh_004_pe_pctrank_1260d(pe: pd.Series) -> pd.Series:
    """Percentile rank of current P/E within trailing 1260-day (5-year) window."""
    return _rolling_rank_pct(pe, _TD_5Y)


def vvh_005_pe_pctrank_expanding(pe: pd.Series) -> pd.Series:
    """Expanding (all-history) percentile rank of current P/E."""
    return pe.expanding(min_periods=5).rank(pct=True)


def vvh_006_pb_pctrank_252d(pb: pd.Series) -> pd.Series:
    """Percentile rank of current P/B within trailing 252-day window."""
    return _rolling_rank_pct(pb, _TD_YEAR)


def vvh_007_pb_pctrank_504d(pb: pd.Series) -> pd.Series:
    """Percentile rank of current P/B within trailing 504-day window."""
    return _rolling_rank_pct(pb, _TD_2Y)


def vvh_008_pb_pctrank_1260d(pb: pd.Series) -> pd.Series:
    """Percentile rank of current P/B within trailing 1260-day (5-year) window."""
    return _rolling_rank_pct(pb, _TD_5Y)


def vvh_009_ps_pctrank_252d(ps: pd.Series) -> pd.Series:
    """Percentile rank of current P/S within trailing 252-day window."""
    return _rolling_rank_pct(ps, _TD_YEAR)


def vvh_010_ps_pctrank_1260d(ps: pd.Series) -> pd.Series:
    """Percentile rank of current P/S within trailing 1260-day window."""
    return _rolling_rank_pct(ps, _TD_5Y)


# --- Group B (011-020): Z-scores of multiples vs trailing mean/std ---

def vvh_011_pe_zscore_252d(pe: pd.Series) -> pd.Series:
    """Z-score of P/E vs trailing 252-day mean and std."""
    return _zscore_rolling(pe, _TD_YEAR)


def vvh_012_pe_zscore_504d(pe: pd.Series) -> pd.Series:
    """Z-score of P/E vs trailing 504-day mean and std."""
    return _zscore_rolling(pe, _TD_2Y)


def vvh_013_pe_zscore_1260d(pe: pd.Series) -> pd.Series:
    """Z-score of P/E vs trailing 1260-day mean and std."""
    return _zscore_rolling(pe, _TD_5Y)


def vvh_014_pb_zscore_252d(pb: pd.Series) -> pd.Series:
    """Z-score of P/B vs trailing 252-day mean and std."""
    return _zscore_rolling(pb, _TD_YEAR)


def vvh_015_pb_zscore_1260d(pb: pd.Series) -> pd.Series:
    """Z-score of P/B vs trailing 1260-day mean and std."""
    return _zscore_rolling(pb, _TD_5Y)


def vvh_016_ps_zscore_252d(ps: pd.Series) -> pd.Series:
    """Z-score of P/S vs trailing 252-day mean and std."""
    return _zscore_rolling(ps, _TD_YEAR)


def vvh_017_ps_zscore_1260d(ps: pd.Series) -> pd.Series:
    """Z-score of P/S vs trailing 1260-day mean and std."""
    return _zscore_rolling(ps, _TD_5Y)


def vvh_018_evebitda_zscore_252d(evebitda: pd.Series) -> pd.Series:
    """Z-score of EV/EBITDA vs trailing 252-day mean and std."""
    return _zscore_rolling(evebitda, _TD_YEAR)


def vvh_019_evebitda_zscore_1260d(evebitda: pd.Series) -> pd.Series:
    """Z-score of EV/EBITDA vs trailing 1260-day mean and std."""
    return _zscore_rolling(evebitda, _TD_5Y)


def vvh_020_evebit_zscore_252d(evebit: pd.Series) -> pd.Series:
    """Z-score of EV/EBIT vs trailing 252-day mean and std."""
    return _zscore_rolling(evebit, _TD_YEAR)


# --- Group C (021-030): Range position (x - min)/(max - min) ---

def vvh_021_pe_rangepos_252d(pe: pd.Series) -> pd.Series:
    """P/E position within its trailing 252-day min-max range."""
    return _range_pos(pe, _TD_YEAR)


def vvh_022_pe_rangepos_504d(pe: pd.Series) -> pd.Series:
    """P/E position within its trailing 504-day min-max range."""
    return _range_pos(pe, _TD_2Y)


def vvh_023_pe_rangepos_1260d(pe: pd.Series) -> pd.Series:
    """P/E position within its trailing 1260-day min-max range."""
    return _range_pos(pe, _TD_5Y)


def vvh_024_pb_rangepos_252d(pb: pd.Series) -> pd.Series:
    """P/B position within its trailing 252-day min-max range."""
    return _range_pos(pb, _TD_YEAR)


def vvh_025_pb_rangepos_1260d(pb: pd.Series) -> pd.Series:
    """P/B position within its trailing 1260-day min-max range."""
    return _range_pos(pb, _TD_5Y)


def vvh_026_ps_rangepos_252d(ps: pd.Series) -> pd.Series:
    """P/S position within its trailing 252-day min-max range."""
    return _range_pos(ps, _TD_YEAR)


def vvh_027_ps_rangepos_1260d(ps: pd.Series) -> pd.Series:
    """P/S position within its trailing 1260-day min-max range."""
    return _range_pos(ps, _TD_5Y)


def vvh_028_evebitda_rangepos_252d(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA position within its trailing 252-day min-max range."""
    return _range_pos(evebitda, _TD_YEAR)


def vvh_029_evebitda_rangepos_1260d(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA position within its trailing 1260-day min-max range."""
    return _range_pos(evebitda, _TD_5Y)


def vvh_030_marketcap_rangepos_252d(marketcap: pd.Series) -> pd.Series:
    """Market cap position within its trailing 252-day min-max range."""
    return _range_pos(marketcap, _TD_YEAR)


# --- Group D (031-040): Current multiple as fraction of trailing median/mean ---

def vvh_031_pe_vs_trailing_median_252d(pe: pd.Series) -> pd.Series:
    """P/E as fraction of its trailing 252-day median (1=at median, <1=below)."""
    med = _rolling_median(pe, _TD_YEAR)
    return _safe_div(pe, med)


def vvh_032_pe_vs_trailing_median_1260d(pe: pd.Series) -> pd.Series:
    """P/E as fraction of its trailing 1260-day median."""
    med = _rolling_median(pe, _TD_5Y)
    return _safe_div(pe, med)


def vvh_033_pb_vs_trailing_median_252d(pb: pd.Series) -> pd.Series:
    """P/B as fraction of its trailing 252-day median."""
    med = _rolling_median(pb, _TD_YEAR)
    return _safe_div(pb, med)


def vvh_034_pb_vs_trailing_median_1260d(pb: pd.Series) -> pd.Series:
    """P/B as fraction of its trailing 1260-day median."""
    med = _rolling_median(pb, _TD_5Y)
    return _safe_div(pb, med)


def vvh_035_ps_vs_trailing_mean_252d(ps: pd.Series) -> pd.Series:
    """P/S as fraction of its trailing 252-day mean."""
    return _safe_div(ps, _rolling_mean(ps, _TD_YEAR))


def vvh_036_ps_vs_trailing_mean_1260d(ps: pd.Series) -> pd.Series:
    """P/S as fraction of its trailing 1260-day mean."""
    return _safe_div(ps, _rolling_mean(ps, _TD_5Y))


def vvh_037_evebitda_vs_trailing_median_252d(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA as fraction of its trailing 252-day median."""
    med = _rolling_median(evebitda, _TD_YEAR)
    return _safe_div(evebitda, med)


def vvh_038_evebitda_vs_trailing_median_1260d(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA as fraction of its trailing 1260-day median."""
    med = _rolling_median(evebitda, _TD_5Y)
    return _safe_div(evebitda, med)


def vvh_039_ev_vs_trailing_mean_252d(ev: pd.Series) -> pd.Series:
    """EV as fraction of its trailing 252-day mean."""
    return _safe_div(ev, _rolling_mean(ev, _TD_YEAR))


def vvh_040_marketcap_vs_trailing_mean_252d(marketcap: pd.Series) -> pd.Series:
    """Market cap as fraction of its trailing 252-day mean."""
    return _safe_div(marketcap, _rolling_mean(marketcap, _TD_YEAR))


# --- Group E (041-050): Distance from trailing min (above trough) ---

def vvh_041_pe_dist_from_252d_min(pe: pd.Series) -> pd.Series:
    """P/E percent above trailing 252-day minimum (0=at trough)."""
    lo = _rolling_min(pe, _TD_YEAR)
    return _safe_div(pe - lo, lo.abs())


def vvh_042_pe_dist_from_1260d_min(pe: pd.Series) -> pd.Series:
    """P/E percent above trailing 1260-day minimum."""
    lo = _rolling_min(pe, _TD_5Y)
    return _safe_div(pe - lo, lo.abs())


def vvh_043_pb_dist_from_252d_min(pb: pd.Series) -> pd.Series:
    """P/B percent above trailing 252-day minimum."""
    lo = _rolling_min(pb, _TD_YEAR)
    return _safe_div(pb - lo, lo.abs())


def vvh_044_pb_dist_from_1260d_min(pb: pd.Series) -> pd.Series:
    """P/B percent above trailing 1260-day minimum."""
    lo = _rolling_min(pb, _TD_5Y)
    return _safe_div(pb - lo, lo.abs())


def vvh_045_ps_dist_from_252d_min(ps: pd.Series) -> pd.Series:
    """P/S percent above trailing 252-day minimum."""
    lo = _rolling_min(ps, _TD_YEAR)
    return _safe_div(ps - lo, lo.abs())


def vvh_046_evebitda_dist_from_252d_min(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA percent above trailing 252-day minimum."""
    lo = _rolling_min(evebitda, _TD_YEAR)
    return _safe_div(evebitda - lo, lo.abs())


def vvh_047_evebitda_dist_from_1260d_min(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA percent above trailing 1260-day minimum."""
    lo = _rolling_min(evebitda, _TD_5Y)
    return _safe_div(evebitda - lo, lo.abs())


def vvh_048_ev_dist_from_252d_min(ev: pd.Series) -> pd.Series:
    """EV percent above trailing 252-day minimum."""
    lo = _rolling_min(ev, _TD_YEAR)
    return _safe_div(ev - lo, lo.abs())


def vvh_049_marketcap_dist_from_252d_min(marketcap: pd.Series) -> pd.Series:
    """Market cap percent above trailing 252-day minimum."""
    lo = _rolling_min(marketcap, _TD_YEAR)
    return _safe_div(marketcap - lo, lo.abs())


def vvh_050_divyield_dist_from_252d_max(divyield: pd.Series) -> pd.Series:
    """Div yield distance below trailing 252-day maximum (cheap = high yield)."""
    hi = _rolling_max(divyield, _TD_YEAR)
    return _safe_div(hi - divyield, hi.clip(lower=_EPS))


# --- Group F (051-060): Multi-year low flags and cheapness counters ---

def vvh_051_pe_at_252d_low_flag(pe: pd.Series) -> pd.Series:
    """1 if P/E equals its trailing 252-day minimum, else 0."""
    lo = _rolling_min(pe, _TD_YEAR)
    return (pe <= lo).astype(float)


def vvh_052_pe_at_1260d_low_flag(pe: pd.Series) -> pd.Series:
    """1 if P/E equals its trailing 1260-day (5-year) minimum, else 0."""
    lo = _rolling_min(pe, _TD_5Y)
    return (pe <= lo).astype(float)


def vvh_053_pb_at_252d_low_flag(pb: pd.Series) -> pd.Series:
    """1 if P/B equals its trailing 252-day minimum, else 0."""
    lo = _rolling_min(pb, _TD_YEAR)
    return (pb <= lo).astype(float)


def vvh_054_pb_at_1260d_low_flag(pb: pd.Series) -> pd.Series:
    """1 if P/B equals its trailing 1260-day minimum, else 0."""
    lo = _rolling_min(pb, _TD_5Y)
    return (pb <= lo).astype(float)


def vvh_055_ps_at_1260d_low_flag(ps: pd.Series) -> pd.Series:
    """1 if P/S equals its trailing 1260-day minimum, else 0."""
    lo = _rolling_min(ps, _TD_5Y)
    return (ps <= lo).astype(float)


def vvh_056_evebitda_at_1260d_low_flag(evebitda: pd.Series) -> pd.Series:
    """1 if EV/EBITDA equals its trailing 1260-day minimum, else 0."""
    lo = _rolling_min(evebitda, _TD_5Y)
    return (evebitda <= lo).astype(float)


def vvh_057_pe_cheap_days_252d(pe: pd.Series) -> pd.Series:
    """Count of days in trailing 252-day window where P/E was below its 252d median."""
    med = _rolling_median(pe, _TD_YEAR)
    below = (pe < med).astype(float)
    return _rolling_sum(below, _TD_YEAR)


def vvh_058_pe_cheap_days_1260d(pe: pd.Series) -> pd.Series:
    """Count of days in trailing 1260-day window where P/E was below its 1260d median."""
    med = _rolling_median(pe, _TD_5Y)
    below = (pe < med).astype(float)
    return _rolling_sum(below, _TD_5Y)


def vvh_059_pb_cheap_days_252d(pb: pd.Series) -> pd.Series:
    """Count of days in trailing 252-day window where P/B was below its 252d median."""
    med = _rolling_median(pb, _TD_YEAR)
    below = (pb < med).astype(float)
    return _rolling_sum(below, _TD_YEAR)


def vvh_060_ps_cheap_days_252d(ps: pd.Series) -> pd.Series:
    """Count of days in trailing 252-day window where P/S was below its 252d median."""
    med = _rolling_median(ps, _TD_YEAR)
    below = (ps < med).astype(float)
    return _rolling_sum(below, _TD_YEAR)


# --- Group G (061-075): Cross-metric composite cheapness, expanding stats, log-z ---

def vvh_061_pe_expanding_zscore(pe: pd.Series) -> pd.Series:
    """Expanding (all-history) z-score of P/E (how extreme vs own full history)."""
    m = pe.expanding(min_periods=5).mean()
    sd = pe.expanding(min_periods=5).std()
    return _safe_div(pe - m, sd)


def vvh_062_pb_expanding_zscore(pb: pd.Series) -> pd.Series:
    """Expanding z-score of P/B."""
    m = pb.expanding(min_periods=5).mean()
    sd = pb.expanding(min_periods=5).std()
    return _safe_div(pb - m, sd)


def vvh_063_ps_expanding_zscore(ps: pd.Series) -> pd.Series:
    """Expanding z-score of P/S."""
    m = ps.expanding(min_periods=5).mean()
    sd = ps.expanding(min_periods=5).std()
    return _safe_div(ps - m, sd)


def vvh_064_evebitda_expanding_zscore(evebitda: pd.Series) -> pd.Series:
    """Expanding z-score of EV/EBITDA."""
    m = evebitda.expanding(min_periods=5).mean()
    sd = evebitda.expanding(min_periods=5).std()
    return _safe_div(evebitda - m, sd)


def vvh_065_marketcap_expanding_zscore(marketcap: pd.Series) -> pd.Series:
    """Expanding z-score of market cap."""
    m = marketcap.expanding(min_periods=5).mean()
    sd = marketcap.expanding(min_periods=5).std()
    return _safe_div(marketcap - m, sd)


def vvh_066_log_pe_zscore_252d(pe: pd.Series) -> pd.Series:
    """Z-score of log(P/E) over trailing 252 days (handles skewed distributions)."""
    lpe = _log_safe(pe.clip(lower=_EPS))
    return _zscore_rolling(lpe, _TD_YEAR)


def vvh_067_log_pb_zscore_252d(pb: pd.Series) -> pd.Series:
    """Z-score of log(P/B) over trailing 252 days."""
    lpb = _log_safe(pb.clip(lower=_EPS))
    return _zscore_rolling(lpb, _TD_YEAR)


def vvh_068_log_ps_zscore_252d(ps: pd.Series) -> pd.Series:
    """Z-score of log(P/S) over trailing 252 days."""
    lps = _log_safe(ps.clip(lower=_EPS))
    return _zscore_rolling(lps, _TD_YEAR)


def vvh_069_log_evebitda_zscore_252d(evebitda: pd.Series) -> pd.Series:
    """Z-score of log(EV/EBITDA) over trailing 252 days."""
    lev = _log_safe(evebitda.clip(lower=_EPS))
    return _zscore_rolling(lev, _TD_YEAR)


def vvh_070_composite_cheapness_pe_pb_ps_252d(pe: pd.Series, pb: pd.Series, ps: pd.Series) -> pd.Series:
    """Composite cheapness: average of P/E, P/B, P/S percentile ranks (252d).
    Low score = cheap on all three metrics simultaneously."""
    r_pe = _rolling_rank_pct(pe, _TD_YEAR)
    r_pb = _rolling_rank_pct(pb, _TD_YEAR)
    r_ps = _rolling_rank_pct(ps, _TD_YEAR)
    return (r_pe + r_pb + r_ps) / 3.0


def vvh_071_composite_cheapness_pe_pb_ps_1260d(pe: pd.Series, pb: pd.Series, ps: pd.Series) -> pd.Series:
    """Composite cheapness: average of P/E, P/B, P/S percentile ranks (1260d)."""
    r_pe = _rolling_rank_pct(pe, _TD_5Y)
    r_pb = _rolling_rank_pct(pb, _TD_5Y)
    r_ps = _rolling_rank_pct(ps, _TD_5Y)
    return (r_pe + r_pb + r_ps) / 3.0


def vvh_072_divyield_pctrank_252d(divyield: pd.Series) -> pd.Series:
    """Percentile rank of dividend yield within trailing 252-day window.
    High rank = high yield = relatively cheap income."""
    return _rolling_rank_pct(divyield, _TD_YEAR)


def vvh_073_divyield_pctrank_1260d(divyield: pd.Series) -> pd.Series:
    """Percentile rank of dividend yield within trailing 1260-day window."""
    return _rolling_rank_pct(divyield, _TD_5Y)


def vvh_074_evebit_pctrank_252d(evebit: pd.Series) -> pd.Series:
    """Percentile rank of EV/EBIT within trailing 252-day window."""
    return _rolling_rank_pct(evebit, _TD_YEAR)


def vvh_075_evebit_pctrank_1260d(evebit: pd.Series) -> pd.Series:
    """Percentile rank of EV/EBIT within trailing 1260-day window."""
    return _rolling_rank_pct(evebit, _TD_5Y)


# --- Group H-ext (151-175): Quantile flags, EWM cheapness, log-range, cross-ratio history ---

def vvh_151_pb_below_10th_pctile_252d_flag(pb: pd.Series) -> pd.Series:
    """1 if P/B is at or below 10th percentile of trailing 252-day distribution."""
    q10 = pb.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.10)
    return (pb <= q10).astype(float)


def vvh_152_pb_below_10th_pctile_1260d_flag(pb: pd.Series) -> pd.Series:
    """1 if P/B is at or below 10th percentile of trailing 1260-day distribution."""
    q10 = pb.rolling(_TD_5Y, min_periods=max(1, _TD_5Y // 2)).quantile(0.10)
    return (pb <= q10).astype(float)


def vvh_153_ps_below_10th_pctile_252d_flag(ps: pd.Series) -> pd.Series:
    """1 if P/S is at or below 10th percentile of trailing 252-day distribution."""
    q10 = ps.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.10)
    return (ps <= q10).astype(float)


def vvh_154_evebitda_below_10th_pctile_252d_flag(evebitda: pd.Series) -> pd.Series:
    """1 if EV/EBITDA is at or below 10th percentile of trailing 252-day distribution."""
    q10 = evebitda.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.10)
    return (evebitda <= q10).astype(float)


def vvh_155_pe_above_90th_pctile_252d_flag(pe: pd.Series) -> pd.Series:
    """1 if P/E is at or above 90th percentile of trailing 252-day distribution (expensive)."""
    q90 = pe.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.90)
    return (pe >= q90).astype(float)


def vvh_156_pe_iqr_normalized_252d(pe: pd.Series) -> pd.Series:
    """P/E position within its trailing 252-day IQR, normalized: (pe - Q25) / (Q75 - Q25)."""
    q75 = pe.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.75)
    q25 = pe.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.25)
    return _safe_div(pe - q25, q75 - q25)


def vvh_157_pb_iqr_normalized_252d(pb: pd.Series) -> pd.Series:
    """P/B position within its trailing 252-day IQR: (pb - Q25) / (Q75 - Q25)."""
    q75 = pb.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.75)
    q25 = pb.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.25)
    return _safe_div(pb - q25, q75 - q25)


def vvh_158_pe_ewm_zscore_63(pe: pd.Series) -> pd.Series:
    """Z-score of P/E vs its 63-day EWM mean (short-term deviation from EWM trend)."""
    ewm = _ewm_mean(pe, _TD_QTR)
    sd = _rolling_std(pe, _TD_QTR)
    return _safe_div(pe - ewm, sd)


def vvh_159_pb_ewm_zscore_63(pb: pd.Series) -> pd.Series:
    """Z-score of P/B vs its 63-day EWM mean."""
    ewm = _ewm_mean(pb, _TD_QTR)
    sd = _rolling_std(pb, _TD_QTR)
    return _safe_div(pb - ewm, sd)


def vvh_160_evebitda_ewm_zscore_63(evebitda: pd.Series) -> pd.Series:
    """Z-score of EV/EBITDA vs its 63-day EWM mean."""
    ewm = _ewm_mean(evebitda, _TD_QTR)
    sd = _rolling_std(evebitda, _TD_QTR)
    return _safe_div(evebitda - ewm, sd)


def vvh_161_log_pe_rangepos_1260d(pe: pd.Series) -> pd.Series:
    """Range position of log(P/E) within trailing 1260-day log range."""
    lpe = _log_safe(pe.clip(lower=_EPS))
    return _range_pos(lpe, _TD_5Y)


def vvh_162_log_pb_rangepos_252d(pb: pd.Series) -> pd.Series:
    """Range position of log(P/B) within trailing 252-day log range."""
    lpb = _log_safe(pb.clip(lower=_EPS))
    return _range_pos(lpb, _TD_YEAR)


def vvh_163_log_ps_rangepos_252d(ps: pd.Series) -> pd.Series:
    """Range position of log(P/S) within trailing 252-day log range."""
    lps = _log_safe(ps.clip(lower=_EPS))
    return _range_pos(lps, _TD_YEAR)


def vvh_164_log_evebitda_zscore_1260d(evebitda: pd.Series) -> pd.Series:
    """Z-score of log(EV/EBITDA) over trailing 1260-day window."""
    lev = _log_safe(evebitda.clip(lower=_EPS))
    return _zscore_rolling(lev, _TD_5Y)


def vvh_165_divyield_expanding_pctrank(divyield: pd.Series) -> pd.Series:
    """Expanding (all-history) percentile rank of dividend yield."""
    return divyield.expanding(min_periods=5).rank(pct=True)


def vvh_166_pe_pctrank_half_126d(pe: pd.Series) -> pd.Series:
    """Percentile rank of P/E within trailing 126-day (half-year) window."""
    return _rolling_rank_pct(pe, _TD_HALF)


def vvh_167_pb_pctrank_half_126d(pb: pd.Series) -> pd.Series:
    """Percentile rank of P/B within trailing 126-day window."""
    return _rolling_rank_pct(pb, _TD_HALF)


def vvh_168_ps_pctrank_half_126d(ps: pd.Series) -> pd.Series:
    """Percentile rank of P/S within trailing 126-day window."""
    return _rolling_rank_pct(ps, _TD_HALF)


def vvh_169_evebitda_pctrank_half_126d(evebitda: pd.Series) -> pd.Series:
    """Percentile rank of EV/EBITDA within trailing 126-day window."""
    return _rolling_rank_pct(evebitda, _TD_HALF)


def vvh_170_divyield_at_1260d_high_flag(divyield: pd.Series) -> pd.Series:
    """1 if dividend yield equals its trailing 1260-day maximum (peak cheapness)."""
    hi = _rolling_max(divyield, _TD_5Y)
    return (divyield >= hi).astype(float)


def vvh_171_pe_cheap_days_504d(pe: pd.Series) -> pd.Series:
    """Count of days in trailing 504-day window where P/E was below its 504d median."""
    med = _rolling_median(pe, _TD_2Y)
    below = (pe < med).astype(float)
    return _rolling_sum(below, _TD_2Y)


def vvh_172_evebitda_cheap_days_252d(evebitda: pd.Series) -> pd.Series:
    """Count of days in trailing 252-day window where EV/EBITDA was below its 252d median."""
    med = _rolling_median(evebitda, _TD_YEAR)
    below = (evebitda < med).astype(float)
    return _rolling_sum(below, _TD_YEAR)


def vvh_173_composite_cheapness_5metric_252d(pe: pd.Series, pb: pd.Series, ps: pd.Series, evebitda: pd.Series, divyield: pd.Series) -> pd.Series:
    """Composite cheapness (5 metrics) via mean of cheapness scores (252d).
    divyield cheapness = pctrank (high rank = cheap)."""
    s1 = 1.0 - _rolling_rank_pct(pe, _TD_YEAR)
    s2 = 1.0 - _rolling_rank_pct(pb, _TD_YEAR)
    s3 = 1.0 - _rolling_rank_pct(ps, _TD_YEAR)
    s4 = 1.0 - _rolling_rank_pct(evebitda, _TD_YEAR)
    s5 = _rolling_rank_pct(divyield, _TD_YEAR)
    return (s1 + s2 + s3 + s4 + s5) / 5.0


def vvh_174_ev_expanding_zscore(ev: pd.Series) -> pd.Series:
    """Expanding z-score of EV (how extreme vs own full history)."""
    m = ev.expanding(min_periods=5).mean()
    sd = ev.expanding(min_periods=5).std()
    return _safe_div(ev - m, sd)


def vvh_175_evebit_expanding_pctrank(evebit: pd.Series) -> pd.Series:
    """Expanding (all-history) percentile rank of EV/EBIT."""
    return evebit.expanding(min_periods=5).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

VALUATION_VS_HISTORY_REGISTRY_001_075 = {
    "vvh_001_pe_pctrank_252d": {"inputs": ["pe"], "func": vvh_001_pe_pctrank_252d},
    "vvh_002_pe_pctrank_504d": {"inputs": ["pe"], "func": vvh_002_pe_pctrank_504d},
    "vvh_003_pe_pctrank_756d": {"inputs": ["pe"], "func": vvh_003_pe_pctrank_756d},
    "vvh_004_pe_pctrank_1260d": {"inputs": ["pe"], "func": vvh_004_pe_pctrank_1260d},
    "vvh_005_pe_pctrank_expanding": {"inputs": ["pe"], "func": vvh_005_pe_pctrank_expanding},
    "vvh_006_pb_pctrank_252d": {"inputs": ["pb"], "func": vvh_006_pb_pctrank_252d},
    "vvh_007_pb_pctrank_504d": {"inputs": ["pb"], "func": vvh_007_pb_pctrank_504d},
    "vvh_008_pb_pctrank_1260d": {"inputs": ["pb"], "func": vvh_008_pb_pctrank_1260d},
    "vvh_009_ps_pctrank_252d": {"inputs": ["ps"], "func": vvh_009_ps_pctrank_252d},
    "vvh_010_ps_pctrank_1260d": {"inputs": ["ps"], "func": vvh_010_ps_pctrank_1260d},
    "vvh_011_pe_zscore_252d": {"inputs": ["pe"], "func": vvh_011_pe_zscore_252d},
    "vvh_012_pe_zscore_504d": {"inputs": ["pe"], "func": vvh_012_pe_zscore_504d},
    "vvh_013_pe_zscore_1260d": {"inputs": ["pe"], "func": vvh_013_pe_zscore_1260d},
    "vvh_014_pb_zscore_252d": {"inputs": ["pb"], "func": vvh_014_pb_zscore_252d},
    "vvh_015_pb_zscore_1260d": {"inputs": ["pb"], "func": vvh_015_pb_zscore_1260d},
    "vvh_016_ps_zscore_252d": {"inputs": ["ps"], "func": vvh_016_ps_zscore_252d},
    "vvh_017_ps_zscore_1260d": {"inputs": ["ps"], "func": vvh_017_ps_zscore_1260d},
    "vvh_018_evebitda_zscore_252d": {"inputs": ["evebitda"], "func": vvh_018_evebitda_zscore_252d},
    "vvh_019_evebitda_zscore_1260d": {"inputs": ["evebitda"], "func": vvh_019_evebitda_zscore_1260d},
    "vvh_020_evebit_zscore_252d": {"inputs": ["evebit"], "func": vvh_020_evebit_zscore_252d},
    "vvh_021_pe_rangepos_252d": {"inputs": ["pe"], "func": vvh_021_pe_rangepos_252d},
    "vvh_022_pe_rangepos_504d": {"inputs": ["pe"], "func": vvh_022_pe_rangepos_504d},
    "vvh_023_pe_rangepos_1260d": {"inputs": ["pe"], "func": vvh_023_pe_rangepos_1260d},
    "vvh_024_pb_rangepos_252d": {"inputs": ["pb"], "func": vvh_024_pb_rangepos_252d},
    "vvh_025_pb_rangepos_1260d": {"inputs": ["pb"], "func": vvh_025_pb_rangepos_1260d},
    "vvh_026_ps_rangepos_252d": {"inputs": ["ps"], "func": vvh_026_ps_rangepos_252d},
    "vvh_027_ps_rangepos_1260d": {"inputs": ["ps"], "func": vvh_027_ps_rangepos_1260d},
    "vvh_028_evebitda_rangepos_252d": {"inputs": ["evebitda"], "func": vvh_028_evebitda_rangepos_252d},
    "vvh_029_evebitda_rangepos_1260d": {"inputs": ["evebitda"], "func": vvh_029_evebitda_rangepos_1260d},
    "vvh_030_marketcap_rangepos_252d": {"inputs": ["marketcap"], "func": vvh_030_marketcap_rangepos_252d},
    "vvh_031_pe_vs_trailing_median_252d": {"inputs": ["pe"], "func": vvh_031_pe_vs_trailing_median_252d},
    "vvh_032_pe_vs_trailing_median_1260d": {"inputs": ["pe"], "func": vvh_032_pe_vs_trailing_median_1260d},
    "vvh_033_pb_vs_trailing_median_252d": {"inputs": ["pb"], "func": vvh_033_pb_vs_trailing_median_252d},
    "vvh_034_pb_vs_trailing_median_1260d": {"inputs": ["pb"], "func": vvh_034_pb_vs_trailing_median_1260d},
    "vvh_035_ps_vs_trailing_mean_252d": {"inputs": ["ps"], "func": vvh_035_ps_vs_trailing_mean_252d},
    "vvh_036_ps_vs_trailing_mean_1260d": {"inputs": ["ps"], "func": vvh_036_ps_vs_trailing_mean_1260d},
    "vvh_037_evebitda_vs_trailing_median_252d": {"inputs": ["evebitda"], "func": vvh_037_evebitda_vs_trailing_median_252d},
    "vvh_038_evebitda_vs_trailing_median_1260d": {"inputs": ["evebitda"], "func": vvh_038_evebitda_vs_trailing_median_1260d},
    "vvh_039_ev_vs_trailing_mean_252d": {"inputs": ["ev"], "func": vvh_039_ev_vs_trailing_mean_252d},
    "vvh_040_marketcap_vs_trailing_mean_252d": {"inputs": ["marketcap"], "func": vvh_040_marketcap_vs_trailing_mean_252d},
    "vvh_041_pe_dist_from_252d_min": {"inputs": ["pe"], "func": vvh_041_pe_dist_from_252d_min},
    "vvh_042_pe_dist_from_1260d_min": {"inputs": ["pe"], "func": vvh_042_pe_dist_from_1260d_min},
    "vvh_043_pb_dist_from_252d_min": {"inputs": ["pb"], "func": vvh_043_pb_dist_from_252d_min},
    "vvh_044_pb_dist_from_1260d_min": {"inputs": ["pb"], "func": vvh_044_pb_dist_from_1260d_min},
    "vvh_045_ps_dist_from_252d_min": {"inputs": ["ps"], "func": vvh_045_ps_dist_from_252d_min},
    "vvh_046_evebitda_dist_from_252d_min": {"inputs": ["evebitda"], "func": vvh_046_evebitda_dist_from_252d_min},
    "vvh_047_evebitda_dist_from_1260d_min": {"inputs": ["evebitda"], "func": vvh_047_evebitda_dist_from_1260d_min},
    "vvh_048_ev_dist_from_252d_min": {"inputs": ["ev"], "func": vvh_048_ev_dist_from_252d_min},
    "vvh_049_marketcap_dist_from_252d_min": {"inputs": ["marketcap"], "func": vvh_049_marketcap_dist_from_252d_min},
    "vvh_050_divyield_dist_from_252d_max": {"inputs": ["divyield"], "func": vvh_050_divyield_dist_from_252d_max},
    "vvh_051_pe_at_252d_low_flag": {"inputs": ["pe"], "func": vvh_051_pe_at_252d_low_flag},
    "vvh_052_pe_at_1260d_low_flag": {"inputs": ["pe"], "func": vvh_052_pe_at_1260d_low_flag},
    "vvh_053_pb_at_252d_low_flag": {"inputs": ["pb"], "func": vvh_053_pb_at_252d_low_flag},
    "vvh_054_pb_at_1260d_low_flag": {"inputs": ["pb"], "func": vvh_054_pb_at_1260d_low_flag},
    "vvh_055_ps_at_1260d_low_flag": {"inputs": ["ps"], "func": vvh_055_ps_at_1260d_low_flag},
    "vvh_056_evebitda_at_1260d_low_flag": {"inputs": ["evebitda"], "func": vvh_056_evebitda_at_1260d_low_flag},
    "vvh_057_pe_cheap_days_252d": {"inputs": ["pe"], "func": vvh_057_pe_cheap_days_252d},
    "vvh_058_pe_cheap_days_1260d": {"inputs": ["pe"], "func": vvh_058_pe_cheap_days_1260d},
    "vvh_059_pb_cheap_days_252d": {"inputs": ["pb"], "func": vvh_059_pb_cheap_days_252d},
    "vvh_060_ps_cheap_days_252d": {"inputs": ["ps"], "func": vvh_060_ps_cheap_days_252d},
    "vvh_061_pe_expanding_zscore": {"inputs": ["pe"], "func": vvh_061_pe_expanding_zscore},
    "vvh_062_pb_expanding_zscore": {"inputs": ["pb"], "func": vvh_062_pb_expanding_zscore},
    "vvh_063_ps_expanding_zscore": {"inputs": ["ps"], "func": vvh_063_ps_expanding_zscore},
    "vvh_064_evebitda_expanding_zscore": {"inputs": ["evebitda"], "func": vvh_064_evebitda_expanding_zscore},
    "vvh_065_marketcap_expanding_zscore": {"inputs": ["marketcap"], "func": vvh_065_marketcap_expanding_zscore},
    "vvh_066_log_pe_zscore_252d": {"inputs": ["pe"], "func": vvh_066_log_pe_zscore_252d},
    "vvh_067_log_pb_zscore_252d": {"inputs": ["pb"], "func": vvh_067_log_pb_zscore_252d},
    "vvh_068_log_ps_zscore_252d": {"inputs": ["ps"], "func": vvh_068_log_ps_zscore_252d},
    "vvh_069_log_evebitda_zscore_252d": {"inputs": ["evebitda"], "func": vvh_069_log_evebitda_zscore_252d},
    "vvh_070_composite_cheapness_pe_pb_ps_252d": {"inputs": ["pe", "pb", "ps"], "func": vvh_070_composite_cheapness_pe_pb_ps_252d},
    "vvh_071_composite_cheapness_pe_pb_ps_1260d": {"inputs": ["pe", "pb", "ps"], "func": vvh_071_composite_cheapness_pe_pb_ps_1260d},
    "vvh_072_divyield_pctrank_252d": {"inputs": ["divyield"], "func": vvh_072_divyield_pctrank_252d},
    "vvh_073_divyield_pctrank_1260d": {"inputs": ["divyield"], "func": vvh_073_divyield_pctrank_1260d},
    "vvh_074_evebit_pctrank_252d": {"inputs": ["evebit"], "func": vvh_074_evebit_pctrank_252d},
    "vvh_075_evebit_pctrank_1260d": {"inputs": ["evebit"], "func": vvh_075_evebit_pctrank_1260d},
    "vvh_151_pb_below_10th_pctile_252d_flag": {"inputs": ["pb"], "func": vvh_151_pb_below_10th_pctile_252d_flag},
    "vvh_152_pb_below_10th_pctile_1260d_flag": {"inputs": ["pb"], "func": vvh_152_pb_below_10th_pctile_1260d_flag},
    "vvh_153_ps_below_10th_pctile_252d_flag": {"inputs": ["ps"], "func": vvh_153_ps_below_10th_pctile_252d_flag},
    "vvh_154_evebitda_below_10th_pctile_252d_flag": {"inputs": ["evebitda"], "func": vvh_154_evebitda_below_10th_pctile_252d_flag},
    "vvh_155_pe_above_90th_pctile_252d_flag": {"inputs": ["pe"], "func": vvh_155_pe_above_90th_pctile_252d_flag},
    "vvh_156_pe_iqr_normalized_252d": {"inputs": ["pe"], "func": vvh_156_pe_iqr_normalized_252d},
    "vvh_157_pb_iqr_normalized_252d": {"inputs": ["pb"], "func": vvh_157_pb_iqr_normalized_252d},
    "vvh_158_pe_ewm_zscore_63": {"inputs": ["pe"], "func": vvh_158_pe_ewm_zscore_63},
    "vvh_159_pb_ewm_zscore_63": {"inputs": ["pb"], "func": vvh_159_pb_ewm_zscore_63},
    "vvh_160_evebitda_ewm_zscore_63": {"inputs": ["evebitda"], "func": vvh_160_evebitda_ewm_zscore_63},
    "vvh_161_log_pe_rangepos_1260d": {"inputs": ["pe"], "func": vvh_161_log_pe_rangepos_1260d},
    "vvh_162_log_pb_rangepos_252d": {"inputs": ["pb"], "func": vvh_162_log_pb_rangepos_252d},
    "vvh_163_log_ps_rangepos_252d": {"inputs": ["ps"], "func": vvh_163_log_ps_rangepos_252d},
    "vvh_164_log_evebitda_zscore_1260d": {"inputs": ["evebitda"], "func": vvh_164_log_evebitda_zscore_1260d},
    "vvh_165_divyield_expanding_pctrank": {"inputs": ["divyield"], "func": vvh_165_divyield_expanding_pctrank},
    "vvh_166_pe_pctrank_half_126d": {"inputs": ["pe"], "func": vvh_166_pe_pctrank_half_126d},
    "vvh_167_pb_pctrank_half_126d": {"inputs": ["pb"], "func": vvh_167_pb_pctrank_half_126d},
    "vvh_168_ps_pctrank_half_126d": {"inputs": ["ps"], "func": vvh_168_ps_pctrank_half_126d},
    "vvh_169_evebitda_pctrank_half_126d": {"inputs": ["evebitda"], "func": vvh_169_evebitda_pctrank_half_126d},
    "vvh_170_divyield_at_1260d_high_flag": {"inputs": ["divyield"], "func": vvh_170_divyield_at_1260d_high_flag},
    "vvh_171_pe_cheap_days_504d": {"inputs": ["pe"], "func": vvh_171_pe_cheap_days_504d},
    "vvh_172_evebitda_cheap_days_252d": {"inputs": ["evebitda"], "func": vvh_172_evebitda_cheap_days_252d},
    "vvh_173_composite_cheapness_5metric_252d": {"inputs": ["pe", "pb", "ps", "evebitda", "divyield"], "func": vvh_173_composite_cheapness_5metric_252d},
    "vvh_174_ev_expanding_zscore": {"inputs": ["ev"], "func": vvh_174_ev_expanding_zscore},
    "vvh_175_evebit_expanding_pctrank": {"inputs": ["evebit"], "func": vvh_175_evebit_expanding_pctrank},
}
