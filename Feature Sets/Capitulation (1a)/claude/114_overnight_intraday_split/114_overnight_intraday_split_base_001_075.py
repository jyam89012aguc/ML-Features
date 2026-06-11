"""
114_overnight_intraday_split — Base Features 001-075
Domain: overnight vs intraday return decomposition — cumulative overnight/intraday
        return, share of decline attributable to each session, overnight-gap
        persistence, intraday reversal of overnight moves, session-level distress
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
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
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _overnight_ret(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Overnight return: prior close -> today open (log approximation)."""
    return open_ / close.shift(1) - 1.0


def _intraday_ret(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday return: today open -> today close."""
    return close / open_ - 1.0


def _total_ret(close: pd.Series) -> pd.Series:
    """Total daily return: prior close -> today close."""
    return close.pct_change(1)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Raw overnight and intraday returns ---

def ois_001_overnight_ret(close: pd.Series, open: pd.Series) -> pd.Series:
    """Raw overnight return: prior close to today open."""
    return _overnight_ret(close, open)


def ois_002_intraday_ret(open: pd.Series, close: pd.Series) -> pd.Series:
    """Raw intraday return: today open to today close."""
    return _intraday_ret(open, close)


def ois_003_total_ret(close: pd.Series) -> pd.Series:
    """Total daily return: prior close to today close."""
    return _total_ret(close)


def ois_004_overnight_ret_abs(close: pd.Series, open: pd.Series) -> pd.Series:
    """Absolute value of overnight return."""
    return _overnight_ret(close, open).abs()


def ois_005_intraday_ret_abs(open: pd.Series, close: pd.Series) -> pd.Series:
    """Absolute value of intraday return."""
    return _intraday_ret(open, close).abs()


def ois_006_overnight_vs_total_ratio(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of overnight return to total daily return (overnight share)."""
    on = _overnight_ret(close, open)
    tot = _total_ret(close)
    return _safe_div(on, tot.replace(0, np.nan))


def ois_007_intraday_vs_total_ratio(open: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of intraday return to total daily return (intraday share)."""
    intra = _intraday_ret(open, close)
    tot = close.pct_change(1)
    return _safe_div(intra, tot.replace(0, np.nan))


def ois_008_overnight_ret_sign(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sign of overnight return: +1 gap-up, -1 gap-down, 0 flat."""
    return np.sign(_overnight_ret(close, open)).astype(float)


def ois_009_intraday_ret_sign(open: pd.Series, close: pd.Series) -> pd.Series:
    """Sign of intraday return: +1 up-day, -1 down-day."""
    return np.sign(_intraday_ret(open, close)).astype(float)


def ois_010_overnight_intraday_same_sign(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary flag: overnight and intraday move in the same direction (gap continuation)."""
    on_sign = np.sign(_overnight_ret(close, open))
    intra_sign = np.sign(_intraday_ret(open, close))
    return (on_sign == intra_sign).astype(float)


# --- Group B (011-020): Cumulative overnight and intraday returns ---

def ois_011_cum_overnight_ret_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative overnight return over trailing 5 days."""
    return _rolling_sum(_overnight_ret(close, open), _TD_WEEK)


def ois_012_cum_overnight_ret_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative overnight return over trailing 21 days."""
    return _rolling_sum(_overnight_ret(close, open), _TD_MON)


def ois_013_cum_overnight_ret_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative overnight return over trailing 63 days."""
    return _rolling_sum(_overnight_ret(close, open), _TD_QTR)


def ois_014_cum_overnight_ret_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative overnight return over trailing 252 days."""
    return _rolling_sum(_overnight_ret(close, open), _TD_YEAR)


def ois_015_cum_intraday_ret_5d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative intraday return over trailing 5 days."""
    return _rolling_sum(_intraday_ret(open, close), _TD_WEEK)


def ois_016_cum_intraday_ret_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative intraday return over trailing 21 days."""
    return _rolling_sum(_intraday_ret(open, close), _TD_MON)


def ois_017_cum_intraday_ret_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative intraday return over trailing 63 days."""
    return _rolling_sum(_intraday_ret(open, close), _TD_QTR)


def ois_018_cum_intraday_ret_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative intraday return over trailing 252 days."""
    return _rolling_sum(_intraday_ret(open, close), _TD_YEAR)


def ois_019_cum_overnight_minus_intraday_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Difference: cumulative overnight minus cumulative intraday return (21d)."""
    on = _rolling_sum(_overnight_ret(close, open), _TD_MON)
    intra = _rolling_sum(_intraday_ret(open, close), _TD_MON)
    return on - intra


def ois_020_cum_overnight_minus_intraday_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Difference: cumulative overnight minus cumulative intraday return (63d)."""
    on = _rolling_sum(_overnight_ret(close, open), _TD_QTR)
    intra = _rolling_sum(_intraday_ret(open, close), _TD_QTR)
    return on - intra


# --- Group C (021-030): Overnight/intraday share of total decline ---

def ois_021_overnight_share_cum_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Overnight share of 21-day cumulative decline (overnight_cum / total_cum)."""
    on = _rolling_sum(_overnight_ret(close, open), _TD_MON)
    tot = _rolling_sum(_total_ret(close), _TD_MON)
    return _safe_div(on, tot.replace(0, np.nan))


def ois_022_overnight_share_cum_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Overnight share of 63-day cumulative decline."""
    on = _rolling_sum(_overnight_ret(close, open), _TD_QTR)
    tot = _rolling_sum(_total_ret(close), _TD_QTR)
    return _safe_div(on, tot.replace(0, np.nan))


def ois_023_intraday_share_cum_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Intraday share of 21-day cumulative decline."""
    intra = _rolling_sum(_intraday_ret(open, close), _TD_MON)
    tot = _rolling_sum(_total_ret(close), _TD_MON)
    return _safe_div(intra, tot.replace(0, np.nan))


def ois_024_intraday_share_cum_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Intraday share of 63-day cumulative decline."""
    intra = _rolling_sum(_intraday_ret(open, close), _TD_QTR)
    tot = _rolling_sum(_total_ret(close), _TD_QTR)
    return _safe_div(intra, tot.replace(0, np.nan))


def ois_025_overnight_downside_share_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of negative total days where overnight return was also negative (21d)."""
    on = _overnight_ret(close, open)
    tot = _total_ret(close)
    neg_tot = (tot < 0).astype(float)
    neg_both = ((tot < 0) & (on < 0)).astype(float)
    neg_cnt = _rolling_sum(neg_tot, _TD_MON)
    both_cnt = _rolling_sum(neg_both, _TD_MON)
    return _safe_div(both_cnt, neg_cnt.replace(0, np.nan))


def ois_026_intraday_downside_share_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of negative total days where intraday return was also negative (21d)."""
    intra = _intraday_ret(open, close)
    tot = _total_ret(close)
    neg_tot = (tot < 0).astype(float)
    neg_both = ((tot < 0) & (intra < 0)).astype(float)
    neg_cnt = _rolling_sum(neg_tot, _TD_MON)
    both_cnt = _rolling_sum(neg_both, _TD_MON)
    return _safe_div(both_cnt, neg_cnt.replace(0, np.nan))


def ois_027_overnight_negative_days_frac_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of days with negative overnight return over trailing 21 days."""
    on = _overnight_ret(close, open)
    return _rolling_sum((on < 0).astype(float), _TD_MON) / _TD_MON


def ois_028_intraday_negative_days_frac_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of days with negative intraday return over trailing 21 days."""
    intra = _intraday_ret(open, close)
    return _rolling_sum((intra < 0).astype(float), _TD_MON) / _TD_MON


def ois_029_overnight_negative_days_frac_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of days with negative overnight return over trailing 63 days."""
    on = _overnight_ret(close, open)
    return _rolling_sum((on < 0).astype(float), _TD_QTR) / _TD_QTR


def ois_030_intraday_negative_days_frac_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of days with negative intraday return over trailing 63 days."""
    intra = _intraday_ret(open, close)
    return _rolling_sum((intra < 0).astype(float), _TD_QTR) / _TD_QTR


# --- Group D (031-040): Overnight/intraday volatility split ---

def ois_031_overnight_vol_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling std of overnight returns over 21 days."""
    return _rolling_std(_overnight_ret(close, open), _TD_MON)


def ois_032_intraday_vol_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling std of intraday returns over 21 days."""
    return _rolling_std(_intraday_ret(open, close), _TD_MON)


def ois_033_overnight_vol_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling std of overnight returns over 63 days."""
    return _rolling_std(_overnight_ret(close, open), _TD_QTR)


def ois_034_intraday_vol_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling std of intraday returns over 63 days."""
    return _rolling_std(_intraday_ret(open, close), _TD_QTR)


def ois_035_overnight_vol_fraction_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Overnight vol as fraction of total vol: overnight_std / (overnight_std + intraday_std)."""
    on_vol = _rolling_std(_overnight_ret(close, open), _TD_MON)
    intra_vol = _rolling_std(_intraday_ret(open, close), _TD_MON)
    total_vol = on_vol + intra_vol
    return _safe_div(on_vol, total_vol.replace(0, np.nan))


def ois_036_overnight_vs_intraday_vol_ratio_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of overnight vol to intraday vol over 21 days."""
    on_vol = _rolling_std(_overnight_ret(close, open), _TD_MON)
    intra_vol = _rolling_std(_intraday_ret(open, close), _TD_MON)
    return _safe_div(on_vol, intra_vol.replace(0, np.nan))


def ois_037_overnight_vs_intraday_vol_ratio_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of overnight vol to intraday vol over 63 days."""
    on_vol = _rolling_std(_overnight_ret(close, open), _TD_QTR)
    intra_vol = _rolling_std(_intraday_ret(open, close), _TD_QTR)
    return _safe_div(on_vol, intra_vol.replace(0, np.nan))


def ois_038_total_vol_explained_by_overnight_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Variance fraction explained by overnight: var(overnight)/var(total) over 21d."""
    on = _overnight_ret(close, open)
    tot = _total_ret(close)
    on_var = on.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).var()
    tot_var = tot.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).var()
    return _safe_div(on_var, tot_var.replace(0, np.nan))


def ois_039_overnight_vol_spike_21d_vs_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day overnight vol relative to 252-day overnight vol (vol spike ratio)."""
    on = _overnight_ret(close, open)
    vol_21 = _rolling_std(on, _TD_MON)
    vol_252 = _rolling_std(on, _TD_YEAR)
    return _safe_div(vol_21, vol_252.replace(0, np.nan))


def ois_040_intraday_vol_spike_21d_vs_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """21-day intraday vol relative to 252-day intraday vol (vol spike ratio)."""
    intra = _intraday_ret(open, close)
    vol_21 = _rolling_std(intra, _TD_MON)
    vol_252 = _rolling_std(intra, _TD_YEAR)
    return _safe_div(vol_21, vol_252.replace(0, np.nan))


# --- Group E (041-050): Overnight gap persistence and intraday reversal ---

def ois_041_intraday_reversal_of_overnight_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary flag: intraday return reverses the overnight move (opposite signs)."""
    on = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    return ((np.sign(on) != np.sign(intra)) & (on != 0) & (intra != 0)).astype(float)


def ois_042_intraday_reversal_frac_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of days where intraday reverses overnight over trailing 21 days."""
    rev = ois_041_intraday_reversal_of_overnight_flag(close, open)
    return _rolling_sum(rev, _TD_MON) / _TD_MON


def ois_043_intraday_reversal_frac_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of days where intraday reverses overnight over trailing 63 days."""
    rev = ois_041_intraday_reversal_of_overnight_flag(close, open)
    return _rolling_sum(rev, _TD_QTR) / _TD_QTR


def ois_044_overnight_gap_down_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary flag: today opened below prior close (gap-down day)."""
    return (open < close.shift(1)).astype(float)


def ois_045_overnight_gap_down_frac_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of gap-down opens over trailing 21 days."""
    return _rolling_sum(ois_044_overnight_gap_down_flag(close, open), _TD_MON) / _TD_MON


def ois_046_overnight_gap_down_frac_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of gap-down opens over trailing 63 days."""
    return _rolling_sum(ois_044_overnight_gap_down_flag(close, open), _TD_QTR) / _TD_QTR


def ois_047_overnight_gap_persistence_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of gap-down days where intraday also closed lower (gap not filled, 21d)."""
    on = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    gap_down = on < 0
    persistent = (gap_down & (intra < 0)).astype(float)
    gap_cnt = _rolling_sum(gap_down.astype(float), _TD_MON)
    pers_cnt = _rolling_sum(persistent, _TD_MON)
    return _safe_div(pers_cnt, gap_cnt.replace(0, np.nan))


def ois_048_overnight_gap_fill_frac_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of gap-down days where intraday recovered (gap filled), 21d."""
    on = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    gap_down = on < 0
    filled = (gap_down & (intra > 0)).astype(float)
    gap_cnt = _rolling_sum(gap_down.astype(float), _TD_MON)
    fill_cnt = _rolling_sum(filled, _TD_MON)
    return _safe_div(fill_cnt, gap_cnt.replace(0, np.nan))


def ois_049_intraday_amplifies_overnight_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary flag: intraday return amplifies (same direction) the overnight move."""
    on = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    return ((np.sign(on) == np.sign(intra)) & (on != 0) & (intra != 0)).astype(float)


def ois_050_intraday_amplification_frac_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of days where intraday amplifies overnight over 21 days."""
    amp = ois_049_intraday_amplifies_overnight_flag(close, open)
    return _rolling_sum(amp, _TD_MON) / _TD_MON


# --- Group F (051-060): Which session carries the distress ---

def ois_051_overnight_down_consec(close: pd.Series, open: pd.Series) -> pd.Series:
    """Consecutive days of negative overnight return (gap-down streak)."""
    on = _overnight_ret(close, open)
    return _consec_streak(on < 0)


def ois_052_intraday_down_consec(open: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive days of negative intraday return (intraday sell streak)."""
    intra = _intraday_ret(open, close)
    return _consec_streak(intra < 0)


def ois_053_both_sessions_down_consec(close: pd.Series, open: pd.Series) -> pd.Series:
    """Consecutive days where both overnight and intraday returns are negative."""
    on = _overnight_ret(close, open)
    intra = _intraday_ret(open, close)
    return _consec_streak((on < 0) & (intra < 0))


def ois_054_overnight_cum_ret_21d_below_zero_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary flag: 21-day cumulative overnight return is negative."""
    return (_rolling_sum(_overnight_ret(close, open), _TD_MON) < 0).astype(float)


def ois_055_intraday_cum_ret_21d_below_zero_flag(open: pd.Series, close: pd.Series) -> pd.Series:
    """Binary flag: 21-day cumulative intraday return is negative."""
    return (_rolling_sum(_intraday_ret(open, close), _TD_MON) < 0).astype(float)


def ois_056_overnight_distress_score_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of negative overnight returns only (overnight distress intensity, 21d)."""
    on = _overnight_ret(close, open)
    return _rolling_sum(on.clip(upper=0.0), _TD_MON)


def ois_057_intraday_distress_score_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of negative intraday returns only (intraday distress intensity, 21d)."""
    intra = _intraday_ret(open, close)
    return _rolling_sum(intra.clip(upper=0.0), _TD_MON)


def ois_058_overnight_distress_score_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of negative overnight returns only (overnight distress intensity, 63d)."""
    on = _overnight_ret(close, open)
    return _rolling_sum(on.clip(upper=0.0), _TD_QTR)


def ois_059_intraday_distress_score_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of negative intraday returns only (intraday distress intensity, 63d)."""
    intra = _intraday_ret(open, close)
    return _rolling_sum(intra.clip(upper=0.0), _TD_QTR)


def ois_060_dominant_session_distress_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Which session dominates distress: +1 overnight worse, -1 intraday worse, 0 equal (21d)."""
    on_dist = _rolling_sum(_overnight_ret(close, open).clip(upper=0.0), _TD_MON)
    intra_dist = _rolling_sum(_intraday_ret(open, close).clip(upper=0.0), _TD_MON)
    return np.sign(intra_dist - on_dist).astype(float)


# --- Group G (061-075): Z-scores, percentile ranks, rolling minima ---

def ois_061_overnight_ret_zscore_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of overnight return vs 63-day distribution."""
    on = _overnight_ret(close, open)
    m = _rolling_mean(on, _TD_QTR)
    s = _rolling_std(on, _TD_QTR)
    return _safe_div(on - m, s)


def ois_062_intraday_ret_zscore_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of intraday return vs 63-day distribution."""
    intra = _intraday_ret(open, close)
    m = _rolling_mean(intra, _TD_QTR)
    s = _rolling_std(intra, _TD_QTR)
    return _safe_div(intra - m, s)


def ois_063_overnight_ret_zscore_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of overnight return vs 252-day distribution."""
    on = _overnight_ret(close, open)
    m = _rolling_mean(on, _TD_YEAR)
    s = _rolling_std(on, _TD_YEAR)
    return _safe_div(on - m, s)


def ois_064_intraday_ret_zscore_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of intraday return vs 252-day distribution."""
    intra = _intraday_ret(open, close)
    m = _rolling_mean(intra, _TD_YEAR)
    s = _rolling_std(intra, _TD_YEAR)
    return _safe_div(intra - m, s)


def ois_065_overnight_ret_pct_rank_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of overnight return within 63-day distribution."""
    on = _overnight_ret(close, open)
    return on.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def ois_066_intraday_ret_pct_rank_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of intraday return within 63-day distribution."""
    intra = _intraday_ret(open, close)
    return intra.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def ois_067_overnight_ret_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of overnight return within 252-day distribution."""
    on = _overnight_ret(close, open)
    return on.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def ois_068_intraday_ret_pct_rank_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of intraday return within 252-day distribution."""
    intra = _intraday_ret(open, close)
    return intra.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def ois_069_cum_overnight_ret_21d_min_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 63-day minimum of 21-day cumulative overnight return."""
    cum = _rolling_sum(_overnight_ret(close, open), _TD_MON)
    return _rolling_min(cum, _TD_QTR)


def ois_070_cum_intraday_ret_21d_min_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63-day minimum of 21-day cumulative intraday return."""
    cum = _rolling_sum(_intraday_ret(open, close), _TD_MON)
    return _rolling_min(cum, _TD_QTR)


def ois_071_overnight_vol_zscore_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of 21d overnight vol vs its 252-day distribution."""
    on = _overnight_ret(close, open)
    vol21 = _rolling_std(on, _TD_MON)
    m = _rolling_mean(vol21, _TD_YEAR)
    s = _rolling_std(vol21, _TD_YEAR)
    return _safe_div(vol21 - m, s)


def ois_072_intraday_vol_zscore_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 21d intraday vol vs its 252-day distribution."""
    intra = _intraday_ret(open, close)
    vol21 = _rolling_std(intra, _TD_MON)
    m = _rolling_mean(vol21, _TD_YEAR)
    s = _rolling_std(vol21, _TD_YEAR)
    return _safe_div(vol21 - m, s)


def ois_073_overnight_gap_size_mean_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Mean absolute overnight gap size over trailing 21 days."""
    return _rolling_mean(_overnight_ret(close, open).abs(), _TD_MON)


def ois_074_intraday_range_mean_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Mean absolute intraday return over trailing 21 days."""
    return _rolling_mean(_intraday_ret(open, close).abs(), _TD_MON)


def ois_075_overnight_to_intraday_distress_ratio_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of overnight distress to intraday distress over 63 days (absolute values)."""
    on_dist = _rolling_sum(_overnight_ret(close, open).clip(upper=0.0).abs(), _TD_QTR)
    intra_dist = _rolling_sum(_intraday_ret(open, close).clip(upper=0.0).abs(), _TD_QTR)
    return _safe_div(on_dist, intra_dist.replace(0, np.nan))


# ── Registry ──────────────────────────────────────────────────────────────────

OVERNIGHT_INTRADAY_SPLIT_REGISTRY_001_075 = {
    "ois_001_overnight_ret": {"inputs": ["close", "open"], "func": ois_001_overnight_ret},
    "ois_002_intraday_ret": {"inputs": ["open", "close"], "func": ois_002_intraday_ret},
    "ois_003_total_ret": {"inputs": ["close"], "func": ois_003_total_ret},
    "ois_004_overnight_ret_abs": {"inputs": ["close", "open"], "func": ois_004_overnight_ret_abs},
    "ois_005_intraday_ret_abs": {"inputs": ["open", "close"], "func": ois_005_intraday_ret_abs},
    "ois_006_overnight_vs_total_ratio": {"inputs": ["close", "open"], "func": ois_006_overnight_vs_total_ratio},
    "ois_007_intraday_vs_total_ratio": {"inputs": ["open", "close"], "func": ois_007_intraday_vs_total_ratio},
    "ois_008_overnight_ret_sign": {"inputs": ["close", "open"], "func": ois_008_overnight_ret_sign},
    "ois_009_intraday_ret_sign": {"inputs": ["open", "close"], "func": ois_009_intraday_ret_sign},
    "ois_010_overnight_intraday_same_sign": {"inputs": ["close", "open"], "func": ois_010_overnight_intraday_same_sign},
    "ois_011_cum_overnight_ret_5d": {"inputs": ["close", "open"], "func": ois_011_cum_overnight_ret_5d},
    "ois_012_cum_overnight_ret_21d": {"inputs": ["close", "open"], "func": ois_012_cum_overnight_ret_21d},
    "ois_013_cum_overnight_ret_63d": {"inputs": ["close", "open"], "func": ois_013_cum_overnight_ret_63d},
    "ois_014_cum_overnight_ret_252d": {"inputs": ["close", "open"], "func": ois_014_cum_overnight_ret_252d},
    "ois_015_cum_intraday_ret_5d": {"inputs": ["open", "close"], "func": ois_015_cum_intraday_ret_5d},
    "ois_016_cum_intraday_ret_21d": {"inputs": ["open", "close"], "func": ois_016_cum_intraday_ret_21d},
    "ois_017_cum_intraday_ret_63d": {"inputs": ["open", "close"], "func": ois_017_cum_intraday_ret_63d},
    "ois_018_cum_intraday_ret_252d": {"inputs": ["open", "close"], "func": ois_018_cum_intraday_ret_252d},
    "ois_019_cum_overnight_minus_intraday_21d": {"inputs": ["close", "open"], "func": ois_019_cum_overnight_minus_intraday_21d},
    "ois_020_cum_overnight_minus_intraday_63d": {"inputs": ["close", "open"], "func": ois_020_cum_overnight_minus_intraday_63d},
    "ois_021_overnight_share_cum_21d": {"inputs": ["close", "open"], "func": ois_021_overnight_share_cum_21d},
    "ois_022_overnight_share_cum_63d": {"inputs": ["close", "open"], "func": ois_022_overnight_share_cum_63d},
    "ois_023_intraday_share_cum_21d": {"inputs": ["close", "open"], "func": ois_023_intraday_share_cum_21d},
    "ois_024_intraday_share_cum_63d": {"inputs": ["close", "open"], "func": ois_024_intraday_share_cum_63d},
    "ois_025_overnight_downside_share_21d": {"inputs": ["close", "open"], "func": ois_025_overnight_downside_share_21d},
    "ois_026_intraday_downside_share_21d": {"inputs": ["close", "open"], "func": ois_026_intraday_downside_share_21d},
    "ois_027_overnight_negative_days_frac_21d": {"inputs": ["close", "open"], "func": ois_027_overnight_negative_days_frac_21d},
    "ois_028_intraday_negative_days_frac_21d": {"inputs": ["open", "close"], "func": ois_028_intraday_negative_days_frac_21d},
    "ois_029_overnight_negative_days_frac_63d": {"inputs": ["close", "open"], "func": ois_029_overnight_negative_days_frac_63d},
    "ois_030_intraday_negative_days_frac_63d": {"inputs": ["open", "close"], "func": ois_030_intraday_negative_days_frac_63d},
    "ois_031_overnight_vol_21d": {"inputs": ["close", "open"], "func": ois_031_overnight_vol_21d},
    "ois_032_intraday_vol_21d": {"inputs": ["open", "close"], "func": ois_032_intraday_vol_21d},
    "ois_033_overnight_vol_63d": {"inputs": ["close", "open"], "func": ois_033_overnight_vol_63d},
    "ois_034_intraday_vol_63d": {"inputs": ["open", "close"], "func": ois_034_intraday_vol_63d},
    "ois_035_overnight_vol_fraction_21d": {"inputs": ["close", "open"], "func": ois_035_overnight_vol_fraction_21d},
    "ois_036_overnight_vs_intraday_vol_ratio_21d": {"inputs": ["close", "open"], "func": ois_036_overnight_vs_intraday_vol_ratio_21d},
    "ois_037_overnight_vs_intraday_vol_ratio_63d": {"inputs": ["close", "open"], "func": ois_037_overnight_vs_intraday_vol_ratio_63d},
    "ois_038_total_vol_explained_by_overnight_21d": {"inputs": ["close", "open"], "func": ois_038_total_vol_explained_by_overnight_21d},
    "ois_039_overnight_vol_spike_21d_vs_252d": {"inputs": ["close", "open"], "func": ois_039_overnight_vol_spike_21d_vs_252d},
    "ois_040_intraday_vol_spike_21d_vs_252d": {"inputs": ["open", "close"], "func": ois_040_intraday_vol_spike_21d_vs_252d},
    "ois_041_intraday_reversal_of_overnight_flag": {"inputs": ["close", "open"], "func": ois_041_intraday_reversal_of_overnight_flag},
    "ois_042_intraday_reversal_frac_21d": {"inputs": ["close", "open"], "func": ois_042_intraday_reversal_frac_21d},
    "ois_043_intraday_reversal_frac_63d": {"inputs": ["close", "open"], "func": ois_043_intraday_reversal_frac_63d},
    "ois_044_overnight_gap_down_flag": {"inputs": ["close", "open"], "func": ois_044_overnight_gap_down_flag},
    "ois_045_overnight_gap_down_frac_21d": {"inputs": ["close", "open"], "func": ois_045_overnight_gap_down_frac_21d},
    "ois_046_overnight_gap_down_frac_63d": {"inputs": ["close", "open"], "func": ois_046_overnight_gap_down_frac_63d},
    "ois_047_overnight_gap_persistence_21d": {"inputs": ["close", "open"], "func": ois_047_overnight_gap_persistence_21d},
    "ois_048_overnight_gap_fill_frac_21d": {"inputs": ["close", "open"], "func": ois_048_overnight_gap_fill_frac_21d},
    "ois_049_intraday_amplifies_overnight_flag": {"inputs": ["close", "open"], "func": ois_049_intraday_amplifies_overnight_flag},
    "ois_050_intraday_amplification_frac_21d": {"inputs": ["close", "open"], "func": ois_050_intraday_amplification_frac_21d},
    "ois_051_overnight_down_consec": {"inputs": ["close", "open"], "func": ois_051_overnight_down_consec},
    "ois_052_intraday_down_consec": {"inputs": ["open", "close"], "func": ois_052_intraday_down_consec},
    "ois_053_both_sessions_down_consec": {"inputs": ["close", "open"], "func": ois_053_both_sessions_down_consec},
    "ois_054_overnight_cum_ret_21d_below_zero_flag": {"inputs": ["close", "open"], "func": ois_054_overnight_cum_ret_21d_below_zero_flag},
    "ois_055_intraday_cum_ret_21d_below_zero_flag": {"inputs": ["open", "close"], "func": ois_055_intraday_cum_ret_21d_below_zero_flag},
    "ois_056_overnight_distress_score_21d": {"inputs": ["close", "open"], "func": ois_056_overnight_distress_score_21d},
    "ois_057_intraday_distress_score_21d": {"inputs": ["open", "close"], "func": ois_057_intraday_distress_score_21d},
    "ois_058_overnight_distress_score_63d": {"inputs": ["close", "open"], "func": ois_058_overnight_distress_score_63d},
    "ois_059_intraday_distress_score_63d": {"inputs": ["open", "close"], "func": ois_059_intraday_distress_score_63d},
    "ois_060_dominant_session_distress_21d": {"inputs": ["close", "open"], "func": ois_060_dominant_session_distress_21d},
    "ois_061_overnight_ret_zscore_63d": {"inputs": ["close", "open"], "func": ois_061_overnight_ret_zscore_63d},
    "ois_062_intraday_ret_zscore_63d": {"inputs": ["open", "close"], "func": ois_062_intraday_ret_zscore_63d},
    "ois_063_overnight_ret_zscore_252d": {"inputs": ["close", "open"], "func": ois_063_overnight_ret_zscore_252d},
    "ois_064_intraday_ret_zscore_252d": {"inputs": ["open", "close"], "func": ois_064_intraday_ret_zscore_252d},
    "ois_065_overnight_ret_pct_rank_63d": {"inputs": ["close", "open"], "func": ois_065_overnight_ret_pct_rank_63d},
    "ois_066_intraday_ret_pct_rank_63d": {"inputs": ["open", "close"], "func": ois_066_intraday_ret_pct_rank_63d},
    "ois_067_overnight_ret_pct_rank_252d": {"inputs": ["close", "open"], "func": ois_067_overnight_ret_pct_rank_252d},
    "ois_068_intraday_ret_pct_rank_252d": {"inputs": ["open", "close"], "func": ois_068_intraday_ret_pct_rank_252d},
    "ois_069_cum_overnight_ret_21d_min_63d": {"inputs": ["close", "open"], "func": ois_069_cum_overnight_ret_21d_min_63d},
    "ois_070_cum_intraday_ret_21d_min_63d": {"inputs": ["open", "close"], "func": ois_070_cum_intraday_ret_21d_min_63d},
    "ois_071_overnight_vol_zscore_252d": {"inputs": ["close", "open"], "func": ois_071_overnight_vol_zscore_252d},
    "ois_072_intraday_vol_zscore_252d": {"inputs": ["open", "close"], "func": ois_072_intraday_vol_zscore_252d},
    "ois_073_overnight_gap_size_mean_21d": {"inputs": ["close", "open"], "func": ois_073_overnight_gap_size_mean_21d},
    "ois_074_intraday_range_mean_21d": {"inputs": ["open", "close"], "func": ois_074_intraday_range_mean_21d},
    "ois_075_overnight_to_intraday_distress_ratio_63d": {"inputs": ["close", "open"], "func": ois_075_overnight_to_intraday_distress_ratio_63d},
}
