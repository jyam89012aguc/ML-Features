"""
41_range_compression — Base Features 076-150
Domain: range compression/squeeze — expand-then-collapse tells, contraction z-scores,
        volume-during-squeeze, multi-window contraction ratios, coil tightness scores,
        compression after expansion (capitulation setup). Range CONTRACTION only.
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Expand-then-collapse capitulation pattern ---

def rcp_076_tr_collapse_after_expansion_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: prior 5d had TR above 252d mean, today TR is below 252d mean (expand then collapse)."""
    tr = _tr(close, high, low)
    mean252 = _rolling_mean(tr, _TD_YEAR)
    prior_expanded = _rolling_min(tr.shift(1), _TD_WEEK) > mean252.shift(1)
    now_compressed = tr < mean252
    return (prior_expanded & now_compressed).astype(float)


def rcp_077_tr_collapse_ratio_after_5d_peak(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's TR divided by 5-day trailing max TR (how much range fell from recent peak)."""
    tr = _tr(close, high, low)
    peak5 = tr.shift(1).rolling(_TD_WEEK, min_periods=1).max()
    return _safe_div(tr, peak5)


def rcp_078_tr_collapse_ratio_after_21d_peak(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's TR divided by 21-day trailing max TR."""
    tr = _tr(close, high, low)
    peak21 = tr.shift(1).rolling(_TD_MON, min_periods=1).max()
    return _safe_div(tr, peak21)


def rcp_079_tr_collapse_ratio_after_63d_peak(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's TR divided by 63-day trailing max TR."""
    tr = _tr(close, high, low)
    peak63 = tr.shift(1).rolling(_TD_QTR, min_periods=1).max()
    return _safe_div(tr, peak63)


def rcp_080_days_since_tr_5d_peak(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Days elapsed since the last 5-day TR peak (how long contraction has lasted)."""
    tr = _tr(close, high, low)
    peak5 = _rolling_max(tr, _TD_WEEK)
    at_peak = (tr >= peak5 * (1 - _EPS)).astype(float)
    group = at_peak.cumsum()
    idx = pd.Series(range(len(tr)), index=tr.index, dtype=float)
    last_peak_idx = idx.where(at_peak == 1).groupby(group).transform("max")
    return (idx - last_peak_idx).clip(lower=0)


def rcp_081_days_since_tr_21d_peak(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Days elapsed since the last 21-day TR peak."""
    tr = _tr(close, high, low)
    peak21 = _rolling_max(tr, _TD_MON)
    at_peak = (tr >= peak21 * (1 - _EPS)).astype(float)
    group = at_peak.cumsum()
    idx = pd.Series(range(len(tr)), index=tr.index, dtype=float)
    last_peak_idx = idx.where(at_peak == 1).groupby(group).transform("max")
    return (idx - last_peak_idx).clip(lower=0)


def rcp_082_expand_then_collapse_score_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Score: 21d max TR minus current TR, normalized by 252d mean TR (expansion amplitude)."""
    tr = _tr(close, high, low)
    peak21 = tr.shift(1).rolling(_TD_MON, min_periods=1).max()
    mean252 = _rolling_mean(tr, _TD_YEAR)
    return _safe_div(peak21 - tr, mean252)


def rcp_083_expand_collapse_ratio_21d_vs_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of (21d max TR - current TR) to 252d max TR (how deep the collapse)."""
    tr = _tr(close, high, low)
    peak21 = tr.shift(1).rolling(_TD_MON, min_periods=1).max()
    peak252 = tr.shift(1).rolling(_TD_YEAR, min_periods=1).max()
    return _safe_div(peak21 - tr, peak252)


def rcp_084_atr_decline_from_21d_peak_pct(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Pct decline of ATR21 from its trailing 63-day peak (smoothed compression depth)."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    peak = atr21.shift(1).rolling(_TD_QTR, min_periods=1).max()
    return _safe_div(atr21 - peak, peak)


def rcp_085_consec_tr_below_21d_max(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days where TR is below the trailing 21-day max TR (contraction streak)."""
    tr = _tr(close, high, low)
    peak21 = tr.shift(1).rolling(_TD_MON, min_periods=1).max()
    cond = tr < peak21
    return _consec_streak(cond)


# --- Group I (086-095): Volume behavior during compression ---

def rcp_086_vol_during_squeeze_vs_baseline(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on NR4 days divided by 21-day avg volume (quiet or panicked squeeze)."""
    rng = high - low
    prev_max = pd.concat([rng.shift(1), rng.shift(2), rng.shift(3)], axis=1).max(axis=1)
    nr4 = rng < prev_max
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_on_nr4 = volume.where(nr4, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(vol_on_nr4, avg_vol)


def rcp_087_vol_below_avg_on_narrow_day(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: today is NR4 AND volume is below 21-day avg volume (classic quiet coil)."""
    rng = high - low
    prev_max = pd.concat([rng.shift(1), rng.shift(2), rng.shift(3)], axis=1).max(axis=1)
    nr4 = rng < prev_max
    avg_vol = _rolling_mean(volume, _TD_MON)
    return (nr4 & (volume < avg_vol)).astype(float)


def rcp_088_consec_low_vol_narrow_days(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Streak of consecutive days with both below-avg TR and below-avg volume."""
    tr = _tr(close, high, low)
    avg_tr = _rolling_mean(tr, _TD_MON)
    avg_vol = _rolling_mean(volume, _TD_MON)
    cond = (tr < avg_tr) & (volume < avg_vol)
    return _consec_streak(cond)


def rcp_089_vol_compression_ratio_21d(volume: pd.Series) -> pd.Series:
    """Volume 5-day std / 5-day mean divided by 21-day std / 21-day mean (vol tightness)."""
    vol5_cv = _safe_div(_rolling_std(volume, _TD_WEEK), _rolling_mean(volume, _TD_WEEK))
    vol21_cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    return _safe_div(vol5_cv, vol21_cv)


def rcp_090_low_vol_squeeze_score(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Combined: BB squeeze flag * (1 - vol_ratio) where low vol = stronger coil signal."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    squeeze = (2.0 * s < 2.0 * atr21).astype(float)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_ratio = _safe_div(volume, avg_vol).clip(upper=3.0)
    return squeeze * (1.0 - vol_ratio.clip(upper=1.0))


def rcp_091_vol_decline_during_tr_compression(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Correlation sign: both TR and volume declining together (silent coil)."""
    tr = _tr(close, high, low)
    tr_declining = (tr < tr.shift(1)).astype(float)
    vol_declining = (volume < volume.shift(1)).astype(float)
    return tr_declining * vol_declining


def rcp_092_vol_consec_declining_on_narrow_tr(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Streak of days where both TR and volume are below their prior-day values."""
    tr = _tr(close, high, low)
    cond = (tr < tr.shift(1)) & (volume < volume.shift(1))
    return _consec_streak(cond)


def rcp_093_squeeze_vol_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of (TR/avg_TR * vol/avg_vol) within trailing 252 days."""
    tr = _tr(close, high, low)
    avg_tr = _rolling_mean(tr, _TD_MON)
    avg_vol = _rolling_mean(volume, _TD_MON)
    score = _safe_div(tr, avg_tr) * _safe_div(volume, avg_vol)
    return score.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def rcp_094_avg_vol_on_nr7_days_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on NR7 days within trailing 21 days vs overall avg."""
    rng = high - low
    prev_max = rng.shift(1).rolling(6, min_periods=3).max()
    nr7 = rng < prev_max
    vol_nr7 = volume.where(nr7, np.nan).rolling(_TD_MON, min_periods=1).mean()
    vol_all = _rolling_mean(volume, _TD_MON)
    return _safe_div(vol_nr7, vol_all)


def rcp_095_low_vol_low_tr_days_fraction_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days with BOTH below-median TR AND below-median volume."""
    tr = _tr(close, high, low)
    med_tr = _rolling_median(tr, _TD_QTR)
    med_vol = _rolling_median(volume, _TD_QTR)
    cond = (tr < med_tr) & (volume < med_vol)
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


# --- Group J (096-105): Range contraction relative to price level ---

def rcp_096_tr_pct_of_close_21d_mean(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day mean TR as percentage of close (normalized ATR)."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_MON), close)


def rcp_097_tr_pct_of_close_63d_mean(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day mean TR as percentage of close."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_QTR), close)


def rcp_098_tr_pct_of_close_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of daily TR/close ratio within trailing 252-day distribution."""
    tr = _tr(close, high, low)
    tr_pct = _safe_div(tr, close)
    return tr_pct.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def rcp_099_hl_pct_of_close_21d_mean(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day mean of (high-low)/close."""
    rng = _safe_div(high - low, close)
    return _rolling_mean(rng, _TD_MON)


def rcp_100_hl_pct_close_ratio_vs_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day mean (HL/close) divided by 252-day mean (HL/close) — relative compression."""
    rng_pct = _safe_div(high - low, close)
    m21 = _rolling_mean(rng_pct, _TD_MON)
    m252 = _rolling_mean(rng_pct, _TD_YEAR)
    return _safe_div(m21, m252)


def rcp_101_open_close_range_pct_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day mean of abs(close-open)/close (intraday body compression)."""
    body = (close - open).abs() / close.replace(0, np.nan)
    return _rolling_mean(body, _TD_MON)


def rcp_102_open_close_body_ratio_to_hl(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of abs(close-open) to (high-low) — low ratio = doji/compression candle."""
    body = (close - open).abs()
    rng = (high - low).replace(0, np.nan)
    return _safe_div(body, rng)


def rcp_103_body_ratio_21d_mean(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day mean of body/range ratio."""
    body = (close - open).abs()
    rng = (high - low).replace(0, np.nan)
    ratio = _safe_div(body, rng)
    return _rolling_mean(ratio, _TD_MON)


def rcp_104_body_ratio_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of body/range ratio within trailing 252-day distribution."""
    body = (close - open).abs()
    rng = (high - low).replace(0, np.nan)
    ratio = _safe_div(body, rng)
    return ratio.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def rcp_105_wicks_fraction_of_range_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day mean of (total wicks) / (high-low range) — high wicks = indecision/compression."""
    rng = (high - low).replace(0, np.nan)
    upper_wick = high - pd.concat([close, open], axis=1).max(axis=1)
    lower_wick = pd.concat([close, open], axis=1).min(axis=1) - low
    total_wick = upper_wick + lower_wick
    wick_frac = _safe_div(total_wick, rng)
    return _rolling_mean(wick_frac, _TD_MON)


# --- Group K (106-115): Multi-window ATR contraction depth ---

def rcp_106_atr5_vs_atr21_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR5 divided by ATR21 — below 1 = short-term compression vs medium-term."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_WEEK), _rolling_mean(tr, _TD_MON))


def rcp_107_atr5_vs_atr63_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR5 divided by ATR63 — below 1 = very short-term compression."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_mean(tr, _TD_WEEK), _rolling_mean(tr, _TD_QTR))


def rcp_108_atr10_vs_atr21_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR10 divided by ATR21 — 2-week vs monthly compression ratio."""
    tr = _tr(close, high, low)
    return _safe_div(_rolling_mean(tr, 10), _rolling_mean(tr, _TD_MON))


def rcp_109_atr21_decline_from_63d_max(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR21 drop from its 63-day peak as a fraction of that peak."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    peak63 = atr21.shift(1).rolling(_TD_QTR, min_periods=1).max()
    return _safe_div(atr21 - peak63, peak63)


def rcp_110_atr5_decline_from_21d_max(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR5 drop from its 21-day peak as a fraction of that peak."""
    tr = _tr(close, high, low)
    atr5 = _rolling_mean(tr, _TD_WEEK)
    peak21 = atr5.shift(1).rolling(_TD_MON, min_periods=1).max()
    return _safe_div(atr5 - peak21, peak21)


def rcp_111_atr21_below_atr63_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: ATR21 < ATR63 (short-term range compressed below medium-term baseline)."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    atr63 = _rolling_mean(tr, _TD_QTR)
    return (atr21 < atr63).astype(float)


def rcp_112_consec_atr21_below_atr63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days where ATR21 < ATR63 (sustained compression below medium baseline)."""
    tr = _tr(close, high, low)
    cond = _rolling_mean(tr, _TD_MON) < _rolling_mean(tr, _TD_QTR)
    return _consec_streak(cond)


def rcp_113_atr21_below_atr252_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: ATR21 < ATR252 (recent range compressed below annual baseline)."""
    tr = _tr(close, high, low)
    return (_rolling_mean(tr, _TD_MON) < _rolling_mean(tr, _TD_YEAR)).astype(float)


def rcp_114_consec_atr21_below_atr252(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days where ATR21 < ATR252 (sustained annual compression)."""
    tr = _tr(close, high, low)
    cond = _rolling_mean(tr, _TD_MON) < _rolling_mean(tr, _TD_YEAR)
    return _consec_streak(cond)


def rcp_115_atr_compression_composite(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Composite: avg of ATR5/ATR21, ATR21/ATR63, ATR63/ATR252 ratios."""
    tr = _tr(close, high, low)
    r1 = _safe_div(_rolling_mean(tr, _TD_WEEK), _rolling_mean(tr, _TD_MON))
    r2 = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_QTR))
    r3 = _safe_div(_rolling_mean(tr, _TD_QTR), _rolling_mean(tr, _TD_YEAR))
    return (r1 + r2 + r3) / 3.0


# --- Group L (116-125): Rolling contraction count and frequency metrics ---

def rcp_116_tr_below_21d_mean_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days where TR < 21d mean TR in trailing 63 days."""
    tr = _tr(close, high, low)
    cond = tr < _rolling_mean(tr, _TD_MON)
    return _rolling_count_true(cond, _TD_QTR)


def rcp_117_tr_below_21d_mean_fraction_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 252 days where daily TR was below 21-day mean TR."""
    tr = _tr(close, high, low)
    cond = tr < _rolling_mean(tr, _TD_MON)
    return _rolling_count_true(cond, _TD_YEAR) / _TD_YEAR


def rcp_118_atr21_at_252d_min_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today's ATR21 is at a 252-day low (maximum recent compression)."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    mn252 = _rolling_min(atr21, _TD_YEAR)
    return (atr21 <= mn252 * (1 + _EPS)).astype(float)


def rcp_119_atr21_at_504d_min_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today's ATR21 is at a 504-day low (very rare multi-year compression)."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    mn504 = _rolling_min(atr21, 504)
    return (atr21 <= mn504 * (1 + _EPS)).astype(float)


def rcp_120_tr_below_10th_pct_252d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today's TR is in the bottom 10th percentile of trailing 252-day TR distribution."""
    tr = _tr(close, high, low)
    p10 = tr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.10)
    return (tr <= p10).astype(float)


def rcp_121_tr_below_25th_pct_252d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: today's TR is in the bottom 25th percentile of trailing 252-day TR distribution."""
    tr = _tr(close, high, low)
    p25 = tr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.25)
    return (tr <= p25).astype(float)


def rcp_122_narrow_day_streak_norm_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current narrowing-TR streak normalized by 252-day average narrowing streak."""
    tr = _tr(close, high, low)
    streak = _consec_streak(tr < tr.shift(1))
    avg = _rolling_mean(streak, _TD_YEAR)
    return _safe_div(streak, avg)


def rcp_123_nr4_streak_zscore_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of current NR4 streak vs 252-day distribution of NR4 streaks."""
    rng = high - low
    prev_max = pd.concat([rng.shift(1), rng.shift(2), rng.shift(3)], axis=1).max(axis=1)
    streak = _consec_streak(rng < prev_max)
    mu = _rolling_mean(streak, _TD_YEAR)
    sigma = _rolling_std(streak, _TD_YEAR)
    return _safe_div(streak - mu, sigma)


def rcp_124_bb_width_min_63d(close: pd.Series) -> pd.Series:
    """Trailing 63-day minimum of the 21-day Bollinger Band width."""
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bw = _safe_div(2.0 * s, m)
    return _rolling_min(bw, _TD_QTR)


def rcp_125_bb_width_min_252d(close: pd.Series) -> pd.Series:
    """Trailing 252-day minimum of the 21-day Bollinger Band width."""
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bw = _safe_div(2.0 * s, m)
    return _rolling_min(bw, _TD_YEAR)


# --- Group M (126-135): Compression z-scores and percentile ranks expanded ---

def rcp_126_atr5_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of ATR5 within trailing 252-day ATR5 distribution."""
    tr = _tr(close, high, low)
    atr5 = _rolling_mean(tr, _TD_WEEK)
    mu = _rolling_mean(atr5, _TD_YEAR)
    sigma = _rolling_std(atr5, _TD_YEAR)
    return _safe_div(atr5 - mu, sigma)


def rcp_127_atr5_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of ATR5 within trailing 252-day ATR5 distribution."""
    tr = _tr(close, high, low)
    atr5 = _rolling_mean(tr, _TD_WEEK)
    return atr5.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def rcp_128_atr63_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of ATR63 within trailing 252-day ATR63 distribution."""
    tr = _tr(close, high, low)
    atr63 = _rolling_mean(tr, _TD_QTR)
    mu = _rolling_mean(atr63, _TD_YEAR)
    sigma = _rolling_std(atr63, _TD_YEAR)
    return _safe_div(atr63 - mu, sigma)


def rcp_129_hl_range_zscore_expanding(high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding all-history z-score of the daily high-low range."""
    rng = high - low
    mu = rng.expanding(min_periods=5).mean()
    sigma = rng.expanding(min_periods=5).std()
    return _safe_div(rng - mu, sigma)


def rcp_130_tr_expanding_zscore(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding all-history z-score of the true range."""
    tr = _tr(close, high, low)
    mu = tr.expanding(min_periods=5).mean()
    sigma = tr.expanding(min_periods=5).std()
    return _safe_div(tr - mu, sigma)


def rcp_131_bb_squeeze_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Bollinger squeeze days within trailing 63 days."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    squeeze = 2.0 * s < 2.0 * atr21
    return _rolling_count_true(squeeze, _TD_QTR)


def rcp_132_bb_squeeze_fraction_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 252 days in Bollinger squeeze condition."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    squeeze = 2.0 * s < 2.0 * atr21
    return _rolling_count_true(squeeze, _TD_YEAR) / _TD_YEAR


def rcp_133_narrow_range_cluster_score_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR4 days in 21d weighted by how narrow each was vs prior-3-day max."""
    rng = high - low
    prev_max = pd.concat([rng.shift(1), rng.shift(2), rng.shift(3)], axis=1).max(axis=1)
    narrowness = (prev_max - rng).clip(lower=0)
    narrowness_on_nr4 = narrowness.where(rng < prev_max, 0.0)
    return _rolling_sum(narrowness_on_nr4, _TD_MON)


def rcp_134_compression_depth_composite_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Composite compression depth: avg of TR/21d_max, BB_pct_rank, ATR21/ATR252."""
    tr = _tr(close, high, low)
    tr_vs_max = _safe_div(tr, _rolling_max(tr, _TD_MON))
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bw = _safe_div(2.0 * s, m)
    bb_rank = bw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    atr_ratio = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_YEAR))
    return (tr_vs_max + bb_rank + atr_ratio) / 3.0


def rcp_135_coil_score_expanding_zscore(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding z-score of ATR21 — how extreme is current compression historically."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    mu = atr21.expanding(min_periods=5).mean()
    sigma = atr21.expanding(min_periods=5).std()
    return _safe_div(atr21 - mu, sigma)


# --- Group N (136-145): Intraday price location tightness during compression ---

def rcp_136_close_near_midpoint_21d_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: close is within 25% of the daily midpoint (indecision = coil compression)."""
    mid = (high + low) / 2.0
    rng = (high - low).replace(0, np.nan)
    deviation = (close - mid).abs() / rng
    return (deviation < 0.25).astype(float)


def rcp_137_close_near_midpoint_count_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of near-midpoint close days in trailing 21 days."""
    mid = (high + low) / 2.0
    rng = (high - low).replace(0, np.nan)
    deviation = (close - mid).abs() / rng
    cond = deviation < 0.25
    return _rolling_count_true(cond, _TD_MON)


def rcp_138_high_low_channel_contraction_score(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 5-day HL channel width to 21-day HL channel width (rapid contraction)."""
    h5 = _rolling_max(high, _TD_WEEK)
    l5 = _rolling_min(low, _TD_WEEK)
    h21 = _rolling_max(high, _TD_MON)
    l21 = _rolling_min(low, _TD_MON)
    return _safe_div(h5 - l5, h21 - l21)


def rcp_139_high_low_channel_5d_vs_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 5-day HL channel to 63-day HL channel."""
    h5 = _rolling_max(high, _TD_WEEK)
    l5 = _rolling_min(low, _TD_WEEK)
    h63 = _rolling_max(high, _TD_QTR)
    l63 = _rolling_min(low, _TD_QTR)
    return _safe_div(h5 - l5, h63 - l63)


def rcp_140_high_low_channel_21d_vs_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 21-day HL channel to 63-day HL channel (medium compression)."""
    h21 = _rolling_max(high, _TD_MON)
    l21 = _rolling_min(low, _TD_MON)
    h63 = _rolling_max(high, _TD_QTR)
    l63 = _rolling_min(low, _TD_QTR)
    return _safe_div(h21 - l21, h63 - l63)


def rcp_141_upper_shadow_compression_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day mean upper shadow / TR ratio (shrinking upper wicks = downtrend compression)."""
    upper_wick = high - pd.concat([close, open], axis=1).max(axis=1)
    tr = _tr(close, high, low)
    ratio = _safe_div(upper_wick, tr)
    return _rolling_mean(ratio, _TD_MON)


def rcp_142_lower_shadow_compression_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day mean lower shadow / TR ratio (shrinking lower wicks = coil)."""
    lower_wick = pd.concat([close, open], axis=1).min(axis=1) - low
    tr = _tr(close, high, low)
    ratio = _safe_div(lower_wick, tr)
    return _rolling_mean(ratio, _TD_MON)


def rcp_143_wick_compression_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of total wick fraction within trailing 252-day distribution."""
    rng = (high - low).replace(0, np.nan)
    upper = high - pd.concat([close, open], axis=1).max(axis=1)
    lower = pd.concat([close, open], axis=1).min(axis=1) - low
    wick_frac = _safe_div(upper + lower, rng)
    return wick_frac.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)


def rcp_144_tr_contraction_speed_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Rate of TR decline over 5 days: (TR - TR_5d_ago) / TR_5d_ago."""
    tr = _tr(close, high, low)
    return _safe_div(tr - tr.shift(_TD_WEEK), tr.shift(_TD_WEEK))


def rcp_145_tr_contraction_speed_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Rate of TR decline over 21 days: (TR - TR_21d_ago) / TR_21d_ago."""
    tr = _tr(close, high, low)
    return _safe_div(tr - tr.shift(_TD_MON), tr.shift(_TD_MON))


# --- Group O (146-150): Composite squeeze distress indicators ---

def rcp_146_squeeze_distress_index(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: BB squeeze flag * (1 - ATR21/ATR252) * (vol_rank) — silent coil score."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    atr252 = _rolling_mean(tr, _TD_YEAR)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    squeeze = (2.0 * s < 2.0 * atr21).astype(float)
    compression = (1.0 - _safe_div(atr21, atr252)).clip(lower=0)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_rank = (1.0 - _safe_div(volume, avg_vol)).clip(lower=0, upper=1)
    return squeeze * compression * vol_rank


def rcp_147_nr4_bb_keltner_triple_squeeze(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: NR4 day AND BB squeeze AND ATR21 < ATR63 (triple compression confirmation)."""
    rng = high - low
    prev_max = pd.concat([rng.shift(1), rng.shift(2), rng.shift(3)], axis=1).max(axis=1)
    nr4 = rng < prev_max
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    atr63 = _rolling_mean(tr, _TD_QTR)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bb_sq = 2.0 * s < 2.0 * atr21
    atr_comp = atr21 < atr63
    return (nr4 & bb_sq & atr_comp).astype(float)


def rcp_148_compression_after_high_vol_flag(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: current TR below 21d mean AND prior 5d had above-avg volume (panic-then-coil)."""
    tr = _tr(close, high, low)
    avg_tr = _rolling_mean(tr, _TD_MON)
    avg_vol = _rolling_mean(volume, _TD_MON)
    prior_high_vol = _rolling_min(volume.shift(1), _TD_WEEK) > avg_vol.shift(1)
    now_compressed = tr < avg_tr
    return (prior_high_vol & now_compressed).astype(float)


def rcp_149_squeeze_duration_weighted_depth(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Squeeze streak length times compression depth (ATR_ratio below 1): duration * depth."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    atr63 = _rolling_mean(tr, _TD_QTR)
    ratio = _safe_div(atr21, atr63)
    depth = (1.0 - ratio).clip(lower=0)
    cond = atr21 < atr63
    streak = _consec_streak(cond)
    return streak * depth


def rcp_150_range_compression_composite_score(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Composite: mean of TR_pct_rank_252d, BB_width_pct_rank_252d, ATR21/ATR252 (lower = more compressed)."""
    tr = _tr(close, high, low)
    tr_rank = tr.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    m = _rolling_mean(close, _TD_MON)
    s = _rolling_std(close, _TD_MON)
    bw = _safe_div(2.0 * s, m)
    bw_rank = bw.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    atr_ratio = _safe_div(_rolling_mean(tr, _TD_MON), _rolling_mean(tr, _TD_YEAR))
    return (tr_rank + bw_rank + atr_ratio) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

RANGE_COMPRESSION_REGISTRY_076_150 = {
    "rcp_076_tr_collapse_after_expansion_flag": {"inputs": ["close", "high", "low"], "func": rcp_076_tr_collapse_after_expansion_flag},
    "rcp_077_tr_collapse_ratio_after_5d_peak": {"inputs": ["close", "high", "low"], "func": rcp_077_tr_collapse_ratio_after_5d_peak},
    "rcp_078_tr_collapse_ratio_after_21d_peak": {"inputs": ["close", "high", "low"], "func": rcp_078_tr_collapse_ratio_after_21d_peak},
    "rcp_079_tr_collapse_ratio_after_63d_peak": {"inputs": ["close", "high", "low"], "func": rcp_079_tr_collapse_ratio_after_63d_peak},
    "rcp_080_days_since_tr_5d_peak": {"inputs": ["close", "high", "low"], "func": rcp_080_days_since_tr_5d_peak},
    "rcp_081_days_since_tr_21d_peak": {"inputs": ["close", "high", "low"], "func": rcp_081_days_since_tr_21d_peak},
    "rcp_082_expand_then_collapse_score_21d": {"inputs": ["close", "high", "low"], "func": rcp_082_expand_then_collapse_score_21d},
    "rcp_083_expand_collapse_ratio_21d_vs_252d": {"inputs": ["close", "high", "low"], "func": rcp_083_expand_collapse_ratio_21d_vs_252d},
    "rcp_084_atr_decline_from_21d_peak_pct": {"inputs": ["close", "high", "low"], "func": rcp_084_atr_decline_from_21d_peak_pct},
    "rcp_085_consec_tr_below_21d_max": {"inputs": ["close", "high", "low"], "func": rcp_085_consec_tr_below_21d_max},
    "rcp_086_vol_during_squeeze_vs_baseline": {"inputs": ["close", "high", "low", "volume"], "func": rcp_086_vol_during_squeeze_vs_baseline},
    "rcp_087_vol_below_avg_on_narrow_day": {"inputs": ["close", "high", "low", "volume"], "func": rcp_087_vol_below_avg_on_narrow_day},
    "rcp_088_consec_low_vol_narrow_days": {"inputs": ["close", "high", "low", "volume"], "func": rcp_088_consec_low_vol_narrow_days},
    "rcp_089_vol_compression_ratio_21d": {"inputs": ["volume"], "func": rcp_089_vol_compression_ratio_21d},
    "rcp_090_low_vol_squeeze_score": {"inputs": ["close", "high", "low", "volume"], "func": rcp_090_low_vol_squeeze_score},
    "rcp_091_vol_decline_during_tr_compression": {"inputs": ["close", "high", "low", "volume"], "func": rcp_091_vol_decline_during_tr_compression},
    "rcp_092_vol_consec_declining_on_narrow_tr": {"inputs": ["close", "high", "low", "volume"], "func": rcp_092_vol_consec_declining_on_narrow_tr},
    "rcp_093_squeeze_vol_pct_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": rcp_093_squeeze_vol_pct_rank_252d},
    "rcp_094_avg_vol_on_nr7_days_21d": {"inputs": ["high", "low", "volume"], "func": rcp_094_avg_vol_on_nr7_days_21d},
    "rcp_095_low_vol_low_tr_days_fraction_63d": {"inputs": ["close", "high", "low", "volume"], "func": rcp_095_low_vol_low_tr_days_fraction_63d},
    "rcp_096_tr_pct_of_close_21d_mean": {"inputs": ["close", "high", "low"], "func": rcp_096_tr_pct_of_close_21d_mean},
    "rcp_097_tr_pct_of_close_63d_mean": {"inputs": ["close", "high", "low"], "func": rcp_097_tr_pct_of_close_63d_mean},
    "rcp_098_tr_pct_of_close_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": rcp_098_tr_pct_of_close_pct_rank_252d},
    "rcp_099_hl_pct_of_close_21d_mean": {"inputs": ["close", "high", "low"], "func": rcp_099_hl_pct_of_close_21d_mean},
    "rcp_100_hl_pct_close_ratio_vs_252d": {"inputs": ["close", "high", "low"], "func": rcp_100_hl_pct_close_ratio_vs_252d},
    "rcp_101_open_close_range_pct_21d": {"inputs": ["close", "open"], "func": rcp_101_open_close_range_pct_21d},
    "rcp_102_open_close_body_ratio_to_hl": {"inputs": ["close", "high", "low", "open"], "func": rcp_102_open_close_body_ratio_to_hl},
    "rcp_103_body_ratio_21d_mean": {"inputs": ["close", "high", "low", "open"], "func": rcp_103_body_ratio_21d_mean},
    "rcp_104_body_ratio_pct_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": rcp_104_body_ratio_pct_rank_252d},
    "rcp_105_wicks_fraction_of_range_21d": {"inputs": ["close", "high", "low", "open"], "func": rcp_105_wicks_fraction_of_range_21d},
    "rcp_106_atr5_vs_atr21_ratio": {"inputs": ["close", "high", "low"], "func": rcp_106_atr5_vs_atr21_ratio},
    "rcp_107_atr5_vs_atr63_ratio": {"inputs": ["close", "high", "low"], "func": rcp_107_atr5_vs_atr63_ratio},
    "rcp_108_atr10_vs_atr21_ratio": {"inputs": ["close", "high", "low"], "func": rcp_108_atr10_vs_atr21_ratio},
    "rcp_109_atr21_decline_from_63d_max": {"inputs": ["close", "high", "low"], "func": rcp_109_atr21_decline_from_63d_max},
    "rcp_110_atr5_decline_from_21d_max": {"inputs": ["close", "high", "low"], "func": rcp_110_atr5_decline_from_21d_max},
    "rcp_111_atr21_below_atr63_flag": {"inputs": ["close", "high", "low"], "func": rcp_111_atr21_below_atr63_flag},
    "rcp_112_consec_atr21_below_atr63": {"inputs": ["close", "high", "low"], "func": rcp_112_consec_atr21_below_atr63},
    "rcp_113_atr21_below_atr252_flag": {"inputs": ["close", "high", "low"], "func": rcp_113_atr21_below_atr252_flag},
    "rcp_114_consec_atr21_below_atr252": {"inputs": ["close", "high", "low"], "func": rcp_114_consec_atr21_below_atr252},
    "rcp_115_atr_compression_composite": {"inputs": ["close", "high", "low"], "func": rcp_115_atr_compression_composite},
    "rcp_116_tr_below_21d_mean_count_63d": {"inputs": ["close", "high", "low"], "func": rcp_116_tr_below_21d_mean_count_63d},
    "rcp_117_tr_below_21d_mean_fraction_252d": {"inputs": ["close", "high", "low"], "func": rcp_117_tr_below_21d_mean_fraction_252d},
    "rcp_118_atr21_at_252d_min_flag": {"inputs": ["close", "high", "low"], "func": rcp_118_atr21_at_252d_min_flag},
    "rcp_119_atr21_at_504d_min_flag": {"inputs": ["close", "high", "low"], "func": rcp_119_atr21_at_504d_min_flag},
    "rcp_120_tr_below_10th_pct_252d_flag": {"inputs": ["close", "high", "low"], "func": rcp_120_tr_below_10th_pct_252d_flag},
    "rcp_121_tr_below_25th_pct_252d_flag": {"inputs": ["close", "high", "low"], "func": rcp_121_tr_below_25th_pct_252d_flag},
    "rcp_122_narrow_day_streak_norm_252d": {"inputs": ["close", "high", "low"], "func": rcp_122_narrow_day_streak_norm_252d},
    "rcp_123_nr4_streak_zscore_252d": {"inputs": ["high", "low"], "func": rcp_123_nr4_streak_zscore_252d},
    "rcp_124_bb_width_min_63d": {"inputs": ["close"], "func": rcp_124_bb_width_min_63d},
    "rcp_125_bb_width_min_252d": {"inputs": ["close"], "func": rcp_125_bb_width_min_252d},
    "rcp_126_atr5_zscore_252d": {"inputs": ["close", "high", "low"], "func": rcp_126_atr5_zscore_252d},
    "rcp_127_atr5_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": rcp_127_atr5_pct_rank_252d},
    "rcp_128_atr63_zscore_252d": {"inputs": ["close", "high", "low"], "func": rcp_128_atr63_zscore_252d},
    "rcp_129_hl_range_zscore_expanding": {"inputs": ["high", "low"], "func": rcp_129_hl_range_zscore_expanding},
    "rcp_130_tr_expanding_zscore": {"inputs": ["close", "high", "low"], "func": rcp_130_tr_expanding_zscore},
    "rcp_131_bb_squeeze_count_63d": {"inputs": ["close", "high", "low"], "func": rcp_131_bb_squeeze_count_63d},
    "rcp_132_bb_squeeze_fraction_252d": {"inputs": ["close", "high", "low"], "func": rcp_132_bb_squeeze_fraction_252d},
    "rcp_133_narrow_range_cluster_score_21d": {"inputs": ["high", "low"], "func": rcp_133_narrow_range_cluster_score_21d},
    "rcp_134_compression_depth_composite_21d": {"inputs": ["close", "high", "low"], "func": rcp_134_compression_depth_composite_21d},
    "rcp_135_coil_score_expanding_zscore": {"inputs": ["close", "high", "low"], "func": rcp_135_coil_score_expanding_zscore},
    "rcp_136_close_near_midpoint_21d_flag": {"inputs": ["close", "high", "low"], "func": rcp_136_close_near_midpoint_21d_flag},
    "rcp_137_close_near_midpoint_count_21d": {"inputs": ["close", "high", "low"], "func": rcp_137_close_near_midpoint_count_21d},
    "rcp_138_high_low_channel_contraction_score": {"inputs": ["close", "high", "low"], "func": rcp_138_high_low_channel_contraction_score},
    "rcp_139_high_low_channel_5d_vs_63d": {"inputs": ["close", "high", "low"], "func": rcp_139_high_low_channel_5d_vs_63d},
    "rcp_140_high_low_channel_21d_vs_63d": {"inputs": ["close", "high", "low"], "func": rcp_140_high_low_channel_21d_vs_63d},
    "rcp_141_upper_shadow_compression_21d": {"inputs": ["close", "high", "low", "open"], "func": rcp_141_upper_shadow_compression_21d},
    "rcp_142_lower_shadow_compression_21d": {"inputs": ["close", "high", "low", "open"], "func": rcp_142_lower_shadow_compression_21d},
    "rcp_143_wick_compression_pct_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": rcp_143_wick_compression_pct_rank_252d},
    "rcp_144_tr_contraction_speed_5d": {"inputs": ["close", "high", "low"], "func": rcp_144_tr_contraction_speed_5d},
    "rcp_145_tr_contraction_speed_21d": {"inputs": ["close", "high", "low"], "func": rcp_145_tr_contraction_speed_21d},
    "rcp_146_squeeze_distress_index": {"inputs": ["close", "high", "low", "volume"], "func": rcp_146_squeeze_distress_index},
    "rcp_147_nr4_bb_keltner_triple_squeeze": {"inputs": ["close", "high", "low"], "func": rcp_147_nr4_bb_keltner_triple_squeeze},
    "rcp_148_compression_after_high_vol_flag": {"inputs": ["close", "high", "low", "volume"], "func": rcp_148_compression_after_high_vol_flag},
    "rcp_149_squeeze_duration_weighted_depth": {"inputs": ["close", "high", "low"], "func": rcp_149_squeeze_duration_weighted_depth},
    "rcp_150_range_compression_composite_score": {"inputs": ["close", "high", "low"], "func": rcp_150_range_compression_composite_score},
}
