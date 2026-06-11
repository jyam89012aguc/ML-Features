"""spectral_cycle_analysis d2 features 151-225 — Pipeline 1b-technical.

75 distinct gap-filling hypotheses extending the 150 in 001-150. Themes:
Ehlers MAMA/FAMA / Sine-Wave / Cyber-Cycle / Burg-AR / Yule-Walker / Welch PSD /
Wavelet decomposition / EMD / Goertzel / Roofing filter / Decycler / coherence.

Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(N). Self-contained helpers — no cross-family imports.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504


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


def _rolling_pct_rank(s, window, min_periods=None):
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


# ---------------- Ehlers-style helpers (recursive, PIT-clean) ----------------

def _hilbert_quad_inphase(price, period=21):
    """Approximate Hilbert in-phase (I) and quadrature (Q) at each bar using
    Ehlers's 7-bar detrender + 4-bar lead. Recursive, PIT-clean.
    Returns (I, Q) both as numpy arrays of len(price)."""
    arr = price.values
    n = arr.size
    I = np.full(n, np.nan)
    Q = np.full(n, np.nan)
    # Ehlers detrender: 0.0962*p[0] + 0.5769*p[2] - 0.5769*p[4] - 0.0962*p[6]
    smp = arr.copy()
    for i in range(n):
        if i < 6 or np.isnan(arr[i]) or np.isnan(arr[i-2]) or np.isnan(arr[i-4]) or np.isnan(arr[i-6]):
            continue
        det = (0.0962 * arr[i] + 0.5769 * arr[i-2] - 0.5769 * arr[i-4] - 0.0962 * arr[i-6]) * (0.075 * period + 0.54)
        # Q1 = (0.0962*det[0] + 0.5769*det[2] - 0.5769*det[4] - 0.0962*det[6]) * (0.075*period+0.54)
        # Simplification: use the detrender output AS the quadrature, and lagged price as in-phase
        Q[i] = det
        I[i] = arr[i - 3] if i >= 3 and not np.isnan(arr[i-3]) else np.nan
    return I, Q


def _hilbert_phase_series(price, period=21):
    """Per-bar Hilbert phase via Ehlers quadrature. Returns pd.Series of phases."""
    I, Q = _hilbert_quad_inphase(price, period=period)
    ph = np.arctan2(Q, np.where(np.abs(I) > 1e-12, I, np.nan))
    return pd.Series(ph, index=price.index)


def _ehlers_mama_fama(price, fast=0.5, slow=0.05):
    """MAMA (Mother of Adaptive MA) + FAMA. Returns (mama, fama) as pd.Series.
    alpha modulated by |delta_phase|: faster when cycle phase changing quickly."""
    arr = price.values
    n = arr.size
    phase = _hilbert_phase_series(price, period=21).values
    mama = np.full(n, np.nan)
    fama = np.full(n, np.nan)
    prev_phase = np.nan
    for i in range(n):
        if np.isnan(arr[i]):
            continue
        if i == 0 or np.isnan(mama[i-1]):
            mama[i] = arr[i]; fama[i] = arr[i]; prev_phase = phase[i] if not np.isnan(phase[i]) else 0.0
            continue
        cur_ph = phase[i] if not np.isnan(phase[i]) else prev_phase
        dp = abs(cur_ph - prev_phase)
        if dp < 1.0:
            dp = 1.0
        alpha = fast / dp
        if alpha < slow:
            alpha = slow
        if alpha > fast:
            alpha = fast
        mama[i] = alpha * arr[i] + (1 - alpha) * mama[i-1]
        fama[i] = 0.5 * alpha * mama[i] + (1 - 0.5 * alpha) * fama[i-1]
        prev_phase = cur_ph
    return pd.Series(mama, index=price.index), pd.Series(fama, index=price.index)


def _ehlers_cyber_cycle(price, alpha=0.07):
    """Ehlers Cyber Cycle Indicator. 4-pole high-pass + simple cycle calc.
    Returns the Cycle output as pd.Series."""
    arr = price.values
    n = arr.size
    # smooth with 4-bar weighted MA
    smooth = np.full(n, np.nan)
    for i in range(n):
        if i < 3 or any(np.isnan(arr[i-k]) for k in (0, 1, 2, 3)):
            continue
        smooth[i] = (arr[i] + 2 * arr[i-1] + 2 * arr[i-2] + arr[i-3]) / 6.0
    cycle = np.full(n, np.nan)
    for i in range(n):
        if i < 6 or np.isnan(smooth[i]) or np.isnan(smooth[i-2]):
            continue
        if i < 7 or np.isnan(cycle[i-1]) or np.isnan(cycle[i-2]):
            # Initialization formula (Ehlers)
            cycle[i] = (arr[i] - 2 * arr[i-1] + arr[i-2]) / 4.0 if (i >= 2 and not np.isnan(arr[i-2])) else np.nan
            continue
        cycle[i] = ((1 - 0.5 * alpha) ** 2) * (smooth[i] - 2 * smooth[i-1] + smooth[i-2])             + 2 * (1 - alpha) * cycle[i-1] - ((1 - alpha) ** 2) * cycle[i-2]
    return pd.Series(cycle, index=price.index)


def _ehlers_cog(price, n=10):
    """Ehlers Center of Gravity Oscillator over n bars."""
    arr = price.values
    out = np.full(arr.size, np.nan)
    for i in range(arr.size):
        if i < n - 1:
            continue
        w = arr[i - n + 1:i + 1]
        if np.isnan(w).any():
            continue
        num = float(((np.arange(1, n + 1)) * w[::-1]).sum())
        den = float(w.sum())
        if den == 0:
            continue
        out[i] = -num / den + (n + 1) / 2.0
    return pd.Series(out, index=price.index)


def _supersmoother(arr, period):
    """2-pole SuperSmoother filter (recursive, PIT-clean)."""
    a1 = np.exp(-np.sqrt(2.0) * np.pi / period)
    b1 = 2.0 * a1 * np.cos(np.sqrt(2.0) * np.pi / period)
    c2 = b1; c3 = -a1 * a1; c1 = 1.0 - c2 - c3
    n = arr.size
    out = np.full(n, np.nan)
    for i in range(n):
        if np.isnan(arr[i]):
            continue
        if i < 2:
            out[i] = arr[i]; continue
        p1 = out[i-1] if not np.isnan(out[i-1]) else arr[i-1]
        p2 = out[i-2] if not np.isnan(out[i-2]) else arr[i-2]
        out[i] = c1 * (arr[i] + (arr[i-1] if not np.isnan(arr[i-1]) else arr[i])) / 2.0 + c2 * p1 + c3 * p2
    return out


def _highpass_2pole(arr, period):
    """Ehlers 2-pole HighPass filter (recursive)."""
    alpha = (np.cos(0.707 * 2.0 * np.pi / period) + np.sin(0.707 * 2.0 * np.pi / period) - 1.0) / np.cos(0.707 * 2.0 * np.pi / period)
    n = arr.size
    out = np.full(n, np.nan)
    for i in range(n):
        if np.isnan(arr[i]):
            continue
        if i < 2:
            out[i] = 0.0; continue
        p1 = out[i-1] if not np.isnan(out[i-1]) else 0.0
        p2 = out[i-2] if not np.isnan(out[i-2]) else 0.0
        out[i] = ((1 - alpha / 2.0) ** 2) * (arr[i] - 2 * arr[i-1] + arr[i-2])             + 2 * (1 - alpha) * p1 - ((1 - alpha) ** 2) * p2
    return out


def _decycler(price, period):
    """Ehlers Decycler = price - HighPass(period)."""
    return price - pd.Series(_highpass_2pole(price.values, period), index=price.index)


def _burg_ar_first_coef(w, order=2):
    """Burg algorithm: AR(order) first coefficient on a window. NaN-safe."""
    valid = ~np.isnan(w)
    if valid.sum() < order + 5:
        return np.nan
    v = (w[valid] if not valid.all() else w).astype(float)
    v = v - v.mean()
    n = v.size
    if n < order + 2:
        return np.nan
    ef = v.copy()
    eb = v.copy()
    a = np.array([1.0])
    for k in range(1, order + 1):
        ef_t = ef[1:]
        eb_t = eb[:-1]
        if ef_t.size == 0:
            return np.nan
        num = -2.0 * float(np.sum(ef_t * eb_t))
        den = float(np.sum(ef_t ** 2) + np.sum(eb_t ** 2))
        if den == 0:
            return np.nan
        kk = num / den
        new_ef = ef_t + kk * eb_t
        new_eb = eb_t + kk * ef_t
        ef = new_ef
        eb = new_eb
        a_new = np.zeros(k + 1)
        a_new[0] = 1.0
        for j in range(1, k):
            a_new[j] = a[j] + kk * a[k - j]
        a_new[k] = kk
        a = a_new
    return float(a[1])


def _yule_walker_ar1(w):
    """Yule-Walker AR(1) coefficient (equivalent to lag-1 autocorrelation)."""
    valid = ~np.isnan(w)
    if valid.sum() < 6:
        return np.nan
    v = w[valid] if not valid.all() else w
    if v.size < 3:
        return np.nan
    m = v.mean()
    vc = v - m
    den = float((vc * vc).sum())
    if den == 0:
        return np.nan
    return float((vc[1:] * vc[:-1]).sum() / den)


def _goertzel_power(w, period):
    """Goertzel single-frequency power estimate at given period."""
    valid = ~np.isnan(w)
    if valid.sum() < period * 2:
        return np.nan
    v = w[valid] if not valid.all() else w
    v = v - v.mean()
    n = v.size
    if period <= 1 or period >= n:
        return np.nan
    k = float(n) / float(period)
    w_omega = 2.0 * np.pi * k / float(n)
    coeff = 2.0 * np.cos(w_omega)
    s_prev = 0.0; s_prev2 = 0.0
    for x in v:
        s = float(x) + coeff * s_prev - s_prev2
        s_prev2 = s_prev
        s_prev = s
    return float(s_prev ** 2 + s_prev2 ** 2 - coeff * s_prev * s_prev2)


def _welch_psd(w, period, seg_len_div=4):
    """Welch's averaged periodogram for power at given period."""
    valid = ~np.isnan(w)
    if valid.sum() < period * 4:
        return np.nan
    v = w[valid] if not valid.all() else w
    v = v - v.mean()
    n = v.size
    seg_len = max(int(n / seg_len_div), period * 2)
    if seg_len >= n:
        seg_len = n
    overlap = seg_len // 2
    if overlap < 1:
        overlap = 1
    energies = []
    start = 0
    while start + seg_len <= n:
        seg = v[start:start + seg_len]
        # Hann window
        wnd = 0.5 - 0.5 * np.cos(2.0 * np.pi * np.arange(seg.size) / max(seg.size - 1, 1))
        seg_w = seg * wnd
        k = float(seg_len) / float(period)
        omega = 2.0 * np.pi * k / float(seg_len)
        t = np.arange(seg_len)
        re = float((seg_w * np.cos(omega * t)).sum())
        im = float((seg_w * np.sin(omega * t)).sum())
        energies.append((re * re + im * im) / float(seg_len))
        start += (seg_len - overlap)
    if not energies:
        return np.nan
    return float(np.mean(energies))


def _haar_detail_energy(w, scale):
    """Haar wavelet detail-coefficient energy at scale (in bars)."""
    valid = ~np.isnan(w)
    if valid.sum() < scale * 4:
        return np.nan
    v = w[valid] if not valid.all() else w
    n = v.size
    # detail = (v[t] - v[t-scale]) / sqrt(2*scale) — boxcar-difference proxy
    d = []
    for t in range(scale, n):
        d.append((float(v[t]) - float(v[t - scale])) / np.sqrt(2.0 * scale))
    if not d:
        return np.nan
    return float(np.sum(np.array(d) ** 2))


def f44_spca_151_mama_minus_close_logclose_d2(close: pd.Series) -> pd.Series:
    mama, fama = _ehlers_mama_fama(_safe_log(close))
    out = mama - _safe_log(close)
    return out.diff().diff()


def f44_spca_152_fama_minus_close_logclose_d2(close: pd.Series) -> pd.Series:
    mama, fama = _ehlers_mama_fama(_safe_log(close))
    out = fama - _safe_log(close)
    return out.diff().diff()


def f44_spca_153_mama_minus_fama_logclose_d2(close: pd.Series) -> pd.Series:
    mama, fama = _ehlers_mama_fama(_safe_log(close))
    out = mama - fama
    return out.diff().diff()


def f44_spca_154_mama_fama_crossover_sign_d2(close: pd.Series) -> pd.Series:
    mama, fama = _ehlers_mama_fama(_safe_log(close))
    out = np.sign(mama - fama)
    return out.diff().diff()


def f44_spca_155_mama_fama_crossover_flip_event_d2(close: pd.Series) -> pd.Series:
    mama, fama = _ehlers_mama_fama(_safe_log(close))
    sg = np.sign(mama - fama)
    out = (sg != sg.shift(1)).astype(float).where(sg.notna() & sg.shift(1).notna(), np.nan)
    return out.diff().diff()


def f44_spca_156_mama_slope_5d_d2(close: pd.Series) -> pd.Series:
    mama, fama = _ehlers_mama_fama(_safe_log(close))
    out = mama - mama.shift(5)
    return out.diff().diff()


def f44_spca_157_mama_fama_spread_zscore_252d_d2(close: pd.Series) -> pd.Series:
    mama, fama = _ehlers_mama_fama(_safe_log(close))
    out = _rolling_zscore(mama - fama, 252, min_periods=84)
    return out.diff().diff()


def f44_spca_158_current_mama_above_fama_streak_d2(close: pd.Series) -> pd.Series:
    mama, fama = _ehlers_mama_fama(_safe_log(close))
    ab = (mama > fama).astype(int).where(mama.notna() & fama.notna(), 0)
    block = (ab != ab.shift(1)).fillna(False).cumsum()
    st = ab.groupby(block).cumcount().astype(float)
    out = (st * (ab > 0)).where(mama.notna() & fama.notna(), np.nan)
    return out.diff().diff()


def f44_spca_159_mama_fama_spread_atr_norm_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    mama, fama = _ehlers_mama_fama(_safe_log(close))
    atr = _atr(high, low, close, n=21)
    out = _safe_div((mama - fama) * close, atr)
    return out.diff().diff()


def f44_spca_160_mama_fama_max_abs_spread_63d_d2(close: pd.Series) -> pd.Series:
    mama, fama = _ehlers_mama_fama(_safe_log(close))
    out = (mama - fama).abs().rolling(63, min_periods=21).max()
    return out.diff().diff()


def f44_spca_161_mama_fama_flip_count_252d_d2(close: pd.Series) -> pd.Series:
    mama, fama = _ehlers_mama_fama(_safe_log(close))
    sg = np.sign(mama - fama)
    fl = (sg != sg.shift(1)).astype(float).where(sg.notna() & sg.shift(1).notna(), np.nan)
    out = fl.rolling(252, min_periods=84).sum()
    return out.diff().diff()


def f44_spca_162_mama_acceleration_5d_d2(close: pd.Series) -> pd.Series:
    mama, fama = _ehlers_mama_fama(_safe_log(close))
    out = mama - 2.0 * mama.shift(5) + mama.shift(10)
    return out.diff().diff()


def f44_spca_163_mama_phase_delta_inv_proxy_d2(close: pd.Series) -> pd.Series:
    ph = _hilbert_phase_series(_safe_log(close), period=21)
    dp = (ph - ph.shift(1)).abs()
    out = 1.0 / dp.replace(0, np.nan)
    return out.diff().diff()


def f44_spca_164_mama_at_top_252d_range_indicator_d2(close: pd.Series) -> pd.Series:
    mama, fama = _ehlers_mama_fama(_safe_log(close))
    rmax = mama.rolling(252, min_periods=84).max()
    out = (mama >= 0.99 * rmax).astype(float).where(rmax.notna(), np.nan)
    return out.diff().diff()


def f44_spca_165_fama_slope_neg_flip_event_d2(close: pd.Series) -> pd.Series:
    mama, fama = _ehlers_mama_fama(_safe_log(close))
    sl = fama.diff()
    sg = np.sign(sl)
    flip = ((sg.shift(1) > 0) & (sg < 0)).astype(float).where(sg.notna() & sg.shift(1).notna(), np.nan)
    out = flip
    return out.diff().diff()


def f44_spca_166_ehlers_sinewave_per_bar_d2(close: pd.Series) -> pd.Series:
    ph = _hilbert_phase_series(_safe_log(close), period=21)
    out = np.sin(ph)
    return out.diff().diff()


def f44_spca_167_ehlers_leadwave_per_bar_d2(close: pd.Series) -> pd.Series:
    ph = _hilbert_phase_series(_safe_log(close), period=21)
    out = np.sin(ph + np.pi / 4.0)
    return out.diff().diff()


def f44_spca_168_ehlers_sine_minus_lead_sign_d2(close: pd.Series) -> pd.Series:
    ph = _hilbert_phase_series(_safe_log(close), period=21)
    out = np.sign(np.sin(ph) - np.sin(ph + np.pi / 4.0))
    return out.diff().diff()


def f44_spca_169_ehlers_sine_lead_flip_event_d2(close: pd.Series) -> pd.Series:
    ph = _hilbert_phase_series(_safe_log(close), period=21)
    sg = np.sign(np.sin(ph) - np.sin(ph + np.pi / 4.0))
    out = (sg != sg.shift(1)).astype(float).where(sg.notna() & sg.shift(1).notna(), np.nan)
    return out.diff().diff()


def f44_spca_170_ehlers_cyber_cycle_d2(close: pd.Series) -> pd.Series:
    out = _ehlers_cyber_cycle(_safe_log(close))
    return out.diff().diff()


def f44_spca_171_ehlers_cyber_cycle_zscore_252d_d2(close: pd.Series) -> pd.Series:
    cc = _ehlers_cyber_cycle(_safe_log(close))
    out = _rolling_zscore(cc, 252, min_periods=84)
    return out.diff().diff()


def f44_spca_172_ehlers_cyber_cycle_sign_flip_d2(close: pd.Series) -> pd.Series:
    cc = _ehlers_cyber_cycle(_safe_log(close))
    sg = np.sign(cc)
    out = (sg != sg.shift(1)).astype(float).where(sg.notna() & sg.shift(1).notna(), np.nan)
    return out.diff().diff()


def f44_spca_173_ehlers_cyber_cycle_local_max_indicator_d2(close: pd.Series) -> pd.Series:
    cc = _ehlers_cyber_cycle(_safe_log(close))
    is_max = ((cc.shift(1) > cc) & (cc.shift(1) > cc.shift(2))).astype(float).where(cc.notna() & cc.shift(2).notna(), np.nan)
    out = is_max
    return out.diff().diff()


def f44_spca_174_ehlers_cog_10bar_d2(close: pd.Series) -> pd.Series:
    out = _ehlers_cog(_safe_log(close), n=10)
    return out.diff().diff()


def f44_spca_175_ehlers_cog_21bar_d2(close: pd.Series) -> pd.Series:
    out = _ehlers_cog(_safe_log(close), n=21)
    return out.diff().diff()


def f44_spca_176_ehlers_cog_trigger_10bar_d2(close: pd.Series) -> pd.Series:
    cog = _ehlers_cog(_safe_log(close), n=10)
    out = cog - cog.shift(1)
    return out.diff().diff()


def f44_spca_177_ehlers_cog_above_zero_indicator_10bar_d2(close: pd.Series) -> pd.Series:
    cog = _ehlers_cog(_safe_log(close), n=10)
    out = (cog > 0).astype(float).where(cog.notna(), np.nan)
    return out.diff().diff()


def f44_spca_178_ehlers_decycler_60d_d2(close: pd.Series) -> pd.Series:
    out = _decycler(_safe_log(close), 60)
    return out.diff().diff()


def f44_spca_179_ehlers_decycler_oscillator_21_60_d2(close: pd.Series) -> pd.Series:
    out = _decycler(_safe_log(close), 21) - _decycler(_safe_log(close), 60)
    return out.diff().diff()


def f44_spca_180_ehlers_decycler_60d_sign_flip_d2(close: pd.Series) -> pd.Series:
    d = _decycler(_safe_log(close), 60)
    sg = np.sign(d)
    out = (sg != sg.shift(1)).astype(float).where(sg.notna() & sg.shift(1).notna(), np.nan)
    return out.diff().diff()


def f44_spca_181_burg_ar2_coef1_logret_252d_d2(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(lambda w: _burg_ar_first_coef(w, order=2), raw=True)
    return out.diff().diff()


def f44_spca_182_burg_ar4_coef1_logret_252d_d2(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(lambda w: _burg_ar_first_coef(w, order=4), raw=True)
    return out.diff().diff()


def f44_spca_183_burg_ar2_coef1_logclose_252d_d2(close: pd.Series) -> pd.Series:
    out = _safe_log(close).rolling(252, min_periods=84).apply(lambda w: _burg_ar_first_coef(w, order=2), raw=True)
    return out.diff().diff()


def f44_spca_184_yw_ar1_logret_63d_d2(close: pd.Series) -> pd.Series:
    out = _safe_log(close).diff().rolling(63, min_periods=21).apply(_yule_walker_ar1, raw=True)
    return out.diff().diff()


def f44_spca_185_yw_ar1_logret_504d_d2(close: pd.Series) -> pd.Series:
    out = _safe_log(close).diff().rolling(504, min_periods=168).apply(_yule_walker_ar1, raw=True)
    return out.diff().diff()


def f44_spca_186_abs_burg_ar2_coef1_252d_d2(close: pd.Series) -> pd.Series:
    out = _safe_log(close).diff().rolling(252, min_periods=84).apply(lambda w: _burg_ar_first_coef(w, order=2), raw=True).abs()
    return out.diff().diff()


def f44_spca_187_burg_ar2_sign_flip_event_252d_d2(close: pd.Series) -> pd.Series:
    c = _safe_log(close).diff().rolling(252, min_periods=84).apply(lambda w: _burg_ar_first_coef(w, order=2), raw=True)
    sg = np.sign(c)
    out = (sg != sg.shift(21)).astype(float).where(sg.notna() & sg.shift(21).notna(), np.nan)
    return out.diff().diff()


def f44_spca_188_burg_ar2_zscore_252d_in_504d_d2(close: pd.Series) -> pd.Series:
    c = _safe_log(close).diff().rolling(252, min_periods=84).apply(lambda w: _burg_ar_first_coef(w, order=2), raw=True)
    out = _rolling_zscore(c, 504, min_periods=168)
    return out.diff().diff()


def f44_spca_189_yw_ar1_63d_minus_504d_d2(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(63, min_periods=21).apply(_yule_walker_ar1, raw=True) - r.rolling(504, min_periods=168).apply(_yule_walker_ar1, raw=True)
    return out.diff().diff()


def f44_spca_190_yw_ar1_abs_logret_252d_d2(close: pd.Series) -> pd.Series:
    ar = _safe_log(close).diff().abs()
    out = ar.rolling(252, min_periods=84).apply(_yule_walker_ar1, raw=True)
    return out.diff().diff()


def f44_spca_191_yw_ar1_sq_logret_252d_d2(close: pd.Series) -> pd.Series:
    ar = (_safe_log(close).diff() ** 2)
    out = ar.rolling(252, min_periods=84).apply(_yule_walker_ar1, raw=True)
    return out.diff().diff()


def f44_spca_192_long_memory_pos_ar1_indicator_252d_d2(close: pd.Series) -> pd.Series:
    ar1 = _safe_log(close).diff().rolling(252, min_periods=84).apply(_yule_walker_ar1, raw=True)
    out = (ar1 > 0.1).astype(float).where(ar1.notna(), np.nan)
    return out.diff().diff()


def f44_spca_193_mean_reversion_neg_ar1_indicator_252d_d2(close: pd.Series) -> pd.Series:
    ar1 = _safe_log(close).diff().rolling(252, min_periods=84).apply(_yule_walker_ar1, raw=True)
    out = (ar1 < -0.1).astype(float).where(ar1.notna(), np.nan)
    return out.diff().diff()


def f44_spca_194_yw_ar1_63d_std_252d_d2(close: pd.Series) -> pd.Series:
    ar1 = _safe_log(close).diff().rolling(63, min_periods=21).apply(_yule_walker_ar1, raw=True)
    out = ar1.rolling(252, min_periods=84).std()
    return out.diff().diff()


def f44_spca_195_burg_ar2_minus_yw_ar1_252d_d2(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(lambda w: _burg_ar_first_coef(w, order=2), raw=True) - r.rolling(252, min_periods=84).apply(_yule_walker_ar1, raw=True)
    return out.diff().diff()


def f44_spca_196_haar_detail_energy_scale5_252d_d2(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(lambda w: _haar_detail_energy(w, 5), raw=True)
    return out.diff().diff()


def f44_spca_197_haar_detail_energy_scale21_252d_d2(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(lambda w: _haar_detail_energy(w, 21), raw=True)
    return out.diff().diff()


def f44_spca_198_haar_detail_energy_scale63_504d_d2(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(504, min_periods=168).apply(lambda w: _haar_detail_energy(w, 63), raw=True)
    return out.diff().diff()


def f44_spca_199_haar_energy_ratio_5_over_21_252d_d2(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    e5 = r.rolling(252, min_periods=84).apply(lambda w: _haar_detail_energy(w, 5), raw=True)
    e21 = r.rolling(252, min_periods=84).apply(lambda w: _haar_detail_energy(w, 21), raw=True)
    out = _safe_div(e5, e21)
    return out.diff().diff()


def f44_spca_200_haar_energy_ratio_5_over_63_504d_d2(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    e5 = r.rolling(504, min_periods=168).apply(lambda w: _haar_detail_energy(w, 5), raw=True)
    e63 = r.rolling(504, min_periods=168).apply(lambda w: _haar_detail_energy(w, 63), raw=True)
    out = _safe_div(e5, e63)
    return out.diff().diff()


def f44_spca_201_daub4_hp_lasttap_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    h = np.array([-0.4830, 0.8365, -0.2241, -0.1294])
    def _f(w):
        if w.size < 4 or np.isnan(w[-4:]).any():
            return np.nan
        return float(np.sum(w[-4:] * h))
    out = lc.rolling(63, min_periods=4).apply(_f, raw=True)
    return out.diff().diff()


def f44_spca_202_daub4_sq_energy_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    h = np.array([-0.4830, 0.8365, -0.2241, -0.1294])
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 8:
            return np.nan
        v = w[valid] if not valid.all() else w
        energies = []
        for t in range(3, v.size):
            energies.append(float(np.sum(v[t-3:t+1] * h)) ** 2)
        if not energies:
            return np.nan
        return float(np.sum(energies))
    out = lc.rolling(63, min_periods=21).apply(_f, raw=True)
    return out.diff().diff()


def f44_spca_203_emd_imf1_amplitude_proxy_5d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    low_pass = lc.ewm(span=5, adjust=False).mean()
    hf = (lc - low_pass).abs()
    out = hf.rolling(21, min_periods=7).max()
    return out.diff().diff()


def f44_spca_204_emd_imf2_amplitude_proxy_21d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    low_pass = lc.ewm(span=21, adjust=False).mean()
    hf = (lc - low_pass).abs()
    out = hf.rolling(63, min_periods=21).max()
    return out.diff().diff()


def f44_spca_205_emd_imf3_amplitude_proxy_63d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    low_pass = lc.ewm(span=63, adjust=False).mean()
    hf = (lc - low_pass).abs()
    out = hf.rolling(252, min_periods=84).max()
    return out.diff().diff()


def f44_spca_206_imf1_share_of_total_energy_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    lp5 = lc.ewm(span=5, adjust=False).mean()
    lp21 = lc.ewm(span=21, adjust=False).mean()
    lp63 = lc.ewm(span=63, adjust=False).mean()
    e1 = ((lc - lp5) ** 2).rolling(252, min_periods=84).sum()
    e2 = ((lp5 - lp21) ** 2).rolling(252, min_periods=84).sum()
    e3 = ((lp21 - lp63) ** 2).rolling(252, min_periods=84).sum()
    out = _safe_div(e1, e1 + e2 + e3)
    return out.diff().diff()


def f44_spca_207_imf3_share_of_total_energy_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    lp5 = lc.ewm(span=5, adjust=False).mean()
    lp21 = lc.ewm(span=21, adjust=False).mean()
    lp63 = lc.ewm(span=63, adjust=False).mean()
    e1 = ((lc - lp5) ** 2).rolling(252, min_periods=84).sum()
    e2 = ((lp5 - lp21) ** 2).rolling(252, min_periods=84).sum()
    e3 = ((lp21 - lp63) ** 2).rolling(252, min_periods=84).sum()
    out = _safe_div(e3, e1 + e2 + e3)
    return out.diff().diff()


def f44_spca_208_wavelet_log_variance_slope_3scales_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    lp5 = lc.ewm(span=5, adjust=False).mean()
    lp21 = lc.ewm(span=21, adjust=False).mean()
    lp63 = lc.ewm(span=63, adjust=False).mean()
    e1 = ((lc - lp5) ** 2).rolling(252, min_periods=84).sum()
    e2 = ((lp5 - lp21) ** 2).rolling(252, min_periods=84).sum()
    e3 = ((lp21 - lp63) ** 2).rolling(252, min_periods=84).sum()
    x = np.log(np.array([5.0, 21.0, 63.0]))
    def _slope(row):
        a = row.values
        if np.isnan(a).any() or (a <= 0).any():
            return np.nan
        y = np.log(a)
        xm = x.mean(); ym = y.mean()
        den = float(((x - xm) ** 2).sum())
        if den <= 0:
            return np.nan
        return float(((x - xm) * (y - ym)).sum() / den)
    stk = pd.concat([e1.rename('a'), e2.rename('b'), e3.rename('c')], axis=1)
    out = stk.apply(_slope, axis=1)
    return out.diff().diff()


def f44_spca_209_wavelet_3scale_entropy_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    lp5 = lc.ewm(span=5, adjust=False).mean()
    lp21 = lc.ewm(span=21, adjust=False).mean()
    lp63 = lc.ewm(span=63, adjust=False).mean()
    e1 = ((lc - lp5) ** 2).rolling(252, min_periods=84).sum()
    e2 = ((lp5 - lp21) ** 2).rolling(252, min_periods=84).sum()
    e3 = ((lp21 - lp63) ** 2).rolling(252, min_periods=84).sum()
    tot = e1 + e2 + e3
    p1 = _safe_div(e1, tot); p2 = _safe_div(e2, tot); p3 = _safe_div(e3, tot)
    stk = pd.concat([p1.rename('a'), p2.rename('b'), p3.rename('c')], axis=1)
    def _ent(row):
        a = row.dropna().values
        a = a[a > 0]
        if a.size < 2:
            return np.nan
        return float(-(a * np.log(a)).sum())
    out = stk.apply(_ent, axis=1)
    return out.diff().diff()


def f44_spca_210_imf3_sign_flip_count_252d_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    lp21 = lc.ewm(span=21, adjust=False).mean()
    lp63 = lc.ewm(span=63, adjust=False).mean()
    imf3 = lp21 - lp63
    sg = np.sign(imf3)
    fl = (sg != sg.shift(1)).astype(float).where(sg.notna() & sg.shift(1).notna(), np.nan)
    out = fl.rolling(252, min_periods=84).sum()
    return out.diff().diff()


def f44_spca_211_goertzel_power_period_21d_in_252d_d2(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(lambda w: _goertzel_power(w, 21), raw=True)
    return out.diff().diff()


def f44_spca_212_goertzel_power_period_42d_in_252d_d2(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(lambda w: _goertzel_power(w, 42), raw=True)
    return out.diff().diff()


def f44_spca_213_goertzel_power_period_63d_in_252d_d2(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(lambda w: _goertzel_power(w, 63), raw=True)
    return out.diff().diff()


def f44_spca_214_goertzel_power_period_252d_in_504d_d2(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(504, min_periods=168).apply(lambda w: _goertzel_power(w, 252), raw=True)
    return out.diff().diff()


def f44_spca_215_welch_psd_period_21d_in_252d_d2(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(lambda w: _welch_psd(w, 21), raw=True)
    return out.diff().diff()


def f44_spca_216_welch_psd_period_63d_in_504d_d2(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(504, min_periods=168).apply(lambda w: _welch_psd(w, 63), raw=True)
    return out.diff().diff()


def f44_spca_217_roofing_filter_hp48_ss10_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    hp = pd.Series(_highpass_2pole(lc.values, 48), index=lc.index)
    ss = pd.Series(_supersmoother(hp.values, 10), index=lc.index)
    out = ss
    return out.diff().diff()


def f44_spca_218_roofing_filter_hp80_ss20_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    hp = pd.Series(_highpass_2pole(lc.values, 80), index=lc.index)
    ss = pd.Series(_supersmoother(hp.values, 20), index=lc.index)
    out = ss
    return out.diff().diff()


def f44_spca_219_roofing_hp48_ss10_sign_flip_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    hp = pd.Series(_highpass_2pole(lc.values, 48), index=lc.index)
    ss = pd.Series(_supersmoother(hp.values, 10), index=lc.index)
    sg = np.sign(ss)
    out = (sg != sg.shift(1)).astype(float).where(sg.notna() & sg.shift(1).notna(), np.nan)
    return out.diff().diff()


def f44_spca_220_decycler60_minus_roofing_hp48_ss10_d2(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    dec = _decycler(lc, 60)
    hp = pd.Series(_highpass_2pole(lc.values, 48), index=lc.index)
    ss = pd.Series(_supersmoother(hp.values, 10), index=lc.index)
    out = dec - lc - ss
    return out.diff().diff()


def f44_spca_221_goertzel21_high_vs_low_corr_252d_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    rh = _safe_log(high).diff()
    rl = _safe_log(low).diff()
    gh = rh.rolling(252, min_periods=84).apply(lambda w: _goertzel_power(w, 21), raw=True)
    gl = rl.rolling(252, min_periods=84).apply(lambda w: _goertzel_power(w, 21), raw=True)
    out = gh.rolling(252, min_periods=84).corr(gl)
    return out.diff().diff()


def f44_spca_222_goertzel63_high_over_low_ratio_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    rh = _safe_log(high).diff()
    rl = _safe_log(low).diff()
    gh = rh.rolling(252, min_periods=84).apply(lambda w: _goertzel_power(w, 63), raw=True)
    gl = rl.rolling(252, min_periods=84).apply(lambda w: _goertzel_power(w, 63), raw=True)
    out = _safe_div(gh, gl)
    return out.diff().diff()


def f44_spca_223_autocorr_decay_lag_below_05_252d_d2(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        v = w[valid] if not valid.all() else w
        m = v.mean()
        vc = v - m
        den = float((vc * vc).sum())
        if den == 0:
            return np.nan
        for k in range(1, min(50, v.size - 5)):
            ac = float((vc[k:] * vc[:-k]).sum() / den)
            if ac < 0.5:
                return float(k)
        return float(50)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff().diff()


def f44_spca_224_ehlers_cyber_cycle_slope_5d_d2(close: pd.Series) -> pd.Series:
    cc = _ehlers_cyber_cycle(_safe_log(close))
    out = cc - cc.shift(5)
    return out.diff().diff()


def f44_spca_225_multi_method_period_disagreement_252d_d2(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _goertzel_peak_period(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        v = w[valid] if not valid.all() else w
        v = v - v.mean()
        best_p = np.nan; best_e = -np.inf
        for p in range(4, min(100, v.size - 5)):
            e = _goertzel_power(v, p)
            if not np.isnan(e) and e > best_e:
                best_e = e; best_p = p
        return float(best_p)
    def _ac_dominant(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        v = w[valid] if not valid.all() else w
        m = v.mean()
        vc = v - m
        den = float((vc * vc).sum())
        if den == 0:
            return np.nan
        best = -np.inf; best_k = np.nan
        for k in range(4, min(100, v.size - 5)):
            ac = float((vc[k:] * vc[:-k]).sum() / den)
            if ac > best:
                best = ac; best_k = k
        return float(best_k)
    gp = r.rolling(252, min_periods=84).apply(_goertzel_peak_period, raw=True)
    ap = r.rolling(252, min_periods=84).apply(_ac_dominant, raw=True)
    out = (gp - ap).abs()
    return out.diff().diff()


# ============================================================
#                         REGISTRY 151_225 (d2)
# ============================================================

SPECTRAL_CYCLE_ANALYSIS_D2_REGISTRY_151_225 = {
    "f44_spca_151_mama_minus_close_logclose_d2": {"inputs": ["close"], "func": f44_spca_151_mama_minus_close_logclose_d2},
    "f44_spca_152_fama_minus_close_logclose_d2": {"inputs": ["close"], "func": f44_spca_152_fama_minus_close_logclose_d2},
    "f44_spca_153_mama_minus_fama_logclose_d2": {"inputs": ["close"], "func": f44_spca_153_mama_minus_fama_logclose_d2},
    "f44_spca_154_mama_fama_crossover_sign_d2": {"inputs": ["close"], "func": f44_spca_154_mama_fama_crossover_sign_d2},
    "f44_spca_155_mama_fama_crossover_flip_event_d2": {"inputs": ["close"], "func": f44_spca_155_mama_fama_crossover_flip_event_d2},
    "f44_spca_156_mama_slope_5d_d2": {"inputs": ["close"], "func": f44_spca_156_mama_slope_5d_d2},
    "f44_spca_157_mama_fama_spread_zscore_252d_d2": {"inputs": ["close"], "func": f44_spca_157_mama_fama_spread_zscore_252d_d2},
    "f44_spca_158_current_mama_above_fama_streak_d2": {"inputs": ["close"], "func": f44_spca_158_current_mama_above_fama_streak_d2},
    "f44_spca_159_mama_fama_spread_atr_norm_d2": {"inputs": ["high", "low", "close"], "func": f44_spca_159_mama_fama_spread_atr_norm_d2},
    "f44_spca_160_mama_fama_max_abs_spread_63d_d2": {"inputs": ["close"], "func": f44_spca_160_mama_fama_max_abs_spread_63d_d2},
    "f44_spca_161_mama_fama_flip_count_252d_d2": {"inputs": ["close"], "func": f44_spca_161_mama_fama_flip_count_252d_d2},
    "f44_spca_162_mama_acceleration_5d_d2": {"inputs": ["close"], "func": f44_spca_162_mama_acceleration_5d_d2},
    "f44_spca_163_mama_phase_delta_inv_proxy_d2": {"inputs": ["close"], "func": f44_spca_163_mama_phase_delta_inv_proxy_d2},
    "f44_spca_164_mama_at_top_252d_range_indicator_d2": {"inputs": ["close"], "func": f44_spca_164_mama_at_top_252d_range_indicator_d2},
    "f44_spca_165_fama_slope_neg_flip_event_d2": {"inputs": ["close"], "func": f44_spca_165_fama_slope_neg_flip_event_d2},
    "f44_spca_166_ehlers_sinewave_per_bar_d2": {"inputs": ["close"], "func": f44_spca_166_ehlers_sinewave_per_bar_d2},
    "f44_spca_167_ehlers_leadwave_per_bar_d2": {"inputs": ["close"], "func": f44_spca_167_ehlers_leadwave_per_bar_d2},
    "f44_spca_168_ehlers_sine_minus_lead_sign_d2": {"inputs": ["close"], "func": f44_spca_168_ehlers_sine_minus_lead_sign_d2},
    "f44_spca_169_ehlers_sine_lead_flip_event_d2": {"inputs": ["close"], "func": f44_spca_169_ehlers_sine_lead_flip_event_d2},
    "f44_spca_170_ehlers_cyber_cycle_d2": {"inputs": ["close"], "func": f44_spca_170_ehlers_cyber_cycle_d2},
    "f44_spca_171_ehlers_cyber_cycle_zscore_252d_d2": {"inputs": ["close"], "func": f44_spca_171_ehlers_cyber_cycle_zscore_252d_d2},
    "f44_spca_172_ehlers_cyber_cycle_sign_flip_d2": {"inputs": ["close"], "func": f44_spca_172_ehlers_cyber_cycle_sign_flip_d2},
    "f44_spca_173_ehlers_cyber_cycle_local_max_indicator_d2": {"inputs": ["close"], "func": f44_spca_173_ehlers_cyber_cycle_local_max_indicator_d2},
    "f44_spca_174_ehlers_cog_10bar_d2": {"inputs": ["close"], "func": f44_spca_174_ehlers_cog_10bar_d2},
    "f44_spca_175_ehlers_cog_21bar_d2": {"inputs": ["close"], "func": f44_spca_175_ehlers_cog_21bar_d2},
    "f44_spca_176_ehlers_cog_trigger_10bar_d2": {"inputs": ["close"], "func": f44_spca_176_ehlers_cog_trigger_10bar_d2},
    "f44_spca_177_ehlers_cog_above_zero_indicator_10bar_d2": {"inputs": ["close"], "func": f44_spca_177_ehlers_cog_above_zero_indicator_10bar_d2},
    "f44_spca_178_ehlers_decycler_60d_d2": {"inputs": ["close"], "func": f44_spca_178_ehlers_decycler_60d_d2},
    "f44_spca_179_ehlers_decycler_oscillator_21_60_d2": {"inputs": ["close"], "func": f44_spca_179_ehlers_decycler_oscillator_21_60_d2},
    "f44_spca_180_ehlers_decycler_60d_sign_flip_d2": {"inputs": ["close"], "func": f44_spca_180_ehlers_decycler_60d_sign_flip_d2},
    "f44_spca_181_burg_ar2_coef1_logret_252d_d2": {"inputs": ["close"], "func": f44_spca_181_burg_ar2_coef1_logret_252d_d2},
    "f44_spca_182_burg_ar4_coef1_logret_252d_d2": {"inputs": ["close"], "func": f44_spca_182_burg_ar4_coef1_logret_252d_d2},
    "f44_spca_183_burg_ar2_coef1_logclose_252d_d2": {"inputs": ["close"], "func": f44_spca_183_burg_ar2_coef1_logclose_252d_d2},
    "f44_spca_184_yw_ar1_logret_63d_d2": {"inputs": ["close"], "func": f44_spca_184_yw_ar1_logret_63d_d2},
    "f44_spca_185_yw_ar1_logret_504d_d2": {"inputs": ["close"], "func": f44_spca_185_yw_ar1_logret_504d_d2},
    "f44_spca_186_abs_burg_ar2_coef1_252d_d2": {"inputs": ["close"], "func": f44_spca_186_abs_burg_ar2_coef1_252d_d2},
    "f44_spca_187_burg_ar2_sign_flip_event_252d_d2": {"inputs": ["close"], "func": f44_spca_187_burg_ar2_sign_flip_event_252d_d2},
    "f44_spca_188_burg_ar2_zscore_252d_in_504d_d2": {"inputs": ["close"], "func": f44_spca_188_burg_ar2_zscore_252d_in_504d_d2},
    "f44_spca_189_yw_ar1_63d_minus_504d_d2": {"inputs": ["close"], "func": f44_spca_189_yw_ar1_63d_minus_504d_d2},
    "f44_spca_190_yw_ar1_abs_logret_252d_d2": {"inputs": ["close"], "func": f44_spca_190_yw_ar1_abs_logret_252d_d2},
    "f44_spca_191_yw_ar1_sq_logret_252d_d2": {"inputs": ["close"], "func": f44_spca_191_yw_ar1_sq_logret_252d_d2},
    "f44_spca_192_long_memory_pos_ar1_indicator_252d_d2": {"inputs": ["close"], "func": f44_spca_192_long_memory_pos_ar1_indicator_252d_d2},
    "f44_spca_193_mean_reversion_neg_ar1_indicator_252d_d2": {"inputs": ["close"], "func": f44_spca_193_mean_reversion_neg_ar1_indicator_252d_d2},
    "f44_spca_194_yw_ar1_63d_std_252d_d2": {"inputs": ["close"], "func": f44_spca_194_yw_ar1_63d_std_252d_d2},
    "f44_spca_195_burg_ar2_minus_yw_ar1_252d_d2": {"inputs": ["close"], "func": f44_spca_195_burg_ar2_minus_yw_ar1_252d_d2},
    "f44_spca_196_haar_detail_energy_scale5_252d_d2": {"inputs": ["close"], "func": f44_spca_196_haar_detail_energy_scale5_252d_d2},
    "f44_spca_197_haar_detail_energy_scale21_252d_d2": {"inputs": ["close"], "func": f44_spca_197_haar_detail_energy_scale21_252d_d2},
    "f44_spca_198_haar_detail_energy_scale63_504d_d2": {"inputs": ["close"], "func": f44_spca_198_haar_detail_energy_scale63_504d_d2},
    "f44_spca_199_haar_energy_ratio_5_over_21_252d_d2": {"inputs": ["close"], "func": f44_spca_199_haar_energy_ratio_5_over_21_252d_d2},
    "f44_spca_200_haar_energy_ratio_5_over_63_504d_d2": {"inputs": ["close"], "func": f44_spca_200_haar_energy_ratio_5_over_63_504d_d2},
    "f44_spca_201_daub4_hp_lasttap_63d_d2": {"inputs": ["close"], "func": f44_spca_201_daub4_hp_lasttap_63d_d2},
    "f44_spca_202_daub4_sq_energy_63d_d2": {"inputs": ["close"], "func": f44_spca_202_daub4_sq_energy_63d_d2},
    "f44_spca_203_emd_imf1_amplitude_proxy_5d_d2": {"inputs": ["close"], "func": f44_spca_203_emd_imf1_amplitude_proxy_5d_d2},
    "f44_spca_204_emd_imf2_amplitude_proxy_21d_d2": {"inputs": ["close"], "func": f44_spca_204_emd_imf2_amplitude_proxy_21d_d2},
    "f44_spca_205_emd_imf3_amplitude_proxy_63d_d2": {"inputs": ["close"], "func": f44_spca_205_emd_imf3_amplitude_proxy_63d_d2},
    "f44_spca_206_imf1_share_of_total_energy_252d_d2": {"inputs": ["close"], "func": f44_spca_206_imf1_share_of_total_energy_252d_d2},
    "f44_spca_207_imf3_share_of_total_energy_252d_d2": {"inputs": ["close"], "func": f44_spca_207_imf3_share_of_total_energy_252d_d2},
    "f44_spca_208_wavelet_log_variance_slope_3scales_252d_d2": {"inputs": ["close"], "func": f44_spca_208_wavelet_log_variance_slope_3scales_252d_d2},
    "f44_spca_209_wavelet_3scale_entropy_252d_d2": {"inputs": ["close"], "func": f44_spca_209_wavelet_3scale_entropy_252d_d2},
    "f44_spca_210_imf3_sign_flip_count_252d_d2": {"inputs": ["close"], "func": f44_spca_210_imf3_sign_flip_count_252d_d2},
    "f44_spca_211_goertzel_power_period_21d_in_252d_d2": {"inputs": ["close"], "func": f44_spca_211_goertzel_power_period_21d_in_252d_d2},
    "f44_spca_212_goertzel_power_period_42d_in_252d_d2": {"inputs": ["close"], "func": f44_spca_212_goertzel_power_period_42d_in_252d_d2},
    "f44_spca_213_goertzel_power_period_63d_in_252d_d2": {"inputs": ["close"], "func": f44_spca_213_goertzel_power_period_63d_in_252d_d2},
    "f44_spca_214_goertzel_power_period_252d_in_504d_d2": {"inputs": ["close"], "func": f44_spca_214_goertzel_power_period_252d_in_504d_d2},
    "f44_spca_215_welch_psd_period_21d_in_252d_d2": {"inputs": ["close"], "func": f44_spca_215_welch_psd_period_21d_in_252d_d2},
    "f44_spca_216_welch_psd_period_63d_in_504d_d2": {"inputs": ["close"], "func": f44_spca_216_welch_psd_period_63d_in_504d_d2},
    "f44_spca_217_roofing_filter_hp48_ss10_d2": {"inputs": ["close"], "func": f44_spca_217_roofing_filter_hp48_ss10_d2},
    "f44_spca_218_roofing_filter_hp80_ss20_d2": {"inputs": ["close"], "func": f44_spca_218_roofing_filter_hp80_ss20_d2},
    "f44_spca_219_roofing_hp48_ss10_sign_flip_d2": {"inputs": ["close"], "func": f44_spca_219_roofing_hp48_ss10_sign_flip_d2},
    "f44_spca_220_decycler60_minus_roofing_hp48_ss10_d2": {"inputs": ["close"], "func": f44_spca_220_decycler60_minus_roofing_hp48_ss10_d2},
    "f44_spca_221_goertzel21_high_vs_low_corr_252d_d2": {"inputs": ["high", "low"], "func": f44_spca_221_goertzel21_high_vs_low_corr_252d_d2},
    "f44_spca_222_goertzel63_high_over_low_ratio_d2": {"inputs": ["high", "low"], "func": f44_spca_222_goertzel63_high_over_low_ratio_d2},
    "f44_spca_223_autocorr_decay_lag_below_05_252d_d2": {"inputs": ["close"], "func": f44_spca_223_autocorr_decay_lag_below_05_252d_d2},
    "f44_spca_224_ehlers_cyber_cycle_slope_5d_d2": {"inputs": ["close"], "func": f44_spca_224_ehlers_cyber_cycle_slope_5d_d2},
    "f44_spca_225_multi_method_period_disagreement_252d_d2": {"inputs": ["close"], "func": f44_spca_225_multi_method_period_disagreement_252d_d2},
}
