"""
58_trading_intensity — Base Features 076-150
Domain: trade-frequency / activity-intensity proxies — how busy the tape is
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — active vs lull regimes, price-discovery intensity
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _active_day(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True when the day moved: close != prior close OR high != low."""
    moved_close = close != close.shift(1)
    has_range   = (high - low) > 0
    return (moved_close | has_range).astype(float)


def _range_pct(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Intraday range as fraction of prior close."""
    return _safe_div(high - low, close.shift(1).replace(0, np.nan))


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi   = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        num  = ((xi - xi_m) * (x - x_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Range-expansion intensity (price discovery breadth) ---

def tin_076_range_expansion_day_frac_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of 21 days where range > 21-day median range (expanded discovery)."""
    rng    = high - low
    med21  = _rolling_median(rng, _TD_MON)
    cond   = (rng > med21).astype(float)
    return _rolling_sum(cond, _TD_MON) / _TD_MON


def tin_077_range_expansion_day_frac_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of 63 days where range > 63-day median range."""
    rng   = high - low
    med63 = _rolling_median(rng, _TD_QTR)
    cond  = (rng > med63).astype(float)
    return _rolling_sum(cond, _TD_QTR) / _TD_QTR


def tin_078_range_expansion_day_frac_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of 252 days where range > 252-day median range."""
    rng    = high - low
    med252 = _rolling_median(rng, _TD_YEAR)
    cond   = (rng > med252).astype(float)
    return _rolling_sum(cond, _TD_YEAR) / _TD_YEAR


def tin_079_range_expansion_count_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of last 5 days with above-median range (recent discovery intensity)."""
    rng   = high - low
    med63 = _rolling_median(rng, _TD_QTR)
    cond  = (rng > med63).astype(float)
    return _rolling_sum(cond, _TD_WEEK)


def tin_080_range_expansion_frac_5d_vs_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day range-expansion fraction divided by 252-day average."""
    rng   = high - low
    med63 = _rolling_median(rng, _TD_QTR)
    cond  = (rng > med63).astype(float)
    f5    = _rolling_sum(cond, _TD_WEEK) / _TD_WEEK
    f252  = _rolling_mean(f5, _TD_YEAR)
    return _safe_div(f5, f252)


def tin_081_high_range_and_high_vol_frac_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21 days with both above-median range AND above-avg volume."""
    rng    = high - low
    med_r  = _rolling_median(rng, _TD_QTR)
    avg_v  = _rolling_mean(volume, _TD_MON)
    cond   = ((rng > med_r) & (volume > avg_v)).astype(float)
    return _rolling_sum(cond, _TD_MON) / _TD_MON


def tin_082_high_range_and_high_vol_frac_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63 days with both above-median range AND above-avg volume."""
    rng   = high - low
    med_r = _rolling_median(rng, _TD_QTR)
    avg_v = _rolling_mean(volume, _TD_MON)
    cond  = ((rng > med_r) & (volume > avg_v)).astype(float)
    return _rolling_sum(cond, _TD_QTR) / _TD_QTR


def tin_083_range_contraction_frac_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of 21 days with below-25th-pctile range (narrow-range lull)."""
    rng   = high - low
    p25   = rng.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    cond  = (rng < p25).astype(float)
    return _rolling_sum(cond, _TD_MON) / _TD_MON


def tin_084_range_contraction_frac_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of 63 days with below-25th-pctile range."""
    rng  = high - low
    p25  = rng.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    cond = (rng < p25).astype(float)
    return _rolling_sum(cond, _TD_QTR) / _TD_QTR


def tin_085_expansion_contraction_ratio_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of expansion-day count to contraction-day count over 63 days."""
    rng    = high - low
    med63  = _rolling_median(rng, _TD_QTR)
    p25    = rng.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    exp_c  = _rolling_sum((rng > med63).astype(float), _TD_QTR)
    con_c  = _rolling_sum((rng < p25).astype(float), _TD_QTR)
    return _safe_div(exp_c, con_c.replace(0, np.nan))


# --- Group I (086-095): Open-to-close activity signals ---

def tin_086_body_vs_range_frac_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Mean ratio of candle body to full range over 21 days (directional commitment)."""
    body  = (close - open).abs()
    rng   = (high - low).replace(0, np.nan)
    ratio = _safe_div(body, rng)
    return _rolling_mean(ratio, _TD_MON)


def tin_087_body_vs_range_frac_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Mean ratio of candle body to full range over 63 days."""
    body  = (close - open).abs()
    rng   = (high - low).replace(0, np.nan)
    ratio = _safe_div(body, rng)
    return _rolling_mean(ratio, _TD_QTR)


def tin_088_large_body_day_frac_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 21 days where body > 50% of range (strong directional session)."""
    body  = (close - open).abs()
    rng   = (high - low).replace(0, np.nan)
    ratio = _safe_div(body, rng)
    cond  = (ratio > 0.5).astype(float)
    return _rolling_sum(cond, _TD_MON) / _TD_MON


def tin_089_large_body_day_frac_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 63 days where body > 50% of range."""
    body  = (close - open).abs()
    rng   = (high - low).replace(0, np.nan)
    ratio = _safe_div(body, rng)
    cond  = (ratio > 0.5).astype(float)
    return _rolling_sum(cond, _TD_QTR) / _TD_QTR


def tin_090_doji_day_frac_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 21 days where body < 10% of range (doji / indecision, low activity)."""
    body  = (close - open).abs()
    rng   = (high - low).replace(0, np.nan)
    ratio = _safe_div(body, rng)
    cond  = (ratio < 0.1).astype(float)
    return _rolling_sum(cond, _TD_MON) / _TD_MON


def tin_091_doji_day_frac_63d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 63 days where body < 10% of range (indecision fraction)."""
    body  = (close - open).abs()
    rng   = (high - low).replace(0, np.nan)
    ratio = _safe_div(body, rng)
    cond  = (ratio < 0.1).astype(float)
    return _rolling_sum(cond, _TD_QTR) / _TD_QTR


def tin_092_gap_open_frac_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 21 days where open gapped away from prior close (activity signal)."""
    gap  = (open - close.shift(1)).abs()
    pct  = _safe_div(gap, close.shift(1).replace(0, np.nan))
    cond = (pct > 0.005).astype(float)
    return _rolling_sum(cond, _TD_MON) / _TD_MON


def tin_093_gap_open_frac_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 63 days where open gapped > 0.5% from prior close."""
    gap  = (open - close.shift(1)).abs()
    pct  = _safe_div(gap, close.shift(1).replace(0, np.nan))
    cond = (pct > 0.005).astype(float)
    return _rolling_sum(cond, _TD_QTR) / _TD_QTR


def tin_094_large_gap_frac_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 21 days with gap > 1% of prior close (high pre-open activity)."""
    gap  = (open - close.shift(1)).abs()
    pct  = _safe_div(gap, close.shift(1).replace(0, np.nan))
    cond = (pct > 0.01).astype(float)
    return _rolling_sum(cond, _TD_MON) / _TD_MON


def tin_095_gap_fill_frac_21d(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of gapped days that fill the gap intraday over 21 days."""
    gap_up   = open > close.shift(1)
    gap_dn   = open < close.shift(1)
    fill_up  = gap_up & (low <= close.shift(1))
    fill_dn  = gap_dn & (high >= close.shift(1))
    filled   = (fill_up | fill_dn).astype(float)
    gapped   = (gap_up | gap_dn).astype(float)
    sum_fill = _rolling_sum(filled, _TD_MON)
    sum_gap  = _rolling_sum(gapped, _TD_MON).replace(0, np.nan)
    return _safe_div(sum_fill, sum_gap)


# --- Group J (096-105): Volume-rate-of-change intensity ---

def tin_096_vol_roc_5d(volume: pd.Series) -> pd.Series:
    """5-day rate of change of volume (acceleration of trade activity)."""
    return _safe_div(volume - volume.shift(_TD_WEEK), volume.shift(_TD_WEEK).replace(0, np.nan))


def tin_097_vol_roc_21d(volume: pd.Series) -> pd.Series:
    """21-day rate of change of volume."""
    return _safe_div(volume - volume.shift(_TD_MON), volume.shift(_TD_MON).replace(0, np.nan))


def tin_098_vol_roc_63d(volume: pd.Series) -> pd.Series:
    """63-day rate of change of volume."""
    return _safe_div(volume - volume.shift(_TD_QTR), volume.shift(_TD_QTR).replace(0, np.nan))


def tin_099_vol_roc_pos_frac_21d(volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days with positive 5-day volume rate of change."""
    roc5 = _safe_div(volume - volume.shift(_TD_WEEK), volume.shift(_TD_WEEK).replace(0, np.nan))
    cond = (roc5 > 0).astype(float)
    return _rolling_sum(cond, _TD_MON) / _TD_MON


def tin_100_vol_roc_pos_frac_63d(volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days with positive 5-day volume rate of change."""
    roc5 = _safe_div(volume - volume.shift(_TD_WEEK), volume.shift(_TD_WEEK).replace(0, np.nan))
    cond = (roc5 > 0).astype(float)
    return _rolling_sum(cond, _TD_QTR) / _TD_QTR


def tin_101_vol_acceleration_5d(volume: pd.Series) -> pd.Series:
    """5-day diff of 5-day volume ROC (second derivative of volume)."""
    roc5 = _safe_div(volume - volume.shift(_TD_WEEK), volume.shift(_TD_WEEK).replace(0, np.nan))
    return roc5.diff(_TD_WEEK)


def tin_102_vol_roc_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 5-day volume ROC relative to 252-day distribution."""
    roc5 = _safe_div(volume - volume.shift(_TD_WEEK), volume.shift(_TD_WEEK).replace(0, np.nan))
    m    = _rolling_mean(roc5, _TD_YEAR)
    s    = _rolling_std(roc5, _TD_YEAR)
    return _safe_div(roc5 - m, s)


def tin_103_rising_vol_consec_streak(volume: pd.Series) -> pd.Series:
    """Current consecutive streak of volume higher than prior day (activity ramp)."""
    cond = volume > volume.shift(1)
    return _consec_streak(cond)


def tin_104_falling_vol_consec_streak(volume: pd.Series) -> pd.Series:
    """Current consecutive streak of volume lower than prior day (activity fade)."""
    cond = volume < volume.shift(1)
    return _consec_streak(cond)


def tin_105_vol_trend_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of log-volume over trailing 21 days."""
    log_v = _log_safe(volume)
    return _linslope(log_v, _TD_MON)


# --- Group K (106-115): Intraday intensity (range momentum) ---

def tin_106_range_roc_5d(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day rate of change of daily range (expansion momentum)."""
    rng = high - low
    return _safe_div(rng - rng.shift(_TD_WEEK), rng.shift(_TD_WEEK).replace(0, np.nan))


def tin_107_range_roc_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day rate of change of daily range."""
    rng = high - low
    return _safe_div(rng - rng.shift(_TD_MON), rng.shift(_TD_MON).replace(0, np.nan))


def tin_108_range_trend_slope_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of daily range over trailing 21 days."""
    rng = high - low
    return _linslope(rng, _TD_MON)


def tin_109_range_trend_slope_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of daily range over trailing 63 days."""
    rng = high - low
    return _linslope(rng, _TD_QTR)


def tin_110_range_zscore_21d_vs_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 21-day mean range relative to 252-day distribution of 21d means."""
    rng   = high - low
    m21   = _rolling_mean(rng, _TD_MON)
    m252  = _rolling_mean(m21, _TD_YEAR)
    s252  = _rolling_std(m21, _TD_YEAR)
    return _safe_div(m21 - m252, s252)


def tin_111_range_pct_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of percentage range (range/price) vs 252-day history."""
    rng_p = _range_pct(close, high, low)
    m     = _rolling_mean(rng_p, _TD_YEAR)
    s     = _rolling_std(rng_p, _TD_YEAR)
    return _safe_div(rng_p - m, s)


def tin_112_expanding_range_day_frac_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of 21 days where range > prior day range."""
    rng  = high - low
    cond = (rng > rng.shift(1)).astype(float)
    return _rolling_sum(cond, _TD_MON) / _TD_MON


def tin_113_contracting_range_day_frac_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of 21 days where range < prior day range."""
    rng  = high - low
    cond = (rng < rng.shift(1)).astype(float)
    return _rolling_sum(cond, _TD_MON) / _TD_MON


def tin_114_range_above_atr21_frac_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of 21 days where range exceeds 21-day average range."""
    rng    = high - low
    atr21  = _rolling_mean(rng, _TD_MON)
    cond   = (rng > atr21).astype(float)
    return _rolling_sum(cond, _TD_MON) / _TD_MON


def tin_115_range_above_atr63_frac_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of 63 days where range exceeds 63-day average range."""
    rng   = high - low
    atr63 = _rolling_mean(rng, _TD_QTR)
    cond  = (rng > atr63).astype(float)
    return _rolling_sum(cond, _TD_QTR) / _TD_QTR


# --- Group L (116-125): Intensity interaction (volume + range combined) ---

def tin_116_vxr_score_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume times range, normalized and averaged over 21 days (VxR intensity)."""
    rng   = high - low
    vxr   = volume * rng
    return _rolling_mean(vxr, _TD_MON)


def tin_117_vxr_score_63d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume times range, normalized and averaged over 63 days."""
    rng  = high - low
    vxr  = volume * rng
    return _rolling_mean(vxr, _TD_QTR)


def tin_118_vxr_zscore_252d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of daily VxR relative to 252-day distribution."""
    rng = high - low
    vxr = volume * rng
    m   = _rolling_mean(vxr, _TD_YEAR)
    s   = _rolling_std(vxr, _TD_YEAR)
    return _safe_div(vxr - m, s)


def tin_119_vxr_pct_rank_252d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of daily VxR within 252-day distribution."""
    rng = high - low
    vxr = volume * rng
    return vxr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def tin_120_vxr_21d_vs_252d_ratio(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day mean VxR to 252-day mean VxR."""
    rng   = high - low
    vxr   = volume * rng
    m21   = _rolling_mean(vxr, _TD_MON)
    m252  = _rolling_mean(vxr, _TD_YEAR)
    return _safe_div(m21, m252)


def tin_121_high_vxr_day_frac_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21 days with VxR above 252-day mean (intense sessions)."""
    rng    = high - low
    vxr    = volume * rng
    avg252 = _rolling_mean(vxr, _TD_YEAR)
    cond   = (vxr > avg252).astype(float)
    return _rolling_sum(cond, _TD_MON) / _TD_MON


def tin_122_high_vxr_day_frac_63d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63 days with VxR above 252-day mean."""
    rng    = high - low
    vxr    = volume * rng
    avg252 = _rolling_mean(vxr, _TD_YEAR)
    cond   = (vxr > avg252).astype(float)
    return _rolling_sum(cond, _TD_QTR) / _TD_QTR


def tin_123_vxr_trend_slope_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of VxR over trailing 21 days."""
    rng = high - low
    vxr = volume * rng
    return _linslope(vxr, _TD_MON)


def tin_124_vxr_ewm21_vs_ewm63(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """EMA21 minus EMA63 of VxR (momentum of intensity)."""
    rng = high - low
    vxr = volume * rng
    e21 = _ewm_mean(vxr, _TD_MON)
    e63 = _ewm_mean(vxr, _TD_QTR)
    return e21 - e63


def tin_125_vxr_expanding_rank(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of VxR (all-history extremity of activity)."""
    rng = high - low
    vxr = volume * rng
    return vxr.expanding(min_periods=5).rank(pct=True)


# --- Group M (126-135): Session-count-based frequency metrics ---

def tin_126_active_sessions_per_week_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average active sessions per 5-day period over trailing 21 days."""
    act   = _active_day(close, high, low)
    sum5  = _rolling_sum(act, _TD_WEEK)
    return _rolling_mean(sum5, _TD_MON)


def tin_127_active_sessions_per_week_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average active sessions per 5-day period over trailing 63 days."""
    act  = _active_day(close, high, low)
    sum5 = _rolling_sum(act, _TD_WEEK)
    return _rolling_mean(sum5, _TD_QTR)


def tin_128_vol_spike_count_21d(volume: pd.Series) -> pd.Series:
    """Count of volume spikes (> 2x 21-day mean) in trailing 21 days."""
    avg  = _rolling_mean(volume, _TD_MON)
    cond = (volume > 2.0 * avg).astype(float)
    return _rolling_sum(cond, _TD_MON)


def tin_129_vol_spike_count_63d(volume: pd.Series) -> pd.Series:
    """Count of volume spikes (> 2x 21-day mean) in trailing 63 days."""
    avg  = _rolling_mean(volume, _TD_MON)
    cond = (volume > 2.0 * avg).astype(float)
    return _rolling_sum(cond, _TD_QTR)


def tin_130_vol_spike_count_252d(volume: pd.Series) -> pd.Series:
    """Count of volume spikes (> 2x 21-day mean) in trailing 252 days."""
    avg  = _rolling_mean(volume, _TD_MON)
    cond = (volume > 2.0 * avg).astype(float)
    return _rolling_sum(cond, _TD_YEAR)


def tin_131_vol_spike_freq_21d_vs_252d(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day spike count to 252-day average spike count."""
    avg   = _rolling_mean(volume, _TD_MON)
    cond  = (volume > 2.0 * avg).astype(float)
    c21   = _rolling_sum(cond, _TD_MON)
    c252  = _rolling_mean(c21, _TD_YEAR)
    return _safe_div(c21, c252)


def tin_132_range_spike_count_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of range spikes (> 2x 21-day mean range) in trailing 21 days."""
    rng  = high - low
    avg  = _rolling_mean(rng, _TD_MON)
    cond = (rng > 2.0 * avg).astype(float)
    return _rolling_sum(cond, _TD_MON)


def tin_133_range_spike_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of range spikes (> 2x 21-day mean range) in trailing 63 days."""
    rng  = high - low
    avg  = _rolling_mean(rng, _TD_MON)
    cond = (rng > 2.0 * avg).astype(float)
    return _rolling_sum(cond, _TD_QTR)


def tin_134_both_vol_and_range_spike_frac_63d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63 days with simultaneous volume AND range spikes (double intensity)."""
    rng     = high - low
    avg_r   = _rolling_mean(rng, _TD_MON)
    avg_v   = _rolling_mean(volume, _TD_MON)
    cond    = ((rng > 2.0 * avg_r) & (volume > 2.0 * avg_v)).astype(float)
    return _rolling_sum(cond, _TD_QTR) / _TD_QTR


def tin_135_vol_below_25pct_count_21d(volume: pd.Series) -> pd.Series:
    """Count of 21 days where volume below 25th-pctile of trailing 63d (deep lull)."""
    p25  = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    cond = (volume < p25).astype(float)
    return _rolling_sum(cond, _TD_MON)


# --- Group N (136-145): Activity intensity Z-scores and ranks ---

def tin_136_active_day_count_21d_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 21-day active-day count in 252-day distribution."""
    act  = _active_day(close, high, low)
    c21  = _rolling_sum(act, _TD_MON)
    m    = _rolling_mean(c21, _TD_YEAR)
    s    = _rolling_std(c21, _TD_YEAR)
    return _safe_div(c21 - m, s)


def tin_137_vol_spike_count_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day volume-spike count in 252-day distribution."""
    avg  = _rolling_mean(volume, _TD_MON)
    cond = (volume > 2.0 * avg).astype(float)
    c21  = _rolling_sum(cond, _TD_MON)
    m    = _rolling_mean(c21, _TD_YEAR)
    s    = _rolling_std(c21, _TD_YEAR)
    return _safe_div(c21 - m, s)


def tin_138_burst_lull_ratio_pct_rank_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day burst/lull ratio in 252-day distribution."""
    avg  = _rolling_mean(volume, _TD_MON)
    high = _rolling_sum((volume > avg).astype(float), _TD_MON)
    low  = _rolling_sum((volume < avg).astype(float), _TD_MON)
    r21  = _safe_div(high, low.replace(0, np.nan))
    return r21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def tin_139_range_expansion_frac_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21-day range-expansion fraction in 252-day distribution."""
    rng   = high - low
    med63 = _rolling_median(rng, _TD_QTR)
    cond  = (rng > med63).astype(float)
    f21   = _rolling_sum(cond, _TD_MON) / _TD_MON
    return f21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def tin_140_discovery_event_count_21d_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of 21-day price-discovery event count in 252-day distribution."""
    rng    = high - low
    med_r  = _rolling_median(rng, _TD_QTR)
    events = ((close != close.shift(1)) & (rng > med_r)).astype(float)
    c21    = _rolling_sum(events, _TD_MON)
    m      = _rolling_mean(c21, _TD_YEAR)
    s      = _rolling_std(c21, _TD_YEAR)
    return _safe_div(c21 - m, s)


def tin_141_vxr_21d_pct_rank_252d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day mean VxR in 252-day distribution."""
    rng  = high - low
    vxr  = volume * rng
    m21  = _rolling_mean(vxr, _TD_MON)
    return m21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def tin_142_activity_composite_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of composite activity signal (active-day * vol_norm) over 252d."""
    act     = _active_day(close, high, low)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_n   = _safe_div(volume, avg_vol.replace(0, np.nan))
    signal  = _rolling_mean(act * vol_n, _TD_MON)
    return signal.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def tin_143_regime_transition_freq_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-day regime-transition count in 252-day distribution."""
    avg    = _rolling_mean(volume, _TD_MON)
    regime = ((_active_day(close, high, low) > 0) & (volume > avg)).astype(int)
    trans  = (regime != regime.shift(1)).astype(float)
    c21    = _rolling_sum(trans, _TD_MON)
    m      = _rolling_mean(c21, _TD_YEAR)
    s      = _rolling_std(c21, _TD_YEAR)
    return _safe_div(c21 - m, s)


def tin_144_vol_trend_slope_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day log-volume OLS slope in 252-day distribution."""
    log_v = _log_safe(volume)
    slp21 = _linslope(log_v, _TD_MON)
    m     = _rolling_mean(slp21, _TD_YEAR)
    s     = _rolling_std(slp21, _TD_YEAR)
    return _safe_div(slp21 - m, s)


def tin_145_expanding_active_frac_rank(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding percentile rank of 21-day active-day fraction (all-history extremity)."""
    act = _active_day(close, high, low)
    f21 = _rolling_sum(act, _TD_MON) / _TD_MON
    return f21.expanding(min_periods=5).rank(pct=True)


# --- Group O (146-150): Composite multi-signal intensity indicators ---

def tin_146_intensity_score_vol_range_active(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Combined z-score: active-day frac + vol/range + VxR (full intensity composite)."""
    act    = _active_day(close, high, low)
    f21    = _rolling_mean(act, _TD_MON)
    f21_z  = _safe_div(f21 - _rolling_mean(f21, _TD_YEAR), _rolling_std(f21, _TD_YEAR))

    rng    = (high - low).replace(0, np.nan)
    vpr    = _safe_div(volume, rng)
    vpr21  = _rolling_mean(vpr, _TD_MON)
    vpr_z  = _safe_div(vpr21 - _rolling_mean(vpr21, _TD_YEAR), _rolling_std(vpr21, _TD_YEAR))

    vxr    = volume * (high - low)
    vxr21  = _rolling_mean(vxr, _TD_MON)
    vxr_z  = _safe_div(vxr21 - _rolling_mean(vxr21, _TD_YEAR), _rolling_std(vxr21, _TD_YEAR))

    return (f21_z + vpr_z + vxr_z) / 3.0


def tin_147_activity_lull_divergence_score(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Score = active-regime frac minus lull-regime frac over 21 days."""
    avg   = _rolling_mean(volume, _TD_MON)
    act   = ((_active_day(close, high, low) > 0) & (volume > avg)).astype(float)
    lull  = ((_active_day(close, high, low) == 0) | (volume < 0.5 * avg)).astype(float)
    f_act  = _rolling_sum(act, _TD_MON) / _TD_MON
    f_lull = _rolling_sum(lull, _TD_MON) / _TD_MON
    return f_act - f_lull


def tin_148_intensity_trend_composite_slope(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day full intensity composite score over 63 days."""
    act    = _active_day(close, high, low)
    f21    = _rolling_mean(act, _TD_MON)
    f21_z  = _safe_div(f21 - _rolling_mean(f21, _TD_YEAR), _rolling_std(f21, _TD_YEAR))

    rng    = (high - low).replace(0, np.nan)
    vpr    = _safe_div(volume, rng)
    vpr21  = _rolling_mean(vpr, _TD_MON)
    vpr_z  = _safe_div(vpr21 - _rolling_mean(vpr21, _TD_YEAR), _rolling_std(vpr21, _TD_YEAR))

    vxr    = volume * (high - low)
    vxr21  = _rolling_mean(vxr, _TD_MON)
    vxr_z  = _safe_div(vxr21 - _rolling_mean(vxr21, _TD_YEAR), _rolling_std(vxr21, _TD_YEAR))

    composite = (f21_z + vpr_z + vxr_z) / 3.0
    return _linslope(composite, _TD_QTR)


def tin_149_vol_range_divergence_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score divergence: vol zscore minus range zscore (intensity decoupling)."""
    rng   = high - low
    v_z   = _safe_div(volume - _rolling_mean(volume, _TD_YEAR), _rolling_std(volume, _TD_YEAR))
    r_z   = _safe_div(rng - _rolling_mean(rng, _TD_YEAR), _rolling_std(rng, _TD_YEAR))
    return _rolling_mean(v_z - r_z, _TD_MON)


def tin_150_activity_intensity_regime_score(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Smoothed regime score: ewm21 of full composite minus ewm63 of full composite."""
    act   = _active_day(close, high, low)
    f21   = _rolling_mean(act, _TD_MON)
    f21_z = _safe_div(f21 - _rolling_mean(f21, _TD_YEAR), _rolling_std(f21, _TD_YEAR))

    rng   = (high - low).replace(0, np.nan)
    vpr   = _safe_div(volume, rng)
    vpr21 = _rolling_mean(vpr, _TD_MON)
    vpr_z = _safe_div(vpr21 - _rolling_mean(vpr21, _TD_YEAR), _rolling_std(vpr21, _TD_YEAR))

    vxr   = volume * (high - low)
    vxr21 = _rolling_mean(vxr, _TD_MON)
    vxr_z = _safe_div(vxr21 - _rolling_mean(vxr21, _TD_YEAR), _rolling_std(vxr21, _TD_YEAR))

    comp  = (f21_z + vpr_z + vxr_z) / 3.0
    return _ewm_mean(comp, _TD_MON) - _ewm_mean(comp, _TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

TRADING_INTENSITY_REGISTRY_076_150 = {
    "tin_076_range_expansion_day_frac_21d": {"inputs": ["close", "high", "low"], "func": tin_076_range_expansion_day_frac_21d},
    "tin_077_range_expansion_day_frac_63d": {"inputs": ["close", "high", "low"], "func": tin_077_range_expansion_day_frac_63d},
    "tin_078_range_expansion_day_frac_252d": {"inputs": ["close", "high", "low"], "func": tin_078_range_expansion_day_frac_252d},
    "tin_079_range_expansion_count_5d": {"inputs": ["close", "high", "low"], "func": tin_079_range_expansion_count_5d},
    "tin_080_range_expansion_frac_5d_vs_252d": {"inputs": ["close", "high", "low"], "func": tin_080_range_expansion_frac_5d_vs_252d},
    "tin_081_high_range_and_high_vol_frac_21d": {"inputs": ["close", "high", "low", "volume"], "func": tin_081_high_range_and_high_vol_frac_21d},
    "tin_082_high_range_and_high_vol_frac_63d": {"inputs": ["close", "high", "low", "volume"], "func": tin_082_high_range_and_high_vol_frac_63d},
    "tin_083_range_contraction_frac_21d": {"inputs": ["close", "high", "low"], "func": tin_083_range_contraction_frac_21d},
    "tin_084_range_contraction_frac_63d": {"inputs": ["close", "high", "low"], "func": tin_084_range_contraction_frac_63d},
    "tin_085_expansion_contraction_ratio_63d": {"inputs": ["close", "high", "low"], "func": tin_085_expansion_contraction_ratio_63d},
    "tin_086_body_vs_range_frac_21d": {"inputs": ["close", "high", "low", "open"], "func": tin_086_body_vs_range_frac_21d},
    "tin_087_body_vs_range_frac_63d": {"inputs": ["close", "high", "low", "open"], "func": tin_087_body_vs_range_frac_63d},
    "tin_088_large_body_day_frac_21d": {"inputs": ["close", "high", "low", "open"], "func": tin_088_large_body_day_frac_21d},
    "tin_089_large_body_day_frac_63d": {"inputs": ["close", "high", "low", "open"], "func": tin_089_large_body_day_frac_63d},
    "tin_090_doji_day_frac_21d": {"inputs": ["close", "high", "low", "open"], "func": tin_090_doji_day_frac_21d},
    "tin_091_doji_day_frac_63d": {"inputs": ["close", "high", "low", "open"], "func": tin_091_doji_day_frac_63d},
    "tin_092_gap_open_frac_21d": {"inputs": ["close", "open"], "func": tin_092_gap_open_frac_21d},
    "tin_093_gap_open_frac_63d": {"inputs": ["close", "open"], "func": tin_093_gap_open_frac_63d},
    "tin_094_large_gap_frac_21d": {"inputs": ["close", "open"], "func": tin_094_large_gap_frac_21d},
    "tin_095_gap_fill_frac_21d": {"inputs": ["close", "high", "low", "open"], "func": tin_095_gap_fill_frac_21d},
    "tin_096_vol_roc_5d": {"inputs": ["volume"], "func": tin_096_vol_roc_5d},
    "tin_097_vol_roc_21d": {"inputs": ["volume"], "func": tin_097_vol_roc_21d},
    "tin_098_vol_roc_63d": {"inputs": ["volume"], "func": tin_098_vol_roc_63d},
    "tin_099_vol_roc_pos_frac_21d": {"inputs": ["volume"], "func": tin_099_vol_roc_pos_frac_21d},
    "tin_100_vol_roc_pos_frac_63d": {"inputs": ["volume"], "func": tin_100_vol_roc_pos_frac_63d},
    "tin_101_vol_acceleration_5d": {"inputs": ["volume"], "func": tin_101_vol_acceleration_5d},
    "tin_102_vol_roc_zscore_252d": {"inputs": ["volume"], "func": tin_102_vol_roc_zscore_252d},
    "tin_103_rising_vol_consec_streak": {"inputs": ["volume"], "func": tin_103_rising_vol_consec_streak},
    "tin_104_falling_vol_consec_streak": {"inputs": ["volume"], "func": tin_104_falling_vol_consec_streak},
    "tin_105_vol_trend_slope_21d": {"inputs": ["volume"], "func": tin_105_vol_trend_slope_21d},
    "tin_106_range_roc_5d": {"inputs": ["high", "low"], "func": tin_106_range_roc_5d},
    "tin_107_range_roc_21d": {"inputs": ["high", "low"], "func": tin_107_range_roc_21d},
    "tin_108_range_trend_slope_21d": {"inputs": ["high", "low"], "func": tin_108_range_trend_slope_21d},
    "tin_109_range_trend_slope_63d": {"inputs": ["high", "low"], "func": tin_109_range_trend_slope_63d},
    "tin_110_range_zscore_21d_vs_252d": {"inputs": ["high", "low"], "func": tin_110_range_zscore_21d_vs_252d},
    "tin_111_range_pct_zscore_252d": {"inputs": ["close", "high", "low"], "func": tin_111_range_pct_zscore_252d},
    "tin_112_expanding_range_day_frac_21d": {"inputs": ["high", "low"], "func": tin_112_expanding_range_day_frac_21d},
    "tin_113_contracting_range_day_frac_21d": {"inputs": ["high", "low"], "func": tin_113_contracting_range_day_frac_21d},
    "tin_114_range_above_atr21_frac_21d": {"inputs": ["high", "low"], "func": tin_114_range_above_atr21_frac_21d},
    "tin_115_range_above_atr63_frac_63d": {"inputs": ["high", "low"], "func": tin_115_range_above_atr63_frac_63d},
    "tin_116_vxr_score_21d": {"inputs": ["high", "low", "volume"], "func": tin_116_vxr_score_21d},
    "tin_117_vxr_score_63d": {"inputs": ["high", "low", "volume"], "func": tin_117_vxr_score_63d},
    "tin_118_vxr_zscore_252d": {"inputs": ["high", "low", "volume"], "func": tin_118_vxr_zscore_252d},
    "tin_119_vxr_pct_rank_252d": {"inputs": ["high", "low", "volume"], "func": tin_119_vxr_pct_rank_252d},
    "tin_120_vxr_21d_vs_252d_ratio": {"inputs": ["high", "low", "volume"], "func": tin_120_vxr_21d_vs_252d_ratio},
    "tin_121_high_vxr_day_frac_21d": {"inputs": ["high", "low", "volume"], "func": tin_121_high_vxr_day_frac_21d},
    "tin_122_high_vxr_day_frac_63d": {"inputs": ["high", "low", "volume"], "func": tin_122_high_vxr_day_frac_63d},
    "tin_123_vxr_trend_slope_21d": {"inputs": ["high", "low", "volume"], "func": tin_123_vxr_trend_slope_21d},
    "tin_124_vxr_ewm21_vs_ewm63": {"inputs": ["high", "low", "volume"], "func": tin_124_vxr_ewm21_vs_ewm63},
    "tin_125_vxr_expanding_rank": {"inputs": ["high", "low", "volume"], "func": tin_125_vxr_expanding_rank},
    "tin_126_active_sessions_per_week_21d": {"inputs": ["close", "high", "low"], "func": tin_126_active_sessions_per_week_21d},
    "tin_127_active_sessions_per_week_63d": {"inputs": ["close", "high", "low"], "func": tin_127_active_sessions_per_week_63d},
    "tin_128_vol_spike_count_21d": {"inputs": ["volume"], "func": tin_128_vol_spike_count_21d},
    "tin_129_vol_spike_count_63d": {"inputs": ["volume"], "func": tin_129_vol_spike_count_63d},
    "tin_130_vol_spike_count_252d": {"inputs": ["volume"], "func": tin_130_vol_spike_count_252d},
    "tin_131_vol_spike_freq_21d_vs_252d": {"inputs": ["volume"], "func": tin_131_vol_spike_freq_21d_vs_252d},
    "tin_132_range_spike_count_21d": {"inputs": ["high", "low"], "func": tin_132_range_spike_count_21d},
    "tin_133_range_spike_count_63d": {"inputs": ["high", "low"], "func": tin_133_range_spike_count_63d},
    "tin_134_both_vol_and_range_spike_frac_63d": {"inputs": ["high", "low", "volume"], "func": tin_134_both_vol_and_range_spike_frac_63d},
    "tin_135_vol_below_25pct_count_21d": {"inputs": ["volume"], "func": tin_135_vol_below_25pct_count_21d},
    "tin_136_active_day_count_21d_zscore_252d": {"inputs": ["close", "high", "low"], "func": tin_136_active_day_count_21d_zscore_252d},
    "tin_137_vol_spike_count_21d_zscore_252d": {"inputs": ["volume"], "func": tin_137_vol_spike_count_21d_zscore_252d},
    "tin_138_burst_lull_ratio_pct_rank_252d": {"inputs": ["close", "volume"], "func": tin_138_burst_lull_ratio_pct_rank_252d},
    "tin_139_range_expansion_frac_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": tin_139_range_expansion_frac_pct_rank_252d},
    "tin_140_discovery_event_count_21d_zscore_252d": {"inputs": ["close", "high", "low"], "func": tin_140_discovery_event_count_21d_zscore_252d},
    "tin_141_vxr_21d_pct_rank_252d": {"inputs": ["high", "low", "volume"], "func": tin_141_vxr_21d_pct_rank_252d},
    "tin_142_activity_composite_pct_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": tin_142_activity_composite_pct_rank_252d},
    "tin_143_regime_transition_freq_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": tin_143_regime_transition_freq_zscore_252d},
    "tin_144_vol_trend_slope_zscore_252d": {"inputs": ["volume"], "func": tin_144_vol_trend_slope_zscore_252d},
    "tin_145_expanding_active_frac_rank": {"inputs": ["close", "high", "low"], "func": tin_145_expanding_active_frac_rank},
    "tin_146_intensity_score_vol_range_active": {"inputs": ["close", "high", "low", "volume"], "func": tin_146_intensity_score_vol_range_active},
    "tin_147_activity_lull_divergence_score": {"inputs": ["close", "high", "low", "volume"], "func": tin_147_activity_lull_divergence_score},
    "tin_148_intensity_trend_composite_slope": {"inputs": ["close", "high", "low", "volume"], "func": tin_148_intensity_trend_composite_slope},
    "tin_149_vol_range_divergence_21d": {"inputs": ["high", "low", "volume"], "func": tin_149_vol_range_divergence_21d},
    "tin_150_activity_intensity_regime_score": {"inputs": ["close", "high", "low", "volume"], "func": tin_150_activity_intensity_regime_score},
}
