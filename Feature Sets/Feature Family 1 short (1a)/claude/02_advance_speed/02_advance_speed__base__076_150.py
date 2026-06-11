"""advance_speed base features 076-150 — continuation of 001-075.

Blocks F (MA-time/extension), G (gap-up dynamics), H (vertical thrust),
I (phase analysis), J (persistence/monotonicity of advance). 75 distinct
hypotheses bringing the family total to 150. PIT discipline as in 001-075.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


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


# ============================================================
#                    FEATURES 076-150
# ============================================================

def f02_advs_076_consecutive_days_close_above_sma21(close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak of close > SMA21."""
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    above = (close > sma).astype(int)
    grp = (above == 0).cumsum()
    return above.groupby(grp).cumsum().astype(float)


def f02_advs_077_consecutive_days_close_above_sma63(close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak of close > SMA63."""
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    above = (close > sma).astype(int)
    grp = (above == 0).cumsum()
    return above.groupby(grp).cumsum().astype(float)


def f02_advs_078_consecutive_days_close_above_sma252(close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak of close > SMA252."""
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    above = (close > sma).astype(int)
    grp = (above == 0).cumsum()
    return above.groupby(grp).cumsum().astype(float)


def f02_advs_079_fraction_of_252d_above_sma21(close: pd.Series) -> pd.Series:
    """Share of last 252 bars closing above their then-SMA21."""
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    flag = (close > sma).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).mean()


def f02_advs_080_fraction_of_252d_above_sma63(close: pd.Series) -> pd.Series:
    """Share of last 252 bars closing above their then-SMA63."""
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    flag = (close > sma).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).mean()


def f02_advs_081_fraction_of_252d_above_sma252(close: pd.Series) -> pd.Series:
    """Share of last 252 bars closing above their then-SMA252."""
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (close > sma).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).mean()


def f02_advs_082_uptrend_continuity_score_252d(close: pd.Series) -> pd.Series:
    """Mean of stacked SMA-positivity score (close>sma21 & sma21>sma63 & sma63>sma252) over 252d."""
    s21 = close.rolling(MDAYS, min_periods=WDAYS).mean()
    s63 = close.rolling(QDAYS, min_periods=MDAYS).mean()
    s252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    score = ((close > s21) & (s21 > s63) & (s63 > s252)).astype(float)
    return score.rolling(YDAYS, min_periods=QDAYS).mean()


def f02_advs_083_first_cross_above_sma252_thrust_21d(close: pd.Series) -> pd.Series:
    """(close/sma252-1) computed on bars where close just crossed above SMA252 (cross flag * extension), 21d max."""
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    cross = (close > sma) & (close.shift(1) <= sma.shift(1))
    ext = _safe_div(close, sma) - 1.0
    cross_val = ext.where(cross, np.nan)
    return cross_val.rolling(MDAYS, min_periods=WDAYS).max()


def f02_advs_084_ma_extension_acceleration_21d(close: pd.Series) -> pd.Series:
    """Slope of (close/SMA21 - 1) over last 21 bars — acceleration of short-MA extension."""
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    ext = _safe_div(close, sma) - 1.0
    return _rolling_slope(ext, MDAYS)


def f02_advs_085_ma_extension_acceleration_63d(close: pd.Series) -> pd.Series:
    """Slope of (close/SMA63 - 1) over last 63 bars."""
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    ext = _safe_div(close, sma) - 1.0
    return _rolling_slope(ext, QDAYS)


def f02_advs_086_ma_extension_acceleration_252d(close: pd.Series) -> pd.Series:
    """Slope of (close/SMA252 - 1) over last 252 bars."""
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    ext = _safe_div(close, sma) - 1.0
    return _rolling_slope(ext, YDAYS)


def f02_advs_087_days_since_sma21_last_cross_below(close: pd.Series) -> pd.Series:
    """Bars since the last close-crosses-below-SMA21 event — uptrend age proxy."""
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    cross_dn = (close < sma) & (close.shift(1) >= sma.shift(1))
    cum = cross_dn.cumsum()
    idx_last = pd.Series(np.arange(len(close)), index=close.index).where(cross_dn).ffill()
    pos = pd.Series(np.arange(len(close)), index=close.index)
    return (pos - idx_last).where(cum > 0, np.nan)


def f02_advs_088_count_log_gap_up_gt_1pct_63d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in last 63 where log(open/prior close) > 0.01."""
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return (g > 0.01).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f02_advs_089_count_log_gap_down_lt_neg1pct_63d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in last 63 where log(open/prior close) < -0.01."""
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return (g < -0.01).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f02_advs_090_mean_log_gap_up_magnitude_63d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Average size of positive overnight log-gaps over 63 bars."""
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return g.where(g > 0).rolling(QDAYS, min_periods=MDAYS).mean()


def f02_advs_091_mean_log_gap_down_magnitude_63d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Average size of negative overnight log-gaps over 63 bars."""
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return g.where(g < 0).rolling(QDAYS, min_periods=MDAYS).mean()


def f02_advs_092_cumulative_log_gap_up_63d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of positive overnight log-gaps over 63 bars."""
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return g.clip(lower=0).rolling(QDAYS, min_periods=MDAYS).sum()


def f02_advs_093_cumulative_log_gap_down_63d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of negative overnight log-gaps over 63 bars."""
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return g.clip(upper=0).rolling(QDAYS, min_periods=MDAYS).sum()


def f02_advs_094_share_of_63d_advance_from_gaps(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of overnight log-gaps over 63d / total 63d log return — share from gaps."""
    g = _safe_log(open_) - _safe_log(close.shift(1))
    cum_gap = g.rolling(QDAYS, min_periods=MDAYS).sum()
    tot = _safe_log(close).diff(QDAYS)
    return _safe_div(cum_gap, tot)


def f02_advs_095_count_runaway_gap_up_252d(open_: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars in 252 with positive gap AND close above prior bar's high — runaway gaps."""
    gap_up = open_ > close.shift(1)
    above = close > high.shift(1)
    return (gap_up & above).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f02_advs_096_count_exhaustion_gap_up_252d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in 252 with positive gap AND close < open — exhaustion gaps."""
    gap_up = open_ > close.shift(1)
    bear_body = close < open_
    return (gap_up & bear_body).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f02_advs_097_max_log_gap_up_252d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Largest positive overnight log-gap over the last 252 bars."""
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return g.rolling(YDAYS, min_periods=QDAYS).max()


def f02_advs_098_overnight_log_return_mean_21d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Mean overnight log return (open vs prior close) over 21 bars."""
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return g.rolling(MDAYS, min_periods=WDAYS).mean()


def f02_advs_099_overnight_log_return_zscore_252d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Overnight log return z-scored vs 252d distribution."""
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return _rolling_zscore(g, YDAYS)


def f02_advs_100_overnight_vs_intraday_log_corr_63d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d corr(overnight log return, intraday close-vs-open log return)."""
    overnight = _safe_log(open_) - _safe_log(close.shift(1))
    intraday = _safe_log(close) - _safe_log(open_)
    return overnight.rolling(QDAYS, min_periods=MDAYS).corr(intraday)


def f02_advs_101_fraction_positive_overnight_252d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Share of last 252 bars with positive overnight log return."""
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return (g > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f02_advs_102_overnight_return_kurt_252d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Excess kurtosis of overnight log returns over 252d."""
    g = _safe_log(open_) - _safe_log(close.shift(1))
    return g.rolling(YDAYS, min_periods=QDAYS).kurt()


def f02_advs_103_log_return_5d_pct_rank_in_252d(close: pd.Series) -> pd.Series:
    """5-day log return percentile-ranked in its 252d distribution (terminal-thrust ranking)."""
    r = _safe_log(close).diff(WDAYS)
    return r.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f02_advs_104_log_return_10d_pct_rank_in_252d(close: pd.Series) -> pd.Series:
    """10-day log return percentile-ranked in its 252d distribution."""
    r = _safe_log(close).diff(10)
    return r.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f02_advs_105_log_return_21d_pct_rank_in_1260d(close: pd.Series) -> pd.Series:
    """21-day log return percentile-ranked vs the 5y distribution — multi-year context."""
    r = _safe_log(close).diff(MDAYS)
    return r.rolling(1260, min_periods=YDAYS).rank(pct=True)


def f02_advs_106_vertical_move_zscore_5d(close: pd.Series) -> pd.Series:
    """5-day log return divided by (21d-stdev * sqrt(5)) — scaled terminal thrust."""
    r1 = _safe_log(close).diff()
    sd = r1.rolling(MDAYS, min_periods=WDAYS).std()
    r5 = _safe_log(close).diff(WDAYS)
    return _safe_div(r5, sd * np.sqrt(WDAYS))


def f02_advs_107_vertical_move_zscore_10d(close: pd.Series) -> pd.Series:
    """10-day log return divided by (21d-stdev * sqrt(10))."""
    r1 = _safe_log(close).diff()
    sd = r1.rolling(MDAYS, min_periods=WDAYS).std()
    r10 = _safe_log(close).diff(10)
    return _safe_div(r10, sd * np.sqrt(10))


def f02_advs_108_vertical_move_zscore_21d(close: pd.Series) -> pd.Series:
    """21-day log return divided by (21d-stdev * sqrt(21))."""
    r1 = _safe_log(close).diff()
    sd = r1.rolling(MDAYS, min_periods=WDAYS).std()
    r21 = _safe_log(close).diff(MDAYS)
    return _safe_div(r21, sd * np.sqrt(MDAYS))


def f02_advs_109_vertical_move_atr_units_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - close.shift(5)) / ATR21 — terminal 5d move in ATR units."""
    atr = _atr(high, low, close, MDAYS)
    return (close - close.shift(WDAYS)) / atr.replace(0, np.nan)


def f02_advs_110_vertical_move_atr_units_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - close.shift(21)) / ATR21 — monthly thrust in ATR units."""
    atr = _atr(high, low, close, MDAYS)
    return (close - close.shift(MDAYS)) / atr.replace(0, np.nan)


def f02_advs_111_count_5d_vertical_z_gt_2_252d(close: pd.Series) -> pd.Series:
    """Days in 252 where the 5d-return z-score > 2 — frequency of vertical 5d thrusts."""
    r1 = _safe_log(close).diff()
    sd = r1.rolling(MDAYS, min_periods=WDAYS).std()
    z5 = _safe_div(_safe_log(close).diff(WDAYS), sd * np.sqrt(WDAYS))
    return (z5 > 2.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f02_advs_112_count_21d_vertical_z_gt_2_252d(close: pd.Series) -> pd.Series:
    """Days in 252 where 21d-return z > 2."""
    r1 = _safe_log(close).diff()
    sd = r1.rolling(MDAYS, min_periods=WDAYS).std()
    z21 = _safe_div(_safe_log(close).diff(MDAYS), sd * np.sqrt(MDAYS))
    return (z21 > 2.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f02_advs_113_max_5d_vertical_z_252d(close: pd.Series) -> pd.Series:
    """Max 5d-return z-score observed inside last 252 bars."""
    r1 = _safe_log(close).diff()
    sd = r1.rolling(MDAYS, min_periods=WDAYS).std()
    z5 = _safe_div(_safe_log(close).diff(WDAYS), sd * np.sqrt(WDAYS))
    return z5.rolling(YDAYS, min_periods=QDAYS).max()


def f02_advs_114_max_21d_vertical_z_252d(close: pd.Series) -> pd.Series:
    """Max 21d-return z-score observed inside last 252 bars."""
    r1 = _safe_log(close).diff()
    sd = r1.rolling(MDAYS, min_periods=WDAYS).std()
    z21 = _safe_div(_safe_log(close).diff(MDAYS), sd * np.sqrt(MDAYS))
    return z21.rolling(YDAYS, min_periods=QDAYS).max()


def f02_advs_115_proximity_to_max_5d_z_252d(close: pd.Series) -> pd.Series:
    """Current 5d-z divided by 252d max 5d-z — proximity to extreme thrust."""
    r1 = _safe_log(close).diff()
    sd = r1.rolling(MDAYS, min_periods=WDAYS).std()
    z5 = _safe_div(_safe_log(close).diff(WDAYS), sd * np.sqrt(WDAYS))
    mx = z5.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(z5, mx)


def f02_advs_116_proximity_to_max_21d_z_252d(close: pd.Series) -> pd.Series:
    """Current 21d-z divided by 252d max 21d-z."""
    r1 = _safe_log(close).diff()
    sd = r1.rolling(MDAYS, min_periods=WDAYS).std()
    z21 = _safe_div(_safe_log(close).diff(MDAYS), sd * np.sqrt(MDAYS))
    mx = z21.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(z21, mx)


def f02_advs_117_pct_of_252d_within_top_decile_5d_returns(close: pd.Series) -> pd.Series:
    """Share of last 252 bars whose 5d return sits in their 252d top-decile (rank>=0.9)."""
    r5 = _safe_log(close).diff(WDAYS)
    rk = r5.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    return (rk >= 0.9).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f02_advs_118_price_to_252d_low_ratio_minus_1(close: pd.Series, low: pd.Series) -> pd.Series:
    """close / 252d-min(low) - 1 — straightforward 1y advance multiple."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(close, rmin) - 1.0


def f02_advs_119_price_to_63d_low_ratio_minus_1(close: pd.Series, low: pd.Series) -> pd.Series:
    """close / 63d-min(low) - 1 — quarterly advance multiple."""
    rmin = low.rolling(QDAYS, min_periods=MDAYS).min()
    return _safe_div(close, rmin) - 1.0


def f02_advs_120_price_to_1260d_low_ratio_minus_1(close: pd.Series, low: pd.Series) -> pd.Series:
    """close / 1260d-min(low) - 1 — secular advance multiple."""
    rmin = low.rolling(1260, min_periods=YDAYS).min()
    return _safe_div(close, rmin) - 1.0


def f02_advs_121_log_return_first_third_252d(close: pd.Series) -> pd.Series:
    """Log return over the FIRST third of the 252d window (lag 252 to lag 168)."""
    lp = _safe_log(close)
    return lp.shift(YDAYS - 252 // 3) - lp.shift(YDAYS)


def f02_advs_122_log_return_middle_third_252d(close: pd.Series) -> pd.Series:
    """Log return over the MIDDLE third of the 252d window (lag 168 to lag 84)."""
    lp = _safe_log(close)
    return lp.shift(YDAYS - 2 * (252 // 3)) - lp.shift(YDAYS - 252 // 3)


def f02_advs_123_log_return_last_third_252d(close: pd.Series) -> pd.Series:
    """Log return over the LAST third of the 252d window (lag 84 to now)."""
    lp = _safe_log(close)
    return lp - lp.shift(YDAYS - 2 * (252 // 3))


def f02_advs_124_ratio_last_third_to_first_third_252d(close: pd.Series) -> pd.Series:
    """Last-third log return divided by first-third — terminal vs initial pace."""
    lp = _safe_log(close)
    third = 252 // 3
    last = lp - lp.shift(YDAYS - 2 * third)
    first = lp.shift(YDAYS - third) - lp.shift(YDAYS)
    return _safe_div(last, first)


def f02_advs_125_ratio_last_third_to_middle_third_252d(close: pd.Series) -> pd.Series:
    """Last-third log return divided by middle-third — late acceleration."""
    lp = _safe_log(close)
    third = 252 // 3
    last = lp - lp.shift(YDAYS - 2 * third)
    mid = lp.shift(YDAYS - 2 * third) - lp.shift(YDAYS - third)
    return _safe_div(last, mid)


def f02_advs_126_days_to_traverse_50pct_252d_range(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars between when close first crossed 50% of 252d range and now — half-range advance time."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    pos = (close - rmin) / rng
    def _days(w):
        if np.isnan(w).any():
            return np.nan
        idx = np.where(w >= 0.5)[0]
        if len(idx) == 0:
            return float(len(w))
        return float((len(w) - 1) - idx[0])
    return pos.rolling(YDAYS, min_periods=QDAYS).apply(_days, raw=True)


def f02_advs_127_days_to_traverse_75pct_252d_range(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars between when close first crossed 75% of 252d range and now."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    pos = (close - rmin) / rng
    def _days(w):
        if np.isnan(w).any():
            return np.nan
        idx = np.where(w >= 0.75)[0]
        if len(idx) == 0:
            return float(len(w))
        return float((len(w) - 1) - idx[0])
    return pos.rolling(YDAYS, min_periods=QDAYS).apply(_days, raw=True)


def f02_advs_128_fraction_252d_log_gain_in_last_5d(close: pd.Series) -> pd.Series:
    """5d log return divided by 252d log return — concentration of gain in last week."""
    lp = _safe_log(close)
    r5 = lp - lp.shift(WDAYS)
    r252 = lp - lp.shift(YDAYS)
    return _safe_div(r5, r252)


def f02_advs_129_fraction_252d_log_gain_in_last_21d(close: pd.Series) -> pd.Series:
    """21d log return divided by 252d log return — concentration in last month."""
    lp = _safe_log(close)
    r21 = lp - lp.shift(MDAYS)
    r252 = lp - lp.shift(YDAYS)
    return _safe_div(r21, r252)


def f02_advs_130_fraction_252d_log_gain_in_last_63d(close: pd.Series) -> pd.Series:
    """63d log return divided by 252d log return — concentration in last quarter."""
    lp = _safe_log(close)
    r63 = lp - lp.shift(QDAYS)
    r252 = lp - lp.shift(YDAYS)
    return _safe_div(r63, r252)


def f02_advs_131_last_quintile_speed_zscore_in_252d(close: pd.Series) -> pd.Series:
    """Mean daily log return over last 50d (1/5 of 252) z-scored vs 252d distribution."""
    r = _safe_log(close).diff()
    last_q = r.rolling(50, min_periods=10).mean()
    return _rolling_zscore(last_q, YDAYS)


def f02_advs_132_first_quintile_speed_zscore_in_252d(close: pd.Series) -> pd.Series:
    """Mean daily log return over the FIRST 50d of the 252d window, z-scored vs current 252d."""
    r = _safe_log(close).diff()
    first_q_mean = r.rolling(50, min_periods=10).mean().shift(YDAYS - 50)
    return _rolling_zscore(first_q_mean, YDAYS)


def f02_advs_133_non_decreasing_close_run_max_252d(close: pd.Series) -> pd.Series:
    """Longest streak of close >= prior close inside last 252 bars."""
    nd = (close >= close.shift(1)).astype(int)
    grp = (nd == 0).cumsum()
    streak = nd.groupby(grp).cumsum()
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f02_advs_134_fraction_higher_highs_252d(high: pd.Series) -> pd.Series:
    """Share of last 252 bars whose high > prior bar's high."""
    hh = (high > high.shift(1)).astype(float)
    return hh.rolling(YDAYS, min_periods=QDAYS).mean()


def f02_advs_135_fraction_higher_lows_252d(low: pd.Series) -> pd.Series:
    """Share of last 252 bars whose low > prior bar's low."""
    hl = (low > low.shift(1)).astype(float)
    return hl.rolling(YDAYS, min_periods=QDAYS).mean()


def f02_advs_136_higher_hi_hi_lo_lo_streak_max_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Longest streak of (higher high AND higher low) inside last 252 bars."""
    flag = ((high > high.shift(1)) & (low > low.shift(1))).astype(int)
    grp = (flag == 0).cumsum()
    streak = flag.groupby(grp).cumsum()
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f02_advs_137_count_distinct_uptrend_legs_252d(close: pd.Series) -> pd.Series:
    """Count of new running-max events inside last 252 bars — leg count."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    new_max = (close >= rmax).astype(float)
    return new_max.rolling(YDAYS, min_periods=QDAYS).sum()


def f02_advs_138_mean_uptrend_leg_log_size_252d(close: pd.Series) -> pd.Series:
    """Mean log-size of segments between consecutive 252d running-max touches."""
    lp = _safe_log(close)
    rmax_lp = lp.rolling(YDAYS, min_periods=QDAYS).max()
    is_peak = (lp >= rmax_lp).astype(int)
    def _mean_leg(w):
        if np.isnan(w).any() or len(w) < 2:
            return np.nan
        peaks = np.where(w > 0.5)[0]
        if len(peaks) < 2:
            return np.nan
        return float(np.diff(peaks).mean())
    return is_peak.rolling(YDAYS, min_periods=QDAYS).apply(_mean_leg, raw=True)


def f02_advs_139_max_uptrend_leg_log_size_252d(close: pd.Series) -> pd.Series:
    """Max bar-gap between consecutive 252d running-max touches inside last 252 bars."""
    lp = _safe_log(close)
    rmax_lp = lp.rolling(YDAYS, min_periods=QDAYS).max()
    is_peak = (lp >= rmax_lp).astype(int)
    def _max_gap(w):
        if np.isnan(w).any():
            return np.nan
        peaks = np.where(w > 0.5)[0]
        if len(peaks) < 2:
            return np.nan
        return float(np.diff(peaks).max())
    return is_peak.rolling(YDAYS, min_periods=QDAYS).apply(_max_gap, raw=True)


def f02_advs_140_mean_pullback_depth_during_advance_252d(close: pd.Series) -> pd.Series:
    """Mean of running drawdown (close vs running 252d max close) over 252d."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(close, rmax) - 1.0
    return dd.rolling(YDAYS, min_periods=QDAYS).mean()


def f02_advs_141_max_pullback_depth_during_advance_252d(close: pd.Series) -> pd.Series:
    """Deepest running drawdown from 252d max close, observed inside last 252 bars."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(close, rmax) - 1.0
    return dd.rolling(YDAYS, min_periods=QDAYS).min()


def f02_advs_142_count_pullbacks_gt_5pct_252d(close: pd.Series) -> pd.Series:
    """Days in 252 where the running drawdown from 252d max close exceeded 5%."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(close, rmax) - 1.0
    return (dd < -0.05).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f02_advs_143_mean_pullback_duration_252d(close: pd.Series) -> pd.Series:
    """Mean length of consecutive drawdown spells (dd < 0) over last 252 bars."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(close, rmax) - 1.0
    flag = (dd < 0).astype(int)
    def _mean_run(w):
        if np.isnan(w).any():
            return np.nan
        runs = []
        c = 0
        for v in w:
            if v > 0.5:
                c += 1
            else:
                if c > 0:
                    runs.append(c)
                c = 0
        if c > 0:
            runs.append(c)
        return float(np.mean(runs)) if runs else 0.0
    return flag.rolling(YDAYS, min_periods=QDAYS).apply(_mean_run, raw=True)


def f02_advs_144_straight_line_advance_r2_252d(close: pd.Series) -> pd.Series:
    """R² of linear fit on close over 252 bars — how straight is the advance line."""
    def _r2(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        ss_tot = ((w - w.mean()) ** 2).sum()
        if ss_tot == 0:
            return np.nan
        c1, c0 = np.polyfit(x, w, 1)
        pred = c1 * x + c0
        return 1.0 - ((w - pred) ** 2).sum() / ss_tot
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_r2, raw=True)


def f02_advs_145_cumulative_drawdown_share_252d(close: pd.Series) -> pd.Series:
    """Mean |running drawdown| over 252d — area of pullbacks vs straight line."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = (_safe_div(close, rmax) - 1.0).abs()
    return dd.rolling(YDAYS, min_periods=QDAYS).mean()


def f02_advs_146_clean_advance_index_252d(close: pd.Series) -> pd.Series:
    """R² of linear fit divided by (1 + mean abs drawdown) — composite cleanness score."""
    def _r2(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        ss_tot = ((w - w.mean()) ** 2).sum()
        if ss_tot == 0:
            return np.nan
        c1, c0 = np.polyfit(x, w, 1)
        pred = c1 * x + c0
        return 1.0 - ((w - pred) ** 2).sum() / ss_tot
    r2 = close.rolling(YDAYS, min_periods=QDAYS).apply(_r2, raw=True)
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd_share = (_safe_div(close, rmax) - 1.0).abs().rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(r2, 1.0 + dd_share)


def f02_advs_147_max_uninterrupted_advance_streak_252d(close: pd.Series) -> pd.Series:
    """Longest streak with close > 252d running max as of bar (touched-or-broke streak)."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    touch = (close >= rmax).astype(int)
    grp = (touch == 0).cumsum()
    streak = touch.groupby(grp).cumsum()
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f02_advs_148_count_lower_lows_during_252d_uptrend(low: pd.Series, close: pd.Series) -> pd.Series:
    """Days in 252 where low < prior bar's low AND close > 252d-SMA — uptrend cracks."""
    ll = low < low.shift(1)
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    in_uptrend = close > sma
    return (ll & in_uptrend).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f02_advs_149_velocity_consistency_score_252d(close: pd.Series) -> pd.Series:
    """Mean / std of daily log returns over 252d — Sharpe-like consistency score."""
    r = _safe_log(close).diff()
    m = r.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(m, sd)


def f02_advs_150_terminal_advance_completeness_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Position-in-252d-range × z-score of 21d return — proximity-to-top × terminal thrust."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    pos = (close - rmin) / rng
    r21 = _safe_log(close).diff(MDAYS)
    z = _rolling_zscore(r21, YDAYS)
    return pos * z


# ============================================================
#                        REGISTRY
# ============================================================

ADVANCE_SPEED_BASE_REGISTRY_076_150 = {
    "f02_advs_076_consecutive_days_close_above_sma21": {"inputs": ["close"], "func": f02_advs_076_consecutive_days_close_above_sma21},
    "f02_advs_077_consecutive_days_close_above_sma63": {"inputs": ["close"], "func": f02_advs_077_consecutive_days_close_above_sma63},
    "f02_advs_078_consecutive_days_close_above_sma252": {"inputs": ["close"], "func": f02_advs_078_consecutive_days_close_above_sma252},
    "f02_advs_079_fraction_of_252d_above_sma21": {"inputs": ["close"], "func": f02_advs_079_fraction_of_252d_above_sma21},
    "f02_advs_080_fraction_of_252d_above_sma63": {"inputs": ["close"], "func": f02_advs_080_fraction_of_252d_above_sma63},
    "f02_advs_081_fraction_of_252d_above_sma252": {"inputs": ["close"], "func": f02_advs_081_fraction_of_252d_above_sma252},
    "f02_advs_082_uptrend_continuity_score_252d": {"inputs": ["close"], "func": f02_advs_082_uptrend_continuity_score_252d},
    "f02_advs_083_first_cross_above_sma252_thrust_21d": {"inputs": ["close"], "func": f02_advs_083_first_cross_above_sma252_thrust_21d},
    "f02_advs_084_ma_extension_acceleration_21d": {"inputs": ["close"], "func": f02_advs_084_ma_extension_acceleration_21d},
    "f02_advs_085_ma_extension_acceleration_63d": {"inputs": ["close"], "func": f02_advs_085_ma_extension_acceleration_63d},
    "f02_advs_086_ma_extension_acceleration_252d": {"inputs": ["close"], "func": f02_advs_086_ma_extension_acceleration_252d},
    "f02_advs_087_days_since_sma21_last_cross_below": {"inputs": ["close"], "func": f02_advs_087_days_since_sma21_last_cross_below},
    "f02_advs_088_count_log_gap_up_gt_1pct_63d": {"inputs": ["open", "close"], "func": f02_advs_088_count_log_gap_up_gt_1pct_63d},
    "f02_advs_089_count_log_gap_down_lt_neg1pct_63d": {"inputs": ["open", "close"], "func": f02_advs_089_count_log_gap_down_lt_neg1pct_63d},
    "f02_advs_090_mean_log_gap_up_magnitude_63d": {"inputs": ["open", "close"], "func": f02_advs_090_mean_log_gap_up_magnitude_63d},
    "f02_advs_091_mean_log_gap_down_magnitude_63d": {"inputs": ["open", "close"], "func": f02_advs_091_mean_log_gap_down_magnitude_63d},
    "f02_advs_092_cumulative_log_gap_up_63d": {"inputs": ["open", "close"], "func": f02_advs_092_cumulative_log_gap_up_63d},
    "f02_advs_093_cumulative_log_gap_down_63d": {"inputs": ["open", "close"], "func": f02_advs_093_cumulative_log_gap_down_63d},
    "f02_advs_094_share_of_63d_advance_from_gaps": {"inputs": ["open", "close"], "func": f02_advs_094_share_of_63d_advance_from_gaps},
    "f02_advs_095_count_runaway_gap_up_252d": {"inputs": ["open", "close", "high"], "func": f02_advs_095_count_runaway_gap_up_252d},
    "f02_advs_096_count_exhaustion_gap_up_252d": {"inputs": ["open", "close"], "func": f02_advs_096_count_exhaustion_gap_up_252d},
    "f02_advs_097_max_log_gap_up_252d": {"inputs": ["open", "close"], "func": f02_advs_097_max_log_gap_up_252d},
    "f02_advs_098_overnight_log_return_mean_21d": {"inputs": ["open", "close"], "func": f02_advs_098_overnight_log_return_mean_21d},
    "f02_advs_099_overnight_log_return_zscore_252d": {"inputs": ["open", "close"], "func": f02_advs_099_overnight_log_return_zscore_252d},
    "f02_advs_100_overnight_vs_intraday_log_corr_63d": {"inputs": ["open", "close"], "func": f02_advs_100_overnight_vs_intraday_log_corr_63d},
    "f02_advs_101_fraction_positive_overnight_252d": {"inputs": ["open", "close"], "func": f02_advs_101_fraction_positive_overnight_252d},
    "f02_advs_102_overnight_return_kurt_252d": {"inputs": ["open", "close"], "func": f02_advs_102_overnight_return_kurt_252d},
    "f02_advs_103_log_return_5d_pct_rank_in_252d": {"inputs": ["close"], "func": f02_advs_103_log_return_5d_pct_rank_in_252d},
    "f02_advs_104_log_return_10d_pct_rank_in_252d": {"inputs": ["close"], "func": f02_advs_104_log_return_10d_pct_rank_in_252d},
    "f02_advs_105_log_return_21d_pct_rank_in_1260d": {"inputs": ["close"], "func": f02_advs_105_log_return_21d_pct_rank_in_1260d},
    "f02_advs_106_vertical_move_zscore_5d": {"inputs": ["close"], "func": f02_advs_106_vertical_move_zscore_5d},
    "f02_advs_107_vertical_move_zscore_10d": {"inputs": ["close"], "func": f02_advs_107_vertical_move_zscore_10d},
    "f02_advs_108_vertical_move_zscore_21d": {"inputs": ["close"], "func": f02_advs_108_vertical_move_zscore_21d},
    "f02_advs_109_vertical_move_atr_units_5d": {"inputs": ["close", "high", "low"], "func": f02_advs_109_vertical_move_atr_units_5d},
    "f02_advs_110_vertical_move_atr_units_21d": {"inputs": ["close", "high", "low"], "func": f02_advs_110_vertical_move_atr_units_21d},
    "f02_advs_111_count_5d_vertical_z_gt_2_252d": {"inputs": ["close"], "func": f02_advs_111_count_5d_vertical_z_gt_2_252d},
    "f02_advs_112_count_21d_vertical_z_gt_2_252d": {"inputs": ["close"], "func": f02_advs_112_count_21d_vertical_z_gt_2_252d},
    "f02_advs_113_max_5d_vertical_z_252d": {"inputs": ["close"], "func": f02_advs_113_max_5d_vertical_z_252d},
    "f02_advs_114_max_21d_vertical_z_252d": {"inputs": ["close"], "func": f02_advs_114_max_21d_vertical_z_252d},
    "f02_advs_115_proximity_to_max_5d_z_252d": {"inputs": ["close"], "func": f02_advs_115_proximity_to_max_5d_z_252d},
    "f02_advs_116_proximity_to_max_21d_z_252d": {"inputs": ["close"], "func": f02_advs_116_proximity_to_max_21d_z_252d},
    "f02_advs_117_pct_of_252d_within_top_decile_5d_returns": {"inputs": ["close"], "func": f02_advs_117_pct_of_252d_within_top_decile_5d_returns},
    "f02_advs_118_price_to_252d_low_ratio_minus_1": {"inputs": ["close", "low"], "func": f02_advs_118_price_to_252d_low_ratio_minus_1},
    "f02_advs_119_price_to_63d_low_ratio_minus_1": {"inputs": ["close", "low"], "func": f02_advs_119_price_to_63d_low_ratio_minus_1},
    "f02_advs_120_price_to_1260d_low_ratio_minus_1": {"inputs": ["close", "low"], "func": f02_advs_120_price_to_1260d_low_ratio_minus_1},
    "f02_advs_121_log_return_first_third_252d": {"inputs": ["close"], "func": f02_advs_121_log_return_first_third_252d},
    "f02_advs_122_log_return_middle_third_252d": {"inputs": ["close"], "func": f02_advs_122_log_return_middle_third_252d},
    "f02_advs_123_log_return_last_third_252d": {"inputs": ["close"], "func": f02_advs_123_log_return_last_third_252d},
    "f02_advs_124_ratio_last_third_to_first_third_252d": {"inputs": ["close"], "func": f02_advs_124_ratio_last_third_to_first_third_252d},
    "f02_advs_125_ratio_last_third_to_middle_third_252d": {"inputs": ["close"], "func": f02_advs_125_ratio_last_third_to_middle_third_252d},
    "f02_advs_126_days_to_traverse_50pct_252d_range": {"inputs": ["close", "high", "low"], "func": f02_advs_126_days_to_traverse_50pct_252d_range},
    "f02_advs_127_days_to_traverse_75pct_252d_range": {"inputs": ["close", "high", "low"], "func": f02_advs_127_days_to_traverse_75pct_252d_range},
    "f02_advs_128_fraction_252d_log_gain_in_last_5d": {"inputs": ["close"], "func": f02_advs_128_fraction_252d_log_gain_in_last_5d},
    "f02_advs_129_fraction_252d_log_gain_in_last_21d": {"inputs": ["close"], "func": f02_advs_129_fraction_252d_log_gain_in_last_21d},
    "f02_advs_130_fraction_252d_log_gain_in_last_63d": {"inputs": ["close"], "func": f02_advs_130_fraction_252d_log_gain_in_last_63d},
    "f02_advs_131_last_quintile_speed_zscore_in_252d": {"inputs": ["close"], "func": f02_advs_131_last_quintile_speed_zscore_in_252d},
    "f02_advs_132_first_quintile_speed_zscore_in_252d": {"inputs": ["close"], "func": f02_advs_132_first_quintile_speed_zscore_in_252d},
    "f02_advs_133_non_decreasing_close_run_max_252d": {"inputs": ["close"], "func": f02_advs_133_non_decreasing_close_run_max_252d},
    "f02_advs_134_fraction_higher_highs_252d": {"inputs": ["high"], "func": f02_advs_134_fraction_higher_highs_252d},
    "f02_advs_135_fraction_higher_lows_252d": {"inputs": ["low"], "func": f02_advs_135_fraction_higher_lows_252d},
    "f02_advs_136_higher_hi_hi_lo_lo_streak_max_252d": {"inputs": ["high", "low"], "func": f02_advs_136_higher_hi_hi_lo_lo_streak_max_252d},
    "f02_advs_137_count_distinct_uptrend_legs_252d": {"inputs": ["close"], "func": f02_advs_137_count_distinct_uptrend_legs_252d},
    "f02_advs_138_mean_uptrend_leg_log_size_252d": {"inputs": ["close"], "func": f02_advs_138_mean_uptrend_leg_log_size_252d},
    "f02_advs_139_max_uptrend_leg_log_size_252d": {"inputs": ["close"], "func": f02_advs_139_max_uptrend_leg_log_size_252d},
    "f02_advs_140_mean_pullback_depth_during_advance_252d": {"inputs": ["close"], "func": f02_advs_140_mean_pullback_depth_during_advance_252d},
    "f02_advs_141_max_pullback_depth_during_advance_252d": {"inputs": ["close"], "func": f02_advs_141_max_pullback_depth_during_advance_252d},
    "f02_advs_142_count_pullbacks_gt_5pct_252d": {"inputs": ["close"], "func": f02_advs_142_count_pullbacks_gt_5pct_252d},
    "f02_advs_143_mean_pullback_duration_252d": {"inputs": ["close"], "func": f02_advs_143_mean_pullback_duration_252d},
    "f02_advs_144_straight_line_advance_r2_252d": {"inputs": ["close"], "func": f02_advs_144_straight_line_advance_r2_252d},
    "f02_advs_145_cumulative_drawdown_share_252d": {"inputs": ["close"], "func": f02_advs_145_cumulative_drawdown_share_252d},
    "f02_advs_146_clean_advance_index_252d": {"inputs": ["close"], "func": f02_advs_146_clean_advance_index_252d},
    "f02_advs_147_max_uninterrupted_advance_streak_252d": {"inputs": ["close"], "func": f02_advs_147_max_uninterrupted_advance_streak_252d},
    "f02_advs_148_count_lower_lows_during_252d_uptrend": {"inputs": ["low", "close"], "func": f02_advs_148_count_lower_lows_during_252d_uptrend},
    "f02_advs_149_velocity_consistency_score_252d": {"inputs": ["close"], "func": f02_advs_149_velocity_consistency_score_252d},
    "f02_advs_150_terminal_advance_completeness_252d": {"inputs": ["close", "high", "low"], "func": f02_advs_150_terminal_advance_completeness_252d},
}
