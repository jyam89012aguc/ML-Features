"""accumulation_distribution_line d3 features 076-150 — Pipeline 1b-technical.

Continuation of the 150-hypothesis family.
Bucket I: Williams Accumulation/Distribution (WAD).
Bucket J: Twiggs Money Flow (TMF).
Bucket K: Negative/Positive Volume Index (NVI/PVI).
Bucket L: Money-flow multiplier (CLV) statistics.
Bucket M: Distribution-day analysis (IBD-style).
Bucket N: Up/down volume asymmetry.
Bucket O: Volume-weighted return.
Bucket P: Cumulative net-buying-pressure.
Bucket Q: Composite money-flow risk / breadth.

Inputs: SEP OHLCV only. Self-contained helpers.
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
    rng = (high - low).replace(0, np.nan)
    return ((close - low) - (high - close)) / rng


def _wad(high, low, close):
    """Williams Accumulation/Distribution Line.
    On up days (C>C_prev): TR_high = max(H, C_prev), AD = C - TR_high(low side: min(L, C_prev))
    Wilder's WAD: if C>C_prev: add (C - min(L,C_prev)); if C<C_prev: add (C - max(H,C_prev)); else 0; cumsum.
    """
    pc = close.shift(1)
    inc = (close - np.minimum(low, pc)).where(close > pc, 0.0)
    dec = (close - np.maximum(high, pc)).where(close < pc, 0.0)
    pad = (inc + dec).fillna(0.0)
    return pad.cumsum()


def _tmf(high, low, close, volume, n):
    """Twiggs Money Flow — Wilder-smoothed CMF."""
    rng = (high - low).replace(0, np.nan)
    pc = close.shift(1)
    th = pd.concat([high, pc], axis=1).max(axis=1)
    tl = pd.concat([low, pc], axis=1).min(axis=1)
    trng = (th - tl).replace(0, np.nan)
    ad = ((close - tl) - (th - close)) / trng * volume
    # Wilder smoothing (EMA alpha=1/n) of both numerator and denominator
    num = ad.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    den = volume.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    return _safe_div(num, den)


def _nvi(close, volume):
    """Negative Volume Index — accumulates pct-change on down-volume days only."""
    vchg = volume.diff()
    rt = close.pct_change().fillna(0.0)
    inc = rt.where(vchg < 0, 0.0)
    out = (1.0 + inc).cumprod()
    return out


def _pvi(close, volume):
    """Positive Volume Index — accumulates pct-change on up-volume days only."""
    vchg = volume.diff()
    rt = close.pct_change().fillna(0.0)
    inc = rt.where(vchg > 0, 0.0)
    out = (1.0 + inc).cumprod()
    return out


# ============================================================
# Bucket I — Williams A/D WAD (076-082)
# ============================================================


def f23_adld_076_wad_line_level_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Williams Accumulation/Distribution Line cumulative level."""
    return (_wad(high, low, close)).diff().diff().diff()


def f23_adld_077_wad_zscore_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WAD z-score vs trailing 252d."""
    return (_rolling_zscore(_wad(high, low, close), YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f23_adld_078_wad_slope_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Quarterly slope of WAD."""
    return (_rolling_slope(_wad(high, low, close), QDAYS)).diff().diff().diff()


def f23_adld_079_wad_slope_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annual slope of WAD."""
    return (_rolling_slope(_wad(high, low, close), YDAYS)).diff().diff().diff()


def f23_adld_080_wad_distance_from_252d_max_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """WAD drop from its trailing 252d max."""
    w = _wad(high, low, close)
    return (w - w.rolling(YDAYS, min_periods=QDAYS).max()).diff().diff().diff()


def f23_adld_081_wad_bearish_div_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish WAD divergence — price new 63d high while WAD < prior 63d WAD max."""
    w = _wad(high, low, close)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    w_below = w < w.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_new & w_below).astype(float).where(w.notna(), np.nan)).diff().diff().diff()


def f23_adld_082_wad_bars_since_252d_max_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since WAD reached its 252d max."""
    w = _wad(high, low, close)
    at_max = w == w.rolling(YDAYS, min_periods=QDAYS).max()
    return (_bars_since_true(at_max)).diff().diff().diff()


def f23_adld_083_tmf_21_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Twiggs Money Flow over 21 bars."""
    return (_tmf(high, low, close, volume, MDAYS)).diff().diff().diff()


def f23_adld_084_tmf_63_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """TMF over 63 bars — quarterly."""
    return (_tmf(high, low, close, volume, QDAYS)).diff().diff().diff()


def f23_adld_085_tmf_252_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """TMF over 252 bars — annual."""
    return (_tmf(high, low, close, volume, YDAYS)).diff().diff().diff()


def f23_adld_086_tmf_zscore_252_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of TMF21 vs trailing 252d."""
    return (_rolling_zscore(_tmf(high, low, close, volume, MDAYS), YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f23_adld_087_tmf_below_zero_state_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if TMF21 < 0 — Wilder-smoothed net-outflow state."""
    t = _tmf(high, low, close, volume, MDAYS)
    return ((t < 0).astype(float).where(t.notna(), np.nan)).diff().diff().diff()


def f23_adld_088_tmf_bearish_div_63_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish TMF divergence at new 63d price high."""
    t = _tmf(high, low, close, volume, MDAYS)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    t_below = t < t.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_new & t_below).astype(float).where(t.notna(), np.nan)).diff().diff().diff()


def f23_adld_089_nvi_level_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Negative Volume Index level."""
    return (_nvi(close, volume)).diff().diff().diff()


def f23_adld_090_nvi_slope_252_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """NVI annual slope — smart-money trend indicator."""
    return (_rolling_slope(_nvi(close, volume), YDAYS)).diff().diff().diff()


def f23_adld_091_pvi_level_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Positive Volume Index level."""
    return (_pvi(close, volume)).diff().diff().diff()


def f23_adld_092_pvi_slope_252_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """PVI annual slope — crowd-trend indicator."""
    return (_rolling_slope(_pvi(close, volume), YDAYS)).diff().diff().diff()


def f23_adld_093_pvi_nvi_ratio_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """PVI / NVI ratio — crowd-vs-smart-money tension."""
    return (_safe_div(_pvi(close, volume), _nvi(close, volume))).diff().diff().diff()


def f23_adld_094_pvi_nvi_ratio_zscore_252_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of PVI/NVI ratio vs 252d distribution."""
    return (_rolling_zscore(_safe_div(_pvi(close, volume), _nvi(close, volume)), YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f23_adld_095_nvi_fraction_below_sma252_in_63_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of past 63 bars NVI < its SMA252 — smart-money under-trend."""
    n = _nvi(close, volume)
    sma = n.rolling(YDAYS, min_periods=QDAYS).mean()
    return ((n < sma).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(sma.notna(), np.nan)).diff().diff().diff()


def f23_adld_096_pvi_nvi_bearish_cross_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if PVI/NVI ratio crossed below its SMA63 — crowd-momentum failure event."""
    r = _safe_div(_pvi(close, volume), _nvi(close, volume))
    sma = r.rolling(QDAYS, min_periods=MDAYS).mean()
    diff = r - sma
    return (((diff.shift(1) > 0) & (diff <= 0)).astype(float).where(diff.notna(), np.nan)).diff().diff().diff()


def f23_adld_097_clv_raw_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close Location Value (Chaikin MFM) raw, in [-1, 1]."""
    return (_mfm(high, low, close)).diff().diff().diff()


def f23_adld_098_clv_mean_21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean CLV over past 21 bars — monthly close-position bias."""
    return (_mfm(high, low, close).rolling(MDAYS, min_periods=WDAYS).mean()).diff().diff().diff()


def f23_adld_099_clv_mean_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean CLV over past 63 bars — quarterly close-position bias."""
    return (_mfm(high, low, close).rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff().diff()


def f23_adld_100_clv_mean_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean CLV over past 252 bars — annual close-position bias."""
    return (_mfm(high, low, close).rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff().diff()


def f23_adld_101_clv_fraction_negative_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with CLV < 0 — close-in-lower-half dwell."""
    m = _mfm(high, low, close)
    return ((m < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(m.notna(), np.nan)).diff().diff().diff()


def f23_adld_102_clv_fraction_negative_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Annual fraction of bars with CLV < 0."""
    m = _mfm(high, low, close)
    return ((m < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(m.notna(), np.nan)).diff().diff().diff()


def f23_adld_103_clv_zscore_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of CLV vs trailing 252d."""
    return (_rolling_zscore(_mfm(high, low, close), YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f23_adld_104_clv_x_volume_sum_63_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (CLV * volume) over 63 bars — quarterly volume-weighted close-bias."""
    return ((_mfm(high, low, close) * volume).rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff().diff()


def f23_adld_105_clv_x_volume_sum_252_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (CLV * volume) over 252 bars — annual volume-weighted close-bias."""
    return ((_mfm(high, low, close) * volume).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f23_adld_106_distribution_day_flag_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if today's close < prior close AND volume > 50d avg volume — IBD distribution day."""
    down = close < close.shift(1)
    bigvol = volume > volume.rolling(50, min_periods=20).mean()
    return ((down & bigvol).astype(float).where(close.notna() & volume.notna(), np.nan)).diff().diff().diff()


def f23_adld_107_distribution_day_count_21_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of distribution days in past 21 bars."""
    down = close < close.shift(1)
    bigvol = volume > volume.rolling(50, min_periods=20).mean()
    ev = (down & bigvol).astype(float)
    return (ev.rolling(MDAYS, min_periods=WDAYS).sum().where(close.notna(), np.nan)).diff().diff().diff()


def f23_adld_108_distribution_day_count_63_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of distribution days in past 63 bars."""
    down = close < close.shift(1)
    bigvol = volume > volume.rolling(50, min_periods=20).mean()
    ev = (down & bigvol).astype(float)
    return (ev.rolling(QDAYS, min_periods=MDAYS).sum().where(close.notna(), np.nan)).diff().diff().diff()


def f23_adld_109_distribution_day_count_252_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Annual count of distribution days."""
    down = close < close.shift(1)
    bigvol = volume > volume.rolling(50, min_periods=20).mean()
    ev = (down & bigvol).astype(float)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum().where(close.notna(), np.nan)).diff().diff().diff()


def f23_adld_110_dist_day_cluster_5_in_21_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 5+ distribution days in past 21 — IBD-style cluster warning."""
    down = close < close.shift(1)
    bigvol = volume > volume.rolling(50, min_periods=20).mean()
    cnt = (down & bigvol).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return ((cnt >= 5).astype(float).where(close.notna(), np.nan)).diff().diff().diff()


def f23_adld_111_dist_day_cluster_10_in_63_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if 10+ distribution days in past 63 — heavy-distribution regime."""
    down = close < close.shift(1)
    bigvol = volume > volume.rolling(50, min_periods=20).mean()
    cnt = (down & bigvol).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return ((cnt >= 10).astype(float).where(close.notna(), np.nan)).diff().diff().diff()


def f23_adld_112_accumulation_day_flag_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if today's close > prior close AND volume > 50d avg — accumulation day."""
    up = close > close.shift(1)
    bigvol = volume > volume.rolling(50, min_periods=20).mean()
    return ((up & bigvol).astype(float).where(close.notna() & volume.notna(), np.nan)).diff().diff().diff()


def f23_adld_113_accumulation_day_count_63_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of accumulation days in past 63 bars — context for net flow."""
    up = close > close.shift(1)
    bigvol = volume > volume.rolling(50, min_periods=20).mean()
    ev = (up & bigvol).astype(float)
    return (ev.rolling(QDAYS, min_periods=MDAYS).sum().where(close.notna(), np.nan)).diff().diff().diff()


def f23_adld_114_net_dist_minus_accum_63_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(distribution days - accumulation days) in past 63 — net high-vol pressure."""
    down = close < close.shift(1)
    up = close > close.shift(1)
    bigvol = volume > volume.rolling(50, min_periods=20).mean()
    d = (down & bigvol).astype(float)
    a = (up & bigvol).astype(float)
    return ((d - a).rolling(QDAYS, min_periods=MDAYS).sum().where(close.notna(), np.nan)).diff().diff().diff()


def f23_adld_115_net_dist_minus_accum_252_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Annual net (distribution - accumulation) count."""
    down = close < close.shift(1)
    up = close > close.shift(1)
    bigvol = volume > volume.rolling(50, min_periods=20).mean()
    d = (down & bigvol).astype(float)
    a = (up & bigvol).astype(float)
    return ((d - a).rolling(YDAYS, min_periods=QDAYS).sum().where(close.notna(), np.nan)).diff().diff().diff()


def f23_adld_116_up_volume_sum_21_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume on up-close days over past 21 bars."""
    up = (close > close.shift(1)).astype(float)
    return ((up * volume).rolling(MDAYS, min_periods=WDAYS).sum().where(close.notna(), np.nan)).diff().diff().diff()


def f23_adld_117_down_volume_sum_21_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume on down-close days over past 21 bars."""
    dn = (close < close.shift(1)).astype(float)
    return ((dn * volume).rolling(MDAYS, min_periods=WDAYS).sum().where(close.notna(), np.nan)).diff().diff().diff()


def f23_adld_118_up_volume_sum_63_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume on up days over 63 bars."""
    up = (close > close.shift(1)).astype(float)
    return ((up * volume).rolling(QDAYS, min_periods=MDAYS).sum().where(close.notna(), np.nan)).diff().diff().diff()


def f23_adld_119_down_volume_sum_63_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of volume on down days over 63 bars."""
    dn = (close < close.shift(1)).astype(float)
    return ((dn * volume).rolling(QDAYS, min_periods=MDAYS).sum().where(close.notna(), np.nan)).diff().diff().diff()


def f23_adld_120_up_minus_down_vol_ratio_21_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(Up-vol - Down-vol) / total vol over 21 bars — monthly net-pressure ratio."""
    sign = np.sign(close.diff()).fillna(0.0)
    uv = (sign.clip(lower=0) * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    dv = ((-sign).clip(lower=0) * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    tot = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    return (_safe_div(uv - dv, tot)).diff().diff().diff()


def f23_adld_121_up_minus_down_vol_ratio_63_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Quarterly net-pressure ratio."""
    sign = np.sign(close.diff()).fillna(0.0)
    uv = (sign.clip(lower=0) * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    dv = ((-sign).clip(lower=0) * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    tot = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    return (_safe_div(uv - dv, tot)).diff().diff().diff()


def f23_adld_122_up_minus_down_vol_ratio_252_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Annual net-pressure ratio."""
    sign = np.sign(close.diff()).fillna(0.0)
    uv = (sign.clip(lower=0) * volume).rolling(YDAYS, min_periods=QDAYS).sum()
    dv = ((-sign).clip(lower=0) * volume).rolling(YDAYS, min_periods=QDAYS).sum()
    tot = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_div(uv - dv, tot)).diff().diff().diff()


def f23_adld_123_up_minus_down_vol_zscore_252_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of (Up-vol - Down-vol) 21-bar sum vs 252d distribution."""
    sign = np.sign(close.diff()).fillna(0.0)
    diff21 = ((sign.clip(lower=0) - (-sign).clip(lower=0)) * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    return (_rolling_zscore(diff21, YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f23_adld_124_up_down_vol_ratio_63_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Up-vol / down-vol ratio over 63 bars (>=1 bullish, <1 bearish)."""
    sign = np.sign(close.diff()).fillna(0.0)
    uv = (sign.clip(lower=0) * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    dv = ((-sign).clip(lower=0) * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    return (_safe_div(uv, dv)).diff().diff().diff()


def f23_adld_125_up_down_vol_ratio_zscore_252_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of up/down vol ratio vs trailing 252d distribution."""
    sign = np.sign(close.diff()).fillna(0.0)
    uv = (sign.clip(lower=0) * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    dv = ((-sign).clip(lower=0) * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    r = _safe_div(uv, dv)
    return (_rolling_zscore(r, YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f23_adld_126_volume_weighted_return_21_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-bar volume-weighted mean return — vol-weighted monthly avg."""
    r = close.pct_change()
    num = (r * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    den = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    return (_safe_div(num, den)).diff().diff().diff()


def f23_adld_127_volume_weighted_return_63_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-bar volume-weighted mean return."""
    r = close.pct_change()
    num = (r * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    den = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    return (_safe_div(num, den)).diff().diff().diff()


def f23_adld_128_volume_weighted_return_252_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-bar volume-weighted mean return."""
    r = close.pct_change()
    num = (r * volume).rolling(YDAYS, min_periods=QDAYS).sum()
    den = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_div(num, den)).diff().diff().diff()


def f23_adld_129_vw_return_minus_simple_return_63_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol-weighted 63d return minus simple 63d return — vol-weighted vs equal-weighted gap."""
    r = close.pct_change()
    num = (r * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    den = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    vw = _safe_div(num, den)
    sim = r.rolling(QDAYS, min_periods=MDAYS).mean()
    return (vw - sim).diff().diff().diff()


def f23_adld_130_vw_return_zscore_252_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21-bar vol-weighted return vs trailing 252d distribution."""
    r = close.pct_change()
    num = (r * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    den = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    return (_rolling_zscore(_safe_div(num, den), YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f23_adld_131_cum_net_buy_pressure_level_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cumulative net-buying pressure = cumsum(CLV * volume)."""
    return ((_mfm(high, low, close) * volume).cumsum()).diff().diff().diff()


def f23_adld_132_cum_net_buy_slope_63_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d slope of cumulative net-buying pressure."""
    return (_rolling_slope((_mfm(high, low, close) * volume).cumsum(), QDAYS)).diff().diff().diff()


def f23_adld_133_cum_net_buy_slope_252_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """252d slope of cumulative net-buying pressure."""
    return (_rolling_slope((_mfm(high, low, close) * volume).cumsum(), YDAYS)).diff().diff().diff()


def f23_adld_134_cum_net_buy_zscore_252_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of cumulative net-buying pressure vs trailing 252d."""
    return (_rolling_zscore((_mfm(high, low, close) * volume).cumsum(), YDAYS, min_periods=QDAYS)).diff().diff().diff()


def f23_adld_135_cum_net_buy_peak_decay_63_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d-max of cumulative net-buying pressure minus its value 63 bars ago."""
    s = (_mfm(high, low, close) * volume).cumsum()
    pmax = s.rolling(QDAYS, min_periods=MDAYS).max()
    return (pmax - pmax.shift(QDAYS)).diff().diff().diff()


def f23_adld_136_cum_net_buy_below_sma63_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if cumulative net-buying pressure < its SMA63 — flow trend below mean."""
    s = (_mfm(high, low, close) * volume).cumsum()
    sma = s.rolling(QDAYS, min_periods=MDAYS).mean()
    return ((s < sma).astype(float).where(sma.notna(), np.nan)).diff().diff().diff()


def f23_adld_137_net_buy_pressure_21_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """sum(CLV*vol)/sum(vol) over 21 — vol-weighted CLV (monthly)."""
    num = (_mfm(high, low, close) * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    den = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    return (_safe_div(num, den)).diff().diff().diff()


def f23_adld_138_net_buy_pressure_63_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """sum(CLV*vol)/sum(vol) over 63 — vol-weighted CLV (quarterly)."""
    num = (_mfm(high, low, close) * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    den = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    return (_safe_div(num, den)).diff().diff().diff()


def f23_adld_139_net_buy_pressure_252_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """sum(CLV*vol)/sum(vol) over 252 — vol-weighted CLV (annual)."""
    num = (_mfm(high, low, close) * volume).rolling(YDAYS, min_periods=QDAYS).sum()
    den = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    return (_safe_div(num, den)).diff().diff().diff()


def f23_adld_140_cum_net_buy_bearish_div_63_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish divergence: price new 63d high while cumulative net-buying < prior 63d max."""
    s = (_mfm(high, low, close) * volume).cumsum()
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    s_below = s < s.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_new & s_below).astype(float).where(s.notna(), np.nan)).diff().diff().diff()


def f23_adld_141_bearish_flow_consensus_count_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bearish-flow flags: {CMF21<0, MFI(14) just-exited-80, KVO<0}."""
    c = _cmf(high, low, close, volume, MDAYS)
    m = _mfi(high, low, close, volume, 14)
    k = _kvo(high, low, close, volume)
    f1 = (c < 0).astype(float)
    f2 = ((m.shift(1) > 80.0) & (m <= 80.0)).astype(float)
    f3 = (k < 0).astype(float)
    return ((f1.fillna(0) + f2.fillna(0) + f3.fillna(0)).where(c.notna() | m.notna() | k.notna(), np.nan)).diff().diff().diff()


def f23_adld_142_bullish_flow_consensus_count_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bullish-flow flags: {CMF21>0, MFI>50, KVO>0}."""
    c = _cmf(high, low, close, volume, MDAYS)
    m = _mfi(high, low, close, volume, 14)
    k = _kvo(high, low, close, volume)
    f1 = (c > 0).astype(float)
    f2 = (m > 50.0).astype(float)
    f3 = (k > 0).astype(float)
    return ((f1.fillna(0) + f2.fillna(0) + f3.fillna(0)).where(c.notna() | m.notna() | k.notna(), np.nan)).diff().diff().diff()


def f23_adld_143_flow_stress_index_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stress = 1 - (bullish-flow-consensus / 3) — high = consensus selling."""
    c = _cmf(high, low, close, volume, MDAYS)
    m = _mfi(high, low, close, volume, 14)
    k = _kvo(high, low, close, volume)
    f1 = (c > 0).astype(float)
    f2 = (m > 50.0).astype(float)
    f3 = (k > 0).astype(float)
    cnt = (f1.fillna(0) + f2.fillna(0) + f3.fillna(0))
    return ((1.0 - cnt / 3.0).where(c.notna() | m.notna() | k.notna(), np.nan)).diff().diff().diff()


def f23_adld_144_ad_minus_wad_divergence_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of AD line minus z-score of WAD — internal-method disagreement."""
    ad = _ad_line(high, low, close, volume)
    w = _wad(high, low, close)
    za = _rolling_zscore(ad, YDAYS, min_periods=QDAYS)
    zw = _rolling_zscore(w, YDAYS, min_periods=QDAYS)
    return (za - zw).diff().diff().diff()


def f23_adld_145_cmf_minus_mfi_norm_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """CMF21 minus normalized MFI((MFI-50)/50) — cross-indicator gap."""
    c = _cmf(high, low, close, volume, MDAYS)
    m = _mfi(high, low, close, volume, 14)
    return (c - (m - 50.0) / 50.0).diff().diff().diff()


def f23_adld_146_cmf_range_63_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d max(CMF21) - 63d min(CMF21) — flow swing amplitude."""
    c = _cmf(high, low, close, volume, MDAYS)
    return (c.rolling(QDAYS, min_periods=MDAYS).max() - c.rolling(QDAYS, min_periods=MDAYS).min()).diff().diff().diff()


def f23_adld_147_mfi_cross_from_ob_count_63_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of MFI(14) OB80-exit events in past 63 bars."""
    m = _mfi(high, low, close, volume, 14)
    ev = ((m.shift(1) > 80.0) & (m <= 80.0)).astype(float)
    return (ev.rolling(QDAYS, min_periods=MDAYS).sum().where(m.notna(), np.nan)).diff().diff().diff()


def f23_adld_148_mfi_cross_from_ob_count_252_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Annual count of MFI OB80-exit events."""
    m = _mfi(high, low, close, volume, 14)
    ev = ((m.shift(1) > 80.0) & (m <= 80.0)).astype(float)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum().where(m.notna(), np.nan)).diff().diff().diff()


def f23_adld_149_force_index_sign_change_count_63_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of Force-Index(EMA13) sign-changes in past 63 bars — force-regime instability."""
    f = close.diff() * volume
    fe = f.ewm(span=13, adjust=False, min_periods=13).mean()
    sgn = np.sign(fe)
    flip = (sgn != sgn.shift(1)).astype(float)
    flip = flip.where(fe.notna() & fe.shift(1).notna(), np.nan)
    return (flip.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff().diff()


def f23_adld_150_tmf_cmf_corr_252_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252d correlation between TMF(21) and CMF(21) — method-agreement strength."""
    t = _tmf(high, low, close, volume, MDAYS)
    c = _cmf(high, low, close, volume, MDAYS)
    return (t.rolling(YDAYS, min_periods=QDAYS).corr(c)).diff().diff().diff()


def _cmf(high, low, close, volume, n):
    mfv = _mfm(high, low, close) * volume
    num = mfv.rolling(n, min_periods=max(n // 3, 2)).sum()
    den = volume.rolling(n, min_periods=max(n // 3, 2)).sum()
    return _safe_div(num, den)


def _mfi(high, low, close, volume, n=14):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    delta = tp.diff()
    pos = rmf.where(delta > 0, 0.0)
    neg = rmf.where(delta < 0, 0.0)
    psum = pos.rolling(n, min_periods=max(n // 3, 2)).sum()
    nsum = neg.rolling(n, min_periods=max(n // 3, 2)).sum()
    mr = _safe_div(psum, nsum)
    return 100.0 - 100.0 / (1.0 + mr)


def _kvo(high, low, close, volume, fast=34, slow=55):
    tp = (high + low + close) / 3.0
    trend = np.sign(tp.diff()).fillna(0.0)
    dm = (high - low)
    cm_raw = dm.where(trend == trend.shift(1), dm + dm.shift(1))
    vf = volume * trend * (2.0 * _safe_div(dm, cm_raw.replace(0, np.nan)) - 1.0) * 100.0
    ef = vf.ewm(span=fast, adjust=False, min_periods=fast).mean()
    es = vf.ewm(span=slow, adjust=False, min_periods=slow).mean()
    return ef - es


def _ad_line(high, low, close, volume):
    return (_mfm(high, low, close) * volume).cumsum()


# ---- helpers used inside above that need defining at module scope ----


# ============================================================
#                         REGISTRY 076-150
# ============================================================

_HLCV = ["high", "low", "close", "volume"]
_HLC = ["high", "low", "close"]
_CV = ["close", "volume"]

ACCUMULATION_DISTRIBUTION_LINE_D3_REGISTRY_076_150 = {
    "f23_adld_076_wad_line_level_d3": {"inputs": _HLC, "func": f23_adld_076_wad_line_level_d3},
    "f23_adld_077_wad_zscore_252_d3": {"inputs": _HLC, "func": f23_adld_077_wad_zscore_252_d3},
    "f23_adld_078_wad_slope_63_d3": {"inputs": _HLC, "func": f23_adld_078_wad_slope_63_d3},
    "f23_adld_079_wad_slope_252_d3": {"inputs": _HLC, "func": f23_adld_079_wad_slope_252_d3},
    "f23_adld_080_wad_distance_from_252d_max_d3": {"inputs": _HLC, "func": f23_adld_080_wad_distance_from_252d_max_d3},
    "f23_adld_081_wad_bearish_div_63_d3": {"inputs": _HLC, "func": f23_adld_081_wad_bearish_div_63_d3},
    "f23_adld_082_wad_bars_since_252d_max_d3": {"inputs": _HLC, "func": f23_adld_082_wad_bars_since_252d_max_d3},
    "f23_adld_083_tmf_21_d3": {"inputs": _HLCV, "func": f23_adld_083_tmf_21_d3},
    "f23_adld_084_tmf_63_d3": {"inputs": _HLCV, "func": f23_adld_084_tmf_63_d3},
    "f23_adld_085_tmf_252_d3": {"inputs": _HLCV, "func": f23_adld_085_tmf_252_d3},
    "f23_adld_086_tmf_zscore_252_d3": {"inputs": _HLCV, "func": f23_adld_086_tmf_zscore_252_d3},
    "f23_adld_087_tmf_below_zero_state_d3": {"inputs": _HLCV, "func": f23_adld_087_tmf_below_zero_state_d3},
    "f23_adld_088_tmf_bearish_div_63_d3": {"inputs": _HLCV, "func": f23_adld_088_tmf_bearish_div_63_d3},
    "f23_adld_089_nvi_level_d3": {"inputs": _CV, "func": f23_adld_089_nvi_level_d3},
    "f23_adld_090_nvi_slope_252_d3": {"inputs": _CV, "func": f23_adld_090_nvi_slope_252_d3},
    "f23_adld_091_pvi_level_d3": {"inputs": _CV, "func": f23_adld_091_pvi_level_d3},
    "f23_adld_092_pvi_slope_252_d3": {"inputs": _CV, "func": f23_adld_092_pvi_slope_252_d3},
    "f23_adld_093_pvi_nvi_ratio_d3": {"inputs": _CV, "func": f23_adld_093_pvi_nvi_ratio_d3},
    "f23_adld_094_pvi_nvi_ratio_zscore_252_d3": {"inputs": _CV, "func": f23_adld_094_pvi_nvi_ratio_zscore_252_d3},
    "f23_adld_095_nvi_fraction_below_sma252_in_63_d3": {"inputs": _CV, "func": f23_adld_095_nvi_fraction_below_sma252_in_63_d3},
    "f23_adld_096_pvi_nvi_bearish_cross_d3": {"inputs": _CV, "func": f23_adld_096_pvi_nvi_bearish_cross_d3},
    "f23_adld_097_clv_raw_d3": {"inputs": _HLC, "func": f23_adld_097_clv_raw_d3},
    "f23_adld_098_clv_mean_21_d3": {"inputs": _HLC, "func": f23_adld_098_clv_mean_21_d3},
    "f23_adld_099_clv_mean_63_d3": {"inputs": _HLC, "func": f23_adld_099_clv_mean_63_d3},
    "f23_adld_100_clv_mean_252_d3": {"inputs": _HLC, "func": f23_adld_100_clv_mean_252_d3},
    "f23_adld_101_clv_fraction_negative_63_d3": {"inputs": _HLC, "func": f23_adld_101_clv_fraction_negative_63_d3},
    "f23_adld_102_clv_fraction_negative_252_d3": {"inputs": _HLC, "func": f23_adld_102_clv_fraction_negative_252_d3},
    "f23_adld_103_clv_zscore_252_d3": {"inputs": _HLC, "func": f23_adld_103_clv_zscore_252_d3},
    "f23_adld_104_clv_x_volume_sum_63_d3": {"inputs": _HLCV, "func": f23_adld_104_clv_x_volume_sum_63_d3},
    "f23_adld_105_clv_x_volume_sum_252_d3": {"inputs": _HLCV, "func": f23_adld_105_clv_x_volume_sum_252_d3},
    "f23_adld_106_distribution_day_flag_d3": {"inputs": _CV, "func": f23_adld_106_distribution_day_flag_d3},
    "f23_adld_107_distribution_day_count_21_d3": {"inputs": _CV, "func": f23_adld_107_distribution_day_count_21_d3},
    "f23_adld_108_distribution_day_count_63_d3": {"inputs": _CV, "func": f23_adld_108_distribution_day_count_63_d3},
    "f23_adld_109_distribution_day_count_252_d3": {"inputs": _CV, "func": f23_adld_109_distribution_day_count_252_d3},
    "f23_adld_110_dist_day_cluster_5_in_21_d3": {"inputs": _CV, "func": f23_adld_110_dist_day_cluster_5_in_21_d3},
    "f23_adld_111_dist_day_cluster_10_in_63_d3": {"inputs": _CV, "func": f23_adld_111_dist_day_cluster_10_in_63_d3},
    "f23_adld_112_accumulation_day_flag_d3": {"inputs": _CV, "func": f23_adld_112_accumulation_day_flag_d3},
    "f23_adld_113_accumulation_day_count_63_d3": {"inputs": _CV, "func": f23_adld_113_accumulation_day_count_63_d3},
    "f23_adld_114_net_dist_minus_accum_63_d3": {"inputs": _CV, "func": f23_adld_114_net_dist_minus_accum_63_d3},
    "f23_adld_115_net_dist_minus_accum_252_d3": {"inputs": _CV, "func": f23_adld_115_net_dist_minus_accum_252_d3},
    "f23_adld_116_up_volume_sum_21_d3": {"inputs": _CV, "func": f23_adld_116_up_volume_sum_21_d3},
    "f23_adld_117_down_volume_sum_21_d3": {"inputs": _CV, "func": f23_adld_117_down_volume_sum_21_d3},
    "f23_adld_118_up_volume_sum_63_d3": {"inputs": _CV, "func": f23_adld_118_up_volume_sum_63_d3},
    "f23_adld_119_down_volume_sum_63_d3": {"inputs": _CV, "func": f23_adld_119_down_volume_sum_63_d3},
    "f23_adld_120_up_minus_down_vol_ratio_21_d3": {"inputs": _CV, "func": f23_adld_120_up_minus_down_vol_ratio_21_d3},
    "f23_adld_121_up_minus_down_vol_ratio_63_d3": {"inputs": _CV, "func": f23_adld_121_up_minus_down_vol_ratio_63_d3},
    "f23_adld_122_up_minus_down_vol_ratio_252_d3": {"inputs": _CV, "func": f23_adld_122_up_minus_down_vol_ratio_252_d3},
    "f23_adld_123_up_minus_down_vol_zscore_252_d3": {"inputs": _CV, "func": f23_adld_123_up_minus_down_vol_zscore_252_d3},
    "f23_adld_124_up_down_vol_ratio_63_d3": {"inputs": _CV, "func": f23_adld_124_up_down_vol_ratio_63_d3},
    "f23_adld_125_up_down_vol_ratio_zscore_252_d3": {"inputs": _CV, "func": f23_adld_125_up_down_vol_ratio_zscore_252_d3},
    "f23_adld_126_volume_weighted_return_21_d3": {"inputs": _CV, "func": f23_adld_126_volume_weighted_return_21_d3},
    "f23_adld_127_volume_weighted_return_63_d3": {"inputs": _CV, "func": f23_adld_127_volume_weighted_return_63_d3},
    "f23_adld_128_volume_weighted_return_252_d3": {"inputs": _CV, "func": f23_adld_128_volume_weighted_return_252_d3},
    "f23_adld_129_vw_return_minus_simple_return_63_d3": {"inputs": _CV, "func": f23_adld_129_vw_return_minus_simple_return_63_d3},
    "f23_adld_130_vw_return_zscore_252_d3": {"inputs": _CV, "func": f23_adld_130_vw_return_zscore_252_d3},
    "f23_adld_131_cum_net_buy_pressure_level_d3": {"inputs": _HLCV, "func": f23_adld_131_cum_net_buy_pressure_level_d3},
    "f23_adld_132_cum_net_buy_slope_63_d3": {"inputs": _HLCV, "func": f23_adld_132_cum_net_buy_slope_63_d3},
    "f23_adld_133_cum_net_buy_slope_252_d3": {"inputs": _HLCV, "func": f23_adld_133_cum_net_buy_slope_252_d3},
    "f23_adld_134_cum_net_buy_zscore_252_d3": {"inputs": _HLCV, "func": f23_adld_134_cum_net_buy_zscore_252_d3},
    "f23_adld_135_cum_net_buy_peak_decay_63_d3": {"inputs": _HLCV, "func": f23_adld_135_cum_net_buy_peak_decay_63_d3},
    "f23_adld_136_cum_net_buy_below_sma63_d3": {"inputs": _HLCV, "func": f23_adld_136_cum_net_buy_below_sma63_d3},
    "f23_adld_137_net_buy_pressure_21_d3": {"inputs": _HLCV, "func": f23_adld_137_net_buy_pressure_21_d3},
    "f23_adld_138_net_buy_pressure_63_d3": {"inputs": _HLCV, "func": f23_adld_138_net_buy_pressure_63_d3},
    "f23_adld_139_net_buy_pressure_252_d3": {"inputs": _HLCV, "func": f23_adld_139_net_buy_pressure_252_d3},
    "f23_adld_140_cum_net_buy_bearish_div_63_d3": {"inputs": _HLCV, "func": f23_adld_140_cum_net_buy_bearish_div_63_d3},
    "f23_adld_141_bearish_flow_consensus_count_d3": {"inputs": _HLCV, "func": f23_adld_141_bearish_flow_consensus_count_d3},
    "f23_adld_142_bullish_flow_consensus_count_d3": {"inputs": _HLCV, "func": f23_adld_142_bullish_flow_consensus_count_d3},
    "f23_adld_143_flow_stress_index_d3": {"inputs": _HLCV, "func": f23_adld_143_flow_stress_index_d3},
    "f23_adld_144_ad_minus_wad_divergence_d3": {"inputs": _HLCV, "func": f23_adld_144_ad_minus_wad_divergence_d3},
    "f23_adld_145_cmf_minus_mfi_norm_d3": {"inputs": _HLCV, "func": f23_adld_145_cmf_minus_mfi_norm_d3},
    "f23_adld_146_cmf_range_63_d3": {"inputs": _HLCV, "func": f23_adld_146_cmf_range_63_d3},
    "f23_adld_147_mfi_cross_from_ob_count_63_d3": {"inputs": _HLCV, "func": f23_adld_147_mfi_cross_from_ob_count_63_d3},
    "f23_adld_148_mfi_cross_from_ob_count_252_d3": {"inputs": _HLCV, "func": f23_adld_148_mfi_cross_from_ob_count_252_d3},
    "f23_adld_149_force_index_sign_change_count_63_d3": {"inputs": _CV, "func": f23_adld_149_force_index_sign_change_count_63_d3},
    "f23_adld_150_tmf_cmf_corr_252_d3": {"inputs": _HLCV, "func": f23_adld_150_tmf_cmf_corr_252_d3},
}
