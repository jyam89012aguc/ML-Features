"""
52_bar_morphology — Base Features 001-075
Domain: candlestick body/range structural statistics — body size, body-to-range ratio,
        body direction counts, doji frequency, marubozu fraction, body dispersion,
        body z-scores, consecutive same-color counts (aggregate structural statistics only)
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
    """Element-wise division; zero denominator → NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _body(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Signed body: close - open (positive = bull, negative = bear)."""
    return close - open_


def _body_abs(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Absolute body size: |close - open|."""
    return (close - open_).abs()


def _range(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bar range: high - low (always >= 0)."""
    return (high - low).clip(lower=0.0)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_quantile(s: pd.Series, w: int, q: float) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).quantile(q)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Absolute body size ---

def bmf_001_body_abs(close: pd.Series, open: pd.Series) -> pd.Series:
    """Absolute body size (|close - open|) in price units."""
    return _body_abs(close, open)


def bmf_002_body_abs_sma5(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day SMA of absolute body size."""
    return _rolling_mean(_body_abs(close, open), _TD_WEEK)


def bmf_003_body_abs_sma21(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day SMA of absolute body size."""
    return _rolling_mean(_body_abs(close, open), _TD_MON)


def bmf_004_body_abs_sma63(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day SMA of absolute body size."""
    return _rolling_mean(_body_abs(close, open), _TD_QTR)


def bmf_005_body_abs_sma252(close: pd.Series, open: pd.Series) -> pd.Series:
    """252-day SMA of absolute body size."""
    return _rolling_mean(_body_abs(close, open), _TD_YEAR)


def bmf_006_body_abs_ema21(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day EMA of absolute body size."""
    return _ewm_mean(_body_abs(close, open), _TD_MON)


def bmf_007_body_abs_median21(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day rolling median of absolute body size."""
    return _rolling_median(_body_abs(close, open), _TD_MON)


def bmf_008_body_abs_median63(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day rolling median of absolute body size."""
    return _rolling_median(_body_abs(close, open), _TD_QTR)


def bmf_009_body_abs_max21(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day rolling max of absolute body size (largest candle recently)."""
    return _rolling_max(_body_abs(close, open), _TD_MON)


def bmf_010_body_abs_max63(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day rolling max of absolute body size."""
    return _rolling_max(_body_abs(close, open), _TD_QTR)


# --- Group B (011-020): Body as percent of price and body-to-range ratio ---

def bmf_011_body_pct_of_price(close: pd.Series, open: pd.Series) -> pd.Series:
    """Absolute body as percent of mid-price ((high+low)/2 proxy: open)."""
    return _safe_div(_body_abs(close, open), open.replace(0, np.nan))


def bmf_012_body_pct_of_close(close: pd.Series, open: pd.Series) -> pd.Series:
    """Absolute body as percent of close price."""
    return _safe_div(_body_abs(close, open), close.replace(0, np.nan))


def bmf_013_body_to_range_ratio(close: pd.Series, open: pd.Series,
                                  high: pd.Series, low: pd.Series) -> pd.Series:
    """Body-to-range ratio: |close-open| / (high-low)."""
    return _safe_div(_body_abs(close, open), _range(high, low))


def bmf_014_body_to_range_sma21(close: pd.Series, open: pd.Series,
                                  high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day SMA of body-to-range ratio."""
    return _rolling_mean(bmf_013_body_to_range_ratio(close, open, high, low), _TD_MON)


def bmf_015_body_to_range_sma63(close: pd.Series, open: pd.Series,
                                  high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day SMA of body-to-range ratio."""
    return _rolling_mean(bmf_013_body_to_range_ratio(close, open, high, low), _TD_QTR)


def bmf_016_body_to_range_sma252(close: pd.Series, open: pd.Series,
                                   high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day SMA of body-to-range ratio."""
    return _rolling_mean(bmf_013_body_to_range_ratio(close, open, high, low), _TD_YEAR)


def bmf_017_body_to_range_median21(close: pd.Series, open: pd.Series,
                                    high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day rolling median of body-to-range ratio."""
    return _rolling_median(bmf_013_body_to_range_ratio(close, open, high, low), _TD_MON)


def bmf_018_body_to_range_median63(close: pd.Series, open: pd.Series,
                                    high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day rolling median of body-to-range ratio."""
    return _rolling_median(bmf_013_body_to_range_ratio(close, open, high, low), _TD_QTR)


def bmf_019_body_to_range_pct_rank_252(close: pd.Series, open: pd.Series,
                                        high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's body-to-range ratio in trailing 252-day window."""
    btr = bmf_013_body_to_range_ratio(close, open, high, low)
    return btr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def bmf_020_body_to_range_max21(close: pd.Series, open: pd.Series,
                                  high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day rolling max of body-to-range ratio."""
    return _rolling_max(bmf_013_body_to_range_ratio(close, open, high, low), _TD_MON)


# --- Group C (021-030): Body direction (bull/bear) counts and fractions ---

def bmf_021_bull_body_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary flag: 1 if close > open (bull body), 0 otherwise."""
    return (close > open).astype(float)


def bmf_022_bear_body_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary flag: 1 if close < open (bear body), 0 otherwise."""
    return (close < open).astype(float)


def bmf_023_bull_body_count_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of bull-body bars in trailing 5 days."""
    return _rolling_sum((close > open).astype(float), _TD_WEEK)


def bmf_024_bull_body_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of bull-body bars in trailing 21 days."""
    return _rolling_sum((close > open).astype(float), _TD_MON)


def bmf_025_bull_body_count_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of bull-body bars in trailing 63 days."""
    return _rolling_sum((close > open).astype(float), _TD_QTR)


def bmf_026_bear_body_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of bear-body bars in trailing 21 days."""
    return _rolling_sum((close < open).astype(float), _TD_MON)


def bmf_027_bear_body_count_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of bear-body bars in trailing 63 days."""
    return _rolling_sum((close < open).astype(float), _TD_QTR)


def bmf_028_bull_body_fraction_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of bull-body bars in trailing 21 days."""
    return _safe_div(
        _rolling_sum((close > open).astype(float), _TD_MON),
        pd.Series(_TD_MON, index=close.index, dtype=float),
    )


def bmf_029_bull_body_fraction_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of bull-body bars in trailing 63 days."""
    return _safe_div(
        _rolling_sum((close > open).astype(float), _TD_QTR),
        pd.Series(_TD_QTR, index=close.index, dtype=float),
    )


def bmf_030_bear_bull_body_ratio_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of bear-body count to bull-body count in trailing 21 days."""
    bear = _rolling_sum((close < open).astype(float), _TD_MON)
    bull = _rolling_sum((close > open).astype(float), _TD_MON)
    return _safe_div(bear, bull)


# --- Group D (031-040): Doji frequency (tiny body) ---

def bmf_031_doji_flag_1pct(close: pd.Series, open: pd.Series,
                             high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: body-to-range ratio < 0.10 (doji — tiny body relative to range)."""
    btr = bmf_013_body_to_range_ratio(close, open, high, low)
    return (btr < 0.10).astype(float)


def bmf_032_doji_flag_5pct(close: pd.Series, open: pd.Series,
                             high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: body-to-range ratio < 0.05 (near-perfect doji)."""
    btr = bmf_013_body_to_range_ratio(close, open, high, low)
    return (btr < 0.05).astype(float)


def bmf_033_doji_count_21d(close: pd.Series, open: pd.Series,
                             high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of doji bars (body/range < 0.10) in trailing 21 days."""
    return _rolling_sum(bmf_031_doji_flag_1pct(close, open, high, low), _TD_MON)


def bmf_034_doji_count_63d(close: pd.Series, open: pd.Series,
                             high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of doji bars in trailing 63 days."""
    return _rolling_sum(bmf_031_doji_flag_1pct(close, open, high, low), _TD_QTR)


def bmf_035_doji_fraction_21d(close: pd.Series, open: pd.Series,
                                high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of doji bars in trailing 21 days."""
    return _safe_div(
        bmf_033_doji_count_21d(close, open, high, low),
        pd.Series(_TD_MON, index=close.index, dtype=float),
    )


def bmf_036_doji_fraction_63d(close: pd.Series, open: pd.Series,
                                high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of doji bars in trailing 63 days."""
    return _safe_div(
        bmf_034_doji_count_63d(close, open, high, low),
        pd.Series(_TD_QTR, index=close.index, dtype=float),
    )


def bmf_037_doji_consec_streak(close: pd.Series, open: pd.Series,
                                 high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive doji-bar streak (body/range < 0.10)."""
    cond = bmf_013_body_to_range_ratio(close, open, high, low) < 0.10
    return _consec_streak(cond)


def bmf_038_doji_fraction_252d(close: pd.Series, open: pd.Series,
                                 high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of doji bars in trailing 252 days."""
    cnt = _rolling_sum(bmf_031_doji_flag_1pct(close, open, high, low), _TD_YEAR)
    return _safe_div(cnt, pd.Series(_TD_YEAR, index=close.index, dtype=float))


def bmf_039_doji_pct_rank_252(close: pd.Series, open: pd.Series,
                                high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's body-to-range ratio within 252-day window (low = doji-like)."""
    btr = bmf_013_body_to_range_ratio(close, open, high, low)
    return btr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def bmf_040_tiny_body_abs_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: absolute body < 21-day median absolute body * 0.25 (very small bar)."""
    babs = _body_abs(close, open)
    med = _rolling_median(babs, _TD_MON)
    return (babs < med * 0.25).astype(float)


# --- Group E (041-050): Marubozu-style full-body bars ---

def bmf_041_marubozu_flag_90pct(close: pd.Series, open: pd.Series,
                                  high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: body-to-range ratio >= 0.90 (marubozu-like, nearly no wicks)."""
    return (bmf_013_body_to_range_ratio(close, open, high, low) >= 0.90).astype(float)


def bmf_042_marubozu_flag_80pct(close: pd.Series, open: pd.Series,
                                  high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: body-to-range ratio >= 0.80."""
    return (bmf_013_body_to_range_ratio(close, open, high, low) >= 0.80).astype(float)


def bmf_043_marubozu_count_21d(close: pd.Series, open: pd.Series,
                                 high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of marubozu bars (body/range >= 0.90) in trailing 21 days."""
    return _rolling_sum(bmf_041_marubozu_flag_90pct(close, open, high, low), _TD_MON)


def bmf_044_marubozu_count_63d(close: pd.Series, open: pd.Series,
                                 high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of marubozu bars in trailing 63 days."""
    return _rolling_sum(bmf_041_marubozu_flag_90pct(close, open, high, low), _TD_QTR)


def bmf_045_marubozu_fraction_21d(close: pd.Series, open: pd.Series,
                                   high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of marubozu bars in trailing 21 days."""
    return _safe_div(
        bmf_043_marubozu_count_21d(close, open, high, low),
        pd.Series(_TD_MON, index=close.index, dtype=float),
    )


def bmf_046_marubozu_fraction_63d(close: pd.Series, open: pd.Series,
                                   high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of marubozu bars in trailing 63 days."""
    return _safe_div(
        bmf_044_marubozu_count_63d(close, open, high, low),
        pd.Series(_TD_QTR, index=close.index, dtype=float),
    )


def bmf_047_bear_marubozu_count_21d(close: pd.Series, open: pd.Series,
                                     high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bear-marubozu bars (body/range >= 0.90 AND close < open) in 21 days."""
    is_maru = bmf_041_marubozu_flag_90pct(close, open, high, low)
    is_bear = (close < open).astype(float)
    return _rolling_sum(is_maru * is_bear, _TD_MON)


def bmf_048_bull_marubozu_count_21d(close: pd.Series, open: pd.Series,
                                     high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bull-marubozu bars in 21 days."""
    is_maru = bmf_041_marubozu_flag_90pct(close, open, high, low)
    is_bull = (close > open).astype(float)
    return _rolling_sum(is_maru * is_bull, _TD_MON)


def bmf_049_marubozu_consec_streak(close: pd.Series, open: pd.Series,
                                    high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive marubozu-bar streak."""
    cond = bmf_013_body_to_range_ratio(close, open, high, low) >= 0.90
    return _consec_streak(cond)


def bmf_050_bear_marubozu_consec_streak(close: pd.Series, open: pd.Series,
                                         high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive bear-marubozu streak (full-body bear candles)."""
    btr = bmf_013_body_to_range_ratio(close, open, high, low)
    cond = (btr >= 0.90) & (close < open)
    return _consec_streak(cond)


# --- Group F (051-060): Body-size dispersion and variability ---

def bmf_051_body_abs_std21(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day rolling std of absolute body size (body volatility)."""
    return _rolling_std(_body_abs(close, open), _TD_MON)


def bmf_052_body_abs_std63(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day rolling std of absolute body size."""
    return _rolling_std(_body_abs(close, open), _TD_QTR)


def bmf_053_body_cv_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Coefficient of variation of body size (std/mean) over 21 days."""
    babs = _body_abs(close, open)
    return _safe_div(_rolling_std(babs, _TD_MON), _rolling_mean(babs, _TD_MON))


def bmf_054_body_cv_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Coefficient of variation of body size over 63 days."""
    babs = _body_abs(close, open)
    return _safe_div(_rolling_std(babs, _TD_QTR), _rolling_mean(babs, _TD_QTR))


def bmf_055_body_iqr_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day interquartile range of absolute body size (robust dispersion)."""
    babs = _body_abs(close, open)
    q75 = _rolling_quantile(babs, _TD_QTR, 0.75)
    q25 = _rolling_quantile(babs, _TD_QTR, 0.25)
    return q75 - q25


def bmf_056_body_range_ratio_std21(close: pd.Series, open: pd.Series,
                                    high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day std of body-to-range ratio (consistency of bar fill)."""
    return _rolling_std(bmf_013_body_to_range_ratio(close, open, high, low), _TD_MON)


def bmf_057_body_range_ratio_std63(close: pd.Series, open: pd.Series,
                                    high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day std of body-to-range ratio."""
    return _rolling_std(bmf_013_body_to_range_ratio(close, open, high, low), _TD_QTR)


def bmf_058_body_abs_norm_by_sma21(close: pd.Series, open: pd.Series) -> pd.Series:
    """Today's absolute body normalized by its 21-day SMA (relative body size)."""
    babs = _body_abs(close, open)
    return _safe_div(babs, _rolling_mean(babs, _TD_MON))


def bmf_059_body_abs_norm_by_sma63(close: pd.Series, open: pd.Series) -> pd.Series:
    """Today's absolute body normalized by its 63-day SMA."""
    babs = _body_abs(close, open)
    return _safe_div(babs, _rolling_mean(babs, _TD_QTR))


def bmf_060_body_abs_expanding_max(close: pd.Series, open: pd.Series) -> pd.Series:
    """Expanding all-time maximum absolute body size (context for extremity)."""
    return _body_abs(close, open).expanding(min_periods=1).max()


# --- Group G (061-075): Body z-scores, body vs prior body, consecutive same-color ---

def bmf_061_body_zscore_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of absolute body size within trailing 21-day window."""
    babs = _body_abs(close, open)
    m = _rolling_mean(babs, _TD_MON)
    s = _rolling_std(babs, _TD_MON)
    return _safe_div(babs - m, s)


def bmf_062_body_zscore_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of absolute body size within trailing 63-day window."""
    babs = _body_abs(close, open)
    m = _rolling_mean(babs, _TD_QTR)
    s = _rolling_std(babs, _TD_QTR)
    return _safe_div(babs - m, s)


def bmf_063_body_zscore_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of absolute body size within trailing 252-day window."""
    babs = _body_abs(close, open)
    m = _rolling_mean(babs, _TD_YEAR)
    s = _rolling_std(babs, _TD_YEAR)
    return _safe_div(babs - m, s)


def bmf_064_body_vs_prior_body_ratio(close: pd.Series, open: pd.Series) -> pd.Series:
    """Today's absolute body divided by prior day's absolute body."""
    babs = _body_abs(close, open)
    return _safe_div(babs, babs.shift(1))


def bmf_065_body_larger_than_prior_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Flag: today's body > prior day's body (expanding body)."""
    babs = _body_abs(close, open)
    return (babs > babs.shift(1)).astype(float)


def bmf_066_body_larger_than_prior_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of days where body > prior body in trailing 21 days."""
    flag = bmf_065_body_larger_than_prior_flag(close, open)
    return _rolling_sum(flag, _TD_MON)


def bmf_067_consec_bull_body_streak(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current consecutive bull-body (close > open) streak length."""
    cond = close > open
    return _consec_streak(cond)


def bmf_068_consec_bear_body_streak(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current consecutive bear-body (close < open) streak length."""
    cond = close < open
    return _consec_streak(cond)


def bmf_069_max_consec_bear_body_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum consecutive bear-body run within trailing 21 days."""
    cond = close < open
    def _max_run(arr):
        mx, cur = 0, 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return cond.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(_max_run, raw=True)


def bmf_070_max_consec_bear_body_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum consecutive bear-body run within trailing 63 days."""
    cond = close < open
    def _max_run(arr):
        mx, cur = 0, 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return cond.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_max_run, raw=True)


def bmf_071_signed_body_sma21(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day SMA of signed body (close - open); positive = net bull pressure."""
    return _rolling_mean(_body(close, open), _TD_MON)


def bmf_072_signed_body_sma63(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day SMA of signed body."""
    return _rolling_mean(_body(close, open), _TD_QTR)


def bmf_073_bear_body_fraction_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of bear-body bars in trailing 252 days."""
    cnt = _rolling_sum((close < open).astype(float), _TD_YEAR)
    return _safe_div(cnt, pd.Series(_TD_YEAR, index=close.index, dtype=float))


def bmf_074_body_abs_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of today's absolute body in trailing 252-day distribution."""
    babs = _body_abs(close, open)
    return babs.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def bmf_075_body_to_range_ratio_expanding_rank(close: pd.Series, open: pd.Series,
                                                high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding percentile rank of body-to-range ratio (all-history context)."""
    btr = bmf_013_body_to_range_ratio(close, open, high, low)
    return btr.expanding(min_periods=5).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

BAR_MORPHOLOGY_REGISTRY_001_075 = {
    "bmf_001_body_abs": {"inputs": ["close", "open"], "func": bmf_001_body_abs},
    "bmf_002_body_abs_sma5": {"inputs": ["close", "open"], "func": bmf_002_body_abs_sma5},
    "bmf_003_body_abs_sma21": {"inputs": ["close", "open"], "func": bmf_003_body_abs_sma21},
    "bmf_004_body_abs_sma63": {"inputs": ["close", "open"], "func": bmf_004_body_abs_sma63},
    "bmf_005_body_abs_sma252": {"inputs": ["close", "open"], "func": bmf_005_body_abs_sma252},
    "bmf_006_body_abs_ema21": {"inputs": ["close", "open"], "func": bmf_006_body_abs_ema21},
    "bmf_007_body_abs_median21": {"inputs": ["close", "open"], "func": bmf_007_body_abs_median21},
    "bmf_008_body_abs_median63": {"inputs": ["close", "open"], "func": bmf_008_body_abs_median63},
    "bmf_009_body_abs_max21": {"inputs": ["close", "open"], "func": bmf_009_body_abs_max21},
    "bmf_010_body_abs_max63": {"inputs": ["close", "open"], "func": bmf_010_body_abs_max63},
    "bmf_011_body_pct_of_price": {"inputs": ["close", "open"], "func": bmf_011_body_pct_of_price},
    "bmf_012_body_pct_of_close": {"inputs": ["close", "open"], "func": bmf_012_body_pct_of_close},
    "bmf_013_body_to_range_ratio": {"inputs": ["close", "open", "high", "low"], "func": bmf_013_body_to_range_ratio},
    "bmf_014_body_to_range_sma21": {"inputs": ["close", "open", "high", "low"], "func": bmf_014_body_to_range_sma21},
    "bmf_015_body_to_range_sma63": {"inputs": ["close", "open", "high", "low"], "func": bmf_015_body_to_range_sma63},
    "bmf_016_body_to_range_sma252": {"inputs": ["close", "open", "high", "low"], "func": bmf_016_body_to_range_sma252},
    "bmf_017_body_to_range_median21": {"inputs": ["close", "open", "high", "low"], "func": bmf_017_body_to_range_median21},
    "bmf_018_body_to_range_median63": {"inputs": ["close", "open", "high", "low"], "func": bmf_018_body_to_range_median63},
    "bmf_019_body_to_range_pct_rank_252": {"inputs": ["close", "open", "high", "low"], "func": bmf_019_body_to_range_pct_rank_252},
    "bmf_020_body_to_range_max21": {"inputs": ["close", "open", "high", "low"], "func": bmf_020_body_to_range_max21},
    "bmf_021_bull_body_flag": {"inputs": ["close", "open"], "func": bmf_021_bull_body_flag},
    "bmf_022_bear_body_flag": {"inputs": ["close", "open"], "func": bmf_022_bear_body_flag},
    "bmf_023_bull_body_count_5d": {"inputs": ["close", "open"], "func": bmf_023_bull_body_count_5d},
    "bmf_024_bull_body_count_21d": {"inputs": ["close", "open"], "func": bmf_024_bull_body_count_21d},
    "bmf_025_bull_body_count_63d": {"inputs": ["close", "open"], "func": bmf_025_bull_body_count_63d},
    "bmf_026_bear_body_count_21d": {"inputs": ["close", "open"], "func": bmf_026_bear_body_count_21d},
    "bmf_027_bear_body_count_63d": {"inputs": ["close", "open"], "func": bmf_027_bear_body_count_63d},
    "bmf_028_bull_body_fraction_21d": {"inputs": ["close", "open"], "func": bmf_028_bull_body_fraction_21d},
    "bmf_029_bull_body_fraction_63d": {"inputs": ["close", "open"], "func": bmf_029_bull_body_fraction_63d},
    "bmf_030_bear_bull_body_ratio_21d": {"inputs": ["close", "open"], "func": bmf_030_bear_bull_body_ratio_21d},
    "bmf_031_doji_flag_1pct": {"inputs": ["close", "open", "high", "low"], "func": bmf_031_doji_flag_1pct},
    "bmf_032_doji_flag_5pct": {"inputs": ["close", "open", "high", "low"], "func": bmf_032_doji_flag_5pct},
    "bmf_033_doji_count_21d": {"inputs": ["close", "open", "high", "low"], "func": bmf_033_doji_count_21d},
    "bmf_034_doji_count_63d": {"inputs": ["close", "open", "high", "low"], "func": bmf_034_doji_count_63d},
    "bmf_035_doji_fraction_21d": {"inputs": ["close", "open", "high", "low"], "func": bmf_035_doji_fraction_21d},
    "bmf_036_doji_fraction_63d": {"inputs": ["close", "open", "high", "low"], "func": bmf_036_doji_fraction_63d},
    "bmf_037_doji_consec_streak": {"inputs": ["close", "open", "high", "low"], "func": bmf_037_doji_consec_streak},
    "bmf_038_doji_fraction_252d": {"inputs": ["close", "open", "high", "low"], "func": bmf_038_doji_fraction_252d},
    "bmf_039_doji_pct_rank_252": {"inputs": ["close", "open", "high", "low"], "func": bmf_039_doji_pct_rank_252},
    "bmf_040_tiny_body_abs_flag": {"inputs": ["close", "open"], "func": bmf_040_tiny_body_abs_flag},
    "bmf_041_marubozu_flag_90pct": {"inputs": ["close", "open", "high", "low"], "func": bmf_041_marubozu_flag_90pct},
    "bmf_042_marubozu_flag_80pct": {"inputs": ["close", "open", "high", "low"], "func": bmf_042_marubozu_flag_80pct},
    "bmf_043_marubozu_count_21d": {"inputs": ["close", "open", "high", "low"], "func": bmf_043_marubozu_count_21d},
    "bmf_044_marubozu_count_63d": {"inputs": ["close", "open", "high", "low"], "func": bmf_044_marubozu_count_63d},
    "bmf_045_marubozu_fraction_21d": {"inputs": ["close", "open", "high", "low"], "func": bmf_045_marubozu_fraction_21d},
    "bmf_046_marubozu_fraction_63d": {"inputs": ["close", "open", "high", "low"], "func": bmf_046_marubozu_fraction_63d},
    "bmf_047_bear_marubozu_count_21d": {"inputs": ["close", "open", "high", "low"], "func": bmf_047_bear_marubozu_count_21d},
    "bmf_048_bull_marubozu_count_21d": {"inputs": ["close", "open", "high", "low"], "func": bmf_048_bull_marubozu_count_21d},
    "bmf_049_marubozu_consec_streak": {"inputs": ["close", "open", "high", "low"], "func": bmf_049_marubozu_consec_streak},
    "bmf_050_bear_marubozu_consec_streak": {"inputs": ["close", "open", "high", "low"], "func": bmf_050_bear_marubozu_consec_streak},
    "bmf_051_body_abs_std21": {"inputs": ["close", "open"], "func": bmf_051_body_abs_std21},
    "bmf_052_body_abs_std63": {"inputs": ["close", "open"], "func": bmf_052_body_abs_std63},
    "bmf_053_body_cv_21d": {"inputs": ["close", "open"], "func": bmf_053_body_cv_21d},
    "bmf_054_body_cv_63d": {"inputs": ["close", "open"], "func": bmf_054_body_cv_63d},
    "bmf_055_body_iqr_63d": {"inputs": ["close", "open"], "func": bmf_055_body_iqr_63d},
    "bmf_056_body_range_ratio_std21": {"inputs": ["close", "open", "high", "low"], "func": bmf_056_body_range_ratio_std21},
    "bmf_057_body_range_ratio_std63": {"inputs": ["close", "open", "high", "low"], "func": bmf_057_body_range_ratio_std63},
    "bmf_058_body_abs_norm_by_sma21": {"inputs": ["close", "open"], "func": bmf_058_body_abs_norm_by_sma21},
    "bmf_059_body_abs_norm_by_sma63": {"inputs": ["close", "open"], "func": bmf_059_body_abs_norm_by_sma63},
    "bmf_060_body_abs_expanding_max": {"inputs": ["close", "open"], "func": bmf_060_body_abs_expanding_max},
    "bmf_061_body_zscore_21d": {"inputs": ["close", "open"], "func": bmf_061_body_zscore_21d},
    "bmf_062_body_zscore_63d": {"inputs": ["close", "open"], "func": bmf_062_body_zscore_63d},
    "bmf_063_body_zscore_252d": {"inputs": ["close", "open"], "func": bmf_063_body_zscore_252d},
    "bmf_064_body_vs_prior_body_ratio": {"inputs": ["close", "open"], "func": bmf_064_body_vs_prior_body_ratio},
    "bmf_065_body_larger_than_prior_flag": {"inputs": ["close", "open"], "func": bmf_065_body_larger_than_prior_flag},
    "bmf_066_body_larger_than_prior_count_21d": {"inputs": ["close", "open"], "func": bmf_066_body_larger_than_prior_count_21d},
    "bmf_067_consec_bull_body_streak": {"inputs": ["close", "open"], "func": bmf_067_consec_bull_body_streak},
    "bmf_068_consec_bear_body_streak": {"inputs": ["close", "open"], "func": bmf_068_consec_bear_body_streak},
    "bmf_069_max_consec_bear_body_21d": {"inputs": ["close", "open"], "func": bmf_069_max_consec_bear_body_21d},
    "bmf_070_max_consec_bear_body_63d": {"inputs": ["close", "open"], "func": bmf_070_max_consec_bear_body_63d},
    "bmf_071_signed_body_sma21": {"inputs": ["close", "open"], "func": bmf_071_signed_body_sma21},
    "bmf_072_signed_body_sma63": {"inputs": ["close", "open"], "func": bmf_072_signed_body_sma63},
    "bmf_073_bear_body_fraction_252d": {"inputs": ["close", "open"], "func": bmf_073_bear_body_fraction_252d},
    "bmf_074_body_abs_pct_rank_252d": {"inputs": ["close", "open"], "func": bmf_074_body_abs_pct_rank_252d},
    "bmf_075_body_to_range_ratio_expanding_rank": {"inputs": ["close", "open", "high", "low"], "func": bmf_075_body_to_range_ratio_expanding_rank},
}
