"""21_dollar_volume_intensity d2 features 451-525 — order-2 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
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

def _consecutive_true_streak(b):
    grp = (~b.fillna(False)).cumsum()
    return b.fillna(False).astype(int).groupby(grp).cumsum()

def _dollar_vol(close, volume):
    return (close * volume).astype(float)

def f21_dvit_451_dv_vs_1d_ago_ratio_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's $-vol / 1-day-ago $-vol."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, dv.shift(1)).diff().diff()

def f21_dvit_452_dv_vs_2d_ago_ratio_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's $-vol / 2-day-ago."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, dv.shift(2)).diff().diff()

def f21_dvit_453_dv_vs_3d_ago_ratio_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's $-vol / 3-day-ago."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, dv.shift(3)).diff().diff()

def f21_dvit_454_dv_vs_5d_ago_ratio_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's $-vol / 5-day-ago."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, dv.shift(5)).diff().diff()

def f21_dvit_455_dv_vs_8d_ago_ratio_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's $-vol / 8-day-ago."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, dv.shift(8)).diff().diff()

def f21_dvit_456_dv_vs_13d_ago_ratio_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's $-vol / 13-day-ago."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, dv.shift(13)).diff().diff()

def f21_dvit_457_dv_vs_3d_mean_ratio_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's $-vol / trailing 3d mean $-vol."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, dv.rolling(3, min_periods=2).mean()).diff().diff()

def f21_dvit_458_dv_vs_8d_mean_ratio_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's $-vol / 8d mean."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, dv.rolling(8, min_periods=3).mean()).diff().diff()

def f21_dvit_459_dv_vs_13d_mean_ratio_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's $-vol / 13d mean."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, dv.rolling(13, min_periods=5).mean()).diff().diff()

def f21_dvit_460_dv_vs_34d_mean_ratio_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's $-vol / 34d mean."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, dv.rolling(34, min_periods=10).mean()).diff().diff()

def f21_dvit_461_dv_vs_55d_mean_ratio_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's $-vol / 55d mean."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, dv.rolling(55, min_periods=15).mean()).diff().diff()

def f21_dvit_462_dv_vs_3d_median_ratio_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's $-vol / 3d median."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, dv.rolling(3, min_periods=2).median()).diff().diff()

def f21_dvit_463_dv_vs_8d_median_ratio_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's $-vol / 8d median."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, dv.rolling(8, min_periods=3).median()).diff().diff()

def f21_dvit_464_dv_vs_13d_median_ratio_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's $-vol / 13d median."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, dv.rolling(13, min_periods=5).median()).diff().diff()

def f21_dvit_465_dv_vs_34d_median_ratio_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's $-vol / 34d median."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, dv.rolling(34, min_periods=10).median()).diff().diff()

def f21_dvit_466_dv_red_bars_avg_21d_d2(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on red bars (close < open) over 21d."""
    dv = _dollar_vol(close, volume)
    return dv.where(close < open, np.nan).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f21_dvit_467_dv_green_bars_avg_21d_d2(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on green bars (close > open) over 21d."""
    dv = _dollar_vol(close, volume)
    return dv.where(close > open, np.nan).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f21_dvit_468_dv_red_to_green_ratio_21d_d2(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(sum red-bar $-vol 21d) / (sum green-bar $-vol 21d)."""
    dv = _dollar_vol(close, volume)
    red = dv.where(close < open, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    grn = dv.where(close > open, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(red, grn + 1.0).diff().diff()

def f21_dvit_469_dv_red_to_green_ratio_63d_d2(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(sum red-bar $-vol 63d) / (sum green-bar $-vol 63d)."""
    dv = _dollar_vol(close, volume)
    red = dv.where(close < open, 0.0).rolling(QDAYS, min_periods=MDAYS).sum()
    grn = dv.where(close > open, 0.0).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(red, grn + 1.0).diff().diff()

def f21_dvit_470_dv_on_close_upper_third_red_252d_d2(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on close-in-upper-third red bars over 252d."""
    pos = _safe_div(close - low, high - low)
    cond = (pos >= 0.67) & (close < open)
    dv = _dollar_vol(close, volume)
    return dv.where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f21_dvit_471_dv_on_close_lower_third_green_252d_d2(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on close-in-lower-third green bars over 252d."""
    pos = _safe_div(close - low, high - low)
    cond = (pos <= 0.33) & (close > open)
    dv = _dollar_vol(close, volume)
    return dv.where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f21_dvit_472_dv_on_big_body_up_252d_d2(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on big-body-up bars (body > 70% of range AND close>open) over 252d."""
    rng = (high - low).replace(0, np.nan)
    body_pct = (close - open).abs() / rng
    cond = (body_pct > 0.7) & (close > open)
    dv = _dollar_vol(close, volume)
    return dv.where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f21_dvit_473_dv_on_big_body_down_252d_d2(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on big-body-down bars over 252d."""
    rng = (high - low).replace(0, np.nan)
    body_pct = (close - open).abs() / rng
    cond = (body_pct > 0.7) & (close < open)
    dv = _dollar_vol(close, volume)
    return dv.where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f21_dvit_474_dv_on_small_body_bars_252d_d2(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on small-body bars (|body|<10% of range) over 252d."""
    rng = (high - low).replace(0, np.nan)
    body_pct = (close - open).abs() / rng
    dv = _dollar_vol(close, volume)
    return dv.where(body_pct < 0.1, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f21_dvit_475_dv_on_long_upper_wick_bars_252d_d2(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on long-upper-wick bars (upper wick > 50% of range) over 252d."""
    rng = (high - low).replace(0, np.nan)
    upper_wick = (high - pd.concat([close, open], axis=1).max(axis=1)) / rng
    dv = _dollar_vol(close, volume)
    return dv.where(upper_wick > 0.5, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f21_dvit_476_log_dv_bb_percent_b_20d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """%B for log-$-vol BB(20, 2)."""
    ldv = _safe_log(_dollar_vol(close, volume))
    m = ldv.rolling(20, min_periods=10).mean()
    s = ldv.rolling(20, min_periods=10).std()
    return _safe_div(ldv - (m - 2.0 * s), 4.0 * s).diff().diff()

def f21_dvit_477_log_dv_bb_bandwidth_20d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """BB bandwidth on log-$-vol(20, 2)."""
    ldv = _safe_log(_dollar_vol(close, volume))
    m = ldv.rolling(20, min_periods=10).mean()
    s = ldv.rolling(20, min_periods=10).std()
    return _safe_div(4.0 * s, m.abs() + 1.0).diff().diff()

def f21_dvit_478_log_dv_above_upper_bb_count_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where log-$-vol > 20d BB upper band."""
    ldv = _safe_log(_dollar_vol(close, volume))
    m = ldv.rolling(20, min_periods=10).mean()
    s = ldv.rolling(20, min_periods=10).std()
    return (ldv > m + 2.0 * s).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f21_dvit_479_log_dv_below_lower_bb_count_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where log-$-vol < 20d BB lower band."""
    ldv = _safe_log(_dollar_vol(close, volume))
    m = ldv.rolling(20, min_periods=10).mean()
    s = ldv.rolling(20, min_periods=10).std()
    return (ldv < m - 2.0 * s).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f21_dvit_480_log_dv_bb_squeeze_indicator_20d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when log-$-vol BB bandwidth in bottom decile of trailing 252d."""
    ldv = _safe_log(_dollar_vol(close, volume))
    m = ldv.rolling(20, min_periods=10).mean()
    s = ldv.rolling(20, min_periods=10).std()
    bw = _safe_div(4.0 * s, m.abs() + 1.0)
    q10 = bw.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
    return (bw <= q10).astype(float).diff().diff()

def f21_dvit_481_log_dv_keltner_position_20d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """log-$-vol position within Keltner-style channel (20EMA log-dv ± 2*ATR21)."""
    ldv = _safe_log(_dollar_vol(close, volume))
    ema = ldv.ewm(span=20, min_periods=10, adjust=False).mean()
    atr = _atr(high, low, close, n=MDAYS)
    upper = ema + 2.0 * atr
    lower = ema - 2.0 * atr
    return _safe_div(ldv - lower, upper - lower).diff().diff()

def f21_dvit_482_dv_envelope_break_count_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where $-vol > 2× 21d-EMA $-vol."""
    dv = _dollar_vol(close, volume)
    ema21 = dv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    return (dv > 2.0 * ema21).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f21_dvit_483_dv_envelope_squeeze_pct_rank_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pct rank(252d) of distance from $-vol to 21d EMA."""
    dv = _dollar_vol(close, volume)
    ema21 = dv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    dist = (dv - ema21).abs()
    return dist.rolling(YDAYS, min_periods=QDAYS).rank(pct=True).diff().diff()

def f21_dvit_484_log_dv_donchian_channel_position_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log-$-vol Donchian position over 21d: (lv - min) / (max - min)."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return _safe_div(ldv - ldv.rolling(MDAYS, min_periods=WDAYS).min(), ldv.rolling(MDAYS, min_periods=WDAYS).max() - ldv.rolling(MDAYS, min_periods=WDAYS).min()).diff().diff()

def f21_dvit_485_log_dv_donchian_channel_position_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log-$-vol Donchian position over 63d."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return _safe_div(ldv - ldv.rolling(QDAYS, min_periods=MDAYS).min(), ldv.rolling(QDAYS, min_periods=MDAYS).max() - ldv.rolling(QDAYS, min_periods=MDAYS).min()).diff().diff()

def f21_dvit_486_log_dv_pct_rank_3d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log-$-vol pct rank within trailing 3-day window."""
    return _safe_log(_dollar_vol(close, volume)).rolling(3, min_periods=2).rank(pct=True).diff().diff()

def f21_dvit_487_log_dv_pct_rank_5d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log-$-vol pct rank within trailing 5-day window."""
    return _safe_log(_dollar_vol(close, volume)).rolling(WDAYS, min_periods=2).rank(pct=True).diff().diff()

def f21_dvit_488_log_dv_pct_rank_8d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log-$-vol pct rank within 8-day window."""
    return _safe_log(_dollar_vol(close, volume)).rolling(8, min_periods=3).rank(pct=True).diff().diff()

def f21_dvit_489_log_dv_pct_rank_13d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log-$-vol pct rank within 13-day window."""
    return _safe_log(_dollar_vol(close, volume)).rolling(13, min_periods=5).rank(pct=True).diff().diff()

def f21_dvit_490_log_dv_pct_rank_34d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log-$-vol pct rank within 34-day window."""
    return _safe_log(_dollar_vol(close, volume)).rolling(34, min_periods=10).rank(pct=True).diff().diff()

def f21_dvit_491_log_dv_pct_rank_55d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log-$-vol pct rank within 55-day window."""
    return _safe_log(_dollar_vol(close, volume)).rolling(55, min_periods=15).rank(pct=True).diff().diff()

def f21_dvit_492_log_dv_pct_rank_126d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log-$-vol pct rank within 126-day window."""
    return _safe_log(_dollar_vol(close, volume)).rolling(126, min_periods=30).rank(pct=True).diff().diff()

def f21_dvit_493_log_dv_pct_rank_diff_5_vs_55_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """pct rank(log-$-vol, 5d) − pct rank(log-$-vol, 55d)."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return (ldv.rolling(WDAYS, min_periods=2).rank(pct=True) - ldv.rolling(55, min_periods=15).rank(pct=True)).diff().diff()

def f21_dvit_494_log_dv_pct_rank_diff_13_vs_126_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """pct rank(log-$-vol, 13d) − pct rank(log-$-vol, 126d)."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return (ldv.rolling(13, min_periods=5).rank(pct=True) - ldv.rolling(126, min_periods=30).rank(pct=True)).diff().diff()

def f21_dvit_495_log_dv_pct_rank_diff_34_vs_252_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """pct rank(log-$-vol, 34d) − pct rank(log-$-vol, 252d)."""
    ldv = _safe_log(_dollar_vol(close, volume))
    return (ldv.rolling(34, min_periods=10).rank(pct=True) - ldv.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)).diff().diff()

def f21_dvit_496_dv_at_top_quartile_21d_range_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on bars where close in top quartile of 21d range, 252d."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    rmin21 = low.rolling(MDAYS, min_periods=WDAYS).min()
    pos = _safe_div(close - rmin21, rmax21 - rmin21)
    dv = _dollar_vol(close, volume)
    return dv.where(pos >= 0.75, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f21_dvit_497_dv_at_top_quartile_63d_range_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on bars where close in top quartile of 63d range, 252d."""
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    rmin = low.rolling(QDAYS, min_periods=MDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    dv = _dollar_vol(close, volume)
    return dv.where(pos >= 0.75, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f21_dvit_498_dv_at_top_quartile_252d_range_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on bars where close in top quartile of 252d range, 252d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    dv = _dollar_vol(close, volume)
    return dv.where(pos >= 0.75, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f21_dvit_499_dv_at_top_quartile_5y_range_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on bars where close in top quartile of 5y range, 252d."""
    rmax = high.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    rmin = low.rolling(DDAYS_5Y, min_periods=YDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    dv = _dollar_vol(close, volume)
    return dv.where(pos >= 0.75, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f21_dvit_500_dv_first_new_21d_high_after_drawdown_avg_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on first-new-21d-high-after-5-down-days bars."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    below = high < rmax21.shift(1)
    streak_below_yest = _consecutive_true_streak(below.shift(1).fillna(False)).astype(float)
    cond = (high >= rmax21) & (streak_below_yest >= WDAYS)
    dv = _dollar_vol(close, volume)
    return dv.where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f21_dvit_501_dv_first_new_252d_high_after_drawdown_avg_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on first-new-252d-high-after-63-down-days bars."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    below = high < rmax.shift(1)
    streak_below_yest = _consecutive_true_streak(below.shift(1).fillna(False)).astype(float)
    cond = (high >= rmax) & (streak_below_yest >= QDAYS)
    dv = _dollar_vol(close, volume)
    return dv.where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f21_dvit_502_dv_within_2pct_of_21d_high_avg_63d_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on bars within 2% of 21d trailing high, over 63d."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    dv = _dollar_vol(close, volume)
    return dv.where(high >= 0.98 * rmax21, np.nan).rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()

def f21_dvit_503_dv_within_2pct_of_63d_high_avg_252d_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on bars within 2% of 63d trailing high, over 252d."""
    rmax63 = high.rolling(QDAYS, min_periods=MDAYS).max()
    dv = _dollar_vol(close, volume)
    return dv.where(high >= 0.98 * rmax63, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f21_dvit_504_dv_within_2pct_of_252d_high_avg_252d_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on bars within 2% of 252d trailing high, over 252d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    dv = _dollar_vol(close, volume)
    return dv.where(high >= 0.98 * rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f21_dvit_505_dv_within_2pct_of_5y_high_avg_252d_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on bars within 2% of 5y trailing high, over 252d."""
    rmax = high.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    dv = _dollar_vol(close, volume)
    return dv.where(high >= 0.98 * rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f21_dvit_506_dv_on_3_consec_new_highs_avg_252d_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on 3-consec-21d-new-high bars, 252d."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    nh = high >= rmax21
    three_nh = nh & nh.shift(1) & nh.shift(2)
    dv = _dollar_vol(close, volume)
    return dv.where(three_nh, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f21_dvit_507_dv_on_5_consec_new_highs_avg_252d_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on 5-consec-21d-new-high bars, 252d."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    nh = high >= rmax21
    five_nh = nh & nh.shift(1) & nh.shift(2) & nh.shift(3) & nh.shift(4)
    dv = _dollar_vol(close, volume)
    return dv.where(five_nh, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f21_dvit_508_dv_on_bars_at_expanding_close_max_avg_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on bars where close = expanding-5y max."""
    rmax = close.expanding(min_periods=YDAYS).max()
    dv = _dollar_vol(close, volume)
    return dv.where(close >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f21_dvit_509_dv_zscore_at_expanding_close_max_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log-$-vol z(252d) on bars where close = expanding-5y max."""
    rmax = close.expanding(min_periods=YDAYS).max()
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return z.where(close >= rmax, np.nan).diff().diff()

def f21_dvit_510_dv_at_top_decile_5y_range_252d_mean_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean log-$-vol z(252d) on bars where close in top decile of 5y range, over 252d."""
    rmax = high.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    rmin = low.rolling(DDAYS_5Y, min_periods=YDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    z = _rolling_zscore(_safe_log(_dollar_vol(close, volume)), YDAYS)
    return z.where(pos >= 0.9, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f21_dvit_511_dv_per_body_size_ratio_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """$-vol / |close - close.shift(1)|."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, close.diff().abs()).diff().diff()

def f21_dvit_512_dv_per_body_size_zscore_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of $-vol / |close.diff|."""
    dv = _dollar_vol(close, volume)
    return _rolling_zscore(_safe_div(dv, close.diff().abs()), YDAYS).diff().diff()

def f21_dvit_513_dv_per_true_range_ratio_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """$-vol / true_range."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, _true_range(high, low, close)).diff().diff()

def f21_dvit_514_dv_per_true_range_zscore_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of $-vol / TR."""
    dv = _dollar_vol(close, volume)
    return _rolling_zscore(_safe_div(dv, _true_range(high, low, close)), YDAYS).diff().diff()

def f21_dvit_515_dv_per_atr_ratio_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """$-vol / ATR21."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv, _atr(high, low, close, n=MDAYS)).diff().diff()

def f21_dvit_516_dv_per_atr_zscore_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of $-vol / ATR21."""
    dv = _dollar_vol(close, volume)
    return _rolling_zscore(_safe_div(dv, _atr(high, low, close, n=MDAYS)), YDAYS).diff().diff()

def f21_dvit_517_dv_per_abs_price_change_5d_sum_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum $-vol 5d / sum |close.diff| 5d."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv.rolling(WDAYS, min_periods=2).sum(), close.diff().abs().rolling(WDAYS, min_periods=2).sum()).diff().diff()

def f21_dvit_518_dv_per_abs_price_change_21d_sum_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum $-vol 21d / sum |close.diff| 21d."""
    dv = _dollar_vol(close, volume)
    return _safe_div(dv.rolling(MDAYS, min_periods=WDAYS).sum(), close.diff().abs().rolling(MDAYS, min_periods=WDAYS).sum()).diff().diff()

def f21_dvit_519_dv_per_hl_spread_ratio_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """$-vol / (high - low)."""
    return _safe_div(_dollar_vol(close, volume), high - low).diff().diff()

def f21_dvit_520_dv_per_hl_spread_zscore_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of $-vol / (high-low)."""
    return _rolling_zscore(_safe_div(_dollar_vol(close, volume), high - low), YDAYS).diff().diff()

def f21_dvit_521_roll_effective_spread_proxy_21d_d2(close: pd.Series) -> pd.Series:
    """Roll(1984) effective-spread proxy over 21d."""
    r = close.diff()
    rcov = r.rolling(MDAYS, min_periods=WDAYS).cov(r.shift(1))
    return (2.0 * np.sqrt((-rcov).clip(lower=0.0))).diff().diff()

def f21_dvit_522_roll_effective_spread_proxy_63d_d2(close: pd.Series) -> pd.Series:
    """Roll(1984) effective-spread proxy over 63d."""
    r = close.diff()
    rcov = r.rolling(QDAYS, min_periods=MDAYS).cov(r.shift(1))
    return (2.0 * np.sqrt((-rcov).clip(lower=0.0))).diff().diff()

def f21_dvit_523_dv_per_roll_spread_proxy_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """$-vol / Roll spread proxy(21d)."""
    r = close.diff()
    rcov = r.rolling(MDAYS, min_periods=WDAYS).cov(r.shift(1))
    spread = 2.0 * np.sqrt((-rcov).clip(lower=0.0))
    return _safe_div(_dollar_vol(close, volume), spread + 1e-09).diff().diff()

def f21_dvit_524_hl_spread_expansion_rate_21d_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """5d-mean (high-low) / 21d-mean (high-low)."""
    sp = high - low
    return _safe_div(sp.rolling(WDAYS, min_periods=2).mean(), sp.rolling(MDAYS, min_periods=WDAYS).mean()).diff().diff()

def f21_dvit_525_hl_spread_compression_indicator_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 when (high-low)/high < 0.5 × trailing-252d median of same."""
    sp = (high - low) / high.replace(0, np.nan)
    med = sp.rolling(YDAYS, min_periods=QDAYS).median()
    return (sp < 0.5 * med).astype(float).diff().diff()
DOLLAR_VOLUME_INTENSITY_D2_REGISTRY_451_525 = {'f21_dvit_451_dv_vs_1d_ago_ratio_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_451_dv_vs_1d_ago_ratio_d2}, 'f21_dvit_452_dv_vs_2d_ago_ratio_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_452_dv_vs_2d_ago_ratio_d2}, 'f21_dvit_453_dv_vs_3d_ago_ratio_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_453_dv_vs_3d_ago_ratio_d2}, 'f21_dvit_454_dv_vs_5d_ago_ratio_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_454_dv_vs_5d_ago_ratio_d2}, 'f21_dvit_455_dv_vs_8d_ago_ratio_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_455_dv_vs_8d_ago_ratio_d2}, 'f21_dvit_456_dv_vs_13d_ago_ratio_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_456_dv_vs_13d_ago_ratio_d2}, 'f21_dvit_457_dv_vs_3d_mean_ratio_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_457_dv_vs_3d_mean_ratio_d2}, 'f21_dvit_458_dv_vs_8d_mean_ratio_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_458_dv_vs_8d_mean_ratio_d2}, 'f21_dvit_459_dv_vs_13d_mean_ratio_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_459_dv_vs_13d_mean_ratio_d2}, 'f21_dvit_460_dv_vs_34d_mean_ratio_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_460_dv_vs_34d_mean_ratio_d2}, 'f21_dvit_461_dv_vs_55d_mean_ratio_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_461_dv_vs_55d_mean_ratio_d2}, 'f21_dvit_462_dv_vs_3d_median_ratio_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_462_dv_vs_3d_median_ratio_d2}, 'f21_dvit_463_dv_vs_8d_median_ratio_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_463_dv_vs_8d_median_ratio_d2}, 'f21_dvit_464_dv_vs_13d_median_ratio_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_464_dv_vs_13d_median_ratio_d2}, 'f21_dvit_465_dv_vs_34d_median_ratio_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_465_dv_vs_34d_median_ratio_d2}, 'f21_dvit_466_dv_red_bars_avg_21d_d2': {'inputs': ['open', 'close', 'volume'], 'func': f21_dvit_466_dv_red_bars_avg_21d_d2}, 'f21_dvit_467_dv_green_bars_avg_21d_d2': {'inputs': ['open', 'close', 'volume'], 'func': f21_dvit_467_dv_green_bars_avg_21d_d2}, 'f21_dvit_468_dv_red_to_green_ratio_21d_d2': {'inputs': ['open', 'close', 'volume'], 'func': f21_dvit_468_dv_red_to_green_ratio_21d_d2}, 'f21_dvit_469_dv_red_to_green_ratio_63d_d2': {'inputs': ['open', 'close', 'volume'], 'func': f21_dvit_469_dv_red_to_green_ratio_63d_d2}, 'f21_dvit_470_dv_on_close_upper_third_red_252d_d2': {'inputs': ['high', 'low', 'open', 'close', 'volume'], 'func': f21_dvit_470_dv_on_close_upper_third_red_252d_d2}, 'f21_dvit_471_dv_on_close_lower_third_green_252d_d2': {'inputs': ['high', 'low', 'open', 'close', 'volume'], 'func': f21_dvit_471_dv_on_close_lower_third_green_252d_d2}, 'f21_dvit_472_dv_on_big_body_up_252d_d2': {'inputs': ['high', 'low', 'open', 'close', 'volume'], 'func': f21_dvit_472_dv_on_big_body_up_252d_d2}, 'f21_dvit_473_dv_on_big_body_down_252d_d2': {'inputs': ['high', 'low', 'open', 'close', 'volume'], 'func': f21_dvit_473_dv_on_big_body_down_252d_d2}, 'f21_dvit_474_dv_on_small_body_bars_252d_d2': {'inputs': ['high', 'low', 'open', 'close', 'volume'], 'func': f21_dvit_474_dv_on_small_body_bars_252d_d2}, 'f21_dvit_475_dv_on_long_upper_wick_bars_252d_d2': {'inputs': ['high', 'low', 'open', 'close', 'volume'], 'func': f21_dvit_475_dv_on_long_upper_wick_bars_252d_d2}, 'f21_dvit_476_log_dv_bb_percent_b_20d_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_476_log_dv_bb_percent_b_20d_d2}, 'f21_dvit_477_log_dv_bb_bandwidth_20d_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_477_log_dv_bb_bandwidth_20d_d2}, 'f21_dvit_478_log_dv_above_upper_bb_count_252d_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_478_log_dv_above_upper_bb_count_252d_d2}, 'f21_dvit_479_log_dv_below_lower_bb_count_252d_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_479_log_dv_below_lower_bb_count_252d_d2}, 'f21_dvit_480_log_dv_bb_squeeze_indicator_20d_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_480_log_dv_bb_squeeze_indicator_20d_d2}, 'f21_dvit_481_log_dv_keltner_position_20d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f21_dvit_481_log_dv_keltner_position_20d_d2}, 'f21_dvit_482_dv_envelope_break_count_252d_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_482_dv_envelope_break_count_252d_d2}, 'f21_dvit_483_dv_envelope_squeeze_pct_rank_252d_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_483_dv_envelope_squeeze_pct_rank_252d_d2}, 'f21_dvit_484_log_dv_donchian_channel_position_21d_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_484_log_dv_donchian_channel_position_21d_d2}, 'f21_dvit_485_log_dv_donchian_channel_position_63d_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_485_log_dv_donchian_channel_position_63d_d2}, 'f21_dvit_486_log_dv_pct_rank_3d_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_486_log_dv_pct_rank_3d_d2}, 'f21_dvit_487_log_dv_pct_rank_5d_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_487_log_dv_pct_rank_5d_d2}, 'f21_dvit_488_log_dv_pct_rank_8d_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_488_log_dv_pct_rank_8d_d2}, 'f21_dvit_489_log_dv_pct_rank_13d_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_489_log_dv_pct_rank_13d_d2}, 'f21_dvit_490_log_dv_pct_rank_34d_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_490_log_dv_pct_rank_34d_d2}, 'f21_dvit_491_log_dv_pct_rank_55d_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_491_log_dv_pct_rank_55d_d2}, 'f21_dvit_492_log_dv_pct_rank_126d_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_492_log_dv_pct_rank_126d_d2}, 'f21_dvit_493_log_dv_pct_rank_diff_5_vs_55_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_493_log_dv_pct_rank_diff_5_vs_55_d2}, 'f21_dvit_494_log_dv_pct_rank_diff_13_vs_126_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_494_log_dv_pct_rank_diff_13_vs_126_d2}, 'f21_dvit_495_log_dv_pct_rank_diff_34_vs_252_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_495_log_dv_pct_rank_diff_34_vs_252_d2}, 'f21_dvit_496_dv_at_top_quartile_21d_range_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f21_dvit_496_dv_at_top_quartile_21d_range_252d_d2}, 'f21_dvit_497_dv_at_top_quartile_63d_range_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f21_dvit_497_dv_at_top_quartile_63d_range_252d_d2}, 'f21_dvit_498_dv_at_top_quartile_252d_range_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f21_dvit_498_dv_at_top_quartile_252d_range_252d_d2}, 'f21_dvit_499_dv_at_top_quartile_5y_range_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f21_dvit_499_dv_at_top_quartile_5y_range_252d_d2}, 'f21_dvit_500_dv_first_new_21d_high_after_drawdown_avg_d2': {'inputs': ['high', 'close', 'volume'], 'func': f21_dvit_500_dv_first_new_21d_high_after_drawdown_avg_d2}, 'f21_dvit_501_dv_first_new_252d_high_after_drawdown_avg_d2': {'inputs': ['high', 'close', 'volume'], 'func': f21_dvit_501_dv_first_new_252d_high_after_drawdown_avg_d2}, 'f21_dvit_502_dv_within_2pct_of_21d_high_avg_63d_d2': {'inputs': ['high', 'close', 'volume'], 'func': f21_dvit_502_dv_within_2pct_of_21d_high_avg_63d_d2}, 'f21_dvit_503_dv_within_2pct_of_63d_high_avg_252d_d2': {'inputs': ['high', 'close', 'volume'], 'func': f21_dvit_503_dv_within_2pct_of_63d_high_avg_252d_d2}, 'f21_dvit_504_dv_within_2pct_of_252d_high_avg_252d_d2': {'inputs': ['high', 'close', 'volume'], 'func': f21_dvit_504_dv_within_2pct_of_252d_high_avg_252d_d2}, 'f21_dvit_505_dv_within_2pct_of_5y_high_avg_252d_d2': {'inputs': ['high', 'close', 'volume'], 'func': f21_dvit_505_dv_within_2pct_of_5y_high_avg_252d_d2}, 'f21_dvit_506_dv_on_3_consec_new_highs_avg_252d_d2': {'inputs': ['high', 'close', 'volume'], 'func': f21_dvit_506_dv_on_3_consec_new_highs_avg_252d_d2}, 'f21_dvit_507_dv_on_5_consec_new_highs_avg_252d_d2': {'inputs': ['high', 'close', 'volume'], 'func': f21_dvit_507_dv_on_5_consec_new_highs_avg_252d_d2}, 'f21_dvit_508_dv_on_bars_at_expanding_close_max_avg_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_508_dv_on_bars_at_expanding_close_max_avg_d2}, 'f21_dvit_509_dv_zscore_at_expanding_close_max_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_509_dv_zscore_at_expanding_close_max_d2}, 'f21_dvit_510_dv_at_top_decile_5y_range_252d_mean_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f21_dvit_510_dv_at_top_decile_5y_range_252d_mean_d2}, 'f21_dvit_511_dv_per_body_size_ratio_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_511_dv_per_body_size_ratio_d2}, 'f21_dvit_512_dv_per_body_size_zscore_252d_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_512_dv_per_body_size_zscore_252d_d2}, 'f21_dvit_513_dv_per_true_range_ratio_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f21_dvit_513_dv_per_true_range_ratio_d2}, 'f21_dvit_514_dv_per_true_range_zscore_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f21_dvit_514_dv_per_true_range_zscore_252d_d2}, 'f21_dvit_515_dv_per_atr_ratio_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f21_dvit_515_dv_per_atr_ratio_d2}, 'f21_dvit_516_dv_per_atr_zscore_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f21_dvit_516_dv_per_atr_zscore_252d_d2}, 'f21_dvit_517_dv_per_abs_price_change_5d_sum_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_517_dv_per_abs_price_change_5d_sum_d2}, 'f21_dvit_518_dv_per_abs_price_change_21d_sum_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_518_dv_per_abs_price_change_21d_sum_d2}, 'f21_dvit_519_dv_per_hl_spread_ratio_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f21_dvit_519_dv_per_hl_spread_ratio_d2}, 'f21_dvit_520_dv_per_hl_spread_zscore_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f21_dvit_520_dv_per_hl_spread_zscore_252d_d2}, 'f21_dvit_521_roll_effective_spread_proxy_21d_d2': {'inputs': ['close'], 'func': f21_dvit_521_roll_effective_spread_proxy_21d_d2}, 'f21_dvit_522_roll_effective_spread_proxy_63d_d2': {'inputs': ['close'], 'func': f21_dvit_522_roll_effective_spread_proxy_63d_d2}, 'f21_dvit_523_dv_per_roll_spread_proxy_21d_d2': {'inputs': ['close', 'volume'], 'func': f21_dvit_523_dv_per_roll_spread_proxy_21d_d2}, 'f21_dvit_524_hl_spread_expansion_rate_21d_d2': {'inputs': ['high', 'low'], 'func': f21_dvit_524_hl_spread_expansion_rate_21d_d2}, 'f21_dvit_525_hl_spread_compression_indicator_d2': {'inputs': ['high', 'low'], 'func': f21_dvit_525_hl_spread_compression_indicator_d2}}