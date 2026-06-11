"""
19_volume_trend — Extended Features 001-075
Domain: directional drift in volume over weeks — volume oscillator, ease of movement (EMV),
        volume RSI, and deeper trend signals
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ──────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9
_EMV_SCALE = 1_000_000.0  # shares scaling for EMV box-ratio

# ── Utility helpers ────────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    """Rolling mean with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    """Rolling std with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    """Rolling sum with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    """Rolling min with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    """Rolling max with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    """Exponential weighted mean."""
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    """Log of series clipped at EPS."""
    return np.log(s.clip(lower=_EPS))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope of s over w periods (unnormalized)."""
    def _slope(x):
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
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=False)


def _linslope_rsq(s: pd.Series, w: int) -> pd.Series:
    """Rolling R-squared of OLS line fit of s over w periods."""
    def _rsq(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        ss_tot = ((x - x_m) ** 2).sum()
        if ss_tot == 0:
            return np.nan
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        slope = num / den
        intercept = x_m - slope * xi_m
        resid = x - (slope * xi + intercept)
        ss_res = (resid ** 2).sum()
        return 1.0 - ss_res / ss_tot
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_rsq, raw=False)


def _rsi_series(s: pd.Series, period: int) -> pd.Series:
    """RSI of an arbitrary series using Wilder smoothing (EWM with alpha=1/period)."""
    delta = s.diff(1)
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = gain.ewm(alpha=1.0 / period, min_periods=max(1, period // 2), adjust=False).mean()
    avg_loss = loss.ewm(alpha=1.0 / period, min_periods=max(1, period // 2), adjust=False).mean()
    rs = _safe_div(avg_gain, avg_loss)
    return 100.0 - _safe_div(100.0, 1.0 + rs)


def _emv_raw(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Raw (unsmoothed) Ease of Movement value."""
    midpoint = (high + low) / 2.0
    dist_moved = midpoint - midpoint.shift(1)
    hl_range = (high - low).replace(0, np.nan)
    box_ratio = _safe_div(volume / _EMV_SCALE, hl_range)
    return _safe_div(dist_moved, box_ratio)


# ── Group A (001-015): Volume Oscillator — SMA-based (fast MA − slow MA) / slow MA * 100 ──

def vtr_ext_001_vol_osc_5_21(volume: pd.Series) -> pd.Series:
    """Volume oscillator (5,21): (SMA5 - SMA21) / SMA21 * 100."""
    fast = _rolling_mean(volume, _TD_WEEK)
    slow = _rolling_mean(volume, _TD_MON)
    return _safe_div(fast - slow, slow) * 100.0


def vtr_ext_002_vol_osc_14_28(volume: pd.Series) -> pd.Series:
    """Volume oscillator (14,28): (SMA14 - SMA28) / SMA28 * 100."""
    fast = _rolling_mean(volume, 14)
    slow = _rolling_mean(volume, 28)
    return _safe_div(fast - slow, slow) * 100.0


def vtr_ext_003_vol_osc_21_63(volume: pd.Series) -> pd.Series:
    """Volume oscillator (21,63): (SMA21 - SMA63) / SMA63 * 100."""
    fast = _rolling_mean(volume, _TD_MON)
    slow = _rolling_mean(volume, _TD_QTR)
    return _safe_div(fast - slow, slow) * 100.0


def vtr_ext_004_vol_osc_5_21_sign(volume: pd.Series) -> pd.Series:
    """Sign of volume oscillator (5,21): +1 above, -1 below."""
    return np.sign(vtr_ext_001_vol_osc_5_21(volume))


def vtr_ext_005_vol_osc_14_28_sign(volume: pd.Series) -> pd.Series:
    """Sign of volume oscillator (14,28)."""
    return np.sign(vtr_ext_002_vol_osc_14_28(volume))


def vtr_ext_006_vol_osc_21_63_sign(volume: pd.Series) -> pd.Series:
    """Sign of volume oscillator (21,63)."""
    return np.sign(vtr_ext_003_vol_osc_21_63(volume))


def vtr_ext_007_vol_osc_5_21_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of volume oscillator (5,21) vs trailing 252-day distribution."""
    osc = vtr_ext_001_vol_osc_5_21(volume)
    m = _rolling_mean(osc, _TD_YEAR)
    s = _rolling_std(osc, _TD_YEAR)
    return _safe_div(osc - m, s)


def vtr_ext_008_vol_osc_21_63_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of volume oscillator (21,63) vs trailing 252-day distribution."""
    osc = vtr_ext_003_vol_osc_21_63(volume)
    m = _rolling_mean(osc, _TD_YEAR)
    s = _rolling_std(osc, _TD_YEAR)
    return _safe_div(osc - m, s)


def vtr_ext_009_vol_osc_5_21_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of volume oscillator (5,21) in trailing 252-day distribution."""
    osc = vtr_ext_001_vol_osc_5_21(volume)
    return osc.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vtr_ext_010_vol_osc_21_63_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of volume oscillator (21,63) in trailing 252-day distribution."""
    osc = vtr_ext_003_vol_osc_21_63(volume)
    return osc.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vtr_ext_011_vol_osc_5_21_below_zero_flag(volume: pd.Series) -> pd.Series:
    """Flag: volume oscillator (5,21) is below zero (short-term vol below medium-term)."""
    return (vtr_ext_001_vol_osc_5_21(volume) < 0.0).astype(float)


def vtr_ext_012_vol_osc_21_63_below_zero_flag(volume: pd.Series) -> pd.Series:
    """Flag: volume oscillator (21,63) is below zero."""
    return (vtr_ext_003_vol_osc_21_63(volume) < 0.0).astype(float)


def vtr_ext_013_vol_osc_both_negative_flag(volume: pd.Series) -> pd.Series:
    """Flag: both volume oscillators (5,21) and (21,63) are simultaneously negative."""
    return (
        (vtr_ext_001_vol_osc_5_21(volume) < 0.0) &
        (vtr_ext_003_vol_osc_21_63(volume) < 0.0)
    ).astype(float)


def vtr_ext_014_vol_osc_5_21_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day change in volume oscillator (5,21): momentum of the oscillator."""
    osc = vtr_ext_001_vol_osc_5_21(volume)
    return osc.diff(_TD_WEEK)


def vtr_ext_015_vol_osc_21_63_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day change in volume oscillator (21,63): medium-term oscillator momentum."""
    osc = vtr_ext_003_vol_osc_21_63(volume)
    return osc.diff(_TD_MON)


# ── Group B (016-025): Volume MACD — EMA-diff with signal line and histogram ──

def vtr_ext_016_vol_macd_line_12_26(volume: pd.Series) -> pd.Series:
    """Volume MACD line: EMA12(volume) - EMA26(volume)."""
    return _ewm_mean(volume, 12) - _ewm_mean(volume, 26)


def vtr_ext_017_vol_macd_signal_9(volume: pd.Series) -> pd.Series:
    """Volume MACD signal line: 9-period EMA of the MACD line."""
    macd = vtr_ext_016_vol_macd_line_12_26(volume)
    return _ewm_mean(macd, 9)


def vtr_ext_018_vol_macd_histogram(volume: pd.Series) -> pd.Series:
    """Volume MACD histogram: MACD line minus signal line."""
    return vtr_ext_016_vol_macd_line_12_26(volume) - vtr_ext_017_vol_macd_signal_9(volume)


def vtr_ext_019_vol_macd_histogram_sign(volume: pd.Series) -> pd.Series:
    """Sign of volume MACD histogram (+1 bullish momentum, -1 bearish)."""
    return np.sign(vtr_ext_018_vol_macd_histogram(volume))


def vtr_ext_020_vol_macd_line_above_signal_flag(volume: pd.Series) -> pd.Series:
    """Flag: MACD line > signal line (positive histogram)."""
    return (vtr_ext_016_vol_macd_line_12_26(volume) > vtr_ext_017_vol_macd_signal_9(volume)).astype(float)


def vtr_ext_021_vol_macd_histogram_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day change in volume MACD histogram (acceleration)."""
    return vtr_ext_018_vol_macd_histogram(volume).diff(_TD_WEEK)


def vtr_ext_022_vol_macd_line_norm(volume: pd.Series) -> pd.Series:
    """Volume MACD line normalized by 252-day rolling mean volume."""
    macd = vtr_ext_016_vol_macd_line_12_26(volume)
    avg = _rolling_mean(volume, _TD_YEAR).clip(lower=_EPS)
    return _safe_div(macd, avg)


def vtr_ext_023_vol_macd_histogram_norm(volume: pd.Series) -> pd.Series:
    """Volume MACD histogram normalized by 252-day rolling mean volume."""
    hist = vtr_ext_018_vol_macd_histogram(volume)
    avg = _rolling_mean(volume, _TD_YEAR).clip(lower=_EPS)
    return _safe_div(hist, avg)


def vtr_ext_024_vol_macd_histogram_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of volume MACD histogram vs trailing 252-day distribution."""
    hist = vtr_ext_018_vol_macd_histogram(volume)
    m = _rolling_mean(hist, _TD_YEAR)
    s = _rolling_std(hist, _TD_YEAR)
    return _safe_div(hist - m, s)


def vtr_ext_025_vol_macd_line_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of volume MACD line in trailing 252-day distribution."""
    macd = vtr_ext_016_vol_macd_line_12_26(volume)
    return macd.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# ── Group C (026-036): Ease of Movement (EMV) ────────────────────────────────

def vtr_ext_026_emv_raw(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Raw (1-day) Ease of Movement: distance_moved / box_ratio."""
    return _emv_raw(high, low, volume)


def vtr_ext_027_emv_sma14(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """14-day SMA-smoothed Ease of Movement (standard EMV indicator)."""
    return _rolling_mean(_emv_raw(high, low, volume), 14)


def vtr_ext_028_emv_sma21(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day SMA-smoothed Ease of Movement."""
    return _rolling_mean(_emv_raw(high, low, volume), _TD_MON)


def vtr_ext_029_emv_sign(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Sign of 14-day smoothed EMV (+1 = upward ease, -1 = downward ease)."""
    return np.sign(vtr_ext_027_emv_sma14(high, low, volume))


def vtr_ext_030_emv_below_zero_flag(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: 14-day smoothed EMV is below zero (volume-weighted downward ease)."""
    return (vtr_ext_027_emv_sma14(high, low, volume) < 0.0).astype(float)


def vtr_ext_031_emv_zscore_252d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 14-day smoothed EMV vs trailing 252-day distribution."""
    emv14 = vtr_ext_027_emv_sma14(high, low, volume)
    m = _rolling_mean(emv14, _TD_YEAR)
    s = _rolling_std(emv14, _TD_YEAR)
    return _safe_div(emv14 - m, s)


def vtr_ext_032_emv_pct_rank_252d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of 14-day smoothed EMV in trailing 252-day distribution."""
    emv14 = vtr_ext_027_emv_sma14(high, low, volume)
    return emv14.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vtr_ext_033_emv_raw_5d_diff(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day change in 14-day smoothed EMV (EMV momentum)."""
    return vtr_ext_027_emv_sma14(high, low, volume).diff(_TD_WEEK)


def vtr_ext_034_emv_raw_sign_persistence_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days where 14-day smoothed EMV > 0."""
    emv_pos = (vtr_ext_027_emv_sma14(high, low, volume) > 0.0).astype(float)
    return _rolling_mean(emv_pos, _TD_MON)


def vtr_ext_035_emv_raw_sign_persistence_63d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days where 14-day smoothed EMV > 0."""
    emv_pos = (vtr_ext_027_emv_sma14(high, low, volume) > 0.0).astype(float)
    return _rolling_mean(emv_pos, _TD_QTR)


def vtr_ext_036_emv_sma21_vs_sma14_diff(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Difference between 21-day and 14-day smoothed EMV (oscillator of oscillator)."""
    return vtr_ext_028_emv_sma21(high, low, volume) - vtr_ext_027_emv_sma14(high, low, volume)


# ── Group D (037-049): Volume RSI — RSI formula applied to volume series ──────

def vtr_ext_037_vol_rsi_14(volume: pd.Series) -> pd.Series:
    """Volume RSI with period 14 (RSI applied to volume changes)."""
    return _rsi_series(volume, 14)


def vtr_ext_038_vol_rsi_21(volume: pd.Series) -> pd.Series:
    """Volume RSI with period 21."""
    return _rsi_series(volume, _TD_MON)


def vtr_ext_039_vol_rsi_14_overbought_flag(volume: pd.Series) -> pd.Series:
    """Flag: volume RSI(14) >= 70 (overbought volume momentum)."""
    return (vtr_ext_037_vol_rsi_14(volume) >= 70.0).astype(float)


def vtr_ext_040_vol_rsi_14_oversold_flag(volume: pd.Series) -> pd.Series:
    """Flag: volume RSI(14) <= 30 (oversold / exhausted volume momentum)."""
    return (vtr_ext_037_vol_rsi_14(volume) <= 30.0).astype(float)


def vtr_ext_041_vol_rsi_21_overbought_flag(volume: pd.Series) -> pd.Series:
    """Flag: volume RSI(21) >= 70."""
    return (vtr_ext_038_vol_rsi_21(volume) >= 70.0).astype(float)


def vtr_ext_042_vol_rsi_21_oversold_flag(volume: pd.Series) -> pd.Series:
    """Flag: volume RSI(21) <= 30."""
    return (vtr_ext_038_vol_rsi_21(volume) <= 30.0).astype(float)


def vtr_ext_043_vol_rsi_14_depth(volume: pd.Series) -> pd.Series:
    """Distance of volume RSI(14) below 50 (positive = below midline)."""
    return 50.0 - vtr_ext_037_vol_rsi_14(volume)


def vtr_ext_044_vol_rsi_21_depth(volume: pd.Series) -> pd.Series:
    """Distance of volume RSI(21) below 50."""
    return 50.0 - vtr_ext_038_vol_rsi_21(volume)


def vtr_ext_045_vol_rsi_14_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of volume RSI(14) vs trailing 252-day distribution."""
    rsi = vtr_ext_037_vol_rsi_14(volume)
    m = _rolling_mean(rsi, _TD_YEAR)
    s = _rolling_std(rsi, _TD_YEAR)
    return _safe_div(rsi - m, s)


def vtr_ext_046_vol_rsi_14_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of volume RSI(14) in trailing 252-day distribution."""
    rsi = vtr_ext_037_vol_rsi_14(volume)
    return rsi.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vtr_ext_047_vol_rsi_14_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day change in volume RSI(14) (momentum of RSI)."""
    return vtr_ext_037_vol_rsi_14(volume).diff(_TD_WEEK)


def vtr_ext_048_vol_rsi_14_vs_rsi_21_diff(volume: pd.Series) -> pd.Series:
    """Difference between volume RSI(14) and RSI(21) (short vs medium RSI spread)."""
    return vtr_ext_037_vol_rsi_14(volume) - vtr_ext_038_vol_rsi_21(volume)


def vtr_ext_049_vol_rsi_14_below_50_frac_63d(volume: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days where volume RSI(14) is below 50."""
    below = (vtr_ext_037_vol_rsi_14(volume) < 50.0).astype(float)
    return _rolling_mean(below, _TD_QTR)


# ── Group E (050-059): Volume trend slope R-squared (trend quality) ───────────
# These use novel window/series combos not in the existing 200.

def vtr_ext_050_vol_rsq_14d(volume: pd.Series) -> pd.Series:
    """R-squared of OLS fit to raw volume over trailing 14 days (2-week quality)."""
    return _linslope_rsq(volume, 14)


def vtr_ext_051_emv_sma14_rsq_63d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """R-squared of OLS fit to 14-day smoothed EMV over trailing 63 days."""
    return _linslope_rsq(vtr_ext_027_emv_sma14(high, low, volume), _TD_QTR)


def vtr_ext_052_vol_rsi_14_rsq_63d(volume: pd.Series) -> pd.Series:
    """R-squared of OLS fit to volume RSI(14) over trailing 63 days."""
    return _linslope_rsq(vtr_ext_037_vol_rsi_14(volume), _TD_QTR)


def vtr_ext_053_vol_osc_5_21_rsq_63d(volume: pd.Series) -> pd.Series:
    """R-squared of OLS fit to volume oscillator (5,21) over trailing 63 days."""
    return _linslope_rsq(vtr_ext_001_vol_osc_5_21(volume), _TD_QTR)


def vtr_ext_054_vol_rsq_14d_signed(volume: pd.Series) -> pd.Series:
    """R-squared of 14-day volume trend, signed by slope direction."""
    rsq = _linslope_rsq(volume, 14)
    sgn = np.sign(_linslope(volume, 14))
    return rsq * sgn


def vtr_ext_055_vol_rsq_14d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 14-day volume R-squared in trailing 252-day distribution."""
    rsq = _linslope_rsq(volume, 14)
    return rsq.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# ── Group F (056-063): Volume drift direction persistence ────────────────────

def vtr_ext_056_vol_drift_dir_persist_14d(volume: pd.Series) -> pd.Series:
    """Direction persistence over 14 days: abs(sum of daily signs) / 14."""
    sign_chg = np.sign(volume.diff(1))
    total_sign = sign_chg.rolling(14, min_periods=7).sum()
    return total_sign.abs() / 14.0


def vtr_ext_057_vol_drift_dir_persist_14d_sign(volume: pd.Series) -> pd.Series:
    """Signed drift persistence over 14 days: sum of daily volume change signs / 14."""
    sign_chg = np.sign(volume.diff(1))
    return sign_chg.rolling(14, min_periods=7).sum() / 14.0


def vtr_ext_058_vol_drift_persist_5d_sign(volume: pd.Series) -> pd.Series:
    """Signed drift persistence over 5 days: sum of daily signs / 5."""
    sign_chg = np.sign(volume.diff(1))
    return sign_chg.rolling(_TD_WEEK, min_periods=3).sum() / float(_TD_WEEK)


def vtr_ext_059_vol_drift_persist_5d_vs_63d_diff(volume: pd.Series) -> pd.Series:
    """Difference between 5-day and 63-day signed drift persistence (recent vs medium)."""
    sc = np.sign(volume.diff(1))
    p5 = sc.rolling(_TD_WEEK, min_periods=3).sum() / float(_TD_WEEK)
    p63 = sc.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum() / float(_TD_QTR)
    return p5 - p63


# ── Group G (060-064): EWM-volume trend (EWM slope / direction) ───────────────

def vtr_ext_060_vol_ewm_trend_14_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of 14-period EWM volume over trailing 21 days."""
    return _linslope(_ewm_mean(volume, 14), _TD_MON)


def vtr_ext_061_vol_ewm_trend_14_sign_21d(volume: pd.Series) -> pd.Series:
    """Sign of 21-day slope of the 14-period EWM volume."""
    return np.sign(_linslope(_ewm_mean(volume, 14), _TD_MON))


def vtr_ext_062_vol_ewm_trend_14_vs_63d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of EWM14 volume to EWM63 volume (short vs medium EWM)."""
    return _safe_div(_ewm_mean(volume, 14), _ewm_mean(volume, _TD_QTR))


def vtr_ext_063_vol_ewm14_5d_change_norm(volume: pd.Series) -> pd.Series:
    """Normalized 5-day change in EWM14 volume: (EWM14 - EWM14_5ago) / EWM14_5ago."""
    e14 = _ewm_mean(volume, 14)
    return _safe_div(e14 - e14.shift(_TD_WEEK), e14.shift(_TD_WEEK).clip(lower=_EPS))


def vtr_ext_064_vol_ewm14_declining_flag(volume: pd.Series) -> pd.Series:
    """Flag: EWM14 volume is lower today than 5 days ago."""
    e14 = _ewm_mean(volume, 14)
    return (e14 < e14.shift(_TD_WEEK)).astype(float)


# ── Group H (065-070): Volume-trend vs price-trend agreement (novel combos) ───

def vtr_ext_065_vol_osc_5_21_vs_price_slope_sign_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Product: sign(vol osc 5,21) * sign(price slope 21d). +1=agree, -1=diverge."""
    vs = np.sign(vtr_ext_001_vol_osc_5_21(volume))
    ps = np.sign(_linslope(close, _TD_MON))
    return vs * ps


def vtr_ext_066_emv_sign_vs_price_direction_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Product: sign(EMV14) * sign(price 21d slope). +1=aligned, -1=diverged."""
    emv_sgn = np.sign(vtr_ext_027_emv_sma14(high, low, volume))
    p_sgn = np.sign(_linslope(close, _TD_MON))
    return emv_sgn * p_sgn


def vtr_ext_067_vol_rsi_above50_price_down_flag_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: volume RSI(14) > 50 while price has negative 21d slope (vol/price diverge)."""
    vol_rsi = vtr_ext_037_vol_rsi_14(volume)
    p_slope = _linslope(close, _TD_MON)
    return ((vol_rsi > 50.0) & (p_slope < 0.0)).astype(float)


def vtr_ext_068_vol_macd_positive_price_down_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: volume MACD histogram > 0 while price has negative 21d slope."""
    hist = vtr_ext_018_vol_macd_histogram(volume)
    p_slope = _linslope(close, _TD_MON)
    return ((hist > 0.0) & (p_slope < 0.0)).astype(float)


def vtr_ext_069_vol_osc_21_63_vs_price_slope_63d_product(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sign agreement: sign(vol osc 21,63) * sign(price 63d slope). +1=agree, -1=diverge."""
    vs = np.sign(vtr_ext_003_vol_osc_21_63(volume))
    ps = np.sign(_linslope(close, _TD_QTR))
    return vs * ps


def vtr_ext_070_vol_rsi_14_price_slope_21d_correlation_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day rolling correlation between volume RSI(14) and 21-day price slope."""
    rsi = vtr_ext_037_vol_rsi_14(volume)
    pslope = _linslope(close, _TD_MON)
    return rsi.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 2)).corr(pslope)


# ── Group I (071-075): Long-term volume up/down drift and ROC ─────────────────

def vtr_ext_071_vol_long_drift_up_frac_252d(volume: pd.Series) -> pd.Series:
    """Fraction of 252 days where volume is above its 63-day lagged value (up-drift)."""
    up = (volume > volume.shift(_TD_QTR)).astype(float)
    return _rolling_mean(up, _TD_YEAR)


def vtr_ext_072_vol_long_drift_down_frac_252d(volume: pd.Series) -> pd.Series:
    """Fraction of 252 days where volume is below its 63-day lagged value (down-drift)."""
    down = (volume < volume.shift(_TD_QTR)).astype(float)
    return _rolling_mean(down, _TD_YEAR)


def vtr_ext_073_vol_long_drift_balance_252d(volume: pd.Series) -> pd.Series:
    """Up-minus-down long drift balance over 252 days (positive = net upward drift)."""
    return vtr_ext_071_vol_long_drift_up_frac_252d(volume) - vtr_ext_072_vol_long_drift_down_frac_252d(volume)


def vtr_ext_074_vol_rsi_14_roc_21d(volume: pd.Series) -> pd.Series:
    """Rate of change of volume RSI(14) over 21 days: (RSI_t - RSI_{t-21}) / 21."""
    rsi = vtr_ext_037_vol_rsi_14(volume)
    return _safe_div(rsi - rsi.shift(_TD_MON), pd.Series(float(_TD_MON), index=rsi.index))


def vtr_ext_075_vol_osc_5_21_roc_21d(volume: pd.Series) -> pd.Series:
    """Rate of change of volume oscillator (5,21) over 21 days."""
    osc = vtr_ext_001_vol_osc_5_21(volume)
    return _safe_div(osc - osc.shift(_TD_MON), pd.Series(float(_TD_MON), index=osc.index))


# ── Registry ───────────────────────────────────────────────────────────────────

VOLUME_TREND_EXTENDED_REGISTRY_001_075 = {
    "vtr_ext_001_vol_osc_5_21": {"inputs": ["volume"], "func": vtr_ext_001_vol_osc_5_21},
    "vtr_ext_002_vol_osc_14_28": {"inputs": ["volume"], "func": vtr_ext_002_vol_osc_14_28},
    "vtr_ext_003_vol_osc_21_63": {"inputs": ["volume"], "func": vtr_ext_003_vol_osc_21_63},
    "vtr_ext_004_vol_osc_5_21_sign": {"inputs": ["volume"], "func": vtr_ext_004_vol_osc_5_21_sign},
    "vtr_ext_005_vol_osc_14_28_sign": {"inputs": ["volume"], "func": vtr_ext_005_vol_osc_14_28_sign},
    "vtr_ext_006_vol_osc_21_63_sign": {"inputs": ["volume"], "func": vtr_ext_006_vol_osc_21_63_sign},
    "vtr_ext_007_vol_osc_5_21_zscore_252d": {"inputs": ["volume"], "func": vtr_ext_007_vol_osc_5_21_zscore_252d},
    "vtr_ext_008_vol_osc_21_63_zscore_252d": {"inputs": ["volume"], "func": vtr_ext_008_vol_osc_21_63_zscore_252d},
    "vtr_ext_009_vol_osc_5_21_pct_rank_252d": {"inputs": ["volume"], "func": vtr_ext_009_vol_osc_5_21_pct_rank_252d},
    "vtr_ext_010_vol_osc_21_63_pct_rank_252d": {"inputs": ["volume"], "func": vtr_ext_010_vol_osc_21_63_pct_rank_252d},
    "vtr_ext_011_vol_osc_5_21_below_zero_flag": {"inputs": ["volume"], "func": vtr_ext_011_vol_osc_5_21_below_zero_flag},
    "vtr_ext_012_vol_osc_21_63_below_zero_flag": {"inputs": ["volume"], "func": vtr_ext_012_vol_osc_21_63_below_zero_flag},
    "vtr_ext_013_vol_osc_both_negative_flag": {"inputs": ["volume"], "func": vtr_ext_013_vol_osc_both_negative_flag},
    "vtr_ext_014_vol_osc_5_21_5d_diff": {"inputs": ["volume"], "func": vtr_ext_014_vol_osc_5_21_5d_diff},
    "vtr_ext_015_vol_osc_21_63_21d_diff": {"inputs": ["volume"], "func": vtr_ext_015_vol_osc_21_63_21d_diff},
    "vtr_ext_016_vol_macd_line_12_26": {"inputs": ["volume"], "func": vtr_ext_016_vol_macd_line_12_26},
    "vtr_ext_017_vol_macd_signal_9": {"inputs": ["volume"], "func": vtr_ext_017_vol_macd_signal_9},
    "vtr_ext_018_vol_macd_histogram": {"inputs": ["volume"], "func": vtr_ext_018_vol_macd_histogram},
    "vtr_ext_019_vol_macd_histogram_sign": {"inputs": ["volume"], "func": vtr_ext_019_vol_macd_histogram_sign},
    "vtr_ext_020_vol_macd_line_above_signal_flag": {"inputs": ["volume"], "func": vtr_ext_020_vol_macd_line_above_signal_flag},
    "vtr_ext_021_vol_macd_histogram_5d_diff": {"inputs": ["volume"], "func": vtr_ext_021_vol_macd_histogram_5d_diff},
    "vtr_ext_022_vol_macd_line_norm": {"inputs": ["volume"], "func": vtr_ext_022_vol_macd_line_norm},
    "vtr_ext_023_vol_macd_histogram_norm": {"inputs": ["volume"], "func": vtr_ext_023_vol_macd_histogram_norm},
    "vtr_ext_024_vol_macd_histogram_zscore_252d": {"inputs": ["volume"], "func": vtr_ext_024_vol_macd_histogram_zscore_252d},
    "vtr_ext_025_vol_macd_line_pct_rank_252d": {"inputs": ["volume"], "func": vtr_ext_025_vol_macd_line_pct_rank_252d},
    "vtr_ext_026_emv_raw": {"inputs": ["high", "low", "volume"], "func": vtr_ext_026_emv_raw},
    "vtr_ext_027_emv_sma14": {"inputs": ["high", "low", "volume"], "func": vtr_ext_027_emv_sma14},
    "vtr_ext_028_emv_sma21": {"inputs": ["high", "low", "volume"], "func": vtr_ext_028_emv_sma21},
    "vtr_ext_029_emv_sign": {"inputs": ["high", "low", "volume"], "func": vtr_ext_029_emv_sign},
    "vtr_ext_030_emv_below_zero_flag": {"inputs": ["high", "low", "volume"], "func": vtr_ext_030_emv_below_zero_flag},
    "vtr_ext_031_emv_zscore_252d": {"inputs": ["high", "low", "volume"], "func": vtr_ext_031_emv_zscore_252d},
    "vtr_ext_032_emv_pct_rank_252d": {"inputs": ["high", "low", "volume"], "func": vtr_ext_032_emv_pct_rank_252d},
    "vtr_ext_033_emv_raw_5d_diff": {"inputs": ["high", "low", "volume"], "func": vtr_ext_033_emv_raw_5d_diff},
    "vtr_ext_034_emv_raw_sign_persistence_21d": {"inputs": ["high", "low", "volume"], "func": vtr_ext_034_emv_raw_sign_persistence_21d},
    "vtr_ext_035_emv_raw_sign_persistence_63d": {"inputs": ["high", "low", "volume"], "func": vtr_ext_035_emv_raw_sign_persistence_63d},
    "vtr_ext_036_emv_sma21_vs_sma14_diff": {"inputs": ["high", "low", "volume"], "func": vtr_ext_036_emv_sma21_vs_sma14_diff},
    "vtr_ext_037_vol_rsi_14": {"inputs": ["volume"], "func": vtr_ext_037_vol_rsi_14},
    "vtr_ext_038_vol_rsi_21": {"inputs": ["volume"], "func": vtr_ext_038_vol_rsi_21},
    "vtr_ext_039_vol_rsi_14_overbought_flag": {"inputs": ["volume"], "func": vtr_ext_039_vol_rsi_14_overbought_flag},
    "vtr_ext_040_vol_rsi_14_oversold_flag": {"inputs": ["volume"], "func": vtr_ext_040_vol_rsi_14_oversold_flag},
    "vtr_ext_041_vol_rsi_21_overbought_flag": {"inputs": ["volume"], "func": vtr_ext_041_vol_rsi_21_overbought_flag},
    "vtr_ext_042_vol_rsi_21_oversold_flag": {"inputs": ["volume"], "func": vtr_ext_042_vol_rsi_21_oversold_flag},
    "vtr_ext_043_vol_rsi_14_depth": {"inputs": ["volume"], "func": vtr_ext_043_vol_rsi_14_depth},
    "vtr_ext_044_vol_rsi_21_depth": {"inputs": ["volume"], "func": vtr_ext_044_vol_rsi_21_depth},
    "vtr_ext_045_vol_rsi_14_zscore_252d": {"inputs": ["volume"], "func": vtr_ext_045_vol_rsi_14_zscore_252d},
    "vtr_ext_046_vol_rsi_14_pct_rank_252d": {"inputs": ["volume"], "func": vtr_ext_046_vol_rsi_14_pct_rank_252d},
    "vtr_ext_047_vol_rsi_14_5d_diff": {"inputs": ["volume"], "func": vtr_ext_047_vol_rsi_14_5d_diff},
    "vtr_ext_048_vol_rsi_14_vs_rsi_21_diff": {"inputs": ["volume"], "func": vtr_ext_048_vol_rsi_14_vs_rsi_21_diff},
    "vtr_ext_049_vol_rsi_14_below_50_frac_63d": {"inputs": ["volume"], "func": vtr_ext_049_vol_rsi_14_below_50_frac_63d},
    "vtr_ext_050_vol_rsq_14d": {"inputs": ["volume"], "func": vtr_ext_050_vol_rsq_14d},
    "vtr_ext_051_emv_sma14_rsq_63d": {"inputs": ["high", "low", "volume"], "func": vtr_ext_051_emv_sma14_rsq_63d},
    "vtr_ext_052_vol_rsi_14_rsq_63d": {"inputs": ["volume"], "func": vtr_ext_052_vol_rsi_14_rsq_63d},
    "vtr_ext_053_vol_osc_5_21_rsq_63d": {"inputs": ["volume"], "func": vtr_ext_053_vol_osc_5_21_rsq_63d},
    "vtr_ext_054_vol_rsq_14d_signed": {"inputs": ["volume"], "func": vtr_ext_054_vol_rsq_14d_signed},
    "vtr_ext_055_vol_rsq_14d_pct_rank_252d": {"inputs": ["volume"], "func": vtr_ext_055_vol_rsq_14d_pct_rank_252d},
    "vtr_ext_056_vol_drift_dir_persist_14d": {"inputs": ["volume"], "func": vtr_ext_056_vol_drift_dir_persist_14d},
    "vtr_ext_057_vol_drift_dir_persist_14d_sign": {"inputs": ["volume"], "func": vtr_ext_057_vol_drift_dir_persist_14d_sign},
    "vtr_ext_058_vol_drift_persist_5d_sign": {"inputs": ["volume"], "func": vtr_ext_058_vol_drift_persist_5d_sign},
    "vtr_ext_059_vol_drift_persist_5d_vs_63d_diff": {"inputs": ["volume"], "func": vtr_ext_059_vol_drift_persist_5d_vs_63d_diff},
    "vtr_ext_060_vol_ewm_trend_14_slope_21d": {"inputs": ["volume"], "func": vtr_ext_060_vol_ewm_trend_14_slope_21d},
    "vtr_ext_061_vol_ewm_trend_14_sign_21d": {"inputs": ["volume"], "func": vtr_ext_061_vol_ewm_trend_14_sign_21d},
    "vtr_ext_062_vol_ewm_trend_14_vs_63d_ratio": {"inputs": ["volume"], "func": vtr_ext_062_vol_ewm_trend_14_vs_63d_ratio},
    "vtr_ext_063_vol_ewm14_5d_change_norm": {"inputs": ["volume"], "func": vtr_ext_063_vol_ewm14_5d_change_norm},
    "vtr_ext_064_vol_ewm14_declining_flag": {"inputs": ["volume"], "func": vtr_ext_064_vol_ewm14_declining_flag},
    "vtr_ext_065_vol_osc_5_21_vs_price_slope_sign_21d": {"inputs": ["close", "volume"], "func": vtr_ext_065_vol_osc_5_21_vs_price_slope_sign_21d},
    "vtr_ext_066_emv_sign_vs_price_direction_21d": {"inputs": ["close", "high", "low", "volume"], "func": vtr_ext_066_emv_sign_vs_price_direction_21d},
    "vtr_ext_067_vol_rsi_above50_price_down_flag_21d": {"inputs": ["close", "volume"], "func": vtr_ext_067_vol_rsi_above50_price_down_flag_21d},
    "vtr_ext_068_vol_macd_positive_price_down_flag": {"inputs": ["close", "volume"], "func": vtr_ext_068_vol_macd_positive_price_down_flag},
    "vtr_ext_069_vol_osc_21_63_vs_price_slope_63d_product": {"inputs": ["close", "volume"], "func": vtr_ext_069_vol_osc_21_63_vs_price_slope_63d_product},
    "vtr_ext_070_vol_rsi_14_price_slope_21d_correlation_63d": {"inputs": ["close", "volume"], "func": vtr_ext_070_vol_rsi_14_price_slope_21d_correlation_63d},
    "vtr_ext_071_vol_long_drift_up_frac_252d": {"inputs": ["volume"], "func": vtr_ext_071_vol_long_drift_up_frac_252d},
    "vtr_ext_072_vol_long_drift_down_frac_252d": {"inputs": ["volume"], "func": vtr_ext_072_vol_long_drift_down_frac_252d},
    "vtr_ext_073_vol_long_drift_balance_252d": {"inputs": ["volume"], "func": vtr_ext_073_vol_long_drift_balance_252d},
    "vtr_ext_074_vol_rsi_14_roc_21d": {"inputs": ["volume"], "func": vtr_ext_074_vol_rsi_14_roc_21d},
    "vtr_ext_075_vol_osc_5_21_roc_21d": {"inputs": ["volume"], "func": vtr_ext_075_vol_osc_5_21_roc_21d},
}
