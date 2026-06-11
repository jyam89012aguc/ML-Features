"""
05_underwater_curve — Extended Features 001-075
Domain: area and depth of the underwater equity curve (accumulated severity)
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
Focus: Martin ratio / Ulcer Performance Index, pain ratio, Burke-ratio variants,
       recovery slope, time-weighted vs equal-weighted area comparisons,
       conditional area below depth thresholds, squared-vs-abs-drawdown integral
       ratios, underwater-curve convexity variants, longest contiguous underwater
       run, decay-weighted (EWM) depth, percentile ranks / z-scores at new windows,
       and rate-of-change of all the above.
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


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _uw_rolling(close: pd.Series, w: int) -> pd.Series:
    """Underwater series vs rolling w-day peak: (close/peak - 1), <= 0."""
    peak = _rolling_max(close, w)
    return _safe_div(close - peak, peak)


def _uw_expanding(close: pd.Series) -> pd.Series:
    """Underwater series vs all-time expanding high: (close/ATH - 1), <= 0."""
    peak = close.expanding(min_periods=1).max()
    return _safe_div(close - peak, peak)


def _ulcer_index(close: pd.Series, w: int) -> pd.Series:
    """Ulcer Index = sqrt(mean(drawdown^2)) over window w."""
    uw = _uw_rolling(close, w)
    return np.sqrt(_rolling_mean(uw ** 2, w))


def _pain_index(close: pd.Series, w: int) -> pd.Series:
    """Pain Index = mean(|drawdown|) over window w."""
    return _rolling_mean(_uw_rolling(close, w).abs(), w)


def _trailing_return(close: pd.Series, w: int) -> pd.Series:
    """Trailing return over w days: close / close.shift(w) - 1."""
    return _safe_div(close, close.shift(w)) - 1.0


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-018): Martin ratio / Ulcer Performance Index and variants ---

def uw_ext_001_martin_ratio_126d(close: pd.Series) -> pd.Series:
    """Martin ratio (UPI) 126d: trailing 126d return / 126d Ulcer Index."""
    ret = _trailing_return(close, _TD_HALF)
    ui = _ulcer_index(close, _TD_HALF)
    return _safe_div(ret, ui + _EPS)


def uw_ext_002_martin_ratio_252d(close: pd.Series) -> pd.Series:
    """Martin ratio (UPI) 252d: trailing 252d return / 252d Ulcer Index."""
    ret = _trailing_return(close, _TD_YEAR)
    ui = _ulcer_index(close, _TD_YEAR)
    return _safe_div(ret, ui + _EPS)


def uw_ext_003_martin_ratio_504d(close: pd.Series) -> pd.Series:
    """Martin ratio (UPI) 504d: trailing 504d return / 504d Ulcer Index."""
    ret = _trailing_return(close, 504)
    ui = _ulcer_index(close, 504)
    return _safe_div(ret, ui + _EPS)


def uw_ext_004_martin_ratio_sign_126d(close: pd.Series) -> pd.Series:
    """Sign of 126d Martin ratio: +1 positive, -1 negative (distress direction)."""
    mr = uw_ext_001_martin_ratio_126d(close)
    return np.sign(mr)


def uw_ext_005_martin_ratio_sign_252d(close: pd.Series) -> pd.Series:
    """Sign of 252d Martin ratio: +1 positive, -1 negative."""
    mr = uw_ext_002_martin_ratio_252d(close)
    return np.sign(mr)


def uw_ext_006_martin_ratio_depth_below_zero_252d(close: pd.Series) -> pd.Series:
    """Depth of 252d Martin ratio below zero: max(0, -martin_ratio_252d)."""
    mr = uw_ext_002_martin_ratio_252d(close)
    return mr.clip(upper=0).abs()


def uw_ext_007_martin_ratio_depth_below_zero_126d(close: pd.Series) -> pd.Series:
    """Depth of 126d Martin ratio below zero: max(0, -martin_ratio_126d)."""
    mr = uw_ext_001_martin_ratio_126d(close)
    return mr.clip(upper=0).abs()


def uw_ext_008_martin_ratio_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 252d Martin ratio over trailing 504d window."""
    mr = uw_ext_002_martin_ratio_252d(close)
    m = mr.rolling(504, min_periods=max(1, 252)).mean()
    s = mr.rolling(504, min_periods=max(1, 252)).std()
    return _safe_div(mr - m, s + _EPS)


def uw_ext_009_martin_ratio_pct_rank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252d Martin ratio within trailing 504d window."""
    mr = uw_ext_002_martin_ratio_252d(close)
    return mr.rolling(504, min_periods=max(1, 252)).rank(pct=True)


def uw_ext_010_martin_ratio_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252d Martin ratio (all-history rank)."""
    mr = uw_ext_002_martin_ratio_252d(close)
    return mr.expanding(min_periods=5).rank(pct=True)


def uw_ext_011_pain_ratio_126d(close: pd.Series) -> pd.Series:
    """Pain ratio 126d: trailing 126d return / 126d Pain Index."""
    ret = _trailing_return(close, _TD_HALF)
    pi = _pain_index(close, _TD_HALF)
    return _safe_div(ret, pi + _EPS)


def uw_ext_012_pain_ratio_252d(close: pd.Series) -> pd.Series:
    """Pain ratio 252d: trailing 252d return / 252d Pain Index."""
    ret = _trailing_return(close, _TD_YEAR)
    pi = _pain_index(close, _TD_YEAR)
    return _safe_div(ret, pi + _EPS)


def uw_ext_013_pain_ratio_504d(close: pd.Series) -> pd.Series:
    """Pain ratio 504d: trailing 504d return / 504d Pain Index."""
    ret = _trailing_return(close, 504)
    pi = _pain_index(close, 504)
    return _safe_div(ret, pi + _EPS)


def uw_ext_014_pain_ratio_depth_below_zero_252d(close: pd.Series) -> pd.Series:
    """Depth of 252d pain ratio below zero: max(0, -pain_ratio_252d)."""
    pr = uw_ext_012_pain_ratio_252d(close)
    return pr.clip(upper=0).abs()


def uw_ext_015_pain_ratio_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of 252d pain ratio over trailing 504d window."""
    pr = uw_ext_012_pain_ratio_252d(close)
    m = pr.rolling(504, min_periods=max(1, 252)).mean()
    s = pr.rolling(504, min_periods=max(1, 252)).std()
    return _safe_div(pr - m, s + _EPS)


def uw_ext_016_martin_vs_pain_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of 252d Martin ratio to 252d pain ratio (Ulcer vs Pain denominator spread)."""
    mr = uw_ext_002_martin_ratio_252d(close)
    pr = uw_ext_012_pain_ratio_252d(close)
    return _safe_div(mr, pr.replace(0, np.nan))


def uw_ext_017_martin_ratio_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in 252d Martin ratio (rate of UPI deterioration)."""
    mr = uw_ext_002_martin_ratio_252d(close)
    return mr.diff(_TD_MON)


def uw_ext_018_pain_ratio_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in 252d pain ratio (rate of pain-ratio deterioration)."""
    pr = uw_ext_012_pain_ratio_252d(close)
    return pr.diff(_TD_MON)


# --- Group B (019-030): Burke-ratio-style sqrt-sum-of-squared-drawdowns ---

def uw_ext_019_burke_ratio_126d(close: pd.Series) -> pd.Series:
    """Burke ratio 126d: trailing 126d return / sqrt(sum(drawdown^2))."""
    ret = _trailing_return(close, _TD_HALF)
    uw = _uw_rolling(close, _TD_HALF)
    burke_denom = np.sqrt(_rolling_sum(uw ** 2, _TD_HALF))
    return _safe_div(ret, burke_denom + _EPS)


def uw_ext_020_burke_ratio_252d(close: pd.Series) -> pd.Series:
    """Burke ratio 252d: trailing 252d return / sqrt(sum(drawdown^2))."""
    ret = _trailing_return(close, _TD_YEAR)
    uw = _uw_rolling(close, _TD_YEAR)
    burke_denom = np.sqrt(_rolling_sum(uw ** 2, _TD_YEAR))
    return _safe_div(ret, burke_denom + _EPS)


def uw_ext_021_burke_ratio_504d(close: pd.Series) -> pd.Series:
    """Burke ratio 504d: trailing 504d return / sqrt(sum(drawdown^2))."""
    ret = _trailing_return(close, 504)
    uw = _uw_rolling(close, 504)
    burke_denom = np.sqrt(_rolling_sum(uw ** 2, 504))
    return _safe_div(ret, burke_denom + _EPS)


def uw_ext_022_burke_denom_126d(close: pd.Series) -> pd.Series:
    """Burke denominator 126d: sqrt(sum(squared drawdowns)) — distress magnitude."""
    uw = _uw_rolling(close, _TD_HALF)
    return np.sqrt(_rolling_sum(uw ** 2, _TD_HALF))


def uw_ext_023_burke_denom_252d(close: pd.Series) -> pd.Series:
    """Burke denominator 252d: sqrt(sum(squared drawdowns))."""
    uw = _uw_rolling(close, _TD_YEAR)
    return np.sqrt(_rolling_sum(uw ** 2, _TD_YEAR))


def uw_ext_024_burke_denom_504d(close: pd.Series) -> pd.Series:
    """Burke denominator 504d: sqrt(sum(squared drawdowns))."""
    uw = _uw_rolling(close, 504)
    return np.sqrt(_rolling_sum(uw ** 2, 504))


def uw_ext_025_burke_depth_below_zero_252d(close: pd.Series) -> pd.Series:
    """Depth of 252d Burke ratio below zero: max(0, -burke_252d)."""
    br = uw_ext_020_burke_ratio_252d(close)
    return br.clip(upper=0).abs()


def uw_ext_026_burke_ratio_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of 252d Burke ratio over trailing 504d window."""
    br = uw_ext_020_burke_ratio_252d(close)
    m = br.rolling(504, min_periods=max(1, 252)).mean()
    s = br.rolling(504, min_periods=max(1, 252)).std()
    return _safe_div(br - m, s + _EPS)


def uw_ext_027_burke_ratio_pct_rank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252d Burke ratio in trailing 504d window."""
    br = uw_ext_020_burke_ratio_252d(close)
    return br.rolling(504, min_periods=max(1, 252)).rank(pct=True)


def uw_ext_028_burke_vs_martin_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of 252d Burke ratio to 252d Martin ratio (sum-sq vs mean-sq denominator)."""
    br = uw_ext_020_burke_ratio_252d(close)
    mr = uw_ext_002_martin_ratio_252d(close)
    return _safe_div(br, mr.replace(0, np.nan))


def uw_ext_029_burke_denom_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in 252d Burke denominator (acceleration of squared-drawdown mass)."""
    bd = uw_ext_023_burke_denom_252d(close)
    return bd.diff(_TD_MON)


def uw_ext_030_burke_ratio_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in 252d Burke ratio (deterioration rate of Burke performance)."""
    br = uw_ext_020_burke_ratio_252d(close)
    return br.diff(_TD_MON)


# --- Group C (031-040): Underwater-curve recovery slope ---

def uw_ext_031_uw_recovery_slope_63d(close: pd.Series) -> pd.Series:
    """Mean positive daily change in underwater curve over 63d (recovery speed)."""
    uw = _uw_rolling(close, _TD_QTR)
    d = uw.diff(1)
    pos_chg = d.where(d > 0, 0.0)
    return _rolling_mean(pos_chg, _TD_QTR)


def uw_ext_032_uw_recovery_slope_252d(close: pd.Series) -> pd.Series:
    """Mean positive daily change in underwater curve over 252d (recovery speed)."""
    uw = _uw_rolling(close, _TD_YEAR)
    d = uw.diff(1)
    pos_chg = d.where(d > 0, 0.0)
    return _rolling_mean(pos_chg, _TD_YEAR)


def uw_ext_033_uw_decline_slope_63d(close: pd.Series) -> pd.Series:
    """Mean negative daily change in underwater curve over 63d (descent speed)."""
    uw = _uw_rolling(close, _TD_QTR)
    d = uw.diff(1)
    neg_chg = d.where(d < 0, 0.0)
    return _rolling_mean(neg_chg.abs(), _TD_QTR)


def uw_ext_034_uw_decline_slope_252d(close: pd.Series) -> pd.Series:
    """Mean negative daily change in underwater curve over 252d (descent speed)."""
    uw = _uw_rolling(close, _TD_YEAR)
    d = uw.diff(1)
    neg_chg = d.where(d < 0, 0.0)
    return _rolling_mean(neg_chg.abs(), _TD_YEAR)


def uw_ext_035_uw_recovery_vs_decline_slope_63d(close: pd.Series) -> pd.Series:
    """Ratio of recovery slope to decline slope over 63d (asymmetry of curve movement)."""
    rec = uw_ext_031_uw_recovery_slope_63d(close)
    dec = uw_ext_033_uw_decline_slope_63d(close)
    return _safe_div(rec, dec + _EPS)


def uw_ext_036_uw_recovery_vs_decline_slope_252d(close: pd.Series) -> pd.Series:
    """Ratio of recovery slope to decline slope over 252d."""
    rec = uw_ext_032_uw_recovery_slope_252d(close)
    dec = uw_ext_034_uw_decline_slope_252d(close)
    return _safe_div(rec, dec + _EPS)


def uw_ext_037_uw_net_slope_63d(close: pd.Series) -> pd.Series:
    """Net mean daily change in underwater curve over 63d (positive = recovering)."""
    uw = _uw_rolling(close, _TD_QTR)
    return _rolling_mean(uw.diff(1), _TD_QTR)


def uw_ext_038_uw_net_slope_252d(close: pd.Series) -> pd.Series:
    """Net mean daily change in underwater curve over 252d."""
    uw = _uw_rolling(close, _TD_YEAR)
    return _rolling_mean(uw.diff(1), _TD_YEAR)


def uw_ext_039_uw_recovery_slope_ewm_63d(close: pd.Series) -> pd.Series:
    """EWM-smoothed daily positive changes in underwater curve (span=63)."""
    uw = _uw_rolling(close, _TD_QTR)
    d = uw.diff(1)
    pos_chg = d.where(d > 0, 0.0)
    return pos_chg.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def uw_ext_040_uw_recovery_slope_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in 252d recovery slope (acceleration of recovery)."""
    rs = uw_ext_032_uw_recovery_slope_252d(close)
    return rs.diff(_TD_MON)


# --- Group D (041-050): Time-weighted vs equal-weighted underwater area ---

def uw_ext_041_tw_vs_ew_area_ratio_63d(close: pd.Series) -> pd.Series:
    """Linearly time-weighted area / equal-weighted area over 63d (recency bias ratio)."""
    uw = _uw_rolling(close, _TD_QTR).abs()
    w = np.arange(1, _TD_QTR + 1, dtype=float)
    def _tw(y: np.ndarray) -> float:
        n = len(y)
        ww = w[-n:]
        return float(np.dot(y, ww) / ww.sum()) if ww.sum() > _EPS else float('nan')
    tw_area = uw.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_tw, raw=True)
    ew_area = _rolling_mean(uw, _TD_QTR)
    return _safe_div(tw_area, ew_area + _EPS)


def uw_ext_042_tw_vs_ew_area_ratio_252d(close: pd.Series) -> pd.Series:
    """Linearly time-weighted area / equal-weighted area over 252d."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    w = np.arange(1, _TD_YEAR + 1, dtype=float)
    def _tw(y: np.ndarray) -> float:
        n = len(y)
        ww = w[-n:]
        return float(np.dot(y, ww) / ww.sum()) if ww.sum() > _EPS else float('nan')
    tw_area = uw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_tw, raw=True)
    ew_area = _rolling_mean(uw, _TD_YEAR)
    return _safe_div(tw_area, ew_area + _EPS)


def uw_ext_043_ewm_vs_ew_area_ratio_63d(close: pd.Series) -> pd.Series:
    """EWM mean depth / equal-weighted mean depth over 63d (exponential vs equal recency)."""
    uw = _uw_rolling(close, _TD_QTR).abs()
    ewm_area = uw.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    ew_area = _rolling_mean(uw, _TD_QTR)
    return _safe_div(ewm_area, ew_area + _EPS)


def uw_ext_044_ewm_vs_ew_area_ratio_252d(close: pd.Series) -> pd.Series:
    """EWM mean depth / equal-weighted mean depth over 252d."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    ewm_area = uw.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()
    ew_area = _rolling_mean(uw, _TD_YEAR)
    return _safe_div(ewm_area, ew_area + _EPS)


def uw_ext_045_ewm_depth_63d(close: pd.Series) -> pd.Series:
    """EWM (span=63) of absolute underwater depth — decay-weighted current distress."""
    uw = _uw_rolling(close, _TD_QTR).abs()
    return uw.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def uw_ext_046_ewm_depth_252d(close: pd.Series) -> pd.Series:
    """EWM (span=252) of absolute underwater depth — slow decay distress signal."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    return uw.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def uw_ext_047_ewm_depth_126d(close: pd.Series) -> pd.Series:
    """EWM (span=126) of absolute underwater depth — medium decay distress signal."""
    uw = _uw_rolling(close, _TD_HALF).abs()
    return uw.ewm(span=_TD_HALF, min_periods=max(1, _TD_HALF // 2)).mean()


def uw_ext_048_tw_minus_ew_area_252d(close: pd.Series) -> pd.Series:
    """Absolute difference: time-weighted minus equal-weighted mean depth over 252d."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    w = np.arange(1, _TD_YEAR + 1, dtype=float)
    def _tw(y: np.ndarray) -> float:
        n = len(y)
        ww = w[-n:]
        return float(np.dot(y, ww) / ww.sum()) if ww.sum() > _EPS else float('nan')
    tw_area = uw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_tw, raw=True)
    ew_area = _rolling_mean(uw, _TD_YEAR)
    return tw_area - ew_area


def uw_ext_049_ewm_depth_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in EWM (span=252) underwater depth (decay-weighted pain acceleration)."""
    ewm_d = uw_ext_046_ewm_depth_252d(close)
    return ewm_d.diff(_TD_MON)


def uw_ext_050_tw_area_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of time-weighted 252d mean depth over trailing 504d window."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    w = np.arange(1, _TD_YEAR + 1, dtype=float)
    def _tw(y: np.ndarray) -> float:
        n = len(y)
        ww = w[-n:]
        return float(np.dot(y, ww) / ww.sum()) if ww.sum() > _EPS else float('nan')
    tw = uw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_tw, raw=True)
    m = tw.rolling(504, min_periods=max(1, 252)).mean()
    s = tw.rolling(504, min_periods=max(1, 252)).std()
    return _safe_div(tw - m, s + _EPS)


# --- Group E (051-060): Conditional underwater area below depth thresholds ---

def uw_ext_051_cond_area_below5pct_252d(close: pd.Series) -> pd.Series:
    """Sum of depths on days with |drawdown| > 5% over 252d (shallow-distress filter)."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    return _rolling_sum(uw.where(uw > 0.05, 0.0), _TD_YEAR)


def uw_ext_052_cond_area_below15pct_252d(close: pd.Series) -> pd.Series:
    """Sum of depths on days with |drawdown| > 15% over 252d."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    return _rolling_sum(uw.where(uw > 0.15, 0.0), _TD_YEAR)


def uw_ext_053_cond_area_below40pct_252d(close: pd.Series) -> pd.Series:
    """Sum of depths on days with |drawdown| > 40% over 252d (deep bear filter)."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    return _rolling_sum(uw.where(uw > 0.40, 0.0), _TD_YEAR)


def uw_ext_054_cond_area_below5pct_ath(close: pd.Series) -> pd.Series:
    """Expanding sum of ATH depths > 5% (all-time shallow distress mass)."""
    uw = _uw_expanding(close).abs()
    return uw.where(uw > 0.05, 0.0).expanding(min_periods=1).sum()


def uw_ext_055_cond_area_below20pct_504d(close: pd.Series) -> pd.Series:
    """Sum of depths on days with |drawdown| > 20% over 504d window."""
    uw = _uw_rolling(close, 504).abs()
    return _rolling_sum(uw.where(uw > 0.20, 0.0), 504)


def uw_ext_056_cond_day_count_below10pct_252d(close: pd.Series) -> pd.Series:
    """Count of days with |drawdown| > 10% over 252d (duration at moderate pain)."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    return _rolling_sum((uw > 0.10).astype(float), _TD_YEAR)


def uw_ext_057_cond_day_count_below20pct_252d(close: pd.Series) -> pd.Series:
    """Count of days with |drawdown| > 20% over 252d (duration at deep pain)."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    return _rolling_sum((uw > 0.20).astype(float), _TD_YEAR)


def uw_ext_058_cond_day_fraction_below10pct_252d(close: pd.Series) -> pd.Series:
    """Fraction of 252d days where |drawdown| > 10%."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    return _rolling_mean((uw > 0.10).astype(float), _TD_YEAR)


def uw_ext_059_cond_day_fraction_below20pct_504d(close: pd.Series) -> pd.Series:
    """Fraction of 504d days where |drawdown| > 20%."""
    uw = _uw_rolling(close, 504).abs()
    return _rolling_mean((uw > 0.20).astype(float), 504)


def uw_ext_060_cond_area_15pct_vs_total_area_252d(close: pd.Series) -> pd.Series:
    """Fraction of 252d total area from days with |drawdown| > 15% (deep-pain concentration)."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    deep = _rolling_sum(uw.where(uw > 0.15, 0.0), _TD_YEAR)
    total = _rolling_sum(uw, _TD_YEAR)
    return _safe_div(deep, total + _EPS)


# --- Group F (061-067): Squared-vs-absolute drawdown integral tail-weighting ---

def uw_ext_061_sq_abs_integral_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio sum(drawdown^2) / sum(|drawdown|) over 63d — tail-weighting measure."""
    uw = _uw_rolling(close, _TD_QTR).abs()
    sq_sum = _rolling_sum(uw ** 2, _TD_QTR)
    abs_sum = _rolling_sum(uw, _TD_QTR)
    return _safe_div(sq_sum, abs_sum + _EPS)


def uw_ext_062_sq_abs_integral_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio sum(drawdown^2) / sum(|drawdown|) over 252d — tail-weighting measure."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    sq_sum = _rolling_sum(uw ** 2, _TD_YEAR)
    abs_sum = _rolling_sum(uw, _TD_YEAR)
    return _safe_div(sq_sum, abs_sum + _EPS)


def uw_ext_063_sq_abs_integral_ratio_504d(close: pd.Series) -> pd.Series:
    """Ratio sum(drawdown^2) / sum(|drawdown|) over 504d — tail-weighting measure."""
    uw = _uw_rolling(close, 504).abs()
    sq_sum = _rolling_sum(uw ** 2, 504)
    abs_sum = _rolling_sum(uw, 504)
    return _safe_div(sq_sum, abs_sum + _EPS)


def uw_ext_064_sq_abs_ratio_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of 252d sq/abs integral ratio over trailing 504d window."""
    r = uw_ext_062_sq_abs_integral_ratio_252d(close)
    m = r.rolling(504, min_periods=max(1, 252)).mean()
    s = r.rolling(504, min_periods=max(1, 252)).std()
    return _safe_div(r - m, s + _EPS)


def uw_ext_065_sq_abs_ratio_pct_rank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252d sq/abs integral ratio in trailing 504d window."""
    r = uw_ext_062_sq_abs_integral_ratio_252d(close)
    return r.rolling(504, min_periods=max(1, 252)).rank(pct=True)


def uw_ext_066_sq_abs_ratio_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in 252d sq/abs integral ratio (tail-weighting acceleration)."""
    r = uw_ext_062_sq_abs_integral_ratio_252d(close)
    return r.diff(_TD_MON)


def uw_ext_067_cube_abs_integral_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio sum(drawdown^3) / sum(|drawdown|) over 252d — cubic tail-weighting."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    cube_sum = _rolling_sum(uw ** 3, _TD_YEAR)
    abs_sum = _rolling_sum(uw, _TD_YEAR)
    return _safe_div(cube_sum, abs_sum + _EPS)


# --- Group G (068-071): Longest contiguous underwater run ---

def uw_ext_068_longest_contiguous_uw_run_126d(close: pd.Series) -> pd.Series:
    """Longest consecutive run of underwater days over trailing 126d window."""
    uw = _uw_rolling(close, _TD_HALF)
    is_uw = (uw < -_EPS).astype(float)
    def _max_run(y: np.ndarray) -> float:
        max_r, cur = 0, 0
        for v in y:
            if v > 0:
                cur += 1
                if cur > max_r:
                    max_r = cur
            else:
                cur = 0
        return float(max_r)
    return is_uw.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(_max_run, raw=True)


def uw_ext_069_longest_contiguous_uw_run_252d(close: pd.Series) -> pd.Series:
    """Longest consecutive run of underwater days over trailing 252d window."""
    uw = _uw_rolling(close, _TD_YEAR)
    is_uw = (uw < -_EPS).astype(float)
    def _max_run(y: np.ndarray) -> float:
        max_r, cur = 0, 0
        for v in y:
            if v > 0:
                cur += 1
                if cur > max_r:
                    max_r = cur
            else:
                cur = 0
        return float(max_r)
    return is_uw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_max_run, raw=True)


def uw_ext_070_longest_run_fraction_252d(close: pd.Series) -> pd.Series:
    """Longest contiguous uw run as fraction of 252d window (duration ratio)."""
    lr = uw_ext_069_longest_contiguous_uw_run_252d(close)
    return _safe_div(lr, pd.Series(_TD_YEAR, index=close.index, dtype=float))


def uw_ext_071_longest_run_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of 252d longest contiguous uw run over trailing 504d window."""
    lr = uw_ext_069_longest_contiguous_uw_run_252d(close)
    m = lr.rolling(504, min_periods=max(1, 252)).mean()
    s = lr.rolling(504, min_periods=max(1, 252)).std()
    return _safe_div(lr - m, s + _EPS)


# --- Group H (072-075): Underwater-curve convexity variants and percentile ranks ---

def uw_ext_072_uw_convexity_126d(close: pd.Series) -> pd.Series:
    """Convexity 126d: area / (window * MDD_126d) — fill-ratio of underwater region."""
    uw = _uw_rolling(close, _TD_HALF).abs()
    area = _rolling_sum(uw, _TD_HALF)
    mdd = uw.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).max()
    return _safe_div(area, (_TD_HALF * mdd) + _EPS)


def uw_ext_073_uw_convexity_504d(close: pd.Series) -> pd.Series:
    """Convexity 504d: area / (window * MDD_504d)."""
    uw = _uw_rolling(close, 504).abs()
    area = _rolling_sum(uw, 504)
    mdd = uw.rolling(504, min_periods=max(1, 252)).max()
    return _safe_div(area, (504 * mdd) + _EPS)


def uw_ext_074_uw_convexity_126d_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of 126d convexity score over trailing 504d window."""
    conv = uw_ext_072_uw_convexity_126d(close)
    m = conv.rolling(504, min_periods=max(1, 252)).mean()
    s = conv.rolling(504, min_periods=max(1, 252)).std()
    return _safe_div(conv - m, s + _EPS)


def uw_ext_075_uw_convexity_252d_pct_rank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252d convexity score (area/(w*MDD)) in trailing 504d window."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    area = _rolling_sum(uw, _TD_YEAR)
    mdd = uw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).max()
    conv = _safe_div(area, (_TD_YEAR * mdd) + _EPS)
    return conv.rolling(504, min_periods=max(1, 252)).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

UNDERWATER_CURVE_EXTENDED_REGISTRY_001_075 = {
    "uw_ext_001_martin_ratio_126d": {"inputs": ["close"], "func": uw_ext_001_martin_ratio_126d},
    "uw_ext_002_martin_ratio_252d": {"inputs": ["close"], "func": uw_ext_002_martin_ratio_252d},
    "uw_ext_003_martin_ratio_504d": {"inputs": ["close"], "func": uw_ext_003_martin_ratio_504d},
    "uw_ext_004_martin_ratio_sign_126d": {"inputs": ["close"], "func": uw_ext_004_martin_ratio_sign_126d},
    "uw_ext_005_martin_ratio_sign_252d": {"inputs": ["close"], "func": uw_ext_005_martin_ratio_sign_252d},
    "uw_ext_006_martin_ratio_depth_below_zero_252d": {"inputs": ["close"], "func": uw_ext_006_martin_ratio_depth_below_zero_252d},
    "uw_ext_007_martin_ratio_depth_below_zero_126d": {"inputs": ["close"], "func": uw_ext_007_martin_ratio_depth_below_zero_126d},
    "uw_ext_008_martin_ratio_zscore_252d": {"inputs": ["close"], "func": uw_ext_008_martin_ratio_zscore_252d},
    "uw_ext_009_martin_ratio_pct_rank_504d": {"inputs": ["close"], "func": uw_ext_009_martin_ratio_pct_rank_504d},
    "uw_ext_010_martin_ratio_expanding_pct_rank": {"inputs": ["close"], "func": uw_ext_010_martin_ratio_expanding_pct_rank},
    "uw_ext_011_pain_ratio_126d": {"inputs": ["close"], "func": uw_ext_011_pain_ratio_126d},
    "uw_ext_012_pain_ratio_252d": {"inputs": ["close"], "func": uw_ext_012_pain_ratio_252d},
    "uw_ext_013_pain_ratio_504d": {"inputs": ["close"], "func": uw_ext_013_pain_ratio_504d},
    "uw_ext_014_pain_ratio_depth_below_zero_252d": {"inputs": ["close"], "func": uw_ext_014_pain_ratio_depth_below_zero_252d},
    "uw_ext_015_pain_ratio_zscore_504d": {"inputs": ["close"], "func": uw_ext_015_pain_ratio_zscore_504d},
    "uw_ext_016_martin_vs_pain_ratio_252d": {"inputs": ["close"], "func": uw_ext_016_martin_vs_pain_ratio_252d},
    "uw_ext_017_martin_ratio_velocity_21d": {"inputs": ["close"], "func": uw_ext_017_martin_ratio_velocity_21d},
    "uw_ext_018_pain_ratio_velocity_21d": {"inputs": ["close"], "func": uw_ext_018_pain_ratio_velocity_21d},
    "uw_ext_019_burke_ratio_126d": {"inputs": ["close"], "func": uw_ext_019_burke_ratio_126d},
    "uw_ext_020_burke_ratio_252d": {"inputs": ["close"], "func": uw_ext_020_burke_ratio_252d},
    "uw_ext_021_burke_ratio_504d": {"inputs": ["close"], "func": uw_ext_021_burke_ratio_504d},
    "uw_ext_022_burke_denom_126d": {"inputs": ["close"], "func": uw_ext_022_burke_denom_126d},
    "uw_ext_023_burke_denom_252d": {"inputs": ["close"], "func": uw_ext_023_burke_denom_252d},
    "uw_ext_024_burke_denom_504d": {"inputs": ["close"], "func": uw_ext_024_burke_denom_504d},
    "uw_ext_025_burke_depth_below_zero_252d": {"inputs": ["close"], "func": uw_ext_025_burke_depth_below_zero_252d},
    "uw_ext_026_burke_ratio_zscore_504d": {"inputs": ["close"], "func": uw_ext_026_burke_ratio_zscore_504d},
    "uw_ext_027_burke_ratio_pct_rank_504d": {"inputs": ["close"], "func": uw_ext_027_burke_ratio_pct_rank_504d},
    "uw_ext_028_burke_vs_martin_ratio_252d": {"inputs": ["close"], "func": uw_ext_028_burke_vs_martin_ratio_252d},
    "uw_ext_029_burke_denom_velocity_21d": {"inputs": ["close"], "func": uw_ext_029_burke_denom_velocity_21d},
    "uw_ext_030_burke_ratio_velocity_21d": {"inputs": ["close"], "func": uw_ext_030_burke_ratio_velocity_21d},
    "uw_ext_031_uw_recovery_slope_63d": {"inputs": ["close"], "func": uw_ext_031_uw_recovery_slope_63d},
    "uw_ext_032_uw_recovery_slope_252d": {"inputs": ["close"], "func": uw_ext_032_uw_recovery_slope_252d},
    "uw_ext_033_uw_decline_slope_63d": {"inputs": ["close"], "func": uw_ext_033_uw_decline_slope_63d},
    "uw_ext_034_uw_decline_slope_252d": {"inputs": ["close"], "func": uw_ext_034_uw_decline_slope_252d},
    "uw_ext_035_uw_recovery_vs_decline_slope_63d": {"inputs": ["close"], "func": uw_ext_035_uw_recovery_vs_decline_slope_63d},
    "uw_ext_036_uw_recovery_vs_decline_slope_252d": {"inputs": ["close"], "func": uw_ext_036_uw_recovery_vs_decline_slope_252d},
    "uw_ext_037_uw_net_slope_63d": {"inputs": ["close"], "func": uw_ext_037_uw_net_slope_63d},
    "uw_ext_038_uw_net_slope_252d": {"inputs": ["close"], "func": uw_ext_038_uw_net_slope_252d},
    "uw_ext_039_uw_recovery_slope_ewm_63d": {"inputs": ["close"], "func": uw_ext_039_uw_recovery_slope_ewm_63d},
    "uw_ext_040_uw_recovery_slope_velocity_21d": {"inputs": ["close"], "func": uw_ext_040_uw_recovery_slope_velocity_21d},
    "uw_ext_041_tw_vs_ew_area_ratio_63d": {"inputs": ["close"], "func": uw_ext_041_tw_vs_ew_area_ratio_63d},
    "uw_ext_042_tw_vs_ew_area_ratio_252d": {"inputs": ["close"], "func": uw_ext_042_tw_vs_ew_area_ratio_252d},
    "uw_ext_043_ewm_vs_ew_area_ratio_63d": {"inputs": ["close"], "func": uw_ext_043_ewm_vs_ew_area_ratio_63d},
    "uw_ext_044_ewm_vs_ew_area_ratio_252d": {"inputs": ["close"], "func": uw_ext_044_ewm_vs_ew_area_ratio_252d},
    "uw_ext_045_ewm_depth_63d": {"inputs": ["close"], "func": uw_ext_045_ewm_depth_63d},
    "uw_ext_046_ewm_depth_252d": {"inputs": ["close"], "func": uw_ext_046_ewm_depth_252d},
    "uw_ext_047_ewm_depth_126d": {"inputs": ["close"], "func": uw_ext_047_ewm_depth_126d},
    "uw_ext_048_tw_minus_ew_area_252d": {"inputs": ["close"], "func": uw_ext_048_tw_minus_ew_area_252d},
    "uw_ext_049_ewm_depth_velocity_21d": {"inputs": ["close"], "func": uw_ext_049_ewm_depth_velocity_21d},
    "uw_ext_050_tw_area_zscore_504d": {"inputs": ["close"], "func": uw_ext_050_tw_area_zscore_504d},
    "uw_ext_051_cond_area_below5pct_252d": {"inputs": ["close"], "func": uw_ext_051_cond_area_below5pct_252d},
    "uw_ext_052_cond_area_below15pct_252d": {"inputs": ["close"], "func": uw_ext_052_cond_area_below15pct_252d},
    "uw_ext_053_cond_area_below40pct_252d": {"inputs": ["close"], "func": uw_ext_053_cond_area_below40pct_252d},
    "uw_ext_054_cond_area_below5pct_ath": {"inputs": ["close"], "func": uw_ext_054_cond_area_below5pct_ath},
    "uw_ext_055_cond_area_below20pct_504d": {"inputs": ["close"], "func": uw_ext_055_cond_area_below20pct_504d},
    "uw_ext_056_cond_day_count_below10pct_252d": {"inputs": ["close"], "func": uw_ext_056_cond_day_count_below10pct_252d},
    "uw_ext_057_cond_day_count_below20pct_252d": {"inputs": ["close"], "func": uw_ext_057_cond_day_count_below20pct_252d},
    "uw_ext_058_cond_day_fraction_below10pct_252d": {"inputs": ["close"], "func": uw_ext_058_cond_day_fraction_below10pct_252d},
    "uw_ext_059_cond_day_fraction_below20pct_504d": {"inputs": ["close"], "func": uw_ext_059_cond_day_fraction_below20pct_504d},
    "uw_ext_060_cond_area_15pct_vs_total_area_252d": {"inputs": ["close"], "func": uw_ext_060_cond_area_15pct_vs_total_area_252d},
    "uw_ext_061_sq_abs_integral_ratio_63d": {"inputs": ["close"], "func": uw_ext_061_sq_abs_integral_ratio_63d},
    "uw_ext_062_sq_abs_integral_ratio_252d": {"inputs": ["close"], "func": uw_ext_062_sq_abs_integral_ratio_252d},
    "uw_ext_063_sq_abs_integral_ratio_504d": {"inputs": ["close"], "func": uw_ext_063_sq_abs_integral_ratio_504d},
    "uw_ext_064_sq_abs_ratio_zscore_504d": {"inputs": ["close"], "func": uw_ext_064_sq_abs_ratio_zscore_504d},
    "uw_ext_065_sq_abs_ratio_pct_rank_504d": {"inputs": ["close"], "func": uw_ext_065_sq_abs_ratio_pct_rank_504d},
    "uw_ext_066_sq_abs_ratio_velocity_21d": {"inputs": ["close"], "func": uw_ext_066_sq_abs_ratio_velocity_21d},
    "uw_ext_067_cube_abs_integral_ratio_252d": {"inputs": ["close"], "func": uw_ext_067_cube_abs_integral_ratio_252d},
    "uw_ext_068_longest_contiguous_uw_run_126d": {"inputs": ["close"], "func": uw_ext_068_longest_contiguous_uw_run_126d},
    "uw_ext_069_longest_contiguous_uw_run_252d": {"inputs": ["close"], "func": uw_ext_069_longest_contiguous_uw_run_252d},
    "uw_ext_070_longest_run_fraction_252d": {"inputs": ["close"], "func": uw_ext_070_longest_run_fraction_252d},
    "uw_ext_071_longest_run_zscore_504d": {"inputs": ["close"], "func": uw_ext_071_longest_run_zscore_504d},
    "uw_ext_072_uw_convexity_126d": {"inputs": ["close"], "func": uw_ext_072_uw_convexity_126d},
    "uw_ext_073_uw_convexity_504d": {"inputs": ["close"], "func": uw_ext_073_uw_convexity_504d},
    "uw_ext_074_uw_convexity_126d_zscore_504d": {"inputs": ["close"], "func": uw_ext_074_uw_convexity_126d_zscore_504d},
    "uw_ext_075_uw_convexity_252d_pct_rank_504d": {"inputs": ["close"], "func": uw_ext_075_uw_convexity_252d_pct_rank_504d},
}
