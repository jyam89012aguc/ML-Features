"""
47_gap_down_clustering — Extended 3rd Derivatives (Features extdrv3_001-025)
Domain: rate of change of extended 2nd-derivative gap-down clustering features —
acceleration of velocity: jerk in cluster intensity z-score evolution, jerk in
island-bottom recency normalization, second-order change in exhaustion-gap
clustering at new lows, acceleration in gap-down concentration momentum,
jerk in vol-weighted gap density, slope-of-slope of cumulative magnitude trends,
and second-order dynamics of intraday recovery fractions.
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


# ── Extended 3rd-Derivative Feature Functions 001-025 ────────────────────────

# --- Group A (001-005): Jerk in island-bottom count and recency velocity ---

def gdc_extdrv3_001_island_bottom_count_5d_5d_diff_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    Second 5-day diff of 5-day island-bottom count (jerk in reversal cluster velocity).
    Captures explosive acceleration in island-bottom formation rate at the weekly scale.
    """
    cnt5 = _rolling_sum(_island_bottom_flag(close, open), _TD_WEEK)
    vel = cnt5.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_extdrv3_002_island_bottom_count_126d_21d_diff_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    5-day diff of the 21-day velocity of 126-day island-bottom count
    (jerk in medium-term reversal frequency). Detects sudden shift in half-year trend.
    """
    cnt126 = _rolling_sum(_island_bottom_flag(close, open), _TD_HALF)
    vel21 = cnt126.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def gdc_extdrv3_003_days_since_island_bottom_norm_5d_diff_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    Second 5-day diff of normalized days-since-island-bottom velocity
    (jerk in recency normalization). Sudden negative jerk = rapid clustering of islands.
    """
    ds = _days_since_island_bottom(close, open)
    normed = _safe_div(ds, _rolling_mean(ds, _TD_QTR))
    vel = normed.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_extdrv3_004_island_top_count_21d_5d_diff_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    Second 5-day diff of 21-day island-top count velocity (jerk in bearish island-top formation).
    Sudden acceleration in island-top frequency signals rapid distribution overhead.
    """
    cnt21 = _rolling_sum(_island_top_flag(close, open), _TD_MON)
    vel = cnt21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_extdrv3_005_island_top_count_252d_21d_diff_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    5-day diff of 21-day velocity of 252-day island-top count (jerk in annual supply trend).
    Captures sudden reversals in the annual bearish island-top trend direction.
    """
    cnt252 = _rolling_sum(_island_top_flag(close, open), _TD_YEAR)
    vel21 = cnt252.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# --- Group B (006-010): Jerk in cluster intensity z-score velocity ---

def gdc_extdrv3_006_gap_down_count_5d_zscore_63d_5d_diff_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    Second 5-day diff of 5d-count z-score vs 63d (jerk in statistical burst detection).
    Captures explosive second-order change in gap-cluster extremity at the weekly scale.
    """
    cnt5 = _rolling_count_true(_down_gap(close, open), _TD_WEEK)
    m = _rolling_mean(cnt5, _TD_QTR)
    s = _rolling_std(cnt5, _TD_QTR)
    z = _safe_div(cnt5 - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_extdrv3_007_gap_down_count_21d_zscore_126d_5d_diff_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    Second 5-day diff of 21d-count z-score vs 126d (jerk in monthly cluster extremity).
    Second-order change in monthly gap-cluster statistical significance.
    """
    cnt21 = _rolling_count_true(_down_gap(close, open), _TD_MON)
    m = _rolling_mean(cnt21, _TD_HALF)
    s = _rolling_std(cnt21, _TD_HALF)
    z = _safe_div(cnt21 - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_extdrv3_008_gap_down_count_63d_zscore_252d_21d_diff_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    5-day diff of 21-day velocity of 63d z-score vs 252d (jerk in quarterly extremity trend).
    Captures sudden direction changes in the quarterly gap-cluster intensity trend.
    """
    cnt63 = _rolling_count_true(_down_gap(close, open), _TD_QTR)
    m = _rolling_mean(cnt63, _TD_YEAR)
    s = _rolling_std(cnt63, _TD_YEAR)
    z = _safe_div(cnt63 - m, s)
    vel21 = z.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def gdc_extdrv3_009_cluster_intensity_score_5d_diff_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    Second 5-day diff of weighted cluster intensity score (jerk in composite z-score velocity).
    Identifies explosive second-order change in the combined burst/sustained cluster signal.
    """
    cnt5 = _rolling_count_true(_down_gap(close, open), _TD_WEEK)
    cnt21 = _rolling_count_true(_down_gap(close, open), _TD_MON)
    cnt63 = _rolling_count_true(_down_gap(close, open), _TD_QTR)
    z5 = _safe_div(cnt5 - _rolling_mean(cnt5, _TD_YEAR), _rolling_std(cnt5, _TD_YEAR))
    z21 = _safe_div(cnt21 - _rolling_mean(cnt21, _TD_YEAR), _rolling_std(cnt21, _TD_YEAR))
    z63 = _safe_div(cnt63 - _rolling_mean(cnt63, _TD_YEAR), _rolling_std(cnt63, _TD_YEAR))
    score = (3.0 * z5.fillna(0.0) + 2.0 * z21.fillna(0.0) + 1.0 * z63.fillna(0.0)) / 6.0
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_extdrv3_010_cluster_intensity_score_slope_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    5-day diff of OLS slope of cluster intensity score over 63 days (slope-of-slope).
    Captures whether the trend in cluster intensity is itself accelerating or reversing.
    """
    cnt5 = _rolling_count_true(_down_gap(close, open), _TD_WEEK)
    cnt21 = _rolling_count_true(_down_gap(close, open), _TD_MON)
    cnt63 = _rolling_count_true(_down_gap(close, open), _TD_QTR)
    z5 = _safe_div(cnt5 - _rolling_mean(cnt5, _TD_YEAR), _rolling_std(cnt5, _TD_YEAR))
    z21 = _safe_div(cnt21 - _rolling_mean(cnt21, _TD_YEAR), _rolling_std(cnt21, _TD_YEAR))
    z63 = _safe_div(cnt63 - _rolling_mean(cnt63, _TD_YEAR), _rolling_std(cnt63, _TD_YEAR))
    score = (3.0 * z5.fillna(0.0) + 2.0 * z21.fillna(0.0) + 1.0 * z63.fillna(0.0)) / 6.0
    slp = _linslope(score, _TD_QTR)
    return slp.diff(_TD_WEEK)


# --- Group C (011-014): Jerk in cumulative gap magnitude velocity ---

def gdc_extdrv3_011_cum_gap_down_pct_10d_5d_diff_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    Second 5-day diff of 10-day cumulative gap-down pct (jerk in short-window magnitude).
    Captures explosive second-order acceleration in immediate gap severity accumulation.
    """
    s10 = _rolling_sum(_down_gap_pct(close, open), 10)
    vel = s10.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_extdrv3_012_cum_gap_down_pct_126d_21d_diff_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    5-day diff of 21-day velocity of 126-day cumulative gap-down pct
    (jerk in half-year magnitude accumulation). Detects sudden shifts in long-term trend.
    """
    s126 = _rolling_sum(_down_gap_pct(close, open), _TD_HALF)
    vel21 = s126.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def gdc_extdrv3_013_cum_gap_pct_per_gap_day_21d_5d_diff_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    Second 5-day diff of average gap magnitude density over 21 days (jerk in per-gap severity).
    Captures explosive acceleration in individual gap severity as capitulation intensifies.
    """
    sum_pct = _rolling_sum(_down_gap_pct(close, open), _TD_MON)
    cnt = _rolling_count_true(_down_gap(close, open), _TD_MON)
    density = _safe_div(sum_pct, cnt)
    vel = density.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_extdrv3_014_max_gap_down_pct_126d_slope_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    5-day diff of the OLS slope of the 126-day max gap pct over 63 days (slope-of-slope).
    Captures whether the trend in worst-case gap severity is itself changing direction.
    """
    mx126 = _rolling_max(_down_gap_pct(close, open), _TD_HALF)
    slp = _linslope(mx126, _TD_QTR)
    return slp.diff(_TD_WEEK)


# --- Group E (015-018): Jerk in streak and exhaustion-gap velocity ---

def gdc_extdrv3_015_longest_gap_streak_42d_5d_diff_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    Second 5-day diff of 42-day max gap streak (jerk in 2-month worst-streak growth).
    Captures explosive second-order acceleration in multi-day gap run formation.
    """
    mx42 = _rolling_max_streak(_down_gap(close, open), 42)
    vel = mx42.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_extdrv3_016_consec_gap_down_norm_126d_5d_diff_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    Second 5-day diff of normalized gap-streak vs 126d average (jerk in relative streak).
    Detects sudden explosive change in how extreme the current streak is historically.
    """
    streak = _consec_streak(_down_gap(close, open))
    normed = _safe_div(streak, _rolling_mean(streak, _TD_HALF))
    vel = normed.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_extdrv3_017_exhaustion_gap_count_new_low_21d_in_63d_5d_diff_5d_diff(
    close: pd.Series, open: pd.Series, low: pd.Series
) -> pd.Series:
    """
    Second 5-day diff of exhaustion-gap count in 63d at 21d lows (jerk in exhaustion clustering).
    Second-order change in how fast new-low gap-downs are clustering — peak capitulation signal.
    """
    prior_low = low.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min().shift(1)
    flag = (_down_gap(close, open) & (open < prior_low)).astype(float)
    cnt63 = _rolling_sum(flag, _TD_QTR)
    vel = cnt63.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_extdrv3_018_exhaustion_gap_consec_streak_5d_diff_5d_diff(
    close: pd.Series, open: pd.Series, low: pd.Series
) -> pd.Series:
    """
    Second 5-day diff of consecutive exhaustion-gap-down streak at 21d lows
    (jerk in exhaustion streak). Captures whether the new-low gap run is explosively accelerating.
    """
    prior_low = low.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min().shift(1)
    cond = _down_gap(close, open) & (open < prior_low)
    streak = _consec_streak(cond)
    vel = streak.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group F (019-021): Jerk in gap-down concentration velocity ---

def gdc_extdrv3_019_gap_down_concentration_21d_5d_diff_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    Second 5-day diff of 21-day gap-down concentration (jerk in gap share of period loss).
    Captures second-order change in whether gaps are increasingly dominating price declines.
    """
    pct_return = _safe_div(close - close.shift(1), close.shift(1).replace(0, np.nan))
    gap_pct = _down_gap_pct(close, open)
    period_loss = (-_rolling_sum(pct_return, _TD_MON)).clip(lower=0.0)
    gap_contrib = _rolling_sum(gap_pct, _TD_MON)
    conc = _safe_div(gap_contrib, period_loss.replace(0, np.nan))
    vel = conc.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_extdrv3_020_gap_down_concentration_63d_21d_diff_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    5-day diff of 21-day velocity of 63-day gap-down concentration
    (jerk in quarterly concentration trend). Captures sudden reversals in concentration trend.
    """
    pct_return = _safe_div(close - close.shift(1), close.shift(1).replace(0, np.nan))
    gap_pct = _down_gap_pct(close, open)
    period_loss = (-_rolling_sum(pct_return, _TD_QTR)).clip(lower=0.0)
    gap_contrib = _rolling_sum(gap_pct, _TD_QTR)
    conc = _safe_div(gap_contrib, period_loss.replace(0, np.nan))
    vel21 = conc.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def gdc_extdrv3_021_wide_range_gap_down_count_63d_5d_diff_5d_diff(
    close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series
) -> pd.Series:
    """
    Second 5-day diff of wide-range gap-down count in 63d (jerk in panic-wide gap clustering).
    Captures whether wide-range-gap acceleration is itself accelerating — extreme panic signal.
    """
    cond_gap = _down_gap(close, open)
    rng = high - low
    avg_rng = _rolling_mean(rng, _TD_MON)
    wide = rng > 1.5 * avg_rng
    confluence = (cond_gap & wide).astype(float)
    cnt63 = _rolling_sum(confluence, _TD_QTR)
    vel = cnt63.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group G (022-025): Jerk in vol-weighted gap density and recovery dynamics ---

def gdc_extdrv3_022_gap_down_vol_sum_21d_norm_252d_5d_diff_5d_diff(
    close: pd.Series, open: pd.Series, volume: pd.Series
) -> pd.Series:
    """
    Second 5-day diff of normalized 21-day gap-day volume sum (jerk in volume panic signal).
    Second-order change in whether gap-day volume is explosively normalizing or collapsing.
    """
    cond = _down_gap(close, open)
    gap_vol = volume.where(cond, 0.0)
    roll21 = _rolling_sum(gap_vol, _TD_MON)
    normed = _safe_div(roll21, _rolling_mean(roll21, _TD_YEAR))
    vel = normed.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_extdrv3_023_gap_down_full_recovery_count_21d_5d_diff_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    Second 5-day diff of 21-day full-recovery gap-down count (jerk in gap-fill frequency).
    Explosive acceleration in gap-fills signals rapid exhaustion of selling pressure.
    """
    cond_gap = _down_gap(close, open)
    full_recovery = cond_gap & (close >= close.shift(1))
    cnt21 = _rolling_sum(full_recovery.astype(float), _TD_MON)
    vel = cnt21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gdc_extdrv3_024_gap_down_next_day_up_fraction_63d_slope_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    5-day diff of OLS slope of 63-day gap-up-next-day fraction over 63 days (slope-of-slope).
    Captures whether the absorption trend (gap-downs being reversed) is itself strengthening.
    """
    cond_gap = _down_gap(close, open)
    next_up = close > close.shift(1)
    follow_up = (cond_gap.shift(1, fill_value=False) & next_up).astype(float)
    cnt_follow = _rolling_sum(follow_up, _TD_QTR)
    cnt_gap = _rolling_count_true(cond_gap, _TD_QTR).replace(0, np.nan)
    frac = _safe_div(cnt_follow, cnt_gap)
    slp = _linslope(frac, _TD_QTR)
    return slp.diff(_TD_WEEK)


def gdc_extdrv3_025_cum_gap_pct_per_gap_day_63d_21d_diff_5d_diff(
    close: pd.Series, open: pd.Series
) -> pd.Series:
    """
    5-day diff of 21-day velocity of 63-day per-gap-day magnitude density
    (jerk in quarterly severity density). Captures sudden reversals in the trend of
    per-gap severity — signals transition between intensifying and abating gap-down pressure.
    """
    sum_pct = _rolling_sum(_down_gap_pct(close, open), _TD_QTR)
    cnt = _rolling_count_true(_down_gap(close, open), _TD_QTR)
    density = _safe_div(sum_pct, cnt)
    vel21 = density.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

GAP_DOWN_CLUSTERING_EXTENDED_REGISTRY_3RD_DERIVATIVES = {
    "gdc_extdrv3_001_island_bottom_count_5d_5d_diff_5d_diff": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv3_001_island_bottom_count_5d_5d_diff_5d_diff},
    "gdc_extdrv3_002_island_bottom_count_126d_21d_diff_5d_diff": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv3_002_island_bottom_count_126d_21d_diff_5d_diff},
    "gdc_extdrv3_003_days_since_island_bottom_norm_5d_diff_5d_diff": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv3_003_days_since_island_bottom_norm_5d_diff_5d_diff},
    "gdc_extdrv3_004_island_top_count_21d_5d_diff_5d_diff": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv3_004_island_top_count_21d_5d_diff_5d_diff},
    "gdc_extdrv3_005_island_top_count_252d_21d_diff_5d_diff": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv3_005_island_top_count_252d_21d_diff_5d_diff},
    "gdc_extdrv3_006_gap_down_count_5d_zscore_63d_5d_diff_5d_diff": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv3_006_gap_down_count_5d_zscore_63d_5d_diff_5d_diff},
    "gdc_extdrv3_007_gap_down_count_21d_zscore_126d_5d_diff_5d_diff": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv3_007_gap_down_count_21d_zscore_126d_5d_diff_5d_diff},
    "gdc_extdrv3_008_gap_down_count_63d_zscore_252d_21d_diff_5d_diff": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv3_008_gap_down_count_63d_zscore_252d_21d_diff_5d_diff},
    "gdc_extdrv3_009_cluster_intensity_score_5d_diff_5d_diff": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv3_009_cluster_intensity_score_5d_diff_5d_diff},
    "gdc_extdrv3_010_cluster_intensity_score_slope_5d_diff": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv3_010_cluster_intensity_score_slope_5d_diff},
    "gdc_extdrv3_011_cum_gap_down_pct_10d_5d_diff_5d_diff": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv3_011_cum_gap_down_pct_10d_5d_diff_5d_diff},
    "gdc_extdrv3_012_cum_gap_down_pct_126d_21d_diff_5d_diff": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv3_012_cum_gap_down_pct_126d_21d_diff_5d_diff},
    "gdc_extdrv3_013_cum_gap_pct_per_gap_day_21d_5d_diff_5d_diff": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv3_013_cum_gap_pct_per_gap_day_21d_5d_diff_5d_diff},
    "gdc_extdrv3_014_max_gap_down_pct_126d_slope_5d_diff": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv3_014_max_gap_down_pct_126d_slope_5d_diff},
    "gdc_extdrv3_015_longest_gap_streak_42d_5d_diff_5d_diff": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv3_015_longest_gap_streak_42d_5d_diff_5d_diff},
    "gdc_extdrv3_016_consec_gap_down_norm_126d_5d_diff_5d_diff": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv3_016_consec_gap_down_norm_126d_5d_diff_5d_diff},
    "gdc_extdrv3_017_exhaustion_gap_count_new_low_21d_in_63d_5d_diff_5d_diff": {
        "inputs": ["close", "open", "low"],
        "func": gdc_extdrv3_017_exhaustion_gap_count_new_low_21d_in_63d_5d_diff_5d_diff},
    "gdc_extdrv3_018_exhaustion_gap_consec_streak_5d_diff_5d_diff": {
        "inputs": ["close", "open", "low"],
        "func": gdc_extdrv3_018_exhaustion_gap_consec_streak_5d_diff_5d_diff},
    "gdc_extdrv3_019_gap_down_concentration_21d_5d_diff_5d_diff": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv3_019_gap_down_concentration_21d_5d_diff_5d_diff},
    "gdc_extdrv3_020_gap_down_concentration_63d_21d_diff_5d_diff": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv3_020_gap_down_concentration_63d_21d_diff_5d_diff},
    "gdc_extdrv3_021_wide_range_gap_down_count_63d_5d_diff_5d_diff": {
        "inputs": ["close", "open", "high", "low"],
        "func": gdc_extdrv3_021_wide_range_gap_down_count_63d_5d_diff_5d_diff},
    "gdc_extdrv3_022_gap_down_vol_sum_21d_norm_252d_5d_diff_5d_diff": {
        "inputs": ["close", "open", "volume"],
        "func": gdc_extdrv3_022_gap_down_vol_sum_21d_norm_252d_5d_diff_5d_diff},
    "gdc_extdrv3_023_gap_down_full_recovery_count_21d_5d_diff_5d_diff": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv3_023_gap_down_full_recovery_count_21d_5d_diff_5d_diff},
    "gdc_extdrv3_024_gap_down_next_day_up_fraction_63d_slope_5d_diff": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv3_024_gap_down_next_day_up_fraction_63d_slope_5d_diff},
    "gdc_extdrv3_025_cum_gap_pct_per_gap_day_63d_21d_diff_5d_diff": {
        "inputs": ["close", "open"],
        "func": gdc_extdrv3_025_cum_gap_pct_per_gap_day_63d_21d_diff_5d_diff},
}
