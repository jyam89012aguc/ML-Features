"""22_on_balance_volume_dynamics d3 features 451-525 — order-3 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
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

def _obv(close, volume):
    sgn = np.sign(close.diff()).fillna(0.0)
    return (sgn * volume).cumsum()

def f22_obvd_451_obv_diff_vs_1d_ago_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's OBV-diff minus 1-day-ago OBV-diff."""
    return (_obv(close, volume).diff() - _obv(close, volume).diff().shift(1)).diff().diff().diff()

def f22_obvd_452_obv_diff_vs_2d_ago_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's OBV-diff minus 2-day-ago OBV-diff."""
    return (_obv(close, volume).diff() - _obv(close, volume).diff().shift(2)).diff().diff().diff()

def f22_obvd_453_obv_diff_vs_3d_ago_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's OBV-diff minus 3-day-ago OBV-diff."""
    return (_obv(close, volume).diff() - _obv(close, volume).diff().shift(3)).diff().diff().diff()

def f22_obvd_454_obv_diff_vs_5d_ago_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's OBV-diff minus 5-day-ago OBV-diff."""
    return (_obv(close, volume).diff() - _obv(close, volume).diff().shift(5)).diff().diff().diff()

def f22_obvd_455_obv_diff_vs_8d_ago_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's OBV-diff minus 8-day-ago OBV-diff."""
    return (_obv(close, volume).diff() - _obv(close, volume).diff().shift(8)).diff().diff().diff()

def f22_obvd_456_obv_diff_vs_13d_ago_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's OBV-diff minus 13-day-ago OBV-diff."""
    return (_obv(close, volume).diff() - _obv(close, volume).diff().shift(13)).diff().diff().diff()

def f22_obvd_457_obv_vs_3d_mean_diff_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV − trailing 3d mean OBV."""
    obv = _obv(close, volume)
    return (obv - obv.rolling(3, min_periods=2).mean()).diff().diff().diff()

def f22_obvd_458_obv_vs_8d_mean_diff_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV − trailing 8d mean OBV."""
    obv = _obv(close, volume)
    return (obv - obv.rolling(8, min_periods=3).mean()).diff().diff().diff()

def f22_obvd_459_obv_vs_13d_mean_diff_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV − trailing 13d mean OBV."""
    obv = _obv(close, volume)
    return (obv - obv.rolling(13, min_periods=5).mean()).diff().diff().diff()

def f22_obvd_460_obv_vs_34d_mean_diff_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV − trailing 34d mean OBV."""
    obv = _obv(close, volume)
    return (obv - obv.rolling(34, min_periods=10).mean()).diff().diff().diff()

def f22_obvd_461_obv_vs_55d_mean_diff_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV − trailing 55d mean OBV."""
    obv = _obv(close, volume)
    return (obv - obv.rolling(55, min_periods=15).mean()).diff().diff().diff()

def f22_obvd_462_obv_vs_3d_median_diff_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV − trailing 3d median."""
    obv = _obv(close, volume)
    return (obv - obv.rolling(3, min_periods=2).median()).diff().diff().diff()

def f22_obvd_463_obv_vs_8d_median_diff_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV − trailing 8d median."""
    obv = _obv(close, volume)
    return (obv - obv.rolling(8, min_periods=3).median()).diff().diff().diff()

def f22_obvd_464_obv_vs_13d_median_diff_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV − trailing 13d median."""
    obv = _obv(close, volume)
    return (obv - obv.rolling(13, min_periods=5).median()).diff().diff().diff()

def f22_obvd_465_obv_vs_34d_median_diff_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV − trailing 34d median."""
    obv = _obv(close, volume)
    return (obv - obv.rolling(34, min_periods=10).median()).diff().diff().diff()

def f22_obvd_466_obv_diff_red_bars_avg_21d_d3(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on red bars (close<open) over 21d."""
    obv = _obv(close, volume)
    return obv.diff().where(close < open, np.nan).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff().diff()

def f22_obvd_467_obv_diff_green_bars_avg_21d_d3(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on green bars (close>open) over 21d."""
    obv = _obv(close, volume)
    return obv.diff().where(close > open, np.nan).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff().diff()

def f22_obvd_468_obv_diff_red_to_green_ratio_21d_d3(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(sum |OBV-diff| on red 21d) / (sum |OBV-diff| on green 21d)."""
    obv = _obv(close, volume)
    d = obv.diff().abs()
    red = d.where(close < open, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    grn = d.where(close > open, 0.0).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(red, grn + 1.0).diff().diff().diff()

def f22_obvd_469_obv_diff_red_to_green_ratio_63d_d3(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(sum |OBV-diff| on red 63d) / (sum |OBV-diff| on green 63d)."""
    obv = _obv(close, volume)
    d = obv.diff().abs()
    red = d.where(close < open, 0.0).rolling(QDAYS, min_periods=MDAYS).sum()
    grn = d.where(close > open, 0.0).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(red, grn + 1.0).diff().diff().diff()

def f22_obvd_470_obv_diff_on_close_upper_third_red_252d_d3(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on close-in-upper-third red bars over 252d."""
    pos = _safe_div(close - low, high - low)
    cond = (pos >= 0.67) & (close < open)
    return _obv(close, volume).diff().where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f22_obvd_471_obv_diff_on_close_lower_third_green_252d_d3(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on close-in-lower-third green bars over 252d."""
    pos = _safe_div(close - low, high - low)
    cond = (pos <= 0.33) & (close > open)
    return _obv(close, volume).diff().where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f22_obvd_472_obv_diff_on_big_body_up_252d_d3(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on big-body-up bars over 252d."""
    rng = (high - low).replace(0, np.nan)
    body_pct = (close - open).abs() / rng
    cond = (body_pct > 0.7) & (close > open)
    return _obv(close, volume).diff().where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f22_obvd_473_obv_diff_on_big_body_down_252d_d3(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on big-body-down bars over 252d."""
    rng = (high - low).replace(0, np.nan)
    body_pct = (close - open).abs() / rng
    cond = (body_pct > 0.7) & (close < open)
    return _obv(close, volume).diff().where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f22_obvd_474_obv_diff_on_small_body_bars_252d_d3(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on small-body bars over 252d."""
    rng = (high - low).replace(0, np.nan)
    body_pct = (close - open).abs() / rng
    return _obv(close, volume).diff().where(body_pct < 0.1, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f22_obvd_475_obv_diff_on_long_upper_wick_bars_252d_d3(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on long-upper-wick bars over 252d."""
    rng = (high - low).replace(0, np.nan)
    upper_wick = (high - pd.concat([close, open], axis=1).max(axis=1)) / rng
    return _obv(close, volume).diff().where(upper_wick > 0.5, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f22_obvd_476_obv_bb_percent_b_20d_classic_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV %B for BB(20, 2)."""
    obv = _obv(close, volume)
    m = obv.rolling(20, min_periods=10).mean()
    s = obv.rolling(20, min_periods=10).std()
    return _safe_div(obv - (m - 2.0 * s), 4.0 * s).diff().diff().diff()

def f22_obvd_477_obv_bb_bandwidth_50d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV BB bandwidth(50, 2)."""
    obv = _obv(close, volume)
    m = obv.rolling(50, min_periods=20).mean()
    s = obv.rolling(50, min_periods=20).std()
    return _safe_div(4.0 * s, m.abs() + 1.0).diff().diff().diff()

def f22_obvd_478_obv_bb_percent_b_50d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV %B for BB(50, 2)."""
    obv = _obv(close, volume)
    m = obv.rolling(50, min_periods=20).mean()
    s = obv.rolling(50, min_periods=20).std()
    return _safe_div(obv - (m - 2.0 * s), 4.0 * s).diff().diff().diff()

def f22_obvd_479_obv_above_upper_bb_50d_count_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where OBV > 50d-BB upper band."""
    obv = _obv(close, volume)
    m = obv.rolling(50, min_periods=20).mean()
    s = obv.rolling(50, min_periods=20).std()
    return (obv > m + 2.0 * s).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f22_obvd_480_obv_below_lower_bb_50d_count_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where OBV < 50d-BB lower band."""
    obv = _obv(close, volume)
    m = obv.rolling(50, min_periods=20).mean()
    s = obv.rolling(50, min_periods=20).std()
    return (obv < m - 2.0 * s).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff().diff()

def f22_obvd_481_obv_walking_lower_bb_indicator_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV below lower 20d-BB for >=3 consecutive bars."""
    obv = _obv(close, volume)
    m = obv.rolling(20, min_periods=10).mean()
    s = obv.rolling(20, min_periods=10).std()
    lower = m - 2.0 * s
    streak = _consecutive_true_streak(obv < lower).astype(float)
    return (streak >= 3).astype(float).diff().diff().diff()

def f22_obvd_482_obv_above_3sigma_bb_50d_indicator_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV > 50d-BB(3-sigma) upper band — extreme."""
    obv = _obv(close, volume)
    m = obv.rolling(50, min_periods=20).mean()
    s = obv.rolling(50, min_periods=20).std()
    return (obv > m + 3.0 * s).astype(float).diff().diff().diff()

def f22_obvd_483_obv_below_3sigma_bb_50d_indicator_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV < 50d-BB(3-sigma) lower band — extreme."""
    obv = _obv(close, volume)
    m = obv.rolling(50, min_periods=20).mean()
    s = obv.rolling(50, min_periods=20).std()
    return (obv < m - 3.0 * s).astype(float).diff().diff().diff()

def f22_obvd_484_obv_donchian_channel_position_21d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(OBV - 21d-min OBV) / (21d-max OBV - 21d-min OBV)."""
    obv = _obv(close, volume)
    return _safe_div(obv - obv.rolling(MDAYS, min_periods=WDAYS).min(), obv.rolling(MDAYS, min_periods=WDAYS).max() - obv.rolling(MDAYS, min_periods=WDAYS).min()).diff().diff().diff()

def f22_obvd_485_obv_donchian_channel_position_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(OBV - 252d-min OBV) / (252d-max OBV - 252d-min OBV)."""
    obv = _obv(close, volume)
    return _safe_div(obv - obv.rolling(YDAYS, min_periods=QDAYS).min(), obv.rolling(YDAYS, min_periods=QDAYS).max() - obv.rolling(YDAYS, min_periods=QDAYS).min()).diff().diff().diff()

def f22_obvd_486_obv_pct_rank_3d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV pct rank within trailing 3d."""
    return _obv(close, volume).rolling(3, min_periods=2).rank(pct=True).diff().diff().diff()

def f22_obvd_487_obv_pct_rank_5d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV pct rank within trailing 5d."""
    return _obv(close, volume).rolling(WDAYS, min_periods=2).rank(pct=True).diff().diff().diff()

def f22_obvd_488_obv_pct_rank_8d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV pct rank within trailing 8d."""
    return _obv(close, volume).rolling(8, min_periods=3).rank(pct=True).diff().diff().diff()

def f22_obvd_489_obv_pct_rank_13d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV pct rank within trailing 13d."""
    return _obv(close, volume).rolling(13, min_periods=5).rank(pct=True).diff().diff().diff()

def f22_obvd_490_obv_pct_rank_34d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV pct rank within trailing 34d."""
    return _obv(close, volume).rolling(34, min_periods=10).rank(pct=True).diff().diff().diff()

def f22_obvd_491_obv_pct_rank_55d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV pct rank within trailing 55d."""
    return _obv(close, volume).rolling(55, min_periods=15).rank(pct=True).diff().diff().diff()

def f22_obvd_492_obv_pct_rank_126d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV pct rank within trailing 126d."""
    return _obv(close, volume).rolling(126, min_periods=30).rank(pct=True).diff().diff().diff()

def f22_obvd_493_obv_pct_rank_diff_5_vs_55_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """pct rank(OBV,5d) − pct rank(OBV,55d)."""
    obv = _obv(close, volume)
    return (obv.rolling(WDAYS, min_periods=2).rank(pct=True) - obv.rolling(55, min_periods=15).rank(pct=True)).diff().diff().diff()

def f22_obvd_494_obv_pct_rank_diff_13_vs_126_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """pct rank(OBV,13d) − pct rank(OBV,126d)."""
    obv = _obv(close, volume)
    return (obv.rolling(13, min_periods=5).rank(pct=True) - obv.rolling(126, min_periods=30).rank(pct=True)).diff().diff().diff()

def f22_obvd_495_obv_pct_rank_diff_34_vs_252_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """pct rank(OBV,34d) − pct rank(OBV,252d)."""
    obv = _obv(close, volume)
    return (obv.rolling(34, min_periods=10).rank(pct=True) - obv.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)).diff().diff().diff()

def f22_obvd_496_obv_diff_at_top_quartile_21d_range_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on close-in-top-quartile-of-21d-range bars, 252d."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    rmin21 = low.rolling(MDAYS, min_periods=WDAYS).min()
    pos = _safe_div(close - rmin21, rmax21 - rmin21)
    return _obv(close, volume).diff().where(pos >= 0.75, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f22_obvd_497_obv_diff_at_top_quartile_63d_range_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on close-in-top-quartile-of-63d-range bars, 252d."""
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    rmin = low.rolling(QDAYS, min_periods=MDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return _obv(close, volume).diff().where(pos >= 0.75, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f22_obvd_498_obv_diff_at_top_quartile_252d_range_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on close-in-top-quartile-of-252d-range bars, 252d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return _obv(close, volume).diff().where(pos >= 0.75, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f22_obvd_499_obv_diff_at_top_quartile_5y_range_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on close-in-top-quartile-of-5y-range bars, 252d."""
    rmax = high.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    rmin = low.rolling(DDAYS_5Y, min_periods=YDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    return _obv(close, volume).diff().where(pos >= 0.75, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f22_obvd_500_obv_diff_at_first_new_252d_high_after_drawdown_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV-diff on bars that are first-new-252d-high after >=63 consec days below."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    below = high < rmax.shift(1)
    streak_below_yest = _consecutive_true_streak(below.shift(1).fillna(False)).astype(float)
    cond = (high >= rmax) & (streak_below_yest >= QDAYS)
    return _obv(close, volume).diff().where(cond, np.nan).diff().diff().diff()

def f22_obvd_501_obv_diff_within_2pct_of_21d_high_avg_63d_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on bars within 2% of 21d trailing high, over 63d."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    return _obv(close, volume).diff().where(high >= 0.98 * rmax21, np.nan).rolling(QDAYS, min_periods=MDAYS).mean().diff().diff().diff()

def f22_obvd_502_obv_diff_within_2pct_of_63d_high_avg_252d_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on bars within 2% of 63d trailing high, over 252d."""
    rmax63 = high.rolling(QDAYS, min_periods=MDAYS).max()
    return _obv(close, volume).diff().where(high >= 0.98 * rmax63, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f22_obvd_503_obv_diff_within_2pct_of_252d_high_avg_252d_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on bars within 2% of 252d trailing high, over 252d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return _obv(close, volume).diff().where(high >= 0.98 * rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f22_obvd_504_obv_diff_within_2pct_of_5y_high_avg_252d_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on bars within 2% of 5y trailing high, over 252d."""
    rmax = high.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    return _obv(close, volume).diff().where(high >= 0.98 * rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f22_obvd_505_obv_diff_on_3_consec_new_highs_avg_252d_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on 3-consec-21d-new-high bars, 252d."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    nh = high >= rmax21
    three_nh = nh & nh.shift(1) & nh.shift(2)
    return _obv(close, volume).diff().where(three_nh, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f22_obvd_506_obv_diff_on_5_consec_new_highs_avg_252d_d3(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on 5-consec-21d-new-high bars, 252d."""
    rmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    nh = high >= rmax21
    five_nh = nh & nh.shift(1) & nh.shift(2) & nh.shift(3) & nh.shift(4)
    return _obv(close, volume).diff().where(five_nh, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f22_obvd_507_obv_diff_on_expanding_close_max_avg_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg OBV-diff on bars where close = expanding-5y max."""
    rmax = close.expanding(min_periods=YDAYS).max()
    return _obv(close, volume).diff().where(close >= rmax, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f22_obvd_508_obv_diff_zscore_at_expanding_close_max_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV-diff z(252d) on bars where close = expanding-5y max."""
    rmax = close.expanding(min_periods=YDAYS).max()
    z = _rolling_zscore(_obv(close, volume).diff(), YDAYS)
    return z.where(close >= rmax, np.nan).diff().diff().diff()

def f22_obvd_509_obv_diff_at_top_decile_5y_range_avg_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean OBV-diff z(252d) on close-in-top-decile-of-5y-range bars."""
    rmax = high.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    rmin = low.rolling(DDAYS_5Y, min_periods=YDAYS).min()
    pos = _safe_div(close - rmin, rmax - rmin)
    z = _rolling_zscore(_obv(close, volume).diff(), YDAYS)
    return z.where(pos >= 0.9, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff().diff()

def f22_obvd_510_obv_pct_rank_252d_when_close_top_decile_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV pct rank(252d) on bars where close in top decile of 252d."""
    pr_c = close.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    pr_o = _obv(close, volume).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return pr_o.where(pr_c >= 0.9, np.nan).diff().diff().diff()

def f22_obvd_511_obv_diff_per_body_size_ratio_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """|OBV-diff| / |close - close.shift(1)| — flow effort per unit price move."""
    obv = _obv(close, volume)
    return _safe_div(obv.diff().abs(), close.diff().abs()).diff().diff().diff()

def f22_obvd_512_obv_diff_per_body_size_zscore_252d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of |OBV-diff| / |close.diff|."""
    obv = _obv(close, volume)
    return _rolling_zscore(_safe_div(obv.diff().abs(), close.diff().abs()), YDAYS).diff().diff().diff()

def f22_obvd_513_obv_diff_per_true_range_ratio_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """|OBV-diff| / true_range."""
    obv = _obv(close, volume)
    return _safe_div(obv.diff().abs(), _true_range(high, low, close)).diff().diff().diff()

def f22_obvd_514_obv_diff_per_true_range_zscore_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of |OBV-diff| / TR."""
    obv = _obv(close, volume)
    return _rolling_zscore(_safe_div(obv.diff().abs(), _true_range(high, low, close)), YDAYS).diff().diff().diff()

def f22_obvd_515_obv_diff_per_atr_ratio_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """|OBV-diff| / ATR21."""
    obv = _obv(close, volume)
    return _safe_div(obv.diff().abs(), _atr(high, low, close, n=MDAYS)).diff().diff().diff()

def f22_obvd_516_obv_diff_per_atr_zscore_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of |OBV-diff| / ATR21."""
    obv = _obv(close, volume)
    return _rolling_zscore(_safe_div(obv.diff().abs(), _atr(high, low, close, n=MDAYS)), YDAYS).diff().diff().diff()

def f22_obvd_517_obv_diff_per_abs_price_change_5d_sum_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum |OBV-diff| 5d / sum |close.diff| 5d."""
    obv = _obv(close, volume)
    return _safe_div(obv.diff().abs().rolling(WDAYS, min_periods=2).sum(), close.diff().abs().rolling(WDAYS, min_periods=2).sum()).diff().diff().diff()

def f22_obvd_518_obv_diff_per_abs_price_change_21d_sum_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum |OBV-diff| 21d / sum |close.diff| 21d."""
    obv = _obv(close, volume)
    return _safe_div(obv.diff().abs().rolling(MDAYS, min_periods=WDAYS).sum(), close.diff().abs().rolling(MDAYS, min_periods=WDAYS).sum()).diff().diff().diff()

def f22_obvd_519_obv_diff_per_hl_spread_ratio_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """|OBV-diff| / (high - low)."""
    obv = _obv(close, volume)
    return _safe_div(obv.diff().abs(), high - low).diff().diff().diff()

def f22_obvd_520_obv_diff_per_hl_spread_zscore_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of |OBV-diff| / (high-low)."""
    obv = _obv(close, volume)
    return _rolling_zscore(_safe_div(obv.diff().abs(), high - low), YDAYS).diff().diff().diff()

def f22_obvd_521_obv_roll_spread_proxy_21d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Roll(1984) effective-spread proxy on OBV-diff over 21d."""
    obv = _obv(close, volume)
    d = obv.diff()
    rcov = d.rolling(MDAYS, min_periods=WDAYS).cov(d.shift(1))
    return (2.0 * np.sqrt((-rcov).clip(lower=0.0))).diff().diff().diff()

def f22_obvd_522_obv_roll_spread_proxy_63d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Roll effective-spread proxy on OBV-diff over 63d."""
    obv = _obv(close, volume)
    d = obv.diff()
    rcov = d.rolling(QDAYS, min_periods=MDAYS).cov(d.shift(1))
    return (2.0 * np.sqrt((-rcov).clip(lower=0.0))).diff().diff().diff()

def f22_obvd_523_obv_diff_per_roll_spread_proxy_21d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """|OBV-diff| / Roll OBV-spread proxy(21d)."""
    obv = _obv(close, volume)
    d = obv.diff()
    rcov = d.rolling(MDAYS, min_periods=WDAYS).cov(d.shift(1))
    spread = 2.0 * np.sqrt((-rcov).clip(lower=0.0))
    return _safe_div(d.abs(), spread + 1e-09).diff().diff().diff()

def f22_obvd_524_obv_diff_kurtosis_21d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21d kurtosis of OBV-diff — single-bar shock concentration."""
    obv = _obv(close, volume)
    return obv.diff().rolling(MDAYS, min_periods=WDAYS).kurt().diff().diff().diff()

def f22_obvd_525_obv_diff_skewness_21d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21d skewness of OBV-diff."""
    obv = _obv(close, volume)
    return obv.diff().rolling(MDAYS, min_periods=WDAYS).skew().diff().diff().diff()
ON_BALANCE_VOLUME_DYNAMICS_D3_REGISTRY_451_525 = {'f22_obvd_451_obv_diff_vs_1d_ago_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_451_obv_diff_vs_1d_ago_d3}, 'f22_obvd_452_obv_diff_vs_2d_ago_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_452_obv_diff_vs_2d_ago_d3}, 'f22_obvd_453_obv_diff_vs_3d_ago_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_453_obv_diff_vs_3d_ago_d3}, 'f22_obvd_454_obv_diff_vs_5d_ago_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_454_obv_diff_vs_5d_ago_d3}, 'f22_obvd_455_obv_diff_vs_8d_ago_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_455_obv_diff_vs_8d_ago_d3}, 'f22_obvd_456_obv_diff_vs_13d_ago_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_456_obv_diff_vs_13d_ago_d3}, 'f22_obvd_457_obv_vs_3d_mean_diff_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_457_obv_vs_3d_mean_diff_d3}, 'f22_obvd_458_obv_vs_8d_mean_diff_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_458_obv_vs_8d_mean_diff_d3}, 'f22_obvd_459_obv_vs_13d_mean_diff_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_459_obv_vs_13d_mean_diff_d3}, 'f22_obvd_460_obv_vs_34d_mean_diff_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_460_obv_vs_34d_mean_diff_d3}, 'f22_obvd_461_obv_vs_55d_mean_diff_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_461_obv_vs_55d_mean_diff_d3}, 'f22_obvd_462_obv_vs_3d_median_diff_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_462_obv_vs_3d_median_diff_d3}, 'f22_obvd_463_obv_vs_8d_median_diff_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_463_obv_vs_8d_median_diff_d3}, 'f22_obvd_464_obv_vs_13d_median_diff_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_464_obv_vs_13d_median_diff_d3}, 'f22_obvd_465_obv_vs_34d_median_diff_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_465_obv_vs_34d_median_diff_d3}, 'f22_obvd_466_obv_diff_red_bars_avg_21d_d3': {'inputs': ['open', 'close', 'volume'], 'func': f22_obvd_466_obv_diff_red_bars_avg_21d_d3}, 'f22_obvd_467_obv_diff_green_bars_avg_21d_d3': {'inputs': ['open', 'close', 'volume'], 'func': f22_obvd_467_obv_diff_green_bars_avg_21d_d3}, 'f22_obvd_468_obv_diff_red_to_green_ratio_21d_d3': {'inputs': ['open', 'close', 'volume'], 'func': f22_obvd_468_obv_diff_red_to_green_ratio_21d_d3}, 'f22_obvd_469_obv_diff_red_to_green_ratio_63d_d3': {'inputs': ['open', 'close', 'volume'], 'func': f22_obvd_469_obv_diff_red_to_green_ratio_63d_d3}, 'f22_obvd_470_obv_diff_on_close_upper_third_red_252d_d3': {'inputs': ['high', 'low', 'open', 'close', 'volume'], 'func': f22_obvd_470_obv_diff_on_close_upper_third_red_252d_d3}, 'f22_obvd_471_obv_diff_on_close_lower_third_green_252d_d3': {'inputs': ['high', 'low', 'open', 'close', 'volume'], 'func': f22_obvd_471_obv_diff_on_close_lower_third_green_252d_d3}, 'f22_obvd_472_obv_diff_on_big_body_up_252d_d3': {'inputs': ['high', 'low', 'open', 'close', 'volume'], 'func': f22_obvd_472_obv_diff_on_big_body_up_252d_d3}, 'f22_obvd_473_obv_diff_on_big_body_down_252d_d3': {'inputs': ['high', 'low', 'open', 'close', 'volume'], 'func': f22_obvd_473_obv_diff_on_big_body_down_252d_d3}, 'f22_obvd_474_obv_diff_on_small_body_bars_252d_d3': {'inputs': ['high', 'low', 'open', 'close', 'volume'], 'func': f22_obvd_474_obv_diff_on_small_body_bars_252d_d3}, 'f22_obvd_475_obv_diff_on_long_upper_wick_bars_252d_d3': {'inputs': ['high', 'low', 'open', 'close', 'volume'], 'func': f22_obvd_475_obv_diff_on_long_upper_wick_bars_252d_d3}, 'f22_obvd_476_obv_bb_percent_b_20d_classic_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_476_obv_bb_percent_b_20d_classic_d3}, 'f22_obvd_477_obv_bb_bandwidth_50d_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_477_obv_bb_bandwidth_50d_d3}, 'f22_obvd_478_obv_bb_percent_b_50d_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_478_obv_bb_percent_b_50d_d3}, 'f22_obvd_479_obv_above_upper_bb_50d_count_252d_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_479_obv_above_upper_bb_50d_count_252d_d3}, 'f22_obvd_480_obv_below_lower_bb_50d_count_252d_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_480_obv_below_lower_bb_50d_count_252d_d3}, 'f22_obvd_481_obv_walking_lower_bb_indicator_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_481_obv_walking_lower_bb_indicator_d3}, 'f22_obvd_482_obv_above_3sigma_bb_50d_indicator_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_482_obv_above_3sigma_bb_50d_indicator_d3}, 'f22_obvd_483_obv_below_3sigma_bb_50d_indicator_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_483_obv_below_3sigma_bb_50d_indicator_d3}, 'f22_obvd_484_obv_donchian_channel_position_21d_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_484_obv_donchian_channel_position_21d_d3}, 'f22_obvd_485_obv_donchian_channel_position_252d_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_485_obv_donchian_channel_position_252d_d3}, 'f22_obvd_486_obv_pct_rank_3d_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_486_obv_pct_rank_3d_d3}, 'f22_obvd_487_obv_pct_rank_5d_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_487_obv_pct_rank_5d_d3}, 'f22_obvd_488_obv_pct_rank_8d_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_488_obv_pct_rank_8d_d3}, 'f22_obvd_489_obv_pct_rank_13d_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_489_obv_pct_rank_13d_d3}, 'f22_obvd_490_obv_pct_rank_34d_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_490_obv_pct_rank_34d_d3}, 'f22_obvd_491_obv_pct_rank_55d_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_491_obv_pct_rank_55d_d3}, 'f22_obvd_492_obv_pct_rank_126d_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_492_obv_pct_rank_126d_d3}, 'f22_obvd_493_obv_pct_rank_diff_5_vs_55_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_493_obv_pct_rank_diff_5_vs_55_d3}, 'f22_obvd_494_obv_pct_rank_diff_13_vs_126_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_494_obv_pct_rank_diff_13_vs_126_d3}, 'f22_obvd_495_obv_pct_rank_diff_34_vs_252_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_495_obv_pct_rank_diff_34_vs_252_d3}, 'f22_obvd_496_obv_diff_at_top_quartile_21d_range_252d_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f22_obvd_496_obv_diff_at_top_quartile_21d_range_252d_d3}, 'f22_obvd_497_obv_diff_at_top_quartile_63d_range_252d_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f22_obvd_497_obv_diff_at_top_quartile_63d_range_252d_d3}, 'f22_obvd_498_obv_diff_at_top_quartile_252d_range_252d_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f22_obvd_498_obv_diff_at_top_quartile_252d_range_252d_d3}, 'f22_obvd_499_obv_diff_at_top_quartile_5y_range_252d_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f22_obvd_499_obv_diff_at_top_quartile_5y_range_252d_d3}, 'f22_obvd_500_obv_diff_at_first_new_252d_high_after_drawdown_d3': {'inputs': ['high', 'close', 'volume'], 'func': f22_obvd_500_obv_diff_at_first_new_252d_high_after_drawdown_d3}, 'f22_obvd_501_obv_diff_within_2pct_of_21d_high_avg_63d_d3': {'inputs': ['high', 'close', 'volume'], 'func': f22_obvd_501_obv_diff_within_2pct_of_21d_high_avg_63d_d3}, 'f22_obvd_502_obv_diff_within_2pct_of_63d_high_avg_252d_d3': {'inputs': ['high', 'close', 'volume'], 'func': f22_obvd_502_obv_diff_within_2pct_of_63d_high_avg_252d_d3}, 'f22_obvd_503_obv_diff_within_2pct_of_252d_high_avg_252d_d3': {'inputs': ['high', 'close', 'volume'], 'func': f22_obvd_503_obv_diff_within_2pct_of_252d_high_avg_252d_d3}, 'f22_obvd_504_obv_diff_within_2pct_of_5y_high_avg_252d_d3': {'inputs': ['high', 'close', 'volume'], 'func': f22_obvd_504_obv_diff_within_2pct_of_5y_high_avg_252d_d3}, 'f22_obvd_505_obv_diff_on_3_consec_new_highs_avg_252d_d3': {'inputs': ['high', 'close', 'volume'], 'func': f22_obvd_505_obv_diff_on_3_consec_new_highs_avg_252d_d3}, 'f22_obvd_506_obv_diff_on_5_consec_new_highs_avg_252d_d3': {'inputs': ['high', 'close', 'volume'], 'func': f22_obvd_506_obv_diff_on_5_consec_new_highs_avg_252d_d3}, 'f22_obvd_507_obv_diff_on_expanding_close_max_avg_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_507_obv_diff_on_expanding_close_max_avg_d3}, 'f22_obvd_508_obv_diff_zscore_at_expanding_close_max_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_508_obv_diff_zscore_at_expanding_close_max_d3}, 'f22_obvd_509_obv_diff_at_top_decile_5y_range_avg_252d_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f22_obvd_509_obv_diff_at_top_decile_5y_range_avg_252d_d3}, 'f22_obvd_510_obv_pct_rank_252d_when_close_top_decile_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_510_obv_pct_rank_252d_when_close_top_decile_d3}, 'f22_obvd_511_obv_diff_per_body_size_ratio_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_511_obv_diff_per_body_size_ratio_d3}, 'f22_obvd_512_obv_diff_per_body_size_zscore_252d_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_512_obv_diff_per_body_size_zscore_252d_d3}, 'f22_obvd_513_obv_diff_per_true_range_ratio_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f22_obvd_513_obv_diff_per_true_range_ratio_d3}, 'f22_obvd_514_obv_diff_per_true_range_zscore_252d_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f22_obvd_514_obv_diff_per_true_range_zscore_252d_d3}, 'f22_obvd_515_obv_diff_per_atr_ratio_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f22_obvd_515_obv_diff_per_atr_ratio_d3}, 'f22_obvd_516_obv_diff_per_atr_zscore_252d_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f22_obvd_516_obv_diff_per_atr_zscore_252d_d3}, 'f22_obvd_517_obv_diff_per_abs_price_change_5d_sum_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_517_obv_diff_per_abs_price_change_5d_sum_d3}, 'f22_obvd_518_obv_diff_per_abs_price_change_21d_sum_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_518_obv_diff_per_abs_price_change_21d_sum_d3}, 'f22_obvd_519_obv_diff_per_hl_spread_ratio_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f22_obvd_519_obv_diff_per_hl_spread_ratio_d3}, 'f22_obvd_520_obv_diff_per_hl_spread_zscore_252d_d3': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f22_obvd_520_obv_diff_per_hl_spread_zscore_252d_d3}, 'f22_obvd_521_obv_roll_spread_proxy_21d_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_521_obv_roll_spread_proxy_21d_d3}, 'f22_obvd_522_obv_roll_spread_proxy_63d_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_522_obv_roll_spread_proxy_63d_d3}, 'f22_obvd_523_obv_diff_per_roll_spread_proxy_21d_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_523_obv_diff_per_roll_spread_proxy_21d_d3}, 'f22_obvd_524_obv_diff_kurtosis_21d_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_524_obv_diff_kurtosis_21d_d3}, 'f22_obvd_525_obv_diff_skewness_21d_d3': {'inputs': ['close', 'volume'], 'func': f22_obvd_525_obv_diff_skewness_21d_d3}}