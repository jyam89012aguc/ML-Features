"""
108_drawdown_history_rank — Extended Features 001-075
Domain: deeper variants of drawdown-history-rank features —
        intraday low-based drawdowns, volume-weighted proximity, log-return
        drawdowns, rolling window severity comparisons, cross-window ranks,
        additional historical benchmark comparisons.
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _expanding_max(s: pd.Series) -> pd.Series:
    return s.expanding(min_periods=1).max()


def _drawdown_depth_pct(close: pd.Series) -> pd.Series:
    """Absolute drawdown depth from expanding peak (fraction >= 0)."""
    peak = _expanding_max(close)
    return _safe_div(peak - close, peak.clip(lower=_EPS))


def _rolling_drawdown_from_peak(close: pd.Series, w: int) -> pd.Series:
    """Drawdown from rolling w-day high (fraction >= 0)."""
    roll_peak = _rolling_max(close, w)
    return _safe_div(roll_peak - close, roll_peak.clip(lower=_EPS))


def _current_dd_duration(close: pd.Series) -> pd.Series:
    """Days elapsed since the current drawdown began."""
    depth = _drawdown_depth_pct(close)
    at_high = (depth < _EPS).astype(int)
    idx = pd.Series(range(len(close)), index=close.index, dtype=float)
    last_high_idx = idx.where(at_high == 1).ffill().fillna(0)
    duration = idx - last_high_idx
    return duration.where(depth >= _EPS, 0.0)


# ── Extended Feature Functions 001-075 ───────────────────────────────────────

# --- Group A (001-015): Intraday low and high based drawdown variants ---

def dhr_ext_001_intraday_low_dd_from_expanding_peak(close: pd.Series, low: pd.Series) -> pd.Series:
    """Drawdown of intraday low from the expanding all-time closing high (fraction >= 0)."""
    peak = _expanding_max(close)
    return _safe_div(peak - low, peak.clip(lower=_EPS))


def dhr_ext_002_intraday_low_dd_from_252d_peak(close: pd.Series, low: pd.Series) -> pd.Series:
    """Drawdown of intraday low from 252-day rolling closing high (fraction >= 0)."""
    peak = _rolling_max(close, _TD_YEAR)
    return _safe_div(peak - low, peak.clip(lower=_EPS))


def dhr_ext_003_intraday_low_expanding_pctrank(close: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding pct-rank of intraday-low-based drawdown depth vs all history."""
    depth = dhr_ext_001_intraday_low_dd_from_expanding_peak(close, low)
    return depth.expanding(min_periods=2).rank(pct=True)


def dhr_ext_004_intraday_low_rolling_pctrank_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """252-day rolling pct-rank of intraday-low drawdown depth."""
    depth = dhr_ext_001_intraday_low_dd_from_expanding_peak(close, low)
    return depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dhr_ext_005_intraday_low_vs_expanding_max_dd_ratio(close: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday-low drawdown as fraction of the all-time worst intraday-low drawdown."""
    depth = dhr_ext_001_intraday_low_dd_from_expanding_peak(close, low)
    max_ever = depth.expanding(min_periods=1).max().clip(lower=_EPS)
    return _safe_div(depth, max_ever)


def dhr_ext_006_intraday_low_new_all_time_low_flag(close: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: today's intraday low is a new all-time expanding low for this ticker."""
    exp_min = low.expanding(min_periods=1).min()
    return (low <= exp_min + _EPS).astype(float)


def dhr_ext_007_typical_price_dd_from_expanding_peak(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Drawdown of typical price (H+L+C)/3 from the expanding typical-price peak."""
    tp = (high + low + close) / 3.0
    peak = _expanding_max(tp)
    return _safe_div(peak - tp, peak.clip(lower=_EPS))


def dhr_ext_008_typical_price_expanding_pctrank(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding pct-rank of typical-price drawdown depth vs all history."""
    depth = dhr_ext_007_typical_price_dd_from_expanding_peak(close, high, low)
    return depth.expanding(min_periods=2).rank(pct=True)


def dhr_ext_009_typical_price_rolling_pctrank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day rolling pct-rank of typical-price drawdown depth."""
    depth = dhr_ext_007_typical_price_dd_from_expanding_peak(close, high, low)
    return depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dhr_ext_010_weighted_close_dd_from_expanding_peak(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Drawdown of weighted close (H+L+2C)/4 from its expanding peak."""
    wc = (high + low + 2.0 * close) / 4.0
    peak = _expanding_max(wc)
    return _safe_div(peak - wc, peak.clip(lower=_EPS))


def dhr_ext_011_weighted_close_expanding_pctrank(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding pct-rank of weighted-close drawdown depth."""
    depth = dhr_ext_010_weighted_close_dd_from_expanding_peak(close, high, low)
    return depth.expanding(min_periods=2).rank(pct=True)


def dhr_ext_012_hl_midpoint_dd_from_expanding_peak(high: pd.Series, low: pd.Series) -> pd.Series:
    """Drawdown of H/L midpoint from its expanding peak."""
    mid = (high + low) / 2.0
    peak = _expanding_max(mid)
    return _safe_div(peak - mid, peak.clip(lower=_EPS))


def dhr_ext_013_hl_midpoint_expanding_pctrank(high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding pct-rank of H/L midpoint drawdown depth."""
    depth = dhr_ext_012_hl_midpoint_dd_from_expanding_peak(high, low)
    return depth.expanding(min_periods=2).rank(pct=True)


def dhr_ext_014_open_price_dd_from_expanding_peak(open: pd.Series) -> pd.Series:
    """Drawdown of open price from its expanding all-time high open."""
    peak = _expanding_max(open)
    return _safe_div(peak - open, peak.clip(lower=_EPS))


def dhr_ext_015_open_price_expanding_pctrank(open: pd.Series) -> pd.Series:
    """Expanding pct-rank of open-price drawdown depth."""
    depth = dhr_ext_014_open_price_dd_from_expanding_peak(open)
    return depth.expanding(min_periods=2).rank(pct=True)


# --- Group B (016-030): Log-return based drawdown variants ---

def dhr_ext_016_log_return_dd_from_expanding_peak(close: pd.Series) -> pd.Series:
    """Log-return drawdown from the all-time expanding log-price peak."""
    log_price = np.log(close.clip(lower=_EPS))
    peak_log = _expanding_max(log_price)
    return (peak_log - log_price).clip(lower=0.0)


def dhr_ext_017_log_return_dd_expanding_pctrank(close: pd.Series) -> pd.Series:
    """Expanding pct-rank of log-return drawdown depth."""
    depth = dhr_ext_016_log_return_dd_from_expanding_peak(close)
    return depth.expanding(min_periods=2).rank(pct=True)


def dhr_ext_018_log_return_dd_rolling_pctrank_252d(close: pd.Series) -> pd.Series:
    """252-day rolling pct-rank of log-return drawdown depth."""
    depth = dhr_ext_016_log_return_dd_from_expanding_peak(close)
    return depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dhr_ext_019_log_return_dd_vs_expanding_max_ratio(close: pd.Series) -> pd.Series:
    """Log-return drawdown as fraction of all-time maximum log drawdown."""
    depth = dhr_ext_016_log_return_dd_from_expanding_peak(close)
    max_ever = depth.expanding(min_periods=1).max().clip(lower=_EPS)
    return _safe_div(depth, max_ever)


def dhr_ext_020_log_return_dd_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding z-score of log-return drawdown depth."""
    depth = dhr_ext_016_log_return_dd_from_expanding_peak(close)
    m = depth.expanding(min_periods=2).mean()
    s = depth.expanding(min_periods=2).std()
    return _safe_div(depth - m, s)


def dhr_ext_021_log_return_dd_vs_expanding_median_ratio(close: pd.Series) -> pd.Series:
    """Log-return drawdown vs expanding median log drawdown ratio."""
    depth = dhr_ext_016_log_return_dd_from_expanding_peak(close)
    med = depth.expanding(min_periods=2).median().clip(lower=_EPS)
    return _safe_div(depth, med)


# --- Group C (022-035): Volume-weighted price proximity vs history ---

def dhr_ext_022_vwap_rolling_dd_from_expanding_peak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Drawdown of 21-day VWAP from its expanding all-time peak (fraction >= 0)."""
    dollar_vol = close * volume
    vwap = _rolling_sum(dollar_vol, _TD_MON) / _rolling_sum(volume.replace(0, np.nan), _TD_MON)
    peak = _expanding_max(vwap)
    return _safe_div(peak - vwap, peak.clip(lower=_EPS))


def dhr_ext_023_vwap_dd_expanding_pctrank(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding pct-rank of 21-day VWAP drawdown depth."""
    depth = dhr_ext_022_vwap_rolling_dd_from_expanding_peak(close, volume)
    return depth.expanding(min_periods=2).rank(pct=True)


def dhr_ext_024_vwap_dd_rolling_pctrank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day rolling pct-rank of 21-day VWAP drawdown depth."""
    depth = dhr_ext_022_vwap_rolling_dd_from_expanding_peak(close, volume)
    return depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dhr_ext_025_volume_weighted_price_pctrank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day pct-rank of volume-weighted average price (VWAP) in trailing 252-day dist."""
    dollar_vol = close * volume
    vwap = _rolling_sum(dollar_vol, _TD_MON) / _rolling_sum(volume.replace(0, np.nan), _TD_MON)
    return vwap.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dhr_ext_026_close_vs_vwap_21d_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Close price relative to 21-day VWAP (ratio; < 1 = below VWAP)."""
    dollar_vol = close * volume
    vwap = _rolling_sum(dollar_vol, _TD_MON) / _rolling_sum(volume.replace(0, np.nan), _TD_MON)
    return _safe_div(close, vwap.clip(lower=_EPS))


def dhr_ext_027_close_below_vwap_252d_fraction(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where close was below the 21-day VWAP."""
    dollar_vol = close * volume
    vwap = _rolling_sum(dollar_vol, _TD_MON) / _rolling_sum(volume.replace(0, np.nan), _TD_MON)
    below = (close < vwap).astype(float)
    return _rolling_sum(below, _TD_YEAR) / _TD_YEAR


# --- Group D (028-042): Longer-window and alternative window depth comparisons ---

def dhr_ext_028_dd_depth_from_5yr_peak_pctrank_vs_3yr(close: pd.Series) -> pd.Series:
    """5-year drawdown depth ranked within the trailing 3-year distribution."""
    depth_5yr = _rolling_drawdown_from_peak(close, 1260)
    return depth_5yr.rolling(756, min_periods=504).rank(pct=True)


def dhr_ext_029_dd_depth_from_3yr_peak_pctrank_vs_1yr(close: pd.Series) -> pd.Series:
    """3-year drawdown depth ranked within the trailing 1-year distribution."""
    depth_3yr = _rolling_drawdown_from_peak(close, 756)
    return depth_3yr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dhr_ext_030_dd_depth_from_2yr_peak_expanding_pctrank(close: pd.Series) -> pd.Series:
    """2-year drawdown depth ranked on expanding all-history basis."""
    depth_2yr = _rolling_drawdown_from_peak(close, 504)
    return depth_2yr.expanding(min_periods=2).rank(pct=True)


def dhr_ext_031_dd_depth_from_126d_peak_pctrank_252d(close: pd.Series) -> pd.Series:
    """Half-year drawdown depth ranked within the trailing year distribution."""
    depth_hyr = _rolling_drawdown_from_peak(close, _TD_HALF)
    return depth_hyr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dhr_ext_032_dd_depth_from_63d_peak_pctrank_252d(close: pd.Series) -> pd.Series:
    """Quarterly drawdown depth ranked within the trailing year distribution."""
    depth_qtr = _rolling_drawdown_from_peak(close, _TD_QTR)
    return depth_qtr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dhr_ext_033_dd_depth_from_21d_peak_pctrank_252d(close: pd.Series) -> pd.Series:
    """Monthly drawdown depth ranked within the trailing year distribution."""
    depth_mon = _rolling_drawdown_from_peak(close, _TD_MON)
    return depth_mon.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dhr_ext_034_dd_depth_from_5d_peak_pctrank_252d(close: pd.Series) -> pd.Series:
    """Weekly drawdown depth ranked within the trailing year distribution."""
    depth_wk = _rolling_drawdown_from_peak(close, _TD_WEEK)
    return depth_wk.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dhr_ext_035_dd_depth_cross_window_divergence(close: pd.Series) -> pd.Series:
    """Divergence: expanding drawdown depth minus 252-day rolling drawdown depth.
    Positive = current drawdown worse on all-time basis than just year basis.
    """
    dd_all = _drawdown_depth_pct(close)
    dd_1yr = _rolling_drawdown_from_peak(close, _TD_YEAR)
    return dd_all - dd_1yr


# --- Group E (036-050): Historical recovery and post-low statistics ---

def dhr_ext_036_days_since_expanding_low_expanding_pctrank(close: pd.Series) -> pd.Series:
    """Expanding pct-rank of days-since-all-time-low (lower rank = more recently at all-time low)."""
    exp_low_idx = close.expanding(min_periods=1).apply(lambda x: float(np.argmin(x)), raw=True)
    idx = pd.Series(range(len(close)), index=close.index, dtype=float)
    d = idx - exp_low_idx
    return d.expanding(min_periods=2).rank(pct=True)


def dhr_ext_037_days_since_252d_low_expanding_pctrank(close: pd.Series) -> pd.Series:
    """Expanding pct-rank of days since last 252-day low was set."""
    def _days_since_min(arr):
        pos = np.argmin(arr)
        return float(len(arr) - 1 - pos)
    d = close.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_days_since_min, raw=True)
    return d.expanding(min_periods=2).rank(pct=True)


def dhr_ext_038_recovery_from_252d_low_pct(close: pd.Series) -> pd.Series:
    """Percentage current price is above the 252-day rolling low (recovery metric)."""
    low_252 = _rolling_min(close, _TD_YEAR).clip(lower=_EPS)
    return _safe_div(close - low_252, low_252)


def dhr_ext_039_recovery_from_252d_low_expanding_pctrank(close: pd.Series) -> pd.Series:
    """Expanding pct-rank of percentage recovery from 252-day low (lower = closer to low)."""
    rec = dhr_ext_038_recovery_from_252d_low_pct(close)
    return rec.expanding(min_periods=2).rank(pct=True)


def dhr_ext_040_recovery_from_expanding_low_pct(close: pd.Series) -> pd.Series:
    """Percentage current price is above the all-time expanding low."""
    exp_low = close.expanding(min_periods=1).min().clip(lower=_EPS)
    return _safe_div(close - exp_low, exp_low)


def dhr_ext_041_recovery_from_expanding_low_pctrank_252d(close: pd.Series) -> pd.Series:
    """252-day rolling pct-rank of percentage recovery from all-time low."""
    rec = dhr_ext_040_recovery_from_expanding_low_pct(close)
    return rec.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dhr_ext_042_dd_drawup_ratio_expanding(close: pd.Series) -> pd.Series:
    """Ratio of current drawdown depth to all-time expanding maximum drawup.
    Draw-up = (current close / expanding low) - 1.
    Proxy for how much the ticker could fall vs how much it has risen.
    """
    depth = _drawdown_depth_pct(close)
    exp_low = close.expanding(min_periods=1).min().clip(lower=_EPS)
    drawup = _safe_div(close - exp_low, exp_low).clip(lower=_EPS)
    return _safe_div(depth, drawup)


# --- Group F (043-057): Rolling distribution statistics of drawdown ---

def dhr_ext_043_rolling_min_dd_depth_252d(close: pd.Series) -> pd.Series:
    """Rolling minimum drawdown depth over trailing 252 days (best 1-year period)."""
    depth = _drawdown_depth_pct(close)
    return _rolling_min(depth, _TD_YEAR)


def dhr_ext_044_rolling_min_dd_depth_504d(close: pd.Series) -> pd.Series:
    """Rolling minimum drawdown depth over trailing 504 days."""
    depth = _drawdown_depth_pct(close)
    return _rolling_min(depth, 504)


def dhr_ext_045_dd_depth_range_252d(close: pd.Series) -> pd.Series:
    """Range (max - min) of drawdown depth over trailing 252 days (drawdown volatility)."""
    depth = _drawdown_depth_pct(close)
    return _rolling_max(depth, _TD_YEAR) - _rolling_min(depth, _TD_YEAR)


def dhr_ext_046_dd_depth_range_504d(close: pd.Series) -> pd.Series:
    """Range of drawdown depth over trailing 504 days."""
    depth = _drawdown_depth_pct(close)
    return _rolling_max(depth, 504) - _rolling_min(depth, 504)


def dhr_ext_047_dd_depth_cv_252d(close: pd.Series) -> pd.Series:
    """Coefficient of variation of drawdown depth over trailing 252 days (std/mean)."""
    depth = _drawdown_depth_pct(close)
    m = _rolling_mean(depth, _TD_YEAR).clip(lower=_EPS)
    s = _rolling_std(depth, _TD_YEAR)
    return _safe_div(s, m)


def dhr_ext_048_dd_depth_rolling_25pct_252d(close: pd.Series) -> pd.Series:
    """Rolling 25th-percentile drawdown depth over trailing 252 days."""
    depth = _drawdown_depth_pct(close)
    return depth.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)


def dhr_ext_049_dd_depth_rolling_75pct_252d(close: pd.Series) -> pd.Series:
    """Rolling 75th-percentile drawdown depth over trailing 252 days."""
    depth = _drawdown_depth_pct(close)
    return depth.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)


def dhr_ext_050_dd_depth_rolling_90pct_504d(close: pd.Series) -> pd.Series:
    """Rolling 90th-percentile drawdown depth over trailing 504 days."""
    depth = _drawdown_depth_pct(close)
    return depth.rolling(504, min_periods=_TD_YEAR).quantile(0.90)


def dhr_ext_051_dd_depth_iqr_252d(close: pd.Series) -> pd.Series:
    """Interquartile range (75th - 25th pct) of drawdown depth in trailing 252 days."""
    depth = _drawdown_depth_pct(close)
    q75 = depth.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    q25 = depth.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    return q75 - q25


def dhr_ext_052_current_dd_vs_iqr_252d_normalised(close: pd.Series) -> pd.Series:
    """Current drawdown depth normalised by 252-day IQR of drawdown depths."""
    depth = _drawdown_depth_pct(close)
    q75 = depth.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    q25 = depth.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    iqr = (q75 - q25).clip(lower=_EPS)
    return _safe_div(depth, iqr)


def dhr_ext_053_dd_depth_skew_252d(close: pd.Series) -> pd.Series:
    """Skewness of drawdown depth distribution over trailing 252 days."""
    depth = _drawdown_depth_pct(close)
    return depth.rolling(_TD_YEAR, min_periods=_TD_QTR).skew()


def dhr_ext_054_dd_depth_kurtosis_252d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of drawdown depth distribution over trailing 252 days."""
    depth = _drawdown_depth_pct(close)
    return depth.rolling(_TD_YEAR, min_periods=_TD_QTR).kurt()


def dhr_ext_055_dd_depth_ewm_21d(close: pd.Series) -> pd.Series:
    """EWM-smoothed (span=21) drawdown depth (emphasises recent distress)."""
    depth = _drawdown_depth_pct(close)
    return _ewm_mean(depth, _TD_MON)


# --- Group G (056-065): Composite multi-window historical rank features ---

def dhr_ext_056_dd_depth_multi_window_rank_avg(close: pd.Series) -> pd.Series:
    """Average of 252d, 504d, 756d rolling pct-ranks of drawdown depth (multi-horizon rank)."""
    depth = _drawdown_depth_pct(close)
    r1 = depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    r2 = depth.rolling(504, min_periods=_TD_YEAR).rank(pct=True)
    r3 = depth.rolling(756, min_periods=504).rank(pct=True)
    return (r1 + r2 + r3) / 3.0


def dhr_ext_057_dd_depth_all_windows_worst_flag(close: pd.Series) -> pd.Series:
    """Binary flag: drawdown is in top 10% worst across ALL of 252d, 504d, 756d windows."""
    depth = _drawdown_depth_pct(close)
    r1 = depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    r2 = depth.rolling(504, min_periods=_TD_YEAR).rank(pct=True)
    r3 = depth.rolling(756, min_periods=504).rank(pct=True)
    return ((r1 >= 0.90) & (r2 >= 0.90) & (r3 >= 0.90)).astype(float)


def dhr_ext_058_dd_depth_expanding_and_1yr_both_top10pct_flag(close: pd.Series) -> pd.Series:
    """Binary flag: drawdown depth in expanding top 10% AND 1-year top 10%."""
    depth = _drawdown_depth_pct(close)
    r_exp = depth.expanding(min_periods=2).rank(pct=True)
    r_1yr = depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return ((r_exp >= 0.90) & (r_1yr >= 0.90)).astype(float)


def dhr_ext_059_dd_capitulation_composite_v2(close: pd.Series) -> pd.Series:
    """Capitulation composite v2: weighted blend of expanding pct-ranks for depth,
    duration, recovery-needed, and price-pct-rank-inverted.
    Higher = more extreme distress relative to own ticker history.
    """
    depth = _drawdown_depth_pct(close)
    dur = _current_dd_duration(close)
    peak = _expanding_max(close)
    rec = _safe_div(peak - close, close.clip(lower=_EPS))
    price_inv = 1.0 - close.expanding(min_periods=2).rank(pct=True)

    r_depth = depth.expanding(min_periods=2).rank(pct=True)
    r_dur = dur.expanding(min_periods=2).rank(pct=True)
    r_rec = rec.expanding(min_periods=2).rank(pct=True)

    return (0.40 * r_depth + 0.20 * r_dur + 0.20 * r_rec + 0.20 * price_inv.fillna(0.5))


def dhr_ext_060_dd_extreme_flag_any_window(close: pd.Series) -> pd.Series:
    """Binary flag: drawdown depth in top 5% worst in ANY of 252d, 504d, 756d, expanding."""
    depth = _drawdown_depth_pct(close)
    r_exp = depth.expanding(min_periods=2).rank(pct=True)
    r_1yr = depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    r_2yr = depth.rolling(504, min_periods=_TD_YEAR).rank(pct=True)
    r_3yr = depth.rolling(756, min_periods=504).rank(pct=True)
    return ((r_exp >= 0.95) | (r_1yr >= 0.95) | (r_2yr >= 0.95) | (r_3yr >= 0.95)).astype(float)


# --- Group H (061-075): Additional severity ranks and cross-series comparisons ---

def dhr_ext_061_low_price_expanding_pctrank(low: pd.Series) -> pd.Series:
    """Expanding pct-rank of intraday low in the full intraday-low history."""
    return low.expanding(min_periods=2).rank(pct=True)


def dhr_ext_062_low_price_rolling_pctrank_252d(low: pd.Series) -> pd.Series:
    """252-day rolling pct-rank of intraday low."""
    return low.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dhr_ext_063_low_price_rolling_pctrank_504d(low: pd.Series) -> pd.Series:
    """504-day rolling pct-rank of intraday low."""
    return low.rolling(504, min_periods=_TD_YEAR).rank(pct=True)


def dhr_ext_064_close_vs_expanding_low_z_score(close: pd.Series) -> pd.Series:
    """Z-score of current close in the expanding distribution of all closes (standardised rank)."""
    m = close.expanding(min_periods=2).mean()
    s = close.expanding(min_periods=2).std().clip(lower=_EPS)
    return _safe_div(close - m, s)


def dhr_ext_065_dd_depth_vs_expanding_25pct_excess(close: pd.Series) -> pd.Series:
    """Excess of current drawdown above the expanding 25th-percentile drawdown."""
    depth = _drawdown_depth_pct(close)
    q25 = depth.expanding(min_periods=4).quantile(0.25)
    return (depth - q25).clip(lower=0.0)


def dhr_ext_066_dd_depth_vs_expanding_50pct_excess(close: pd.Series) -> pd.Series:
    """Excess of current drawdown above the expanding 50th-percentile (median) drawdown."""
    depth = _drawdown_depth_pct(close)
    q50 = depth.expanding(min_periods=2).median()
    return (depth - q50).clip(lower=0.0)


def dhr_ext_067_dd_depth_normalised_by_expanding_iqr(close: pd.Series) -> pd.Series:
    """Current drawdown depth normalised by expanding IQR of drawdown depths."""
    depth = _drawdown_depth_pct(close)
    q75 = depth.expanding(min_periods=4).quantile(0.75)
    q25 = depth.expanding(min_periods=4).quantile(0.25)
    iqr = (q75 - q25).clip(lower=_EPS)
    return _safe_div(depth, iqr)


def dhr_ext_068_fraction_252d_close_below_expanding_median(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where close was below the expanding median price."""
    exp_med = close.expanding(min_periods=2).median()
    below = (close < exp_med).astype(float)
    return _rolling_sum(below, _TD_YEAR) / _TD_YEAR


def dhr_ext_069_fraction_252d_dd_depth_above_current(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days with drawdown depth greater than today's depth (inverted rank)."""
    depth = _drawdown_depth_pct(close)
    return 1.0 - depth.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dhr_ext_070_dd_depth_momentum_5d_vs_expanding_rank(close: pd.Series) -> pd.Series:
    """Expanding pct-rank of the 5-day change in drawdown depth (rank of velocity)."""
    vel = _drawdown_depth_pct(close).diff(_TD_WEEK)
    return vel.expanding(min_periods=2).rank(pct=True)


def dhr_ext_071_dd_depth_momentum_21d_vs_expanding_rank(close: pd.Series) -> pd.Series:
    """Expanding pct-rank of the 21-day change in drawdown depth."""
    vel = _drawdown_depth_pct(close).diff(_TD_MON)
    return vel.expanding(min_periods=2).rank(pct=True)


def dhr_ext_072_is_price_in_lowest_decile_expanding(close: pd.Series) -> pd.Series:
    """Binary flag: current price is in the expanding lowest 10th percentile."""
    return (close.expanding(min_periods=10).rank(pct=True) <= 0.10).astype(float)


def dhr_ext_073_is_price_in_lowest_quintile_expanding(close: pd.Series) -> pd.Series:
    """Binary flag: current price is in the expanding lowest 20th percentile."""
    return (close.expanding(min_periods=5).rank(pct=True) <= 0.20).astype(float)


def dhr_ext_074_dd_depth_and_duration_both_top10pct_expanding(close: pd.Series) -> pd.Series:
    """Binary flag: BOTH depth AND duration are in the expanding top 10% simultaneously."""
    depth = _drawdown_depth_pct(close)
    dur = _current_dd_duration(close)
    r_depth = depth.expanding(min_periods=2).rank(pct=True)
    r_dur = dur.expanding(min_periods=2).rank(pct=True)
    return ((r_depth >= 0.90) & (r_dur >= 0.90)).astype(float)


def dhr_ext_075_dd_history_rank_final_composite(close: pd.Series) -> pd.Series:
    """Final composite: unweighted average of seven expanding pct-rank signals for
    drawdown depth, duration, recovery-needed, depth×duration, log-return depth,
    price-rank-inverted, and underwater-fraction.
    Higher score = more extreme by this ticker's own history.
    """
    depth = _drawdown_depth_pct(close)
    dur = _current_dd_duration(close)
    peak = _expanding_max(close)
    rec = _safe_div(peak - close, close.clip(lower=_EPS))
    log_depth = dhr_ext_016_log_return_dd_from_expanding_peak(close)
    price_inv = 1.0 - close.expanding(min_periods=2).rank(pct=True)
    uw_frac = _rolling_sum((depth > _EPS).astype(float), _TD_YEAR) / _TD_YEAR

    r1 = depth.expanding(min_periods=2).rank(pct=True)
    r2 = dur.expanding(min_periods=2).rank(pct=True)
    r3 = rec.expanding(min_periods=2).rank(pct=True)
    r4 = (depth * dur).expanding(min_periods=2).rank(pct=True)
    r5 = log_depth.expanding(min_periods=2).rank(pct=True)
    r6 = price_inv.fillna(0.5)
    r7 = uw_frac.expanding(min_periods=2).rank(pct=True)

    return (r1 + r2 + r3 + r4 + r5 + r6 + r7) / 7.0


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_HISTORY_RANK_EXTENDED_REGISTRY_001_075 = {
    "dhr_ext_001_intraday_low_dd_from_expanding_peak": {"inputs": ["close", "low"], "func": dhr_ext_001_intraday_low_dd_from_expanding_peak},
    "dhr_ext_002_intraday_low_dd_from_252d_peak": {"inputs": ["close", "low"], "func": dhr_ext_002_intraday_low_dd_from_252d_peak},
    "dhr_ext_003_intraday_low_expanding_pctrank": {"inputs": ["close", "low"], "func": dhr_ext_003_intraday_low_expanding_pctrank},
    "dhr_ext_004_intraday_low_rolling_pctrank_252d": {"inputs": ["close", "low"], "func": dhr_ext_004_intraday_low_rolling_pctrank_252d},
    "dhr_ext_005_intraday_low_vs_expanding_max_dd_ratio": {"inputs": ["close", "low"], "func": dhr_ext_005_intraday_low_vs_expanding_max_dd_ratio},
    "dhr_ext_006_intraday_low_new_all_time_low_flag": {"inputs": ["close", "low"], "func": dhr_ext_006_intraday_low_new_all_time_low_flag},
    "dhr_ext_007_typical_price_dd_from_expanding_peak": {"inputs": ["close", "high", "low"], "func": dhr_ext_007_typical_price_dd_from_expanding_peak},
    "dhr_ext_008_typical_price_expanding_pctrank": {"inputs": ["close", "high", "low"], "func": dhr_ext_008_typical_price_expanding_pctrank},
    "dhr_ext_009_typical_price_rolling_pctrank_252d": {"inputs": ["close", "high", "low"], "func": dhr_ext_009_typical_price_rolling_pctrank_252d},
    "dhr_ext_010_weighted_close_dd_from_expanding_peak": {"inputs": ["close", "high", "low"], "func": dhr_ext_010_weighted_close_dd_from_expanding_peak},
    "dhr_ext_011_weighted_close_expanding_pctrank": {"inputs": ["close", "high", "low"], "func": dhr_ext_011_weighted_close_expanding_pctrank},
    "dhr_ext_012_hl_midpoint_dd_from_expanding_peak": {"inputs": ["high", "low"], "func": dhr_ext_012_hl_midpoint_dd_from_expanding_peak},
    "dhr_ext_013_hl_midpoint_expanding_pctrank": {"inputs": ["high", "low"], "func": dhr_ext_013_hl_midpoint_expanding_pctrank},
    "dhr_ext_014_open_price_dd_from_expanding_peak": {"inputs": ["open"], "func": dhr_ext_014_open_price_dd_from_expanding_peak},
    "dhr_ext_015_open_price_expanding_pctrank": {"inputs": ["open"], "func": dhr_ext_015_open_price_expanding_pctrank},
    "dhr_ext_016_log_return_dd_from_expanding_peak": {"inputs": ["close"], "func": dhr_ext_016_log_return_dd_from_expanding_peak},
    "dhr_ext_017_log_return_dd_expanding_pctrank": {"inputs": ["close"], "func": dhr_ext_017_log_return_dd_expanding_pctrank},
    "dhr_ext_018_log_return_dd_rolling_pctrank_252d": {"inputs": ["close"], "func": dhr_ext_018_log_return_dd_rolling_pctrank_252d},
    "dhr_ext_019_log_return_dd_vs_expanding_max_ratio": {"inputs": ["close"], "func": dhr_ext_019_log_return_dd_vs_expanding_max_ratio},
    "dhr_ext_020_log_return_dd_expanding_zscore": {"inputs": ["close"], "func": dhr_ext_020_log_return_dd_expanding_zscore},
    "dhr_ext_021_log_return_dd_vs_expanding_median_ratio": {"inputs": ["close"], "func": dhr_ext_021_log_return_dd_vs_expanding_median_ratio},
    "dhr_ext_022_vwap_rolling_dd_from_expanding_peak": {"inputs": ["close", "volume"], "func": dhr_ext_022_vwap_rolling_dd_from_expanding_peak},
    "dhr_ext_023_vwap_dd_expanding_pctrank": {"inputs": ["close", "volume"], "func": dhr_ext_023_vwap_dd_expanding_pctrank},
    "dhr_ext_024_vwap_dd_rolling_pctrank_252d": {"inputs": ["close", "volume"], "func": dhr_ext_024_vwap_dd_rolling_pctrank_252d},
    "dhr_ext_025_volume_weighted_price_pctrank_252d": {"inputs": ["close", "volume"], "func": dhr_ext_025_volume_weighted_price_pctrank_252d},
    "dhr_ext_026_close_vs_vwap_21d_ratio": {"inputs": ["close", "volume"], "func": dhr_ext_026_close_vs_vwap_21d_ratio},
    "dhr_ext_027_close_below_vwap_252d_fraction": {"inputs": ["close", "volume"], "func": dhr_ext_027_close_below_vwap_252d_fraction},
    "dhr_ext_028_dd_depth_from_5yr_peak_pctrank_vs_3yr": {"inputs": ["close"], "func": dhr_ext_028_dd_depth_from_5yr_peak_pctrank_vs_3yr},
    "dhr_ext_029_dd_depth_from_3yr_peak_pctrank_vs_1yr": {"inputs": ["close"], "func": dhr_ext_029_dd_depth_from_3yr_peak_pctrank_vs_1yr},
    "dhr_ext_030_dd_depth_from_2yr_peak_expanding_pctrank": {"inputs": ["close"], "func": dhr_ext_030_dd_depth_from_2yr_peak_expanding_pctrank},
    "dhr_ext_031_dd_depth_from_126d_peak_pctrank_252d": {"inputs": ["close"], "func": dhr_ext_031_dd_depth_from_126d_peak_pctrank_252d},
    "dhr_ext_032_dd_depth_from_63d_peak_pctrank_252d": {"inputs": ["close"], "func": dhr_ext_032_dd_depth_from_63d_peak_pctrank_252d},
    "dhr_ext_033_dd_depth_from_21d_peak_pctrank_252d": {"inputs": ["close"], "func": dhr_ext_033_dd_depth_from_21d_peak_pctrank_252d},
    "dhr_ext_034_dd_depth_from_5d_peak_pctrank_252d": {"inputs": ["close"], "func": dhr_ext_034_dd_depth_from_5d_peak_pctrank_252d},
    "dhr_ext_035_dd_depth_cross_window_divergence": {"inputs": ["close"], "func": dhr_ext_035_dd_depth_cross_window_divergence},
    "dhr_ext_036_days_since_expanding_low_expanding_pctrank": {"inputs": ["close"], "func": dhr_ext_036_days_since_expanding_low_expanding_pctrank},
    "dhr_ext_037_days_since_252d_low_expanding_pctrank": {"inputs": ["close"], "func": dhr_ext_037_days_since_252d_low_expanding_pctrank},
    "dhr_ext_038_recovery_from_252d_low_pct": {"inputs": ["close"], "func": dhr_ext_038_recovery_from_252d_low_pct},
    "dhr_ext_039_recovery_from_252d_low_expanding_pctrank": {"inputs": ["close"], "func": dhr_ext_039_recovery_from_252d_low_expanding_pctrank},
    "dhr_ext_040_recovery_from_expanding_low_pct": {"inputs": ["close"], "func": dhr_ext_040_recovery_from_expanding_low_pct},
    "dhr_ext_041_recovery_from_expanding_low_pctrank_252d": {"inputs": ["close"], "func": dhr_ext_041_recovery_from_expanding_low_pctrank_252d},
    "dhr_ext_042_dd_drawup_ratio_expanding": {"inputs": ["close"], "func": dhr_ext_042_dd_drawup_ratio_expanding},
    "dhr_ext_043_rolling_min_dd_depth_252d": {"inputs": ["close"], "func": dhr_ext_043_rolling_min_dd_depth_252d},
    "dhr_ext_044_rolling_min_dd_depth_504d": {"inputs": ["close"], "func": dhr_ext_044_rolling_min_dd_depth_504d},
    "dhr_ext_045_dd_depth_range_252d": {"inputs": ["close"], "func": dhr_ext_045_dd_depth_range_252d},
    "dhr_ext_046_dd_depth_range_504d": {"inputs": ["close"], "func": dhr_ext_046_dd_depth_range_504d},
    "dhr_ext_047_dd_depth_cv_252d": {"inputs": ["close"], "func": dhr_ext_047_dd_depth_cv_252d},
    "dhr_ext_048_dd_depth_rolling_25pct_252d": {"inputs": ["close"], "func": dhr_ext_048_dd_depth_rolling_25pct_252d},
    "dhr_ext_049_dd_depth_rolling_75pct_252d": {"inputs": ["close"], "func": dhr_ext_049_dd_depth_rolling_75pct_252d},
    "dhr_ext_050_dd_depth_rolling_90pct_504d": {"inputs": ["close"], "func": dhr_ext_050_dd_depth_rolling_90pct_504d},
    "dhr_ext_051_dd_depth_iqr_252d": {"inputs": ["close"], "func": dhr_ext_051_dd_depth_iqr_252d},
    "dhr_ext_052_current_dd_vs_iqr_252d_normalised": {"inputs": ["close"], "func": dhr_ext_052_current_dd_vs_iqr_252d_normalised},
    "dhr_ext_053_dd_depth_skew_252d": {"inputs": ["close"], "func": dhr_ext_053_dd_depth_skew_252d},
    "dhr_ext_054_dd_depth_kurtosis_252d": {"inputs": ["close"], "func": dhr_ext_054_dd_depth_kurtosis_252d},
    "dhr_ext_055_dd_depth_ewm_21d": {"inputs": ["close"], "func": dhr_ext_055_dd_depth_ewm_21d},
    "dhr_ext_056_dd_depth_multi_window_rank_avg": {"inputs": ["close"], "func": dhr_ext_056_dd_depth_multi_window_rank_avg},
    "dhr_ext_057_dd_depth_all_windows_worst_flag": {"inputs": ["close"], "func": dhr_ext_057_dd_depth_all_windows_worst_flag},
    "dhr_ext_058_dd_depth_expanding_and_1yr_both_top10pct_flag": {"inputs": ["close"], "func": dhr_ext_058_dd_depth_expanding_and_1yr_both_top10pct_flag},
    "dhr_ext_059_dd_capitulation_composite_v2": {"inputs": ["close"], "func": dhr_ext_059_dd_capitulation_composite_v2},
    "dhr_ext_060_dd_extreme_flag_any_window": {"inputs": ["close"], "func": dhr_ext_060_dd_extreme_flag_any_window},
    "dhr_ext_061_low_price_expanding_pctrank": {"inputs": ["low"], "func": dhr_ext_061_low_price_expanding_pctrank},
    "dhr_ext_062_low_price_rolling_pctrank_252d": {"inputs": ["low"], "func": dhr_ext_062_low_price_rolling_pctrank_252d},
    "dhr_ext_063_low_price_rolling_pctrank_504d": {"inputs": ["low"], "func": dhr_ext_063_low_price_rolling_pctrank_504d},
    "dhr_ext_064_close_vs_expanding_low_z_score": {"inputs": ["close"], "func": dhr_ext_064_close_vs_expanding_low_z_score},
    "dhr_ext_065_dd_depth_vs_expanding_25pct_excess": {"inputs": ["close"], "func": dhr_ext_065_dd_depth_vs_expanding_25pct_excess},
    "dhr_ext_066_dd_depth_vs_expanding_50pct_excess": {"inputs": ["close"], "func": dhr_ext_066_dd_depth_vs_expanding_50pct_excess},
    "dhr_ext_067_dd_depth_normalised_by_expanding_iqr": {"inputs": ["close"], "func": dhr_ext_067_dd_depth_normalised_by_expanding_iqr},
    "dhr_ext_068_fraction_252d_close_below_expanding_median": {"inputs": ["close"], "func": dhr_ext_068_fraction_252d_close_below_expanding_median},
    "dhr_ext_069_fraction_252d_dd_depth_above_current": {"inputs": ["close"], "func": dhr_ext_069_fraction_252d_dd_depth_above_current},
    "dhr_ext_070_dd_depth_momentum_5d_vs_expanding_rank": {"inputs": ["close"], "func": dhr_ext_070_dd_depth_momentum_5d_vs_expanding_rank},
    "dhr_ext_071_dd_depth_momentum_21d_vs_expanding_rank": {"inputs": ["close"], "func": dhr_ext_071_dd_depth_momentum_21d_vs_expanding_rank},
    "dhr_ext_072_is_price_in_lowest_decile_expanding": {"inputs": ["close"], "func": dhr_ext_072_is_price_in_lowest_decile_expanding},
    "dhr_ext_073_is_price_in_lowest_quintile_expanding": {"inputs": ["close"], "func": dhr_ext_073_is_price_in_lowest_quintile_expanding},
    "dhr_ext_074_dd_depth_and_duration_both_top10pct_expanding": {"inputs": ["close"], "func": dhr_ext_074_dd_depth_and_duration_both_top10pct_expanding},
    "dhr_ext_075_dd_history_rank_final_composite": {"inputs": ["close"], "func": dhr_ext_075_dd_history_rank_final_composite},
}
