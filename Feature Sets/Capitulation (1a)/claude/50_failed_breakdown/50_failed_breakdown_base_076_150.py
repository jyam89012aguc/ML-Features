"""
50_failed_breakdown — Base Features 076-150
Domain: undercut-and-reclaim of prior support lows — failed breakdown / bear trap / spring
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Same-bar detection: low pierces prior support, close reclaims above it on the SAME bar.
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


def _prior_low(low: pd.Series, w: int) -> pd.Series:
    """Rolling min of PRIOR bars: shift(1) then rolling min — strictly backward-looking."""
    return low.shift(1).rolling(w, min_periods=max(1, w // 2)).min()


def _failed_breakdown_flag(close: pd.Series, high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    """Binary flag: low < prior w-day low AND close >= prior w-day low (same bar)."""
    support = _prior_low(low, w)
    return ((low < support) & (close >= support)).astype(float)


def _days_since_fb(fb_flag: pd.Series) -> pd.Series:
    """Trading days elapsed since the most recent failed-breakdown event."""
    not_fb = (fb_flag == 0)
    group = fb_flag.cumsum()
    out = not_fb.astype(int).groupby(group).cumsum().astype(float)
    out = out.where(group > 0, np.nan)
    return out


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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): False-breakdown clustering and pattern scoring ---

def fbd_076_fb_cluster_density_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Density of 21d FB events per trading day in trailing 21-day window."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_MON), _TD_MON)
    return _safe_div(cnt, pd.Series(_TD_MON, index=close.index))


def fbd_077_fb_cluster_density_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Density of 21d FB events per trading day in trailing 63-day window."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_MON), _TD_QTR)
    return _safe_div(cnt, pd.Series(_TD_QTR, index=close.index))


def fbd_078_fb_cluster_density_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Density of 21d FB events per trading day in trailing 252-day window."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_MON), _TD_YEAR)
    return _safe_div(cnt, pd.Series(_TD_YEAR, index=close.index))


def fbd_079_fb_21d_score_weighted_depth(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Sum of undercut-depth-pct on 21d FB events over trailing 63 days (depth-weighted count)."""
    support = _prior_low(low, _TD_MON)
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    depth_pct = _safe_div((support - low).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    weighted = fb * depth_pct
    return _rolling_sum(weighted, _TD_QTR)


def fbd_080_fb_21d_score_weighted_volume(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume-ratio on 21d FB events over trailing 63 days (volume-weighted count)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol).fillna(0)
    weighted = fb * vol_ratio
    return _rolling_sum(weighted, _TD_QTR)


def fbd_081_consecutive_fb_streak(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive days with a 21d failed-breakdown (multi-bar spring streak)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    cond = fb > 0
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def fbd_082_max_fb_streak_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum consecutive 21d-FB days within trailing 252 days."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    cond = fb > 0
    def _max_run(arr):
        mx = 0; cur = 0
        for v in arr:
            if v: cur += 1; mx = max(mx, cur)
            else: cur = 0
        return float(mx)
    return cond.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_max_run, raw=True)


def fbd_083_fb_21d_after_extended_decline(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Failed 21d breakdown occurring after close is down >20% from 63d high (deep bear trap)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    hi63 = close.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).max()
    drawdown = _safe_div(close - hi63, hi63)
    deep_decline = (drawdown < -0.20).astype(float)
    return (fb * deep_decline)


def fbd_084_fb_21d_after_high_vol_selloff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Failed 21d breakdown after 5-day cumulative volume above 2x avg (panic-then-spring)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol)
    hi_vol_5d = vol_ratio.rolling(_TD_WEEK, min_periods=1).mean() > 1.5
    return (fb * hi_vol_5d.astype(float))


def fbd_085_fb_21d_near_52wk_low(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Failed 21d breakdown when close is within 5% of 252-day low (deep support test)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    low_252 = _prior_low(low, _TD_YEAR)
    near = _safe_div(close - low_252, low_252) < 0.05
    return (fb * near.astype(float))


def fbd_086_test_without_reclaim_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 21-day support undercuts that did NOT reclaim (failed tests) in trailing 21d."""
    support = _prior_low(low, _TD_MON)
    undercut_no_reclaim = ((low < support) & (close < support)).astype(float)
    return _rolling_sum(undercut_no_reclaim, _TD_MON)


def fbd_087_test_without_reclaim_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of 21-day support undercuts without reclaim in trailing 63 days."""
    support = _prior_low(low, _TD_MON)
    undercut_no_reclaim = ((low < support) & (close < support)).astype(float)
    return _rolling_sum(undercut_no_reclaim, _TD_QTR)


def fbd_088_reclaim_rate_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of 21d support undercuts that were reclaimed (FB) vs total undercuts (21d window)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    support = _prior_low(low, _TD_MON)
    total_undercut = (low < support).astype(float)
    fb_cnt = _rolling_sum(fb, _TD_MON)
    undercut_cnt = _rolling_sum(total_undercut, _TD_MON).clip(lower=1)
    return _safe_div(fb_cnt, undercut_cnt)


def fbd_089_reclaim_rate_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of 21d support undercuts reclaimed over trailing 63 days."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    support = _prior_low(low, _TD_MON)
    total_undercut = (low < support).astype(float)
    fb_cnt = _rolling_sum(fb, _TD_QTR)
    undercut_cnt = _rolling_sum(total_undercut, _TD_QTR).clip(lower=1)
    return _safe_div(fb_cnt, undercut_cnt)


def fbd_090_fb_support_tested_multiple_times_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: 21-day support has been tested (low < support) 3+ times in past 63 days."""
    support = _prior_low(low, _TD_MON)
    test = (low < support).astype(float)
    test_cnt = _rolling_sum(test, _TD_QTR)
    return (test_cnt >= 3).astype(float)


# --- Group G (091-110): Support-level change and stability measures ---

def fbd_091_support_21d_change_pct(close: pd.Series, low: pd.Series) -> pd.Series:
    """Pct change in 21-day support level over the past 21 days (dropping support = bearish)."""
    support = _prior_low(low, _TD_MON)
    return _safe_div(support - support.shift(_TD_MON), support.shift(_TD_MON))


def fbd_092_support_63d_change_pct(close: pd.Series, low: pd.Series) -> pd.Series:
    """Pct change in 63-day support level over the past 21 days."""
    support = _prior_low(low, _TD_QTR)
    return _safe_div(support - support.shift(_TD_MON), support.shift(_TD_MON))


def fbd_093_support_21d_slope_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of 21-day support level over trailing 21 days (trend in support floor)."""
    support = _prior_low(low, _TD_MON)
    return _linslope(support, _TD_MON)


def fbd_094_support_63d_slope_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of 63-day support level over trailing 21 days."""
    support = _prior_low(low, _TD_QTR)
    return _linslope(support, _TD_MON)


def fbd_095_support_stability_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Std deviation of 21-day support level over trailing 63 days (stable = tighter range)."""
    support = _prior_low(low, _TD_MON)
    return _rolling_std(support, _TD_QTR)


def fbd_096_close_to_support_ratio_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of close to 21-day support (>1 = above support, <1 = below)."""
    support = _prior_low(low, _TD_MON)
    return _safe_div(close, support.replace(0, np.nan))


def fbd_097_close_to_support_ratio_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of close to 63-day support."""
    support = _prior_low(low, _TD_QTR)
    return _safe_div(close, support.replace(0, np.nan))


def fbd_098_low_to_support_ratio_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of intraday low to 21-day support (measures depth of any undercut)."""
    support = _prior_low(low, _TD_MON)
    return _safe_div(low, support.replace(0, np.nan))


def fbd_099_support_21d_vs_sma21(close: pd.Series, low: pd.Series) -> pd.Series:
    """21-day support as % above/below the 21-day SMA (support vs trend)."""
    support = _prior_low(low, _TD_MON)
    sma21 = _rolling_mean(close, _TD_MON)
    return _safe_div(support - sma21, sma21)


def fbd_100_support_63d_vs_sma200(close: pd.Series, low: pd.Series) -> pd.Series:
    """63-day support as % above/below the 200-day SMA."""
    support = _prior_low(low, _TD_QTR)
    sma200 = _rolling_mean(close, 200)
    return _safe_div(support - sma200, sma200)


def fbd_101_fb_21d_pct_of_all_undercuts_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of 21d undercut events that became full FB over trailing 252 days."""
    fb_cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_MON), _TD_YEAR)
    support = _prior_low(low, _TD_MON)
    undercut_cnt = _rolling_sum((low < support).astype(float), _TD_YEAR).clip(lower=1)
    return _safe_div(fb_cnt, undercut_cnt)


def fbd_102_avg_support_undercut_pct_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Average depth of ALL 21d-support undercuts (FB or not) over trailing 252 days."""
    support = _prior_low(low, _TD_MON)
    undercut = ((support - low) / support.replace(0, np.nan)).clip(lower=0)
    undercut_masked = undercut.where(low < support, np.nan)
    return undercut_masked.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def fbd_103_support_21d_new_low_flag(close: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: 21-day support is at a new 252-day low today (deepening support floor)."""
    support = _prior_low(low, _TD_MON)
    support_252_low = support.shift(1).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()
    return (support < support_252_low).astype(float)


def fbd_104_support_63d_new_low_flag(close: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: 63-day support is at a new 252-day low today."""
    support = _prior_low(low, _TD_QTR)
    support_252_low = support.shift(1).rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).min()
    return (support < support_252_low).astype(float)


def fbd_105_support_21d_pct_rank_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21d support level within its trailing 252-day range."""
    support = _prior_low(low, _TD_MON)
    return support.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fbd_106_support_63d_pct_rank_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 63d support level within its trailing 252-day range."""
    support = _prior_low(low, _TD_QTR)
    return support.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fbd_107_close_minus_support_21d_zscore(close: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of (close - 21d support) over trailing 252 days."""
    support = _prior_low(low, _TD_MON)
    margin = close - support
    m = _rolling_mean(margin, _TD_YEAR)
    s = _rolling_std(margin, _TD_YEAR)
    return _safe_div(margin - m, s)


def fbd_108_undercut_normalized_by_atr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Undercut depth on 21d FB events normalized by 21-day ATR (size-adjusted pierce)."""
    support = _prior_low(low, _TD_MON)
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    pierce = (support - low).clip(lower=0)
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)
    atr21 = _rolling_mean(tr, _TD_MON)
    ratio = _safe_div(pierce, atr21)
    return ratio.where(fb > 0, 0.0)


def fbd_109_reclaim_as_fraction_of_atr_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close-above-support reclaim size normalized by 21-day ATR on FB bars."""
    support = _prior_low(low, _TD_MON)
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    reclaim = (close - support).clip(lower=0)
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)
    atr21 = _rolling_mean(tr, _TD_MON)
    ratio = _safe_div(reclaim, atr21)
    return ratio.where(fb > 0, 0.0)


def fbd_110_fb_composite_score_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite FB quality score = depth_pct * volume_ratio on 21d FB bars (trailing 63d mean)."""
    support = _prior_low(low, _TD_MON)
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    depth_pct = _safe_div((support - low).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol).fillna(1)
    score = fb * depth_pct * vol_ratio
    return _rolling_mean(score, _TD_QTR)


# --- Group H (111-130): Volume behavior around failed breakdowns ---

def fbd_111_avg_vol_on_fb_21d_window63(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Average raw volume on 21d-FB days over trailing 63 days."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    vol_on_fb = volume.where(fb > 0, np.nan)
    return vol_on_fb.rolling(_TD_QTR, min_periods=1).mean()


def fbd_112_vol_surge_ratio_fb_vs_nonfb_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of avg volume on FB days vs non-FB days in trailing 63 days."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    vol_fb = volume.where(fb > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    vol_nonfb = volume.where(fb == 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(vol_fb, vol_nonfb)


def fbd_113_vol_on_undercut_vs_reclaim_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on 21d undercut days (any, FB or not) vs average volume in trailing 21 days."""
    support = _prior_low(low, _TD_MON)
    undercut = (low < support)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol)
    return vol_ratio.where(undercut, np.nan).rolling(_TD_MON, min_periods=1).mean()


def fbd_114_vol_expansion_fb_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on 21d FB vs prior 5-day avg volume (expansion at spring point)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    avg_vol5 = _rolling_mean(volume, _TD_WEEK)
    vol_expansion = _safe_div(volume, avg_vol5)
    return vol_expansion.where(fb > 0, 0.0)


def fbd_115_vol_expansion_63d_fb(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on 63d FB vs prior 5-day avg volume."""
    fb = _failed_breakdown_flag(close, high, low, _TD_QTR)
    avg_vol5 = _rolling_mean(volume, _TD_WEEK)
    vol_expansion = _safe_div(volume, avg_vol5)
    return vol_expansion.where(fb > 0, 0.0)


def fbd_116_cumvol_5d_before_fb_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day trailing cumulative volume level relative to 21d avg (volume buildup into FB)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    vol5 = _rolling_sum(volume, _TD_WEEK)
    avg_vol21 = _rolling_mean(volume, _TD_MON) * _TD_WEEK
    vol_ratio = _safe_div(vol5, avg_vol21)
    return vol_ratio.where(fb > 0, 0.0)


def fbd_117_vol_dryup_post_fb_5d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume ratio (day+1 to +5 avg vs FB-day volume) using only prior bars — dry-up after FB."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    avg_vol5 = _rolling_mean(volume, _TD_WEEK)
    ratio = _safe_div(avg_vol5, volume)
    return ratio.where(fb.shift(1) > 0, np.nan).fillna(0.0)


def fbd_118_vol_on_fb_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct rank of volume-on-FB-day within trailing 252-day volume distribution."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    vol_fb = volume.where(fb > 0, np.nan).fillna(0)
    return vol_fb.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def fbd_119_vol_ratio_fb_21d_zscore(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of volume-ratio on FB days vs 252-day avg FB volume ratio."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol)
    vol_on_fb = vol_ratio.where(fb > 0, np.nan)
    m = vol_on_fb.rolling(_TD_YEAR, min_periods=_TD_QTR).mean()
    s = vol_on_fb.rolling(_TD_YEAR, min_periods=_TD_QTR).std()
    return _safe_div(vol_ratio - m, s)


def fbd_120_vol_ratio_undercut_no_reclaim(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg volume ratio on 21d undercut days that did NOT reclaim (failed spring attempt) in 63d."""
    support = _prior_low(low, _TD_MON)
    failed_test = ((low < support) & (close < support))
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol)
    vol_fail = vol_ratio.where(failed_test, np.nan)
    return vol_fail.rolling(_TD_QTR, min_periods=1).mean()


# --- Group I (121-135): Return-based measures around failed breakdowns ---

def fbd_121_close_return_on_fb_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Daily log-return of bar on 21d failed-breakdown events."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    log_ret = _log_safe(close) - _log_safe(close.shift(1))
    return log_ret.where(fb > 0, 0.0)


def fbd_122_avg_return_on_fb_21d_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average log-return on 21d FB days over trailing 63 days."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    log_ret = _log_safe(close) - _log_safe(close.shift(1))
    fb_ret = log_ret.where(fb > 0, np.nan)
    return fb_ret.rolling(_TD_QTR, min_periods=1).mean()


def fbd_123_avg_return_on_fb_21d_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average log-return on 21d FB days over trailing 252 days."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    log_ret = _log_safe(close) - _log_safe(close.shift(1))
    fb_ret = log_ret.where(fb > 0, np.nan)
    return fb_ret.rolling(_TD_YEAR, min_periods=_TD_QTR).mean()


def fbd_124_max_return_on_fb_21d_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum log-return recorded on 21d FB days over trailing 252 days."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    log_ret = _log_safe(close) - _log_safe(close.shift(1))
    fb_ret = log_ret.where(fb > 0, np.nan).fillna(0)
    return _rolling_max(fb_ret, _TD_YEAR)


def fbd_125_return_5d_pre_fb_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day log-return ending on 21d FB day (momentum context into the spring)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    ret5 = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    return ret5.where(fb > 0, 0.0)


def fbd_126_return_21d_pre_fb(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day log-return ending on 21d FB day (medium-term context)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    ret21 = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    return ret21.where(fb > 0, 0.0)


def fbd_127_return_volatility_on_fb_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Std dev of log-returns on 21d FB days over trailing 63 days."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    log_ret = _log_safe(close) - _log_safe(close.shift(1))
    fb_ret = log_ret.where(fb > 0, np.nan)
    return fb_ret.rolling(_TD_QTR, min_periods=1).std()


def fbd_128_cumret_since_last_fb_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Cumulative log-return since the last 21d FB event (gain after spring)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    log_ret = _log_safe(close) - _log_safe(close.shift(1))
    group = fb.cumsum()
    cum = log_ret.groupby(group).cumsum()
    cum = cum.where(group > 0, np.nan)
    on_fb = fb > 0
    return cum.where(~on_fb, 0.0)


def fbd_129_max_drawdown_since_last_fb_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max drawdown (close from prior close peak) since last 21d FB event."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    group = fb.cumsum()
    rolling_peak = close.groupby(group).transform("cummax")
    drawdown = _safe_div(close - rolling_peak, rolling_peak)
    return drawdown.where(group > 0, np.nan)


def fbd_130_intrabar_reversal_pct_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Intrabar reversal on 21d FB: (close - low) / (high - low) captures % recovery from low."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    bar_range = (high - low).replace(0, np.nan)
    reversal = _safe_div(close - low, bar_range)
    return reversal.where(fb > 0, 0.0)


# --- Group J (131-150): Cross-level tests, aggregated scores, rank features ---

def fbd_131_fb_21d_count_norm_63d_avg(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day FB count normalized by its 63-day rolling average (relative frequency)."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_MON), _TD_MON)
    avg = _rolling_mean(cnt, _TD_QTR)
    return _safe_div(cnt, avg)


def fbd_132_fb_21d_count_norm_252d_avg(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day FB count normalized by its 252-day rolling average."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_MON), _TD_MON)
    avg = _rolling_mean(cnt, _TD_YEAR)
    return _safe_div(cnt, avg)


def fbd_133_support_undercut_both_21_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: bar undercuts BOTH 21d and 63d support levels simultaneously."""
    support21 = _prior_low(low, _TD_MON)
    support63 = _prior_low(low, _TD_QTR)
    return ((low < support21) & (low < support63)).astype(float)


def fbd_134_fb_both_21_63d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: bar is a failed breakdown at BOTH 21d and 63d support simultaneously."""
    fb21 = _failed_breakdown_flag(close, high, low, _TD_MON)
    fb63 = _failed_breakdown_flag(close, high, low, _TD_QTR)
    return ((fb21 > 0) & (fb63 > 0)).astype(float)


def fbd_135_fb_triple_level_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: failed breakdown at 21d, 63d, AND 126d support all on the same bar."""
    fb21 = _failed_breakdown_flag(close, high, low, _TD_MON)
    fb63 = _failed_breakdown_flag(close, high, low, _TD_QTR)
    fb126 = _failed_breakdown_flag(close, high, low, _TD_HALF)
    return ((fb21 > 0) & (fb63 > 0) & (fb126 > 0)).astype(float)


def fbd_136_fb_21d_expanding_count(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding all-time count of 21d failed-breakdown events."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    return fb.expanding(min_periods=1).sum()


def fbd_137_fb_63d_expanding_count(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding all-time count of 63d failed-breakdown events."""
    fb = _failed_breakdown_flag(close, high, low, _TD_QTR)
    return fb.expanding(min_periods=1).sum()


def fbd_138_fb_21d_pct_rank_expanding(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding percentile rank of 21-day FB count (21d window)."""
    cnt = _rolling_sum(_failed_breakdown_flag(close, high, low, _TD_MON), _TD_MON)
    return cnt.expanding(min_periods=5).rank(pct=True)


def fbd_139_support_distance_compression_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 21d support to 63d support (compression: close to 1 = converging floors)."""
    s21 = _prior_low(low, _TD_MON)
    s63 = _prior_low(low, _TD_QTR)
    return _safe_div(s21, s63.replace(0, np.nan))


def fbd_140_support_distance_compression_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 63d support to 252d support (compression of medium to long-term floor)."""
    s63 = _prior_low(low, _TD_QTR)
    s252 = _prior_low(low, _TD_YEAR)
    return _safe_div(s63, s252.replace(0, np.nan))


def fbd_141_fb_21d_bear_trap_score(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Bear-trap quality composite: undercut_pct + vol_ratio + reclaim_pct on 21d FB."""
    support = _prior_low(low, _TD_MON)
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    depth = _safe_div((support - low).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_r = _safe_div(volume, avg_vol).fillna(1).clip(upper=5)
    reclaim = _safe_div((close - support).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    score = (depth + vol_r / 5.0 + reclaim).where(fb > 0, 0.0)
    return score


def fbd_142_fb_21d_at_ema50_support(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Failed 21d breakdown occurring when 21d support is within 1% of the 50-day EMA."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    support = _prior_low(low, _TD_MON)
    ema50 = _ewm_mean(close, 50)
    near_ema50 = (_safe_div((support - ema50).abs(), ema50.replace(0, np.nan)) < 0.01).astype(float)
    return (fb * near_ema50)


def fbd_143_fb_21d_at_ema200_support(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Failed 21d breakdown occurring when 21d support is within 1% of the 200-day EMA."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    support = _prior_low(low, _TD_MON)
    ema200 = _ewm_mean(close, 200)
    near_ema200 = (_safe_div((support - ema200).abs(), ema200.replace(0, np.nan)) < 0.01).astype(float)
    return (fb * near_ema200)


def fbd_144_fb_21d_reclaim_above_vwap_proxy(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Failed 21d breakdown where close is above 21-day VWAP proxy (vol-weighted avg close)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    vwap_num = _rolling_sum(close * volume, _TD_MON)
    vwap_den = _rolling_sum(volume, _TD_MON)
    vwap = _safe_div(vwap_num, vwap_den)
    return (fb * (close >= vwap).astype(float))


def fbd_145_fb_21d_with_rsi_oversold(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Failed 21d breakdown occurring when 14-day RSI is below 30 (oversold spring)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    delta = close.diff(1)
    gain = delta.clip(lower=0)
    loss = (-delta).clip(lower=0)
    avg_gain = _rolling_mean(gain, 14)
    avg_loss = _rolling_mean(loss, 14)
    rs = _safe_div(avg_gain, avg_loss)
    rsi = 100 - _safe_div(pd.Series(100, index=close.index), 1 + rs)
    return (fb * (rsi < 30).astype(float))


def fbd_146_fb_21d_with_rsi_divergence(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Failed 21d breakdown when close makes 21d low but RSI does NOT make new 21d low."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    delta = close.diff(1)
    gain = delta.clip(lower=0)
    loss = (-delta).clip(lower=0)
    avg_gain = _rolling_mean(gain, 14)
    avg_loss = _rolling_mean(loss, 14)
    rs = _safe_div(avg_gain, avg_loss)
    rsi = 100 - _safe_div(pd.Series(100, index=close.index), 1 + rs)
    rsi_21_low = rsi.shift(1).rolling(_TD_MON, min_periods=1).min()
    diverge = (rsi >= rsi_21_low).astype(float)
    return (fb * diverge)


def fbd_147_fb_21d_with_narrow_spread(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Failed 21d breakdown with bar range < 50% of 21-day avg bar range (tight spring)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    bar_range = high - low
    avg_range = _rolling_mean(bar_range, _TD_MON)
    narrow = (bar_range < 0.5 * avg_range).astype(float)
    return (fb * narrow)


def fbd_148_fb_21d_with_wide_spread(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Failed 21d breakdown with bar range > 2x the 21-day avg bar range (wide reversal bar)."""
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    bar_range = high - low
    avg_range = _rolling_mean(bar_range, _TD_MON)
    wide = (bar_range > 2.0 * avg_range).astype(float)
    return (fb * wide)


def fbd_149_undercut_test_ratio_21d_vs_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 21-day undercut test count to 252-day undercut test count (recent vs historical)."""
    support = _prior_low(low, _TD_MON)
    test = (low < support).astype(float)
    cnt21 = _rolling_sum(test, _TD_MON)
    cnt252 = _rolling_sum(test, _TD_YEAR).clip(lower=1)
    return _safe_div(cnt21, cnt252)


def fbd_150_fb_21d_strength_score_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day rolling mean of bear-trap quality scores (persistent spring strength)."""
    support = _prior_low(low, _TD_MON)
    fb = _failed_breakdown_flag(close, high, low, _TD_MON)
    depth = _safe_div((support - low).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_r = _safe_div(volume, avg_vol).fillna(1).clip(upper=5)
    reclaim = _safe_div((close - support).clip(lower=0), support.replace(0, np.nan)).fillna(0)
    score = (depth + vol_r / 5.0 + reclaim).where(fb > 0, 0.0)
    return _rolling_mean(score, _TD_YEAR)


# ── Registry ──────────────────────────────────────────────────────────────────

FAILED_BREAKDOWN_REGISTRY_076_150 = {
    "fbd_076_fb_cluster_density_21d": {"inputs": ["close", "high", "low"], "func": fbd_076_fb_cluster_density_21d},
    "fbd_077_fb_cluster_density_63d": {"inputs": ["close", "high", "low"], "func": fbd_077_fb_cluster_density_63d},
    "fbd_078_fb_cluster_density_252d": {"inputs": ["close", "high", "low"], "func": fbd_078_fb_cluster_density_252d},
    "fbd_079_fb_21d_score_weighted_depth": {"inputs": ["close", "high", "low"], "func": fbd_079_fb_21d_score_weighted_depth},
    "fbd_080_fb_21d_score_weighted_volume": {"inputs": ["close", "high", "low", "volume"], "func": fbd_080_fb_21d_score_weighted_volume},
    "fbd_081_consecutive_fb_streak": {"inputs": ["close", "high", "low"], "func": fbd_081_consecutive_fb_streak},
    "fbd_082_max_fb_streak_252d": {"inputs": ["close", "high", "low"], "func": fbd_082_max_fb_streak_252d},
    "fbd_083_fb_21d_after_extended_decline": {"inputs": ["close", "high", "low"], "func": fbd_083_fb_21d_after_extended_decline},
    "fbd_084_fb_21d_after_high_vol_selloff": {"inputs": ["close", "high", "low", "volume"], "func": fbd_084_fb_21d_after_high_vol_selloff},
    "fbd_085_fb_21d_near_52wk_low": {"inputs": ["close", "high", "low"], "func": fbd_085_fb_21d_near_52wk_low},
    "fbd_086_test_without_reclaim_21d": {"inputs": ["close", "high", "low"], "func": fbd_086_test_without_reclaim_21d},
    "fbd_087_test_without_reclaim_63d": {"inputs": ["close", "high", "low"], "func": fbd_087_test_without_reclaim_63d},
    "fbd_088_reclaim_rate_21d": {"inputs": ["close", "high", "low"], "func": fbd_088_reclaim_rate_21d},
    "fbd_089_reclaim_rate_63d": {"inputs": ["close", "high", "low"], "func": fbd_089_reclaim_rate_63d},
    "fbd_090_fb_support_tested_multiple_times_21d": {"inputs": ["close", "high", "low"], "func": fbd_090_fb_support_tested_multiple_times_21d},
    "fbd_091_support_21d_change_pct": {"inputs": ["close", "low"], "func": fbd_091_support_21d_change_pct},
    "fbd_092_support_63d_change_pct": {"inputs": ["close", "low"], "func": fbd_092_support_63d_change_pct},
    "fbd_093_support_21d_slope_21d": {"inputs": ["close", "low"], "func": fbd_093_support_21d_slope_21d},
    "fbd_094_support_63d_slope_21d": {"inputs": ["close", "low"], "func": fbd_094_support_63d_slope_21d},
    "fbd_095_support_stability_21d": {"inputs": ["close", "low"], "func": fbd_095_support_stability_21d},
    "fbd_096_close_to_support_ratio_21d": {"inputs": ["close", "low"], "func": fbd_096_close_to_support_ratio_21d},
    "fbd_097_close_to_support_ratio_63d": {"inputs": ["close", "low"], "func": fbd_097_close_to_support_ratio_63d},
    "fbd_098_low_to_support_ratio_21d": {"inputs": ["close", "low"], "func": fbd_098_low_to_support_ratio_21d},
    "fbd_099_support_21d_vs_sma21": {"inputs": ["close", "low"], "func": fbd_099_support_21d_vs_sma21},
    "fbd_100_support_63d_vs_sma200": {"inputs": ["close", "low"], "func": fbd_100_support_63d_vs_sma200},
    "fbd_101_fb_21d_pct_of_all_undercuts_252d": {"inputs": ["close", "high", "low"], "func": fbd_101_fb_21d_pct_of_all_undercuts_252d},
    "fbd_102_avg_support_undercut_pct_252d": {"inputs": ["close", "low"], "func": fbd_102_avg_support_undercut_pct_252d},
    "fbd_103_support_21d_new_low_flag": {"inputs": ["close", "low"], "func": fbd_103_support_21d_new_low_flag},
    "fbd_104_support_63d_new_low_flag": {"inputs": ["close", "low"], "func": fbd_104_support_63d_new_low_flag},
    "fbd_105_support_21d_pct_rank_252d": {"inputs": ["close", "low"], "func": fbd_105_support_21d_pct_rank_252d},
    "fbd_106_support_63d_pct_rank_252d": {"inputs": ["close", "low"], "func": fbd_106_support_63d_pct_rank_252d},
    "fbd_107_close_minus_support_21d_zscore": {"inputs": ["close", "low"], "func": fbd_107_close_minus_support_21d_zscore},
    "fbd_108_undercut_normalized_by_atr": {"inputs": ["close", "high", "low"], "func": fbd_108_undercut_normalized_by_atr},
    "fbd_109_reclaim_as_fraction_of_atr_21d": {"inputs": ["close", "high", "low"], "func": fbd_109_reclaim_as_fraction_of_atr_21d},
    "fbd_110_fb_composite_score_21d": {"inputs": ["close", "high", "low", "volume"], "func": fbd_110_fb_composite_score_21d},
    "fbd_111_avg_vol_on_fb_21d_window63": {"inputs": ["close", "high", "low", "volume"], "func": fbd_111_avg_vol_on_fb_21d_window63},
    "fbd_112_vol_surge_ratio_fb_vs_nonfb_63d": {"inputs": ["close", "high", "low", "volume"], "func": fbd_112_vol_surge_ratio_fb_vs_nonfb_63d},
    "fbd_113_vol_on_undercut_vs_reclaim_21d": {"inputs": ["close", "high", "low", "volume"], "func": fbd_113_vol_on_undercut_vs_reclaim_21d},
    "fbd_114_vol_expansion_fb_21d": {"inputs": ["close", "high", "low", "volume"], "func": fbd_114_vol_expansion_fb_21d},
    "fbd_115_vol_expansion_63d_fb": {"inputs": ["close", "high", "low", "volume"], "func": fbd_115_vol_expansion_63d_fb},
    "fbd_116_cumvol_5d_before_fb_21d": {"inputs": ["close", "high", "low", "volume"], "func": fbd_116_cumvol_5d_before_fb_21d},
    "fbd_117_vol_dryup_post_fb_5d": {"inputs": ["close", "high", "low", "volume"], "func": fbd_117_vol_dryup_post_fb_5d},
    "fbd_118_vol_on_fb_pct_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": fbd_118_vol_on_fb_pct_rank_252d},
    "fbd_119_vol_ratio_fb_21d_zscore": {"inputs": ["close", "high", "low", "volume"], "func": fbd_119_vol_ratio_fb_21d_zscore},
    "fbd_120_vol_ratio_undercut_no_reclaim": {"inputs": ["close", "high", "low", "volume"], "func": fbd_120_vol_ratio_undercut_no_reclaim},
    "fbd_121_close_return_on_fb_21d": {"inputs": ["close", "high", "low"], "func": fbd_121_close_return_on_fb_21d},
    "fbd_122_avg_return_on_fb_21d_63d": {"inputs": ["close", "high", "low"], "func": fbd_122_avg_return_on_fb_21d_63d},
    "fbd_123_avg_return_on_fb_21d_252d": {"inputs": ["close", "high", "low"], "func": fbd_123_avg_return_on_fb_21d_252d},
    "fbd_124_max_return_on_fb_21d_252d": {"inputs": ["close", "high", "low"], "func": fbd_124_max_return_on_fb_21d_252d},
    "fbd_125_return_5d_pre_fb_21d": {"inputs": ["close", "high", "low"], "func": fbd_125_return_5d_pre_fb_21d},
    "fbd_126_return_21d_pre_fb": {"inputs": ["close", "high", "low"], "func": fbd_126_return_21d_pre_fb},
    "fbd_127_return_volatility_on_fb_63d": {"inputs": ["close", "high", "low"], "func": fbd_127_return_volatility_on_fb_63d},
    "fbd_128_cumret_since_last_fb_21d": {"inputs": ["close", "high", "low"], "func": fbd_128_cumret_since_last_fb_21d},
    "fbd_129_max_drawdown_since_last_fb_21d": {"inputs": ["close", "high", "low"], "func": fbd_129_max_drawdown_since_last_fb_21d},
    "fbd_130_intrabar_reversal_pct_21d": {"inputs": ["close", "high", "low", "open"], "func": fbd_130_intrabar_reversal_pct_21d},
    "fbd_131_fb_21d_count_norm_63d_avg": {"inputs": ["close", "high", "low"], "func": fbd_131_fb_21d_count_norm_63d_avg},
    "fbd_132_fb_21d_count_norm_252d_avg": {"inputs": ["close", "high", "low"], "func": fbd_132_fb_21d_count_norm_252d_avg},
    "fbd_133_support_undercut_both_21_63d": {"inputs": ["close", "high", "low"], "func": fbd_133_support_undercut_both_21_63d},
    "fbd_134_fb_both_21_63d_flag": {"inputs": ["close", "high", "low"], "func": fbd_134_fb_both_21_63d_flag},
    "fbd_135_fb_triple_level_flag": {"inputs": ["close", "high", "low"], "func": fbd_135_fb_triple_level_flag},
    "fbd_136_fb_21d_expanding_count": {"inputs": ["close", "high", "low"], "func": fbd_136_fb_21d_expanding_count},
    "fbd_137_fb_63d_expanding_count": {"inputs": ["close", "high", "low"], "func": fbd_137_fb_63d_expanding_count},
    "fbd_138_fb_21d_pct_rank_expanding": {"inputs": ["close", "high", "low"], "func": fbd_138_fb_21d_pct_rank_expanding},
    "fbd_139_support_distance_compression_21d": {"inputs": ["close", "low"], "func": fbd_139_support_distance_compression_21d},
    "fbd_140_support_distance_compression_63d": {"inputs": ["close", "low"], "func": fbd_140_support_distance_compression_63d},
    "fbd_141_fb_21d_bear_trap_score": {"inputs": ["close", "high", "low", "volume"], "func": fbd_141_fb_21d_bear_trap_score},
    "fbd_142_fb_21d_at_ema50_support": {"inputs": ["close", "high", "low"], "func": fbd_142_fb_21d_at_ema50_support},
    "fbd_143_fb_21d_at_ema200_support": {"inputs": ["close", "high", "low"], "func": fbd_143_fb_21d_at_ema200_support},
    "fbd_144_fb_21d_reclaim_above_vwap_proxy": {"inputs": ["close", "high", "low", "volume"], "func": fbd_144_fb_21d_reclaim_above_vwap_proxy},
    "fbd_145_fb_21d_with_rsi_oversold": {"inputs": ["close", "high", "low"], "func": fbd_145_fb_21d_with_rsi_oversold},
    "fbd_146_fb_21d_with_rsi_divergence": {"inputs": ["close", "high", "low"], "func": fbd_146_fb_21d_with_rsi_divergence},
    "fbd_147_fb_21d_with_narrow_spread": {"inputs": ["close", "high", "low"], "func": fbd_147_fb_21d_with_narrow_spread},
    "fbd_148_fb_21d_with_wide_spread": {"inputs": ["close", "high", "low"], "func": fbd_148_fb_21d_with_wide_spread},
    "fbd_149_undercut_test_ratio_21d_vs_252d": {"inputs": ["close", "high", "low"], "func": fbd_149_undercut_test_ratio_21d_vs_252d},
    "fbd_150_fb_21d_strength_score_252d": {"inputs": ["close", "high", "low", "volume"], "func": fbd_150_fb_21d_strength_score_252d},
}
