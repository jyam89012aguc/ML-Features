"""accumulation_distribution_line d2 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__076_150.py.
Bucket A: Accumulation/Distribution Line core level / slope / extension.
Bucket B: AD line vs price divergence.
Bucket C: Chaikin Money Flow (CMF) level / state / dwell.
Bucket D: Money Flow Index (MFI) level / OB state / dwell / decay.
Bucket E: Force Index variants.
Bucket F: Klinger Volume Oscillator (KVO) level / cross / divergence.
Bucket G: Volume Price Trend (VPT).
Bucket H: Chaikin Oscillator dynamics.

Inputs: SEP OHLCV (high, low, close, volume). PIT-clean: right-anchored rolling,
explicit min_periods, no centered windows, no .shift(N). Self-contained helpers.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260


# ---------------------------- helpers ----------------------------

def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _bars_since_true(mask):
    arr = mask.astype(bool).to_numpy()
    out = np.full(arr.shape, np.nan)
    last = -1
    for i in range(arr.size):
        if arr[i]:
            last = i
            out[i] = 0.0
        elif last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=mask.index)


def _streak_true(mask):
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)


# ---------- domain helpers ----------

def _mfm(high, low, close):
    """Money flow multiplier (Chaikin's CLV): ((C-L)-(H-C))/(H-L), in [-1,1]."""
    rng = (high - low).replace(0, np.nan)
    return ((close - low) - (high - close)) / rng


def _ad_line(high, low, close, volume):
    """Chaikin Accumulation/Distribution Line — cumulative money-flow volume."""
    mfv = _mfm(high, low, close) * volume
    return mfv.cumsum()


def _cmf(high, low, close, volume, n):
    """Chaikin Money Flow over n bars = sum(mfv) / sum(volume)."""
    mfv = _mfm(high, low, close) * volume
    num = mfv.rolling(n, min_periods=max(n // 3, 2)).sum()
    den = volume.rolling(n, min_periods=max(n // 3, 2)).sum()
    return _safe_div(num, den)


def _mfi(high, low, close, volume, n=14):
    """Money Flow Index (Quong/Soudack) — vol-weighted RSI of typical price."""
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    delta = tp.diff()
    pos = rmf.where(delta > 0, 0.0)
    neg = rmf.where(delta < 0, 0.0)
    psum = pos.rolling(n, min_periods=max(n // 3, 2)).sum()
    nsum = neg.rolling(n, min_periods=max(n // 3, 2)).sum()
    mr = _safe_div(psum, nsum)
    return 100.0 - 100.0 / (1.0 + mr)


def _force_index(close, volume, n):
    """Elder Force Index = (C - C_prev) * V, EMA-smoothed over n."""
    raw = close.diff() * volume
    if n <= 1:
        return raw
    return raw.ewm(span=n, adjust=False, min_periods=n).mean()


def _kvo(high, low, close, volume, fast=34, slow=55):
    """Klinger Volume Oscillator (Klinger's volume force)."""
    tp = (high + low + close) / 3.0
    trend = np.sign(tp.diff()).fillna(0.0)
    dm = (high - low)
    cm_raw = dm.where(trend == trend.shift(1), dm + dm.shift(1))
    vf = volume * trend * (2.0 * _safe_div(dm, cm_raw.replace(0, np.nan)) - 1.0) * 100.0
    ef = vf.ewm(span=fast, adjust=False, min_periods=fast).mean()
    es = vf.ewm(span=slow, adjust=False, min_periods=slow).mean()
    return ef - es


def _kvo_signal(kvo_line, n=13):
    return kvo_line.ewm(span=n, adjust=False, min_periods=n).mean()


def _vpt(close, volume):
    """Volume Price Trend = cumsum( volume * (close - close_prev) / close_prev )."""
    rt = close.pct_change()
    return (volume * rt).cumsum()


def _chaikin_osc(high, low, close, volume, fast=3, slow=10):
    """Chaikin Oscillator = EMA_fast(AD) - EMA_slow(AD)."""
    ad = _ad_line(high, low, close, volume)
    ef = ad.ewm(span=fast, adjust=False, min_periods=fast).mean()
    es = ad.ewm(span=slow, adjust=False, min_periods=slow).mean()
    return ef - es


# ============================================================
# Bucket A — AD line core (001-010)
# ============================================================


def f23_adld_001_ad_line_level_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Raw cumulative Accumulation/Distribution Line level."""
    return (_ad_line(high, low, close, volume)).diff().diff()


def f23_adld_002_ad_line_zscore_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """AD line z-score vs trailing 252d distribution."""
    return (_rolling_zscore(_ad_line(high, low, close, volume), YDAYS, min_periods=QDAYS)).diff().diff()


def f23_adld_003_ad_distance_sma21_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """AD line minus its SMA21 — short-term distribution gap."""
    ad = _ad_line(high, low, close, volume)
    return (ad - ad.rolling(MDAYS, min_periods=WDAYS).mean()).diff().diff()


def f23_adld_004_ad_distance_sma63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """AD line minus SMA63 — quarterly distribution gap."""
    ad = _ad_line(high, low, close, volume)
    return (ad - ad.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff()


def f23_adld_005_ad_distance_sma252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """AD line minus SMA252 — annual distribution gap."""
    ad = _ad_line(high, low, close, volume)
    return (ad - ad.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()


def f23_adld_006_ad_slope_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d slope of AD line — quarterly accumulation/distribution rate."""
    return (_rolling_slope(_ad_line(high, low, close, volume), QDAYS)).diff().diff()


def f23_adld_007_ad_slope_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252d slope of AD line — annual flow direction."""
    return (_rolling_slope(_ad_line(high, low, close, volume), YDAYS)).diff().diff()


def f23_adld_008_ad_distance_from_252d_max_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """AD line drop from its trailing 252d maximum — saturation gap."""
    ad = _ad_line(high, low, close, volume)
    return (ad - ad.rolling(YDAYS, min_periods=QDAYS).max()).diff().diff()


def f23_adld_009_ad_ratio_to_252d_max_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """AD line / 252d AD max — normalized saturation (sensitive only when AD>0)."""
    ad = _ad_line(high, low, close, volume)
    return (_safe_div(ad, ad.rolling(YDAYS, min_periods=QDAYS).max())).diff().diff()


def f23_adld_010_chaikin_osc_3_10_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Chaikin oscillator EMA3(AD) - EMA10(AD) — classical Chaikin osc."""
    return (_chaikin_osc(high, low, close, volume, 3, 10)).diff().diff()


def f23_adld_011_ad_price_corr_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d correlation between AD line and price — decoupling indicator."""
    ad = _ad_line(high, low, close, volume)
    return (close.rolling(QDAYS, min_periods=MDAYS).corr(ad)).diff().diff()


def f23_adld_012_ad_price_corr_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252d correlation AD vs price — long-horizon decoupling."""
    ad = _ad_line(high, low, close, volume)
    return (close.rolling(YDAYS, min_periods=QDAYS).corr(ad)).diff().diff()


def f23_adld_013_ad_bearish_div_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 at price new 63d high while AD < prior 63d AD max — bearish AD divergence."""
    ad = _ad_line(high, low, close, volume)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    ad_below = ad < ad.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_new & ad_below).astype(float).where(ad.notna(), np.nan)).diff().diff()


def f23_adld_014_ad_bearish_div_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 at price new 252d high while AD < prior 252d AD max — long-horizon AD divergence."""
    ad = _ad_line(high, low, close, volume)
    p_new = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    ad_below = ad < ad.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    return ((p_new & ad_below).astype(float).where(ad.notna(), np.nan)).diff().diff()


def f23_adld_015_ad_bearish_div_count_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bearish AD-divergence events in trailing 63 bars."""
    ad = _ad_line(high, low, close, volume)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    ad_below = ad < ad.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    ev = (p_new & ad_below).astype(float)
    return (ev.rolling(QDAYS, min_periods=MDAYS).sum().where(ad.notna(), np.nan)).diff().diff()


def f23_adld_016_ad_bearish_div_count_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Annual count of bearish AD-divergence events."""
    ad = _ad_line(high, low, close, volume)
    p_new = high >= high.rolling(YDAYS, min_periods=QDAYS).max()
    ad_below = ad < ad.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    ev = (p_new & ad_below).astype(float)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum().where(ad.notna(), np.nan)).diff().diff()


def f23_adld_017_bars_since_last_ad_div_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since most recent AD bearish-divergence event."""
    ad = _ad_line(high, low, close, volume)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    ad_below = ad < ad.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (_bars_since_true(p_new & ad_below)).diff().diff()


def f23_adld_018_ad_div_amplitude_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """At AD-div bars, amplitude = prior 63d AD-max - AD; else NaN ffilled briefly."""
    ad = _ad_line(high, low, close, volume)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    prior_max = ad.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    amp = (prior_max - ad).where(p_new & (ad < prior_max), np.nan)
    return (amp.ffill(limit=QDAYS)).diff().diff()


def f23_adld_019_ad_fraction_below_sma252_in_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of past 63 bars AD below its SMA252 — quarterly under-flow regime."""
    ad = _ad_line(high, low, close, volume)
    sma = ad.rolling(YDAYS, min_periods=QDAYS).mean()
    return ((ad < sma).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(sma.notna(), np.nan)).diff().diff()


def f23_adld_020_ad_fraction_below_sma252_in_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of past 252 bars AD below its SMA252 — annual under-flow regime."""
    ad = _ad_line(high, low, close, volume)
    sma = ad.rolling(YDAYS, min_periods=QDAYS).mean()
    return ((ad < sma).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(sma.notna(), np.nan)).diff().diff()


def f23_adld_021_cmf_21_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Chaikin Money Flow over 21 bars — monthly flow."""
    return (_cmf(high, low, close, volume, MDAYS)).diff().diff()


def f23_adld_022_cmf_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """CMF over 63 bars — quarterly flow."""
    return (_cmf(high, low, close, volume, QDAYS)).diff().diff()


def f23_adld_023_cmf_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """CMF over 252 bars — annual flow."""
    return (_cmf(high, low, close, volume, YDAYS)).diff().diff()


def f23_adld_024_cmf_zscore_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of CMF21 vs its 252d distribution."""
    return (_rolling_zscore(_cmf(high, low, close, volume, MDAYS), YDAYS, min_periods=QDAYS)).diff().diff()


def f23_adld_025_cmf_below_zero_state_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if CMF21 < 0 — net-outflow state."""
    c = _cmf(high, low, close, volume, MDAYS)
    return ((c < 0).astype(float).where(c.notna(), np.nan)).diff().diff()


def f23_adld_026_cmf_below_neg10_state_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if CMF21 < -0.10 — moderate-outflow state."""
    c = _cmf(high, low, close, volume, MDAYS)
    return ((c < -0.10).astype(float).where(c.notna(), np.nan)).diff().diff()


def f23_adld_027_cmf_below_neg25_extreme_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if CMF21 < -0.25 — extreme outflow state."""
    c = _cmf(high, low, close, volume, MDAYS)
    return ((c < -0.25).astype(float).where(c.notna(), np.nan)).diff().diff()


def f23_adld_028_cmf_just_crossed_below_zero_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if CMF21 crossed below zero this bar — flow regime flip event."""
    c = _cmf(high, low, close, volume, MDAYS)
    return (((c.shift(1) >= 0) & (c < 0)).astype(float).where(c.notna(), np.nan)).diff().diff()


def f23_adld_029_cmf_dwell_below_zero_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with CMF21 < 0 — quarterly outflow dwell."""
    c = _cmf(high, low, close, volume, MDAYS)
    return ((c < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(c.notna(), np.nan)).diff().diff()


def f23_adld_030_cmf_dwell_below_zero_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with CMF21 < 0 — annual outflow dwell."""
    c = _cmf(high, low, close, volume, MDAYS)
    return ((c < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(c.notna(), np.nan)).diff().diff()


def f23_adld_031_cmf_bars_since_252d_max_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since CMF21 hit its 252d maximum — recency of peak inflow."""
    c = _cmf(high, low, close, volume, MDAYS)
    at_max = c == c.rolling(YDAYS, min_periods=QDAYS).max()
    return (_bars_since_true(at_max)).diff().diff()


def f23_adld_032_mfi_14_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Classical MFI(14) — volume-weighted RSI on typical price."""
    return (_mfi(high, low, close, volume, 14)).diff().diff()


def f23_adld_033_mfi_21_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """MFI(21) — monthly horizon (distinct concept)."""
    return (_mfi(high, low, close, volume, MDAYS)).diff().diff()


def f23_adld_034_mfi_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """MFI(63) — quarterly horizon (distinct concept)."""
    return (_mfi(high, low, close, volume, QDAYS)).diff().diff()


def f23_adld_035_mfi_above_80_state_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if MFI(14) > 80 — classical OB state."""
    m = _mfi(high, low, close, volume, 14)
    return ((m > 80.0).astype(float).where(m.notna(), np.nan)).diff().diff()


def f23_adld_036_mfi_above_90_extreme_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if MFI(14) > 90 — extreme OB (distinct hypothesis: severity)."""
    m = _mfi(high, low, close, volume, 14)
    return ((m > 90.0).astype(float).where(m.notna(), np.nan)).diff().diff()


def f23_adld_037_mfi_just_exited_above_80_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if MFI(14) was > 80 prior bar and <= 80 now — OB-exit trigger."""
    m = _mfi(high, low, close, volume, 14)
    return (((m.shift(1) > 80.0) & (m <= 80.0)).astype(float).where(m.notna(), np.nan)).diff().diff()


def f23_adld_038_mfi_dwell_above_80_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with MFI(14) > 80 — quarterly OB dwell."""
    m = _mfi(high, low, close, volume, 14)
    return ((m > 80.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(m.notna(), np.nan)).diff().diff()


def f23_adld_039_mfi_dwell_above_80_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with MFI(14) > 80 — annual OB dwell."""
    m = _mfi(high, low, close, volume, 14)
    return ((m > 80.0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(m.notna(), np.nan)).diff().diff()


def f23_adld_040_mfi_bars_since_ob80_exit_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since most recent MFI OB80 exit — recency of bearish MFI trigger."""
    m = _mfi(high, low, close, volume, 14)
    ev = (m.shift(1) > 80.0) & (m <= 80.0)
    return (_bars_since_true(ev)).diff().diff()


def f23_adld_041_mfi_bars_since_252d_max_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since MFI(14) reached its 252d max — recency of MFI peak."""
    m = _mfi(high, low, close, volume, 14)
    at_max = m == m.rolling(YDAYS, min_periods=QDAYS).max()
    return (_bars_since_true(at_max)).diff().diff()


def f23_adld_042_mfi_cumulative_ob_area_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (MFI - 80) over OB bars past 252 — MFI saturation intensity."""
    m = _mfi(high, low, close, volume, 14)
    area = (m - 80.0).clip(lower=0).where(m.notna(), np.nan)
    return (area.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()


def f23_adld_043_mfi_peak_decay_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d-max of MFI minus its value 63 bars ago — quarterly MFI peak decay."""
    m = _mfi(high, low, close, volume, 14)
    pmax = m.rolling(QDAYS, min_periods=MDAYS).max()
    return (pmax - pmax.shift(QDAYS)).diff().diff()


def f23_adld_044_mfi_bearish_div_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 at price new 63d high while MFI < prior 63d MFI max — vol-weighted bearish div."""
    m = _mfi(high, low, close, volume, 14)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    m_below = m < m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_new & m_below).astype(float).where(m.notna(), np.nan)).diff().diff()


def f23_adld_045_force_index_raw_1bar_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Raw 1-bar Force Index = (C - C_prev) * V."""
    return (_force_index(close, volume, 1)).diff().diff()


def f23_adld_046_force_index_ema13_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Elder Force Index (EMA13) — short-term force smoothing."""
    return (_force_index(close, volume, 13)).diff().diff()


def f23_adld_047_force_index_ema63_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Force Index EMA63 — quarterly force smoothing (distinct concept)."""
    return (_force_index(close, volume, QDAYS)).diff().diff()


def f23_adld_048_force_index_zscore_252_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of Force-Index(EMA13) vs trailing 252d."""
    return (_rolling_zscore(_force_index(close, volume, 13), YDAYS, min_periods=QDAYS)).diff().diff()


def f23_adld_049_force_index_below_zero_state_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if Force-Index(EMA13) < 0 — net-selling-force state."""
    f = _force_index(close, volume, 13)
    return ((f < 0).astype(float).where(f.notna(), np.nan)).diff().diff()


def f23_adld_050_force_index_just_crossed_below_zero_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if Force-Index(EMA13) crossed below 0 — bearish force-regime trigger."""
    f = _force_index(close, volume, 13)
    return (((f.shift(1) >= 0) & (f < 0)).astype(float).where(f.notna(), np.nan)).diff().diff()


def f23_adld_051_force_index_dwell_below_zero_63_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of past 63 bars Force-Index(EMA13) < 0 — bearish force dwell."""
    f = _force_index(close, volume, 13)
    return ((f < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(f.notna(), np.nan)).diff().diff()


def f23_adld_052_force_index_slope_63_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d slope of Force-Index(EMA13) — quarterly force trend."""
    return (_rolling_slope(_force_index(close, volume, 13), QDAYS)).diff().diff()


def f23_adld_053_force_index_cumulative_252_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of raw 1-bar Force-Index over 252 bars — annual net force."""
    return (_force_index(close, volume, 1).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()


def f23_adld_054_kvo_line_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Klinger Volume Oscillator line (EMA34 - EMA55 of volume force)."""
    return (_kvo(high, low, close, volume)).diff().diff()


def f23_adld_055_kvo_signal_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """KVO signal line = EMA13(KVO)."""
    return (_kvo_signal(_kvo(high, low, close, volume), 13)).diff().diff()


def f23_adld_056_kvo_histogram_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """KVO histogram = KVO - signal."""
    k = _kvo(high, low, close, volume)
    return (k - _kvo_signal(k, 13)).diff().diff()


def f23_adld_057_kvo_below_signal_state_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if KVO < its signal — bearish KVO state."""
    k = _kvo(high, low, close, volume)
    s = _kvo_signal(k, 13)
    return ((k < s).astype(float).where(k.notna() & s.notna(), np.nan)).diff().diff()


def f23_adld_058_kvo_bearish_cross_event_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if KVO crossed below its signal this bar."""
    k = _kvo(high, low, close, volume)
    s = _kvo_signal(k, 13)
    diff = k - s
    return (((diff.shift(1) > 0) & (diff <= 0)).astype(float).where(diff.notna(), np.nan)).diff().diff()


def f23_adld_059_kvo_bearish_cross_count_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bearish KVO/signal crosses in 63 bars — cross density."""
    k = _kvo(high, low, close, volume)
    s = _kvo_signal(k, 13)
    diff = k - s
    ev = ((diff.shift(1) > 0) & (diff <= 0)).astype(float)
    return (ev.rolling(QDAYS, min_periods=MDAYS).sum().where(diff.notna(), np.nan)).diff().diff()


def f23_adld_060_kvo_dwell_below_zero_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of past 63 bars KVO < 0 — bearish KVO dwell."""
    k = _kvo(high, low, close, volume)
    return ((k < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(k.notna(), np.nan)).diff().diff()


def f23_adld_061_kvo_peak_decay_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d-max of KVO minus its value 63 bars ago — KVO peak decay."""
    k = _kvo(high, low, close, volume)
    pmax = k.rolling(QDAYS, min_periods=MDAYS).max()
    return (pmax - pmax.shift(QDAYS)).diff().diff()


def f23_adld_062_kvo_bearish_div_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 at price new 63d high while KVO < prior 63d KVO max — KVO bearish divergence."""
    k = _kvo(high, low, close, volume)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    k_below = k < k.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_new & k_below).astype(float).where(k.notna(), np.nan)).diff().diff()


def f23_adld_063_vpt_level_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume Price Trend cumulative level."""
    return (_vpt(close, volume)).diff().diff()


def f23_adld_064_vpt_slope_63_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d slope of VPT."""
    return (_rolling_slope(_vpt(close, volume), QDAYS)).diff().diff()


def f23_adld_065_vpt_slope_252_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252d slope of VPT."""
    return (_rolling_slope(_vpt(close, volume), YDAYS)).diff().diff()


def f23_adld_066_vpt_zscore_252_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of VPT vs trailing 252d."""
    return (_rolling_zscore(_vpt(close, volume), YDAYS, min_periods=QDAYS)).diff().diff()


def f23_adld_067_vpt_distance_from_252d_max_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """VPT minus its trailing 252d max — drop from peak inflow."""
    v = _vpt(close, volume)
    return (v - v.rolling(YDAYS, min_periods=QDAYS).max()).diff().diff()


def f23_adld_068_vpt_distance_from_sma63_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """VPT minus SMA63 — quarterly mean-reversion gap."""
    v = _vpt(close, volume)
    return (v - v.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff()


def f23_adld_069_chaikin_osc_level_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Chaikin oscillator EMA3(AD) - EMA10(AD) raw level (alias)."""
    return (_chaikin_osc(high, low, close, volume, 3, 10)).diff().diff()


def f23_adld_070_chaikin_osc_below_zero_state_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if Chaikin osc < 0 — bearish Chaikin state."""
    c = _chaikin_osc(high, low, close, volume, 3, 10)
    return ((c < 0).astype(float).where(c.notna(), np.nan)).diff().diff()


def f23_adld_071_chaikin_osc_just_crossed_below_zero_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if Chaikin osc crossed below zero this bar — bearish trigger."""
    c = _chaikin_osc(high, low, close, volume, 3, 10)
    return (((c.shift(1) >= 0) & (c < 0)).astype(float).where(c.notna(), np.nan)).diff().diff()


def f23_adld_072_chaikin_osc_dwell_below_zero_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of past 63 bars Chaikin osc < 0 — bearish dwell."""
    c = _chaikin_osc(high, low, close, volume, 3, 10)
    return ((c < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(c.notna(), np.nan)).diff().diff()


def f23_adld_073_chaikin_osc_bearish_div_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 at price new 63d high while Chaikin osc < prior 63d Chaikin osc max — bearish div."""
    c = _chaikin_osc(high, low, close, volume, 3, 10)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    c_below = c < c.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_new & c_below).astype(float).where(c.notna(), np.nan)).diff().diff()


def f23_adld_074_chaikin_osc_peak_decay_63_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d-max of Chaikin osc minus its value 63 bars ago — peak decay."""
    c = _chaikin_osc(high, low, close, volume, 3, 10)
    pmax = c.rolling(QDAYS, min_periods=MDAYS).max()
    return (pmax - pmax.shift(QDAYS)).diff().diff()


def f23_adld_075_chaikin_osc_zscore_252_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of Chaikin osc vs trailing 252d."""
    return (_rolling_zscore(_chaikin_osc(high, low, close, volume, 3, 10), YDAYS, min_periods=QDAYS)).diff().diff()


# ============================================================
#                         REGISTRY 001-075 (d2)
# ============================================================

_HLCV = ["high", "low", "close", "volume"]
_HLC = ["high", "low", "close"]
_CV = ["close", "volume"]

ACCUMULATION_DISTRIBUTION_LINE_D2_REGISTRY_001_075 = {
    "f23_adld_001_ad_line_level_d2": {"inputs": _HLCV, "func": f23_adld_001_ad_line_level_d2},
    "f23_adld_002_ad_line_zscore_252_d2": {"inputs": _HLCV, "func": f23_adld_002_ad_line_zscore_252_d2},
    "f23_adld_003_ad_distance_sma21_d2": {"inputs": _HLCV, "func": f23_adld_003_ad_distance_sma21_d2},
    "f23_adld_004_ad_distance_sma63_d2": {"inputs": _HLCV, "func": f23_adld_004_ad_distance_sma63_d2},
    "f23_adld_005_ad_distance_sma252_d2": {"inputs": _HLCV, "func": f23_adld_005_ad_distance_sma252_d2},
    "f23_adld_006_ad_slope_63_d2": {"inputs": _HLCV, "func": f23_adld_006_ad_slope_63_d2},
    "f23_adld_007_ad_slope_252_d2": {"inputs": _HLCV, "func": f23_adld_007_ad_slope_252_d2},
    "f23_adld_008_ad_distance_from_252d_max_d2": {"inputs": _HLCV, "func": f23_adld_008_ad_distance_from_252d_max_d2},
    "f23_adld_009_ad_ratio_to_252d_max_d2": {"inputs": _HLCV, "func": f23_adld_009_ad_ratio_to_252d_max_d2},
    "f23_adld_010_chaikin_osc_3_10_d2": {"inputs": _HLCV, "func": f23_adld_010_chaikin_osc_3_10_d2},
    "f23_adld_011_ad_price_corr_63_d2": {"inputs": _HLCV, "func": f23_adld_011_ad_price_corr_63_d2},
    "f23_adld_012_ad_price_corr_252_d2": {"inputs": _HLCV, "func": f23_adld_012_ad_price_corr_252_d2},
    "f23_adld_013_ad_bearish_div_63_d2": {"inputs": _HLCV, "func": f23_adld_013_ad_bearish_div_63_d2},
    "f23_adld_014_ad_bearish_div_252_d2": {"inputs": _HLCV, "func": f23_adld_014_ad_bearish_div_252_d2},
    "f23_adld_015_ad_bearish_div_count_63_d2": {"inputs": _HLCV, "func": f23_adld_015_ad_bearish_div_count_63_d2},
    "f23_adld_016_ad_bearish_div_count_252_d2": {"inputs": _HLCV, "func": f23_adld_016_ad_bearish_div_count_252_d2},
    "f23_adld_017_bars_since_last_ad_div_63_d2": {"inputs": _HLCV, "func": f23_adld_017_bars_since_last_ad_div_63_d2},
    "f23_adld_018_ad_div_amplitude_63_d2": {"inputs": _HLCV, "func": f23_adld_018_ad_div_amplitude_63_d2},
    "f23_adld_019_ad_fraction_below_sma252_in_63_d2": {"inputs": _HLCV, "func": f23_adld_019_ad_fraction_below_sma252_in_63_d2},
    "f23_adld_020_ad_fraction_below_sma252_in_252_d2": {"inputs": _HLCV, "func": f23_adld_020_ad_fraction_below_sma252_in_252_d2},
    "f23_adld_021_cmf_21_d2": {"inputs": _HLCV, "func": f23_adld_021_cmf_21_d2},
    "f23_adld_022_cmf_63_d2": {"inputs": _HLCV, "func": f23_adld_022_cmf_63_d2},
    "f23_adld_023_cmf_252_d2": {"inputs": _HLCV, "func": f23_adld_023_cmf_252_d2},
    "f23_adld_024_cmf_zscore_252_d2": {"inputs": _HLCV, "func": f23_adld_024_cmf_zscore_252_d2},
    "f23_adld_025_cmf_below_zero_state_d2": {"inputs": _HLCV, "func": f23_adld_025_cmf_below_zero_state_d2},
    "f23_adld_026_cmf_below_neg10_state_d2": {"inputs": _HLCV, "func": f23_adld_026_cmf_below_neg10_state_d2},
    "f23_adld_027_cmf_below_neg25_extreme_d2": {"inputs": _HLCV, "func": f23_adld_027_cmf_below_neg25_extreme_d2},
    "f23_adld_028_cmf_just_crossed_below_zero_d2": {"inputs": _HLCV, "func": f23_adld_028_cmf_just_crossed_below_zero_d2},
    "f23_adld_029_cmf_dwell_below_zero_63_d2": {"inputs": _HLCV, "func": f23_adld_029_cmf_dwell_below_zero_63_d2},
    "f23_adld_030_cmf_dwell_below_zero_252_d2": {"inputs": _HLCV, "func": f23_adld_030_cmf_dwell_below_zero_252_d2},
    "f23_adld_031_cmf_bars_since_252d_max_d2": {"inputs": _HLCV, "func": f23_adld_031_cmf_bars_since_252d_max_d2},
    "f23_adld_032_mfi_14_d2": {"inputs": _HLCV, "func": f23_adld_032_mfi_14_d2},
    "f23_adld_033_mfi_21_d2": {"inputs": _HLCV, "func": f23_adld_033_mfi_21_d2},
    "f23_adld_034_mfi_63_d2": {"inputs": _HLCV, "func": f23_adld_034_mfi_63_d2},
    "f23_adld_035_mfi_above_80_state_d2": {"inputs": _HLCV, "func": f23_adld_035_mfi_above_80_state_d2},
    "f23_adld_036_mfi_above_90_extreme_d2": {"inputs": _HLCV, "func": f23_adld_036_mfi_above_90_extreme_d2},
    "f23_adld_037_mfi_just_exited_above_80_d2": {"inputs": _HLCV, "func": f23_adld_037_mfi_just_exited_above_80_d2},
    "f23_adld_038_mfi_dwell_above_80_63_d2": {"inputs": _HLCV, "func": f23_adld_038_mfi_dwell_above_80_63_d2},
    "f23_adld_039_mfi_dwell_above_80_252_d2": {"inputs": _HLCV, "func": f23_adld_039_mfi_dwell_above_80_252_d2},
    "f23_adld_040_mfi_bars_since_ob80_exit_d2": {"inputs": _HLCV, "func": f23_adld_040_mfi_bars_since_ob80_exit_d2},
    "f23_adld_041_mfi_bars_since_252d_max_d2": {"inputs": _HLCV, "func": f23_adld_041_mfi_bars_since_252d_max_d2},
    "f23_adld_042_mfi_cumulative_ob_area_252_d2": {"inputs": _HLCV, "func": f23_adld_042_mfi_cumulative_ob_area_252_d2},
    "f23_adld_043_mfi_peak_decay_63_d2": {"inputs": _HLCV, "func": f23_adld_043_mfi_peak_decay_63_d2},
    "f23_adld_044_mfi_bearish_div_63_d2": {"inputs": _HLCV, "func": f23_adld_044_mfi_bearish_div_63_d2},
    "f23_adld_045_force_index_raw_1bar_d2": {"inputs": _CV, "func": f23_adld_045_force_index_raw_1bar_d2},
    "f23_adld_046_force_index_ema13_d2": {"inputs": _CV, "func": f23_adld_046_force_index_ema13_d2},
    "f23_adld_047_force_index_ema63_d2": {"inputs": _CV, "func": f23_adld_047_force_index_ema63_d2},
    "f23_adld_048_force_index_zscore_252_d2": {"inputs": _CV, "func": f23_adld_048_force_index_zscore_252_d2},
    "f23_adld_049_force_index_below_zero_state_d2": {"inputs": _CV, "func": f23_adld_049_force_index_below_zero_state_d2},
    "f23_adld_050_force_index_just_crossed_below_zero_d2": {"inputs": _CV, "func": f23_adld_050_force_index_just_crossed_below_zero_d2},
    "f23_adld_051_force_index_dwell_below_zero_63_d2": {"inputs": _CV, "func": f23_adld_051_force_index_dwell_below_zero_63_d2},
    "f23_adld_052_force_index_slope_63_d2": {"inputs": _CV, "func": f23_adld_052_force_index_slope_63_d2},
    "f23_adld_053_force_index_cumulative_252_d2": {"inputs": _CV, "func": f23_adld_053_force_index_cumulative_252_d2},
    "f23_adld_054_kvo_line_d2": {"inputs": _HLCV, "func": f23_adld_054_kvo_line_d2},
    "f23_adld_055_kvo_signal_d2": {"inputs": _HLCV, "func": f23_adld_055_kvo_signal_d2},
    "f23_adld_056_kvo_histogram_d2": {"inputs": _HLCV, "func": f23_adld_056_kvo_histogram_d2},
    "f23_adld_057_kvo_below_signal_state_d2": {"inputs": _HLCV, "func": f23_adld_057_kvo_below_signal_state_d2},
    "f23_adld_058_kvo_bearish_cross_event_d2": {"inputs": _HLCV, "func": f23_adld_058_kvo_bearish_cross_event_d2},
    "f23_adld_059_kvo_bearish_cross_count_63_d2": {"inputs": _HLCV, "func": f23_adld_059_kvo_bearish_cross_count_63_d2},
    "f23_adld_060_kvo_dwell_below_zero_63_d2": {"inputs": _HLCV, "func": f23_adld_060_kvo_dwell_below_zero_63_d2},
    "f23_adld_061_kvo_peak_decay_63_d2": {"inputs": _HLCV, "func": f23_adld_061_kvo_peak_decay_63_d2},
    "f23_adld_062_kvo_bearish_div_63_d2": {"inputs": _HLCV, "func": f23_adld_062_kvo_bearish_div_63_d2},
    "f23_adld_063_vpt_level_d2": {"inputs": _CV, "func": f23_adld_063_vpt_level_d2},
    "f23_adld_064_vpt_slope_63_d2": {"inputs": _CV, "func": f23_adld_064_vpt_slope_63_d2},
    "f23_adld_065_vpt_slope_252_d2": {"inputs": _CV, "func": f23_adld_065_vpt_slope_252_d2},
    "f23_adld_066_vpt_zscore_252_d2": {"inputs": _CV, "func": f23_adld_066_vpt_zscore_252_d2},
    "f23_adld_067_vpt_distance_from_252d_max_d2": {"inputs": _CV, "func": f23_adld_067_vpt_distance_from_252d_max_d2},
    "f23_adld_068_vpt_distance_from_sma63_d2": {"inputs": _CV, "func": f23_adld_068_vpt_distance_from_sma63_d2},
    "f23_adld_069_chaikin_osc_level_d2": {"inputs": _HLCV, "func": f23_adld_069_chaikin_osc_level_d2},
    "f23_adld_070_chaikin_osc_below_zero_state_d2": {"inputs": _HLCV, "func": f23_adld_070_chaikin_osc_below_zero_state_d2},
    "f23_adld_071_chaikin_osc_just_crossed_below_zero_d2": {"inputs": _HLCV, "func": f23_adld_071_chaikin_osc_just_crossed_below_zero_d2},
    "f23_adld_072_chaikin_osc_dwell_below_zero_63_d2": {"inputs": _HLCV, "func": f23_adld_072_chaikin_osc_dwell_below_zero_63_d2},
    "f23_adld_073_chaikin_osc_bearish_div_63_d2": {"inputs": _HLCV, "func": f23_adld_073_chaikin_osc_bearish_div_63_d2},
    "f23_adld_074_chaikin_osc_peak_decay_63_d2": {"inputs": _HLCV, "func": f23_adld_074_chaikin_osc_peak_decay_63_d2},
    "f23_adld_075_chaikin_osc_zscore_252_d2": {"inputs": _HLCV, "func": f23_adld_075_chaikin_osc_zscore_252_d2},
}
