"""40_atr_expansion_dynamics d3 features 451-525 — order-3 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
import math
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260

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
    idx = num.index if hasattr(num, 'index') else None
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

def _ema(s, n):
    return s.ewm(span=n, min_periods=n, adjust=False).mean()

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
        xm = x.mean()
        wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def _bars_since(ind):
    arr = ind.fillna(0).astype(int).values
    out = np.full(len(arr), np.nan)
    bars = np.nan
    for i, x in enumerate(arr):
        if x:
            bars = 0
        elif np.isfinite(bars):
            bars = bars + 1
        out[i] = bars
    return pd.Series(out, index=ind.index)

def f40_atxd_451_resistance_test_count_63d_252d_d3(high: pd.Series) -> pd.Series:
    """Count of bars where high within 1% of 63d-max (resistance tests) over 252d."""
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    return ((rmax - high) / rmax < 0.01).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_452_support_test_count_63d_252d_d3(low: pd.Series) -> pd.Series:
    """Count of bars where low within 1% of 63d-min (support tests) over 252d."""
    rmin = low.rolling(QDAYS, min_periods=MDAYS).min()
    return ((low - rmin) / rmin < 0.01).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_453_resistance_break_count_252d_d3(high: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where close > prior 63d-max (resistance break) over 252d."""
    rmax_prior = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (close > rmax_prior).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_454_support_break_count_252d_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where close < prior 63d-min (support break) over 252d."""
    rmin_prior = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    return (close < rmin_prior).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_455_atr_at_resistance_test_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR(21) on bars where high tests 63d-max (within 1%), over 252d."""
    a = _atr(high, low, close, MDAYS)
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    test = (rmax - high) / rmax < 0.01
    return a.where(test, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_456_atr_at_support_test_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR(21) on bars where low tests 63d-min (within 1%), over 252d."""
    a = _atr(high, low, close, MDAYS)
    rmin = low.rolling(QDAYS, min_periods=MDAYS).min()
    test = (low - rmin) / rmin < 0.01
    return a.where(test, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_457_bars_since_resistance_test_d3(high: pd.Series) -> pd.Series:
    """Bars since high last tested 63d-max within 1%."""
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    test = (rmax - high) / rmax < 0.01
    return _bars_since(test.astype(float)).diff().diff().diff()

def f40_atxd_458_bars_since_support_test_d3(low: pd.Series) -> pd.Series:
    """Bars since low last tested 63d-min within 1%."""
    rmin = low.rolling(QDAYS, min_periods=MDAYS).min()
    test = (low - rmin) / rmin < 0.01
    return _bars_since(test.astype(float)).diff().diff().diff()

def f40_atxd_459_failed_resistance_break_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """High pierces 63d-max but close < prior max, count over 252d (false breakout)."""
    rmax_prior = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    pierce = high > rmax_prior
    failed = close < rmax_prior
    return (pierce & failed).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_460_failed_support_break_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Low pierces 63d-min but close > prior min, count over 252d (false breakdown)."""
    rmin_prior = low.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    pierce = low < rmin_prior
    failed = close > rmin_prior
    return (pierce & failed).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_461_atr_trend_5d_slope_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean 5d slope of ATR(21) over 252d (vol-trend persistence)."""
    a = _atr(high, low, close, MDAYS)
    return _rolling_slope(a, WDAYS).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_462_atr_trend_21d_slope_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean 21d slope of ATR(21) over 252d."""
    a = _atr(high, low, close, MDAYS)
    return _rolling_slope(a, MDAYS).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_463_atr_trend_sign_consistency_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars where 5d-ATR-slope same sign as 21d-ATR-slope, over 63d."""
    a = _atr(high, low, close, MDAYS)
    sl5 = _rolling_slope(a, WDAYS)
    sl21 = _rolling_slope(a, MDAYS)
    same = (np.sign(sl5) == np.sign(sl21)) & (np.sign(sl5) != 0)
    return same.astype(float).rolling(QDAYS, min_periods=MDAYS).mean().diff().diff().diff()

def f40_atxd_464_atr_trend_strength_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """|21d slope of ATR(21)| × bars-of-consistent-direction / 21 — trend strength."""
    a = _atr(high, low, close, MDAYS)
    sl = _rolling_slope(a, MDAYS)
    sign = np.sign(sl)
    same_dir_run = sign.groupby((sign != sign.shift(1)).cumsum()).cumcount() + 1
    return _safe_div(sl.abs() * same_dir_run, MDAYS).diff().diff().diff()

def f40_atxd_465_atr_trend_reversals_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of 21d-ATR-slope sign changes over 252d (trend reversals)."""
    a = _atr(high, low, close, MDAYS)
    sl = _rolling_slope(a, MDAYS)
    return np.sign(sl).diff().abs().rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_466_atr_max_runup_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max ATR(21) / min(ATR(21)) within trailing 63d (vol-runup factor)."""
    a = _atr(high, low, close, MDAYS)
    return _safe_div(a.rolling(QDAYS, min_periods=MDAYS).max(), a.rolling(QDAYS, min_periods=MDAYS).min()).diff().diff().diff()

def f40_atxd_467_atr_max_rundown_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """min ATR(21) / max(ATR(21)) within trailing 63d (vol-rundown factor)."""
    a = _atr(high, low, close, MDAYS)
    return _safe_div(a.rolling(QDAYS, min_periods=MDAYS).min(), a.rolling(QDAYS, min_periods=MDAYS).max()).diff().diff().diff()

def f40_atxd_468_atr_trend_zscore_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 21d-ATR-slope within 252d (normalized trend strength)."""
    a = _atr(high, low, close, MDAYS)
    return _rolling_zscore(_rolling_slope(a, MDAYS), YDAYS).diff().diff().diff()

def f40_atxd_469_atr_trend_persistence_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """AR(1) coef of 21d-ATR-slope over 252d — trend persistence."""
    a = _atr(high, low, close, MDAYS)
    sl = _rolling_slope(a, MDAYS)
    return sl.rolling(YDAYS, min_periods=QDAYS).corr(sl.shift(1)).diff().diff().diff()

def f40_atxd_470_atr_directional_score_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Net signed ΔATR(21) over 63d / Σ|ΔATR(21)| (directional vs choppy ATR)."""
    a = _atr(high, low, close, MDAYS)
    da = a.diff()
    net = da.rolling(QDAYS, min_periods=MDAYS).sum()
    total = da.abs().rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(net, total).diff().diff().diff()

def f40_atxd_471_atr_after_nr4_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR(21) in 5 bars after NR4 events over 252d."""
    rng = high - low
    nr4_lag = (rng.shift(WDAYS) == rng.rolling(4, min_periods=4).min().shift(WDAYS)).fillna(False)
    a = _atr(high, low, close, MDAYS)
    return a.where(nr4_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_472_atr_after_wr7_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR(21) in 5 bars after WR7 events over 252d."""
    rng = high - low
    wr7_lag = (rng.shift(WDAYS) == rng.rolling(7, min_periods=7).max().shift(WDAYS)).fillna(False)
    a = _atr(high, low, close, MDAYS)
    return a.where(wr7_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_473_atr_after_inside_bar_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR(21) in 5 bars after inside-bar events over 252d."""
    inside_lag = ((high.shift(WDAYS) < high.shift(WDAYS + 1)) & (low.shift(WDAYS) > low.shift(WDAYS + 1))).fillna(False)
    a = _atr(high, low, close, MDAYS)
    return a.where(inside_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_474_atr_after_outside_bar_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR(21) in 5 bars after outside-bar events over 252d."""
    outside_lag = ((high.shift(WDAYS) > high.shift(WDAYS + 1)) & (low.shift(WDAYS) < low.shift(WDAYS + 1))).fillna(False)
    a = _atr(high, low, close, MDAYS)
    return a.where(outside_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_475_atr_after_doji_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR(21) in 5 bars after doji bars (|C-O|/range < 0.1) over 252d."""
    rng = (high - low).replace(0, np.nan)
    doji_lag = ((close.shift(WDAYS) - open.shift(WDAYS)).abs() / rng.shift(WDAYS) < 0.1).fillna(False)
    a = _atr(high, low, close, MDAYS)
    return a.where(doji_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_476_atr_after_gap_up_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR(21) in 5 bars after >1% gap-up events over 252d."""
    gap_lag = (open.shift(WDAYS) > close.shift(WDAYS + 1) * 1.01).fillna(False)
    a = _atr(high, low, close, MDAYS)
    return a.where(gap_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_477_atr_after_gap_down_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR(21) in 5 bars after >1% gap-down events over 252d."""
    gap_lag = (open.shift(WDAYS) < close.shift(WDAYS + 1) * 0.99).fillna(False)
    a = _atr(high, low, close, MDAYS)
    return a.where(gap_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_478_atr_after_engulfing_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR(21) in 5 bars after engulfing bars (today's body > 1.5·prior body) over 252d."""
    body = (close - open).abs()
    engulf_lag = (body.shift(WDAYS) > 1.5 * body.shift(WDAYS + 1)).fillna(False)
    a = _atr(high, low, close, MDAYS)
    return a.where(engulf_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_479_atr_change_after_big_close_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (ATR_now − ATR_5d_ago) on bars 5d after big-close (|r|>2σ_21) over 252d."""
    r = (close - close.shift(1)) / close.shift(1)
    sig_r = r.rolling(MDAYS, min_periods=WDAYS).std()
    big_lag = (r.shift(WDAYS).abs() > 2 * sig_r.shift(WDAYS)).fillna(False)
    a = _atr(high, low, close, MDAYS)
    return (a - a.shift(WDAYS)).where(big_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_480_atr_after_5d_streak_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR(21) after 5-day same-direction streak (5 consecutive up or down) over 252d."""
    r = close.diff()
    up5 = (r.shift(1) > 0) & (r.shift(2) > 0) & (r.shift(3) > 0) & (r.shift(4) > 0) & (r.shift(5) > 0)
    dn5 = (r.shift(1) < 0) & (r.shift(2) < 0) & (r.shift(3) < 0) & (r.shift(4) < 0) & (r.shift(5) < 0)
    streak = up5 | dn5
    a = _atr(high, low, close, MDAYS)
    return a.where(streak, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_481_tr_skew_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Skew of TR over 63d."""
    return _true_range(high, low, close).rolling(QDAYS, min_periods=MDAYS).skew().diff().diff().diff()

def f40_atxd_482_tr_kurt_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Kurt of TR over 63d."""
    return _true_range(high, low, close).rolling(QDAYS, min_periods=MDAYS).kurt().diff().diff().diff()

def f40_atxd_483_tr_skew_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Skew of TR over 252d."""
    return _true_range(high, low, close).rolling(YDAYS, min_periods=QDAYS).skew().diff().diff().diff()

def f40_atxd_484_log_tr_skew_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Skew of log(TR) over 252d (log-scale skew)."""
    return _safe_log(_true_range(high, low, close)).rolling(YDAYS, min_periods=QDAYS).skew().diff().diff().diff()

def f40_atxd_485_log_tr_kurt_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Kurt of log(TR) over 252d."""
    return _safe_log(_true_range(high, low, close)).rolling(YDAYS, min_periods=QDAYS).kurt().diff().diff().diff()

def f40_atxd_486_tr_p99_over_p50_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """p99(TR)/p50(TR) over 252d (right-tail extremity)."""
    tr = _true_range(high, low, close)
    return _safe_div(tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.99), tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.5)).diff().diff().diff()

def f40_atxd_487_tr_p99_over_p90_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """p99(TR)/p90(TR) over 252d (deep-tail concentration)."""
    tr = _true_range(high, low, close)
    return _safe_div(tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.99), tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)).diff().diff().diff()

def f40_atxd_488_tr_p90_p10_range_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """p90(TR) − p10(TR) over 252d (range-of-range central spread)."""
    tr = _true_range(high, low, close)
    return (tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.9) - tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)).diff().diff().diff()

def f40_atxd_489_tr_bimodality_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bimodality coef of TR distribution over 252d."""
    tr = _true_range(high, low, close)
    sk = tr.rolling(YDAYS, min_periods=QDAYS).skew()
    kt = tr.rolling(YDAYS, min_periods=QDAYS).kurt()
    n = YDAYS
    corr = 3.0 * (n - 1) ** 2 / ((n - 2) * (n - 3))
    return ((sk ** 2 + 1.0) / (kt + corr)).diff().diff().diff()

def f40_atxd_490_tr_entropy_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Shannon entropy of TR-bin distribution (10 bins) over 252d."""
    tr = _true_range(high, low, close)

    def _ent(w):
        ww = w[~np.isnan(w)]
        if len(ww) < QDAYS:
            return np.nan
        h, _ = np.histogram(ww, bins=10)
        p = h.astype(float) / h.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    return tr.rolling(YDAYS, min_periods=QDAYS).apply(_ent, raw=True).diff().diff().diff()

def f40_atxd_491_nbar_true_range_5d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-bar true range: max(H, 5d) − min(L, 5d)."""
    return (high.rolling(WDAYS, min_periods=2).max() - low.rolling(WDAYS, min_periods=2).min()).diff().diff().diff()

def f40_atxd_492_nbar_true_range_63d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """63-bar true range: max(H, 63d) − min(L, 63d)."""
    return (high.rolling(QDAYS, min_periods=MDAYS).max() - low.rolling(QDAYS, min_periods=MDAYS).min()).diff().diff().diff()

def f40_atxd_493_nbar_true_range_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    """252-bar true range."""
    return (high.rolling(YDAYS, min_periods=QDAYS).max() - low.rolling(YDAYS, min_periods=QDAYS).min()).diff().diff().diff()

def f40_atxd_494_close_position_in_5d_range_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close-position in 5d range: (C − 5d-min-L) / (5d-max-H − 5d-min-L)."""
    h5 = high.rolling(WDAYS, min_periods=2).max()
    l5 = low.rolling(WDAYS, min_periods=2).min()
    return _safe_div(close - l5, h5 - l5).diff().diff().diff()

def f40_atxd_495_close_position_in_63d_range_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close-position in 63d range."""
    h = high.rolling(QDAYS, min_periods=MDAYS).max()
    l = low.rolling(QDAYS, min_periods=MDAYS).min()
    return _safe_div(close - l, h - l).diff().diff().diff()

def f40_atxd_496_close_position_in_252d_range_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close-position in 252d range."""
    h = high.rolling(YDAYS, min_periods=QDAYS).max()
    l = low.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(close - l, h - l).diff().diff().diff()

def f40_atxd_497_nbar_range_to_sum_tr_ratio_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-bar true range / Σ TR(63d) — overlap ratio at quarterly horizon."""
    nbar = high.rolling(QDAYS, min_periods=MDAYS).max() - low.rolling(QDAYS, min_periods=MDAYS).min()
    sum_tr = _true_range(high, low, close).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(nbar, sum_tr).diff().diff().diff()

def f40_atxd_498_nbar_range_to_sum_tr_ratio_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-bar true range / Σ TR(252d)."""
    nbar = high.rolling(YDAYS, min_periods=QDAYS).max() - low.rolling(YDAYS, min_periods=QDAYS).min()
    sum_tr = _true_range(high, low, close).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(nbar, sum_tr).diff().diff().diff()

def f40_atxd_499_5d_range_pct_of_close_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-bar true range / close — 5d range as fraction of price."""
    nbar = high.rolling(WDAYS, min_periods=2).max() - low.rolling(WDAYS, min_periods=2).min()
    return _safe_div(nbar, close).diff().diff().diff()

def f40_atxd_500_63d_range_pct_of_close_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-bar true range / close."""
    nbar = high.rolling(QDAYS, min_periods=MDAYS).max() - low.rolling(QDAYS, min_periods=MDAYS).min()
    return _safe_div(nbar, close).diff().diff().diff()

def f40_atxd_501_atr_at_252d_low_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean ATR(21) on bars where close at 252d-low, over 252d."""
    a = _atr(high, low, close, MDAYS)
    at_low = close <= close.rolling(YDAYS, min_periods=QDAYS).min()
    return a.where(at_low, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_502_atr_at_252d_pullback_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean ATR(21) on bars in 5-10% pullback from 252d-high, over 252d."""
    a = _atr(high, low, close, MDAYS)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    in_pullback = (close >= 0.9 * rmax) & (close < 0.95 * rmax)
    return a.where(in_pullback, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_503_atr_at_breakdown_count_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean ATR(21) on bars where close < 21d-low (breakdown) over 252d."""
    a = _atr(high, low, close, MDAYS)
    breakdown = close < close.rolling(MDAYS, min_periods=WDAYS).min()
    return a.where(breakdown, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_504_atr_at_breakout_count_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean ATR(21) on bars where close > 21d-high (breakout) over 252d."""
    a = _atr(high, low, close, MDAYS)
    breakout = close > close.rolling(MDAYS, min_periods=WDAYS).max()
    return a.where(breakout, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_505_atr_pre_252d_high_5d_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean ATR(21) in 5 bars before 252d-high events, over 252d."""
    a = _atr(high, low, close, MDAYS)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    new_high = close >= rmax
    pre = a.rolling(WDAYS, min_periods=2).mean().shift(1)
    return pre.where(new_high, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_506_atr_post_252d_low_5d_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean ATR(21) in 5 bars after 252d-low events over 252d (causal lag)."""
    a = _atr(high, low, close, MDAYS)
    new_low_lag = close.shift(WDAYS) <= close.shift(WDAYS).rolling(YDAYS, min_periods=QDAYS).min()
    return a.where(new_low_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_507_range_at_252d_low_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean (high - low) on bars where close at 252d-low, over 252d."""
    new_low = close <= close.rolling(YDAYS, min_periods=QDAYS).min()
    return (high - low).where(new_low, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_508_range_at_252d_high_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean (high - low) on bars where close at 252d-high, over 252d."""
    new_high = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    return (high - low).where(new_high, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_509_atr_in_consolidation_zones_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean ATR(21) in bars where 21d-range < 5% of mean close, over 252d (consolidation ATR)."""
    a = _atr(high, low, close, MDAYS)
    range21 = close.rolling(MDAYS, min_periods=WDAYS).max() - close.rolling(MDAYS, min_periods=WDAYS).min()
    mean21 = close.rolling(MDAYS, min_periods=WDAYS).mean()
    cons = _safe_div(range21, mean21) < 0.05
    return a.where(cons, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_510_atr_in_trending_zones_252d_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean ATR(21) in bars where |21d return| > 10% (trending) over 252d."""
    a = _atr(high, low, close, MDAYS)
    r21 = _safe_log(close) - _safe_log(close.shift(MDAYS))
    trending = r21.abs() > 0.1
    return a.where(trending, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_511_tr_vs_5d_avg_252d_pctrank_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pct-rank of (TR / 5d-avg-TR) within 252d distribution."""
    tr = _true_range(high, low, close)
    ratio = _safe_div(tr, tr.rolling(WDAYS, min_periods=2).mean())
    return ratio.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True).diff().diff().diff()

def f40_atxd_512_tr_vs_21d_avg_252d_pctrank_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pct-rank of (TR / 21d-avg-TR) within 252d."""
    tr = _true_range(high, low, close)
    ratio = _safe_div(tr, tr.rolling(MDAYS, min_periods=WDAYS).mean())
    return ratio.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True).diff().diff().diff()

def f40_atxd_513_tr_above_5d_max_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where TR > 5d-max-TR (excluding today via shift), over 252d."""
    tr = _true_range(high, low, close)
    prior_5d_max = tr.shift(1).rolling(WDAYS, min_periods=2).max()
    return (tr > prior_5d_max).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_514_tr_below_5d_min_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where TR < 5d-min-TR over 252d."""
    tr = _true_range(high, low, close)
    prior_5d_min = tr.shift(1).rolling(WDAYS, min_periods=2).min()
    return (tr < prior_5d_min).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f40_atxd_515_atr_above_21d_avg_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars where ATR(21) > 21d-avg of ATR(21), over 252d."""
    a = _atr(high, low, close, MDAYS)
    return (a > a.rolling(MDAYS, min_periods=WDAYS).mean()).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_516_tr_growth_rate_5d_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (TR_t / TR_t-5 − 1) over 252d (5d TR growth rate)."""
    tr = _true_range(high, low, close)
    return _safe_div(tr - tr.shift(WDAYS), tr.shift(WDAYS)).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_517_atr_acceleration_rate_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean Δ²ATR(21) over 252d (ATR-acceleration average)."""
    a = _atr(high, low, close, MDAYS)
    return a.diff().diff().rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_518_atr_jerk_rate_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean Δ³ATR(21) over 252d (ATR jerk)."""
    a = _atr(high, low, close, MDAYS)
    return a.diff().diff().diff().rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_519_atr_5d_consistency_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 − std(ATR(21))/mean(ATR(21)) over 5d, mean over 252d (short-horizon consistency)."""
    a = _atr(high, low, close, MDAYS)
    cv5 = _safe_div(a.rolling(WDAYS, min_periods=2).std(), a.rolling(WDAYS, min_periods=2).mean())
    return (1.0 - cv5).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_520_atr_21d_consistency_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 − std(ATR(21))/mean(ATR(21)) over 21d, mean over 252d."""
    a = _atr(high, low, close, MDAYS)
    cv21 = _safe_div(a.rolling(MDAYS, min_periods=WDAYS).std(), a.rolling(MDAYS, min_periods=WDAYS).mean())
    return (1.0 - cv21).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f40_atxd_521_tr_pct_rank_window_5d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pct-rank of current TR within trailing 5d."""
    tr = _true_range(high, low, close)
    return tr.rolling(WDAYS, min_periods=2).apply(lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True).diff().diff().diff()

def f40_atxd_522_tr_pct_rank_window_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pct-rank of current TR within trailing 21d."""
    tr = _true_range(high, low, close)
    return tr.rolling(MDAYS, min_periods=WDAYS).apply(lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True).diff().diff().diff()

def f40_atxd_523_atr_log_volatility_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std of log(ATR(21)) over 252d — log-scale ATR volatility."""
    return _safe_log(_atr(high, low, close, MDAYS)).rolling(YDAYS, min_periods=QDAYS).std().diff().diff().diff()

def f40_atxd_524_atr_volatility_of_volatility_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """std(std(ATR,21d), 63d) over 252d — vol-of-vol-of-ATR."""
    a = _atr(high, low, close, MDAYS)
    vov = a.rolling(MDAYS, min_periods=WDAYS).std()
    return vov.rolling(QDAYS, min_periods=MDAYS).std().diff().diff().diff()

def f40_atxd_525_atr_jump_z_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where |ΔATR(21)| z-score > 2 over 252d (ATR-jumps)."""
    a = _atr(high, low, close, MDAYS)
    da = a.diff()
    z = _rolling_zscore(da, YDAYS)
    return (z.abs() > 2).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()
ATR_EXPANSION_DYNAMICS_D3_REGISTRY_451_525 = {'f40_atxd_451_resistance_test_count_63d_252d_d3': {'inputs': ['high'], 'func': f40_atxd_451_resistance_test_count_63d_252d_d3}, 'f40_atxd_452_support_test_count_63d_252d_d3': {'inputs': ['low'], 'func': f40_atxd_452_support_test_count_63d_252d_d3}, 'f40_atxd_453_resistance_break_count_252d_d3': {'inputs': ['high', 'close'], 'func': f40_atxd_453_resistance_break_count_252d_d3}, 'f40_atxd_454_support_break_count_252d_d3': {'inputs': ['low', 'close'], 'func': f40_atxd_454_support_break_count_252d_d3}, 'f40_atxd_455_atr_at_resistance_test_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_455_atr_at_resistance_test_252d_d3}, 'f40_atxd_456_atr_at_support_test_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_456_atr_at_support_test_252d_d3}, 'f40_atxd_457_bars_since_resistance_test_d3': {'inputs': ['high'], 'func': f40_atxd_457_bars_since_resistance_test_d3}, 'f40_atxd_458_bars_since_support_test_d3': {'inputs': ['low'], 'func': f40_atxd_458_bars_since_support_test_d3}, 'f40_atxd_459_failed_resistance_break_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_459_failed_resistance_break_count_252d_d3}, 'f40_atxd_460_failed_support_break_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_460_failed_support_break_count_252d_d3}, 'f40_atxd_461_atr_trend_5d_slope_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_461_atr_trend_5d_slope_252d_d3}, 'f40_atxd_462_atr_trend_21d_slope_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_462_atr_trend_21d_slope_252d_d3}, 'f40_atxd_463_atr_trend_sign_consistency_63d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_463_atr_trend_sign_consistency_63d_d3}, 'f40_atxd_464_atr_trend_strength_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_464_atr_trend_strength_252d_d3}, 'f40_atxd_465_atr_trend_reversals_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_465_atr_trend_reversals_252d_d3}, 'f40_atxd_466_atr_max_runup_63d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_466_atr_max_runup_63d_d3}, 'f40_atxd_467_atr_max_rundown_63d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_467_atr_max_rundown_63d_d3}, 'f40_atxd_468_atr_trend_zscore_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_468_atr_trend_zscore_252d_d3}, 'f40_atxd_469_atr_trend_persistence_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_469_atr_trend_persistence_252d_d3}, 'f40_atxd_470_atr_directional_score_63d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_470_atr_directional_score_63d_d3}, 'f40_atxd_471_atr_after_nr4_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_471_atr_after_nr4_252d_d3}, 'f40_atxd_472_atr_after_wr7_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_472_atr_after_wr7_252d_d3}, 'f40_atxd_473_atr_after_inside_bar_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_473_atr_after_inside_bar_252d_d3}, 'f40_atxd_474_atr_after_outside_bar_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_474_atr_after_outside_bar_252d_d3}, 'f40_atxd_475_atr_after_doji_252d_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f40_atxd_475_atr_after_doji_252d_d3}, 'f40_atxd_476_atr_after_gap_up_252d_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f40_atxd_476_atr_after_gap_up_252d_d3}, 'f40_atxd_477_atr_after_gap_down_252d_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f40_atxd_477_atr_after_gap_down_252d_d3}, 'f40_atxd_478_atr_after_engulfing_252d_d3': {'inputs': ['open', 'high', 'low', 'close'], 'func': f40_atxd_478_atr_after_engulfing_252d_d3}, 'f40_atxd_479_atr_change_after_big_close_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_479_atr_change_after_big_close_252d_d3}, 'f40_atxd_480_atr_after_5d_streak_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_480_atr_after_5d_streak_252d_d3}, 'f40_atxd_481_tr_skew_63d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_481_tr_skew_63d_d3}, 'f40_atxd_482_tr_kurt_63d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_482_tr_kurt_63d_d3}, 'f40_atxd_483_tr_skew_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_483_tr_skew_252d_d3}, 'f40_atxd_484_log_tr_skew_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_484_log_tr_skew_252d_d3}, 'f40_atxd_485_log_tr_kurt_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_485_log_tr_kurt_252d_d3}, 'f40_atxd_486_tr_p99_over_p50_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_486_tr_p99_over_p50_252d_d3}, 'f40_atxd_487_tr_p99_over_p90_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_487_tr_p99_over_p90_252d_d3}, 'f40_atxd_488_tr_p90_p10_range_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_488_tr_p90_p10_range_252d_d3}, 'f40_atxd_489_tr_bimodality_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_489_tr_bimodality_252d_d3}, 'f40_atxd_490_tr_entropy_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_490_tr_entropy_252d_d3}, 'f40_atxd_491_nbar_true_range_5d_d3': {'inputs': ['high', 'low'], 'func': f40_atxd_491_nbar_true_range_5d_d3}, 'f40_atxd_492_nbar_true_range_63d_d3': {'inputs': ['high', 'low'], 'func': f40_atxd_492_nbar_true_range_63d_d3}, 'f40_atxd_493_nbar_true_range_252d_d3': {'inputs': ['high', 'low'], 'func': f40_atxd_493_nbar_true_range_252d_d3}, 'f40_atxd_494_close_position_in_5d_range_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_494_close_position_in_5d_range_d3}, 'f40_atxd_495_close_position_in_63d_range_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_495_close_position_in_63d_range_d3}, 'f40_atxd_496_close_position_in_252d_range_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_496_close_position_in_252d_range_d3}, 'f40_atxd_497_nbar_range_to_sum_tr_ratio_63d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_497_nbar_range_to_sum_tr_ratio_63d_d3}, 'f40_atxd_498_nbar_range_to_sum_tr_ratio_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_498_nbar_range_to_sum_tr_ratio_252d_d3}, 'f40_atxd_499_5d_range_pct_of_close_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_499_5d_range_pct_of_close_d3}, 'f40_atxd_500_63d_range_pct_of_close_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_500_63d_range_pct_of_close_d3}, 'f40_atxd_501_atr_at_252d_low_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f40_atxd_501_atr_at_252d_low_252d_d3}, 'f40_atxd_502_atr_at_252d_pullback_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f40_atxd_502_atr_at_252d_pullback_252d_d3}, 'f40_atxd_503_atr_at_breakdown_count_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f40_atxd_503_atr_at_breakdown_count_252d_d3}, 'f40_atxd_504_atr_at_breakout_count_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f40_atxd_504_atr_at_breakout_count_252d_d3}, 'f40_atxd_505_atr_pre_252d_high_5d_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f40_atxd_505_atr_pre_252d_high_5d_252d_d3}, 'f40_atxd_506_atr_post_252d_low_5d_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f40_atxd_506_atr_post_252d_low_5d_252d_d3}, 'f40_atxd_507_range_at_252d_low_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f40_atxd_507_range_at_252d_low_252d_d3}, 'f40_atxd_508_range_at_252d_high_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f40_atxd_508_range_at_252d_high_252d_d3}, 'f40_atxd_509_atr_in_consolidation_zones_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f40_atxd_509_atr_in_consolidation_zones_252d_d3}, 'f40_atxd_510_atr_in_trending_zones_252d_d3': {'inputs': ['close', 'high', 'low'], 'func': f40_atxd_510_atr_in_trending_zones_252d_d3}, 'f40_atxd_511_tr_vs_5d_avg_252d_pctrank_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_511_tr_vs_5d_avg_252d_pctrank_d3}, 'f40_atxd_512_tr_vs_21d_avg_252d_pctrank_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_512_tr_vs_21d_avg_252d_pctrank_d3}, 'f40_atxd_513_tr_above_5d_max_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_513_tr_above_5d_max_count_252d_d3}, 'f40_atxd_514_tr_below_5d_min_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_514_tr_below_5d_min_count_252d_d3}, 'f40_atxd_515_atr_above_21d_avg_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_515_atr_above_21d_avg_count_252d_d3}, 'f40_atxd_516_tr_growth_rate_5d_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_516_tr_growth_rate_5d_252d_d3}, 'f40_atxd_517_atr_acceleration_rate_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_517_atr_acceleration_rate_252d_d3}, 'f40_atxd_518_atr_jerk_rate_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_518_atr_jerk_rate_252d_d3}, 'f40_atxd_519_atr_5d_consistency_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_519_atr_5d_consistency_252d_d3}, 'f40_atxd_520_atr_21d_consistency_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_520_atr_21d_consistency_252d_d3}, 'f40_atxd_521_tr_pct_rank_window_5d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_521_tr_pct_rank_window_5d_d3}, 'f40_atxd_522_tr_pct_rank_window_21d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_522_tr_pct_rank_window_21d_d3}, 'f40_atxd_523_atr_log_volatility_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_523_atr_log_volatility_252d_d3}, 'f40_atxd_524_atr_volatility_of_volatility_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_524_atr_volatility_of_volatility_252d_d3}, 'f40_atxd_525_atr_jump_z_count_252d_d3': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_525_atr_jump_z_count_252d_d3}}