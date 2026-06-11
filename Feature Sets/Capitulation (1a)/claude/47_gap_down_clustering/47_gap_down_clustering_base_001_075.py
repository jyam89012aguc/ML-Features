"""
47_gap_down_clustering — Base Features 001-075
Domain: clustered down-gaps and gap streaks — consecutive down-gap runs, count/density of
down-gaps in trailing windows, cumulative gap magnitude, inter-gap timing, cluster recency,
accelerating gap sequences, breakaway/continuation gap patterns, and island reversal detection.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Island reversal: a gap DOWN into a price cluster followed by a gap UP out of it leaves bars
stranded as an "island." Confirmed using only trailing (past) data — the confirming gap-up
has already occurred before the signal fires.
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


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _consec_streak(cond: pd.Series) -> pd.Series:
    """
    Count consecutive True values up to each row (backward-looking).
    Uses cumsum-group trick: each False increments the group counter;
    within a True group, cumsum gives the run length.
    Returns 0 on False rows and the current streak length on True rows.
    """
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond: pd.Series, w: int) -> pd.Series:
    """Maximum consecutive-True run length over trailing w periods (scalar apply)."""
    def _max_run(arr):
        mx = 0
        cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return cond.rolling(w, min_periods=max(1, w // 2)).apply(_max_run, raw=True)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _down_gap(close: pd.Series, open: pd.Series) -> pd.Series:
    """Boolean: today's open < prior close (down-gap day)."""
    return open < close.shift(1)


def _down_gap_size(close: pd.Series, open: pd.Series) -> pd.Series:
    """Raw down-gap magnitude: prior_close - open (zero on non-gap days)."""
    raw = close.shift(1) - open
    return raw.clip(lower=0.0)


def _down_gap_pct(close: pd.Series, open: pd.Series) -> pd.Series:
    """Down-gap as a fraction of prior close (zero on non-gap days)."""
    size = _down_gap_size(close, open)
    return _safe_div(size, close.shift(1).replace(0, np.nan))


def _up_gap(close: pd.Series, open: pd.Series) -> pd.Series:
    """Boolean: today's open > prior close (up-gap day)."""
    return open > close.shift(1)


def _up_gap_pct(close: pd.Series, open: pd.Series) -> pd.Series:
    """Up-gap as a fraction of prior close (zero on non-gap days)."""
    raw = (open - close.shift(1)).clip(lower=0.0)
    return _safe_div(raw, close.shift(1).replace(0, np.nan))


# ── Island reversal helpers ───────────────────────────────────────────────────

def _island_bottom_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Backward-looking island-bottom flag: fired on day T when:
      - Day T-k (some past day) had a gap DOWN (open[T-k] < close[T-k-1])
      - The island body spanned k days (k >= 1)
      - Day T has a gap UP (open[T] > close[T-1])
    We use k=1 through k=5 (islands up to 5 bars wide).
    On the day the confirming gap-up occurs, the signal fires (no look-ahead).
    Returns 1.0 on days that complete an island-bottom pattern.
    """
    dg = _down_gap(close, open)       # down-gap flag at each bar
    ug = _up_gap(close, open)         # up-gap flag at each bar
    # An island bottom completes today if today is a gap-up AND
    # the entry gap-down occurred 1 to 5 bars ago.
    result = pd.Series(0.0, index=close.index)
    for lag in range(1, 6):
        entry_gap = dg.shift(lag, fill_value=False)
        result = result + (ug & entry_gap).astype(float)
    # clip to binary
    return result.clip(upper=1.0)


def _island_bottom_width(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Width (bars) of the island that just completed on each bar where
    _island_bottom_flag==1. The width is the lag (1-5) of the entry gap-down.
    Returns 0 on non-island days.
    """
    dg = _down_gap(close, open)
    ug = _up_gap(close, open)
    result = pd.Series(0.0, index=close.index)
    for lag in range(1, 6):
        entry_gap = dg.shift(lag, fill_value=False)
        mask = (ug & entry_gap & (result == 0.0))
        result = result.where(~mask, float(lag))
    return result


def _island_top_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Island-top flag: fired on day T when today is a gap-DOWN and
    the entry gap-up occurred 1-5 bars ago. Completeness-first, no look-ahead.
    """
    dg = _down_gap(close, open)
    ug = _up_gap(close, open)
    result = pd.Series(0.0, index=close.index)
    for lag in range(1, 6):
        entry_gap = ug.shift(lag, fill_value=False)
        result = result + (dg & entry_gap).astype(float)
    return result.clip(upper=1.0)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Current consecutive down-gap streak ---

def gdc_001_consec_gap_down_current(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current run of consecutive days with a down-gap open (open < prior close)."""
    return _consec_streak(_down_gap(close, open))


def gdc_002_consec_gap_down_current_log(close: pd.Series, open: pd.Series) -> pd.Series:
    """Log1p of current consecutive down-gap streak (compresses long tails)."""
    return np.log1p(gdc_001_consec_gap_down_current(close, open))


def gdc_003_consec_gap_down_norm_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current down-gap streak normalized by its 21-day rolling average."""
    streak = gdc_001_consec_gap_down_current(close, open)
    return _safe_div(streak, _rolling_mean(streak, _TD_MON))


def gdc_004_consec_gap_down_norm_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current down-gap streak normalized by its 63-day rolling average."""
    streak = gdc_001_consec_gap_down_current(close, open)
    return _safe_div(streak, _rolling_mean(streak, _TD_QTR))


def gdc_005_consec_gap_down_norm_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current down-gap streak normalized by its 252-day rolling average."""
    streak = gdc_001_consec_gap_down_current(close, open)
    return _safe_div(streak, _rolling_mean(streak, _TD_YEAR))


def gdc_006_consec_gap_down_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of current down-gap streak within trailing 252 days."""
    streak = gdc_001_consec_gap_down_current(close, open)
    return streak.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def gdc_007_consec_gap_down_ge2_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary flag: current consecutive down-gap streak >= 2."""
    return (gdc_001_consec_gap_down_current(close, open) >= 2).astype(float)


def gdc_008_consec_gap_down_ge3_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary flag: current consecutive down-gap streak >= 3."""
    return (gdc_001_consec_gap_down_current(close, open) >= 3).astype(float)


def gdc_009_consec_gap_down_ge5_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary flag: current consecutive down-gap streak >= 5 (full week of gaps)."""
    return (gdc_001_consec_gap_down_current(close, open) >= 5).astype(float)


def gdc_010_consec_gap_down_expanding_max(close: pd.Series, open: pd.Series) -> pd.Series:
    """Expanding all-time maximum consecutive down-gap streak."""
    streak = gdc_001_consec_gap_down_current(close, open)
    return streak.expanding(min_periods=1).max()


# --- Group B (011-020): Max consecutive down-gap streak in rolling windows ---

def gdc_011_max_gap_down_streak_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum consecutive down-gap streak within trailing 5 days."""
    return _rolling_max_streak(_down_gap(close, open), _TD_WEEK)


def gdc_012_max_gap_down_streak_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum consecutive down-gap streak within trailing 21 days."""
    return _rolling_max_streak(_down_gap(close, open), _TD_MON)


def gdc_013_max_gap_down_streak_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum consecutive down-gap streak within trailing 63 days."""
    return _rolling_max_streak(_down_gap(close, open), _TD_QTR)


def gdc_014_max_gap_down_streak_126d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum consecutive down-gap streak within trailing 126 days."""
    return _rolling_max_streak(_down_gap(close, open), _TD_HALF)


def gdc_015_max_gap_down_streak_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum consecutive down-gap streak within trailing 252 days."""
    return _rolling_max_streak(_down_gap(close, open), _TD_YEAR)


def gdc_016_current_vs_max_gap_streak_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current down-gap streak as fraction of 63-day max down-gap streak."""
    cur = gdc_001_consec_gap_down_current(close, open)
    mx = gdc_013_max_gap_down_streak_63d(close, open)
    return _safe_div(cur, mx)


def gdc_017_current_vs_max_gap_streak_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current down-gap streak as fraction of 252-day max down-gap streak."""
    cur = gdc_001_consec_gap_down_current(close, open)
    mx = gdc_015_max_gap_down_streak_252d(close, open)
    return _safe_div(cur, mx)


def gdc_018_max_gap_streak_21d_vs_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of 21-day max gap streak to 252-day max gap streak (recent intensity)."""
    return _safe_div(
        gdc_012_max_gap_down_streak_21d(close, open),
        gdc_015_max_gap_down_streak_252d(close, open),
    )


def gdc_019_max_gap_streak_63d_vs_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of 63-day max gap streak to 252-day max gap streak."""
    return _safe_div(
        gdc_013_max_gap_down_streak_63d(close, open),
        gdc_015_max_gap_down_streak_252d(close, open),
    )


def gdc_020_max_gap_streak_252d_expanding_rank(close: pd.Series, open: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252-day max down-gap streak (all-history)."""
    mx = gdc_015_max_gap_down_streak_252d(close, open)
    return mx.expanding(min_periods=5).rank(pct=True)


# --- Group C (021-030): Down-gap count in trailing windows ---

def gdc_021_gap_down_count_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of down-gap days in the trailing 5 trading days."""
    return _rolling_count_true(_down_gap(close, open), _TD_WEEK)


def gdc_022_gap_down_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of down-gap days in the trailing 21 trading days."""
    return _rolling_count_true(_down_gap(close, open), _TD_MON)


def gdc_023_gap_down_count_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of down-gap days in the trailing 63 trading days."""
    return _rolling_count_true(_down_gap(close, open), _TD_QTR)


def gdc_024_gap_down_count_126d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of down-gap days in the trailing 126 trading days."""
    return _rolling_count_true(_down_gap(close, open), _TD_HALF)


def gdc_025_gap_down_count_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of down-gap days in the trailing 252 trading days."""
    return _rolling_count_true(_down_gap(close, open), _TD_YEAR)


def gdc_026_gap_down_fraction_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of the last 5 days that had a down-gap open."""
    return gdc_021_gap_down_count_5d(close, open) / _TD_WEEK


def gdc_027_gap_down_fraction_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of the last 21 days that had a down-gap open."""
    return gdc_022_gap_down_count_21d(close, open) / _TD_MON


def gdc_028_gap_down_fraction_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of the last 63 days that had a down-gap open."""
    return gdc_023_gap_down_count_63d(close, open) / _TD_QTR


def gdc_029_gap_down_fraction_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of the last 252 days that had a down-gap open."""
    return gdc_025_gap_down_count_252d(close, open) / _TD_YEAR


def gdc_030_gap_down_count_5d_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of 5-day down-gap count within trailing 252 days."""
    cnt = gdc_021_gap_down_count_5d(close, open)
    return cnt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group D (031-040): Down-gap magnitude clustering ---

def gdc_031_cum_gap_down_size_current_streak(close: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative down-gap magnitude (in points) over the current consecutive gap streak."""
    size = _down_gap_size(close, open)
    cond = _down_gap(close, open)
    group = (~cond).cumsum()
    return size.groupby(group).cumsum().where(cond, 0.0)


def gdc_032_cum_gap_down_pct_current_streak(close: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative down-gap percentage over the current consecutive gap streak."""
    pct = _down_gap_pct(close, open)
    cond = _down_gap(close, open)
    group = (~cond).cumsum()
    return pct.groupby(group).cumsum().where(cond, 0.0)


def gdc_033_avg_gap_down_size_current_streak(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average per-day down-gap size over the current consecutive gap streak."""
    cum = gdc_031_cum_gap_down_size_current_streak(close, open)
    length = gdc_001_consec_gap_down_current(close, open)
    return _safe_div(cum, length)


def gdc_034_sum_gap_down_pct_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of down-gap percentage magnitudes over trailing 21 days."""
    return _rolling_sum(_down_gap_pct(close, open), _TD_MON)


def gdc_035_sum_gap_down_pct_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of down-gap percentage magnitudes over trailing 63 days."""
    return _rolling_sum(_down_gap_pct(close, open), _TD_QTR)


def gdc_036_sum_gap_down_pct_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of down-gap percentage magnitudes over trailing 252 days."""
    return _rolling_sum(_down_gap_pct(close, open), _TD_YEAR)


def gdc_037_avg_gap_down_pct_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average down-gap pct on gap days over trailing 21 days."""
    pct = _down_gap_pct(close, open)
    cond = _down_gap(close, open)
    return pct.where(cond, np.nan).rolling(_TD_MON, min_periods=1).mean()


def gdc_038_avg_gap_down_pct_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average down-gap pct on gap days over trailing 63 days."""
    pct = _down_gap_pct(close, open)
    cond = _down_gap(close, open)
    return pct.where(cond, np.nan).rolling(_TD_QTR, min_periods=1).mean()


def gdc_039_max_gap_down_pct_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum single-day down-gap percentage within trailing 21 days."""
    return _rolling_max(_down_gap_pct(close, open), _TD_MON)


def gdc_040_max_gap_down_pct_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum single-day down-gap percentage within trailing 63 days."""
    return _rolling_max(_down_gap_pct(close, open), _TD_QTR)


# --- Group E (041-050): Down-gap density and clustering metrics ---

def gdc_041_gap_down_density_5in21(close: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: 5 or more down-gap days within the last 21 days (dense cluster)."""
    return (gdc_022_gap_down_count_21d(close, open) >= 5).astype(float)


def gdc_042_gap_down_density_10in21(close: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: 10 or more down-gap days within the last 21 days (extreme cluster)."""
    return (gdc_022_gap_down_count_21d(close, open) >= 10).astype(float)


def gdc_043_gap_down_density_15in63(close: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: 15 or more down-gap days within the last 63 days."""
    return (gdc_023_gap_down_count_63d(close, open) >= 15).astype(float)


def gdc_044_gap_down_density_21d_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of 21-day down-gap count within trailing 252 days."""
    cnt = gdc_022_gap_down_count_21d(close, open)
    return cnt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def gdc_045_gap_down_density_63d_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of 63-day down-gap count within trailing 252 days."""
    cnt = gdc_023_gap_down_count_63d(close, open)
    return cnt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def gdc_046_gap_down_count_21d_norm_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day down-gap count normalized by its 252-day average."""
    cnt = gdc_022_gap_down_count_21d(close, open)
    return _safe_div(cnt, _rolling_mean(cnt, _TD_YEAR))


def gdc_047_gap_down_count_63d_norm_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day down-gap count normalized by its 252-day average."""
    cnt = gdc_023_gap_down_count_63d(close, open)
    return _safe_div(cnt, _rolling_mean(cnt, _TD_YEAR))


def gdc_048_gap_down_cluster_accel_21_5(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day count divided by 5-day count (cluster acceleration into recent window)."""
    cnt21 = gdc_022_gap_down_count_21d(close, open)
    cnt5 = gdc_021_gap_down_count_5d(close, open)
    return _safe_div(cnt5 * (_TD_MON / _TD_WEEK), cnt21)


def gdc_049_gap_down_cluster_accel_63_21(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day base vs 21-day recent cluster rate acceleration ratio."""
    cnt63 = gdc_023_gap_down_count_63d(close, open)
    cnt21 = gdc_022_gap_down_count_21d(close, open)
    rate63 = _safe_div(cnt63, pd.Series(_TD_QTR, index=close.index, dtype=float))
    rate21 = _safe_div(cnt21, pd.Series(_TD_MON, index=close.index, dtype=float))
    return _safe_div(rate21, rate63)


def gdc_050_gap_down_ewm_count_span21(close: pd.Series, open: pd.Series) -> pd.Series:
    """Exponentially weighted count of down-gap events, span=21 (recency-weighted density)."""
    return _ewm_mean(_down_gap(close, open).astype(float), _TD_MON)


# --- Group F (051-060): Inter-gap timing and recency ---

def gdc_051_days_since_last_gap_down(close: pd.Series, open: pd.Series) -> pd.Series:
    """Number of trading days since the most recent down-gap (0 = today is a gap)."""
    cond = _down_gap(close, open).astype(float)
    not_gap = 1.0 - cond
    group = cond.cumsum()
    days_since = not_gap.groupby(group).cumsum()
    return days_since


def gdc_052_days_since_last_gap_down_norm_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Days-since-last-gap normalized by 21-day average inter-gap interval."""
    ds = gdc_051_days_since_last_gap_down(close, open)
    return _safe_div(ds, _rolling_mean(ds, _TD_MON))


def gdc_053_avg_inter_gap_interval_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 21-day average of days-since-last-gap (typical spacing)."""
    ds = gdc_051_days_since_last_gap_down(close, open)
    return _rolling_mean(ds, _TD_MON)


def gdc_054_avg_inter_gap_interval_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 63-day average of days-since-last-gap (typical spacing)."""
    ds = gdc_051_days_since_last_gap_down(close, open)
    return _rolling_mean(ds, _TD_QTR)


def gdc_055_min_inter_gap_interval_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Minimum days-between-gaps within trailing 21 days (tightest clustering)."""
    ds = gdc_051_days_since_last_gap_down(close, open)
    cond = _down_gap(close, open)
    gap_ds = ds.where(cond, np.nan)
    return gap_ds.rolling(_TD_MON, min_periods=1).min()


def gdc_056_min_inter_gap_interval_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Minimum days-between-gaps within trailing 63 days."""
    ds = gdc_051_days_since_last_gap_down(close, open)
    cond = _down_gap(close, open)
    gap_ds = ds.where(cond, np.nan)
    return gap_ds.rolling(_TD_QTR, min_periods=1).min()


def gdc_057_gap_down_recency_decay_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Exponentially decayed signal of recent gap-down events, span=21."""
    return _ewm_mean(_down_gap(close, open).astype(float), _TD_MON)


def gdc_058_gap_down_recency_decay_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Exponentially decayed signal of recent gap-down events, span=5."""
    return _ewm_mean(_down_gap(close, open).astype(float), _TD_WEEK)


def gdc_059_days_since_last_gap_down_log(close: pd.Series, open: pd.Series) -> pd.Series:
    """Log1p of days since the last down-gap (compresses long waits)."""
    return np.log1p(gdc_051_days_since_last_gap_down(close, open))


def gdc_060_gap_down_count_21d_vs_63d_ratio(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of 21-day to 63-day down-gap count scaled by window (clustering surge)."""
    cnt21 = gdc_022_gap_down_count_21d(close, open)
    cnt63 = gdc_023_gap_down_count_63d(close, open)
    return _safe_div(cnt21 / _TD_MON, cnt63 / _TD_QTR)


# --- Group G (061-068): Runs within N days, streak frequency ---

def gdc_061_gap_down_runs_2in5(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of 5-day windows (in the last 21d) where at least 2 down-gaps occurred."""
    cond = _down_gap(close, open).astype(float)
    cnt5 = cond.rolling(_TD_WEEK, min_periods=_TD_WEEK).sum()
    return (cnt5 >= 2).astype(float).rolling(_TD_MON, min_periods=1).sum()


def gdc_062_gap_down_runs_3in5(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of 5-day windows (in the last 63d) where at least 3 down-gaps occurred."""
    cond = _down_gap(close, open).astype(float)
    cnt5 = cond.rolling(_TD_WEEK, min_periods=_TD_WEEK).sum()
    return (cnt5 >= 3).astype(float).rolling(_TD_QTR, min_periods=1).sum()


def gdc_063_gap_down_runs_4in10(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of 10-day windows (in the last 63d) where 4 or more down-gaps occurred."""
    cond = _down_gap(close, open).astype(float)
    cnt10 = cond.rolling(10, min_periods=10).sum()
    return (cnt10 >= 4).astype(float).rolling(_TD_QTR, min_periods=1).sum()


def gdc_064_gap_down_streak_starts_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of new consecutive down-gap streaks started in trailing 21 days."""
    cond = _down_gap(close, open)
    prev = cond.shift(1, fill_value=False)
    is_start = (cond & (~prev)).astype(float)
    return _rolling_sum(is_start, _TD_MON)


def gdc_065_gap_down_streak_starts_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of new consecutive down-gap streaks started in trailing 63 days."""
    cond = _down_gap(close, open)
    prev = cond.shift(1, fill_value=False)
    is_start = (cond & (~prev)).astype(float)
    return _rolling_sum(is_start, _TD_QTR)


def gdc_066_avg_gap_streak_len_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average length of completed down-gap streaks over trailing 63 days."""
    cond = _down_gap(close, open)
    is_down = cond.astype(float)
    prev = cond.shift(1, fill_value=False)
    is_start = (cond & (~prev)).astype(float)
    total_down = _rolling_sum(is_down, _TD_QTR)
    num_starts = _rolling_sum(is_start, _TD_QTR)
    return _safe_div(total_down, num_starts.clip(lower=1))


def gdc_067_avg_gap_streak_len_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average length of down-gap streaks over trailing 252 days."""
    cond = _down_gap(close, open)
    is_down = cond.astype(float)
    prev = cond.shift(1, fill_value=False)
    is_start = (cond & (~prev)).astype(float)
    total_down = _rolling_sum(is_down, _TD_YEAR)
    num_starts = _rolling_sum(is_start, _TD_YEAR)
    return _safe_div(total_down, num_starts.clip(lower=1))


def gdc_068_gap_down_streak_len_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of current gap-streak length within trailing 252 days."""
    streak = gdc_001_consec_gap_down_current(close, open)
    return streak.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group H (069-075): Island Reversal Detection ---
# An island-bottom reversal = gap DOWN into a small cluster, then gap UP out,
# leaving bars "stranded." Confirmed when the exit gap-up has already occurred.

def gdc_069_island_bottom_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Island-bottom reversal flag: fires on the day a gap-up confirms the island.
    Entry was a gap-down 1-5 bars ago; today gaps up, completing the bottom island.
    Fully backward-looking — the confirming gap-up has already happened.
    """
    return _island_bottom_flag(close, open)


def gdc_070_island_bottom_width_bars(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Width in bars of the confirmed island bottom (1-5). Zero on non-island days.
    Narrower islands (1 bar = single-bar island reversal) are the sharpest signal.
    """
    return _island_bottom_width(close, open)


def gdc_071_single_bar_island_bottom_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Single-bar island-bottom flag: gap-down yesterday, gap-up today.
    The sharpest form — one stranded bar between two bracketing gaps.
    """
    dg_lag1 = _down_gap(close, open).shift(1, fill_value=False)
    ug = _up_gap(close, open)
    return (ug & dg_lag1).astype(float)


def gdc_072_island_bottom_entry_gap_pct(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Down-gap pct of the entry gap that created the most recent island bottom.
    Measured as the down-gap pct on the bar where the island-entry gap-down occurred
    (lagged to align with the confirmation day). Zero on non-island days.
    """
    dg_pct = _down_gap_pct(close, open)
    ug = _up_gap(close, open)
    result = pd.Series(0.0, index=close.index)
    for lag in range(1, 6):
        entry_gap = _down_gap(close, open).shift(lag, fill_value=False)
        mask = ug & entry_gap & (result == 0.0)
        result = result.where(~mask, dg_pct.shift(lag).fillna(0.0))
    return result


def gdc_073_island_bottom_exit_gap_pct(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Up-gap pct of the confirming exit gap on island-bottom days. Zero on non-island days.
    Larger exit gaps signal stronger reversal potential.
    """
    ug_pct = _up_gap_pct(close, open)
    flag = _island_bottom_flag(close, open)
    return ug_pct * flag


def gdc_074_island_bottom_count_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of island-bottom reversals in the trailing 63 trading days."""
    return _rolling_sum(_island_bottom_flag(close, open), _TD_QTR)


def gdc_075_island_bottom_count_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of island-bottom reversals in the trailing 252 trading days."""
    return _rolling_sum(_island_bottom_flag(close, open), _TD_YEAR)


# ── Registry ──────────────────────────────────────────────────────────────────

GAP_DOWN_CLUSTERING_REGISTRY_001_075 = {
    "gdc_001_consec_gap_down_current": {"inputs": ["close", "open"], "func": gdc_001_consec_gap_down_current},
    "gdc_002_consec_gap_down_current_log": {"inputs": ["close", "open"], "func": gdc_002_consec_gap_down_current_log},
    "gdc_003_consec_gap_down_norm_21d": {"inputs": ["close", "open"], "func": gdc_003_consec_gap_down_norm_21d},
    "gdc_004_consec_gap_down_norm_63d": {"inputs": ["close", "open"], "func": gdc_004_consec_gap_down_norm_63d},
    "gdc_005_consec_gap_down_norm_252d": {"inputs": ["close", "open"], "func": gdc_005_consec_gap_down_norm_252d},
    "gdc_006_consec_gap_down_pct_rank_252d": {"inputs": ["close", "open"], "func": gdc_006_consec_gap_down_pct_rank_252d},
    "gdc_007_consec_gap_down_ge2_flag": {"inputs": ["close", "open"], "func": gdc_007_consec_gap_down_ge2_flag},
    "gdc_008_consec_gap_down_ge3_flag": {"inputs": ["close", "open"], "func": gdc_008_consec_gap_down_ge3_flag},
    "gdc_009_consec_gap_down_ge5_flag": {"inputs": ["close", "open"], "func": gdc_009_consec_gap_down_ge5_flag},
    "gdc_010_consec_gap_down_expanding_max": {"inputs": ["close", "open"], "func": gdc_010_consec_gap_down_expanding_max},
    "gdc_011_max_gap_down_streak_5d": {"inputs": ["close", "open"], "func": gdc_011_max_gap_down_streak_5d},
    "gdc_012_max_gap_down_streak_21d": {"inputs": ["close", "open"], "func": gdc_012_max_gap_down_streak_21d},
    "gdc_013_max_gap_down_streak_63d": {"inputs": ["close", "open"], "func": gdc_013_max_gap_down_streak_63d},
    "gdc_014_max_gap_down_streak_126d": {"inputs": ["close", "open"], "func": gdc_014_max_gap_down_streak_126d},
    "gdc_015_max_gap_down_streak_252d": {"inputs": ["close", "open"], "func": gdc_015_max_gap_down_streak_252d},
    "gdc_016_current_vs_max_gap_streak_63d": {"inputs": ["close", "open"], "func": gdc_016_current_vs_max_gap_streak_63d},
    "gdc_017_current_vs_max_gap_streak_252d": {"inputs": ["close", "open"], "func": gdc_017_current_vs_max_gap_streak_252d},
    "gdc_018_max_gap_streak_21d_vs_252d": {"inputs": ["close", "open"], "func": gdc_018_max_gap_streak_21d_vs_252d},
    "gdc_019_max_gap_streak_63d_vs_252d": {"inputs": ["close", "open"], "func": gdc_019_max_gap_streak_63d_vs_252d},
    "gdc_020_max_gap_streak_252d_expanding_rank": {"inputs": ["close", "open"], "func": gdc_020_max_gap_streak_252d_expanding_rank},
    "gdc_021_gap_down_count_5d": {"inputs": ["close", "open"], "func": gdc_021_gap_down_count_5d},
    "gdc_022_gap_down_count_21d": {"inputs": ["close", "open"], "func": gdc_022_gap_down_count_21d},
    "gdc_023_gap_down_count_63d": {"inputs": ["close", "open"], "func": gdc_023_gap_down_count_63d},
    "gdc_024_gap_down_count_126d": {"inputs": ["close", "open"], "func": gdc_024_gap_down_count_126d},
    "gdc_025_gap_down_count_252d": {"inputs": ["close", "open"], "func": gdc_025_gap_down_count_252d},
    "gdc_026_gap_down_fraction_5d": {"inputs": ["close", "open"], "func": gdc_026_gap_down_fraction_5d},
    "gdc_027_gap_down_fraction_21d": {"inputs": ["close", "open"], "func": gdc_027_gap_down_fraction_21d},
    "gdc_028_gap_down_fraction_63d": {"inputs": ["close", "open"], "func": gdc_028_gap_down_fraction_63d},
    "gdc_029_gap_down_fraction_252d": {"inputs": ["close", "open"], "func": gdc_029_gap_down_fraction_252d},
    "gdc_030_gap_down_count_5d_pct_rank_252d": {"inputs": ["close", "open"], "func": gdc_030_gap_down_count_5d_pct_rank_252d},
    "gdc_031_cum_gap_down_size_current_streak": {"inputs": ["close", "open"], "func": gdc_031_cum_gap_down_size_current_streak},
    "gdc_032_cum_gap_down_pct_current_streak": {"inputs": ["close", "open"], "func": gdc_032_cum_gap_down_pct_current_streak},
    "gdc_033_avg_gap_down_size_current_streak": {"inputs": ["close", "open"], "func": gdc_033_avg_gap_down_size_current_streak},
    "gdc_034_sum_gap_down_pct_21d": {"inputs": ["close", "open"], "func": gdc_034_sum_gap_down_pct_21d},
    "gdc_035_sum_gap_down_pct_63d": {"inputs": ["close", "open"], "func": gdc_035_sum_gap_down_pct_63d},
    "gdc_036_sum_gap_down_pct_252d": {"inputs": ["close", "open"], "func": gdc_036_sum_gap_down_pct_252d},
    "gdc_037_avg_gap_down_pct_21d": {"inputs": ["close", "open"], "func": gdc_037_avg_gap_down_pct_21d},
    "gdc_038_avg_gap_down_pct_63d": {"inputs": ["close", "open"], "func": gdc_038_avg_gap_down_pct_63d},
    "gdc_039_max_gap_down_pct_21d": {"inputs": ["close", "open"], "func": gdc_039_max_gap_down_pct_21d},
    "gdc_040_max_gap_down_pct_63d": {"inputs": ["close", "open"], "func": gdc_040_max_gap_down_pct_63d},
    "gdc_041_gap_down_density_5in21": {"inputs": ["close", "open"], "func": gdc_041_gap_down_density_5in21},
    "gdc_042_gap_down_density_10in21": {"inputs": ["close", "open"], "func": gdc_042_gap_down_density_10in21},
    "gdc_043_gap_down_density_15in63": {"inputs": ["close", "open"], "func": gdc_043_gap_down_density_15in63},
    "gdc_044_gap_down_density_21d_pct_rank_252d": {"inputs": ["close", "open"], "func": gdc_044_gap_down_density_21d_pct_rank_252d},
    "gdc_045_gap_down_density_63d_pct_rank_252d": {"inputs": ["close", "open"], "func": gdc_045_gap_down_density_63d_pct_rank_252d},
    "gdc_046_gap_down_count_21d_norm_252d": {"inputs": ["close", "open"], "func": gdc_046_gap_down_count_21d_norm_252d},
    "gdc_047_gap_down_count_63d_norm_252d": {"inputs": ["close", "open"], "func": gdc_047_gap_down_count_63d_norm_252d},
    "gdc_048_gap_down_cluster_accel_21_5": {"inputs": ["close", "open"], "func": gdc_048_gap_down_cluster_accel_21_5},
    "gdc_049_gap_down_cluster_accel_63_21": {"inputs": ["close", "open"], "func": gdc_049_gap_down_cluster_accel_63_21},
    "gdc_050_gap_down_ewm_count_span21": {"inputs": ["close", "open"], "func": gdc_050_gap_down_ewm_count_span21},
    "gdc_051_days_since_last_gap_down": {"inputs": ["close", "open"], "func": gdc_051_days_since_last_gap_down},
    "gdc_052_days_since_last_gap_down_norm_21d": {"inputs": ["close", "open"], "func": gdc_052_days_since_last_gap_down_norm_21d},
    "gdc_053_avg_inter_gap_interval_21d": {"inputs": ["close", "open"], "func": gdc_053_avg_inter_gap_interval_21d},
    "gdc_054_avg_inter_gap_interval_63d": {"inputs": ["close", "open"], "func": gdc_054_avg_inter_gap_interval_63d},
    "gdc_055_min_inter_gap_interval_21d": {"inputs": ["close", "open"], "func": gdc_055_min_inter_gap_interval_21d},
    "gdc_056_min_inter_gap_interval_63d": {"inputs": ["close", "open"], "func": gdc_056_min_inter_gap_interval_63d},
    "gdc_057_gap_down_recency_decay_21d": {"inputs": ["close", "open"], "func": gdc_057_gap_down_recency_decay_21d},
    "gdc_058_gap_down_recency_decay_5d": {"inputs": ["close", "open"], "func": gdc_058_gap_down_recency_decay_5d},
    "gdc_059_days_since_last_gap_down_log": {"inputs": ["close", "open"], "func": gdc_059_days_since_last_gap_down_log},
    "gdc_060_gap_down_count_21d_vs_63d_ratio": {"inputs": ["close", "open"], "func": gdc_060_gap_down_count_21d_vs_63d_ratio},
    "gdc_061_gap_down_runs_2in5": {"inputs": ["close", "open"], "func": gdc_061_gap_down_runs_2in5},
    "gdc_062_gap_down_runs_3in5": {"inputs": ["close", "open"], "func": gdc_062_gap_down_runs_3in5},
    "gdc_063_gap_down_runs_4in10": {"inputs": ["close", "open"], "func": gdc_063_gap_down_runs_4in10},
    "gdc_064_gap_down_streak_starts_21d": {"inputs": ["close", "open"], "func": gdc_064_gap_down_streak_starts_21d},
    "gdc_065_gap_down_streak_starts_63d": {"inputs": ["close", "open"], "func": gdc_065_gap_down_streak_starts_63d},
    "gdc_066_avg_gap_streak_len_63d": {"inputs": ["close", "open"], "func": gdc_066_avg_gap_streak_len_63d},
    "gdc_067_avg_gap_streak_len_252d": {"inputs": ["close", "open"], "func": gdc_067_avg_gap_streak_len_252d},
    "gdc_068_gap_down_streak_len_pct_rank_252d": {"inputs": ["close", "open"], "func": gdc_068_gap_down_streak_len_pct_rank_252d},
    "gdc_069_island_bottom_flag": {"inputs": ["close", "open"], "func": gdc_069_island_bottom_flag},
    "gdc_070_island_bottom_width_bars": {"inputs": ["close", "open"], "func": gdc_070_island_bottom_width_bars},
    "gdc_071_single_bar_island_bottom_flag": {"inputs": ["close", "open"], "func": gdc_071_single_bar_island_bottom_flag},
    "gdc_072_island_bottom_entry_gap_pct": {"inputs": ["close", "open"], "func": gdc_072_island_bottom_entry_gap_pct},
    "gdc_073_island_bottom_exit_gap_pct": {"inputs": ["close", "open"], "func": gdc_073_island_bottom_exit_gap_pct},
    "gdc_074_island_bottom_count_63d": {"inputs": ["close", "open"], "func": gdc_074_island_bottom_count_63d},
    "gdc_075_island_bottom_count_252d": {"inputs": ["close", "open"], "func": gdc_075_island_bottom_count_252d},
}
