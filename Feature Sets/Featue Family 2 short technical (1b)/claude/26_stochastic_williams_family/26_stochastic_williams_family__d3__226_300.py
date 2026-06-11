"""stochastic_williams_family d3 features 226-300 — Pipeline 1b-technical.

75 distinct "statistical / cycle / advanced" hypotheses. Themes:
Ehlers cycle indicators (simplified) (226-233),
ConnorsRSI individual components (234-241),
Range / percentile based (242-251),
Cross dynamics filters (252-261),
Multi-timeframe alignment (262-271),
Statistical signal quality (272-281),
Composites / aggregates (282-300).

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers — no cross-file imports.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504


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


def _bars_since_true(mask: pd.Series) -> pd.Series:
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


def _streak_true(mask: pd.Series) -> pd.Series:
    arr = mask.astype(bool).to_numpy()
    out = np.zeros(arr.shape, dtype=float)
    c = 0
    for i in range(arr.size):
        c = c + 1 if arr[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=mask.index)


def _ema(s, span, min_periods=None):
    if min_periods is None:
        min_periods = max(span // 2, 2)
    return s.ewm(span=span, adjust=False, min_periods=min_periods).mean()


def _stoch_k(high, low, close, n, smooth_k=1):
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    k = 100.0 * _safe_div(close - ll, hh - ll)
    if smooth_k > 1:
        k = k.rolling(smooth_k, min_periods=max(smooth_k // 2, 1)).mean()
    return k


def _williams_r(high, low, close, n):
    ll = low.rolling(n, min_periods=max(n // 3, 2)).min()
    hh = high.rolling(n, min_periods=max(n // 3, 2)).max()
    return -100.0 * _safe_div(hh - close, hh - ll)


def _rsi(close, n=14):
    delta = close.diff()
    up = delta.clip(lower=0)
    dn = (-delta).clip(lower=0)
    au = up.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    ad = dn.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    rs = _safe_div(au, ad)
    return 100.0 - 100.0 / (1.0 + rs)


def _pct_rank(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return s.rolling(window, min_periods=min_periods).apply(_rk, raw=True)


def _ehlers_super_smoother(s, period=10):
    """Ehlers 2-pole IIR (Butterworth) smoother. Recursive — uses only past values."""
    a1 = np.exp(-1.414 * np.pi / period)
    b1 = 2.0 * a1 * np.cos(1.414 * np.pi / period)
    c2 = b1
    c3 = -a1 * a1
    c1 = 1.0 - c2 - c3
    arr = s.to_numpy()
    out = np.full(arr.shape, np.nan)
    for i in range(arr.size):
        if i < 2 or np.isnan(arr[i]) or np.isnan(arr[i-1]):
            if not np.isnan(arr[i]):
                out[i] = arr[i]
            continue
        prev1 = out[i-1] if not np.isnan(out[i-1]) else arr[i-1]
        prev2 = out[i-2] if not np.isnan(out[i-2]) else arr[i-2] if not np.isnan(arr[i-2]) else arr[i]
        out[i] = c1 * (arr[i] + arr[i-1]) / 2.0 + c2 * prev1 + c3 * prev2
    return pd.Series(out, index=s.index)


def _laguerre_filter(s, gamma=0.4):
    """Ehlers 4-pole Laguerre filter (recursive)."""
    arr = s.to_numpy()
    L0 = np.zeros(arr.shape); L1 = np.zeros(arr.shape)
    L2 = np.zeros(arr.shape); L3 = np.zeros(arr.shape)
    out = np.full(arr.shape, np.nan)
    for i in range(arr.size):
        if np.isnan(arr[i]):
            continue
        pL0 = L0[i-1] if i > 0 else arr[i]
        pL1 = L1[i-1] if i > 0 else arr[i]
        pL2 = L2[i-1] if i > 0 else arr[i]
        pL3 = L3[i-1] if i > 0 else arr[i]
        L0[i] = (1.0 - gamma) * arr[i] + gamma * pL0
        L1[i] = -gamma * L0[i] + pL0 + gamma * pL1
        L2[i] = -gamma * L1[i] + pL1 + gamma * pL2
        L3[i] = -gamma * L2[i] + pL2 + gamma * pL3
        out[i] = (L0[i] + 2.0 * L1[i] + 2.0 * L2[i] + L3[i]) / 6.0
    return pd.Series(out, index=s.index)


def _highpass_filter(s, n=20):
    """Simple Ehlers single-pole high-pass: s - lowpass."""
    return s - _ema(s, n)


def _zlema(s, n):
    lag = int((n - 1) // 2)
    adj = 2.0 * s - s.shift(lag)
    return _ema(adj, n)


def _rsi_on_series(s, n):
    """Generic RSI on any series."""
    delta = s.diff()
    up = delta.clip(lower=0)
    dn = (-delta).clip(lower=0)
    au = up.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    ad = dn.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean()
    rs = _safe_div(au, ad)
    return 100.0 - 100.0 / (1.0 + rs)


def _streak_signed(close):
    """Signed consecutive-streak length (positive when up, negative when down)."""
    dp = close.diff()
    sign = np.sign(dp)
    out = np.zeros(close.size)
    cur = 0.0
    s_arr = sign.to_numpy()
    for i in range(close.size):
        sg = s_arr[i]
        if np.isnan(sg) or sg == 0:
            cur = 0.0
        elif cur >= 0 and sg > 0:
            cur = cur + 1.0
        elif cur <= 0 and sg < 0:
            cur = cur - 1.0
        else:
            cur = sg
        out[i] = cur
    return pd.Series(out, index=close.index)


def _connors_rsi(close, n_rsi=3, n_streak=2, n_rank=100):
    r1 = _rsi_on_series(close, n_rsi)
    streak = _streak_signed(close)
    r2 = _rsi_on_series(streak, n_streak)
    ret = close.pct_change()
    pr = _pct_rank(ret, n_rank, min_periods=max(n_rank // 4, 5)) * 100.0
    return (r1 + r2 + pr) / 3.0


def _stc(close, fast=23, slow=50, cycle=10, factor=0.5):
    macd = _ema(close, fast) - _ema(close, slow)
    ll = macd.rolling(cycle, min_periods=max(cycle // 3, 2)).min()
    hh = macd.rolling(cycle, min_periods=max(cycle // 3, 2)).max()
    k1 = 100.0 * _safe_div(macd - ll, hh - ll)
    d1 = k1.ewm(alpha=factor, adjust=False, min_periods=max(cycle // 2, 2)).mean()
    ll2 = d1.rolling(cycle, min_periods=max(cycle // 3, 2)).min()
    hh2 = d1.rolling(cycle, min_periods=max(cycle // 3, 2)).max()
    k2 = 100.0 * _safe_div(d1 - ll2, hh2 - ll2)
    return k2.ewm(alpha=factor, adjust=False, min_periods=max(cycle // 2, 2)).mean()


def _awesome_osc(high, low):
    mp = (high + low) / 2.0
    return mp.rolling(5, min_periods=3).mean() - mp.rolling(34, min_periods=11).mean()


def _swma4(s):
    return (s + 2.0 * s.shift(1) + 2.0 * s.shift(2) + s.shift(3)) / 6.0


def _rvi(open_s, high, low, close, n=10):
    num = _swma4(close - open_s).rolling(n, min_periods=max(n // 3, 2)).mean()
    den = _swma4(high - low).rolling(n, min_periods=max(n // 3, 2)).mean()
    return _safe_div(num, den)


def _inverse_fisher(s, scale=0.1):
    x = (scale * s).clip(-10.0, 10.0)
    e = np.exp(2.0 * x)
    return (e - 1.0) / (e + 1.0)


def _all_basket_signals(open_s, high, low, close):
    """Return a dict of indicator series across modern + classical oscillators."""
    k = _stoch_k(high, low, close, 14)
    wr = _williams_r(high, low, close, 14)
    stc = _stc(close)
    ao = _awesome_osc(high, low)
    crsi = _connors_rsi(close)
    rvi = _rvi(open_s, high, low, close, 10)
    m = close.rolling(20, min_periods=7).mean()
    sd = close.rolling(20, min_periods=7).std()
    pctb = _safe_div(close - (m - 2.0 * sd), 4.0 * sd)
    ift_s = _inverse_fisher(k - 50.0, scale=0.1)
    ift_w = _inverse_fisher(wr + 50.0, scale=0.1)
    return {
        'k': k, 'wr': wr, 'stc': stc, 'ao': ao, 'crsi': crsi, 'rvi': rvi,
        'pctb': pctb, 'ift_s': ift_s, 'ift_w': ift_w,
    }


def _resample_stoch(high, low, close, agg_n, k_n=14):
    """Stoch K computed on agg_n-bar aggregated OHLC bars (right-anchored rolling agg, PIT-clean).
    Maps aggregated K back to daily index via forward-fill of last agg value."""
    # Right-anchored rolling aggregate per bar
    agg_high = high.rolling(agg_n, min_periods=max(agg_n // 2, 2)).max()
    agg_low = low.rolling(agg_n, min_periods=max(agg_n // 2, 2)).min()
    agg_close = close  # close-of-bar is current close
    # Stoch on aggregated bars: lookback k_n agg-bars = k_n * agg_n daily bars
    full_n = k_n * agg_n
    ll = agg_low.rolling(full_n, min_periods=max(full_n // 3, agg_n)).min()
    hh = agg_high.rolling(full_n, min_periods=max(full_n // 3, agg_n)).max()
    return 100.0 * _safe_div(agg_close - ll, hh - ll)


# ============================================================
# Ehlers cycle indicators (226-233)
# ============================================================


def f26_stwf_226_ehlers_super_smoother_stoch_14_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stoch %K(14) smoothed with Ehlers SuperSmoother (2-pole IIR, period 10)."""
    return (_ehlers_super_smoother(_stoch_k(high, low, close, 14), period=10)).diff().diff().diff()


def f26_stwf_227_laguerre_filter_stoch_06_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stoch %K(14) smoothed with Ehlers 4-pole Laguerre filter (gamma=0.4)."""
    return (_laguerre_filter(_stoch_k(high, low, close, 14), gamma=0.4)).diff().diff().diff()


def f26_stwf_228_ehlers_decycler_oscillator_14_d3(close: pd.Series) -> pd.Series:
    """Ehlers Decycler Oscillator: close - lowpass(close, n=20) = highpass component."""
    return (_highpass_filter(close, n=20)).diff().diff().diff()


def f26_stwf_229_ehlers_zero_lag_ema_stoch_14_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ehlers ZLEMA applied to stoch %K(14)."""
    return (_zlema(_stoch_k(high, low, close, 14), 9)).diff().diff().diff()


def f26_stwf_230_ehlers_smoothed_adaptive_momentum_d3(close: pd.Series) -> pd.Series:
    """Adaptive momentum: 10d momentum * adaptive smoothing factor (1/(1+|momentum_zscore|))."""
    mom = close - close.shift(10)
    z = _rolling_zscore(mom, QDAYS, min_periods=MDAYS).abs()
    alpha = 1.0 / (1.0 + z.fillna(0))
    return (mom * alpha).diff().diff().diff()


def f26_stwf_231_ehlers_homodyne_period_proxy_d3(close: pd.Series) -> pd.Series:
    """Simplified homodyne instantaneous period proxy: 2*pi / |angle of complex pair (I+jQ)|.
    I = close - close.shift(3); Q = (close - close.shift(6)). Period bounded [6, 50]."""
    I = (close - close.shift(3))
    Q = (close - close.shift(6))
    ang = np.arctan2(Q, I).abs()
    period = (2.0 * np.pi) / ang.replace(0, np.nan)
    return (period.clip(6.0, 50.0)).diff().diff().diff()


def f26_stwf_232_ehlers_instantaneous_trendline_d3(close: pd.Series) -> pd.Series:
    """Ehlers Instantaneous Trendline (simplified): (close + 2*close.shift(1) + 2*close.shift(2) + close.shift(3))/6."""
    return (_swma4(close)).diff().diff().diff()


def f26_stwf_233_ehlers_mama_smoothed_stoch_proxy_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """MESA Adaptive MA proxy applied to stoch K: alpha = 0.5/(1 + phase_change).
    phase_change approximated by rolling 5d std of K normalized by 21d std."""
    k = _stoch_k(high, low, close, 14)
    sd_s = k.rolling(5, min_periods=3).std()
    sd_l = k.rolling(MDAYS, min_periods=WDAYS).std()
    phase = _safe_div(sd_s, sd_l).fillna(1.0).clip(0.1, 5.0)
    alpha = (0.5 / (1.0 + phase)).clip(0.05, 0.5)
    arr = k.to_numpy()
    a_arr = alpha.to_numpy()
    out = np.full(arr.shape, np.nan)
    prev = np.nan
    for i in range(arr.size):
        v = arr[i]; a = a_arr[i]
        if np.isnan(prev):
            if not np.isnan(v) and not np.isnan(a):
                prev = v; out[i] = v
        else:
            if not np.isnan(v) and not np.isnan(a):
                prev = prev + a * (v - prev); out[i] = prev
            else:
                out[i] = prev
    return (pd.Series(out, index=k.index)).diff().diff().diff()


def f26_stwf_234_rsi_streak_2_value_d3(close: pd.Series) -> pd.Series:
    """RSI(2) applied to consecutive signed-streak series — pure streak-RSI component."""
    return (_rsi_on_series(_streak_signed(close), 2)).diff().diff().diff()


def f26_stwf_235_rsi_streak_consecutive_up_count_d3(close: pd.Series) -> pd.Series:
    """Current consecutive up-day streak length."""
    s = _streak_signed(close)
    return (s.where(s > 0, 0.0)).diff().diff().diff()


def f26_stwf_236_rsi_streak_consecutive_down_count_d3(close: pd.Series) -> pd.Series:
    """Current consecutive down-day streak length (positive value = days down)."""
    s = _streak_signed(close)
    return ((-s).where(s < 0, 0.0)).diff().diff().diff()


def f26_stwf_237_rsi_streak_above_90_state_d3(close: pd.Series) -> pd.Series:
    """1 if Streak-RSI(2) > 90 — extreme streak-momentum OB."""
    r2 = _rsi_on_series(_streak_signed(close), 2)
    return ((r2 > 90.0).astype(float).where(r2.notna(), np.nan)).diff().diff().diff()


def f26_stwf_238_percent_rank_returns_100_value_d3(close: pd.Series) -> pd.Series:
    """Percent rank of 1d return within trailing 100 bars."""
    ret = close.pct_change()
    return (_pct_rank(ret, 100, min_periods=25) * 100.0).diff().diff().diff()


def f26_stwf_239_percent_rank_returns_above_90_state_d3(close: pd.Series) -> pd.Series:
    """1 if percent rank of today's return in trailing 100 bars > 90."""
    ret = close.pct_change()
    pr = _pct_rank(ret, 100, min_periods=25) * 100.0
    return ((pr > 90.0).astype(float).where(pr.notna(), np.nan)).diff().diff().diff()


def f26_stwf_240_percent_rank_returns_dwell_above_80_63_d3(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars where return-percentile-rank > 80 — extreme-return dwell."""
    ret = close.pct_change()
    pr = _pct_rank(ret, 100, min_periods=25) * 100.0
    return ((pr > 80.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(pr.notna(), np.nan)).diff().diff().diff()


def f26_stwf_241_crsi_components_individual_zscore_252_d3(close: pd.Series) -> pd.Series:
    """Mean of z-scores of the 3 CRSI components over 252d — distribution-normalized basket score."""
    r1 = _rsi_on_series(close, 3)
    r2 = _rsi_on_series(_streak_signed(close), 2)
    pr = _pct_rank(close.pct_change(), 100, min_periods=25) * 100.0
    z1 = _rolling_zscore(r1, YDAYS, min_periods=QDAYS)
    z2 = _rolling_zscore(r2, YDAYS, min_periods=QDAYS)
    z3 = _rolling_zscore(pr, YDAYS, min_periods=QDAYS)
    return ((z1 + z2 + z3) / 3.0).diff().diff().diff()


def f26_stwf_242_percentile_rank_close_21d_d3(close: pd.Series) -> pd.Series:
    """Percentile rank of close in trailing 21 bars — monthly close position."""
    return (_pct_rank(close, MDAYS, min_periods=WDAYS) * 100.0).diff().diff().diff()


def f26_stwf_243_percentile_rank_close_63d_d3(close: pd.Series) -> pd.Series:
    """Percentile rank of close in trailing 63 bars — quarterly close position."""
    return (_pct_rank(close, QDAYS, min_periods=MDAYS) * 100.0).diff().diff().diff()


def f26_stwf_244_percentile_rank_high_252d_d3(high: pd.Series) -> pd.Series:
    """Percentile rank of daily high in trailing 252 bars — annual high position."""
    return (_pct_rank(high, YDAYS, min_periods=QDAYS) * 100.0).diff().diff().diff()


def f26_stwf_245_median_close_pos_in_21d_range_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - 21d median(close)) / (21d range) — position relative to median."""
    med = close.rolling(MDAYS, min_periods=WDAYS).median()
    rng = high.rolling(MDAYS, min_periods=WDAYS).max() - low.rolling(MDAYS, min_periods=WDAYS).min()
    return (_safe_div(close - med, rng)).diff().diff().diff()


def f26_stwf_246_iqr_normalized_close_position_63_d3(close: pd.Series) -> pd.Series:
    """(close - 63d median) / IQR(close, 63) — robust z-score-like measure."""
    med = close.rolling(QDAYS, min_periods=MDAYS).median()
    q3 = close.rolling(QDAYS, min_periods=MDAYS).quantile(0.75)
    q1 = close.rolling(QDAYS, min_periods=MDAYS).quantile(0.25)
    iqr = (q3 - q1).replace(0, np.nan)
    return (_safe_div(close - med, iqr)).diff().diff().diff()


def f26_stwf_247_range_position_volume_weighted_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average of close-position-in-range over 21d."""
    ll = low.rolling(MDAYS, min_periods=WDAYS).min()
    hh = high.rolling(MDAYS, min_periods=WDAYS).max()
    pos = _safe_div(close - ll, hh - ll)
    num = (pos * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    den = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    return (_safe_div(num, den)).diff().diff().diff()


def f26_stwf_248_percentile_above_q95_state_63d_d3(close: pd.Series) -> pd.Series:
    """1 if close is above 63d 95th percentile — quarterly distribution OB."""
    q = close.rolling(QDAYS, min_periods=MDAYS).quantile(0.95)
    return ((close > q).astype(float).where(q.notna(), np.nan)).diff().diff().diff()


def f26_stwf_249_close_in_q90_range_above_state_252d_d3(close: pd.Series) -> pd.Series:
    """1 if close in top decile of 252d distribution — annual extreme."""
    q = close.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return ((close > q).astype(float).where(q.notna(), np.nan)).diff().diff().diff()


def f26_stwf_250_percentile_consecutive_streak_above_q80_63d_d3(close: pd.Series) -> pd.Series:
    """Current consecutive bars with close > 63d 80th percentile — distribution-OB streak."""
    q = close.rolling(QDAYS, min_periods=MDAYS).quantile(0.80)
    return (_streak_true(close > q).where(q.notna(), np.nan)).diff().diff().diff()


def f26_stwf_251_percentile_band_decay_velocity_63_d3(close: pd.Series) -> pd.Series:
    """Decay of close-percentile rank: pct_rank(close, 21) - pct_rank(close, 21).shift(63)."""
    pr = _pct_rank(close, MDAYS, min_periods=WDAYS)
    return (pr - pr.shift(QDAYS)).diff().diff().diff()


def f26_stwf_252_stoch_ema_minus_stoch_sma_14_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """EMA(14)(K) - SMA(14)(K) — smoothing-method divergence (EMA leads SMA in trend)."""
    k = _stoch_k(high, low, close, 14)
    return (_ema(k, 14) - k.rolling(14, min_periods=5).mean()).diff().diff().diff()


def f26_stwf_253_stoch_smoothed_signal_3bar_confirm_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K < D for 3 consecutive bars — bearish cross requires 3-bar confirmation."""
    k = _stoch_k(high, low, close, 14)
    d = k.rolling(3, min_periods=2).mean()
    below = k < d
    streak = _streak_true(below)
    # 1 only on the bar streak first reaches 3
    return (((streak >= 3) & (streak.shift(1) < 3)).astype(float).where(k.notna(), np.nan)).diff().diff().diff()


def f26_stwf_254_stoch_cross_with_min_distance_filter_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K crosses below D AND |K - D| > 5 on the bar before cross — distance-filtered cross."""
    k = _stoch_k(high, low, close, 14)
    d = k.rolling(3, min_periods=2).mean()
    diff = k - d
    cross = (diff.shift(1) > 0) & (diff <= 0)
    return ((cross & (diff.shift(1).abs() > 5.0)).astype(float).where(diff.notna(), np.nan)).diff().diff().diff()


def f26_stwf_255_stoch_cross_with_extreme_filter_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K crosses below D while K(prev) > 80 — extreme-OB-only cross."""
    k = _stoch_k(high, low, close, 14)
    d = k.rolling(3, min_periods=2).mean()
    diff = k - d
    cross = (diff.shift(1) > 0) & (diff <= 0)
    return ((cross & (k.shift(1) > 80.0)).astype(float).where(diff.notna(), np.nan)).diff().diff().diff()


def f26_stwf_256_stoch_cross_with_volume_confirm_d3(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if K crosses below D AND volume > 1.5 * 21d-mean(volume) — volume-confirmed bearish cross."""
    k = _stoch_k(high, low, close, 14)
    d = k.rolling(3, min_periods=2).mean()
    diff = k - d
    cross = (diff.shift(1) > 0) & (diff <= 0)
    vol_high = volume > 1.5 * volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return ((cross & vol_high).astype(float).where(diff.notna(), np.nan)).diff().diff().diff()


def f26_stwf_257_stoch_pivot_count_in_ob_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of local maxima of K (K[t-1] > K[t-2] and K[t-1] > K[t]) where K[t-1] > 80, past 63 bars."""
    k = _stoch_k(high, low, close, 14)
    is_peak = (k.shift(1) > k.shift(2)) & (k.shift(1) > k) & (k.shift(1) > 80.0)
    return (is_peak.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().where(k.notna(), np.nan)).diff().diff().diff()


def f26_stwf_258_stoch_pivot_to_pivot_amplitude_decay_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """K-peak amplitude decay: most recent 21d K-peak / 21d K-peak from 42 bars ago."""
    k = _stoch_k(high, low, close, 14)
    pmax_now = k.rolling(MDAYS, min_periods=WDAYS).max()
    pmax_old = pmax_now.shift(MDAYS * 2)
    return (_safe_div(pmax_now, pmax_old)).diff().diff().diff()


def f26_stwf_259_stoch_zigzag_compression_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if (63d K-range) / (252d K-range) < 0.4 — zigzag compression of oscillator."""
    k = _stoch_k(high, low, close, 14)
    r63 = k.rolling(QDAYS, min_periods=MDAYS).max() - k.rolling(QDAYS, min_periods=MDAYS).min()
    r252 = k.rolling(YDAYS, min_periods=QDAYS).max() - k.rolling(YDAYS, min_periods=QDAYS).min()
    return ((_safe_div(r63, r252) < 0.4).astype(float).where(r252.notna(), np.nan)).diff().diff().diff()


def f26_stwf_260_stoch_hook_with_confirmation_filter_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K-D bearish cross at K>80 AND K stays below D for next 2 bars (using shift, no peek)."""
    k = _stoch_k(high, low, close, 14)
    d = k.rolling(3, min_periods=2).mean()
    diff = k - d
    # bar t-2: cross fired. bars t-1, t: confirmed below
    cross_t2 = ((diff.shift(3) > 0) & (diff.shift(2) <= 0) & (k.shift(2) > 80.0))
    below_t1 = diff.shift(1) <= 0
    below_t = diff <= 0
    return ((cross_t2 & below_t1 & below_t).astype(float).where(diff.notna(), np.nan)).diff().diff().diff()


def f26_stwf_261_stoch_failed_cross_count_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bullish K-D crosses that reverted (bearish cross fired within 5 bars), past 63 bars."""
    k = _stoch_k(high, low, close, 14)
    d = k.rolling(3, min_periods=2).mean()
    diff = k - d
    bu = ((diff.shift(1) <= 0) & (diff > 0)).astype(float)
    be = ((diff.shift(1) > 0) & (diff <= 0)).astype(float)
    # for bu at bar t, fail if any be in bars t+1..t+5 — encoded via lookback:
    # bu_5_ago through bu_1_ago, with be in past 5 bars (excluding bu bar)
    fail = pd.Series(0.0, index=k.index)
    for lag in range(1, 6):
        bu_lag = bu.shift(lag)
        be_in_window = be.rolling(lag, min_periods=1).sum() > 0
        fail = fail + ((bu_lag > 0) & be_in_window).astype(float) * (1.0 / 5.0)
    return (fail.rolling(QDAYS, min_periods=MDAYS).sum().where(diff.notna(), np.nan)).diff().diff().diff()


def f26_stwf_262_weekly_stoch_overbought_aggregate_5d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K(14) computed on 5d-aggregated bars > 80 — weekly-tf OB state."""
    k = _resample_stoch(high, low, close, agg_n=5, k_n=14)
    return ((k > 80.0).astype(float).where(k.notna(), np.nan)).diff().diff().diff()


def f26_stwf_263_monthly_stoch_overbought_aggregate_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K(14) on 21d-aggregated bars > 80 — monthly-tf OB state."""
    k = _resample_stoch(high, low, close, agg_n=21, k_n=14)
    return ((k > 80.0).astype(float).where(k.notna(), np.nan)).diff().diff().diff()


def f26_stwf_264_quarterly_stoch_overbought_aggregate_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if K(14) on 63d-aggregated bars > 80 — quarterly-tf OB state."""
    k = _resample_stoch(high, low, close, agg_n=63, k_n=14)
    return ((k > 80.0).astype(float).where(k.notna(), np.nan)).diff().diff().diff()


def f26_stwf_265_cross_timeframe_stoch_dispersion_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std of K(14) across daily / weekly / monthly aggregated bars — multi-tf dispersion."""
    k_d = _stoch_k(high, low, close, 14)
    k_w = _resample_stoch(high, low, close, agg_n=5, k_n=14)
    k_m = _resample_stoch(high, low, close, agg_n=21, k_n=14)
    df = pd.concat([k_d.rename(0), k_w.rename(1), k_m.rename(2)], axis=1)
    return (df.std(axis=1)).diff().diff().diff()


def f26_stwf_266_cross_timeframe_oscillator_alignment_score_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of timeframes (daily, weekly, monthly) where K > 50 — bullish-alignment score."""
    k_d = _stoch_k(high, low, close, 14)
    k_w = _resample_stoch(high, low, close, agg_n=5, k_n=14)
    k_m = _resample_stoch(high, low, close, agg_n=21, k_n=14)
    cnt = ((k_d > 50.0).astype(float).fillna(0)
           + (k_w > 50.0).astype(float).fillna(0)
           + (k_m > 50.0).astype(float).fillna(0))
    return (cnt.where(k_d.notna(), np.nan)).diff().diff().diff()


def f26_stwf_267_overbought_persistence_across_timeframes_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars where ALL of {daily, weekly, monthly} K(14) > 80 — multi-tf OB persistence."""
    k_d = _stoch_k(high, low, close, 14)
    k_w = _resample_stoch(high, low, close, agg_n=5, k_n=14)
    k_m = _resample_stoch(high, low, close, agg_n=21, k_n=14)
    all_ob = ((k_d > 80.0) & (k_w > 80.0) & (k_m > 80.0)).astype(float)
    return (all_ob.rolling(QDAYS, min_periods=MDAYS).mean().where(k_d.notna(), np.nan)).diff().diff().diff()


def f26_stwf_268_divergence_across_timeframes_count_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of timeframes (daily/weekly/monthly) with bearish K-divergence — multi-tf div count."""
    k_d = _stoch_k(high, low, close, 14)
    k_w = _resample_stoch(high, low, close, agg_n=5, k_n=14)
    k_m = _resample_stoch(high, low, close, agg_n=21, k_n=14)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    div_d = (k_d < k_d.shift(1).rolling(QDAYS, min_periods=MDAYS).max()) & p_new
    div_w = (k_w < k_w.shift(1).rolling(QDAYS, min_periods=MDAYS).max()) & p_new
    div_m = (k_m < k_m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()) & p_new
    cnt = (div_d.astype(float).fillna(0) + div_w.astype(float).fillna(0) + div_m.astype(float).fillna(0))
    return (cnt.where(p_new, np.nan)).diff().diff().diff()


def f26_stwf_269_higher_tf_overbought_short_tf_decline_indicator_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if monthly-K > 80 AND daily-K just exited OB — higher-tf OB + short-tf decline."""
    k_d = _stoch_k(high, low, close, 14)
    k_m = _resample_stoch(high, low, close, agg_n=21, k_n=14)
    daily_exit = (k_d.shift(1) > 80.0) & (k_d <= 80.0)
    return (((k_m > 80.0) & daily_exit).astype(float).where(k_d.notna() & k_m.notna(), np.nan)).diff().diff().diff()


def f26_stwf_270_multi_tf_oscillator_failure_count_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of timeframes with K-D bearish cross in past 5 bars but not in another timeframe — divergent-cross failure."""
    out_total = pd.Series(0.0, index=close.index)
    flags = []
    for agg in (1, 5, 21):
        if agg == 1:
            k = _stoch_k(high, low, close, 14)
        else:
            k = _resample_stoch(high, low, close, agg_n=agg, k_n=14)
        d = k.rolling(3, min_periods=2).mean()
        diff = k - d
        be = ((diff.shift(1) > 0) & (diff <= 0)).astype(float).rolling(WDAYS, min_periods=1).sum() > 0
        flags.append(be.astype(float))
    # count timeframes that fired
    total_fired = flags[0] + flags[1] + flags[2]
    # failure: some fired, some didn't (i.e., 1 or 2 fired but not all 3, not 0)
    fail = ((total_fired >= 1) & (total_fired <= 2)).astype(float)
    return (fail.where(close.notna(), np.nan)).diff().diff().diff()


def f26_stwf_271_tf_lead_lag_oscillator_score_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lead/lag: (bars since daily K hit 21d-max) - (bars since monthly K hit 21d-max).
    Positive => monthly led (slower TF peaked first)."""
    k_d = _stoch_k(high, low, close, 14)
    k_m = _resample_stoch(high, low, close, agg_n=21, k_n=14)
    bs_d = _bars_since_true(k_d == k_d.rolling(MDAYS, min_periods=WDAYS).max())
    bs_m = _bars_since_true(k_m == k_m.rolling(MDAYS, min_periods=WDAYS).max())
    return (bs_d - bs_m).diff().diff().diff()


def f26_stwf_272_stoch_autocorrelation_lag_1_21d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of stoch K over 21 bars."""
    k = _stoch_k(high, low, close, 14)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 5:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 3:
            return np.nan
        m = v.mean(); vc = v - m
        den = float((vc * vc).sum())
        if den == 0:
            return (np.nan).diff().diff().diff()
        return float((vc[1:] * vc[:-1]).sum() / den)
    return k.rolling(MDAYS, min_periods=WDAYS).apply(_f, raw=True)


def f26_stwf_273_stoch_autocorrelation_lag_5_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Lag-5 autocorrelation of stoch K over 63 bars — weekly persistence."""
    k = _stoch_k(high, low, close, 14)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 7:
            return np.nan
        m = v.mean(); vc = v - m
        den = float((vc * vc).sum())
        if den == 0:
            return (np.nan).diff().diff().diff()
        return float((vc[5:] * vc[:-5]).sum() / den)
    return k.rolling(QDAYS, min_periods=MDAYS).apply(_f, raw=True)


def f26_stwf_274_stoch_partial_autocorrelation_proxy_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Residual autocorrelation after EMA(5) — partial-AC proxy at lag 1 over 63 bars."""
    k = _stoch_k(high, low, close, 14)
    res = k - _ema(k, 5)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 3:
            return np.nan
        m = v.mean(); vc = v - m
        den = float((vc * vc).sum())
        if den == 0:
            return (np.nan).diff().diff().diff()
        return float((vc[1:] * vc[:-1]).sum() / den)
    return res.rolling(QDAYS, min_periods=MDAYS).apply(_f, raw=True)


def f26_stwf_275_stoch_information_coefficient_with_returns_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d corr(K_lag1, return_today) — IC of yesterday's K vs today's return.
    PIT-clean: uses K.shift(1) (past info) vs current return."""
    k = _stoch_k(high, low, close, 14)
    ret = close.pct_change()
    return (k.shift(1).rolling(QDAYS, min_periods=MDAYS).corr(ret)).diff().diff().diff()


def f26_stwf_276_oscillator_signal_noise_ratio_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Signal/noise: std(EMA5(K)) / std(K - EMA5(K)) — over 63 bars."""
    k = _stoch_k(high, low, close, 14)
    sig = _ema(k, 5)
    noise = k - sig
    return (_safe_div(sig.rolling(QDAYS, min_periods=MDAYS).std(), noise.rolling(QDAYS, min_periods=MDAYS).std())).diff().diff().diff()


def f26_stwf_277_stoch_predictability_zscore_252_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of (rolling 21d lag-1 autocorrelation of K) over 252 bars — predictability index."""
    k = _stoch_k(high, low, close, 14)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 5:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 3:
            return np.nan
        m = v.mean(); vc = v - m
        den = float((vc * vc).sum())
        if den == 0:
            return (np.nan).diff().diff().diff()
        return float((vc[1:] * vc[:-1]).sum() / den)
    ac = k.rolling(MDAYS, min_periods=WDAYS).apply(_f, raw=True)
    return _rolling_zscore(ac, YDAYS, min_periods=QDAYS)


def f26_stwf_278_stoch_entropy_distribution_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Shannon entropy of K-distribution discretized into 10 bins over 63 bars."""
    k = _stoch_k(high, low, close, 14)
    def _ent(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        h, _ = np.histogram(v, bins=10, range=(0.0, 100.0))
        if h.sum() == 0:
            return (np.nan).diff().diff().diff()
        p = h / h.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    return k.rolling(QDAYS, min_periods=MDAYS).apply(_ent, raw=True)


def f26_stwf_279_stoch_innovation_residual_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """K minus EMA(21)(K) — innovation residual."""
    k = _stoch_k(high, low, close, 14)
    return (k - _ema(k, MDAYS)).diff().diff().diff()


def f26_stwf_280_stoch_long_memory_hurst_proxy_63_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Simplified R/S Hurst exponent proxy of K over 63 bars: log(R/S) / log(n)."""
    k = _stoch_k(high, low, close, 14)
    def _hurst(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid] if not valid.all() else w
        if v.size < 10:
            return np.nan
        m = v.mean()
        Y = np.cumsum(v - m)
        R = float(Y.max() - Y.min())
        S = float(v.std())
        if S == 0 or R <= 0:
            return (np.nan).diff().diff().diff()
        return float(np.log(R / S) / np.log(v.size))
    return k.rolling(QDAYS, min_periods=MDAYS).apply(_hurst, raw=True)


def f26_stwf_281_stoch_kurtosis_at_top_state_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d kurtosis of K — only defined when K > 80 (top-regime tail behavior)."""
    k = _stoch_k(high, low, close, 14)
    kt = k.rolling(QDAYS, min_periods=MDAYS).kurt()
    return (kt.where(k > 80.0, np.nan)).diff().diff().diff()


def f26_stwf_282_extended_modern_basket_topping_count_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of OB indicators in {STC>75, AO<0, CRSI>85, RVI<0, BB%B>1, IFT-stoch>0.5, IFT-WR>0.5}."""
    b = _all_basket_signals(open, high, low, close)
    cnt = ((b['stc'] > 75.0).astype(float).fillna(0)
           + (b['ao'] < 0).astype(float).fillna(0)
           + (b['crsi'] > 85.0).astype(float).fillna(0)
           + (b['rvi'] < 0).astype(float).fillna(0)
           + (b['pctb'] > 1.0).astype(float).fillna(0)
           + (b['ift_s'] > 0.5).astype(float).fillna(0)
           + (b['ift_w'] > 0.5).astype(float).fillna(0))
    return (cnt.where(close.notna(), np.nan)).diff().diff().diff()


def f26_stwf_283_count_modern_basket_in_extreme_state_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of basket indicators with z > 2 in 252d distribution — extreme-state breadth."""
    b = _all_basket_signals(open, high, low, close)
    items = [b['stc'], b['ao'], b['crsi'], b['rvi'], b['pctb']]
    cnt = pd.Series(0.0, index=close.index)
    for s in items:
        z = _rolling_zscore(s, YDAYS, min_periods=QDAYS)
        cnt = cnt + (z > 2.0).astype(float).fillna(0)
    return (cnt.where(close.notna(), np.nan)).diff().diff().diff()


def f26_stwf_284_count_modern_basket_recent_exit_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of basket indicators that had an OB exit in past 5 bars."""
    b = _all_basket_signals(open, high, low, close)
    pairs = [(b['stc'], 75.0), (b['crsi'], 85.0), (b['pctb'], 1.0), (b['ift_s'], 0.5), (b['ift_w'], 0.5)]
    cnt = pd.Series(0.0, index=close.index)
    for s, t in pairs:
        ex = ((s.shift(1) > t) & (s <= t)).astype(float).rolling(WDAYS, min_periods=1).sum() > 0
        cnt = cnt + ex.astype(float)
    return (cnt.where(close.notna(), np.nan)).diff().diff().diff()


def f26_stwf_285_count_modern_basket_with_divergence_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of basket indicators showing bearish divergence on current bar (new price high but indicator below prior max)."""
    b = _all_basket_signals(open, high, low, close)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    items = [b['stc'], b['ao'], b['crsi'], b['rvi'], b['k'], b['wr']]
    cnt = pd.Series(0.0, index=close.index)
    for s in items:
        below = s < s.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
        cnt = cnt + (below & p_new).astype(float).fillna(0)
    return (cnt.where(p_new, np.nan)).diff().diff().diff()


def f26_stwf_286_modern_basket_avg_zscore_252_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Average z-score across {STC, AO, CRSI, RVI, BB%B} over 252 bars."""
    b = _all_basket_signals(open, high, low, close)
    items = [b['stc'], b['ao'], b['crsi'], b['rvi'], b['pctb']]
    z_list = [_rolling_zscore(s, YDAYS, min_periods=QDAYS) for s in items]
    return (pd.concat([z.rename(i) for i, z in enumerate(z_list)], axis=1).mean(axis=1)).diff().diff().diff()


def f26_stwf_287_modern_basket_dispersion_zscore_252_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std of z-scores across {STC, AO, CRSI, RVI, BB%B} — basket disagreement."""
    b = _all_basket_signals(open, high, low, close)
    items = [b['stc'], b['ao'], b['crsi'], b['rvi'], b['pctb']]
    z_list = [_rolling_zscore(s, YDAYS, min_periods=QDAYS) for s in items]
    return (pd.concat([z.rename(i) for i, z in enumerate(z_list)], axis=1).std(axis=1)).diff().diff().diff()


def f26_stwf_288_combined_classical_modern_consensus_bearish_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Combined classical (K>80, WR>-20) + modern (STC>75, CRSI>85, BB%B>1) bearish-consensus count."""
    b = _all_basket_signals(open, high, low, close)
    cnt = ((b['k'] > 80.0).astype(float).fillna(0)
           + (b['wr'] > -20.0).astype(float).fillna(0)
           + (b['stc'] > 75.0).astype(float).fillna(0)
           + (b['crsi'] > 85.0).astype(float).fillna(0)
           + (b['pctb'] > 1.0).astype(float).fillna(0))
    return (cnt.where(close.notna(), np.nan)).diff().diff().diff()


def f26_stwf_289_oscillator_universe_breadth_indicator_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative count over 21d of (classical+modern) OB-firings — oscillator-universe breadth."""
    b = _all_basket_signals(open, high, low, close)
    items_thresh = [(b['k'], 80.0, '>'), (b['wr'], -20.0, '>'), (b['stc'], 75.0, '>'),
                    (b['crsi'], 85.0, '>'), (b['pctb'], 1.0, '>'), (b['ift_s'], 0.5, '>'),
                    (b['ift_w'], 0.5, '>'), (b['ao'], 0, '<'), (b['rvi'], 0, '<')]
    daily = pd.Series(0.0, index=close.index)
    for s, t, op in items_thresh:
        if op == '>':
            daily = daily + (s > t).astype(float).fillna(0)
        else:
            daily = daily + (s < t).astype(float).fillna(0)
    return (daily.rolling(MDAYS, min_periods=WDAYS).sum().where(close.notna(), np.nan)).diff().diff().diff()


def f26_stwf_290_oscillator_universe_extreme_count_at_top_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Extended-basket topping count gated to bars where close = 252d-high (terminal-top context)."""
    b = _all_basket_signals(open, high, low, close)
    cnt = ((b['k'] > 80.0).astype(float).fillna(0)
           + (b['stc'] > 75.0).astype(float).fillna(0)
           + (b['crsi'] > 85.0).astype(float).fillna(0)
           + (b['pctb'] > 1.0).astype(float).fillna(0)
           + (b['ift_s'] > 0.5).astype(float).fillna(0))
    at_max = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    return (cnt.where(at_max, np.nan)).diff().diff().diff()


def f26_stwf_291_oscillator_universe_decay_velocity_post_peak_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Decay velocity: (basket OB count 21 bars ago) - (current basket OB count) — positive => fading momentum."""
    b = _all_basket_signals(open, high, low, close)
    cnt = ((b['k'] > 80.0).astype(float).fillna(0)
           + (b['stc'] > 75.0).astype(float).fillna(0)
           + (b['crsi'] > 85.0).astype(float).fillna(0)
           + (b['pctb'] > 1.0).astype(float).fillna(0))
    return (cnt.shift(MDAYS) - cnt).diff().diff().diff()


def f26_stwf_292_oscillator_universe_terminal_pattern_score_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Terminal score = (basket peak count in last 21) + (#exits last 21) — terminal-distribution pattern."""
    b = _all_basket_signals(open, high, low, close)
    pairs = [(b['k'], 80.0), (b['stc'], 75.0), (b['crsi'], 85.0), (b['pctb'], 1.0), (b['ift_s'], 0.5)]
    in_ob = pd.Series(0.0, index=close.index)
    exits = pd.Series(0.0, index=close.index)
    for s, t in pairs:
        in_ob = in_ob + (s > t).astype(float).fillna(0).rolling(MDAYS, min_periods=WDAYS).sum()
        exits = exits + ((s.shift(1) > t) & (s <= t)).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()
    return ((in_ob + exits).where(close.notna(), np.nan)).diff().diff().diff()


def f26_stwf_293_temporal_alignment_oscillator_peaks_63_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Max - min of (bars-since-63d-peak) across basket — alignment of indicator peaks (small = aligned)."""
    b = _all_basket_signals(open, high, low, close)
    items = [b['k'], b['stc'], b['crsi'], b['pctb'], b['ift_s'], b['ift_w']]
    bs_list = []
    for s in items:
        at_max = s == s.rolling(QDAYS, min_periods=MDAYS).max()
        bs_list.append(_bars_since_true(at_max))
    df = pd.concat([b_.rename(i) for i, b_ in enumerate(bs_list)], axis=1)
    return (df.max(axis=1) - df.min(axis=1)).diff().diff().diff()


def f26_stwf_294_oscillator_peak_clustering_index_63_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std of (bars-since-63d-peak) across basket — peak clustering (low = peaks cluster in time)."""
    b = _all_basket_signals(open, high, low, close)
    items = [b['k'], b['stc'], b['crsi'], b['pctb'], b['ift_s']]
    bs_list = []
    for s in items:
        at_max = s == s.rolling(QDAYS, min_periods=MDAYS).max()
        bs_list.append(_bars_since_true(at_max))
    df = pd.concat([b_.rename(i) for i, b_ in enumerate(bs_list)], axis=1)
    return (df.std(axis=1)).diff().diff().diff()


def f26_stwf_295_oscillator_failure_breadth_at_top_indicator_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """At price 252d-high: count of basket indicators that failed to make new 63d max — failure breadth at top."""
    b = _all_basket_signals(open, high, low, close)
    at_max = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    items = [b['k'], b['stc'], b['crsi'], b['rvi'], b['ift_s']]
    cnt = pd.Series(0.0, index=close.index)
    for s in items:
        not_at_max = s < s.rolling(QDAYS, min_periods=MDAYS).max()
        cnt = cnt + not_at_max.astype(float).fillna(0)
    return (cnt.where(at_max, np.nan)).diff().diff().diff()


def f26_stwf_296_oscillator_extreme_to_normal_velocity_avg_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Average (max - current) across basket in 21d — extreme-to-normal velocity."""
    b = _all_basket_signals(open, high, low, close)
    items = [b['k'], b['stc'], b['crsi'], b['pctb'], b['ift_s']]
    vels = []
    for s in items:
        vels.append(s.rolling(MDAYS, min_periods=WDAYS).max() - s)
    df = pd.concat([v.rename(i) for i, v in enumerate(vels)], axis=1)
    return (df.mean(axis=1)).diff().diff().diff()


def f26_stwf_297_oscillator_basket_correlation_breakdown_indicator_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if avg pairwise basket correlation (63d) drops below 0 — correlation breakdown."""
    b = _all_basket_signals(open, high, low, close)
    items = [b['k'], b['stc'], b['crsi'], b['rvi']]
    pairs = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            pairs.append(items[i].rolling(QDAYS, min_periods=MDAYS).corr(items[j]))
    df = pd.concat([p.rename(i) for i, p in enumerate(pairs)], axis=1)
    avg_corr = df.mean(axis=1)
    return ((avg_corr < 0).astype(float).where(avg_corr.notna(), np.nan)).diff().diff().diff()


def f26_stwf_298_classical_modern_basket_z_diff_252_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Avg z(classical = K, WR) minus avg z(modern = STC, CRSI, BB%B) — old-basket vs new-basket divergence."""
    b = _all_basket_signals(open, high, low, close)
    z_k = _rolling_zscore(b['k'], YDAYS, min_periods=QDAYS)
    z_w = _rolling_zscore(b['wr'], YDAYS, min_periods=QDAYS)
    z_stc = _rolling_zscore(b['stc'], YDAYS, min_periods=QDAYS)
    z_crsi = _rolling_zscore(b['crsi'], YDAYS, min_periods=QDAYS)
    z_pctb = _rolling_zscore(b['pctb'], YDAYS, min_periods=QDAYS)
    classical = (z_k + z_w) / 2.0
    modern = (z_stc + z_crsi + z_pctb) / 3.0
    return (classical - modern).diff().diff().diff()


def f26_stwf_299_universe_persistence_after_extreme_252_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars where extended-basket OB count >= 3 — persistent multi-osc OB regime."""
    b = _all_basket_signals(open, high, low, close)
    cnt = ((b['k'] > 80.0).astype(float).fillna(0)
           + (b['stc'] > 75.0).astype(float).fillna(0)
           + (b['crsi'] > 85.0).astype(float).fillna(0)
           + (b['pctb'] > 1.0).astype(float).fillna(0)
           + (b['ift_s'] > 0.5).astype(float).fillna(0))
    return ((cnt >= 3).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(close.notna(), np.nan)).diff().diff().diff()


def f26_stwf_300_extended_terminal_oscillator_aggregate_score_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Master terminal score: (basket OB count) * (avg z-score) * (at-252d-high indicator) — final composite."""
    b = _all_basket_signals(open, high, low, close)
    cnt = ((b['k'] > 80.0).astype(float).fillna(0)
           + (b['stc'] > 75.0).astype(float).fillna(0)
           + (b['crsi'] > 85.0).astype(float).fillna(0)
           + (b['pctb'] > 1.0).astype(float).fillna(0)
           + (b['ift_s'] > 0.5).astype(float).fillna(0))
    z_list = [_rolling_zscore(s, YDAYS, min_periods=QDAYS) for s in (b['k'], b['stc'], b['crsi'], b['pctb'], b['ift_s'])]
    avg_z = pd.concat([z.rename(i) for i, z in enumerate(z_list)], axis=1).mean(axis=1)
    at_max = (high == high.rolling(YDAYS, min_periods=QDAYS).max()).astype(float)
    return ((cnt * avg_z * at_max).where(close.notna(), np.nan)).diff().diff().diff()


# ============================================================
#                         REGISTRY 226-300 (d3)
# ============================================================

STOCHASTIC_WILLIAMS_FAMILY_D3_REGISTRY_226_300 = {
    "f26_stwf_226_ehlers_super_smoother_stoch_14_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_226_ehlers_super_smoother_stoch_14_d3},
    "f26_stwf_227_laguerre_filter_stoch_06_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_227_laguerre_filter_stoch_06_d3},
    "f26_stwf_228_ehlers_decycler_oscillator_14_d3": {"inputs": ["close"], "func": f26_stwf_228_ehlers_decycler_oscillator_14_d3},
    "f26_stwf_229_ehlers_zero_lag_ema_stoch_14_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_229_ehlers_zero_lag_ema_stoch_14_d3},
    "f26_stwf_230_ehlers_smoothed_adaptive_momentum_d3": {"inputs": ["close"], "func": f26_stwf_230_ehlers_smoothed_adaptive_momentum_d3},
    "f26_stwf_231_ehlers_homodyne_period_proxy_d3": {"inputs": ["close"], "func": f26_stwf_231_ehlers_homodyne_period_proxy_d3},
    "f26_stwf_232_ehlers_instantaneous_trendline_d3": {"inputs": ["close"], "func": f26_stwf_232_ehlers_instantaneous_trendline_d3},
    "f26_stwf_233_ehlers_mama_smoothed_stoch_proxy_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_233_ehlers_mama_smoothed_stoch_proxy_d3},
    "f26_stwf_234_rsi_streak_2_value_d3": {"inputs": ["close"], "func": f26_stwf_234_rsi_streak_2_value_d3},
    "f26_stwf_235_rsi_streak_consecutive_up_count_d3": {"inputs": ["close"], "func": f26_stwf_235_rsi_streak_consecutive_up_count_d3},
    "f26_stwf_236_rsi_streak_consecutive_down_count_d3": {"inputs": ["close"], "func": f26_stwf_236_rsi_streak_consecutive_down_count_d3},
    "f26_stwf_237_rsi_streak_above_90_state_d3": {"inputs": ["close"], "func": f26_stwf_237_rsi_streak_above_90_state_d3},
    "f26_stwf_238_percent_rank_returns_100_value_d3": {"inputs": ["close"], "func": f26_stwf_238_percent_rank_returns_100_value_d3},
    "f26_stwf_239_percent_rank_returns_above_90_state_d3": {"inputs": ["close"], "func": f26_stwf_239_percent_rank_returns_above_90_state_d3},
    "f26_stwf_240_percent_rank_returns_dwell_above_80_63_d3": {"inputs": ["close"], "func": f26_stwf_240_percent_rank_returns_dwell_above_80_63_d3},
    "f26_stwf_241_crsi_components_individual_zscore_252_d3": {"inputs": ["close"], "func": f26_stwf_241_crsi_components_individual_zscore_252_d3},
    "f26_stwf_242_percentile_rank_close_21d_d3": {"inputs": ["close"], "func": f26_stwf_242_percentile_rank_close_21d_d3},
    "f26_stwf_243_percentile_rank_close_63d_d3": {"inputs": ["close"], "func": f26_stwf_243_percentile_rank_close_63d_d3},
    "f26_stwf_244_percentile_rank_high_252d_d3": {"inputs": ["high"], "func": f26_stwf_244_percentile_rank_high_252d_d3},
    "f26_stwf_245_median_close_pos_in_21d_range_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_245_median_close_pos_in_21d_range_d3},
    "f26_stwf_246_iqr_normalized_close_position_63_d3": {"inputs": ["close"], "func": f26_stwf_246_iqr_normalized_close_position_63_d3},
    "f26_stwf_247_range_position_volume_weighted_21d_d3": {"inputs": ["high", "low", "close", "volume"], "func": f26_stwf_247_range_position_volume_weighted_21d_d3},
    "f26_stwf_248_percentile_above_q95_state_63d_d3": {"inputs": ["close"], "func": f26_stwf_248_percentile_above_q95_state_63d_d3},
    "f26_stwf_249_close_in_q90_range_above_state_252d_d3": {"inputs": ["close"], "func": f26_stwf_249_close_in_q90_range_above_state_252d_d3},
    "f26_stwf_250_percentile_consecutive_streak_above_q80_63d_d3": {"inputs": ["close"], "func": f26_stwf_250_percentile_consecutive_streak_above_q80_63d_d3},
    "f26_stwf_251_percentile_band_decay_velocity_63_d3": {"inputs": ["close"], "func": f26_stwf_251_percentile_band_decay_velocity_63_d3},
    "f26_stwf_252_stoch_ema_minus_stoch_sma_14_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_252_stoch_ema_minus_stoch_sma_14_d3},
    "f26_stwf_253_stoch_smoothed_signal_3bar_confirm_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_253_stoch_smoothed_signal_3bar_confirm_d3},
    "f26_stwf_254_stoch_cross_with_min_distance_filter_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_254_stoch_cross_with_min_distance_filter_d3},
    "f26_stwf_255_stoch_cross_with_extreme_filter_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_255_stoch_cross_with_extreme_filter_d3},
    "f26_stwf_256_stoch_cross_with_volume_confirm_d3": {"inputs": ["high", "low", "close", "volume"], "func": f26_stwf_256_stoch_cross_with_volume_confirm_d3},
    "f26_stwf_257_stoch_pivot_count_in_ob_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_257_stoch_pivot_count_in_ob_63_d3},
    "f26_stwf_258_stoch_pivot_to_pivot_amplitude_decay_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_258_stoch_pivot_to_pivot_amplitude_decay_d3},
    "f26_stwf_259_stoch_zigzag_compression_indicator_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_259_stoch_zigzag_compression_indicator_d3},
    "f26_stwf_260_stoch_hook_with_confirmation_filter_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_260_stoch_hook_with_confirmation_filter_d3},
    "f26_stwf_261_stoch_failed_cross_count_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_261_stoch_failed_cross_count_63_d3},
    "f26_stwf_262_weekly_stoch_overbought_aggregate_5d_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_262_weekly_stoch_overbought_aggregate_5d_d3},
    "f26_stwf_263_monthly_stoch_overbought_aggregate_21d_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_263_monthly_stoch_overbought_aggregate_21d_d3},
    "f26_stwf_264_quarterly_stoch_overbought_aggregate_63d_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_264_quarterly_stoch_overbought_aggregate_63d_d3},
    "f26_stwf_265_cross_timeframe_stoch_dispersion_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_265_cross_timeframe_stoch_dispersion_d3},
    "f26_stwf_266_cross_timeframe_oscillator_alignment_score_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_266_cross_timeframe_oscillator_alignment_score_d3},
    "f26_stwf_267_overbought_persistence_across_timeframes_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_267_overbought_persistence_across_timeframes_d3},
    "f26_stwf_268_divergence_across_timeframes_count_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_268_divergence_across_timeframes_count_d3},
    "f26_stwf_269_higher_tf_overbought_short_tf_decline_indicator_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_269_higher_tf_overbought_short_tf_decline_indicator_d3},
    "f26_stwf_270_multi_tf_oscillator_failure_count_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_270_multi_tf_oscillator_failure_count_d3},
    "f26_stwf_271_tf_lead_lag_oscillator_score_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_271_tf_lead_lag_oscillator_score_d3},
    "f26_stwf_272_stoch_autocorrelation_lag_1_21d_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_272_stoch_autocorrelation_lag_1_21d_d3},
    "f26_stwf_273_stoch_autocorrelation_lag_5_63d_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_273_stoch_autocorrelation_lag_5_63d_d3},
    "f26_stwf_274_stoch_partial_autocorrelation_proxy_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_274_stoch_partial_autocorrelation_proxy_d3},
    "f26_stwf_275_stoch_information_coefficient_with_returns_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_275_stoch_information_coefficient_with_returns_63_d3},
    "f26_stwf_276_oscillator_signal_noise_ratio_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_276_oscillator_signal_noise_ratio_63_d3},
    "f26_stwf_277_stoch_predictability_zscore_252_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_277_stoch_predictability_zscore_252_d3},
    "f26_stwf_278_stoch_entropy_distribution_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_278_stoch_entropy_distribution_63_d3},
    "f26_stwf_279_stoch_innovation_residual_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_279_stoch_innovation_residual_63_d3},
    "f26_stwf_280_stoch_long_memory_hurst_proxy_63_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_280_stoch_long_memory_hurst_proxy_63_d3},
    "f26_stwf_281_stoch_kurtosis_at_top_state_d3": {"inputs": ["high", "low", "close"], "func": f26_stwf_281_stoch_kurtosis_at_top_state_d3},
    "f26_stwf_282_extended_modern_basket_topping_count_d3": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_282_extended_modern_basket_topping_count_d3},
    "f26_stwf_283_count_modern_basket_in_extreme_state_d3": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_283_count_modern_basket_in_extreme_state_d3},
    "f26_stwf_284_count_modern_basket_recent_exit_d3": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_284_count_modern_basket_recent_exit_d3},
    "f26_stwf_285_count_modern_basket_with_divergence_d3": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_285_count_modern_basket_with_divergence_d3},
    "f26_stwf_286_modern_basket_avg_zscore_252_d3": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_286_modern_basket_avg_zscore_252_d3},
    "f26_stwf_287_modern_basket_dispersion_zscore_252_d3": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_287_modern_basket_dispersion_zscore_252_d3},
    "f26_stwf_288_combined_classical_modern_consensus_bearish_d3": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_288_combined_classical_modern_consensus_bearish_d3},
    "f26_stwf_289_oscillator_universe_breadth_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_289_oscillator_universe_breadth_indicator_d3},
    "f26_stwf_290_oscillator_universe_extreme_count_at_top_d3": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_290_oscillator_universe_extreme_count_at_top_d3},
    "f26_stwf_291_oscillator_universe_decay_velocity_post_peak_d3": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_291_oscillator_universe_decay_velocity_post_peak_d3},
    "f26_stwf_292_oscillator_universe_terminal_pattern_score_d3": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_292_oscillator_universe_terminal_pattern_score_d3},
    "f26_stwf_293_temporal_alignment_oscillator_peaks_63_d3": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_293_temporal_alignment_oscillator_peaks_63_d3},
    "f26_stwf_294_oscillator_peak_clustering_index_63_d3": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_294_oscillator_peak_clustering_index_63_d3},
    "f26_stwf_295_oscillator_failure_breadth_at_top_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_295_oscillator_failure_breadth_at_top_indicator_d3},
    "f26_stwf_296_oscillator_extreme_to_normal_velocity_avg_d3": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_296_oscillator_extreme_to_normal_velocity_avg_d3},
    "f26_stwf_297_oscillator_basket_correlation_breakdown_indicator_d3": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_297_oscillator_basket_correlation_breakdown_indicator_d3},
    "f26_stwf_298_classical_modern_basket_z_diff_252_d3": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_298_classical_modern_basket_z_diff_252_d3},
    "f26_stwf_299_universe_persistence_after_extreme_252_d3": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_299_universe_persistence_after_extreme_252_d3},
    "f26_stwf_300_extended_terminal_oscillator_aggregate_score_d3": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_300_extended_terminal_oscillator_aggregate_score_d3},
}
