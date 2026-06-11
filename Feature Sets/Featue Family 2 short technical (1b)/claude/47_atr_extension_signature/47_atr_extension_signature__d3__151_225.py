"""atr_extension_signature d3 features 151-225 — Pipeline 1b-technical.

Continuation gap-fill: covers reference-types that were missing from 001-150 —
Bollinger / Keltner / Donchian channels, alternative MAs (HMA / TEMA / KAMA /
WMA / VWMA / ZLEMA), typical/median/weighted-close references, linear-regression
residual & channel, cumulative-extreme anchors, advanced wick/shadow geometry,
and multi-bar (5/10) lookback extensions.

Bucket S: Bollinger-band extension (151-160).
Bucket T: Keltner-channel extension (161-167).
Bucket U: Donchian-channel extension (168-174).
Bucket V: Alternative-MA extension (175-186).
Bucket W: Typical / median / weighted-close extension (187-194).
Bucket X: Linear-regression channel & residual (195-202).
Bucket Y: Cumulative max / min extension (203-209).
Bucket Z: Wick / shadow advanced geometry (210-217).
Bucket AA: Multi-bar high / low extension (218-225).

Inputs: SEP OHLCV. Self-contained helpers; PIT-clean.
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


def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _wma(s, n):
    def _f(w):
        nw = len(w)
        valid = ~np.isnan(w)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        x = w.copy()
        x[~valid] = 0.0
        wv = np.arange(1, nw + 1, dtype=float)
        wv[~valid] = 0.0
        ws = wv.sum()
        return (x * wv).sum() / ws if ws != 0 else np.nan
    return s.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


def _hma(s, n):
    half = max(n // 2, 1)
    wma_half = _wma(s, half)
    wma_full = _wma(s, n)
    raw = 2.0 * wma_half - wma_full
    return _wma(raw, max(int(np.sqrt(n)), 2))


def _tema(s, n):
    e1 = _ema(s, n)
    e2 = _ema(e1, n)
    e3 = _ema(e2, n)
    return 3.0 * e1 - 3.0 * e2 + e3


def _kama(s, n=10, fast=2, slow=30):
    """Kaufman Adaptive MA — efficiency-ratio-weighted EMA."""
    change = (s - s.shift(n)).abs()
    volatility = s.diff().abs().rolling(n, min_periods=max(n // 3, 2)).sum()
    er = _safe_div(change, volatility).fillna(0.0)
    fast_sc = 2.0 / (fast + 1.0)
    slow_sc = 2.0 / (slow + 1.0)
    sc = (er * (fast_sc - slow_sc) + slow_sc) ** 2
    arr = s.to_numpy(dtype=float)
    sc_arr = sc.to_numpy(dtype=float)
    out = np.full(arr.shape, np.nan)
    if arr.size > n:
        # initialize at index n with raw value
        if not np.isnan(arr[n]):
            out[n] = arr[n]
        for i in range(n + 1, arr.size):
            if np.isnan(out[i - 1]):
                if not np.isnan(arr[i]):
                    out[i] = arr[i]
            else:
                if np.isnan(arr[i]) or np.isnan(sc_arr[i]):
                    out[i] = out[i - 1]
                else:
                    out[i] = out[i - 1] + sc_arr[i] * (arr[i] - out[i - 1])
    return pd.Series(out, index=s.index)


def _zlema(s, n):
    """Zero-lag EMA: EMA of (close + (close - close[n/2-1]))."""
    lag = max((n - 1) // 2, 1)
    return _ema(s + (s - s.shift(lag)), n)


def _vwma(price, volume, n):
    num = (price * volume).rolling(n, min_periods=max(n // 3, 2)).sum()
    den = volume.rolling(n, min_periods=max(n // 3, 2)).sum()
    return _safe_div(num, den)


def _lr_endpoint(s, n):
    """Endpoint value of a linear regression line over window n (the LR value at the most recent bar)."""
    sl = _rolling_slope(s, n)
    m = s.rolling(n, min_periods=max(n // 3, 2)).mean()
    return m + sl * (n - 1) / 2.0


def _lr_residual_std(s, n):
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < max(n // 3, 4):
            return np.nan
        x = np.arange(len(w), dtype=float)
        if not valid.all():
            x = x[valid]; w = w[valid]
        xm = x.mean(); wm = w.mean()
        sx2 = ((x - xm) ** 2).sum()
        if sx2 == 0:
            return np.nan
        slope = ((x - xm) * (w - wm)).sum() / sx2
        intercept = wm - slope * xm
        yhat = slope * x + intercept
        resid = w - yhat
        return float(np.std(resid, ddof=1)) if resid.size > 1 else np.nan
    return s.rolling(n, min_periods=max(n // 3, 4)).apply(_f, raw=True)


def _lr_r_squared(s, n):
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < max(n // 3, 4):
            return np.nan
        x = np.arange(len(w), dtype=float)
        if not valid.all():
            x = x[valid]; w = w[valid]
        xm = x.mean(); wm = w.mean()
        sx2 = ((x - xm) ** 2).sum()
        sy2 = ((w - wm) ** 2).sum()
        if sx2 == 0 or sy2 == 0:
            return np.nan
        slope = ((x - xm) * (w - wm)).sum() / sx2
        ss_res = (w - (slope * x + wm - slope * xm)) ** 2
        return float(1.0 - ss_res.sum() / sy2)
    return s.rolling(n, min_periods=max(n // 3, 4)).apply(_f, raw=True)


# ============================================================
# Bucket S — Bollinger-band extension (151-160)
# ============================================================


def f47_atxs_151_close_minus_bb_upper_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - BB(20,2)-upper) / ATR21 — extension above upper Bollinger band in ATR units."""
    m = close.rolling(20, min_periods=10).mean()
    sd = close.rolling(20, min_periods=10).std()
    return (_safe_div(close - (m + 2.0 * sd), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_152_close_minus_bb_mid_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - BB(20)-mid) / ATR21 — extension above BB centerline (SMA20) in ATR units."""
    m = close.rolling(20, min_periods=10).mean()
    return (_safe_div(close - m, _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_153_close_minus_bb_lower_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - BB(20,2)-lower) / ATR21 — extension above lower Bollinger band."""
    m = close.rolling(20, min_periods=10).mean()
    sd = close.rolling(20, min_periods=10).std()
    return (_safe_div(close - (m - 2.0 * sd), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_154_bollinger_pct_b_d3(close: pd.Series) -> pd.Series:
    """%B = (close - BB-lower)/(BB-upper - BB-lower) — position in band (0=lower, 1=upper, >1=above)."""
    m = close.rolling(20, min_periods=10).mean()
    sd = close.rolling(20, min_periods=10).std()
    upper = m + 2.0 * sd
    lower = m - 2.0 * sd
    return (_safe_div(close - lower, upper - lower)).diff().diff().diff()


def f47_atxs_155_close_above_bb_upper_state_d3(close: pd.Series) -> pd.Series:
    """1 if close > BB(20,2) upper — outside-upper-band state."""
    m = close.rolling(20, min_periods=10).mean()
    sd = close.rolling(20, min_periods=10).std()
    return ((close > (m + 2.0 * sd)).astype(float).where(sd.notna(), np.nan)).diff().diff().diff()


def f47_atxs_156_bb_walk_above_upper_streak_d3(close: pd.Series) -> pd.Series:
    """Current consecutive run of close > BB-upper — Bollinger-walk streak length."""
    m = close.rolling(20, min_periods=10).mean()
    sd = close.rolling(20, min_periods=10).std()
    return (_streak_true(close > (m + 2.0 * sd)).where(sd.notna(), np.nan)).diff().diff().diff()


def f47_atxs_157_bb_bandwidth_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bollinger bandwidth (upper - lower) / ATR21 — band-width in ATR units."""
    sd = close.rolling(20, min_periods=10).std()
    return (_safe_div(4.0 * sd, _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_158_bb_squeeze_state_10th_pct_d3(close: pd.Series) -> pd.Series:
    """1 if BB bandwidth is in lowest 10% of trailing 252d — squeeze regime indicator."""
    sd = close.rolling(20, min_periods=10).std()
    bw = sd * 4.0
    q10 = bw.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    return ((bw <= q10).astype(float).where(q10.notna(), np.nan)).diff().diff().diff()


def f47_atxs_159_high_minus_bb_upper_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(high - BB-upper) / ATR21 — intra-bar overshoot of upper band in ATR units."""
    m = close.rolling(20, min_periods=10).mean()
    sd = close.rolling(20, min_periods=10).std()
    return (_safe_div(high - (m + 2.0 * sd), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_160_bb_walk_above_upper_count_21_d3(close: pd.Series) -> pd.Series:
    """Count of past 21 bars with close > BB upper — recent walking-the-band intensity."""
    m = close.rolling(20, min_periods=10).mean()
    sd = close.rolling(20, min_periods=10).std()
    flag = (close > (m + 2.0 * sd)).astype(float)
    return (flag.rolling(MDAYS, min_periods=WDAYS).sum().where(sd.notna(), np.nan)).diff().diff().diff()


def f47_atxs_161_close_minus_keltner_upper_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - Keltner-upper) / ATR21 — Keltner = EMA20 ± 2*ATR(20); extension above upper."""
    e = _ema(close, 20)
    a = _atr(high, low, close, 20)
    return (_safe_div(close - (e + 2.0 * a), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_162_close_minus_keltner_mid_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - Keltner-mid) / ATR21 — extension above EMA20 in ATR21 units."""
    e = _ema(close, 20)
    return (_safe_div(close - e, _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_163_keltner_position_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - Keltner-lower)/(Keltner-upper - Keltner-lower) — position in channel."""
    e = _ema(close, 20)
    a = _atr(high, low, close, 20)
    upper = e + 2.0 * a
    lower = e - 2.0 * a
    return (_safe_div(close - lower, upper - lower)).diff().diff().diff()


def f47_atxs_164_close_above_keltner_upper_state_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close > Keltner upper — outside-channel state."""
    e = _ema(close, 20)
    a = _atr(high, low, close, 20)
    return ((close > (e + 2.0 * a)).astype(float).where(a.notna(), np.nan)).diff().diff().diff()


def f47_atxs_165_bars_since_keltner_upper_exit_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since close last crossed back inside Keltner upper (from above)."""
    e = _ema(close, 20)
    a = _atr(high, low, close, 20)
    upper = e + 2.0 * a
    ev = (close.shift(1) > upper.shift(1)) & (close <= upper)
    return (_bars_since_true(ev)).diff().diff().diff()


def f47_atxs_166_keltner_over_bb_bandwidth_ratio_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Keltner-bandwidth / Bollinger-bandwidth — when <1, BB is wider (TTM-squeeze release zone)."""
    a = _atr(high, low, close, 20)
    sd = close.rolling(20, min_periods=10).std()
    return (_safe_div(4.0 * a, 4.0 * sd)).diff().diff().diff()


def f47_atxs_167_ttm_squeeze_state_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if BB inside Keltner (BB-upper < Keltner-upper AND BB-lower > Keltner-lower) — TTM squeeze."""
    m = close.rolling(20, min_periods=10).mean()
    sd = close.rolling(20, min_periods=10).std()
    e = _ema(close, 20)
    a = _atr(high, low, close, 20)
    bb_u = m + 2.0 * sd; bb_l = m - 2.0 * sd
    k_u = e + 2.0 * a; k_l = e - 2.0 * a
    return (((bb_u < k_u) & (bb_l > k_l)).astype(float).where(sd.notna() & a.notna(), np.nan)).diff().diff().diff()


def f47_atxs_168_close_minus_donchian20_upper_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 20d-high) / ATR21 — Donchian-20 upper-band extension (alt of f47_atxs_027 horizon=21)."""
    return (_safe_div(close - high.rolling(20, min_periods=10).max(), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_169_donchian20_position_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 20d-low)/(20d-high - 20d-low) — position in Donchian-20 channel."""
    hh = high.rolling(20, min_periods=10).max()
    ll = low.rolling(20, min_periods=10).min()
    return (_safe_div(close - ll, hh - ll)).diff().diff().diff()


def f47_atxs_170_donchian20_width_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Donchian-20 width (20d-high - 20d-low) / ATR21 — channel width in ATR units."""
    hh = high.rolling(20, min_periods=10).max()
    ll = low.rolling(20, min_periods=10).min()
    return (_safe_div(hh - ll, _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_171_close_minus_donchian55_upper_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 55d-high) / ATR21 — Donchian-55 upper extension (Turtle-trader system level)."""
    return (_safe_div(close - high.rolling(55, min_periods=20).max(), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_172_donchian55_width_over_atr252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Donchian-55 width / ATR252 — long-channel width in annual ATR."""
    hh = high.rolling(55, min_periods=20).max()
    ll = low.rolling(55, min_periods=20).min()
    return (_safe_div(hh - ll, _atr(high, low, close, YDAYS))).diff().diff().diff()


def f47_atxs_173_donchian20_55_upper_diff_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(20d-high - 55d-high) / ATR21 — recent-vs-medium high stack in ATR units."""
    return (_safe_div(high.rolling(20, min_periods=10).max() - high.rolling(55, min_periods=20).max(), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_174_bars_since_donchian20_upper_touch_d3(high: pd.Series) -> pd.Series:
    """Bars since high last touched its 20d max (Donchian-20 upper)."""
    return (_bars_since_true(high == high.rolling(20, min_periods=10).max())).diff().diff().diff()


def f47_atxs_175_close_minus_hma21_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - HMA(21)) / ATR21 — Hull MA extension (low-lag smoothed)."""
    return (_safe_div(close - _hma(close, MDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_176_close_minus_hma63_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - HMA(63)) / ATR21 — quarterly Hull MA extension."""
    return (_safe_div(close - _hma(close, QDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_177_close_minus_tema21_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - TEMA(21)) / ATR21 — Triple-EMA extension (zero-lag-style)."""
    return (_safe_div(close - _tema(close, MDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_178_close_minus_tema63_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - TEMA(63)) / ATR21 — quarterly TEMA extension."""
    return (_safe_div(close - _tema(close, QDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_179_close_minus_kama21_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - KAMA(21)) / ATR21 — Kaufman Adaptive MA extension."""
    return (_safe_div(close - _kama(close, n=MDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_180_close_minus_kama63_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - KAMA(63)) / ATR21 — quarterly KAMA extension."""
    return (_safe_div(close - _kama(close, n=QDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_181_close_minus_triangular_ma21_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - Triangular-MA(21)) / ATR21 — TMA = SMA-of-SMA."""
    inner = max(MDAYS // 2 + 1, 2)
    tma = close.rolling(inner, min_periods=max(inner // 3, 2)).mean().rolling(inner, min_periods=max(inner // 3, 2)).mean()
    return (_safe_div(close - tma, _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_182_close_minus_wma21_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - WMA(21)) / ATR21 — weighted MA extension."""
    return (_safe_div(close - _wma(close, MDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_183_close_minus_wma63_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - WMA(63)) / ATR21 — quarterly WMA extension."""
    return (_safe_div(close - _wma(close, QDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_184_close_minus_vwma21_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - VWMA(21)) / ATR21 — vol-weighted MA extension (monthly)."""
    return (_safe_div(close - _vwma(close, volume, MDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_185_close_minus_vwma63_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - VWMA(63)) / ATR21 — quarterly VWMA extension."""
    return (_safe_div(close - _vwma(close, volume, QDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_186_close_minus_zlema21_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - ZLEMA(21)) / ATR21 — zero-lag EMA extension."""
    return (_safe_div(close - _zlema(close, MDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_187_typical_minus_sma21_typical_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(typical - SMA21(typical)) / ATR21 where typical = HLC/3."""
    tp = (high + low + close) / 3.0
    return (_safe_div(tp - _sma(tp, MDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_188_median_minus_sma21_median_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(median - SMA21(median)) / ATR21 where median = (H+L)/2."""
    med = (high + low) / 2.0
    return (_safe_div(med - _sma(med, MDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_189_wclose_minus_sma21_wclose_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(weighted-close - SMA21(wclose)) / ATR21 where wclose = (H+L+2C)/4."""
    wc = (high + low + 2.0 * close) / 4.0
    return (_safe_div(wc - _sma(wc, MDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_190_median_minus_sma21_close_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(median(HL) - SMA21(close)) / ATR21 — intra-bar midpoint vs MA21 of close (gap-from-MA)."""
    med = (high + low) / 2.0
    return (_safe_div(med - _sma(close, MDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_191_typical_minus_sma63_typical_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(typical - SMA63(typical)) / ATR21 — quarterly typical-price extension."""
    tp = (high + low + close) / 3.0
    return (_safe_div(tp - _sma(tp, QDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_192_typical_minus_sma252_typical_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(typical - SMA252(typical)) / ATR21 — annual typical-price extension."""
    tp = (high + low + close) / 3.0
    return (_safe_div(tp - _sma(tp, YDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_193_typical_ext_minus_close_ext_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(typical-SMA21(typical))/ATR21 - (close-SMA21(close))/ATR21 — gap between typical-ext and close-ext."""
    a = _atr(high, low, close, MDAYS)
    tp = (high + low + close) / 3.0
    return (_safe_div(tp - _sma(tp, MDAYS), a) - _safe_div(close - _sma(close, MDAYS), a)).diff().diff().diff()


def f47_atxs_194_avgclose_minus_sma21_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """((H+C)/2 - SMA21(close)) / ATR21 — average-of-high-and-close vs MA in ATR units."""
    return (_safe_div((high + close) / 2.0 - _sma(close, MDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_195_close_minus_lr21_endpoint_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - LR21 endpoint) / ATR21 — residual from 21d regression in ATR units."""
    return (_safe_div(close - _lr_endpoint(close, MDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_196_close_minus_lr63_endpoint_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - LR63 endpoint) / ATR21 — quarterly LR residual."""
    return (_safe_div(close - _lr_endpoint(close, QDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_197_close_minus_lr252_endpoint_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - LR252 endpoint) / ATR21 — annual LR residual."""
    return (_safe_div(close - _lr_endpoint(close, YDAYS), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_198_lr21_upper_band_minus_close_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(LR21-endpoint + 2*resid-std - close) / ATR21 — gap below 21d LR upper-band in ATR units."""
    endpoint = _lr_endpoint(close, MDAYS)
    rstd = _lr_residual_std(close, MDAYS)
    return (_safe_div(endpoint + 2.0 * rstd - close, _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_199_close_minus_lr21_lower_band_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - (LR21-endpoint - 2*resid-std)) / ATR21 — extension above 21d LR lower-band."""
    endpoint = _lr_endpoint(close, MDAYS)
    rstd = _lr_residual_std(close, MDAYS)
    return (_safe_div(close - (endpoint - 2.0 * rstd), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_200_lr21_r_squared_d3(close: pd.Series) -> pd.Series:
    """R-squared of 21d linear regression — trend quality (1 = perfect linear trend)."""
    return (_lr_r_squared(close, MDAYS)).diff().diff().diff()


def f47_atxs_201_lr_residual_zscore_63_d3(close: pd.Series) -> pd.Series:
    """Z-score (63d) of residual (close - LR21 endpoint) — recent residual vs own short-term distribution."""
    return (_rolling_zscore(close - _lr_endpoint(close, MDAYS), QDAYS, min_periods=MDAYS)).diff().diff().diff()


def f47_atxs_202_lr21_band_position_d3(close: pd.Series) -> pd.Series:
    """(close - (LR-endpoint - 2*rstd)) / (4*rstd) — position within 21d LR ±2 band (0..1 inside)."""
    endpoint = _lr_endpoint(close, MDAYS)
    rstd = _lr_residual_std(close, MDAYS)
    return (_safe_div(close - (endpoint - 2.0 * rstd), 4.0 * rstd)).diff().diff().diff()


def f47_atxs_203_close_minus_cummax_high_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - all-time high) / ATR21 — distance below ATH in ATR units (<=0)."""
    return (_safe_div(close - high.cummax(), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_204_close_minus_cummax_high_over_atr252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - all-time high) / ATR252 — annual-ATR drawdown depth."""
    return (_safe_div(close - high.cummax(), _atr(high, low, close, YDAYS))).diff().diff().diff()


def f47_atxs_205_close_minus_cummax_close_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - all-time close-max) / ATR21 — close-based drawdown depth in ATR21."""
    return (_safe_div(close - close.cummax(), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_206_close_minus_504d_cummax_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 504d high) / ATR21 — 2-year peak distance."""
    return (_safe_div(close - high.rolling(DDAYS_2Y, min_periods=YDAYS).max(), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_207_close_minus_1260d_cummax_over_atr252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 1260d high) / ATR252 — 5-year peak distance."""
    return (_safe_div(close - high.rolling(DDAYS_5Y, min_periods=YDAYS).max(), _atr(high, low, close, YDAYS))).diff().diff().diff()


def f47_atxs_208_bars_since_cummax_high_d3(high: pd.Series) -> pd.Series:
    """Bars since high equals its cumulative-max (last all-time-high event)."""
    return (_bars_since_true(high == high.cummax())).diff().diff().diff()


def f47_atxs_209_504d_channel_position_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 504d-low)/(504d-high - 504d-low) — position in 2-year HL channel."""
    hh = high.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    ll = low.rolling(DDAYS_2Y, min_periods=YDAYS).min()
    return (_safe_div(close - ll, hh - ll)).diff().diff().diff()


def f47_atxs_210_upper_wick_signed_over_atr21_d3(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(high - max(close, open)) / ATR21 — upper-wick length in ATR units (non-negative)."""
    return (_safe_div(high - pd.concat([close, open_], axis=1).max(axis=1), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_211_lower_wick_over_atr21_d3(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(min(close, open) - low) / ATR21 — lower-wick length in ATR units."""
    return (_safe_div(pd.concat([close, open_], axis=1).min(axis=1) - low, _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_212_upper_wick_over_body_ratio_d3(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Upper-wick / |body| — upper rejection magnitude vs body (high values = rejection)."""
    body = (close - open_).abs().replace(0, np.nan)
    return (_safe_div(high - pd.concat([close, open_], axis=1).max(axis=1), body)).diff().diff().diff()


def f47_atxs_213_lower_wick_over_body_ratio_d3(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lower-wick / |body|."""
    body = (close - open_).abs().replace(0, np.nan)
    return (_safe_div(pd.concat([close, open_], axis=1).min(axis=1) - low, body)).diff().diff().diff()


def f47_atxs_214_body_over_true_range_d3(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """|close - open| / true-range — body fraction of full true range."""
    return (_safe_div((close - open_).abs(), _true_range(high, low, close))).diff().diff().diff()


def f47_atxs_215_close_minus_hl_mid_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - (H+L)/2) / ATR21 — close-vs-midpoint signed gap in ATR units."""
    return (_safe_div(close - (high + low) / 2.0, _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_216_close_position_in_hl_range_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - low)/(high - low) — close position in bar range (single-bar CLV-variant)."""
    return (_safe_div(close - low, high - low)).diff().diff().diff()


def f47_atxs_217_avg_close_position_past_21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean past 21 of (close - low)/(high - low) — average close-position-in-range monthly."""
    pos = _safe_div(close - low, high - low)
    return (pos.rolling(MDAYS, min_periods=WDAYS).mean().where(pos.notna(), np.nan)).diff().diff().diff()


def f47_atxs_218_close_minus_5d_high_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 5d high) / ATR21 — 5-bar peak distance in ATR21."""
    return (_safe_div(close - high.rolling(WDAYS, min_periods=2).max(), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_219_close_minus_10d_high_over_atr21_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 10d high) / ATR21 — 10-bar peak distance."""
    return (_safe_div(close - high.rolling(10, min_periods=3).max(), _atr(high, low, close, MDAYS))).diff().diff().diff()


def f47_atxs_220_close_minus_5d_high_over_atr5_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 5d high) / ATR5 — short-horizon peak-distance, short ATR."""
    return (_safe_div(close - high.rolling(WDAYS, min_periods=2).max(), _atr(high, low, close, WDAYS))).diff().diff().diff()


def f47_atxs_221_close_position_21bar_range_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 21d low)/(21d high - 21d low) — 21-bar channel position (distinct from CLV)."""
    return (_safe_div(close - low.rolling(MDAYS, min_periods=WDAYS).min(),

                     high.rolling(MDAYS, min_periods=WDAYS).max() - low.rolling(MDAYS, min_periods=WDAYS).min())).diff().diff().diff()


def f47_atxs_222_close_position_63bar_range_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-bar channel position."""
    return (_safe_div(close - low.rolling(QDAYS, min_periods=MDAYS).min(),

                     high.rolling(QDAYS, min_periods=MDAYS).max() - low.rolling(QDAYS, min_periods=MDAYS).min())).diff().diff().diff()


def f47_atxs_223_close_position_252bar_range_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-bar channel position."""
    return (_safe_div(close - low.rolling(YDAYS, min_periods=QDAYS).min(),

                     high.rolling(YDAYS, min_periods=QDAYS).max() - low.rolling(YDAYS, min_periods=QDAYS).min())).diff().diff().diff()


def f47_atxs_224_close_position_504bar_range_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """504-bar channel position (multi-year)."""
    return (_safe_div(close - low.rolling(DDAYS_2Y, min_periods=YDAYS).min(),

                     high.rolling(DDAYS_2Y, min_periods=YDAYS).max() - low.rolling(DDAYS_2Y, min_periods=YDAYS).min())).diff().diff().diff()


def f47_atxs_225_close_position_252bar_range_zscore_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 252-bar channel position vs trailing 252d distribution — channel-rank percentile."""
    pos = _safe_div(close - low.rolling(YDAYS, min_periods=QDAYS).min(),
                    high.rolling(YDAYS, min_periods=QDAYS).max() - low.rolling(YDAYS, min_periods=QDAYS).min())
    return (_rolling_zscore(pos, YDAYS, min_periods=QDAYS)).diff().diff().diff()


# ============================================================
#                         REGISTRY 151-225 (d3)
# ============================================================

_HLC = ["high", "low", "close"]
_HLCV = ["high", "low", "close", "volume"]
_OHLC = ["open", "high", "low", "close"]

ATR_EXTENSION_SIGNATURE_D3_REGISTRY_151_225 = {
    "f47_atxs_151_close_minus_bb_upper_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_151_close_minus_bb_upper_over_atr21_d3},
    "f47_atxs_152_close_minus_bb_mid_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_152_close_minus_bb_mid_over_atr21_d3},
    "f47_atxs_153_close_minus_bb_lower_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_153_close_minus_bb_lower_over_atr21_d3},
    "f47_atxs_154_bollinger_pct_b_d3": {"inputs": ["close"], "func": f47_atxs_154_bollinger_pct_b_d3},
    "f47_atxs_155_close_above_bb_upper_state_d3": {"inputs": ["close"], "func": f47_atxs_155_close_above_bb_upper_state_d3},
    "f47_atxs_156_bb_walk_above_upper_streak_d3": {"inputs": ["close"], "func": f47_atxs_156_bb_walk_above_upper_streak_d3},
    "f47_atxs_157_bb_bandwidth_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_157_bb_bandwidth_over_atr21_d3},
    "f47_atxs_158_bb_squeeze_state_10th_pct_d3": {"inputs": ["close"], "func": f47_atxs_158_bb_squeeze_state_10th_pct_d3},
    "f47_atxs_159_high_minus_bb_upper_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_159_high_minus_bb_upper_over_atr21_d3},
    "f47_atxs_160_bb_walk_above_upper_count_21_d3": {"inputs": ["close"], "func": f47_atxs_160_bb_walk_above_upper_count_21_d3},
    "f47_atxs_161_close_minus_keltner_upper_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_161_close_minus_keltner_upper_over_atr21_d3},
    "f47_atxs_162_close_minus_keltner_mid_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_162_close_minus_keltner_mid_over_atr21_d3},
    "f47_atxs_163_keltner_position_d3": {"inputs": _HLC, "func": f47_atxs_163_keltner_position_d3},
    "f47_atxs_164_close_above_keltner_upper_state_d3": {"inputs": _HLC, "func": f47_atxs_164_close_above_keltner_upper_state_d3},
    "f47_atxs_165_bars_since_keltner_upper_exit_d3": {"inputs": _HLC, "func": f47_atxs_165_bars_since_keltner_upper_exit_d3},
    "f47_atxs_166_keltner_over_bb_bandwidth_ratio_d3": {"inputs": _HLC, "func": f47_atxs_166_keltner_over_bb_bandwidth_ratio_d3},
    "f47_atxs_167_ttm_squeeze_state_d3": {"inputs": _HLC, "func": f47_atxs_167_ttm_squeeze_state_d3},
    "f47_atxs_168_close_minus_donchian20_upper_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_168_close_minus_donchian20_upper_over_atr21_d3},
    "f47_atxs_169_donchian20_position_d3": {"inputs": _HLC, "func": f47_atxs_169_donchian20_position_d3},
    "f47_atxs_170_donchian20_width_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_170_donchian20_width_over_atr21_d3},
    "f47_atxs_171_close_minus_donchian55_upper_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_171_close_minus_donchian55_upper_over_atr21_d3},
    "f47_atxs_172_donchian55_width_over_atr252_d3": {"inputs": _HLC, "func": f47_atxs_172_donchian55_width_over_atr252_d3},
    "f47_atxs_173_donchian20_55_upper_diff_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_173_donchian20_55_upper_diff_over_atr21_d3},
    "f47_atxs_174_bars_since_donchian20_upper_touch_d3": {"inputs": ["high"], "func": f47_atxs_174_bars_since_donchian20_upper_touch_d3},
    "f47_atxs_175_close_minus_hma21_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_175_close_minus_hma21_over_atr21_d3},
    "f47_atxs_176_close_minus_hma63_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_176_close_minus_hma63_over_atr21_d3},
    "f47_atxs_177_close_minus_tema21_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_177_close_minus_tema21_over_atr21_d3},
    "f47_atxs_178_close_minus_tema63_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_178_close_minus_tema63_over_atr21_d3},
    "f47_atxs_179_close_minus_kama21_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_179_close_minus_kama21_over_atr21_d3},
    "f47_atxs_180_close_minus_kama63_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_180_close_minus_kama63_over_atr21_d3},
    "f47_atxs_181_close_minus_triangular_ma21_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_181_close_minus_triangular_ma21_over_atr21_d3},
    "f47_atxs_182_close_minus_wma21_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_182_close_minus_wma21_over_atr21_d3},
    "f47_atxs_183_close_minus_wma63_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_183_close_minus_wma63_over_atr21_d3},
    "f47_atxs_184_close_minus_vwma21_over_atr21_d3": {"inputs": _HLCV, "func": f47_atxs_184_close_minus_vwma21_over_atr21_d3},
    "f47_atxs_185_close_minus_vwma63_over_atr21_d3": {"inputs": _HLCV, "func": f47_atxs_185_close_minus_vwma63_over_atr21_d3},
    "f47_atxs_186_close_minus_zlema21_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_186_close_minus_zlema21_over_atr21_d3},
    "f47_atxs_187_typical_minus_sma21_typical_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_187_typical_minus_sma21_typical_over_atr21_d3},
    "f47_atxs_188_median_minus_sma21_median_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_188_median_minus_sma21_median_over_atr21_d3},
    "f47_atxs_189_wclose_minus_sma21_wclose_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_189_wclose_minus_sma21_wclose_over_atr21_d3},
    "f47_atxs_190_median_minus_sma21_close_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_190_median_minus_sma21_close_over_atr21_d3},
    "f47_atxs_191_typical_minus_sma63_typical_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_191_typical_minus_sma63_typical_over_atr21_d3},
    "f47_atxs_192_typical_minus_sma252_typical_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_192_typical_minus_sma252_typical_over_atr21_d3},
    "f47_atxs_193_typical_ext_minus_close_ext_d3": {"inputs": _HLC, "func": f47_atxs_193_typical_ext_minus_close_ext_d3},
    "f47_atxs_194_avgclose_minus_sma21_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_194_avgclose_minus_sma21_over_atr21_d3},
    "f47_atxs_195_close_minus_lr21_endpoint_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_195_close_minus_lr21_endpoint_over_atr21_d3},
    "f47_atxs_196_close_minus_lr63_endpoint_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_196_close_minus_lr63_endpoint_over_atr21_d3},
    "f47_atxs_197_close_minus_lr252_endpoint_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_197_close_minus_lr252_endpoint_over_atr21_d3},
    "f47_atxs_198_lr21_upper_band_minus_close_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_198_lr21_upper_band_minus_close_over_atr21_d3},
    "f47_atxs_199_close_minus_lr21_lower_band_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_199_close_minus_lr21_lower_band_over_atr21_d3},
    "f47_atxs_200_lr21_r_squared_d3": {"inputs": ["close"], "func": f47_atxs_200_lr21_r_squared_d3},
    "f47_atxs_201_lr_residual_zscore_63_d3": {"inputs": ["close"], "func": f47_atxs_201_lr_residual_zscore_63_d3},
    "f47_atxs_202_lr21_band_position_d3": {"inputs": ["close"], "func": f47_atxs_202_lr21_band_position_d3},
    "f47_atxs_203_close_minus_cummax_high_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_203_close_minus_cummax_high_over_atr21_d3},
    "f47_atxs_204_close_minus_cummax_high_over_atr252_d3": {"inputs": _HLC, "func": f47_atxs_204_close_minus_cummax_high_over_atr252_d3},
    "f47_atxs_205_close_minus_cummax_close_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_205_close_minus_cummax_close_over_atr21_d3},
    "f47_atxs_206_close_minus_504d_cummax_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_206_close_minus_504d_cummax_over_atr21_d3},
    "f47_atxs_207_close_minus_1260d_cummax_over_atr252_d3": {"inputs": _HLC, "func": f47_atxs_207_close_minus_1260d_cummax_over_atr252_d3},
    "f47_atxs_208_bars_since_cummax_high_d3": {"inputs": ["high"], "func": f47_atxs_208_bars_since_cummax_high_d3},
    "f47_atxs_209_504d_channel_position_d3": {"inputs": _HLC, "func": f47_atxs_209_504d_channel_position_d3},
    "f47_atxs_210_upper_wick_signed_over_atr21_d3": {"inputs": _OHLC, "func": f47_atxs_210_upper_wick_signed_over_atr21_d3},
    "f47_atxs_211_lower_wick_over_atr21_d3": {"inputs": _OHLC, "func": f47_atxs_211_lower_wick_over_atr21_d3},
    "f47_atxs_212_upper_wick_over_body_ratio_d3": {"inputs": _OHLC, "func": f47_atxs_212_upper_wick_over_body_ratio_d3},
    "f47_atxs_213_lower_wick_over_body_ratio_d3": {"inputs": _OHLC, "func": f47_atxs_213_lower_wick_over_body_ratio_d3},
    "f47_atxs_214_body_over_true_range_d3": {"inputs": _OHLC, "func": f47_atxs_214_body_over_true_range_d3},
    "f47_atxs_215_close_minus_hl_mid_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_215_close_minus_hl_mid_over_atr21_d3},
    "f47_atxs_216_close_position_in_hl_range_d3": {"inputs": _HLC, "func": f47_atxs_216_close_position_in_hl_range_d3},
    "f47_atxs_217_avg_close_position_past_21_d3": {"inputs": _HLC, "func": f47_atxs_217_avg_close_position_past_21_d3},
    "f47_atxs_218_close_minus_5d_high_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_218_close_minus_5d_high_over_atr21_d3},
    "f47_atxs_219_close_minus_10d_high_over_atr21_d3": {"inputs": _HLC, "func": f47_atxs_219_close_minus_10d_high_over_atr21_d3},
    "f47_atxs_220_close_minus_5d_high_over_atr5_d3": {"inputs": _HLC, "func": f47_atxs_220_close_minus_5d_high_over_atr5_d3},
    "f47_atxs_221_close_position_21bar_range_d3": {"inputs": _HLC, "func": f47_atxs_221_close_position_21bar_range_d3},
    "f47_atxs_222_close_position_63bar_range_d3": {"inputs": _HLC, "func": f47_atxs_222_close_position_63bar_range_d3},
    "f47_atxs_223_close_position_252bar_range_d3": {"inputs": _HLC, "func": f47_atxs_223_close_position_252bar_range_d3},
    "f47_atxs_224_close_position_504bar_range_d3": {"inputs": _HLC, "func": f47_atxs_224_close_position_504bar_range_d3},
    "f47_atxs_225_close_position_252bar_range_zscore_252_d3": {"inputs": _HLC, "func": f47_atxs_225_close_position_252bar_range_zscore_252_d3},
}
