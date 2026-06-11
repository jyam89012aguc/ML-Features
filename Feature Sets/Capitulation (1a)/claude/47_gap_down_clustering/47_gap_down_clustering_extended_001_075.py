"""
47_gap_down_clustering — Extended Features 001-075
Domain: clustered down-gaps and gap streaks — deeper island-reversal variants (island
depth, island return magnitude, multi-bar width buckets, island-bottom recency at
additional windows); gap-down cluster intensity (normalized rolling counts, cluster
z-scores at new window pairs, burst detection); cumulative gap-down magnitude over
cluster windows; consecutive-gap-down longest-streak variants; gap-down acceleration
(second-order magnitude change); gap-down concentration (share of period decline from
gaps); gap-down + wide-range + volume confluence; exhaustion-gap-down at new lows;
gap-down-then-recovery intraday signatures; and rate-of-change of cluster-intensity
at novel window combinations not covered by existing files.
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
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond: pd.Series, w: int) -> pd.Series:
    """Maximum consecutive-True run length over trailing w periods (raw apply)."""
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
    """Down-gap as fraction of prior close (zero on non-gap days)."""
    size = _down_gap_size(close, open)
    return _safe_div(size, close.shift(1).replace(0, np.nan))


def _up_gap(close: pd.Series, open: pd.Series) -> pd.Series:
    """Boolean: today's open > prior close (up-gap day)."""
    return open > close.shift(1)


def _up_gap_pct(close: pd.Series, open: pd.Series) -> pd.Series:
    """Up-gap as fraction of prior close (zero on non-gap days)."""
    raw = (open - close.shift(1)).clip(lower=0.0)
    return _safe_div(raw, close.shift(1).replace(0, np.nan))


def _island_bottom_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Island-bottom flag: gap-down 1-5 bars ago + gap-up today. Backward-looking.
    Fires on the confirmation (exit gap-up) day only.
    """
    dg = _down_gap(close, open)
    ug = _up_gap(close, open)
    result = pd.Series(0.0, index=close.index)
    for lag in range(1, 6):
        entry_gap = dg.shift(lag, fill_value=False)
        result = result + (ug & entry_gap).astype(float)
    return result.clip(upper=1.0)


def _island_bottom_width(close: pd.Series, open: pd.Series) -> pd.Series:
    """Width (bars) of confirmed island bottom (1-5). Zero on non-island days."""
    dg = _down_gap(close, open)
    ug = _up_gap(close, open)
    result = pd.Series(0.0, index=close.index)
    for lag in range(1, 6):
        entry_gap = dg.shift(lag, fill_value=False)
        mask = (ug & entry_gap & (result == 0.0))
        result = result.where(~mask, float(lag))
    return result


def _island_top_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Island-top flag: gap-up 1-5 bars ago + gap-down today. Backward-looking."""
    dg = _down_gap(close, open)
    ug = _up_gap(close, open)
    result = pd.Series(0.0, index=close.index)
    for lag in range(1, 6):
        entry_gap = ug.shift(lag, fill_value=False)
        result = result + (dg & entry_gap).astype(float)
    return result.clip(upper=1.0)


def _days_since_island_bottom(close: pd.Series, open: pd.Series) -> pd.Series:
    """Bars elapsed since the last confirmed island-bottom signal."""
    flag = _island_bottom_flag(close, open)
    not_island = 1.0 - flag
    group = flag.cumsum()
    return not_island.groupby(group).cumsum()


# ── Extended Feature Functions 001-075 ───────────────────────────────────────

# --- Group A (001-010): Deeper island-reversal variants ---

def gdc_ext_001_island_bottom_width1_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: island-bottom with exactly width=1 bar (sharpest form), same as single-bar check."""
    w = _island_bottom_width(close, open)
    return (w == 1.0).astype(float)


def gdc_ext_002_island_bottom_width2_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: island-bottom with exactly 2-bar width."""
    w = _island_bottom_width(close, open)
    return (w == 2.0).astype(float)


def gdc_ext_003_island_bottom_width3to5_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: island-bottom with width 3-5 bars (wider island cluster)."""
    w = _island_bottom_width(close, open)
    return ((w >= 3.0) & (w <= 5.0)).astype(float)


def gdc_ext_004_island_bottom_depth_pct(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Island depth: on island-bottom confirmation days, the low of the island body
    relative to the entry day's prior close. Measures how far down the island traded.
    Approximated as the entry gap-down pct (how far open dropped from prior close).
    Zero on non-island days.
    """
    dg = _down_gap(close, open)
    ug = _up_gap(close, open)
    dg_pct = _down_gap_pct(close, open)
    result = pd.Series(0.0, index=close.index)
    flag = pd.Series(0.0, index=close.index)
    for lag in range(1, 6):
        entry_gap = dg.shift(lag, fill_value=False)
        mask = ug & entry_gap & (flag == 0.0)
        result = result.where(~mask, dg_pct.shift(lag).fillna(0.0))
        flag = flag.where(~mask, 1.0)
    return result


def gdc_ext_005_island_bottom_return_pct(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Island return pct: on island-bottom confirmation days, the exit up-gap pct
    minus the entry down-gap pct. Positive = gap-up exceeds gap-down (net gain).
    Zero on non-island days.
    """
    dg = _down_gap(close, open)
    ug = _up_gap(close, open)
    dg_pct = _down_gap_pct(close, open)
    ug_pct = _up_gap_pct(close, open)
    entry_pct = pd.Series(0.0, index=close.index)
    flag = pd.Series(0.0, index=close.index)
    for lag in range(1, 6):
        entry_gap = dg.shift(lag, fill_value=False)
        mask = ug & entry_gap & (flag == 0.0)
        entry_pct = entry_pct.where(~mask, dg_pct.shift(lag).fillna(0.0))
        flag = flag.where(~mask, 1.0)
    return (ug_pct - entry_pct) * flag


def gdc_ext_006_island_bottom_count_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of island-bottom reversals in the trailing 5 trading days."""
    return _rolling_sum(_island_bottom_flag(close, open), _TD_WEEK)


def gdc_ext_007_island_bottom_count_126d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of island-bottom reversals in the trailing 126 trading days."""
    return _rolling_sum(_island_bottom_flag(close, open), _TD_HALF)


def gdc_ext_008_days_since_island_bottom_norm_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Days since last island-bottom normalized by 63-day average of that series."""
    ds = _days_since_island_bottom(close, open)
    return _safe_div(ds, _rolling_mean(ds, _TD_QTR))


def gdc_ext_009_island_top_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of confirmed island-top patterns in the trailing 21 days."""
    return _rolling_sum(_island_top_flag(close, open), _TD_MON)


def gdc_ext_010_island_top_count_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of confirmed island-top patterns in the trailing 252 days."""
    return _rolling_sum(_island_top_flag(close, open), _TD_YEAR)


# --- Group B (011-020): Gap-down cluster intensity (z-scores, burst detection) ---

def gdc_ext_011_gap_down_count_5d_zscore_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of 5-day down-gap count vs its 63-day distribution."""
    cnt5 = _rolling_count_true(_down_gap(close, open), _TD_WEEK)
    m = _rolling_mean(cnt5, _TD_QTR)
    s = _rolling_std(cnt5, _TD_QTR)
    return _safe_div(cnt5 - m, s)


def gdc_ext_012_gap_down_count_21d_zscore_126d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of 21-day down-gap count vs its 126-day distribution."""
    cnt21 = _rolling_count_true(_down_gap(close, open), _TD_MON)
    m = _rolling_mean(cnt21, _TD_HALF)
    s = _rolling_std(cnt21, _TD_HALF)
    return _safe_div(cnt21 - m, s)


def gdc_ext_013_gap_down_count_63d_zscore_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of 63-day down-gap count vs its 252-day distribution."""
    cnt63 = _rolling_count_true(_down_gap(close, open), _TD_QTR)
    m = _rolling_mean(cnt63, _TD_YEAR)
    s = _rolling_std(cnt63, _TD_YEAR)
    return _safe_div(cnt63 - m, s)


def gdc_ext_014_gap_down_burst_3in3_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Burst flag: all 3 consecutive days had a down-gap (3-day mini-burst)."""
    cnt3 = _rolling_count_true(_down_gap(close, open), 3)
    return (cnt3 >= 3.0).astype(float)


def gdc_ext_015_gap_down_burst_4in5_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Burst flag: 4 or more down-gaps in last 5 days (near-saturated burst)."""
    cnt5 = _rolling_count_true(_down_gap(close, open), _TD_WEEK)
    return (cnt5 >= 4.0).astype(float)


def gdc_ext_016_gap_down_burst_8in10_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Burst flag: 8 or more down-gaps in last 10 days (sustained burst)."""
    cnt10 = _rolling_count_true(_down_gap(close, open), 10)
    return (cnt10 >= 8.0).astype(float)


def gdc_ext_017_gap_down_count_10d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of down-gap days in the trailing 10 trading days."""
    return _rolling_count_true(_down_gap(close, open), 10)


def gdc_ext_018_gap_down_count_10d_norm_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """10-day down-gap count normalized by its 252-day rolling average."""
    cnt10 = _rolling_count_true(_down_gap(close, open), 10)
    return _safe_div(cnt10, _rolling_mean(cnt10, _TD_YEAR))


def gdc_ext_019_gap_down_cluster_intensity_score(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Cluster intensity score: weighted sum of z-scored counts at 5d, 21d, 63d windows
    (weights 3:2:1 to emphasize recency). Combines burst and sustained signals.
    """
    cnt5 = _rolling_count_true(_down_gap(close, open), _TD_WEEK)
    cnt21 = _rolling_count_true(_down_gap(close, open), _TD_MON)
    cnt63 = _rolling_count_true(_down_gap(close, open), _TD_QTR)
    z5 = _safe_div(cnt5 - _rolling_mean(cnt5, _TD_YEAR), _rolling_std(cnt5, _TD_YEAR))
    z21 = _safe_div(cnt21 - _rolling_mean(cnt21, _TD_YEAR), _rolling_std(cnt21, _TD_YEAR))
    z63 = _safe_div(cnt63 - _rolling_mean(cnt63, _TD_YEAR), _rolling_std(cnt63, _TD_YEAR))
    return (3.0 * z5.fillna(0.0) + 2.0 * z21.fillna(0.0) + 1.0 * z63.fillna(0.0)) / 6.0


def gdc_ext_020_gap_down_cluster_intensity_pct_rank(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of cluster intensity score within trailing 252 days."""
    score = gdc_ext_019_gap_down_cluster_intensity_score(close, open)
    return score.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group C (021-030): Cumulative gap-down magnitude over cluster windows ---

def gdc_ext_021_cum_gap_down_pct_10d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative down-gap percentage over trailing 10 days."""
    return _rolling_sum(_down_gap_pct(close, open), 10)


def gdc_ext_022_cum_gap_down_pct_126d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative down-gap percentage over trailing 126 days."""
    return _rolling_sum(_down_gap_pct(close, open), _TD_HALF)


def gdc_ext_023_cum_gap_down_pct_21d_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of 21-day cumulative gap-down pct within 252-day window."""
    s21 = _rolling_sum(_down_gap_pct(close, open), _TD_MON)
    return s21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def gdc_ext_024_cum_gap_down_pct_63d_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of 63-day cumulative gap-down pct within 252-day window."""
    s63 = _rolling_sum(_down_gap_pct(close, open), _TD_QTR)
    return s63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def gdc_ext_025_cum_gap_pct_10d_zscore_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of 10-day cumulative gap-down pct vs its 252-day distribution."""
    s10 = _rolling_sum(_down_gap_pct(close, open), 10)
    m = _rolling_mean(s10, _TD_YEAR)
    s = _rolling_std(s10, _TD_YEAR)
    return _safe_div(s10 - m, s)


def gdc_ext_026_cum_gap_pct_per_gap_day_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average gap-down pct per gap-day (magnitude density) over 21 days."""
    sum_pct = _rolling_sum(_down_gap_pct(close, open), _TD_MON)
    cnt = _rolling_count_true(_down_gap(close, open), _TD_MON)
    return _safe_div(sum_pct, cnt)


def gdc_ext_027_cum_gap_pct_per_gap_day_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average gap-down pct per gap-day (magnitude density) over 63 days."""
    sum_pct = _rolling_sum(_down_gap_pct(close, open), _TD_QTR)
    cnt = _rolling_count_true(_down_gap(close, open), _TD_QTR)
    return _safe_div(sum_pct, cnt)


def gdc_ext_028_cum_gap_pct_21d_vs_126d_norm(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rate of 21-day cumulative gap pct vs 126-day rate (novel window pair)."""
    s21 = _rolling_sum(_down_gap_pct(close, open), _TD_MON) / _TD_MON
    s126 = _rolling_sum(_down_gap_pct(close, open), _TD_HALF) / _TD_HALF
    return _safe_div(s21, s126)


def gdc_ext_029_max_gap_down_pct_126d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum single-day down-gap percentage within trailing 126 days."""
    return _rolling_max(_down_gap_pct(close, open), _TD_HALF)


def gdc_ext_030_max_gap_down_pct_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum single-day down-gap percentage within trailing 252 days."""
    return _rolling_max(_down_gap_pct(close, open), _TD_YEAR)


# --- Group D (031-040): Consecutive-gap-down streaks and longest-streak variants ---

def gdc_ext_031_longest_gap_streak_ever(close: pd.Series, open: pd.Series) -> pd.Series:
    """Expanding (all-time) maximum consecutive down-gap streak length."""
    streak = _consec_streak(_down_gap(close, open))
    return streak.expanding(min_periods=1).max()


def gdc_ext_032_current_vs_all_time_max_streak(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current down-gap streak as fraction of all-time max streak (expanding)."""
    streak = _consec_streak(_down_gap(close, open))
    atm = streak.expanding(min_periods=1).max()
    return _safe_div(streak, atm)


def gdc_ext_033_longest_gap_streak_10d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum consecutive down-gap streak within trailing 10 days."""
    return _rolling_max_streak(_down_gap(close, open), 10)


def gdc_ext_034_longest_gap_streak_42d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum consecutive down-gap streak within trailing 42 days (2-month)."""
    return _rolling_max_streak(_down_gap(close, open), 42)


def gdc_ext_035_gap_streak_length_pct_rank_126d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of current gap-streak length within trailing 126 days."""
    streak = _consec_streak(_down_gap(close, open))
    return streak.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)


def gdc_ext_036_gap_streak_ge4_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary flag: current consecutive down-gap streak >= 4 bars."""
    return (_consec_streak(_down_gap(close, open)) >= 4.0).astype(float)


def gdc_ext_037_gap_streak_ge7_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary flag: current consecutive down-gap streak >= 7 bars (1.5 trading weeks)."""
    return (_consec_streak(_down_gap(close, open)) >= 7.0).astype(float)


def gdc_ext_038_gap_streak_ge10_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary flag: current consecutive down-gap streak >= 10 bars (2 full weeks)."""
    return (_consec_streak(_down_gap(close, open)) >= 10.0).astype(float)


def gdc_ext_039_consec_gap_down_norm_126d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current down-gap streak normalized by its 126-day rolling average."""
    streak = _consec_streak(_down_gap(close, open))
    return _safe_div(streak, _rolling_mean(streak, _TD_HALF))


def gdc_ext_040_gap_down_longest_streak_126d_vs_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of 126-day max streak to 252-day max streak (novel window pair)."""
    mx126 = _rolling_max_streak(_down_gap(close, open), _TD_HALF)
    mx252 = _rolling_max_streak(_down_gap(close, open), _TD_YEAR)
    return _safe_div(mx126, mx252)


# --- Group E (041-050): Gap-down acceleration and concentration ---

def gdc_ext_041_gap_down_pct_accel_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Gap-down pct acceleration: diff of 5-day diff of daily gap-down pct
    (second-order change in per-day gap severity). Zero on non-gap days.
    """
    pct = _down_gap_pct(close, open)
    return pct.diff(_TD_WEEK).diff(_TD_WEEK)


def gdc_ext_042_gap_down_concentration_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Gap-down concentration: fraction of the trailing 21-day price decline
    (close-to-close) attributable to down-gap opens. Measures how much of the
    period's loss happened at the open vs intraday.
    """
    pct_return = _safe_div(close - close.shift(1), close.shift(1).replace(0, np.nan))
    gap_pct = _down_gap_pct(close, open)
    period_loss = (-_rolling_sum(pct_return, _TD_MON)).clip(lower=0.0)
    gap_contrib = _rolling_sum(gap_pct, _TD_MON)
    return _safe_div(gap_contrib, period_loss.replace(0, np.nan))


def gdc_ext_043_gap_down_concentration_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Gap-down concentration over 63 days: fraction of the 63-day price decline
    attributable to down-gap opens (gap share of decline).
    """
    pct_return = _safe_div(close - close.shift(1), close.shift(1).replace(0, np.nan))
    gap_pct = _down_gap_pct(close, open)
    period_loss = (-_rolling_sum(pct_return, _TD_QTR)).clip(lower=0.0)
    gap_contrib = _rolling_sum(gap_pct, _TD_QTR)
    return _safe_div(gap_contrib, period_loss.replace(0, np.nan))


def gdc_ext_044_gap_down_share_of_daily_range_21d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    On gap-down days, the gap size as share of the full intraday range (prior close to high).
    Average over 21 days. Measures how dominant the opening gap is relative to total range.
    """
    cond = _down_gap(close, open)
    gap_size = _down_gap_size(close, open)
    full_range = (high - low + _down_gap_size(close, open)).replace(0, np.nan)
    ratio = _safe_div(gap_size, full_range).where(cond, np.nan)
    return ratio.rolling(_TD_MON, min_periods=1).mean()


def gdc_ext_045_gap_down_pct_sum_21d_norm_close_vol(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    21-day cumulative gap-down pct weighted by normalized volume (vol/21d-avg-vol).
    Captures clusters where both price drops at open AND volume are elevated.
    """
    avg_vol = _rolling_mean(volume, _TD_MON)
    norm_vol = _safe_div(volume, avg_vol)
    gap_pct = _down_gap_pct(close, open)
    return _rolling_sum(gap_pct * norm_vol, _TD_MON)


def gdc_ext_046_gap_down_pct_sum_63d_norm_close_vol(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    63-day cumulative gap-down pct weighted by normalized volume (vol/21d-avg-vol).
    """
    avg_vol = _rolling_mean(volume, _TD_MON)
    norm_vol = _safe_div(volume, avg_vol)
    gap_pct = _down_gap_pct(close, open)
    return _rolling_sum(gap_pct * norm_vol, _TD_QTR)


def gdc_ext_047_gap_down_count_5d_expanding_pct_rank(close: pd.Series, open: pd.Series) -> pd.Series:
    """Expanding percentile rank of 5-day down-gap count (all-history context)."""
    cnt5 = _rolling_count_true(_down_gap(close, open), _TD_WEEK)
    return cnt5.expanding(min_periods=5).rank(pct=True)


def gdc_ext_048_gap_down_count_21d_expanding_pct_rank(close: pd.Series, open: pd.Series) -> pd.Series:
    """Expanding percentile rank of 21-day down-gap count (all-history context)."""
    cnt21 = _rolling_count_true(_down_gap(close, open), _TD_MON)
    return cnt21.expanding(min_periods=5).rank(pct=True)


def gdc_ext_049_gap_down_mean_pct_126d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 126-day mean of daily down-gap pct (baseline severity)."""
    return _rolling_mean(_down_gap_pct(close, open), _TD_HALF)


def gdc_ext_050_gap_down_std_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 63-day standard deviation of daily down-gap pct (gap volatility, QTR window)."""
    return _rolling_std(_down_gap_pct(close, open), _TD_QTR)


# --- Group F (051-060): Gap-down + wide-range + volume confluence ---

def gdc_ext_051_wide_range_gap_down_count_21d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    Count of days with gap-down AND intraday range > 1.5x its 21-day average, over 21d.
    Wide-range gap-down days signal panic selling with broad price discovery.
    """
    cond_gap = _down_gap(close, open)
    rng = high - low
    avg_rng = _rolling_mean(rng, _TD_MON)
    wide = rng > 1.5 * avg_rng
    confluence = (cond_gap & wide).astype(float)
    return _rolling_sum(confluence, _TD_MON)


def gdc_ext_052_wide_range_gap_down_count_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    Count of days with gap-down AND intraday range > 1.5x its 21-day average, over 63d.
    """
    cond_gap = _down_gap(close, open)
    rng = high - low
    avg_rng = _rolling_mean(rng, _TD_MON)
    wide = rng > 1.5 * avg_rng
    confluence = (cond_gap & wide).astype(float)
    return _rolling_sum(confluence, _TD_QTR)


def gdc_ext_053_high_vol_wide_range_gap_down_21d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Count of days with gap-down + wide range (>1.5x avg) + volume > 1.5x avg over 21d.
    Triple confluence: panic gap, extended range, and elevated volume.
    """
    cond_gap = _down_gap(close, open)
    rng = high - low
    avg_rng = _rolling_mean(rng, _TD_MON)
    avg_vol = _rolling_mean(volume, _TD_MON)
    triple = (cond_gap & (rng > 1.5 * avg_rng) & (volume > 1.5 * avg_vol)).astype(float)
    return _rolling_sum(triple, _TD_MON)


def gdc_ext_054_gap_down_with_close_near_low_21d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    Count of gap-down days where close is in the bottom 25% of the day's range (21d).
    Gaps that also close weak indicate continued selling pressure throughout the session.
    """
    cond_gap = _down_gap(close, open)
    rng = (high - low).replace(0, np.nan)
    close_position = _safe_div(close - low, rng)
    weak_close = close_position < 0.25
    flag = (cond_gap & weak_close).astype(float)
    return _rolling_sum(flag, _TD_MON)


def gdc_ext_055_gap_down_with_close_near_low_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """
    Count of gap-down days where close is in bottom 25% of day's range (63d).
    """
    cond_gap = _down_gap(close, open)
    rng = (high - low).replace(0, np.nan)
    close_position = _safe_div(close - low, rng)
    weak_close = close_position < 0.25
    flag = (cond_gap & weak_close).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def gdc_ext_056_gap_down_vol_zscore_on_gap_days_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Average z-score of volume (vs 21d mean/std) on gap-down days, over trailing 21 days.
    Measures abnormality of volume specifically on gap-down events.
    """
    cond = _down_gap(close, open)
    m = _rolling_mean(volume, _TD_MON)
    s = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - m, s)
    gap_vol_z = vol_z.where(cond, np.nan)
    return gap_vol_z.rolling(_TD_MON, min_periods=1).mean()


def gdc_ext_057_gap_down_vol_zscore_on_gap_days_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Average z-score of volume (vs 21d mean/std) on gap-down days, over trailing 63 days.
    """
    cond = _down_gap(close, open)
    m = _rolling_mean(volume, _TD_MON)
    s = _rolling_std(volume, _TD_MON)
    vol_z = _safe_div(volume - m, s)
    gap_vol_z = vol_z.where(cond, np.nan)
    return gap_vol_z.rolling(_TD_QTR, min_periods=1).mean()


def gdc_ext_058_gap_down_vol_surge_3x_count_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Count of gap-down days with volume > 3x its 21-day average over trailing 63 days.
    Extreme-volume gap-downs flag institutional panic or forced selling.
    """
    avg_vol = _rolling_mean(volume, _TD_MON)
    flag = (_down_gap(close, open) & (volume > 3.0 * avg_vol)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def gdc_ext_059_gap_down_above_avg_vol_fraction_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Fraction of gap-down days in 63d that had volume above the 21-day average volume.
    """
    cond = _down_gap(close, open)
    avg_vol = _rolling_mean(volume, _TD_MON)
    above = (cond & (volume > avg_vol)).astype(float)
    gap_cnt = _rolling_count_true(cond, _TD_QTR).replace(0, np.nan)
    above_cnt = _rolling_sum(above, _TD_QTR)
    return _safe_div(above_cnt, gap_cnt)


def gdc_ext_060_gap_down_vol_sum_21d_norm_252d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    21-day sum of volume on gap-down days normalized by 252-day average of that metric.
    Measures whether recent gap-day volume is historically elevated.
    """
    cond = _down_gap(close, open)
    gap_vol = volume.where(cond, 0.0)
    roll21 = _rolling_sum(gap_vol, _TD_MON)
    return _safe_div(roll21, _rolling_mean(roll21, _TD_YEAR))


# --- Group G (061-068): Exhaustion-gap-down at new lows ---

def gdc_ext_061_exhaustion_gap_down_new_low_21d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """
    Exhaustion gap-down flag: gap-down that also sets a new 21-day low on the open.
    Open is below the prior 21-day low, confirming a new-low breakout gap (21d).
    """
    prior_low = low.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min().shift(1)
    flag = (_down_gap(close, open) & (open < prior_low)).astype(float)
    return flag


def gdc_ext_062_exhaustion_gap_down_new_low_63d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """
    Exhaustion gap-down flag: open gaps down AND sets a new 63-day low on open.
    """
    prior_low = low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min().shift(1)
    flag = (_down_gap(close, open) & (open < prior_low)).astype(float)
    return flag


def gdc_ext_063_exhaustion_gap_down_new_low_252d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """
    Exhaustion gap-down flag: open gaps down AND sets a new 252-day (1-year) low on open.
    The most extreme form — a new-annual-low gap-down open.
    """
    prior_low = low.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min().shift(1)
    flag = (_down_gap(close, open) & (open < prior_low)).astype(float)
    return flag


def gdc_ext_064_exhaustion_gap_count_new_low_21d_in_63d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Count of exhaustion gap-downs (open < prior 21d low) in trailing 63 days."""
    flag = gdc_ext_061_exhaustion_gap_down_new_low_21d(close, open, low)
    return _rolling_sum(flag, _TD_QTR)


def gdc_ext_065_exhaustion_gap_count_new_low_63d_in_252d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Count of exhaustion gap-downs (open < prior 63d low) in trailing 252 days."""
    flag = gdc_ext_062_exhaustion_gap_down_new_low_63d(close, open, low)
    return _rolling_sum(flag, _TD_YEAR)


def gdc_ext_066_gap_down_new_low_21d_pct(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """
    Down-gap pct magnitude on days where open sets a new 21-day low (zero otherwise).
    Larger values = more severe exhaustion-gap episodes.
    """
    prior_low = low.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min().shift(1)
    cond = _down_gap(close, open) & (open < prior_low)
    return _down_gap_pct(close, open).where(cond, 0.0)


def gdc_ext_067_gap_down_new_low_63d_pct(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """
    Down-gap pct magnitude on days where open sets a new 63-day low (zero otherwise).
    """
    prior_low = low.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min().shift(1)
    cond = _down_gap(close, open) & (open < prior_low)
    return _down_gap_pct(close, open).where(cond, 0.0)


def gdc_ext_068_exhaustion_gap_flag_new_low_21d_consec(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive streak of exhaustion gap-downs (each opening < prior 21d low)."""
    prior_low = low.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min().shift(1)
    cond = _down_gap(close, open) & (open < prior_low)
    return _consec_streak(cond)


# --- Group H (069-075): Gap-down-then-recovery intraday signatures ---

def gdc_ext_069_gap_down_recovery_close_above_open_pct_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    On gap-down days where close > open (gap partially recovered intraday),
    average recovery pct = (close - open) / prior_close over 21 days.
    Larger values = stronger intraday bounce after gap-down.
    """
    cond = _down_gap(close, open) & (close > open)
    recovery = _safe_div(close - open, close.shift(1).replace(0, np.nan)).where(cond, np.nan)
    return recovery.rolling(_TD_MON, min_periods=1).mean()


def gdc_ext_070_gap_down_recovery_close_above_open_pct_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Average intraday recovery pct on gap-down days that close above open over 63 days.
    """
    cond = _down_gap(close, open) & (close > open)
    recovery = _safe_div(close - open, close.shift(1).replace(0, np.nan)).where(cond, np.nan)
    return recovery.rolling(_TD_QTR, min_periods=1).mean()


def gdc_ext_071_gap_down_full_recovery_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Count of gap-down days in trailing 21d where close >= prior close
    (full intraday recovery: the gap was completely filled).
    """
    cond_gap = _down_gap(close, open)
    full_recovery = cond_gap & (close >= close.shift(1))
    return _rolling_sum(full_recovery.astype(float), _TD_MON)


def gdc_ext_072_gap_down_partial_recovery_fraction_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Fraction of gap-down days in 63d where close > open but close < prior close
    (partial recovery: bounced off lows but did not fill the gap).
    """
    cond_gap = _down_gap(close, open)
    partial = cond_gap & (close > open) & (close < close.shift(1))
    partial_cnt = _rolling_sum(partial.astype(float), _TD_QTR)
    gap_cnt = _rolling_count_true(cond_gap, _TD_QTR).replace(0, np.nan)
    return _safe_div(partial_cnt, gap_cnt)


def gdc_ext_073_gap_down_next_day_up_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Count of gap-down days in trailing 21d followed by a higher close the next day.
    Measures how often gap-downs are immediately reversed by the following session.
    """
    cond_gap = _down_gap(close, open)
    next_up = close > close.shift(1)
    follow_up = (cond_gap.shift(1, fill_value=False) & next_up).astype(float)
    return _rolling_sum(follow_up, _TD_MON)


def gdc_ext_074_gap_down_next_day_up_fraction_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    Fraction of gap-down days in 63d followed by a higher close the next session.
    Higher fractions signal that gap-downs are being absorbed (bullish exhaustion).
    """
    cond_gap = _down_gap(close, open)
    next_up = close > close.shift(1)
    follow_up = (cond_gap.shift(1, fill_value=False) & next_up).astype(float)
    cnt_follow = _rolling_sum(follow_up, _TD_QTR)
    cnt_gap = _rolling_count_true(cond_gap, _TD_QTR).replace(0, np.nan)
    return _safe_div(cnt_follow, cnt_gap)


def gdc_ext_075_gap_down_then_recovery_composite_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """
    Composite recovery signal: fraction of gap-down days (21d) where close > open
    AND volume is above the 21-day average volume (high-conviction intraday reversal).
    """
    cond_gap = _down_gap(close, open)
    avg_vol = _rolling_mean(volume, _TD_MON)
    recovery_with_vol = (cond_gap & (close > open) & (volume > avg_vol)).astype(float)
    cnt_recovery = _rolling_sum(recovery_with_vol, _TD_MON)
    cnt_gap = _rolling_count_true(cond_gap, _TD_MON).replace(0, np.nan)
    return _safe_div(cnt_recovery, cnt_gap)


# ── Registry ──────────────────────────────────────────────────────────────────

GAP_DOWN_CLUSTERING_EXTENDED_REGISTRY_001_075 = {
    "gdc_ext_001_island_bottom_width1_flag": {"inputs": ["close", "open"], "func": gdc_ext_001_island_bottom_width1_flag},
    "gdc_ext_002_island_bottom_width2_flag": {"inputs": ["close", "open"], "func": gdc_ext_002_island_bottom_width2_flag},
    "gdc_ext_003_island_bottom_width3to5_flag": {"inputs": ["close", "open"], "func": gdc_ext_003_island_bottom_width3to5_flag},
    "gdc_ext_004_island_bottom_depth_pct": {"inputs": ["close", "open"], "func": gdc_ext_004_island_bottom_depth_pct},
    "gdc_ext_005_island_bottom_return_pct": {"inputs": ["close", "open"], "func": gdc_ext_005_island_bottom_return_pct},
    "gdc_ext_006_island_bottom_count_5d": {"inputs": ["close", "open"], "func": gdc_ext_006_island_bottom_count_5d},
    "gdc_ext_007_island_bottom_count_126d": {"inputs": ["close", "open"], "func": gdc_ext_007_island_bottom_count_126d},
    "gdc_ext_008_days_since_island_bottom_norm_63d": {"inputs": ["close", "open"], "func": gdc_ext_008_days_since_island_bottom_norm_63d},
    "gdc_ext_009_island_top_count_21d": {"inputs": ["close", "open"], "func": gdc_ext_009_island_top_count_21d},
    "gdc_ext_010_island_top_count_252d": {"inputs": ["close", "open"], "func": gdc_ext_010_island_top_count_252d},
    "gdc_ext_011_gap_down_count_5d_zscore_63d": {"inputs": ["close", "open"], "func": gdc_ext_011_gap_down_count_5d_zscore_63d},
    "gdc_ext_012_gap_down_count_21d_zscore_126d": {"inputs": ["close", "open"], "func": gdc_ext_012_gap_down_count_21d_zscore_126d},
    "gdc_ext_013_gap_down_count_63d_zscore_252d": {"inputs": ["close", "open"], "func": gdc_ext_013_gap_down_count_63d_zscore_252d},
    "gdc_ext_014_gap_down_burst_3in3_flag": {"inputs": ["close", "open"], "func": gdc_ext_014_gap_down_burst_3in3_flag},
    "gdc_ext_015_gap_down_burst_4in5_flag": {"inputs": ["close", "open"], "func": gdc_ext_015_gap_down_burst_4in5_flag},
    "gdc_ext_016_gap_down_burst_8in10_flag": {"inputs": ["close", "open"], "func": gdc_ext_016_gap_down_burst_8in10_flag},
    "gdc_ext_017_gap_down_count_10d": {"inputs": ["close", "open"], "func": gdc_ext_017_gap_down_count_10d},
    "gdc_ext_018_gap_down_count_10d_norm_252d": {"inputs": ["close", "open"], "func": gdc_ext_018_gap_down_count_10d_norm_252d},
    "gdc_ext_019_gap_down_cluster_intensity_score": {"inputs": ["close", "open"], "func": gdc_ext_019_gap_down_cluster_intensity_score},
    "gdc_ext_020_gap_down_cluster_intensity_pct_rank": {"inputs": ["close", "open"], "func": gdc_ext_020_gap_down_cluster_intensity_pct_rank},
    "gdc_ext_021_cum_gap_down_pct_10d": {"inputs": ["close", "open"], "func": gdc_ext_021_cum_gap_down_pct_10d},
    "gdc_ext_022_cum_gap_down_pct_126d": {"inputs": ["close", "open"], "func": gdc_ext_022_cum_gap_down_pct_126d},
    "gdc_ext_023_cum_gap_down_pct_21d_pct_rank_252d": {"inputs": ["close", "open"], "func": gdc_ext_023_cum_gap_down_pct_21d_pct_rank_252d},
    "gdc_ext_024_cum_gap_down_pct_63d_pct_rank_252d": {"inputs": ["close", "open"], "func": gdc_ext_024_cum_gap_down_pct_63d_pct_rank_252d},
    "gdc_ext_025_cum_gap_pct_10d_zscore_252d": {"inputs": ["close", "open"], "func": gdc_ext_025_cum_gap_pct_10d_zscore_252d},
    "gdc_ext_026_cum_gap_pct_per_gap_day_21d": {"inputs": ["close", "open"], "func": gdc_ext_026_cum_gap_pct_per_gap_day_21d},
    "gdc_ext_027_cum_gap_pct_per_gap_day_63d": {"inputs": ["close", "open"], "func": gdc_ext_027_cum_gap_pct_per_gap_day_63d},
    "gdc_ext_028_cum_gap_pct_21d_vs_126d_norm": {"inputs": ["close", "open"], "func": gdc_ext_028_cum_gap_pct_21d_vs_126d_norm},
    "gdc_ext_029_max_gap_down_pct_126d": {"inputs": ["close", "open"], "func": gdc_ext_029_max_gap_down_pct_126d},
    "gdc_ext_030_max_gap_down_pct_252d": {"inputs": ["close", "open"], "func": gdc_ext_030_max_gap_down_pct_252d},
    "gdc_ext_031_longest_gap_streak_ever": {"inputs": ["close", "open"], "func": gdc_ext_031_longest_gap_streak_ever},
    "gdc_ext_032_current_vs_all_time_max_streak": {"inputs": ["close", "open"], "func": gdc_ext_032_current_vs_all_time_max_streak},
    "gdc_ext_033_longest_gap_streak_10d": {"inputs": ["close", "open"], "func": gdc_ext_033_longest_gap_streak_10d},
    "gdc_ext_034_longest_gap_streak_42d": {"inputs": ["close", "open"], "func": gdc_ext_034_longest_gap_streak_42d},
    "gdc_ext_035_gap_streak_length_pct_rank_126d": {"inputs": ["close", "open"], "func": gdc_ext_035_gap_streak_length_pct_rank_126d},
    "gdc_ext_036_gap_streak_ge4_flag": {"inputs": ["close", "open"], "func": gdc_ext_036_gap_streak_ge4_flag},
    "gdc_ext_037_gap_streak_ge7_flag": {"inputs": ["close", "open"], "func": gdc_ext_037_gap_streak_ge7_flag},
    "gdc_ext_038_gap_streak_ge10_flag": {"inputs": ["close", "open"], "func": gdc_ext_038_gap_streak_ge10_flag},
    "gdc_ext_039_consec_gap_down_norm_126d": {"inputs": ["close", "open"], "func": gdc_ext_039_consec_gap_down_norm_126d},
    "gdc_ext_040_gap_down_longest_streak_126d_vs_252d": {"inputs": ["close", "open"], "func": gdc_ext_040_gap_down_longest_streak_126d_vs_252d},
    "gdc_ext_041_gap_down_pct_accel_5d": {"inputs": ["close", "open"], "func": gdc_ext_041_gap_down_pct_accel_5d},
    "gdc_ext_042_gap_down_concentration_21d": {"inputs": ["close", "open"], "func": gdc_ext_042_gap_down_concentration_21d},
    "gdc_ext_043_gap_down_concentration_63d": {"inputs": ["close", "open"], "func": gdc_ext_043_gap_down_concentration_63d},
    "gdc_ext_044_gap_down_share_of_daily_range_21d": {"inputs": ["close", "open", "high", "low"], "func": gdc_ext_044_gap_down_share_of_daily_range_21d},
    "gdc_ext_045_gap_down_pct_sum_21d_norm_close_vol": {"inputs": ["close", "open", "volume"], "func": gdc_ext_045_gap_down_pct_sum_21d_norm_close_vol},
    "gdc_ext_046_gap_down_pct_sum_63d_norm_close_vol": {"inputs": ["close", "open", "volume"], "func": gdc_ext_046_gap_down_pct_sum_63d_norm_close_vol},
    "gdc_ext_047_gap_down_count_5d_expanding_pct_rank": {"inputs": ["close", "open"], "func": gdc_ext_047_gap_down_count_5d_expanding_pct_rank},
    "gdc_ext_048_gap_down_count_21d_expanding_pct_rank": {"inputs": ["close", "open"], "func": gdc_ext_048_gap_down_count_21d_expanding_pct_rank},
    "gdc_ext_049_gap_down_mean_pct_126d": {"inputs": ["close", "open"], "func": gdc_ext_049_gap_down_mean_pct_126d},
    "gdc_ext_050_gap_down_std_63d": {"inputs": ["close", "open"], "func": gdc_ext_050_gap_down_std_63d},
    "gdc_ext_051_wide_range_gap_down_count_21d": {"inputs": ["close", "open", "high", "low"], "func": gdc_ext_051_wide_range_gap_down_count_21d},
    "gdc_ext_052_wide_range_gap_down_count_63d": {"inputs": ["close", "open", "high", "low"], "func": gdc_ext_052_wide_range_gap_down_count_63d},
    "gdc_ext_053_high_vol_wide_range_gap_down_21d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gdc_ext_053_high_vol_wide_range_gap_down_21d},
    "gdc_ext_054_gap_down_with_close_near_low_21d": {"inputs": ["close", "open", "high", "low"], "func": gdc_ext_054_gap_down_with_close_near_low_21d},
    "gdc_ext_055_gap_down_with_close_near_low_63d": {"inputs": ["close", "open", "high", "low"], "func": gdc_ext_055_gap_down_with_close_near_low_63d},
    "gdc_ext_056_gap_down_vol_zscore_on_gap_days_21d": {"inputs": ["close", "open", "volume"], "func": gdc_ext_056_gap_down_vol_zscore_on_gap_days_21d},
    "gdc_ext_057_gap_down_vol_zscore_on_gap_days_63d": {"inputs": ["close", "open", "volume"], "func": gdc_ext_057_gap_down_vol_zscore_on_gap_days_63d},
    "gdc_ext_058_gap_down_vol_surge_3x_count_63d": {"inputs": ["close", "open", "volume"], "func": gdc_ext_058_gap_down_vol_surge_3x_count_63d},
    "gdc_ext_059_gap_down_above_avg_vol_fraction_63d": {"inputs": ["close", "open", "volume"], "func": gdc_ext_059_gap_down_above_avg_vol_fraction_63d},
    "gdc_ext_060_gap_down_vol_sum_21d_norm_252d": {"inputs": ["close", "open", "volume"], "func": gdc_ext_060_gap_down_vol_sum_21d_norm_252d},
    "gdc_ext_061_exhaustion_gap_down_new_low_21d": {"inputs": ["close", "open", "low"], "func": gdc_ext_061_exhaustion_gap_down_new_low_21d},
    "gdc_ext_062_exhaustion_gap_down_new_low_63d": {"inputs": ["close", "open", "low"], "func": gdc_ext_062_exhaustion_gap_down_new_low_63d},
    "gdc_ext_063_exhaustion_gap_down_new_low_252d": {"inputs": ["close", "open", "low"], "func": gdc_ext_063_exhaustion_gap_down_new_low_252d},
    "gdc_ext_064_exhaustion_gap_count_new_low_21d_in_63d": {"inputs": ["close", "open", "low"], "func": gdc_ext_064_exhaustion_gap_count_new_low_21d_in_63d},
    "gdc_ext_065_exhaustion_gap_count_new_low_63d_in_252d": {"inputs": ["close", "open", "low"], "func": gdc_ext_065_exhaustion_gap_count_new_low_63d_in_252d},
    "gdc_ext_066_gap_down_new_low_21d_pct": {"inputs": ["close", "open", "low"], "func": gdc_ext_066_gap_down_new_low_21d_pct},
    "gdc_ext_067_gap_down_new_low_63d_pct": {"inputs": ["close", "open", "low"], "func": gdc_ext_067_gap_down_new_low_63d_pct},
    "gdc_ext_068_exhaustion_gap_flag_new_low_21d_consec": {"inputs": ["close", "open", "low"], "func": gdc_ext_068_exhaustion_gap_flag_new_low_21d_consec},
    "gdc_ext_069_gap_down_recovery_close_above_open_pct_21d": {"inputs": ["close", "open"], "func": gdc_ext_069_gap_down_recovery_close_above_open_pct_21d},
    "gdc_ext_070_gap_down_recovery_close_above_open_pct_63d": {"inputs": ["close", "open"], "func": gdc_ext_070_gap_down_recovery_close_above_open_pct_63d},
    "gdc_ext_071_gap_down_full_recovery_count_21d": {"inputs": ["close", "open"], "func": gdc_ext_071_gap_down_full_recovery_count_21d},
    "gdc_ext_072_gap_down_partial_recovery_fraction_63d": {"inputs": ["close", "open"], "func": gdc_ext_072_gap_down_partial_recovery_fraction_63d},
    "gdc_ext_073_gap_down_next_day_up_count_21d": {"inputs": ["close", "open"], "func": gdc_ext_073_gap_down_next_day_up_count_21d},
    "gdc_ext_074_gap_down_next_day_up_fraction_63d": {"inputs": ["close", "open"], "func": gdc_ext_074_gap_down_next_day_up_fraction_63d},
    "gdc_ext_075_gap_down_then_recovery_composite_21d": {"inputs": ["close", "open", "volume"], "func": gdc_ext_075_gap_down_then_recovery_composite_21d},
}
