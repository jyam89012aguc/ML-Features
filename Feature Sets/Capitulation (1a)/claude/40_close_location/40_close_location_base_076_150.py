"""
40_close_location — Base Features 076-150
Domain: close's position within the daily range — close location value (CLV)
Covers: CLV persistence, multi-day patterns, volume-weighted CLV, CLV vs
moving-average bands, accumulation/distribution variants, CLV run-length
statistics, cross-window ratios, and capitulation-specific composites.
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond: pd.Series, w: int) -> pd.Series:
    """Maximum consecutive-True run length over trailing w periods."""
    def _max_run(arr):
        mx = 0
        cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return cond.rolling(w, min_periods=max(1, w // 2)).apply(_max_run, raw=True)


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


def _clv_raw(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Core CLV = ((close-low)-(high-close))/(high-low), NaN when range=0."""
    hl = high - low
    return _safe_div((close - low) - (high - close), hl)


def _close_frac(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close as fraction of range: (close-low)/(high-low), in [0,1]."""
    return _safe_div(close - low, high - low)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): CLV OLS slope and trend direction ---

def clv_076_clv_slope_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of CLV over trailing 5 days (short-term CLV trend)."""
    return _linslope(_clv_raw(close, high, low), _TD_WEEK)


def clv_077_clv_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of CLV over trailing 21 days."""
    return _linslope(_clv_raw(close, high, low), _TD_MON)


def clv_078_clv_slope_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of CLV over trailing 63 days."""
    return _linslope(_clv_raw(close, high, low), _TD_QTR)


def clv_079_close_frac_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of close-fraction over trailing 21 days."""
    return _linslope(_close_frac(close, high, low), _TD_MON)


def clv_080_close_frac_slope_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of close-fraction over trailing 63 days."""
    return _linslope(_close_frac(close, high, low), _TD_QTR)


def clv_081_clv_trend_declining_flag_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: 21-day OLS slope of CLV is negative (deteriorating close location)."""
    return (_linslope(_clv_raw(close, high, low), _TD_MON) < 0).astype(float)


def clv_082_clv_trend_improving_flag_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: 21-day OLS slope of CLV is positive (improving close location)."""
    return (_linslope(_clv_raw(close, high, low), _TD_MON) > 0).astype(float)


def clv_083_clv_sma5_vs_sma21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day SMA of CLV minus 21-day SMA (short-vs-medium trend)."""
    clv = _clv_raw(close, high, low)
    return _rolling_mean(clv, _TD_WEEK) - _rolling_mean(clv, _TD_MON)


def clv_084_clv_sma21_vs_sma63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day SMA of CLV minus 63-day SMA (medium-vs-long trend)."""
    clv = _clv_raw(close, high, low)
    return _rolling_mean(clv, _TD_MON) - _rolling_mean(clv, _TD_QTR)


def clv_085_clv_sma63_vs_sma252(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day SMA of CLV minus 252-day SMA (quarterly-vs-annual trend)."""
    clv = _clv_raw(close, high, low)
    return _rolling_mean(clv, _TD_QTR) - _rolling_mean(clv, _TD_YEAR)


# --- Group I (086-095): Volume-weighted CLV (A/D-style) ---

def clv_086_vwclv_cumsum(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding cumulative sum of volume*CLV (Accumulation/Distribution Line)."""
    clv = _clv_raw(close, high, low)
    return (clv * volume).cumsum()


def clv_087_vwclv_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day rolling sum of volume*CLV (short-term A/D pressure)."""
    return _rolling_sum(_clv_raw(close, high, low) * volume, _TD_MON)


def clv_088_vwclv_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day rolling sum of volume*CLV."""
    return _rolling_sum(_clv_raw(close, high, low) * volume, _TD_QTR)


def clv_089_vwclv_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day rolling sum of volume*CLV."""
    return _rolling_sum(_clv_raw(close, high, low) * volume, _TD_YEAR)


def clv_090_vwclv_avg_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day volume-weighted average CLV."""
    clv = _clv_raw(close, high, low)
    return _safe_div(_rolling_sum(clv * volume, _TD_MON), _rolling_sum(volume, _TD_MON))


def clv_091_vwclv_avg_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day volume-weighted average CLV."""
    clv = _clv_raw(close, high, low)
    return _safe_div(_rolling_sum(clv * volume, _TD_QTR), _rolling_sum(volume, _TD_QTR))


def clv_092_vwclv_vs_clv_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day VWCLV minus 21-day plain CLV SMA (volume-weighting effect)."""
    clv = _clv_raw(close, high, low)
    vwavg = _safe_div(_rolling_sum(clv * volume, _TD_MON), _rolling_sum(volume, _TD_MON))
    return vwavg - _rolling_mean(clv, _TD_MON)


def clv_093_vwclv_neg_sum_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day sum of volume*CLV on days when CLV < 0 (distribution pressure)."""
    clv = _clv_raw(close, high, low)
    neg_contrib = (clv * volume).where(clv < 0, 0.0)
    return _rolling_sum(neg_contrib, _TD_MON)


def clv_094_vwclv_pos_sum_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day sum of volume*CLV on days when CLV > 0 (accumulation pressure)."""
    clv = _clv_raw(close, high, low)
    pos_contrib = (clv * volume).where(clv > 0, 0.0)
    return _rolling_sum(pos_contrib, _TD_MON)


def clv_095_vwclv_bull_bear_ratio_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day positive-vol*CLV sum to abs(negative-vol*CLV) sum."""
    clv = _clv_raw(close, high, low)
    pos = _rolling_sum((clv * volume).where(clv > 0, 0.0), _TD_MON)
    neg = _rolling_sum((clv * volume).where(clv < 0, 0.0).abs(), _TD_MON)
    return _safe_div(pos, neg)


# --- Group J (096-105): CLV persistence and autocorrelation ---

def clv_096_clv_1d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """1-day change in CLV (daily CLV velocity)."""
    return _clv_raw(close, high, low).diff(1)


def clv_097_clv_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day change in CLV."""
    return _clv_raw(close, high, low).diff(_TD_WEEK)


def clv_098_clv_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day change in CLV."""
    return _clv_raw(close, high, low).diff(_TD_MON)


def clv_099_close_frac_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day change in close-fraction-of-range."""
    return _close_frac(close, high, low).diff(_TD_WEEK)


def clv_100_close_frac_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day change in close-fraction-of-range."""
    return _close_frac(close, high, low).diff(_TD_MON)


def clv_101_clv_pos_to_neg_flip(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: CLV crossed from positive to negative (bull-to-bear close location)."""
    clv = _clv_raw(close, high, low)
    return ((clv < 0) & (clv.shift(1) >= 0)).astype(float)


def clv_102_clv_neg_to_pos_flip(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: CLV crossed from negative to positive (bear-to-bull close location)."""
    clv = _clv_raw(close, high, low)
    return ((clv > 0) & (clv.shift(1) <= 0)).astype(float)


def clv_103_clv_5d_diff_abs(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Absolute 5-day change in CLV (magnitude of location shift)."""
    return _clv_raw(close, high, low).diff(_TD_WEEK).abs()


def clv_104_clv_persistence_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days in past 21 where CLV same sign as today (sign persistence)."""
    clv = _clv_raw(close, high, low)
    same_sign = ((clv * clv.shift(1)) > 0).astype(float)
    return _rolling_sum(same_sign, _TD_MON)


def clv_105_clv_direction_changes_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of CLV sign changes over trailing 21 days (instability measure)."""
    clv = _clv_raw(close, high, low)
    flip = ((clv * clv.shift(1)) < 0).astype(float)
    return _rolling_sum(flip, _TD_MON)


# --- Group K (106-115): Cross-window ratios and relative CLV ---

def clv_106_clv_sma5_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 5-day CLV SMA within trailing 252 days."""
    sma5 = _rolling_mean(_clv_raw(close, high, low), _TD_WEEK)
    return sma5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def clv_107_clv_sma21_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21-day CLV SMA within trailing 252 days."""
    sma21 = _rolling_mean(_clv_raw(close, high, low), _TD_MON)
    return sma21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def clv_108_clv_ratio_5d_vs_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 5-day avg CLV to 252-day avg CLV (short-vs-long location bias)."""
    clv = _clv_raw(close, high, low)
    return _safe_div(_rolling_mean(clv, _TD_WEEK), _rolling_mean(clv, _TD_YEAR))


def clv_109_clv_ratio_21d_vs_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 21-day avg CLV to 252-day avg CLV."""
    clv = _clv_raw(close, high, low)
    return _safe_div(_rolling_mean(clv, _TD_MON), _rolling_mean(clv, _TD_YEAR))


def clv_110_close_frac_expanding_zscore(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of close-fraction versus full expanding history."""
    cf = _close_frac(close, high, low)
    m = cf.expanding(min_periods=5).mean()
    s = cf.expanding(min_periods=5).std()
    return _safe_div(cf - m, s)


def clv_111_clv_expanding_zscore(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of CLV versus full expanding history."""
    clv = _clv_raw(close, high, low)
    m = clv.expanding(min_periods=5).mean()
    s = clv.expanding(min_periods=5).std()
    return _safe_div(clv - m, s)


def clv_112_clv_range_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Range of CLV over trailing 5 days (max - min)."""
    clv = _clv_raw(close, high, low)
    return _rolling_max(clv, _TD_WEEK) - _rolling_min(clv, _TD_WEEK)


def clv_113_clv_range_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Range of CLV over trailing 21 days (max - min)."""
    clv = _clv_raw(close, high, low)
    return _rolling_max(clv, _TD_MON) - _rolling_min(clv, _TD_MON)


def clv_114_clv_vs_min_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CLV minus its 252-day minimum (distance above worst location)."""
    clv = _clv_raw(close, high, low)
    return clv - _rolling_min(clv, _TD_YEAR)


def clv_115_clv_vs_max_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CLV minus its 252-day maximum (distance below best location)."""
    clv = _clv_raw(close, high, low)
    return clv - _rolling_max(clv, _TD_YEAR)


# --- Group L (116-125): CLV interactions with price trend ---

def clv_116_clv_times_ret_1d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CLV multiplied by 1-day return (location-weighted daily move)."""
    ret = close.pct_change(1)
    return _clv_raw(close, high, low) * ret


def clv_117_clv_times_ret_sign(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CLV times sign of 1-day return (+1/-1/0)."""
    return _clv_raw(close, high, low) * np.sign(close.pct_change(1))


def clv_118_clv_on_down_days_avg_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average CLV on down-price days over trailing 21 days."""
    clv = _clv_raw(close, high, low)
    ret = close.pct_change(1)
    down_clv = clv.where(ret < 0, np.nan)
    return down_clv.rolling(_TD_MON, min_periods=1).mean()


def clv_119_clv_on_up_days_avg_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average CLV on up-price days over trailing 21 days."""
    clv = _clv_raw(close, high, low)
    ret = close.pct_change(1)
    up_clv = clv.where(ret > 0, np.nan)
    return up_clv.rolling(_TD_MON, min_periods=1).mean()


def clv_120_clv_down_vs_up_avg_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio: avg CLV on down days / avg CLV on up days over 21 days."""
    clv = _clv_raw(close, high, low)
    ret = close.pct_change(1)
    down = clv.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    up = clv.where(ret > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(down, up)


def clv_121_clv_on_down_days_avg_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average CLV on down-price days over trailing 63 days."""
    clv = _clv_raw(close, high, low)
    ret = close.pct_change(1)
    return clv.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()


def clv_122_clv_negative_on_down_day_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today is a down-price day AND CLV is negative (weak day)."""
    clv = _clv_raw(close, high, low)
    ret = close.pct_change(1)
    return ((ret < 0) & (clv < 0)).astype(float)


def clv_123_count_weak_days_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days over 21 with both negative return and CLV < 0."""
    clv = _clv_raw(close, high, low)
    ret = close.pct_change(1)
    weak = (ret < 0) & (clv < 0)
    return _rolling_count_true(weak, _TD_MON)


def clv_124_count_weak_days_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days over 63 with both negative return and CLV < 0."""
    clv = _clv_raw(close, high, low)
    ret = close.pct_change(1)
    weak = (ret < 0) & (clv < 0)
    return _rolling_count_true(weak, _TD_QTR)


def clv_125_clv_positive_on_up_day_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today is an up-price day AND CLV is positive (strong bull day)."""
    clv = _clv_raw(close, high, low)
    ret = close.pct_change(1)
    return ((ret > 0) & (clv > 0)).astype(float)


# --- Group M (126-135): CLV relative to Bollinger-band-like bounds ---

def clv_126_clv_bb_upper_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Upper Bollinger band of CLV (mean + 2*std, 21-day)."""
    clv = _clv_raw(close, high, low)
    return _rolling_mean(clv, _TD_MON) + 2.0 * _rolling_std(clv, _TD_MON)


def clv_127_clv_bb_lower_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Lower Bollinger band of CLV (mean - 2*std, 21-day)."""
    clv = _clv_raw(close, high, low)
    return _rolling_mean(clv, _TD_MON) - 2.0 * _rolling_std(clv, _TD_MON)


def clv_128_clv_below_bb_lower_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: CLV below its 21-day lower Bollinger band (extreme bearish close)."""
    clv = _clv_raw(close, high, low)
    lower = _rolling_mean(clv, _TD_MON) - 2.0 * _rolling_std(clv, _TD_MON)
    return (clv < lower).astype(float)


def clv_129_clv_above_bb_upper_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: CLV above its 21-day upper Bollinger band (extreme bullish close)."""
    clv = _clv_raw(close, high, low)
    upper = _rolling_mean(clv, _TD_MON) + 2.0 * _rolling_std(clv, _TD_MON)
    return (clv > upper).astype(float)


def clv_130_clv_within_bb_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CLV normalized within 21-day Bollinger bands: (CLV-lower)/(upper-lower)."""
    clv = _clv_raw(close, high, low)
    m = _rolling_mean(clv, _TD_MON)
    s = _rolling_std(clv, _TD_MON)
    upper = m + 2.0 * s
    lower = m - 2.0 * s
    return _safe_div(clv - lower, upper - lower)


def clv_131_close_frac_bb_lower_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close-fraction below its 21-day lower BB: flag."""
    cf = _close_frac(close, high, low)
    lower = _rolling_mean(cf, _TD_MON) - 2.0 * _rolling_std(cf, _TD_MON)
    return (cf < lower).astype(float)


def clv_132_clv_bb_width_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Width of CLV 21-day Bollinger bands (4*std)."""
    return 4.0 * _rolling_std(_clv_raw(close, high, low), _TD_MON)


def clv_133_clv_bb_width_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Width of CLV 63-day Bollinger bands."""
    return 4.0 * _rolling_std(_clv_raw(close, high, low), _TD_QTR)


def clv_134_clv_below_bb_lower_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: CLV below its 63-day lower Bollinger band."""
    clv = _clv_raw(close, high, low)
    lower = _rolling_mean(clv, _TD_QTR) - 2.0 * _rolling_std(clv, _TD_QTR)
    return (clv < lower).astype(float)


def clv_135_clv_within_bb_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """CLV normalized within 63-day Bollinger bands."""
    clv = _clv_raw(close, high, low)
    m = _rolling_mean(clv, _TD_QTR)
    s = _rolling_std(clv, _TD_QTR)
    upper = m + 2.0 * s
    lower = m - 2.0 * s
    return _safe_div(clv - lower, upper - lower)


# --- Group N (136-145): CLV run-length statistics ---

def clv_136_avg_neg_clv_streak_len_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average length of negative-CLV streaks over trailing 252 days."""
    def _avg_run(arr):
        total = 0
        runs = 0
        cur = 0
        for v in arr:
            if v:
                cur += 1
            else:
                if cur > 0:
                    total += cur
                    runs += 1
                cur = 0
        if cur > 0:
            total += cur
            runs += 1
        return float(total) / float(runs) if runs > 0 else 0.0
    cond = (_clv_raw(close, high, low) < 0)
    return cond.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_avg_run, raw=True)


def clv_137_avg_pos_clv_streak_len_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average length of positive-CLV streaks over trailing 252 days."""
    def _avg_run(arr):
        total = 0
        runs = 0
        cur = 0
        for v in arr:
            if v:
                cur += 1
            else:
                if cur > 0:
                    total += cur
                    runs += 1
                cur = 0
        if cur > 0:
            total += cur
            runs += 1
        return float(total) / float(runs) if runs > 0 else 0.0
    cond = (_clv_raw(close, high, low) > 0)
    return cond.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_avg_run, raw=True)


def clv_138_neg_streak_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Number of distinct negative-CLV streak starts over trailing 252 days."""
    clv = _clv_raw(close, high, low)
    is_neg = (clv < 0).astype(float)
    is_start = (is_neg == 1) & (is_neg.shift(1).fillna(0) == 0)
    return _rolling_sum(is_start.astype(float), _TD_YEAR)


def clv_139_clv_neg_streak_len_norm_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current neg-CLV streak as fraction of 252-day avg neg-CLV streak length."""
    cond = _clv_raw(close, high, low) < 0
    cur = _consec_streak(cond)
    avg = clv_136_avg_neg_clv_streak_len_252d(close, high, low)
    return _safe_div(cur, avg)


def clv_140_consec_neg_clv_norm_21d_avg(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current neg-CLV streak normalized by its 21-day rolling average."""
    cond = _clv_raw(close, high, low) < 0
    cur = _consec_streak(cond)
    avg = _rolling_mean(cur, _TD_MON)
    return _safe_div(cur, avg)


def clv_141_max_neg_clv_streak_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max consecutive negative-CLV streak within trailing 126 days."""
    cond = _clv_raw(close, high, low) < 0
    return _rolling_max_streak(cond, _TD_HALF)


def clv_142_max_near_low_streak_126d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max consecutive near-low close streak within trailing 126 days."""
    cond = _close_frac(close, high, low) <= 0.25
    return _rolling_max_streak(cond, _TD_HALF)


def clv_143_near_low_streak_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of current near-low streak within trailing 252 days."""
    cond = _close_frac(close, high, low) <= 0.25
    cur = _consec_streak(cond)
    return cur.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def clv_144_clv_neg_run_freq_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Frequency of negative-CLV streak starts per 252-day window."""
    clv = _clv_raw(close, high, low)
    is_neg = (clv < 0).astype(float)
    is_start = (is_neg == 1) & (is_neg.shift(1).fillna(0) == 0)
    return _rolling_sum(is_start.astype(float), _TD_YEAR)


def clv_145_clv_neg_day_frac_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 21 days with negative CLV."""
    return _rolling_count_true(_clv_raw(close, high, low) < 0, _TD_MON) / _TD_MON


# --- Group O (146-150): Capitulation composites and cross-series ---

def clv_146_clv_cap_composite_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Composite: avg CLV (21d) + frac near-low (21d) mapped to single distress score."""
    clv = _clv_raw(close, high, low)
    cf = _close_frac(close, high, low)
    avg_clv = _rolling_mean(clv, _TD_MON)
    frac_near_low = _rolling_count_true(cf <= 0.25, _TD_MON) / _TD_MON
    # Scale avg_clv from [-1,1] -> [1,0] (lower CLV = higher distress) and average
    return (1.0 - avg_clv) / 2.0 * 0.5 + frac_near_low * 0.5


def clv_147_clv_neg_and_near_low_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days with BOTH CLV < 0 AND close-frac < 0.25 over 21 days."""
    clv = _clv_raw(close, high, low)
    cf = _close_frac(close, high, low)
    both = (clv < 0) & (cf < 0.25)
    return _rolling_count_true(both, _TD_MON)


def clv_148_clv_max_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Trailing 252-day maximum CLV (best location seen in past year)."""
    return _rolling_max(_clv_raw(close, high, low), _TD_YEAR)


def clv_149_clv_min_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 252-day minimum CLV over full expanding history."""
    clv_min = _rolling_min(_clv_raw(close, high, low), _TD_YEAR)
    return clv_min.expanding(min_periods=5).rank(pct=True)


def clv_150_close_frac_low_vs_high_ratio_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio: count near-low closes / count near-high closes over 63 days."""
    cf = _close_frac(close, high, low)
    lo = _rolling_count_true(cf <= 0.25, _TD_QTR)
    hi = _rolling_count_true(cf >= 0.75, _TD_QTR)
    return _safe_div(lo, hi)


# ── Registry ──────────────────────────────────────────────────────────────────

CLOSE_LOCATION_REGISTRY_076_150 = {
    "clv_076_clv_slope_5d": {"inputs": ["close", "high", "low"], "func": clv_076_clv_slope_5d},
    "clv_077_clv_slope_21d": {"inputs": ["close", "high", "low"], "func": clv_077_clv_slope_21d},
    "clv_078_clv_slope_63d": {"inputs": ["close", "high", "low"], "func": clv_078_clv_slope_63d},
    "clv_079_close_frac_slope_21d": {"inputs": ["close", "high", "low"], "func": clv_079_close_frac_slope_21d},
    "clv_080_close_frac_slope_63d": {"inputs": ["close", "high", "low"], "func": clv_080_close_frac_slope_63d},
    "clv_081_clv_trend_declining_flag_21d": {"inputs": ["close", "high", "low"], "func": clv_081_clv_trend_declining_flag_21d},
    "clv_082_clv_trend_improving_flag_21d": {"inputs": ["close", "high", "low"], "func": clv_082_clv_trend_improving_flag_21d},
    "clv_083_clv_sma5_vs_sma21": {"inputs": ["close", "high", "low"], "func": clv_083_clv_sma5_vs_sma21},
    "clv_084_clv_sma21_vs_sma63": {"inputs": ["close", "high", "low"], "func": clv_084_clv_sma21_vs_sma63},
    "clv_085_clv_sma63_vs_sma252": {"inputs": ["close", "high", "low"], "func": clv_085_clv_sma63_vs_sma252},
    "clv_086_vwclv_cumsum": {"inputs": ["close", "high", "low", "volume"], "func": clv_086_vwclv_cumsum},
    "clv_087_vwclv_21d": {"inputs": ["close", "high", "low", "volume"], "func": clv_087_vwclv_21d},
    "clv_088_vwclv_63d": {"inputs": ["close", "high", "low", "volume"], "func": clv_088_vwclv_63d},
    "clv_089_vwclv_252d": {"inputs": ["close", "high", "low", "volume"], "func": clv_089_vwclv_252d},
    "clv_090_vwclv_avg_21d": {"inputs": ["close", "high", "low", "volume"], "func": clv_090_vwclv_avg_21d},
    "clv_091_vwclv_avg_63d": {"inputs": ["close", "high", "low", "volume"], "func": clv_091_vwclv_avg_63d},
    "clv_092_vwclv_vs_clv_21d": {"inputs": ["close", "high", "low", "volume"], "func": clv_092_vwclv_vs_clv_21d},
    "clv_093_vwclv_neg_sum_21d": {"inputs": ["close", "high", "low", "volume"], "func": clv_093_vwclv_neg_sum_21d},
    "clv_094_vwclv_pos_sum_21d": {"inputs": ["close", "high", "low", "volume"], "func": clv_094_vwclv_pos_sum_21d},
    "clv_095_vwclv_bull_bear_ratio_21d": {"inputs": ["close", "high", "low", "volume"], "func": clv_095_vwclv_bull_bear_ratio_21d},
    "clv_096_clv_1d_diff": {"inputs": ["close", "high", "low"], "func": clv_096_clv_1d_diff},
    "clv_097_clv_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_097_clv_5d_diff},
    "clv_098_clv_21d_diff": {"inputs": ["close", "high", "low"], "func": clv_098_clv_21d_diff},
    "clv_099_close_frac_5d_diff": {"inputs": ["close", "high", "low"], "func": clv_099_close_frac_5d_diff},
    "clv_100_close_frac_21d_diff": {"inputs": ["close", "high", "low"], "func": clv_100_close_frac_21d_diff},
    "clv_101_clv_pos_to_neg_flip": {"inputs": ["close", "high", "low"], "func": clv_101_clv_pos_to_neg_flip},
    "clv_102_clv_neg_to_pos_flip": {"inputs": ["close", "high", "low"], "func": clv_102_clv_neg_to_pos_flip},
    "clv_103_clv_5d_diff_abs": {"inputs": ["close", "high", "low"], "func": clv_103_clv_5d_diff_abs},
    "clv_104_clv_persistence_21d": {"inputs": ["close", "high", "low"], "func": clv_104_clv_persistence_21d},
    "clv_105_clv_direction_changes_21d": {"inputs": ["close", "high", "low"], "func": clv_105_clv_direction_changes_21d},
    "clv_106_clv_sma5_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": clv_106_clv_sma5_pct_rank_252d},
    "clv_107_clv_sma21_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": clv_107_clv_sma21_pct_rank_252d},
    "clv_108_clv_ratio_5d_vs_252d": {"inputs": ["close", "high", "low"], "func": clv_108_clv_ratio_5d_vs_252d},
    "clv_109_clv_ratio_21d_vs_252d": {"inputs": ["close", "high", "low"], "func": clv_109_clv_ratio_21d_vs_252d},
    "clv_110_close_frac_expanding_zscore": {"inputs": ["close", "high", "low"], "func": clv_110_close_frac_expanding_zscore},
    "clv_111_clv_expanding_zscore": {"inputs": ["close", "high", "low"], "func": clv_111_clv_expanding_zscore},
    "clv_112_clv_range_5d": {"inputs": ["close", "high", "low"], "func": clv_112_clv_range_5d},
    "clv_113_clv_range_21d": {"inputs": ["close", "high", "low"], "func": clv_113_clv_range_21d},
    "clv_114_clv_vs_min_252d": {"inputs": ["close", "high", "low"], "func": clv_114_clv_vs_min_252d},
    "clv_115_clv_vs_max_252d": {"inputs": ["close", "high", "low"], "func": clv_115_clv_vs_max_252d},
    "clv_116_clv_times_ret_1d": {"inputs": ["close", "high", "low"], "func": clv_116_clv_times_ret_1d},
    "clv_117_clv_times_ret_sign": {"inputs": ["close", "high", "low"], "func": clv_117_clv_times_ret_sign},
    "clv_118_clv_on_down_days_avg_21d": {"inputs": ["close", "high", "low"], "func": clv_118_clv_on_down_days_avg_21d},
    "clv_119_clv_on_up_days_avg_21d": {"inputs": ["close", "high", "low"], "func": clv_119_clv_on_up_days_avg_21d},
    "clv_120_clv_down_vs_up_avg_21d": {"inputs": ["close", "high", "low"], "func": clv_120_clv_down_vs_up_avg_21d},
    "clv_121_clv_on_down_days_avg_63d": {"inputs": ["close", "high", "low"], "func": clv_121_clv_on_down_days_avg_63d},
    "clv_122_clv_negative_on_down_day_flag": {"inputs": ["close", "high", "low"], "func": clv_122_clv_negative_on_down_day_flag},
    "clv_123_count_weak_days_21d": {"inputs": ["close", "high", "low"], "func": clv_123_count_weak_days_21d},
    "clv_124_count_weak_days_63d": {"inputs": ["close", "high", "low"], "func": clv_124_count_weak_days_63d},
    "clv_125_clv_positive_on_up_day_flag": {"inputs": ["close", "high", "low"], "func": clv_125_clv_positive_on_up_day_flag},
    "clv_126_clv_bb_upper_21d": {"inputs": ["close", "high", "low"], "func": clv_126_clv_bb_upper_21d},
    "clv_127_clv_bb_lower_21d": {"inputs": ["close", "high", "low"], "func": clv_127_clv_bb_lower_21d},
    "clv_128_clv_below_bb_lower_21d": {"inputs": ["close", "high", "low"], "func": clv_128_clv_below_bb_lower_21d},
    "clv_129_clv_above_bb_upper_21d": {"inputs": ["close", "high", "low"], "func": clv_129_clv_above_bb_upper_21d},
    "clv_130_clv_within_bb_21d": {"inputs": ["close", "high", "low"], "func": clv_130_clv_within_bb_21d},
    "clv_131_close_frac_bb_lower_21d": {"inputs": ["close", "high", "low"], "func": clv_131_close_frac_bb_lower_21d},
    "clv_132_clv_bb_width_21d": {"inputs": ["close", "high", "low"], "func": clv_132_clv_bb_width_21d},
    "clv_133_clv_bb_width_63d": {"inputs": ["close", "high", "low"], "func": clv_133_clv_bb_width_63d},
    "clv_134_clv_below_bb_lower_63d": {"inputs": ["close", "high", "low"], "func": clv_134_clv_below_bb_lower_63d},
    "clv_135_clv_within_bb_63d": {"inputs": ["close", "high", "low"], "func": clv_135_clv_within_bb_63d},
    "clv_136_avg_neg_clv_streak_len_252d": {"inputs": ["close", "high", "low"], "func": clv_136_avg_neg_clv_streak_len_252d},
    "clv_137_avg_pos_clv_streak_len_252d": {"inputs": ["close", "high", "low"], "func": clv_137_avg_pos_clv_streak_len_252d},
    "clv_138_neg_streak_count_252d": {"inputs": ["close", "high", "low"], "func": clv_138_neg_streak_count_252d},
    "clv_139_clv_neg_streak_len_norm_252d": {"inputs": ["close", "high", "low"], "func": clv_139_clv_neg_streak_len_norm_252d},
    "clv_140_consec_neg_clv_norm_21d_avg": {"inputs": ["close", "high", "low"], "func": clv_140_consec_neg_clv_norm_21d_avg},
    "clv_141_max_neg_clv_streak_126d": {"inputs": ["close", "high", "low"], "func": clv_141_max_neg_clv_streak_126d},
    "clv_142_max_near_low_streak_126d": {"inputs": ["close", "high", "low"], "func": clv_142_max_near_low_streak_126d},
    "clv_143_near_low_streak_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": clv_143_near_low_streak_pct_rank_252d},
    "clv_144_clv_neg_run_freq_252d": {"inputs": ["close", "high", "low"], "func": clv_144_clv_neg_run_freq_252d},
    "clv_145_clv_neg_day_frac_21d": {"inputs": ["close", "high", "low"], "func": clv_145_clv_neg_day_frac_21d},
    "clv_146_clv_cap_composite_21d": {"inputs": ["close", "high", "low"], "func": clv_146_clv_cap_composite_21d},
    "clv_147_clv_neg_and_near_low_21d": {"inputs": ["close", "high", "low"], "func": clv_147_clv_neg_and_near_low_21d},
    "clv_148_clv_max_252d": {"inputs": ["close", "high", "low"], "func": clv_148_clv_max_252d},
    "clv_149_clv_min_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": clv_149_clv_min_pct_rank_252d},
    "clv_150_close_frac_low_vs_high_ratio_63d": {"inputs": ["close", "high", "low"], "func": clv_150_close_frac_low_vs_high_ratio_63d},
}
