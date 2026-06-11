"""
27_momentum_exhaustion — Extended Features ext_001-075
Domain: loss of downside momentum — deceleration / exhaustion of the decline
Extended coverage: deeper ROC/Kaufman-ER/TD-DeMark variants (additional lookbacks,
thresholds, z-scores, percentile ranks, regime flags), TD sequential countdown
(13-count) and perfected-setup features, ROC-of-ROC and momentum-deceleration
confluence, exhaustion composites combining multiple momentum measures, and
rate-of-change & acceleration variants of these indicators.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Self-contained: numpy/pandas only; no cross-file imports.
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_ret(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS)).diff(1)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _down_ret_abs(close: pd.Series) -> pd.Series:
    """Absolute daily log-return on down days; NaN otherwise."""
    r = _log_ret(close)
    return r.abs().where(r < 0, np.nan)


def _roc(close: pd.Series, n: int) -> pd.Series:
    """Rate of Change: (close / close.shift(n) - 1) * 100."""
    return _safe_div(close, close.shift(n).replace(0, np.nan)) * 100.0 - 100.0


def _kaufman_er(close: pd.Series, n: int) -> pd.Series:
    """Kaufman Efficiency Ratio over n periods (0=choppy, 1=trending)."""
    direction = (close - close.shift(n)).abs()
    volatility = close.diff(1).abs().rolling(n, min_periods=max(2, n // 2)).sum()
    return _safe_div(direction, volatility)


def _td_buy_setup_count(close: pd.Series) -> pd.Series:
    """
    TD/DeMark buy-setup running count (backward-looking only).
    Increments each bar where close < close.shift(4); resets otherwise.
    Count capped at 13.
    """
    condition = (close < close.shift(4)).astype(int).values
    n = len(condition)
    counts = np.full(n, np.nan, dtype=float)
    running = 0
    for i in range(4, n):
        if np.isnan(close.iloc[i]) or np.isnan(close.iloc[i - 4]):
            running = 0
            counts[i] = np.nan
        elif condition[i] == 1:
            running = min(running + 1, 13)
            counts[i] = float(running)
        else:
            running = 0
            counts[i] = 0.0
    return pd.Series(counts, index=close.index)


def _td_countdown_count(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """
    TD Sequential countdown (backward-looking only).
    Countdown condition: close <= low.shift(2).
    Starts counting only after a completed buy setup (count >= 9 from _td_buy_setup_count).
    Counter increments toward 13, then resets when a new setup completes.
    Returns running countdown count (0-13); NaN before first setup completion.
    """
    setup = _td_buy_setup_count(close).values
    cd_cond = (close <= low.shift(2)).astype(int).values
    n = len(close)
    counts = np.full(n, np.nan, dtype=float)
    in_countdown = False
    cd_count = 0
    for i in range(n):
        if np.isnan(setup[i]):
            in_countdown = False
            cd_count = 0
            counts[i] = np.nan
            continue
        # New completed setup resets countdown
        if setup[i] >= 9.0:
            in_countdown = True
            cd_count = 0
        if in_countdown:
            if cd_cond[i] == 1:
                cd_count = min(cd_count + 1, 13)
            counts[i] = float(cd_count)
        else:
            counts[i] = np.nan
    return pd.Series(counts, index=close.index)


def _td_perfected_setup_flag_arr(close: pd.Series, low: pd.Series) -> pd.Series:
    """
    TD Perfected Buy Setup flag (backward-looking only).
    A setup is perfected when the low on bar 8 or bar 9 of the setup is <= the low
    on bar 6 or bar 7. Returns 1 on the perfecting bar, 0 otherwise, NaN before bar 9.
    """
    setup = _td_buy_setup_count(close).values
    low_vals = low.values
    n = len(close)
    flags = np.full(n, np.nan, dtype=float)
    # track bar index within current setup
    bar_lows = {}  # bar_number -> low_value for current setup
    for i in range(n):
        s = setup[i]
        if np.isnan(s):
            bar_lows = {}
            flags[i] = np.nan
            continue
        bar_num = int(s)
        if bar_num == 0:
            bar_lows = {}
            flags[i] = 0.0
            continue
        bar_lows[bar_num] = low_vals[i]
        if bar_num >= 9:
            low_8 = bar_lows.get(8, np.nan)
            low_9 = bar_lows.get(9, np.nan)
            low_6 = bar_lows.get(6, np.nan)
            low_7 = bar_lows.get(7, np.nan)
            ref_low = min(v for v in [low_6, low_7] if not np.isnan(v)) if any(
                not np.isnan(v) for v in [low_6, low_7]) else np.nan
            cand_low = min(v for v in [low_8, low_9] if not np.isnan(v)) if any(
                not np.isnan(v) for v in [low_8, low_9]) else np.nan
            if np.isnan(ref_low) or np.isnan(cand_low):
                flags[i] = 0.0
            else:
                flags[i] = 1.0 if cand_low <= ref_low else 0.0
        else:
            flags[i] = 0.0
    return pd.Series(flags, index=close.index)


# ── Extended Feature Functions ext_001-075 ────────────────────────────────────

# --- Group A (ext_001-010): ROC deeper lookbacks, thresholds, and regime flags ---

def mex_ext_001_roc_3d(close: pd.Series) -> pd.Series:
    """Rate of Change 3-day: ultra-short momentum pulse."""
    return _roc(close, 3)


def mex_ext_002_roc_42d(close: pd.Series) -> pd.Series:
    """Rate of Change 42-day: between monthly and quarterly."""
    return _roc(close, 42)


def mex_ext_003_roc_5d_threshold_neg5_flag(close: pd.Series) -> pd.Series:
    """Flag (0/1): 5-day ROC <= -5% (severe short-term momentum selloff)."""
    roc5 = _roc(close, _TD_WEEK)
    return (roc5 <= -5.0).astype(float)


def mex_ext_004_roc_21d_threshold_neg15_flag(close: pd.Series) -> pd.Series:
    """Flag (0/1): 21-day ROC <= -15% (severe monthly momentum washout)."""
    roc21 = _roc(close, _TD_MON)
    return (roc21 <= -15.0).astype(float)


def mex_ext_005_roc_63d_threshold_neg25_flag(close: pd.Series) -> pd.Series:
    """Flag (0/1): 63-day ROC <= -25% (quarterly momentum in bear territory)."""
    roc63 = _roc(close, _TD_QTR)
    return (roc63 <= -25.0).astype(float)


def mex_ext_006_roc_5d_zscore_126d(close: pd.Series) -> pd.Series:
    """Z-score of 5-day ROC within its trailing 126-day distribution."""
    roc5 = _roc(close, _TD_WEEK)
    m = _rolling_mean(roc5, _TD_HALF)
    s = _rolling_std(roc5, _TD_HALF)
    return _safe_div(roc5 - m, s)


def mex_ext_007_roc_21d_zscore_126d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day ROC within its trailing 126-day distribution."""
    roc21 = _roc(close, _TD_MON)
    m = _rolling_mean(roc21, _TD_HALF)
    s = _rolling_std(roc21, _TD_HALF)
    return _safe_div(roc21 - m, s)


def mex_ext_008_roc_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day ROC within its trailing 252-day distribution."""
    roc63 = _roc(close, _TD_QTR)
    m = _rolling_mean(roc63, _TD_YEAR)
    s = _rolling_std(roc63, _TD_YEAR)
    return _safe_div(roc63 - m, s)


def mex_ext_009_roc_5d_pct_rank_126d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5-day ROC within its trailing 126-day distribution."""
    roc5 = _roc(close, _TD_WEEK)
    return roc5.rolling(_TD_HALF, min_periods=_TD_MON).rank(pct=True)


def mex_ext_010_roc_21d_pct_rank_126d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day ROC within its trailing 126-day distribution."""
    roc21 = _roc(close, _TD_MON)
    return roc21.rolling(_TD_HALF, min_periods=_TD_MON).rank(pct=True)


# --- Group B (ext_011-018): ROC negative streak counts and regime flags ---

def mex_ext_011_roc_5d_neg_streak(close: pd.Series) -> pd.Series:
    """Consecutive bars where 5-day ROC < 0 (running count, resets on positive)."""
    roc5 = _roc(close, _TD_WEEK)
    is_neg = (roc5 < 0).astype(int).values
    n = len(is_neg)
    result = np.zeros(n, dtype=float)
    streak = 0
    for i in range(n):
        if np.isnan(roc5.iloc[i]):
            streak = 0
            result[i] = np.nan
        elif is_neg[i] == 1:
            streak += 1
            result[i] = float(streak)
        else:
            streak = 0
            result[i] = 0.0
    return pd.Series(result, index=close.index)


def mex_ext_012_roc_21d_neg_streak(close: pd.Series) -> pd.Series:
    """Consecutive bars where 21-day ROC < 0 (running count, resets on positive)."""
    roc21 = _roc(close, _TD_MON)
    is_neg = (roc21 < 0).astype(int).values
    n = len(is_neg)
    result = np.zeros(n, dtype=float)
    streak = 0
    for i in range(n):
        if np.isnan(roc21.iloc[i]):
            streak = 0
            result[i] = np.nan
        elif is_neg[i] == 1:
            streak += 1
            result[i] = float(streak)
        else:
            streak = 0
            result[i] = 0.0
    return pd.Series(result, index=close.index)


def mex_ext_013_roc_63d_neg_streak(close: pd.Series) -> pd.Series:
    """Consecutive bars where 63-day ROC < 0 (running count, resets on positive)."""
    roc63 = _roc(close, _TD_QTR)
    is_neg = (roc63 < 0).astype(int).values
    n = len(is_neg)
    result = np.zeros(n, dtype=float)
    streak = 0
    for i in range(n):
        if np.isnan(roc63.iloc[i]):
            streak = 0
            result[i] = np.nan
        elif is_neg[i] == 1:
            streak += 1
            result[i] = float(streak)
        else:
            streak = 0
            result[i] = 0.0
    return pd.Series(result, index=close.index)


def mex_ext_014_roc_5d_neg_streak_zscore_126d(close: pd.Series) -> pd.Series:
    """Z-score of 5-day ROC negative streak within its 126-day distribution."""
    roc5 = _roc(close, _TD_WEEK)
    is_neg = (roc5 < 0).astype(int).values
    n = len(is_neg)
    streak_arr = np.zeros(n, dtype=float)
    streak = 0
    for i in range(n):
        if np.isnan(roc5.iloc[i]):
            streak = 0
            streak_arr[i] = np.nan
        elif is_neg[i] == 1:
            streak += 1
            streak_arr[i] = float(streak)
        else:
            streak = 0
            streak_arr[i] = 0.0
    s = pd.Series(streak_arr, index=close.index)
    m = _rolling_mean(s.fillna(0.0), _TD_HALF)
    sd = _rolling_std(s.fillna(0.0), _TD_HALF)
    return _safe_div(s - m, sd)


def mex_ext_015_roc_5d_positive_crossover_rate_21d(close: pd.Series) -> pd.Series:
    """Fraction of last 21 bars where 5-day ROC crossed from negative to non-negative."""
    roc5 = _roc(close, _TD_WEEK)
    cross = ((roc5 >= 0) & (roc5.shift(1) < 0)).astype(float)
    return _rolling_mean(cross, _TD_MON)


def mex_ext_016_roc_5d_improving_streak(close: pd.Series) -> pd.Series:
    """Consecutive bars where 5-day ROC is higher than prior bar (momentum improving streak)."""
    roc5 = _roc(close, _TD_WEEK)
    improving = (roc5 > roc5.shift(1)).astype(int).values
    n = len(improving)
    result = np.zeros(n, dtype=float)
    streak = 0
    for i in range(n):
        if np.isnan(roc5.iloc[i]) or np.isnan(roc5.iloc[i - 1] if i > 0 else np.nan):
            streak = 0
            result[i] = np.nan
        elif improving[i] == 1:
            streak += 1
            result[i] = float(streak)
        else:
            streak = 0
            result[i] = 0.0
    return pd.Series(result, index=close.index)


def mex_ext_017_roc_21d_range_position_252d(close: pd.Series) -> pd.Series:
    """Position of 21-day ROC within its 252-day min-max range (0=at min, 1=at max)."""
    roc21 = _roc(close, _TD_MON)
    rmin = _rolling_min(roc21, _TD_YEAR)
    rmax = _rolling_max(roc21, _TD_YEAR)
    return _safe_div(roc21 - rmin, (rmax - rmin).replace(0, np.nan))


def mex_ext_018_roc_63d_range_position_252d(close: pd.Series) -> pd.Series:
    """Position of 63-day ROC within its 252-day min-max range."""
    roc63 = _roc(close, _TD_QTR)
    rmin = _rolling_min(roc63, _TD_YEAR)
    rmax = _rolling_max(roc63, _TD_YEAR)
    return _safe_div(roc63 - rmin, (rmax - rmin).replace(0, np.nan))


# --- Group C (ext_019-026): Kaufman ER deeper lookbacks, z-scores, thresholds ---

def mex_ext_019_kaufman_er_5d(close: pd.Series) -> pd.Series:
    """Kaufman Efficiency Ratio 5-day: shortest ER; low = ultra-choppy."""
    return _kaufman_er(close, _TD_WEEK)


def mex_ext_020_kaufman_er_42d(close: pd.Series) -> pd.Series:
    """Kaufman Efficiency Ratio 42-day: between monthly and quarterly ER."""
    return _kaufman_er(close, 42)


def mex_ext_021_kaufman_er_126d(close: pd.Series) -> pd.Series:
    """Kaufman Efficiency Ratio 126-day (semi-annual): low = half-year choppiness."""
    return _kaufman_er(close, _TD_HALF)


def mex_ext_022_kaufman_er_5d_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of Kaufman ER (5d) within trailing 63-day distribution."""
    er5 = _kaufman_er(close, _TD_WEEK)
    m = _rolling_mean(er5, _TD_QTR)
    s = _rolling_std(er5, _TD_QTR)
    return _safe_div(er5 - m, s)


def mex_ext_023_kaufman_er_21d_zscore_126d(close: pd.Series) -> pd.Series:
    """Z-score of Kaufman ER (21d) within trailing 126-day distribution."""
    er21 = _kaufman_er(close, _TD_MON)
    m = _rolling_mean(er21, _TD_HALF)
    s = _rolling_std(er21, _TD_HALF)
    return _safe_div(er21 - m, s)


def mex_ext_024_kaufman_er_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of Kaufman ER (63d) within trailing 252-day distribution."""
    er63 = _kaufman_er(close, _TD_QTR)
    m = _rolling_mean(er63, _TD_YEAR)
    s = _rolling_std(er63, _TD_YEAR)
    return _safe_div(er63 - m, s)


def mex_ext_025_kaufman_er_5d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of Kaufman ER (5d) in trailing 252-day distribution."""
    er5 = _kaufman_er(close, _TD_WEEK)
    return er5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def mex_ext_026_kaufman_er_42d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of Kaufman ER (42d) in trailing 252-day distribution."""
    er42 = _kaufman_er(close, 42)
    return er42.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group D (ext_027-034): Kaufman ER regime flags and cross-period ratios ---

def mex_ext_027_kaufman_er_5d_below_thresh_flag(close: pd.Series) -> pd.Series:
    """Flag (0/1): Kaufman ER (5d) < 0.2 — ultra-choppy regime (exhaustion plateau)."""
    er5 = _kaufman_er(close, _TD_WEEK)
    return (er5 < 0.2).astype(float)


def mex_ext_028_kaufman_er_21d_below_thresh_flag(close: pd.Series) -> pd.Series:
    """Flag (0/1): Kaufman ER (21d) < 0.25 — monthly choppiness regime."""
    er21 = _kaufman_er(close, _TD_MON)
    return (er21 < 0.25).astype(float)


def mex_ext_029_kaufman_er_5d_vs_21d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of Kaufman ER (5d) to ER (21d): <1 = short-term choppier than medium."""
    er5 = _kaufman_er(close, _TD_WEEK)
    er21 = _kaufman_er(close, _TD_MON)
    return _safe_div(er5, er21)


def mex_ext_030_kaufman_er_21d_vs_63d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of Kaufman ER (21d) to ER (63d): cross-period efficiency comparison."""
    er21 = _kaufman_er(close, _TD_MON)
    er63 = _kaufman_er(close, _TD_QTR)
    return _safe_div(er21, er63)


def mex_ext_031_kaufman_er_63d_vs_126d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of Kaufman ER (63d) to ER (126d)."""
    er63 = _kaufman_er(close, _TD_QTR)
    er126 = _kaufman_er(close, _TD_HALF)
    return _safe_div(er63, er126)


def mex_ext_032_kaufman_er_5d_neg_streak(close: pd.Series) -> pd.Series:
    """Consecutive bars where Kaufman ER (5d) < 0.3 (choppy plateau streak)."""
    er5 = _kaufman_er(close, _TD_WEEK)
    is_low = (er5 < 0.3).astype(int).values
    n = len(is_low)
    result = np.zeros(n, dtype=float)
    streak = 0
    for i in range(n):
        if np.isnan(er5.iloc[i]):
            streak = 0
            result[i] = np.nan
        elif is_low[i] == 1:
            streak += 1
            result[i] = float(streak)
        else:
            streak = 0
            result[i] = 0.0
    return pd.Series(result, index=close.index)


def mex_ext_033_kaufman_er_21d_slope_126d(close: pd.Series) -> pd.Series:
    """OLS slope of Kaufman ER (21d) over 126 days: longer-term ER trend."""
    er21 = _kaufman_er(close, _TD_MON)
    def _slope(x):
        if len(x) < max(2, _TD_HALF // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        return np.nan if den == 0 else num / den
    return er21.rolling(_TD_HALF, min_periods=max(2, _TD_HALF // 2)).apply(_slope, raw=False)


def mex_ext_034_kaufman_er_10d_acceleration_5d(close: pd.Series) -> pd.Series:
    """5-day diff of (5-day diff of Kaufman ER 10d): ER acceleration signal."""
    er10 = _kaufman_er(close, 10)
    vel = er10.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group E (ext_035-046): TD Sequential extended — countdown, perfected setup ---

def mex_ext_035_td_countdown_count(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """TD Sequential countdown count (0-13): bars with close <= low.shift(2) after setup >= 9."""
    return _td_countdown_count(close, low, high)


def mex_ext_036_td_countdown_13_flag(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Flag (0/1): TD countdown count == 13 (classic countdown completion = buy signal)."""
    cd = _td_countdown_count(close, low, high)
    return (cd == 13.0).astype(float)


def mex_ext_037_td_countdown_gte9_flag(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Flag (0/1): TD countdown count >= 9 (countdown in late stage)."""
    cd = _td_countdown_count(close, low, high)
    return (cd >= 9.0).astype(float)


def mex_ext_038_td_countdown_zscore_63d(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Z-score of TD countdown count within its trailing 63-day distribution."""
    cd = _td_countdown_count(close, low, high).fillna(0.0)
    m = _rolling_mean(cd, _TD_QTR)
    s = _rolling_std(cd, _TD_QTR)
    return _safe_div(cd - m, s)


def mex_ext_039_td_countdown_pct_rank_252d(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Percentile rank of TD countdown count in trailing 252-day distribution."""
    cd = _td_countdown_count(close, low, high).fillna(0.0)
    return cd.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def mex_ext_040_td_countdown_slope_21d(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """OLS slope of TD countdown count over 21 days."""
    cd = _td_countdown_count(close, low, high).fillna(0.0)
    def _slope(x):
        if len(x) < max(2, _TD_MON // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        return np.nan if den == 0 else num / den
    return cd.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).apply(_slope, raw=False)


def mex_ext_041_td_countdown_bars_since_13(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Bars since last TD countdown of 13 was hit; NaN if never. Capped at 126."""
    cd = _td_countdown_count(close, low, high)
    n = len(cd)
    result = np.full(n, np.nan, dtype=float)
    last_hit = -1
    for i in range(n):
        if cd.iloc[i] == 13.0:
            last_hit = i
            result[i] = 0.0
        elif last_hit >= 0:
            result[i] = float(min(i - last_hit, 126))
    return pd.Series(result, index=close.index)


def mex_ext_042_td_perfected_setup_flag(close: pd.Series, low: pd.Series) -> pd.Series:
    """Flag (0/1): TD Perfected Buy Setup — low on bar 8 or 9 <= low on bar 6 or 7."""
    return _td_perfected_setup_flag_arr(close, low)


def mex_ext_043_td_perfected_setup_rate_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Rolling 63-day rate of TD Perfected Buy Setup flags (frequency of perfected setups)."""
    flag = _td_perfected_setup_flag_arr(close, low).fillna(0.0)
    return _rolling_mean(flag, _TD_QTR)


def mex_ext_044_td_setup_gt5_flag(close: pd.Series) -> pd.Series:
    """Flag (0/1): TD buy-setup count > 5 (setup more than half complete)."""
    counts = _td_buy_setup_count(close)
    return (counts > 5.0).astype(float)


def mex_ext_045_td_setup_count_pct_rank_126d(close: pd.Series) -> pd.Series:
    """Percentile rank of TD buy-setup count in trailing 126-day distribution."""
    counts = _td_buy_setup_count(close).fillna(0.0)
    return counts.rolling(_TD_HALF, min_periods=_TD_MON).rank(pct=True)


def mex_ext_046_td_buy_condition_rate_63d(close: pd.Series) -> pd.Series:
    """Rolling 63-day fraction of bars with close < close.shift(4) (long-window TD buy rate)."""
    cond = (close < close.shift(4)).astype(float)
    return _rolling_mean(cond, _TD_QTR)


# --- Group F (ext_047-054): ROC-of-ROC (2nd order ROC) momentum deceleration ---

def mex_ext_047_roc_of_roc_5d_5d(close: pd.Series) -> pd.Series:
    """ROC of ROC: 5-day ROC of the 5-day ROC series (deceleration of short momentum)."""
    roc5 = _roc(close, _TD_WEEK)
    return _safe_div(roc5, roc5.shift(_TD_WEEK).replace(0, np.nan)) * 100.0 - 100.0


def mex_ext_048_roc_of_roc_21d_21d(close: pd.Series) -> pd.Series:
    """ROC of ROC: 21-day ROC of the 21-day ROC series."""
    roc21 = _roc(close, _TD_MON)
    return _safe_div(roc21, roc21.shift(_TD_MON).replace(0, np.nan)) * 100.0 - 100.0


def mex_ext_049_roc_of_roc_5d_21d(close: pd.Series) -> pd.Series:
    """21-day ROC of the 5-day ROC series (medium-term view of short momentum change)."""
    roc5 = _roc(close, _TD_WEEK)
    return _safe_div(roc5, roc5.shift(_TD_MON).replace(0, np.nan)) * 100.0 - 100.0


def mex_ext_050_roc_of_roc_5d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of (5-day ROC of 5-day ROC) over 21 days."""
    roc5 = _roc(close, _TD_WEEK)
    roc_of_roc = _safe_div(roc5, roc5.shift(_TD_WEEK).replace(0, np.nan)) * 100.0 - 100.0
    def _slope(x):
        if len(x) < max(2, _TD_MON // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        return np.nan if den == 0 else num / den
    return roc_of_roc.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).apply(_slope, raw=False)


def mex_ext_051_roc_of_roc_5d_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of (5d ROC of 5d ROC) within 63-day distribution."""
    roc5 = _roc(close, _TD_WEEK)
    roc_of_roc = _safe_div(roc5, roc5.shift(_TD_WEEK).replace(0, np.nan)) * 100.0 - 100.0
    m = _rolling_mean(roc_of_roc, _TD_QTR)
    s = _rolling_std(roc_of_roc, _TD_QTR)
    return _safe_div(roc_of_roc - m, s)


def mex_ext_052_roc_of_kaufman_er_10d_5d(close: pd.Series) -> pd.Series:
    """5-day ROC of Kaufman ER (10d): momentum of the efficiency ratio itself."""
    er10 = _kaufman_er(close, 10)
    return _safe_div(er10, er10.shift(_TD_WEEK).replace(0, np.nan)) * 100.0 - 100.0


def mex_ext_053_roc_of_kaufman_er_21d_21d(close: pd.Series) -> pd.Series:
    """21-day ROC of Kaufman ER (21d): medium-term momentum of efficiency."""
    er21 = _kaufman_er(close, _TD_MON)
    return _safe_div(er21, er21.shift(_TD_MON).replace(0, np.nan)) * 100.0 - 100.0


def mex_ext_054_roc_of_td_setup_count_5d(close: pd.Series) -> pd.Series:
    """5-day change rate of TD buy-setup count (normalized by prior count)."""
    counts = _td_buy_setup_count(close).fillna(0.0)
    prior = counts.shift(_TD_WEEK).replace(0, np.nan)
    return _safe_div(counts - prior, prior)


# --- Group G (ext_055-062): Momentum deceleration confluence features ---

def mex_ext_055_roc5_and_er10_decel_confluence(close: pd.Series) -> pd.Series:
    """Confluence score: (1 if 5d ROC improving) + (1 if ER-10d rising) scaled to [0,1]."""
    roc5 = _roc(close, _TD_WEEK)
    roc5_improv = (roc5 > roc5.shift(1)).astype(float)
    er10 = _kaufman_er(close, 10)
    er10_rising = (er10 > er10.shift(1)).astype(float)
    return (roc5_improv + er10_rising) / 2.0


def mex_ext_056_roc21_and_er21_low_regime_confluence(close: pd.Series) -> pd.Series:
    """Confluence: (1 if 21d ROC < 0) + (1 if ER-21d < 0.3) — deep negative but stalling."""
    roc21 = _roc(close, _TD_MON)
    neg = (roc21 < 0).astype(float)
    er21 = _kaufman_er(close, _TD_MON)
    choppy = (er21 < 0.3).astype(float)
    return (neg + choppy) / 2.0


def mex_ext_057_td_setup_and_roc_neg_confluence(close: pd.Series) -> pd.Series:
    """Confluence: TD setup >= 6 AND 21d ROC < -10% (advanced setup during deep decline)."""
    counts = _td_buy_setup_count(close)
    setup_adv = (counts >= 6.0).astype(float)
    roc21 = _roc(close, _TD_MON)
    deep_dn = (roc21 < -10.0).astype(float)
    return (setup_adv + deep_dn) / 2.0


def mex_ext_058_td_setup9_and_er_low_confluence(close: pd.Series) -> pd.Series:
    """Confluence: TD setup == 9 AND Kaufman ER-21d < 0.35 (completed setup + choppy)."""
    counts = _td_buy_setup_count(close)
    setup9 = (counts >= 9.0).astype(float)
    er21 = _kaufman_er(close, _TD_MON)
    low_er = (er21 < 0.35).astype(float)
    return (setup9 + low_er) / 2.0


def mex_ext_059_triple_roc_decel_confluence(close: pd.Series) -> pd.Series:
    """Confluence of 5d, 21d, 63d ROC all improving vs prior bar (3-period decel signal)."""
    roc5 = _roc(close, _TD_WEEK)
    roc21 = _roc(close, _TD_MON)
    roc63 = _roc(close, _TD_QTR)
    imp5 = (roc5 > roc5.shift(1)).astype(float)
    imp21 = (roc21 > roc21.shift(1)).astype(float)
    imp63 = (roc63 > roc63.shift(1)).astype(float)
    return (imp5 + imp21 + imp63) / 3.0


def mex_ext_060_er_convergence_confluence(close: pd.Series) -> pd.Series:
    """Confluence: ER-5d, ER-21d, ER-63d all < 0.4 (multi-horizon choppiness = exhaustion plateau)."""
    er5 = _kaufman_er(close, _TD_WEEK)
    er21 = _kaufman_er(close, _TD_MON)
    er63 = _kaufman_er(close, _TD_QTR)
    low5 = (er5 < 0.4).astype(float)
    low21 = (er21 < 0.4).astype(float)
    low63 = (er63 < 0.4).astype(float)
    return (low5 + low21 + low63) / 3.0


def mex_ext_061_roc_er_td_triple_confluence(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Triple confluence: 21d ROC improving + ER-21 < 0.35 + TD countdown > 0 (multi-signal)."""
    roc21 = _roc(close, _TD_MON)
    roc_imp = (roc21 > roc21.shift(1)).astype(float)
    er21 = _kaufman_er(close, _TD_MON)
    er_low = (er21 < 0.35).astype(float)
    cd = _td_countdown_count(close, low, high).fillna(0.0)
    cd_active = (cd > 0).astype(float)
    return (roc_imp + er_low + cd_active) / 3.0


def mex_ext_062_roc_neg_streak_and_setup_confluence(close: pd.Series) -> pd.Series:
    """Confluence of 21d ROC negative streak >= 5 AND TD setup >= 5 (persistent momentum weakness + setup building)."""
    roc21 = _roc(close, _TD_MON)
    is_neg = (roc21 < 0).astype(int).values
    n = len(is_neg)
    streak_arr = np.zeros(n, dtype=float)
    streak = 0
    for i in range(n):
        if np.isnan(roc21.iloc[i]):
            streak = 0
            streak_arr[i] = np.nan
        elif is_neg[i] == 1:
            streak += 1
            streak_arr[i] = float(streak)
        else:
            streak = 0
            streak_arr[i] = 0.0
    streak_s = pd.Series(streak_arr, index=close.index)
    long_streak = (streak_s >= 5).astype(float)
    counts = _td_buy_setup_count(close).fillna(0.0)
    setup_adv = (counts >= 5).astype(float)
    return (long_streak + setup_adv) / 2.0


# --- Group H (ext_063-070): Exhaustion composites combining multiple measures ---

def mex_ext_063_exhaustion_composite_roc_er_5d(close: pd.Series) -> pd.Series:
    """Composite of z-scored 5d ROC + z-scored ER-10d (both normalized, averaged)."""
    roc5 = _roc(close, _TD_WEEK)
    m_r = _rolling_mean(roc5, _TD_QTR)
    s_r = _rolling_std(roc5, _TD_QTR)
    z_roc = _safe_div(roc5 - m_r, s_r)

    er10 = _kaufman_er(close, 10)
    m_e = _rolling_mean(er10, _TD_QTR)
    s_e = _rolling_std(er10, _TD_QTR)
    z_er = _safe_div(er10 - m_e, s_e)

    return (z_roc + z_er) / 2.0


def mex_ext_064_exhaustion_composite_21d(close: pd.Series) -> pd.Series:
    """Composite: z-scored 21d ROC + z-scored ER-21d + z-scored TD-setup-count (3 signals avg)."""
    roc21 = _roc(close, _TD_MON)
    m_r = _rolling_mean(roc21, _TD_QTR)
    s_r = _rolling_std(roc21, _TD_QTR)
    z_roc = _safe_div(roc21 - m_r, s_r)

    er21 = _kaufman_er(close, _TD_MON)
    m_e = _rolling_mean(er21, _TD_QTR)
    s_e = _rolling_std(er21, _TD_QTR)
    z_er = _safe_div(er21 - m_e, s_e)

    counts = _td_buy_setup_count(close).fillna(0.0)
    m_t = _rolling_mean(counts, _TD_QTR)
    s_t = _rolling_std(counts, _TD_QTR)
    z_td = _safe_div(counts - m_t, s_t)

    return (z_roc + z_er + z_td) / 3.0


def mex_ext_065_exhaustion_composite_pct_rank(close: pd.Series) -> pd.Series:
    """Mean of 252d pct-ranks: 5d ROC + ER-21d + TD-setup (rank-based composite)."""
    roc5 = _roc(close, _TD_WEEK)
    rk_roc = roc5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    er21 = _kaufman_er(close, _TD_MON)
    rk_er = er21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    counts = _td_buy_setup_count(close).fillna(0.0)
    rk_td = counts.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (rk_roc + rk_er + rk_td) / 3.0


def mex_ext_066_exhaustion_composite_slope_21d(close: pd.Series) -> pd.Series:
    """Composite of slopes: OLS slope-21d of (5d ROC + ER-10d + TD-setup-count) avg."""
    roc5 = _roc(close, _TD_WEEK)
    er10 = _kaufman_er(close, 10)
    counts = _td_buy_setup_count(close).fillna(0.0)

    def _slope(x):
        if len(x) < max(2, _TD_MON // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean(); x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        return np.nan if den == 0 else num / den

    slp_roc = roc5.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).apply(_slope, raw=False)
    slp_er = er10.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).apply(_slope, raw=False)
    slp_td = counts.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).apply(_slope, raw=False)
    return (slp_roc + slp_er + slp_td) / 3.0


def mex_ext_067_exhaustion_multi_signal_flag(close: pd.Series) -> pd.Series:
    """Multi-signal exhaustion flag: sum of (5d ROC neg + ER-21<0.3 + TD-setup>=6 + 63d ROC neg) / 4."""
    roc5 = _roc(close, _TD_WEEK)
    roc63 = _roc(close, _TD_QTR)
    er21 = _kaufman_er(close, _TD_MON)
    counts = _td_buy_setup_count(close).fillna(0.0)
    sig1 = (roc5 < 0).astype(float)
    sig2 = (er21 < 0.3).astype(float)
    sig3 = (counts >= 6).astype(float)
    sig4 = (roc63 < 0).astype(float)
    return (sig1 + sig2 + sig3 + sig4) / 4.0


def mex_ext_068_exhaustion_composite_ema_smoothed(close: pd.Series) -> pd.Series:
    """EMA-5 smoothed version of the 21d exhaustion composite (ext_064)."""
    roc21 = _roc(close, _TD_MON)
    m_r = _rolling_mean(roc21, _TD_QTR)
    s_r = _rolling_std(roc21, _TD_QTR)
    z_roc = _safe_div(roc21 - m_r, s_r)

    er21 = _kaufman_er(close, _TD_MON)
    m_e = _rolling_mean(er21, _TD_QTR)
    s_e = _rolling_std(er21, _TD_QTR)
    z_er = _safe_div(er21 - m_e, s_e)

    counts = _td_buy_setup_count(close).fillna(0.0)
    m_t = _rolling_mean(counts, _TD_QTR)
    s_t = _rolling_std(counts, _TD_QTR)
    z_td = _safe_div(counts - m_t, s_t)

    composite = (z_roc + z_er + z_td) / 3.0
    return _ewm_mean(composite.fillna(0.0), _TD_WEEK)


def mex_ext_069_roc_er_divergence_score(close: pd.Series) -> pd.Series:
    """Divergence: ER-21d improving while 21d ROC still falling (stall without bounce)."""
    roc21 = _roc(close, _TD_MON)
    er21 = _kaufman_er(close, _TD_MON)
    roc_falling = (roc21 < roc21.shift(1)).astype(float)
    er_rising = (er21 > er21.shift(1)).astype(float)
    return roc_falling * er_rising  # 1 only when ER rising but ROC still falling


def mex_ext_070_countdown_setup_progress_composite(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Combined TD progress score: (setup_count/13 + countdown_count/13) / 2 in [0,1]."""
    setup = _td_buy_setup_count(close).fillna(0.0)
    cd = _td_countdown_count(close, low, high).fillna(0.0)
    return (setup / 13.0 + cd / 13.0) / 2.0


# --- Group I (ext_071-075): Rate-of-change and acceleration variants ---

def mex_ext_071_roc_5d_acceleration_21d(close: pd.Series) -> pd.Series:
    """21-day OLS slope of (5-day diff of 5-day ROC): acceleration of short momentum."""
    roc5 = _roc(close, _TD_WEEK)
    vel = roc5.diff(_TD_WEEK)
    def _slope(x):
        if len(x) < max(2, _TD_MON // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean(); x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        return np.nan if den == 0 else num / den
    return vel.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).apply(_slope, raw=False)


def mex_ext_072_roc_21d_acceleration_63d(close: pd.Series) -> pd.Series:
    """63-day OLS slope of (21-day diff of 21-day ROC): acceleration of medium momentum."""
    roc21 = _roc(close, _TD_MON)
    vel = roc21.diff(_TD_MON)
    def _slope(x):
        if len(x) < max(2, _TD_QTR // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean(); x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        return np.nan if den == 0 else num / den
    return vel.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_slope, raw=False)


def mex_ext_073_kaufman_er_21d_acceleration_63d(close: pd.Series) -> pd.Series:
    """63-day OLS slope of (21-day diff of ER-21d): acceleration of efficiency trend."""
    er21 = _kaufman_er(close, _TD_MON)
    vel = er21.diff(_TD_MON)
    def _slope(x):
        if len(x) < max(2, _TD_QTR // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean(); x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        return np.nan if den == 0 else num / den
    return vel.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_slope, raw=False)


def mex_ext_074_td_setup_count_acceleration_5d(close: pd.Series) -> pd.Series:
    """5-day change in the 5-day change of TD buy-setup count (2nd derivative of setup count)."""
    counts = _td_buy_setup_count(close).fillna(0.0)
    vel = counts.diff(1)
    return vel.diff(_TD_WEEK)


def mex_ext_075_exhaustion_composite_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """252-day pct rank of the 21d exhaustion composite (ext_064 formula, ranked)."""
    roc21 = _roc(close, _TD_MON)
    m_r = _rolling_mean(roc21, _TD_QTR)
    s_r = _rolling_std(roc21, _TD_QTR)
    z_roc = _safe_div(roc21 - m_r, s_r)

    er21 = _kaufman_er(close, _TD_MON)
    m_e = _rolling_mean(er21, _TD_QTR)
    s_e = _rolling_std(er21, _TD_QTR)
    z_er = _safe_div(er21 - m_e, s_e)

    counts = _td_buy_setup_count(close).fillna(0.0)
    m_t = _rolling_mean(counts, _TD_QTR)
    s_t = _rolling_std(counts, _TD_QTR)
    z_td = _safe_div(counts - m_t, s_t)

    composite = ((z_roc.fillna(0.0) + z_er.fillna(0.0) + z_td.fillna(0.0)) / 3.0)
    return composite.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

MOMENTUM_EXHAUSTION_EXTENDED_REGISTRY_001_075 = {
    "mex_ext_001_roc_3d": {"inputs": ["close"], "func": mex_ext_001_roc_3d},
    "mex_ext_002_roc_42d": {"inputs": ["close"], "func": mex_ext_002_roc_42d},
    "mex_ext_003_roc_5d_threshold_neg5_flag": {"inputs": ["close"], "func": mex_ext_003_roc_5d_threshold_neg5_flag},
    "mex_ext_004_roc_21d_threshold_neg15_flag": {"inputs": ["close"], "func": mex_ext_004_roc_21d_threshold_neg15_flag},
    "mex_ext_005_roc_63d_threshold_neg25_flag": {"inputs": ["close"], "func": mex_ext_005_roc_63d_threshold_neg25_flag},
    "mex_ext_006_roc_5d_zscore_126d": {"inputs": ["close"], "func": mex_ext_006_roc_5d_zscore_126d},
    "mex_ext_007_roc_21d_zscore_126d": {"inputs": ["close"], "func": mex_ext_007_roc_21d_zscore_126d},
    "mex_ext_008_roc_63d_zscore_252d": {"inputs": ["close"], "func": mex_ext_008_roc_63d_zscore_252d},
    "mex_ext_009_roc_5d_pct_rank_126d": {"inputs": ["close"], "func": mex_ext_009_roc_5d_pct_rank_126d},
    "mex_ext_010_roc_21d_pct_rank_126d": {"inputs": ["close"], "func": mex_ext_010_roc_21d_pct_rank_126d},
    "mex_ext_011_roc_5d_neg_streak": {"inputs": ["close"], "func": mex_ext_011_roc_5d_neg_streak},
    "mex_ext_012_roc_21d_neg_streak": {"inputs": ["close"], "func": mex_ext_012_roc_21d_neg_streak},
    "mex_ext_013_roc_63d_neg_streak": {"inputs": ["close"], "func": mex_ext_013_roc_63d_neg_streak},
    "mex_ext_014_roc_5d_neg_streak_zscore_126d": {"inputs": ["close"], "func": mex_ext_014_roc_5d_neg_streak_zscore_126d},
    "mex_ext_015_roc_5d_positive_crossover_rate_21d": {"inputs": ["close"], "func": mex_ext_015_roc_5d_positive_crossover_rate_21d},
    "mex_ext_016_roc_5d_improving_streak": {"inputs": ["close"], "func": mex_ext_016_roc_5d_improving_streak},
    "mex_ext_017_roc_21d_range_position_252d": {"inputs": ["close"], "func": mex_ext_017_roc_21d_range_position_252d},
    "mex_ext_018_roc_63d_range_position_252d": {"inputs": ["close"], "func": mex_ext_018_roc_63d_range_position_252d},
    "mex_ext_019_kaufman_er_5d": {"inputs": ["close"], "func": mex_ext_019_kaufman_er_5d},
    "mex_ext_020_kaufman_er_42d": {"inputs": ["close"], "func": mex_ext_020_kaufman_er_42d},
    "mex_ext_021_kaufman_er_126d": {"inputs": ["close"], "func": mex_ext_021_kaufman_er_126d},
    "mex_ext_022_kaufman_er_5d_zscore_63d": {"inputs": ["close"], "func": mex_ext_022_kaufman_er_5d_zscore_63d},
    "mex_ext_023_kaufman_er_21d_zscore_126d": {"inputs": ["close"], "func": mex_ext_023_kaufman_er_21d_zscore_126d},
    "mex_ext_024_kaufman_er_63d_zscore_252d": {"inputs": ["close"], "func": mex_ext_024_kaufman_er_63d_zscore_252d},
    "mex_ext_025_kaufman_er_5d_pct_rank_252d": {"inputs": ["close"], "func": mex_ext_025_kaufman_er_5d_pct_rank_252d},
    "mex_ext_026_kaufman_er_42d_pct_rank_252d": {"inputs": ["close"], "func": mex_ext_026_kaufman_er_42d_pct_rank_252d},
    "mex_ext_027_kaufman_er_5d_below_thresh_flag": {"inputs": ["close"], "func": mex_ext_027_kaufman_er_5d_below_thresh_flag},
    "mex_ext_028_kaufman_er_21d_below_thresh_flag": {"inputs": ["close"], "func": mex_ext_028_kaufman_er_21d_below_thresh_flag},
    "mex_ext_029_kaufman_er_5d_vs_21d_ratio": {"inputs": ["close"], "func": mex_ext_029_kaufman_er_5d_vs_21d_ratio},
    "mex_ext_030_kaufman_er_21d_vs_63d_ratio": {"inputs": ["close"], "func": mex_ext_030_kaufman_er_21d_vs_63d_ratio},
    "mex_ext_031_kaufman_er_63d_vs_126d_ratio": {"inputs": ["close"], "func": mex_ext_031_kaufman_er_63d_vs_126d_ratio},
    "mex_ext_032_kaufman_er_5d_neg_streak": {"inputs": ["close"], "func": mex_ext_032_kaufman_er_5d_neg_streak},
    "mex_ext_033_kaufman_er_21d_slope_126d": {"inputs": ["close"], "func": mex_ext_033_kaufman_er_21d_slope_126d},
    "mex_ext_034_kaufman_er_10d_acceleration_5d": {"inputs": ["close"], "func": mex_ext_034_kaufman_er_10d_acceleration_5d},
    "mex_ext_035_td_countdown_count": {"inputs": ["close", "low", "high"], "func": mex_ext_035_td_countdown_count},
    "mex_ext_036_td_countdown_13_flag": {"inputs": ["close", "low", "high"], "func": mex_ext_036_td_countdown_13_flag},
    "mex_ext_037_td_countdown_gte9_flag": {"inputs": ["close", "low", "high"], "func": mex_ext_037_td_countdown_gte9_flag},
    "mex_ext_038_td_countdown_zscore_63d": {"inputs": ["close", "low", "high"], "func": mex_ext_038_td_countdown_zscore_63d},
    "mex_ext_039_td_countdown_pct_rank_252d": {"inputs": ["close", "low", "high"], "func": mex_ext_039_td_countdown_pct_rank_252d},
    "mex_ext_040_td_countdown_slope_21d": {"inputs": ["close", "low", "high"], "func": mex_ext_040_td_countdown_slope_21d},
    "mex_ext_041_td_countdown_bars_since_13": {"inputs": ["close", "low", "high"], "func": mex_ext_041_td_countdown_bars_since_13},
    "mex_ext_042_td_perfected_setup_flag": {"inputs": ["close", "low"], "func": mex_ext_042_td_perfected_setup_flag},
    "mex_ext_043_td_perfected_setup_rate_63d": {"inputs": ["close", "low"], "func": mex_ext_043_td_perfected_setup_rate_63d},
    "mex_ext_044_td_setup_gt5_flag": {"inputs": ["close"], "func": mex_ext_044_td_setup_gt5_flag},
    "mex_ext_045_td_setup_count_pct_rank_126d": {"inputs": ["close"], "func": mex_ext_045_td_setup_count_pct_rank_126d},
    "mex_ext_046_td_buy_condition_rate_63d": {"inputs": ["close"], "func": mex_ext_046_td_buy_condition_rate_63d},
    "mex_ext_047_roc_of_roc_5d_5d": {"inputs": ["close"], "func": mex_ext_047_roc_of_roc_5d_5d},
    "mex_ext_048_roc_of_roc_21d_21d": {"inputs": ["close"], "func": mex_ext_048_roc_of_roc_21d_21d},
    "mex_ext_049_roc_of_roc_5d_21d": {"inputs": ["close"], "func": mex_ext_049_roc_of_roc_5d_21d},
    "mex_ext_050_roc_of_roc_5d_slope_21d": {"inputs": ["close"], "func": mex_ext_050_roc_of_roc_5d_slope_21d},
    "mex_ext_051_roc_of_roc_5d_zscore_63d": {"inputs": ["close"], "func": mex_ext_051_roc_of_roc_5d_zscore_63d},
    "mex_ext_052_roc_of_kaufman_er_10d_5d": {"inputs": ["close"], "func": mex_ext_052_roc_of_kaufman_er_10d_5d},
    "mex_ext_053_roc_of_kaufman_er_21d_21d": {"inputs": ["close"], "func": mex_ext_053_roc_of_kaufman_er_21d_21d},
    "mex_ext_054_roc_of_td_setup_count_5d": {"inputs": ["close"], "func": mex_ext_054_roc_of_td_setup_count_5d},
    "mex_ext_055_roc5_and_er10_decel_confluence": {"inputs": ["close"], "func": mex_ext_055_roc5_and_er10_decel_confluence},
    "mex_ext_056_roc21_and_er21_low_regime_confluence": {"inputs": ["close"], "func": mex_ext_056_roc21_and_er21_low_regime_confluence},
    "mex_ext_057_td_setup_and_roc_neg_confluence": {"inputs": ["close"], "func": mex_ext_057_td_setup_and_roc_neg_confluence},
    "mex_ext_058_td_setup9_and_er_low_confluence": {"inputs": ["close"], "func": mex_ext_058_td_setup9_and_er_low_confluence},
    "mex_ext_059_triple_roc_decel_confluence": {"inputs": ["close"], "func": mex_ext_059_triple_roc_decel_confluence},
    "mex_ext_060_er_convergence_confluence": {"inputs": ["close"], "func": mex_ext_060_er_convergence_confluence},
    "mex_ext_061_roc_er_td_triple_confluence": {"inputs": ["close", "low", "high"], "func": mex_ext_061_roc_er_td_triple_confluence},
    "mex_ext_062_roc_neg_streak_and_setup_confluence": {"inputs": ["close"], "func": mex_ext_062_roc_neg_streak_and_setup_confluence},
    "mex_ext_063_exhaustion_composite_roc_er_5d": {"inputs": ["close"], "func": mex_ext_063_exhaustion_composite_roc_er_5d},
    "mex_ext_064_exhaustion_composite_21d": {"inputs": ["close"], "func": mex_ext_064_exhaustion_composite_21d},
    "mex_ext_065_exhaustion_composite_pct_rank": {"inputs": ["close"], "func": mex_ext_065_exhaustion_composite_pct_rank},
    "mex_ext_066_exhaustion_composite_slope_21d": {"inputs": ["close"], "func": mex_ext_066_exhaustion_composite_slope_21d},
    "mex_ext_067_exhaustion_multi_signal_flag": {"inputs": ["close"], "func": mex_ext_067_exhaustion_multi_signal_flag},
    "mex_ext_068_exhaustion_composite_ema_smoothed": {"inputs": ["close"], "func": mex_ext_068_exhaustion_composite_ema_smoothed},
    "mex_ext_069_roc_er_divergence_score": {"inputs": ["close"], "func": mex_ext_069_roc_er_divergence_score},
    "mex_ext_070_countdown_setup_progress_composite": {"inputs": ["close", "low", "high"], "func": mex_ext_070_countdown_setup_progress_composite},
    "mex_ext_071_roc_5d_acceleration_21d": {"inputs": ["close"], "func": mex_ext_071_roc_5d_acceleration_21d},
    "mex_ext_072_roc_21d_acceleration_63d": {"inputs": ["close"], "func": mex_ext_072_roc_21d_acceleration_63d},
    "mex_ext_073_kaufman_er_21d_acceleration_63d": {"inputs": ["close"], "func": mex_ext_073_kaufman_er_21d_acceleration_63d},
    "mex_ext_074_td_setup_count_acceleration_5d": {"inputs": ["close"], "func": mex_ext_074_td_setup_count_acceleration_5d},
    "mex_ext_075_exhaustion_composite_21d_pct_rank_252d": {"inputs": ["close"], "func": mex_ext_075_exhaustion_composite_21d_pct_rank_252d},
}
