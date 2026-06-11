"""32_divergence_detection d1 features 376-450 — order-1 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff(). Self-contained; helpers redefined locally per HANDOFF."""
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_5Y = 1260

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
    idx = num.index if hasattr(num, 'index') else None
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
        xm = x.mean()
        wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def _pct_rank(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).rank(pct=True)

def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()

def _sma(s, n):
    return s.rolling(n, min_periods=max(n // 3, 2)).mean()

def _bars_since_true(flag):
    f = (flag.fillna(0) > 0).astype(int)
    idx = np.arange(len(f))
    last = np.where(f.values == 1, idx, np.nan)
    last_ffill = pd.Series(last, index=f.index).ffill()
    return pd.Series(idx, index=f.index) - last_ffill

def _rsi_wilder(close, n=14):
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = (-delta).clip(lower=0)
    ag = gain.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    al = loss.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    rs = _safe_div(ag, al)
    return 100.0 - 100.0 / (1.0 + rs)

def _macd_line(close, fast=12, slow=26):
    return _ema(close, fast) - _ema(close, slow)

def _macd_hist(close, fast=12, slow=26, sig=9):
    line = _macd_line(close, fast, slow)
    return line - _ema(line, sig)

def _obv(close, volume):
    return (np.sign(close.diff().fillna(0)) * volume).cumsum()

def _stoch_k(high, low, close, n=14):
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    return 100.0 * _safe_div(close - ll, hh - ll)

def _mfi(high, low, close, volume, n=14):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    delta = tp.diff()
    pos = rmf.where(delta > 0, 0).rolling(n, min_periods=max(n // 3, 2)).sum()
    neg = rmf.where(delta < 0, 0).rolling(n, min_periods=max(n // 3, 2)).sum()
    mr = _safe_div(pos, neg)
    return 100.0 - 100.0 / (1.0 + mr)

def _shift_div_bearish(price, osc, k):
    pp = price.shift(k)
    op = osc.shift(k)
    return ((price > pp) & (osc < op)).astype(float).where(pp.notna() & op.notna(), np.nan)

def _slope_div_sign(price, osc, n):
    ps = _rolling_slope(_safe_log(price), n)
    osl = _rolling_slope(osc, n)
    return ((ps > 0) & (osl < 0)).astype(float).where(ps.notna() & osl.notna(), np.nan)

def _div_confirmed_within(price, osc, div_lookback, confirm_window, confirm_drop_pct):
    """+1 (held at confirm bar) when a divergence fired N=confirm_window bars ago AND
    price has since dropped >= confirm_drop_pct (PIT-safe: looks back, never forward)."""
    flag = _shift_div_bearish(price, osc, div_lookback).fillna(0)
    flag_then = flag.shift(confirm_window).fillna(0)
    price_then = price.shift(confirm_window)
    dropped = price / price_then - 1.0 <= -confirm_drop_pct
    return ((flag_then == 1) & dropped).astype(float)

def _div_failed_within(price, osc, div_lookback, confirm_window, fail_rise_pct):
    """+1 when divergence fired N bars ago AND price has since risen >= fail_rise_pct (failed div)."""
    flag = _shift_div_bearish(price, osc, div_lookback).fillna(0)
    flag_then = flag.shift(confirm_window).fillna(0)
    price_then = price.shift(confirm_window)
    rose = price / price_then - 1.0 >= fail_rise_pct
    return ((flag_then == 1) & rose).astype(float)

def _nth_most_recent_event_offset(flag, n_th, max_lookback):
    """For each bar, returns the bars-back-to-the-Nth-most-recent True event in trailing max_lookback.
    Uses a rolling-apply window because order matters."""
    f = (flag.fillna(0) > 0).astype(int).values
    out = np.full(len(f), np.nan)
    for t in range(len(f)):
        start = max(0, t - max_lookback + 1)
        events = [i for i in range(t, start - 1, -1) if f[i] == 1]
        if len(events) >= n_th:
            out[t] = float(t - events[n_th - 1])
    return pd.Series(out, index=flag.index)

def _bb(close, n=20, k=2.0):
    m = _sma(close, n)
    sd = close.rolling(n, min_periods=max(n // 3, 2)).std()
    return (m, m + k * sd, m - k * sd)

def _keltner_upper(high, low, close, n=20, atr_mult=2.0):
    return _ema(close, n) + atr_mult * _atr(high, low, close, n)

def _keltner_lower(high, low, close, n=20, atr_mult=2.0):
    return _ema(close, n) - atr_mult * _atr(high, low, close, n)

def _bb_width(close, n=20, k=2.0):
    m, u, l = _bb(close, n, k)
    return _safe_div(u - l, m)

def _bb_squeeze_flag(close, high, low):
    _, ubb, lbb = _bb(close, 20, 2.0)
    ku = _keltner_upper(high, low, close, 20, 2.0)
    kl = _keltner_lower(high, low, close, 20, 2.0)
    return ((ubb < ku) & (lbb > kl)).astype(float).where(ubb.notna() & ku.notna(), np.nan)

def _is_doji(open_, close, high, low, body_max_frac=0.1):
    rng = (high - low).replace(0, np.nan)
    return ((close - open_).abs() / rng < body_max_frac).astype(float).where(rng.notna(), np.nan)

def _is_shooting_star(open_, close, high, low):
    rng = (high - low).replace(0, np.nan)
    uw = (high - pd.concat([open_, close], axis=1).max(axis=1)) / rng
    lw = (pd.concat([open_, close], axis=1).min(axis=1) - low) / rng
    body = (close - open_).abs() / rng
    return ((uw > 0.6) & (lw < 0.1) & (body < 0.3)).astype(float).where(rng.notna(), np.nan)

def _is_hanging_man(open_, close, high, low):
    rng = (high - low).replace(0, np.nan)
    lw = (pd.concat([open_, close], axis=1).min(axis=1) - low) / rng
    uw = (high - pd.concat([open_, close], axis=1).max(axis=1)) / rng
    body = (close - open_).abs() / rng
    return ((lw > 0.6) & (uw < 0.1) & (body < 0.3)).astype(float).where(rng.notna(), np.nan)

def _is_bearish_engulfing(open_, close):
    pc = close.shift(1)
    po = open_.shift(1)
    return ((pc > po) & (close < open_) & (close < po) & (open_ > pc)).astype(float).where(pc.notna() & po.notna(), np.nan)

def _is_3_black_crows(open_, close):
    return ((close < open_) & (close.shift(1) < open_.shift(1)) & (close.shift(2) < open_.shift(2)) & (close < close.shift(1)) & (close.shift(1) < close.shift(2))).astype(float).where(close.shift(2).notna(), np.nan)

def _is_gravestone_doji(open_, close, high, low):
    rng = (high - low).replace(0, np.nan)
    body = (open_ - close).abs() / rng
    lw = (pd.concat([open_, close], axis=1).min(axis=1) - low) / rng
    uw = (high - pd.concat([open_, close], axis=1).max(axis=1)) / rng
    return ((body < 0.1) & (lw < 0.1) & (uw > 0.7)).astype(float).where(rng.notna(), np.nan)

def _slope_sign_neg(price, osc, n):
    """+1 if osc 63d-slope < 0."""
    osl = _rolling_slope(osc, n)
    return (osl < 0).astype(float).where(osl.notna(), np.nan)

def _count_5osc_neg_slope(close, volume, high, low):
    parts = [_slope_sign_neg(close, _rsi_wilder(close, 14), QDAYS), _slope_sign_neg(close, _macd_line(close, 12, 26), QDAYS), _slope_sign_neg(close, _obv(close, volume), QDAYS), _slope_sign_neg(close, _stoch_k(high, low, close, 14), QDAYS), _slope_sign_neg(close, _mfi(high, low, close, volume, 14), QDAYS)]
    return sum((p.fillna(0) for p in parts))

def f32_divd_376_rsi_div_confirmed_within_5d_drop_3pct_d1(close: pd.Series) -> pd.Series:
    """+1 (held at confirm bar) when RSI 21d-shift-div fired 5 bars ago AND price has since dropped >= 3%."""
    return _div_confirmed_within(close, _rsi_wilder(close, 14), MDAYS, WDAYS, 0.03).diff()

def f32_divd_377_rsi_div_confirmed_within_21d_drop_5pct_d1(close: pd.Series) -> pd.Series:
    """+1 when RSI 21d-shift-div fired 21 bars ago AND price has since dropped >= 5%."""
    return _div_confirmed_within(close, _rsi_wilder(close, 14), MDAYS, MDAYS, 0.05).diff()

def f32_divd_378_macdline_div_confirmed_within_5d_drop_3pct_d1(close: pd.Series) -> pd.Series:
    """+1 when MACD-line 21d-shift-div fired 5 bars ago AND price has since dropped >= 3%."""
    return _div_confirmed_within(close, _macd_line(close, 12, 26), MDAYS, WDAYS, 0.03).diff()

def f32_divd_379_obv_div_confirmed_within_21d_drop_5pct_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when OBV 21d-shift-div fired 21 bars ago AND price has since dropped >= 5%."""
    return _div_confirmed_within(close, _obv(close, volume), MDAYS, MDAYS, 0.05).diff()

def f32_divd_380_rsi_div_failed_within_21d_rise_3pct_d1(close: pd.Series) -> pd.Series:
    """+1 when RSI 21d-shift-div fired 21 bars ago AND price has since RISEN >= 3% (failed div)."""
    return _div_failed_within(close, _rsi_wilder(close, 14), MDAYS, MDAYS, 0.03).diff()

def f32_divd_381_macdline_div_failed_within_21d_rise_3pct_d1(close: pd.Series) -> pd.Series:
    """+1 when MACD-line 21d-shift-div fired 21 bars ago AND price has since risen >= 3% (failed div)."""
    return _div_failed_within(close, _macd_line(close, 12, 26), MDAYS, MDAYS, 0.03).diff()

def f32_divd_382_obv_div_failed_within_21d_rise_3pct_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """+1 when OBV 21d-shift-div fired 21 bars ago AND price has since risen >= 3% (failed div)."""
    return _div_failed_within(close, _obv(close, volume), MDAYS, MDAYS, 0.03).diff()

def f32_divd_383_rsi_div_confirmation_rate_252d_d1(close: pd.Series) -> pd.Series:
    """Confirmation rate: count of 21d-confirmed-with-5%-drop / count of all RSI div events, trailing 252d."""
    confirmed = _div_confirmed_within(close, _rsi_wilder(close, 14), MDAYS, MDAYS, 0.05).rolling(YDAYS, min_periods=QDAYS).sum()
    all_div = _shift_div_bearish(close, _rsi_wilder(close, 14), MDAYS).fillna(0).shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(confirmed, all_div).diff()

def f32_divd_384_rsi_div_failure_rate_252d_d1(close: pd.Series) -> pd.Series:
    """Failure rate: count of 21d-failed-with-3%-rise / count of all RSI div events, trailing 252d."""
    failed = _div_failed_within(close, _rsi_wilder(close, 14), MDAYS, MDAYS, 0.03).rolling(YDAYS, min_periods=QDAYS).sum()
    all_div = _shift_div_bearish(close, _rsi_wilder(close, 14), MDAYS).fillna(0).shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(failed, all_div).diff()

def f32_divd_385_macdline_div_confirmation_rate_252d_d1(close: pd.Series) -> pd.Series:
    """MACD-line div confirmation rate, trailing 252d (5% drop within 21d after div)."""
    confirmed = _div_confirmed_within(close, _macd_line(close, 12, 26), MDAYS, MDAYS, 0.05).rolling(YDAYS, min_periods=QDAYS).sum()
    all_div = _shift_div_bearish(close, _macd_line(close, 12, 26), MDAYS).fillna(0).shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(confirmed, all_div).diff()

def f32_divd_386_obv_div_confirmation_rate_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV div confirmation rate, trailing 252d."""
    confirmed = _div_confirmed_within(close, _obv(close, volume), MDAYS, MDAYS, 0.05).rolling(YDAYS, min_periods=QDAYS).sum()
    all_div = _shift_div_bearish(close, _obv(close, volume), MDAYS).fillna(0).shift(MDAYS).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(confirmed, all_div).diff()

def f32_divd_387_rsi_div_followed_by_5d_higher_high_indicator_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 when RSI 21d-shift-div fired 5 bars ago AND today's high > the div-bar's high (failed)."""
    flag = _shift_div_bearish(close, _rsi_wilder(close, 14), MDAYS).fillna(0)
    flag_then = flag.shift(WDAYS).fillna(0)
    high_then = high.shift(WDAYS)
    return ((flag_then == 1) & (high > high_then)).astype(float).diff()

def f32_divd_388_rsi_div_followed_by_5d_lower_low_indicator_d1(close: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when RSI 21d-shift-div fired 5 bars ago AND today's low < the div-bar's low (confirmed)."""
    flag = _shift_div_bearish(close, _rsi_wilder(close, 14), MDAYS).fillna(0)
    flag_then = flag.shift(WDAYS).fillna(0)
    low_then = low.shift(WDAYS)
    return ((flag_then == 1) & (low < low_then)).astype(float).diff()

def f32_divd_389_rsi_div_5d_followup_close_change_pct_d1(close: pd.Series) -> pd.Series:
    """At each bar: if RSI div fired 5 bars ago, the % change in close since; else NaN (held forward)."""
    flag = _shift_div_bearish(close, _rsi_wilder(close, 14), MDAYS).fillna(0)
    flag_then = flag.shift(WDAYS).fillna(0)
    pct_change = close / close.shift(WDAYS) - 1.0
    return pct_change.where(flag_then == 1, np.nan).ffill().diff()

def f32_divd_390_rsi_div_21d_followup_close_change_pct_d1(close: pd.Series) -> pd.Series:
    """At each bar: if RSI div fired 21 bars ago, the % change in close since (held forward)."""
    flag = _shift_div_bearish(close, _rsi_wilder(close, 14), MDAYS).fillna(0)
    flag_then = flag.shift(MDAYS).fillna(0)
    pct_change = close / close.shift(MDAYS) - 1.0
    return pct_change.where(flag_then == 1, np.nan).ffill().diff()

def f32_divd_391_rsi_div_bars_to_1st_most_recent_252d_d1(close: pd.Series) -> pd.Series:
    """Bars-back-to-1st-most-recent RSI 21d-shift-div in trailing 252d."""
    flag = _shift_div_bearish(close, _rsi_wilder(close, 14), MDAYS)
    return _nth_most_recent_event_offset(flag, 1, YDAYS).diff()

def f32_divd_392_rsi_div_bars_to_2nd_most_recent_252d_d1(close: pd.Series) -> pd.Series:
    """Bars-back-to-2nd-most-recent RSI 21d-shift-div in trailing 252d."""
    flag = _shift_div_bearish(close, _rsi_wilder(close, 14), MDAYS)
    return _nth_most_recent_event_offset(flag, 2, YDAYS).diff()

def f32_divd_393_rsi_div_bars_to_3rd_most_recent_252d_d1(close: pd.Series) -> pd.Series:
    """Bars-back-to-3rd-most-recent RSI 21d-shift-div in trailing 252d."""
    flag = _shift_div_bearish(close, _rsi_wilder(close, 14), MDAYS)
    return _nth_most_recent_event_offset(flag, 3, YDAYS).diff()

def f32_divd_394_rsi_div_gap_1st_to_2nd_252d_d1(close: pd.Series) -> pd.Series:
    """Bars between 1st and 2nd most-recent RSI 21d-shift-div in trailing 252d."""
    flag = _shift_div_bearish(close, _rsi_wilder(close, 14), MDAYS)
    o1 = _nth_most_recent_event_offset(flag, 1, YDAYS)
    o2 = _nth_most_recent_event_offset(flag, 2, YDAYS)
    return (o2 - o1).diff()

def f32_divd_395_rsi_div_gap_2nd_to_3rd_252d_d1(close: pd.Series) -> pd.Series:
    """Bars between 2nd and 3rd most-recent RSI 21d-shift-div in trailing 252d."""
    flag = _shift_div_bearish(close, _rsi_wilder(close, 14), MDAYS)
    o2 = _nth_most_recent_event_offset(flag, 2, YDAYS)
    o3 = _nth_most_recent_event_offset(flag, 3, YDAYS)
    return (o3 - o2).diff()

def f32_divd_396_macdline_div_bars_to_1st_most_recent_252d_d1(close: pd.Series) -> pd.Series:
    """Bars-back-to-1st-most-recent MACD-line 21d-shift-div in trailing 252d."""
    flag = _shift_div_bearish(close, _macd_line(close, 12, 26), MDAYS)
    return _nth_most_recent_event_offset(flag, 1, YDAYS).diff()

def f32_divd_397_macdline_div_bars_to_2nd_most_recent_252d_d1(close: pd.Series) -> pd.Series:
    """Bars-back-to-2nd-most-recent MACD-line 21d-shift-div in trailing 252d."""
    flag = _shift_div_bearish(close, _macd_line(close, 12, 26), MDAYS)
    return _nth_most_recent_event_offset(flag, 2, YDAYS).diff()

def f32_divd_398_obv_div_bars_to_1st_most_recent_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars-back-to-1st-most-recent OBV 21d-shift-div in trailing 252d."""
    flag = _shift_div_bearish(close, _obv(close, volume), MDAYS)
    return _nth_most_recent_event_offset(flag, 1, YDAYS).diff()

def f32_divd_399_obv_div_bars_to_3rd_most_recent_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars-back-to-3rd-most-recent OBV 21d-shift-div in trailing 252d."""
    flag = _shift_div_bearish(close, _obv(close, volume), MDAYS)
    return _nth_most_recent_event_offset(flag, 3, YDAYS).diff()

def f32_divd_400_rsi_div_3_events_in_63d_indicator_d1(close: pd.Series) -> pd.Series:
    """+1 when 3+ RSI 21d-shift-div events occurred in trailing 63d (cluster signal)."""
    flag = _shift_div_bearish(close, _rsi_wilder(close, 14), MDAYS).fillna(0)
    return (flag.rolling(QDAYS, min_periods=MDAYS).sum() >= 3).astype(float).diff()

def f32_divd_401_rsi_div_magnitude_slope_21d_d1(close: pd.Series) -> pd.Series:
    """21d slope of |RSI 63d-slope-div-magnitude| — positive = divergence intensifying."""
    ps = _rolling_slope(_safe_log(close), QDAYS)
    osl = _rolling_slope(_rolling_zscore(_rsi_wilder(close, 14), QDAYS), QDAYS)
    mag = (ps - osl).abs()
    return _rolling_slope(mag, MDAYS).diff()

def f32_divd_402_rsi_div_magnitude_slope_63d_d1(close: pd.Series) -> pd.Series:
    """63d slope of |RSI 63d-slope-div-magnitude|."""
    ps = _rolling_slope(_safe_log(close), QDAYS)
    osl = _rolling_slope(_rolling_zscore(_rsi_wilder(close, 14), QDAYS), QDAYS)
    mag = (ps - osl).abs()
    return _rolling_slope(mag, QDAYS).diff()

def f32_divd_403_macdline_div_magnitude_slope_21d_d1(close: pd.Series) -> pd.Series:
    """21d slope of |MACD-line 63d-slope-div-magnitude|."""
    ps = _rolling_slope(_safe_log(close), QDAYS)
    osl = _rolling_slope(_rolling_zscore(_macd_line(close, 12, 26), QDAYS), QDAYS)
    mag = (ps - osl).abs()
    return _rolling_slope(mag, MDAYS).diff()

def f32_divd_404_obv_div_magnitude_slope_21d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d slope of |OBV 63d-slope-div-magnitude|."""
    ps = _rolling_slope(_safe_log(close), QDAYS)
    osl = _rolling_slope(_rolling_zscore(_obv(close, volume), QDAYS), QDAYS)
    mag = (ps - osl).abs()
    return _rolling_slope(mag, MDAYS).diff()

def f32_divd_405_rsi_div_magnitude_half_life_estimate_63d_d1(close: pd.Series) -> pd.Series:
    """Half-life estimate: -ln(2) / regression-slope of log(|div_mag|+eps) on time over 63d."""
    ps = _rolling_slope(_safe_log(close), QDAYS)
    osl = _rolling_slope(_rolling_zscore(_rsi_wilder(close, 14), QDAYS), QDAYS)
    mag = (ps - osl).abs() + 1e-12
    log_mag = np.log(mag)
    slope = _rolling_slope(log_mag, QDAYS)
    return _safe_div(-np.log(2.0), slope).diff()

def f32_divd_406_rsi_div_count_decay_rate_21d_d1(close: pd.Series) -> pd.Series:
    """21d change in (rolling 63d RSI div count) — declining = events dying off."""
    flag = _shift_div_bearish(close, _rsi_wilder(close, 14), MDAYS).fillna(0)
    cnt = flag.rolling(QDAYS, min_periods=MDAYS).sum()
    return (cnt - cnt.shift(MDAYS)).diff()

def f32_divd_407_obv_div_count_decay_rate_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d change in (rolling 252d OBV div count)."""
    flag = _shift_div_bearish(close, _obv(close, volume), MDAYS).fillna(0)
    cnt = flag.rolling(YDAYS, min_periods=QDAYS).sum()
    return (cnt - cnt.shift(QDAYS)).diff()

def f32_divd_408_rsi_div_magnitude_acceleration_21d_d1(close: pd.Series) -> pd.Series:
    """Slope-of-slope of |RSI div magnitude| over 21d — acceleration."""
    ps = _rolling_slope(_safe_log(close), QDAYS)
    osl = _rolling_slope(_rolling_zscore(_rsi_wilder(close, 14), QDAYS), QDAYS)
    mag = (ps - osl).abs()
    s = _rolling_slope(mag, MDAYS)
    return _rolling_slope(s, MDAYS).diff()

def f32_divd_409_rsi_div_magnitude_pct_change_21d_d1(close: pd.Series) -> pd.Series:
    """21-day percentage change of |RSI div magnitude| — decay/growth %."""
    ps = _rolling_slope(_safe_log(close), QDAYS)
    osl = _rolling_slope(_rolling_zscore(_rsi_wilder(close, 14), QDAYS), QDAYS)
    mag = (ps - osl).abs() + 1e-12
    return mag.pct_change(MDAYS).diff()

def f32_divd_410_rsi_div_magnitude_pct_change_63d_d1(close: pd.Series) -> pd.Series:
    """63-day percentage change of |RSI div magnitude|."""
    ps = _rolling_slope(_safe_log(close), QDAYS)
    osl = _rolling_slope(_rolling_zscore(_rsi_wilder(close, 14), QDAYS), QDAYS)
    mag = (ps - osl).abs() + 1e-12
    return mag.pct_change(QDAYS).diff()

def f32_divd_411_bb_squeeze_indicator_20d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when Bollinger Bands(20,2) are inside Keltner Channels(20, 2×ATR) (classic squeeze)."""
    _, ubb, lbb = _bb(close, 20, 2.0)
    ku = _keltner_upper(high, low, close, 20, 2.0)
    kl = _keltner_lower(high, low, close, 20, 2.0)
    return ((ubb < ku) & (lbb > kl)).astype(float).where(ubb.notna() & ku.notna(), np.nan).diff()

def f32_divd_412_bb_squeeze_duration_consec_bars_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive-bar streak in BB squeeze (longer = more potential energy)."""
    sqz = _bb_squeeze_flag(close, high, low).fillna(0).astype(int)
    grp = (sqz == 0).cumsum()
    return sqz.groupby(grp).cumsum().astype(float).diff()

def f32_divd_413_bb_squeeze_release_event_indicator_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 on bar where BB squeeze ended (squeeze=1 prior, squeeze=0 today)."""
    sqz = _bb_squeeze_flag(close, high, low).fillna(0)
    return ((sqz.shift(1) == 1) & (sqz == 0)).astype(float).where(sqz.notna() & sqz.shift(1).notna(), np.nan).diff()

def f32_divd_414_bb_squeeze_release_with_negative_close_event_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when BB squeeze released AND today's close < prior close (bearish release)."""
    sqz = _bb_squeeze_flag(close, high, low).fillna(0)
    rel = ((sqz.shift(1) == 1) & (sqz == 0)).astype(float)
    bear = (close < close.shift(1)).astype(float)
    return (rel * bear).where(rel.notna(), np.nan).diff()

def f32_divd_415_bb_walk_upper_band_streak_d1(close: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where close > upper Bollinger Band(20, 2) — walking the upper band."""
    _, ubb, _ = _bb(close, 20, 2.0)
    flag = (close > ubb).astype(int).fillna(0)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float).diff()

def f32_divd_416_bb_walk_upper_band_count_63d_d1(close: pd.Series) -> pd.Series:
    """Count of trailing-63d bars where close > upper BB(20, 2)."""
    _, ubb, _ = _bb(close, 20, 2.0)
    return (close > ubb).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f32_divd_417_bb_width_pct_rank_252d_d1(close: pd.Series) -> pd.Series:
    """Percentile rank of BB width(20, 2) in trailing 252d. Low rank = tight bands."""
    return _pct_rank(_bb_width(close, 20, 2.0), YDAYS).diff()

def f32_divd_418_keltner_upper_break_event_indicator_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when close crosses above Keltner upper(20, 2×ATR) for the first time (event)."""
    ku = _keltner_upper(high, low, close, 20, 2.0)
    above = (close > ku).astype(int).fillna(0)
    return ((above == 1) & (above.shift(1) == 0)).astype(float).where(ku.notna() & above.shift(1).notna(), np.nan).diff()

def f32_divd_419_keltner_upper_break_count_252d_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of trailing-252d Keltner-upper break events."""
    ku = _keltner_upper(high, low, close, 20, 2.0)
    above = (close > ku).astype(int).fillna(0)
    return ((above == 1) & (above.shift(1) == 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f32_divd_420_keltner_upper_walk_streak_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where close > Keltner upper band."""
    ku = _keltner_upper(high, low, close, 20, 2.0)
    flag = (close > ku).astype(int).fillna(0)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float).diff()

def f32_divd_421_bb_squeeze_x_close_at_252d_high_indicator_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when BB squeeze active AND close within 1% of 252d max."""
    sqz = _bb_squeeze_flag(close, high, low)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (sqz * near).where(sqz.notna() & near.notna(), np.nan).diff()

def f32_divd_422_bb_walk_upper_x_rsi_div_indicator_d1(close: pd.Series) -> pd.Series:
    """+1 when close > BB upper AND RSI 63d bearish slope-div fires (extension + div)."""
    _, ubb, _ = _bb(close, 20, 2.0)
    above = (close > ubb).astype(float)
    div = _slope_div_sign(close, _rsi_wilder(close, 14), QDAYS)
    return (above * div).where(above.notna() & div.notna(), np.nan).diff()

def f32_divd_423_keltner_break_failed_indicator_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when close was > Keltner upper 5 bars ago BUT < Keltner upper today (failed break)."""
    ku = _keltner_upper(high, low, close, 20, 2.0)
    was_above = (close.shift(WDAYS) > ku.shift(WDAYS)).astype(float)
    not_above = (close <= ku).astype(float)
    return (was_above * not_above).where(ku.notna() & ku.shift(WDAYS).notna(), np.nan).diff()

def f32_divd_424_bb_width_contraction_event_indicator_d1(close: pd.Series) -> pd.Series:
    """+1 on bar where BB width(20) hits a new 63d-trailing-min (tightest in 63d)."""
    w = _bb_width(close, 20, 2.0)
    return (w == w.rolling(QDAYS, min_periods=MDAYS).min()).astype(float).where(w.notna(), np.nan).diff()

def f32_divd_425_donchian_high_break_failed_indicator_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 when close > 21d-trailing-max(high) 5 bars ago BUT close < 21d-trailing-max(high) today (failed Donchian break)."""
    dhigh = high.rolling(MDAYS, min_periods=WDAYS).max()
    was_above = (close.shift(WDAYS) > dhigh.shift(WDAYS)).astype(float)
    not_above = (close <= dhigh).astype(float)
    return (was_above * not_above).where(dhigh.notna() & dhigh.shift(WDAYS).notna(), np.nan).diff()

def f32_divd_426_doji_at_252d_high_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when bar is a doji AND close within 1% of 252d max (indecision at top)."""
    doji = _is_doji(open, close, high, low)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (doji * near).where(doji.notna() & near.notna(), np.nan).diff()

def f32_divd_427_doji_at_1260d_high_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when bar is a doji AND close within 2% of 1260d max (indecision at secular peak)."""
    doji = _is_doji(open, close, high, low)
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return (doji * near).where(doji.notna() & near.notna(), np.nan).diff()

def f32_divd_428_shooting_star_at_252d_high_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when shooting star at 252d-high bar."""
    ss = _is_shooting_star(open, close, high, low)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (ss * near).where(ss.notna() & near.notna(), np.nan).diff()

def f32_divd_429_shooting_star_at_1260d_high_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when shooting star at 1260d-high bar."""
    ss = _is_shooting_star(open, close, high, low)
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return (ss * near).where(ss.notna() & near.notna(), np.nan).diff()

def f32_divd_430_hanging_man_at_252d_high_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when hanging-man pattern at 252d-high bar."""
    hm = _is_hanging_man(open, close, high, low)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (hm * near).where(hm.notna() & near.notna(), np.nan).diff()

def f32_divd_431_bearish_engulfing_at_252d_high_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 when bearish engulfing AND close within 1% of 252d max."""
    be = _is_bearish_engulfing(open, close)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (be * near).where(be.notna() & near.notna(), np.nan).diff()

def f32_divd_432_bearish_engulfing_at_1260d_high_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 when bearish engulfing AND close within 2% of 1260d max."""
    be = _is_bearish_engulfing(open, close)
    near = (close >= close.rolling(DDAYS_5Y, min_periods=YDAYS).max() * 0.98).astype(float)
    return (be * near).where(be.notna() & near.notna(), np.nan).diff()

def f32_divd_433_3_black_crows_at_252d_high_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series) -> pd.Series:
    """+1 when 3 black crows fires AND close within 1% of 252d max."""
    bc = _is_3_black_crows(open, close)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (bc * near).where(bc.notna() & near.notna(), np.nan).diff()

def f32_divd_434_gravestone_doji_at_252d_high_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when gravestone doji at 252d-high bar (classic top signal)."""
    gd = _is_gravestone_doji(open, close, high, low)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (gd * near).where(gd.notna() & near.notna(), np.nan).diff()

def f32_divd_435_outside_down_bar_at_252d_high_indicator_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when today's high > prior high AND low < prior low AND close < prior close AND near 252d high."""
    outside_down = ((high > high.shift(1)) & (low < low.shift(1)) & (close < close.shift(1))).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (outside_down * near).where(close.notna() & near.notna(), np.nan).diff()

def f32_divd_436_inside_bar_at_252d_high_indicator_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when today's high < prior high AND low > prior low (inside bar) AND close near 252d high."""
    inside = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (inside * near).where(close.notna() & near.notna(), np.nan).diff()

def f32_divd_437_wide_range_bar_at_252d_high_indicator_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when today's range > 1.5 × 21d-mean AND close near 252d high."""
    rng = high - low
    wide = (rng > 1.5 * rng.rolling(MDAYS, min_periods=WDAYS).mean()).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (wide * near).where(close.notna() & near.notna(), np.nan).diff()

def f32_divd_438_long_upper_wick_at_252d_high_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when upper-wick > 50% of bar range AND close near 252d high (rejection)."""
    rng = (high - low).replace(0, np.nan)
    uw = (high - pd.concat([open, close], axis=1).max(axis=1)) / rng
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return ((uw > 0.5).astype(float) * near).where(rng.notna() & near.notna(), np.nan).diff()

def f32_divd_439_pin_bar_top_at_252d_high_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when upper-wick > 2× body AND close near 252d high (pin-bar rejection at top)."""
    body = (close - open).abs()
    uw = high - pd.concat([open, close], axis=1).max(axis=1)
    pin = (uw > 2.0 * body).astype(float)
    near = (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99).astype(float)
    return (pin * near).where(close.notna() & near.notna(), np.nan).diff()

def f32_divd_440_marubozu_bullish_at_252d_high_indicator_d1(open: pd.Series, close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when bar is bullish marubozu (body >= 95% of range, close > open) AND near 252d high (final push)."""
    rng = (high - low).replace(0, np.nan)
    body = (close - open) / rng
    return ((body >= 0.95) & (close >= close.rolling(YDAYS, min_periods=QDAYS).max() * 0.99)).astype(float).where(rng.notna(), np.nan).diff()

def f32_divd_441_rsi_first_to_flip_negative_in_5osc_indicator_d1(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when RSI flipped to negative slope today AND none of MACD/OBV/Stoch%K/MFI had flipped negative
    within prior 5 bars (RSI was first-mover in 5-oscillator panel)."""
    rsi_neg = _slope_sign_neg(close, _rsi_wilder(close, 14), QDAYS)
    macd_neg = _slope_sign_neg(close, _macd_line(close, 12, 26), QDAYS)
    obv_neg = _slope_sign_neg(close, _obv(close, volume), QDAYS)
    sk_neg = _slope_sign_neg(close, _stoch_k(high, low, close, 14), QDAYS)
    mfi_neg = _slope_sign_neg(close, _mfi(high, low, close, volume, 14), QDAYS)
    rsi_new = ((rsi_neg == 1) & (rsi_neg.shift(1) == 0)).astype(float)
    others_recent = ((macd_neg.rolling(WDAYS, min_periods=1).max() == 1) | (obv_neg.rolling(WDAYS, min_periods=1).max() == 1) | (sk_neg.rolling(WDAYS, min_periods=1).max() == 1) | (mfi_neg.rolling(WDAYS, min_periods=1).max() == 1)).astype(float)
    return (rsi_new * (1 - others_recent.shift(1).fillna(0))).diff()

def f32_divd_442_macdline_first_to_flip_negative_in_5osc_indicator_d1(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when MACD-line flipped to negative slope today AND others (RSI/OBV/Stoch/MFI) hadn't flipped within 5 prior bars."""
    rsi_neg = _slope_sign_neg(close, _rsi_wilder(close, 14), QDAYS)
    macd_neg = _slope_sign_neg(close, _macd_line(close, 12, 26), QDAYS)
    obv_neg = _slope_sign_neg(close, _obv(close, volume), QDAYS)
    sk_neg = _slope_sign_neg(close, _stoch_k(high, low, close, 14), QDAYS)
    mfi_neg = _slope_sign_neg(close, _mfi(high, low, close, volume, 14), QDAYS)
    macd_new = ((macd_neg == 1) & (macd_neg.shift(1) == 0)).astype(float)
    others_recent = ((rsi_neg.rolling(WDAYS, min_periods=1).max() == 1) | (obv_neg.rolling(WDAYS, min_periods=1).max() == 1) | (sk_neg.rolling(WDAYS, min_periods=1).max() == 1) | (mfi_neg.rolling(WDAYS, min_periods=1).max() == 1)).astype(float)
    return (macd_new * (1 - others_recent.shift(1).fillna(0))).diff()

def f32_divd_443_obv_first_to_flip_negative_in_5osc_indicator_d1(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when OBV flipped to negative slope today AND others hadn't within prior 5 bars."""
    rsi_neg = _slope_sign_neg(close, _rsi_wilder(close, 14), QDAYS)
    macd_neg = _slope_sign_neg(close, _macd_line(close, 12, 26), QDAYS)
    obv_neg = _slope_sign_neg(close, _obv(close, volume), QDAYS)
    sk_neg = _slope_sign_neg(close, _stoch_k(high, low, close, 14), QDAYS)
    mfi_neg = _slope_sign_neg(close, _mfi(high, low, close, volume, 14), QDAYS)
    obv_new = ((obv_neg == 1) & (obv_neg.shift(1) == 0)).astype(float)
    others_recent = ((rsi_neg.rolling(WDAYS, min_periods=1).max() == 1) | (macd_neg.rolling(WDAYS, min_periods=1).max() == 1) | (sk_neg.rolling(WDAYS, min_periods=1).max() == 1) | (mfi_neg.rolling(WDAYS, min_periods=1).max() == 1)).astype(float)
    return (obv_new * (1 - others_recent.shift(1).fillna(0))).diff()

def f32_divd_444_count_oscillators_negative_slope_5osc_d1(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Integer count (0..5) of 5 oscillators currently with negative 63d slope."""
    return _count_5osc_neg_slope(close, volume, high, low).diff()

def f32_divd_445_bars_since_first_oscillator_flipped_negative_d1(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since the FIRST oscillator (of 5) flipped to negative slope (min bars-since across 5)."""
    flips = []
    for osc in [_rsi_wilder(close, 14), _macd_line(close, 12, 26), _obv(close, volume), _stoch_k(high, low, close, 14), _mfi(high, low, close, volume, 14)]:
        s = _rolling_slope(osc, QDAYS)
        flip = ((s.shift(1) > 0) & (s <= 0)).astype(float)
        flips.append(_bars_since_true(flip))
    df = pd.concat([f.rename(f'f{i}') for i, f in enumerate(flips)], axis=1)
    return df.min(axis=1).diff()

def f32_divd_446_bars_since_3_oscillators_flipped_negative_d1(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since the moment when AT LEAST 3 of 5 osc were simultaneously in negative-slope regime."""
    cnt = _count_5osc_neg_slope(close, volume, high, low)
    flag = (cnt >= 3).astype(float)
    return _bars_since_true(flag).diff()

def f32_divd_447_first_flip_to_5_flipped_count_252d_d1(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars in trailing 252d where ALL 5 oscillators were simultaneously in negative slope."""
    cnt = _count_5osc_neg_slope(close, volume, high, low)
    return (cnt == 5).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f32_divd_448_order_index_first_flipped_5osc_d1(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Integer (0..4) indicating which of 5 osc most recently flipped first:
    0=RSI, 1=MACD, 2=OBV, 3=Stoch%K, 4=MFI."""
    flips = []
    for osc in [_rsi_wilder(close, 14), _macd_line(close, 12, 26), _obv(close, volume), _stoch_k(high, low, close, 14), _mfi(high, low, close, volume, 14)]:
        s = _rolling_slope(osc, QDAYS)
        flip = ((s.shift(1) > 0) & (s <= 0)).astype(float)
        flips.append(_bars_since_true(flip))
    df = pd.concat([f.rename(f'f{i}') for i, f in enumerate(flips)], axis=1)
    df.columns = list(range(5))
    return df.fillna(np.inf).idxmin(axis=1).where(df.notna().any(axis=1), np.nan).astype(float).diff()

def f32_divd_449_all_5_oscillators_negative_slope_indicator_d1(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """+1 when ALL 5 oscillators are currently in negative 63d-slope regime simultaneously."""
    cnt = _count_5osc_neg_slope(close, volume, high, low)
    return (cnt == 5).astype(float).diff()

def f32_divd_450_all_5_oscillators_negative_slope_streak_d1(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where all 5 osc negative-slope."""
    cnt = _count_5osc_neg_slope(close, volume, high, low)
    flag = (cnt == 5).astype(int)
    grp = (flag == 0).cumsum()
    return flag.groupby(grp).cumsum().astype(float).diff()
DIVERGENCE_DETECTION_D1_REGISTRY_376_450 = {'f32_divd_376_rsi_div_confirmed_within_5d_drop_3pct_d1': {'inputs': ['close'], 'func': f32_divd_376_rsi_div_confirmed_within_5d_drop_3pct_d1}, 'f32_divd_377_rsi_div_confirmed_within_21d_drop_5pct_d1': {'inputs': ['close'], 'func': f32_divd_377_rsi_div_confirmed_within_21d_drop_5pct_d1}, 'f32_divd_378_macdline_div_confirmed_within_5d_drop_3pct_d1': {'inputs': ['close'], 'func': f32_divd_378_macdline_div_confirmed_within_5d_drop_3pct_d1}, 'f32_divd_379_obv_div_confirmed_within_21d_drop_5pct_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_379_obv_div_confirmed_within_21d_drop_5pct_d1}, 'f32_divd_380_rsi_div_failed_within_21d_rise_3pct_d1': {'inputs': ['close'], 'func': f32_divd_380_rsi_div_failed_within_21d_rise_3pct_d1}, 'f32_divd_381_macdline_div_failed_within_21d_rise_3pct_d1': {'inputs': ['close'], 'func': f32_divd_381_macdline_div_failed_within_21d_rise_3pct_d1}, 'f32_divd_382_obv_div_failed_within_21d_rise_3pct_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_382_obv_div_failed_within_21d_rise_3pct_d1}, 'f32_divd_383_rsi_div_confirmation_rate_252d_d1': {'inputs': ['close'], 'func': f32_divd_383_rsi_div_confirmation_rate_252d_d1}, 'f32_divd_384_rsi_div_failure_rate_252d_d1': {'inputs': ['close'], 'func': f32_divd_384_rsi_div_failure_rate_252d_d1}, 'f32_divd_385_macdline_div_confirmation_rate_252d_d1': {'inputs': ['close'], 'func': f32_divd_385_macdline_div_confirmation_rate_252d_d1}, 'f32_divd_386_obv_div_confirmation_rate_252d_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_386_obv_div_confirmation_rate_252d_d1}, 'f32_divd_387_rsi_div_followed_by_5d_higher_high_indicator_d1': {'inputs': ['close', 'high'], 'func': f32_divd_387_rsi_div_followed_by_5d_higher_high_indicator_d1}, 'f32_divd_388_rsi_div_followed_by_5d_lower_low_indicator_d1': {'inputs': ['close', 'low'], 'func': f32_divd_388_rsi_div_followed_by_5d_lower_low_indicator_d1}, 'f32_divd_389_rsi_div_5d_followup_close_change_pct_d1': {'inputs': ['close'], 'func': f32_divd_389_rsi_div_5d_followup_close_change_pct_d1}, 'f32_divd_390_rsi_div_21d_followup_close_change_pct_d1': {'inputs': ['close'], 'func': f32_divd_390_rsi_div_21d_followup_close_change_pct_d1}, 'f32_divd_391_rsi_div_bars_to_1st_most_recent_252d_d1': {'inputs': ['close'], 'func': f32_divd_391_rsi_div_bars_to_1st_most_recent_252d_d1}, 'f32_divd_392_rsi_div_bars_to_2nd_most_recent_252d_d1': {'inputs': ['close'], 'func': f32_divd_392_rsi_div_bars_to_2nd_most_recent_252d_d1}, 'f32_divd_393_rsi_div_bars_to_3rd_most_recent_252d_d1': {'inputs': ['close'], 'func': f32_divd_393_rsi_div_bars_to_3rd_most_recent_252d_d1}, 'f32_divd_394_rsi_div_gap_1st_to_2nd_252d_d1': {'inputs': ['close'], 'func': f32_divd_394_rsi_div_gap_1st_to_2nd_252d_d1}, 'f32_divd_395_rsi_div_gap_2nd_to_3rd_252d_d1': {'inputs': ['close'], 'func': f32_divd_395_rsi_div_gap_2nd_to_3rd_252d_d1}, 'f32_divd_396_macdline_div_bars_to_1st_most_recent_252d_d1': {'inputs': ['close'], 'func': f32_divd_396_macdline_div_bars_to_1st_most_recent_252d_d1}, 'f32_divd_397_macdline_div_bars_to_2nd_most_recent_252d_d1': {'inputs': ['close'], 'func': f32_divd_397_macdline_div_bars_to_2nd_most_recent_252d_d1}, 'f32_divd_398_obv_div_bars_to_1st_most_recent_252d_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_398_obv_div_bars_to_1st_most_recent_252d_d1}, 'f32_divd_399_obv_div_bars_to_3rd_most_recent_252d_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_399_obv_div_bars_to_3rd_most_recent_252d_d1}, 'f32_divd_400_rsi_div_3_events_in_63d_indicator_d1': {'inputs': ['close'], 'func': f32_divd_400_rsi_div_3_events_in_63d_indicator_d1}, 'f32_divd_401_rsi_div_magnitude_slope_21d_d1': {'inputs': ['close'], 'func': f32_divd_401_rsi_div_magnitude_slope_21d_d1}, 'f32_divd_402_rsi_div_magnitude_slope_63d_d1': {'inputs': ['close'], 'func': f32_divd_402_rsi_div_magnitude_slope_63d_d1}, 'f32_divd_403_macdline_div_magnitude_slope_21d_d1': {'inputs': ['close'], 'func': f32_divd_403_macdline_div_magnitude_slope_21d_d1}, 'f32_divd_404_obv_div_magnitude_slope_21d_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_404_obv_div_magnitude_slope_21d_d1}, 'f32_divd_405_rsi_div_magnitude_half_life_estimate_63d_d1': {'inputs': ['close'], 'func': f32_divd_405_rsi_div_magnitude_half_life_estimate_63d_d1}, 'f32_divd_406_rsi_div_count_decay_rate_21d_d1': {'inputs': ['close'], 'func': f32_divd_406_rsi_div_count_decay_rate_21d_d1}, 'f32_divd_407_obv_div_count_decay_rate_63d_d1': {'inputs': ['close', 'volume'], 'func': f32_divd_407_obv_div_count_decay_rate_63d_d1}, 'f32_divd_408_rsi_div_magnitude_acceleration_21d_d1': {'inputs': ['close'], 'func': f32_divd_408_rsi_div_magnitude_acceleration_21d_d1}, 'f32_divd_409_rsi_div_magnitude_pct_change_21d_d1': {'inputs': ['close'], 'func': f32_divd_409_rsi_div_magnitude_pct_change_21d_d1}, 'f32_divd_410_rsi_div_magnitude_pct_change_63d_d1': {'inputs': ['close'], 'func': f32_divd_410_rsi_div_magnitude_pct_change_63d_d1}, 'f32_divd_411_bb_squeeze_indicator_20d_d1': {'inputs': ['close', 'high', 'low'], 'func': f32_divd_411_bb_squeeze_indicator_20d_d1}, 'f32_divd_412_bb_squeeze_duration_consec_bars_d1': {'inputs': ['close', 'high', 'low'], 'func': f32_divd_412_bb_squeeze_duration_consec_bars_d1}, 'f32_divd_413_bb_squeeze_release_event_indicator_d1': {'inputs': ['close', 'high', 'low'], 'func': f32_divd_413_bb_squeeze_release_event_indicator_d1}, 'f32_divd_414_bb_squeeze_release_with_negative_close_event_d1': {'inputs': ['close', 'high', 'low'], 'func': f32_divd_414_bb_squeeze_release_with_negative_close_event_d1}, 'f32_divd_415_bb_walk_upper_band_streak_d1': {'inputs': ['close'], 'func': f32_divd_415_bb_walk_upper_band_streak_d1}, 'f32_divd_416_bb_walk_upper_band_count_63d_d1': {'inputs': ['close'], 'func': f32_divd_416_bb_walk_upper_band_count_63d_d1}, 'f32_divd_417_bb_width_pct_rank_252d_d1': {'inputs': ['close'], 'func': f32_divd_417_bb_width_pct_rank_252d_d1}, 'f32_divd_418_keltner_upper_break_event_indicator_d1': {'inputs': ['close', 'high', 'low'], 'func': f32_divd_418_keltner_upper_break_event_indicator_d1}, 'f32_divd_419_keltner_upper_break_count_252d_d1': {'inputs': ['close', 'high', 'low'], 'func': f32_divd_419_keltner_upper_break_count_252d_d1}, 'f32_divd_420_keltner_upper_walk_streak_d1': {'inputs': ['close', 'high', 'low'], 'func': f32_divd_420_keltner_upper_walk_streak_d1}, 'f32_divd_421_bb_squeeze_x_close_at_252d_high_indicator_d1': {'inputs': ['close', 'high', 'low'], 'func': f32_divd_421_bb_squeeze_x_close_at_252d_high_indicator_d1}, 'f32_divd_422_bb_walk_upper_x_rsi_div_indicator_d1': {'inputs': ['close'], 'func': f32_divd_422_bb_walk_upper_x_rsi_div_indicator_d1}, 'f32_divd_423_keltner_break_failed_indicator_d1': {'inputs': ['close', 'high', 'low'], 'func': f32_divd_423_keltner_break_failed_indicator_d1}, 'f32_divd_424_bb_width_contraction_event_indicator_d1': {'inputs': ['close'], 'func': f32_divd_424_bb_width_contraction_event_indicator_d1}, 'f32_divd_425_donchian_high_break_failed_indicator_d1': {'inputs': ['close', 'high'], 'func': f32_divd_425_donchian_high_break_failed_indicator_d1}, 'f32_divd_426_doji_at_252d_high_indicator_d1': {'inputs': ['open', 'close', 'high', 'low'], 'func': f32_divd_426_doji_at_252d_high_indicator_d1}, 'f32_divd_427_doji_at_1260d_high_indicator_d1': {'inputs': ['open', 'close', 'high', 'low'], 'func': f32_divd_427_doji_at_1260d_high_indicator_d1}, 'f32_divd_428_shooting_star_at_252d_high_indicator_d1': {'inputs': ['open', 'close', 'high', 'low'], 'func': f32_divd_428_shooting_star_at_252d_high_indicator_d1}, 'f32_divd_429_shooting_star_at_1260d_high_indicator_d1': {'inputs': ['open', 'close', 'high', 'low'], 'func': f32_divd_429_shooting_star_at_1260d_high_indicator_d1}, 'f32_divd_430_hanging_man_at_252d_high_indicator_d1': {'inputs': ['open', 'close', 'high', 'low'], 'func': f32_divd_430_hanging_man_at_252d_high_indicator_d1}, 'f32_divd_431_bearish_engulfing_at_252d_high_indicator_d1': {'inputs': ['open', 'close', 'high'], 'func': f32_divd_431_bearish_engulfing_at_252d_high_indicator_d1}, 'f32_divd_432_bearish_engulfing_at_1260d_high_indicator_d1': {'inputs': ['open', 'close', 'high'], 'func': f32_divd_432_bearish_engulfing_at_1260d_high_indicator_d1}, 'f32_divd_433_3_black_crows_at_252d_high_indicator_d1': {'inputs': ['open', 'close', 'high'], 'func': f32_divd_433_3_black_crows_at_252d_high_indicator_d1}, 'f32_divd_434_gravestone_doji_at_252d_high_indicator_d1': {'inputs': ['open', 'close', 'high', 'low'], 'func': f32_divd_434_gravestone_doji_at_252d_high_indicator_d1}, 'f32_divd_435_outside_down_bar_at_252d_high_indicator_d1': {'inputs': ['close', 'high', 'low'], 'func': f32_divd_435_outside_down_bar_at_252d_high_indicator_d1}, 'f32_divd_436_inside_bar_at_252d_high_indicator_d1': {'inputs': ['close', 'high', 'low'], 'func': f32_divd_436_inside_bar_at_252d_high_indicator_d1}, 'f32_divd_437_wide_range_bar_at_252d_high_indicator_d1': {'inputs': ['close', 'high', 'low'], 'func': f32_divd_437_wide_range_bar_at_252d_high_indicator_d1}, 'f32_divd_438_long_upper_wick_at_252d_high_indicator_d1': {'inputs': ['open', 'close', 'high', 'low'], 'func': f32_divd_438_long_upper_wick_at_252d_high_indicator_d1}, 'f32_divd_439_pin_bar_top_at_252d_high_indicator_d1': {'inputs': ['open', 'close', 'high', 'low'], 'func': f32_divd_439_pin_bar_top_at_252d_high_indicator_d1}, 'f32_divd_440_marubozu_bullish_at_252d_high_indicator_d1': {'inputs': ['open', 'close', 'high', 'low'], 'func': f32_divd_440_marubozu_bullish_at_252d_high_indicator_d1}, 'f32_divd_441_rsi_first_to_flip_negative_in_5osc_indicator_d1': {'inputs': ['close', 'volume', 'high', 'low'], 'func': f32_divd_441_rsi_first_to_flip_negative_in_5osc_indicator_d1}, 'f32_divd_442_macdline_first_to_flip_negative_in_5osc_indicator_d1': {'inputs': ['close', 'volume', 'high', 'low'], 'func': f32_divd_442_macdline_first_to_flip_negative_in_5osc_indicator_d1}, 'f32_divd_443_obv_first_to_flip_negative_in_5osc_indicator_d1': {'inputs': ['close', 'volume', 'high', 'low'], 'func': f32_divd_443_obv_first_to_flip_negative_in_5osc_indicator_d1}, 'f32_divd_444_count_oscillators_negative_slope_5osc_d1': {'inputs': ['close', 'volume', 'high', 'low'], 'func': f32_divd_444_count_oscillators_negative_slope_5osc_d1}, 'f32_divd_445_bars_since_first_oscillator_flipped_negative_d1': {'inputs': ['close', 'volume', 'high', 'low'], 'func': f32_divd_445_bars_since_first_oscillator_flipped_negative_d1}, 'f32_divd_446_bars_since_3_oscillators_flipped_negative_d1': {'inputs': ['close', 'volume', 'high', 'low'], 'func': f32_divd_446_bars_since_3_oscillators_flipped_negative_d1}, 'f32_divd_447_first_flip_to_5_flipped_count_252d_d1': {'inputs': ['close', 'volume', 'high', 'low'], 'func': f32_divd_447_first_flip_to_5_flipped_count_252d_d1}, 'f32_divd_448_order_index_first_flipped_5osc_d1': {'inputs': ['close', 'volume', 'high', 'low'], 'func': f32_divd_448_order_index_first_flipped_5osc_d1}, 'f32_divd_449_all_5_oscillators_negative_slope_indicator_d1': {'inputs': ['close', 'volume', 'high', 'low'], 'func': f32_divd_449_all_5_oscillators_negative_slope_indicator_d1}, 'f32_divd_450_all_5_oscillators_negative_slope_streak_d1': {'inputs': ['close', 'volume', 'high', 'low'], 'func': f32_divd_450_all_5_oscillators_negative_slope_streak_d1}}