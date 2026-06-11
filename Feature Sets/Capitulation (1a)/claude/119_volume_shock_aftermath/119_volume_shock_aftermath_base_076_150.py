"""
119_volume_shock_aftermath — Base Features 076-150
Domain: volume-shock aftermath — deeper characterization of volume behavior and
        price dynamics in the elapsed days following prior shock events
Includes: VWAP-relative measures, high-low range on shock days, shock day
          bar morphology aftermath, volume-price correlation post-shock,
          dollar-volume shock metrics, multi-threshold shock composites
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

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


def _vol_zscore(volume: pd.Series, w: int) -> pd.Series:
    """Z-score of volume relative to its rolling mean/std over w days."""
    m = _rolling_mean(volume, w)
    s = _rolling_std(volume, w)
    return _safe_div(volume - m, s.clip(lower=_EPS))


def _shock_flag(volume: pd.Series, w: int, z_thresh: float = 2.0) -> pd.Series:
    """Binary flag: volume z-score > z_thresh within rolling w-day window."""
    return (_vol_zscore(volume, w) > z_thresh).astype(float)


def _dollar_volume(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume = close * volume."""
    return close * volume


def _typical_price(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Typical price = (high + low + close) / 3."""
    return (high + low + close) / 3.0


def _days_since_last_shock(volume: pd.Series, w: int, z_thresh: float = 2.0) -> pd.Series:
    """Days elapsed since the most recent shock day (0 = today is shock)."""
    flag = _shock_flag(volume, w, z_thresh)
    idx = pd.Series(np.arange(len(flag), dtype=float), index=flag.index)
    last = idx.where(flag == 1.0).ffill().fillna(-1.0)
    elapsed = idx - last
    return elapsed.where(last >= 0.0, np.nan)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Dollar-volume shock metrics ---

def vsa_076_dollar_vol_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of dollar volume (close*volume) vs 21-day baseline."""
    dv = _dollar_volume(close, volume)
    return _vol_zscore(dv, _TD_MON)


def vsa_077_dollar_vol_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of dollar volume vs 63-day baseline."""
    dv = _dollar_volume(close, volume)
    return _vol_zscore(dv, _TD_QTR)


def vsa_078_dollar_vol_shock_flag_21dz2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: dollar-volume shock (z>2 vs 21d window)."""
    dv = _dollar_volume(close, volume)
    return (_vol_zscore(dv, _TD_MON) > 2.0).astype(float)


def vsa_079_dollar_vol_shock_flag_63dz2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: dollar-volume shock (z>2 vs 63d window)."""
    dv = _dollar_volume(close, volume)
    return (_vol_zscore(dv, _TD_QTR) > 2.0).astype(float)


def vsa_080_dollar_vol_days_since_shock_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days since last dollar-volume shock (21d window, z>2)."""
    dv = _dollar_volume(close, volume)
    return _days_since_last_shock(dv, _TD_MON, 2.0)


def vsa_081_dollar_vol_ratio_21d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume / 21-day mean dollar volume."""
    dv = _dollar_volume(close, volume)
    return _safe_div(dv, _rolling_mean(dv, _TD_MON).clip(lower=_EPS))


def vsa_082_dollar_vol_ratio_63d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume / 63-day mean dollar volume."""
    dv = _dollar_volume(close, volume)
    return _safe_div(dv, _rolling_mean(dv, _TD_QTR).clip(lower=_EPS))


def vsa_083_dollar_vol_shock_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of dollar-volume shock days in trailing 63 days (z>2 vs 63d)."""
    dv = _dollar_volume(close, volume)
    flag = (_vol_zscore(dv, _TD_QTR) > 2.0).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def vsa_084_dollar_vol_percentile_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of dollar volume within trailing 63-day distribution."""
    dv = _dollar_volume(close, volume)
    return dv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def vsa_085_dollar_vol_decay_since_shock(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume / dollar volume on last shock day (21d/z2 shock)."""
    dv = _dollar_volume(close, volume)
    flag = _shock_flag(volume, _TD_MON, 2.0)
    shock_dv = dv.where(flag == 1.0).ffill()
    return _safe_div(dv, shock_dv.clip(lower=_EPS))


# --- Group I (086-095): High-low range and bar morphology on/after shock days ---

def vsa_086_range_on_shock_day_21dz2(close: pd.Series, high: pd.Series,
                                      low: pd.Series, volume: pd.Series) -> pd.Series:
    """High-low range on last shock day (21d/z2) divided by close."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    bar_range = _safe_div(high - low, close.clip(lower=_EPS))
    return bar_range.where(flag == 1.0).ffill()


def vsa_087_range_ratio_post_shock(close: pd.Series, high: pd.Series,
                                    low: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's bar range / bar range on last shock day (21d/z2)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    bar_range = high - low
    shock_range = bar_range.where(flag == 1.0).ffill()
    return _safe_div(bar_range, shock_range.clip(lower=_EPS))


def vsa_088_close_location_on_shock_day(close: pd.Series, high: pd.Series,
                                         low: pd.Series, volume: pd.Series) -> pd.Series:
    """Close location value on last shock day: (close-low)/(high-low) 0-1."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    hl = (high - low).replace(0, np.nan)
    cl = _safe_div(close - low, hl)
    return cl.where(flag == 1.0).ffill()


def vsa_089_shock_down_bar_flag(close: pd.Series, high: pd.Series,
                                 low: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: last shock day was a down bar (close < open or close < prev close)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    down = (close < close.shift(1)).astype(float)
    shock_down = (flag == 1.0) & (down == 1.0)
    return shock_down.astype(float).where(flag == 1.0).ffill().fillna(0.0)


def vsa_090_post_shock_range_compression_5d(close: pd.Series, high: pd.Series,
                                              low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day mean bar range (normalized by close) after shock — range compression flag."""
    bar_range = _safe_div(high - low, close.clip(lower=_EPS))
    return _rolling_mean(bar_range, _TD_WEEK)


def vsa_091_shock_day_lower_wick_21dz2(close: pd.Series, high: pd.Series,
                                        low: pd.Series, open_: pd.Series,
                                        volume: pd.Series) -> pd.Series:
    """Lower wick size on last shock day as fraction of range (21d/z2)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    body_low = pd.concat([close, open_], axis=1).min(axis=1)
    hl = (high - low).replace(0, np.nan)
    lower_wick = _safe_div(body_low - low, hl)
    return lower_wick.where(flag == 1.0).ffill()


def vsa_092_avg_range_5d_vs_shock_day_range(close: pd.Series, high: pd.Series,
                                              low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day avg bar range / shock-day bar range (21d/z2); < 1 means range compressed."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    bar_range = high - low
    shock_range = bar_range.where(flag == 1.0).ffill()
    return _safe_div(_rolling_mean(bar_range, _TD_WEEK), shock_range.clip(lower=_EPS))


def vsa_093_high_low_ratio_post_shock_21d(close: pd.Series, high: pd.Series,
                                           low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day mean (high/low ratio - 1) measuring volatility in aftermath window."""
    hl_ratio = _safe_div(high, low.clip(lower=_EPS)) - 1.0
    return _rolling_mean(hl_ratio, _TD_MON)


def vsa_094_shock_day_return_magnitude_21dz2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Absolute return on last shock day (21d/z2) — size of the shock-day move."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    ret_abs = close.pct_change(1).abs()
    return ret_abs.where(flag == 1.0).ffill()


def vsa_095_shock_day_negative_close_21dz2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Magnitude of negative return on last shock day (0 if positive close)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    neg_ret = close.pct_change(1).clip(upper=0.0).abs()
    return neg_ret.where(flag == 1.0).ffill()


# --- Group J (096-105): Volume-price correlation post-shock ---

def vsa_096_vol_price_corr_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day correlation between volume and close (volume chasing price)."""
    return volume.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).corr(close)


def vsa_097_vol_price_corr_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day correlation between volume and close."""
    return volume.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).corr(close)


def vsa_098_vol_ret_corr_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day correlation between volume and daily returns."""
    ret = close.pct_change(1)
    return volume.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).corr(ret)


def vsa_099_vol_ret_corr_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day correlation between volume and daily returns."""
    ret = close.pct_change(1)
    return volume.rolling(_TD_QTR, min_periods=max(10, _TD_QTR // 2)).corr(ret)


def vsa_100_vol_neg_ret_comovement_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days in 21d with both high volume (>1.2x mean) and negative return."""
    high_vol = (_safe_div(volume, _rolling_mean(volume, _TD_MON).clip(lower=_EPS)) > 1.2).astype(float)
    neg_ret = (close.pct_change(1) < 0.0).astype(float)
    return _rolling_sum(high_vol * neg_ret, _TD_MON)


def vsa_101_vol_neg_ret_comovement_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days in 63d with both high volume (>1.2x mean) and negative return."""
    high_vol = (_safe_div(volume, _rolling_mean(volume, _TD_QTR).clip(lower=_EPS)) > 1.2).astype(float)
    neg_ret = (close.pct_change(1) < 0.0).astype(float)
    return _rolling_sum(high_vol * neg_ret, _TD_QTR)


def vsa_102_shock_vol_neg_ret_product_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (vol_zscore * negative_return) over 21 days."""
    z = _vol_zscore(volume, _TD_MON).clip(lower=0.0)
    neg_ret = close.pct_change(1).clip(upper=0.0).abs()
    return _rolling_sum(z * neg_ret, _TD_MON)


def vsa_103_shock_vol_neg_ret_product_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (vol_zscore * negative_return) over 63 days."""
    z = _vol_zscore(volume, _TD_QTR).clip(lower=0.0)
    neg_ret = close.pct_change(1).clip(upper=0.0).abs()
    return _rolling_sum(z * neg_ret, _TD_QTR)


def vsa_104_obv_21d_trend(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV 21-day linear slope normalized by average OBV (negative = bearish)."""
    obv = (np.sign(close.diff(1)) * volume).fillna(0.0).cumsum()
    def slope(x):
        x = x[~np.isnan(x)]
        if len(x) < 3:
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean(); xm = x.mean()
        num = ((xi - xi_m) * (x - xm)).sum()
        den = ((xi - xi_m) ** 2).sum()
        xm_abs = abs(xm)
        if den == 0 or xm_abs < _EPS:
            return np.nan
        return (num / den) / xm_abs
    return obv.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).apply(slope, raw=True)


def vsa_105_obv_5d_trend(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV 5-day linear slope normalized by average OBV."""
    obv = (np.sign(close.diff(1)) * volume).fillna(0.0).cumsum()
    def slope(x):
        x = x[~np.isnan(x)]
        if len(x) < 2:
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean(); xm = x.mean()
        num = ((xi - xi_m) * (x - xm)).sum()
        den = ((xi - xi_m) ** 2).sum()
        xm_abs = abs(xm)
        if den == 0 or xm_abs < _EPS:
            return np.nan
        return (num / den) / xm_abs
    return obv.rolling(_TD_WEEK, min_periods=2).apply(slope, raw=True)


# --- Group K (106-115): Multi-threshold shock composites ---

def vsa_106_shock_intensity_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of clipped vol z-scores over 21 days (total shock intensity)."""
    z = _vol_zscore(volume, _TD_MON).clip(lower=0.0)
    return _rolling_sum(z, _TD_MON)


def vsa_107_shock_intensity_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of clipped vol z-scores over 63 days."""
    z = _vol_zscore(volume, _TD_QTR).clip(lower=0.0)
    return _rolling_sum(z, _TD_QTR)


def vsa_108_shock_intensity_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of clipped vol z-scores over 252 days."""
    z = _vol_zscore(volume, _TD_QTR).clip(lower=0.0)
    return _rolling_sum(z, _TD_YEAR)


def vsa_109_peak_shock_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum vol z-score in trailing 21 days (peak shock intensity)."""
    z = _vol_zscore(volume, _TD_MON)
    return _rolling_max(z, _TD_MON)


def vsa_110_peak_shock_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Maximum vol z-score in trailing 63 days."""
    z = _vol_zscore(volume, _TD_QTR)
    return _rolling_max(z, _TD_QTR)


def vsa_111_shock_ratio_z2_vs_z3_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of z>3 shocks to z>2 shocks in trailing 63 days (severity fraction)."""
    cnt2 = _rolling_sum(_shock_flag(volume, _TD_QTR, 2.0), _TD_QTR)
    cnt3 = _rolling_sum(_shock_flag(volume, _TD_QTR, 3.0), _TD_QTR)
    return _safe_div(cnt3, cnt2.clip(lower=_EPS))


def vsa_112_shock_expanding_count_z2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding all-time count of volume-shock days (63d/z2)."""
    return _shock_flag(volume, _TD_QTR, 2.0).expanding(min_periods=1).sum()


def vsa_113_vol_zscore_5d_max(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max vol z-score (21d window) in trailing 5 days."""
    z = _vol_zscore(volume, _TD_MON)
    return _rolling_max(z, _TD_WEEK)


def vsa_114_vol_zscore_21d_percentile_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of today's vol z-score (21d) within trailing 252 days."""
    z = _vol_zscore(volume, _TD_MON)
    return z.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vsa_115_multiple_shock_windows_agreement(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: shock detected in both 21d and 63d windows simultaneously."""
    f21 = _shock_flag(volume, _TD_MON, 2.0)
    f63 = _shock_flag(volume, _TD_QTR, 2.0)
    return ((f21 == 1.0) & (f63 == 1.0)).astype(float)


# --- Group L (116-125): Typical-price weighted volume aftermath ---

def vsa_116_vwap_21d(close: pd.Series, high: pd.Series,
                      low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day VWAP (volume-weighted average typical price)."""
    tp = _typical_price(high, low, close)
    return _safe_div(_rolling_sum(tp * volume, _TD_MON),
                     _rolling_sum(volume, _TD_MON).clip(lower=_EPS))


def vsa_117_close_vs_vwap_21d(close: pd.Series, high: pd.Series,
                                low: pd.Series, volume: pd.Series) -> pd.Series:
    """Close relative to 21-day VWAP: (close - vwap) / vwap."""
    tp = _typical_price(high, low, close)
    vwap = _safe_div(_rolling_sum(tp * volume, _TD_MON),
                     _rolling_sum(volume, _TD_MON).clip(lower=_EPS))
    return _safe_div(close - vwap, vwap.clip(lower=_EPS))


def vsa_118_close_vs_vwap_63d(close: pd.Series, high: pd.Series,
                                low: pd.Series, volume: pd.Series) -> pd.Series:
    """Close relative to 63-day VWAP: (close - vwap) / vwap."""
    tp = _typical_price(high, low, close)
    vwap = _safe_div(_rolling_sum(tp * volume, _TD_QTR),
                     _rolling_sum(volume, _TD_QTR).clip(lower=_EPS))
    return _safe_div(close - vwap, vwap.clip(lower=_EPS))


def vsa_119_shock_day_vwap_deviation(close: pd.Series, high: pd.Series,
                                      low: pd.Series, volume: pd.Series) -> pd.Series:
    """Deviation of close from 21d VWAP on last shock day (21d/z2)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    tp = _typical_price(high, low, close)
    vwap = _safe_div(_rolling_sum(tp * volume, _TD_MON),
                     _rolling_sum(volume, _TD_MON).clip(lower=_EPS))
    dev = _safe_div(close - vwap, vwap.clip(lower=_EPS))
    return dev.where(flag == 1.0).ffill()


def vsa_120_vol_weighted_avg_return_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average daily return over trailing 21 days."""
    ret = close.pct_change(1).fillna(0.0)
    return _safe_div(_rolling_sum(ret * volume, _TD_MON),
                     _rolling_sum(volume, _TD_MON).clip(lower=_EPS))


def vsa_121_vol_weighted_avg_return_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average daily return over trailing 63 days."""
    ret = close.pct_change(1).fillna(0.0)
    return _safe_div(_rolling_sum(ret * volume, _TD_QTR),
                     _rolling_sum(volume, _TD_QTR).clip(lower=_EPS))


def vsa_122_vol_weighted_neg_return_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average of negative daily returns over 21 days (down-pressure)."""
    neg_ret = close.pct_change(1).clip(upper=0.0)
    return _safe_div(_rolling_sum(neg_ret * volume, _TD_MON),
                     _rolling_sum(volume, _TD_MON).clip(lower=_EPS))


def vsa_123_vol_weighted_neg_return_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average of negative daily returns over 63 days."""
    neg_ret = close.pct_change(1).clip(upper=0.0)
    return _safe_div(_rolling_sum(neg_ret * volume, _TD_QTR),
                     _rolling_sum(volume, _TD_QTR).clip(lower=_EPS))


def vsa_124_shock_day_typical_price_vs_close(close: pd.Series, high: pd.Series,
                                              low: pd.Series, volume: pd.Series) -> pd.Series:
    """Typical price vs close on last shock day (positive = closed below midpoint)."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    tp = _typical_price(high, low, close)
    diff = _safe_div(tp - close, close.clip(lower=_EPS))
    return diff.where(flag == 1.0).ffill()


def vsa_125_post_shock_close_vs_vwap_21d(close: pd.Series, high: pd.Series,
                                          low: pd.Series, volume: pd.Series) -> pd.Series:
    """Days in trailing 21d where close < 21d VWAP (below water)."""
    tp = _typical_price(high, low, close)
    vwap = _safe_div(_rolling_sum(tp * volume, _TD_MON),
                     _rolling_sum(volume, _TD_MON).clip(lower=_EPS))
    below = (close < vwap).astype(float)
    return _rolling_sum(below, _TD_MON)


# --- Group M (126-135): Relative volume normalization and regime ---

def vsa_126_vol_norm_expanding_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume / expanding-mean volume (long-term relative volume)."""
    exp_mean = volume.expanding(min_periods=5).mean()
    return _safe_div(volume, exp_mean.clip(lower=_EPS))


def vsa_127_vol_21d_mean_vs_252d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day mean volume / 252-day mean volume (short-vs-long regime)."""
    return _safe_div(_rolling_mean(volume, _TD_MON),
                     _rolling_mean(volume, _TD_YEAR).clip(lower=_EPS))


def vsa_128_vol_63d_mean_vs_252d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day mean volume / 252-day mean volume."""
    return _safe_div(_rolling_mean(volume, _TD_QTR),
                     _rolling_mean(volume, _TD_YEAR).clip(lower=_EPS))


def vsa_129_vol_5d_mean_vs_21d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day mean volume / 21-day mean volume (ultra-short regime)."""
    return _safe_div(_rolling_mean(volume, _TD_WEEK),
                     _rolling_mean(volume, _TD_MON).clip(lower=_EPS))


def vsa_130_vol_expanding_percentile_rank(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of today's volume."""
    return volume.expanding(min_periods=5).rank(pct=True)


def vsa_131_vol_zscore_21d_ewm5(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day EWM of 21-day volume z-score (smoothed shock indicator)."""
    z = _vol_zscore(volume, _TD_MON)
    return _ewm_mean(z, _TD_WEEK)


def vsa_132_vol_zscore_63d_ewm21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day EWM of 63-day volume z-score."""
    z = _vol_zscore(volume, _TD_QTR)
    return _ewm_mean(z, _TD_MON)


def vsa_133_vol_spike_to_trough_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max volume / min volume in 21-day window (spike-to-trough ratio)."""
    mx = _rolling_max(volume, _TD_MON)
    mn = _rolling_min(volume, _TD_MON)
    return _safe_div(mx, mn.clip(lower=_EPS))


def vsa_134_vol_spike_to_trough_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max volume / min volume in 63-day window."""
    mx = _rolling_max(volume, _TD_QTR)
    mn = _rolling_min(volume, _TD_QTR)
    return _safe_div(mx, mn.clip(lower=_EPS))


def vsa_135_vol_zscore_252d_percentile_rank(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 252d vol z-score within its 252d distribution."""
    z = _vol_zscore(volume, _TD_YEAR)
    return z.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group N (136-145): Post-shock OBV and flow metrics ---

def vsa_136_obv_vs_21d_mean(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV relative to its 21-day mean (OBV momentum)."""
    obv = (np.sign(close.diff(1)) * volume).fillna(0.0).cumsum()
    return _safe_div(obv, _rolling_mean(obv, _TD_MON).abs().clip(lower=_EPS))


def vsa_137_obv_21d_change(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day change in OBV (cumulative volume direction over month)."""
    obv = (np.sign(close.diff(1)) * volume).fillna(0.0).cumsum()
    return obv.diff(_TD_MON)


def vsa_138_obv_5d_change(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day change in OBV."""
    obv = (np.sign(close.diff(1)) * volume).fillna(0.0).cumsum()
    return obv.diff(_TD_WEEK)


def vsa_139_pos_vol_fraction_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of volume in 21d that occurred on up-days (positive flow)."""
    up = (close.diff(1) > 0.0).astype(float)
    up_vol = _rolling_sum(up * volume, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    return _safe_div(up_vol, total_vol.clip(lower=_EPS))


def vsa_140_neg_vol_fraction_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of volume in 21d on down-days (selling pressure)."""
    dn = (close.diff(1) < 0.0).astype(float)
    dn_vol = _rolling_sum(dn * volume, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    return _safe_div(dn_vol, total_vol.clip(lower=_EPS))


def vsa_141_neg_vol_fraction_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of volume in 63d on down-days."""
    dn = (close.diff(1) < 0.0).astype(float)
    dn_vol = _rolling_sum(dn * volume, _TD_QTR)
    total_vol = _rolling_sum(volume, _TD_QTR)
    return _safe_div(dn_vol, total_vol.clip(lower=_EPS))


def vsa_142_up_down_vol_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Up-day volume / down-day volume ratio over 21 days."""
    up_vol = _rolling_sum((close.diff(1) > 0.0).astype(float) * volume, _TD_MON)
    dn_vol = _rolling_sum((close.diff(1) < 0.0).astype(float) * volume, _TD_MON)
    return _safe_div(up_vol, dn_vol.clip(lower=_EPS))


def vsa_143_up_down_vol_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Up-day volume / down-day volume ratio over 63 days."""
    up_vol = _rolling_sum((close.diff(1) > 0.0).astype(float) * volume, _TD_QTR)
    dn_vol = _rolling_sum((close.diff(1) < 0.0).astype(float) * volume, _TD_QTR)
    return _safe_div(up_vol, dn_vol.clip(lower=_EPS))


def vsa_144_shock_day_obv_change(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV 1-day change on last shock day (21d/z2) — direction of shock flow."""
    flag = _shock_flag(volume, _TD_MON, 2.0)
    obv_delta = np.sign(close.diff(1)) * volume
    return obv_delta.where(flag == 1.0).ffill()


def vsa_145_post_shock_obv_5d_change(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day cumulative OBV change (flow direction in immediate aftermath)."""
    obv = (np.sign(close.diff(1)) * volume).fillna(0.0).cumsum()
    return obv.diff(_TD_WEEK)


# --- Group O (146-150): Miscellaneous aftermath signatures ---

def vsa_146_vol_zscore_21d_abs_max_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of today's vol z-score (21d) to its 252-day absolute maximum."""
    z = _vol_zscore(volume, _TD_MON)
    max252 = z.rolling(_TD_YEAR, min_periods=_TD_QTR).max()
    return _safe_div(z, max252.clip(lower=_EPS))


def vsa_147_shock_sequence_flag_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: 3+ shock days (21d/z2) have occurred in trailing 63 days."""
    cnt = _rolling_sum(_shock_flag(volume, _TD_MON, 2.0), _TD_QTR)
    return (cnt >= 3.0).astype(float)


def vsa_148_post_shock_price_vol_divergence(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price declining while volume also declining (divergence score = -1 * both trends)."""
    price_trend = close.pct_change(_TD_WEEK)
    vol_trend = _safe_div(_rolling_mean(volume, _TD_WEEK),
                          _rolling_mean(volume, _TD_MON).clip(lower=_EPS)) - 1.0
    # Both declining = negative * negative = positive score; capitulation-aligned
    return ((-price_trend).clip(lower=0.0)) * ((-vol_trend).clip(lower=0.0))


def vsa_149_shock_count_z2_vs_z3_expanding(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding ratio: severe shocks (z>3) / all shocks (z>2) — lifetime severity."""
    cnt2 = _shock_flag(volume, _TD_QTR, 2.0).expanding(min_periods=1).sum()
    cnt3 = _shock_flag(volume, _TD_QTR, 3.0).expanding(min_periods=1).sum()
    return _safe_div(cnt3, cnt2.clip(lower=_EPS))


def vsa_150_vol_shock_aftermath_net_score(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Net aftermath score: shock_intensity_21d * neg_vol_fraction_21d * (1 - vol_decay)."""
    intensity = _rolling_sum(_vol_zscore(volume, _TD_MON).clip(lower=0.0), _TD_MON)
    dn = (close.diff(1) < 0.0).astype(float)
    dn_vol = _rolling_sum(dn * volume, _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    neg_frac = _safe_div(dn_vol, total_vol.clip(lower=_EPS))
    flag = _shock_flag(volume, _TD_MON, 2.0)
    shock_vol = volume.where(flag == 1.0).ffill()
    decay = _safe_div(volume, shock_vol.clip(lower=_EPS)).fillna(1.0)
    return intensity * neg_frac * (1.0 - decay.clip(upper=1.0))


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_SHOCK_AFTERMATH_REGISTRY_076_150 = {
    "vsa_076_dollar_vol_zscore_21d": {"inputs": ["close", "volume"], "func": vsa_076_dollar_vol_zscore_21d},
    "vsa_077_dollar_vol_zscore_63d": {"inputs": ["close", "volume"], "func": vsa_077_dollar_vol_zscore_63d},
    "vsa_078_dollar_vol_shock_flag_21dz2": {"inputs": ["close", "volume"], "func": vsa_078_dollar_vol_shock_flag_21dz2},
    "vsa_079_dollar_vol_shock_flag_63dz2": {"inputs": ["close", "volume"], "func": vsa_079_dollar_vol_shock_flag_63dz2},
    "vsa_080_dollar_vol_days_since_shock_21d": {"inputs": ["close", "volume"], "func": vsa_080_dollar_vol_days_since_shock_21d},
    "vsa_081_dollar_vol_ratio_21d_mean": {"inputs": ["close", "volume"], "func": vsa_081_dollar_vol_ratio_21d_mean},
    "vsa_082_dollar_vol_ratio_63d_mean": {"inputs": ["close", "volume"], "func": vsa_082_dollar_vol_ratio_63d_mean},
    "vsa_083_dollar_vol_shock_count_63d": {"inputs": ["close", "volume"], "func": vsa_083_dollar_vol_shock_count_63d},
    "vsa_084_dollar_vol_percentile_rank_63d": {"inputs": ["close", "volume"], "func": vsa_084_dollar_vol_percentile_rank_63d},
    "vsa_085_dollar_vol_decay_since_shock": {"inputs": ["close", "volume"], "func": vsa_085_dollar_vol_decay_since_shock},
    "vsa_086_range_on_shock_day_21dz2": {"inputs": ["close", "high", "low", "volume"], "func": vsa_086_range_on_shock_day_21dz2},
    "vsa_087_range_ratio_post_shock": {"inputs": ["close", "high", "low", "volume"], "func": vsa_087_range_ratio_post_shock},
    "vsa_088_close_location_on_shock_day": {"inputs": ["close", "high", "low", "volume"], "func": vsa_088_close_location_on_shock_day},
    "vsa_089_shock_down_bar_flag": {"inputs": ["close", "high", "low", "volume"], "func": vsa_089_shock_down_bar_flag},
    "vsa_090_post_shock_range_compression_5d": {"inputs": ["close", "high", "low", "volume"], "func": vsa_090_post_shock_range_compression_5d},
    "vsa_091_shock_day_lower_wick_21dz2": {"inputs": ["close", "high", "low", "open", "volume"], "func": vsa_091_shock_day_lower_wick_21dz2},
    "vsa_092_avg_range_5d_vs_shock_day_range": {"inputs": ["close", "high", "low", "volume"], "func": vsa_092_avg_range_5d_vs_shock_day_range},
    "vsa_093_high_low_ratio_post_shock_21d": {"inputs": ["close", "high", "low", "volume"], "func": vsa_093_high_low_ratio_post_shock_21d},
    "vsa_094_shock_day_return_magnitude_21dz2": {"inputs": ["close", "volume"], "func": vsa_094_shock_day_return_magnitude_21dz2},
    "vsa_095_shock_day_negative_close_21dz2": {"inputs": ["close", "volume"], "func": vsa_095_shock_day_negative_close_21dz2},
    "vsa_096_vol_price_corr_21d": {"inputs": ["close", "volume"], "func": vsa_096_vol_price_corr_21d},
    "vsa_097_vol_price_corr_63d": {"inputs": ["close", "volume"], "func": vsa_097_vol_price_corr_63d},
    "vsa_098_vol_ret_corr_21d": {"inputs": ["close", "volume"], "func": vsa_098_vol_ret_corr_21d},
    "vsa_099_vol_ret_corr_63d": {"inputs": ["close", "volume"], "func": vsa_099_vol_ret_corr_63d},
    "vsa_100_vol_neg_ret_comovement_21d": {"inputs": ["close", "volume"], "func": vsa_100_vol_neg_ret_comovement_21d},
    "vsa_101_vol_neg_ret_comovement_63d": {"inputs": ["close", "volume"], "func": vsa_101_vol_neg_ret_comovement_63d},
    "vsa_102_shock_vol_neg_ret_product_21d": {"inputs": ["close", "volume"], "func": vsa_102_shock_vol_neg_ret_product_21d},
    "vsa_103_shock_vol_neg_ret_product_63d": {"inputs": ["close", "volume"], "func": vsa_103_shock_vol_neg_ret_product_63d},
    "vsa_104_obv_21d_trend": {"inputs": ["close", "volume"], "func": vsa_104_obv_21d_trend},
    "vsa_105_obv_5d_trend": {"inputs": ["close", "volume"], "func": vsa_105_obv_5d_trend},
    "vsa_106_shock_intensity_21d": {"inputs": ["close", "volume"], "func": vsa_106_shock_intensity_21d},
    "vsa_107_shock_intensity_63d": {"inputs": ["close", "volume"], "func": vsa_107_shock_intensity_63d},
    "vsa_108_shock_intensity_252d": {"inputs": ["close", "volume"], "func": vsa_108_shock_intensity_252d},
    "vsa_109_peak_shock_zscore_21d": {"inputs": ["close", "volume"], "func": vsa_109_peak_shock_zscore_21d},
    "vsa_110_peak_shock_zscore_63d": {"inputs": ["close", "volume"], "func": vsa_110_peak_shock_zscore_63d},
    "vsa_111_shock_ratio_z2_vs_z3_63d": {"inputs": ["close", "volume"], "func": vsa_111_shock_ratio_z2_vs_z3_63d},
    "vsa_112_shock_expanding_count_z2": {"inputs": ["close", "volume"], "func": vsa_112_shock_expanding_count_z2},
    "vsa_113_vol_zscore_5d_max": {"inputs": ["close", "volume"], "func": vsa_113_vol_zscore_5d_max},
    "vsa_114_vol_zscore_21d_percentile_rank_252d": {"inputs": ["close", "volume"], "func": vsa_114_vol_zscore_21d_percentile_rank_252d},
    "vsa_115_multiple_shock_windows_agreement": {"inputs": ["close", "volume"], "func": vsa_115_multiple_shock_windows_agreement},
    "vsa_116_vwap_21d": {"inputs": ["close", "high", "low", "volume"], "func": vsa_116_vwap_21d},
    "vsa_117_close_vs_vwap_21d": {"inputs": ["close", "high", "low", "volume"], "func": vsa_117_close_vs_vwap_21d},
    "vsa_118_close_vs_vwap_63d": {"inputs": ["close", "high", "low", "volume"], "func": vsa_118_close_vs_vwap_63d},
    "vsa_119_shock_day_vwap_deviation": {"inputs": ["close", "high", "low", "volume"], "func": vsa_119_shock_day_vwap_deviation},
    "vsa_120_vol_weighted_avg_return_21d": {"inputs": ["close", "volume"], "func": vsa_120_vol_weighted_avg_return_21d},
    "vsa_121_vol_weighted_avg_return_63d": {"inputs": ["close", "volume"], "func": vsa_121_vol_weighted_avg_return_63d},
    "vsa_122_vol_weighted_neg_return_21d": {"inputs": ["close", "volume"], "func": vsa_122_vol_weighted_neg_return_21d},
    "vsa_123_vol_weighted_neg_return_63d": {"inputs": ["close", "volume"], "func": vsa_123_vol_weighted_neg_return_63d},
    "vsa_124_shock_day_typical_price_vs_close": {"inputs": ["close", "high", "low", "volume"], "func": vsa_124_shock_day_typical_price_vs_close},
    "vsa_125_post_shock_close_vs_vwap_21d": {"inputs": ["close", "high", "low", "volume"], "func": vsa_125_post_shock_close_vs_vwap_21d},
    "vsa_126_vol_norm_expanding_mean": {"inputs": ["close", "volume"], "func": vsa_126_vol_norm_expanding_mean},
    "vsa_127_vol_21d_mean_vs_252d_mean": {"inputs": ["close", "volume"], "func": vsa_127_vol_21d_mean_vs_252d_mean},
    "vsa_128_vol_63d_mean_vs_252d_mean": {"inputs": ["close", "volume"], "func": vsa_128_vol_63d_mean_vs_252d_mean},
    "vsa_129_vol_5d_mean_vs_21d_mean": {"inputs": ["close", "volume"], "func": vsa_129_vol_5d_mean_vs_21d_mean},
    "vsa_130_vol_expanding_percentile_rank": {"inputs": ["close", "volume"], "func": vsa_130_vol_expanding_percentile_rank},
    "vsa_131_vol_zscore_21d_ewm5": {"inputs": ["close", "volume"], "func": vsa_131_vol_zscore_21d_ewm5},
    "vsa_132_vol_zscore_63d_ewm21": {"inputs": ["close", "volume"], "func": vsa_132_vol_zscore_63d_ewm21},
    "vsa_133_vol_spike_to_trough_ratio_21d": {"inputs": ["close", "volume"], "func": vsa_133_vol_spike_to_trough_ratio_21d},
    "vsa_134_vol_spike_to_trough_ratio_63d": {"inputs": ["close", "volume"], "func": vsa_134_vol_spike_to_trough_ratio_63d},
    "vsa_135_vol_zscore_252d_percentile_rank": {"inputs": ["close", "volume"], "func": vsa_135_vol_zscore_252d_percentile_rank},
    "vsa_136_obv_vs_21d_mean": {"inputs": ["close", "volume"], "func": vsa_136_obv_vs_21d_mean},
    "vsa_137_obv_21d_change": {"inputs": ["close", "volume"], "func": vsa_137_obv_21d_change},
    "vsa_138_obv_5d_change": {"inputs": ["close", "volume"], "func": vsa_138_obv_5d_change},
    "vsa_139_pos_vol_fraction_21d": {"inputs": ["close", "volume"], "func": vsa_139_pos_vol_fraction_21d},
    "vsa_140_neg_vol_fraction_21d": {"inputs": ["close", "volume"], "func": vsa_140_neg_vol_fraction_21d},
    "vsa_141_neg_vol_fraction_63d": {"inputs": ["close", "volume"], "func": vsa_141_neg_vol_fraction_63d},
    "vsa_142_up_down_vol_ratio_21d": {"inputs": ["close", "volume"], "func": vsa_142_up_down_vol_ratio_21d},
    "vsa_143_up_down_vol_ratio_63d": {"inputs": ["close", "volume"], "func": vsa_143_up_down_vol_ratio_63d},
    "vsa_144_shock_day_obv_change": {"inputs": ["close", "volume"], "func": vsa_144_shock_day_obv_change},
    "vsa_145_post_shock_obv_5d_change": {"inputs": ["close", "volume"], "func": vsa_145_post_shock_obv_5d_change},
    "vsa_146_vol_zscore_21d_abs_max_252d": {"inputs": ["close", "volume"], "func": vsa_146_vol_zscore_21d_abs_max_252d},
    "vsa_147_shock_sequence_flag_21d": {"inputs": ["close", "volume"], "func": vsa_147_shock_sequence_flag_21d},
    "vsa_148_post_shock_price_vol_divergence": {"inputs": ["close", "volume"], "func": vsa_148_post_shock_price_vol_divergence},
    "vsa_149_shock_count_z2_vs_z3_expanding": {"inputs": ["close", "volume"], "func": vsa_149_shock_count_z2_vs_z3_expanding},
    "vsa_150_vol_shock_aftermath_net_score": {"inputs": ["close", "volume"], "func": vsa_150_vol_shock_aftermath_net_score},
}
