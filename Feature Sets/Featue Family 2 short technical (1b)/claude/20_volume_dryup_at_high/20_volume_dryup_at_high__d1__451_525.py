"""20_volume_dryup_at_high d1 features 451-525 — order-1 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff(). Self-contained; helpers redefined locally per HANDOFF."""
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

def f20_vdah_451_vol_vs_1d_ago_ratio_d1(volume: pd.Series) -> pd.Series:
    """Today's vol / 1-day-ago vol."""
    return _safe_div(volume, volume.shift(1)).diff()

def f20_vdah_452_vol_vs_2d_ago_ratio_d1(volume: pd.Series) -> pd.Series:
    """Today's vol / 2-day-ago vol."""
    return _safe_div(volume, volume.shift(2)).diff()

def f20_vdah_453_vol_vs_3d_ago_ratio_d1(volume: pd.Series) -> pd.Series:
    """Today's vol / 3-day-ago vol."""
    return _safe_div(volume, volume.shift(3)).diff()

def f20_vdah_454_vol_vs_5d_ago_ratio_d1(volume: pd.Series) -> pd.Series:
    """Today's vol / 5-day-ago vol."""
    return _safe_div(volume, volume.shift(5)).diff()

def f20_vdah_455_vol_vs_8d_ago_ratio_d1(volume: pd.Series) -> pd.Series:
    """Today's vol / 8-day-ago vol."""
    return _safe_div(volume, volume.shift(8)).diff()

def f20_vdah_456_vol_vs_13d_ago_ratio_d1(volume: pd.Series) -> pd.Series:
    """Today's vol / 13-day-ago vol."""
    return _safe_div(volume, volume.shift(13)).diff()

def f20_vdah_457_vol_vs_3d_mean_ratio_d1(volume: pd.Series) -> pd.Series:
    """Today's vol / trailing 3d mean vol."""
    return _safe_div(volume, volume.rolling(3, min_periods=2).mean()).diff()

def f20_vdah_458_vol_vs_8d_mean_ratio_d1(volume: pd.Series) -> pd.Series:
    """Today's vol / trailing 8d mean vol."""
    return _safe_div(volume, volume.rolling(8, min_periods=3).mean()).diff()

def f20_vdah_459_vol_vs_13d_mean_ratio_d1(volume: pd.Series) -> pd.Series:
    """Today's vol / trailing 13d mean vol."""
    return _safe_div(volume, volume.rolling(13, min_periods=5).mean()).diff()

def f20_vdah_460_vol_vs_34d_mean_ratio_d1(volume: pd.Series) -> pd.Series:
    """Today's vol / trailing 34d mean vol."""
    return _safe_div(volume, volume.rolling(34, min_periods=10).mean()).diff()

def f20_vdah_461_vol_vs_55d_mean_ratio_d1(volume: pd.Series) -> pd.Series:
    """Today's vol / trailing 55d mean vol."""
    return _safe_div(volume, volume.rolling(55, min_periods=15).mean()).diff()

def f20_vdah_462_vol_vs_3d_median_ratio_d1(volume: pd.Series) -> pd.Series:
    """Today's vol / trailing 3d median vol."""
    return _safe_div(volume, volume.rolling(3, min_periods=2).median()).diff()

def f20_vdah_463_vol_vs_8d_median_ratio_d1(volume: pd.Series) -> pd.Series:
    """Today's vol / trailing 8d median vol."""
    return _safe_div(volume, volume.rolling(8, min_periods=3).median()).diff()

def f20_vdah_464_vol_vs_13d_median_ratio_d1(volume: pd.Series) -> pd.Series:
    """Today's vol / trailing 13d median vol."""
    return _safe_div(volume, volume.rolling(13, min_periods=5).median()).diff()

def f20_vdah_465_vol_vs_34d_median_ratio_d1(volume: pd.Series) -> pd.Series:
    """Today's vol / trailing 34d median vol."""
    return _safe_div(volume, volume.rolling(34, min_periods=10).median()).diff()

def f20_vdah_466_vol_red_bars_avg_21d_d1(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on red bars (close < open) over trailing 21d."""
    return volume.where(close < open, np.nan).rolling(MDAYS, min_periods=WDAYS).mean().diff()

def f20_vdah_467_vol_green_bars_avg_21d_d1(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on green bars (close > open) over trailing 21d."""
    return volume.where(close > open, np.nan).rolling(MDAYS, min_periods=WDAYS).mean().diff()

def f20_vdah_468_vol_red_to_green_ratio_21d_d1(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(sum red-bar vol 21d) / (sum green-bar vol 21d)."""
    red = volume.where(close < open, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    grn = volume.where(close > open, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(red, grn + 1.0).diff()

def f20_vdah_469_vol_red_to_green_ratio_63d_d1(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(sum red-bar vol 63d) / (sum green-bar vol 63d)."""
    red = volume.where(close < open, 0.0).rolling(QDAYS, min_periods=MDAYS).sum()
    grn = volume.where(close > open, 0.0).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(red, grn + 1.0).diff()

def f20_vdah_470_vol_on_close_upper_third_red_252d_d1(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on bars where close in upper third of range AND close < open, over 252d."""
    pos = _safe_div(close - low, high - low)
    cond = (pos >= 0.67) & (close < open)
    return volume.where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f20_vdah_471_vol_on_close_lower_third_green_252d_d1(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on bars where close in lower third of range AND close > open, over 252d."""
    pos = _safe_div(close - low, high - low)
    cond = (pos <= 0.33) & (close > open)
    return volume.where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f20_vdah_472_vol_on_big_body_up_252d_d1(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on big-body-up bars (body > 70% of range AND close > open) over 252d."""
    rng = (high - low).replace(0, np.nan)
    body_pct = (close - open).abs() / rng
    cond = (body_pct > 0.7) & (close > open)
    return volume.where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f20_vdah_473_vol_on_big_body_down_252d_d1(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on big-body-down bars (body > 70% of range AND close < open) over 252d."""
    rng = (high - low).replace(0, np.nan)
    body_pct = (close - open).abs() / rng
    cond = (body_pct > 0.7) & (close < open)
    return volume.where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f20_vdah_474_vol_on_small_body_bars_252d_d1(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on small-body bars (|close-open| < 10% of range — doji-like) over 252d."""
    rng = (high - low).replace(0, np.nan)
    body_pct = (close - open).abs() / rng
    return volume.where(body_pct < 0.1, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f20_vdah_475_vol_on_long_upper_wick_bars_252d_d1(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on bars with upper wick > 50% of range (rejection candles) over 252d."""
    rng = (high - low).replace(0, np.nan)
    upper_wick = (high - pd.concat([close, open], axis=1).max(axis=1)) / rng
    return volume.where(upper_wick > 0.5, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f20_vdah_476_log_vol_bb_percent_b_20d_d1(volume: pd.Series) -> pd.Series:
    """%B for log-volume Bollinger Bands(20, 2): (log_vol - lower) / (upper - lower)."""
    lv = _safe_log(volume)
    m = lv.rolling(20, min_periods=10).mean()
    s = lv.rolling(20, min_periods=10).std()
    return _safe_div(lv - (m - 2.0 * s), 4.0 * s).diff()

def f20_vdah_477_log_vol_bb_bandwidth_20d_d1(volume: pd.Series) -> pd.Series:
    """Bollinger bandwidth on log-vol(20, 2): 4*std / |mean|."""
    lv = _safe_log(volume)
    m = lv.rolling(20, min_periods=10).mean()
    s = lv.rolling(20, min_periods=10).std()
    return _safe_div(4.0 * s, m.abs() + 1.0).diff()

def f20_vdah_478_log_vol_above_upper_bb_count_252d_d1(volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars with log-vol > 20d BB upper band."""
    lv = _safe_log(volume)
    m = lv.rolling(20, min_periods=10).mean()
    s = lv.rolling(20, min_periods=10).std()
    return (lv > m + 2.0 * s).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f20_vdah_479_log_vol_below_lower_bb_count_252d_d1(volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars with log-vol < 20d BB lower band."""
    lv = _safe_log(volume)
    m = lv.rolling(20, min_periods=10).mean()
    s = lv.rolling(20, min_periods=10).std()
    return (lv < m - 2.0 * s).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f20_vdah_480_log_vol_bb_squeeze_indicator_20d_d1(volume: pd.Series) -> pd.Series:
    """1 when log-vol BB bandwidth is in bottom decile of trailing 252d."""
    lv = _safe_log(volume)
    m = lv.rolling(20, min_periods=10).mean()
    s = lv.rolling(20, min_periods=10).std()
    bw = _safe_div(4.0 * s, m.abs() + 1.0)
    q10 = bw.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
    return (bw <= q10).astype(float).diff()

def f20_vdah_481_log_vol_keltner_position_20d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Position of log-vol within Keltner-style channel (20EMA log-vol ± 2*ATR21)."""
    lv = _safe_log(volume)
    ema = lv.ewm(span=20, min_periods=10, adjust=False).mean()
    atr = _atr(high, low, close, n=MDAYS)
    upper = ema + 2.0 * atr
    lower = ema - 2.0 * atr
    return _safe_div(lv - lower, upper - lower).diff()

def f20_vdah_482_vol_envelope_break_count_252d_d1(volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where vol breaks above (21d-EMA * 2) envelope."""
    ema21 = volume.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    return (volume > 2.0 * ema21).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f20_vdah_483_vol_envelope_squeeze_pct_rank_252d_d1(volume: pd.Series) -> pd.Series:
    """Percentile rank(252d) of distance from vol to 21d EMA, normalized by 252d std."""
    ema21 = volume.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()
    dist = (volume - ema21).abs()
    return dist.rolling(YDAYS, min_periods=QDAYS).rank(pct=True).diff()

def f20_vdah_484_log_vol_donchian_channel_position_21d_d1(volume: pd.Series) -> pd.Series:
    """(log_vol - 21d-min) / (21d-max - 21d-min) — Donchian-style position."""
    lv = _safe_log(volume)
    return _safe_div(lv - lv.rolling(MDAYS, min_periods=WDAYS).min(), lv.rolling(MDAYS, min_periods=WDAYS).max() - lv.rolling(MDAYS, min_periods=WDAYS).min()).diff()

def f20_vdah_485_log_vol_donchian_channel_position_63d_d1(volume: pd.Series) -> pd.Series:
    """(log_vol - 63d-min) / (63d-max - 63d-min)."""
    lv = _safe_log(volume)
    return _safe_div(lv - lv.rolling(QDAYS, min_periods=MDAYS).min(), lv.rolling(QDAYS, min_periods=MDAYS).max() - lv.rolling(QDAYS, min_periods=MDAYS).min()).diff()

def f20_vdah_486_log_vol_pct_rank_3d_d1(volume: pd.Series) -> pd.Series:
    """log-vol pct rank within trailing 3-day window."""
    return _safe_log(volume).rolling(3, min_periods=2).rank(pct=True).diff()

def f20_vdah_487_log_vol_pct_rank_5d_d1(volume: pd.Series) -> pd.Series:
    """log-vol pct rank within trailing 5-day window."""
    return _safe_log(volume).rolling(WDAYS, min_periods=2).rank(pct=True).diff()

def f20_vdah_488_log_vol_pct_rank_8d_d1(volume: pd.Series) -> pd.Series:
    """log-vol pct rank within trailing 8-day window."""
    return _safe_log(volume).rolling(8, min_periods=3).rank(pct=True).diff()

def f20_vdah_489_log_vol_pct_rank_13d_d1(volume: pd.Series) -> pd.Series:
    """log-vol pct rank within trailing 13-day window."""
    return _safe_log(volume).rolling(13, min_periods=5).rank(pct=True).diff()

def f20_vdah_490_log_vol_pct_rank_34d_d1(volume: pd.Series) -> pd.Series:
    """log-vol pct rank within trailing 34-day window."""
    return _safe_log(volume).rolling(34, min_periods=10).rank(pct=True).diff()

def f20_vdah_491_log_vol_pct_rank_55d_d1(volume: pd.Series) -> pd.Series:
    """log-vol pct rank within trailing 55-day window."""
    return _safe_log(volume).rolling(55, min_periods=15).rank(pct=True).diff()

def f20_vdah_492_log_vol_pct_rank_126d_d1(volume: pd.Series) -> pd.Series:
    """log-vol pct rank within trailing 126-day window."""
    return _safe_log(volume).rolling(126, min_periods=30).rank(pct=True).diff()

def f20_vdah_493_log_vol_pct_rank_diff_5_vs_55_d1(volume: pd.Series) -> pd.Series:
    """pct rank(log-vol, 5d) − pct rank(log-vol, 55d) — short-vs-long-rank shift."""
    lv = _safe_log(volume)
    return (lv.rolling(WDAYS, min_periods=2).rank(pct=True) - lv.rolling(55, min_periods=15).rank(pct=True)).diff()

def f20_vdah_494_log_vol_pct_rank_diff_13_vs_126_d1(volume: pd.Series) -> pd.Series:
    """pct rank(log-vol, 13d) − pct rank(log-vol, 126d)."""
    lv = _safe_log(volume)
    return (lv.rolling(13, min_periods=5).rank(pct=True) - lv.rolling(126, min_periods=30).rank(pct=True)).diff()

def f20_vdah_495_log_vol_pct_rank_diff_34_vs_252_d1(volume: pd.Series) -> pd.Series:
    """pct rank(log-vol, 34d) − pct rank(log-vol, 252d)."""
    lv = _safe_log(volume)
    return (lv.rolling(34, min_periods=10).rank(pct=True) - lv.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)).diff()

def f20_vdah_496_vol_at_top_quartile_21d_range_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on bars where close in top quartile of 21d range, trailing 252d."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    rmin21 = low.rolling(MDAYS, min_periods=WDAYS).min()
    pos = _safe_div(close - rmin21, rmax21 - rmin21)
    return volume.where(pos >= 0.75, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f20_vdah_497_vol_at_top_quartile_63d_range_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on bars where close in top quartile of 63d range, trailing 252d."""
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    rmin = low.rolling(QDAYS, min_periods=MDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return volume.where(pos >= 0.75, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f20_vdah_498_vol_at_top_quartile_252d_range_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on bars where close in top quartile of 252d range, trailing 252d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return volume.where(pos >= 0.75, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f20_vdah_499_vol_at_top_quartile_5y_range_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on bars where close in top quartile of 5y range, trailing 252d."""
    rmax = high.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    rmin = low.rolling(DDAYS_5Y, min_periods=YDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return volume.where(pos >= 0.75, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f20_vdah_500_vol_first_new_21d_high_after_drawdown_indicator_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when today's high is the first new 21d-high after >=5 consec days below it."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    below = high < rmax21.shift(1)
    streak_below_yest = _consecutive_true_streak(below.shift(1).fillna(False)).astype(float)
    return ((high >= rmax21) & (streak_below_yest >= WDAYS)).astype(float).diff()

def f20_vdah_501_vol_first_new_63d_high_after_drawdown_indicator_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when today's high is the first new 63d-high after >=21 consec days below it."""
    rmax63 = high.rolling(QDAYS, min_periods=MDAYS).max()
    below = high < rmax63.shift(1)
    streak_below_yest = _consecutive_true_streak(below.shift(1).fillna(False)).astype(float)
    return ((high >= rmax63) & (streak_below_yest >= MDAYS)).astype(float).diff()

def f20_vdah_502_vol_first_new_252d_high_after_drawdown_indicator_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when today's high is the first new 252d-high after >=63 consec days below it."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    below = high < rmax.shift(1)
    streak_below_yest = _consecutive_true_streak(below.shift(1).fillna(False)).astype(float)
    return ((high >= rmax) & (streak_below_yest >= QDAYS)).astype(float).diff()

def f20_vdah_503_vol_within_2pct_of_21d_high_avg_63d_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on bars within 2% of 21d trailing high, over trailing 63d."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    return volume.where(high >= 0.98 * rmax21, np.nan).rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f20_vdah_504_vol_within_2pct_of_63d_high_avg_252d_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on bars within 2% of 63d trailing high, over trailing 252d."""
    rmax63 = high.rolling(QDAYS, min_periods=MDAYS).max()
    return volume.where(high >= 0.98 * rmax63, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f20_vdah_505_vol_within_2pct_of_252d_high_avg_252d_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on bars within 2% of 252d trailing high, over 252d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return volume.where(high >= 0.98 * rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f20_vdah_506_vol_within_2pct_of_5y_high_avg_252d_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on bars within 2% of 5y trailing high, over 252d."""
    rmax = high.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    return volume.where(high >= 0.98 * rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f20_vdah_507_vol_on_3_consec_new_highs_avg_252d_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on bars where 3+ consecutive 21d-new-highs occurred."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    nh = high >= rmax21
    three_nh = nh & nh.shift(1) & nh.shift(2)
    return volume.where(three_nh, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f20_vdah_508_vol_on_5_consec_new_highs_avg_252d_d1(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on bars where 5+ consecutive 21d-new-highs occurred."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    nh = high >= rmax21
    five_nh = nh & nh.shift(1) & nh.shift(2) & nh.shift(3) & nh.shift(4)
    return volume.where(five_nh, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f20_vdah_509_vol_on_bars_at_expanding_close_max_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on bars where close = expanding-5y max."""
    rmax = close.expanding(min_periods=YDAYS).max()
    return volume.where(close >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f20_vdah_510_vol_zscore_at_expanding_close_max_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log-vol z(252d) on bars where close = expanding-5y max."""
    rmax = close.expanding(min_periods=YDAYS).max()
    z = _rolling_zscore(_safe_log(volume), YDAYS)
    return z.where(close >= rmax, np.nan).diff()

def f20_vdah_511_vol_per_body_size_ratio_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """vol / |close - close.shift(1)| — effort per unit price move (single bar)."""
    return _safe_div(volume, close.diff().abs()).diff()

def f20_vdah_512_vol_per_body_size_zscore_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of vol / |close.diff|."""
    return _rolling_zscore(_safe_div(volume, close.diff().abs()), YDAYS).diff()

def f20_vdah_513_vol_per_true_range_ratio_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vol / true_range — effort per unit range."""
    return _safe_div(volume, _true_range(high, low, close)).diff()

def f20_vdah_514_vol_per_true_range_zscore_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of vol / TR."""
    return _rolling_zscore(_safe_div(volume, _true_range(high, low, close)), YDAYS).diff()

def f20_vdah_515_vol_per_atr_ratio_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """vol / ATR21."""
    return _safe_div(volume, _atr(high, low, close, n=MDAYS)).diff()

def f20_vdah_516_vol_per_atr_zscore_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of vol / ATR21."""
    return _rolling_zscore(_safe_div(volume, _atr(high, low, close, n=MDAYS)), YDAYS).diff()

def f20_vdah_517_vol_per_abs_price_change_5d_sum_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum vol 5d / sum |close.diff| 5d — effort vs result over 5d."""
    return _safe_div(volume.rolling(WDAYS, min_periods=2).sum(), close.diff().abs().rolling(WDAYS, min_periods=2).sum()).diff()

def f20_vdah_518_vol_per_abs_price_change_21d_sum_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum vol 21d / sum |close.diff| 21d."""
    return _safe_div(volume.rolling(MDAYS, min_periods=WDAYS).sum(), close.diff().abs().rolling(MDAYS, min_periods=WDAYS).sum()).diff()

def f20_vdah_519_vol_per_hl_spread_ratio_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """vol / (high - low)."""
    return _safe_div(volume, high - low).diff()

def f20_vdah_520_vol_per_hl_spread_zscore_252d_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of vol / (high-low)."""
    return _rolling_zscore(_safe_div(volume, high - low), YDAYS).diff()

def f20_vdah_521_roll_effective_spread_proxy_21d_d1(close: pd.Series) -> pd.Series:
    """Roll (1984) effective-spread proxy: 2 * sqrt(max(-cov(r_t, r_{t-1}), 0)) over trailing 21d."""
    r = close.diff()
    rcov = r.rolling(MDAYS, min_periods=WDAYS).cov(r.shift(1))
    return (2.0 * np.sqrt((-rcov).clip(lower=0.0))).diff()

def f20_vdah_522_roll_effective_spread_proxy_63d_d1(close: pd.Series) -> pd.Series:
    """Roll effective-spread proxy over trailing 63d."""
    r = close.diff()
    rcov = r.rolling(QDAYS, min_periods=MDAYS).cov(r.shift(1))
    return (2.0 * np.sqrt((-rcov).clip(lower=0.0))).diff()

def f20_vdah_523_vol_per_roll_spread_proxy_21d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """vol / Roll effective-spread proxy(21d)."""
    r = close.diff()
    rcov = r.rolling(MDAYS, min_periods=WDAYS).cov(r.shift(1))
    spread = 2.0 * np.sqrt((-rcov).clip(lower=0.0))
    return _safe_div(volume, spread + 1e-09).diff()

def f20_vdah_524_hl_spread_expansion_rate_21d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """5d-mean (high-low) / 21d-mean (high-low) — short-vs-long range expansion."""
    sp = high - low
    return _safe_div(sp.rolling(WDAYS, min_periods=2).mean(), sp.rolling(MDAYS, min_periods=WDAYS).mean()).diff()

def f20_vdah_525_hl_spread_compression_indicator_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 when (high - low) / close < 0.5 × trailing 252d-median of same — range compression."""
    sp = (high - low) / close.replace(0, np.nan) if False else (high - low) / high.replace(0, np.nan)
    sp2 = (high - low) / high.replace(0, np.nan)
    med = sp2.rolling(YDAYS, min_periods=QDAYS).median()
    return (sp2 < 0.5 * med).astype(float).diff()
VOLUME_DRYUP_AT_HIGH_D1_REGISTRY_451_525 = {'f20_vdah_451_vol_vs_1d_ago_ratio_d1': {'inputs': ['volume'], 'func': f20_vdah_451_vol_vs_1d_ago_ratio_d1}, 'f20_vdah_452_vol_vs_2d_ago_ratio_d1': {'inputs': ['volume'], 'func': f20_vdah_452_vol_vs_2d_ago_ratio_d1}, 'f20_vdah_453_vol_vs_3d_ago_ratio_d1': {'inputs': ['volume'], 'func': f20_vdah_453_vol_vs_3d_ago_ratio_d1}, 'f20_vdah_454_vol_vs_5d_ago_ratio_d1': {'inputs': ['volume'], 'func': f20_vdah_454_vol_vs_5d_ago_ratio_d1}, 'f20_vdah_455_vol_vs_8d_ago_ratio_d1': {'inputs': ['volume'], 'func': f20_vdah_455_vol_vs_8d_ago_ratio_d1}, 'f20_vdah_456_vol_vs_13d_ago_ratio_d1': {'inputs': ['volume'], 'func': f20_vdah_456_vol_vs_13d_ago_ratio_d1}, 'f20_vdah_457_vol_vs_3d_mean_ratio_d1': {'inputs': ['volume'], 'func': f20_vdah_457_vol_vs_3d_mean_ratio_d1}, 'f20_vdah_458_vol_vs_8d_mean_ratio_d1': {'inputs': ['volume'], 'func': f20_vdah_458_vol_vs_8d_mean_ratio_d1}, 'f20_vdah_459_vol_vs_13d_mean_ratio_d1': {'inputs': ['volume'], 'func': f20_vdah_459_vol_vs_13d_mean_ratio_d1}, 'f20_vdah_460_vol_vs_34d_mean_ratio_d1': {'inputs': ['volume'], 'func': f20_vdah_460_vol_vs_34d_mean_ratio_d1}, 'f20_vdah_461_vol_vs_55d_mean_ratio_d1': {'inputs': ['volume'], 'func': f20_vdah_461_vol_vs_55d_mean_ratio_d1}, 'f20_vdah_462_vol_vs_3d_median_ratio_d1': {'inputs': ['volume'], 'func': f20_vdah_462_vol_vs_3d_median_ratio_d1}, 'f20_vdah_463_vol_vs_8d_median_ratio_d1': {'inputs': ['volume'], 'func': f20_vdah_463_vol_vs_8d_median_ratio_d1}, 'f20_vdah_464_vol_vs_13d_median_ratio_d1': {'inputs': ['volume'], 'func': f20_vdah_464_vol_vs_13d_median_ratio_d1}, 'f20_vdah_465_vol_vs_34d_median_ratio_d1': {'inputs': ['volume'], 'func': f20_vdah_465_vol_vs_34d_median_ratio_d1}, 'f20_vdah_466_vol_red_bars_avg_21d_d1': {'inputs': ['open', 'close', 'volume'], 'func': f20_vdah_466_vol_red_bars_avg_21d_d1}, 'f20_vdah_467_vol_green_bars_avg_21d_d1': {'inputs': ['open', 'close', 'volume'], 'func': f20_vdah_467_vol_green_bars_avg_21d_d1}, 'f20_vdah_468_vol_red_to_green_ratio_21d_d1': {'inputs': ['open', 'close', 'volume'], 'func': f20_vdah_468_vol_red_to_green_ratio_21d_d1}, 'f20_vdah_469_vol_red_to_green_ratio_63d_d1': {'inputs': ['open', 'close', 'volume'], 'func': f20_vdah_469_vol_red_to_green_ratio_63d_d1}, 'f20_vdah_470_vol_on_close_upper_third_red_252d_d1': {'inputs': ['high', 'low', 'open', 'close', 'volume'], 'func': f20_vdah_470_vol_on_close_upper_third_red_252d_d1}, 'f20_vdah_471_vol_on_close_lower_third_green_252d_d1': {'inputs': ['high', 'low', 'open', 'close', 'volume'], 'func': f20_vdah_471_vol_on_close_lower_third_green_252d_d1}, 'f20_vdah_472_vol_on_big_body_up_252d_d1': {'inputs': ['high', 'low', 'open', 'close', 'volume'], 'func': f20_vdah_472_vol_on_big_body_up_252d_d1}, 'f20_vdah_473_vol_on_big_body_down_252d_d1': {'inputs': ['high', 'low', 'open', 'close', 'volume'], 'func': f20_vdah_473_vol_on_big_body_down_252d_d1}, 'f20_vdah_474_vol_on_small_body_bars_252d_d1': {'inputs': ['high', 'low', 'open', 'close', 'volume'], 'func': f20_vdah_474_vol_on_small_body_bars_252d_d1}, 'f20_vdah_475_vol_on_long_upper_wick_bars_252d_d1': {'inputs': ['high', 'low', 'open', 'close', 'volume'], 'func': f20_vdah_475_vol_on_long_upper_wick_bars_252d_d1}, 'f20_vdah_476_log_vol_bb_percent_b_20d_d1': {'inputs': ['volume'], 'func': f20_vdah_476_log_vol_bb_percent_b_20d_d1}, 'f20_vdah_477_log_vol_bb_bandwidth_20d_d1': {'inputs': ['volume'], 'func': f20_vdah_477_log_vol_bb_bandwidth_20d_d1}, 'f20_vdah_478_log_vol_above_upper_bb_count_252d_d1': {'inputs': ['volume'], 'func': f20_vdah_478_log_vol_above_upper_bb_count_252d_d1}, 'f20_vdah_479_log_vol_below_lower_bb_count_252d_d1': {'inputs': ['volume'], 'func': f20_vdah_479_log_vol_below_lower_bb_count_252d_d1}, 'f20_vdah_480_log_vol_bb_squeeze_indicator_20d_d1': {'inputs': ['volume'], 'func': f20_vdah_480_log_vol_bb_squeeze_indicator_20d_d1}, 'f20_vdah_481_log_vol_keltner_position_20d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f20_vdah_481_log_vol_keltner_position_20d_d1}, 'f20_vdah_482_vol_envelope_break_count_252d_d1': {'inputs': ['volume'], 'func': f20_vdah_482_vol_envelope_break_count_252d_d1}, 'f20_vdah_483_vol_envelope_squeeze_pct_rank_252d_d1': {'inputs': ['volume'], 'func': f20_vdah_483_vol_envelope_squeeze_pct_rank_252d_d1}, 'f20_vdah_484_log_vol_donchian_channel_position_21d_d1': {'inputs': ['volume'], 'func': f20_vdah_484_log_vol_donchian_channel_position_21d_d1}, 'f20_vdah_485_log_vol_donchian_channel_position_63d_d1': {'inputs': ['volume'], 'func': f20_vdah_485_log_vol_donchian_channel_position_63d_d1}, 'f20_vdah_486_log_vol_pct_rank_3d_d1': {'inputs': ['volume'], 'func': f20_vdah_486_log_vol_pct_rank_3d_d1}, 'f20_vdah_487_log_vol_pct_rank_5d_d1': {'inputs': ['volume'], 'func': f20_vdah_487_log_vol_pct_rank_5d_d1}, 'f20_vdah_488_log_vol_pct_rank_8d_d1': {'inputs': ['volume'], 'func': f20_vdah_488_log_vol_pct_rank_8d_d1}, 'f20_vdah_489_log_vol_pct_rank_13d_d1': {'inputs': ['volume'], 'func': f20_vdah_489_log_vol_pct_rank_13d_d1}, 'f20_vdah_490_log_vol_pct_rank_34d_d1': {'inputs': ['volume'], 'func': f20_vdah_490_log_vol_pct_rank_34d_d1}, 'f20_vdah_491_log_vol_pct_rank_55d_d1': {'inputs': ['volume'], 'func': f20_vdah_491_log_vol_pct_rank_55d_d1}, 'f20_vdah_492_log_vol_pct_rank_126d_d1': {'inputs': ['volume'], 'func': f20_vdah_492_log_vol_pct_rank_126d_d1}, 'f20_vdah_493_log_vol_pct_rank_diff_5_vs_55_d1': {'inputs': ['volume'], 'func': f20_vdah_493_log_vol_pct_rank_diff_5_vs_55_d1}, 'f20_vdah_494_log_vol_pct_rank_diff_13_vs_126_d1': {'inputs': ['volume'], 'func': f20_vdah_494_log_vol_pct_rank_diff_13_vs_126_d1}, 'f20_vdah_495_log_vol_pct_rank_diff_34_vs_252_d1': {'inputs': ['volume'], 'func': f20_vdah_495_log_vol_pct_rank_diff_34_vs_252_d1}, 'f20_vdah_496_vol_at_top_quartile_21d_range_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f20_vdah_496_vol_at_top_quartile_21d_range_252d_d1}, 'f20_vdah_497_vol_at_top_quartile_63d_range_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f20_vdah_497_vol_at_top_quartile_63d_range_252d_d1}, 'f20_vdah_498_vol_at_top_quartile_252d_range_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f20_vdah_498_vol_at_top_quartile_252d_range_252d_d1}, 'f20_vdah_499_vol_at_top_quartile_5y_range_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f20_vdah_499_vol_at_top_quartile_5y_range_252d_d1}, 'f20_vdah_500_vol_first_new_21d_high_after_drawdown_indicator_d1': {'inputs': ['high', 'volume'], 'func': f20_vdah_500_vol_first_new_21d_high_after_drawdown_indicator_d1}, 'f20_vdah_501_vol_first_new_63d_high_after_drawdown_indicator_d1': {'inputs': ['high', 'volume'], 'func': f20_vdah_501_vol_first_new_63d_high_after_drawdown_indicator_d1}, 'f20_vdah_502_vol_first_new_252d_high_after_drawdown_indicator_d1': {'inputs': ['high', 'volume'], 'func': f20_vdah_502_vol_first_new_252d_high_after_drawdown_indicator_d1}, 'f20_vdah_503_vol_within_2pct_of_21d_high_avg_63d_d1': {'inputs': ['high', 'volume'], 'func': f20_vdah_503_vol_within_2pct_of_21d_high_avg_63d_d1}, 'f20_vdah_504_vol_within_2pct_of_63d_high_avg_252d_d1': {'inputs': ['high', 'volume'], 'func': f20_vdah_504_vol_within_2pct_of_63d_high_avg_252d_d1}, 'f20_vdah_505_vol_within_2pct_of_252d_high_avg_252d_d1': {'inputs': ['high', 'volume'], 'func': f20_vdah_505_vol_within_2pct_of_252d_high_avg_252d_d1}, 'f20_vdah_506_vol_within_2pct_of_5y_high_avg_252d_d1': {'inputs': ['high', 'volume'], 'func': f20_vdah_506_vol_within_2pct_of_5y_high_avg_252d_d1}, 'f20_vdah_507_vol_on_3_consec_new_highs_avg_252d_d1': {'inputs': ['high', 'volume'], 'func': f20_vdah_507_vol_on_3_consec_new_highs_avg_252d_d1}, 'f20_vdah_508_vol_on_5_consec_new_highs_avg_252d_d1': {'inputs': ['high', 'volume'], 'func': f20_vdah_508_vol_on_5_consec_new_highs_avg_252d_d1}, 'f20_vdah_509_vol_on_bars_at_expanding_close_max_d1': {'inputs': ['close', 'volume'], 'func': f20_vdah_509_vol_on_bars_at_expanding_close_max_d1}, 'f20_vdah_510_vol_zscore_at_expanding_close_max_d1': {'inputs': ['close', 'volume'], 'func': f20_vdah_510_vol_zscore_at_expanding_close_max_d1}, 'f20_vdah_511_vol_per_body_size_ratio_d1': {'inputs': ['close', 'volume'], 'func': f20_vdah_511_vol_per_body_size_ratio_d1}, 'f20_vdah_512_vol_per_body_size_zscore_252d_d1': {'inputs': ['close', 'volume'], 'func': f20_vdah_512_vol_per_body_size_zscore_252d_d1}, 'f20_vdah_513_vol_per_true_range_ratio_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f20_vdah_513_vol_per_true_range_ratio_d1}, 'f20_vdah_514_vol_per_true_range_zscore_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f20_vdah_514_vol_per_true_range_zscore_252d_d1}, 'f20_vdah_515_vol_per_atr_ratio_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f20_vdah_515_vol_per_atr_ratio_d1}, 'f20_vdah_516_vol_per_atr_zscore_252d_d1': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f20_vdah_516_vol_per_atr_zscore_252d_d1}, 'f20_vdah_517_vol_per_abs_price_change_5d_sum_d1': {'inputs': ['close', 'volume'], 'func': f20_vdah_517_vol_per_abs_price_change_5d_sum_d1}, 'f20_vdah_518_vol_per_abs_price_change_21d_sum_d1': {'inputs': ['close', 'volume'], 'func': f20_vdah_518_vol_per_abs_price_change_21d_sum_d1}, 'f20_vdah_519_vol_per_hl_spread_ratio_d1': {'inputs': ['high', 'low', 'volume'], 'func': f20_vdah_519_vol_per_hl_spread_ratio_d1}, 'f20_vdah_520_vol_per_hl_spread_zscore_252d_d1': {'inputs': ['high', 'low', 'volume'], 'func': f20_vdah_520_vol_per_hl_spread_zscore_252d_d1}, 'f20_vdah_521_roll_effective_spread_proxy_21d_d1': {'inputs': ['close'], 'func': f20_vdah_521_roll_effective_spread_proxy_21d_d1}, 'f20_vdah_522_roll_effective_spread_proxy_63d_d1': {'inputs': ['close'], 'func': f20_vdah_522_roll_effective_spread_proxy_63d_d1}, 'f20_vdah_523_vol_per_roll_spread_proxy_21d_d1': {'inputs': ['close', 'volume'], 'func': f20_vdah_523_vol_per_roll_spread_proxy_21d_d1}, 'f20_vdah_524_hl_spread_expansion_rate_21d_d1': {'inputs': ['high', 'low'], 'func': f20_vdah_524_hl_spread_expansion_rate_21d_d1}, 'f20_vdah_525_hl_spread_compression_indicator_d1': {'inputs': ['high', 'low'], 'func': f20_vdah_525_hl_spread_compression_indicator_d1}}