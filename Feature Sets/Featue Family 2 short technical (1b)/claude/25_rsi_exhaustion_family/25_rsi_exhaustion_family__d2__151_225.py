"""rsi_exhaustion_family d2 features 151-225 — Pipeline 1b-technical.

GAP-FILL extension to base 001-150. DISTINCT concepts NOT covered:

- Stochastic RSI (StochRSI) with K and D smoothing — different normalization from Connors
- OS (oversold) zone features — existing 001-150 was OB-heavy; symmetric coverage needed
- Bullish divergences (mirror of existing bearish-only divergence coverage)
- Wilder failure swings (4-step canonical pattern) bearish + bullish
- Dynamic OB/OS bands (rolling-quantile RSI levels, NOT fixed 70/30)
- Bollinger Bands ON RSI (RSI Bollinger)
- Laguerre RSI (Ehlers filter applied to RSI)
- RSI confirmation/disconfirmation of price new highs/lows
- Multi-horizon RSI compression / consensus / alignment
- RSI BB squeeze indicator
- Heikin-Ashi RSI smoothed
- RSI mid-band oscillator (centered around 50)
- Weekly/monthly RSI proxy
- Composite top/bottom signatures, RSI phase classifier

Inputs: SEP OHLCV only. PIT-clean. Self-contained helpers — no cross-family imports.
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


def _bars_since(event):
    idx_at = np.where(event.to_numpy(), np.arange(len(event)), np.nan)
    last = pd.Series(idx_at, index=event.index).ffill()
    return pd.Series(np.arange(len(event), dtype=float), index=event.index) - last


# ---- family-specific helpers ----

def _rsi_wilder(close: pd.Series, n: int) -> pd.Series:
    """Wilder RSI of length n using EWMA smoothing of gains/losses."""
    d = close.diff()
    gain = d.where(d > 0, 0.0)
    loss = (-d).where(d < 0, 0.0)
    avg_gain = gain.ewm(alpha=1.0 / n, min_periods=n, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1.0 / n, min_periods=n, adjust=False).mean()
    rs = _safe_div(avg_gain, avg_loss)
    return 100.0 - 100.0 / (1.0 + rs)


def _stoch_rsi(close: pd.Series, rsi_n: int = 14, stoch_n: int = 14):
    """StochRSI: stochastic oscillator applied to RSI. Returns (raw, K, D) all in [0, 1]."""
    rsi = _rsi_wilder(close, rsi_n)
    rsi_max = rsi.rolling(stoch_n, min_periods=max(stoch_n // 3, 2)).max()
    rsi_min = rsi.rolling(stoch_n, min_periods=max(stoch_n // 3, 2)).min()
    raw = _safe_div(rsi - rsi_min, rsi_max - rsi_min)
    K = raw.rolling(3, min_periods=2).mean()
    D = K.rolling(3, min_periods=2).mean()
    return raw, K, D


def _laguerre_rsi(close: pd.Series, gamma: float = 0.5) -> pd.Series:
    """Laguerre RSI (Ehlers): 4-stage Laguerre filter with RSI-like output [0..100]."""
    n = len(close)
    arr = close.to_numpy()
    L0 = np.full(n, np.nan); L1 = np.full(n, np.nan); L2 = np.full(n, np.nan); L3 = np.full(n, np.nan)
    out = np.full(n, np.nan)
    L0_prev = L1_prev = L2_prev = L3_prev = 0.0
    started = False
    for i in range(n):
        v = arr[i]
        if np.isnan(v):
            continue
        if not started:
            L0_prev = L1_prev = L2_prev = L3_prev = v
            started = True
            continue
        L0_cur = (1.0 - gamma) * v + gamma * L0_prev
        L1_cur = -gamma * L0_cur + L0_prev + gamma * L1_prev
        L2_cur = -gamma * L1_cur + L1_prev + gamma * L2_prev
        L3_cur = -gamma * L2_cur + L2_prev + gamma * L3_prev
        L0[i], L1[i], L2[i], L3[i] = L0_cur, L1_cur, L2_cur, L3_cur
        # CU and CD
        CU = 0.0; CD = 0.0
        for a, b in [(L0_cur, L1_cur), (L1_cur, L2_cur), (L2_cur, L3_cur)]:
            if a >= b: CU += (a - b)
            else: CD += (b - a)
        if (CU + CD) > 0:
            out[i] = 100.0 * CU / (CU + CD)
        L0_prev, L1_prev, L2_prev, L3_prev = L0_cur, L1_cur, L2_cur, L3_cur
    return pd.Series(out, index=close.index)


def _div_bear_window(price, indicator, n):
    p_max = price.rolling(n, min_periods=max(n // 3, 2)).max()
    p_at_high = price >= p_max
    ind_prev_max = indicator.shift(1).rolling(n, min_periods=max(n // 3, 2)).max()
    return (p_at_high & (indicator < ind_prev_max)).astype(float)


def _div_bull_window(price, indicator, n):
    p_min = price.rolling(n, min_periods=max(n // 3, 2)).min()
    p_at_low = price <= p_min
    ind_prev_min = indicator.shift(1).rolling(n, min_periods=max(n // 3, 2)).min()
    return (p_at_low & (indicator > ind_prev_min)).astype(float)


def _hidden_div_bull_window(price, indicator, n):
    p_prev_min = price.shift(1).rolling(n, min_periods=max(n // 3, 2)).min()
    p_higher_l = (price > p_prev_min)
    ind_prev_min = indicator.shift(1).rolling(n, min_periods=max(n // 3, 2)).min()
    ind_lower_l = (indicator < ind_prev_min)
    return (p_higher_l & ind_lower_l).astype(float)


# ============================================================
# Bucket A — StochRSI (151-157)
# ============================================================

def f25_rsxh_151_stoch_rsi_14_14_raw(close: pd.Series) -> pd.Series:
    """Raw StochRSI (RSI14, stoch window 14): 0..1 normalized RSI position within rolling RSI range."""
    raw, _, _ = _stoch_rsi(close, 14, 14)
    return raw


def f25_rsxh_152_stoch_rsi_K_14_14(close: pd.Series) -> pd.Series:
    """StochRSI 3-bar SMA-smoothed K line."""
    _, K, _ = _stoch_rsi(close, 14, 14)
    return K


def f25_rsxh_153_stoch_rsi_D_14_14(close: pd.Series) -> pd.Series:
    """StochRSI 3-bar SMA-smoothed D line (smoothed K)."""
    _, _, D = _stoch_rsi(close, 14, 14)
    return D


def f25_rsxh_154_stoch_rsi_above_0_8_state(close: pd.Series) -> pd.Series:
    """Indicator: StochRSI raw > 0.8 (canonical OB threshold for StochRSI)."""
    raw, _, _ = _stoch_rsi(close, 14, 14)
    return (raw > 0.8).astype(float)


def f25_rsxh_155_stoch_rsi_below_0_2_state(close: pd.Series) -> pd.Series:
    """Indicator: StochRSI raw < 0.2 (canonical OS threshold)."""
    raw, _, _ = _stoch_rsi(close, 14, 14)
    return (raw < 0.2).astype(float)


def f25_rsxh_156_stoch_rsi_K_D_bearish_cross_event(close: pd.Series) -> pd.Series:
    """Indicator: today K crossed BELOW D AND K was above 0.8 yesterday — bearish StochRSI cross from OB."""
    _, K, D = _stoch_rsi(close, 14, 14)
    return ((K < D) & (K.shift(1) >= D.shift(1)) & (K.shift(1) > 0.8)).astype(float)


def f25_rsxh_157_stoch_rsi_bearish_div_63(close: pd.Series) -> pd.Series:
    """Bearish StochRSI divergence: price new 63d high but StochRSI raw < prior 63d StochRSI max."""
    raw, _, _ = _stoch_rsi(close, 14, 14)
    return _div_bear_window(close, raw, QDAYS)


# ============================================================
# Bucket B — OS-zone features (mirror of OB coverage) (158-167)
# ============================================================

def f25_rsxh_158_rsi14_below_30_state(close: pd.Series) -> pd.Series:
    """Indicator: RSI14 < 30 (canonical OS state)."""
    return (_rsi_wilder(close, 14) < 30).astype(float)


def f25_rsxh_159_rsi14_below_20_state(close: pd.Series) -> pd.Series:
    """Indicator: RSI14 < 20 (extreme OS)."""
    return (_rsi_wilder(close, 14) < 20).astype(float)


def f25_rsxh_160_rsi14_below_10_state(close: pd.Series) -> pd.Series:
    """Indicator: RSI14 < 10 (extreme capitulation OS)."""
    return (_rsi_wilder(close, 14) < 10).astype(float)


def f25_rsxh_161_rsi14_just_exited_os30(close: pd.Series) -> pd.Series:
    """Indicator: RSI14 just crossed above 30 from below (OS exit event)."""
    rsi = _rsi_wilder(close, 14)
    return ((rsi >= 30) & (rsi.shift(1) < 30)).astype(float)


def f25_rsxh_162_rsi14_just_exited_os20(close: pd.Series) -> pd.Series:
    """Indicator: RSI14 just crossed above 20 from below."""
    rsi = _rsi_wilder(close, 14)
    return ((rsi >= 20) & (rsi.shift(1) < 20)).astype(float)


def f25_rsxh_163_bars_since_rsi14_os30_exit(close: pd.Series) -> pd.Series:
    """Bars since the most recent OS30-exit event (RSI14 crossing above 30 from below)."""
    rsi = _rsi_wilder(close, 14)
    ev = (rsi >= 30) & (rsi.shift(1) < 30)
    return _bars_since(ev.fillna(False))


def f25_rsxh_164_count_rsi14_os30_exits_252(close: pd.Series) -> pd.Series:
    """Count of OS30-exit events in trailing 252d."""
    rsi = _rsi_wilder(close, 14)
    ev = ((rsi >= 30) & (rsi.shift(1) < 30)).astype(float)
    return ev.rolling(YDAYS, min_periods=QDAYS).sum()


def f25_rsxh_165_fraction_rsi14_os30_past_63(close: pd.Series) -> pd.Series:
    """Fraction of last 63 bars where RSI14 < 30."""
    return (_rsi_wilder(close, 14) < 30).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()


def f25_rsxh_166_cumulative_os30_area_252(close: pd.Series) -> pd.Series:
    """Cumulative (30 - RSI14).clip(lower=0) over trailing 252d — area below OS30 line."""
    rsi = _rsi_wilder(close, 14)
    return (30.0 - rsi).clip(lower=0).rolling(YDAYS, min_periods=QDAYS).sum()


def f25_rsxh_167_longest_rsi14_os30_run_252(close: pd.Series) -> pd.Series:
    """Longest consecutive bar run with RSI14 < 30 in trailing 252d."""
    rsi_os = (_rsi_wilder(close, 14) < 30).fillna(False)
    grp = (~rsi_os).cumsum()
    streak = rsi_os.astype(int).groupby(grp).cumsum().astype(float)
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


# ============================================================
# Bucket C — Bullish divergences (mirror) (168-174)
# ============================================================

def f25_rsxh_168_price_vs_rsi14_bull_div_63(close: pd.Series) -> pd.Series:
    """Bullish RSI14 divergence: price new 63d low but RSI > prior 63d RSI min."""
    return _div_bull_window(close, _rsi_wilder(close, 14), QDAYS)


def f25_rsxh_169_price_vs_rsi14_bull_div_252(close: pd.Series) -> pd.Series:
    """Bullish RSI14 divergence (252d horizon)."""
    return _div_bull_window(close, _rsi_wilder(close, 14), YDAYS)


def f25_rsxh_170_count_bullish_rsi_div_63(close: pd.Series) -> pd.Series:
    """Count of bullish RSI14 divergence events in trailing 63d."""
    return _div_bull_window(close, _rsi_wilder(close, 14), QDAYS).rolling(QDAYS, min_periods=MDAYS).sum()


def f25_rsxh_171_count_bullish_rsi_div_252(close: pd.Series) -> pd.Series:
    """Count of bullish RSI14 divergence events in trailing 252d."""
    return _div_bull_window(close, _rsi_wilder(close, 14), QDAYS).rolling(YDAYS, min_periods=QDAYS).sum()


def f25_rsxh_172_bars_since_last_bullish_rsi_div_63(close: pd.Series) -> pd.Series:
    """Bars since the most recent bullish RSI14 divergence event."""
    ev = _div_bull_window(close, _rsi_wilder(close, 14), QDAYS).astype(bool)
    return _bars_since(ev)


def f25_rsxh_173_hidden_bullish_div_63(close: pd.Series) -> pd.Series:
    """Hidden bullish RSI14 divergence: price higher-low but RSI lower-low."""
    return _hidden_div_bull_window(close, _rsi_wilder(close, 14), QDAYS)


def f25_rsxh_174_triple_bullish_div_within_63(close: pd.Series) -> pd.Series:
    """Indicator: 3+ bullish RSI14 divergence events within last 63 bars."""
    cnt = _div_bull_window(close, _rsi_wilder(close, 14), QDAYS).rolling(QDAYS, min_periods=MDAYS).sum()
    return (cnt >= 3).astype(float)


# ============================================================
# Bucket D — Wilder failure swings (175-178)
# ============================================================

def f25_rsxh_175_rsi14_bearish_failure_swing_indicator(close: pd.Series) -> pd.Series:
    """Canonical Wilder bearish failure swing (4 steps): RSI above 70, then pulls back, then bounces but stays
    below first peak, then breaks below intervening trough. Approximation:
    - bar t-30..t-1: RSI reached above 70 (peak_1)
    - bar t-15..t-5: RSI pulled back, formed trough between peak_1 and peak_2
    - bar t-15..t-1: RSI bounced to peak_2 < peak_1 (failure to make new high)
    - today: RSI < trough between peaks (break of trough)."""
    rsi = _rsi_wilder(close, 14)
    n = len(close); arr = rsi.to_numpy(); out = np.full(n, 0.0)
    for i in range(30, n):
        window = arr[i - 30:i]
        if np.isnan(window).any(): continue
        # find first peak above 70
        above_70_idx = np.where(window >= 70)[0]
        if above_70_idx.size == 0: continue
        peak1_idx = above_70_idx[0] + int(np.argmax(window[above_70_idx[0]:]))
        if peak1_idx >= len(window) - 5: continue
        peak1 = window[peak1_idx]
        # find trough after peak1 (must dip below 70 then bounce)
        after_p1 = window[peak1_idx + 1:]
        trough_local = np.min(after_p1)
        trough_idx = peak1_idx + 1 + int(np.argmin(after_p1))
        if trough_local >= 70: continue  # didn't dip below 70
        if trough_idx >= len(window) - 2: continue
        # find peak2 after trough that is LOWER than peak1
        after_trough = window[trough_idx + 1:]
        peak2_local = np.max(after_trough)
        if peak2_local >= peak1: continue  # made new high — not a failure swing
        # today RSI < trough_local
        if arr[i] < trough_local:
            out[i] = 1.0
    return pd.Series(out, index=close.index)


def f25_rsxh_176_rsi14_bullish_failure_swing_indicator(close: pd.Series) -> pd.Series:
    """Canonical Wilder bullish failure swing: mirror of bearish. RSI dropped below 30, bounced, retraced but
    stayed above 30, broke above intervening peak."""
    rsi = _rsi_wilder(close, 14)
    n = len(close); arr = rsi.to_numpy(); out = np.full(n, 0.0)
    for i in range(30, n):
        window = arr[i - 30:i]
        if np.isnan(window).any(): continue
        below_30_idx = np.where(window <= 30)[0]
        if below_30_idx.size == 0: continue
        trough1_idx = below_30_idx[0] + int(np.argmin(window[below_30_idx[0]:]))
        if trough1_idx >= len(window) - 5: continue
        trough1 = window[trough1_idx]
        after_t1 = window[trough1_idx + 1:]
        peak_local = np.max(after_t1)
        peak_idx = trough1_idx + 1 + int(np.argmax(after_t1))
        if peak_local <= 30: continue
        if peak_idx >= len(window) - 2: continue
        after_peak = window[peak_idx + 1:]
        trough2_local = np.min(after_peak)
        if trough2_local <= trough1: continue
        if arr[i] > peak_local:
            out[i] = 1.0
    return pd.Series(out, index=close.index)


def f25_rsxh_177_count_bearish_failure_swings_252(close: pd.Series) -> pd.Series:
    """Count of Wilder bearish failure swings in 252d."""
    return f25_rsxh_175_rsi14_bearish_failure_swing_indicator(close).rolling(YDAYS, min_periods=QDAYS).sum()


def f25_rsxh_178_count_bullish_failure_swings_252(close: pd.Series) -> pd.Series:
    """Count of Wilder bullish failure swings in 252d."""
    return f25_rsxh_176_rsi14_bullish_failure_swing_indicator(close).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket E — Dynamic OB/OS bands (179-183)
# ============================================================

def f25_rsxh_179_rsi14_dynamic_ob_band_q90_252(close: pd.Series) -> pd.Series:
    """Dynamic OB band: 90th-percentile RSI14 over trailing 252d (data-adaptive level)."""
    return _rsi_wilder(close, 14).rolling(YDAYS, min_periods=QDAYS).quantile(0.9)


def f25_rsxh_180_rsi14_above_dynamic_ob_indicator(close: pd.Series) -> pd.Series:
    """Indicator: RSI14 > its dynamic 252d Q90 (rather than fixed 70) — adaptive OB."""
    rsi = _rsi_wilder(close, 14)
    return (rsi > rsi.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)).astype(float)


def f25_rsxh_181_rsi14_dynamic_os_band_q10_252(close: pd.Series) -> pd.Series:
    """Dynamic OS band: 10th-percentile RSI14 over trailing 252d."""
    return _rsi_wilder(close, 14).rolling(YDAYS, min_periods=QDAYS).quantile(0.1)


def f25_rsxh_182_rsi14_below_dynamic_os_indicator(close: pd.Series) -> pd.Series:
    """Indicator: RSI14 < its dynamic 252d Q10."""
    rsi = _rsi_wilder(close, 14)
    return (rsi < rsi.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)).astype(float)


def f25_rsxh_183_dynamic_ob_band_width_252(close: pd.Series) -> pd.Series:
    """Width of dynamic OB band: Q90 - Q10 of RSI14 over 252d — RSI dispersion regime."""
    rsi = _rsi_wilder(close, 14)
    return rsi.rolling(YDAYS, min_periods=QDAYS).quantile(0.9) - rsi.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)


# ============================================================
# Bucket F — Bollinger Bands on RSI (184-187)
# ============================================================

def f25_rsxh_184_rsi14_bb_upper_21(close: pd.Series) -> pd.Series:
    """Upper Bollinger Band (21d mean + 2 stdev) of RSI14."""
    rsi = _rsi_wilder(close, 14)
    return rsi.rolling(MDAYS, min_periods=WDAYS).mean() + 2.0 * rsi.rolling(MDAYS, min_periods=WDAYS).std()


def f25_rsxh_185_rsi14_bb_lower_21(close: pd.Series) -> pd.Series:
    """Lower Bollinger Band of RSI14."""
    rsi = _rsi_wilder(close, 14)
    return rsi.rolling(MDAYS, min_periods=WDAYS).mean() - 2.0 * rsi.rolling(MDAYS, min_periods=WDAYS).std()


def f25_rsxh_186_rsi14_above_bb_upper_indicator(close: pd.Series) -> pd.Series:
    """Indicator: RSI14 above its 21d upper Bollinger Band — unusually strong RSI."""
    rsi = _rsi_wilder(close, 14)
    upper = rsi.rolling(MDAYS, min_periods=WDAYS).mean() + 2.0 * rsi.rolling(MDAYS, min_periods=WDAYS).std()
    return (rsi > upper).astype(float)


def f25_rsxh_187_rsi14_bb_width_zscore_252(close: pd.Series) -> pd.Series:
    """Z-score of (21d BB width on RSI14) vs 252d distribution — RSI dispersion shifts."""
    rsi = _rsi_wilder(close, 14)
    width = 4.0 * rsi.rolling(MDAYS, min_periods=WDAYS).std()
    return _rolling_zscore(width, YDAYS, min_periods=QDAYS)


# ============================================================
# Bucket G — Laguerre RSI (Ehlers) (188-191)
# ============================================================

def f25_rsxh_188_laguerre_rsi_gamma_05(close: pd.Series) -> pd.Series:
    """Ehlers Laguerre RSI with gamma=0.5 — smooth fast-responsive RSI variant."""
    return _laguerre_rsi(close, gamma=0.5)


def f25_rsxh_189_laguerre_rsi_above_85_state(close: pd.Series) -> pd.Series:
    """Indicator: Laguerre RSI > 85 (its standard OB threshold)."""
    return (_laguerre_rsi(close, gamma=0.5) > 85).astype(float)


def f25_rsxh_190_laguerre_rsi_above_85_just_exited(close: pd.Series) -> pd.Series:
    """Indicator: Laguerre RSI crossed below 85 from above (OB exit event)."""
    lrsi = _laguerre_rsi(close, gamma=0.5)
    return ((lrsi < 85) & (lrsi.shift(1) >= 85)).astype(float)


def f25_rsxh_191_laguerre_rsi_zscore_252(close: pd.Series) -> pd.Series:
    """Z-score of Laguerre RSI vs 252d distribution."""
    return _rolling_zscore(_laguerre_rsi(close, gamma=0.5), YDAYS, min_periods=QDAYS)


# ============================================================
# Bucket H — RSI confirmation / disconfirmation of price (192-195)
# ============================================================

def f25_rsxh_192_rsi_confirms_new_high_indicator(close: pd.Series) -> pd.Series:
    """Indicator: price at new 21d high AND RSI14 also at new 21d high (both confirming uptrend)."""
    p_max21 = close.rolling(MDAYS, min_periods=WDAYS).max()
    rsi = _rsi_wilder(close, 14)
    rsi_max21 = rsi.rolling(MDAYS, min_periods=WDAYS).max()
    return ((close >= p_max21) & (rsi >= rsi_max21)).astype(float)


def f25_rsxh_193_rsi_disconfirms_new_high_indicator(close: pd.Series) -> pd.Series:
    """Indicator: price at new 21d high BUT RSI14 LOWER than its 21d max — bearish disconfirmation."""
    p_max21 = close.rolling(MDAYS, min_periods=WDAYS).max()
    rsi = _rsi_wilder(close, 14)
    rsi_max21 = rsi.rolling(MDAYS, min_periods=WDAYS).max()
    return ((close >= p_max21) & (rsi < rsi_max21)).astype(float)


def f25_rsxh_194_count_rsi_disconfirms_new_high_252(close: pd.Series) -> pd.Series:
    """Count of disconfirmation events in 252d — accumulated weakness signal."""
    return f25_rsxh_193_rsi_disconfirms_new_high_indicator(close).rolling(YDAYS, min_periods=QDAYS).sum()


def f25_rsxh_195_rsi_confirms_new_low_indicator(close: pd.Series) -> pd.Series:
    """Indicator: price at new 21d low AND RSI14 at new 21d low (confirming downtrend)."""
    p_min21 = close.rolling(MDAYS, min_periods=WDAYS).min()
    rsi = _rsi_wilder(close, 14)
    rsi_min21 = rsi.rolling(MDAYS, min_periods=WDAYS).min()
    return ((close <= p_min21) & (rsi <= rsi_min21)).astype(float)


# ============================================================
# Bucket I — Multi-horizon RSI compression / consensus (196-200)
# ============================================================

def f25_rsxh_196_rsi_std_compression_short_long_ratio(close: pd.Series) -> pd.Series:
    """Ratio: 14d-std-of-RSI14 / 63d-std-of-RSI14 — short-term RSI vol vs long-term."""
    rsi = _rsi_wilder(close, 14)
    return _safe_div(rsi.rolling(14, min_periods=5).std(), rsi.rolling(QDAYS, min_periods=MDAYS).std())


def f25_rsxh_197_multi_horizon_rsi_consensus_OB_count(close: pd.Series) -> pd.Series:
    """Count of {RSI7, RSI14, RSI21, RSI63} currently > 70."""
    return ((_rsi_wilder(close, 7) > 70).astype(float)
            + (_rsi_wilder(close, 14) > 70).astype(float)
            + (_rsi_wilder(close, 21) > 70).astype(float)
            + (_rsi_wilder(close, 63) > 70).astype(float))


def f25_rsxh_198_multi_horizon_rsi_consensus_OS_count(close: pd.Series) -> pd.Series:
    """Count of {RSI7, RSI14, RSI21, RSI63} currently < 30."""
    return ((_rsi_wilder(close, 7) < 30).astype(float)
            + (_rsi_wilder(close, 14) < 30).astype(float)
            + (_rsi_wilder(close, 21) < 30).astype(float)
            + (_rsi_wilder(close, 63) < 30).astype(float))


def f25_rsxh_199_rsi_horizon_disagreement_max_minus_min(close: pd.Series) -> pd.Series:
    """Max - min across {RSI7, RSI14, RSI21, RSI63} — disagreement across horizons."""
    df = pd.concat([_rsi_wilder(close, n).rename(f'r{n}') for n in [7, 14, 21, 63]], axis=1)
    return df.max(axis=1) - df.min(axis=1)


def f25_rsxh_200_rsi_horizon_alignment_score(close: pd.Series) -> pd.Series:
    """Alignment score: count of pairs (R7, R14, R21, R63) where shorter-horizon RSI > longer-horizon RSI
    (3 pairs; max value 3 = strong bullish ordering)."""
    r7 = _rsi_wilder(close, 7); r14 = _rsi_wilder(close, 14); r21 = _rsi_wilder(close, 21); r63 = _rsi_wilder(close, 63)
    return ((r7 > r14).astype(float) + (r14 > r21).astype(float) + (r21 > r63).astype(float))


# ============================================================
# Bucket J — RSI BB squeeze (201-203)
# ============================================================

def f25_rsxh_201_rsi_bb_squeeze_indicator(close: pd.Series) -> pd.Series:
    """Indicator: RSI14 BB width < bottom 20% of 252d distribution — squeeze."""
    rsi = _rsi_wilder(close, 14)
    width = 4.0 * rsi.rolling(MDAYS, min_periods=WDAYS).std()
    q20 = width.rolling(YDAYS, min_periods=QDAYS).quantile(0.2)
    return (width < q20).astype(float)


def f25_rsxh_202_rsi_bb_squeeze_count_252(close: pd.Series) -> pd.Series:
    """Count of RSI BB squeeze bars in trailing 252d."""
    return f25_rsxh_201_rsi_bb_squeeze_indicator(close).rolling(YDAYS, min_periods=QDAYS).sum()


def f25_rsxh_203_bars_since_rsi_bb_squeeze_release(close: pd.Series) -> pd.Series:
    """Bars since the most recent RSI BB squeeze release (transition from squeeze to non-squeeze)."""
    sq = f25_rsxh_201_rsi_bb_squeeze_indicator(close).astype(bool)
    release = sq.shift(1).fillna(False) & ~sq
    return _bars_since(release.fillna(False))


# ============================================================
# Bucket K — Heikin-Ashi RSI (204-206)
# ============================================================

def _heikin_ashi_close(open_, high, low, close):
    """Heikin-Ashi close = (O+H+L+C) / 4."""
    return (open_ + high + low + close) / 4.0


def f25_rsxh_204_heikin_ashi_close(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Heikin-Ashi close (smoothed close proxy)."""
    return _heikin_ashi_close(open_, high, low, close)


def f25_rsxh_205_rsi14_of_heikin_ashi_close(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """RSI14 computed on Heikin-Ashi close — smoother RSI."""
    return _rsi_wilder(_heikin_ashi_close(open_, high, low, close), 14)


def f25_rsxh_206_ha_rsi_above_70_state(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: HA-RSI14 > 70 (smoother OB signal)."""
    return (_rsi_wilder(_heikin_ashi_close(open_, high, low, close), 14) > 70).astype(float)


# ============================================================
# Bucket L — RSI mid-band oscillator (207-209)
# ============================================================

def f25_rsxh_207_rsi_mid_band_normalized(close: pd.Series) -> pd.Series:
    """Normalized RSI mid-band oscillator: (RSI14 - 50) / 50, ranges -1..+1."""
    return (_rsi_wilder(close, 14) - 50.0) / 50.0


def f25_rsxh_208_rsi_mid_band_zscore_252(close: pd.Series) -> pd.Series:
    """Z-score of mid-band oscillator vs 252d distribution."""
    return _rolling_zscore((_rsi_wilder(close, 14) - 50.0) / 50.0, YDAYS, min_periods=QDAYS)


def f25_rsxh_209_rsi_mid_band_dwell_negative_63(close: pd.Series) -> pd.Series:
    """Fraction of last 63 bars where mid-band osc < 0 (RSI < 50 = bearish bias)."""
    return ((_rsi_wilder(close, 14) - 50.0) / 50.0 < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean()


# ============================================================
# Bucket M — Weekly / monthly RSI proxy (210-212)
# ============================================================

def f25_rsxh_210_weekly_rsi_proxy_14(close: pd.Series) -> pd.Series:
    """Weekly RSI proxy: RSI14 of 5-bar (weekly) resampled close (take 5d-mean as 'weekly close')."""
    weekly = close.rolling(WDAYS, min_periods=WDAYS).mean()
    return _rsi_wilder(weekly, 14)


def f25_rsxh_211_weekly_rsi_above_70_state(close: pd.Series) -> pd.Series:
    """Indicator: weekly RSI proxy > 70."""
    return (f25_rsxh_210_weekly_rsi_proxy_14(close) > 70).astype(float)


def f25_rsxh_212_monthly_rsi_proxy_14(close: pd.Series) -> pd.Series:
    """Monthly RSI proxy: RSI14 of 21-bar resampled close."""
    monthly = close.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rsi_wilder(monthly, 14)


# ============================================================
# Bucket N — Composite indicators / regimes (213-220)
# ============================================================

def f25_rsxh_213_composite_rsi_top_signature_252(close: pd.Series) -> pd.Series:
    """Composite top: RSI14 > Q90(252d) AND bearish RSI div in last 21d AND bearish failure swing in last 63d."""
    rsi = _rsi_wilder(close, 14)
    q90 = rsi.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    high_rsi = (rsi > q90).astype(float)
    bear_div_recent = _div_bear_window(close, rsi, QDAYS).rolling(MDAYS, min_periods=WDAYS).max().fillna(0)
    fail_swing_recent = f25_rsxh_175_rsi14_bearish_failure_swing_indicator(close).rolling(QDAYS, min_periods=MDAYS).max().fillna(0)
    return high_rsi + bear_div_recent + fail_swing_recent


def f25_rsxh_214_composite_rsi_bottom_signature_252(close: pd.Series) -> pd.Series:
    """Composite bottom: RSI14 < Q10(252d) AND bullish RSI div in last 21d AND bullish failure swing in 63d."""
    rsi = _rsi_wilder(close, 14)
    q10 = rsi.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
    low_rsi = (rsi < q10).astype(float)
    bull_div_recent = _div_bull_window(close, rsi, QDAYS).rolling(MDAYS, min_periods=WDAYS).max().fillna(0)
    fail_swing_recent = f25_rsxh_176_rsi14_bullish_failure_swing_indicator(close).rolling(QDAYS, min_periods=MDAYS).max().fillna(0)
    return low_rsi + bull_div_recent + fail_swing_recent


def f25_rsxh_215_rsi_phase_classifier_252(close: pd.Series) -> pd.Series:
    """Categorical RSI phase: 0=OS_extreme (<20), 1=OS (20-30), 2=neutral_dn (30-50), 3=neutral_up (50-70),
    4=OB (70-80), 5=OB_extreme (>=80)."""
    rsi = _rsi_wilder(close, 14)
    arr = rsi.to_numpy(); n = len(close)
    out = np.full(n, np.nan)
    m = ~np.isnan(arr)
    out = np.where(m & (arr < 20), 0, out)
    out = np.where(m & (arr >= 20) & (arr < 30), 1, out)
    out = np.where(m & (arr >= 30) & (arr < 50), 2, out)
    out = np.where(m & (arr >= 50) & (arr < 70), 3, out)
    out = np.where(m & (arr >= 70) & (arr < 80), 4, out)
    out = np.where(m & (arr >= 80), 5, out)
    return pd.Series(out, index=close.index)


def f25_rsxh_216_rsi_regime_persistence_score_252(close: pd.Series) -> pd.Series:
    """Mean run-length of each RSI phase (categorical from 215) over 252d — higher = more persistent regimes."""
    phase = f25_rsxh_215_rsi_phase_classifier_252(close)
    same = (phase == phase.shift(1))
    grp = (~same).cumsum()
    run_lens = same.astype(int).groupby(grp).cumsum().astype(float)
    return run_lens.rolling(YDAYS, min_periods=QDAYS).mean()


def f25_rsxh_217_rsi_OB_OS_imbalance_252(close: pd.Series) -> pd.Series:
    """Count of OB bars (RSI14 > 70) minus count of OS bars (RSI14 < 30) in trailing 252d."""
    rsi = _rsi_wilder(close, 14)
    ob = (rsi > 70).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    os = (rsi < 30).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()
    return ob - os


def f25_rsxh_218_rsi_quality_score_at_new_high_252(close: pd.Series) -> pd.Series:
    """Mean RSI14 on bars where price set a new 252d high in trailing 252d.
    High mean = strong momentum at peaks. Low mean = weak peaks (bearish)."""
    rmax = close.rolling(YDAYS, min_periods=QDAYS).max()
    at_new_high = (close >= rmax)
    rsi = _rsi_wilder(close, 14)
    return rsi.where(at_new_high, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f25_rsxh_219_count_failed_OB_breakouts_252(close: pd.Series) -> pd.Series:
    """Count of bars in 252d where RSI14 broke above 70 then within 21 bars failed to exceed prior 21d-RSI-max.
    PIT-safe via shift."""
    rsi = _rsi_wilder(close, 14)
    just_broke = ((rsi > 70) & (rsi.shift(1) <= 70))
    rsi_max_21 = rsi.rolling(MDAYS, min_periods=WDAYS).max()
    # Failure: 21 bars after the break, RSI21d-max < (RSI at break + 5) approx — too vague.
    # Simpler: bars where just_broke 21d ago AND RSI today < RSI 21d ago
    fail = just_broke.shift(MDAYS).fillna(False) & (rsi < rsi.shift(MDAYS))
    return fail.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f25_rsxh_220_rsi_acceleration_change_event_count_252(close: pd.Series) -> pd.Series:
    """Count of bars in 252d where 5d RSI velocity changed sign (was positive, now negative or vice versa)."""
    rsi = _rsi_wilder(close, 14)
    v = rsi - rsi.shift(WDAYS)
    sign_change = (np.sign(v) != np.sign(v.shift(WDAYS))) & v.notna() & v.shift(WDAYS).notna()
    return sign_change.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket O — Lower-OS / higher-OS pattern (mirror of OB) (221-225)
# ============================================================

def f25_rsxh_221_count_lower_OS_troughs_63(close: pd.Series) -> pd.Series:
    """Count of bars in 63d where RSI14 set a lower local-low (compared to RSI 21d-min from 21d ago) — RSI making lower OS troughs (bearish)."""
    rsi = _rsi_wilder(close, 14)
    rsi_min21 = rsi.rolling(MDAYS, min_periods=WDAYS).min()
    return (rsi_min21 < rsi_min21.shift(MDAYS)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f25_rsxh_222_count_lower_OS_troughs_252(close: pd.Series) -> pd.Series:
    """Same lower-OS-trough count over 252d."""
    rsi = _rsi_wilder(close, 14)
    rsi_min21 = rsi.rolling(MDAYS, min_periods=WDAYS).min()
    return (rsi_min21 < rsi_min21.shift(MDAYS)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f25_rsxh_223_higher_OS_troughs_count_63(close: pd.Series) -> pd.Series:
    """Count of bars in 63d where RSI14 21d-min > prior RSI14 21d-min — RSI making higher OS troughs (bullish strengthening)."""
    rsi = _rsi_wilder(close, 14)
    rsi_min21 = rsi.rolling(MDAYS, min_periods=WDAYS).min()
    return (rsi_min21 > rsi_min21.shift(MDAYS)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f25_rsxh_224_higher_OS_troughs_count_252(close: pd.Series) -> pd.Series:
    """Same higher-OS-troughs over 252d."""
    rsi = _rsi_wilder(close, 14)
    rsi_min21 = rsi.rolling(MDAYS, min_periods=WDAYS).min()
    return (rsi_min21 > rsi_min21.shift(MDAYS)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f25_rsxh_225_composite_full_top_signature_weighted_rsi(close: pd.Series) -> pd.Series:
    """Final weighted top: 3 × composite_top + 2 × failure_swing_recent + 1 × disconfirmed_new_high_count + 1 × lower-OB-peaks."""
    a = f25_rsxh_213_composite_rsi_top_signature_252(close).fillna(0)
    b = f25_rsxh_175_rsi14_bearish_failure_swing_indicator(close).rolling(QDAYS, min_periods=MDAYS).max().fillna(0)
    c = f25_rsxh_194_count_rsi_disconfirms_new_high_252(close).fillna(0)
    rsi = _rsi_wilder(close, 14)
    rsi_max21 = rsi.rolling(MDAYS, min_periods=WDAYS).max()
    lower_ob_peaks = (rsi_max21 < rsi_max21.shift(MDAYS)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().fillna(0)
    return 3.0 * a + 2.0 * b + c + lower_ob_peaks


# ============================================================
#                         REGISTRY 151-225
# ============================================================



def f25_rsxh_151_stoch_rsi_14_14_raw_d2(close):
    return f25_rsxh_151_stoch_rsi_14_14_raw(close).diff().diff()


def f25_rsxh_152_stoch_rsi_K_14_14_d2(close):
    return f25_rsxh_152_stoch_rsi_K_14_14(close).diff().diff()


def f25_rsxh_153_stoch_rsi_D_14_14_d2(close):
    return f25_rsxh_153_stoch_rsi_D_14_14(close).diff().diff()


def f25_rsxh_154_stoch_rsi_above_0_8_state_d2(close):
    return f25_rsxh_154_stoch_rsi_above_0_8_state(close).diff().diff()


def f25_rsxh_155_stoch_rsi_below_0_2_state_d2(close):
    return f25_rsxh_155_stoch_rsi_below_0_2_state(close).diff().diff()


def f25_rsxh_156_stoch_rsi_K_D_bearish_cross_event_d2(close):
    return f25_rsxh_156_stoch_rsi_K_D_bearish_cross_event(close).diff().diff()


def f25_rsxh_157_stoch_rsi_bearish_div_63_d2(close):
    return f25_rsxh_157_stoch_rsi_bearish_div_63(close).diff().diff()


def f25_rsxh_158_rsi14_below_30_state_d2(close):
    return f25_rsxh_158_rsi14_below_30_state(close).diff().diff()


def f25_rsxh_159_rsi14_below_20_state_d2(close):
    return f25_rsxh_159_rsi14_below_20_state(close).diff().diff()


def f25_rsxh_160_rsi14_below_10_state_d2(close):
    return f25_rsxh_160_rsi14_below_10_state(close).diff().diff()


def f25_rsxh_161_rsi14_just_exited_os30_d2(close):
    return f25_rsxh_161_rsi14_just_exited_os30(close).diff().diff()


def f25_rsxh_162_rsi14_just_exited_os20_d2(close):
    return f25_rsxh_162_rsi14_just_exited_os20(close).diff().diff()


def f25_rsxh_163_bars_since_rsi14_os30_exit_d2(close):
    return f25_rsxh_163_bars_since_rsi14_os30_exit(close).diff().diff()


def f25_rsxh_164_count_rsi14_os30_exits_252_d2(close):
    return f25_rsxh_164_count_rsi14_os30_exits_252(close).diff().diff()


def f25_rsxh_165_fraction_rsi14_os30_past_63_d2(close):
    return f25_rsxh_165_fraction_rsi14_os30_past_63(close).diff().diff()


def f25_rsxh_166_cumulative_os30_area_252_d2(close):
    return f25_rsxh_166_cumulative_os30_area_252(close).diff().diff()


def f25_rsxh_167_longest_rsi14_os30_run_252_d2(close):
    return f25_rsxh_167_longest_rsi14_os30_run_252(close).diff().diff()


def f25_rsxh_168_price_vs_rsi14_bull_div_63_d2(close):
    return f25_rsxh_168_price_vs_rsi14_bull_div_63(close).diff().diff()


def f25_rsxh_169_price_vs_rsi14_bull_div_252_d2(close):
    return f25_rsxh_169_price_vs_rsi14_bull_div_252(close).diff().diff()


def f25_rsxh_170_count_bullish_rsi_div_63_d2(close):
    return f25_rsxh_170_count_bullish_rsi_div_63(close).diff().diff()


def f25_rsxh_171_count_bullish_rsi_div_252_d2(close):
    return f25_rsxh_171_count_bullish_rsi_div_252(close).diff().diff()


def f25_rsxh_172_bars_since_last_bullish_rsi_div_63_d2(close):
    return f25_rsxh_172_bars_since_last_bullish_rsi_div_63(close).diff().diff()


def f25_rsxh_173_hidden_bullish_div_63_d2(close):
    return f25_rsxh_173_hidden_bullish_div_63(close).diff().diff()


def f25_rsxh_174_triple_bullish_div_within_63_d2(close):
    return f25_rsxh_174_triple_bullish_div_within_63(close).diff().diff()


def f25_rsxh_175_rsi14_bearish_failure_swing_indicator_d2(close):
    return f25_rsxh_175_rsi14_bearish_failure_swing_indicator(close).diff().diff()


def f25_rsxh_176_rsi14_bullish_failure_swing_indicator_d2(close):
    return f25_rsxh_176_rsi14_bullish_failure_swing_indicator(close).diff().diff()


def f25_rsxh_177_count_bearish_failure_swings_252_d2(close):
    return f25_rsxh_177_count_bearish_failure_swings_252(close).diff().diff()


def f25_rsxh_178_count_bullish_failure_swings_252_d2(close):
    return f25_rsxh_178_count_bullish_failure_swings_252(close).diff().diff()


def f25_rsxh_179_rsi14_dynamic_ob_band_q90_252_d2(close):
    return f25_rsxh_179_rsi14_dynamic_ob_band_q90_252(close).diff().diff()


def f25_rsxh_180_rsi14_above_dynamic_ob_indicator_d2(close):
    return f25_rsxh_180_rsi14_above_dynamic_ob_indicator(close).diff().diff()


def f25_rsxh_181_rsi14_dynamic_os_band_q10_252_d2(close):
    return f25_rsxh_181_rsi14_dynamic_os_band_q10_252(close).diff().diff()


def f25_rsxh_182_rsi14_below_dynamic_os_indicator_d2(close):
    return f25_rsxh_182_rsi14_below_dynamic_os_indicator(close).diff().diff()


def f25_rsxh_183_dynamic_ob_band_width_252_d2(close):
    return f25_rsxh_183_dynamic_ob_band_width_252(close).diff().diff()


def f25_rsxh_184_rsi14_bb_upper_21_d2(close):
    return f25_rsxh_184_rsi14_bb_upper_21(close).diff().diff()


def f25_rsxh_185_rsi14_bb_lower_21_d2(close):
    return f25_rsxh_185_rsi14_bb_lower_21(close).diff().diff()


def f25_rsxh_186_rsi14_above_bb_upper_indicator_d2(close):
    return f25_rsxh_186_rsi14_above_bb_upper_indicator(close).diff().diff()


def f25_rsxh_187_rsi14_bb_width_zscore_252_d2(close):
    return f25_rsxh_187_rsi14_bb_width_zscore_252(close).diff().diff()


def f25_rsxh_188_laguerre_rsi_gamma_05_d2(close):
    return f25_rsxh_188_laguerre_rsi_gamma_05(close).diff().diff()


def f25_rsxh_189_laguerre_rsi_above_85_state_d2(close):
    return f25_rsxh_189_laguerre_rsi_above_85_state(close).diff().diff()


def f25_rsxh_190_laguerre_rsi_above_85_just_exited_d2(close):
    return f25_rsxh_190_laguerre_rsi_above_85_just_exited(close).diff().diff()


def f25_rsxh_191_laguerre_rsi_zscore_252_d2(close):
    return f25_rsxh_191_laguerre_rsi_zscore_252(close).diff().diff()


def f25_rsxh_192_rsi_confirms_new_high_indicator_d2(close):
    return f25_rsxh_192_rsi_confirms_new_high_indicator(close).diff().diff()


def f25_rsxh_193_rsi_disconfirms_new_high_indicator_d2(close):
    return f25_rsxh_193_rsi_disconfirms_new_high_indicator(close).diff().diff()


def f25_rsxh_194_count_rsi_disconfirms_new_high_252_d2(close):
    return f25_rsxh_194_count_rsi_disconfirms_new_high_252(close).diff().diff()


def f25_rsxh_195_rsi_confirms_new_low_indicator_d2(close):
    return f25_rsxh_195_rsi_confirms_new_low_indicator(close).diff().diff()


def f25_rsxh_196_rsi_std_compression_short_long_ratio_d2(close):
    return f25_rsxh_196_rsi_std_compression_short_long_ratio(close).diff().diff()


def f25_rsxh_197_multi_horizon_rsi_consensus_OB_count_d2(close):
    return f25_rsxh_197_multi_horizon_rsi_consensus_OB_count(close).diff().diff()


def f25_rsxh_198_multi_horizon_rsi_consensus_OS_count_d2(close):
    return f25_rsxh_198_multi_horizon_rsi_consensus_OS_count(close).diff().diff()


def f25_rsxh_199_rsi_horizon_disagreement_max_minus_min_d2(close):
    return f25_rsxh_199_rsi_horizon_disagreement_max_minus_min(close).diff().diff()


def f25_rsxh_200_rsi_horizon_alignment_score_d2(close):
    return f25_rsxh_200_rsi_horizon_alignment_score(close).diff().diff()


def f25_rsxh_201_rsi_bb_squeeze_indicator_d2(close):
    return f25_rsxh_201_rsi_bb_squeeze_indicator(close).diff().diff()


def f25_rsxh_202_rsi_bb_squeeze_count_252_d2(close):
    return f25_rsxh_202_rsi_bb_squeeze_count_252(close).diff().diff()


def f25_rsxh_203_bars_since_rsi_bb_squeeze_release_d2(close):
    return f25_rsxh_203_bars_since_rsi_bb_squeeze_release(close).diff().diff()


def f25_rsxh_204_heikin_ashi_close_d2(open_, high, low, close):
    return f25_rsxh_204_heikin_ashi_close(open_, high, low, close).diff().diff()


def f25_rsxh_205_rsi14_of_heikin_ashi_close_d2(open_, high, low, close):
    return f25_rsxh_205_rsi14_of_heikin_ashi_close(open_, high, low, close).diff().diff()


def f25_rsxh_206_ha_rsi_above_70_state_d2(open_, high, low, close):
    return f25_rsxh_206_ha_rsi_above_70_state(open_, high, low, close).diff().diff()


def f25_rsxh_207_rsi_mid_band_normalized_d2(close):
    return f25_rsxh_207_rsi_mid_band_normalized(close).diff().diff()


def f25_rsxh_208_rsi_mid_band_zscore_252_d2(close):
    return f25_rsxh_208_rsi_mid_band_zscore_252(close).diff().diff()


def f25_rsxh_209_rsi_mid_band_dwell_negative_63_d2(close):
    return f25_rsxh_209_rsi_mid_band_dwell_negative_63(close).diff().diff()


def f25_rsxh_210_weekly_rsi_proxy_14_d2(close):
    return f25_rsxh_210_weekly_rsi_proxy_14(close).diff().diff()


def f25_rsxh_211_weekly_rsi_above_70_state_d2(close):
    return f25_rsxh_211_weekly_rsi_above_70_state(close).diff().diff()


def f25_rsxh_212_monthly_rsi_proxy_14_d2(close):
    return f25_rsxh_212_monthly_rsi_proxy_14(close).diff().diff()


def f25_rsxh_213_composite_rsi_top_signature_252_d2(close):
    return f25_rsxh_213_composite_rsi_top_signature_252(close).diff().diff()


def f25_rsxh_214_composite_rsi_bottom_signature_252_d2(close):
    return f25_rsxh_214_composite_rsi_bottom_signature_252(close).diff().diff()


def f25_rsxh_215_rsi_phase_classifier_252_d2(close):
    return f25_rsxh_215_rsi_phase_classifier_252(close).diff().diff()


def f25_rsxh_216_rsi_regime_persistence_score_252_d2(close):
    return f25_rsxh_216_rsi_regime_persistence_score_252(close).diff().diff()


def f25_rsxh_217_rsi_OB_OS_imbalance_252_d2(close):
    return f25_rsxh_217_rsi_OB_OS_imbalance_252(close).diff().diff()


def f25_rsxh_218_rsi_quality_score_at_new_high_252_d2(close):
    return f25_rsxh_218_rsi_quality_score_at_new_high_252(close).diff().diff()


def f25_rsxh_219_count_failed_OB_breakouts_252_d2(close):
    return f25_rsxh_219_count_failed_OB_breakouts_252(close).diff().diff()


def f25_rsxh_220_rsi_acceleration_change_event_count_252_d2(close):
    return f25_rsxh_220_rsi_acceleration_change_event_count_252(close).diff().diff()


def f25_rsxh_221_count_lower_OS_troughs_63_d2(close):
    return f25_rsxh_221_count_lower_OS_troughs_63(close).diff().diff()


def f25_rsxh_222_count_lower_OS_troughs_252_d2(close):
    return f25_rsxh_222_count_lower_OS_troughs_252(close).diff().diff()


def f25_rsxh_223_higher_OS_troughs_count_63_d2(close):
    return f25_rsxh_223_higher_OS_troughs_count_63(close).diff().diff()


def f25_rsxh_224_higher_OS_troughs_count_252_d2(close):
    return f25_rsxh_224_higher_OS_troughs_count_252(close).diff().diff()


def f25_rsxh_225_composite_full_top_signature_weighted_rsi_d2(close):
    return f25_rsxh_225_composite_full_top_signature_weighted_rsi(close).diff().diff()


RSI_EXHAUSTION_FAMILY_D2_REGISTRY_151_225 = {
    "f25_rsxh_151_stoch_rsi_14_14_raw_d2": {"inputs": ["close"], "func": f25_rsxh_151_stoch_rsi_14_14_raw_d2},
    "f25_rsxh_152_stoch_rsi_K_14_14_d2": {"inputs": ["close"], "func": f25_rsxh_152_stoch_rsi_K_14_14_d2},
    "f25_rsxh_153_stoch_rsi_D_14_14_d2": {"inputs": ["close"], "func": f25_rsxh_153_stoch_rsi_D_14_14_d2},
    "f25_rsxh_154_stoch_rsi_above_0_8_state_d2": {"inputs": ["close"], "func": f25_rsxh_154_stoch_rsi_above_0_8_state_d2},
    "f25_rsxh_155_stoch_rsi_below_0_2_state_d2": {"inputs": ["close"], "func": f25_rsxh_155_stoch_rsi_below_0_2_state_d2},
    "f25_rsxh_156_stoch_rsi_K_D_bearish_cross_event_d2": {"inputs": ["close"], "func": f25_rsxh_156_stoch_rsi_K_D_bearish_cross_event_d2},
    "f25_rsxh_157_stoch_rsi_bearish_div_63_d2": {"inputs": ["close"], "func": f25_rsxh_157_stoch_rsi_bearish_div_63_d2},
    "f25_rsxh_158_rsi14_below_30_state_d2": {"inputs": ["close"], "func": f25_rsxh_158_rsi14_below_30_state_d2},
    "f25_rsxh_159_rsi14_below_20_state_d2": {"inputs": ["close"], "func": f25_rsxh_159_rsi14_below_20_state_d2},
    "f25_rsxh_160_rsi14_below_10_state_d2": {"inputs": ["close"], "func": f25_rsxh_160_rsi14_below_10_state_d2},
    "f25_rsxh_161_rsi14_just_exited_os30_d2": {"inputs": ["close"], "func": f25_rsxh_161_rsi14_just_exited_os30_d2},
    "f25_rsxh_162_rsi14_just_exited_os20_d2": {"inputs": ["close"], "func": f25_rsxh_162_rsi14_just_exited_os20_d2},
    "f25_rsxh_163_bars_since_rsi14_os30_exit_d2": {"inputs": ["close"], "func": f25_rsxh_163_bars_since_rsi14_os30_exit_d2},
    "f25_rsxh_164_count_rsi14_os30_exits_252_d2": {"inputs": ["close"], "func": f25_rsxh_164_count_rsi14_os30_exits_252_d2},
    "f25_rsxh_165_fraction_rsi14_os30_past_63_d2": {"inputs": ["close"], "func": f25_rsxh_165_fraction_rsi14_os30_past_63_d2},
    "f25_rsxh_166_cumulative_os30_area_252_d2": {"inputs": ["close"], "func": f25_rsxh_166_cumulative_os30_area_252_d2},
    "f25_rsxh_167_longest_rsi14_os30_run_252_d2": {"inputs": ["close"], "func": f25_rsxh_167_longest_rsi14_os30_run_252_d2},
    "f25_rsxh_168_price_vs_rsi14_bull_div_63_d2": {"inputs": ["close"], "func": f25_rsxh_168_price_vs_rsi14_bull_div_63_d2},
    "f25_rsxh_169_price_vs_rsi14_bull_div_252_d2": {"inputs": ["close"], "func": f25_rsxh_169_price_vs_rsi14_bull_div_252_d2},
    "f25_rsxh_170_count_bullish_rsi_div_63_d2": {"inputs": ["close"], "func": f25_rsxh_170_count_bullish_rsi_div_63_d2},
    "f25_rsxh_171_count_bullish_rsi_div_252_d2": {"inputs": ["close"], "func": f25_rsxh_171_count_bullish_rsi_div_252_d2},
    "f25_rsxh_172_bars_since_last_bullish_rsi_div_63_d2": {"inputs": ["close"], "func": f25_rsxh_172_bars_since_last_bullish_rsi_div_63_d2},
    "f25_rsxh_173_hidden_bullish_div_63_d2": {"inputs": ["close"], "func": f25_rsxh_173_hidden_bullish_div_63_d2},
    "f25_rsxh_174_triple_bullish_div_within_63_d2": {"inputs": ["close"], "func": f25_rsxh_174_triple_bullish_div_within_63_d2},
    "f25_rsxh_175_rsi14_bearish_failure_swing_indicator_d2": {"inputs": ["close"], "func": f25_rsxh_175_rsi14_bearish_failure_swing_indicator_d2},
    "f25_rsxh_176_rsi14_bullish_failure_swing_indicator_d2": {"inputs": ["close"], "func": f25_rsxh_176_rsi14_bullish_failure_swing_indicator_d2},
    "f25_rsxh_177_count_bearish_failure_swings_252_d2": {"inputs": ["close"], "func": f25_rsxh_177_count_bearish_failure_swings_252_d2},
    "f25_rsxh_178_count_bullish_failure_swings_252_d2": {"inputs": ["close"], "func": f25_rsxh_178_count_bullish_failure_swings_252_d2},
    "f25_rsxh_179_rsi14_dynamic_ob_band_q90_252_d2": {"inputs": ["close"], "func": f25_rsxh_179_rsi14_dynamic_ob_band_q90_252_d2},
    "f25_rsxh_180_rsi14_above_dynamic_ob_indicator_d2": {"inputs": ["close"], "func": f25_rsxh_180_rsi14_above_dynamic_ob_indicator_d2},
    "f25_rsxh_181_rsi14_dynamic_os_band_q10_252_d2": {"inputs": ["close"], "func": f25_rsxh_181_rsi14_dynamic_os_band_q10_252_d2},
    "f25_rsxh_182_rsi14_below_dynamic_os_indicator_d2": {"inputs": ["close"], "func": f25_rsxh_182_rsi14_below_dynamic_os_indicator_d2},
    "f25_rsxh_183_dynamic_ob_band_width_252_d2": {"inputs": ["close"], "func": f25_rsxh_183_dynamic_ob_band_width_252_d2},
    "f25_rsxh_184_rsi14_bb_upper_21_d2": {"inputs": ["close"], "func": f25_rsxh_184_rsi14_bb_upper_21_d2},
    "f25_rsxh_185_rsi14_bb_lower_21_d2": {"inputs": ["close"], "func": f25_rsxh_185_rsi14_bb_lower_21_d2},
    "f25_rsxh_186_rsi14_above_bb_upper_indicator_d2": {"inputs": ["close"], "func": f25_rsxh_186_rsi14_above_bb_upper_indicator_d2},
    "f25_rsxh_187_rsi14_bb_width_zscore_252_d2": {"inputs": ["close"], "func": f25_rsxh_187_rsi14_bb_width_zscore_252_d2},
    "f25_rsxh_188_laguerre_rsi_gamma_05_d2": {"inputs": ["close"], "func": f25_rsxh_188_laguerre_rsi_gamma_05_d2},
    "f25_rsxh_189_laguerre_rsi_above_85_state_d2": {"inputs": ["close"], "func": f25_rsxh_189_laguerre_rsi_above_85_state_d2},
    "f25_rsxh_190_laguerre_rsi_above_85_just_exited_d2": {"inputs": ["close"], "func": f25_rsxh_190_laguerre_rsi_above_85_just_exited_d2},
    "f25_rsxh_191_laguerre_rsi_zscore_252_d2": {"inputs": ["close"], "func": f25_rsxh_191_laguerre_rsi_zscore_252_d2},
    "f25_rsxh_192_rsi_confirms_new_high_indicator_d2": {"inputs": ["close"], "func": f25_rsxh_192_rsi_confirms_new_high_indicator_d2},
    "f25_rsxh_193_rsi_disconfirms_new_high_indicator_d2": {"inputs": ["close"], "func": f25_rsxh_193_rsi_disconfirms_new_high_indicator_d2},
    "f25_rsxh_194_count_rsi_disconfirms_new_high_252_d2": {"inputs": ["close"], "func": f25_rsxh_194_count_rsi_disconfirms_new_high_252_d2},
    "f25_rsxh_195_rsi_confirms_new_low_indicator_d2": {"inputs": ["close"], "func": f25_rsxh_195_rsi_confirms_new_low_indicator_d2},
    "f25_rsxh_196_rsi_std_compression_short_long_ratio_d2": {"inputs": ["close"], "func": f25_rsxh_196_rsi_std_compression_short_long_ratio_d2},
    "f25_rsxh_197_multi_horizon_rsi_consensus_OB_count_d2": {"inputs": ["close"], "func": f25_rsxh_197_multi_horizon_rsi_consensus_OB_count_d2},
    "f25_rsxh_198_multi_horizon_rsi_consensus_OS_count_d2": {"inputs": ["close"], "func": f25_rsxh_198_multi_horizon_rsi_consensus_OS_count_d2},
    "f25_rsxh_199_rsi_horizon_disagreement_max_minus_min_d2": {"inputs": ["close"], "func": f25_rsxh_199_rsi_horizon_disagreement_max_minus_min_d2},
    "f25_rsxh_200_rsi_horizon_alignment_score_d2": {"inputs": ["close"], "func": f25_rsxh_200_rsi_horizon_alignment_score_d2},
    "f25_rsxh_201_rsi_bb_squeeze_indicator_d2": {"inputs": ["close"], "func": f25_rsxh_201_rsi_bb_squeeze_indicator_d2},
    "f25_rsxh_202_rsi_bb_squeeze_count_252_d2": {"inputs": ["close"], "func": f25_rsxh_202_rsi_bb_squeeze_count_252_d2},
    "f25_rsxh_203_bars_since_rsi_bb_squeeze_release_d2": {"inputs": ["close"], "func": f25_rsxh_203_bars_since_rsi_bb_squeeze_release_d2},
    "f25_rsxh_204_heikin_ashi_close_d2": {"inputs": ["open", "high", "low", "close"], "func": f25_rsxh_204_heikin_ashi_close_d2},
    "f25_rsxh_205_rsi14_of_heikin_ashi_close_d2": {"inputs": ["open", "high", "low", "close"], "func": f25_rsxh_205_rsi14_of_heikin_ashi_close_d2},
    "f25_rsxh_206_ha_rsi_above_70_state_d2": {"inputs": ["open", "high", "low", "close"], "func": f25_rsxh_206_ha_rsi_above_70_state_d2},
    "f25_rsxh_207_rsi_mid_band_normalized_d2": {"inputs": ["close"], "func": f25_rsxh_207_rsi_mid_band_normalized_d2},
    "f25_rsxh_208_rsi_mid_band_zscore_252_d2": {"inputs": ["close"], "func": f25_rsxh_208_rsi_mid_band_zscore_252_d2},
    "f25_rsxh_209_rsi_mid_band_dwell_negative_63_d2": {"inputs": ["close"], "func": f25_rsxh_209_rsi_mid_band_dwell_negative_63_d2},
    "f25_rsxh_210_weekly_rsi_proxy_14_d2": {"inputs": ["close"], "func": f25_rsxh_210_weekly_rsi_proxy_14_d2},
    "f25_rsxh_211_weekly_rsi_above_70_state_d2": {"inputs": ["close"], "func": f25_rsxh_211_weekly_rsi_above_70_state_d2},
    "f25_rsxh_212_monthly_rsi_proxy_14_d2": {"inputs": ["close"], "func": f25_rsxh_212_monthly_rsi_proxy_14_d2},
    "f25_rsxh_213_composite_rsi_top_signature_252_d2": {"inputs": ["close"], "func": f25_rsxh_213_composite_rsi_top_signature_252_d2},
    "f25_rsxh_214_composite_rsi_bottom_signature_252_d2": {"inputs": ["close"], "func": f25_rsxh_214_composite_rsi_bottom_signature_252_d2},
    "f25_rsxh_215_rsi_phase_classifier_252_d2": {"inputs": ["close"], "func": f25_rsxh_215_rsi_phase_classifier_252_d2},
    "f25_rsxh_216_rsi_regime_persistence_score_252_d2": {"inputs": ["close"], "func": f25_rsxh_216_rsi_regime_persistence_score_252_d2},
    "f25_rsxh_217_rsi_OB_OS_imbalance_252_d2": {"inputs": ["close"], "func": f25_rsxh_217_rsi_OB_OS_imbalance_252_d2},
    "f25_rsxh_218_rsi_quality_score_at_new_high_252_d2": {"inputs": ["close"], "func": f25_rsxh_218_rsi_quality_score_at_new_high_252_d2},
    "f25_rsxh_219_count_failed_OB_breakouts_252_d2": {"inputs": ["close"], "func": f25_rsxh_219_count_failed_OB_breakouts_252_d2},
    "f25_rsxh_220_rsi_acceleration_change_event_count_252_d2": {"inputs": ["close"], "func": f25_rsxh_220_rsi_acceleration_change_event_count_252_d2},
    "f25_rsxh_221_count_lower_OS_troughs_63_d2": {"inputs": ["close"], "func": f25_rsxh_221_count_lower_OS_troughs_63_d2},
    "f25_rsxh_222_count_lower_OS_troughs_252_d2": {"inputs": ["close"], "func": f25_rsxh_222_count_lower_OS_troughs_252_d2},
    "f25_rsxh_223_higher_OS_troughs_count_63_d2": {"inputs": ["close"], "func": f25_rsxh_223_higher_OS_troughs_count_63_d2},
    "f25_rsxh_224_higher_OS_troughs_count_252_d2": {"inputs": ["close"], "func": f25_rsxh_224_higher_OS_troughs_count_252_d2},
    "f25_rsxh_225_composite_full_top_signature_weighted_rsi_d2": {"inputs": ["close"], "func": f25_rsxh_225_composite_full_top_signature_weighted_rsi_d2},
}
