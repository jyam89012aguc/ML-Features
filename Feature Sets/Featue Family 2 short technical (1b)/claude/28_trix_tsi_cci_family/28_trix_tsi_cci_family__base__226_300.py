"""trix_tsi_cci_family base features 226-300 — Pipeline 1b-technical.

75 distinct hypotheses (statistical / cycle / regime / aggregate) extending 151-225.
Buckets:
  Hilbert-Transform & cycle-period proxies (10).
  DPO advanced statistics (8).
  Oscillator signal-to-noise / information-coefficient (10).
  Pattern detectors on oscillators (10).
  Multi-horizon family alignment (10).
  Regime modeling (10).
  Aggregate / terminal scoring (17).

Inputs: SEP OHLCV. PIT-clean. Self-contained helpers (no cross-family imports).
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


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 2, 2)).mean()


def _trix(close, n=15):
    e1 = _ema(close, n)
    e2 = _ema(e1, n)
    e3 = _ema(e2, n)
    return 100.0 * e3.pct_change()


def _tsi(close, n1=25, n2=13):
    m = close.diff()
    e1 = _ema(m, n1)
    e2 = _ema(e1, n2)
    a1 = _ema(m.abs(), n1)
    a2 = _ema(a1, n2)
    return 100.0 * _safe_div(e2, a2)


def _cci(high, low, close, n=20):
    tp = (high + low + close) / 3.0
    sma = tp.rolling(n, min_periods=max(n // 3, 2)).mean()
    mad = (tp - sma).abs().rolling(n, min_periods=max(n // 3, 2)).mean()
    return _safe_div(tp - sma, 0.015 * mad)


def _dpo(close, n=20):
    sma = close.rolling(n, min_periods=max(n // 3, 2)).mean()
    return close - sma.shift(n // 2 + 1)


def _kst(close):
    roc10 = close.pct_change(10)
    roc15 = close.pct_change(15)
    roc20 = close.pct_change(20)
    roc30 = close.pct_change(30)
    r1 = roc10.rolling(10, min_periods=5).mean()
    r2 = roc15.rolling(10, min_periods=5).mean()
    r3 = roc20.rolling(10, min_periods=5).mean()
    r4 = roc30.rolling(15, min_periods=8).mean()
    return r1 + 2.0 * r2 + 3.0 * r3 + 4.0 * r4


def _cmo(close, n=14):
    d = close.diff()
    up = d.clip(lower=0)
    dn = (-d).clip(lower=0)
    su = up.rolling(n, min_periods=max(n // 3, 2)).sum()
    sd = dn.rolling(n, min_periods=max(n // 3, 2)).sum()
    return 100.0 * _safe_div(su - sd, su + sd)


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


# ---------- Hilbert / cycle proxies ----------

def _hilbert_inphase(close):
    """I = close - close.shift(2) — simplified Hilbert in-phase proxy."""
    return close - close.shift(2)


def _hilbert_quadrature(close):
    """Q = lagged-I (shifted by 1) — simplified Hilbert quadrature proxy."""
    return _hilbert_inphase(close).shift(1)


def _hilbert_period_proxy(close, n=21):
    """Instantaneous period proxy: 2*pi / arctan(Q / I) ... use rolling stdev ratio for stability."""
    i = _hilbert_inphase(close)
    q = _hilbert_quadrature(close)
    # angular frequency proxy = arctan2(Q, I).diff(); smooth then invert
    phase = np.arctan2(q, i)
    dphase = phase.diff()
    dphase = dphase.where(dphase.abs() > 1e-6, np.nan)
    period = (2.0 * np.pi) / dphase.abs()
    return period.rolling(n, min_periods=max(n // 3, 2)).median()


def _dominant_cycle_proxy(close, n=21):
    """Approximation: max-power cycle in 21d by autocorrelation."""
    def _f(w):
        if np.isnan(w).any() or len(w) < 5:
            return np.nan
        max_lag = min(len(w) - 1, 21)
        best_p = np.nan
        best_v = -np.inf
        wc = w - w.mean()
        for lag in range(2, max_lag + 1):
            if len(wc) <= lag:
                break
            a = wc[lag:]
            b = wc[:-lag]
            denom = np.sqrt((a * a).sum() * (b * b).sum())
            if denom == 0:
                continue
            v = (a * b).sum() / denom
            if v > best_v:
                best_v = v
                best_p = float(lag)
        return best_p
    return close.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


# ============================================================
# Bucket Y — Hilbert / cycle period estimators (226-235)
# ============================================================

def f28_ttcf_226_hilbert_in_phase_proxy(close: pd.Series) -> pd.Series:
    """In-phase component (Hilbert proxy): I = close - close.shift(2)."""
    return _hilbert_inphase(close)


def f28_ttcf_227_hilbert_quadrature_proxy(close: pd.Series) -> pd.Series:
    """Quadrature component (Hilbert proxy): Q = lagged-I (shift 1)."""
    return _hilbert_quadrature(close)


def f28_ttcf_228_hilbert_period_proxy(close: pd.Series) -> pd.Series:
    """Hilbert instantaneous-period proxy (21d median): 2pi / |d(arctan2(Q,I))|."""
    return _hilbert_period_proxy(close, MDAYS)


def f28_ttcf_229_dominant_cycle_proxy_21(close: pd.Series) -> pd.Series:
    """Dominant cycle estimator over 21d via max-autocorrelation lag (Goertzel approximation)."""
    return _dominant_cycle_proxy(close, MDAYS)


def f28_ttcf_230_trend_vs_cycle_ratio_63(close: pd.Series) -> pd.Series:
    """abs(63d slope of close) / 63d rolling std(close.diff()) — trend strength relative to cycle noise."""
    sl = _rolling_slope(close, QDAYS).abs()
    sd = close.diff().rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(sl, sd)


def f28_ttcf_231_dominant_cycle_zscore_252(close: pd.Series) -> pd.Series:
    """252d z-score of dominant-cycle period — distribution-based cycle-length position."""
    return _rolling_zscore(_dominant_cycle_proxy(close, MDAYS), YDAYS, min_periods=QDAYS)


def f28_ttcf_232_cycle_phase_bearish_state(close: pd.Series) -> pd.Series:
    """1 if cycle phase angle in (pi/2, pi] OR (-pi, -pi/2] — bearish-quarter-cycle phase state."""
    i = _hilbert_inphase(close)
    q = _hilbert_quadrature(close)
    phase = np.arctan2(q, i)
    bearish = (phase > (np.pi / 2.0)) | (phase < (-np.pi / 2.0))
    return bearish.astype(float).where(phase.notna(), np.nan)


def f28_ttcf_233_cycle_phase_dwell_in_top_quartile_63(close: pd.Series) -> pd.Series:
    """Fraction of past 63 bars with cycle phase in (0, pi/2] — top-quartile phase dwell."""
    i = _hilbert_inphase(close)
    q = _hilbert_quadrature(close)
    phase = np.arctan2(q, i)
    top_q = (phase > 0) & (phase <= (np.pi / 2.0))
    return top_q.astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(phase.notna(), np.nan)


def f28_ttcf_234_cycle_amplitude_decay_63(close: pd.Series) -> pd.Series:
    """Cycle amplitude (sqrt(I^2+Q^2)) 63d max - amplitude 63 bars ago — amplitude decay."""
    i = _hilbert_inphase(close)
    q = _hilbert_quadrature(close)
    amp = np.sqrt(i.pow(2) + q.pow(2))
    pmax = amp.rolling(QDAYS, min_periods=MDAYS).max()
    return pmax - pmax.shift(QDAYS)


def f28_ttcf_235_cycle_amplitude_zscore_252(close: pd.Series) -> pd.Series:
    """252d z-score of cycle amplitude — distribution-based cycle-amplitude position."""
    i = _hilbert_inphase(close)
    q = _hilbert_quadrature(close)
    amp = np.sqrt(i.pow(2) + q.pow(2))
    return _rolling_zscore(amp, YDAYS, min_periods=QDAYS)


# ============================================================
# Bucket Z — DPO advanced (236-243)
# ============================================================

def f28_ttcf_236_dpo_residual_volatility_63(close: pd.Series) -> pd.Series:
    """63d std of DPO(21) residuals (DPO - EMA21(DPO)) — cycle-residual volatility."""
    d = _dpo(close, MDAYS)
    res = d - _ema(d, MDAYS)
    return res.rolling(QDAYS, min_periods=MDAYS).std()


def f28_ttcf_237_dpo_zero_cross_count_252(close: pd.Series) -> pd.Series:
    """Count of DPO sign-flips (zero crosses) in past 252 — annual cycle-instability."""
    d = _dpo(close, MDAYS)
    flip = (d * d.shift(1)) < 0
    return flip.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().where(d.notna(), np.nan)


def f28_ttcf_238_dpo_recent_peak_height_zscore(close: pd.Series) -> pd.Series:
    """z-score (over 252d) of DPO's 63d rolling max — recent peak height in distribution context."""
    d = _dpo(close, MDAYS)
    pmax = d.rolling(QDAYS, min_periods=MDAYS).max()
    return _rolling_zscore(pmax, YDAYS, min_periods=QDAYS)


def f28_ttcf_239_dpo_consecutive_above_zero_streak(close: pd.Series) -> pd.Series:
    """Current streak length of DPO > 0 — consecutive bullish-cycle bars."""
    d = _dpo(close, MDAYS)
    return _streak_true(d > 0).where(d.notna(), np.nan)


def f28_ttcf_240_dpo_persistence_above_q90_504(close: pd.Series) -> pd.Series:
    """Fraction of past 504 bars (2y) with DPO above its 504d q90 — bi-annual persistence."""
    d = _dpo(close, MDAYS)
    q = d.rolling(DDAYS_2Y, min_periods=YDAYS).quantile(0.90)
    return (d > q).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).mean().where(d.notna() & q.notna(), np.nan)


def f28_ttcf_241_dpo_seasonality_check_252(close: pd.Series) -> pd.Series:
    """Mean of (DPO autocorr at lag 21, lag 63) within 252d — cyclical seasonality proxy."""
    d = _dpo(close, MDAYS)
    a21 = d.rolling(YDAYS, min_periods=QDAYS).corr(d.shift(MDAYS))
    a63 = d.rolling(YDAYS, min_periods=QDAYS).corr(d.shift(QDAYS))
    return (a21 + a63) / 2.0


def f28_ttcf_242_dpo_skew_63(close: pd.Series) -> pd.Series:
    """63d skew of DPO — cycle-asymmetry."""
    return _dpo(close, MDAYS).rolling(QDAYS, min_periods=MDAYS).skew()


def f28_ttcf_243_dpo_kurtosis_63(close: pd.Series) -> pd.Series:
    """63d kurtosis of DPO — cycle-tail thickness."""
    return _dpo(close, MDAYS).rolling(QDAYS, min_periods=MDAYS).kurt()


# ============================================================
# Bucket AA — Oscillator signal-to-noise / info-coef (244-253)
# ============================================================

def _snr(sig, n):
    """Signal-to-noise: |mean(sig)| / std(sig) over rolling n."""
    return _safe_div(sig.rolling(n, min_periods=max(n // 3, 2)).mean().abs(),
                     sig.rolling(n, min_periods=max(n // 3, 2)).std())


def f28_ttcf_244_trix_signal_to_noise_ratio_63(close: pd.Series) -> pd.Series:
    """63d |mean|/std of TRIX(15) — trend-quality of TRIX."""
    return _snr(_trix(close, 15), QDAYS)


def f28_ttcf_245_tsi_signal_to_noise_ratio_63(close: pd.Series) -> pd.Series:
    """63d |mean|/std of TSI(25,13) — trend-quality of TSI."""
    return _snr(_tsi(close, 25, 13), QDAYS)


def f28_ttcf_246_cci_signal_to_noise_ratio_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d |mean|/std of CCI(20) — trend-quality of CCI."""
    return _snr(_cci(high, low, close, 20), QDAYS)


def f28_ttcf_247_cmo_signal_to_noise_ratio_63(close: pd.Series) -> pd.Series:
    """63d |mean|/std of CMO(14) — trend-quality of CMO."""
    return _snr(_cmo(close, 14), QDAYS)


def f28_ttcf_248_dpo_signal_to_noise_ratio_63(close: pd.Series) -> pd.Series:
    """63d |mean|/std of DPO(21) — cycle-strength of DPO."""
    return _snr(_dpo(close, MDAYS), QDAYS)


def f28_ttcf_249_kst_signal_to_noise_ratio_63(close: pd.Series) -> pd.Series:
    """63d |mean|/std of KST — trend-quality of KST."""
    return _snr(_kst(close), QDAYS)


def f28_ttcf_250_basket_signal_to_noise_avg_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean of basket SNRs (TRIX, TSI, CCI, CMO, DPO, KST) — ensemble trend-quality."""
    sn = pd.concat([
        _snr(_trix(close, 15), QDAYS).rename(0),
        _snr(_tsi(close, 25, 13), QDAYS).rename(1),
        _snr(_cci(high, low, close, 20), QDAYS).rename(2),
        _snr(_cmo(close, 14), QDAYS).rename(3),
        _snr(_dpo(close, MDAYS), QDAYS).rename(4),
        _snr(_kst(close), QDAYS).rename(5),
    ], axis=1)
    return sn.mean(axis=1)


def f28_ttcf_251_trix_information_coefficient_returns_63(close: pd.Series) -> pd.Series:
    """63d Pearson corr of TRIX with NEXT-bar return (PIT: TRIX shifted +1 to align past TRIX with next return)."""
    t = _trix(close, 15).shift(1)
    r = close.pct_change()
    return t.rolling(QDAYS, min_periods=MDAYS).corr(r)


def f28_ttcf_252_tsi_information_coefficient_returns_63(close: pd.Series) -> pd.Series:
    """63d Pearson corr of TSI(t-1) with bar-return(t)."""
    t = _tsi(close, 25, 13).shift(1)
    r = close.pct_change()
    return t.rolling(QDAYS, min_periods=MDAYS).corr(r)


def f28_ttcf_253_basket_information_coefficient_returns_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean IC across basket (TRIX, TSI, CCI, CMO, KST) lag-1 corr with return."""
    r = close.pct_change()
    ics = []
    for sig in (_trix(close, 15), _tsi(close, 25, 13), _cci(high, low, close, 20),
                _cmo(close, 14), _kst(close)):
        ics.append(sig.shift(1).rolling(QDAYS, min_periods=MDAYS).corr(r))
    return pd.concat([s.rename(i) for i, s in enumerate(ics)], axis=1).mean(axis=1)


# ============================================================
# Bucket BB — Pattern detectors on oscillators (254-263)
# ============================================================

def _triangle_pattern(sig, n=QDAYS):
    """Indicator: rolling range (max-min) is shrinking over n bars (regression slope < 0)."""
    rng = sig.rolling(MDAYS, min_periods=WDAYS).max() - sig.rolling(MDAYS, min_periods=WDAYS).min()
    sl = _rolling_slope(rng, n)
    return (sl < 0).astype(float).where(sl.notna(), np.nan)


def _head_shoulders_proxy(sig, n=QDAYS):
    """Approximate H&S: middle 1/3 of window has higher max than first 1/3 and last 1/3."""
    def _f(w):
        if np.isnan(w).any() or len(w) < 9:
            return np.nan
        third = max(len(w) // 3, 3)
        l = w[:third].max()
        m = w[third:2 * third].max()
        r = w[2 * third:].max()
        return float((m > l) and (m > r))
    return sig.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)


def _double_top(sig, thresh, n=QDAYS):
    """Approximate double-top in OB region: count of crossings of thresh (each up-down crossing pair = 1 top)."""
    above = (sig > thresh)
    enter = above & ~above.shift(1, fill_value=False)
    return (enter.astype(float).rolling(n, min_periods=max(n // 3, 2)).sum() >= 2).astype(float).where(sig.notna(), np.nan)


def f28_ttcf_254_trix_triangle_pattern_indicator_63(close: pd.Series) -> pd.Series:
    """1 if TRIX 21d range slope (over 63d) < 0 — TRIX triangle/contraction pattern."""
    return _triangle_pattern(_trix(close, 15), QDAYS)


def f28_ttcf_255_tsi_head_shoulders_pattern_proxy_63(close: pd.Series) -> pd.Series:
    """1 if TSI max in middle 1/3 of 63d window exceeds left/right thirds — H&S proxy."""
    return _head_shoulders_proxy(_tsi(close, 25, 13), QDAYS)


def f28_ttcf_256_cci_w_pattern_in_extreme_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Double-bottom (W) within extreme-low CCI region (<-100): >=2 entries below -100 in 63d."""
    c = _cci(high, low, close, 20)
    below = (c < -100.0)
    enter = below & ~below.shift(1, fill_value=False)
    return (enter.astype(float).rolling(QDAYS, min_periods=MDAYS).sum() >= 2).astype(float).where(c.notna(), np.nan)


def f28_ttcf_257_cmo_double_top_in_ob_63(close: pd.Series) -> pd.Series:
    """Double-top in CMO OB region (>50): >=2 entries above 50 in 63d."""
    return _double_top(_cmo(close, 14), 50.0, QDAYS)


def f28_ttcf_258_kst_failure_swing_pattern_63(close: pd.Series) -> pd.Series:
    """1 if KST made a higher-high then lower-high within 63d AND price made higher-high — failure swing."""
    k = _kst(close)
    k_high = k.rolling(QDAYS, min_periods=MDAYS).max()
    k_prev = k_high.shift(MDAYS)
    fail = k_high < k_prev
    return fail.astype(float).where(k.notna(), np.nan)


def f28_ttcf_259_dpo_consolidation_then_break_indicator_63(close: pd.Series) -> pd.Series:
    """1 if DPO range (21d) was < 50% of 63d-avg-range AND current DPO breaks above/below that range."""
    d = _dpo(close, MDAYS)
    rng21 = d.rolling(MDAYS, min_periods=WDAYS).max() - d.rolling(MDAYS, min_periods=WDAYS).min()
    rng_avg = rng21.rolling(QDAYS, min_periods=MDAYS).mean()
    prior_consolid = rng21.shift(MDAYS) < 0.5 * rng_avg
    pmax21 = d.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    pmin21 = d.shift(1).rolling(MDAYS, min_periods=WDAYS).min()
    brk = (d > pmax21) | (d < pmin21)
    return (prior_consolid & brk).astype(float).where(d.notna(), np.nan)


def f28_ttcf_260_cycle_pattern_break_indicator_63(close: pd.Series) -> pd.Series:
    """1 if dominant cycle period dropped by > 30% vs its 63d rolling median — cycle-regime break."""
    p = _dominant_cycle_proxy(close, MDAYS)
    med = p.rolling(QDAYS, min_periods=MDAYS).median()
    return (p < 0.7 * med).astype(float).where(p.notna() & med.notna(), np.nan)


def f28_ttcf_261_basket_triple_top_consensus_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if >=3 of basket {TRIX, TSI, CCI, CMO, KST} show triangle pattern in 63d."""
    cnt = pd.Series(0.0, index=close.index)
    for sig in (_trix(close, 15), _tsi(close, 25, 13), _cci(high, low, close, 20),
                _cmo(close, 14), _kst(close)):
        cnt = cnt + _triangle_pattern(sig, QDAYS).fillna(0)
    return (cnt >= 3).astype(float).where(close.notna(), np.nan)


def f28_ttcf_262_basket_head_shoulders_consensus(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if >=3 basket indicators show H&S middle-peak in 63d window."""
    cnt = pd.Series(0.0, index=close.index)
    for sig in (_trix(close, 15), _tsi(close, 25, 13), _cci(high, low, close, 20),
                _cmo(close, 14), _kst(close)):
        cnt = cnt + _head_shoulders_proxy(sig, QDAYS).fillna(0)
    return (cnt >= 3).astype(float).where(close.notna(), np.nan)


def f28_ttcf_263_basket_failure_swing_count_63(close: pd.Series) -> pd.Series:
    """Count of basket indicators with KST-style failure swing (lower 63d high than 21-prior 63d high)."""
    cnt = pd.Series(0.0, index=close.index)
    for sig in (_trix(close, 15), _tsi(close, 25, 13), _kst(close), _cmo(close, 14)):
        sh = sig.rolling(QDAYS, min_periods=MDAYS).max()
        fail = sh < sh.shift(MDAYS)
        cnt = cnt + fail.astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)


# ============================================================
# Bucket CC — Multi-horizon alignment within family (264-273)
# ============================================================

def _alignment_state(short_, med, long_):
    """1 if short > 0 AND med > 0 AND long > 0; -1 if all < 0; 0 otherwise."""
    bull = (short_ > 0) & (med > 0) & (long_ > 0)
    bear = (short_ < 0) & (med < 0) & (long_ < 0)
    out = pd.Series(np.nan, index=short_.index)
    out = out.where(~bull, 1.0)
    out = out.where(~bear, -1.0)
    valid = short_.notna() & med.notna() & long_.notna()
    out = out.where(valid, np.nan)
    return out.fillna(0.0).where(valid, np.nan)


def f28_ttcf_264_trix_short_med_long_alignment_state(close: pd.Series) -> pd.Series:
    """TRIX alignment across (5, 15, 50) — +1 all bullish, -1 all bearish, else 0."""
    return _alignment_state(_trix(close, 5), _trix(close, 15), _trix(close, 50))


def f28_ttcf_265_tsi_short_med_long_alignment_state(close: pd.Series) -> pd.Series:
    """TSI alignment across (5,3),(25,13),(50,25)."""
    return _alignment_state(_tsi(close, 5, 3), _tsi(close, 25, 13), _tsi(close, 50, 25))


def f28_ttcf_266_cci_short_med_long_alignment_state(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """CCI alignment across (5, 20, 100)."""
    return _alignment_state(_cci(high, low, close, 5),
                            _cci(high, low, close, 20),
                            _cci(high, low, close, 100))


def f28_ttcf_267_cmo_short_med_long_alignment_state(close: pd.Series) -> pd.Series:
    """CMO alignment across (5, 14, 100)."""
    return _alignment_state(_cmo(close, 5), _cmo(close, 14), _cmo(close, 100))


def f28_ttcf_268_dpo_short_med_long_alignment_state(close: pd.Series) -> pd.Series:
    """DPO alignment across (5, 21, 252)."""
    return _alignment_state(_dpo(close, 5), _dpo(close, MDAYS), _dpo(close, YDAYS))


def f28_ttcf_269_kst_short_med_long_alignment_state(close: pd.Series) -> pd.Series:
    """KST alignment using KST vs SMA(21,63,252) of KST — short/med/long smoothing."""
    k = _kst(close)
    return _alignment_state(k - k.rolling(MDAYS, min_periods=WDAYS).mean(),
                            k - k.rolling(QDAYS, min_periods=MDAYS).mean(),
                            k - k.rolling(YDAYS, min_periods=QDAYS).mean())


def f28_ttcf_270_cross_horizon_dispersion_zscore_252(close: pd.Series) -> pd.Series:
    """Std across z-scores of TRIX horizons {5,15,50} — TRIX cross-horizon dispersion."""
    zs = pd.concat([
        _rolling_zscore(_trix(close, 5), YDAYS, min_periods=QDAYS).rename(0),
        _rolling_zscore(_trix(close, 15), YDAYS, min_periods=QDAYS).rename(1),
        _rolling_zscore(_trix(close, 50), YDAYS, min_periods=QDAYS).rename(2),
    ], axis=1)
    return zs.std(axis=1)


def f28_ttcf_271_all_horizons_in_decline_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of oscillators whose ALL three horizons have 63d slope < 0."""
    cnt = pd.Series(0.0, index=close.index)
    families = [
        (_trix(close, 5), _trix(close, 15), _trix(close, 50)),
        (_tsi(close, 5, 3), _tsi(close, 25, 13), _tsi(close, 50, 25)),
        (_cci(high, low, close, 5), _cci(high, low, close, 20), _cci(high, low, close, 100)),
        (_cmo(close, 5), _cmo(close, 14), _cmo(close, 100)),
    ]
    for s, m, l in families:
        ss = _rolling_slope(s, QDAYS); ms = _rolling_slope(m, QDAYS); ls = _rolling_slope(l, QDAYS)
        all_decl = (ss < 0) & (ms < 0) & (ls < 0)
        cnt = cnt + all_decl.astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)


def f28_ttcf_272_monotonic_decline_across_horizons_state(close: pd.Series) -> pd.Series:
    """1 if TRIX(5) < TRIX(15) < TRIX(50) AND all < 0 — monotone short-to-long decline."""
    t5 = _trix(close, 5); t15 = _trix(close, 15); t50 = _trix(close, 50)
    cond = (t5 < t15) & (t15 < t50) & (t50 < 0)
    return cond.astype(float).where(t5.notna() & t15.notna() & t50.notna(), np.nan)


def f28_ttcf_273_horizon_lead_lag_difference_21(close: pd.Series) -> pd.Series:
    """TRIX(15) - TRIX(15).shift(21) minus TRIX(50) - TRIX(50).shift(21) — relative 21d horizon-lead change."""
    return (_trix(close, 15) - _trix(close, 15).shift(MDAYS)) - (_trix(close, 50) - _trix(close, 50).shift(MDAYS))


# ============================================================
# Bucket DD — Regime modeling (274-283)
# ============================================================

def _regime_age(state_mask: pd.Series) -> pd.Series:
    """Bars since regime last flipped — current regime age."""
    arr = state_mask.astype(bool).to_numpy()
    n = arr.size
    out = np.full(n, np.nan)
    age = 0
    started = False
    last = None
    for i in range(n):
        if not started:
            last = arr[i]
            age = 0
            started = True
            out[i] = 0.0
            continue
        if arr[i] != last:
            age = 0
            last = arr[i]
        else:
            age += 1
        out[i] = float(age)
    return pd.Series(out, index=state_mask.index)


def f28_ttcf_274_trix_regime_above_zero_persistence(close: pd.Series) -> pd.Series:
    """Current age (bars) of TRIX(15) > 0 / < 0 regime."""
    t = _trix(close, 15)
    return _regime_age(t > 0).where(t.notna(), np.nan)


def f28_ttcf_275_tsi_regime_age_current(close: pd.Series) -> pd.Series:
    """Current age of TSI(25,13) > 0 / < 0 regime."""
    t = _tsi(close, 25, 13)
    return _regime_age(t > 0).where(t.notna(), np.nan)


def f28_ttcf_276_cci_regime_above_100_persistence(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current age of CCI(20) > 100 / <= 100 regime."""
    c = _cci(high, low, close, 20)
    return _regime_age(c > 100.0).where(c.notna(), np.nan)


def f28_ttcf_277_cmo_regime_above_50_persistence(close: pd.Series) -> pd.Series:
    """Current age of CMO(14) > 50 / <= 50 regime."""
    c = _cmo(close, 14)
    return _regime_age(c > 50.0).where(c.notna(), np.nan)


def f28_ttcf_278_dpo_regime_above_zero_persistence(close: pd.Series) -> pd.Series:
    """Current age of DPO(21) > 0 / < 0 regime."""
    d = _dpo(close, MDAYS)
    return _regime_age(d > 0).where(d.notna(), np.nan)


def f28_ttcf_279_kst_regime_above_zero_persistence(close: pd.Series) -> pd.Series:
    """Current age of KST > 0 / < 0 regime."""
    k = _kst(close)
    return _regime_age(k > 0).where(k.notna(), np.nan)


def f28_ttcf_280_basket_regime_age_avg(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean regime age across (TRIX>0, TSI>0, CCI>100, CMO>50, DPO>0, KST>0)."""
    ages = []
    ages.append(_regime_age(_trix(close, 15) > 0))
    ages.append(_regime_age(_tsi(close, 25, 13) > 0))
    ages.append(_regime_age(_cci(high, low, close, 20) > 100.0))
    ages.append(_regime_age(_cmo(close, 14) > 50.0))
    ages.append(_regime_age(_dpo(close, MDAYS) > 0))
    ages.append(_regime_age(_kst(close) > 0))
    return pd.concat([a.rename(i) for i, a in enumerate(ages)], axis=1).mean(axis=1)


def f28_ttcf_281_basket_regime_change_count_252(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of basket-regime flips over past 252 bars (across all 6 indicators)."""
    cnt = pd.Series(0.0, index=close.index)
    for mask in ((_trix(close, 15) > 0), (_tsi(close, 25, 13) > 0),
                 (_cci(high, low, close, 20) > 100.0), (_cmo(close, 14) > 50.0),
                 (_dpo(close, MDAYS) > 0), (_kst(close) > 0)):
        flip = (mask.astype(int).diff().abs() > 0).astype(float)
        cnt = cnt + flip.rolling(YDAYS, min_periods=QDAYS).sum().fillna(0)
    return cnt.where(close.notna(), np.nan)


def f28_ttcf_282_basket_regime_terminal_indicator(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if avg basket regime age > 100 bars AND at least 3 indicators just flipped bearish in past 21."""
    avg_age = f28_ttcf_280_basket_regime_age_avg(high, low, close)
    flips = pd.Series(0.0, index=close.index)
    for mask in ((_trix(close, 15) > 0), (_tsi(close, 25, 13) > 0),
                 (_cci(high, low, close, 20) > 100.0), (_cmo(close, 14) > 50.0),
                 (_dpo(close, MDAYS) > 0), (_kst(close) > 0)):
        bearish_flip = mask.astype(int).diff() < 0
        flips = flips + bearish_flip.astype(float).rolling(MDAYS, min_periods=1).max().fillna(0)
    return ((avg_age > 100.0) & (flips >= 3)).astype(float).where(avg_age.notna(), np.nan)


def f28_ttcf_283_basket_regime_transition_velocity(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Number of basket regime flips in past 21 — regime transition velocity."""
    cnt = pd.Series(0.0, index=close.index)
    for mask in ((_trix(close, 15) > 0), (_tsi(close, 25, 13) > 0),
                 (_cci(high, low, close, 20) > 100.0), (_cmo(close, 14) > 50.0),
                 (_dpo(close, MDAYS) > 0), (_kst(close) > 0)):
        flip = (mask.astype(int).diff().abs() > 0).astype(float)
        cnt = cnt + flip.rolling(MDAYS, min_periods=WDAYS).sum().fillna(0)
    return cnt.where(close.notna(), np.nan)


# ============================================================
# Bucket EE — Aggregate / terminal scoring (284-300)
# ============================================================

# extended-basket helpers: PFE, ER, RWI, VQI (modern) + TRIX, TSI, CCI, CMO, DPO, KST (classical)

def _pfe(close, n=10):
    diff_n = close - close.shift(n)
    num = np.sqrt(diff_n.pow(2) + float(n) ** 2)
    d1 = close.diff()
    path = np.sqrt(d1.pow(2) + 1.0).rolling(n, min_periods=max(n // 3, 2)).sum()
    raw = 100.0 * np.sign(diff_n) * _safe_div(num, path)
    return _ema(raw, 5)


def _efficiency_ratio(close, n=10):
    num = (close - close.shift(n)).abs()
    den = close.diff().abs().rolling(n, min_periods=max(n // 3, 2)).sum()
    return _safe_div(num, den)


def _rwi_high(high, low, close, n=14):
    return _safe_div(high - low.shift(n), _atr(high, low, close, n) * np.sqrt(float(n)))


def _vqi_proxy(open_, high, low, close):
    pc = close.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    a = _safe_div(close - pc, tr)
    b = _safe_div(close - open_, (high - low).replace(0, np.nan))
    return _ema(_ema(((a + b) / 2.0).cumsum(), 5), 9)


def _extended_basket_classical(high, low, close):
    return [_trix(close, 15), _tsi(close, 25, 13), _cci(high, low, close, 20),
            _cmo(close, 14), _dpo(close, MDAYS), _kst(close)]


def _extended_basket_modern(open_, high, low, close):
    return [_pfe(close, 10), _efficiency_ratio(close, 10),
            _rwi_high(high, low, close, 14), _vqi_proxy(open_, high, low, close)]


def f28_ttcf_284_extended_basket_topping_score(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum over all 10 basket indicators (6 classical + 4 modern) of z-score > 1 (OB count). Higher = more extended."""
    cnt = pd.Series(0.0, index=close.index)
    for sig in _extended_basket_classical(high, low, close) + _extended_basket_modern(open, high, low, close):
        z = _rolling_zscore(sig, YDAYS, min_periods=QDAYS)
        cnt = cnt + (z > 1.0).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)


def f28_ttcf_285_extended_basket_extreme_z_count_252(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of basket indicators with |z|>2 over 252d — extreme breadth."""
    cnt = pd.Series(0.0, index=close.index)
    for sig in _extended_basket_classical(high, low, close) + _extended_basket_modern(open, high, low, close):
        z = _rolling_zscore(sig, YDAYS, min_periods=QDAYS)
        cnt = cnt + (z.abs() > 2.0).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)


def f28_ttcf_286_extended_basket_bearish_cross_count_21d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of basket indicators with bearish EMA9 signal-cross in past 21 bars."""
    cnt = pd.Series(0.0, index=close.index)
    for sig in _extended_basket_classical(high, low, close) + _extended_basket_modern(open, high, low, close):
        s = _ema(sig, 9)
        d = sig - s
        ev = ((d.shift(1) > 0) & (d <= 0)).astype(float)
        cnt = cnt + (ev.rolling(MDAYS, min_periods=1).max() > 0).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)


def f28_ttcf_287_extended_basket_divergence_count_63(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of basket indicators with bearish divergence (price 63d-high but indicator below)."""
    cnt = pd.Series(0.0, index=close.index)
    p_new = high >= high.rolling(QDAYS, min_periods=MDAYS).max()
    for sig in _extended_basket_classical(high, low, close) + _extended_basket_modern(open, high, low, close):
        below = sig < sig.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
        cnt = cnt + (p_new & below).astype(float).fillna(0)
    return cnt.where(close.notna(), np.nan)


def f28_ttcf_288_extended_basket_avg_zscore_252(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean 252d z-score across all 10 basket indicators — extended-ensemble extension."""
    zs = []
    for sig in _extended_basket_classical(high, low, close) + _extended_basket_modern(open, high, low, close):
        zs.append(_rolling_zscore(sig, YDAYS, min_periods=QDAYS))
    return pd.concat([z.rename(i) for i, z in enumerate(zs)], axis=1).mean(axis=1)


def f28_ttcf_289_extended_basket_dispersion_zscore_252(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std across 252d z-scores of all 10 basket indicators — extended-basket dispersion."""
    zs = []
    for sig in _extended_basket_classical(high, low, close) + _extended_basket_modern(open, high, low, close):
        zs.append(_rolling_zscore(sig, YDAYS, min_periods=QDAYS))
    return pd.concat([z.rename(i) for i, z in enumerate(zs)], axis=1).std(axis=1)


def f28_ttcf_290_extended_basket_correlation_break_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if mean pairwise 63d corr among 5 basket indicators (TRIX,TSI,CCI,CMO,KST)
    drops > 0.4 vs its 252d rolling mean — basket decoupling."""
    cols = [_trix(close, 15), _tsi(close, 25, 13), _cci(high, low, close, 20),
            _cmo(close, 14), _kst(close)]
    pairs = []
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            pairs.append(cols[i].rolling(QDAYS, min_periods=MDAYS).corr(cols[j]))
    mean_corr = pd.concat([p.rename(k) for k, p in enumerate(pairs)], axis=1).mean(axis=1)
    base = mean_corr.rolling(YDAYS, min_periods=QDAYS).mean()
    return ((base - mean_corr) > 0.4).astype(float).where(mean_corr.notna() & base.notna(), np.nan)


def f28_ttcf_291_extended_basket_persistence_after_extreme_252(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars where >=5/10 basket indicators had z>1 — sustained extension."""
    cnt = pd.Series(0.0, index=close.index)
    for sig in _extended_basket_classical(high, low, close) + _extended_basket_modern(open, high, low, close):
        z = _rolling_zscore(sig, YDAYS, min_periods=QDAYS)
        cnt = cnt + (z > 1.0).astype(float).fillna(0)
    return (cnt >= 5).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(close.notna(), np.nan)


def f28_ttcf_292_extended_basket_decay_velocity_post_peak_63(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean fractional decay (63d max - current)/|63d max| across 10 indicators."""
    out = pd.Series(0.0, index=close.index)
    n_ind = 0
    for sig in _extended_basket_classical(high, low, close) + _extended_basket_modern(open, high, low, close):
        pmax = sig.rolling(QDAYS, min_periods=MDAYS).max()
        out = out + _safe_div(pmax - sig, pmax.abs()).fillna(0)
        n_ind += 1
    return (out / float(n_ind)).where(close.notna(), np.nan)


def f28_ttcf_293_classical_modern_basket_consensus_bearish(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if classical-basket avg-z < 0 AND modern-basket avg-z < 0 AND both have at least one z<-1."""
    c_zs = [_rolling_zscore(s, YDAYS, min_periods=QDAYS) for s in _extended_basket_classical(high, low, close)]
    m_zs = [_rolling_zscore(s, YDAYS, min_periods=QDAYS) for s in _extended_basket_modern(open, high, low, close)]
    c_mean = pd.concat([z.rename(i) for i, z in enumerate(c_zs)], axis=1).mean(axis=1)
    m_mean = pd.concat([z.rename(i) for i, z in enumerate(m_zs)], axis=1).mean(axis=1)
    c_neg1 = pd.concat([z.rename(i) for i, z in enumerate(c_zs)], axis=1).min(axis=1) < -1.0
    m_neg1 = pd.concat([z.rename(i) for i, z in enumerate(m_zs)], axis=1).min(axis=1) < -1.0
    cond = (c_mean < 0) & (m_mean < 0) & c_neg1 & m_neg1
    return cond.astype(float).where(c_mean.notna() & m_mean.notna(), np.nan)


def f28_ttcf_294_cross_oscillator_terminal_indicator(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if (>=5/10 basket indicators z>2) AND (>=3/10 had bearish cross in past 21d) — terminal pattern."""
    ext_count = f28_ttcf_285_extended_basket_extreme_z_count_252(open, high, low, close)
    cross_count = f28_ttcf_286_extended_basket_bearish_cross_count_21d(open, high, low, close)
    return ((ext_count >= 5) & (cross_count >= 3)).astype(float).where(ext_count.notna(), np.nan)


def f28_ttcf_295_multi_indicator_topping_aggregate_at_252_high(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Topping-score (z>1 count among 10 basket) when price at its 252d high; NaN otherwise."""
    at_max = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    score = f28_ttcf_284_extended_basket_topping_score(open, high, low, close)
    return score.where(at_max, np.nan)


def f28_ttcf_296_extended_failure_breadth_at_top(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Number of basket indicators with failure-swing pattern (lower 63d high vs 21-bar prior) when price at 252d high."""
    at_max = high == high.rolling(YDAYS, min_periods=QDAYS).max()
    cnt = pd.Series(0.0, index=close.index)
    for sig in _extended_basket_classical(high, low, close) + _extended_basket_modern(open, high, low, close):
        sh = sig.rolling(QDAYS, min_periods=MDAYS).max()
        fail = sh < sh.shift(MDAYS)
        cnt = cnt + fail.astype(float).fillna(0)
    return cnt.where(at_max, np.nan)


def f28_ttcf_297_extended_extreme_to_normal_velocity_avg(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Avg velocity from 63d-z-max to current-z across 10 basket — extreme-to-normal velocity."""
    out = pd.Series(0.0, index=close.index)
    n_ind = 0
    for sig in _extended_basket_classical(high, low, close) + _extended_basket_modern(open, high, low, close):
        z = _rolling_zscore(sig, YDAYS, min_periods=QDAYS)
        pmax = z.rolling(QDAYS, min_periods=MDAYS).max()
        out = out + ((pmax - z) / float(QDAYS)).fillna(0)
        n_ind += 1
    return (out / float(n_ind)).where(close.notna(), np.nan)


def f28_ttcf_298_extended_universe_correlation_breakdown(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean pairwise 63d corr among all 10 basket indicators — extended-universe corr (drops = breakdown)."""
    cols = _extended_basket_classical(high, low, close) + _extended_basket_modern(open, high, low, close)
    pairs = []
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            pairs.append(cols[i].rolling(QDAYS, min_periods=MDAYS).corr(cols[j]))
    return pd.concat([p.rename(k) for k, p in enumerate(pairs)], axis=1).mean(axis=1)


def f28_ttcf_299_extended_universe_persistence_after_extreme_252(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of past 252 bars where extended-basket-avg-z > 1.5 — sustained extreme-extension."""
    avgz = f28_ttcf_288_extended_basket_avg_zscore_252(open, high, low, close)
    return (avgz > 1.5).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(avgz.notna(), np.nan)


def f28_ttcf_300_extended_terminal_topping_master_score(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Master terminal score = topping-score + extreme-z count + bearish-cross count + divergence count
    + (correlation-break indicator * 5). Higher = stronger terminal topping signal."""
    a = f28_ttcf_284_extended_basket_topping_score(open, high, low, close).fillna(0)
    b = f28_ttcf_285_extended_basket_extreme_z_count_252(open, high, low, close).fillna(0)
    c = f28_ttcf_286_extended_basket_bearish_cross_count_21d(open, high, low, close).fillna(0)
    d = f28_ttcf_287_extended_basket_divergence_count_63(open, high, low, close).fillna(0)
    e = f28_ttcf_290_extended_basket_correlation_break_63(high, low, close).fillna(0) * 5.0
    return (a + b + c + d + e).where(close.notna(), np.nan)


# ============================================================
#                         REGISTRY 226_300
# ============================================================

TRIX_TSI_CCI_FAMILY_BASE_REGISTRY_226_300 = {
    "f28_ttcf_226_hilbert_in_phase_proxy": {"inputs": ["close"], "func": f28_ttcf_226_hilbert_in_phase_proxy},
    "f28_ttcf_227_hilbert_quadrature_proxy": {"inputs": ["close"], "func": f28_ttcf_227_hilbert_quadrature_proxy},
    "f28_ttcf_228_hilbert_period_proxy": {"inputs": ["close"], "func": f28_ttcf_228_hilbert_period_proxy},
    "f28_ttcf_229_dominant_cycle_proxy_21": {"inputs": ["close"], "func": f28_ttcf_229_dominant_cycle_proxy_21},
    "f28_ttcf_230_trend_vs_cycle_ratio_63": {"inputs": ["close"], "func": f28_ttcf_230_trend_vs_cycle_ratio_63},
    "f28_ttcf_231_dominant_cycle_zscore_252": {"inputs": ["close"], "func": f28_ttcf_231_dominant_cycle_zscore_252},
    "f28_ttcf_232_cycle_phase_bearish_state": {"inputs": ["close"], "func": f28_ttcf_232_cycle_phase_bearish_state},
    "f28_ttcf_233_cycle_phase_dwell_in_top_quartile_63": {"inputs": ["close"], "func": f28_ttcf_233_cycle_phase_dwell_in_top_quartile_63},
    "f28_ttcf_234_cycle_amplitude_decay_63": {"inputs": ["close"], "func": f28_ttcf_234_cycle_amplitude_decay_63},
    "f28_ttcf_235_cycle_amplitude_zscore_252": {"inputs": ["close"], "func": f28_ttcf_235_cycle_amplitude_zscore_252},
    "f28_ttcf_236_dpo_residual_volatility_63": {"inputs": ["close"], "func": f28_ttcf_236_dpo_residual_volatility_63},
    "f28_ttcf_237_dpo_zero_cross_count_252": {"inputs": ["close"], "func": f28_ttcf_237_dpo_zero_cross_count_252},
    "f28_ttcf_238_dpo_recent_peak_height_zscore": {"inputs": ["close"], "func": f28_ttcf_238_dpo_recent_peak_height_zscore},
    "f28_ttcf_239_dpo_consecutive_above_zero_streak": {"inputs": ["close"], "func": f28_ttcf_239_dpo_consecutive_above_zero_streak},
    "f28_ttcf_240_dpo_persistence_above_q90_504": {"inputs": ["close"], "func": f28_ttcf_240_dpo_persistence_above_q90_504},
    "f28_ttcf_241_dpo_seasonality_check_252": {"inputs": ["close"], "func": f28_ttcf_241_dpo_seasonality_check_252},
    "f28_ttcf_242_dpo_skew_63": {"inputs": ["close"], "func": f28_ttcf_242_dpo_skew_63},
    "f28_ttcf_243_dpo_kurtosis_63": {"inputs": ["close"], "func": f28_ttcf_243_dpo_kurtosis_63},
    "f28_ttcf_244_trix_signal_to_noise_ratio_63": {"inputs": ["close"], "func": f28_ttcf_244_trix_signal_to_noise_ratio_63},
    "f28_ttcf_245_tsi_signal_to_noise_ratio_63": {"inputs": ["close"], "func": f28_ttcf_245_tsi_signal_to_noise_ratio_63},
    "f28_ttcf_246_cci_signal_to_noise_ratio_63": {"inputs": ["high", "low", "close"], "func": f28_ttcf_246_cci_signal_to_noise_ratio_63},
    "f28_ttcf_247_cmo_signal_to_noise_ratio_63": {"inputs": ["close"], "func": f28_ttcf_247_cmo_signal_to_noise_ratio_63},
    "f28_ttcf_248_dpo_signal_to_noise_ratio_63": {"inputs": ["close"], "func": f28_ttcf_248_dpo_signal_to_noise_ratio_63},
    "f28_ttcf_249_kst_signal_to_noise_ratio_63": {"inputs": ["close"], "func": f28_ttcf_249_kst_signal_to_noise_ratio_63},
    "f28_ttcf_250_basket_signal_to_noise_avg_63": {"inputs": ["high", "low", "close"], "func": f28_ttcf_250_basket_signal_to_noise_avg_63},
    "f28_ttcf_251_trix_information_coefficient_returns_63": {"inputs": ["close"], "func": f28_ttcf_251_trix_information_coefficient_returns_63},
    "f28_ttcf_252_tsi_information_coefficient_returns_63": {"inputs": ["close"], "func": f28_ttcf_252_tsi_information_coefficient_returns_63},
    "f28_ttcf_253_basket_information_coefficient_returns_63": {"inputs": ["high", "low", "close"], "func": f28_ttcf_253_basket_information_coefficient_returns_63},
    "f28_ttcf_254_trix_triangle_pattern_indicator_63": {"inputs": ["close"], "func": f28_ttcf_254_trix_triangle_pattern_indicator_63},
    "f28_ttcf_255_tsi_head_shoulders_pattern_proxy_63": {"inputs": ["close"], "func": f28_ttcf_255_tsi_head_shoulders_pattern_proxy_63},
    "f28_ttcf_256_cci_w_pattern_in_extreme_63": {"inputs": ["high", "low", "close"], "func": f28_ttcf_256_cci_w_pattern_in_extreme_63},
    "f28_ttcf_257_cmo_double_top_in_ob_63": {"inputs": ["close"], "func": f28_ttcf_257_cmo_double_top_in_ob_63},
    "f28_ttcf_258_kst_failure_swing_pattern_63": {"inputs": ["close"], "func": f28_ttcf_258_kst_failure_swing_pattern_63},
    "f28_ttcf_259_dpo_consolidation_then_break_indicator_63": {"inputs": ["close"], "func": f28_ttcf_259_dpo_consolidation_then_break_indicator_63},
    "f28_ttcf_260_cycle_pattern_break_indicator_63": {"inputs": ["close"], "func": f28_ttcf_260_cycle_pattern_break_indicator_63},
    "f28_ttcf_261_basket_triple_top_consensus_indicator": {"inputs": ["high", "low", "close"], "func": f28_ttcf_261_basket_triple_top_consensus_indicator},
    "f28_ttcf_262_basket_head_shoulders_consensus": {"inputs": ["high", "low", "close"], "func": f28_ttcf_262_basket_head_shoulders_consensus},
    "f28_ttcf_263_basket_failure_swing_count_63": {"inputs": ["close"], "func": f28_ttcf_263_basket_failure_swing_count_63},
    "f28_ttcf_264_trix_short_med_long_alignment_state": {"inputs": ["close"], "func": f28_ttcf_264_trix_short_med_long_alignment_state},
    "f28_ttcf_265_tsi_short_med_long_alignment_state": {"inputs": ["close"], "func": f28_ttcf_265_tsi_short_med_long_alignment_state},
    "f28_ttcf_266_cci_short_med_long_alignment_state": {"inputs": ["high", "low", "close"], "func": f28_ttcf_266_cci_short_med_long_alignment_state},
    "f28_ttcf_267_cmo_short_med_long_alignment_state": {"inputs": ["close"], "func": f28_ttcf_267_cmo_short_med_long_alignment_state},
    "f28_ttcf_268_dpo_short_med_long_alignment_state": {"inputs": ["close"], "func": f28_ttcf_268_dpo_short_med_long_alignment_state},
    "f28_ttcf_269_kst_short_med_long_alignment_state": {"inputs": ["close"], "func": f28_ttcf_269_kst_short_med_long_alignment_state},
    "f28_ttcf_270_cross_horizon_dispersion_zscore_252": {"inputs": ["close"], "func": f28_ttcf_270_cross_horizon_dispersion_zscore_252},
    "f28_ttcf_271_all_horizons_in_decline_count_63": {"inputs": ["high", "low", "close"], "func": f28_ttcf_271_all_horizons_in_decline_count_63},
    "f28_ttcf_272_monotonic_decline_across_horizons_state": {"inputs": ["close"], "func": f28_ttcf_272_monotonic_decline_across_horizons_state},
    "f28_ttcf_273_horizon_lead_lag_difference_21": {"inputs": ["close"], "func": f28_ttcf_273_horizon_lead_lag_difference_21},
    "f28_ttcf_274_trix_regime_above_zero_persistence": {"inputs": ["close"], "func": f28_ttcf_274_trix_regime_above_zero_persistence},
    "f28_ttcf_275_tsi_regime_age_current": {"inputs": ["close"], "func": f28_ttcf_275_tsi_regime_age_current},
    "f28_ttcf_276_cci_regime_above_100_persistence": {"inputs": ["high", "low", "close"], "func": f28_ttcf_276_cci_regime_above_100_persistence},
    "f28_ttcf_277_cmo_regime_above_50_persistence": {"inputs": ["close"], "func": f28_ttcf_277_cmo_regime_above_50_persistence},
    "f28_ttcf_278_dpo_regime_above_zero_persistence": {"inputs": ["close"], "func": f28_ttcf_278_dpo_regime_above_zero_persistence},
    "f28_ttcf_279_kst_regime_above_zero_persistence": {"inputs": ["close"], "func": f28_ttcf_279_kst_regime_above_zero_persistence},
    "f28_ttcf_280_basket_regime_age_avg": {"inputs": ["high", "low", "close"], "func": f28_ttcf_280_basket_regime_age_avg},
    "f28_ttcf_281_basket_regime_change_count_252": {"inputs": ["high", "low", "close"], "func": f28_ttcf_281_basket_regime_change_count_252},
    "f28_ttcf_282_basket_regime_terminal_indicator": {"inputs": ["high", "low", "close"], "func": f28_ttcf_282_basket_regime_terminal_indicator},
    "f28_ttcf_283_basket_regime_transition_velocity": {"inputs": ["high", "low", "close"], "func": f28_ttcf_283_basket_regime_transition_velocity},
    "f28_ttcf_284_extended_basket_topping_score": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_284_extended_basket_topping_score},
    "f28_ttcf_285_extended_basket_extreme_z_count_252": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_285_extended_basket_extreme_z_count_252},
    "f28_ttcf_286_extended_basket_bearish_cross_count_21d": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_286_extended_basket_bearish_cross_count_21d},
    "f28_ttcf_287_extended_basket_divergence_count_63": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_287_extended_basket_divergence_count_63},
    "f28_ttcf_288_extended_basket_avg_zscore_252": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_288_extended_basket_avg_zscore_252},
    "f28_ttcf_289_extended_basket_dispersion_zscore_252": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_289_extended_basket_dispersion_zscore_252},
    "f28_ttcf_290_extended_basket_correlation_break_63": {"inputs": ["high", "low", "close"], "func": f28_ttcf_290_extended_basket_correlation_break_63},
    "f28_ttcf_291_extended_basket_persistence_after_extreme_252": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_291_extended_basket_persistence_after_extreme_252},
    "f28_ttcf_292_extended_basket_decay_velocity_post_peak_63": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_292_extended_basket_decay_velocity_post_peak_63},
    "f28_ttcf_293_classical_modern_basket_consensus_bearish": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_293_classical_modern_basket_consensus_bearish},
    "f28_ttcf_294_cross_oscillator_terminal_indicator": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_294_cross_oscillator_terminal_indicator},
    "f28_ttcf_295_multi_indicator_topping_aggregate_at_252_high": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_295_multi_indicator_topping_aggregate_at_252_high},
    "f28_ttcf_296_extended_failure_breadth_at_top": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_296_extended_failure_breadth_at_top},
    "f28_ttcf_297_extended_extreme_to_normal_velocity_avg": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_297_extended_extreme_to_normal_velocity_avg},
    "f28_ttcf_298_extended_universe_correlation_breakdown": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_298_extended_universe_correlation_breakdown},
    "f28_ttcf_299_extended_universe_persistence_after_extreme_252": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_299_extended_universe_persistence_after_extreme_252},
    "f28_ttcf_300_extended_terminal_topping_master_score": {"inputs": ["open", "high", "low", "close"], "func": f28_ttcf_300_extended_terminal_topping_master_score},
}
