"""fibonacci_extension_signature d1 features 076-150 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__001_075.py. Each feature
encodes a *different concept* in the prior-swing Fibonacci-extension overshoot
theme: cross-anchor lifetime swings, geometric (log) swings, sigma-normalized
overshoots, dwell streaks, statistical extension distributions, retracement
after extension, fib cluster density, retest patterns, structural age, and
drawdown-from-max-extension dynamics.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family
imports.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


# ---------------------------- helpers ----------------------------

def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


# ---- family-specific helpers (PIT-clean) ----

def _swing_low(low: pd.Series, n: int) -> pd.Series:
    win = 2 * n + 1
    rolling_min = low.rolling(win, min_periods=win).min()
    cand = low.shift(n)
    is_pivot = (cand == rolling_min) & cand.notna() & rolling_min.notna()
    return cand.where(is_pivot, np.nan).ffill()


def _swing_high(high: pd.Series, n: int) -> pd.Series:
    win = 2 * n + 1
    rolling_max = high.rolling(win, min_periods=win).max()
    cand = high.shift(n)
    is_pivot = (cand == rolling_max) & cand.notna() & rolling_max.notna()
    return cand.where(is_pivot, np.nan).ffill()


def _ext_value(price: pd.Series, sl: pd.Series, sh: pd.Series) -> pd.Series:
    return _safe_div(price - sl, sh - sl)


def _fib_target(sl: pd.Series, sh: pd.Series, ratio: float) -> pd.Series:
    return sl + ratio * (sh - sl)


def _log_dist(price: pd.Series, target: pd.Series) -> pd.Series:
    return _safe_log(price) - _safe_log(target)


def _atl(low: pd.Series) -> pd.Series:
    """Expanding all-time low."""
    return low.expanding(min_periods=QDAYS).min()


def _ath(high: pd.Series) -> pd.Series:
    """Expanding all-time high."""
    return high.expanding(min_periods=QDAYS).max()


SW_S = 10
SW_M = 30
SW_L = 90


# ============================================================
# Bucket N — Cross-anchor lifetime swing extension (076-082)
# Anchor swing = ATL-to-ATH (expanding) instead of recent pivot swing.
# ============================================================

def f08_fibx_076_log_dist_above_1_618_ext_of_lifetime_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance above 1.618 ext of lifetime ATL→ATH swing — cross-anchor overshoot."""
    return _log_dist(close, _fib_target(_atl(low), _ath(high), 1.618))


def f08_fibx_077_log_dist_above_2_0_ext_of_lifetime_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance above 2.0 ext of lifetime swing."""
    return _log_dist(close, _fib_target(_atl(low), _ath(high), 2.0))


def f08_fibx_078_log_dist_above_2_618_ext_of_lifetime_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance above 2.618 ext of lifetime swing — extreme lifetime overshoot."""
    return _log_dist(close, _fib_target(_atl(low), _ath(high), 2.618))


def f08_fibx_079_atr_dist_above_1_618_ext_of_lifetime_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR distance above 1.618 ext of lifetime swing."""
    return _safe_div(close - _fib_target(_atl(low), _ath(high), 1.618), _atr(high, low, close, n=MDAYS))


def f08_fibx_080_current_extension_value_lifetime_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ext value (fraction) on lifetime ATL→ATH swing — 1.0 = at ATH."""
    return _ext_value(close, _atl(low), _ath(high))


def f08_fibx_081_count_fib_levels_exceeded_lifetime_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """How many of {1.272,1.618,2.0,2.618,4.236} fib levels of the lifetime swing close is above."""
    sl = _atl(low); sh = _ath(high)
    cnt = pd.Series(0.0, index=close.index)
    valid = sl.notna() & sh.notna()
    for r in [1.272, 1.618, 2.0, 2.618, 4.236]:
        cnt = cnt + (close > _fib_target(sl, sh, r)).astype(float)
    return cnt.where(valid, np.nan)


def f08_fibx_082_bars_since_first_crossing_1_618_lifetime(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since first ever crossing above 1.618 ext of lifetime swing."""
    sl = _atl(low); sh = _ath(high)
    tgt = _fib_target(sl, sh, 1.618)
    cross_up = (close > tgt) & (close.shift(1) <= tgt.shift(1))
    idx_at_cross = np.where(cross_up.to_numpy(), np.arange(len(close)), np.nan)
    last_cross_idx = pd.Series(idx_at_cross, index=close.index).ffill()
    return pd.Series(np.arange(len(close), dtype=float), index=close.index) - last_cross_idx


# ============================================================
# Bucket O — Cross-horizon disagreement (083)
# ============================================================

def f08_fibx_083_extension_disagreement_medium_vs_lifetime(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Difference between medium-swing ext and lifetime-swing ext — local vs lifetime stretch."""
    em = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    el = _ext_value(close, _atl(low), _ath(high))
    return em - el


# ============================================================
# Bucket P — Geometric (log-space) swings & sigma normalization (084-091)
# ============================================================

def _log_swing_low(low: pd.Series, n: int) -> pd.Series:
    """Swing low computed on log-prices — geometric pivot."""
    log_low = _safe_log(low)
    win = 2 * n + 1
    rmin = log_low.rolling(win, min_periods=win).min()
    cand = log_low.shift(n)
    is_pivot = (cand == rmin) & cand.notna() & rmin.notna()
    return cand.where(is_pivot, np.nan).ffill()


def _log_swing_high(high: pd.Series, n: int) -> pd.Series:
    log_high = _safe_log(high)
    win = 2 * n + 1
    rmax = log_high.rolling(win, min_periods=win).max()
    cand = log_high.shift(n)
    is_pivot = (cand == rmax) & cand.notna() & rmax.notna()
    return cand.where(is_pivot, np.nan).ffill()


def f08_fibx_084_geometric_extension_log_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Geometric ext on log-prices: (log(close) - log_swing_low) / (log_swing_high - log_swing_low)."""
    lsl = _log_swing_low(low, SW_M); lsh = _log_swing_high(high, SW_M)
    return _safe_div(_safe_log(close) - lsl, lsh - lsl)


def f08_fibx_085_geometric_extension_log_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Geometric ext on log-prices for long swing."""
    lsl = _log_swing_low(low, SW_L); lsh = _log_swing_high(high, SW_L)
    return _safe_div(_safe_log(close) - lsl, lsh - lsl)


def f08_fibx_086_log_dist_above_1_618_geometric_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """In log-space: log(close) - (log_sl + 1.618 * (log_sh - log_sl))."""
    lsl = _log_swing_low(low, SW_M); lsh = _log_swing_high(high, SW_M)
    return _safe_log(close) - (lsl + 1.618 * (lsh - lsl))


def f08_fibx_087_log_dist_above_1_618_geometric_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Geometric-space 1.618 distance for long swing."""
    lsl = _log_swing_low(low, SW_L); lsh = _log_swing_high(high, SW_L)
    return _safe_log(close) - (lsl + 1.618 * (lsh - lsl))


def f08_fibx_088_sigma_normalized_extension_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log-extension above swing_high (1.0 fib) normalized by 63d realized log-vol."""
    sh = _swing_high(high, SW_M)
    ret = _safe_log(close).diff()
    sigma = ret.rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(_safe_log(close) - _safe_log(sh), sigma)


def f08_fibx_089_sigma_normalized_extension_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log-extension above long-swing high normalized by 252d realized log-vol."""
    sh = _swing_high(high, SW_L)
    ret = _safe_log(close).diff()
    sigma = ret.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(_safe_log(close) - _safe_log(sh), sigma)


def f08_fibx_090_sigma_normalized_log_dist_above_1_618_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sigma-normalized log-dist above 1.618 of medium swing."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    ret = _safe_log(close).diff()
    sigma = ret.rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(_log_dist(close, _fib_target(sl, sh, 1.618)), sigma)


def f08_fibx_091_sigma_normalized_log_dist_above_2_0_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sigma-normalized log-dist above 2.0 of long swing."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    ret = _safe_log(close).diff()
    sigma = ret.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(_log_dist(close, _fib_target(sl, sh, 2.0)), sigma)


# ============================================================
# Bucket Q — High-counts & streaks above fib targets (092-096)
# ============================================================

def f08_fibx_092_count_bars_high_above_1_618_ext_medium_swing_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in last 63d where high > 1.618 ext of medium swing — frequency of fib breach."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    breach = (high > _fib_target(sl, sh, 1.618)).astype(float)
    return breach.rolling(QDAYS, min_periods=MDAYS).sum()


def f08_fibx_093_count_bars_high_above_2_0_ext_medium_swing_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in last 63d where high > 2.0 ext of medium swing."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    breach = (high > _fib_target(sl, sh, 2.0)).astype(float)
    return breach.rolling(QDAYS, min_periods=MDAYS).sum()


def f08_fibx_094_count_bars_high_above_2_618_ext_long_swing_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in last 252d where high > 2.618 ext of long swing."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    breach = (high > _fib_target(sl, sh, 2.618)).astype(float)
    return breach.rolling(YDAYS, min_periods=QDAYS).sum()


def _streak_above(condition: pd.Series) -> pd.Series:
    """Length of current run where condition is True (resets on False)."""
    grp = (~condition).cumsum()
    return condition.astype(int).groupby(grp).cumsum().astype(float)


def f08_fibx_095_consecutive_days_close_above_1_618_ext_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Length of current streak where close > 1.618 ext of medium swing."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    cond = close > _fib_target(sl, sh, 1.618)
    return _streak_above(cond.fillna(False))


def f08_fibx_096_consecutive_days_close_above_2_0_ext_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Length of current streak where close > 2.0 ext of long swing."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    cond = close > _fib_target(sl, sh, 2.0)
    return _streak_above(cond.fillna(False))


# ============================================================
# Bucket R — Statistical distributions of extension over windows (097-107)
# ============================================================

def f08_fibx_097_fraction_63d_window_above_1_618_ext_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 63d window with close above 1.618 ext — dwell density."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    above = (close > _fib_target(sl, sh, 1.618)).astype(float)
    return above.rolling(QDAYS, min_periods=MDAYS).mean()


def f08_fibx_098_fraction_252d_window_above_1_0_ext_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 252d window with close above swing_high (1.0 ext) on long swing."""
    sh = _swing_high(high, SW_L)
    return (close > sh).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f08_fibx_099_mean_extension_value_medium_swing_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 63d mean of ext value on medium swing — sustained-extension level."""
    e = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return e.rolling(QDAYS, min_periods=MDAYS).mean()


def f08_fibx_100_max_extension_value_medium_swing_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 63d max of ext value on medium swing — peak overshoot."""
    e = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return e.rolling(QDAYS, min_periods=MDAYS).max()


def f08_fibx_101_max_extension_value_long_swing_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Trailing 252d max of ext value on long swing."""
    e = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    return e.rolling(YDAYS, min_periods=QDAYS).max()


def f08_fibx_102_range_of_extension_medium_swing_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Range (max - min) of ext value over trailing 63d."""
    e = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return e.rolling(QDAYS, min_periods=MDAYS).max() - e.rolling(QDAYS, min_periods=MDAYS).min()


def f08_fibx_103_range_of_extension_long_swing_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Range of ext value over trailing 252d on long swing."""
    e = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    return e.rolling(YDAYS, min_periods=QDAYS).max() - e.rolling(YDAYS, min_periods=QDAYS).min()


def f08_fibx_104_std_extension_medium_swing_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stdev of ext value over trailing 63d — extension volatility."""
    e = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return e.rolling(QDAYS, min_periods=MDAYS).std()


def f08_fibx_105_zscore_current_extension_in_252d_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of current ext value against trailing 252d distribution (long swing)."""
    e = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    return _rolling_zscore(e, YDAYS, min_periods=QDAYS)


def f08_fibx_106_percentile_rank_current_extension_in_252d_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Empirical percentile rank of current ext value vs trailing 252d (long swing)."""
    e = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    def _rk(w):
        if np.isnan(w).all(): return np.nan
        last = w[-1]
        if np.isnan(last): return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0: return np.nan
        return float((v <= last).sum()) / float(v.size)
    return e.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)


def f08_fibx_107_percentile_rank_current_extension_in_1260d_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of current ext vs trailing 5y distribution."""
    e = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    def _rk(w):
        if np.isnan(w).all(): return np.nan
        last = w[-1]
        if np.isnan(last): return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0: return np.nan
        return float((v <= last).sum()) / float(v.size)
    return e.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_rk, raw=True)


# ============================================================
# Bucket S — Retracement after extension / recovery (108-114)
# ============================================================

def f08_fibx_108_retracement_after_max_extension_medium_swing_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max retracement of close from rolling 63d max-ext on medium swing — how much we've fallen back."""
    e = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    max_e = e.rolling(QDAYS, min_periods=MDAYS).max()
    return max_e - e


def f08_fibx_109_retracement_after_max_extension_long_swing_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max retracement from 252d max-ext on long swing."""
    e = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    return e.rolling(YDAYS, min_periods=QDAYS).max() - e


def f08_fibx_110_recovery_from_retracement_medium_swing_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current ext minus 21d-trailing min ext — how much we've bounced from recent low."""
    e = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return e - e.rolling(MDAYS, min_periods=WDAYS).min()


def f08_fibx_111_negative_extension_below_1_0_after_breach_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ext < 1.0 now but max-ext-in-63d was > 1.272 — breached then retreated."""
    e = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    max63 = e.rolling(QDAYS, min_periods=MDAYS).max()
    return ((e < 1.0) & (max63 > 1.272)).astype(float).where(e.notna() & max63.notna(), np.nan)


def f08_fibx_112_depth_of_intra_extension_pullback_medium_swing_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Largest intraday pullback (using low) while ext > 1.0: rolling 63d max of (max_close - low) / max_close."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    above = close > sh
    rolling_max_close = close.where(above).rolling(QDAYS, min_periods=WDAYS).max()
    pullback = _safe_div(rolling_max_close - low, rolling_max_close)
    return pullback.rolling(QDAYS, min_periods=WDAYS).max()


def f08_fibx_113_count_distinct_max_extensions_medium_swing_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in last 252d where ext set a new 21d-trailing maximum — frequency of new-extension-highs."""
    e = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    rmax = e.rolling(MDAYS, min_periods=WDAYS).max()
    new_max = (e == rmax) & e.notna()
    return new_max.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f08_fibx_114_mean_bars_between_new_extension_highs_medium_swing_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean bar-gap between consecutive new-ext-max events in last 252d — fading frequency."""
    e = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    rmax = e.rolling(MDAYS, min_periods=WDAYS).max()
    new_max = (e == rmax) & e.notna()
    cnt = new_max.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(YDAYS, cnt)


# ============================================================
# Bucket T — Fib cluster density & zone geometry (115-122)
# ============================================================

def f08_fibx_115_fib_cluster_count_within_atr_of_close_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of fib levels {1.0,1.272,1.618,2.0,2.618,4.236} of medium swing within 1 ATR of close."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    atr = _atr(high, low, close, n=MDAYS)
    cnt = pd.Series(0.0, index=close.index)
    valid = sl.notna() & sh.notna() & atr.notna()
    for r in [1.0, 1.272, 1.618, 2.0, 2.618, 4.236]:
        within = (_fib_target(sl, sh, r) - close).abs() <= atr
        cnt = cnt + within.astype(float)
    return cnt.where(valid, np.nan)


def f08_fibx_116_fib_cluster_count_within_2atr_of_close_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of long-swing fib levels within 2 ATR of close."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    atr = _atr(high, low, close, n=MDAYS)
    cnt = pd.Series(0.0, index=close.index)
    valid = sl.notna() & sh.notna() & atr.notna()
    for r in [1.0, 1.272, 1.618, 2.0, 2.618, 4.236]:
        within = (_fib_target(sl, sh, r) - close).abs() <= (2.0 * atr)
        cnt = cnt + within.astype(float)
    return cnt.where(valid, np.nan)


def f08_fibx_117_fib_cluster_density_near_close_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Density score: 1 / (mean ATR-normalized distance to nearest 3 fib levels)."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    atr = _atr(high, low, close, n=MDAYS)
    parts = []
    for i, r in enumerate([1.0, 1.272, 1.618, 2.0, 2.618, 4.236]):
        parts.append(_safe_div((_fib_target(sl, sh, r) - close).abs(), atr).rename(f"r{i}"))
    df = pd.concat(parts, axis=1)
    nearest3_mean = df.apply(lambda row: np.nanmean(np.sort(row.to_numpy())[:3]), axis=1)
    return _safe_div(1.0, nearest3_mean)


def f08_fibx_118_nearest_fib_zone_width_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Width (price units) of the fib zone we're currently in (lower-fib to upper-fib bracket) on medium swing."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    ratios = [0.0, 1.0, 1.272, 1.618, 2.0, 2.618, 4.236, 10.0]
    targets = [_fib_target(sl, sh, r) for r in ratios]
    df = pd.concat([t.rename(f"r{i}") for i, t in enumerate(targets)], axis=1)
    def _width(row):
        arr = row.to_numpy()
        c = row.name
        return np.nan  # not used; replaced below
    # vectorize: for each bar, find adjacent pair of fibs bracketing close
    close_arr = close.to_numpy()
    tgt_arr = df.to_numpy()
    out = np.full(len(close), np.nan)
    for i in range(len(close)):
        c = close_arr[i]
        row = tgt_arr[i]
        if np.isnan(c) or np.isnan(row).any(): continue
        srt = np.sort(row)
        idx = np.searchsorted(srt, c)
        if 0 < idx < len(srt):
            out[i] = srt[idx] - srt[idx - 1]
    return pd.Series(out, index=close.index)


def f08_fibx_119_position_within_fib_zone_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position within current fib zone: 0=at lower fib, 1=at upper fib."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    ratios = [0.0, 1.0, 1.272, 1.618, 2.0, 2.618, 4.236, 10.0]
    targets = [_fib_target(sl, sh, r) for r in ratios]
    df = pd.concat([t.rename(f"r{i}") for i, t in enumerate(targets)], axis=1)
    close_arr = close.to_numpy()
    tgt_arr = df.to_numpy()
    out = np.full(len(close), np.nan)
    for i in range(len(close)):
        c = close_arr[i]
        row = tgt_arr[i]
        if np.isnan(c) or np.isnan(row).any(): continue
        srt = np.sort(row)
        idx = np.searchsorted(srt, c)
        if 0 < idx < len(srt) and srt[idx] != srt[idx - 1]:
            out[i] = (c - srt[idx - 1]) / (srt[idx] - srt[idx - 1])
    return pd.Series(out, index=close.index)


def f08_fibx_120_extension_dispersion_across_horizons(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std of ext values across short/medium/long swings — timescale disagreement."""
    es = _ext_value(close, _swing_low(low, SW_S), _swing_high(high, SW_S))
    em = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    el = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    return pd.concat([es.rename("s"), em.rename("m"), el.rename("l")], axis=1).std(axis=1)


def f08_fibx_121_extension_range_across_horizons(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Range (max-min) of ext values across short/medium/long swings."""
    es = _ext_value(close, _swing_low(low, SW_S), _swing_high(high, SW_S))
    em = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    el = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    df = pd.concat([es.rename("s"), em.rename("m"), el.rename("l")], axis=1)
    return df.max(axis=1) - df.min(axis=1)


def f08_fibx_122_log_diff_extension_medium_minus_long(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log-difference of medium-swing ext minus long-swing ext."""
    em = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    el = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    return _safe_log(em) - _safe_log(el)


# ============================================================
# Bucket U — Indicators: at zone top / retest / valid-breakout (123-130)
# ============================================================

def f08_fibx_123_close_at_or_above_fib_zone_top_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: close >= top of current fib zone (i.e., close is at or above next higher fib)."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    ratios = [1.0, 1.272, 1.618, 2.0, 2.618, 4.236]
    upper_arr = np.full(len(close), np.nan)
    close_arr = close.to_numpy()
    tgt_mat = np.column_stack([_fib_target(sl, sh, r).to_numpy() for r in ratios])
    for i in range(len(close)):
        c = close_arr[i]
        row = tgt_mat[i]
        if np.isnan(c) or np.isnan(row).any(): continue
        higher = row[row > c]
        upper_arr[i] = higher.min() if higher.size > 0 else np.nan
    upper = pd.Series(upper_arr, index=close.index)
    return (close >= upper).astype(float).where(upper.notna(), np.nan)


def f08_fibx_124_close_at_or_above_fib_zone_top_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Same indicator for long swing — close at or above next higher fib."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    ratios = [1.0, 1.272, 1.618, 2.0, 2.618, 4.236]
    upper_arr = np.full(len(close), np.nan)
    close_arr = close.to_numpy()
    tgt_mat = np.column_stack([_fib_target(sl, sh, r).to_numpy() for r in ratios])
    for i in range(len(close)):
        c = close_arr[i]
        row = tgt_mat[i]
        if np.isnan(c) or np.isnan(row).any(): continue
        higher = row[row > c]
        upper_arr[i] = higher.min() if higher.size > 0 else np.nan
    upper = pd.Series(upper_arr, index=close.index)
    return (close >= upper).astype(float).where(upper.notna(), np.nan)


def f08_fibx_125_high_intraday_above_fib_zone_top_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: high (not close) >= next-upper fib of medium swing — intraday probe through zone top."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    ratios = [1.0, 1.272, 1.618, 2.0, 2.618, 4.236]
    upper_arr = np.full(len(close), np.nan)
    close_arr = close.to_numpy()
    tgt_mat = np.column_stack([_fib_target(sl, sh, r).to_numpy() for r in ratios])
    for i in range(len(close)):
        c = close_arr[i]
        row = tgt_mat[i]
        if np.isnan(c) or np.isnan(row).any(): continue
        higher = row[row > c]
        upper_arr[i] = higher.min() if higher.size > 0 else np.nan
    upper = pd.Series(upper_arr, index=close.index)
    return (high >= upper).astype(float).where(upper.notna(), np.nan)


def f08_fibx_126_price_in_extreme_zone_above_2_618_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: close > 2.618 ext of medium swing (in extreme zone)."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    return (close > _fib_target(sl, sh, 2.618)).astype(float).where(sl.notna() & sh.notna(), np.nan)


def f08_fibx_127_price_in_extreme_zone_above_4_236_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: close > 4.236 ext of long swing — terminal blowoff zone."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    return (close > _fib_target(sl, sh, 4.236)).astype(float).where(sl.notna() & sh.notna(), np.nan)


def f08_fibx_128_retest_of_swing_high_after_extension_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: max-ext in 21d was > 1.272, and current low <= swing_high (back to the breakout level)."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    e = _ext_value(close, sl, sh)
    max21 = e.rolling(MDAYS, min_periods=WDAYS).max()
    return ((max21 > 1.272) & (low <= sh)).astype(float).where(sl.notna() & sh.notna(), np.nan)


def f08_fibx_129_retest_failure_indicator_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: close < swing_high after a 21d window where ext was > 1.272 — retest failed."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    e = _ext_value(close, sl, sh)
    max21 = e.rolling(MDAYS, min_periods=WDAYS).max()
    return ((max21 > 1.272) & (close < sh)).astype(float).where(sl.notna() & sh.notna(), np.nan)


def f08_fibx_130_valid_breakout_indicator_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: close > swing_high for last 5 consecutive bars on medium swing — confirmed breakout, no fail."""
    sh = _swing_high(high, SW_M)
    above = (close > sh).astype(float)
    return (above.rolling(WDAYS, min_periods=WDAYS).sum() == float(WDAYS)).astype(float).where(sh.notna(), np.nan)


# ============================================================
# Bucket V — Aim/support distance & structural age (131-138)
# ============================================================

def f08_fibx_131_higher_fib_target_aim_distance_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized distance UP to nearest fib above current close (the next aim-for level)."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    atr = _atr(high, low, close, n=MDAYS)
    ratios = [1.0, 1.272, 1.618, 2.0, 2.618, 4.236]
    out = np.full(len(close), np.nan)
    close_arr = close.to_numpy()
    tgt_mat = np.column_stack([_fib_target(sl, sh, r).to_numpy() for r in ratios])
    atr_arr = atr.to_numpy()
    for i in range(len(close)):
        c = close_arr[i]; a = atr_arr[i]
        row = tgt_mat[i]
        if np.isnan(c) or np.isnan(row).any() or np.isnan(a) or a == 0: continue
        higher = row[row > c]
        if higher.size > 0:
            out[i] = (higher.min() - c) / a
    return pd.Series(out, index=close.index)


def f08_fibx_132_lower_fib_support_distance_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized distance DOWN to nearest fib below current close (support level)."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    atr = _atr(high, low, close, n=MDAYS)
    ratios = [1.0, 1.272, 1.618, 2.0, 2.618, 4.236]
    out = np.full(len(close), np.nan)
    close_arr = close.to_numpy()
    tgt_mat = np.column_stack([_fib_target(sl, sh, r).to_numpy() for r in ratios])
    atr_arr = atr.to_numpy()
    for i in range(len(close)):
        c = close_arr[i]; a = atr_arr[i]
        row = tgt_mat[i]
        if np.isnan(c) or np.isnan(row).any() or np.isnan(a) or a == 0: continue
        lower = row[row < c]
        if lower.size > 0:
            out[i] = (c - lower.max()) / a
    return pd.Series(out, index=close.index)


def f08_fibx_133_fib_support_break_indicator_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: today close < nearest-fib-below 21d ago — just broke the most-recently-relevant fib support."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    ratios = [1.0, 1.272, 1.618, 2.0, 2.618, 4.236]
    out = np.full(len(close), np.nan)
    close_arr = close.to_numpy()
    close_lag = close.shift(MDAYS).to_numpy()
    tgt_mat_lag = np.column_stack([_fib_target(sl, sh, r).shift(MDAYS).to_numpy() for r in ratios])
    for i in range(len(close)):
        c = close_arr[i]; c_lag = close_lag[i]
        row = tgt_mat_lag[i]
        if np.isnan(c) or np.isnan(c_lag) or np.isnan(row).any(): continue
        lower = row[row < c_lag]
        if lower.size > 0:
            out[i] = float(c < lower.max())
    return pd.Series(out, index=close.index)


def f08_fibx_134_structural_extension_age_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since most recent confirmed swing-low pivot — age of the current upswing structure."""
    sl_series = _swing_low(low, SW_M)
    changed = sl_series.ne(sl_series.shift(1)).fillna(False)
    idx_at_change = np.where(changed.to_numpy(), np.arange(len(close)), np.nan)
    last_change_idx = pd.Series(idx_at_change, index=close.index).ffill()
    return pd.Series(np.arange(len(close), dtype=float), index=close.index) - last_change_idx


def f08_fibx_135_structural_swing_size_log_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log magnitude of current medium swing: log(swing_high) - log(swing_low)."""
    sl = _swing_low(low, SW_M); sh = _swing_high(high, SW_M)
    return _safe_log(sh) - _safe_log(sl)


def f08_fibx_136_structural_swing_size_log_long(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Log magnitude of current long swing."""
    sl = _swing_low(low, SW_L); sh = _swing_high(high, SW_L)
    return _safe_log(sh) - _safe_log(sl)


def f08_fibx_137_log_swing_size_zscore_in_504d_medium(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of current log swing size (medium) vs trailing 504d distribution of same metric."""
    sz = _safe_log(_swing_high(high, SW_M)) - _safe_log(_swing_low(low, SW_M))
    return _rolling_zscore(sz, DDAYS_2Y, min_periods=YDAYS)


def f08_fibx_138_extension_speed_log_per_bar_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Average log-extension increment per bar since last swing-low: log(close/swing_low) / age_in_bars."""
    sl = _swing_low(low, SW_M)
    age = _swing_low(low, SW_M)
    changed = sl.ne(sl.shift(1)).fillna(False)
    idx_at_change = np.where(changed.to_numpy(), np.arange(len(close)), np.nan)
    last_change_idx = pd.Series(idx_at_change, index=close.index).ffill()
    age_bars = pd.Series(np.arange(len(close), dtype=float), index=close.index) - last_change_idx
    log_ext = _safe_log(close) - _safe_log(sl)
    return _safe_div(log_ext, age_bars.replace(0, np.nan))


# ============================================================
# Bucket W — Oscillator / progress / drawdown-from-max (139-150)
# ============================================================

def f08_fibx_139_annualized_extension_rate_long_swing_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annualized rate of change of ext value on long swing over trailing 252d."""
    e = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    return (e - e.shift(YDAYS))


def f08_fibx_140_fib_extension_oscillator_medium_swing_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Detrended ext on medium swing: ext - 63d_mean(ext) — cyclical component."""
    e = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return e - e.rolling(QDAYS, min_periods=MDAYS).mean()


def f08_fibx_141_fib_extension_oscillator_long_swing_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Detrended ext on long swing: ext - 252d_mean(ext)."""
    e = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    return e - e.rolling(YDAYS, min_periods=QDAYS).mean()


def f08_fibx_142_extension_drawdown_from_63d_max_medium_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Drawdown of ext from 63d trailing max — overshoot recovery."""
    e = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return e / e.rolling(QDAYS, min_periods=MDAYS).max() - 1.0


def f08_fibx_143_pct_of_252d_max_extension_currently_held_long(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current ext / 252d max ext (long swing) — held fraction of peak."""
    e = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    return _safe_div(e, e.rolling(YDAYS, min_periods=QDAYS).max())


def f08_fibx_144_extension_drawdown_from_252d_max_long_swing(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-normalized drawdown of ext-value space from 252d max on long swing."""
    e = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    return e.rolling(YDAYS, min_periods=QDAYS).max() - e


def f08_fibx_145_extension_velocity_zscore_252d_long(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 21d extension velocity on long swing vs 252d distribution of same metric."""
    e = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    v = e - e.shift(MDAYS)
    return _rolling_zscore(v, YDAYS, min_periods=QDAYS)


def f08_fibx_146_extension_acceleration_signed_medium_swing_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Signed 5d acceleration of ext value on medium swing — 2nd discrete diff."""
    e = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return e.diff(WDAYS).diff(WDAYS)


def f08_fibx_147_extension_jerk_signed_medium_swing_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Signed 5d jerk of ext value — 3rd discrete diff (note: d1/d2/d3 of this go further)."""
    e = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    return e.diff(WDAYS).diff(WDAYS).diff(WDAYS)


def f08_fibx_148_extension_concavity_medium_swing_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean of trailing-63d 2nd-diff of ext — average concavity of extension path."""
    e = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    d2 = e.diff().diff()
    return d2.rolling(QDAYS, min_periods=MDAYS).mean()


def f08_fibx_149_cumulative_extension_above_1_0_medium_swing_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum over trailing 63d of (ext - 1.0).clip(lower=0) on medium swing — accumulated overshoot."""
    e = _ext_value(close, _swing_low(low, SW_M), _swing_high(high, SW_M))
    overshoot = (e - 1.0).clip(lower=0)
    return overshoot.rolling(QDAYS, min_periods=MDAYS).sum()


def f08_fibx_150_cumulative_extension_above_1_618_long_swing_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum over trailing 252d of (ext - 1.618).clip(lower=0) on long swing — accumulated extreme overshoot."""
    e = _ext_value(close, _swing_low(low, SW_L), _swing_high(high, SW_L))
    overshoot = (e - 1.618).clip(lower=0)
    return overshoot.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
#                         REGISTRY 076-150
# ============================================================



def f08_fibx_076_log_dist_above_1_618_ext_of_lifetime_swing_d1(high, low, close):
    return f08_fibx_076_log_dist_above_1_618_ext_of_lifetime_swing(high, low, close).diff()


def f08_fibx_077_log_dist_above_2_0_ext_of_lifetime_swing_d1(high, low, close):
    return f08_fibx_077_log_dist_above_2_0_ext_of_lifetime_swing(high, low, close).diff()


def f08_fibx_078_log_dist_above_2_618_ext_of_lifetime_swing_d1(high, low, close):
    return f08_fibx_078_log_dist_above_2_618_ext_of_lifetime_swing(high, low, close).diff()


def f08_fibx_079_atr_dist_above_1_618_ext_of_lifetime_swing_d1(high, low, close):
    return f08_fibx_079_atr_dist_above_1_618_ext_of_lifetime_swing(high, low, close).diff()


def f08_fibx_080_current_extension_value_lifetime_swing_d1(high, low, close):
    return f08_fibx_080_current_extension_value_lifetime_swing(high, low, close).diff()


def f08_fibx_081_count_fib_levels_exceeded_lifetime_swing_d1(high, low, close):
    return f08_fibx_081_count_fib_levels_exceeded_lifetime_swing(high, low, close).diff()


def f08_fibx_082_bars_since_first_crossing_1_618_lifetime_d1(high, low, close):
    return f08_fibx_082_bars_since_first_crossing_1_618_lifetime(high, low, close).diff()


def f08_fibx_083_extension_disagreement_medium_vs_lifetime_d1(high, low, close):
    return f08_fibx_083_extension_disagreement_medium_vs_lifetime(high, low, close).diff()


def f08_fibx_084_geometric_extension_log_medium_swing_d1(high, low, close):
    return f08_fibx_084_geometric_extension_log_medium_swing(high, low, close).diff()


def f08_fibx_085_geometric_extension_log_long_swing_d1(high, low, close):
    return f08_fibx_085_geometric_extension_log_long_swing(high, low, close).diff()


def f08_fibx_086_log_dist_above_1_618_geometric_medium_swing_d1(high, low, close):
    return f08_fibx_086_log_dist_above_1_618_geometric_medium_swing(high, low, close).diff()


def f08_fibx_087_log_dist_above_1_618_geometric_long_swing_d1(high, low, close):
    return f08_fibx_087_log_dist_above_1_618_geometric_long_swing(high, low, close).diff()


def f08_fibx_088_sigma_normalized_extension_medium_swing_d1(high, low, close):
    return f08_fibx_088_sigma_normalized_extension_medium_swing(high, low, close).diff()


def f08_fibx_089_sigma_normalized_extension_long_swing_d1(high, low, close):
    return f08_fibx_089_sigma_normalized_extension_long_swing(high, low, close).diff()


def f08_fibx_090_sigma_normalized_log_dist_above_1_618_medium_swing_d1(high, low, close):
    return f08_fibx_090_sigma_normalized_log_dist_above_1_618_medium_swing(high, low, close).diff()


def f08_fibx_091_sigma_normalized_log_dist_above_2_0_long_swing_d1(high, low, close):
    return f08_fibx_091_sigma_normalized_log_dist_above_2_0_long_swing(high, low, close).diff()


def f08_fibx_092_count_bars_high_above_1_618_ext_medium_swing_63d_d1(high, low, close):
    return f08_fibx_092_count_bars_high_above_1_618_ext_medium_swing_63d(high, low, close).diff()


def f08_fibx_093_count_bars_high_above_2_0_ext_medium_swing_63d_d1(high, low, close):
    return f08_fibx_093_count_bars_high_above_2_0_ext_medium_swing_63d(high, low, close).diff()


def f08_fibx_094_count_bars_high_above_2_618_ext_long_swing_252d_d1(high, low, close):
    return f08_fibx_094_count_bars_high_above_2_618_ext_long_swing_252d(high, low, close).diff()


def f08_fibx_095_consecutive_days_close_above_1_618_ext_medium_swing_d1(high, low, close):
    return f08_fibx_095_consecutive_days_close_above_1_618_ext_medium_swing(high, low, close).diff()


def f08_fibx_096_consecutive_days_close_above_2_0_ext_long_swing_d1(high, low, close):
    return f08_fibx_096_consecutive_days_close_above_2_0_ext_long_swing(high, low, close).diff()


def f08_fibx_097_fraction_63d_window_above_1_618_ext_medium_swing_d1(high, low, close):
    return f08_fibx_097_fraction_63d_window_above_1_618_ext_medium_swing(high, low, close).diff()


def f08_fibx_098_fraction_252d_window_above_1_0_ext_long_swing_d1(high, low, close):
    return f08_fibx_098_fraction_252d_window_above_1_0_ext_long_swing(high, low, close).diff()


def f08_fibx_099_mean_extension_value_medium_swing_63d_d1(high, low, close):
    return f08_fibx_099_mean_extension_value_medium_swing_63d(high, low, close).diff()


def f08_fibx_100_max_extension_value_medium_swing_63d_d1(high, low, close):
    return f08_fibx_100_max_extension_value_medium_swing_63d(high, low, close).diff()


def f08_fibx_101_max_extension_value_long_swing_252d_d1(high, low, close):
    return f08_fibx_101_max_extension_value_long_swing_252d(high, low, close).diff()


def f08_fibx_102_range_of_extension_medium_swing_63d_d1(high, low, close):
    return f08_fibx_102_range_of_extension_medium_swing_63d(high, low, close).diff()


def f08_fibx_103_range_of_extension_long_swing_252d_d1(high, low, close):
    return f08_fibx_103_range_of_extension_long_swing_252d(high, low, close).diff()


def f08_fibx_104_std_extension_medium_swing_63d_d1(high, low, close):
    return f08_fibx_104_std_extension_medium_swing_63d(high, low, close).diff()


def f08_fibx_105_zscore_current_extension_in_252d_long_swing_d1(high, low, close):
    return f08_fibx_105_zscore_current_extension_in_252d_long_swing(high, low, close).diff()


def f08_fibx_106_percentile_rank_current_extension_in_252d_long_swing_d1(high, low, close):
    return f08_fibx_106_percentile_rank_current_extension_in_252d_long_swing(high, low, close).diff()


def f08_fibx_107_percentile_rank_current_extension_in_1260d_long_swing_d1(high, low, close):
    return f08_fibx_107_percentile_rank_current_extension_in_1260d_long_swing(high, low, close).diff()


def f08_fibx_108_retracement_after_max_extension_medium_swing_63d_d1(high, low, close):
    return f08_fibx_108_retracement_after_max_extension_medium_swing_63d(high, low, close).diff()


def f08_fibx_109_retracement_after_max_extension_long_swing_252d_d1(high, low, close):
    return f08_fibx_109_retracement_after_max_extension_long_swing_252d(high, low, close).diff()


def f08_fibx_110_recovery_from_retracement_medium_swing_21d_d1(high, low, close):
    return f08_fibx_110_recovery_from_retracement_medium_swing_21d(high, low, close).diff()


def f08_fibx_111_negative_extension_below_1_0_after_breach_medium_swing_d1(high, low, close):
    return f08_fibx_111_negative_extension_below_1_0_after_breach_medium_swing(high, low, close).diff()


def f08_fibx_112_depth_of_intra_extension_pullback_medium_swing_63d_d1(high, low, close):
    return f08_fibx_112_depth_of_intra_extension_pullback_medium_swing_63d(high, low, close).diff()


def f08_fibx_113_count_distinct_max_extensions_medium_swing_252d_d1(high, low, close):
    return f08_fibx_113_count_distinct_max_extensions_medium_swing_252d(high, low, close).diff()


def f08_fibx_114_mean_bars_between_new_extension_highs_medium_swing_252d_d1(high, low, close):
    return f08_fibx_114_mean_bars_between_new_extension_highs_medium_swing_252d(high, low, close).diff()


def f08_fibx_115_fib_cluster_count_within_atr_of_close_medium_swing_d1(high, low, close):
    return f08_fibx_115_fib_cluster_count_within_atr_of_close_medium_swing(high, low, close).diff()


def f08_fibx_116_fib_cluster_count_within_2atr_of_close_long_swing_d1(high, low, close):
    return f08_fibx_116_fib_cluster_count_within_2atr_of_close_long_swing(high, low, close).diff()


def f08_fibx_117_fib_cluster_density_near_close_medium_swing_d1(high, low, close):
    return f08_fibx_117_fib_cluster_density_near_close_medium_swing(high, low, close).diff()


def f08_fibx_118_nearest_fib_zone_width_medium_swing_d1(high, low, close):
    return f08_fibx_118_nearest_fib_zone_width_medium_swing(high, low, close).diff()


def f08_fibx_119_position_within_fib_zone_medium_swing_d1(high, low, close):
    return f08_fibx_119_position_within_fib_zone_medium_swing(high, low, close).diff()


def f08_fibx_120_extension_dispersion_across_horizons_d1(high, low, close):
    return f08_fibx_120_extension_dispersion_across_horizons(high, low, close).diff()


def f08_fibx_121_extension_range_across_horizons_d1(high, low, close):
    return f08_fibx_121_extension_range_across_horizons(high, low, close).diff()


def f08_fibx_122_log_diff_extension_medium_minus_long_d1(high, low, close):
    return f08_fibx_122_log_diff_extension_medium_minus_long(high, low, close).diff()


def f08_fibx_123_close_at_or_above_fib_zone_top_medium_swing_d1(high, low, close):
    return f08_fibx_123_close_at_or_above_fib_zone_top_medium_swing(high, low, close).diff()


def f08_fibx_124_close_at_or_above_fib_zone_top_long_swing_d1(high, low, close):
    return f08_fibx_124_close_at_or_above_fib_zone_top_long_swing(high, low, close).diff()


def f08_fibx_125_high_intraday_above_fib_zone_top_medium_swing_d1(high, low, close):
    return f08_fibx_125_high_intraday_above_fib_zone_top_medium_swing(high, low, close).diff()


def f08_fibx_126_price_in_extreme_zone_above_2_618_medium_swing_d1(high, low, close):
    return f08_fibx_126_price_in_extreme_zone_above_2_618_medium_swing(high, low, close).diff()


def f08_fibx_127_price_in_extreme_zone_above_4_236_long_swing_d1(high, low, close):
    return f08_fibx_127_price_in_extreme_zone_above_4_236_long_swing(high, low, close).diff()


def f08_fibx_128_retest_of_swing_high_after_extension_medium_swing_d1(high, low, close):
    return f08_fibx_128_retest_of_swing_high_after_extension_medium_swing(high, low, close).diff()


def f08_fibx_129_retest_failure_indicator_medium_swing_d1(high, low, close):
    return f08_fibx_129_retest_failure_indicator_medium_swing(high, low, close).diff()


def f08_fibx_130_valid_breakout_indicator_medium_swing_d1(high, low, close):
    return f08_fibx_130_valid_breakout_indicator_medium_swing(high, low, close).diff()


def f08_fibx_131_higher_fib_target_aim_distance_medium_swing_d1(high, low, close):
    return f08_fibx_131_higher_fib_target_aim_distance_medium_swing(high, low, close).diff()


def f08_fibx_132_lower_fib_support_distance_medium_swing_d1(high, low, close):
    return f08_fibx_132_lower_fib_support_distance_medium_swing(high, low, close).diff()


def f08_fibx_133_fib_support_break_indicator_medium_swing_d1(high, low, close):
    return f08_fibx_133_fib_support_break_indicator_medium_swing(high, low, close).diff()


def f08_fibx_134_structural_extension_age_medium_swing_d1(high, low, close):
    return f08_fibx_134_structural_extension_age_medium_swing(high, low, close).diff()


def f08_fibx_135_structural_swing_size_log_medium_d1(high, low, close):
    return f08_fibx_135_structural_swing_size_log_medium(high, low, close).diff()


def f08_fibx_136_structural_swing_size_log_long_d1(high, low, close):
    return f08_fibx_136_structural_swing_size_log_long(high, low, close).diff()


def f08_fibx_137_log_swing_size_zscore_in_504d_medium_d1(high, low, close):
    return f08_fibx_137_log_swing_size_zscore_in_504d_medium(high, low, close).diff()


def f08_fibx_138_extension_speed_log_per_bar_medium_swing_d1(high, low, close):
    return f08_fibx_138_extension_speed_log_per_bar_medium_swing(high, low, close).diff()


def f08_fibx_139_annualized_extension_rate_long_swing_252d_d1(high, low, close):
    return f08_fibx_139_annualized_extension_rate_long_swing_252d(high, low, close).diff()


def f08_fibx_140_fib_extension_oscillator_medium_swing_63d_d1(high, low, close):
    return f08_fibx_140_fib_extension_oscillator_medium_swing_63d(high, low, close).diff()


def f08_fibx_141_fib_extension_oscillator_long_swing_252d_d1(high, low, close):
    return f08_fibx_141_fib_extension_oscillator_long_swing_252d(high, low, close).diff()


def f08_fibx_142_extension_drawdown_from_63d_max_medium_swing_d1(high, low, close):
    return f08_fibx_142_extension_drawdown_from_63d_max_medium_swing(high, low, close).diff()


def f08_fibx_143_pct_of_252d_max_extension_currently_held_long_d1(high, low, close):
    return f08_fibx_143_pct_of_252d_max_extension_currently_held_long(high, low, close).diff()


def f08_fibx_144_extension_drawdown_from_252d_max_long_swing_d1(high, low, close):
    return f08_fibx_144_extension_drawdown_from_252d_max_long_swing(high, low, close).diff()


def f08_fibx_145_extension_velocity_zscore_252d_long_d1(high, low, close):
    return f08_fibx_145_extension_velocity_zscore_252d_long(high, low, close).diff()


def f08_fibx_146_extension_acceleration_signed_medium_swing_5d_d1(high, low, close):
    return f08_fibx_146_extension_acceleration_signed_medium_swing_5d(high, low, close).diff()


def f08_fibx_147_extension_jerk_signed_medium_swing_5d_d1(high, low, close):
    return f08_fibx_147_extension_jerk_signed_medium_swing_5d(high, low, close).diff()


def f08_fibx_148_extension_concavity_medium_swing_63d_d1(high, low, close):
    return f08_fibx_148_extension_concavity_medium_swing_63d(high, low, close).diff()


def f08_fibx_149_cumulative_extension_above_1_0_medium_swing_63d_d1(high, low, close):
    return f08_fibx_149_cumulative_extension_above_1_0_medium_swing_63d(high, low, close).diff()


def f08_fibx_150_cumulative_extension_above_1_618_long_swing_252d_d1(high, low, close):
    return f08_fibx_150_cumulative_extension_above_1_618_long_swing_252d(high, low, close).diff()


FIBONACCI_EXTENSION_SIGNATURE_D1_REGISTRY_076_150 = {
    "f08_fibx_076_log_dist_above_1_618_ext_of_lifetime_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_076_log_dist_above_1_618_ext_of_lifetime_swing_d1},
    "f08_fibx_077_log_dist_above_2_0_ext_of_lifetime_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_077_log_dist_above_2_0_ext_of_lifetime_swing_d1},
    "f08_fibx_078_log_dist_above_2_618_ext_of_lifetime_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_078_log_dist_above_2_618_ext_of_lifetime_swing_d1},
    "f08_fibx_079_atr_dist_above_1_618_ext_of_lifetime_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_079_atr_dist_above_1_618_ext_of_lifetime_swing_d1},
    "f08_fibx_080_current_extension_value_lifetime_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_080_current_extension_value_lifetime_swing_d1},
    "f08_fibx_081_count_fib_levels_exceeded_lifetime_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_081_count_fib_levels_exceeded_lifetime_swing_d1},
    "f08_fibx_082_bars_since_first_crossing_1_618_lifetime_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_082_bars_since_first_crossing_1_618_lifetime_d1},
    "f08_fibx_083_extension_disagreement_medium_vs_lifetime_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_083_extension_disagreement_medium_vs_lifetime_d1},
    "f08_fibx_084_geometric_extension_log_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_084_geometric_extension_log_medium_swing_d1},
    "f08_fibx_085_geometric_extension_log_long_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_085_geometric_extension_log_long_swing_d1},
    "f08_fibx_086_log_dist_above_1_618_geometric_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_086_log_dist_above_1_618_geometric_medium_swing_d1},
    "f08_fibx_087_log_dist_above_1_618_geometric_long_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_087_log_dist_above_1_618_geometric_long_swing_d1},
    "f08_fibx_088_sigma_normalized_extension_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_088_sigma_normalized_extension_medium_swing_d1},
    "f08_fibx_089_sigma_normalized_extension_long_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_089_sigma_normalized_extension_long_swing_d1},
    "f08_fibx_090_sigma_normalized_log_dist_above_1_618_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_090_sigma_normalized_log_dist_above_1_618_medium_swing_d1},
    "f08_fibx_091_sigma_normalized_log_dist_above_2_0_long_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_091_sigma_normalized_log_dist_above_2_0_long_swing_d1},
    "f08_fibx_092_count_bars_high_above_1_618_ext_medium_swing_63d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_092_count_bars_high_above_1_618_ext_medium_swing_63d_d1},
    "f08_fibx_093_count_bars_high_above_2_0_ext_medium_swing_63d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_093_count_bars_high_above_2_0_ext_medium_swing_63d_d1},
    "f08_fibx_094_count_bars_high_above_2_618_ext_long_swing_252d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_094_count_bars_high_above_2_618_ext_long_swing_252d_d1},
    "f08_fibx_095_consecutive_days_close_above_1_618_ext_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_095_consecutive_days_close_above_1_618_ext_medium_swing_d1},
    "f08_fibx_096_consecutive_days_close_above_2_0_ext_long_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_096_consecutive_days_close_above_2_0_ext_long_swing_d1},
    "f08_fibx_097_fraction_63d_window_above_1_618_ext_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_097_fraction_63d_window_above_1_618_ext_medium_swing_d1},
    "f08_fibx_098_fraction_252d_window_above_1_0_ext_long_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_098_fraction_252d_window_above_1_0_ext_long_swing_d1},
    "f08_fibx_099_mean_extension_value_medium_swing_63d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_099_mean_extension_value_medium_swing_63d_d1},
    "f08_fibx_100_max_extension_value_medium_swing_63d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_100_max_extension_value_medium_swing_63d_d1},
    "f08_fibx_101_max_extension_value_long_swing_252d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_101_max_extension_value_long_swing_252d_d1},
    "f08_fibx_102_range_of_extension_medium_swing_63d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_102_range_of_extension_medium_swing_63d_d1},
    "f08_fibx_103_range_of_extension_long_swing_252d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_103_range_of_extension_long_swing_252d_d1},
    "f08_fibx_104_std_extension_medium_swing_63d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_104_std_extension_medium_swing_63d_d1},
    "f08_fibx_105_zscore_current_extension_in_252d_long_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_105_zscore_current_extension_in_252d_long_swing_d1},
    "f08_fibx_106_percentile_rank_current_extension_in_252d_long_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_106_percentile_rank_current_extension_in_252d_long_swing_d1},
    "f08_fibx_107_percentile_rank_current_extension_in_1260d_long_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_107_percentile_rank_current_extension_in_1260d_long_swing_d1},
    "f08_fibx_108_retracement_after_max_extension_medium_swing_63d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_108_retracement_after_max_extension_medium_swing_63d_d1},
    "f08_fibx_109_retracement_after_max_extension_long_swing_252d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_109_retracement_after_max_extension_long_swing_252d_d1},
    "f08_fibx_110_recovery_from_retracement_medium_swing_21d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_110_recovery_from_retracement_medium_swing_21d_d1},
    "f08_fibx_111_negative_extension_below_1_0_after_breach_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_111_negative_extension_below_1_0_after_breach_medium_swing_d1},
    "f08_fibx_112_depth_of_intra_extension_pullback_medium_swing_63d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_112_depth_of_intra_extension_pullback_medium_swing_63d_d1},
    "f08_fibx_113_count_distinct_max_extensions_medium_swing_252d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_113_count_distinct_max_extensions_medium_swing_252d_d1},
    "f08_fibx_114_mean_bars_between_new_extension_highs_medium_swing_252d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_114_mean_bars_between_new_extension_highs_medium_swing_252d_d1},
    "f08_fibx_115_fib_cluster_count_within_atr_of_close_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_115_fib_cluster_count_within_atr_of_close_medium_swing_d1},
    "f08_fibx_116_fib_cluster_count_within_2atr_of_close_long_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_116_fib_cluster_count_within_2atr_of_close_long_swing_d1},
    "f08_fibx_117_fib_cluster_density_near_close_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_117_fib_cluster_density_near_close_medium_swing_d1},
    "f08_fibx_118_nearest_fib_zone_width_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_118_nearest_fib_zone_width_medium_swing_d1},
    "f08_fibx_119_position_within_fib_zone_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_119_position_within_fib_zone_medium_swing_d1},
    "f08_fibx_120_extension_dispersion_across_horizons_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_120_extension_dispersion_across_horizons_d1},
    "f08_fibx_121_extension_range_across_horizons_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_121_extension_range_across_horizons_d1},
    "f08_fibx_122_log_diff_extension_medium_minus_long_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_122_log_diff_extension_medium_minus_long_d1},
    "f08_fibx_123_close_at_or_above_fib_zone_top_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_123_close_at_or_above_fib_zone_top_medium_swing_d1},
    "f08_fibx_124_close_at_or_above_fib_zone_top_long_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_124_close_at_or_above_fib_zone_top_long_swing_d1},
    "f08_fibx_125_high_intraday_above_fib_zone_top_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_125_high_intraday_above_fib_zone_top_medium_swing_d1},
    "f08_fibx_126_price_in_extreme_zone_above_2_618_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_126_price_in_extreme_zone_above_2_618_medium_swing_d1},
    "f08_fibx_127_price_in_extreme_zone_above_4_236_long_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_127_price_in_extreme_zone_above_4_236_long_swing_d1},
    "f08_fibx_128_retest_of_swing_high_after_extension_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_128_retest_of_swing_high_after_extension_medium_swing_d1},
    "f08_fibx_129_retest_failure_indicator_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_129_retest_failure_indicator_medium_swing_d1},
    "f08_fibx_130_valid_breakout_indicator_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_130_valid_breakout_indicator_medium_swing_d1},
    "f08_fibx_131_higher_fib_target_aim_distance_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_131_higher_fib_target_aim_distance_medium_swing_d1},
    "f08_fibx_132_lower_fib_support_distance_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_132_lower_fib_support_distance_medium_swing_d1},
    "f08_fibx_133_fib_support_break_indicator_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_133_fib_support_break_indicator_medium_swing_d1},
    "f08_fibx_134_structural_extension_age_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_134_structural_extension_age_medium_swing_d1},
    "f08_fibx_135_structural_swing_size_log_medium_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_135_structural_swing_size_log_medium_d1},
    "f08_fibx_136_structural_swing_size_log_long_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_136_structural_swing_size_log_long_d1},
    "f08_fibx_137_log_swing_size_zscore_in_504d_medium_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_137_log_swing_size_zscore_in_504d_medium_d1},
    "f08_fibx_138_extension_speed_log_per_bar_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_138_extension_speed_log_per_bar_medium_swing_d1},
    "f08_fibx_139_annualized_extension_rate_long_swing_252d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_139_annualized_extension_rate_long_swing_252d_d1},
    "f08_fibx_140_fib_extension_oscillator_medium_swing_63d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_140_fib_extension_oscillator_medium_swing_63d_d1},
    "f08_fibx_141_fib_extension_oscillator_long_swing_252d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_141_fib_extension_oscillator_long_swing_252d_d1},
    "f08_fibx_142_extension_drawdown_from_63d_max_medium_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_142_extension_drawdown_from_63d_max_medium_swing_d1},
    "f08_fibx_143_pct_of_252d_max_extension_currently_held_long_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_143_pct_of_252d_max_extension_currently_held_long_d1},
    "f08_fibx_144_extension_drawdown_from_252d_max_long_swing_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_144_extension_drawdown_from_252d_max_long_swing_d1},
    "f08_fibx_145_extension_velocity_zscore_252d_long_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_145_extension_velocity_zscore_252d_long_d1},
    "f08_fibx_146_extension_acceleration_signed_medium_swing_5d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_146_extension_acceleration_signed_medium_swing_5d_d1},
    "f08_fibx_147_extension_jerk_signed_medium_swing_5d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_147_extension_jerk_signed_medium_swing_5d_d1},
    "f08_fibx_148_extension_concavity_medium_swing_63d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_148_extension_concavity_medium_swing_63d_d1},
    "f08_fibx_149_cumulative_extension_above_1_0_medium_swing_63d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_149_cumulative_extension_above_1_0_medium_swing_63d_d1},
    "f08_fibx_150_cumulative_extension_above_1_618_long_swing_252d_d1": {"inputs": ["high", "low", "close"], "func": f08_fibx_150_cumulative_extension_above_1_618_long_swing_252d_d1},
}
