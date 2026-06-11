"""advance_magnitude_duration base 001-075 — Pipeline 1a-inverse short-side blowup family.

Hypothesis: HOW BIG the advance is and HOW LONG it has lasted (and their
interaction) predict whether the eventual peak will lead to a stuck -80%
drawdown. Distinct from advance_speed which measures velocity character.
75 distinct hypotheses (continued in __base__076_150.py). SEP-only OHLCV.
PIT-clean: right-anchored rolling, explicit min_periods, no .shift(-N).
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
#                    FEATURES 001-075
# ============================================================

def f03_amad_001_log_advance_magnitude_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Log(close / 252d-min(low)) — raw 1y advance magnitude."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_log(close) - _safe_log(rmin)


def f03_amad_002_log_advance_magnitude_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Log(close / 63d-min(low)) — quarterly advance magnitude."""
    rmin = low.rolling(QDAYS, min_periods=MDAYS).min()
    return _safe_log(close) - _safe_log(rmin)


def f03_amad_003_log_advance_magnitude_1260d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Log(close / 1260d-min(low)) — 5y advance magnitude."""
    rmin = low.rolling(1260, min_periods=YDAYS).min()
    return _safe_log(close) - _safe_log(rmin)


def f03_amad_004_log_advance_magnitude_2520d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Log(close / 2520d-min(low)) — 10y secular advance magnitude."""
    rmin = low.rolling(2520, min_periods=YDAYS * 2).min()
    return _safe_log(close) - _safe_log(rmin)


def f03_amad_005_log_advance_close_anchored_1260d(close: pd.Series) -> pd.Series:
    """Log(close / 1260d-min(close)) — close-anchored 5y advance (vs f03_amad_003 which uses low)."""
    rmin = close.rolling(1260, min_periods=YDAYS).min()
    return _safe_log(close) - _safe_log(rmin)


def f03_amad_006_log_high_above_252d_low(high: pd.Series, low: pd.Series) -> pd.Series:
    """Log(252d-max(high) / 252d-min(low)) — peak-to-trough log span over 252 bars."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_log(rmax) - _safe_log(rmin)


def f03_amad_007_log_high_above_1260d_low(high: pd.Series, low: pd.Series) -> pd.Series:
    """Log(252d-max(high) / 1260d-min(low)) — annual peak vs secular trough."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(1260, min_periods=YDAYS).min()
    return _safe_log(rmax) - _safe_log(rmin)


def f03_amad_008_multiplicative_advance_pct_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """(close / 252d-min(low) - 1) * 100 — pct advance from annual trough."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    return (_safe_div(close, rmin) - 1.0) * 100.0


def f03_amad_009_log_high_now_minus_log_low_then_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Log(high) - log(252d-min(low)) — current high's log distance above 252d trough low."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_log(high) - _safe_log(rmin)


def f03_amad_010_log_high_now_minus_log_low_then_1260d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Log(high) - log(1260d-min(low)) — current high's log distance above 5y trough low."""
    rmin = low.rolling(1260, min_periods=YDAYS).min()
    return _safe_log(high) - _safe_log(rmin)


def f03_amad_011_cumulative_positive_log_return_252d(close: pd.Series) -> pd.Series:
    """Sum of positive daily log returns over 252 bars — additive lifetime gain."""
    r = _safe_log(close).diff()
    return r.clip(lower=0).rolling(YDAYS, min_periods=QDAYS).sum()


def f03_amad_012_secular_advance_log_zscore_in_2520d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of log(close/252d-low) vs its own 2520d (10y) distribution."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    adv = _safe_log(close) - _safe_log(rmin)
    return _rolling_zscore(adv, 2520, min_periods=YDAYS * 2)


def f03_amad_013_anchored_vwap_advance_log_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log(close / 252d-VWAP) — advance vs volume-weighted base."""
    pv = (close * volume).rolling(YDAYS, min_periods=QDAYS).sum()
    vv = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_log(close) - _safe_log(_safe_div(pv, vv))


def f03_amad_014_max_running_total_log_return_252d(close: pd.Series) -> pd.Series:
    """Max value reached by the running 252d trailing log return inside the last 252 bars."""
    r252 = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return r252.rolling(YDAYS, min_periods=QDAYS).max()


def f03_amad_015_net_log_return_252d(close: pd.Series) -> pd.Series:
    """Net 252d trailing log return on close (current vs 252d-ago close)."""
    return _safe_log(close) - _safe_log(close.shift(YDAYS))


def f03_amad_016_days_above_sma252_in_252d(close: pd.Series) -> pd.Series:
    """Count of bars in last 252 where close > SMA252."""
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    return (close > sma).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f03_amad_017_days_above_50pct_of_252d_range(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars in last 252 where close sits in the upper 50% of 252d range."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    pos = (close - rmin) / rng
    return (pos > 0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f03_amad_018_days_in_HH_HL_state_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars in 252 with both higher high AND higher low — classical uptrend."""
    flag = ((high > high.shift(1)) & (low > low.shift(1))).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f03_amad_019_days_within_5pct_of_252d_high(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of bars in 252 where close >= 0.95 * 252d-max(high)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    flag = (close >= 0.95 * rmax).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f03_amad_020_days_within_10pct_of_252d_high(close: pd.Series, high: pd.Series) -> pd.Series:
    """Count of bars in 252 where close >= 0.90 * 252d-max(high)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    flag = (close >= 0.90 * rmax).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f03_amad_021_longest_streak_close_above_sma63_252d(close: pd.Series) -> pd.Series:
    """Longest consecutive-bar streak of close > SMA63 inside last 252 bars."""
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    flag = (close > sma).astype(int)
    grp = (flag == 0).cumsum()
    streak = flag.groupby(grp).cumsum()
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f03_amad_022_longest_streak_close_above_sma252_252d(close: pd.Series) -> pd.Series:
    """Longest consecutive-bar streak of close > SMA252 inside last 252 bars."""
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (close > sma).astype(int)
    grp = (flag == 0).cumsum()
    streak = flag.groupby(grp).cumsum()
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f03_amad_023_days_since_last_close_below_sma63(close: pd.Series) -> pd.Series:
    """Bars since the most recent close < SMA63 event."""
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    below = close < sma
    pos = pd.Series(np.arange(len(close)), index=close.index)
    last = pos.where(below).ffill()
    return pos - last


def f03_amad_024_days_since_last_close_below_sma252(close: pd.Series) -> pd.Series:
    """Bars since the most recent close < SMA252 event."""
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    below = close < sma
    pos = pd.Series(np.arange(len(close)), index=close.index)
    last = pos.where(below).ffill()
    return pos - last


def f03_amad_025_days_since_first_252d_high_in_current_uptrend(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars since the FIRST new-252d-high event of the current above-SMA252 streak."""
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    above = (close > sma)
    streak_id = (~above).cumsum()
    rmax_prior = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high = (high > rmax_prior) & above
    pos = pd.Series(np.arange(len(close)), index=close.index)
    first_in_streak = pos.where(new_high).groupby(streak_id).cummin()
    return (pos - first_in_streak).where(above, np.nan)


def f03_amad_026_days_above_anchored_252d_vwap(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bars in 252 where close > rolling 252d VWAP."""
    pv = (close * volume).rolling(YDAYS, min_periods=QDAYS).sum()
    vv = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    vwap = _safe_div(pv, vv)
    return (close > vwap).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f03_amad_027_uptrend_state_score_252d(close: pd.Series) -> pd.Series:
    """Mean over 252d of (close>SMA21 & SMA21>SMA63 & SMA63>SMA252 & SMA252 rising)."""
    s21 = close.rolling(MDAYS, min_periods=WDAYS).mean()
    s63 = close.rolling(QDAYS, min_periods=MDAYS).mean()
    s252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((close > s21) & (s21 > s63) & (s63 > s252) & (s252 > s252.shift(MDAYS))).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).mean()


def f03_amad_028_count_higher_highs_252d(high: pd.Series) -> pd.Series:
    """Count of bars in 252 with high > prior bar's high."""
    return (high > high.shift(1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f03_amad_029_count_higher_lows_252d(low: pd.Series) -> pd.Series:
    """Count of bars in 252 with low > prior bar's low."""
    return (low > low.shift(1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f03_amad_030_count_close_in_top_decile_of_252d_range(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars in 252 where close-position-in-range >= 0.9."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    pos = (close - rmin) / rng
    return (pos >= 0.9).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f03_amad_031_log_advance_per_bar_252d_window(close: pd.Series) -> pd.Series:
    """Net 252d log return / 252 — mean log return per bar across window."""
    return (_safe_log(close) - _safe_log(close.shift(YDAYS))) / float(YDAYS)


def f03_amad_032_log_advance_per_bar_63d_window(close: pd.Series) -> pd.Series:
    """Net 63d log return / 63."""
    return (_safe_log(close) - _safe_log(close.shift(QDAYS))) / float(QDAYS)


def f03_amad_033_atr_units_per_bar_advance_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - 252d-low) / ATR21 / 252 — bar-normalized advance in ATR-equivalent units."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    atr = _atr(high, low, close, MDAYS)
    return ((close - rmin) / atr.replace(0, np.nan)) / float(YDAYS)


def f03_amad_034_position_in_252d_range(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close position in 252d range — 0=trough, 1=peak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    return (close - rmin) / rng


def f03_amad_035_log_advance_per_bar_above_sma63_252d(close: pd.Series) -> pd.Series:
    """252d log return / count of bars above SMA63 in last 252 — advance per uptrend bar."""
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    above = (close > sma).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    ret = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return _safe_div(ret, above + 1.0)


def f03_amad_036_cumulative_gain_per_bar_above_sma252_252d(close: pd.Series) -> pd.Series:
    """Cumulative log return / count of bars above SMA252."""
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    above = (close > sma).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    cum = _safe_log(close).diff().clip(lower=0).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(cum, above + 1.0)


def f03_amad_037_amplitude_normalized_advance_252d(close: pd.Series) -> pd.Series:
    """252d log advance / 252d std of daily log returns — return per unit risk."""
    ret = _safe_log(close) - _safe_log(close.shift(YDAYS))
    sd = _safe_log(close).diff().rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(ret, sd)


def f03_amad_038_normalized_magnitude_per_uptrend_day_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - 252d-low) / range / count of uptrend bars — gain per uptrend bar in range units."""
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    up = (close > sma).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    pos = (close - rmin) / rng
    return _safe_div(pos, up + 1.0)


def f03_amad_039_advance_efficiency_per_uptrend_bar_252d(close: pd.Series) -> pd.Series:
    """252d log advance / 252d count of close>prior-close bars."""
    up = (close.diff() > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    ret = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return _safe_div(ret, up + 1.0)


def f03_amad_040_secular_per_bar_log_advance_2520d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Log(close/2520d-low) / 2520 — secular per-bar advance rate."""
    rmin = low.rolling(2520, min_periods=YDAYS * 2).min()
    return (_safe_log(close) - _safe_log(rmin)) / 2520.0


def f03_amad_041_advance_magnitude_per_atr_252d(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """(close - 252d-low) / ATR21 — advance magnitude in ATR multiples."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    atr = _atr(high, low, close, MDAYS)
    return (close - rmin) / atr.replace(0, np.nan)


def f03_amad_042_trough_to_peak_log_per_age_score_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Log(252d-max(high)/252d-min(low)) / (bars since 252d-low + 1)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    def _dsm(w):
        return (len(w) - 1) - int(np.argmin(w))
    age = low.rolling(YDAYS, min_periods=QDAYS).apply(_dsm, raw=True)
    return _safe_div(_safe_log(rmax) - _safe_log(rmin), age + 1.0)


def f03_amad_043_first_third_log_return_per_bar_252d(close: pd.Series) -> pd.Series:
    """Log return over the FIRST third of the 252d window, divided by 84 bars."""
    third = 252 // 3
    lp = _safe_log(close)
    return (lp.shift(YDAYS - third) - lp.shift(YDAYS)) / float(third)


def f03_amad_044_last_third_log_return_per_bar_252d(close: pd.Series) -> pd.Series:
    """Log return over the LAST third of the 252d window, divided by 84 bars."""
    third = 252 // 3
    lp = _safe_log(close)
    return (lp - lp.shift(YDAYS - 2 * third)) / float(third)


def f03_amad_045_amplitude_per_pullback_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252d log range / (1 + count of >5% running pullbacks) — uninterrupted amplitude."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = _safe_log(rmax) - _safe_log(rmin)
    running_max = close.rolling(YDAYS, min_periods=QDAYS).max()
    dd = _safe_div(close, running_max) - 1.0
    pullbacks = (dd < -0.05).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(rng, 1.0 + pullbacks)


def f03_amad_046_quantile_p95_log_close_252d(close: pd.Series) -> pd.Series:
    """95th percentile of log close over 252 bars — high end of price distribution."""
    return _safe_log(close).rolling(YDAYS, min_periods=QDAYS).quantile(0.95)


def f03_amad_047_quantile_p50_log_close_252d(close: pd.Series) -> pd.Series:
    """Median log close over 252 bars."""
    return _safe_log(close).rolling(YDAYS, min_periods=QDAYS).quantile(0.50)


def f03_amad_048_quantile_p5_log_close_252d(close: pd.Series) -> pd.Series:
    """5th percentile of log close over 252 bars."""
    return _safe_log(close).rolling(YDAYS, min_periods=QDAYS).quantile(0.05)


def f03_amad_049_close_to_p95_log_distance_252d(close: pd.Series) -> pd.Series:
    """Log(close) - p95 of log(close) over 252d — distance above 95th percentile."""
    return _safe_log(close) - _safe_log(close).rolling(YDAYS, min_periods=QDAYS).quantile(0.95)


def f03_amad_050_close_to_p50_log_distance_252d(close: pd.Series) -> pd.Series:
    """Log(close) - median log close over 252d."""
    return _safe_log(close) - _safe_log(close).rolling(YDAYS, min_periods=QDAYS).quantile(0.50)


def f03_amad_051_quantile_iqr_log_close_252d(close: pd.Series) -> pd.Series:
    """IQR of log close over 252 bars — log-price dispersion."""
    lp = _safe_log(close)
    return lp.rolling(YDAYS, min_periods=QDAYS).quantile(0.75) - lp.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)


def f03_amad_052_distribution_skew_log_close_252d(close: pd.Series) -> pd.Series:
    """Skewness of log close over 252 bars — distribution asymmetry."""
    return _safe_log(close).rolling(YDAYS, min_periods=QDAYS).skew()


def f03_amad_053_distribution_kurt_log_close_252d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of log close over 252 bars."""
    return _safe_log(close).rolling(YDAYS, min_periods=QDAYS).kurt()


def f03_amad_054_distance_to_252d_max_normalized_by_std_log_close(close: pd.Series) -> pd.Series:
    """(252d-max - close) / 252d-std of log close — sigma below the rolling top."""
    lp = _safe_log(close)
    mx = lp.rolling(YDAYS, min_periods=QDAYS).max()
    sd = lp.rolling(YDAYS, min_periods=QDAYS).std()
    return (mx - lp) / sd.replace(0, np.nan)


def f03_amad_055_max_to_min_log_close_252d(close: pd.Series) -> pd.Series:
    """Log close max - log close min over 252d — log-price range."""
    lp = _safe_log(close)
    return lp.rolling(YDAYS, min_periods=QDAYS).max() - lp.rolling(YDAYS, min_periods=QDAYS).min()


def f03_amad_056_max_to_min_log_close_1260d(close: pd.Series) -> pd.Series:
    """Log close range over 1260d."""
    lp = _safe_log(close)
    return lp.rolling(1260, min_periods=YDAYS).max() - lp.rolling(1260, min_periods=YDAYS).min()


def f03_amad_057_max_to_min_log_close_2520d(close: pd.Series) -> pd.Series:
    """Log close range over 2520d (10y)."""
    lp = _safe_log(close)
    return lp.rolling(2520, min_periods=YDAYS * 2).max() - lp.rolling(2520, min_periods=YDAYS * 2).min()


def f03_amad_058_max_to_min_log_close_63d(close: pd.Series) -> pd.Series:
    """Log close range over 63d (quarter)."""
    lp = _safe_log(close)
    return lp.rolling(QDAYS, min_periods=MDAYS).max() - lp.rolling(QDAYS, min_periods=MDAYS).min()


def f03_amad_059_log_close_iqr_to_range_ratio_252d(close: pd.Series) -> pd.Series:
    """IQR / (max-min) of log close over 252d — middle vs tails breadth."""
    lp = _safe_log(close)
    iqr = lp.rolling(YDAYS, min_periods=QDAYS).quantile(0.75) - lp.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    rng = lp.rolling(YDAYS, min_periods=QDAYS).max() - lp.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(iqr, rng)


def f03_amad_060_distance_close_to_252d_median_atr_units(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(close - median(close)) / ATR21 over 252d window — ATR-units above median."""
    med = close.rolling(YDAYS, min_periods=QDAYS).median()
    atr = _atr(high, low, close, MDAYS)
    return (close - med) / atr.replace(0, np.nan)


def f03_amad_061_trough_to_peak_atr_units_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """(252d-max(close) - 252d-min(close)) / ATR21 — peak-to-trough span in ATR units."""
    mx = close.rolling(YDAYS, min_periods=QDAYS).max()
    mn = close.rolling(YDAYS, min_periods=QDAYS).min()
    atr = _atr(high, low, close, MDAYS)
    return (mx - mn) / atr.replace(0, np.nan)


def f03_amad_062_trough_to_peak_bars_252d(close: pd.Series) -> pd.Series:
    """Bars between 252d argmin and argmax (positive if peak follows trough)."""
    def _span(w):
        if np.isnan(w).any():
            return np.nan
        return float(int(np.argmax(w)) - int(np.argmin(w)))
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_span, raw=True)


def f03_amad_063_trough_to_peak_speed_252d(close: pd.Series) -> pd.Series:
    """(log peak - log trough) / |argmax - argmin| — speed of the trough-to-peak leg."""
    lp = _safe_log(close)
    def _spd(w):
        if np.isnan(w).any():
            return np.nan
        a, b = int(np.argmin(w)), int(np.argmax(w))
        if a == b:
            return np.nan
        return float((w[b] - w[a]) / (b - a))
    return lp.rolling(YDAYS, min_periods=QDAYS).apply(_spd, raw=True)


def f03_amad_064_peak_to_now_bars_252d(close: pd.Series) -> pd.Series:
    """Bars since 252d argmax of close — peak age."""
    def _pa(w):
        return float((len(w) - 1) - int(np.argmax(w)))
    return close.rolling(YDAYS, min_periods=QDAYS).apply(_pa, raw=True)


def f03_amad_065_peak_to_now_log_decay_252d(close: pd.Series) -> pd.Series:
    """Log(close / 252d-max(close)) — log distance below the peak."""
    return _safe_log(close) - _safe_log(close.rolling(YDAYS, min_periods=QDAYS).max())


def f03_amad_066_mid_advance_position_marker_252d(close: pd.Series) -> pd.Series:
    """(close - midpoint of 252d range) / range — signed marker of being past midpoint."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = close.rolling(YDAYS, min_periods=QDAYS).min()
    mid = (rmax + rmin) / 2.0
    rng = (rmax - rmin).replace(0, np.nan)
    return (close - mid) / rng


def f03_amad_067_trough_age_252d(low: pd.Series) -> pd.Series:
    """Bars since 252d argmin of low."""
    def _ta(w):
        return float((len(w) - 1) - int(np.argmin(w)))
    return low.rolling(YDAYS, min_periods=QDAYS).apply(_ta, raw=True)


def f03_amad_068_advance_age_signed_score_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Trough-age minus peak-age (252d) — positive = peak more recent than trough."""
    def _ta(w):
        return float((len(w) - 1) - int(np.argmin(w)))
    def _pa(w):
        return float((len(w) - 1) - int(np.argmax(w)))
    ta = low.rolling(YDAYS, min_periods=QDAYS).apply(_ta, raw=True)
    pa = close.rolling(YDAYS, min_periods=QDAYS).apply(_pa, raw=True)
    return ta - pa


def f03_amad_069_mature_advance_indicator_252d(close: pd.Series) -> pd.Series:
    """1 if 252d peak occurred > 21 bars ago AND uptrend (close>SMA252), else 0; mean over 21d."""
    def _pa(w):
        return float((len(w) - 1) - int(np.argmax(w)))
    pa = close.rolling(YDAYS, min_periods=QDAYS).apply(_pa, raw=True)
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((pa > MDAYS) & (close > sma)).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean()


def f03_amad_070_days_in_distribution_top_decile_252d(close: pd.Series) -> pd.Series:
    """Count of bars in 252 whose log close >= p90 of 252d log close."""
    lp = _safe_log(close)
    p90 = lp.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return (lp >= p90).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f03_amad_071_trough_to_peak_log_x_age_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Log(252d-max(close)/252d-min(low)) × peak_age — accumulated peak signal."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    def _pa(w):
        return float((len(w) - 1) - int(np.argmax(w)))
    pa = close.rolling(YDAYS, min_periods=QDAYS).apply(_pa, raw=True)
    return (_safe_log(rmax) - _safe_log(rmin)) * pa


def f03_amad_072_peak_to_prior_peak_log_advance_252d(close: pd.Series) -> pd.Series:
    """Log(252d-max(close) / 252d-max(close) lagged 252) — peak vs prior-year peak growth."""
    mx = close.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_log(mx) - _safe_log(mx.shift(YDAYS))


def f03_amad_073_secular_trough_to_peak_log_2520d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Log(2520d-max(close)/2520d-min(low)) — 10y peak-to-trough log span."""
    mx = close.rolling(2520, min_periods=YDAYS * 2).max()
    mn = low.rolling(2520, min_periods=YDAYS * 2).min()
    return _safe_log(mx) - _safe_log(mn)


def f03_amad_074_long_horizon_advance_completeness_2520d(close: pd.Series) -> pd.Series:
    """Close / 2520d-max(close) — how complete the secular advance looks (1.0 = at top)."""
    return _safe_div(close, close.rolling(2520, min_periods=YDAYS * 2).max())


def f03_amad_075_advance_completeness_pct_of_252d_max(close: pd.Series) -> pd.Series:
    """Close / 252d-max(close) — annual advance completeness (1.0 = at top)."""
    return _safe_div(close, close.rolling(YDAYS, min_periods=QDAYS).max())


# ============================================================
#                        REGISTRY
# ============================================================

ADVANCE_MAGNITUDE_DURATION_BASE_REGISTRY_001_075 = {
    "f03_amad_001_log_advance_magnitude_252d": {"inputs": ["close", "low"], "func": f03_amad_001_log_advance_magnitude_252d},
    "f03_amad_002_log_advance_magnitude_63d": {"inputs": ["close", "low"], "func": f03_amad_002_log_advance_magnitude_63d},
    "f03_amad_003_log_advance_magnitude_1260d": {"inputs": ["close", "low"], "func": f03_amad_003_log_advance_magnitude_1260d},
    "f03_amad_004_log_advance_magnitude_2520d": {"inputs": ["close", "low"], "func": f03_amad_004_log_advance_magnitude_2520d},
    "f03_amad_005_log_advance_close_anchored_1260d": {"inputs": ["close"], "func": f03_amad_005_log_advance_close_anchored_1260d},
    "f03_amad_006_log_high_above_252d_low": {"inputs": ["high", "low"], "func": f03_amad_006_log_high_above_252d_low},
    "f03_amad_007_log_high_above_1260d_low": {"inputs": ["high", "low"], "func": f03_amad_007_log_high_above_1260d_low},
    "f03_amad_008_multiplicative_advance_pct_252d": {"inputs": ["close", "low"], "func": f03_amad_008_multiplicative_advance_pct_252d},
    "f03_amad_009_log_high_now_minus_log_low_then_252d": {"inputs": ["high", "low"], "func": f03_amad_009_log_high_now_minus_log_low_then_252d},
    "f03_amad_010_log_high_now_minus_log_low_then_1260d": {"inputs": ["high", "low"], "func": f03_amad_010_log_high_now_minus_log_low_then_1260d},
    "f03_amad_011_cumulative_positive_log_return_252d": {"inputs": ["close"], "func": f03_amad_011_cumulative_positive_log_return_252d},
    "f03_amad_012_secular_advance_log_zscore_in_2520d": {"inputs": ["close", "low"], "func": f03_amad_012_secular_advance_log_zscore_in_2520d},
    "f03_amad_013_anchored_vwap_advance_log_252d": {"inputs": ["close", "volume"], "func": f03_amad_013_anchored_vwap_advance_log_252d},
    "f03_amad_014_max_running_total_log_return_252d": {"inputs": ["close"], "func": f03_amad_014_max_running_total_log_return_252d},
    "f03_amad_015_net_log_return_252d": {"inputs": ["close"], "func": f03_amad_015_net_log_return_252d},
    "f03_amad_016_days_above_sma252_in_252d": {"inputs": ["close"], "func": f03_amad_016_days_above_sma252_in_252d},
    "f03_amad_017_days_above_50pct_of_252d_range": {"inputs": ["close", "high", "low"], "func": f03_amad_017_days_above_50pct_of_252d_range},
    "f03_amad_018_days_in_HH_HL_state_252d": {"inputs": ["high", "low"], "func": f03_amad_018_days_in_HH_HL_state_252d},
    "f03_amad_019_days_within_5pct_of_252d_high": {"inputs": ["close", "high"], "func": f03_amad_019_days_within_5pct_of_252d_high},
    "f03_amad_020_days_within_10pct_of_252d_high": {"inputs": ["close", "high"], "func": f03_amad_020_days_within_10pct_of_252d_high},
    "f03_amad_021_longest_streak_close_above_sma63_252d": {"inputs": ["close"], "func": f03_amad_021_longest_streak_close_above_sma63_252d},
    "f03_amad_022_longest_streak_close_above_sma252_252d": {"inputs": ["close"], "func": f03_amad_022_longest_streak_close_above_sma252_252d},
    "f03_amad_023_days_since_last_close_below_sma63": {"inputs": ["close"], "func": f03_amad_023_days_since_last_close_below_sma63},
    "f03_amad_024_days_since_last_close_below_sma252": {"inputs": ["close"], "func": f03_amad_024_days_since_last_close_below_sma252},
    "f03_amad_025_days_since_first_252d_high_in_current_uptrend": {"inputs": ["close", "high"], "func": f03_amad_025_days_since_first_252d_high_in_current_uptrend},
    "f03_amad_026_days_above_anchored_252d_vwap": {"inputs": ["close", "volume"], "func": f03_amad_026_days_above_anchored_252d_vwap},
    "f03_amad_027_uptrend_state_score_252d": {"inputs": ["close"], "func": f03_amad_027_uptrend_state_score_252d},
    "f03_amad_028_count_higher_highs_252d": {"inputs": ["high"], "func": f03_amad_028_count_higher_highs_252d},
    "f03_amad_029_count_higher_lows_252d": {"inputs": ["low"], "func": f03_amad_029_count_higher_lows_252d},
    "f03_amad_030_count_close_in_top_decile_of_252d_range": {"inputs": ["close", "high", "low"], "func": f03_amad_030_count_close_in_top_decile_of_252d_range},
    "f03_amad_031_log_advance_per_bar_252d_window": {"inputs": ["close"], "func": f03_amad_031_log_advance_per_bar_252d_window},
    "f03_amad_032_log_advance_per_bar_63d_window": {"inputs": ["close"], "func": f03_amad_032_log_advance_per_bar_63d_window},
    "f03_amad_033_atr_units_per_bar_advance_252d": {"inputs": ["close", "high", "low"], "func": f03_amad_033_atr_units_per_bar_advance_252d},
    "f03_amad_034_position_in_252d_range": {"inputs": ["close", "high", "low"], "func": f03_amad_034_position_in_252d_range},
    "f03_amad_035_log_advance_per_bar_above_sma63_252d": {"inputs": ["close"], "func": f03_amad_035_log_advance_per_bar_above_sma63_252d},
    "f03_amad_036_cumulative_gain_per_bar_above_sma252_252d": {"inputs": ["close"], "func": f03_amad_036_cumulative_gain_per_bar_above_sma252_252d},
    "f03_amad_037_amplitude_normalized_advance_252d": {"inputs": ["close"], "func": f03_amad_037_amplitude_normalized_advance_252d},
    "f03_amad_038_normalized_magnitude_per_uptrend_day_252d": {"inputs": ["close", "high", "low"], "func": f03_amad_038_normalized_magnitude_per_uptrend_day_252d},
    "f03_amad_039_advance_efficiency_per_uptrend_bar_252d": {"inputs": ["close"], "func": f03_amad_039_advance_efficiency_per_uptrend_bar_252d},
    "f03_amad_040_secular_per_bar_log_advance_2520d": {"inputs": ["close", "low"], "func": f03_amad_040_secular_per_bar_log_advance_2520d},
    "f03_amad_041_advance_magnitude_per_atr_252d": {"inputs": ["close", "low", "high"], "func": f03_amad_041_advance_magnitude_per_atr_252d},
    "f03_amad_042_trough_to_peak_log_per_age_score_252d": {"inputs": ["close", "high", "low"], "func": f03_amad_042_trough_to_peak_log_per_age_score_252d},
    "f03_amad_043_first_third_log_return_per_bar_252d": {"inputs": ["close"], "func": f03_amad_043_first_third_log_return_per_bar_252d},
    "f03_amad_044_last_third_log_return_per_bar_252d": {"inputs": ["close"], "func": f03_amad_044_last_third_log_return_per_bar_252d},
    "f03_amad_045_amplitude_per_pullback_252d": {"inputs": ["close", "high", "low"], "func": f03_amad_045_amplitude_per_pullback_252d},
    "f03_amad_046_quantile_p95_log_close_252d": {"inputs": ["close"], "func": f03_amad_046_quantile_p95_log_close_252d},
    "f03_amad_047_quantile_p50_log_close_252d": {"inputs": ["close"], "func": f03_amad_047_quantile_p50_log_close_252d},
    "f03_amad_048_quantile_p5_log_close_252d": {"inputs": ["close"], "func": f03_amad_048_quantile_p5_log_close_252d},
    "f03_amad_049_close_to_p95_log_distance_252d": {"inputs": ["close"], "func": f03_amad_049_close_to_p95_log_distance_252d},
    "f03_amad_050_close_to_p50_log_distance_252d": {"inputs": ["close"], "func": f03_amad_050_close_to_p50_log_distance_252d},
    "f03_amad_051_quantile_iqr_log_close_252d": {"inputs": ["close"], "func": f03_amad_051_quantile_iqr_log_close_252d},
    "f03_amad_052_distribution_skew_log_close_252d": {"inputs": ["close"], "func": f03_amad_052_distribution_skew_log_close_252d},
    "f03_amad_053_distribution_kurt_log_close_252d": {"inputs": ["close"], "func": f03_amad_053_distribution_kurt_log_close_252d},
    "f03_amad_054_distance_to_252d_max_normalized_by_std_log_close": {"inputs": ["close"], "func": f03_amad_054_distance_to_252d_max_normalized_by_std_log_close},
    "f03_amad_055_max_to_min_log_close_252d": {"inputs": ["close"], "func": f03_amad_055_max_to_min_log_close_252d},
    "f03_amad_056_max_to_min_log_close_1260d": {"inputs": ["close"], "func": f03_amad_056_max_to_min_log_close_1260d},
    "f03_amad_057_max_to_min_log_close_2520d": {"inputs": ["close"], "func": f03_amad_057_max_to_min_log_close_2520d},
    "f03_amad_058_max_to_min_log_close_63d": {"inputs": ["close"], "func": f03_amad_058_max_to_min_log_close_63d},
    "f03_amad_059_log_close_iqr_to_range_ratio_252d": {"inputs": ["close"], "func": f03_amad_059_log_close_iqr_to_range_ratio_252d},
    "f03_amad_060_distance_close_to_252d_median_atr_units": {"inputs": ["close", "high", "low"], "func": f03_amad_060_distance_close_to_252d_median_atr_units},
    "f03_amad_061_trough_to_peak_atr_units_252d": {"inputs": ["close", "high", "low"], "func": f03_amad_061_trough_to_peak_atr_units_252d},
    "f03_amad_062_trough_to_peak_bars_252d": {"inputs": ["close"], "func": f03_amad_062_trough_to_peak_bars_252d},
    "f03_amad_063_trough_to_peak_speed_252d": {"inputs": ["close"], "func": f03_amad_063_trough_to_peak_speed_252d},
    "f03_amad_064_peak_to_now_bars_252d": {"inputs": ["close"], "func": f03_amad_064_peak_to_now_bars_252d},
    "f03_amad_065_peak_to_now_log_decay_252d": {"inputs": ["close"], "func": f03_amad_065_peak_to_now_log_decay_252d},
    "f03_amad_066_mid_advance_position_marker_252d": {"inputs": ["close"], "func": f03_amad_066_mid_advance_position_marker_252d},
    "f03_amad_067_trough_age_252d": {"inputs": ["low"], "func": f03_amad_067_trough_age_252d},
    "f03_amad_068_advance_age_signed_score_252d": {"inputs": ["close", "low"], "func": f03_amad_068_advance_age_signed_score_252d},
    "f03_amad_069_mature_advance_indicator_252d": {"inputs": ["close"], "func": f03_amad_069_mature_advance_indicator_252d},
    "f03_amad_070_days_in_distribution_top_decile_252d": {"inputs": ["close"], "func": f03_amad_070_days_in_distribution_top_decile_252d},
    "f03_amad_071_trough_to_peak_log_x_age_252d": {"inputs": ["close", "low"], "func": f03_amad_071_trough_to_peak_log_x_age_252d},
    "f03_amad_072_peak_to_prior_peak_log_advance_252d": {"inputs": ["close"], "func": f03_amad_072_peak_to_prior_peak_log_advance_252d},
    "f03_amad_073_secular_trough_to_peak_log_2520d": {"inputs": ["close", "low"], "func": f03_amad_073_secular_trough_to_peak_log_2520d},
    "f03_amad_074_long_horizon_advance_completeness_2520d": {"inputs": ["close"], "func": f03_amad_074_long_horizon_advance_completeness_2520d},
    "f03_amad_075_advance_completeness_pct_of_252d_max": {"inputs": ["close"], "func": f03_amad_075_advance_completeness_pct_of_252d_max},
}
