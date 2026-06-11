"""
33_trend_breakdown — Base Features 001-075
Domain: moving-average crossover events, death crosses, days-since-crossover,
        bearish-crossover counts, MACD line/signal crossovers, histogram sign-flips,
        ADX/DMI trend-strength collapse, Parabolic SAR flip events,
        Aroon oscillator bearish signals, MA slope turning negative.
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


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _days_since(cond: pd.Series) -> pd.Series:
    """Days since last True; 0 on True rows, rising integer on False rows."""
    result = pd.Series(np.nan, index=cond.index)
    counter = np.nan
    for i, v in enumerate(cond):
        if v:
            counter = 0
        elif not np.isnan(counter):
            counter += 1
        result.iloc[i] = counter
    return result.astype(float)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low  - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


def _macd_components(close: pd.Series):
    """Return (macd_line, signal_line, histogram)."""
    ema12 = _ewm_mean(close, 12)
    ema26 = _ewm_mean(close, 26)
    macd  = ema12 - ema26
    sig   = _ewm_mean(macd, 9)
    hist  = macd - sig
    return macd, sig, hist


def _adx_components(close: pd.Series, high: pd.Series, low: pd.Series, period: int = 14):
    """Return (adx, plus_di, minus_di) using Wilder smoothing."""
    tr  = _tr(close, high, low)
    dm_plus  = (high - high.shift(1)).clip(lower=0.0)
    dm_minus = (low.shift(1) - low).clip(lower=0.0)
    # zero out when the other direction is larger
    dm_plus  = dm_plus.where(dm_plus > dm_minus, 0.0)
    dm_minus = dm_minus.where(dm_minus > dm_plus, 0.0)
    atr   = tr.ewm(alpha=1/period, min_periods=period // 2, adjust=False).mean()
    sdi_p = dm_plus.ewm(alpha=1/period, min_periods=period // 2, adjust=False).mean()
    sdi_m = dm_minus.ewm(alpha=1/period, min_periods=period // 2, adjust=False).mean()
    di_p  = _safe_div(sdi_p, atr) * 100
    di_m  = _safe_div(sdi_m, atr) * 100
    dx    = _safe_div((di_p - di_m).abs(), (di_p + di_m).abs()) * 100
    adx   = dx.ewm(alpha=1/period, min_periods=period // 2, adjust=False).mean()
    return adx, di_p, di_m


def _parabolic_sar(high: pd.Series, low: pd.Series,
                   af_step: float = 0.02, af_max: float = 0.2):
    """
    Compute Parabolic SAR using an explicit forward-only loop.
    Returns (sar_series, trend_series) where trend=1 means uptrend (price above SAR),
    trend=-1 means downtrend (price below SAR). Backward-looking only.
    """
    n = len(high)
    hi = high.values
    lo = low.values
    sar = np.full(n, np.nan)
    trend = np.full(n, np.nan)

    if n < 2:
        return (pd.Series(sar, index=high.index),
                pd.Series(trend, index=high.index))

    # Initialise at bar 1 based on bar 0 direction assumption
    # Start bullish
    is_bull = True
    ep = hi[0]   # extreme point
    af = af_step
    sar[0] = lo[0]
    trend[0] = 1.0

    for i in range(1, n):
        prev_sar = sar[i - 1]
        if is_bull:
            new_sar = prev_sar + af * (ep - prev_sar)
            # SAR cannot be above prior two lows
            new_sar = min(new_sar, lo[i - 1])
            if i >= 2:
                new_sar = min(new_sar, lo[i - 2])
            if lo[i] < new_sar:
                # Flip to bearish
                is_bull = False
                new_sar = ep  # SAR jumps to prior extreme point
                ep = lo[i]
                af = af_step
                trend[i] = -1.0
            else:
                trend[i] = 1.0
                if hi[i] > ep:
                    ep = hi[i]
                    af = min(af + af_step, af_max)
        else:
            new_sar = prev_sar + af * (ep - prev_sar)
            # SAR cannot be below prior two highs
            new_sar = max(new_sar, hi[i - 1])
            if i >= 2:
                new_sar = max(new_sar, hi[i - 2])
            if hi[i] > new_sar:
                # Flip to bullish
                is_bull = True
                new_sar = ep  # SAR jumps to prior extreme point
                ep = hi[i]
                af = af_step
                trend[i] = 1.0
            else:
                trend[i] = -1.0
                if lo[i] < ep:
                    ep = lo[i]
                    af = min(af + af_step, af_max)
        sar[i] = new_sar

    return (pd.Series(sar, index=high.index),
            pd.Series(trend, index=high.index))


def _aroon(high: pd.Series, low: pd.Series, period: int):
    """
    Compute Aroon Up, Aroon Down, Aroon Oscillator for given period.
    Aroon Up  = 100 * (period - bars_since_period_high) / period
    Aroon Down= 100 * (period - bars_since_period_low)  / period
    Returns (aroon_up, aroon_down, aroon_osc).
    """
    w = period + 1  # include current bar

    def _bars_since_high(arr):
        idx = np.argmax(arr)
        return float(len(arr) - 1 - idx)

    def _bars_since_low(arr):
        idx = np.argmin(arr)
        return float(len(arr) - 1 - idx)

    bs_high = high.rolling(w, min_periods=w).apply(_bars_since_high, raw=True)
    bs_low  = low.rolling(w, min_periods=w).apply(_bars_since_low,  raw=True)

    up  = (period - bs_high) / period * 100
    dn  = (period - bs_low)  / period * 100
    osc = up - dn
    return up, dn, osc


# ── Feature functions 001-075 ──────────────────────────────────────────────────

# --- Group A (001-010): SMA crossover events — death cross / fast-below-slow ---

def tbd_001_sma50_below_sma200_flag(close: pd.Series) -> pd.Series:
    """Binary flag: SMA50 < SMA200 (death-cross state active)."""
    return ((_rolling_mean(close, 50) < _rolling_mean(close, 200)).astype(float))


def tbd_002_sma20_below_sma50_flag(close: pd.Series) -> pd.Series:
    """Binary flag: SMA20 < SMA50 (short-term death cross)."""
    return ((_rolling_mean(close, _TD_MON) < _rolling_mean(close, 50)).astype(float))


def tbd_003_sma20_below_sma200_flag(close: pd.Series) -> pd.Series:
    """Binary flag: SMA20 < SMA200 (fast MA deeply below slow MA)."""
    return ((_rolling_mean(close, _TD_MON) < _rolling_mean(close, 200)).astype(float))


def tbd_004_sma50_below_sma100_flag(close: pd.Series) -> pd.Series:
    """Binary flag: SMA50 < SMA100."""
    return ((_rolling_mean(close, 50) < _rolling_mean(close, 100)).astype(float))


def tbd_005_sma10_below_sma20_flag(close: pd.Series) -> pd.Series:
    """Binary flag: SMA10 < SMA20 (very-short death cross)."""
    return ((_rolling_mean(close, 10) < _rolling_mean(close, _TD_MON)).astype(float))


def tbd_006_triple_death_cross_flag(close: pd.Series) -> pd.Series:
    """Flag: SMA20 < SMA50 AND SMA50 < SMA200 simultaneously."""
    sma20  = _rolling_mean(close, _TD_MON)
    sma50  = _rolling_mean(close, 50)
    sma200 = _rolling_mean(close, 200)
    return ((sma20 < sma50) & (sma50 < sma200)).astype(float)


def tbd_007_death_cross_event(close: pd.Series) -> pd.Series:
    """Impulse flag: day SMA50 crosses below SMA200 (transition 0→1)."""
    sma50  = _rolling_mean(close, 50)
    sma200 = _rolling_mean(close, 200)
    below  = sma50 < sma200
    return (below & ~below.shift(1).fillna(False)).astype(float)


def tbd_008_sma20_below_sma50_event(close: pd.Series) -> pd.Series:
    """Impulse flag: day SMA20 crosses below SMA50."""
    sma20 = _rolling_mean(close, _TD_MON)
    sma50 = _rolling_mean(close, 50)
    below = sma20 < sma50
    return (below & ~below.shift(1).fillna(False)).astype(float)


def tbd_009_bearish_cross_count_252d(close: pd.Series) -> pd.Series:
    """Count of SMA50-below-SMA200 crossover events in trailing 252 days."""
    return _rolling_sum(tbd_007_death_cross_event(close), _TD_YEAR)


def tbd_010_bearish_cross_count_63d(close: pd.Series) -> pd.Series:
    """Count of SMA20-below-SMA50 crossover events in trailing 63 days."""
    return _rolling_sum(tbd_008_sma20_below_sma50_event(close), _TD_QTR)


# --- Group B (011-020): Days since crossover events ---

def tbd_011_days_since_death_cross(close: pd.Series) -> pd.Series:
    """Days elapsed since last SMA50-below-SMA200 crossover event."""
    return _days_since(tbd_007_death_cross_event(close))


def tbd_012_days_since_sma20_below_sma50(close: pd.Series) -> pd.Series:
    """Days elapsed since last SMA20-below-SMA50 crossover."""
    return _days_since(tbd_008_sma20_below_sma50_event(close))


def tbd_013_days_since_ema12_below_ema26(close: pd.Series) -> pd.Series:
    """Days elapsed since last EMA12-below-EMA26 crossover."""
    ema12 = _ewm_mean(close, 12)
    ema26 = _ewm_mean(close, 26)
    below = ema12 < ema26
    event = (below & ~below.shift(1).fillna(False))
    return _days_since(event)


def tbd_014_days_since_sma10_below_sma20(close: pd.Series) -> pd.Series:
    """Days elapsed since last SMA10-below-SMA20 crossover."""
    sma10 = _rolling_mean(close, 10)
    sma20 = _rolling_mean(close, _TD_MON)
    below = sma10 < sma20
    event = (below & ~below.shift(1).fillna(False))
    return _days_since(event)


def tbd_015_days_since_triple_death_cross(close: pd.Series) -> pd.Series:
    """Days elapsed since last triple death-cross formation."""
    return _days_since(tbd_006_triple_death_cross_flag(close).diff(1) > 0)


def tbd_016_days_since_sma50_below_sma100(close: pd.Series) -> pd.Series:
    """Days elapsed since last SMA50-below-SMA100 crossover."""
    sma50  = _rolling_mean(close, 50)
    sma100 = _rolling_mean(close, 100)
    below  = sma50 < sma100
    event  = (below & ~below.shift(1).fillna(False))
    return _days_since(event)


def tbd_017_days_since_last_golden_cross(close: pd.Series) -> pd.Series:
    """Days since last golden cross (SMA50 crossed above SMA200)."""
    sma50  = _rolling_mean(close, 50)
    sma200 = _rolling_mean(close, 200)
    above  = sma50 > sma200
    event  = (above & ~above.shift(1).fillna(False))
    return _days_since(event)


def tbd_018_death_cross_days_norm_252d(close: pd.Series) -> pd.Series:
    """Days-since-death-cross normalized by 252-day average gap between crosses."""
    ds = tbd_011_days_since_death_cross(close)
    avg = _rolling_mean(ds, _TD_YEAR)
    return _safe_div(ds, avg)


def tbd_019_multi_cross_composite_flag(close: pd.Series) -> pd.Series:
    """Flag: SMA20<SMA50 AND SMA50<SMA200 AND EMA12<EMA26 all simultaneously."""
    sma20  = _rolling_mean(close, _TD_MON)
    sma50  = _rolling_mean(close, 50)
    sma200 = _rolling_mean(close, 200)
    ema12  = _ewm_mean(close, 12)
    ema26  = _ewm_mean(close, 26)
    return ((sma20 < sma50) & (sma50 < sma200) & (ema12 < ema26)).astype(float)


def tbd_020_bearish_cross_density_252d(close: pd.Series) -> pd.Series:
    """Total bearish-cross events per 252 days (SMA20<SMA50 + SMA50<SMA200 events)."""
    e1 = tbd_007_death_cross_event(close)
    e2 = tbd_008_sma20_below_sma50_event(close)
    sma10 = _rolling_mean(close, 10)
    sma20 = _rolling_mean(close, _TD_MON)
    b3    = sma10 < sma20
    e3    = (b3 & ~b3.shift(1).fillna(False)).astype(float)
    return _rolling_sum(e1 + e2 + e3, _TD_YEAR)


# --- Group C (021-030): EMA crossover events and states ---

def tbd_021_ema12_below_ema26_flag(close: pd.Series) -> pd.Series:
    """Flag: EMA12 < EMA26 (MACD line negative state)."""
    return ((_ewm_mean(close, 12) < _ewm_mean(close, 26)).astype(float))


def tbd_022_ema20_below_ema50_flag(close: pd.Series) -> pd.Series:
    """Flag: EMA20 < EMA50."""
    return ((_ewm_mean(close, _TD_MON) < _ewm_mean(close, 50)).astype(float))


def tbd_023_ema50_below_ema200_flag(close: pd.Series) -> pd.Series:
    """Flag: EMA50 < EMA200 (EMA death-cross state)."""
    return ((_ewm_mean(close, 50) < _ewm_mean(close, 200)).astype(float))


def tbd_024_ema12_below_ema26_event(close: pd.Series) -> pd.Series:
    """Impulse flag: day EMA12 crosses below EMA26."""
    below = _ewm_mean(close, 12) < _ewm_mean(close, 26)
    return (below & ~below.shift(1).fillna(False)).astype(float)


def tbd_025_ema20_below_ema50_event(close: pd.Series) -> pd.Series:
    """Impulse flag: day EMA20 crosses below EMA50."""
    below = _ewm_mean(close, _TD_MON) < _ewm_mean(close, 50)
    return (below & ~below.shift(1).fillna(False)).astype(float)


def tbd_026_ema50_below_ema200_event(close: pd.Series) -> pd.Series:
    """Impulse flag: day EMA50 crosses below EMA200."""
    below = _ewm_mean(close, 50) < _ewm_mean(close, 200)
    return (below & ~below.shift(1).fillna(False)).astype(float)


def tbd_027_ema_bearish_cross_count_252d(close: pd.Series) -> pd.Series:
    """Count of EMA bearish crossover events (12/26, 20/50, 50/200) in 252 days."""
    e1 = tbd_024_ema12_below_ema26_event(close)
    e2 = tbd_025_ema20_below_ema50_event(close)
    e3 = tbd_026_ema50_below_ema200_event(close)
    return _rolling_sum(e1 + e2 + e3, _TD_YEAR)


def tbd_028_triple_ema_death_cross_flag(close: pd.Series) -> pd.Series:
    """Flag: EMA12<EMA26 AND EMA20<EMA50 AND EMA50<EMA200."""
    return ((_ewm_mean(close, 12) < _ewm_mean(close, 26)) &
            (_ewm_mean(close, _TD_MON) < _ewm_mean(close, 50)) &
            (_ewm_mean(close, 50) < _ewm_mean(close, 200))).astype(float)


def tbd_029_days_since_ema50_below_ema200(close: pd.Series) -> pd.Series:
    """Days since EMA50 crossed below EMA200."""
    return _days_since(tbd_026_ema50_below_ema200_event(close))


def tbd_030_ema_cross_count_63d(close: pd.Series) -> pd.Series:
    """Count of EMA12/26 and EMA20/50 bearish crossovers in trailing 63 days."""
    e1 = tbd_024_ema12_below_ema26_event(close)
    e2 = tbd_025_ema20_below_ema50_event(close)
    return _rolling_sum(e1 + e2, _TD_QTR)


# --- Group D (031-040): MACD crossover and histogram sign-flip events ---

def tbd_031_macd_below_signal_flag(close: pd.Series) -> pd.Series:
    """Flag: MACD line < signal line (bearish MACD cross state)."""
    macd, sig, _ = _macd_components(close)
    return ((macd < sig).astype(float))


def tbd_032_macd_histogram_negative_flag(close: pd.Series) -> pd.Series:
    """Flag: MACD histogram < 0."""
    _, _, hist = _macd_components(close)
    return ((hist < 0).astype(float))


def tbd_033_macd_cross_below_signal_event(close: pd.Series) -> pd.Series:
    """Impulse: MACD line crosses below signal line (bearish MACD cross)."""
    macd, sig, _ = _macd_components(close)
    below = macd < sig
    return (below & ~below.shift(1).fillna(False)).astype(float)


def tbd_034_macd_histogram_sign_flip_neg_event(close: pd.Series) -> pd.Series:
    """Impulse: MACD histogram flips from positive to negative."""
    _, _, hist = _macd_components(close)
    neg = hist < 0
    return (neg & ~neg.shift(1).fillna(False)).astype(float)


def tbd_035_days_since_macd_bearish_cross(close: pd.Series) -> pd.Series:
    """Days since MACD line crossed below signal line."""
    return _days_since(tbd_033_macd_cross_below_signal_event(close))


def tbd_036_days_since_macd_hist_neg_flip(close: pd.Series) -> pd.Series:
    """Days since MACD histogram flipped negative."""
    return _days_since(tbd_034_macd_histogram_sign_flip_neg_event(close))


def tbd_037_macd_bearish_cross_count_252d(close: pd.Series) -> pd.Series:
    """Count of MACD bearish-cross events in trailing 252 days."""
    return _rolling_sum(tbd_033_macd_cross_below_signal_event(close), _TD_YEAR)


def tbd_038_macd_histogram_neg_streak(close: pd.Series) -> pd.Series:
    """Consecutive days MACD histogram has been negative."""
    _, _, hist = _macd_components(close)
    return _consec_streak(hist < 0)


def tbd_039_macd_line_below_zero_flag(close: pd.Series) -> pd.Series:
    """Flag: MACD line itself < 0 (both MAs fully aligned bearish)."""
    macd, _, _ = _macd_components(close)
    return ((macd < 0).astype(float))


def tbd_040_macd_line_below_zero_event(close: pd.Series) -> pd.Series:
    """Impulse: MACD line crosses zero from above (deeper breakdown)."""
    macd, _, _ = _macd_components(close)
    neg = macd < 0
    return (neg & ~neg.shift(1).fillna(False)).astype(float)


# --- Group E (041-050): ADX/DMI trend-strength collapse ---

def tbd_041_adx14_below_25_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: ADX(14) < 25 (trend strength weak / collapsed)."""
    adx, _, _ = _adx_components(close, high, low, 14)
    return ((adx < 25).astype(float))


def tbd_042_adx14_below_20_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: ADX(14) < 20 (very weak trend)."""
    adx, _, _ = _adx_components(close, high, low, 14)
    return ((adx < 20).astype(float))


def tbd_043_adx14_falling_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: ADX(14) today < ADX(14) 5 days ago (trend weakening)."""
    adx, _, _ = _adx_components(close, high, low, 14)
    return ((adx < adx.shift(_TD_WEEK)).astype(float))


def tbd_044_dmi_minus_above_plus_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: DI- > DI+ (bearish DMI alignment)."""
    _, di_p, di_m = _adx_components(close, high, low, 14)
    return ((di_m > di_p).astype(float))


def tbd_045_dmi_bearish_cross_event(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Impulse: DI- crosses above DI+ (bearish DMI crossover)."""
    _, di_p, di_m = _adx_components(close, high, low, 14)
    above = di_m > di_p
    return (above & ~above.shift(1).fillna(False)).astype(float)


def tbd_046_days_since_dmi_bearish_cross(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Days since DI- last crossed above DI+."""
    return _days_since(tbd_045_dmi_bearish_cross_event(close, high, low))


def tbd_047_adx14_collapse_from_peak_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ADX drop from 63-day peak (trend dissipation magnitude)."""
    adx, _, _ = _adx_components(close, high, low, 14)
    peak = _rolling_max(adx, _TD_QTR)
    return peak - adx


def tbd_048_adx14_pct_below_peak_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ADX as pct of 252-day peak ADX (relative collapse)."""
    adx, _, _ = _adx_components(close, high, low, 14)
    peak = _rolling_max(adx, _TD_YEAR)
    return _safe_div(adx, peak)


def tbd_049_dmi_minus_above_plus_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Days with DI->DI+ in trailing 63 days (bearish DMI prevalence)."""
    _, di_p, di_m = _adx_components(close, high, low, 14)
    return _rolling_count_true(di_m > di_p, _TD_QTR)


def tbd_050_adx_dmi_combined_breakdown_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: ADX<25 AND DI->DI+ (weak trend AND bearish direction)."""
    adx, di_p, di_m = _adx_components(close, high, low, 14)
    return ((adx < 25) & (di_m > di_p)).astype(float)


# --- Group F (051-060): MA slope sign-change events ---

def tbd_051_sma20_slope_negative_flag(close: pd.Series) -> pd.Series:
    """Flag: SMA20 today < SMA20 yesterday (slope turned negative)."""
    sma20 = _rolling_mean(close, _TD_MON)
    return ((sma20 < sma20.shift(1)).astype(float))


def tbd_052_sma50_slope_negative_flag(close: pd.Series) -> pd.Series:
    """Flag: SMA50 slope negative (declining medium-term trend)."""
    sma50 = _rolling_mean(close, 50)
    return ((sma50 < sma50.shift(1)).astype(float))


def tbd_053_sma200_slope_negative_flag(close: pd.Series) -> pd.Series:
    """Flag: SMA200 slope negative (long-term trend turned down)."""
    sma200 = _rolling_mean(close, 200)
    return ((sma200 < sma200.shift(1)).astype(float))


def tbd_054_ema12_slope_negative_flag(close: pd.Series) -> pd.Series:
    """Flag: EMA12 slope negative (fast EMA declining)."""
    ema12 = _ewm_mean(close, 12)
    return ((ema12 < ema12.shift(1)).astype(float))


def tbd_055_ema26_slope_negative_flag(close: pd.Series) -> pd.Series:
    """Flag: EMA26 slope negative."""
    ema26 = _ewm_mean(close, 26)
    return ((ema26 < ema26.shift(1)).astype(float))


def tbd_056_sma200_slope_neg_event(close: pd.Series) -> pd.Series:
    """Impulse: SMA200 slope flips from positive to negative."""
    sma200 = _rolling_mean(close, 200)
    neg = sma200 < sma200.shift(1)
    return (neg & ~neg.shift(1).fillna(False)).astype(float)


def tbd_057_all_ma_slopes_negative_flag(close: pd.Series) -> pd.Series:
    """Flag: SMA20, SMA50, SMA200 all have negative slopes simultaneously."""
    sma20  = _rolling_mean(close, _TD_MON)
    sma50  = _rolling_mean(close, 50)
    sma200 = _rolling_mean(close, 200)
    return ((sma20 < sma20.shift(1)) &
            (sma50 < sma50.shift(1)) &
            (sma200 < sma200.shift(1))).astype(float)


def tbd_058_sma20_neg_slope_streak(close: pd.Series) -> pd.Series:
    """Consecutive days SMA20 slope has been negative."""
    sma20 = _rolling_mean(close, _TD_MON)
    return _consec_streak(sma20 < sma20.shift(1))


def tbd_059_sma200_neg_slope_streak(close: pd.Series) -> pd.Series:
    """Consecutive days SMA200 slope has been negative."""
    sma200 = _rolling_mean(close, 200)
    return _consec_streak(sma200 < sma200.shift(1))


def tbd_060_days_since_sma200_slope_turned_neg(close: pd.Series) -> pd.Series:
    """Days since SMA200 slope last flipped from positive to negative."""
    return _days_since(tbd_056_sma200_slope_neg_event(close))


# --- Group G (061-068): Parabolic SAR — flip events, distance, bars-since ---

def tbd_061_psar_price_below_sar_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: close price is below Parabolic SAR (bearish/downtrend state)."""
    sar, trend = _parabolic_sar(high, low)
    return ((trend < 0).astype(float))


def tbd_062_psar_flip_to_bearish_event(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Impulse: Parabolic SAR flips from bullish to bearish (trend=-1 transition)."""
    _, trend = _parabolic_sar(high, low)
    bearish = trend < 0
    return (bearish & ~bearish.shift(1).fillna(False)).astype(float)


def tbd_063_psar_bars_since_bearish_flip(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since last Parabolic SAR flip to bearish."""
    return _days_since(tbd_062_psar_flip_to_bearish_event(close, high, low))


def tbd_064_psar_distance_from_price(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Signed distance (close - SAR) / close; negative = price below SAR (bearish)."""
    sar, _ = _parabolic_sar(high, low)
    return _safe_div(close - sar, close)


def tbd_065_psar_bearish_flip_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of Parabolic SAR bearish-flip events in trailing 63 days."""
    return _rolling_sum(tbd_062_psar_flip_to_bearish_event(close, high, low), _TD_QTR)


def tbd_066_psar_bearish_streak(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive bars Parabolic SAR has been in bearish (downtrend) state."""
    _, trend = _parabolic_sar(high, low)
    return _consec_streak(trend < 0)


def tbd_067_psar_bearish_fraction_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days Parabolic SAR was in bearish state."""
    _, trend = _parabolic_sar(high, low)
    return _rolling_count_true(trend < 0, _TD_QTR) / _TD_QTR


def tbd_068_psar_distance_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of (close - SAR)/close distance over trailing 63 days."""
    dist = tbd_064_psar_distance_from_price(close, high, low)
    m = _rolling_mean(dist, _TD_QTR)
    s = _rolling_std(dist, _TD_QTR)
    return _safe_div(dist - m, s)


# --- Group H (069-075): Aroon oscillator — bearish dominance ---

def tbd_069_aroon_down14_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Aroon Down(14) > Aroon Up(14) (bearish Aroon dominance, 14-period)."""
    up, dn, _ = _aroon(high, low, 14)
    return ((dn > up).astype(float))


def tbd_070_aroon_oscillator14_negative_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Aroon Oscillator(14) < 0 (net bearish momentum)."""
    _, _, osc = _aroon(high, low, 14)
    return ((osc < 0).astype(float))


def tbd_071_aroon_down25_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Aroon Down(25) > Aroon Up(25) (bearish Aroon dominance, 25-period)."""
    up, dn, _ = _aroon(high, low, 25)
    return ((dn > up).astype(float))


def tbd_072_aroon_oscillator14_value(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon Oscillator value (14-period): Up14 - Down14; negative = bearish."""
    _, _, osc = _aroon(high, low, 14)
    return osc


def tbd_073_aroon_oscillator25_value(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon Oscillator value (25-period): Up25 - Down25; negative = bearish."""
    _, _, osc = _aroon(high, low, 25)
    return osc


def tbd_074_aroon_down14_above_90_flag(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: Aroon Down(14) >= 90 (strong bearish recent-low signal)."""
    _, dn, _ = _aroon(high, low, 14)
    return ((dn >= 90).astype(float))


def tbd_075_aroon_bearish_cross_event14(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Impulse: Aroon Down(14) crosses above Aroon Up(14) (bearish cross event)."""
    up, dn, _ = _aroon(high, low, 14)
    bearish = dn > up
    return (bearish & ~bearish.shift(1).fillna(False)).astype(float)


# ── Registry ──────────────────────────────────────────────────────────────────

TREND_BREAKDOWN_REGISTRY_001_075 = {
    "tbd_001_sma50_below_sma200_flag": {"inputs": ["close"], "func": tbd_001_sma50_below_sma200_flag},
    "tbd_002_sma20_below_sma50_flag": {"inputs": ["close"], "func": tbd_002_sma20_below_sma50_flag},
    "tbd_003_sma20_below_sma200_flag": {"inputs": ["close"], "func": tbd_003_sma20_below_sma200_flag},
    "tbd_004_sma50_below_sma100_flag": {"inputs": ["close"], "func": tbd_004_sma50_below_sma100_flag},
    "tbd_005_sma10_below_sma20_flag": {"inputs": ["close"], "func": tbd_005_sma10_below_sma20_flag},
    "tbd_006_triple_death_cross_flag": {"inputs": ["close"], "func": tbd_006_triple_death_cross_flag},
    "tbd_007_death_cross_event": {"inputs": ["close"], "func": tbd_007_death_cross_event},
    "tbd_008_sma20_below_sma50_event": {"inputs": ["close"], "func": tbd_008_sma20_below_sma50_event},
    "tbd_009_bearish_cross_count_252d": {"inputs": ["close"], "func": tbd_009_bearish_cross_count_252d},
    "tbd_010_bearish_cross_count_63d": {"inputs": ["close"], "func": tbd_010_bearish_cross_count_63d},
    "tbd_011_days_since_death_cross": {"inputs": ["close"], "func": tbd_011_days_since_death_cross},
    "tbd_012_days_since_sma20_below_sma50": {"inputs": ["close"], "func": tbd_012_days_since_sma20_below_sma50},
    "tbd_013_days_since_ema12_below_ema26": {"inputs": ["close"], "func": tbd_013_days_since_ema12_below_ema26},
    "tbd_014_days_since_sma10_below_sma20": {"inputs": ["close"], "func": tbd_014_days_since_sma10_below_sma20},
    "tbd_015_days_since_triple_death_cross": {"inputs": ["close"], "func": tbd_015_days_since_triple_death_cross},
    "tbd_016_days_since_sma50_below_sma100": {"inputs": ["close"], "func": tbd_016_days_since_sma50_below_sma100},
    "tbd_017_days_since_last_golden_cross": {"inputs": ["close"], "func": tbd_017_days_since_last_golden_cross},
    "tbd_018_death_cross_days_norm_252d": {"inputs": ["close"], "func": tbd_018_death_cross_days_norm_252d},
    "tbd_019_multi_cross_composite_flag": {"inputs": ["close"], "func": tbd_019_multi_cross_composite_flag},
    "tbd_020_bearish_cross_density_252d": {"inputs": ["close"], "func": tbd_020_bearish_cross_density_252d},
    "tbd_021_ema12_below_ema26_flag": {"inputs": ["close"], "func": tbd_021_ema12_below_ema26_flag},
    "tbd_022_ema20_below_ema50_flag": {"inputs": ["close"], "func": tbd_022_ema20_below_ema50_flag},
    "tbd_023_ema50_below_ema200_flag": {"inputs": ["close"], "func": tbd_023_ema50_below_ema200_flag},
    "tbd_024_ema12_below_ema26_event": {"inputs": ["close"], "func": tbd_024_ema12_below_ema26_event},
    "tbd_025_ema20_below_ema50_event": {"inputs": ["close"], "func": tbd_025_ema20_below_ema50_event},
    "tbd_026_ema50_below_ema200_event": {"inputs": ["close"], "func": tbd_026_ema50_below_ema200_event},
    "tbd_027_ema_bearish_cross_count_252d": {"inputs": ["close"], "func": tbd_027_ema_bearish_cross_count_252d},
    "tbd_028_triple_ema_death_cross_flag": {"inputs": ["close"], "func": tbd_028_triple_ema_death_cross_flag},
    "tbd_029_days_since_ema50_below_ema200": {"inputs": ["close"], "func": tbd_029_days_since_ema50_below_ema200},
    "tbd_030_ema_cross_count_63d": {"inputs": ["close"], "func": tbd_030_ema_cross_count_63d},
    "tbd_031_macd_below_signal_flag": {"inputs": ["close"], "func": tbd_031_macd_below_signal_flag},
    "tbd_032_macd_histogram_negative_flag": {"inputs": ["close"], "func": tbd_032_macd_histogram_negative_flag},
    "tbd_033_macd_cross_below_signal_event": {"inputs": ["close"], "func": tbd_033_macd_cross_below_signal_event},
    "tbd_034_macd_histogram_sign_flip_neg_event": {"inputs": ["close"], "func": tbd_034_macd_histogram_sign_flip_neg_event},
    "tbd_035_days_since_macd_bearish_cross": {"inputs": ["close"], "func": tbd_035_days_since_macd_bearish_cross},
    "tbd_036_days_since_macd_hist_neg_flip": {"inputs": ["close"], "func": tbd_036_days_since_macd_hist_neg_flip},
    "tbd_037_macd_bearish_cross_count_252d": {"inputs": ["close"], "func": tbd_037_macd_bearish_cross_count_252d},
    "tbd_038_macd_histogram_neg_streak": {"inputs": ["close"], "func": tbd_038_macd_histogram_neg_streak},
    "tbd_039_macd_line_below_zero_flag": {"inputs": ["close"], "func": tbd_039_macd_line_below_zero_flag},
    "tbd_040_macd_line_below_zero_event": {"inputs": ["close"], "func": tbd_040_macd_line_below_zero_event},
    "tbd_041_adx14_below_25_flag": {"inputs": ["close", "high", "low"], "func": tbd_041_adx14_below_25_flag},
    "tbd_042_adx14_below_20_flag": {"inputs": ["close", "high", "low"], "func": tbd_042_adx14_below_20_flag},
    "tbd_043_adx14_falling_flag": {"inputs": ["close", "high", "low"], "func": tbd_043_adx14_falling_flag},
    "tbd_044_dmi_minus_above_plus_flag": {"inputs": ["close", "high", "low"], "func": tbd_044_dmi_minus_above_plus_flag},
    "tbd_045_dmi_bearish_cross_event": {"inputs": ["close", "high", "low"], "func": tbd_045_dmi_bearish_cross_event},
    "tbd_046_days_since_dmi_bearish_cross": {"inputs": ["close", "high", "low"], "func": tbd_046_days_since_dmi_bearish_cross},
    "tbd_047_adx14_collapse_from_peak_63d": {"inputs": ["close", "high", "low"], "func": tbd_047_adx14_collapse_from_peak_63d},
    "tbd_048_adx14_pct_below_peak_252d": {"inputs": ["close", "high", "low"], "func": tbd_048_adx14_pct_below_peak_252d},
    "tbd_049_dmi_minus_above_plus_count_63d": {"inputs": ["close", "high", "low"], "func": tbd_049_dmi_minus_above_plus_count_63d},
    "tbd_050_adx_dmi_combined_breakdown_flag": {"inputs": ["close", "high", "low"], "func": tbd_050_adx_dmi_combined_breakdown_flag},
    "tbd_051_sma20_slope_negative_flag": {"inputs": ["close"], "func": tbd_051_sma20_slope_negative_flag},
    "tbd_052_sma50_slope_negative_flag": {"inputs": ["close"], "func": tbd_052_sma50_slope_negative_flag},
    "tbd_053_sma200_slope_negative_flag": {"inputs": ["close"], "func": tbd_053_sma200_slope_negative_flag},
    "tbd_054_ema12_slope_negative_flag": {"inputs": ["close"], "func": tbd_054_ema12_slope_negative_flag},
    "tbd_055_ema26_slope_negative_flag": {"inputs": ["close"], "func": tbd_055_ema26_slope_negative_flag},
    "tbd_056_sma200_slope_neg_event": {"inputs": ["close"], "func": tbd_056_sma200_slope_neg_event},
    "tbd_057_all_ma_slopes_negative_flag": {"inputs": ["close"], "func": tbd_057_all_ma_slopes_negative_flag},
    "tbd_058_sma20_neg_slope_streak": {"inputs": ["close"], "func": tbd_058_sma20_neg_slope_streak},
    "tbd_059_sma200_neg_slope_streak": {"inputs": ["close"], "func": tbd_059_sma200_neg_slope_streak},
    "tbd_060_days_since_sma200_slope_turned_neg": {"inputs": ["close"], "func": tbd_060_days_since_sma200_slope_turned_neg},
    "tbd_061_psar_price_below_sar_flag": {"inputs": ["close", "high", "low"], "func": tbd_061_psar_price_below_sar_flag},
    "tbd_062_psar_flip_to_bearish_event": {"inputs": ["close", "high", "low"], "func": tbd_062_psar_flip_to_bearish_event},
    "tbd_063_psar_bars_since_bearish_flip": {"inputs": ["close", "high", "low"], "func": tbd_063_psar_bars_since_bearish_flip},
    "tbd_064_psar_distance_from_price": {"inputs": ["close", "high", "low"], "func": tbd_064_psar_distance_from_price},
    "tbd_065_psar_bearish_flip_count_63d": {"inputs": ["close", "high", "low"], "func": tbd_065_psar_bearish_flip_count_63d},
    "tbd_066_psar_bearish_streak": {"inputs": ["close", "high", "low"], "func": tbd_066_psar_bearish_streak},
    "tbd_067_psar_bearish_fraction_63d": {"inputs": ["close", "high", "low"], "func": tbd_067_psar_bearish_fraction_63d},
    "tbd_068_psar_distance_zscore_63d": {"inputs": ["close", "high", "low"], "func": tbd_068_psar_distance_zscore_63d},
    "tbd_069_aroon_down14_flag": {"inputs": ["close", "high", "low"], "func": tbd_069_aroon_down14_flag},
    "tbd_070_aroon_oscillator14_negative_flag": {"inputs": ["close", "high", "low"], "func": tbd_070_aroon_oscillator14_negative_flag},
    "tbd_071_aroon_down25_flag": {"inputs": ["close", "high", "low"], "func": tbd_071_aroon_down25_flag},
    "tbd_072_aroon_oscillator14_value": {"inputs": ["close", "high", "low"], "func": tbd_072_aroon_oscillator14_value},
    "tbd_073_aroon_oscillator25_value": {"inputs": ["close", "high", "low"], "func": tbd_073_aroon_oscillator25_value},
    "tbd_074_aroon_down14_above_90_flag": {"inputs": ["close", "high", "low"], "func": tbd_074_aroon_down14_above_90_flag},
    "tbd_075_aroon_bearish_cross_event14": {"inputs": ["close", "high", "low"], "func": tbd_075_aroon_bearish_cross_event14},
}
