"""atr_extension_signature d1 features 226-300 — Pipeline 1b-technical.

Second gap-fill batch. Covers Heikin-Ashi, chandelier/PSAR-style trailing
references, advanced VWAP variants, Bollinger %B & walk dynamics, channel /
Aroon percent indicators, multi-MA composite extension, time-since-event,
conditional regime ratios, breakout-amplitude / failed-breakout extensions,
and pure structural channel-position (no ATR).

Bucket BB: Heikin-Ashi extensions (226-232).
Bucket CC: Volatility-stop / chandelier-style (233-239).
Bucket DD: VWMA / advanced VWAP (240-247).
Bucket EE: Bollinger advanced (248-255).
Bucket FF: Channel / percent indicators (256-262).
Bucket GG: Composite multi-MA extension (263-270).
Bucket HH: Time-since composites (271-278).
Bucket II: Conditional ratios / regimes (279-286).
Bucket JJ: Anchored & breakout extensions (287-294).
Bucket KK: Pure structural channel position (295-300).

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


def _heikin_ashi(open_, high, low, close):
    """Heikin-Ashi (HA) candles. Returns dict of ha_open, ha_close, ha_high, ha_low."""
    ha_close = (open_ + high + low + close) / 4.0
    arr_o = open_.to_numpy(dtype=float)
    arr_c = close.to_numpy(dtype=float)
    ha_c_arr = ha_close.to_numpy(dtype=float)
    ha_o = np.full(arr_o.shape, np.nan)
    if arr_o.size > 0:
        ha_o[0] = (arr_o[0] + arr_c[0]) / 2.0 if not (np.isnan(arr_o[0]) or np.isnan(arr_c[0])) else np.nan
        for i in range(1, arr_o.size):
            prev_ha_o = ha_o[i - 1]
            prev_ha_c = ha_c_arr[i - 1]
            if np.isnan(prev_ha_o) or np.isnan(prev_ha_c):
                ha_o[i] = (arr_o[i] + arr_c[i]) / 2.0 if not (np.isnan(arr_o[i]) or np.isnan(arr_c[i])) else np.nan
            else:
                ha_o[i] = (prev_ha_o + prev_ha_c) / 2.0
    ha_open = pd.Series(ha_o, index=open_.index)
    ha_high = pd.concat([high, ha_open, ha_close], axis=1).max(axis=1)
    ha_low = pd.concat([low, ha_open, ha_close], axis=1).min(axis=1)
    return {"open": ha_open, "high": ha_high, "low": ha_low, "close": ha_close}


def _chandelier_long(high, low, close, n=22, k=3.0):
    """Chandelier long exit: highest-n high - k * ATR(n)."""
    return high.rolling(n, min_periods=max(n // 3, 2)).max() - k * _atr(high, low, close, n)


def _chandelier_short(high, low, close, n=22, k=3.0):
    """Chandelier short exit: lowest-n low + k * ATR(n)."""
    return low.rolling(n, min_periods=max(n // 3, 2)).min() + k * _atr(high, low, close, n)


def _vwma(price, volume, n):
    num = (price * volume).rolling(n, min_periods=max(n // 3, 2)).sum()
    den = volume.rolling(n, min_periods=max(n // 3, 2)).sum()
    return _safe_div(num, den)


def _aroon_up(high, n):
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        idx_max = int(np.nanargmax(w))
        return 100.0 * idx_max / (len(w) - 1) if len(w) > 1 else np.nan
    return high.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


def _aroon_down(low, n):
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        idx_min = int(np.nanargmin(w))
        return 100.0 * idx_min / (len(w) - 1) if len(w) > 1 else np.nan
    return low.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


# ============================================================
# Bucket BB — Heikin-Ashi extensions (226-232)
# ============================================================


def f47_atxs_226_ha_close_minus_sma21_over_atr21_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(HA-close - SMA21(HA-close)) / ATR21 — Heikin-Ashi smoothed-close extension."""
    ha = _heikin_ashi(open_, high, low, close)
    return (_safe_div(ha["close"] - _sma(ha["close"], MDAYS), _atr(high, low, close, MDAYS))).diff()


def f47_atxs_227_ha_bullish_streak_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive run of HA-bullish bars (HA-close > HA-open) — HA trend persistence."""
    ha = _heikin_ashi(open_, high, low, close)
    return (_streak_true(ha["close"] > ha["open"])).diff()


def f47_atxs_228_ha_bullish_streak_max_past_21_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Longest HA-bullish streak in past 21 — recent trend strength."""
    ha = _heikin_ashi(open_, high, low, close)
    s = _streak_true(ha["close"] > ha["open"])
    return (s.rolling(MDAYS, min_periods=WDAYS).max().where(ha["close"].notna(), np.nan)).diff()


def f47_atxs_229_ha_bullish_streak_max_past_63_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Longest HA-bullish streak in past 63."""
    ha = _heikin_ashi(open_, high, low, close)
    s = _streak_true(ha["close"] > ha["open"])
    return (s.rolling(QDAYS, min_periods=MDAYS).max().where(ha["close"].notna(), np.nan)).diff()


def f47_atxs_230_ha_bearish_streak_max_past_21_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Longest HA-bearish streak in past 21 — recent down-trend strength."""
    ha = _heikin_ashi(open_, high, low, close)
    s = _streak_true(ha["close"] < ha["open"])
    return (s.rolling(MDAYS, min_periods=WDAYS).max().where(ha["close"].notna(), np.nan)).diff()


def f47_atxs_231_ha_upper_shadow_over_atr21_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """HA upper-shadow length / ATR21 — HA-rejection above."""
    ha = _heikin_ashi(open_, high, low, close)
    upper = ha["high"] - pd.concat([ha["open"], ha["close"]], axis=1).max(axis=1)
    return (_safe_div(upper, _atr(high, low, close, MDAYS))).diff()


def f47_atxs_232_ha_lower_shadow_over_atr21_d1(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """HA lower-shadow length / ATR21."""
    ha = _heikin_ashi(open_, high, low, close)
    lower = pd.concat([ha["open"], ha["close"]], axis=1).min(axis=1) - ha["low"]
    return (_safe_div(lower, _atr(high, low, close, MDAYS))).diff()


def f47_atxs_233_close_minus_chandelier_long_over_atr21_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - chandelier-long-exit) / ATR21 — distance above trailing long-stop in ATR units."""
    return (_safe_div(close - _chandelier_long(high, low, close), _atr(high, low, close, MDAYS))).diff()


def f47_atxs_234_chandelier_short_minus_close_over_atr21_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(chandelier-short-exit - close) / ATR21 — distance below trailing short-stop."""
    return (_safe_div(_chandelier_short(high, low, close) - close, _atr(high, low, close, MDAYS))).diff()


def f47_atxs_235_bars_since_chandelier_long_exit_hit_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since close last crossed below chandelier-long-exit (trail stop hit)."""
    ch = _chandelier_long(high, low, close)
    ev = (close.shift(1) >= ch.shift(1)) & (close < ch)
    return (_bars_since_true(ev)).diff()


def f47_atxs_236_chandelier_long_exit_count_252_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of chandelier-long-exit hits past 252 — trailing-stop event density."""
    ch = _chandelier_long(high, low, close)
    ev = ((close.shift(1) >= ch.shift(1)) & (close < ch)).astype(float)
    return (ev.rolling(YDAYS, min_periods=QDAYS).sum().where(ch.notna(), np.nan)).diff()


def f47_atxs_237_chandelier_position_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - chand-short)/(chand-long - chand-short) — position between long/short stops (0..1)."""
    cl = _chandelier_long(high, low, close)
    cs = _chandelier_short(high, low, close)
    return (_safe_div(close - cs, cl - cs)).diff()


def f47_atxs_238_close_above_chandelier_long_state_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close > chandelier-long-exit — long-trend-intact state."""
    ch = _chandelier_long(high, low, close)
    return ((close > ch).astype(float).where(ch.notna(), np.nan)).diff()


def f47_atxs_239_close_below_chandelier_short_state_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if close < chandelier-short-exit — short-trend-intact state."""
    ch = _chandelier_short(high, low, close)
    return ((close < ch).astype(float).where(ch.notna(), np.nan)).diff()


def f47_atxs_240_close_minus_vwma252_over_atr21_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - VWMA(252)) / ATR21 — annual VWMA extension."""
    return (_safe_div(close - _vwma(close, volume, YDAYS), _atr(high, low, close, MDAYS))).diff()


def f47_atxs_241_vwma21_minus_sma21_over_atr21_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(VWMA21 - SMA21) / ATR21 — vol-weight vs equal-weight bias in ATR units."""
    return (_safe_div(_vwma(close, volume, MDAYS) - _sma(close, MDAYS), _atr(high, low, close, MDAYS))).diff()


def f47_atxs_242_vwma63_minus_sma63_over_atr21_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(VWMA63 - SMA63) / ATR21 — quarterly vol-weight vs equal-weight gap."""
    return (_safe_div(_vwma(close, volume, QDAYS) - _sma(close, QDAYS), _atr(high, low, close, MDAYS))).diff()


def f47_atxs_243_close_minus_vwap_from_252d_high_over_atr21_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - VWAP-anchored-from-252d-high) / ATR21 — distance from peak-anchored VWAP.

    Anchored from the bar in the trailing 252d window where high was at its max.
    """
    high_arr = high.to_numpy(dtype=float)
    pv = (close * volume).to_numpy(dtype=float)
    vol_arr = volume.to_numpy(dtype=float)
    n = high_arr.size
    avwap = np.full(n, np.nan)
    for t in range(n):
        lo = max(0, t - YDAYS + 1)
        w = high_arr[lo : t + 1]
        if w.size == 0 or np.isnan(w).all():
            continue
        rel = int(np.nanargmax(w))
        k = lo + rel
        sum_pv = np.nansum(pv[k : t + 1])
        sum_v = np.nansum(vol_arr[k : t + 1])
        if sum_v == 0:
            continue
        avwap[t] = sum_pv / sum_v
    avwap_s = pd.Series(avwap, index=close.index)
    return (_safe_div(close - avwap_s, _atr(high, low, close, MDAYS))).diff()


def f47_atxs_244_close_minus_vwap_from_504d_high_over_atr252_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - VWAP-anchored-from-504d-high) / ATR252 — multi-year-peak-anchored VWAP gap."""
    high_arr = high.to_numpy(dtype=float)
    pv = (close * volume).to_numpy(dtype=float)
    vol_arr = volume.to_numpy(dtype=float)
    n = high_arr.size
    avwap = np.full(n, np.nan)
    for t in range(n):
        lo = max(0, t - DDAYS_2Y + 1)
        w = high_arr[lo : t + 1]
        if w.size == 0 or np.isnan(w).all():
            continue
        rel = int(np.nanargmax(w))
        k = lo + rel
        sum_pv = np.nansum(pv[k : t + 1])
        sum_v = np.nansum(vol_arr[k : t + 1])
        if sum_v == 0:
            continue
        avwap[t] = sum_pv / sum_v
    avwap_s = pd.Series(avwap, index=close.index)
    return (_safe_div(close - avwap_s, _atr(high, low, close, YDAYS))).diff()


def f47_atxs_245_close_minus_cum_vwap_over_atr21_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - cumulative VWAP from start of series) / ATR21 — IPO-anchored cumulative VWAP gap."""
    cv = _safe_div((close * volume).cumsum(), volume.cumsum())
    return (_safe_div(close - cv, _atr(high, low, close, MDAYS))).diff()


def f47_atxs_246_close_minus_cum_vwap_over_atr252_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - cumulative VWAP) / ATR252 — annual-ATR version of cum-VWAP gap."""
    cv = _safe_div((close * volume).cumsum(), volume.cumsum())
    return (_safe_div(close - cv, _atr(high, low, close, YDAYS))).diff()


def f47_atxs_247_close_minus_vwma126_over_atr63_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - VWMA(126)) / ATR63 — half-year VWMA extension in quarterly ATR."""
    return (_safe_div(close - _vwma(close, volume, 126), _atr(high, low, close, QDAYS))).diff()


def f47_atxs_248_bollinger_pct_b_alt_horizon_d1(close: pd.Series) -> pd.Series:
    """%B over 50-bar BB (distinct horizon from 20-bar in 154) — longer-period band position."""
    m = close.rolling(50, min_periods=20).mean()
    sd = close.rolling(50, min_periods=20).std()
    return (_safe_div(close - (m - 2.0 * sd), 4.0 * sd)).diff()


def f47_atxs_249_pct_b_q95_state_252_d1(close: pd.Series) -> pd.Series:
    """1 if 20-bar %B > its trailing 252d 95th percentile — extreme upper-band position."""
    m = close.rolling(20, min_periods=10).mean()
    sd = close.rolling(20, min_periods=10).std()
    pb = _safe_div(close - (m - 2.0 * sd), 4.0 * sd)
    q = pb.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    return ((pb > q).astype(float).where(q.notna(), np.nan)).diff()


def f47_atxs_250_pct_b_q99_state_252_d1(close: pd.Series) -> pd.Series:
    """1 if 20-bar %B > 99th pct of trailing 252d — superextreme band position."""
    m = close.rolling(20, min_periods=10).mean()
    sd = close.rolling(20, min_periods=10).std()
    pb = _safe_div(close - (m - 2.0 * sd), 4.0 * sd)
    q = pb.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    return ((pb > q).astype(float).where(q.notna(), np.nan)).diff()


def f47_atxs_251_bb_bandwidth_zscore_252_d1(close: pd.Series) -> pd.Series:
    """Z-score of BB-bandwidth (4*sd) vs trailing 252d — band-width regime."""
    sd = close.rolling(20, min_periods=10).std()
    return (_rolling_zscore(sd * 4.0, YDAYS, min_periods=QDAYS)).diff()


def f47_atxs_252_bb_bandwidth_pct_rank_252_d1(close: pd.Series) -> pd.Series:
    """Percentile rank of BB-bandwidth vs trailing 252d."""
    sd = close.rolling(20, min_periods=10).std()
    return ((sd * 4.0).rolling(YDAYS, min_periods=QDAYS).rank(pct=True)).diff()


def f47_atxs_253_bb_walk_above_upper_count_63_d1(close: pd.Series) -> pd.Series:
    """Count past 63 of bars with close > BB upper — quarterly walking-the-band intensity."""
    m = close.rolling(20, min_periods=10).mean()
    sd = close.rolling(20, min_periods=10).std()
    return ((close > (m + 2.0 * sd)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(sd.notna(), np.nan)).diff()


def f47_atxs_254_bb_walk_above_upper_count_252_d1(close: pd.Series) -> pd.Series:
    """Annual count of bars with close > BB upper."""
    m = close.rolling(20, min_periods=10).mean()
    sd = close.rolling(20, min_periods=10).std()
    return ((close > (m + 2.0 * sd)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(sd.notna(), np.nan)).diff()


def f47_atxs_255_bb_walk_above_upper_3plus_state_d1(close: pd.Series) -> pd.Series:
    """1 if BB-walk streak >= 3 — sustained upper-band walk."""
    m = close.rolling(20, min_periods=10).mean()
    sd = close.rolling(20, min_periods=10).std()
    streak = _streak_true(close > (m + 2.0 * sd))
    return ((streak >= 3).astype(float).where(sd.notna(), np.nan)).diff()


def f47_atxs_256_donchian_position_21_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position of close in 21d HL range (Donchian-21 position)."""
    hh = high.rolling(MDAYS, min_periods=WDAYS).max()
    ll = low.rolling(MDAYS, min_periods=WDAYS).min()
    return (_safe_div(close - ll, hh - ll)).diff()


def f47_atxs_257_donchian_position_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position of close in 63d HL range."""
    hh = high.rolling(QDAYS, min_periods=MDAYS).max()
    ll = low.rolling(QDAYS, min_periods=MDAYS).min()
    return (_safe_div(close - ll, hh - ll)).diff()


def f47_atxs_258_donchian_position_252_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position of close in 252d HL range."""
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    return (_safe_div(close - ll, hh - ll)).diff()


def f47_atxs_259_donchian_position_504_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position of close in 504d (2y) HL range."""
    hh = high.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    ll = low.rolling(DDAYS_2Y, min_periods=YDAYS).min()
    return (_safe_div(close - ll, hh - ll)).diff()


def f47_atxs_260_aroon_up_21_d1(high: pd.Series) -> pd.Series:
    """Aroon-up(21) — bars since 21d high, normalized 0-100 (100 = today is the high)."""
    return (_aroon_up(high, MDAYS)).diff()


def f47_atxs_261_aroon_up_minus_down_63_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Aroon-up(63) - Aroon-down(63) — quarterly trend bias from Aroon."""
    return (_aroon_up(high, QDAYS) - _aroon_down(low, QDAYS)).diff()


def f47_atxs_262_cci_20_zscore_252_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score (252d) of CCI(20) — Commodity Channel Index extension in own-distribution units.

    CCI = (typical - SMA20(typical)) / (0.015 * mean-abs-dev(typical))
    """
    tp = (high + low + close) / 3.0
    sma_tp = tp.rolling(20, min_periods=10).mean()
    mad = (tp - sma_tp).abs().rolling(20, min_periods=10).mean()
    cci = _safe_div(tp - sma_tp, 0.015 * mad)
    return (_rolling_zscore(cci, YDAYS, min_periods=QDAYS)).diff()


def f47_atxs_263_mean_ext_across_4_horizons_atr21_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean of (close-SMA_k)/ATR21 across k in {21,63,200,252} — average multi-horizon extension."""
    a = _atr(high, low, close, MDAYS)
    e1 = _safe_div(close - _sma(close, MDAYS), a)
    e2 = _safe_div(close - _sma(close, QDAYS), a)
    e3 = _safe_div(close - _sma(close, 200), a)
    e4 = _safe_div(close - _sma(close, YDAYS), a)
    return ((e1 + e2 + e3 + e4) / 4.0).diff()


def f47_atxs_264_std_ext_across_4_horizons_atr21_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std of (close-SMA_k)/ATR21 across k in {21,63,200,252} — dispersion of multi-horizon ext."""
    a = _atr(high, low, close, MDAYS)
    e = pd.concat([
        _safe_div(close - _sma(close, MDAYS), a).rename("e21"),
        _safe_div(close - _sma(close, QDAYS), a).rename("e63"),
        _safe_div(close - _sma(close, 200), a).rename("e200"),
        _safe_div(close - _sma(close, YDAYS), a).rename("e252"),
    ], axis=1)
    return (e.std(axis=1)).diff()


def f47_atxs_265_max_ext_across_4_horizons_atr21_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max of (close-SMA_k)/ATR21 across k in {21,63,200,252} — most-extended horizon."""
    a = _atr(high, low, close, MDAYS)
    e = pd.concat([
        _safe_div(close - _sma(close, MDAYS), a).rename("e21"),
        _safe_div(close - _sma(close, QDAYS), a).rename("e63"),
        _safe_div(close - _sma(close, 200), a).rename("e200"),
        _safe_div(close - _sma(close, YDAYS), a).rename("e252"),
    ], axis=1)
    return (e.max(axis=1)).diff()


def f47_atxs_266_count_ma_above_4_horizons_d1(close: pd.Series) -> pd.Series:
    """Count of MAs (5,21,50,200) below which close currently sits OVER — # of MAs price is above."""
    c = ((close > _sma(close, WDAYS)).astype(float).fillna(0)
         + (close > _sma(close, MDAYS)).astype(float).fillna(0)
         + (close > _sma(close, 50)).astype(float).fillna(0)
         + (close > _sma(close, 200)).astype(float).fillna(0))
    return (c).diff()


def f47_atxs_267_all_4_mas_above_state_d1(close: pd.Series) -> pd.Series:
    """1 if close > each of SMA(5,21,50,200) — fully bullish stack state."""
    return (((close > _sma(close, WDAYS)) & (close > _sma(close, MDAYS))

            & (close > _sma(close, 50)) & (close > _sma(close, 200))).astype(float).where(_sma(close, 200).notna(), np.nan)).diff()


def f47_atxs_268_all_4_mas_above_dwell_21_d1(close: pd.Series) -> pd.Series:
    """Fraction past 21 with close above all 4 MAs (5,21,50,200)."""
    s = ((close > _sma(close, WDAYS)) & (close > _sma(close, MDAYS))
         & (close > _sma(close, 50)) & (close > _sma(close, 200))).astype(float)
    return (s.rolling(MDAYS, min_periods=WDAYS).mean().where(_sma(close, 200).notna(), np.nan)).diff()


def f47_atxs_269_all_4_mas_below_state_d1(close: pd.Series) -> pd.Series:
    """1 if close < each of SMA(5,21,50,200) — fully bearish stack state."""
    return (((close < _sma(close, WDAYS)) & (close < _sma(close, MDAYS))

            & (close < _sma(close, 50)) & (close < _sma(close, 200))).astype(float).where(_sma(close, 200).notna(), np.nan)).diff()


def f47_atxs_270_ma_stack_cross_event_21d_d1(close: pd.Series) -> pd.Series:
    """1 if past 21 bars contained transition from bullish stack to bearish stack."""
    bull = ((close > _sma(close, WDAYS)) & (close > _sma(close, MDAYS))
            & (close > _sma(close, 50)) & (close > _sma(close, 200)))
    bear = ((close < _sma(close, WDAYS)) & (close < _sma(close, MDAYS))
            & (close < _sma(close, 50)) & (close < _sma(close, 200)))
    had_bull_recent = bull.rolling(MDAYS, min_periods=WDAYS).max() > 0
    now_bear = bear
    return ((had_bull_recent & now_bear).astype(float).where(_sma(close, 200).notna(), np.nan)).diff()


def f47_atxs_271_bars_since_ext_sma200_atr21_above_5_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since (close-SMA200)/ATR21 > 5 — extreme overextension recency."""
    e = _safe_div(close - _sma(close, 200), _atr(high, low, close, MDAYS))
    return (_bars_since_true(e > 5.0)).diff()


def f47_atxs_272_bars_since_ext_sma200_atr21_below_neg2_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since (close-SMA200)/ATR21 < -2 — deep underextension recency."""
    e = _safe_div(close - _sma(close, 200), _atr(high, low, close, MDAYS))
    return (_bars_since_true(e < -2.0)).diff()


def f47_atxs_273_bars_since_bb_walk_above_upper_d1(close: pd.Series) -> pd.Series:
    """Bars since close was last > BB-upper (last upper-band touch)."""
    m = close.rolling(20, min_periods=10).mean()
    sd = close.rolling(20, min_periods=10).std()
    return (_bars_since_true(close > (m + 2.0 * sd))).diff()


def f47_atxs_274_longest_bb_walk_above_upper_streak_252_d1(close: pd.Series) -> pd.Series:
    """Longest BB-walk-above-upper streak in past 252."""
    m = close.rolling(20, min_periods=10).mean()
    sd = close.rolling(20, min_periods=10).std()
    s = _streak_true(close > (m + 2.0 * sd))
    return (s.rolling(YDAYS, min_periods=QDAYS).max().where(sd.notna(), np.nan)).diff()


def f47_atxs_275_longest_above_sma21_streak_252_d1(close: pd.Series) -> pd.Series:
    """Longest consecutive-above-SMA21 streak in past 252."""
    s = _streak_true(close > _sma(close, MDAYS))
    return (s.rolling(YDAYS, min_periods=QDAYS).max().where(_sma(close, MDAYS).notna(), np.nan)).diff()


def f47_atxs_276_longest_above_sma200_streak_252_d1(close: pd.Series) -> pd.Series:
    """Longest consecutive-above-SMA200 streak in past 252."""
    s = _streak_true(close > _sma(close, 200))
    return (s.rolling(YDAYS, min_periods=QDAYS).max().where(_sma(close, 200).notna(), np.nan)).diff()


def f47_atxs_277_current_above_sma21_streak_d1(close: pd.Series) -> pd.Series:
    """Current consecutive-above-SMA21 streak."""
    return (_streak_true(close > _sma(close, MDAYS)).where(_sma(close, MDAYS).notna(), np.nan)).diff()


def f47_atxs_278_current_above_sma200_streak_d1(close: pd.Series) -> pd.Series:
    """Current consecutive-above-SMA200 streak."""
    return (_streak_true(close > _sma(close, 200)).where(_sma(close, 200).notna(), np.nan)).diff()


def f47_atxs_279_short_over_medium_ext_ratio_d1(close: pd.Series) -> pd.Series:
    """(close - SMA21)/(close - SMA63) — short-extension vs medium-extension ratio."""
    return (_safe_div(close - _sma(close, MDAYS), close - _sma(close, QDAYS))).diff()


def f47_atxs_280_medium_over_long_ext_ratio_d1(close: pd.Series) -> pd.Series:
    """(close - SMA63)/(close - SMA252) — medium-vs-long extension ratio."""
    return (_safe_div(close - _sma(close, QDAYS), close - _sma(close, YDAYS))).diff()


def f47_atxs_281_positive_ext_only_sma21_atr21_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close-SMA21)/ATR21 only when close > SMA21, else NaN — positive-only extension."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return (e.where(close > _sma(close, MDAYS), np.nan)).diff()


def f47_atxs_282_mean_above_ext_past_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean of positive-only extension past 63 — avg magnitude when over-extended above MA."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    pos = e.where(e > 0)
    return (pos.rolling(QDAYS, min_periods=MDAYS).mean()).diff()


def f47_atxs_283_mean_below_ext_past_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean of negative-only extension past 63 — avg magnitude when under-extended below MA."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    neg = e.where(e < 0)
    return (neg.rolling(QDAYS, min_periods=MDAYS).mean()).diff()


def f47_atxs_284_prob_close_above_sma21_in_252_d1(close: pd.Series) -> pd.Series:
    """Probability of close > SMA21 past 252 — bull-side fraction."""
    return ((close > _sma(close, MDAYS)).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(_sma(close, MDAYS).notna(), np.nan)).diff()


def f47_atxs_285_prob_close_above_sma200_in_252_d1(close: pd.Series) -> pd.Series:
    """Probability of close > SMA200 past 252."""
    return ((close > _sma(close, 200)).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(_sma(close, 200).notna(), np.nan)).diff()


def f47_atxs_286_prob_ext_above_2_past_252_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Probability of (close-SMA21)/ATR21 > 2 past 252 — overextension prior probability."""
    e = _safe_div(close - _sma(close, MDAYS), _atr(high, low, close, MDAYS))
    return ((e > 2.0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(e.notna(), np.nan)).diff()


def f47_atxs_287_dist_from_252d_breakout_level_atr21_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - highest-high-prior-to-today over 252d) / ATR21 — extension above 252d breakout level.

    Uses high.shift(1).rolling to exclude today, so this measures distance ABOVE the breakout level.
    """
    bo = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    return (_safe_div(close - bo, _atr(high, low, close, MDAYS))).diff()


def f47_atxs_288_dist_from_63d_breakout_level_atr21_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 63d-prior-max-high) / ATR21 — extension above quarterly breakout level."""
    bo = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (_safe_div(close - bo, _atr(high, low, close, MDAYS))).diff()


def f47_atxs_289_dist_from_21d_breakout_level_atr21_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 21d-prior-max-high) / ATR21 — extension above monthly breakout level."""
    bo = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    return (_safe_div(close - bo, _atr(high, low, close, MDAYS))).diff()


def f47_atxs_290_breakout_amplitude_21d_atr_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """max(close - 21d-prior-max-high, 0) / ATR21 — positive breakout amplitude (0 if not above)."""
    bo = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    return ((_safe_div(close - bo, _atr(high, low, close, MDAYS))).clip(lower=0)).diff()


def f47_atxs_291_breakout_amplitude_63d_atr_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """max(close - 63d-prior-max-high, 0) / ATR21 — positive quarterly breakout amplitude."""
    bo = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((_safe_div(close - bo, _atr(high, low, close, MDAYS))).clip(lower=0)).diff()


def f47_atxs_292_sustained_above_21d_breakout_count_63_d1(high: pd.Series) -> pd.Series:
    """Count past 63 bars where close > 21d-prior-max-high — sustained-above-breakout count."""
    bo = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    return ((high >= bo).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(bo.notna(), np.nan)).diff()


def f47_atxs_293_failed_breakout_count_63_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count past 63 bars where intraday high > 21d-prior-max-high BUT close <= 21d-prior-max-high — failed-BO count."""
    bo = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    failed = (high > bo) & (close <= bo)
    return (failed.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(bo.notna(), np.nan)).diff()


def f47_atxs_294_bars_since_21d_breakout_d1(high: pd.Series) -> pd.Series:
    """Bars since high last reached its 21d prior-max-high level."""
    bo = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    return (_bars_since_true(high >= bo)).diff()


def f47_atxs_295_close_position_in_2y_range_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position of close in 504d (2y) HL range — duplicate label preserved as channel-position summary."""
    hh = high.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    ll = low.rolling(DDAYS_2Y, min_periods=YDAYS).min()
    return (_safe_div(close - ll, hh - ll)).diff()


def f47_atxs_296_close_position_in_1y_range_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position of close in 252d (1y) HL range."""
    hh = high.rolling(YDAYS, min_periods=QDAYS).max()
    ll = low.rolling(YDAYS, min_periods=QDAYS).min()
    return (_safe_div(close - ll, hh - ll)).diff()


def f47_atxs_297_close_position_in_quarter_range_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position of close in 63d HL range."""
    hh = high.rolling(QDAYS, min_periods=MDAYS).max()
    ll = low.rolling(QDAYS, min_periods=MDAYS).min()
    return (_safe_div(close - ll, hh - ll)).diff()


def f47_atxs_298_close_position_in_month_range_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position of close in 21d HL range — monthly channel position (no ATR)."""
    hh = high.rolling(MDAYS, min_periods=WDAYS).max()
    ll = low.rolling(MDAYS, min_periods=WDAYS).min()
    return (_safe_div(close - ll, hh - ll)).diff()


def f47_atxs_299_close_pct_rank_cumulative_d1(close: pd.Series) -> pd.Series:
    """Cumulative percentile rank of close vs all prior closes — lifetime ranking (0..1)."""
    return (close.expanding(min_periods=MDAYS).rank(pct=True)).diff()


def f47_atxs_300_close_pct_rank_1260_d1(close: pd.Series) -> pd.Series:
    """Percentile rank of close vs trailing 1260d (5y) distribution."""
    return (close.rolling(DDAYS_5Y, min_periods=YDAYS).rank(pct=True)).diff()


# ============================================================
#                         REGISTRY 226-300 (d1)
# ============================================================

_HLC = ["high", "low", "close"]
_HLCV = ["high", "low", "close", "volume"]
_OHLC = ["open", "high", "low", "close"]

ATR_EXTENSION_SIGNATURE_D1_REGISTRY_226_300 = {
    "f47_atxs_226_ha_close_minus_sma21_over_atr21_d1": {"inputs": _OHLC, "func": f47_atxs_226_ha_close_minus_sma21_over_atr21_d1},
    "f47_atxs_227_ha_bullish_streak_d1": {"inputs": _OHLC, "func": f47_atxs_227_ha_bullish_streak_d1},
    "f47_atxs_228_ha_bullish_streak_max_past_21_d1": {"inputs": _OHLC, "func": f47_atxs_228_ha_bullish_streak_max_past_21_d1},
    "f47_atxs_229_ha_bullish_streak_max_past_63_d1": {"inputs": _OHLC, "func": f47_atxs_229_ha_bullish_streak_max_past_63_d1},
    "f47_atxs_230_ha_bearish_streak_max_past_21_d1": {"inputs": _OHLC, "func": f47_atxs_230_ha_bearish_streak_max_past_21_d1},
    "f47_atxs_231_ha_upper_shadow_over_atr21_d1": {"inputs": _OHLC, "func": f47_atxs_231_ha_upper_shadow_over_atr21_d1},
    "f47_atxs_232_ha_lower_shadow_over_atr21_d1": {"inputs": _OHLC, "func": f47_atxs_232_ha_lower_shadow_over_atr21_d1},
    "f47_atxs_233_close_minus_chandelier_long_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_233_close_minus_chandelier_long_over_atr21_d1},
    "f47_atxs_234_chandelier_short_minus_close_over_atr21_d1": {"inputs": _HLC, "func": f47_atxs_234_chandelier_short_minus_close_over_atr21_d1},
    "f47_atxs_235_bars_since_chandelier_long_exit_hit_d1": {"inputs": _HLC, "func": f47_atxs_235_bars_since_chandelier_long_exit_hit_d1},
    "f47_atxs_236_chandelier_long_exit_count_252_d1": {"inputs": _HLC, "func": f47_atxs_236_chandelier_long_exit_count_252_d1},
    "f47_atxs_237_chandelier_position_d1": {"inputs": _HLC, "func": f47_atxs_237_chandelier_position_d1},
    "f47_atxs_238_close_above_chandelier_long_state_d1": {"inputs": _HLC, "func": f47_atxs_238_close_above_chandelier_long_state_d1},
    "f47_atxs_239_close_below_chandelier_short_state_d1": {"inputs": _HLC, "func": f47_atxs_239_close_below_chandelier_short_state_d1},
    "f47_atxs_240_close_minus_vwma252_over_atr21_d1": {"inputs": _HLCV, "func": f47_atxs_240_close_minus_vwma252_over_atr21_d1},
    "f47_atxs_241_vwma21_minus_sma21_over_atr21_d1": {"inputs": _HLCV, "func": f47_atxs_241_vwma21_minus_sma21_over_atr21_d1},
    "f47_atxs_242_vwma63_minus_sma63_over_atr21_d1": {"inputs": _HLCV, "func": f47_atxs_242_vwma63_minus_sma63_over_atr21_d1},
    "f47_atxs_243_close_minus_vwap_from_252d_high_over_atr21_d1": {"inputs": _HLCV, "func": f47_atxs_243_close_minus_vwap_from_252d_high_over_atr21_d1},
    "f47_atxs_244_close_minus_vwap_from_504d_high_over_atr252_d1": {"inputs": _HLCV, "func": f47_atxs_244_close_minus_vwap_from_504d_high_over_atr252_d1},
    "f47_atxs_245_close_minus_cum_vwap_over_atr21_d1": {"inputs": _HLCV, "func": f47_atxs_245_close_minus_cum_vwap_over_atr21_d1},
    "f47_atxs_246_close_minus_cum_vwap_over_atr252_d1": {"inputs": _HLCV, "func": f47_atxs_246_close_minus_cum_vwap_over_atr252_d1},
    "f47_atxs_247_close_minus_vwma126_over_atr63_d1": {"inputs": _HLCV, "func": f47_atxs_247_close_minus_vwma126_over_atr63_d1},
    "f47_atxs_248_bollinger_pct_b_alt_horizon_d1": {"inputs": ["close"], "func": f47_atxs_248_bollinger_pct_b_alt_horizon_d1},
    "f47_atxs_249_pct_b_q95_state_252_d1": {"inputs": ["close"], "func": f47_atxs_249_pct_b_q95_state_252_d1},
    "f47_atxs_250_pct_b_q99_state_252_d1": {"inputs": ["close"], "func": f47_atxs_250_pct_b_q99_state_252_d1},
    "f47_atxs_251_bb_bandwidth_zscore_252_d1": {"inputs": ["close"], "func": f47_atxs_251_bb_bandwidth_zscore_252_d1},
    "f47_atxs_252_bb_bandwidth_pct_rank_252_d1": {"inputs": ["close"], "func": f47_atxs_252_bb_bandwidth_pct_rank_252_d1},
    "f47_atxs_253_bb_walk_above_upper_count_63_d1": {"inputs": ["close"], "func": f47_atxs_253_bb_walk_above_upper_count_63_d1},
    "f47_atxs_254_bb_walk_above_upper_count_252_d1": {"inputs": ["close"], "func": f47_atxs_254_bb_walk_above_upper_count_252_d1},
    "f47_atxs_255_bb_walk_above_upper_3plus_state_d1": {"inputs": ["close"], "func": f47_atxs_255_bb_walk_above_upper_3plus_state_d1},
    "f47_atxs_256_donchian_position_21_d1": {"inputs": _HLC, "func": f47_atxs_256_donchian_position_21_d1},
    "f47_atxs_257_donchian_position_63_d1": {"inputs": _HLC, "func": f47_atxs_257_donchian_position_63_d1},
    "f47_atxs_258_donchian_position_252_d1": {"inputs": _HLC, "func": f47_atxs_258_donchian_position_252_d1},
    "f47_atxs_259_donchian_position_504_d1": {"inputs": _HLC, "func": f47_atxs_259_donchian_position_504_d1},
    "f47_atxs_260_aroon_up_21_d1": {"inputs": ["high"], "func": f47_atxs_260_aroon_up_21_d1},
    "f47_atxs_261_aroon_up_minus_down_63_d1": {"inputs": ["high", "low"], "func": f47_atxs_261_aroon_up_minus_down_63_d1},
    "f47_atxs_262_cci_20_zscore_252_d1": {"inputs": _HLC, "func": f47_atxs_262_cci_20_zscore_252_d1},
    "f47_atxs_263_mean_ext_across_4_horizons_atr21_d1": {"inputs": _HLC, "func": f47_atxs_263_mean_ext_across_4_horizons_atr21_d1},
    "f47_atxs_264_std_ext_across_4_horizons_atr21_d1": {"inputs": _HLC, "func": f47_atxs_264_std_ext_across_4_horizons_atr21_d1},
    "f47_atxs_265_max_ext_across_4_horizons_atr21_d1": {"inputs": _HLC, "func": f47_atxs_265_max_ext_across_4_horizons_atr21_d1},
    "f47_atxs_266_count_ma_above_4_horizons_d1": {"inputs": ["close"], "func": f47_atxs_266_count_ma_above_4_horizons_d1},
    "f47_atxs_267_all_4_mas_above_state_d1": {"inputs": ["close"], "func": f47_atxs_267_all_4_mas_above_state_d1},
    "f47_atxs_268_all_4_mas_above_dwell_21_d1": {"inputs": ["close"], "func": f47_atxs_268_all_4_mas_above_dwell_21_d1},
    "f47_atxs_269_all_4_mas_below_state_d1": {"inputs": ["close"], "func": f47_atxs_269_all_4_mas_below_state_d1},
    "f47_atxs_270_ma_stack_cross_event_21d_d1": {"inputs": ["close"], "func": f47_atxs_270_ma_stack_cross_event_21d_d1},
    "f47_atxs_271_bars_since_ext_sma200_atr21_above_5_d1": {"inputs": _HLC, "func": f47_atxs_271_bars_since_ext_sma200_atr21_above_5_d1},
    "f47_atxs_272_bars_since_ext_sma200_atr21_below_neg2_d1": {"inputs": _HLC, "func": f47_atxs_272_bars_since_ext_sma200_atr21_below_neg2_d1},
    "f47_atxs_273_bars_since_bb_walk_above_upper_d1": {"inputs": ["close"], "func": f47_atxs_273_bars_since_bb_walk_above_upper_d1},
    "f47_atxs_274_longest_bb_walk_above_upper_streak_252_d1": {"inputs": ["close"], "func": f47_atxs_274_longest_bb_walk_above_upper_streak_252_d1},
    "f47_atxs_275_longest_above_sma21_streak_252_d1": {"inputs": ["close"], "func": f47_atxs_275_longest_above_sma21_streak_252_d1},
    "f47_atxs_276_longest_above_sma200_streak_252_d1": {"inputs": ["close"], "func": f47_atxs_276_longest_above_sma200_streak_252_d1},
    "f47_atxs_277_current_above_sma21_streak_d1": {"inputs": ["close"], "func": f47_atxs_277_current_above_sma21_streak_d1},
    "f47_atxs_278_current_above_sma200_streak_d1": {"inputs": ["close"], "func": f47_atxs_278_current_above_sma200_streak_d1},
    "f47_atxs_279_short_over_medium_ext_ratio_d1": {"inputs": ["close"], "func": f47_atxs_279_short_over_medium_ext_ratio_d1},
    "f47_atxs_280_medium_over_long_ext_ratio_d1": {"inputs": ["close"], "func": f47_atxs_280_medium_over_long_ext_ratio_d1},
    "f47_atxs_281_positive_ext_only_sma21_atr21_d1": {"inputs": _HLC, "func": f47_atxs_281_positive_ext_only_sma21_atr21_d1},
    "f47_atxs_282_mean_above_ext_past_63_d1": {"inputs": _HLC, "func": f47_atxs_282_mean_above_ext_past_63_d1},
    "f47_atxs_283_mean_below_ext_past_63_d1": {"inputs": _HLC, "func": f47_atxs_283_mean_below_ext_past_63_d1},
    "f47_atxs_284_prob_close_above_sma21_in_252_d1": {"inputs": ["close"], "func": f47_atxs_284_prob_close_above_sma21_in_252_d1},
    "f47_atxs_285_prob_close_above_sma200_in_252_d1": {"inputs": ["close"], "func": f47_atxs_285_prob_close_above_sma200_in_252_d1},
    "f47_atxs_286_prob_ext_above_2_past_252_d1": {"inputs": _HLC, "func": f47_atxs_286_prob_ext_above_2_past_252_d1},
    "f47_atxs_287_dist_from_252d_breakout_level_atr21_d1": {"inputs": _HLC, "func": f47_atxs_287_dist_from_252d_breakout_level_atr21_d1},
    "f47_atxs_288_dist_from_63d_breakout_level_atr21_d1": {"inputs": _HLC, "func": f47_atxs_288_dist_from_63d_breakout_level_atr21_d1},
    "f47_atxs_289_dist_from_21d_breakout_level_atr21_d1": {"inputs": _HLC, "func": f47_atxs_289_dist_from_21d_breakout_level_atr21_d1},
    "f47_atxs_290_breakout_amplitude_21d_atr_d1": {"inputs": _HLC, "func": f47_atxs_290_breakout_amplitude_21d_atr_d1},
    "f47_atxs_291_breakout_amplitude_63d_atr_d1": {"inputs": _HLC, "func": f47_atxs_291_breakout_amplitude_63d_atr_d1},
    "f47_atxs_292_sustained_above_21d_breakout_count_63_d1": {"inputs": ["high"], "func": f47_atxs_292_sustained_above_21d_breakout_count_63_d1},
    "f47_atxs_293_failed_breakout_count_63_d1": {"inputs": _HLC, "func": f47_atxs_293_failed_breakout_count_63_d1},
    "f47_atxs_294_bars_since_21d_breakout_d1": {"inputs": ["high"], "func": f47_atxs_294_bars_since_21d_breakout_d1},
    "f47_atxs_295_close_position_in_2y_range_d1": {"inputs": _HLC, "func": f47_atxs_295_close_position_in_2y_range_d1},
    "f47_atxs_296_close_position_in_1y_range_d1": {"inputs": _HLC, "func": f47_atxs_296_close_position_in_1y_range_d1},
    "f47_atxs_297_close_position_in_quarter_range_d1": {"inputs": _HLC, "func": f47_atxs_297_close_position_in_quarter_range_d1},
    "f47_atxs_298_close_position_in_month_range_d1": {"inputs": _HLC, "func": f47_atxs_298_close_position_in_month_range_d1},
    "f47_atxs_299_close_pct_rank_cumulative_d1": {"inputs": ["close"], "func": f47_atxs_299_close_pct_rank_cumulative_d1},
    "f47_atxs_300_close_pct_rank_1260_d1": {"inputs": ["close"], "func": f47_atxs_300_close_pct_rank_1260_d1},
}
