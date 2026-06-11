"""
09_price_compression — Base Features 076-150
Domain: price range narrowing / contraction near the absolute low
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


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).std()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _true_range(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    prev_c = close.shift(1)
    return pd.concat([
        high - low,
        (high - prev_c).abs(),
        (low  - prev_c).abs(),
    ], axis=1).max(axis=1)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group I (076-085): Volatility squeeze / Keltner-vs-BB overlap ---

def pcmp_076_bb_keltner_squeeze_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bollinger Band width minus Keltner Channel width (21d) — squeeze when negative."""
    bb_ma  = _rolling_mean(close, _TD_MON)
    bb_sd  = _rolling_std(close, _TD_MON)
    bb_w   = 4.0 * bb_sd
    tr     = _true_range(close, high, low)
    kc_w   = 4.0 * _rolling_mean(tr, _TD_MON)
    return _safe_div(bb_w - kc_w, bb_ma)


def pcmp_077_bb_keltner_squeeze_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bollinger Band width minus Keltner Channel width (63d) — normalized by MA."""
    bb_ma  = _rolling_mean(close, _TD_QTR)
    bb_sd  = _rolling_std(close, _TD_QTR)
    bb_w   = 4.0 * bb_sd
    tr     = _true_range(close, high, low)
    kc_w   = 4.0 * _rolling_mean(tr, _TD_QTR)
    return _safe_div(bb_w - kc_w, bb_ma)


def pcmp_078_squeeze_duration_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 21 days where BB-width < Keltner-width (squeeze active)."""
    bb_sd = _rolling_std(close, _TD_MON)
    bb_w  = 4.0 * bb_sd
    tr    = _true_range(close, high, low)
    kc_w  = 4.0 * _rolling_mean(tr, _TD_MON)
    in_sq = (bb_w < kc_w).astype(float)
    return _rolling_mean(in_sq, _TD_MON)


def pcmp_079_squeeze_duration_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 63 days with BB-width < Keltner-width."""
    bb_sd = _rolling_std(close, _TD_QTR)
    bb_w  = 4.0 * bb_sd
    tr    = _true_range(close, high, low)
    kc_w  = 4.0 * _rolling_mean(tr, _TD_QTR)
    in_sq = (bb_w < kc_w).astype(float)
    return _rolling_mean(in_sq, _TD_QTR)


def pcmp_080_bb_upper_lower_ratio_21d(close: pd.Series) -> pd.Series:
    """(upper BB - lower BB) / close — relative band width, 21d."""
    ma  = _rolling_mean(close, _TD_MON)
    sd  = _rolling_std(close, _TD_MON)
    return _safe_div(4.0 * sd, close)


def pcmp_081_bb_upper_lower_ratio_63d(close: pd.Series) -> pd.Series:
    """(upper BB - lower BB) / close — relative band width, 63d."""
    sd  = _rolling_std(close, _TD_QTR)
    return _safe_div(4.0 * sd, close)


def pcmp_082_bb_pct_b_21d(close: pd.Series) -> pd.Series:
    """Bollinger %B: position of close within 21-day BB (0=lower band, 1=upper)."""
    ma    = _rolling_mean(close, _TD_MON)
    sd    = _rolling_std(close, _TD_MON)
    upper = ma + 2.0 * sd
    lower = ma - 2.0 * sd
    return _safe_div(close - lower, upper - lower)


def pcmp_083_bb_pct_b_63d(close: pd.Series) -> pd.Series:
    """Bollinger %B within 63-day BB."""
    ma    = _rolling_mean(close, _TD_QTR)
    sd    = _rolling_std(close, _TD_QTR)
    upper = ma + 2.0 * sd
    lower = ma - 2.0 * sd
    return _safe_div(close - lower, upper - lower)


def pcmp_084_bb_width_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 21-day BB width (all-history squeeze rank)."""
    bbw = _safe_div(4.0 * _rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))
    return bbw.expanding(min_periods=5).rank(pct=True)


def pcmp_085_ewm_bb_width_ratio(close: pd.Series) -> pd.Series:
    """Ratio of EWM-std (span=21) to EWM-std (span=252) — EWM squeeze."""
    return _safe_div(_ewm_std(close, _TD_MON), _ewm_std(close, _TD_YEAR))


# --- Group J (086-095): Log-price dispersion and variance compression ---

def pcmp_086_log_range_21d(close: pd.Series) -> pd.Series:
    """log(rolling_max/rolling_min) of close over 21 days — log channel width."""
    return _log_safe(_rolling_max(close, _TD_MON)) - _log_safe(_rolling_min(close, _TD_MON))


def pcmp_087_log_range_63d(close: pd.Series) -> pd.Series:
    """log(rolling_max/rolling_min) of close over 63 days."""
    return _log_safe(_rolling_max(close, _TD_QTR)) - _log_safe(_rolling_min(close, _TD_QTR))


def pcmp_088_log_range_252d(close: pd.Series) -> pd.Series:
    """log(rolling_max/rolling_min) of close over 252 days."""
    return _log_safe(_rolling_max(close, _TD_YEAR)) - _log_safe(_rolling_min(close, _TD_YEAR))


def pcmp_089_log_range_ratio_21d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day log-range to 252-day log-range — compression ratio."""
    lr21  = _log_safe(_rolling_max(close, _TD_MON))  - _log_safe(_rolling_min(close, _TD_MON))
    lr252 = _log_safe(_rolling_max(close, _TD_YEAR)) - _log_safe(_rolling_min(close, _TD_YEAR))
    return _safe_div(lr21, lr252)


def pcmp_090_log_range_ratio_63d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63-day log-range to 252-day log-range."""
    lr63  = _log_safe(_rolling_max(close, _TD_QTR))  - _log_safe(_rolling_min(close, _TD_QTR))
    lr252 = _log_safe(_rolling_max(close, _TD_YEAR)) - _log_safe(_rolling_min(close, _TD_YEAR))
    return _safe_div(lr63, lr252)


def pcmp_091_log_return_std_ratio_5d_vs_63d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day log-return std to 63-day log-return std."""
    lr  = _log_safe(close).diff(1)
    s5  = lr.rolling(_TD_WEEK, min_periods=2).std()
    s63 = lr.rolling(_TD_QTR,  min_periods=max(2, _TD_QTR // 2)).std()
    return _safe_div(s5, s63)


def pcmp_092_variance_ratio_21d_vs_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day return variance to 63-day return variance."""
    lr  = _log_safe(close).diff(1)
    v21 = lr.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).var()
    v63 = lr.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).var()
    return _safe_div(v21, v63)


def pcmp_093_variance_ratio_21d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day return variance to 252-day return variance."""
    lr   = _log_safe(close).diff(1)
    v21  = lr.rolling(_TD_MON,  min_periods=max(2, _TD_MON // 2)).var()
    v252 = lr.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).var()
    return _safe_div(v21, v252)


def pcmp_094_log_range_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day log-range within 252-day history."""
    lr21 = _log_safe(_rolling_max(close, _TD_MON)) - _log_safe(_rolling_min(close, _TD_MON))
    return _rolling_rank_pct(lr21, _TD_YEAR)


def pcmp_095_log_range_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day log-range over trailing 252 days."""
    lr21 = _log_safe(_rolling_max(close, _TD_MON)) - _log_safe(_rolling_min(close, _TD_MON))
    return _zscore_rolling(lr21, _TD_YEAR)


# --- Group K (096-105): Absolute and relative HL channel compression ---

def pcmp_096_hl_channel_compression_5d_vs_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day (max-H minus min-L) vs 252-day (max-H minus min-L), ratio."""
    band5   = _rolling_max(high, _TD_WEEK) - _rolling_min(low, _TD_WEEK)
    band252 = _rolling_max(high, _TD_YEAR) - _rolling_min(low, _TD_YEAR)
    return _safe_div(band5, band252)


def pcmp_097_hl_channel_compression_21d_vs_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day HL band vs 252-day HL band, ratio."""
    band21  = _rolling_max(high, _TD_MON)  - _rolling_min(low, _TD_MON)
    band252 = _rolling_max(high, _TD_YEAR) - _rolling_min(low, _TD_YEAR)
    return _safe_div(band21, band252)


def pcmp_098_hl_channel_compression_63d_vs_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day HL band vs 252-day HL band, ratio."""
    band63  = _rolling_max(high, _TD_QTR)  - _rolling_min(low, _TD_QTR)
    band252 = _rolling_max(high, _TD_YEAR) - _rolling_min(low, _TD_YEAR)
    return _safe_div(band63, band252)


def pcmp_099_hl_channel_compression_5d_vs_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day HL band vs 63-day HL band, ratio."""
    band5  = _rolling_max(high, _TD_WEEK) - _rolling_min(low, _TD_WEEK)
    band63 = _rolling_max(high, _TD_QTR)  - _rolling_min(low, _TD_QTR)
    return _safe_div(band5, band63)


def pcmp_100_hl_band_pct_rank_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21-day HL band within 252-day history."""
    band = _rolling_max(high, _TD_MON) - _rolling_min(low, _TD_MON)
    return _rolling_rank_pct(band, _TD_YEAR)


def pcmp_101_hl_band_zscore_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 21-day HL band within 252-day history."""
    band = _rolling_max(high, _TD_MON) - _rolling_min(low, _TD_MON)
    return _zscore_rolling(band, _TD_YEAR)


def pcmp_102_hl_band_pct_rank_504d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21-day HL band within 504-day history."""
    band = _rolling_max(high, _TD_MON) - _rolling_min(low, _TD_MON)
    return band.rolling(504, min_periods=_TD_QTR).rank(pct=True)


def pcmp_103_high_rolling_std_21d(high: pd.Series) -> pd.Series:
    """21-day rolling std of high prices (dispersion of highs narrowing)."""
    return _rolling_std(high, _TD_MON)


def pcmp_104_low_rolling_std_21d(low: pd.Series) -> pd.Series:
    """21-day rolling std of low prices (dispersion of lows narrowing)."""
    return _rolling_std(low, _TD_MON)


def pcmp_105_hl_std_sum_ratio_21d_vs_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """(std_high_21d + std_low_21d) / (std_high_252d + std_low_252d)."""
    num = _rolling_std(high, _TD_MON)  + _rolling_std(low, _TD_MON)
    den = _rolling_std(high, _TD_YEAR) + _rolling_std(low, _TD_YEAR)
    return _safe_div(num, den)


# --- Group L (106-115): Close-to-close range as fraction of trend ---

def pcmp_106_close_range_frac_sma21(close: pd.Series) -> pd.Series:
    """21-day channel-width of close divided by 21-day SMA — range relative to trend."""
    ch = _rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON)
    ma = _rolling_mean(close, _TD_MON)
    return _safe_div(ch, ma)


def pcmp_107_close_range_frac_sma63(close: pd.Series) -> pd.Series:
    """63-day channel-width of close divided by 63-day SMA."""
    ch = _rolling_max(close, _TD_QTR) - _rolling_min(close, _TD_QTR)
    ma = _rolling_mean(close, _TD_QTR)
    return _safe_div(ch, ma)


def pcmp_108_close_range_frac_sma252(close: pd.Series) -> pd.Series:
    """252-day channel-width of close divided by 252-day SMA."""
    ch = _rolling_max(close, _TD_YEAR) - _rolling_min(close, _TD_YEAR)
    ma = _rolling_mean(close, _TD_YEAR)
    return _safe_div(ch, ma)


def pcmp_109_hl_range_frac_ema21(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-day mean HL range normalized by 21-day EMA of close."""
    hl   = _rolling_mean(high - low, _TD_MON)
    ema  = _ewm_mean(close, _TD_MON)
    return _safe_div(hl, ema)


def pcmp_110_hl_range_frac_ema63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day mean HL range normalized by 63-day EMA of close."""
    hl   = _rolling_mean(high - low, _TD_QTR)
    ema  = _ewm_mean(close, _TD_QTR)
    return _safe_div(hl, ema)


def pcmp_111_tr_std_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day rolling std of true range — TR variability (compression = low variability)."""
    tr = _true_range(close, high, low)
    return _rolling_std(tr, _TD_MON)


def pcmp_112_tr_std_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day rolling std of true range."""
    tr = _true_range(close, high, low)
    return _rolling_std(tr, _TD_QTR)


def pcmp_113_tr_cv_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Coefficient of variation of TR over 21 days (std/mean)."""
    tr = _true_range(close, high, low)
    return _safe_div(_rolling_std(tr, _TD_MON), _rolling_mean(tr, _TD_MON))


def pcmp_114_tr_cv_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Coefficient of variation of TR over 63 days."""
    tr = _true_range(close, high, low)
    return _safe_div(_rolling_std(tr, _TD_QTR), _rolling_mean(tr, _TD_QTR))


def pcmp_115_tr_iqr_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day IQR of TR (Q75-Q25) — robust range dispersion."""
    tr = _true_range(close, high, low)
    q75 = tr.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.75)
    q25 = tr.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).quantile(0.25)
    return q75 - q25


# --- Group M (116-125): Open-gap contraction and overnight range ---

def pcmp_116_overnight_gap_frac_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """21-day mean of |open - prev_close| / prev_close — overnight gap compression."""
    gap = (open - close.shift(1)).abs() / close.shift(1).replace(0, np.nan)
    return _rolling_mean(gap, _TD_MON)


def pcmp_117_overnight_gap_frac_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """63-day mean of |open - prev_close| / prev_close."""
    gap = (open - close.shift(1)).abs() / close.shift(1).replace(0, np.nan)
    return _rolling_mean(gap, _TD_QTR)


def pcmp_118_overnight_gap_std_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """21-day std of overnight gaps / prev_close — variability of gaps."""
    gap = (open - close.shift(1)) / close.shift(1).replace(0, np.nan)
    return _rolling_std(gap, _TD_MON)


def pcmp_119_intraday_range_frac_oc_21d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day avg of (HL range) / max(|open|,|close|,eps) — ratio of swing to body."""
    hl   = (high - low).clip(lower=0.0)
    body = pd.concat([open.abs(), close.abs()], axis=1).max(axis=1).replace(0, np.nan)
    return _rolling_mean(hl / body, _TD_MON)


def pcmp_120_intraday_range_frac_oc_63d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day avg of HL range / reference price."""
    hl   = (high - low).clip(lower=0.0)
    body = pd.concat([open.abs(), close.abs()], axis=1).max(axis=1).replace(0, np.nan)
    return _rolling_mean(hl / body, _TD_QTR)


def pcmp_121_close_open_body_pct_rank_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of |close-open|/close in trailing 252 days."""
    body = (close - open).abs() / close.replace(0, np.nan)
    return _rolling_rank_pct(body, _TD_YEAR)


def pcmp_122_upper_shadow_frac_21d(open: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """21-day mean upper shadow / close: (high - max(open,close)) / close."""
    body_top = pd.concat([open, close], axis=1).max(axis=1)
    upper    = (high - body_top).clip(lower=0.0) / close.replace(0, np.nan)
    return _rolling_mean(upper, _TD_MON)


def pcmp_123_lower_shadow_frac_21d(open: pd.Series, close: pd.Series, low: pd.Series) -> pd.Series:
    """21-day mean lower shadow / close: (min(open,close) - low) / close."""
    body_bot = pd.concat([open, close], axis=1).min(axis=1)
    lower    = (body_bot - low).clip(lower=0.0) / close.replace(0, np.nan)
    return _rolling_mean(lower, _TD_MON)


def pcmp_124_shadow_to_body_ratio_21d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day avg of (upper+lower shadow) / |close-open| — candle structure compression."""
    body_top = pd.concat([open, close], axis=1).max(axis=1)
    body_bot = pd.concat([open, close], axis=1).min(axis=1)
    shadow   = (high - body_top) + (body_bot - low)
    body     = (close - open).abs().replace(0, np.nan)
    return _rolling_mean(shadow / body, _TD_MON)


def pcmp_125_narrow_body_frac_21d(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of bars where body < 25% of HL range over 21 days (doji-like compression)."""
    body = (close - open).abs()
    hl   = (high - low).replace(0, np.nan)
    ratio = body / hl
    narrow = (ratio < 0.25).astype(float)
    return _rolling_mean(narrow, _TD_MON)


# --- Group N (126-135): Volume-normalized range (range per unit of volume) ---

def pcmp_126_range_per_volume_5d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day avg of (high-low) / volume — range generated per share traded."""
    rv = _safe_div(high - low, volume)
    return _rolling_mean(rv, _TD_WEEK)


def pcmp_127_range_per_volume_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day avg of (high-low) / volume."""
    rv = _safe_div(high - low, volume)
    return _rolling_mean(rv, _TD_MON)


def pcmp_128_range_per_volume_63d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day avg of (high-low) / volume."""
    rv = _safe_div(high - low, volume)
    return _rolling_mean(rv, _TD_QTR)


def pcmp_129_tr_per_volume_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day avg of TR / volume — TR efficiency."""
    rv = _safe_div(_true_range(close, high, low), volume)
    return _rolling_mean(rv, _TD_MON)


def pcmp_130_range_volume_ratio_5d_vs_252d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 5-day avg range/vol to 252-day avg range/vol."""
    rv = _safe_div(high - low, volume)
    return _safe_div(_rolling_mean(rv, _TD_WEEK), _rolling_mean(rv, _TD_YEAR))


def pcmp_131_hl_range_zscore_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of daily HL range vs trailing 252-day distribution."""
    hl = high - low
    return _zscore_rolling(hl, _TD_YEAR)


def pcmp_132_hl_range_zscore_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of daily HL range vs trailing 63-day distribution."""
    hl = high - low
    return _zscore_rolling(hl, _TD_QTR)


def pcmp_133_tr_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of today's TR vs trailing 252-day TR distribution."""
    tr = _true_range(close, high, low)
    return _zscore_rolling(tr, _TD_YEAR)


def pcmp_134_tr_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of today's TR vs trailing 63-day TR distribution."""
    tr = _true_range(close, high, low)
    return _zscore_rolling(tr, _TD_QTR)


def pcmp_135_volume_weighted_tr_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean TR over 21 days (how much range high-volume bars make)."""
    tr     = _true_range(close, high, low)
    v_norm = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    return _rolling_mean(tr * v_norm, _TD_MON)


# --- Group O (136-145): Multi-scale compression scores ---

def pcmp_136_compression_score_21d_vs_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Composite 21d-vs-252d compression: avg of TR-ratio, BB-width-ratio, log-range-ratio."""
    tr        = _true_range(close, high, low)
    tr_ratio  = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_YEAR))
    bbw21     = _safe_div(4.0 * _rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))
    bbw252    = _safe_div(4.0 * _rolling_std(close, _TD_YEAR), _rolling_mean(close, _TD_YEAR))
    bbw_ratio = _safe_div(bbw21, bbw252)
    lr21      = _log_safe(_rolling_max(close, _TD_MON))  - _log_safe(_rolling_min(close, _TD_MON))
    lr252     = _log_safe(_rolling_max(close, _TD_YEAR)) - _log_safe(_rolling_min(close, _TD_YEAR))
    lr_ratio  = _safe_div(lr21, lr252)
    return (tr_ratio + bbw_ratio + lr_ratio) / 3.0


def pcmp_137_compression_score_63d_vs_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Composite 63d-vs-252d compression: TR-ratio + BB-width-ratio + log-range-ratio."""
    tr        = _true_range(close, high, low)
    tr_ratio  = _safe_div(_rolling_mean(tr, _TD_QTR), _rolling_mean(tr, _TD_YEAR))
    bbw63     = _safe_div(4.0 * _rolling_std(close, _TD_QTR), _rolling_mean(close, _TD_QTR))
    bbw252    = _safe_div(4.0 * _rolling_std(close, _TD_YEAR), _rolling_mean(close, _TD_YEAR))
    bbw_ratio = _safe_div(bbw63, bbw252)
    lr63      = _log_safe(_rolling_max(close, _TD_QTR))  - _log_safe(_rolling_min(close, _TD_QTR))
    lr252     = _log_safe(_rolling_max(close, _TD_YEAR)) - _log_safe(_rolling_min(close, _TD_YEAR))
    lr_ratio  = _safe_div(lr63, lr252)
    return (tr_ratio + bbw_ratio + lr_ratio) / 3.0


def pcmp_138_range_contraction_streak_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Number of the last 21 days with HL range below its 63-day median."""
    hl     = high - low
    med63  = _rolling_median(hl, _TD_QTR)
    below  = (hl < med63).astype(float)
    return _rolling_sum(below, _TD_MON)


def pcmp_139_range_contraction_streak_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of last 63 days with HL range below its 252-day median."""
    hl     = high - low
    med252 = _rolling_median(hl, _TD_YEAR)
    below  = (hl < med252).astype(float)
    return _rolling_sum(below, _TD_QTR)


def pcmp_140_tr_below_21d_mean_frac_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 63 days where TR is below its own 21-day average."""
    tr      = _true_range(close, high, low)
    avg21   = _rolling_mean(tr, _TD_MON)
    below   = (tr < avg21).astype(float)
    return _rolling_mean(below, _TD_QTR)


def pcmp_141_range_percentile_q10_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """10th percentile of daily HL range over trailing 252 days."""
    hl = high - low
    return hl.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.10)


def pcmp_142_range_percentile_q25_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """25th percentile of daily HL range over trailing 252 days."""
    hl = high - low
    return hl.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)


def pcmp_143_tr_percentile_q10_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """10th percentile of daily TR over trailing 252 days."""
    tr = _true_range(close, high, low)
    return tr.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.10)


def pcmp_144_close_std_ratio_21d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day price std to 252-day price std (price level dispersion)."""
    return _safe_div(_rolling_std(close, _TD_MON), _rolling_std(close, _TD_YEAR))


def pcmp_145_close_std_ratio_63d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63-day price std to 252-day price std."""
    return _safe_div(_rolling_std(close, _TD_QTR), _rolling_std(close, _TD_YEAR))


# --- Group P (146-150): EWM-ATR compression and final composite ---

def pcmp_146_ewm_atr_ratio_21_vs_252(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of EWM-ATR (span=21) to EWM-ATR (span=252) — fast vs slow ATR compression."""
    tr = _true_range(close, high, low)
    return _safe_div(_ewm_mean(tr, _TD_MON), _ewm_mean(tr, _TD_YEAR))


def pcmp_147_ewm_atr_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of EWM-ATR (span=21) within trailing 252-day window."""
    tr     = _true_range(close, high, low)
    ewmatr = _ewm_mean(tr, _TD_MON)
    return _rolling_rank_pct(ewmatr, _TD_YEAR)


def pcmp_148_range_momentum_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day slope of HL range (negative = contracting range over the period)."""
    hl  = high - low
    idx = pd.Series(np.arange(len(hl), dtype=float), index=hl.index)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom < _EPS:
            return np.nan
        return float(((x - xm) * (arr - ym)).sum() / denom)
    return hl.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).apply(_slope, raw=True)


def pcmp_149_tr_momentum_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day slope of TR (negative = TR contracting over the period)."""
    tr = _true_range(close, high, low)
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x = np.arange(n, dtype=float)
        xm = x.mean()
        ym = arr.mean()
        denom = ((x - xm) ** 2).sum()
        if denom < _EPS:
            return np.nan
        return float(((x - xm) * (arr - ym)).sum() / denom)
    return tr.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).apply(_slope, raw=True)


def pcmp_150_grand_compression_composite(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Grand composite: equal-weight avg of BB-width rank, TR rank, log-range rank,
    and channel-width rank — all 252-day percentile ranks."""
    bbw21   = _safe_div(4.0 * _rolling_std(close, _TD_MON), _rolling_mean(close, _TD_MON))
    bbw_r   = _rolling_rank_pct(bbw21, _TD_YEAR)
    tr      = _true_range(close, high, low)
    tr_r    = _rolling_rank_pct(tr, _TD_YEAR)
    lr21    = _log_safe(_rolling_max(close, _TD_MON)) - _log_safe(_rolling_min(close, _TD_MON))
    lr_r    = _rolling_rank_pct(lr21, _TD_YEAR)
    cw21    = _safe_div(_rolling_max(close, _TD_MON) - _rolling_min(close, _TD_MON),
                        _rolling_min(close, _TD_MON))
    cw_r    = _rolling_rank_pct(cw21, _TD_YEAR)
    return (bbw_r + tr_r + lr_r + cw_r) / 4.0


# ── Registry ──────────────────────────────────────────────────────────────────

PRICE_COMPRESSION_REGISTRY_076_150 = {
    "pcmp_076_bb_keltner_squeeze_21d":            {"inputs": ["close", "high", "low"], "func": pcmp_076_bb_keltner_squeeze_21d},
    "pcmp_077_bb_keltner_squeeze_63d":            {"inputs": ["close", "high", "low"], "func": pcmp_077_bb_keltner_squeeze_63d},
    "pcmp_078_squeeze_duration_21d":              {"inputs": ["close", "high", "low"], "func": pcmp_078_squeeze_duration_21d},
    "pcmp_079_squeeze_duration_63d":              {"inputs": ["close", "high", "low"], "func": pcmp_079_squeeze_duration_63d},
    "pcmp_080_bb_upper_lower_ratio_21d":          {"inputs": ["close"], "func": pcmp_080_bb_upper_lower_ratio_21d},
    "pcmp_081_bb_upper_lower_ratio_63d":          {"inputs": ["close"], "func": pcmp_081_bb_upper_lower_ratio_63d},
    "pcmp_082_bb_pct_b_21d":                      {"inputs": ["close"], "func": pcmp_082_bb_pct_b_21d},
    "pcmp_083_bb_pct_b_63d":                      {"inputs": ["close"], "func": pcmp_083_bb_pct_b_63d},
    "pcmp_084_bb_width_expanding_pct_rank":       {"inputs": ["close"], "func": pcmp_084_bb_width_expanding_pct_rank},
    "pcmp_085_ewm_bb_width_ratio":                {"inputs": ["close"], "func": pcmp_085_ewm_bb_width_ratio},
    "pcmp_086_log_range_21d":                     {"inputs": ["close"], "func": pcmp_086_log_range_21d},
    "pcmp_087_log_range_63d":                     {"inputs": ["close"], "func": pcmp_087_log_range_63d},
    "pcmp_088_log_range_252d":                    {"inputs": ["close"], "func": pcmp_088_log_range_252d},
    "pcmp_089_log_range_ratio_21d_vs_252d":       {"inputs": ["close"], "func": pcmp_089_log_range_ratio_21d_vs_252d},
    "pcmp_090_log_range_ratio_63d_vs_252d":       {"inputs": ["close"], "func": pcmp_090_log_range_ratio_63d_vs_252d},
    "pcmp_091_log_return_std_ratio_5d_vs_63d":    {"inputs": ["close"], "func": pcmp_091_log_return_std_ratio_5d_vs_63d},
    "pcmp_092_variance_ratio_21d_vs_63d":         {"inputs": ["close"], "func": pcmp_092_variance_ratio_21d_vs_63d},
    "pcmp_093_variance_ratio_21d_vs_252d":        {"inputs": ["close"], "func": pcmp_093_variance_ratio_21d_vs_252d},
    "pcmp_094_log_range_pct_rank_252d":           {"inputs": ["close"], "func": pcmp_094_log_range_pct_rank_252d},
    "pcmp_095_log_range_zscore_252d":             {"inputs": ["close"], "func": pcmp_095_log_range_zscore_252d},
    "pcmp_096_hl_channel_compression_5d_vs_252d": {"inputs": ["high", "low"], "func": pcmp_096_hl_channel_compression_5d_vs_252d},
    "pcmp_097_hl_channel_compression_21d_vs_252d": {"inputs": ["high", "low"], "func": pcmp_097_hl_channel_compression_21d_vs_252d},
    "pcmp_098_hl_channel_compression_63d_vs_252d": {"inputs": ["high", "low"], "func": pcmp_098_hl_channel_compression_63d_vs_252d},
    "pcmp_099_hl_channel_compression_5d_vs_63d":  {"inputs": ["high", "low"], "func": pcmp_099_hl_channel_compression_5d_vs_63d},
    "pcmp_100_hl_band_pct_rank_252d":             {"inputs": ["high", "low"], "func": pcmp_100_hl_band_pct_rank_252d},
    "pcmp_101_hl_band_zscore_252d":               {"inputs": ["high", "low"], "func": pcmp_101_hl_band_zscore_252d},
    "pcmp_102_hl_band_pct_rank_504d":             {"inputs": ["high", "low"], "func": pcmp_102_hl_band_pct_rank_504d},
    "pcmp_103_high_rolling_std_21d":              {"inputs": ["high"], "func": pcmp_103_high_rolling_std_21d},
    "pcmp_104_low_rolling_std_21d":               {"inputs": ["low"], "func": pcmp_104_low_rolling_std_21d},
    "pcmp_105_hl_std_sum_ratio_21d_vs_252d":      {"inputs": ["high", "low"], "func": pcmp_105_hl_std_sum_ratio_21d_vs_252d},
    "pcmp_106_close_range_frac_sma21":            {"inputs": ["close"], "func": pcmp_106_close_range_frac_sma21},
    "pcmp_107_close_range_frac_sma63":            {"inputs": ["close"], "func": pcmp_107_close_range_frac_sma63},
    "pcmp_108_close_range_frac_sma252":           {"inputs": ["close"], "func": pcmp_108_close_range_frac_sma252},
    "pcmp_109_hl_range_frac_ema21":               {"inputs": ["high", "low", "close"], "func": pcmp_109_hl_range_frac_ema21},
    "pcmp_110_hl_range_frac_ema63":               {"inputs": ["high", "low", "close"], "func": pcmp_110_hl_range_frac_ema63},
    "pcmp_111_tr_std_21d":                        {"inputs": ["close", "high", "low"], "func": pcmp_111_tr_std_21d},
    "pcmp_112_tr_std_63d":                        {"inputs": ["close", "high", "low"], "func": pcmp_112_tr_std_63d},
    "pcmp_113_tr_cv_21d":                         {"inputs": ["close", "high", "low"], "func": pcmp_113_tr_cv_21d},
    "pcmp_114_tr_cv_63d":                         {"inputs": ["close", "high", "low"], "func": pcmp_114_tr_cv_63d},
    "pcmp_115_tr_iqr_63d":                        {"inputs": ["close", "high", "low"], "func": pcmp_115_tr_iqr_63d},
    "pcmp_116_overnight_gap_frac_21d":            {"inputs": ["open", "close"], "func": pcmp_116_overnight_gap_frac_21d},
    "pcmp_117_overnight_gap_frac_63d":            {"inputs": ["open", "close"], "func": pcmp_117_overnight_gap_frac_63d},
    "pcmp_118_overnight_gap_std_21d":             {"inputs": ["open", "close"], "func": pcmp_118_overnight_gap_std_21d},
    "pcmp_119_intraday_range_frac_oc_21d":        {"inputs": ["open", "close", "high", "low"], "func": pcmp_119_intraday_range_frac_oc_21d},
    "pcmp_120_intraday_range_frac_oc_63d":        {"inputs": ["open", "close", "high", "low"], "func": pcmp_120_intraday_range_frac_oc_63d},
    "pcmp_121_close_open_body_pct_rank_252d":     {"inputs": ["open", "close"], "func": pcmp_121_close_open_body_pct_rank_252d},
    "pcmp_122_upper_shadow_frac_21d":             {"inputs": ["open", "close", "high"], "func": pcmp_122_upper_shadow_frac_21d},
    "pcmp_123_lower_shadow_frac_21d":             {"inputs": ["open", "close", "low"], "func": pcmp_123_lower_shadow_frac_21d},
    "pcmp_124_shadow_to_body_ratio_21d":          {"inputs": ["open", "close", "high", "low"], "func": pcmp_124_shadow_to_body_ratio_21d},
    "pcmp_125_narrow_body_frac_21d":              {"inputs": ["open", "close", "high", "low"], "func": pcmp_125_narrow_body_frac_21d},
    "pcmp_126_range_per_volume_5d":               {"inputs": ["high", "low", "volume"], "func": pcmp_126_range_per_volume_5d},
    "pcmp_127_range_per_volume_21d":              {"inputs": ["high", "low", "volume"], "func": pcmp_127_range_per_volume_21d},
    "pcmp_128_range_per_volume_63d":              {"inputs": ["high", "low", "volume"], "func": pcmp_128_range_per_volume_63d},
    "pcmp_129_tr_per_volume_21d":                 {"inputs": ["close", "high", "low", "volume"], "func": pcmp_129_tr_per_volume_21d},
    "pcmp_130_range_volume_ratio_5d_vs_252d":     {"inputs": ["high", "low", "volume"], "func": pcmp_130_range_volume_ratio_5d_vs_252d},
    "pcmp_131_hl_range_zscore_252d":              {"inputs": ["high", "low"], "func": pcmp_131_hl_range_zscore_252d},
    "pcmp_132_hl_range_zscore_63d":               {"inputs": ["high", "low"], "func": pcmp_132_hl_range_zscore_63d},
    "pcmp_133_tr_zscore_252d":                    {"inputs": ["close", "high", "low"], "func": pcmp_133_tr_zscore_252d},
    "pcmp_134_tr_zscore_63d":                     {"inputs": ["close", "high", "low"], "func": pcmp_134_tr_zscore_63d},
    "pcmp_135_volume_weighted_tr_21d":            {"inputs": ["close", "high", "low", "volume"], "func": pcmp_135_volume_weighted_tr_21d},
    "pcmp_136_compression_score_21d_vs_252d":     {"inputs": ["close", "high", "low"], "func": pcmp_136_compression_score_21d_vs_252d},
    "pcmp_137_compression_score_63d_vs_252d":     {"inputs": ["close", "high", "low"], "func": pcmp_137_compression_score_63d_vs_252d},
    "pcmp_138_range_contraction_streak_21d":      {"inputs": ["high", "low"], "func": pcmp_138_range_contraction_streak_21d},
    "pcmp_139_range_contraction_streak_63d":      {"inputs": ["high", "low"], "func": pcmp_139_range_contraction_streak_63d},
    "pcmp_140_tr_below_21d_mean_frac_63d":        {"inputs": ["close", "high", "low"], "func": pcmp_140_tr_below_21d_mean_frac_63d},
    "pcmp_141_range_percentile_q10_252d":         {"inputs": ["high", "low"], "func": pcmp_141_range_percentile_q10_252d},
    "pcmp_142_range_percentile_q25_252d":         {"inputs": ["high", "low"], "func": pcmp_142_range_percentile_q25_252d},
    "pcmp_143_tr_percentile_q10_252d":            {"inputs": ["close", "high", "low"], "func": pcmp_143_tr_percentile_q10_252d},
    "pcmp_144_close_std_ratio_21d_vs_252d":       {"inputs": ["close"], "func": pcmp_144_close_std_ratio_21d_vs_252d},
    "pcmp_145_close_std_ratio_63d_vs_252d":       {"inputs": ["close"], "func": pcmp_145_close_std_ratio_63d_vs_252d},
    "pcmp_146_ewm_atr_ratio_21_vs_252":           {"inputs": ["close", "high", "low"], "func": pcmp_146_ewm_atr_ratio_21_vs_252},
    "pcmp_147_ewm_atr_pct_rank_252d":             {"inputs": ["close", "high", "low"], "func": pcmp_147_ewm_atr_pct_rank_252d},
    "pcmp_148_range_momentum_21d":                {"inputs": ["high", "low"], "func": pcmp_148_range_momentum_21d},
    "pcmp_149_tr_momentum_63d":                   {"inputs": ["close", "high", "low"], "func": pcmp_149_tr_momentum_63d},
    "pcmp_150_grand_compression_composite":       {"inputs": ["close", "high", "low"], "func": pcmp_150_grand_compression_composite},
}
