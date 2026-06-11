"""
30_relative_strength — Base Features 001-075
Domain: price location relative to its own moving averages —
        SMA/EMA ratios, percent distances, depth below MA, MA count below
        price, MA stacking order, Mansfield-style RS (price vs long MA,
        z-scored / range-positioned), DEMA and TEMA constructs.
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


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _sma(close: pd.Series, w: int) -> pd.Series:
    return _rolling_mean(close, w)


def _ema(close: pd.Series, span: int) -> pd.Series:
    return _ewm_mean(close, span)


def _dema(close: pd.Series, span: int) -> pd.Series:
    """Double EMA: 2*EMA(n) - EMA(EMA(n))."""
    e1 = _ema(close, span)
    e2 = _ema(e1, span)
    return 2.0 * e1 - e2


def _tema(close: pd.Series, span: int) -> pd.Series:
    """Triple EMA: 3*EMA - 3*EMA(EMA) + EMA(EMA(EMA))."""
    e1 = _ema(close, span)
    e2 = _ema(e1, span)
    e3 = _ema(e2, span)
    return 3.0 * e1 - 3.0 * e2 + e3


def _mansfield_raw(close: pd.Series, long_period: int) -> pd.Series:
    """Raw Mansfield-style RS proxy: close/SMA(long) - 1."""
    ma = _sma(close, long_period)
    return _safe_div(close - ma, ma)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Close / SMA ratio (close ÷ SMA — level above/below) ---

def rst_001_close_to_sma10_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to 10-day SMA (>1 above, <1 below)."""
    return _safe_div(close, _sma(close, 10))


def rst_002_close_to_sma21_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to 21-day SMA."""
    return _safe_div(close, _sma(close, _TD_MON))


def rst_003_close_to_sma50_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to 50-day SMA."""
    return _safe_div(close, _sma(close, 50))


def rst_004_close_to_sma63_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to 63-day SMA."""
    return _safe_div(close, _sma(close, _TD_QTR))


def rst_005_close_to_sma100_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to 100-day SMA."""
    return _safe_div(close, _sma(close, 100))


def rst_006_close_to_sma200_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to 200-day SMA."""
    return _safe_div(close, _sma(close, 200))


def rst_007_close_to_ema10_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to 10-day EMA."""
    return _safe_div(close, _ema(close, 10))


def rst_008_close_to_ema21_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to 21-day EMA."""
    return _safe_div(close, _ema(close, _TD_MON))


def rst_009_close_to_ema50_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to 50-day EMA."""
    return _safe_div(close, _ema(close, 50))


def rst_010_close_to_ema63_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to 63-day EMA."""
    return _safe_div(close, _ema(close, _TD_QTR))


def rst_011_close_to_ema100_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to 100-day EMA."""
    return _safe_div(close, _ema(close, 100))


def rst_012_close_to_ema200_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to 200-day EMA."""
    return _safe_div(close, _ema(close, 200))


# --- Group B (013-024): Percent distance from MA (signed, %) ---

def rst_013_pct_dist_sma10(close: pd.Series) -> pd.Series:
    """Percent distance of close from 10-day SMA ((close-SMA)/SMA)."""
    ma = _sma(close, 10)
    return _safe_div(close - ma, ma)


def rst_014_pct_dist_sma21(close: pd.Series) -> pd.Series:
    """Percent distance of close from 21-day SMA."""
    ma = _sma(close, _TD_MON)
    return _safe_div(close - ma, ma)


def rst_015_pct_dist_sma50(close: pd.Series) -> pd.Series:
    """Percent distance of close from 50-day SMA."""
    ma = _sma(close, 50)
    return _safe_div(close - ma, ma)


def rst_016_pct_dist_sma63(close: pd.Series) -> pd.Series:
    """Percent distance of close from 63-day SMA."""
    ma = _sma(close, _TD_QTR)
    return _safe_div(close - ma, ma)


def rst_017_pct_dist_sma100(close: pd.Series) -> pd.Series:
    """Percent distance of close from 100-day SMA."""
    ma = _sma(close, 100)
    return _safe_div(close - ma, ma)


def rst_018_pct_dist_sma200(close: pd.Series) -> pd.Series:
    """Percent distance of close from 200-day SMA."""
    ma = _sma(close, 200)
    return _safe_div(close - ma, ma)


def rst_019_pct_dist_ema10(close: pd.Series) -> pd.Series:
    """Percent distance of close from 10-day EMA."""
    ma = _ema(close, 10)
    return _safe_div(close - ma, ma)


def rst_020_pct_dist_ema21(close: pd.Series) -> pd.Series:
    """Percent distance of close from 21-day EMA."""
    ma = _ema(close, _TD_MON)
    return _safe_div(close - ma, ma)


def rst_021_pct_dist_ema50(close: pd.Series) -> pd.Series:
    """Percent distance of close from 50-day EMA."""
    ma = _ema(close, 50)
    return _safe_div(close - ma, ma)


def rst_022_pct_dist_ema63(close: pd.Series) -> pd.Series:
    """Percent distance of close from 63-day EMA."""
    ma = _ema(close, _TD_QTR)
    return _safe_div(close - ma, ma)


def rst_023_pct_dist_ema100(close: pd.Series) -> pd.Series:
    """Percent distance of close from 100-day EMA."""
    ma = _ema(close, 100)
    return _safe_div(close - ma, ma)


def rst_024_pct_dist_ema200(close: pd.Series) -> pd.Series:
    """Percent distance of close from 200-day EMA."""
    ma = _ema(close, 200)
    return _safe_div(close - ma, ma)


# --- Group C (025-034): Depth below MA (negative only, clipped at 0) ---

def rst_025_depth_below_sma21(close: pd.Series) -> pd.Series:
    """How far below SMA21 close is (0 if above; negative value in pct terms)."""
    ma = _sma(close, _TD_MON)
    return (_safe_div(close - ma, ma)).clip(upper=0.0)


def rst_026_depth_below_sma50(close: pd.Series) -> pd.Series:
    """How far below SMA50 close is (0 if above)."""
    ma = _sma(close, 50)
    return (_safe_div(close - ma, ma)).clip(upper=0.0)


def rst_027_depth_below_sma100(close: pd.Series) -> pd.Series:
    """How far below SMA100 close is (0 if above)."""
    ma = _sma(close, 100)
    return (_safe_div(close - ma, ma)).clip(upper=0.0)


def rst_028_depth_below_sma200(close: pd.Series) -> pd.Series:
    """How far below SMA200 close is (0 if above); key capitulation measure."""
    ma = _sma(close, 200)
    return (_safe_div(close - ma, ma)).clip(upper=0.0)


def rst_029_depth_below_ema21(close: pd.Series) -> pd.Series:
    """How far below EMA21 close is (0 if above)."""
    ma = _ema(close, _TD_MON)
    return (_safe_div(close - ma, ma)).clip(upper=0.0)


def rst_030_depth_below_ema50(close: pd.Series) -> pd.Series:
    """How far below EMA50 close is (0 if above)."""
    ma = _ema(close, 50)
    return (_safe_div(close - ma, ma)).clip(upper=0.0)


def rst_031_depth_below_ema200(close: pd.Series) -> pd.Series:
    """How far below EMA200 close is (0 if above)."""
    ma = _ema(close, 200)
    return (_safe_div(close - ma, ma)).clip(upper=0.0)


# --- Group D (032-040): Count of MAs below price and stacking scores ---

def rst_032_count_smas_below_6(close: pd.Series) -> pd.Series:
    """Count of 6 SMAs (10,21,50,63,100,200) that close is below (0-6)."""
    return (
        (close < _sma(close, 10)).astype(float)
        + (close < _sma(close, _TD_MON)).astype(float)
        + (close < _sma(close, 50)).astype(float)
        + (close < _sma(close, _TD_QTR)).astype(float)
        + (close < _sma(close, 100)).astype(float)
        + (close < _sma(close, 200)).astype(float)
    )


def rst_033_count_emas_below_6(close: pd.Series) -> pd.Series:
    """Count of 6 EMAs (10,21,50,63,100,200) that close is below (0-6)."""
    return (
        (close < _ema(close, 10)).astype(float)
        + (close < _ema(close, _TD_MON)).astype(float)
        + (close < _ema(close, 50)).astype(float)
        + (close < _ema(close, _TD_QTR)).astype(float)
        + (close < _ema(close, 100)).astype(float)
        + (close < _ema(close, 200)).astype(float)
    )


def rst_034_below_all_6_smas_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is below ALL 6 SMAs (10,21,50,63,100,200)."""
    return (rst_032_count_smas_below_6(close) >= 6).astype(float)


def rst_035_below_all_6_emas_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is below ALL 6 EMAs (10,21,50,63,100,200)."""
    return (rst_033_count_emas_below_6(close) >= 6).astype(float)


def rst_036_count_mas_below_combined_12(close: pd.Series) -> pd.Series:
    """Count of all 12 MAs (6 SMA + 6 EMA) that close is below (0-12)."""
    return rst_032_count_smas_below_6(close) + rst_033_count_emas_below_6(close)


def rst_037_sma50_vs_sma200_ratio(close: pd.Series) -> pd.Series:
    """Ratio of SMA50 to SMA200 (death-cross distance metric)."""
    return _safe_div(_sma(close, 50), _sma(close, 200))


def rst_038_ma_stack_score_sma(close: pd.Series) -> pd.Series:
    """Bearish MA-stack score: count of SMA pairs where shorter < longer (0-3)."""
    s10  = _sma(close, 10)
    s21  = _sma(close, _TD_MON)
    s63  = _sma(close, _TD_QTR)
    s200 = _sma(close, 200)
    return (
        (s10 < s21).astype(float)
        + (s21 < s63).astype(float)
        + (s63 < s200).astype(float)
    )


def rst_039_ma_stack_score_ema(close: pd.Series) -> pd.Series:
    """Bearish MA-stack score: count of EMA pairs where shorter < longer (0-3)."""
    e10  = _ema(close, 10)
    e21  = _ema(close, _TD_MON)
    e63  = _ema(close, _TD_QTR)
    e200 = _ema(close, 200)
    return (
        (e10 < e21).astype(float)
        + (e21 < e63).astype(float)
        + (e63 < e200).astype(float)
    )


def rst_040_sum_depth_below_12_mas(close: pd.Series) -> pd.Series:
    """Sum of pct-depth below all 12 MAs (6 SMA + 6 EMA, clipped at 0)."""
    spans = [10, _TD_MON, 50, _TD_QTR, 100, 200]
    sma_d = [_safe_div(close - _sma(close, w), _sma(close, w)).clip(upper=0.0) for w in spans]
    ema_d = [_safe_div(close - _ema(close, w), _ema(close, w)).clip(upper=0.0) for w in spans]
    return sum(sma_d) + sum(ema_d)


# --- Group E (041-054): Mansfield-style Relative Strength (price vs own long MA) ---
# Mansfield RS = close/SMA_long - 1, then normalized over trailing window.
# Without a benchmark, this measures how extended/compressed price is
# relative to its own long-term trend, z-scored or range-positioned.

def rst_041_mansfield_raw_126d(close: pd.Series) -> pd.Series:
    """Mansfield-style raw RS: (close/SMA126) - 1 (half-year base)."""
    return _mansfield_raw(close, _TD_HALF)


def rst_042_mansfield_raw_252d(close: pd.Series) -> pd.Series:
    """Mansfield-style raw RS: (close/SMA252) - 1 (annual base)."""
    return _mansfield_raw(close, _TD_YEAR)


def rst_043_mansfield_zscore_126d_252w(close: pd.Series) -> pd.Series:
    """Mansfield RS (126d base) z-scored over trailing 252-day window."""
    raw = _mansfield_raw(close, _TD_HALF)
    m = _rolling_mean(raw, _TD_YEAR)
    s = _rolling_std(raw, _TD_YEAR)
    return _safe_div(raw - m, s)


def rst_044_mansfield_zscore_252d_252w(close: pd.Series) -> pd.Series:
    """Mansfield RS (252d base) z-scored over trailing 252-day window."""
    raw = _mansfield_raw(close, _TD_YEAR)
    m = _rolling_mean(raw, _TD_YEAR)
    s = _rolling_std(raw, _TD_YEAR)
    return _safe_div(raw - m, s)


def rst_045_mansfield_zscore_126d_504w(close: pd.Series) -> pd.Series:
    """Mansfield RS (126d base) z-scored over trailing 504-day window."""
    raw = _mansfield_raw(close, _TD_HALF)
    m = _rolling_mean(raw, 504)
    s = _rolling_std(raw, 504)
    return _safe_div(raw - m, s)


def rst_046_mansfield_zscore_252d_504w(close: pd.Series) -> pd.Series:
    """Mansfield RS (252d base) z-scored over trailing 504-day window."""
    raw = _mansfield_raw(close, _TD_YEAR)
    m = _rolling_mean(raw, 504)
    s = _rolling_std(raw, 504)
    return _safe_div(raw - m, s)


def rst_047_mansfield_range_pos_126d_252w(close: pd.Series) -> pd.Series:
    """Mansfield RS (126d base) range-positioned in 252-day window (0=min, 1=max)."""
    raw = _mansfield_raw(close, _TD_HALF)
    mx = _rolling_max(raw, _TD_YEAR)
    mn = _rolling_min(raw, _TD_YEAR)
    rng = (mx - mn).replace(0, np.nan)
    return _safe_div(raw - mn, rng)


def rst_048_mansfield_range_pos_252d_252w(close: pd.Series) -> pd.Series:
    """Mansfield RS (252d base) range-positioned in 252-day window."""
    raw = _mansfield_raw(close, _TD_YEAR)
    mx = _rolling_max(raw, _TD_YEAR)
    mn = _rolling_min(raw, _TD_YEAR)
    rng = (mx - mn).replace(0, np.nan)
    return _safe_div(raw - mn, rng)


def rst_049_mansfield_range_pos_126d_504w(close: pd.Series) -> pd.Series:
    """Mansfield RS (126d base) range-positioned in 504-day window."""
    raw = _mansfield_raw(close, _TD_HALF)
    mx = _rolling_max(raw, 504)
    mn = _rolling_min(raw, 504)
    rng = (mx - mn).replace(0, np.nan)
    return _safe_div(raw - mn, rng)


def rst_050_mansfield_pctrank_252d_252w(close: pd.Series) -> pd.Series:
    """Percentile rank of Mansfield RS (252d base) within trailing 252-day window."""
    raw = _mansfield_raw(close, _TD_YEAR)
    return raw.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rst_051_mansfield_pctrank_126d_504w(close: pd.Series) -> pd.Series:
    """Percentile rank of Mansfield RS (126d base) within trailing 504-day window."""
    raw = _mansfield_raw(close, _TD_HALF)
    return raw.rolling(504, min_periods=_TD_YEAR).rank(pct=True)


def rst_052_mansfield_expanding_zscore_252d(close: pd.Series) -> pd.Series:
    """Expanding all-history z-score of Mansfield RS (252d base)."""
    raw = _mansfield_raw(close, _TD_YEAR)
    m = raw.expanding(min_periods=5).mean()
    s = raw.expanding(min_periods=5).std()
    return _safe_div(raw - m, s)


def rst_053_mansfield_below_zero_flag_252d(close: pd.Series) -> pd.Series:
    """Flag: Mansfield RS (252d base) is negative (price below its annual SMA)."""
    return (_mansfield_raw(close, _TD_YEAR) < 0.0).astype(float)


def rst_054_mansfield_depth_below_zero_252d(close: pd.Series) -> pd.Series:
    """Depth of Mansfield RS (252d base) below zero (0 if positive)."""
    return _mansfield_raw(close, _TD_YEAR).clip(upper=0.0)


# --- Group F (055-075): DEMA and TEMA constructs ---

def rst_055_close_to_dema21_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to DEMA21 (Double EMA, 21-day)."""
    return _safe_div(close, _dema(close, _TD_MON))


def rst_056_close_to_dema50_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to DEMA50."""
    return _safe_div(close, _dema(close, 50))


def rst_057_close_to_dema200_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to DEMA200."""
    return _safe_div(close, _dema(close, 200))


def rst_058_pct_dist_dema21(close: pd.Series) -> pd.Series:
    """Percent distance of close from DEMA21 ((close - DEMA21) / DEMA21)."""
    d = _dema(close, _TD_MON)
    return _safe_div(close - d, d)


def rst_059_pct_dist_dema50(close: pd.Series) -> pd.Series:
    """Percent distance of close from DEMA50."""
    d = _dema(close, 50)
    return _safe_div(close - d, d)


def rst_060_pct_dist_dema200(close: pd.Series) -> pd.Series:
    """Percent distance of close from DEMA200."""
    d = _dema(close, 200)
    return _safe_div(close - d, d)


def rst_061_depth_below_dema200(close: pd.Series) -> pd.Series:
    """Depth below DEMA200 (0 if above; negative = distress)."""
    d = _dema(close, 200)
    return _safe_div(close - d, d).clip(upper=0.0)


def rst_062_close_to_tema21_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to TEMA21 (Triple EMA, 21-day)."""
    return _safe_div(close, _tema(close, _TD_MON))


def rst_063_close_to_tema50_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to TEMA50."""
    return _safe_div(close, _tema(close, 50))


def rst_064_close_to_tema200_ratio(close: pd.Series) -> pd.Series:
    """Ratio of close to TEMA200."""
    return _safe_div(close, _tema(close, 200))


def rst_065_pct_dist_tema21(close: pd.Series) -> pd.Series:
    """Percent distance of close from TEMA21."""
    t = _tema(close, _TD_MON)
    return _safe_div(close - t, t)


def rst_066_pct_dist_tema50(close: pd.Series) -> pd.Series:
    """Percent distance of close from TEMA50."""
    t = _tema(close, 50)
    return _safe_div(close - t, t)


def rst_067_pct_dist_tema200(close: pd.Series) -> pd.Series:
    """Percent distance of close from TEMA200."""
    t = _tema(close, 200)
    return _safe_div(close - t, t)


def rst_068_depth_below_tema200(close: pd.Series) -> pd.Series:
    """Depth below TEMA200 (0 if above; negative = distress)."""
    t = _tema(close, 200)
    return _safe_div(close - t, t).clip(upper=0.0)


def rst_069_dema_vs_ema_21_spread(close: pd.Series) -> pd.Series:
    """DEMA21 minus EMA21 as pct of close (lag-reduction proxy)."""
    return _safe_div(_dema(close, _TD_MON) - _ema(close, _TD_MON), close)


def rst_070_dema_vs_ema_200_spread(close: pd.Series) -> pd.Series:
    """DEMA200 minus EMA200 as pct of close."""
    return _safe_div(_dema(close, 200) - _ema(close, 200), close)


def rst_071_tema_vs_ema_21_spread(close: pd.Series) -> pd.Series:
    """TEMA21 minus EMA21 as pct of close."""
    return _safe_div(_tema(close, _TD_MON) - _ema(close, _TD_MON), close)


def rst_072_tema_vs_dema_50_spread(close: pd.Series) -> pd.Series:
    """TEMA50 minus DEMA50 as pct of close (curvature of 50d trend signal)."""
    return _safe_div(_tema(close, 50) - _dema(close, 50), close)


def rst_073_dema21_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of (close/DEMA21 - 1) pct-distance vs trailing 252 days."""
    raw = _safe_div(close - _dema(close, _TD_MON), _dema(close, _TD_MON))
    m = _rolling_mean(raw, _TD_YEAR)
    s = _rolling_std(raw, _TD_YEAR)
    return _safe_div(raw - m, s)


def rst_074_dema200_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of (close/DEMA200 - 1) pct-distance vs trailing 252 days."""
    raw = _safe_div(close - _dema(close, 200), _dema(close, 200))
    m = _rolling_mean(raw, _TD_YEAR)
    s = _rolling_std(raw, _TD_YEAR)
    return _safe_div(raw - m, s)


def rst_075_tema200_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of (close/TEMA200 - 1) pct-distance vs trailing 252 days."""
    raw = _safe_div(close - _tema(close, 200), _tema(close, 200))
    m = _rolling_mean(raw, _TD_YEAR)
    s = _rolling_std(raw, _TD_YEAR)
    return _safe_div(raw - m, s)


# ── Registry ──────────────────────────────────────────────────────────────────

RELATIVE_STRENGTH_REGISTRY_001_075 = {
    "rst_001_close_to_sma10_ratio": {"inputs": ["close"], "func": rst_001_close_to_sma10_ratio},
    "rst_002_close_to_sma21_ratio": {"inputs": ["close"], "func": rst_002_close_to_sma21_ratio},
    "rst_003_close_to_sma50_ratio": {"inputs": ["close"], "func": rst_003_close_to_sma50_ratio},
    "rst_004_close_to_sma63_ratio": {"inputs": ["close"], "func": rst_004_close_to_sma63_ratio},
    "rst_005_close_to_sma100_ratio": {"inputs": ["close"], "func": rst_005_close_to_sma100_ratio},
    "rst_006_close_to_sma200_ratio": {"inputs": ["close"], "func": rst_006_close_to_sma200_ratio},
    "rst_007_close_to_ema10_ratio": {"inputs": ["close"], "func": rst_007_close_to_ema10_ratio},
    "rst_008_close_to_ema21_ratio": {"inputs": ["close"], "func": rst_008_close_to_ema21_ratio},
    "rst_009_close_to_ema50_ratio": {"inputs": ["close"], "func": rst_009_close_to_ema50_ratio},
    "rst_010_close_to_ema63_ratio": {"inputs": ["close"], "func": rst_010_close_to_ema63_ratio},
    "rst_011_close_to_ema100_ratio": {"inputs": ["close"], "func": rst_011_close_to_ema100_ratio},
    "rst_012_close_to_ema200_ratio": {"inputs": ["close"], "func": rst_012_close_to_ema200_ratio},
    "rst_013_pct_dist_sma10": {"inputs": ["close"], "func": rst_013_pct_dist_sma10},
    "rst_014_pct_dist_sma21": {"inputs": ["close"], "func": rst_014_pct_dist_sma21},
    "rst_015_pct_dist_sma50": {"inputs": ["close"], "func": rst_015_pct_dist_sma50},
    "rst_016_pct_dist_sma63": {"inputs": ["close"], "func": rst_016_pct_dist_sma63},
    "rst_017_pct_dist_sma100": {"inputs": ["close"], "func": rst_017_pct_dist_sma100},
    "rst_018_pct_dist_sma200": {"inputs": ["close"], "func": rst_018_pct_dist_sma200},
    "rst_019_pct_dist_ema10": {"inputs": ["close"], "func": rst_019_pct_dist_ema10},
    "rst_020_pct_dist_ema21": {"inputs": ["close"], "func": rst_020_pct_dist_ema21},
    "rst_021_pct_dist_ema50": {"inputs": ["close"], "func": rst_021_pct_dist_ema50},
    "rst_022_pct_dist_ema63": {"inputs": ["close"], "func": rst_022_pct_dist_ema63},
    "rst_023_pct_dist_ema100": {"inputs": ["close"], "func": rst_023_pct_dist_ema100},
    "rst_024_pct_dist_ema200": {"inputs": ["close"], "func": rst_024_pct_dist_ema200},
    "rst_025_depth_below_sma21": {"inputs": ["close"], "func": rst_025_depth_below_sma21},
    "rst_026_depth_below_sma50": {"inputs": ["close"], "func": rst_026_depth_below_sma50},
    "rst_027_depth_below_sma100": {"inputs": ["close"], "func": rst_027_depth_below_sma100},
    "rst_028_depth_below_sma200": {"inputs": ["close"], "func": rst_028_depth_below_sma200},
    "rst_029_depth_below_ema21": {"inputs": ["close"], "func": rst_029_depth_below_ema21},
    "rst_030_depth_below_ema50": {"inputs": ["close"], "func": rst_030_depth_below_ema50},
    "rst_031_depth_below_ema200": {"inputs": ["close"], "func": rst_031_depth_below_ema200},
    "rst_032_count_smas_below_6": {"inputs": ["close"], "func": rst_032_count_smas_below_6},
    "rst_033_count_emas_below_6": {"inputs": ["close"], "func": rst_033_count_emas_below_6},
    "rst_034_below_all_6_smas_flag": {"inputs": ["close"], "func": rst_034_below_all_6_smas_flag},
    "rst_035_below_all_6_emas_flag": {"inputs": ["close"], "func": rst_035_below_all_6_emas_flag},
    "rst_036_count_mas_below_combined_12": {"inputs": ["close"], "func": rst_036_count_mas_below_combined_12},
    "rst_037_sma50_vs_sma200_ratio": {"inputs": ["close"], "func": rst_037_sma50_vs_sma200_ratio},
    "rst_038_ma_stack_score_sma": {"inputs": ["close"], "func": rst_038_ma_stack_score_sma},
    "rst_039_ma_stack_score_ema": {"inputs": ["close"], "func": rst_039_ma_stack_score_ema},
    "rst_040_sum_depth_below_12_mas": {"inputs": ["close"], "func": rst_040_sum_depth_below_12_mas},
    "rst_041_mansfield_raw_126d": {"inputs": ["close"], "func": rst_041_mansfield_raw_126d},
    "rst_042_mansfield_raw_252d": {"inputs": ["close"], "func": rst_042_mansfield_raw_252d},
    "rst_043_mansfield_zscore_126d_252w": {"inputs": ["close"], "func": rst_043_mansfield_zscore_126d_252w},
    "rst_044_mansfield_zscore_252d_252w": {"inputs": ["close"], "func": rst_044_mansfield_zscore_252d_252w},
    "rst_045_mansfield_zscore_126d_504w": {"inputs": ["close"], "func": rst_045_mansfield_zscore_126d_504w},
    "rst_046_mansfield_zscore_252d_504w": {"inputs": ["close"], "func": rst_046_mansfield_zscore_252d_504w},
    "rst_047_mansfield_range_pos_126d_252w": {"inputs": ["close"], "func": rst_047_mansfield_range_pos_126d_252w},
    "rst_048_mansfield_range_pos_252d_252w": {"inputs": ["close"], "func": rst_048_mansfield_range_pos_252d_252w},
    "rst_049_mansfield_range_pos_126d_504w": {"inputs": ["close"], "func": rst_049_mansfield_range_pos_126d_504w},
    "rst_050_mansfield_pctrank_252d_252w": {"inputs": ["close"], "func": rst_050_mansfield_pctrank_252d_252w},
    "rst_051_mansfield_pctrank_126d_504w": {"inputs": ["close"], "func": rst_051_mansfield_pctrank_126d_504w},
    "rst_052_mansfield_expanding_zscore_252d": {"inputs": ["close"], "func": rst_052_mansfield_expanding_zscore_252d},
    "rst_053_mansfield_below_zero_flag_252d": {"inputs": ["close"], "func": rst_053_mansfield_below_zero_flag_252d},
    "rst_054_mansfield_depth_below_zero_252d": {"inputs": ["close"], "func": rst_054_mansfield_depth_below_zero_252d},
    "rst_055_close_to_dema21_ratio": {"inputs": ["close"], "func": rst_055_close_to_dema21_ratio},
    "rst_056_close_to_dema50_ratio": {"inputs": ["close"], "func": rst_056_close_to_dema50_ratio},
    "rst_057_close_to_dema200_ratio": {"inputs": ["close"], "func": rst_057_close_to_dema200_ratio},
    "rst_058_pct_dist_dema21": {"inputs": ["close"], "func": rst_058_pct_dist_dema21},
    "rst_059_pct_dist_dema50": {"inputs": ["close"], "func": rst_059_pct_dist_dema50},
    "rst_060_pct_dist_dema200": {"inputs": ["close"], "func": rst_060_pct_dist_dema200},
    "rst_061_depth_below_dema200": {"inputs": ["close"], "func": rst_061_depth_below_dema200},
    "rst_062_close_to_tema21_ratio": {"inputs": ["close"], "func": rst_062_close_to_tema21_ratio},
    "rst_063_close_to_tema50_ratio": {"inputs": ["close"], "func": rst_063_close_to_tema50_ratio},
    "rst_064_close_to_tema200_ratio": {"inputs": ["close"], "func": rst_064_close_to_tema200_ratio},
    "rst_065_pct_dist_tema21": {"inputs": ["close"], "func": rst_065_pct_dist_tema21},
    "rst_066_pct_dist_tema50": {"inputs": ["close"], "func": rst_066_pct_dist_tema50},
    "rst_067_pct_dist_tema200": {"inputs": ["close"], "func": rst_067_pct_dist_tema200},
    "rst_068_depth_below_tema200": {"inputs": ["close"], "func": rst_068_depth_below_tema200},
    "rst_069_dema_vs_ema_21_spread": {"inputs": ["close"], "func": rst_069_dema_vs_ema_21_spread},
    "rst_070_dema_vs_ema_200_spread": {"inputs": ["close"], "func": rst_070_dema_vs_ema_200_spread},
    "rst_071_tema_vs_ema_21_spread": {"inputs": ["close"], "func": rst_071_tema_vs_ema_21_spread},
    "rst_072_tema_vs_dema_50_spread": {"inputs": ["close"], "func": rst_072_tema_vs_dema_50_spread},
    "rst_073_dema21_zscore_252d": {"inputs": ["close"], "func": rst_073_dema21_zscore_252d},
    "rst_074_dema200_zscore_252d": {"inputs": ["close"], "func": rst_074_dema200_zscore_252d},
    "rst_075_tema200_zscore_252d": {"inputs": ["close"], "func": rst_075_tema200_zscore_252d},
}
