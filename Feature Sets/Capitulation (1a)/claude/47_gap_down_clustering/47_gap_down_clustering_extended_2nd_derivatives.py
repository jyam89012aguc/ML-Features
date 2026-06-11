"""
47_gap_down_clustering — Extended 2nd Derivatives (Features extdrv2_001-025)
Domain: rate of change of extended base gap-down clustering concepts — velocity of
island-bottom width/depth/return dynamics, cluster intensity z-score evolution,
cumulative gap magnitude rate of change, exhaustion-gap streak velocity, gap-down
concentration momentum, wide-range-gap confluence acceleration, vol-weighted gap
density dynamics, and intraday recovery trend velocity.
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


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


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
    """Maximum consecutive-True run length over trailing w periods."""
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


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


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
    """Island-bottom: gap-down 1-5 bars ago + gap-up today. Backward-looking."""
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


# ── Extended 2nd-Derivative Feature Functions 001-025 ────────────────────────

# --- Group A (001-005): Island-bottom dynamics — velocity of width, depth, return, and recency ---

def gdc_extdrv2_001_island_bottom_count_5d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    5-day diff of the 5-day island-bottom rolling count (gdc_ext_006 base concept).
    Captures velocity of island-reversal cluster formation at the shortest window.
    """
    cnt5 = _rolling_sum(_island_bottom_flag(close, open), _TD_WEEK)
    return cnt5.diff(_TD_WEEK)


def gdc_extdrv2_002_island_bottom_count_126d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    21-day diff of the 126-day island-bottom rolling count (gdc_ext_007 base concept).
    Measures medium-term velocity: is island-reversal frequency rising over the half-year?
    """
    cnt126 = _rolling_sum(_island_bottom_flag(close, open), _TD_HALF)
    return cnt126.diff(_TD_MON)


def gdc_extdrv2_003_days_since_island_bottom_norm_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    5-day diff of normalized days-since-island-bottom (gdc_ext_008 base concept).
    Falling values = normalized recency is shrinking, island bottoms are clustering.
    """
    ds = _days_since_island_bottom(close, open)
    normed = _safe_div(ds, _rolling_mean(ds, _TD_QTR))
    return normed.diff(_TD_WEEK)


def gdc_extdrv2_004_island_top_count_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    5-day diff of 21-day island-top count (gdc_ext_009 base concept).
    Velocity of bearish island-top activity — rising = accumulating overhead supply.
    """
    cnt21 = _rolling_sum(_island_top_flag(close, open), _TD_MON)
    return cnt21.diff(_TD_WEEK)


def gdc_extdrv2_005_island_top_count_252d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    21-day diff of 252-day island-top count (gdc_ext_010 base concept).
    Measures whether bearish island-top frequency is increasing on an annual basis.
    """
    cnt252 = _rolling_sum(_island_top_flag(close, open), _TD_YEAR)
    return cnt252.diff(_TD_MON)


# --- Group B (006-010): Cluster intensity z-score velocity ---

def gdc_extdrv2_006_gap_down_count_5d_zscore_63d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    5-day diff of the 5d-count z-score vs 63d distribution (gdc_ext_011 base concept).
    Velocity of statistical burst detection: rising = cluster just became extreme.
    """
    cnt5 = _rolling_count_true(_down_gap(close, open), _TD_WEEK)
    m = _rolling_mean(cnt5, _TD_QTR)
    s = _rolling_std(cnt5, _TD_QTR)
    z = _safe_div(cnt5 - m, s)
    return z.diff(_TD_WEEK)


def gdc_extdrv2_007_gap_down_count_21d_zscore_126d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    5-day diff of the 21d-count z-score vs 126d distribution (gdc_ext_012 base concept).
    Detects whether the monthly gap-cluster is statistically accelerating this week.
    """
    cnt21 = _rolling_count_true(_down_gap(close, open), _TD_MON)
    m = _rolling_mean(cnt21, _TD_HALF)
    s = _rolling_std(cnt21, _TD_HALF)
    z = _safe_div(cnt21 - m, s)
    return z.diff(_TD_WEEK)


def gdc_extdrv2_008_gap_down_count_63d_zscore_252d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    21-day diff of the 63d-count z-score vs 252d distribution (gdc_ext_013 base concept).
    Monthly velocity of quarterly extremity — rising = persistent cluster intensification.
    """
    cnt63 = _rolling_count_true(_down_gap(close, open), _TD_QTR)
    m = _rolling_mean(cnt63, _TD_YEAR)
    s = _rolling_std(cnt63, _TD_YEAR)
    z = _safe_div(cnt63 - m, s)
    return z.diff(_TD_MON)


def gdc_extdrv2_009_cluster_intensity_score_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    5-day diff of the weighted cluster intensity score (gdc_ext_019 base concept).
    Velocity of the composite z-score: positive = intensity accelerating this week.
    """
    cnt5 = _rolling_count_true(_down_gap(close, open), _TD_WEEK)
    cnt21 = _rolling_count_true(_down_gap(close, open), _TD_MON)
    cnt63 = _rolling_count_true(_down_gap(close, open), _TD_QTR)
    z5 = _safe_div(cnt5 - _rolling_mean(cnt5, _TD_YEAR), _rolling_std(cnt5, _TD_YEAR))
    z21 = _safe_div(cnt21 - _rolling_mean(cnt21, _TD_YEAR), _rolling_std(cnt21, _TD_YEAR))
    z63 = _safe_div(cnt63 - _rolling_mean(cnt63, _TD_YEAR), _rolling_std(cnt63, _TD_YEAR))
    score = (3.0 * z5.fillna(0.0) + 2.0 * z21.fillna(0.0) + 1.0 * z63.fillna(0.0)) / 6.0
    return score.diff(_TD_WEEK)


def gdc_extdrv2_010_cluster_intensity_score_slope_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    OLS slope of the cluster intensity score over 63 days (gdc_ext_019 base concept).
    Trend of the composite z-score: positive slope = intensifying cluster trend.
    """
    cnt5 = _rolling_count_true(_down_gap(close, open), _TD_WEEK)
    cnt21 = _rolling_count_true(_down_gap(close, open), _TD_MON)
    cnt63 = _rolling_count_true(_down_gap(close, open), _TD_QTR)
    z5 = _safe_div(cnt5 - _rolling_mean(cnt5, _TD_YEAR), _rolling_std(cnt5, _TD_YEAR))
    z21 = _safe_div(cnt21 - _rolling_mean(cnt21, _TD_YEAR), _rolling_std(cnt21, _TD_YEAR))
    z63 = _safe_div(cnt63 - _rolling_mean(cnt63, _TD_YEAR), _rolling_std(cnt63, _TD_YEAR))
    score = (3.0 * z5.fillna(0.0) + 2.0 * z21.fillna(0.0) + 1.0 * z63.fillna(0.0)) / 6.0
    return _linslope(score, _TD_QTR)


# --- Group C (011-015): Cumulative gap magnitude velocity ---

def gdc_extdrv2_011_cum_gap_down_pct_10d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    5-day diff of the 10-day cumulative gap-down pct (gdc_ext_021 base concept).
    Velocity of short-window gap magnitude accumulation.
    """
    s10 = _rolling_sum(_down_gap_pct(close, open), 10)
    return s10.diff(_TD_WEEK)


def gdc_extdrv2_012_cum_gap_down_pct_126d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    21-day diff of the 126-day cumulative gap-down pct (gdc_ext_022 base concept).
    Monthly velocity of half-year gap severity accumulation.
    """
    s126 = _rolling_sum(_down_gap_pct(close, open), _TD_HALF)
    return s126.diff(_TD_MON)


def gdc_extdrv2_013_cum_gap_pct_per_gap_day_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    5-day diff of average gap-down pct per gap-day over 21 days (gdc_ext_026 base concept).
    Captures whether individual gap severity is increasing or decreasing recently.
    """
    sum_pct = _rolling_sum(_down_gap_pct(close, open), _TD_MON)
    cnt = _rolling_count_true(_down_gap(close, open), _TD_MON)
    density = _safe_div(sum_pct, cnt)
    return density.diff(_TD_WEEK)


def gdc_extdrv2_014_cum_gap_pct_per_gap_day_63d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    21-day diff of average gap-down pct per gap-day over 63 days (gdc_ext_027 base concept).
    Monthly velocity of quarterly magnitude density — rising = gap severity intensifying.
    """
    sum_pct = _rolling_sum(_down_gap_pct(close, open), _TD_QTR)
    cnt = _rolling_count_true(_down_gap(close, open), _TD_QTR)
    density = _safe_div(sum_pct, cnt)
    return density.diff(_TD_MON)


def gdc_extdrv2_015_max_gap_down_pct_126d_slope_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    OLS slope of the 126-day maximum gap-down pct over 63 days (gdc_ext_029 base concept).
    Trend in worst-case single-day gap severity over the half-year window.
    """
    mx126 = _rolling_max(_down_gap_pct(close, open), _TD_HALF)
    return _linslope(mx126, _TD_QTR)


# --- Group D (016-019): Consecutive streak and exhaustion-gap velocity ---

def gdc_extdrv2_016_longest_gap_streak_42d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    5-day diff of the 42-day maximum consecutive gap-streak (gdc_ext_034 base concept).
    Velocity of the 2-month worst-streak: rising = new multi-day gap runs emerging.
    """
    mx42 = _rolling_max_streak(_down_gap(close, open), 42)
    return mx42.diff(_TD_WEEK)


def gdc_extdrv2_017_consec_gap_down_norm_126d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    5-day diff of current gap-streak normalized by 126-day average (gdc_ext_039 base).
    Velocity of normalized streak: positive = relative streak intensity growing.
    """
    streak = _consec_streak(_down_gap(close, open))
    normed = _safe_div(streak, _rolling_mean(streak, _TD_HALF))
    return normed.diff(_TD_WEEK)


def gdc_extdrv2_018_exhaustion_gap_count_new_low_21d_in_63d_5d_diff(
    close: pd.Series, open: pd.Series, low: pd.Series
) -> pd.Series:
    """
    5-day diff of exhaustion-gap count (open < prior 21d low) in trailing 63d
    (gdc_ext_064 base concept). Velocity of exhaustion-gap clustering at new lows.
    """
    prior_low = low.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min().shift(1)
    flag = (_down_gap(close, open) & (open < prior_low)).astype(float)
    cnt63 = _rolling_sum(flag, _TD_QTR)
    return cnt63.diff(_TD_WEEK)


def gdc_extdrv2_019_exhaustion_gap_consec_streak_5d_diff(
    close: pd.Series, open: pd.Series, low: pd.Series
) -> pd.Series:
    """
    5-day diff of consecutive exhaustion-gap-down streak at 21d lows (gdc_ext_068 base).
    Velocity of the sustained exhaustion run: rising = new-low gaps compounding.
    """
    prior_low = low.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min().shift(1)
    cond = _down_gap(close, open) & (open < prior_low)
    streak = _consec_streak(cond)
    return streak.diff(_TD_WEEK)


# --- Group E (020-022): Gap-down concentration and wide-range velocity ---

def gdc_extdrv2_020_gap_down_concentration_21d_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    5-day diff of the 21-day gap-down concentration (gdc_ext_042 base concept).
    Velocity of gap share of period decline — rising = gaps driving more of the loss.
    """
    pct_return = _safe_div(close - close.shift(1), close.shift(1).replace(0, np.nan))
    gap_pct = _down_gap_pct(close, open)
    period_loss = (-_rolling_sum(pct_return, _TD_MON)).clip(lower=0.0)
    gap_contrib = _rolling_sum(gap_pct, _TD_MON)
    conc = _safe_div(gap_contrib, period_loss.replace(0, np.nan))
    return conc.diff(_TD_WEEK)


def gdc_extdrv2_021_gap_down_concentration_63d_21d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """
    21-day diff of the 63-day gap-down concentration (gdc_ext_043 base concept).
    Monthly velocity: rising = gaps increasingly dominate quarterly decline.
    """
    pct_return = _safe_div(close - close.shift(1), close.shift(1).replace(0, np.nan))
    gap_pct = _down_gap_pct(close, open)
    period_loss = (-_rolling_sum(pct_return, _TD_QTR)).clip(lower=0.0)
    gap_contrib = _rolling_sum(gap_pct, _TD_QTR)
    conc = _safe_div(gap_contrib, period_loss.replace(0, np.nan))
    return conc.diff(_TD_MON)


def gdc_extdrv2_022_wide_range_gap_down_count_63d_5d_diff(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """
    5-day diff of wide-range gap-down count over 63 days (gdc_ext_052 base concept).
    Weekly velocity: positive = panic-wide gap-down events are accelerating.
    """
    cond_gap = _down_gap(close, open)
    rng = high - low
    avg_rng = _rolling_mean(rng, _TD_MON)
    wide = rng > 1.5 * avg_rng
    confluence = (cond_gap & wide).astype(float)
    cnt63 = _rolling_sum(confluence, _TD_QTR)
    return cnt63.diff(_TD_WEEK)


# --- Group F (023-025): Intraday recovery and vol-weighted gap velocity ---

def gdc_extdrv2_023_gap_down_vol_sum_21d_norm_252d_5d_diff(
    close: pd.Series, open: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    5-day diff of 21-day gap-day volume sum normalized by 252-day average (gdc_ext_060 base).
    Velocity of historically elevated gap-day volume: rising = volume panic accelerating.
    """
    cond = _down_gap(close, open)
    gap_vol = volume.where(cond, 0.0)
    roll21 = _rolling_sum(gap_vol, _TD_MON)
    normed = _safe_div(roll21, _rolling_mean(roll21, _TD_YEAR))
    return normed.diff(_TD_WEEK)


def gdc_extdrv2_024_gap_down_full_recovery_count_21d_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    5-day diff of 21-day full-recovery gap-down count (gdc_ext_071 base concept).
    Velocity of gap-fill events: rising = intraday recoveries accelerating (exhaustion signal).
    """
    cond_gap = _down_gap(close, open)
    full_recovery = cond_gap & (close >= close.shift(1))
    cnt21 = _rolling_sum(full_recovery.astype(float), _TD_MON)
    return cnt21.diff(_TD_WEEK)


def gdc_extdrv2_025_gap_down_next_day_up_fraction_63d_slope_63d(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    OLS slope of the fraction of gap-down days followed by a higher close (63d)
    over a 63-day window (gdc_ext_074 base concept). Rising slope = capitulation
    absorption trend: gap-downs are increasingly being reversed the next session.
    """
    cond_gap = _down_gap(close, open)
    next_up = close > close.shift(1)
    follow_up = (cond_gap.shift(1, fill_value=False) & next_up).astype(float)
    cnt_follow = _rolling_sum(follow_up, _TD_QTR)
    cnt_gap = _rolling_count_true(cond_gap, _TD_QTR).replace(0, np.nan)
    frac = _safe_div(cnt_follow, cnt_gap)
    return _linslope(frac, _TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

GAP_DOWN_CLUSTERING_EXTENDED_REGISTRY_2ND_DERIVATIVES = {
    "gdc_extdrv2_001_island_bottom_count_5d_5d_diff": {
        "inputs": ["close", "open"], "func": gdc_extdrv2_001_island_bottom_count_5d_5d_diff},
    "gdc_extdrv2_002_island_bottom_count_126d_21d_diff": {
        "inputs": ["close", "open"], "func": gdc_extdrv2_002_island_bottom_count_126d_21d_diff},
    "gdc_extdrv2_003_days_since_island_bottom_norm_5d_diff": {
        "inputs": ["close", "open"], "func": gdc_extdrv2_003_days_since_island_bottom_norm_5d_diff},
    "gdc_extdrv2_004_island_top_count_21d_5d_diff": {
        "inputs": ["close", "open"], "func": gdc_extdrv2_004_island_top_count_21d_5d_diff},
    "gdc_extdrv2_005_island_top_count_252d_21d_diff": {
        "inputs": ["close", "open"], "func": gdc_extdrv2_005_island_top_count_252d_21d_diff},
    "gdc_extdrv2_006_gap_down_count_5d_zscore_63d_5d_diff": {
        "inputs": ["close", "open"], "func": gdc_extdrv2_006_gap_down_count_5d_zscore_63d_5d_diff},
    "gdc_extdrv2_007_gap_down_count_21d_zscore_126d_5d_diff": {
        "inputs": ["close", "open"], "func": gdc_extdrv2_007_gap_down_count_21d_zscore_126d_5d_diff},
    "gdc_extdrv2_008_gap_down_count_63d_zscore_252d_21d_diff": {
        "inputs": ["close", "open"], "func": gdc_extdrv2_008_gap_down_count_63d_zscore_252d_21d_diff},
    "gdc_extdrv2_009_cluster_intensity_score_5d_diff": {
        "inputs": ["close", "open"], "func": gdc_extdrv2_009_cluster_intensity_score_5d_diff},
    "gdc_extdrv2_010_cluster_intensity_score_slope_63d": {
        "inputs": ["close", "open"], "func": gdc_extdrv2_010_cluster_intensity_score_slope_63d},
    "gdc_extdrv2_011_cum_gap_down_pct_10d_5d_diff": {
        "inputs": ["close", "open"], "func": gdc_extdrv2_011_cum_gap_down_pct_10d_5d_diff},
    "gdc_extdrv2_012_cum_gap_down_pct_126d_21d_diff": {
        "inputs": ["close", "open"], "func": gdc_extdrv2_012_cum_gap_down_pct_126d_21d_diff},
    "gdc_extdrv2_013_cum_gap_pct_per_gap_day_21d_5d_diff": {
        "inputs": ["close", "open"], "func": gdc_extdrv2_013_cum_gap_pct_per_gap_day_21d_5d_diff},
    "gdc_extdrv2_014_cum_gap_pct_per_gap_day_63d_21d_diff": {
        "inputs": ["close", "open"], "func": gdc_extdrv2_014_cum_gap_pct_per_gap_day_63d_21d_diff},
    "gdc_extdrv2_015_max_gap_down_pct_126d_slope_63d": {
        "inputs": ["close", "open"], "func": gdc_extdrv2_015_max_gap_down_pct_126d_slope_63d},
    "gdc_extdrv2_016_longest_gap_streak_42d_5d_diff": {
        "inputs": ["close", "open"], "func": gdc_extdrv2_016_longest_gap_streak_42d_5d_diff},
    "gdc_extdrv2_017_consec_gap_down_norm_126d_5d_diff": {
        "inputs": ["close", "open"], "func": gdc_extdrv2_017_consec_gap_down_norm_126d_5d_diff},
    "gdc_extdrv2_018_exhaustion_gap_count_new_low_21d_in_63d_5d_diff": {
        "inputs": ["close", "open", "low"],
        "func": gdc_extdrv2_018_exhaustion_gap_count_new_low_21d_in_63d_5d_diff},
    "gdc_extdrv2_019_exhaustion_gap_consec_streak_5d_diff": {
        "inputs": ["close", "open", "low"],
        "func": gdc_extdrv2_019_exhaustion_gap_consec_streak_5d_diff},
    "gdc_extdrv2_020_gap_down_concentration_21d_5d_diff": {
        "inputs": ["close", "open"], "func": gdc_extdrv2_020_gap_down_concentration_21d_5d_diff},
    "gdc_extdrv2_021_gap_down_concentration_63d_21d_diff": {
        "inputs": ["close", "open"], "func": gdc_extdrv2_021_gap_down_concentration_63d_21d_diff},
    "gdc_extdrv2_022_wide_range_gap_down_count_63d_5d_diff": {
        "inputs": ["close", "open", "high", "low"],
        "func": gdc_extdrv2_022_wide_range_gap_down_count_63d_5d_diff},
    "gdc_extdrv2_023_gap_down_vol_sum_21d_norm_252d_5d_diff": {
        "inputs": ["close", "open", "volume"],
        "func": gdc_extdrv2_023_gap_down_vol_sum_21d_norm_252d_5d_diff},
    "gdc_extdrv2_024_gap_down_full_recovery_count_21d_5d_diff": {
        "inputs": ["close", "open"], "func": gdc_extdrv2_024_gap_down_full_recovery_count_21d_5d_diff},
    "gdc_extdrv2_025_gap_down_next_day_up_fraction_63d_slope_63d": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv2_025_gap_down_next_day_up_fraction_63d_slope_63d},
}
