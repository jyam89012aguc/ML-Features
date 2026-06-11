"""donchian_bollinger_keltner_bands base features 076-150 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __base__001_075.py. Each feature
encodes a *different concept* in the volatility-band theme: multi-band
agreement, band-slope dynamics, asymmetry, band-width volatility, band-touch
percentiles, multi-horizon hierarchy, band-volume participation, composite
topping-quality.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family
imports.
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


# Family-specific helpers (identical to __base__001_075.py).

def _bollinger(close, n, k):
    mid = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    sd = close.rolling(n, min_periods=max(n // 3, 2)).std()
    return mid + k * sd, mid, mid - k * sd


def _keltner(high, low, close, n_ema, n_atr, k):
    mid = close.ewm(span=n_ema, adjust=False, min_periods=max(n_ema // 3, 2)).mean()
    atr = _atr(high, low, close, n=n_atr)
    return mid + k * atr, mid, mid - k * atr


def _donchian(high, low, n):
    mp = max(n // 3, 2)
    return high.rolling(n, min_periods=mp).max(), low.rolling(n, min_periods=mp).min()


def _band_width_rel(upper, lower, mid):
    return _safe_div(upper - lower, mid)


def _band_position(close, upper, lower):
    return _safe_div(close - lower, upper - lower)


def _bars_since_true(mask):
    arr = mask.values.astype(bool)
    n = len(arr)
    out = np.full(n, np.nan)
    last = -1
    for i in range(n):
        if arr[i]:
            last = i; out[i] = 0.0
        elif last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=mask.index)


def _streak_true(mask):
    arr = mask.values.astype(bool)
    n = len(arr)
    out = np.zeros(n, dtype=float)
    run = 0
    for i in range(n):
        run = run + 1 if arr[i] else 0
        out[i] = float(run)
    return pd.Series(out, index=mask.index)


def _starc(high, low, close, n=15, mult=2.0):
    """STARC bands (Stoller): SMA(close, n) ± mult × ATR(n)."""
    mid = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    atr = _atr(high, low, close, n=n)
    return mid + mult * atr, mid, mid - mult * atr


def _acceleration_bands(high, low, close, n=20, factor=2.0):
    """Price Headley's Acceleration Bands."""
    ratio = factor * _safe_div(high - low, high + low)
    upper = (high * (1 + ratio)).rolling(n, min_periods=max(n // 3, 2)).mean()
    lower = (low * (1 - ratio)).rolling(n, min_periods=max(n // 3, 2)).mean()
    mid = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    return upper, mid, lower


def _moving_average_envelope(close, n, pct):
    """Moving Average Envelope: SMA(close, n) ± pct."""
    mid = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    return mid * (1 + pct), mid, mid * (1 - pct)


def _choppiness_index(high, low, close, n=14):
    """Choppiness Index (Dreiss): 100 × log10(ΣTR/range) / log10(n). Low=trending, high=ranging."""
    mp = max(n // 3, 2)
    tr = _true_range(high, low, close)
    tr_sum = tr.rolling(n, min_periods=mp).sum()
    max_hi = high.rolling(n, min_periods=mp).max()
    min_lo = low.rolling(n, min_periods=mp).min()
    rng = (max_hi - min_lo).replace(0, np.nan)
    return 100.0 * np.log10(_safe_div(tr_sum, rng)) / np.log10(n)


def _mass_index(high, low, n=25, n_ema=9):
    """Mass Index (Dorsey): Σ(EMA9(HL)/EMA9(EMA9(HL))) over n. Reversal trigger: >27 then <26.5."""
    hl = high - low
    e1 = hl.ewm(span=n_ema, adjust=False, min_periods=max(n_ema // 3, 2)).mean()
    e2 = e1.ewm(span=n_ema, adjust=False, min_periods=max(n_ema // 3, 2)).mean()
    ratio = _safe_div(e1, e2)
    return ratio.rolling(n, min_periods=max(n // 3, 2)).sum()


def _standard_error_bands(close, n=21, k=2.0):
    """Standard Error Bands: rolling LR line ± k × residual SE over n bars. Returns (upper, mid, lower)."""
    mp = max(n // 3, 3)
    arr = close.values
    nb = len(arr)
    mid_arr = np.full(nb, np.nan); se_arr = np.full(nb, np.nan)
    for i in range(nb):
        s = max(0, i - n + 1)
        if i - s + 1 < mp:
            continue
        w = arr[s:i + 1]
        valid = ~np.isnan(w)
        if valid.sum() < mp:
            continue
        w = w[valid]
        if w.size < 3:
            continue
        x = np.arange(w.size, dtype=float)
        xm = x.mean(); wm = w.mean()
        sxx = ((x - xm) ** 2).sum()
        if sxx == 0:
            continue
        sxy = ((x - xm) * (w - wm)).sum()
        b = sxy / sxx
        a = wm - b * xm
        y_pred = a + b * x
        resid = w - y_pred
        mid_arr[i] = float(a + b * x[-1])
        se_arr[i] = float(np.sqrt((resid ** 2).sum() / max(w.size - 2, 1)))
    mid = pd.Series(mid_arr, index=close.index)
    se = pd.Series(se_arr, index=close.index)
    return mid + k * se, mid, mid - k * se


def _ttm_squeeze_momentum(high, low, close, n=20):
    """TTM Squeeze Momentum (Carter): LR value of (close − ((donchian_mid + sma)/2)) over n bars."""
    mp = max(n // 3, 2)
    hh = high.rolling(n, min_periods=mp).max()
    ll = low.rolling(n, min_periods=mp).min()
    dmid = (hh + ll) / 2.0
    sma = close.rolling(n, min_periods=mp).mean()
    src = close - (dmid + sma) / 2.0
    def _fit_last(w):
        if not np.isfinite(w).all() or len(w) < 3:
            return np.nan
        x = np.arange(len(w), dtype=float)
        xm = x.mean(); wm = w.mean()
        sxx = ((x - xm) ** 2).sum()
        if sxx == 0:
            return np.nan
        sxy = ((x - xm) * (w - wm)).sum()
        b = sxy / sxx
        a = wm - b * xm
        return float(a + b * x[-1])
    return src.rolling(n, min_periods=mp).apply(_fit_last, raw=True)


# ============================================================
# Bucket H — Multi-band agreement (076-085)
# ============================================================

def f16_dbkb_076_count_upper_breaks_3systems_today(high, low, close):
    """Count of (Bollinger, Keltner, Donchian-20) upper bands today's close is above."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 2.0)
    du, dl = _donchian(high, low, 20)
    return ((close > bu).astype(float).fillna(0)
            + (close > ku).astype(float).fillna(0)
            + (high >= du).astype(float).fillna(0))


def f16_dbkb_077_count_lower_breaks_3systems_today(high, low, close):
    """Count of (Bollinger, Keltner, Donchian-20) lower bands today's close is below."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 2.0)
    du, dl = _donchian(high, low, 20)
    return ((close < bl).astype(float).fillna(0)
            + (close < kl).astype(float).fillna(0)
            + (low <= dl).astype(float).fillna(0))


def f16_dbkb_078_cross_system_break_disagreement_63d(high, low, close):
    """Bars in 63d where exactly one of 3 upper-bands is broken (cross-system disagreement)."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 2.0)
    du, dl = _donchian(high, low, 20)
    cnt = (close > bu).astype(int).fillna(0) + (close > ku).astype(int).fillna(0) + (high >= du).astype(int).fillna(0)
    one = (cnt == 1).astype(float)
    return one.rolling(QDAYS, min_periods=MDAYS).sum()


def f16_dbkb_079_std_band_positions_3systems(high, low, close):
    """Std of (Bollinger %B, Keltner %position, Donchian-20 %position) — dispersion of band positions."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 2.0)
    du, dl = _donchian(high, low, 20)
    p1 = _band_position(close, bu, bl); p2 = _band_position(close, ku, kl); p3 = _band_position(close, du, dl)
    pieces = pd.concat([p1.rename("a"), p2.rename("b"), p3.rename("c")], axis=1)
    return pieces.std(axis=1)


def f16_dbkb_080_indicator_all_three_position_top_decile(high, low, close):
    """Indicator: all of (Bollinger %B, Keltner %position, Donchian-20 %position) > 0.9."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 2.0)
    du, dl = _donchian(high, low, 20)
    p1 = _band_position(close, bu, bl); p2 = _band_position(close, ku, kl); p3 = _band_position(close, du, dl)
    return ((p1 > 0.9) & (p2 > 0.9) & (p3 > 0.9)).astype(float)


def f16_dbkb_081_count_systems_close_above_all_uppers_63d_frac(high, low, close):
    """Fraction of bars in 63d where close is above all 3 upper bands."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 2.0)
    du, dl = _donchian(high, low, 20)
    cond = ((close > bu) & (close > ku) & (high >= du)).astype(float)
    return cond.rolling(QDAYS, min_periods=MDAYS).mean()


def f16_dbkb_082_indicator_split_keltner_above_bollinger_below_close(high, low, close):
    """Indicator: close > Keltner upper BUT close < Bollinger upper (price between bands — divergence)."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 2.0)
    return ((close > ku) & (close < bu)).astype(float).where(ku.notna() & bu.notna(), np.nan)


def f16_dbkb_083_moving_average_envelope_5pct_upper_break_count_63d(close):
    """Count of bars in 63d where close > SMA(20)×1.05 — fixed-percent Moving Average Envelope upper break (non-vol)."""
    upper, mid, lower = _moving_average_envelope(close, 20, 0.05)
    br = (close > upper).astype(float).where(upper.notna(), np.nan)
    return br.rolling(QDAYS, min_periods=MDAYS).sum()


def f16_dbkb_084_pairwise_corr_band_positions_63d(high, low, close):
    """Mean pairwise correlation of (Bollinger %B, Keltner %position, Donchian %position) over 63d."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 2.0)
    du, dl = _donchian(high, low, 20)
    p1 = _band_position(close, bu, bl); p2 = _band_position(close, ku, kl); p3 = _band_position(close, du, dl)
    c12 = p1.rolling(QDAYS, min_periods=MDAYS).corr(p2)
    c13 = p1.rolling(QDAYS, min_periods=MDAYS).corr(p3)
    c23 = p2.rolling(QDAYS, min_periods=MDAYS).corr(p3)
    return (c12 + c13 + c23) / 3.0


def f16_dbkb_085_count_distinct_break_patterns_63d(high, low, close):
    """Number of distinct (Bollinger, Keltner, Donchian) upper-break code combinations seen in 63d."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 2.0)
    du, dl = _donchian(high, low, 20)
    code = ((close > bu).astype(int).fillna(0) * 4 + (close > ku).astype(int).fillna(0) * 2 + (high >= du).astype(int).fillna(0)).astype(float)
    return code.rolling(QDAYS, min_periods=MDAYS).apply(lambda w: float(len(np.unique(w[~np.isnan(w)]))), raw=True)


# ============================================================
# Bucket I — Band-slope dynamics (086-095)
# ============================================================

def f16_dbkb_086_slope_bollinger_upper_21d(close):
    """Slope of Bollinger(20,2) upper over trailing 21d."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    return _rolling_slope(upper, MDAYS)


def f16_dbkb_087_slope_donchian_upper_20_21d(high, low, close):
    """Slope of Donchian(20) upper over trailing 21d (range-top trajectory)."""
    u, l = _donchian(high, low, 20)
    return _rolling_slope(u, MDAYS)


def f16_dbkb_088_slope_keltner_mid_63d(high, low, close):
    """Slope of Keltner(20,10,2) mid (EMA20) over trailing 63d."""
    upper, mid, lower = _keltner(high, low, close, 20, 10, 2.0)
    return _rolling_slope(mid, QDAYS)


def f16_dbkb_089_slope_diff_upper_minus_lower_bollinger_21d(close):
    """Slope of Bollinger upper − slope of Bollinger lower over 21d — band-opening velocity."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    return _rolling_slope(upper, MDAYS) - _rolling_slope(lower, MDAYS)


def f16_dbkb_090_slope_donchian_upper_252_63d(high, low, close):
    """Slope of Donchian(252) upper over trailing 63d — annual range-top trajectory."""
    u, l = _donchian(high, low, YDAYS)
    return _rolling_slope(u, QDAYS)


def f16_dbkb_091_slope_diff_bollinger_mid_vs_close_63d(close):
    """Slope of Bollinger mid − slope of close over 63d — midline-vs-price divergence."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    return _rolling_slope(mid, QDAYS) - _rolling_slope(close, QDAYS)


def f16_dbkb_092_slope_bollinger_width_63d(close):
    """Slope of Bollinger(20,2) width over trailing 63d — expansion/contraction rate."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    return _rolling_slope(_band_width_rel(upper, lower, mid), QDAYS)


def f16_dbkb_093_slope_keltner_width_63d(high, low, close):
    """Slope of Keltner(20,10,2) width over trailing 63d."""
    upper, mid, lower = _keltner(high, low, close, 20, 10, 2.0)
    return _rolling_slope(_band_width_rel(upper, lower, mid), QDAYS)


def f16_dbkb_094_slope_donchian_width_55_63d(high, low, close):
    """Slope of Donchian(55) width over trailing 63d."""
    u, l = _donchian(high, low, 55)
    mid = (u + l) / 2.0
    return _rolling_slope(_band_width_rel(u, l, mid), QDAYS)


def f16_dbkb_095_curvature_diff_upper_slopes_21vs63(close):
    """Slope(Bollinger upper, 21d) − Slope(Bollinger upper, 63d) — short-vs-medium upper-slope curvature."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    return _rolling_slope(upper, MDAYS) - _rolling_slope(upper, QDAYS)


# ============================================================
# Bucket J — Band asymmetry (096-105)
# ============================================================

def f16_dbkb_096_ratio_upper_to_lower_distance_bollinger(close):
    """(Bollinger upper − close) / (close − Bollinger lower) — close closer to upper or lower?"""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    return _safe_div(upper - close, close - lower)


def f16_dbkb_097_ttm_squeeze_momentum_direction_20(high, low, close):
    """Sign of TTM Squeeze Momentum (Carter, n=20) — direction at squeeze release. +1 bullish, -1 bearish."""
    return np.sign(_ttm_squeeze_momentum(high, low, close, n=20))


def f16_dbkb_098_skew_bollinger_pct_b_63d(close):
    """Skewness of Bollinger %B distribution over trailing 63d."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    pb = _band_position(close, upper, lower)
    return pb.rolling(QDAYS, min_periods=MDAYS).skew()


def f16_dbkb_099_imbalance_upper_to_lower_breaks_252d_bollinger(close):
    """(Bollinger upper breaks − lower breaks) / (upper + lower) over 252d — break asymmetry."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    up = (close > upper).astype(float).where(upper.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).sum()
    dn = (close < lower).astype(float).where(lower.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(up - dn, up + dn)


def f16_dbkb_100_imbalance_upper_to_lower_touches_donchian_252(high, low, close):
    """(Donchian-252 upper touches − lower touches) / (sum) over 252d — range-top vs range-bottom asymmetry."""
    u, l = _donchian(high, low, YDAYS)
    ut = (high >= u).astype(float).where(u.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).sum()
    lt = (low <= l).astype(float).where(l.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(ut - lt, ut + lt)


def f16_dbkb_101_pos_in_bollinger_band_centered_minus_half(close):
    """Bollinger %B − 0.5 — signed deviation from band center."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    return _band_position(close, upper, lower) - 0.5


def f16_dbkb_102_atr_normalized_close_to_upper_minus_close_to_lower(high, low, close):
    """((Bollinger upper − close) − (close − Bollinger lower)) / ATR(21) — asymmetry in ATR units."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    return _safe_div((upper - close) - (close - lower), _atr(high, low, close, n=MDAYS))


def f16_dbkb_103_dwell_time_pct_b_above_05_minus_below_05_252d(close):
    """Fraction-of-bars(%B>0.5) − Fraction-of-bars(%B<0.5) over 252d — dwell-time asymmetry."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    pb = _band_position(close, upper, lower)
    up = (pb > 0.5).astype(float).where(pb.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    dn = (pb < 0.5).astype(float).where(pb.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return up - dn


def f16_dbkb_104_choppiness_index_14d(high, low, close):
    """Choppiness Index (Dreiss, 14d): 100·log10(ΣTR/range)/log10(14). <38.2 = trending; >61.8 = ranging."""
    return _choppiness_index(high, low, close, n=14)


def f16_dbkb_105_ratio_bars_above_mid_to_bars_below_mid_bollinger_252d(close):
    """In 252d: bars-with-close-above-mid / bars-with-close-below-mid (Bollinger)."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    above = (close > mid).astype(float).where(mid.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).sum()
    below = (close < mid).astype(float).where(mid.notna(), np.nan).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(above, below)


# ============================================================
# Bucket K — Band-width volatility (106-114)
# ============================================================

def f16_dbkb_106_std_bollinger_width_in_63d(close):
    """Std of Bollinger(20,2) width over trailing 63d — vol-of-band-width."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    return _band_width_rel(upper, lower, mid).rolling(QDAYS, min_periods=MDAYS).std()


def f16_dbkb_107_mass_index_reversal_trigger_25d(high, low, close):
    """Indicator: Mass Index(25,9) crossed >27 within last 25 bars AND crossed back <26.5 today — Dorsey reversal trigger."""
    mi = _mass_index(high, low, n=25, n_ema=9)
    crossed_high_in_25 = (mi > 27).astype(int).rolling(25, min_periods=1).max().fillna(0)
    crossed_back = ((mi < 26.5) & (mi.shift(1) >= 26.5)).astype(int)
    return ((crossed_back == 1) & (crossed_high_in_25 == 1)).astype(float)


def f16_dbkb_108_entropy_bollinger_width_63d(close):
    """5-bin Shannon entropy of Bollinger(20,2) width distribution over 63d."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    w = _band_width_rel(upper, lower, mid)
    def _ent(arr):
        v = arr[~np.isnan(arr)]
        if v.size < 10:
            return np.nan
        lo, hi = v.min(), v.max()
        if hi <= lo:
            return 0.0
        bins = np.linspace(lo, hi, 6)
        counts, _ = np.histogram(v, bins=bins)
        s = counts.sum()
        if s == 0:
            return np.nan
        p = counts / s
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    return w.rolling(QDAYS, min_periods=MDAYS).apply(_ent, raw=True)


def f16_dbkb_109_std_keltner_width_in_63d(high, low, close):
    """Std of Keltner(20,10,2) width over trailing 63d."""
    upper, mid, lower = _keltner(high, low, close, 20, 10, 2.0)
    return _band_width_rel(upper, lower, mid).rolling(QDAYS, min_periods=MDAYS).std()


def f16_dbkb_110_mass_index_25_9(high, low, close):
    """Mass Index (Dorsey, 25-bar Σ of EMA9(HL)/EMA9(EMA9(HL))). Reversal trigger >27 then crossing back below 26.5."""
    return _mass_index(high, low, n=25, n_ema=9)


def f16_dbkb_111_ratio_std_bollinger_width_21_to_252d(close):
    """Std(width, 21d) / Std(width, 252d) — width-vol compression metric."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    w = _band_width_rel(upper, lower, mid)
    return _safe_div(w.rolling(MDAYS, min_periods=WDAYS).std(), w.rolling(YDAYS, min_periods=QDAYS).std())


def f16_dbkb_112_smoothed_d1_bollinger_width_5d(close):
    """5d-smoothed first-difference of Bollinger(20,2) width — width velocity."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    return _band_width_rel(upper, lower, mid).diff().rolling(WDAYS, min_periods=2).mean()


def f16_dbkb_113_triple_squeeze_bb_kc_dc_p10_indicator(high, low, close):
    """Indicator: Bollinger(20,2) + Keltner(20,10,2) + Donchian(20) widths ALL ≤ their 10th-pct(252d) — triple-system compression."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 2.0)
    du, dl = _donchian(high, low, 20)
    bw = _band_width_rel(bu, bl, bm)
    kw = _band_width_rel(ku, kl, km)
    dw = _band_width_rel(du, dl, (du + dl) / 2.0)
    p10_b = bw.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    p10_k = kw.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    p10_d = dw.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    return ((bw <= p10_b) & (kw <= p10_k) & (dw <= p10_d)).astype(float).where(
        p10_b.notna() & p10_k.notna() & p10_d.notna(), np.nan
    )


def f16_dbkb_114_max_drawdown_bollinger_width_from_252d_peak(close):
    """Bollinger width / its trailing-252d-max − 1 — width drawdown from its peak."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    w = _band_width_rel(upper, lower, mid)
    return _safe_div(w, w.rolling(YDAYS, min_periods=QDAYS).max()) - 1.0


# ============================================================
# Bucket L — Band-touch percentiles & extremes (115-122)
# ============================================================

def f16_dbkb_115_pctile_rank_bollinger_width_in_1260d(close):
    """Empirical percentile rank of Bollinger(20,2) width in trailing 1260d distribution."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    w = _band_width_rel(upper, lower, mid)
    def _rk(arr):
        if np.isnan(arr).all():
            return np.nan
        last = arr[-1]
        v = arr[~np.isnan(arr)]
        return float((v <= last).sum()) / float(v.size) if v.size else np.nan
    return w.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_rk, raw=True)


def f16_dbkb_116_indicator_extreme_extension_above_bollinger_upper(high, low, close):
    """Indicator: close > Bollinger upper + 1×ATR(21) — extreme extension beyond upper band."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    atr = _atr(high, low, close, n=MDAYS)
    return (close > upper + atr).astype(float).where(upper.notna() & atr.notna(), np.nan)


def f16_dbkb_117_pctile_rank_bollinger_pct_b_252d(close):
    """Empirical percentile rank of current Bollinger %B in trailing 252d."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    pb = _band_position(close, upper, lower)
    def _rk(arr):
        if np.isnan(arr).all():
            return np.nan
        last = arr[-1]
        v = arr[~np.isnan(arr)]
        return float((v <= last).sum()) / float(v.size) if v.size else np.nan
    return pb.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)


def f16_dbkb_118_bars_since_bollinger_pct_b_above_p95(close):
    """Bars since most recent Bollinger %B > its 252d 95th-pct."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    pb = _band_position(close, upper, lower)
    p95 = pb.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    return _bars_since_true(((pb > p95) & p95.notna()).astype(bool))


def f16_dbkb_119_count_bars_donchian_252_upper_touched_504d(high, low, close):
    """Count of bars in 504d where high >= Donchian(252) upper — annual-high touch count."""
    u, l = _donchian(high, low, YDAYS)
    return ((high >= u) & u.notna()).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f16_dbkb_120_max_excursion_above_bollinger_upper_atr_21d(high, low, close):
    """Max (close − Bollinger upper)/ATR(21) over trailing 21d — peak ATR-normalized excursion."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    atr = _atr(high, low, close, n=MDAYS)
    e = _safe_div(close - upper, atr).clip(lower=0)
    return e.rolling(MDAYS, min_periods=WDAYS).max()


def f16_dbkb_121_bollinger_m_top_detector_21d(close):
    """Bulkowski-style M-top indicator: 2+ Bollinger upper-touches in last 21d, separated by ≥3 bars, with a close-below-mid bar between them."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    touch = ((close >= 0.99 * upper) & upper.notna()).values
    below_mid = ((close < mid) & mid.notna()).values
    nb = len(touch)
    out = np.full(nb, np.nan)
    for i in range(nb):
        s = max(0, i - 20)
        if i - s + 1 < 7:
            continue
        touch_idx = [s + j for j in range(i - s + 1) if touch[s + j]]
        if len(touch_idx) < 2:
            out[i] = 0.0
            continue
        found = False
        for a in range(len(touch_idx)):
            for b in range(a + 1, len(touch_idx)):
                if touch_idx[b] - touch_idx[a] < 3:
                    continue
                between_below = False
                for kk in range(touch_idx[a] + 1, touch_idx[b]):
                    if below_mid[kk]:
                        between_below = True; break
                if between_below:
                    found = True; break
            if found:
                break
        out[i] = 1.0 if found else 0.0
    return pd.Series(out, index=close.index)


def f16_dbkb_122_indicator_today_at_252d_band_extreme(close):
    """Indicator: today's Bollinger %B equals trailing-252d max of %B (current band-extreme bar)."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    pb = _band_position(close, upper, lower)
    return (pb >= pb.rolling(YDAYS, min_periods=QDAYS).max()).astype(float).where(pb.notna(), np.nan)


# ============================================================
# Bucket M — Multi-horizon band hierarchy (123-132)
# ============================================================

def f16_dbkb_123_diff_bollinger_width_20_minus_50_norm_mid(close):
    """(Bollinger(20,2) width − Bollinger(50,2) width) / mid_20 — short-vs-medium width difference."""
    u20, m20, l20 = _bollinger(close, 20, 2.0)
    u50, m50, l50 = _bollinger(close, 50, 2.0)
    return _safe_div((u20 - l20) - (u50 - l50), m20)


def f16_dbkb_124_ratio_bollinger_width_20_to_50(close):
    """Bollinger(20,2) width / Bollinger(50,2) width — short/medium width ratio."""
    u20, m20, l20 = _bollinger(close, 20, 2.0)
    u50, m50, l50 = _bollinger(close, 50, 2.0)
    return _safe_div(u20 - l20, u50 - l50)


def f16_dbkb_125_keltner_short_vs_long_width_ratio(high, low, close):
    """Keltner(20,10,2) width / Keltner(50,20,2) width."""
    u1, m1, l1 = _keltner(high, low, close, 20, 10, 2.0)
    u2, m2, l2 = _keltner(high, low, close, 50, 20, 2.0)
    return _safe_div(u1 - l1, u2 - l2)


def f16_dbkb_126_donchian_20_vs_55_width_ratio(high, low, close):
    """Donchian(20) width / Donchian(55) width — short vs Turtle-medium."""
    u20, l20 = _donchian(high, low, 20)
    u55, l55 = _donchian(high, low, 55)
    return _safe_div(u20 - l20, u55 - l55)


def f16_dbkb_127_count_horizons_in_squeeze(high, low, close):
    """Count of {Bollinger(20,2), Bollinger(50,2), Bollinger(252,2)} in their respective 10th-pct-width state."""
    def _sqz(n):
        u, m, l = _bollinger(close, n, 2.0)
        w = _band_width_rel(u, l, m)
        p10 = w.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
        return (w <= p10).astype(float).where(p10.notna(), np.nan)
    return _sqz(20).fillna(0) + _sqz(50).fillna(0) + _sqz(YDAYS).fillna(0)


def f16_dbkb_128_indicator_all_3_bollinger_horizons_widening(close):
    """Indicator: Bollinger width is increasing (positive 5d slope) across 20, 50, 252 horizons simultaneously."""
    def _sl(n):
        u, m, l = _bollinger(close, n, 2.0)
        return _rolling_slope(_band_width_rel(u, l, m), WDAYS)
    return ((_sl(20) > 0) & (_sl(50) > 0) & (_sl(YDAYS) > 0)).astype(float)


def f16_dbkb_129_diff_pct_b_20_minus_pct_b_50(close):
    """Bollinger(20,2) %B − Bollinger(50,2) %B — short-vs-medium position difference."""
    u20, m20, l20 = _bollinger(close, 20, 2.0)
    u50, m50, l50 = _bollinger(close, 50, 2.0)
    return _band_position(close, u20, l20) - _band_position(close, u50, l50)


def f16_dbkb_130_ratio_donchian_252_to_1260_width(high, low, close):
    """Donchian(252) width / Donchian(1260) width — annual vs 5y range ratio."""
    u252, l252 = _donchian(high, low, YDAYS)
    u1260, l1260 = _donchian(high, low, DDAYS_5Y)
    return _safe_div(u252 - l252, u1260 - l1260)


def f16_dbkb_131_keltner_long_horizon_pct_position_252_50(high, low, close):
    """Keltner(50,20,2) %position — long-horizon Keltner band position."""
    upper, mid, lower = _keltner(high, low, close, 50, 20, 2.0)
    return _band_position(close, upper, lower)


def f16_dbkb_132_count_horizons_close_above_upper(high, low, close):
    """Count of {Bollinger(20,2), Keltner(20,10,2), Donchian(20)} upper bands close is above currently — multi-horizon variant."""
    bu, bm, bl = _bollinger(close, 50, 2.0)  # medium Bollinger
    ku, km, kl = _keltner(high, low, close, 50, 20, 2.0)  # slow Keltner
    du, dl = _donchian(high, low, 55)  # turtle Donchian
    return ((close > bu).astype(float).fillna(0)
            + (close > ku).astype(float).fillna(0)
            + (high >= du).astype(float).fillna(0))


# ============================================================
# Bucket N — Band-related volume / participation (133-140)
# ============================================================

def f16_dbkb_133_volume_zscore_on_bollinger_upper_break_bars_252d(high, low, close, volume):
    """Mean z-score(252d) of volume on bars where close > Bollinger upper, over 252d (volume-weighted break-quality)."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    vz = _rolling_zscore(volume, YDAYS)
    bv = vz.where((close > upper) & upper.notna(), np.nan)
    return bv.rolling(YDAYS, min_periods=QDAYS).mean()


def f16_dbkb_134_obv_sign_on_bollinger_upper_break_252d(close, volume):
    """Mean sign of close-return on Bollinger upper-break bars, weighted by volume z-score, over 252d."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    sign_ret = np.sign(close.diff())
    vz = _rolling_zscore(volume, YDAYS)
    masked = (sign_ret * vz).where((close > upper) & upper.notna(), np.nan)
    return masked.rolling(YDAYS, min_periods=QDAYS).mean()


def f16_dbkb_135_dollar_volume_on_donchian_upper_break_bars_252d(high, low, close, volume):
    """Mean (close × volume) on Donchian(20)-upper-break bars over 252d — dollar-vol on breakouts."""
    u, l = _donchian(high, low, 20)
    dv = close * volume
    masked = dv.where((high >= u) & u.notna(), np.nan)
    return masked.rolling(YDAYS, min_periods=QDAYS).mean()


def f16_dbkb_136_count_high_volume_bollinger_breaks_252d(close, volume):
    """Count in 252d of bars where close>Bollinger upper AND volume z-score>2 — climax breakouts."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    vz = _rolling_zscore(volume, YDAYS)
    cond = ((close > upper) & upper.notna() & (vz > 2)).astype(float)
    return cond.rolling(YDAYS, min_periods=QDAYS).sum()


def f16_dbkb_137_avg_volume_in_squeeze_state_252d(high, low, close, volume):
    """Mean volume during TTM-squeeze bars over 252d, normalized by 252d-mean volume — squeeze participation."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 1.5)
    sq = ((bu < ku) & (bl > kl)).astype(bool)
    v_in = volume.where(sq, np.nan)
    return _safe_div(v_in.rolling(YDAYS, min_periods=QDAYS).mean(), volume.rolling(YDAYS, min_periods=QDAYS).mean())


def f16_dbkb_138_volume_decline_in_walking_upper_bollinger_21d(close, volume):
    """If walking-upper (close>upper for ≥3 of last 5 bars): mean(vol_last_5) / mean(vol_prev_5) — volume-decline indicator."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    walking = (((close > upper).astype(int).rolling(WDAYS, min_periods=WDAYS).sum()) >= 3)
    v5 = volume.rolling(WDAYS, min_periods=WDAYS).mean()
    v_prev = v5.shift(WDAYS)
    return (_safe_div(v5, v_prev)).where(walking, np.nan)


def f16_dbkb_139_volume_zscore_on_first_keltner_upper_break_in_21d(high, low, close, volume):
    """Volume z-score(252d) at most-recent Keltner upper-break bar within the trailing 21d window."""
    upper, mid, lower = _keltner(high, low, close, 20, 10, 2.0)
    vz = _rolling_zscore(volume, YDAYS)
    breaks = ((close > upper) & upper.notna()).astype(bool)
    bsb = _bars_since_true(breaks)
    arr = vz.values; bs = bsb.values
    n = len(arr)
    out = np.full(n, np.nan)
    for i in range(n):
        if np.isnan(bs[i]) or bs[i] > MDAYS:
            continue
        anchor = i - int(bs[i])
        if 0 <= anchor < n and not np.isnan(arr[anchor]):
            out[i] = arr[anchor]
    return pd.Series(out, index=close.index)


def f16_dbkb_140_dollar_volume_decline_during_walking_donchian_55_21d(high, low, close, volume):
    """If walking-upper Donchian(55) (high>=upper for ≥3 of last 5): mean(dv_last_5) / mean(dv_prev_5)."""
    u, l = _donchian(high, low, 55)
    walking = (((high >= u).astype(int).rolling(WDAYS, min_periods=WDAYS).sum()) >= 3)
    dv = close * volume
    dv5 = dv.rolling(WDAYS, min_periods=WDAYS).mean()
    return (_safe_div(dv5, dv5.shift(WDAYS))).where(walking, np.nan)


# ============================================================
# Bucket O — Composite topping-quality (141-150)
# ============================================================

def f16_dbkb_141_walking_upper_x_width_pctile_rank(close):
    """(walking-upper fraction in 21d) × (Bollinger-width percentile rank in 252d) — extension × expansion combined."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    walk_frac = ((close > upper) & upper.notna()).astype(float).rolling(MDAYS, min_periods=WDAYS).mean()
    w = _band_width_rel(upper, lower, mid)
    def _rk(arr):
        if np.isnan(arr).all():
            return np.nan
        last = arr[-1]
        v = arr[~np.isnan(arr)]
        return float((v <= last).sum()) / float(v.size) if v.size else np.nan
    width_rk = w.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)
    return walk_frac * width_rk


def f16_dbkb_142_composite_extension_health_bollinger_keltner(high, low, close):
    """Bollinger %B × Keltner %position — joint extended-position score."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 2.0)
    return _band_position(close, bu, bl) * _band_position(close, ku, kl)


def f16_dbkb_143_consensus_break_failure_index_252d(high, low, close):
    """In 252d: bars where (Bollinger upper-break-then-fail) OR (Keltner upper-break-then-fail within 5d) — failure consensus count."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 2.0)
    b_past = ((close > bu) & bu.notna()).shift(WDAYS).fillna(False)
    b_fail = (close < bm).rolling(WDAYS, min_periods=1).max().fillna(0) > 0
    bfail = (b_past & b_fail).astype(int)
    k_past = ((close > ku) & ku.notna()).shift(WDAYS).fillna(False)
    k_fail = (close < km).rolling(WDAYS, min_periods=1).max().fillna(0) > 0
    kfail = (k_past & k_fail).astype(int)
    any_fail = ((bfail + kfail) > 0).astype(float)
    return any_fail.rolling(YDAYS, min_periods=QDAYS).sum()


def f16_dbkb_144_squeeze_then_fail_upper_break_indicator(high, low, close):
    """Indicator: a TTM-squeeze release within last 21d AND a Bollinger upper-break-then-fail within last 21d."""
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 1.5)
    sq = ((bu < ku) & (bl > kl)).astype(int)
    release = ((sq.shift(1) == 1) & (sq == 0)).astype(int)
    rel_in_21 = release.rolling(MDAYS, min_periods=1).sum().fillna(0) > 0
    bu2, bm2, bl2 = _bollinger(close, 20, 2.0)
    b_past = ((close > bu2) & bu2.notna()).shift(WDAYS).fillna(False)
    b_fail = (close < bm2).rolling(WDAYS, min_periods=1).max().fillna(0) > 0
    bfail = (b_past & b_fail).astype(int)
    bfail_in_21 = bfail.rolling(MDAYS, min_periods=1).sum().fillna(0) > 0
    return (rel_in_21 & bfail_in_21).astype(float)


def f16_dbkb_145_band_position_acceleration_21d(close):
    """Second-difference of Bollinger %B over 21d — acceleration of band position."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    return _band_position(close, upper, lower).diff().diff().rolling(WDAYS, min_periods=2).mean()


def f16_dbkb_146_topping_quality_composite_score(high, low, close):
    """Σ z-scored of (extension above Bollinger upper, walking-upper fraction, width-pctile-rank, position-asymmetry)."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    ext = _rolling_zscore(_safe_div(close - upper, upper), YDAYS)
    walk = _rolling_zscore(((close > upper) & upper.notna()).astype(float).rolling(MDAYS, min_periods=WDAYS).mean(), YDAYS)
    w = _band_width_rel(upper, lower, mid)
    def _rk(arr):
        if np.isnan(arr).all():
            return np.nan
        last = arr[-1]
        v = arr[~np.isnan(arr)]
        return float((v <= last).sum()) / float(v.size) if v.size else np.nan
    wpr = w.rolling(YDAYS, min_periods=QDAYS).apply(_rk, raw=True)
    asym = _rolling_zscore(_band_position(close, upper, lower) - 0.5, YDAYS)
    return ext.fillna(0) + walk.fillna(0) + wpr.fillna(0) + asym.fillna(0)


def f16_dbkb_147_diff_pct_b_now_minus_p95_252d(close):
    """Bollinger %B − its 95th-pct in 252d — distance above empirical-extreme position."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    pb = _band_position(close, upper, lower)
    p95 = pb.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    return pb - p95


def f16_dbkb_148_indicator_compound_break_failure_walking_squeeze(high, low, close):
    """Indicator: walking-upper-Bollinger AND post-TTM-squeeze release AND Bollinger break-failure recent — compound topping setup."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    walking = (((close > upper).astype(int).rolling(WDAYS, min_periods=WDAYS).sum()) >= 3)
    bu, bm, bl = _bollinger(close, 20, 2.0)
    ku, km, kl = _keltner(high, low, close, 20, 10, 1.5)
    sq = ((bu < ku) & (bl > kl)).astype(int)
    release = ((sq.shift(1) == 1) & (sq == 0)).astype(int)
    rel_in_21 = release.rolling(MDAYS, min_periods=1).sum().fillna(0) > 0
    b_past = ((close > upper) & upper.notna()).shift(WDAYS).fillna(False)
    b_fail = (close < mid).rolling(WDAYS, min_periods=1).max().fillna(0) > 0
    bfail_in_21 = (b_past & b_fail).astype(int).rolling(MDAYS, min_periods=1).sum().fillna(0) > 0
    return (walking & rel_in_21 & bfail_in_21).astype(float)


def f16_dbkb_149_ratio_walking_upper_to_walking_lower_63d(close):
    """(fraction of bars with close>Bollinger upper in 63d) / (fraction with close<Bollinger lower in 63d)."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    up = ((close > upper) & upper.notna()).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    dn = ((close < lower) & lower.notna()).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(up, dn)


def f16_dbkb_150_cum_extension_above_bollinger_upper_atr_252d(high, low, close):
    """Σ max((close − Bollinger upper)/ATR(21), 0) over trailing 252d — cumulative ATR-extension."""
    upper, mid, lower = _bollinger(close, 20, 2.0)
    atr = _atr(high, low, close, n=MDAYS)
    e = _safe_div(close - upper, atr).clip(lower=0)
    return e.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
#                         REGISTRY 076-150
# ============================================================

DONCHIAN_BOLLINGER_KELTNER_BANDS_BASE_REGISTRY_076_150 = {
    "f16_dbkb_076_count_upper_breaks_3systems_today": {"inputs": ["high", "low", "close"], "func": f16_dbkb_076_count_upper_breaks_3systems_today},
    "f16_dbkb_077_count_lower_breaks_3systems_today": {"inputs": ["high", "low", "close"], "func": f16_dbkb_077_count_lower_breaks_3systems_today},
    "f16_dbkb_078_cross_system_break_disagreement_63d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_078_cross_system_break_disagreement_63d},
    "f16_dbkb_079_std_band_positions_3systems": {"inputs": ["high", "low", "close"], "func": f16_dbkb_079_std_band_positions_3systems},
    "f16_dbkb_080_indicator_all_three_position_top_decile": {"inputs": ["high", "low", "close"], "func": f16_dbkb_080_indicator_all_three_position_top_decile},
    "f16_dbkb_081_count_systems_close_above_all_uppers_63d_frac": {"inputs": ["high", "low", "close"], "func": f16_dbkb_081_count_systems_close_above_all_uppers_63d_frac},
    "f16_dbkb_082_indicator_split_keltner_above_bollinger_below_close": {"inputs": ["high", "low", "close"], "func": f16_dbkb_082_indicator_split_keltner_above_bollinger_below_close},
    "f16_dbkb_083_moving_average_envelope_5pct_upper_break_count_63d": {"inputs": ["close"], "func": f16_dbkb_083_moving_average_envelope_5pct_upper_break_count_63d},
    "f16_dbkb_084_pairwise_corr_band_positions_63d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_084_pairwise_corr_band_positions_63d},
    "f16_dbkb_085_count_distinct_break_patterns_63d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_085_count_distinct_break_patterns_63d},
    "f16_dbkb_086_slope_bollinger_upper_21d": {"inputs": ["close"], "func": f16_dbkb_086_slope_bollinger_upper_21d},
    "f16_dbkb_087_slope_donchian_upper_20_21d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_087_slope_donchian_upper_20_21d},
    "f16_dbkb_088_slope_keltner_mid_63d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_088_slope_keltner_mid_63d},
    "f16_dbkb_089_slope_diff_upper_minus_lower_bollinger_21d": {"inputs": ["close"], "func": f16_dbkb_089_slope_diff_upper_minus_lower_bollinger_21d},
    "f16_dbkb_090_slope_donchian_upper_252_63d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_090_slope_donchian_upper_252_63d},
    "f16_dbkb_091_slope_diff_bollinger_mid_vs_close_63d": {"inputs": ["close"], "func": f16_dbkb_091_slope_diff_bollinger_mid_vs_close_63d},
    "f16_dbkb_092_slope_bollinger_width_63d": {"inputs": ["close"], "func": f16_dbkb_092_slope_bollinger_width_63d},
    "f16_dbkb_093_slope_keltner_width_63d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_093_slope_keltner_width_63d},
    "f16_dbkb_094_slope_donchian_width_55_63d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_094_slope_donchian_width_55_63d},
    "f16_dbkb_095_curvature_diff_upper_slopes_21vs63": {"inputs": ["close"], "func": f16_dbkb_095_curvature_diff_upper_slopes_21vs63},
    "f16_dbkb_096_ratio_upper_to_lower_distance_bollinger": {"inputs": ["close"], "func": f16_dbkb_096_ratio_upper_to_lower_distance_bollinger},
    "f16_dbkb_097_ttm_squeeze_momentum_direction_20": {"inputs": ["high", "low", "close"], "func": f16_dbkb_097_ttm_squeeze_momentum_direction_20},
    "f16_dbkb_098_skew_bollinger_pct_b_63d": {"inputs": ["close"], "func": f16_dbkb_098_skew_bollinger_pct_b_63d},
    "f16_dbkb_099_imbalance_upper_to_lower_breaks_252d_bollinger": {"inputs": ["close"], "func": f16_dbkb_099_imbalance_upper_to_lower_breaks_252d_bollinger},
    "f16_dbkb_100_imbalance_upper_to_lower_touches_donchian_252": {"inputs": ["high", "low", "close"], "func": f16_dbkb_100_imbalance_upper_to_lower_touches_donchian_252},
    "f16_dbkb_101_pos_in_bollinger_band_centered_minus_half": {"inputs": ["close"], "func": f16_dbkb_101_pos_in_bollinger_band_centered_minus_half},
    "f16_dbkb_102_atr_normalized_close_to_upper_minus_close_to_lower": {"inputs": ["high", "low", "close"], "func": f16_dbkb_102_atr_normalized_close_to_upper_minus_close_to_lower},
    "f16_dbkb_103_dwell_time_pct_b_above_05_minus_below_05_252d": {"inputs": ["close"], "func": f16_dbkb_103_dwell_time_pct_b_above_05_minus_below_05_252d},
    "f16_dbkb_104_choppiness_index_14d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_104_choppiness_index_14d},
    "f16_dbkb_105_ratio_bars_above_mid_to_bars_below_mid_bollinger_252d": {"inputs": ["close"], "func": f16_dbkb_105_ratio_bars_above_mid_to_bars_below_mid_bollinger_252d},
    "f16_dbkb_106_std_bollinger_width_in_63d": {"inputs": ["close"], "func": f16_dbkb_106_std_bollinger_width_in_63d},
    "f16_dbkb_107_mass_index_reversal_trigger_25d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_107_mass_index_reversal_trigger_25d},
    "f16_dbkb_108_entropy_bollinger_width_63d": {"inputs": ["close"], "func": f16_dbkb_108_entropy_bollinger_width_63d},
    "f16_dbkb_109_std_keltner_width_in_63d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_109_std_keltner_width_in_63d},
    "f16_dbkb_110_mass_index_25_9": {"inputs": ["high", "low", "close"], "func": f16_dbkb_110_mass_index_25_9},
    "f16_dbkb_111_ratio_std_bollinger_width_21_to_252d": {"inputs": ["close"], "func": f16_dbkb_111_ratio_std_bollinger_width_21_to_252d},
    "f16_dbkb_112_smoothed_d1_bollinger_width_5d": {"inputs": ["close"], "func": f16_dbkb_112_smoothed_d1_bollinger_width_5d},
    "f16_dbkb_113_triple_squeeze_bb_kc_dc_p10_indicator": {"inputs": ["high", "low", "close"], "func": f16_dbkb_113_triple_squeeze_bb_kc_dc_p10_indicator},
    "f16_dbkb_114_max_drawdown_bollinger_width_from_252d_peak": {"inputs": ["close"], "func": f16_dbkb_114_max_drawdown_bollinger_width_from_252d_peak},
    "f16_dbkb_115_pctile_rank_bollinger_width_in_1260d": {"inputs": ["close"], "func": f16_dbkb_115_pctile_rank_bollinger_width_in_1260d},
    "f16_dbkb_116_indicator_extreme_extension_above_bollinger_upper": {"inputs": ["high", "low", "close"], "func": f16_dbkb_116_indicator_extreme_extension_above_bollinger_upper},
    "f16_dbkb_117_pctile_rank_bollinger_pct_b_252d": {"inputs": ["close"], "func": f16_dbkb_117_pctile_rank_bollinger_pct_b_252d},
    "f16_dbkb_118_bars_since_bollinger_pct_b_above_p95": {"inputs": ["close"], "func": f16_dbkb_118_bars_since_bollinger_pct_b_above_p95},
    "f16_dbkb_119_count_bars_donchian_252_upper_touched_504d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_119_count_bars_donchian_252_upper_touched_504d},
    "f16_dbkb_120_max_excursion_above_bollinger_upper_atr_21d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_120_max_excursion_above_bollinger_upper_atr_21d},
    "f16_dbkb_121_bollinger_m_top_detector_21d": {"inputs": ["close"], "func": f16_dbkb_121_bollinger_m_top_detector_21d},
    "f16_dbkb_122_indicator_today_at_252d_band_extreme": {"inputs": ["close"], "func": f16_dbkb_122_indicator_today_at_252d_band_extreme},
    "f16_dbkb_123_diff_bollinger_width_20_minus_50_norm_mid": {"inputs": ["close"], "func": f16_dbkb_123_diff_bollinger_width_20_minus_50_norm_mid},
    "f16_dbkb_124_ratio_bollinger_width_20_to_50": {"inputs": ["close"], "func": f16_dbkb_124_ratio_bollinger_width_20_to_50},
    "f16_dbkb_125_keltner_short_vs_long_width_ratio": {"inputs": ["high", "low", "close"], "func": f16_dbkb_125_keltner_short_vs_long_width_ratio},
    "f16_dbkb_126_donchian_20_vs_55_width_ratio": {"inputs": ["high", "low", "close"], "func": f16_dbkb_126_donchian_20_vs_55_width_ratio},
    "f16_dbkb_127_count_horizons_in_squeeze": {"inputs": ["high", "low", "close"], "func": f16_dbkb_127_count_horizons_in_squeeze},
    "f16_dbkb_128_indicator_all_3_bollinger_horizons_widening": {"inputs": ["close"], "func": f16_dbkb_128_indicator_all_3_bollinger_horizons_widening},
    "f16_dbkb_129_diff_pct_b_20_minus_pct_b_50": {"inputs": ["close"], "func": f16_dbkb_129_diff_pct_b_20_minus_pct_b_50},
    "f16_dbkb_130_ratio_donchian_252_to_1260_width": {"inputs": ["high", "low", "close"], "func": f16_dbkb_130_ratio_donchian_252_to_1260_width},
    "f16_dbkb_131_keltner_long_horizon_pct_position_252_50": {"inputs": ["high", "low", "close"], "func": f16_dbkb_131_keltner_long_horizon_pct_position_252_50},
    "f16_dbkb_132_count_horizons_close_above_upper": {"inputs": ["high", "low", "close"], "func": f16_dbkb_132_count_horizons_close_above_upper},
    "f16_dbkb_133_volume_zscore_on_bollinger_upper_break_bars_252d": {"inputs": ["high", "low", "close", "volume"], "func": f16_dbkb_133_volume_zscore_on_bollinger_upper_break_bars_252d},
    "f16_dbkb_134_obv_sign_on_bollinger_upper_break_252d": {"inputs": ["close", "volume"], "func": f16_dbkb_134_obv_sign_on_bollinger_upper_break_252d},
    "f16_dbkb_135_dollar_volume_on_donchian_upper_break_bars_252d": {"inputs": ["high", "low", "close", "volume"], "func": f16_dbkb_135_dollar_volume_on_donchian_upper_break_bars_252d},
    "f16_dbkb_136_count_high_volume_bollinger_breaks_252d": {"inputs": ["close", "volume"], "func": f16_dbkb_136_count_high_volume_bollinger_breaks_252d},
    "f16_dbkb_137_avg_volume_in_squeeze_state_252d": {"inputs": ["high", "low", "close", "volume"], "func": f16_dbkb_137_avg_volume_in_squeeze_state_252d},
    "f16_dbkb_138_volume_decline_in_walking_upper_bollinger_21d": {"inputs": ["close", "volume"], "func": f16_dbkb_138_volume_decline_in_walking_upper_bollinger_21d},
    "f16_dbkb_139_volume_zscore_on_first_keltner_upper_break_in_21d": {"inputs": ["high", "low", "close", "volume"], "func": f16_dbkb_139_volume_zscore_on_first_keltner_upper_break_in_21d},
    "f16_dbkb_140_dollar_volume_decline_during_walking_donchian_55_21d": {"inputs": ["high", "low", "close", "volume"], "func": f16_dbkb_140_dollar_volume_decline_during_walking_donchian_55_21d},
    "f16_dbkb_141_walking_upper_x_width_pctile_rank": {"inputs": ["close"], "func": f16_dbkb_141_walking_upper_x_width_pctile_rank},
    "f16_dbkb_142_composite_extension_health_bollinger_keltner": {"inputs": ["high", "low", "close"], "func": f16_dbkb_142_composite_extension_health_bollinger_keltner},
    "f16_dbkb_143_consensus_break_failure_index_252d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_143_consensus_break_failure_index_252d},
    "f16_dbkb_144_squeeze_then_fail_upper_break_indicator": {"inputs": ["high", "low", "close"], "func": f16_dbkb_144_squeeze_then_fail_upper_break_indicator},
    "f16_dbkb_145_band_position_acceleration_21d": {"inputs": ["close"], "func": f16_dbkb_145_band_position_acceleration_21d},
    "f16_dbkb_146_topping_quality_composite_score": {"inputs": ["high", "low", "close"], "func": f16_dbkb_146_topping_quality_composite_score},
    "f16_dbkb_147_diff_pct_b_now_minus_p95_252d": {"inputs": ["close"], "func": f16_dbkb_147_diff_pct_b_now_minus_p95_252d},
    "f16_dbkb_148_indicator_compound_break_failure_walking_squeeze": {"inputs": ["high", "low", "close"], "func": f16_dbkb_148_indicator_compound_break_failure_walking_squeeze},
    "f16_dbkb_149_ratio_walking_upper_to_walking_lower_63d": {"inputs": ["close"], "func": f16_dbkb_149_ratio_walking_upper_to_walking_lower_63d},
    "f16_dbkb_150_cum_extension_above_bollinger_upper_atr_252d": {"inputs": ["high", "low", "close"], "func": f16_dbkb_150_cum_extension_above_bollinger_upper_atr_252d},
}
