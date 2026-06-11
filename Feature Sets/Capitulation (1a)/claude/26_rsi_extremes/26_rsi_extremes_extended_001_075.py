"""
26_rsi_extremes — Extended Features 001-075
Domain: RSI oversold readings — deeper variants, cross-RSI confluence, regime flags,
        volume-weighted RSI, additional price series, rate-of-change variants
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rsi(close: pd.Series, period: int) -> pd.Series:
    """Wilder smoothed RSI for a given lookback period."""
    delta = close.diff(1)
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = gain.ewm(alpha=1.0 / period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1.0 / period, min_periods=period, adjust=False).mean()
    rs = _safe_div(avg_gain, avg_loss)
    return 100.0 - 100.0 / (1.0 + rs)


def _rsi_sma(close: pd.Series, period: int) -> pd.Series:
    """Simple-average (Cutler) RSI for a given lookback."""
    delta = close.diff(1)
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = _rolling_mean(gain, period)
    avg_loss = _rolling_mean(loss, period)
    rs = _safe_div(avg_gain, avg_loss)
    return 100.0 - 100.0 / (1.0 + rs)


def _rsi_ema(close: pd.Series, period: int) -> pd.Series:
    """EMA-smoothed RSI (span=period, not Wilder's alpha=1/period)."""
    delta = close.diff(1)
    gain = delta.clip(lower=0.0)
    loss = (-delta).clip(lower=0.0)
    avg_gain = gain.ewm(span=period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(span=period, min_periods=period, adjust=False).mean()
    rs = _safe_div(avg_gain, avg_loss)
    return 100.0 - 100.0 / (1.0 + rs)


def _stochrsi_k(close: pd.Series, rsi_period: int, stoch_period: int) -> pd.Series:
    """StochRSI %K: (RSI - min(RSI,n)) / (max(RSI,n) - min(RSI,n)), 0-100."""
    r = _rsi(close, rsi_period)
    mn = _rolling_min(r, stoch_period)
    mx = _rolling_max(r, stoch_period)
    k = _safe_div(r - mn, mx - mn)
    return k * 100.0


def _laguerre_rsi(close: pd.Series, gamma: float) -> pd.Series:
    """Ehlers Laguerre RSI using a 4-pole Laguerre filter."""
    n = len(close)
    vals = close.values.astype(float)
    g = float(gamma)
    g1 = 1.0 - g

    L0 = np.full(n, np.nan)
    L1 = np.full(n, np.nan)
    L2 = np.full(n, np.nan)
    L3 = np.full(n, np.nan)
    cu = np.full(n, np.nan)
    cd = np.full(n, np.nan)

    first = 0
    while first < n and np.isnan(vals[first]):
        first += 1
    if first >= n:
        return pd.Series(np.nan, index=close.index)

    L0[first] = vals[first]
    L1[first] = vals[first]
    L2[first] = vals[first]
    L3[first] = vals[first]

    for i in range(first + 1, n):
        if np.isnan(vals[i]):
            L0[i] = L0[i - 1]
            L1[i] = L1[i - 1]
            L2[i] = L2[i - 1]
            L3[i] = L3[i - 1]
        else:
            L0[i] = g1 * vals[i] + g * L0[i - 1]
            L1[i] = -g * L0[i] + L0[i - 1] + g * L1[i - 1]
            L2[i] = -g * L1[i] + L1[i - 1] + g * L2[i - 1]
            L3[i] = -g * L2[i] + L2[i - 1] + g * L3[i - 1]

        cu_i = 0.0
        cd_i = 0.0
        if L0[i] >= L1[i]:
            cu_i += L0[i] - L1[i]
        else:
            cd_i += L1[i] - L0[i]
        if L1[i] >= L2[i]:
            cu_i += L1[i] - L2[i]
        else:
            cd_i += L2[i] - L1[i]
        if L2[i] >= L3[i]:
            cu_i += L2[i] - L3[i]
        else:
            cd_i += L3[i] - L2[i]
        cu[i] = cu_i
        cd[i] = cd_i

    with np.errstate(invalid='ignore', divide='ignore'):
        denom = cu + cd
        lrsi = np.where(denom == 0.0, 50.0, cu / denom * 100.0)

    result = pd.Series(lrsi, index=close.index)
    result.iloc[:first] = np.nan
    return result


def _vrsi(close: pd.Series, volume: pd.Series, period: int) -> pd.Series:
    """Volume-weighted RSI: gains/losses weighted by volume before smoothing."""
    delta = close.diff(1)
    gain = delta.clip(lower=0.0) * volume
    loss = (-delta).clip(lower=0.0) * volume
    avg_gain = gain.ewm(alpha=1.0 / period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1.0 / period, min_periods=period, adjust=False).mean()
    rs = _safe_div(avg_gain, avg_loss)
    return 100.0 - 100.0 / (1.0 + rs)


def _time_since_below(rsi_series: pd.Series, threshold: float) -> pd.Series:
    """Days elapsed since rsi_series was last below threshold (0 = currently below)."""
    below = (rsi_series < threshold).astype(float)
    idx = pd.Series(range(len(below)), index=below.index, dtype=float)
    last_idx = idx.where(below == 1.0).ffill().fillna(0.0)
    return (idx - last_idx).where(~rsi_series.isna(), np.nan)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Additional Wilder RSI lookback periods ---

def rsi_ext_001_rsi10(close: pd.Series) -> pd.Series:
    """Wilder RSI with 10-day lookback (between weekly and bi-weekly)."""
    return _rsi(close, 10)


def rsi_ext_002_rsi12(close: pd.Series) -> pd.Series:
    """Wilder RSI with 12-day lookback (two-week RSI)."""
    return _rsi(close, 12)


def rsi_ext_003_rsi45(close: pd.Series) -> pd.Series:
    """Wilder RSI with 45-day lookback (between monthly and quarterly)."""
    return _rsi(close, 45)


def rsi_ext_004_rsi180(close: pd.Series) -> pd.Series:
    """Wilder RSI with 180-day lookback (semi-annual)."""
    return _rsi(close, 180)


def rsi_ext_005_rsi252(close: pd.Series) -> pd.Series:
    """Wilder RSI with 252-day lookback (annual horizon RSI)."""
    return _rsi(close, _TD_YEAR)


def rsi_ext_006_rsi10_depth_below30(close: pd.Series) -> pd.Series:
    """Depth of RSI10 below 30 oversold threshold (0 when above)."""
    return (30.0 - _rsi(close, 10)).clip(lower=0.0)


def rsi_ext_007_rsi12_depth_below30(close: pd.Series) -> pd.Series:
    """Depth of RSI12 below 30 oversold threshold."""
    return (30.0 - _rsi(close, 12)).clip(lower=0.0)


def rsi_ext_008_rsi45_depth_below40(close: pd.Series) -> pd.Series:
    """Depth of RSI45 below 40 (mid-horizon oversold)."""
    return (40.0 - _rsi(close, 45)).clip(lower=0.0)


def rsi_ext_009_rsi10_consec_below30(close: pd.Series) -> pd.Series:
    """Consecutive days RSI10 has been below 30."""
    return _consec_streak(_rsi(close, 10) < 30.0)


def rsi_ext_010_rsi12_consec_below30(close: pd.Series) -> pd.Series:
    """Consecutive days RSI12 has been below 30."""
    return _consec_streak(_rsi(close, 12) < 30.0)


# --- Group B (011-018): Additional depth-below variants (thresholds 15, 25) ---

def rsi_ext_011_rsi14_depth_below25(close: pd.Series) -> pd.Series:
    """Depth of RSI14 below 25 (between standard 20 and 30 thresholds)."""
    return (25.0 - _rsi(close, 14)).clip(lower=0.0)


def rsi_ext_012_rsi7_depth_below25(close: pd.Series) -> pd.Series:
    """Depth of RSI7 below 25 oversold threshold."""
    return (25.0 - _rsi(close, 7)).clip(lower=0.0)


def rsi_ext_013_rsi14_depth_below15(close: pd.Series) -> pd.Series:
    """Depth of RSI14 below 15 (severe capitulation level)."""
    return (15.0 - _rsi(close, 14)).clip(lower=0.0)


def rsi_ext_014_rsi7_depth_below15(close: pd.Series) -> pd.Series:
    """Depth of RSI7 below 15 (fast indicator at severe oversold)."""
    return (15.0 - _rsi(close, 7)).clip(lower=0.0)


def rsi_ext_015_rsi21_depth_below25(close: pd.Series) -> pd.Series:
    """Depth of RSI21 below 25."""
    return (25.0 - _rsi(close, _TD_MON)).clip(lower=0.0)


def rsi_ext_016_rsi63_depth_below25(close: pd.Series) -> pd.Series:
    """Depth of RSI63 below 25 (quarterly RSI in deep oversold)."""
    return (25.0 - _rsi(close, _TD_QTR)).clip(lower=0.0)


def rsi_ext_017_rsi14_depth_below35(close: pd.Series) -> pd.Series:
    """Depth of RSI14 below 35 (mild-oversold entry zone)."""
    return (35.0 - _rsi(close, 14)).clip(lower=0.0)


def rsi_ext_018_rsi14_below25_flag(close: pd.Series) -> pd.Series:
    """Binary flag: RSI14 < 25."""
    return (_rsi(close, 14) < 25.0).astype(float)


# --- Group C (019-026): Additional consecutive-day streaks ---

def rsi_ext_019_consec_days_rsi14_below25(close: pd.Series) -> pd.Series:
    """Consecutive days RSI14 has been below 25."""
    return _consec_streak(_rsi(close, 14) < 25.0)


def rsi_ext_020_consec_days_rsi14_below15(close: pd.Series) -> pd.Series:
    """Consecutive days RSI14 has been below 15."""
    return _consec_streak(_rsi(close, 14) < 15.0)


def rsi_ext_021_consec_days_rsi21_below20(close: pd.Series) -> pd.Series:
    """Consecutive days RSI21 has been below 20."""
    return _consec_streak(_rsi(close, _TD_MON) < 20.0)


def rsi_ext_022_consec_days_rsi45_below40(close: pd.Series) -> pd.Series:
    """Consecutive days RSI45 has been below 40 (mid-horizon oversold streak)."""
    return _consec_streak(_rsi(close, 45) < 40.0)


def rsi_ext_023_consec_days_rsi10_below30(close: pd.Series) -> pd.Series:
    """Consecutive days RSI10 has been below 30."""
    return _consec_streak(_rsi(close, 10) < 30.0)


def rsi_ext_024_consec_days_rsi7_below15(close: pd.Series) -> pd.Series:
    """Consecutive days RSI7 has been below 15."""
    return _consec_streak(_rsi(close, 7) < 15.0)


def rsi_ext_025_consec_days_rsi7_below10(close: pd.Series) -> pd.Series:
    """Consecutive days RSI7 has been below 10 (extreme fast-RSI streak)."""
    return _consec_streak(_rsi(close, 7) < 10.0)


def rsi_ext_026_consec_days_rsi21_below40(close: pd.Series) -> pd.Series:
    """Consecutive days RSI21 has been below 40 — already 027 exists for <40 but that's rsi21; net-new phrasing: max of that streak over 63d."""
    streak = _consec_streak(_rsi(close, _TD_MON) < 40.0)
    return _rolling_max(streak, _TD_QTR)


# --- Group D (027-032): Time-since-extreme for additional variants ---

def rsi_ext_027_time_since_rsi21_last_below30(close: pd.Series) -> pd.Series:
    """Days elapsed since RSI21 was last below 30."""
    return _time_since_below(_rsi(close, _TD_MON), 30.0)


def rsi_ext_028_time_since_rsi63_last_below40(close: pd.Series) -> pd.Series:
    """Days elapsed since RSI63 was last below 40."""
    return _time_since_below(_rsi(close, _TD_QTR), 40.0)


def rsi_ext_029_time_since_rsi14_last_below25(close: pd.Series) -> pd.Series:
    """Days elapsed since RSI14 was last below 25."""
    return _time_since_below(_rsi(close, 14), 25.0)


def rsi_ext_030_time_since_rsi7_last_below15(close: pd.Series) -> pd.Series:
    """Days elapsed since RSI7 was last below 15 (severe fast-RSI extreme)."""
    return _time_since_below(_rsi(close, 7), 15.0)


def rsi_ext_031_time_since_rsi14_last_below15(close: pd.Series) -> pd.Series:
    """Days elapsed since RSI14 was last below 15 (severe capitulation)."""
    return _time_since_below(_rsi(close, 14), 15.0)


def rsi_ext_032_time_since_rsi10_last_below30(close: pd.Series) -> pd.Series:
    """Days elapsed since RSI10 was last below 30."""
    return _time_since_below(_rsi(close, 10), 30.0)


# --- Group E (033-040): Rolling minimum RSI — new window/period combos ---

def rsi_ext_033_rsi14_min_5d(close: pd.Series) -> pd.Series:
    """Minimum RSI14 over trailing 5 days (weekly worst)."""
    return _rolling_min(_rsi(close, 14), _TD_WEEK)


def rsi_ext_034_rsi10_min_21d(close: pd.Series) -> pd.Series:
    """Minimum RSI10 over trailing 21 days."""
    return _rolling_min(_rsi(close, 10), _TD_MON)


def rsi_ext_035_rsi10_min_63d(close: pd.Series) -> pd.Series:
    """Minimum RSI10 over trailing 63 days."""
    return _rolling_min(_rsi(close, 10), _TD_QTR)


def rsi_ext_036_rsi12_min_21d(close: pd.Series) -> pd.Series:
    """Minimum RSI12 over trailing 21 days."""
    return _rolling_min(_rsi(close, 12), _TD_MON)


def rsi_ext_037_rsi45_min_252d(close: pd.Series) -> pd.Series:
    """Minimum RSI45 over trailing 252 days."""
    return _rolling_min(_rsi(close, 45), _TD_YEAR)


def rsi_ext_038_rsi21_min_21d(close: pd.Series) -> pd.Series:
    """Minimum RSI21 over trailing 21 days (same-window worst)."""
    return _rolling_min(_rsi(close, _TD_MON), _TD_MON)


def rsi_ext_039_rsi7_min_5d(close: pd.Series) -> pd.Series:
    """Minimum RSI7 over trailing 5 days (weekly trough)."""
    return _rolling_min(_rsi(close, 7), _TD_WEEK)


def rsi_ext_040_rsi7_expanding_min(close: pd.Series) -> pd.Series:
    """All-time expanding minimum of RSI7."""
    return _rsi(close, 7).expanding(min_periods=7).min()


# --- Group F (041-048): Percentile rank — new window/period combos ---

def rsi_ext_041_rsi14_pct_rank_21d(close: pd.Series) -> pd.Series:
    """Percentile rank of RSI14 within trailing 21-day distribution."""
    r = _rsi(close, 14)
    return r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)


def rsi_ext_042_rsi14_pct_rank_126d(close: pd.Series) -> pd.Series:
    """Percentile rank of RSI14 within trailing 126-day (half-year) distribution."""
    r = _rsi(close, 14)
    return r.rolling(_TD_HALF, min_periods=_TD_QTR).rank(pct=True)


def rsi_ext_043_rsi10_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of RSI10 within trailing 252-day distribution."""
    r = _rsi(close, 10)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rsi_ext_044_rsi12_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of RSI12 within trailing 252-day distribution."""
    r = _rsi(close, 12)
    return r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rsi_ext_045_rsi21_pct_rank_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of RSI21 within trailing 63-day distribution."""
    r = _rsi(close, _TD_MON)
    return r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def rsi_ext_046_rsi7_pct_rank_21d(close: pd.Series) -> pd.Series:
    """Percentile rank of RSI7 within trailing 21-day distribution."""
    r = _rsi(close, 7)
    return r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)


def rsi_ext_047_rsi7_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of RSI7."""
    return _rsi(close, 7).expanding(min_periods=7).rank(pct=True)


def rsi_ext_048_rsi21_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of RSI21."""
    return _rsi(close, _TD_MON).expanding(min_periods=_TD_MON).rank(pct=True)


# --- Group G (049-055): Z-score variants — new periods ---

def rsi_ext_049_rsi7_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of RSI7 relative to its 63-day distribution."""
    r = _rsi(close, 7)
    m = _rolling_mean(r, _TD_QTR)
    s = _rolling_std(r, _TD_QTR)
    return _safe_div(r - m, s)


def rsi_ext_050_rsi21_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of RSI21 relative to its 252-day distribution."""
    r = _rsi(close, _TD_MON)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    return _safe_div(r - m, s)


def rsi_ext_051_rsi63_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of RSI63 relative to its 252-day distribution."""
    r = _rsi(close, _TD_QTR)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    return _safe_div(r - m, s)


def rsi_ext_052_rsi10_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of RSI10 relative to its 252-day distribution."""
    r = _rsi(close, 10)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    return _safe_div(r - m, s)


def rsi_ext_053_rsi14_zscore_21d(close: pd.Series) -> pd.Series:
    """Z-score of RSI14 relative to its trailing 21-day distribution."""
    r = _rsi(close, 14)
    m = _rolling_mean(r, _TD_MON)
    s = _rolling_std(r, _TD_MON)
    return _safe_div(r - m, s)


def rsi_ext_054_rsi14_zscore_126d(close: pd.Series) -> pd.Series:
    """Z-score of RSI14 relative to its trailing 126-day (half-year) distribution."""
    r = _rsi(close, 14)
    m = _rolling_mean(r, _TD_HALF)
    s = _rolling_std(r, _TD_HALF)
    return _safe_div(r - m, s)


def rsi_ext_055_rsi7_expanding_zscore(close: pd.Series) -> pd.Series:
    """Expanding all-history z-score of RSI7."""
    r = _rsi(close, 7)
    m = r.expanding(min_periods=7).mean()
    s = r.expanding(min_periods=7).std()
    return _safe_div(r - m, s)


# --- Group H (056-062): Volume-weighted RSI (VRSI) ---

def rsi_ext_056_vrsi14(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted RSI (14): gains/losses scaled by daily volume before Wilder smoothing."""
    return _vrsi(close, volume, 14)


def rsi_ext_057_vrsi7(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted RSI (7): fast volume-weighted oversold signal."""
    return _vrsi(close, volume, 7)


def rsi_ext_058_vrsi14_depth_below30(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Depth of VRSI(14) below 30 oversold threshold."""
    return (30.0 - _vrsi(close, volume, 14)).clip(lower=0.0)


def rsi_ext_059_vrsi14_below30_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: VRSI(14) < 30 (volume-weighted oversold)."""
    return (_vrsi(close, volume, 14) < 30.0).astype(float)


def rsi_ext_060_vrsi14_consec_below30(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days VRSI(14) has been below 30."""
    return _consec_streak(_vrsi(close, volume, 14) < 30.0)


def rsi_ext_061_vrsi7_below30_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: VRSI(7) < 30."""
    return (_vrsi(close, volume, 7) < 30.0).astype(float)


def rsi_ext_062_vrsi14_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of VRSI(14) relative to its 252-day distribution."""
    r = _vrsi(close, volume, 14)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    return _safe_div(r - m, s)


# --- Group I (063-067): RSI on open and weighted-close price series ---

def rsi_ext_063_rsi14_on_open(open: pd.Series) -> pd.Series:
    """Wilder RSI14 computed on open prices."""
    return _rsi(open, 14)


def rsi_ext_064_rsi14_on_open_depth_below30(open: pd.Series) -> pd.Series:
    """Depth of RSI14-of-open prices below 30."""
    return (30.0 - _rsi(open, 14)).clip(lower=0.0)


def rsi_ext_065_rsi14_weighted_close(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """RSI14 of weighted close (H+L+2*C)/4."""
    wc = (high + low + 2.0 * close) / 4.0
    return _rsi(wc, 14)


def rsi_ext_066_rsi14_weighted_close_depth_below30(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Depth of RSI14-of-weighted-close below 30."""
    wc = (high + low + 2.0 * close) / 4.0
    return (30.0 - _rsi(wc, 14)).clip(lower=0.0)


def rsi_ext_067_rsi14_hl_midpoint(high: pd.Series, low: pd.Series) -> pd.Series:
    """RSI14 computed on daily high-low midpoint (H+L)/2."""
    mid = (high + low) / 2.0
    return _rsi(mid, 14)


# --- Group J (068-073): Cross-RSI confluence features ---

def rsi_ext_068_confluence_count_below30(close: pd.Series) -> pd.Series:
    """Count of RSI variants (RSI5, RSI10, RSI14, RSI21, RSI63) simultaneously below 30."""
    flags = [
        (_rsi(close, _TD_WEEK) < 30.0).astype(float),
        (_rsi(close, 10) < 30.0).astype(float),
        (_rsi(close, 14) < 30.0).astype(float),
        (_rsi(close, _TD_MON) < 30.0).astype(float),
        (_rsi(close, _TD_QTR) < 30.0).astype(float),
    ]
    result = flags[0]
    for f in flags[1:]:
        result = result + f
    return result


def rsi_ext_069_confluence_depth_sum_5variants(close: pd.Series) -> pd.Series:
    """Sum of depth-below-30 across RSI5, RSI10, RSI14, RSI21, RSI63 (5-variant distress)."""
    depths = [
        (30.0 - _rsi(close, _TD_WEEK)).clip(lower=0.0),
        (30.0 - _rsi(close, 10)).clip(lower=0.0),
        (30.0 - _rsi(close, 14)).clip(lower=0.0),
        (30.0 - _rsi(close, _TD_MON)).clip(lower=0.0),
        (30.0 - _rsi(close, _TD_QTR)).clip(lower=0.0),
    ]
    result = depths[0]
    for d in depths[1:]:
        result = result + d
    return result


def rsi_ext_070_rsi_all4_below30_flag(close: pd.Series) -> pd.Series:
    """Binary flag: RSI5, RSI14, RSI21, RSI63 ALL simultaneously below 30."""
    r5 = _rsi(close, _TD_WEEK)
    r14 = _rsi(close, 14)
    r21 = _rsi(close, _TD_MON)
    r63 = _rsi(close, _TD_QTR)
    return ((r5 < 30.0) & (r14 < 30.0) & (r21 < 30.0) & (r63 < 30.0)).astype(float)


def rsi_ext_071_cutler_vs_wilder_rsi14_diff(close: pd.Series) -> pd.Series:
    """Difference: Cutler RSI14 minus Wilder RSI14 (method divergence, SMA vs Wilder)."""
    return _rsi_sma(close, 14) - _rsi(close, 14)


def rsi_ext_072_rsi21_minus_rsi63(close: pd.Series) -> pd.Series:
    """RSI21 minus RSI63 (monthly vs quarterly momentum spread)."""
    return _rsi(close, _TD_MON) - _rsi(close, _TD_QTR)


def rsi_ext_073_rsi2_minus_rsi14(close: pd.Series) -> pd.Series:
    """RSI2 minus RSI14 (ultra-short vs standard — mean-reversion divergence)."""
    return _rsi(close, 2) - _rsi(close, 14)


# --- Group K (074): RSI regime flag and final composite ---

def rsi_ext_074_rsi14_bear_regime_flag(close: pd.Series) -> pd.Series:
    """Bear regime flag: RSI14 has been below 50 for at least 10 of the last 21 days."""
    r = _rsi(close, 14)
    count_below50 = _rolling_sum((r < 50.0).astype(float), _TD_MON)
    return (count_below50 >= 10.0).astype(float)


def rsi_ext_075_rsi14_capitulation_composite(close: pd.Series) -> pd.Series:
    """Capitulation composite: weighted sum normalizing RSI14 depth, z-score and pct-rank.
    Score = depth_below30/30 + (1 - pct_rank_252d) + abs(zscore_252d).clip(0,3)/3.
    Higher = more extreme oversold."""
    r = _rsi(close, 14)
    depth = (30.0 - r).clip(lower=0.0) / 30.0
    pct_rank = r.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    z = _safe_div(r - m, s).abs().clip(upper=3.0) / 3.0
    return depth + (1.0 - pct_rank.fillna(0.5)) + z


# ── Registry ──────────────────────────────────────────────────────────────────

RSI_EXTREMES_EXTENDED_REGISTRY_001_075 = {
    "rsi_ext_001_rsi10": {"inputs": ["close"], "func": rsi_ext_001_rsi10},
    "rsi_ext_002_rsi12": {"inputs": ["close"], "func": rsi_ext_002_rsi12},
    "rsi_ext_003_rsi45": {"inputs": ["close"], "func": rsi_ext_003_rsi45},
    "rsi_ext_004_rsi180": {"inputs": ["close"], "func": rsi_ext_004_rsi180},
    "rsi_ext_005_rsi252": {"inputs": ["close"], "func": rsi_ext_005_rsi252},
    "rsi_ext_006_rsi10_depth_below30": {"inputs": ["close"], "func": rsi_ext_006_rsi10_depth_below30},
    "rsi_ext_007_rsi12_depth_below30": {"inputs": ["close"], "func": rsi_ext_007_rsi12_depth_below30},
    "rsi_ext_008_rsi45_depth_below40": {"inputs": ["close"], "func": rsi_ext_008_rsi45_depth_below40},
    "rsi_ext_009_rsi10_consec_below30": {"inputs": ["close"], "func": rsi_ext_009_rsi10_consec_below30},
    "rsi_ext_010_rsi12_consec_below30": {"inputs": ["close"], "func": rsi_ext_010_rsi12_consec_below30},
    "rsi_ext_011_rsi14_depth_below25": {"inputs": ["close"], "func": rsi_ext_011_rsi14_depth_below25},
    "rsi_ext_012_rsi7_depth_below25": {"inputs": ["close"], "func": rsi_ext_012_rsi7_depth_below25},
    "rsi_ext_013_rsi14_depth_below15": {"inputs": ["close"], "func": rsi_ext_013_rsi14_depth_below15},
    "rsi_ext_014_rsi7_depth_below15": {"inputs": ["close"], "func": rsi_ext_014_rsi7_depth_below15},
    "rsi_ext_015_rsi21_depth_below25": {"inputs": ["close"], "func": rsi_ext_015_rsi21_depth_below25},
    "rsi_ext_016_rsi63_depth_below25": {"inputs": ["close"], "func": rsi_ext_016_rsi63_depth_below25},
    "rsi_ext_017_rsi14_depth_below35": {"inputs": ["close"], "func": rsi_ext_017_rsi14_depth_below35},
    "rsi_ext_018_rsi14_below25_flag": {"inputs": ["close"], "func": rsi_ext_018_rsi14_below25_flag},
    "rsi_ext_019_consec_days_rsi14_below25": {"inputs": ["close"], "func": rsi_ext_019_consec_days_rsi14_below25},
    "rsi_ext_020_consec_days_rsi14_below15": {"inputs": ["close"], "func": rsi_ext_020_consec_days_rsi14_below15},
    "rsi_ext_021_consec_days_rsi21_below20": {"inputs": ["close"], "func": rsi_ext_021_consec_days_rsi21_below20},
    "rsi_ext_022_consec_days_rsi45_below40": {"inputs": ["close"], "func": rsi_ext_022_consec_days_rsi45_below40},
    "rsi_ext_023_consec_days_rsi10_below30": {"inputs": ["close"], "func": rsi_ext_023_consec_days_rsi10_below30},
    "rsi_ext_024_consec_days_rsi7_below15": {"inputs": ["close"], "func": rsi_ext_024_consec_days_rsi7_below15},
    "rsi_ext_025_consec_days_rsi7_below10": {"inputs": ["close"], "func": rsi_ext_025_consec_days_rsi7_below10},
    "rsi_ext_026_consec_days_rsi21_below40_max_63d": {"inputs": ["close"], "func": rsi_ext_026_consec_days_rsi21_below40},
    "rsi_ext_027_time_since_rsi21_last_below30": {"inputs": ["close"], "func": rsi_ext_027_time_since_rsi21_last_below30},
    "rsi_ext_028_time_since_rsi63_last_below40": {"inputs": ["close"], "func": rsi_ext_028_time_since_rsi63_last_below40},
    "rsi_ext_029_time_since_rsi14_last_below25": {"inputs": ["close"], "func": rsi_ext_029_time_since_rsi14_last_below25},
    "rsi_ext_030_time_since_rsi7_last_below15": {"inputs": ["close"], "func": rsi_ext_030_time_since_rsi7_last_below15},
    "rsi_ext_031_time_since_rsi14_last_below15": {"inputs": ["close"], "func": rsi_ext_031_time_since_rsi14_last_below15},
    "rsi_ext_032_time_since_rsi10_last_below30": {"inputs": ["close"], "func": rsi_ext_032_time_since_rsi10_last_below30},
    "rsi_ext_033_rsi14_min_5d": {"inputs": ["close"], "func": rsi_ext_033_rsi14_min_5d},
    "rsi_ext_034_rsi10_min_21d": {"inputs": ["close"], "func": rsi_ext_034_rsi10_min_21d},
    "rsi_ext_035_rsi10_min_63d": {"inputs": ["close"], "func": rsi_ext_035_rsi10_min_63d},
    "rsi_ext_036_rsi12_min_21d": {"inputs": ["close"], "func": rsi_ext_036_rsi12_min_21d},
    "rsi_ext_037_rsi45_min_252d": {"inputs": ["close"], "func": rsi_ext_037_rsi45_min_252d},
    "rsi_ext_038_rsi21_min_21d": {"inputs": ["close"], "func": rsi_ext_038_rsi21_min_21d},
    "rsi_ext_039_rsi7_min_5d": {"inputs": ["close"], "func": rsi_ext_039_rsi7_min_5d},
    "rsi_ext_040_rsi7_expanding_min": {"inputs": ["close"], "func": rsi_ext_040_rsi7_expanding_min},
    "rsi_ext_041_rsi14_pct_rank_21d": {"inputs": ["close"], "func": rsi_ext_041_rsi14_pct_rank_21d},
    "rsi_ext_042_rsi14_pct_rank_126d": {"inputs": ["close"], "func": rsi_ext_042_rsi14_pct_rank_126d},
    "rsi_ext_043_rsi10_pct_rank_252d": {"inputs": ["close"], "func": rsi_ext_043_rsi10_pct_rank_252d},
    "rsi_ext_044_rsi12_pct_rank_252d": {"inputs": ["close"], "func": rsi_ext_044_rsi12_pct_rank_252d},
    "rsi_ext_045_rsi21_pct_rank_63d": {"inputs": ["close"], "func": rsi_ext_045_rsi21_pct_rank_63d},
    "rsi_ext_046_rsi7_pct_rank_21d": {"inputs": ["close"], "func": rsi_ext_046_rsi7_pct_rank_21d},
    "rsi_ext_047_rsi7_expanding_pct_rank": {"inputs": ["close"], "func": rsi_ext_047_rsi7_expanding_pct_rank},
    "rsi_ext_048_rsi21_expanding_pct_rank": {"inputs": ["close"], "func": rsi_ext_048_rsi21_expanding_pct_rank},
    "rsi_ext_049_rsi7_zscore_63d": {"inputs": ["close"], "func": rsi_ext_049_rsi7_zscore_63d},
    "rsi_ext_050_rsi21_zscore_252d": {"inputs": ["close"], "func": rsi_ext_050_rsi21_zscore_252d},
    "rsi_ext_051_rsi63_zscore_252d": {"inputs": ["close"], "func": rsi_ext_051_rsi63_zscore_252d},
    "rsi_ext_052_rsi10_zscore_252d": {"inputs": ["close"], "func": rsi_ext_052_rsi10_zscore_252d},
    "rsi_ext_053_rsi14_zscore_21d": {"inputs": ["close"], "func": rsi_ext_053_rsi14_zscore_21d},
    "rsi_ext_054_rsi14_zscore_126d": {"inputs": ["close"], "func": rsi_ext_054_rsi14_zscore_126d},
    "rsi_ext_055_rsi7_expanding_zscore": {"inputs": ["close"], "func": rsi_ext_055_rsi7_expanding_zscore},
    "rsi_ext_056_vrsi14": {"inputs": ["close", "volume"], "func": rsi_ext_056_vrsi14},
    "rsi_ext_057_vrsi7": {"inputs": ["close", "volume"], "func": rsi_ext_057_vrsi7},
    "rsi_ext_058_vrsi14_depth_below30": {"inputs": ["close", "volume"], "func": rsi_ext_058_vrsi14_depth_below30},
    "rsi_ext_059_vrsi14_below30_flag": {"inputs": ["close", "volume"], "func": rsi_ext_059_vrsi14_below30_flag},
    "rsi_ext_060_vrsi14_consec_below30": {"inputs": ["close", "volume"], "func": rsi_ext_060_vrsi14_consec_below30},
    "rsi_ext_061_vrsi7_below30_flag": {"inputs": ["close", "volume"], "func": rsi_ext_061_vrsi7_below30_flag},
    "rsi_ext_062_vrsi14_zscore_252d": {"inputs": ["close", "volume"], "func": rsi_ext_062_vrsi14_zscore_252d},
    "rsi_ext_063_rsi14_on_open": {"inputs": ["open"], "func": rsi_ext_063_rsi14_on_open},
    "rsi_ext_064_rsi14_on_open_depth_below30": {"inputs": ["open"], "func": rsi_ext_064_rsi14_on_open_depth_below30},
    "rsi_ext_065_rsi14_weighted_close": {"inputs": ["close", "high", "low"], "func": rsi_ext_065_rsi14_weighted_close},
    "rsi_ext_066_rsi14_weighted_close_depth_below30": {"inputs": ["close", "high", "low"], "func": rsi_ext_066_rsi14_weighted_close_depth_below30},
    "rsi_ext_067_rsi14_hl_midpoint": {"inputs": ["high", "low"], "func": rsi_ext_067_rsi14_hl_midpoint},
    "rsi_ext_068_confluence_count_below30": {"inputs": ["close"], "func": rsi_ext_068_confluence_count_below30},
    "rsi_ext_069_confluence_depth_sum_5variants": {"inputs": ["close"], "func": rsi_ext_069_confluence_depth_sum_5variants},
    "rsi_ext_070_rsi_all4_below30_flag": {"inputs": ["close"], "func": rsi_ext_070_rsi_all4_below30_flag},
    "rsi_ext_071_cutler_vs_wilder_rsi14_diff": {"inputs": ["close"], "func": rsi_ext_071_cutler_vs_wilder_rsi14_diff},
    "rsi_ext_072_rsi21_minus_rsi63": {"inputs": ["close"], "func": rsi_ext_072_rsi21_minus_rsi63},
    "rsi_ext_073_rsi2_minus_rsi14": {"inputs": ["close"], "func": rsi_ext_073_rsi2_minus_rsi14},
    "rsi_ext_074_rsi14_bear_regime_flag": {"inputs": ["close"], "func": rsi_ext_074_rsi14_bear_regime_flag},
    "rsi_ext_075_rsi14_capitulation_composite": {"inputs": ["close"], "func": rsi_ext_075_rsi14_capitulation_composite},
}
