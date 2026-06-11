"""
05_underwater_curve — Base Features 001-075
Domain: area and depth of the underwater equity curve (accumulated severity)
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


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _uw_rolling(close: pd.Series, w: int) -> pd.Series:
    """Underwater series vs rolling w-day peak: (close/peak - 1), <= 0."""
    peak = _rolling_max(close, w)
    return _safe_div(close - peak, peak)


def _uw_expanding(close: pd.Series) -> pd.Series:
    """Underwater series vs all-time expanding high: (close/ATH - 1), <= 0."""
    peak = close.expanding(min_periods=1).max()
    return _safe_div(close - peak, peak)


def _log_uw_rolling(close: pd.Series, w: int) -> pd.Series:
    """Log-space underwater: log(close/peak), <= 0."""
    peak = _rolling_max(close, w)
    return np.log((close / peak.replace(0, np.nan)).clip(lower=_EPS))


def _log_uw_expanding(close: pd.Series) -> pd.Series:
    """Log-space underwater vs ATH: log(close/ATH), <= 0."""
    peak = close.expanding(min_periods=1).max()
    return np.log((close / peak.replace(0, np.nan)).clip(lower=_EPS))


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Plain underwater area (integral of drawdown curve) ---

def uw_001_area_21d_rolling(close: pd.Series) -> pd.Series:
    """Sum of absolute underwater depths over 21-day rolling window (pain area)."""
    uw = _uw_rolling(close, _TD_MON)
    return _rolling_sum(uw.abs(), _TD_MON)


def uw_002_area_63d_rolling(close: pd.Series) -> pd.Series:
    """Sum of absolute underwater depths over 63-day rolling window."""
    uw = _uw_rolling(close, _TD_QTR)
    return _rolling_sum(uw.abs(), _TD_QTR)


def uw_003_area_126d_rolling(close: pd.Series) -> pd.Series:
    """Sum of absolute underwater depths over 126-day rolling window."""
    uw = _uw_rolling(close, _TD_HALF)
    return _rolling_sum(uw.abs(), _TD_HALF)


def uw_004_area_252d_rolling(close: pd.Series) -> pd.Series:
    """Sum of absolute underwater depths over 252-day rolling window."""
    uw = _uw_rolling(close, _TD_YEAR)
    return _rolling_sum(uw.abs(), _TD_YEAR)


def uw_005_area_504d_rolling(close: pd.Series) -> pd.Series:
    """Sum of absolute underwater depths over 504-day rolling window."""
    uw = _uw_rolling(close, 504)
    return _rolling_sum(uw.abs(), 504)


def uw_006_area_756d_rolling(close: pd.Series) -> pd.Series:
    """Sum of absolute underwater depths over 756-day rolling window."""
    uw = _uw_rolling(close, 756)
    return _rolling_sum(uw.abs(), 756)


def uw_007_area_ath_expanding(close: pd.Series) -> pd.Series:
    """Expanding cumulative sum of absolute ATH underwater depths (all-time pain)."""
    uw = _uw_expanding(close)
    return uw.abs().expanding(min_periods=1).sum()


def uw_008_area_normalized_21d(close: pd.Series) -> pd.Series:
    """21-day underwater area divided by window length (mean daily depth)."""
    return _safe_div(uw_001_area_21d_rolling(close), pd.Series(_TD_MON, index=close.index, dtype=float))


def uw_009_area_normalized_63d(close: pd.Series) -> pd.Series:
    """63-day underwater area divided by window length."""
    return _safe_div(uw_002_area_63d_rolling(close), pd.Series(_TD_QTR, index=close.index, dtype=float))


def uw_010_area_normalized_252d(close: pd.Series) -> pd.Series:
    """252-day underwater area divided by window length."""
    return _safe_div(uw_004_area_252d_rolling(close), pd.Series(_TD_YEAR, index=close.index, dtype=float))


def uw_011_area_log_21d(close: pd.Series) -> pd.Series:
    """21-day rolling sum of absolute log-space underwater depths."""
    return _rolling_sum(_log_uw_rolling(close, _TD_MON).abs(), _TD_MON)


def uw_012_area_log_63d(close: pd.Series) -> pd.Series:
    """63-day rolling sum of absolute log-space underwater depths."""
    return _rolling_sum(_log_uw_rolling(close, _TD_QTR).abs(), _TD_QTR)


def uw_013_area_log_252d(close: pd.Series) -> pd.Series:
    """252-day rolling sum of absolute log-space underwater depths."""
    return _rolling_sum(_log_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)


def uw_014_area_log_ath_expanding(close: pd.Series) -> pd.Series:
    """Expanding cumulative absolute log-space ATH underwater area."""
    return _log_uw_expanding(close).abs().expanding(min_periods=1).sum()


def uw_015_area_intraday_low_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day area using intraday low vs intraday peak (maximum daily pain)."""
    peak = _rolling_max(high, _TD_YEAR)
    uw_low = _safe_div(low - peak, peak).abs()
    return _rolling_sum(uw_low, _TD_YEAR)


# --- Group B (016-030): Pain index (mean underwater depth) and Ulcer-type ---

def uw_016_pain_index_21d(close: pd.Series) -> pd.Series:
    """Mean absolute underwater depth over 21 days (Pain Index, 1-month)."""
    return _rolling_mean(_uw_rolling(close, _TD_MON).abs(), _TD_MON)


def uw_017_pain_index_63d(close: pd.Series) -> pd.Series:
    """Mean absolute underwater depth over 63 days (Pain Index, 1-quarter)."""
    return _rolling_mean(_uw_rolling(close, _TD_QTR).abs(), _TD_QTR)


def uw_018_pain_index_252d(close: pd.Series) -> pd.Series:
    """Mean absolute underwater depth over 252 days (Pain Index, 1-year)."""
    return _rolling_mean(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)


def uw_019_pain_index_504d(close: pd.Series) -> pd.Series:
    """Mean absolute underwater depth over 504 days (Pain Index, 2-year)."""
    return _rolling_mean(_uw_rolling(close, 504).abs(), 504)


def uw_020_pain_index_ath_expanding(close: pd.Series) -> pd.Series:
    """Expanding mean absolute ATH underwater depth (all-time Pain Index)."""
    return _uw_expanding(close).abs().expanding(min_periods=1).mean()


def uw_021_ulcer_index_21d(close: pd.Series) -> pd.Series:
    """Ulcer Index over 21 days: sqrt(mean(drawdown^2))."""
    uw = _uw_rolling(close, _TD_MON)
    return np.sqrt(_rolling_mean(uw ** 2, _TD_MON))


def uw_022_ulcer_index_63d(close: pd.Series) -> pd.Series:
    """Ulcer Index over 63 days."""
    uw = _uw_rolling(close, _TD_QTR)
    return np.sqrt(_rolling_mean(uw ** 2, _TD_QTR))


def uw_023_ulcer_index_252d(close: pd.Series) -> pd.Series:
    """Ulcer Index over 252 days."""
    uw = _uw_rolling(close, _TD_YEAR)
    return np.sqrt(_rolling_mean(uw ** 2, _TD_YEAR))


def uw_024_ulcer_index_504d(close: pd.Series) -> pd.Series:
    """Ulcer Index over 504 days."""
    uw = _uw_rolling(close, 504)
    return np.sqrt(_rolling_mean(uw ** 2, 504))


def uw_025_ulcer_index_ath_expanding(close: pd.Series) -> pd.Series:
    """Expanding Ulcer Index vs ATH."""
    uw = _uw_expanding(close)
    return np.sqrt((uw ** 2).expanding(min_periods=1).mean())


def uw_026_pain_index_median_63d(close: pd.Series) -> pd.Series:
    """Median (not mean) absolute underwater depth over 63 days."""
    return _rolling_median(_uw_rolling(close, _TD_QTR).abs(), _TD_QTR)


def uw_027_pain_index_median_252d(close: pd.Series) -> pd.Series:
    """Median absolute underwater depth over 252 days."""
    return _rolling_median(_uw_rolling(close, _TD_YEAR).abs(), _TD_YEAR)


def uw_028_ulcer_index_log_63d(close: pd.Series) -> pd.Series:
    """Log-space Ulcer Index: sqrt(mean(log_uw^2)) over 63 days."""
    luw = _log_uw_rolling(close, _TD_QTR)
    return np.sqrt(_rolling_mean(luw ** 2, _TD_QTR))


def uw_029_ulcer_index_log_252d(close: pd.Series) -> pd.Series:
    """Log-space Ulcer Index over 252 days."""
    luw = _log_uw_rolling(close, _TD_YEAR)
    return np.sqrt(_rolling_mean(luw ** 2, _TD_YEAR))


def uw_030_pain_vs_ulcer_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of Pain Index to Ulcer Index over 252d (shape of distress distribution)."""
    pi = uw_018_pain_index_252d(close)
    ui = uw_023_ulcer_index_252d(close)
    return _safe_div(pi, ui)


# --- Group C (031-045): Time-weighted and recency-biased area ---

def uw_031_area_linear_weighted_21d(close: pd.Series) -> pd.Series:
    """Linearly time-weighted underwater area over 21 days (recent days get higher weight)."""
    uw = _uw_rolling(close, _TD_MON).abs()
    w = np.arange(1, _TD_MON + 1, dtype=float)
    def _wsum(y: np.ndarray) -> float:
        n = len(y)
        ww = w[-n:]
        return float(np.sum(y * ww))
    return uw.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(_wsum, raw=True)


def uw_032_area_linear_weighted_63d(close: pd.Series) -> pd.Series:
    """Linearly time-weighted underwater area over 63 days."""
    uw = _uw_rolling(close, _TD_QTR).abs()
    w = np.arange(1, _TD_QTR + 1, dtype=float)
    def _wsum(y: np.ndarray) -> float:
        n = len(y)
        ww = w[-n:]
        return float(np.sum(y * ww))
    return uw.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_wsum, raw=True)


def uw_033_area_linear_weighted_252d(close: pd.Series) -> pd.Series:
    """Linearly time-weighted underwater area over 252 days."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    w = np.arange(1, _TD_YEAR + 1, dtype=float)
    def _wsum(y: np.ndarray) -> float:
        n = len(y)
        ww = w[-n:]
        return float(np.sum(y * ww))
    return uw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(_wsum, raw=True)


def uw_034_area_exp_weighted_21d(close: pd.Series) -> pd.Series:
    """Exponentially-weighted (EWM) mean underwater depth over 21 days."""
    uw = _uw_rolling(close, _TD_MON).abs()
    return uw.ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def uw_035_area_exp_weighted_63d(close: pd.Series) -> pd.Series:
    """Exponentially-weighted mean underwater depth over 63 days."""
    uw = _uw_rolling(close, _TD_QTR).abs()
    return uw.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def uw_036_area_exp_weighted_252d(close: pd.Series) -> pd.Series:
    """Exponentially-weighted mean underwater depth over 252 days."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    return uw.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def uw_037_area_front_half_vs_back_half_63d(close: pd.Series) -> pd.Series:
    """Ratio of back-half to front-half area in 63-day window (front-loaded vs back-loaded pain)."""
    uw = _uw_rolling(close, _TD_QTR).abs()
    front = _rolling_sum(uw.shift(_TD_QTR // 2), _TD_QTR // 2)
    back = _rolling_sum(uw, _TD_QTR // 2)
    return _safe_div(back, front + _EPS)


def uw_038_area_front_half_vs_back_half_252d(close: pd.Series) -> pd.Series:
    """Ratio of back-half to front-half area in 252-day window."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    front = _rolling_sum(uw.shift(_TD_YEAR // 2), _TD_YEAR // 2)
    back = _rolling_sum(uw, _TD_YEAR // 2)
    return _safe_div(back, front + _EPS)


def uw_039_area_quarter_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of last-quarter area to prior-quarter area in 126-day window."""
    uw = _uw_rolling(close, _TD_HALF).abs()
    recent = _rolling_sum(uw, _TD_QTR)
    prior = _rolling_sum(uw.shift(_TD_QTR), _TD_QTR)
    return _safe_div(recent, prior + _EPS)


def uw_040_area_month_ratio_63d(close: pd.Series) -> pd.Series:
    """Ratio of last-month area to prior-2-month area in 63-day window."""
    uw = _uw_rolling(close, _TD_QTR).abs()
    recent = _rolling_sum(uw, _TD_MON)
    prior = _rolling_sum(uw.shift(_TD_MON), _TD_MON * 2)
    return _safe_div(recent, prior + _EPS)


def uw_041_area_cumulative_ath_vs_1yr_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 252-day area to expanding ATH area (recent pain vs all-time pain)."""
    a252 = uw_004_area_252d_rolling(close)
    a_ath = uw_007_area_ath_expanding(close)
    return _safe_div(a252, a_ath + _EPS)


def uw_042_area_21d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day area to 252-day area (acute vs chronic pain)."""
    return _safe_div(uw_001_area_21d_rolling(close), uw_004_area_252d_rolling(close) + _EPS)


def uw_043_area_63d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 63-day area to 252-day area (quarterly vs annual pain)."""
    return _safe_div(uw_002_area_63d_rolling(close), uw_004_area_252d_rolling(close) + _EPS)


def uw_044_area_126d_vs_504d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 126-day area to 504-day area."""
    a126 = uw_003_area_126d_rolling(close)
    a504 = uw_005_area_504d_rolling(close)
    return _safe_div(a126, a504 + _EPS)


def uw_045_area_cumsum_acceleration_21d(close: pd.Series) -> pd.Series:
    """Rate of change of cumulative ATH underwater area (how fast pain accumulates)."""
    a_ath = uw_007_area_ath_expanding(close)
    return a_ath.diff(_TD_MON)


# --- Group D (046-060): Underwater intensity, depth-duration products ---

def uw_046_intensity_depth_x_area_63d(close: pd.Series) -> pd.Series:
    """Underwater intensity: current depth * cumulative 63-day area (depth x duration)."""
    depth = _uw_rolling(close, _TD_QTR).abs()
    area = uw_002_area_63d_rolling(close)
    return depth * area


def uw_047_intensity_depth_x_area_252d(close: pd.Series) -> pd.Series:
    """Underwater intensity: current depth * cumulative 252-day area."""
    depth = _uw_rolling(close, _TD_YEAR).abs()
    area = uw_004_area_252d_rolling(close)
    return depth * area


def uw_048_intensity_ath_depth_x_ath_area(close: pd.Series) -> pd.Series:
    """ATH intensity: current ATH depth * expanding ATH area."""
    depth = _uw_expanding(close).abs()
    area = uw_007_area_ath_expanding(close)
    return depth * area


def uw_049_intensity_ulcer_x_area_252d(close: pd.Series) -> pd.Series:
    """Product of Ulcer Index and area over 252d (compound distress metric)."""
    return uw_023_ulcer_index_252d(close) * uw_004_area_252d_rolling(close)


def uw_050_max_sustained_submersion_63d(close: pd.Series) -> pd.Series:
    """Maximum single-day underwater depth seen in trailing 63-day window."""
    return _uw_rolling(close, _TD_QTR).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).max()


def uw_051_max_sustained_submersion_252d(close: pd.Series) -> pd.Series:
    """Maximum single-day underwater depth seen in trailing 252-day window."""
    return _uw_rolling(close, _TD_YEAR).abs().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).max()


def uw_052_max_sustained_submersion_ath(close: pd.Series) -> pd.Series:
    """Expanding maximum ATH drawdown depth (all-time maximum pain)."""
    return _uw_expanding(close).abs().expanding(min_periods=1).max()


def uw_053_area_to_mdd_ratio_63d(close: pd.Series) -> pd.Series:
    """63-day area divided by 63-day max drawdown depth (area per unit of depth)."""
    area = uw_002_area_63d_rolling(close)
    mdd = _uw_rolling(close, _TD_QTR).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).max()
    return _safe_div(area, mdd + _EPS)


def uw_054_area_to_mdd_ratio_252d(close: pd.Series) -> pd.Series:
    """252-day area divided by 252-day max drawdown depth."""
    area = uw_004_area_252d_rolling(close)
    mdd = _uw_rolling(close, _TD_YEAR).abs().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).max()
    return _safe_div(area, mdd + _EPS)


def uw_055_area_to_mdd_ratio_ath(close: pd.Series) -> pd.Series:
    """Expanding ATH area divided by expanding ATH max depth."""
    area = uw_007_area_ath_expanding(close)
    mdd = _uw_expanding(close).abs().expanding(min_periods=1).max()
    return _safe_div(area, mdd + _EPS)


def uw_056_conditional_mean_depth_below20_252d(close: pd.Series) -> pd.Series:
    """Mean underwater depth on days where drawdown exceeds 20% (conditional pain)."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    deep = uw.where(uw > 0.20)
    return deep.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def uw_057_conditional_mean_depth_below10_252d(close: pd.Series) -> pd.Series:
    """Mean underwater depth on days where drawdown exceeds 10%."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    deep = uw.where(uw > 0.10)
    return deep.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def uw_058_conditional_area_below20_252d(close: pd.Series) -> pd.Series:
    """Sum of underwater depths on days exceeding 20% drawdown over 252 days."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    deep = uw.where(uw > 0.20, 0.0)
    return deep.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).sum()


def uw_059_conditional_area_below30_252d(close: pd.Series) -> pd.Series:
    """Sum of underwater depths exceeding 30% over 252 days."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    deep = uw.where(uw > 0.30, 0.0)
    return deep.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).sum()


def uw_060_conditional_area_below50_ath(close: pd.Series) -> pd.Series:
    """Expanding sum of ATH depths exceeding 50% (deep bear market accumulated pain)."""
    uw = _uw_expanding(close).abs()
    deep = uw.where(uw > 0.50, 0.0)
    return deep.expanding(min_periods=1).sum()


# --- Group E (061-075): Volatility-adjusted, volume-weighted, and shape metrics ---

def uw_061_vol_adj_area_63d(close: pd.Series) -> pd.Series:
    """63-day underwater area divided by 63-day return volatility (vol-adjusted pain)."""
    area = uw_002_area_63d_rolling(close)
    vol = close.pct_change().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).std()
    return _safe_div(area, vol + _EPS)


def uw_062_vol_adj_area_252d(close: pd.Series) -> pd.Series:
    """252-day underwater area divided by 252-day return volatility."""
    area = uw_004_area_252d_rolling(close)
    vol = close.pct_change().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).std()
    return _safe_div(area, vol + _EPS)


def uw_063_vol_adj_ulcer_252d(close: pd.Series) -> pd.Series:
    """Ulcer Index divided by return vol over 252d (Ulcer per unit of vol)."""
    ui = uw_023_ulcer_index_252d(close)
    vol = close.pct_change().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).std()
    return _safe_div(ui, vol + _EPS)


def uw_064_volume_weighted_area_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted underwater area over 63 days (distress amplified by trading volume)."""
    uw = _uw_rolling(close, _TD_QTR).abs()
    avg_vol = _rolling_mean(volume, _TD_QTR)
    v_norm = _safe_div(volume, avg_vol + _EPS)
    return _rolling_sum(uw * v_norm, _TD_QTR)


def uw_065_volume_weighted_area_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted underwater area over 252 days."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    v_norm = _safe_div(volume, avg_vol + _EPS)
    return _rolling_sum(uw * v_norm, _TD_YEAR)


def uw_066_volume_weighted_pain_index_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean underwater depth over 252 days."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    v_norm = _safe_div(volume, avg_vol + _EPS)
    return _rolling_mean(uw * v_norm, _TD_YEAR)


def uw_067_high_vol_deep_uw_area_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Area of days with both above-avg volume AND underwater > 10% over 252d."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    flag = ((uw > 0.10) & (volume > avg_vol)).astype(float)
    return _rolling_sum(flag * uw, _TD_YEAR)


def uw_068_uw_area_dispersion_252d(close: pd.Series) -> pd.Series:
    """Standard deviation of daily underwater depths over 252d (depth volatility)."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    return _rolling_std(uw, _TD_YEAR)


def uw_069_uw_area_skew_252d(close: pd.Series) -> pd.Series:
    """Skewness of underwater depth distribution over 252d (tail shape)."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    return uw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).skew()


def uw_070_uw_area_kurt_252d(close: pd.Series) -> pd.Series:
    """Kurtosis of underwater depth distribution over 252d (tail heaviness)."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    return uw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).kurt()


def uw_071_uw_area_q90_252d(close: pd.Series) -> pd.Series:
    """90th percentile of underwater depths over 252d (severe-day threshold)."""
    uw = _uw_rolling(close, _TD_YEAR).abs()
    return uw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.90)


def uw_072_uw_area_q95_ath_expanding(close: pd.Series) -> pd.Series:
    """Expanding 95th percentile of ATH underwater depths (extreme pain marker)."""
    uw = _uw_expanding(close).abs()
    return uw.expanding(min_periods=1).quantile(0.95)


def uw_073_uw_path_length_63d(close: pd.Series) -> pd.Series:
    """Total variation of underwater series over 63d (curve roughness/agitation)."""
    uw = _uw_rolling(close, _TD_QTR)
    return uw.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()


def uw_074_uw_path_length_252d(close: pd.Series) -> pd.Series:
    """Total variation of underwater series over 252d."""
    uw = _uw_rolling(close, _TD_YEAR)
    return uw.diff(1).abs().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).sum()


def uw_075_uw_convexity_score_252d(close: pd.Series) -> pd.Series:
    """Area / (window * MDD): how 'filled' the underwater region is vs worst-case depth."""
    area = uw_004_area_252d_rolling(close)
    mdd = _uw_rolling(close, _TD_YEAR).abs().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).max()
    return _safe_div(area, (_TD_YEAR * mdd) + _EPS)


# ── Registry ──────────────────────────────────────────────────────────────────

UNDERWATER_CURVE_REGISTRY_001_075 = {
    "uw_001_area_21d_rolling": {"inputs": ["close"], "func": uw_001_area_21d_rolling},
    "uw_002_area_63d_rolling": {"inputs": ["close"], "func": uw_002_area_63d_rolling},
    "uw_003_area_126d_rolling": {"inputs": ["close"], "func": uw_003_area_126d_rolling},
    "uw_004_area_252d_rolling": {"inputs": ["close"], "func": uw_004_area_252d_rolling},
    "uw_005_area_504d_rolling": {"inputs": ["close"], "func": uw_005_area_504d_rolling},
    "uw_006_area_756d_rolling": {"inputs": ["close"], "func": uw_006_area_756d_rolling},
    "uw_007_area_ath_expanding": {"inputs": ["close"], "func": uw_007_area_ath_expanding},
    "uw_008_area_normalized_21d": {"inputs": ["close"], "func": uw_008_area_normalized_21d},
    "uw_009_area_normalized_63d": {"inputs": ["close"], "func": uw_009_area_normalized_63d},
    "uw_010_area_normalized_252d": {"inputs": ["close"], "func": uw_010_area_normalized_252d},
    "uw_011_area_log_21d": {"inputs": ["close"], "func": uw_011_area_log_21d},
    "uw_012_area_log_63d": {"inputs": ["close"], "func": uw_012_area_log_63d},
    "uw_013_area_log_252d": {"inputs": ["close"], "func": uw_013_area_log_252d},
    "uw_014_area_log_ath_expanding": {"inputs": ["close"], "func": uw_014_area_log_ath_expanding},
    "uw_015_area_intraday_low_252d": {"inputs": ["close", "high", "low"], "func": uw_015_area_intraday_low_252d},
    "uw_016_pain_index_21d": {"inputs": ["close"], "func": uw_016_pain_index_21d},
    "uw_017_pain_index_63d": {"inputs": ["close"], "func": uw_017_pain_index_63d},
    "uw_018_pain_index_252d": {"inputs": ["close"], "func": uw_018_pain_index_252d},
    "uw_019_pain_index_504d": {"inputs": ["close"], "func": uw_019_pain_index_504d},
    "uw_020_pain_index_ath_expanding": {"inputs": ["close"], "func": uw_020_pain_index_ath_expanding},
    "uw_021_ulcer_index_21d": {"inputs": ["close"], "func": uw_021_ulcer_index_21d},
    "uw_022_ulcer_index_63d": {"inputs": ["close"], "func": uw_022_ulcer_index_63d},
    "uw_023_ulcer_index_252d": {"inputs": ["close"], "func": uw_023_ulcer_index_252d},
    "uw_024_ulcer_index_504d": {"inputs": ["close"], "func": uw_024_ulcer_index_504d},
    "uw_025_ulcer_index_ath_expanding": {"inputs": ["close"], "func": uw_025_ulcer_index_ath_expanding},
    "uw_026_pain_index_median_63d": {"inputs": ["close"], "func": uw_026_pain_index_median_63d},
    "uw_027_pain_index_median_252d": {"inputs": ["close"], "func": uw_027_pain_index_median_252d},
    "uw_028_ulcer_index_log_63d": {"inputs": ["close"], "func": uw_028_ulcer_index_log_63d},
    "uw_029_ulcer_index_log_252d": {"inputs": ["close"], "func": uw_029_ulcer_index_log_252d},
    "uw_030_pain_vs_ulcer_ratio_252d": {"inputs": ["close"], "func": uw_030_pain_vs_ulcer_ratio_252d},
    "uw_031_area_linear_weighted_21d": {"inputs": ["close"], "func": uw_031_area_linear_weighted_21d},
    "uw_032_area_linear_weighted_63d": {"inputs": ["close"], "func": uw_032_area_linear_weighted_63d},
    "uw_033_area_linear_weighted_252d": {"inputs": ["close"], "func": uw_033_area_linear_weighted_252d},
    "uw_034_area_exp_weighted_21d": {"inputs": ["close"], "func": uw_034_area_exp_weighted_21d},
    "uw_035_area_exp_weighted_63d": {"inputs": ["close"], "func": uw_035_area_exp_weighted_63d},
    "uw_036_area_exp_weighted_252d": {"inputs": ["close"], "func": uw_036_area_exp_weighted_252d},
    "uw_037_area_front_half_vs_back_half_63d": {"inputs": ["close"], "func": uw_037_area_front_half_vs_back_half_63d},
    "uw_038_area_front_half_vs_back_half_252d": {"inputs": ["close"], "func": uw_038_area_front_half_vs_back_half_252d},
    "uw_039_area_quarter_ratio_63d": {"inputs": ["close"], "func": uw_039_area_quarter_ratio_63d},
    "uw_040_area_month_ratio_63d": {"inputs": ["close"], "func": uw_040_area_month_ratio_63d},
    "uw_041_area_cumulative_ath_vs_1yr_ratio": {"inputs": ["close"], "func": uw_041_area_cumulative_ath_vs_1yr_ratio},
    "uw_042_area_21d_vs_252d_ratio": {"inputs": ["close"], "func": uw_042_area_21d_vs_252d_ratio},
    "uw_043_area_63d_vs_252d_ratio": {"inputs": ["close"], "func": uw_043_area_63d_vs_252d_ratio},
    "uw_044_area_126d_vs_504d_ratio": {"inputs": ["close"], "func": uw_044_area_126d_vs_504d_ratio},
    "uw_045_area_cumsum_acceleration_21d": {"inputs": ["close"], "func": uw_045_area_cumsum_acceleration_21d},
    "uw_046_intensity_depth_x_area_63d": {"inputs": ["close"], "func": uw_046_intensity_depth_x_area_63d},
    "uw_047_intensity_depth_x_area_252d": {"inputs": ["close"], "func": uw_047_intensity_depth_x_area_252d},
    "uw_048_intensity_ath_depth_x_ath_area": {"inputs": ["close"], "func": uw_048_intensity_ath_depth_x_ath_area},
    "uw_049_intensity_ulcer_x_area_252d": {"inputs": ["close"], "func": uw_049_intensity_ulcer_x_area_252d},
    "uw_050_max_sustained_submersion_63d": {"inputs": ["close"], "func": uw_050_max_sustained_submersion_63d},
    "uw_051_max_sustained_submersion_252d": {"inputs": ["close"], "func": uw_051_max_sustained_submersion_252d},
    "uw_052_max_sustained_submersion_ath": {"inputs": ["close"], "func": uw_052_max_sustained_submersion_ath},
    "uw_053_area_to_mdd_ratio_63d": {"inputs": ["close"], "func": uw_053_area_to_mdd_ratio_63d},
    "uw_054_area_to_mdd_ratio_252d": {"inputs": ["close"], "func": uw_054_area_to_mdd_ratio_252d},
    "uw_055_area_to_mdd_ratio_ath": {"inputs": ["close"], "func": uw_055_area_to_mdd_ratio_ath},
    "uw_056_conditional_mean_depth_below20_252d": {"inputs": ["close"], "func": uw_056_conditional_mean_depth_below20_252d},
    "uw_057_conditional_mean_depth_below10_252d": {"inputs": ["close"], "func": uw_057_conditional_mean_depth_below10_252d},
    "uw_058_conditional_area_below20_252d": {"inputs": ["close"], "func": uw_058_conditional_area_below20_252d},
    "uw_059_conditional_area_below30_252d": {"inputs": ["close"], "func": uw_059_conditional_area_below30_252d},
    "uw_060_conditional_area_below50_ath": {"inputs": ["close"], "func": uw_060_conditional_area_below50_ath},
    "uw_061_vol_adj_area_63d": {"inputs": ["close"], "func": uw_061_vol_adj_area_63d},
    "uw_062_vol_adj_area_252d": {"inputs": ["close"], "func": uw_062_vol_adj_area_252d},
    "uw_063_vol_adj_ulcer_252d": {"inputs": ["close"], "func": uw_063_vol_adj_ulcer_252d},
    "uw_064_volume_weighted_area_63d": {"inputs": ["close", "volume"], "func": uw_064_volume_weighted_area_63d},
    "uw_065_volume_weighted_area_252d": {"inputs": ["close", "volume"], "func": uw_065_volume_weighted_area_252d},
    "uw_066_volume_weighted_pain_index_252d": {"inputs": ["close", "volume"], "func": uw_066_volume_weighted_pain_index_252d},
    "uw_067_high_vol_deep_uw_area_252d": {"inputs": ["close", "volume"], "func": uw_067_high_vol_deep_uw_area_252d},
    "uw_068_uw_area_dispersion_252d": {"inputs": ["close"], "func": uw_068_uw_area_dispersion_252d},
    "uw_069_uw_area_skew_252d": {"inputs": ["close"], "func": uw_069_uw_area_skew_252d},
    "uw_070_uw_area_kurt_252d": {"inputs": ["close"], "func": uw_070_uw_area_kurt_252d},
    "uw_071_uw_area_q90_252d": {"inputs": ["close"], "func": uw_071_uw_area_q90_252d},
    "uw_072_uw_area_q95_ath_expanding": {"inputs": ["close"], "func": uw_072_uw_area_q95_ath_expanding},
    "uw_073_uw_path_length_63d": {"inputs": ["close"], "func": uw_073_uw_path_length_63d},
    "uw_074_uw_path_length_252d": {"inputs": ["close"], "func": uw_074_uw_path_length_252d},
    "uw_075_uw_convexity_score_252d": {"inputs": ["close"], "func": uw_075_uw_convexity_score_252d},
}
