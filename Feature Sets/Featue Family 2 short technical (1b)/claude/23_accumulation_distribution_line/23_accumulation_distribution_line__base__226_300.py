"""accumulation_distribution_line base features 226-300 — Pipeline 1b-technical.

4th-tier extension. 75 NEW distinct hypotheses across Chaikin / Wilder / Elder /
Klinger / Twiggs / Williams /Fosback / Wyckoff practitioner literatures.
Strictly disjoint from base 001-225.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers.
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


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=max(n // 3, 2)).mean()


# ---- domain helpers (PIT-clean) ----

def _clv(high, low, close):
    return _safe_div(((close - low) - (high - close)), (high - low))


def _ad_line(high, low, close, volume):
    return (_clv(high, low, close) * volume).cumsum()


def _cmf(high, low, close, volume, n=20):
    mfv = _clv(high, low, close) * volume
    return _safe_div(mfv.rolling(n, min_periods=max(n // 3, 2)).sum(),
                     volume.rolling(n, min_periods=max(n // 3, 2)).sum())


def _mfi_components(high, low, close, volume, n=14):
    """Returns (pmf_n, nmf_n, mfi) — Wilder typical-price money flow."""
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pmf = rmf.where(tp > tp.shift(1), 0.0)
    nmf = rmf.where(tp < tp.shift(1), 0.0)
    pmf_n = pmf.rolling(n, min_periods=max(n // 3, 2)).sum()
    nmf_n = nmf.rolling(n, min_periods=max(n // 3, 2)).sum()
    mfr = _safe_div(pmf_n, nmf_n)
    mfi = 100.0 - 100.0 / (1.0 + mfr)
    return pmf_n, nmf_n, mfi


def _mfi(high, low, close, volume, n=14):
    _, _, m = _mfi_components(high, low, close, volume, n)
    return m


def _force_index(close, volume, n=13):
    raw = close.diff() * volume
    if n <= 1:
        return raw
    return raw.ewm(span=n, adjust=False, min_periods=max(n // 3, 2)).mean()


def _kvo(high, low, close, volume, fast=34, slow=55):
    tp = (high + low + close) / 3.0
    trend = np.sign(tp.diff()).fillna(0.0)
    dm = (high - low)
    cm = dm.where(trend == trend.shift(1), dm + dm.shift(1))
    vf = volume * trend * (2.0 * _safe_div(dm, cm.replace(0, np.nan)) - 1.0) * 100.0
    ef = vf.ewm(span=fast, adjust=False, min_periods=max(fast // 3, 2)).mean()
    es = vf.ewm(span=slow, adjust=False, min_periods=max(slow // 3, 2)).mean()
    return ef - es


def _kvo_signal(kvo, n=13):
    return kvo.ewm(span=n, adjust=False, min_periods=max(n // 3, 2)).mean()


def _twiggs_mf(high, low, close, volume, n=21):
    """Twiggs Money Flow — uses TR-based denominator and Wilder smoothing."""
    tr_high = pd.concat([high, close.shift(1)], axis=1).max(axis=1)
    tr_low = pd.concat([low, close.shift(1)], axis=1).min(axis=1)
    tr = tr_high - tr_low
    ad = _safe_div(2.0 * close - tr_high - tr_low, tr.replace(0, np.nan)) * volume
    # Wilder smoothing approx: EMA with alpha=1/n
    ad_w = ad.ewm(alpha=1.0 / n, adjust=False, min_periods=max(n // 3, 2)).mean()
    v_w = volume.ewm(alpha=1.0 / n, adjust=False, min_periods=max(n // 3, 2)).mean()
    return _safe_div(ad_w, v_w)


def _pvi(close, volume):
    rt = close.pct_change()
    inc = volume > volume.shift(1)
    delta = rt.where(inc, 0.0).fillna(0.0)
    return (1.0 + delta).cumprod() * 1000.0


def _nvi(close, volume):
    rt = close.pct_change()
    dec = volume < volume.shift(1)
    delta = rt.where(dec, 0.0).fillna(0.0)
    return (1.0 + delta).cumprod() * 1000.0


def _williams_ad(high, low, close):
    """Larry Williams AD = cumsum of true range accumulation."""
    pc = close.shift(1)
    th = pd.concat([high, pc], axis=1).max(axis=1)
    tl = pd.concat([low, pc], axis=1).min(axis=1)
    ad = pd.Series(0.0, index=close.index)
    ad = ad.where(close == pc, np.nan)
    up = close > pc
    dn = close < pc
    ad = (close - tl).where(up, 0.0) + (close - th).where(dn, 0.0)
    return ad.cumsum()


def _chaikin_osc(high, low, close, volume, fast=3, slow=10):
    ad = _ad_line(high, low, close, volume)
    return ad.ewm(span=fast, adjust=False, min_periods=max(fast // 3, 2)).mean() \
         - ad.ewm(span=slow, adjust=False, min_periods=max(slow // 3, 2)).mean()


def _pivot_high_event(s, k=5):
    """Confirmed local-high pivot: s[t-k] > s[t-k+1..t] AND > s[t-2k..t-k-1].
    Implemented right-anchored: at bar t, look at window of (2k+1) ending at t,
    centred at position k from the end means we need the bar at t-k to be max.
    To be PIT-clean we mark at bar t whether t-k was a confirmed pivot
    (i.e. it was the strict max of window [t-2k..t])."""
    n = 2 * k + 1
    rmax = s.rolling(n, min_periods=n).max()
    # the center of the window (position k from the start of the window) is s.shift(k)
    center = s.shift(k)
    is_pivot = (center == rmax) & rmax.notna()
    return is_pivot.astype(float)


def _pivot_low_event(s, k=5):
    n = 2 * k + 1
    rmin = s.rolling(n, min_periods=n).min()
    center = s.shift(k)
    is_pivot = (center == rmin) & rmin.notna()
    return is_pivot.astype(float)


def _avwap_from(price, volume, anchor_mask):
    """Anchored VWAP: at each bar, cumulative VWAP since the last True in anchor_mask.
    PIT-clean: anchor_mask is a boolean Series of trigger bars (known at bar t)."""
    grp = anchor_mask.astype(bool).cumsum()
    pv = price * volume
    pv_cs = pv.groupby(grp).cumsum()
    v_cs = volume.groupby(grp).cumsum()
    out = _safe_div(pv_cs, v_cs)
    # mask bars before any anchor (grp == 0)
    return out.where(grp > 0, np.nan)


# ============================================================
# Bucket A — Chaikin Oscillator deeper (226-230)
# ============================================================

def f23_adld_226_chaikin_osc_3_10_histogram_diminishing_peaks_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of Chaikin-osc local peaks in last 63d that are LOWER than previous peak
    while price prints higher highs — diminishing positive momentum sequence."""
    co = _chaikin_osc(high, low, close, volume, 3, 10)
    pk = _pivot_high_event(co, k=3)
    pk_val = co.where(pk > 0).ffill()
    prev_pk_val = pk_val.shift(QDAYS // 3)
    declining = (pk_val < prev_pk_val).astype(float)
    p_hh = close > close.shift(MDAYS)
    return (declining * p_hh.astype(float)).rolling(QDAYS, min_periods=MDAYS).sum()


def f23_adld_227_chaikin_osc_zero_cross_count_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Number of zero-line crosses by Chaikin oscillator in last 63d — regime instability."""
    co = _chaikin_osc(high, low, close, volume, 3, 10)
    cross = ((co * co.shift(1)) < 0).astype(float)
    return cross.rolling(QDAYS, min_periods=MDAYS).sum()


def f23_adld_228_chaikin_osc_bearish_div_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish Chaikin-osc divergence at 252d horizon: price new 252d high, osc < prior 252d max."""
    co = _chaikin_osc(high, low, close, volume, 3, 10)
    p_new = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    co_below = co < co.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    return (p_new & co_below).astype(float)


def f23_adld_229_chaikin_osc_negative_area_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Integral of negative values of Chaikin osc over trailing 252d — distribution intensity."""
    co = _chaikin_osc(high, low, close, volume, 3, 10)
    neg = (-co.clip(upper=0.0))
    return neg.rolling(YDAYS, min_periods=QDAYS).sum()


def f23_adld_230_chaikin_osc_lower_high_at_price_high(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """At confirmed price pivot-high (k=5), 1 if Chaikin osc's pivot value < previous osc pivot value."""
    co = _chaikin_osc(high, low, close, volume, 3, 10)
    p_pv = _pivot_high_event(close, k=5)
    co_pv = co.where(_pivot_high_event(co, k=5) > 0).ffill()
    prev_co = co_pv.shift(1)
    ev = (p_pv > 0) & (co_pv < prev_co)
    return ev.astype(float)


# ============================================================
# Bucket B — Money Flow Index (231-239)
# ============================================================

def f23_adld_231_mfi_failure_swing_top_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Wilder failure swing top on MFI(14): a high>80, pullback, a lower high that fails to exceed,
    then break of intervening low. Approximated: MFI peak1>80, peak2<peak1, then MFI breaks
    intervening trough within 63d."""
    m = _mfi(high, low, close, volume, 14)
    p = _pivot_high_event(m, k=3) > 0
    t = _pivot_low_event(m, k=3) > 0
    pk = m.where(p).ffill()
    pk_prev = pk.shift(1)
    tr = m.where(t).ffill()
    cond_two_peaks = (pk_prev > 80.0) & (pk < pk_prev) & (pk > 50.0)
    cond_break = m < tr
    ev = (cond_two_peaks & cond_break).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).max()


def f23_adld_232_mfi_14_vs_28_overbought_disagreement(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if MFI(14)>80 but MFI(28)<70 — short-horizon-only overbought reading."""
    m14 = _mfi(high, low, close, volume, 14)
    m28 = _mfi(high, low, close, volume, 28)
    return ((m14 > 80.0) & (m28 < 70.0)).astype(float).where(m14.notna() & m28.notna(), np.nan)


def f23_adld_233_mfi_14_vs_56_overbought_disagreement(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if MFI(14)>80 but MFI(56)<70 — long-horizon non-confirmation."""
    m14 = _mfi(high, low, close, volume, 14)
    m56 = _mfi(high, low, close, volume, 56)
    return ((m14 > 80.0) & (m56 < 70.0)).astype(float).where(m14.notna() & m56.notna(), np.nan)


def f23_adld_234_mfi_triple_screen_bearish(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Elder triple-screen bearish: weekly (5d-resample proxy via MFI(70)) declining,
    daily MFI(14) declining, today's tactical MFI(5) above 80 and falling."""
    m_w = _mfi(high, low, close, volume, 70)
    m_d = _mfi(high, low, close, volume, 14)
    m_t = _mfi(high, low, close, volume, 5)
    cond = (m_w.diff() < 0) & (m_d.diff() < 0) & (m_t > 80.0) & (m_t.diff() < 0)
    return cond.astype(float).where(m_w.notna() & m_d.notna() & m_t.notna(), np.nan)


def f23_adld_235_mfi_bearish_div_magnitude_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """At a 63d price-high, magnitude = (prior MFI max - current MFI). Else NaN, ffilled briefly."""
    m = _mfi(high, low, close, volume, 14)
    p_new = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    prior_max = m.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    amp = (prior_max - m).where(p_new & (m < prior_max), np.nan)
    return amp.ffill(limit=QDAYS)


def f23_adld_236_mfi_bearish_div_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish MFI(14) divergence at 252d horizon."""
    m = _mfi(high, low, close, volume, 14)
    p_new = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    m_below = m < m.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    return (p_new & m_below).astype(float)


def f23_adld_237_mfi_pct_rank_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of MFI(14) in trailing 252d distribution."""
    m = _mfi(high, low, close, volume, 14)
    return m.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f23_adld_238_mfi_descending_peaks_count_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of MFI(14) confirmed peaks in last 63d that are below their predecessor."""
    m = _mfi(high, low, close, volume, 14)
    p = _pivot_high_event(m, k=3) > 0
    pk = m.where(p).ffill()
    pk_prev = pk.shift(1)
    descending = ((pk < pk_prev) & p).astype(float)
    return descending.rolling(QDAYS, min_periods=MDAYS).sum()


def f23_adld_239_mfi_negative_money_flow_dominance_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Wilder negative money flow / (positive + negative money flow) over 63d — share of outflow."""
    pmf, nmf, _ = _mfi_components(high, low, close, volume, QDAYS)
    return _safe_div(nmf, pmf + nmf)


# ============================================================
# Bucket C — Klinger Volume Oscillator (240-244)
# ============================================================

def f23_adld_240_kvo_bearish_div_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish KVO divergence at 252d horizon: price new 252d high, KVO below prior max."""
    k = _kvo(high, low, close, volume, 34, 55)
    p_new = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    k_below = k < k.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    return (p_new & k_below).astype(float)


def f23_adld_241_kvo_histogram_descending_peaks_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of KVO-histogram (kvo-signal) confirmed peaks in 63d that decline vs prior."""
    k = _kvo(high, low, close, volume, 34, 55)
    h = k - _kvo_signal(k, 13)
    p = _pivot_high_event(h, k=3) > 0
    pk = h.where(p).ffill()
    pk_prev = pk.shift(1)
    desc = ((pk < pk_prev) & p).astype(float)
    return desc.rolling(QDAYS, min_periods=MDAYS).sum()


def f23_adld_242_kvo_zero_cross_at_high_event(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if KVO crosses zero from above within 5d of a fresh 252d price high."""
    k = _kvo(high, low, close, volume, 34, 55)
    zc = ((k < 0) & (k.shift(1) >= 0)).astype(float)
    p_new = (close >= close.rolling(YDAYS, min_periods=QDAYS).max()).astype(float)
    near_high = p_new.rolling(WDAYS, min_periods=2).max()
    return (zc * near_high).where(k.notna(), np.nan)


def f23_adld_243_kvo_signal_distance_zscore_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of (KVO - signal) vs 252d distribution — histogram stretch."""
    k = _kvo(high, low, close, volume, 34, 55)
    h = k - _kvo_signal(k, 13)
    return _rolling_zscore(h, YDAYS, min_periods=QDAYS)


def f23_adld_244_kvo_negative_dwell_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 252d where KVO < 0."""
    k = _kvo(high, low, close, volume, 34, 55)
    return (k < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().where(k.notna(), np.nan)


# ============================================================
# Bucket D — Twiggs Money Flow (245-250)
# ============================================================

def f23_adld_245_tmf_zero_cross_event_at_high(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """TMF crosses zero from above within 5d of fresh 252d price high."""
    tmf = _twiggs_mf(high, low, close, volume, 21)
    zc = ((tmf < 0) & (tmf.shift(1) >= 0)).astype(float)
    p_new = (close >= close.rolling(YDAYS, min_periods=QDAYS).max()).astype(float)
    near_high = p_new.rolling(WDAYS, min_periods=2).max()
    return (zc * near_high).where(tmf.notna(), np.nan)


def f23_adld_246_tmf_slope_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d rolling slope of Twiggs Money Flow — flow regime gradient."""
    return _rolling_slope(_twiggs_mf(high, low, close, volume, 21), QDAYS)


def f23_adld_247_tmf_dwell_below_zero_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63d where TMF < 0."""
    tmf = _twiggs_mf(high, low, close, volume, 21)
    return (tmf < 0).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(tmf.notna(), np.nan)


def f23_adld_248_tmf_negative_area_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Integral of negative TMF over 252d — outflow intensity."""
    tmf = _twiggs_mf(high, low, close, volume, 21)
    neg = (-tmf.clip(upper=0.0))
    return neg.rolling(YDAYS, min_periods=QDAYS).sum()


def f23_adld_249_tmf_bearish_div_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish TMF divergence at 252d horizon."""
    tmf = _twiggs_mf(high, low, close, volume, 21)
    p_new = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    t_below = tmf < tmf.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    return (p_new & t_below).astype(float)


def f23_adld_250_tmf_below_neg10_extreme_state(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: TMF < -0.10 (Twiggs 'strong distribution' threshold)."""
    tmf = _twiggs_mf(high, low, close, volume, 21)
    return (tmf < -0.10).astype(float).where(tmf.notna(), np.nan)


# ============================================================
# Bucket E — CMF deeper (251-255)
# ============================================================

def f23_adld_251_cmf_zero_cross_at_252d_high_event(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """CMF21 crosses zero from above within 5d of a fresh 252d price high."""
    c = _cmf(high, low, close, volume, MDAYS)
    zc = ((c < 0) & (c.shift(1) >= 0)).astype(float)
    p_new = (close >= close.rolling(YDAYS, min_periods=QDAYS).max()).astype(float)
    near_high = p_new.rolling(WDAYS, min_periods=2).max()
    return (zc * near_high).where(c.notna(), np.nan)


def f23_adld_252_cmf_below_neg10_dwell_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63d where CMF21 < -0.10."""
    c = _cmf(high, low, close, volume, MDAYS)
    return (c < -0.10).astype(float).rolling(QDAYS, min_periods=MDAYS).mean().where(c.notna(), np.nan)


def f23_adld_253_cmf_bearish_div_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish CMF21 divergence at 252d horizon."""
    c = _cmf(high, low, close, volume, MDAYS)
    p_new = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    c_below = c < c.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    return (p_new & c_below).astype(float)


def f23_adld_254_cmf_descending_peaks_count_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of CMF21 confirmed peaks in 63d below their predecessor."""
    c = _cmf(high, low, close, volume, MDAYS)
    p = _pivot_high_event(c, k=3) > 0
    pk = c.where(p).ffill()
    pk_prev = pk.shift(1)
    desc = ((pk < pk_prev) & p).astype(float)
    return desc.rolling(QDAYS, min_periods=MDAYS).sum()


def f23_adld_255_cmf_negative_area_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Integral of negative CMF21 over 252d — outflow intensity."""
    c = _cmf(high, low, close, volume, MDAYS)
    neg = (-c.clip(upper=0.0))
    return neg.rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket F — Force Index (Elder) extensions (256-262)
# ============================================================

def f23_adld_256_force_index_ema13_bearish_cross(close: pd.Series, volume: pd.Series) -> pd.Series:
    """FI EMA13 crosses below zero — Elder canonical bearish signal."""
    fi = _force_index(close, volume, 13)
    return ((fi < 0) & (fi.shift(1) >= 0)).astype(float).where(fi.notna(), np.nan)


def f23_adld_257_force_index_ema2_spike_bearish(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Elder tactical: 2-period FI < -2 sigma of its 63d distribution."""
    fi2 = _force_index(close, volume, 2)
    z = _rolling_zscore(fi2, QDAYS)
    return (z < -2.0).astype(float).where(z.notna(), np.nan)


def f23_adld_258_force_index_bearish_div_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish FI(13) divergence at 63d horizon."""
    fi = _force_index(close, volume, 13)
    p_new = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    f_below = fi < fi.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return (p_new & f_below).astype(float)


def f23_adld_259_force_index_bearish_div_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish FI(13) divergence at 252d horizon."""
    fi = _force_index(close, volume, 13)
    p_new = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    f_below = fi < fi.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    return (p_new & f_below).astype(float)


def f23_adld_260_force_index_pct_rank_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of FI(13) in trailing 252d distribution."""
    fi = _force_index(close, volume, 13)
    return fi.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f23_adld_261_force_index_extreme_neg_z3_event(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Indicator: FI(13) z-score (252d) < -3."""
    fi = _force_index(close, volume, 13)
    z = _rolling_zscore(fi, YDAYS, min_periods=QDAYS)
    return (z < -3.0).astype(float).where(z.notna(), np.nan)


def f23_adld_262_force_index_extreme_neg_count_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of FI(13) z < -2 events in last 63d."""
    fi = _force_index(close, volume, 13)
    z = _rolling_zscore(fi, YDAYS, min_periods=QDAYS)
    ev = (z < -2.0).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
# Bucket G — AD line breakdown / structure (263-272)
# ============================================================

def f23_adld_263_ad_line_breakdown_below_63d_low_event(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if AD line breaks below its 63d trailing min AND close still within 5% of 252d high
    (price-leadership-with-flow-failure event)."""
    ad = _ad_line(high, low, close, volume)
    ad_break = ad < ad.shift(1).rolling(QDAYS, min_periods=MDAYS).min()
    p_near_high = close >= 0.95 * close.rolling(YDAYS, min_periods=QDAYS).max()
    return (ad_break & p_near_high).astype(float)


def f23_adld_264_ad_line_breakdown_below_252d_low_event(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if AD line breaks below its 252d trailing min — structural distribution break."""
    ad = _ad_line(high, low, close, volume)
    return (ad < ad.shift(1).rolling(YDAYS, min_periods=QDAYS).min()).astype(float)


def f23_adld_265_ad_line_distance_below_sma50(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """AD line - SMA50(AD), normalized by AD's 252d std — canonical Chaikin horizon stretch."""
    ad = _ad_line(high, low, close, volume)
    sma = ad.rolling(50, min_periods=MDAYS).mean()
    sd = ad.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(ad - sma, sd)


def f23_adld_266_ad_line_acceleration_21(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second derivative of AD line over 21 bars (slope-of-slope)."""
    ad = _ad_line(high, low, close, volume)
    s1 = _rolling_slope(ad, MDAYS)
    return _rolling_slope(s1, MDAYS)


def f23_adld_267_ad_line_curvature_sign_change_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Number of curvature (2nd-difference) sign changes in AD line over last 63d — inflection density."""
    ad = _ad_line(high, low, close, volume)
    cur = ad.diff().diff()
    sign_change = ((cur * cur.shift(1)) < 0).astype(float)
    return sign_change.rolling(QDAYS, min_periods=MDAYS).sum()


def f23_adld_268_ad_line_bars_since_last_peak_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since AD line's 252d rolling maximum — staleness of accumulation peak."""
    ad = _ad_line(high, low, close, volume)
    at_max = ad == ad.rolling(YDAYS, min_periods=QDAYS).max()
    return _bars_since(at_max)


def f23_adld_269_ad_line_pct_rank_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of AD line value within trailing 252d distribution."""
    ad = _ad_line(high, low, close, volume)
    return ad.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f23_adld_270_ad_line_negative_slope_streak_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive-bars streak with AD line 63d-slope < 0."""
    ad = _ad_line(high, low, close, volume)
    sl = _rolling_slope(ad, QDAYS)
    neg = (sl < 0).astype(int).to_numpy()
    out = np.zeros(neg.size, dtype=float)
    c = 0
    for i in range(neg.size):
        c = c + 1 if neg[i] else 0
        out[i] = float(c)
    return pd.Series(out, index=ad.index).where(sl.notna(), np.nan)


def f23_adld_271_ad_line_bearish_div_at_confirmed_pivot(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """At confirmed price-pivot-high (Williams rule, k=5), 1 if AD line's pivot value < previous AD pivot."""
    ad = _ad_line(high, low, close, volume)
    p_pv = _pivot_high_event(close, k=5) > 0
    ad_pv = ad.where(_pivot_high_event(ad, k=5) > 0).ffill()
    prev = ad_pv.shift(1)
    return (p_pv & (ad_pv < prev)).astype(float)


def f23_adld_272_ad_line_drawdown_z_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of (running_max(AD) - AD) over 252d — drawdown stretch in std units."""
    ad = _ad_line(high, low, close, volume)
    rmax = ad.rolling(YDAYS, min_periods=QDAYS).max()
    dd = rmax - ad
    return _rolling_zscore(dd, YDAYS, min_periods=QDAYS)


# ============================================================
# Bucket H — Williams AD disagreement & VSA effort/result (273-278)
# ============================================================

def f23_adld_273_wad_minus_chaikin_ad_disagreement_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d correlation between WAD and Chaikin AD — divergent flow models."""
    wad = _williams_ad(high, low, close)
    cad = _ad_line(high, low, close, volume)
    return wad.rolling(QDAYS, min_periods=MDAYS).corr(cad)


def f23_adld_274_wad_descending_peaks_count_63(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of WAD confirmed peaks in last 63d that decline vs prior peak."""
    wad = _williams_ad(high, low, close)
    p = _pivot_high_event(wad, k=3) > 0
    pk = wad.where(p).ffill()
    pk_prev = pk.shift(1)
    desc = ((pk < pk_prev) & p).astype(float)
    return desc.rolling(QDAYS, min_periods=MDAYS).sum()


def f23_adld_275_wad_bullish_div_63_inverted(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Hidden bearish on WAD: price lower-high (63d), WAD higher-high (63d)."""
    wad = _williams_ad(high, low, close)
    p_prev_max = close.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    w_prev_max = wad.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    return ((close < p_prev_max) & (wad > w_prev_max)).astype(float)


def f23_adld_276_effort_vs_result_ad_per_pct_move_21(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Wyckoff effort/result: 21d sum(|CLV*V|) / 21d sum(|log return|) — units of flow per unit move."""
    eff = (_clv(high, low, close).abs() * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    res = _safe_log(close).diff().abs().rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(eff, res)


def f23_adld_277_effort_vs_result_ad_per_pct_move_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Wyckoff effort/result at 63d horizon."""
    eff = (_clv(high, low, close).abs() * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    res = _safe_log(close).diff().abs().rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(eff, res)


def f23_adld_278_high_effort_low_result_event(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 if volume z (252d) > 2 AND |today's return| < 0.5 * ATR21/close — high effort, low result."""
    vz = _rolling_zscore(volume, YDAYS, min_periods=QDAYS)
    rt = (close - close.shift(1)).abs()
    a = _atr(high, low, close, MDAYS)
    cond = (vz > 2.0) & (rt < 0.5 * a)
    return cond.astype(float).where(vz.notna() & a.notna(), np.nan)


# ============================================================
# Bucket I — Velocities (279-283)
# ============================================================

def f23_adld_279_chaikin_money_flow_velocity_21(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-bar change of CMF21 — flow regime acceleration."""
    return _cmf(high, low, close, volume, MDAYS).diff(MDAYS)


def f23_adld_280_mfi_velocity_21(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-bar change of MFI(14)."""
    return _mfi(high, low, close, volume, 14).diff(MDAYS)


def f23_adld_281_kvo_signal_velocity_21(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-bar change of KVO signal line."""
    k = _kvo(high, low, close, volume, 34, 55)
    return _kvo_signal(k, 13).diff(MDAYS)


def f23_adld_282_force_index_signal_line_bearish_cross(close: pd.Series, volume: pd.Series) -> pd.Series:
    """FI EMA13 crosses below EMA63 — signal line bearish cross."""
    s = _force_index(close, volume, 13)
    l = _force_index(close, volume, QDAYS)
    return ((s < l) & (s.shift(1) >= l.shift(1))).astype(float).where(s.notna() & l.notna(), np.nan)


def f23_adld_283_chaikin_osc_signal_line_bearish_cross(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Chaikin osc (3,10) crosses below its EMA(9) signal line."""
    co = _chaikin_osc(high, low, close, volume, 3, 10)
    sig = _ema(co, 9)
    return ((co < sig) & (co.shift(1) >= sig.shift(1))).astype(float).where(co.notna() & sig.notna(), np.nan)


# ============================================================
# Bucket J — Multi-indicator unanimity / rolling over (284-286)
# ============================================================

def f23_adld_284_unanimous_bearish_flow_state(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Strict AND across {CMF<0, MFI<50, KVO<0, TMF<0, FI<0, AD-slope63<0}."""
    cmf = _cmf(high, low, close, volume, MDAYS)
    mfi = _mfi(high, low, close, volume, 14)
    k = _kvo(high, low, close, volume, 34, 55)
    tmf = _twiggs_mf(high, low, close, volume, 21)
    fi = _force_index(close, volume, 13)
    ad = _ad_line(high, low, close, volume)
    sl = _rolling_slope(ad, QDAYS)
    cond = (cmf < 0) & (mfi < 50.0) & (k < 0) & (tmf < 0) & (fi < 0) & (sl < 0)
    valid = cmf.notna() & mfi.notna() & k.notna() & tmf.notna() & fi.notna() & sl.notna()
    return cond.astype(float).where(valid, np.nan)


def f23_adld_285_unanimous_bearish_flow_dwell_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63d in unanimous-bearish flow state."""
    cmf = _cmf(high, low, close, volume, MDAYS)
    mfi = _mfi(high, low, close, volume, 14)
    k = _kvo(high, low, close, volume, 34, 55)
    tmf = _twiggs_mf(high, low, close, volume, 21)
    fi = _force_index(close, volume, 13)
    ad = _ad_line(high, low, close, volume)
    sl = _rolling_slope(ad, QDAYS)
    cond = (cmf < 0) & (mfi < 50.0) & (k < 0) & (tmf < 0) & (fi < 0) & (sl < 0)
    return cond.astype(float).rolling(QDAYS, min_periods=MDAYS).mean()


def f23_adld_286_money_flow_indicators_rolling_over_count(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of {CMF, MFI, KVO, TMF, FI, AD-slope63} where 21d-max occurred >10 bars ago."""
    cmf = _cmf(high, low, close, volume, MDAYS)
    mfi = _mfi(high, low, close, volume, 14)
    k = _kvo(high, low, close, volume, 34, 55)
    tmf = _twiggs_mf(high, low, close, volume, 21)
    fi = _force_index(close, volume, 13)
    ad = _ad_line(high, low, close, volume)
    sl = _rolling_slope(ad, QDAYS)
    def _rolled_over(x):
        m = x.rolling(MDAYS, min_periods=WDAYS).max()
        at_max = (x == m)
        bs = _bars_since(at_max)
        return (bs > 10.0).astype(float).where(x.notna(), 0.0)
    parts = [_rolled_over(s).rename(f"i{i}") for i, s in enumerate([cmf, mfi, k, tmf, fi, sl])]
    df = pd.concat(parts, axis=1)
    return df.sum(axis=1)


# ============================================================
# Bucket K — MFI top reversal + AVWAP + raw MF ratios (287-291)
# ============================================================

def f23_adld_287_mfi_top_then_break_5d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """MFI(14) was > 80 in last 5d AND now < 70 — Wilder reversal trigger."""
    m = _mfi(high, low, close, volume, 14)
    was_ob = (m > 80.0).rolling(WDAYS, min_periods=2).max()
    now_below = (m < 70.0).astype(float)
    return ((was_ob > 0) & (now_below > 0)).astype(float).where(m.notna(), np.nan)


def f23_adld_288_anchored_vwap_52w_high_breakdown_event(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """First close below the AVWAP anchored to the rolling 252d high, within last 21d."""
    # anchor at bar where high == 252d max
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    anchor = (high >= rmax) & rmax.notna()
    avwap = _avwap_from(close, volume, anchor)
    cross = (close < avwap) & (close.shift(1) >= avwap.shift(1))
    return cross.astype(float).rolling(MDAYS, min_periods=2).max().where(avwap.notna(), np.nan)


def f23_adld_289_anchored_vwap_ath_distance_atr(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - AVWAP anchored at expanding ATH), normalized by ATR21."""
    ath = high.expanding(min_periods=QDAYS).max()
    anchor = (high >= ath) & ath.notna()
    avwap = _avwap_from(close, volume, anchor)
    a = _atr(high, low, close, MDAYS)
    return _safe_div(close - avwap, a)


def f23_adld_290_pos_mf_to_neg_mf_ratio_14d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Wilder raw PMF/NMF over 14 bars."""
    pmf, nmf, _ = _mfi_components(high, low, close, volume, 14)
    return _safe_div(pmf, nmf)


def f23_adld_291_pos_mf_to_neg_mf_ratio_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Wilder raw PMF/NMF over 63 bars."""
    pmf, nmf, _ = _mfi_components(high, low, close, volume, QDAYS)
    return _safe_div(pmf, nmf)


# ============================================================
# Bucket L — Distribution-day clustering (IBD) (292-294)
# ============================================================

def f23_adld_292_dist_day_clv_weighted_count_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """IBD distribution day (close down >=0.2% AND volume > prior day) weighted by -CLV; sum 63d."""
    rt = close.pct_change()
    dd_flag = (rt <= -0.002) & (volume > volume.shift(1))
    w = (-_clv(high, low, close)).clip(lower=0.0)
    weighted = w.where(dd_flag, 0.0)
    return weighted.rolling(QDAYS, min_periods=MDAYS).sum()


def f23_adld_293_dist_day_following_new_high_count_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of distribution days in 63d that occurred within 5d of a fresh 252d-high."""
    rt = close.pct_change()
    dd_flag = (rt <= -0.002) & (volume > volume.shift(1))
    p_new = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    near = p_new.astype(float).rolling(WDAYS, min_periods=2).max()
    ev = (dd_flag & (near > 0)).astype(float)
    return ev.rolling(QDAYS, min_periods=MDAYS).sum()


def f23_adld_294_ad_line_slope_z_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 63d AD slope vs 252d distribution."""
    ad = _ad_line(high, low, close, volume)
    sl = _rolling_slope(ad, QDAYS)
    return _rolling_zscore(sl, YDAYS, min_periods=QDAYS)


# ============================================================
# Bucket M — Amplitude / compression (295-296)
# ============================================================

def f23_adld_295_chaikin_osc_amplitude_decay_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(recent 21d peak-trough range of Chaikin osc) / (prior 21d range) — amplitude decay ratio."""
    co = _chaikin_osc(high, low, close, volume, 3, 10)
    r_now = co.rolling(MDAYS, min_periods=WDAYS).max() - co.rolling(MDAYS, min_periods=WDAYS).min()
    r_prior = r_now.shift(MDAYS)
    return _safe_div(r_now, r_prior)


def f23_adld_296_kvo_amplitude_compression_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(21d KVO range) / (63d KVO range) — compression of KVO swings."""
    k = _kvo(high, low, close, volume, 34, 55)
    r_s = k.rolling(MDAYS, min_periods=WDAYS).max() - k.rolling(MDAYS, min_periods=WDAYS).min()
    r_l = k.rolling(QDAYS, min_periods=MDAYS).max() - k.rolling(QDAYS, min_periods=MDAYS).min()
    return _safe_div(r_s, r_l)


# ============================================================
# Bucket N — Topping/climax composites (297-300)
# ============================================================

def f23_adld_297_mfi_overbought_streak_in_uptrend_63(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bars in last 63d where MFI(14)>80 AND close>200d MA."""
    m = _mfi(high, low, close, volume, 14)
    sma = close.rolling(200, min_periods=63).mean()
    cond = (m > 80.0) & (close > sma)
    return cond.astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f23_adld_298_force_index_long_term_climax_event(close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    """1 if raw FI > 99th percentile of trailing 252d AND price at 252d high (long-term climax)."""
    fi = (close.diff() * volume)
    pr = fi.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)
    p_new = close >= close.rolling(YDAYS, min_periods=QDAYS).max()
    return ((pr >= 0.99) & p_new).astype(float).where(pr.notna(), np.nan)


def f23_adld_299_pvi_at_high_with_neg_slope_event(close: pd.Series, volume: pd.Series, high: pd.Series) -> pd.Series:
    """1 if PVI prints fresh 252d high AND PVI 21d slope < 0 (early flow weakening at retail-dom)."""
    pvi = _pvi(close, volume)
    pvi_nh = pvi >= pvi.rolling(YDAYS, min_periods=QDAYS).max()
    sl = _rolling_slope(pvi, MDAYS)
    p_near = close >= 0.95 * close.rolling(YDAYS, min_periods=QDAYS).max()
    return (pvi_nh & (sl < 0) & p_near).astype(float).where(sl.notna(), np.nan)


def f23_adld_300_money_flow_topping_pattern_score_252(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite practitioner checklist (0-7 score) over trailing 252d:
       +1 each: CMF<0, MFI<50, KVO<0, TMF<0, FI(13)<0, AD-slope63<0, Chaikin-osc<0."""
    cmf = _cmf(high, low, close, volume, MDAYS)
    mfi = _mfi(high, low, close, volume, 14)
    k = _kvo(high, low, close, volume, 34, 55)
    tmf = _twiggs_mf(high, low, close, volume, 21)
    fi = _force_index(close, volume, 13)
    ad = _ad_line(high, low, close, volume)
    sl = _rolling_slope(ad, QDAYS)
    co = _chaikin_osc(high, low, close, volume, 3, 10)
    parts = [
        (cmf < 0).astype(float).rename("a"),
        (mfi < 50.0).astype(float).rename("b"),
        (k < 0).astype(float).rename("c"),
        (tmf < 0).astype(float).rename("d"),
        (fi < 0).astype(float).rename("e"),
        (sl < 0).astype(float).rename("f"),
        (co < 0).astype(float).rename("g"),
    ]
    df = pd.concat(parts, axis=1)
    return df.sum(axis=1)


# ============================================================
#                         REGISTRY 226-300
# ============================================================

_HLCV = ["high", "low", "close", "volume"]
_HLC = ["high", "low", "close"]
_CV = ["close", "volume"]
_HLV = ["high", "low", "volume"]
_CVH = ["close", "volume", "high"]

ACCUMULATION_DISTRIBUTION_LINE_BASE_REGISTRY_226_300 = {
    "f23_adld_226_chaikin_osc_3_10_histogram_diminishing_peaks_63": {"inputs": _HLCV, "func": f23_adld_226_chaikin_osc_3_10_histogram_diminishing_peaks_63},
    "f23_adld_227_chaikin_osc_zero_cross_count_63": {"inputs": _HLCV, "func": f23_adld_227_chaikin_osc_zero_cross_count_63},
    "f23_adld_228_chaikin_osc_bearish_div_252": {"inputs": _HLCV, "func": f23_adld_228_chaikin_osc_bearish_div_252},
    "f23_adld_229_chaikin_osc_negative_area_252": {"inputs": _HLCV, "func": f23_adld_229_chaikin_osc_negative_area_252},
    "f23_adld_230_chaikin_osc_lower_high_at_price_high": {"inputs": _HLCV, "func": f23_adld_230_chaikin_osc_lower_high_at_price_high},
    "f23_adld_231_mfi_failure_swing_top_63": {"inputs": _HLCV, "func": f23_adld_231_mfi_failure_swing_top_63},
    "f23_adld_232_mfi_14_vs_28_overbought_disagreement": {"inputs": _HLCV, "func": f23_adld_232_mfi_14_vs_28_overbought_disagreement},
    "f23_adld_233_mfi_14_vs_56_overbought_disagreement": {"inputs": _HLCV, "func": f23_adld_233_mfi_14_vs_56_overbought_disagreement},
    "f23_adld_234_mfi_triple_screen_bearish": {"inputs": _HLCV, "func": f23_adld_234_mfi_triple_screen_bearish},
    "f23_adld_235_mfi_bearish_div_magnitude_63": {"inputs": _HLCV, "func": f23_adld_235_mfi_bearish_div_magnitude_63},
    "f23_adld_236_mfi_bearish_div_252": {"inputs": _HLCV, "func": f23_adld_236_mfi_bearish_div_252},
    "f23_adld_237_mfi_pct_rank_252": {"inputs": _HLCV, "func": f23_adld_237_mfi_pct_rank_252},
    "f23_adld_238_mfi_descending_peaks_count_63": {"inputs": _HLCV, "func": f23_adld_238_mfi_descending_peaks_count_63},
    "f23_adld_239_mfi_negative_money_flow_dominance_63": {"inputs": _HLCV, "func": f23_adld_239_mfi_negative_money_flow_dominance_63},
    "f23_adld_240_kvo_bearish_div_252": {"inputs": _HLCV, "func": f23_adld_240_kvo_bearish_div_252},
    "f23_adld_241_kvo_histogram_descending_peaks_63": {"inputs": _HLCV, "func": f23_adld_241_kvo_histogram_descending_peaks_63},
    "f23_adld_242_kvo_zero_cross_at_high_event": {"inputs": _HLCV, "func": f23_adld_242_kvo_zero_cross_at_high_event},
    "f23_adld_243_kvo_signal_distance_zscore_252": {"inputs": _HLCV, "func": f23_adld_243_kvo_signal_distance_zscore_252},
    "f23_adld_244_kvo_negative_dwell_252": {"inputs": _HLCV, "func": f23_adld_244_kvo_negative_dwell_252},
    "f23_adld_245_tmf_zero_cross_event_at_high": {"inputs": _HLCV, "func": f23_adld_245_tmf_zero_cross_event_at_high},
    "f23_adld_246_tmf_slope_63": {"inputs": _HLCV, "func": f23_adld_246_tmf_slope_63},
    "f23_adld_247_tmf_dwell_below_zero_63": {"inputs": _HLCV, "func": f23_adld_247_tmf_dwell_below_zero_63},
    "f23_adld_248_tmf_negative_area_252": {"inputs": _HLCV, "func": f23_adld_248_tmf_negative_area_252},
    "f23_adld_249_tmf_bearish_div_252": {"inputs": _HLCV, "func": f23_adld_249_tmf_bearish_div_252},
    "f23_adld_250_tmf_below_neg10_extreme_state": {"inputs": _HLCV, "func": f23_adld_250_tmf_below_neg10_extreme_state},
    "f23_adld_251_cmf_zero_cross_at_252d_high_event": {"inputs": _HLCV, "func": f23_adld_251_cmf_zero_cross_at_252d_high_event},
    "f23_adld_252_cmf_below_neg10_dwell_63": {"inputs": _HLCV, "func": f23_adld_252_cmf_below_neg10_dwell_63},
    "f23_adld_253_cmf_bearish_div_252": {"inputs": _HLCV, "func": f23_adld_253_cmf_bearish_div_252},
    "f23_adld_254_cmf_descending_peaks_count_63": {"inputs": _HLCV, "func": f23_adld_254_cmf_descending_peaks_count_63},
    "f23_adld_255_cmf_negative_area_252": {"inputs": _HLCV, "func": f23_adld_255_cmf_negative_area_252},
    "f23_adld_256_force_index_ema13_bearish_cross": {"inputs": _CV, "func": f23_adld_256_force_index_ema13_bearish_cross},
    "f23_adld_257_force_index_ema2_spike_bearish": {"inputs": _CV, "func": f23_adld_257_force_index_ema2_spike_bearish},
    "f23_adld_258_force_index_bearish_div_63": {"inputs": _CV, "func": f23_adld_258_force_index_bearish_div_63},
    "f23_adld_259_force_index_bearish_div_252": {"inputs": _CV, "func": f23_adld_259_force_index_bearish_div_252},
    "f23_adld_260_force_index_pct_rank_252": {"inputs": _CV, "func": f23_adld_260_force_index_pct_rank_252},
    "f23_adld_261_force_index_extreme_neg_z3_event": {"inputs": _CV, "func": f23_adld_261_force_index_extreme_neg_z3_event},
    "f23_adld_262_force_index_extreme_neg_count_63": {"inputs": _CV, "func": f23_adld_262_force_index_extreme_neg_count_63},
    "f23_adld_263_ad_line_breakdown_below_63d_low_event": {"inputs": _HLCV, "func": f23_adld_263_ad_line_breakdown_below_63d_low_event},
    "f23_adld_264_ad_line_breakdown_below_252d_low_event": {"inputs": _HLCV, "func": f23_adld_264_ad_line_breakdown_below_252d_low_event},
    "f23_adld_265_ad_line_distance_below_sma50": {"inputs": _HLCV, "func": f23_adld_265_ad_line_distance_below_sma50},
    "f23_adld_266_ad_line_acceleration_21": {"inputs": _HLCV, "func": f23_adld_266_ad_line_acceleration_21},
    "f23_adld_267_ad_line_curvature_sign_change_63": {"inputs": _HLCV, "func": f23_adld_267_ad_line_curvature_sign_change_63},
    "f23_adld_268_ad_line_bars_since_last_peak_252": {"inputs": _HLCV, "func": f23_adld_268_ad_line_bars_since_last_peak_252},
    "f23_adld_269_ad_line_pct_rank_252": {"inputs": _HLCV, "func": f23_adld_269_ad_line_pct_rank_252},
    "f23_adld_270_ad_line_negative_slope_streak_63": {"inputs": _HLCV, "func": f23_adld_270_ad_line_negative_slope_streak_63},
    "f23_adld_271_ad_line_bearish_div_at_confirmed_pivot": {"inputs": _HLCV, "func": f23_adld_271_ad_line_bearish_div_at_confirmed_pivot},
    "f23_adld_272_ad_line_drawdown_z_252": {"inputs": _HLCV, "func": f23_adld_272_ad_line_drawdown_z_252},
    "f23_adld_273_wad_minus_chaikin_ad_disagreement_63": {"inputs": _HLCV, "func": f23_adld_273_wad_minus_chaikin_ad_disagreement_63},
    "f23_adld_274_wad_descending_peaks_count_63": {"inputs": _HLC, "func": f23_adld_274_wad_descending_peaks_count_63},
    "f23_adld_275_wad_bullish_div_63_inverted": {"inputs": _HLC, "func": f23_adld_275_wad_bullish_div_63_inverted},
    "f23_adld_276_effort_vs_result_ad_per_pct_move_21": {"inputs": _HLCV, "func": f23_adld_276_effort_vs_result_ad_per_pct_move_21},
    "f23_adld_277_effort_vs_result_ad_per_pct_move_63": {"inputs": _HLCV, "func": f23_adld_277_effort_vs_result_ad_per_pct_move_63},
    "f23_adld_278_high_effort_low_result_event": {"inputs": _HLCV, "func": f23_adld_278_high_effort_low_result_event},
    "f23_adld_279_chaikin_money_flow_velocity_21": {"inputs": _HLCV, "func": f23_adld_279_chaikin_money_flow_velocity_21},
    "f23_adld_280_mfi_velocity_21": {"inputs": _HLCV, "func": f23_adld_280_mfi_velocity_21},
    "f23_adld_281_kvo_signal_velocity_21": {"inputs": _HLCV, "func": f23_adld_281_kvo_signal_velocity_21},
    "f23_adld_282_force_index_signal_line_bearish_cross": {"inputs": _CV, "func": f23_adld_282_force_index_signal_line_bearish_cross},
    "f23_adld_283_chaikin_osc_signal_line_bearish_cross": {"inputs": _HLCV, "func": f23_adld_283_chaikin_osc_signal_line_bearish_cross},
    "f23_adld_284_unanimous_bearish_flow_state": {"inputs": _HLCV, "func": f23_adld_284_unanimous_bearish_flow_state},
    "f23_adld_285_unanimous_bearish_flow_dwell_63": {"inputs": _HLCV, "func": f23_adld_285_unanimous_bearish_flow_dwell_63},
    "f23_adld_286_money_flow_indicators_rolling_over_count": {"inputs": _HLCV, "func": f23_adld_286_money_flow_indicators_rolling_over_count},
    "f23_adld_287_mfi_top_then_break_5d": {"inputs": _HLCV, "func": f23_adld_287_mfi_top_then_break_5d},
    "f23_adld_288_anchored_vwap_52w_high_breakdown_event": {"inputs": _HLCV, "func": f23_adld_288_anchored_vwap_52w_high_breakdown_event},
    "f23_adld_289_anchored_vwap_ath_distance_atr": {"inputs": _HLCV, "func": f23_adld_289_anchored_vwap_ath_distance_atr},
    "f23_adld_290_pos_mf_to_neg_mf_ratio_14d": {"inputs": _HLCV, "func": f23_adld_290_pos_mf_to_neg_mf_ratio_14d},
    "f23_adld_291_pos_mf_to_neg_mf_ratio_63d": {"inputs": _HLCV, "func": f23_adld_291_pos_mf_to_neg_mf_ratio_63d},
    "f23_adld_292_dist_day_clv_weighted_count_63": {"inputs": _HLCV, "func": f23_adld_292_dist_day_clv_weighted_count_63},
    "f23_adld_293_dist_day_following_new_high_count_63": {"inputs": _HLCV, "func": f23_adld_293_dist_day_following_new_high_count_63},
    "f23_adld_294_ad_line_slope_z_252": {"inputs": _HLCV, "func": f23_adld_294_ad_line_slope_z_252},
    "f23_adld_295_chaikin_osc_amplitude_decay_63": {"inputs": _HLCV, "func": f23_adld_295_chaikin_osc_amplitude_decay_63},
    "f23_adld_296_kvo_amplitude_compression_63": {"inputs": _HLCV, "func": f23_adld_296_kvo_amplitude_compression_63},
    "f23_adld_297_mfi_overbought_streak_in_uptrend_63": {"inputs": _HLCV, "func": f23_adld_297_mfi_overbought_streak_in_uptrend_63},
    "f23_adld_298_force_index_long_term_climax_event": {"inputs": _CVH, "func": f23_adld_298_force_index_long_term_climax_event},
    "f23_adld_299_pvi_at_high_with_neg_slope_event": {"inputs": _CVH, "func": f23_adld_299_pvi_at_high_with_neg_slope_event},
    "f23_adld_300_money_flow_topping_pattern_score_252": {"inputs": _HLCV, "func": f23_adld_300_money_flow_topping_pattern_score_252},
}
