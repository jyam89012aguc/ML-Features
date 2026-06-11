"""
01_drawdown_depth — Base Features 001-075
Domain: decline magnitude vs trailing highs (1/3/5y, ATH)
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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Raw close-to-peak drawdown, various windows ---

def dd_001_drawdown_from_21d_high(close: pd.Series) -> pd.Series:
    """Close vs 21-day rolling high (1-month drawdown)."""
    h = _rolling_max(close, _TD_MON)
    return _safe_div(close - h, h)


def dd_002_drawdown_from_63d_high(close: pd.Series) -> pd.Series:
    """Close vs 63-day rolling high (1-quarter drawdown)."""
    h = _rolling_max(close, _TD_QTR)
    return _safe_div(close - h, h)


def dd_003_drawdown_from_126d_high(close: pd.Series) -> pd.Series:
    """Close vs 126-day rolling high (half-year drawdown)."""
    h = _rolling_max(close, _TD_HALF)
    return _safe_div(close - h, h)


def dd_004_drawdown_from_252d_high(close: pd.Series) -> pd.Series:
    """Close vs 252-day rolling high (1-year drawdown)."""
    h = _rolling_max(close, _TD_YEAR)
    return _safe_div(close - h, h)


def dd_005_drawdown_from_504d_high(close: pd.Series) -> pd.Series:
    """Close vs 504-day rolling high (2-year drawdown)."""
    h = _rolling_max(close, 504)
    return _safe_div(close - h, h)


def dd_006_drawdown_from_756d_high(close: pd.Series) -> pd.Series:
    """Close vs 756-day rolling high (3-year drawdown)."""
    h = _rolling_max(close, 756)
    return _safe_div(close - h, h)


def dd_007_drawdown_from_1260d_high(close: pd.Series) -> pd.Series:
    """Close vs 1260-day rolling high (5-year drawdown)."""
    h = _rolling_max(close, 1260)
    return _safe_div(close - h, h)


def dd_008_drawdown_from_ath(close: pd.Series) -> pd.Series:
    """Close vs all-time-high (expanding max drawdown)."""
    h = close.expanding(min_periods=1).max()
    return _safe_div(close - h, h)


def dd_009_log_drawdown_from_252d_high(close: pd.Series) -> pd.Series:
    """Log-space drawdown from 252-day high."""
    h = _rolling_max(close, _TD_YEAR)
    return _log_safe(close) - _log_safe(h)


def dd_010_log_drawdown_from_ath(close: pd.Series) -> pd.Series:
    """Log-space drawdown from all-time high."""
    h = close.expanding(min_periods=1).max()
    return _log_safe(close) - _log_safe(h)


# --- Group B (011-020): Daily low vs peak drawdowns ---

def dd_011_low_drawdown_from_21d_close_high(close: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday low vs 21-day close high."""
    h = _rolling_max(close, _TD_MON)
    return _safe_div(low - h, h)


def dd_012_low_drawdown_from_63d_close_high(close: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday low vs 63-day close high."""
    h = _rolling_max(close, _TD_QTR)
    return _safe_div(low - h, h)


def dd_013_low_drawdown_from_252d_close_high(close: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday low vs 252-day close high."""
    h = _rolling_max(close, _TD_YEAR)
    return _safe_div(low - h, h)


def dd_014_low_drawdown_from_ath_close(close: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday low vs all-time close high."""
    h = close.expanding(min_periods=1).max()
    return _safe_div(low - h, h)


def dd_015_low_drawdown_from_252d_intraday_high(high: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday low vs 252-day intraday high."""
    h = _rolling_max(high, _TD_YEAR)
    return _safe_div(low - h, h)


def dd_016_low_drawdown_from_504d_intraday_high(high: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday low vs 504-day intraday high."""
    h = _rolling_max(high, 504)
    return _safe_div(low - h, h)


def dd_017_low_drawdown_from_ath_intraday(high: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday low vs all-time intraday high."""
    h = high.expanding(min_periods=1).max()
    return _safe_div(low - h, h)


def dd_018_open_drawdown_from_252d_high(close: pd.Series, open: pd.Series) -> pd.Series:
    """Open price vs 252-day close high."""
    h = _rolling_max(close, _TD_YEAR)
    return _safe_div(open - h, h)


def dd_019_open_drawdown_from_ath(close: pd.Series, open: pd.Series) -> pd.Series:
    """Open price vs all-time close high."""
    h = close.expanding(min_periods=1).max()
    return _safe_div(open - h, h)


def dd_020_close_vs_252d_low_range(close: pd.Series) -> pd.Series:
    """Close position within 252-day high-low range (0=low, 1=high)."""
    h = _rolling_max(close, _TD_YEAR)
    l = _rolling_min(close, _TD_YEAR)
    return _safe_div(close - l, h - l)


# --- Group C (021-030): Volatility-adjusted drawdown measures ---

def dd_021_dd_252d_vol_adj(close: pd.Series) -> pd.Series:
    """252-day drawdown divided by realized daily vol (annualized)."""
    dd = dd_004_drawdown_from_252d_high(close)
    vol = _rolling_std(_daily_ret(close), _TD_YEAR)
    return _safe_div(dd, vol)


def dd_022_dd_504d_vol_adj(close: pd.Series) -> pd.Series:
    """504-day drawdown divided by 504-day realized vol."""
    dd = dd_005_drawdown_from_504d_high(close)
    vol = _rolling_std(_daily_ret(close), 504)
    return _safe_div(dd, vol)


def dd_023_dd_ath_vol_adj(close: pd.Series) -> pd.Series:
    """ATH drawdown divided by expanding realized vol."""
    dd = dd_008_drawdown_from_ath(close)
    vol = _daily_ret(close).expanding(min_periods=5).std()
    return _safe_div(dd, vol)


def dd_024_dd_252d_cv_adj(close: pd.Series) -> pd.Series:
    """252-day drawdown divided by coefficient of variation (std/mean)."""
    dd = dd_004_drawdown_from_252d_high(close)
    cv = _safe_div(_rolling_std(close, _TD_YEAR), _rolling_mean(close, _TD_YEAR))
    return _safe_div(dd, cv)


def dd_025_dd_63d_vol_adj(close: pd.Series) -> pd.Series:
    """63-day drawdown divided by 63-day realized vol."""
    dd = dd_002_drawdown_from_63d_high(close)
    vol = _rolling_std(_daily_ret(close), _TD_QTR)
    return _safe_div(dd, vol)


def dd_026_dd_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 252-day drawdown over a trailing 252-day window."""
    dd = dd_004_drawdown_from_252d_high(close)
    return _zscore_rolling(dd, _TD_YEAR)


def dd_027_dd_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of 252-day drawdown over a trailing 504-day window."""
    dd = dd_004_drawdown_from_252d_high(close)
    return _zscore_rolling(dd, 504)


def dd_028_dd_zscore_1260d(close: pd.Series) -> pd.Series:
    """Z-score of 1260-day drawdown over trailing 1260-day window."""
    dd = dd_007_drawdown_from_1260d_high(close)
    return _zscore_rolling(dd, 1260)


def dd_029_dd_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding z-score of ATH drawdown (how extreme vs own history)."""
    dd = dd_008_drawdown_from_ath(close)
    m = dd.expanding(min_periods=5).mean()
    sd = dd.expanding(min_periods=5).std()
    return _safe_div(dd - m, sd)


def dd_030_dd_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 252-day drawdown within trailing 252-day window."""
    dd = dd_004_drawdown_from_252d_high(close)
    return _rolling_rank_pct(dd, _TD_YEAR)


# --- Group D (031-040): Multi-window ratios and intensity ---

def dd_031_dd_ratio_63d_to_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63-day dd to 252-day dd (recent vs annual severity)."""
    return _safe_div(dd_002_drawdown_from_63d_high(close), dd_004_drawdown_from_252d_high(close))


def dd_032_dd_ratio_21d_to_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day dd to 63-day dd (short-term acceleration)."""
    return _safe_div(dd_001_drawdown_from_21d_high(close), dd_002_drawdown_from_63d_high(close))


def dd_033_dd_ratio_252d_to_ath(close: pd.Series) -> pd.Series:
    """Ratio of 252-day dd to ATH dd (how much of ATH dd is recent)."""
    return _safe_div(dd_004_drawdown_from_252d_high(close), dd_008_drawdown_from_ath(close))


def dd_034_dd_ratio_504d_to_ath(close: pd.Series) -> pd.Series:
    """Ratio of 504-day dd to ATH dd."""
    return _safe_div(dd_005_drawdown_from_504d_high(close), dd_008_drawdown_from_ath(close))


def dd_035_dd_ratio_126d_to_504d(close: pd.Series) -> pd.Series:
    """Ratio of 126-day dd to 504-day dd."""
    return _safe_div(dd_003_drawdown_from_126d_high(close), dd_005_drawdown_from_504d_high(close))


def dd_036_dd_intensity_252d(close: pd.Series) -> pd.Series:
    """Current 252-day dd as fraction of trailing 252-day max drawdown."""
    dd = dd_004_drawdown_from_252d_high(close)
    mdd = _rolling_min(dd, _TD_YEAR)
    return _safe_div(dd, mdd)


def dd_037_dd_intensity_1260d(close: pd.Series) -> pd.Series:
    """Current 252-day dd as fraction of trailing 5-year max drawdown."""
    dd = dd_004_drawdown_from_252d_high(close)
    mdd = _rolling_min(dd, 1260)
    return _safe_div(dd, mdd)


def dd_038_dd_intensity_ath(close: pd.Series) -> pd.Series:
    """ATH dd as fraction of expanding maximum ATH dd."""
    dd = dd_008_drawdown_from_ath(close)
    mdd = dd.expanding(min_periods=1).min()
    return _safe_div(dd, mdd)


def dd_039_dd_pct_rank_1260d(close: pd.Series) -> pd.Series:
    """Percentile rank of ATH drawdown within trailing 1260-day window."""
    dd = dd_008_drawdown_from_ath(close)
    return _rolling_rank_pct(dd, 1260)


def dd_040_dd_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 252d drawdown (all-history rank)."""
    dd = dd_004_drawdown_from_252d_high(close)
    return dd.expanding(min_periods=5).rank(pct=True)


# --- Group E (041-050): Moving-average-based drawdown measures ---

def dd_041_close_vs_sma21(close: pd.Series) -> pd.Series:
    """Percent deviation of close from 21-day SMA."""
    ma = _rolling_mean(close, _TD_MON)
    return _safe_div(close - ma, ma)


def dd_042_close_vs_sma63(close: pd.Series) -> pd.Series:
    """Percent deviation of close from 63-day SMA."""
    ma = _rolling_mean(close, _TD_QTR)
    return _safe_div(close - ma, ma)


def dd_043_close_vs_sma126(close: pd.Series) -> pd.Series:
    """Percent deviation of close from 126-day SMA."""
    ma = _rolling_mean(close, _TD_HALF)
    return _safe_div(close - ma, ma)


def dd_044_close_vs_sma200(close: pd.Series) -> pd.Series:
    """Percent deviation of close from 200-day SMA."""
    ma = _rolling_mean(close, 200)
    return _safe_div(close - ma, ma)


def dd_045_close_vs_ema21(close: pd.Series) -> pd.Series:
    """Percent deviation of close from 21-day EMA."""
    ma = _ewm_mean(close, _TD_MON)
    return _safe_div(close - ma, ma)


def dd_046_close_vs_ema63(close: pd.Series) -> pd.Series:
    """Percent deviation of close from 63-day EMA."""
    ma = _ewm_mean(close, _TD_QTR)
    return _safe_div(close - ma, ma)


def dd_047_close_vs_ema200(close: pd.Series) -> pd.Series:
    """Percent deviation of close from 200-day EMA."""
    ma = _ewm_mean(close, 200)
    return _safe_div(close - ma, ma)


def dd_048_sma21_vs_sma200(close: pd.Series) -> pd.Series:
    """Percent deviation of 21-day SMA from 200-day SMA (golden/death cross)."""
    ma21 = _rolling_mean(close, _TD_MON)
    ma200 = _rolling_mean(close, 200)
    return _safe_div(ma21 - ma200, ma200)


def dd_049_sma63_vs_sma200(close: pd.Series) -> pd.Series:
    """Percent deviation of 63-day SMA from 200-day SMA."""
    ma63 = _rolling_mean(close, _TD_QTR)
    ma200 = _rolling_mean(close, 200)
    return _safe_div(ma63 - ma200, ma200)


def dd_050_ema21_vs_ema200(close: pd.Series) -> pd.Series:
    """Percent deviation of 21-day EMA from 200-day EMA."""
    ema21 = _ewm_mean(close, _TD_MON)
    ema200 = _ewm_mean(close, 200)
    return _safe_div(ema21 - ema200, ema200)


# --- Group F (051-060): Drawdown persistence and area measures ---

def dd_051_underwater_fraction_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days where close was below its own prior 252d high."""
    dd = dd_004_drawdown_from_252d_high(close)
    below = (dd < 0).astype(float)
    return _rolling_mean(below, _TD_YEAR)


def dd_052_underwater_fraction_504d(close: pd.Series) -> pd.Series:
    """Fraction of last 504 days below own 252-day rolling high."""
    dd = dd_004_drawdown_from_252d_high(close)
    below = (dd < 0).astype(float)
    return _rolling_mean(below, 504)


def dd_053_avg_dd_252d(close: pd.Series) -> pd.Series:
    """Mean 252-day drawdown depth over trailing 252 days."""
    dd = dd_004_drawdown_from_252d_high(close)
    return _rolling_mean(dd, _TD_YEAR)


def dd_054_avg_dd_504d(close: pd.Series) -> pd.Series:
    """Mean 252-day drawdown depth over trailing 504 days."""
    dd = dd_004_drawdown_from_252d_high(close)
    return _rolling_mean(dd, 504)


def dd_055_dd_area_63d(close: pd.Series) -> pd.Series:
    """Sum of 63-day drawdown values over trailing 63 days (area under curve)."""
    dd = dd_002_drawdown_from_63d_high(close)
    return _rolling_sum(dd, _TD_QTR)


def dd_056_dd_area_252d(close: pd.Series) -> pd.Series:
    """Sum of 252-day drawdown values over trailing 252 days."""
    dd = dd_004_drawdown_from_252d_high(close)
    return _rolling_sum(dd, _TD_YEAR)


def dd_057_dd_vol_of_dd_63d(close: pd.Series) -> pd.Series:
    """Std dev of 63-day drawdown series over trailing 63 days."""
    dd = dd_002_drawdown_from_63d_high(close)
    return _rolling_std(dd, _TD_QTR)


def dd_058_dd_vol_of_dd_252d(close: pd.Series) -> pd.Series:
    """Std dev of 252-day drawdown series over trailing 252 days."""
    dd = dd_004_drawdown_from_252d_high(close)
    return _rolling_std(dd, _TD_YEAR)


def dd_059_dd_skew_252d(close: pd.Series) -> pd.Series:
    """Skewness of daily returns over trailing 252 days (negative = left tail)."""
    return _daily_ret(close).rolling(_TD_YEAR, min_periods=_TD_QTR).skew()


def dd_060_dd_kurtosis_252d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of daily returns over trailing 252 days (fat tails)."""
    return _daily_ret(close).rolling(_TD_YEAR, min_periods=_TD_QTR).kurt()


# --- Group G (061-075): Log-spread, range, and ATR-based drawdown measures ---

def dd_061_log_spread_from_252d_high(close: pd.Series) -> pd.Series:
    """Log distance from current close to 252-day high (always positive)."""
    h = _rolling_max(close, _TD_YEAR)
    return _log_safe(h) - _log_safe(close)


def dd_062_log_spread_from_ath(close: pd.Series) -> pd.Series:
    """Log distance from current close to all-time high."""
    h = close.expanding(min_periods=1).max()
    return _log_safe(h) - _log_safe(close)


def dd_063_log_spread_from_504d_high(close: pd.Series) -> pd.Series:
    """Log distance from current close to 504-day high."""
    h = _rolling_max(close, 504)
    return _log_safe(h) - _log_safe(close)


def dd_064_atr_normalized_dd_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day drawdown expressed in ATR units."""
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)
    atr = _rolling_mean(tr, _TD_QTR)
    h = _rolling_max(close, _TD_QTR)
    return _safe_div(close - h, atr)


def dd_065_atr_normalized_dd_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day drawdown expressed in 252-day ATR units."""
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)
    atr = _rolling_mean(tr, _TD_YEAR)
    h = _rolling_max(close, _TD_YEAR)
    return _safe_div(close - h, atr)


def dd_066_dd_vs_252d_range(close: pd.Series) -> pd.Series:
    """252-day drawdown normalized by 252-day high-low range."""
    h = _rolling_max(close, _TD_YEAR)
    l = _rolling_min(close, _TD_YEAR)
    return _safe_div(close - h, h - l)


def dd_067_dd_vs_504d_range(close: pd.Series) -> pd.Series:
    """504-day drawdown normalized by 504-day high-low range."""
    h = _rolling_max(close, 504)
    l = _rolling_min(close, 504)
    return _safe_div(close - h, h - l)


def dd_068_close_vs_252d_low(close: pd.Series) -> pd.Series:
    """Percent above the 252-day closing low (distance from trough)."""
    l = _rolling_min(close, _TD_YEAR)
    return _safe_div(close - l, l)


def dd_069_close_vs_504d_low(close: pd.Series) -> pd.Series:
    """Percent above the 504-day closing low."""
    l = _rolling_min(close, 504)
    return _safe_div(close - l, l)


def dd_070_close_vs_1260d_low(close: pd.Series) -> pd.Series:
    """Percent above the 1260-day (5-year) closing low."""
    l = _rolling_min(close, 1260)
    return _safe_div(close - l, l)


def dd_071_close_vs_ath_low_ratio(close: pd.Series) -> pd.Series:
    """Ratio of current close to expanding (all-time) closing low."""
    l = close.expanding(min_periods=1).min()
    return _safe_div(close, l)


def dd_072_volume_weighted_dd_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted 252-day drawdown (distress weighted by trading activity)."""
    dd = dd_004_drawdown_from_252d_high(close)
    v_norm = _safe_div(volume, _rolling_mean(volume, _TD_YEAR))
    return _rolling_mean(dd * v_norm, _TD_YEAR)


def dd_073_volume_weighted_dd_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted 63-day drawdown."""
    dd = dd_002_drawdown_from_63d_high(close)
    v_norm = _safe_div(volume, _rolling_mean(volume, _TD_QTR))
    return _rolling_mean(dd * v_norm, _TD_QTR)


def dd_074_dd_tail_q05_252d(close: pd.Series) -> pd.Series:
    """5th percentile of 252-day drawdown over trailing 252-day window (tail risk)."""
    dd = dd_004_drawdown_from_252d_high(close)
    return dd.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.05)


def dd_075_dd_composite_weighted(close: pd.Series) -> pd.Series:
    """Composite drawdown: 50% 21d + 30% 63d + 20% 252d (multi-scale severity)."""
    dd21 = dd_001_drawdown_from_21d_high(close)
    dd63 = dd_002_drawdown_from_63d_high(close)
    dd252 = dd_004_drawdown_from_252d_high(close)
    return 0.5 * dd21 + 0.3 * dd63 + 0.2 * dd252


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_DEPTH_REGISTRY_001_075 = {
    "dd_001_drawdown_from_21d_high": {"inputs": ["close"], "func": dd_001_drawdown_from_21d_high},
    "dd_002_drawdown_from_63d_high": {"inputs": ["close"], "func": dd_002_drawdown_from_63d_high},
    "dd_003_drawdown_from_126d_high": {"inputs": ["close"], "func": dd_003_drawdown_from_126d_high},
    "dd_004_drawdown_from_252d_high": {"inputs": ["close"], "func": dd_004_drawdown_from_252d_high},
    "dd_005_drawdown_from_504d_high": {"inputs": ["close"], "func": dd_005_drawdown_from_504d_high},
    "dd_006_drawdown_from_756d_high": {"inputs": ["close"], "func": dd_006_drawdown_from_756d_high},
    "dd_007_drawdown_from_1260d_high": {"inputs": ["close"], "func": dd_007_drawdown_from_1260d_high},
    "dd_008_drawdown_from_ath": {"inputs": ["close"], "func": dd_008_drawdown_from_ath},
    "dd_009_log_drawdown_from_252d_high": {"inputs": ["close"], "func": dd_009_log_drawdown_from_252d_high},
    "dd_010_log_drawdown_from_ath": {"inputs": ["close"], "func": dd_010_log_drawdown_from_ath},
    "dd_011_low_drawdown_from_21d_close_high": {"inputs": ["close", "low"], "func": dd_011_low_drawdown_from_21d_close_high},
    "dd_012_low_drawdown_from_63d_close_high": {"inputs": ["close", "low"], "func": dd_012_low_drawdown_from_63d_close_high},
    "dd_013_low_drawdown_from_252d_close_high": {"inputs": ["close", "low"], "func": dd_013_low_drawdown_from_252d_close_high},
    "dd_014_low_drawdown_from_ath_close": {"inputs": ["close", "low"], "func": dd_014_low_drawdown_from_ath_close},
    "dd_015_low_drawdown_from_252d_intraday_high": {"inputs": ["high", "low"], "func": dd_015_low_drawdown_from_252d_intraday_high},
    "dd_016_low_drawdown_from_504d_intraday_high": {"inputs": ["high", "low"], "func": dd_016_low_drawdown_from_504d_intraday_high},
    "dd_017_low_drawdown_from_ath_intraday": {"inputs": ["high", "low"], "func": dd_017_low_drawdown_from_ath_intraday},
    "dd_018_open_drawdown_from_252d_high": {"inputs": ["close", "open"], "func": dd_018_open_drawdown_from_252d_high},
    "dd_019_open_drawdown_from_ath": {"inputs": ["close", "open"], "func": dd_019_open_drawdown_from_ath},
    "dd_020_close_vs_252d_low_range": {"inputs": ["close"], "func": dd_020_close_vs_252d_low_range},
    "dd_021_dd_252d_vol_adj": {"inputs": ["close"], "func": dd_021_dd_252d_vol_adj},
    "dd_022_dd_504d_vol_adj": {"inputs": ["close"], "func": dd_022_dd_504d_vol_adj},
    "dd_023_dd_ath_vol_adj": {"inputs": ["close"], "func": dd_023_dd_ath_vol_adj},
    "dd_024_dd_252d_cv_adj": {"inputs": ["close"], "func": dd_024_dd_252d_cv_adj},
    "dd_025_dd_63d_vol_adj": {"inputs": ["close"], "func": dd_025_dd_63d_vol_adj},
    "dd_026_dd_zscore_252d": {"inputs": ["close"], "func": dd_026_dd_zscore_252d},
    "dd_027_dd_zscore_504d": {"inputs": ["close"], "func": dd_027_dd_zscore_504d},
    "dd_028_dd_zscore_1260d": {"inputs": ["close"], "func": dd_028_dd_zscore_1260d},
    "dd_029_dd_expanding_zscore": {"inputs": ["close"], "func": dd_029_dd_expanding_zscore},
    "dd_030_dd_pct_rank_252d": {"inputs": ["close"], "func": dd_030_dd_pct_rank_252d},
    "dd_031_dd_ratio_63d_to_252d": {"inputs": ["close"], "func": dd_031_dd_ratio_63d_to_252d},
    "dd_032_dd_ratio_21d_to_63d": {"inputs": ["close"], "func": dd_032_dd_ratio_21d_to_63d},
    "dd_033_dd_ratio_252d_to_ath": {"inputs": ["close"], "func": dd_033_dd_ratio_252d_to_ath},
    "dd_034_dd_ratio_504d_to_ath": {"inputs": ["close"], "func": dd_034_dd_ratio_504d_to_ath},
    "dd_035_dd_ratio_126d_to_504d": {"inputs": ["close"], "func": dd_035_dd_ratio_126d_to_504d},
    "dd_036_dd_intensity_252d": {"inputs": ["close"], "func": dd_036_dd_intensity_252d},
    "dd_037_dd_intensity_1260d": {"inputs": ["close"], "func": dd_037_dd_intensity_1260d},
    "dd_038_dd_intensity_ath": {"inputs": ["close"], "func": dd_038_dd_intensity_ath},
    "dd_039_dd_pct_rank_1260d": {"inputs": ["close"], "func": dd_039_dd_pct_rank_1260d},
    "dd_040_dd_expanding_pct_rank": {"inputs": ["close"], "func": dd_040_dd_expanding_pct_rank},
    "dd_041_close_vs_sma21": {"inputs": ["close"], "func": dd_041_close_vs_sma21},
    "dd_042_close_vs_sma63": {"inputs": ["close"], "func": dd_042_close_vs_sma63},
    "dd_043_close_vs_sma126": {"inputs": ["close"], "func": dd_043_close_vs_sma126},
    "dd_044_close_vs_sma200": {"inputs": ["close"], "func": dd_044_close_vs_sma200},
    "dd_045_close_vs_ema21": {"inputs": ["close"], "func": dd_045_close_vs_ema21},
    "dd_046_close_vs_ema63": {"inputs": ["close"], "func": dd_046_close_vs_ema63},
    "dd_047_close_vs_ema200": {"inputs": ["close"], "func": dd_047_close_vs_ema200},
    "dd_048_sma21_vs_sma200": {"inputs": ["close"], "func": dd_048_sma21_vs_sma200},
    "dd_049_sma63_vs_sma200": {"inputs": ["close"], "func": dd_049_sma63_vs_sma200},
    "dd_050_ema21_vs_ema200": {"inputs": ["close"], "func": dd_050_ema21_vs_ema200},
    "dd_051_underwater_fraction_252d": {"inputs": ["close"], "func": dd_051_underwater_fraction_252d},
    "dd_052_underwater_fraction_504d": {"inputs": ["close"], "func": dd_052_underwater_fraction_504d},
    "dd_053_avg_dd_252d": {"inputs": ["close"], "func": dd_053_avg_dd_252d},
    "dd_054_avg_dd_504d": {"inputs": ["close"], "func": dd_054_avg_dd_504d},
    "dd_055_dd_area_63d": {"inputs": ["close"], "func": dd_055_dd_area_63d},
    "dd_056_dd_area_252d": {"inputs": ["close"], "func": dd_056_dd_area_252d},
    "dd_057_dd_vol_of_dd_63d": {"inputs": ["close"], "func": dd_057_dd_vol_of_dd_63d},
    "dd_058_dd_vol_of_dd_252d": {"inputs": ["close"], "func": dd_058_dd_vol_of_dd_252d},
    "dd_059_dd_skew_252d": {"inputs": ["close"], "func": dd_059_dd_skew_252d},
    "dd_060_dd_kurtosis_252d": {"inputs": ["close"], "func": dd_060_dd_kurtosis_252d},
    "dd_061_log_spread_from_252d_high": {"inputs": ["close"], "func": dd_061_log_spread_from_252d_high},
    "dd_062_log_spread_from_ath": {"inputs": ["close"], "func": dd_062_log_spread_from_ath},
    "dd_063_log_spread_from_504d_high": {"inputs": ["close"], "func": dd_063_log_spread_from_504d_high},
    "dd_064_atr_normalized_dd_63d": {"inputs": ["close", "high", "low"], "func": dd_064_atr_normalized_dd_63d},
    "dd_065_atr_normalized_dd_252d": {"inputs": ["close", "high", "low"], "func": dd_065_atr_normalized_dd_252d},
    "dd_066_dd_vs_252d_range": {"inputs": ["close"], "func": dd_066_dd_vs_252d_range},
    "dd_067_dd_vs_504d_range": {"inputs": ["close"], "func": dd_067_dd_vs_504d_range},
    "dd_068_close_vs_252d_low": {"inputs": ["close"], "func": dd_068_close_vs_252d_low},
    "dd_069_close_vs_504d_low": {"inputs": ["close"], "func": dd_069_close_vs_504d_low},
    "dd_070_close_vs_1260d_low": {"inputs": ["close"], "func": dd_070_close_vs_1260d_low},
    "dd_071_close_vs_ath_low_ratio": {"inputs": ["close"], "func": dd_071_close_vs_ath_low_ratio},
    "dd_072_volume_weighted_dd_252d": {"inputs": ["close", "volume"], "func": dd_072_volume_weighted_dd_252d},
    "dd_073_volume_weighted_dd_63d": {"inputs": ["close", "volume"], "func": dd_073_volume_weighted_dd_63d},
    "dd_074_dd_tail_q05_252d": {"inputs": ["close"], "func": dd_074_dd_tail_q05_252d},
    "dd_075_dd_composite_weighted": {"inputs": ["close"], "func": dd_075_dd_composite_weighted},
}
