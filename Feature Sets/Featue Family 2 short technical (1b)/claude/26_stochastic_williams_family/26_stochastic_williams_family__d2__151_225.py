"""stochastic_williams_family d2 features 151-225 — Pipeline 1b-technical.

75 distinct "modern oscillator" hypotheses extending 001-150. Themes:
Schaff Trend Cycle (151-160), Awesome Osc + Accelerator (161-170),
Fisher / Inverse Fisher Transform (171-178), Connors RSI (179-184),
Bollinger %B / Donchian %B (185-192), Relative Vigor Index (193-200),
Adaptive smoothed stochastic variants (201-210),
Bollinger Bands on stoch + Keltner (211-218),
Cross-oscillator composites (219-225).

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


def _stc(close, fast=23, slow=50, cycle=10, factor=0.5):
    """Schaff Trend Cycle of MACD line. Two rounds of stoch-smoothing on MACD.
    Recursive smoothing approximated with EMA blending using factor."""
    macd = _ema(close, fast) - _ema(close, slow)
    # Round 1: stoch of MACD over cycle
    ll = macd.rolling(cycle, min_periods=max(cycle // 3, 2)).min()
    hh = macd.rolling(cycle, min_periods=max(cycle // 3, 2)).max()
    k1 = 100.0 * _safe_div(macd - ll, hh - ll)
    # blend (recursive smoothing)
    d1 = k1.ewm(alpha=factor, adjust=False, min_periods=max(cycle // 2, 2)).mean()
    # Round 2: stoch of d1
    ll2 = d1.rolling(cycle, min_periods=max(cycle // 3, 2)).min()
    hh2 = d1.rolling(cycle, min_periods=max(cycle // 3, 2)).max()
    k2 = 100.0 * _safe_div(d1 - ll2, hh2 - ll2)
    stc = k2.ewm(alpha=factor, adjust=False, min_periods=max(cycle // 2, 2)).mean()
    return stc


def _awesome_osc(high, low):
    mp = (high + low) / 2.0
    return mp.rolling(5, min_periods=3).mean() - mp.rolling(34, min_periods=11).mean()


def _ac_osc(high, low):
    ao = _awesome_osc(high, low)
    return ao - ao.rolling(5, min_periods=3).mean()


def _fisher_transform(close, n=10):
    """Ehlers Fisher Transform on price-normalized [-1,1] index using rolling high/low."""
    ll = close.rolling(n, min_periods=max(n // 3, 2)).min()
    hh = close.rolling(n, min_periods=max(n // 3, 2)).max()
    rng = (hh - ll).replace(0, np.nan)
    raw = 2.0 * (close - ll) / rng - 1.0
    # bound and smooth recursively (EMA with alpha 0.33)
    x = raw.clip(-0.999, 0.999).ewm(alpha=0.33, adjust=False, min_periods=max(n // 3, 2)).mean().clip(-0.999, 0.999)
    return 0.5 * np.log((1.0 + x) / (1.0 - x))


def _inverse_fisher(s, scale=0.1):
    """Inverse Fisher Transform: (e^2x - 1) / (e^2x + 1), with input scaled to [-1,1] range."""
    x = (scale * s).clip(-10.0, 10.0)
    e = np.exp(2.0 * x)
    return (e - 1.0) / (e + 1.0)


def _wma(s, n):
    """Weighted moving average. Weights grow linearly from 1 at oldest to n at newest."""
    if n < 1:
        return pd.Series(np.nan, index=s.index)
    w = np.arange(1, n + 1, dtype=float)
    def _f(a):
        if a.size != n:
            return np.nan
        valid = ~np.isnan(a)
        if valid.sum() < max(n // 3, 2):
            return np.nan
        if not valid.all():
            return float(np.nansum(a * w) / w[valid].sum())
        return float((a * w).sum() / w.sum())
    return s.rolling(n, min_periods=n).apply(_f, raw=True)


def _hma(s, n):
    """Hull MA."""
    half = max(int(n // 2), 1)
    sqn = max(int(np.sqrt(n)), 1)
    return _wma(2.0 * _wma(s, half) - _wma(s, n), sqn)


def _dema(s, n):
    e = _ema(s, n)
    return 2.0 * e - _ema(e, n)


def _tema(s, n):
    e = _ema(s, n)
    e2 = _ema(e, n)
    return 3.0 * e - 3.0 * e2 + _ema(e2, n)


def _kama(s, n=10, fast=2, slow=30):
    ch = (s - s.shift(n)).abs()
    vol = s.diff().abs().rolling(n, min_periods=max(n // 3, 2)).sum()
    er = _safe_div(ch, vol).clip(0.0, 1.0)
    fc = 2.0 / (fast + 1.0)
    sc = 2.0 / (slow + 1.0)
    alpha = (er * (fc - sc) + sc) ** 2
    out = pd.Series(np.nan, index=s.index)
    prev = np.nan
    s_arr = s.to_numpy()
    a_arr = alpha.to_numpy()
    for i in range(s.size):
        v = s_arr[i]
        a = a_arr[i]
        if np.isnan(prev):
            if not np.isnan(v) and not np.isnan(a):
                prev = v
                out.iloc[i] = v
        else:
            if not np.isnan(v) and not np.isnan(a):
                prev = prev + a * (v - prev)
                out.iloc[i] = prev
            else:
                out.iloc[i] = prev
    return out


def _zlema(s, n):
    lag = int((n - 1) // 2)
    adj = 2.0 * s - s.shift(lag)
    return _ema(adj, n)


def _ha_close(open_s, high, low, close):
    return (open_s + high + low + close) / 4.0


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


def _connors_rsi(close, n_rsi=3, n_streak=2, n_rank=100):
    r1 = _rsi(close, n_rsi)
    # streak signed length
    dp = close.diff()
    sign = np.sign(dp)
    streak = pd.Series(0.0, index=close.index)
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
        streak.iloc[i] = cur
    r2 = _rsi(streak, n_streak)
    # percent rank of 1d returns over n_rank
    ret = close.pct_change()
    pr = _pct_rank(ret, n_rank, min_periods=max(n_rank // 4, 5)) * 100.0
    return (r1 + r2 + pr) / 3.0


def _consec_streak_dir(s, positive=True):
    """Consecutive count of bars where sign(diff(s)) matches direction."""
    sg = np.sign(s.diff())
    if positive:
        m = sg > 0
    else:
        m = sg < 0
    return _streak_true(m)


def _swma4(s):
    """Sym-weighted MA over 4 bars: (a + 2b + 2c + d) / 6, weights at lags 3,2,1,0."""
    return (s + 2.0 * s.shift(1) + 2.0 * s.shift(2) + s.shift(3)) / 6.0


def _rvi(open_s, high, low, close, n=10):
    num = _swma4(close - open_s).rolling(n, min_periods=max(n // 3, 2)).mean()
    den = _swma4(high - low).rolling(n, min_periods=max(n // 3, 2)).mean()
    return _safe_div(num, den)


# ============================================================
# Schaff Trend Cycle (151-160)
# ============================================================


def f26_stwf_151_stc_classical_23_50_10_d2(close: pd.Series) -> pd.Series:
    """Schaff Trend Cycle (23/50/10) — level of double-stochastic MACD."""
    return (_stc(close)).diff().diff()


def f26_stwf_152_stc_signal_bearish_cross_indicator_d2(close: pd.Series) -> pd.Series:
    """1 if STC crossed below its EMA(3) signal this bar — STC bearish cross."""
    s = _stc(close)
    sig = _ema(s, 3)
    diff = s - sig
    return (((diff.shift(1) > 0) & (diff <= 0)).astype(float).where(diff.notna(), np.nan)).diff().diff()


def f26_stwf_153_stc_above_75_state_d2(close: pd.Series) -> pd.Series:
    """1 if STC > 75 — STC OB regime."""
    s = _stc(close)
    return ((s > 75.0).astype(float).where(s.notna(), np.nan)).diff().diff()


def f26_stwf_154_stc_just_exited_above_75_d2(close: pd.Series) -> pd.Series:
    """1 if STC just crossed back below 75 — STC OB-exit trigger."""
    s = _stc(close)
    return (((s.shift(1) > 75.0) & (s <= 75.0)).astype(float).where(s.notna(), np.nan)).diff().diff()


def f26_stwf_155_stc_dwell_above_75_63_d2(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with STC > 75 — STC OB dwell."""
    s = _stc(close)
    return ((s > 75.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(s.notna(), np.nan)).diff().diff()


def f26_stwf_156_stc_div_vs_price_63_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish divergence: new 63d high in price but STC below prior 63d STC max."""
    s = _stc(close)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    s_below = s < s.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_new & s_below).astype(float).where(s.notna(), np.nan)).diff().diff()


def f26_stwf_157_stc_bars_since_252_max_d2(close: pd.Series) -> pd.Series:
    """Bars since STC hit its 252d max — recency of STC peak."""
    s = _stc(close)
    at_max = s == s.rolling(YDAYS, min_periods=QDAYS).max()
    return (_bars_since_true(at_max)).diff().diff()


def f26_stwf_158_stc_zscore_252_d2(close: pd.Series) -> pd.Series:
    """Z-score of STC over 252 bars."""
    return (_rolling_zscore(_stc(close), YDAYS, min_periods=QDAYS)).diff().diff()


def f26_stwf_159_stc_peak_decay_63_d2(close: pd.Series) -> pd.Series:
    """STC 63d max minus its value 63 bars ago — quarterly STC peak decay."""
    s = _stc(close)
    pmax = s.rolling(QDAYS, min_periods=MDAYS).max()
    return (pmax - pmax.shift(QDAYS)).diff().diff()


def f26_stwf_160_stc_persistence_above_zero_252_d2(close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars where STC > 50 (midline) — long-term bullish-regime persistence."""
    s = _stc(close)
    return ((s > 50.0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(s.notna(), np.nan)).diff().diff()


def f26_stwf_161_ao_5_34_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bill Williams Awesome Oscillator: SMA5 - SMA34 on median price."""
    return (_awesome_osc(high, low)).diff().diff()


def f26_stwf_162_ao_above_zero_state_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 if AO > 0 — AO bullish regime."""
    ao = _awesome_osc(high, low)
    return ((ao > 0).astype(float).where(ao.notna(), np.nan)).diff().diff()


def f26_stwf_163_ao_zero_cross_down_indicator_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 if AO crossed below 0 this bar — AO zero-cross down."""
    ao = _awesome_osc(high, low)
    return (((ao.shift(1) > 0) & (ao <= 0)).astype(float).where(ao.notna(), np.nan)).diff().diff()


def f26_stwf_164_ao_div_vs_price_63_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bearish divergence using AO: new 63d price high but AO below prior 63d AO max."""
    ao = _awesome_osc(high, low)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    ao_below = ao < ao.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_new & ao_below).astype(float).where(ao.notna(), np.nan)).diff().diff()


def f26_stwf_165_ao_zscore_252_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of AO over trailing 252 bars."""
    return (_rolling_zscore(_awesome_osc(high, low), YDAYS, min_periods=QDAYS)).diff().diff()


def f26_stwf_166_ac_oscillator_5_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bill Williams Accelerator Oscillator: AO - SMA5(AO)."""
    return (_ac_osc(high, low)).diff().diff()


def f26_stwf_167_ac_above_zero_state_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 if AC > 0 — accelerator bullish."""
    ac = _ac_osc(high, low)
    return ((ac > 0).astype(float).where(ac.notna(), np.nan)).diff().diff()


def f26_stwf_168_ac_zero_cross_down_indicator_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """1 if AC crossed below 0 this bar — AC zero-cross down."""
    ac = _ac_osc(high, low)
    return (((ac.shift(1) > 0) & (ac <= 0)).astype(float).where(ac.notna(), np.nan)).diff().diff()


def f26_stwf_169_ac_consecutive_red_bars_streak_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive count of bars where AC declined — bear momentum streak."""
    ac = _ac_osc(high, low)
    return (_streak_true(ac.diff() < 0).where(ac.notna(), np.nan)).diff().diff()


def f26_stwf_170_ac_bars_since_252_max_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars since AC hit its 252d max."""
    ac = _ac_osc(high, low)
    at_max = ac == ac.rolling(YDAYS, min_periods=QDAYS).max()
    return (_bars_since_true(at_max)).diff().diff()


def f26_stwf_171_fisher_transform_price_10_d2(close: pd.Series) -> pd.Series:
    """Ehlers Fisher Transform of price-normalized index, n=10."""
    return (_fisher_transform(close, 10)).diff().diff()


def f26_stwf_172_fisher_transform_zero_cross_down_d2(close: pd.Series) -> pd.Series:
    """1 if Fisher Transform crossed below 0 this bar."""
    f = _fisher_transform(close, 10)
    return (((f.shift(1) > 0) & (f <= 0)).astype(float).where(f.notna(), np.nan)).diff().diff()


def f26_stwf_173_inverse_fisher_transform_stoch_14_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Inverse Fisher Transform of (stoch %K - 50) scaled — IFT-stoch level in [-1,1]."""
    k = _stoch_k(high, low, close, 14)
    return (_inverse_fisher(k - 50.0, scale=0.1)).diff().diff()


def f26_stwf_174_ift_stoch_above_05_state_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if IFT-stoch > 0.5 — IFT-stoch OB regime."""
    ift = _inverse_fisher(_stoch_k(high, low, close, 14) - 50.0, scale=0.1)
    return ((ift > 0.5).astype(float).where(ift.notna(), np.nan)).diff().diff()


def f26_stwf_175_ift_stoch_just_exited_above_05_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if IFT-stoch just dropped back below 0.5 — IFT OB-exit."""
    ift = _inverse_fisher(_stoch_k(high, low, close, 14) - 50.0, scale=0.1)
    return (((ift.shift(1) > 0.5) & (ift <= 0.5)).astype(float).where(ift.notna(), np.nan)).diff().diff()


def f26_stwf_176_ift_williams_r_14_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Inverse Fisher Transform of Williams %R(14) (mapped to [-1,1] domain via /50 + 1)."""
    wr = _williams_r(high, low, close, 14)
    # wr in [-100, 0] => shift to [-50, 50] then scale
    return (_inverse_fisher(wr + 50.0, scale=0.1)).diff().diff()


def f26_stwf_177_ift_williams_r_above_05_state_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if IFT-Williams > 0.5 — IFT-WR OB regime."""
    ift = _inverse_fisher(_williams_r(high, low, close, 14) + 50.0, scale=0.1)
    return ((ift > 0.5).astype(float).where(ift.notna(), np.nan)).diff().diff()


def f26_stwf_178_ift_williams_r_bars_since_252_max_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since IFT-WR hit 252d max — recency of IFT-WR peak."""
    ift = _inverse_fisher(_williams_r(high, low, close, 14) + 50.0, scale=0.1)
    at_max = ift == ift.rolling(YDAYS, min_periods=QDAYS).max()
    return (_bars_since_true(at_max)).diff().diff()


def f26_stwf_179_connors_rsi_full_3_2_100_d2(close: pd.Series) -> pd.Series:
    """Connors RSI: (RSI3 + StreakRSI2 + PctRank(returns,100)) / 3."""
    return (_connors_rsi(close)).diff().diff()


def f26_stwf_180_connors_rsi_above_85_state_d2(close: pd.Series) -> pd.Series:
    """1 if CRSI > 85 — Connors OB regime."""
    c = _connors_rsi(close)
    return ((c > 85.0).astype(float).where(c.notna(), np.nan)).diff().diff()


def f26_stwf_181_connors_rsi_just_exited_above_85_d2(close: pd.Series) -> pd.Series:
    """1 if CRSI just crossed back below 85 — Connors OB-exit."""
    c = _connors_rsi(close)
    return (((c.shift(1) > 85.0) & (c <= 85.0)).astype(float).where(c.notna(), np.nan)).diff().diff()


def f26_stwf_182_connors_rsi_above_95_state_d2(close: pd.Series) -> pd.Series:
    """1 if CRSI > 95 — Connors extreme-OB regime."""
    c = _connors_rsi(close)
    return ((c > 95.0).astype(float).where(c.notna(), np.nan)).diff().diff()


def f26_stwf_183_connors_rsi_dwell_above_85_63_d2(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with CRSI > 85 — Connors OB dwell."""
    c = _connors_rsi(close)
    return ((c > 85.0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(c.notna(), np.nan)).diff().diff()


def f26_stwf_184_connors_rsi_div_vs_price_63_d2(high: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish div: new 63d high in price but CRSI below prior 63d CRSI max."""
    c = _connors_rsi(close)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    c_below = c < c.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_new & c_below).astype(float).where(c.notna(), np.nan)).diff().diff()


def f26_stwf_185_bollinger_pctb_20_2_d2(close: pd.Series) -> pd.Series:
    """Bollinger %B (20, 2-sigma) = (close - lower) / (upper - lower)."""
    m = close.rolling(20, min_periods=7).mean()
    sd = close.rolling(20, min_periods=7).std()
    up = m + 2.0 * sd
    lo = m - 2.0 * sd
    return (_safe_div(close - lo, up - lo)).diff().diff()


def f26_stwf_186_bollinger_pctb_above_1_state_d2(close: pd.Series) -> pd.Series:
    """1 if BB %B > 1 — close above upper band (walking-the-band OB)."""
    m = close.rolling(20, min_periods=7).mean()
    sd = close.rolling(20, min_periods=7).std()
    up = m + 2.0 * sd
    lo = m - 2.0 * sd
    p = _safe_div(close - lo, up - lo)
    return ((p > 1.0).astype(float).where(p.notna(), np.nan)).diff().diff()


def f26_stwf_187_bollinger_pctb_just_exited_above_1_d2(close: pd.Series) -> pd.Series:
    """1 if BB %B just dropped from > 1 to <= 1 this bar — upper-band exit."""
    m = close.rolling(20, min_periods=7).mean()
    sd = close.rolling(20, min_periods=7).std()
    up = m + 2.0 * sd
    lo = m - 2.0 * sd
    p = _safe_div(close - lo, up - lo)
    return (((p.shift(1) > 1.0) & (p <= 1.0)).astype(float).where(p.notna(), np.nan)).diff().diff()


def f26_stwf_188_bollinger_pctb_dwell_above_08_63_d2(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with BB %B > 0.8 — dwell near upper band."""
    m = close.rolling(20, min_periods=7).mean()
    sd = close.rolling(20, min_periods=7).std()
    up = m + 2.0 * sd
    lo = m - 2.0 * sd
    p = _safe_div(close - lo, up - lo)
    return ((p > 0.8).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(p.notna(), np.nan)).diff().diff()


def f26_stwf_189_donchian_pctb_20_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Donchian %B (20) = (close - 20d_low) / (20d_high - 20d_low)."""
    ll = low.rolling(20, min_periods=7).min()
    hh = high.rolling(20, min_periods=7).max()
    return (_safe_div(close - ll, hh - ll)).diff().diff()


def f26_stwf_190_donchian_pctb_above_09_state_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Donchian %B > 0.9 — close near upper Donchian channel."""
    ll = low.rolling(20, min_periods=7).min()
    hh = high.rolling(20, min_periods=7).max()
    p = _safe_div(close - ll, hh - ll)
    return ((p > 0.9).astype(float).where(p.notna(), np.nan)).diff().diff()


def f26_stwf_191_donchian_pctb_just_exited_above_09_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Donchian %B just dropped below 0.9 from above — upper-channel exit."""
    ll = low.rolling(20, min_periods=7).min()
    hh = high.rolling(20, min_periods=7).max()
    p = _safe_div(close - ll, hh - ll)
    return (((p.shift(1) > 0.9) & (p <= 0.9)).astype(float).where(p.notna(), np.nan)).diff().diff()


def f26_stwf_192_donchian_pctb_bars_since_252_max_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since Donchian %B hit its 252d max."""
    ll = low.rolling(20, min_periods=7).min()
    hh = high.rolling(20, min_periods=7).max()
    p = _safe_div(close - ll, hh - ll)
    at_max = p == p.rolling(YDAYS, min_periods=QDAYS).max()
    return (_bars_since_true(at_max)).diff().diff()


def f26_stwf_193_rvi_10_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relative Vigor Index (10) — vigor of bullish vs full range."""
    return (_rvi(open, high, low, close, 10)).diff().diff()


def f26_stwf_194_rvi_signal_4_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """RVI signal line — SWMA-4 of RVI."""
    return (_swma4(_rvi(open, high, low, close, 10))).diff().diff()


def f26_stwf_195_rvi_signal_bearish_cross_indicator_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if RVI crossed below its signal this bar — RVI bearish cross."""
    r = _rvi(open, high, low, close, 10)
    sig = _swma4(r)
    diff = r - sig
    return (((diff.shift(1) > 0) & (diff <= 0)).astype(float).where(diff.notna(), np.nan)).diff().diff()


def f26_stwf_196_rvi_above_zero_state_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if RVI > 0 — vigor bullish."""
    r = _rvi(open, high, low, close, 10)
    return ((r > 0).astype(float).where(r.notna(), np.nan)).diff().diff()


def f26_stwf_197_rvi_div_vs_price_63_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish div: new 63d price-high but RVI below prior 63d RVI max."""
    r = _rvi(open, high, low, close, 10)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    r_below = r < r.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((p_new & r_below).astype(float).where(r.notna(), np.nan)).diff().diff()


def f26_stwf_198_rvi_zscore_252_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of RVI over 252 bars."""
    return (_rolling_zscore(_rvi(open, high, low, close, 10), YDAYS, min_periods=QDAYS)).diff().diff()


def f26_stwf_199_rvi_bars_since_252_max_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars since RVI hit its 252d max — recency of vigor peak."""
    r = _rvi(open, high, low, close, 10)
    at_max = r == r.rolling(YDAYS, min_periods=QDAYS).max()
    return (_bars_since_true(at_max)).diff().diff()


def f26_stwf_200_rvi_dwell_above_zero_252_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars with RVI > 0 — vigor bullish persistence."""
    r = _rvi(open, high, low, close, 10)
    return ((r > 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(r.notna(), np.nan)).diff().diff()


def f26_stwf_201_stoch_hull_smoothed_14_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stoch %K(14) smoothed with Hull MA(9) — adaptive low-lag smoothing."""
    return (_hma(_stoch_k(high, low, close, 14), 9)).diff().diff()


def f26_stwf_202_stoch_dema_smoothed_14_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stoch %K(14) smoothed with DEMA(9)."""
    return (_dema(_stoch_k(high, low, close, 14), 9)).diff().diff()


def f26_stwf_203_stoch_tema_smoothed_14_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stoch %K(14) smoothed with TEMA(9)."""
    return (_tema(_stoch_k(high, low, close, 14), 9)).diff().diff()


def f26_stwf_204_stoch_kama_smoothed_14_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stoch %K(14) smoothed with KAMA(10) — efficiency-weighted EMA."""
    return (_kama(_stoch_k(high, low, close, 14), n=10)).diff().diff()


def f26_stwf_205_stoch_zero_lag_ema_smoothed_14_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stoch %K(14) smoothed with ZLEMA(9)."""
    return (_zlema(_stoch_k(high, low, close, 14), 9)).diff().diff()


def f26_stwf_206_heiken_ashi_close_stoch_14_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Stoch %K(14) computed on Heiken-Ashi close (smoother input)."""
    hac = _ha_close(open, high, low, close)
    ll = low.rolling(14, min_periods=5).min()
    hh = high.rolling(14, min_periods=5).max()
    return (100.0 * _safe_div(hac - ll, hh - ll)).diff().diff()


def f26_stwf_207_heiken_ashi_close_stoch_in_ob_state_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if HA-close-stoch %K > 80 — HA OB regime."""
    hac = _ha_close(open, high, low, close)
    ll = low.rolling(14, min_periods=5).min()
    hh = high.rolling(14, min_periods=5).max()
    k = 100.0 * _safe_div(hac - ll, hh - ll)
    return ((k > 80.0).astype(float).where(k.notna(), np.nan)).diff().diff()


def f26_stwf_208_stoch_double_smoothed_ema_5_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Double-smoothed stoch: EMA5 of EMA5 of %K(14)."""
    return (_ema(_ema(_stoch_k(high, low, close, 14), 5), 5)).diff().diff()


def f26_stwf_209_stoch_kama_residual_zscore_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of (%K - KAMA-smoothed K) over 63 — residual from adaptive smoother."""
    k = _stoch_k(high, low, close, 14)
    kam = _kama(k, n=10)
    return (_rolling_zscore(k - kam, QDAYS, min_periods=MDAYS)).diff().diff()


def f26_stwf_210_stoch_efficiency_ratio_weighted_d2(close: pd.Series) -> pd.Series:
    """Efficiency Ratio (Kaufman): |close - close.shift(10)| / sum(|close diffs|, 10) — trend-strength weighting for stoch context."""
    ch = (close - close.shift(10)).abs()
    vol = close.diff().abs().rolling(10, min_periods=4).sum()
    return (_safe_div(ch, vol).clip(0.0, 1.0)).diff().diff()


def f26_stwf_211_stoch_bb_upper_band_20_2_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bollinger upper band computed on stoch %K(14) (20,2). Identifies stoch overextension."""
    k = _stoch_k(high, low, close, 14)
    m = k.rolling(20, min_periods=7).mean()
    sd = k.rolling(20, min_periods=7).std()
    return (m + 2.0 * sd).diff().diff()


def f26_stwf_212_stoch_bb_lower_band_20_2_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bollinger lower band on stoch %K — context for asymmetric extension."""
    k = _stoch_k(high, low, close, 14)
    m = k.rolling(20, min_periods=7).mean()
    sd = k.rolling(20, min_periods=7).std()
    return (m - 2.0 * sd).diff().diff()


def f26_stwf_213_stoch_bb_pctb_14_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """%B of stoch %K against its own BB(20,2) — position of stoch in its volatility band."""
    k = _stoch_k(high, low, close, 14)
    m = k.rolling(20, min_periods=7).mean()
    sd = k.rolling(20, min_periods=7).std()
    return (_safe_div(k - (m - 2.0 * sd), 4.0 * sd)).diff().diff()


def f26_stwf_214_stoch_above_upper_bb_state_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if stoch %K exceeds its own BB upper band — extreme stoch breakout."""
    k = _stoch_k(high, low, close, 14)
    m = k.rolling(20, min_periods=7).mean()
    sd = k.rolling(20, min_periods=7).std()
    up = m + 2.0 * sd
    return ((k > up).astype(float).where(up.notna(), np.nan)).diff().diff()


def f26_stwf_215_stoch_just_exited_above_upper_bb_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if stoch %K just crossed back below its BB upper band — stoch BB-exit."""
    k = _stoch_k(high, low, close, 14)
    m = k.rolling(20, min_periods=7).mean()
    sd = k.rolling(20, min_periods=7).std()
    up = m + 2.0 * sd
    above = k > up
    return (((above.shift(1)) & (~above)).astype(float).where(up.notna(), np.nan)).diff().diff()


def f26_stwf_216_stoch_above_upper_bb_dwell_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with stoch above its upper BB."""
    k = _stoch_k(high, low, close, 14)
    m = k.rolling(20, min_periods=7).mean()
    sd = k.rolling(20, min_periods=7).std()
    up = m + 2.0 * sd
    return ((k > up).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(up.notna(), np.nan)).diff().diff()


def f26_stwf_217_stoch_bb_squeeze_indicator_63_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if BB-width on stoch is below its 252d 10th percentile — stoch BB squeeze (compression precedes expansion)."""
    k = _stoch_k(high, low, close, 14)
    sd = k.rolling(20, min_periods=7).std()
    bw = 4.0 * sd
    q10 = bw.rolling(YDAYS, min_periods=QDAYS).quantile(0.10)
    return ((bw < q10).astype(float).where(bw.notna() & q10.notna(), np.nan)).diff().diff()


def f26_stwf_218_stoch_keltner_position_14_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Position of stoch %K in Keltner channel built from stoch SMA + mult * ATR-of-stoch.
    Position = (K - mid) / (mult * stoch_atr_proxy)."""
    k = _stoch_k(high, low, close, 14)
    mid = k.rolling(20, min_periods=7).mean()
    # 'ATR of stoch' proxy: absolute first-difference average
    sa = k.diff().abs().rolling(14, min_periods=5).mean()
    return (_safe_div(k - mid, 2.0 * sa)).diff().diff()


def f26_stwf_219_williamsr_kd_hook_at_top_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if Williams %R (used as K) crosses below its EMA9 (as D) while both > -20 — Williams-KD top hook."""
    wr = _williams_r(high, low, close, 14)
    wr_d = _ema(wr, 9)
    diff = wr - wr_d
    return (((diff.shift(1) > 0) & (diff <= 0) & (wr > -20.0) & (wr_d > -20.0)).astype(float).where(diff.notna(), np.nan)).diff().diff()


def f26_stwf_220_stoch_rsi_kd_hook_at_top_d2(close: pd.Series) -> pd.Series:
    """1 if Stoch-RSI K crosses below D while both > 80 — Stoch-RSI top hook."""
    r = _rsi(close, 14)
    ll = r.rolling(14, min_periods=5).min()
    hh = r.rolling(14, min_periods=5).max()
    raw_k = 100.0 * _safe_div(r - ll, hh - ll)
    k = raw_k.rolling(3, min_periods=2).mean()
    d = k.rolling(3, min_periods=2).mean()
    diff = k - d
    return (((diff.shift(1) > 0) & (diff <= 0) & (k > 80.0) & (d > 80.0)).astype(float).where(diff.notna(), np.nan)).diff().diff()


def f26_stwf_221_cross_oscillator_kd_hook_count_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of {stoch, stoch-RSI, Williams} top-hook events in past 21 bars — multi-osc hook breadth."""
    # stoch KD hook
    k = _stoch_k(high, low, close, 14)
    d = k.rolling(3, min_periods=2).mean()
    diff_s = k - d
    h_s = ((diff_s.shift(1) > 0) & (diff_s <= 0) & (k > 80.0) & (d > 80.0)).astype(float)
    # stoch-RSI hook
    r = _rsi(close, 14)
    ll = r.rolling(14, min_periods=5).min()
    hh = r.rolling(14, min_periods=5).max()
    raw_k = 100.0 * _safe_div(r - ll, hh - ll)
    kr = raw_k.rolling(3, min_periods=2).mean()
    dr = kr.rolling(3, min_periods=2).mean()
    diff_r = kr - dr
    h_r = ((diff_r.shift(1) > 0) & (diff_r <= 0) & (kr > 80.0) & (dr > 80.0)).astype(float)
    # Williams hook
    wr = _williams_r(high, low, close, 14)
    wd = _ema(wr, 9)
    diff_w = wr - wd
    h_w = ((diff_w.shift(1) > 0) & (diff_w <= 0) & (wr > -20.0) & (wd > -20.0)).astype(float)
    return ((h_s.fillna(0) + h_r.fillna(0) + h_w.fillna(0)).rolling(MDAYS, min_periods=WDAYS).sum().where(k.notna(), np.nan)).diff().diff()


def f26_stwf_222_combined_inverse_fisher_extreme_count_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of {IFT-stoch, IFT-WR, IFT-UO} indicators > 0.5 — extreme-IFT breadth."""
    ift_s = _inverse_fisher(_stoch_k(high, low, close, 14) - 50.0, scale=0.1)
    ift_w = _inverse_fisher(_williams_r(high, low, close, 14) + 50.0, scale=0.1)
    # Ultimate-osc proxy: blend of stoch at 3 horizons (lightweight UO substitute)
    uo = (_stoch_k(high, low, close, 7) * 4 + _stoch_k(high, low, close, 14) * 2 + _stoch_k(high, low, close, 28)) / 7.0
    ift_u = _inverse_fisher(uo - 50.0, scale=0.1)
    cnt = ((ift_s > 0.5).astype(float).fillna(0)
           + (ift_w > 0.5).astype(float).fillna(0)
           + (ift_u > 0.5).astype(float).fillna(0))
    return (cnt.where(ift_s.notna(), np.nan)).diff().diff()


def f26_stwf_223_combined_modern_oscillator_topping_score_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of indicators: STC>75 + AO<0 + CRSI>85 + RVI<0 + BB%B>1 — modern-basket topping count."""
    stc = _stc(close)
    ao = _awesome_osc(high, low)
    crsi = _connors_rsi(close)
    rvi = _rvi(open, high, low, close, 10)
    m = close.rolling(20, min_periods=7).mean()
    sd = close.rolling(20, min_periods=7).std()
    pctb = _safe_div(close - (m - 2.0 * sd), 4.0 * sd)
    cnt = ((stc > 75.0).astype(float).fillna(0)
           + (ao < 0).astype(float).fillna(0)
           + (crsi > 85.0).astype(float).fillna(0)
           + (rvi < 0).astype(float).fillna(0)
           + (pctb > 1.0).astype(float).fillna(0))
    return (cnt.where(close.notna(), np.nan)).diff().diff()


def f26_stwf_224_modern_oscillator_basket_correlation_63_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean pairwise rolling-63d correlation across z-scored {STC, AO, CRSI, RVI}."""
    stc = _rolling_zscore(_stc(close), YDAYS, min_periods=QDAYS)
    ao = _rolling_zscore(_awesome_osc(high, low), YDAYS, min_periods=QDAYS)
    crsi = _rolling_zscore(_connors_rsi(close), YDAYS, min_periods=QDAYS)
    rvi = _rolling_zscore(_rvi(open, high, low, close, 10), YDAYS, min_periods=QDAYS)
    series_pairs = [(stc, ao), (stc, crsi), (stc, rvi), (ao, crsi), (ao, rvi), (crsi, rvi)]
    corrs = [a.rolling(QDAYS, min_periods=MDAYS).corr(b) for a, b in series_pairs]
    df = pd.concat([c.rename(i) for i, c in enumerate(corrs)], axis=1)
    return (df.mean(axis=1)).diff().diff()


def f26_stwf_225_modern_oscillator_basket_dispersion_252_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std of z-scored {STC, AO, CRSI, RVI} — basket dispersion (high = oscillators disagree)."""
    stc = _rolling_zscore(_stc(close), YDAYS, min_periods=QDAYS)
    ao = _rolling_zscore(_awesome_osc(high, low), YDAYS, min_periods=QDAYS)
    crsi = _rolling_zscore(_connors_rsi(close), YDAYS, min_periods=QDAYS)
    rvi = _rolling_zscore(_rvi(open, high, low, close, 10), YDAYS, min_periods=QDAYS)
    df = pd.concat([stc.rename(0), ao.rename(1), crsi.rename(2), rvi.rename(3)], axis=1)
    return (df.std(axis=1)).diff().diff()


# ============================================================
#                         REGISTRY 151-225 (d2)
# ============================================================

STOCHASTIC_WILLIAMS_FAMILY_D2_REGISTRY_151_225 = {
    "f26_stwf_151_stc_classical_23_50_10_d2": {"inputs": ["close"], "func": f26_stwf_151_stc_classical_23_50_10_d2},
    "f26_stwf_152_stc_signal_bearish_cross_indicator_d2": {"inputs": ["close"], "func": f26_stwf_152_stc_signal_bearish_cross_indicator_d2},
    "f26_stwf_153_stc_above_75_state_d2": {"inputs": ["close"], "func": f26_stwf_153_stc_above_75_state_d2},
    "f26_stwf_154_stc_just_exited_above_75_d2": {"inputs": ["close"], "func": f26_stwf_154_stc_just_exited_above_75_d2},
    "f26_stwf_155_stc_dwell_above_75_63_d2": {"inputs": ["close"], "func": f26_stwf_155_stc_dwell_above_75_63_d2},
    "f26_stwf_156_stc_div_vs_price_63_d2": {"inputs": ["high", "close"], "func": f26_stwf_156_stc_div_vs_price_63_d2},
    "f26_stwf_157_stc_bars_since_252_max_d2": {"inputs": ["close"], "func": f26_stwf_157_stc_bars_since_252_max_d2},
    "f26_stwf_158_stc_zscore_252_d2": {"inputs": ["close"], "func": f26_stwf_158_stc_zscore_252_d2},
    "f26_stwf_159_stc_peak_decay_63_d2": {"inputs": ["close"], "func": f26_stwf_159_stc_peak_decay_63_d2},
    "f26_stwf_160_stc_persistence_above_zero_252_d2": {"inputs": ["close"], "func": f26_stwf_160_stc_persistence_above_zero_252_d2},
    "f26_stwf_161_ao_5_34_d2": {"inputs": ["high", "low"], "func": f26_stwf_161_ao_5_34_d2},
    "f26_stwf_162_ao_above_zero_state_d2": {"inputs": ["high", "low"], "func": f26_stwf_162_ao_above_zero_state_d2},
    "f26_stwf_163_ao_zero_cross_down_indicator_d2": {"inputs": ["high", "low"], "func": f26_stwf_163_ao_zero_cross_down_indicator_d2},
    "f26_stwf_164_ao_div_vs_price_63_d2": {"inputs": ["high", "low"], "func": f26_stwf_164_ao_div_vs_price_63_d2},
    "f26_stwf_165_ao_zscore_252_d2": {"inputs": ["high", "low"], "func": f26_stwf_165_ao_zscore_252_d2},
    "f26_stwf_166_ac_oscillator_5_d2": {"inputs": ["high", "low"], "func": f26_stwf_166_ac_oscillator_5_d2},
    "f26_stwf_167_ac_above_zero_state_d2": {"inputs": ["high", "low"], "func": f26_stwf_167_ac_above_zero_state_d2},
    "f26_stwf_168_ac_zero_cross_down_indicator_d2": {"inputs": ["high", "low"], "func": f26_stwf_168_ac_zero_cross_down_indicator_d2},
    "f26_stwf_169_ac_consecutive_red_bars_streak_d2": {"inputs": ["high", "low"], "func": f26_stwf_169_ac_consecutive_red_bars_streak_d2},
    "f26_stwf_170_ac_bars_since_252_max_d2": {"inputs": ["high", "low"], "func": f26_stwf_170_ac_bars_since_252_max_d2},
    "f26_stwf_171_fisher_transform_price_10_d2": {"inputs": ["close"], "func": f26_stwf_171_fisher_transform_price_10_d2},
    "f26_stwf_172_fisher_transform_zero_cross_down_d2": {"inputs": ["close"], "func": f26_stwf_172_fisher_transform_zero_cross_down_d2},
    "f26_stwf_173_inverse_fisher_transform_stoch_14_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_173_inverse_fisher_transform_stoch_14_d2},
    "f26_stwf_174_ift_stoch_above_05_state_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_174_ift_stoch_above_05_state_d2},
    "f26_stwf_175_ift_stoch_just_exited_above_05_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_175_ift_stoch_just_exited_above_05_d2},
    "f26_stwf_176_ift_williams_r_14_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_176_ift_williams_r_14_d2},
    "f26_stwf_177_ift_williams_r_above_05_state_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_177_ift_williams_r_above_05_state_d2},
    "f26_stwf_178_ift_williams_r_bars_since_252_max_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_178_ift_williams_r_bars_since_252_max_d2},
    "f26_stwf_179_connors_rsi_full_3_2_100_d2": {"inputs": ["close"], "func": f26_stwf_179_connors_rsi_full_3_2_100_d2},
    "f26_stwf_180_connors_rsi_above_85_state_d2": {"inputs": ["close"], "func": f26_stwf_180_connors_rsi_above_85_state_d2},
    "f26_stwf_181_connors_rsi_just_exited_above_85_d2": {"inputs": ["close"], "func": f26_stwf_181_connors_rsi_just_exited_above_85_d2},
    "f26_stwf_182_connors_rsi_above_95_state_d2": {"inputs": ["close"], "func": f26_stwf_182_connors_rsi_above_95_state_d2},
    "f26_stwf_183_connors_rsi_dwell_above_85_63_d2": {"inputs": ["close"], "func": f26_stwf_183_connors_rsi_dwell_above_85_63_d2},
    "f26_stwf_184_connors_rsi_div_vs_price_63_d2": {"inputs": ["high", "close"], "func": f26_stwf_184_connors_rsi_div_vs_price_63_d2},
    "f26_stwf_185_bollinger_pctb_20_2_d2": {"inputs": ["close"], "func": f26_stwf_185_bollinger_pctb_20_2_d2},
    "f26_stwf_186_bollinger_pctb_above_1_state_d2": {"inputs": ["close"], "func": f26_stwf_186_bollinger_pctb_above_1_state_d2},
    "f26_stwf_187_bollinger_pctb_just_exited_above_1_d2": {"inputs": ["close"], "func": f26_stwf_187_bollinger_pctb_just_exited_above_1_d2},
    "f26_stwf_188_bollinger_pctb_dwell_above_08_63_d2": {"inputs": ["close"], "func": f26_stwf_188_bollinger_pctb_dwell_above_08_63_d2},
    "f26_stwf_189_donchian_pctb_20_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_189_donchian_pctb_20_d2},
    "f26_stwf_190_donchian_pctb_above_09_state_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_190_donchian_pctb_above_09_state_d2},
    "f26_stwf_191_donchian_pctb_just_exited_above_09_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_191_donchian_pctb_just_exited_above_09_d2},
    "f26_stwf_192_donchian_pctb_bars_since_252_max_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_192_donchian_pctb_bars_since_252_max_d2},
    "f26_stwf_193_rvi_10_d2": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_193_rvi_10_d2},
    "f26_stwf_194_rvi_signal_4_d2": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_194_rvi_signal_4_d2},
    "f26_stwf_195_rvi_signal_bearish_cross_indicator_d2": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_195_rvi_signal_bearish_cross_indicator_d2},
    "f26_stwf_196_rvi_above_zero_state_d2": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_196_rvi_above_zero_state_d2},
    "f26_stwf_197_rvi_div_vs_price_63_d2": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_197_rvi_div_vs_price_63_d2},
    "f26_stwf_198_rvi_zscore_252_d2": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_198_rvi_zscore_252_d2},
    "f26_stwf_199_rvi_bars_since_252_max_d2": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_199_rvi_bars_since_252_max_d2},
    "f26_stwf_200_rvi_dwell_above_zero_252_d2": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_200_rvi_dwell_above_zero_252_d2},
    "f26_stwf_201_stoch_hull_smoothed_14_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_201_stoch_hull_smoothed_14_d2},
    "f26_stwf_202_stoch_dema_smoothed_14_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_202_stoch_dema_smoothed_14_d2},
    "f26_stwf_203_stoch_tema_smoothed_14_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_203_stoch_tema_smoothed_14_d2},
    "f26_stwf_204_stoch_kama_smoothed_14_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_204_stoch_kama_smoothed_14_d2},
    "f26_stwf_205_stoch_zero_lag_ema_smoothed_14_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_205_stoch_zero_lag_ema_smoothed_14_d2},
    "f26_stwf_206_heiken_ashi_close_stoch_14_d2": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_206_heiken_ashi_close_stoch_14_d2},
    "f26_stwf_207_heiken_ashi_close_stoch_in_ob_state_d2": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_207_heiken_ashi_close_stoch_in_ob_state_d2},
    "f26_stwf_208_stoch_double_smoothed_ema_5_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_208_stoch_double_smoothed_ema_5_d2},
    "f26_stwf_209_stoch_kama_residual_zscore_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_209_stoch_kama_residual_zscore_63_d2},
    "f26_stwf_210_stoch_efficiency_ratio_weighted_d2": {"inputs": ["close"], "func": f26_stwf_210_stoch_efficiency_ratio_weighted_d2},
    "f26_stwf_211_stoch_bb_upper_band_20_2_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_211_stoch_bb_upper_band_20_2_d2},
    "f26_stwf_212_stoch_bb_lower_band_20_2_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_212_stoch_bb_lower_band_20_2_d2},
    "f26_stwf_213_stoch_bb_pctb_14_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_213_stoch_bb_pctb_14_d2},
    "f26_stwf_214_stoch_above_upper_bb_state_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_214_stoch_above_upper_bb_state_d2},
    "f26_stwf_215_stoch_just_exited_above_upper_bb_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_215_stoch_just_exited_above_upper_bb_d2},
    "f26_stwf_216_stoch_above_upper_bb_dwell_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_216_stoch_above_upper_bb_dwell_63_d2},
    "f26_stwf_217_stoch_bb_squeeze_indicator_63_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_217_stoch_bb_squeeze_indicator_63_d2},
    "f26_stwf_218_stoch_keltner_position_14_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_218_stoch_keltner_position_14_d2},
    "f26_stwf_219_williamsr_kd_hook_at_top_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_219_williamsr_kd_hook_at_top_d2},
    "f26_stwf_220_stoch_rsi_kd_hook_at_top_d2": {"inputs": ["close"], "func": f26_stwf_220_stoch_rsi_kd_hook_at_top_d2},
    "f26_stwf_221_cross_oscillator_kd_hook_count_21d_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_221_cross_oscillator_kd_hook_count_21d_d2},
    "f26_stwf_222_combined_inverse_fisher_extreme_count_d2": {"inputs": ["high", "low", "close"], "func": f26_stwf_222_combined_inverse_fisher_extreme_count_d2},
    "f26_stwf_223_combined_modern_oscillator_topping_score_d2": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_223_combined_modern_oscillator_topping_score_d2},
    "f26_stwf_224_modern_oscillator_basket_correlation_63_d2": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_224_modern_oscillator_basket_correlation_63_d2},
    "f26_stwf_225_modern_oscillator_basket_dispersion_252_d2": {"inputs": ["open", "high", "low", "close"], "func": f26_stwf_225_modern_oscillator_basket_dispersion_252_d2},
}
