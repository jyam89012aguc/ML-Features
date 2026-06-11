"""spectral_cycle_analysis d1 features 076-150 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __d1__001_075.py. Each
feature encodes a different concept in the spectral / cycle theme:
Fisher transform / autocorr dominant-period / DFT energy / Hilbert phase /
DPO / spectral entropy / bandpass filters / cycle regime transitions / composites.

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


def _fisher_transform(s):
    """Fisher transform F(x) = 0.5 * log((1+x)/(1-x)); clipped to (-0.999, 0.999)."""
    x = s.clip(-0.999, 0.999)
    return 0.5 * np.log((1.0 + x) / (1.0 - x))


def _normalize_minmax_neg1_pos1(s, n, min_periods=None):
    """Map s into [-1, 1] using rolling min/max."""
    if min_periods is None:
        min_periods = max(n // 3, 2)
    rmin = s.rolling(n, min_periods=min_periods).min()
    rmax = s.rolling(n, min_periods=min_periods).max()
    return _safe_div(2.0 * (s - rmin), (rmax - rmin)) - 1.0


def _dominant_period_autocorr(w, max_lag=120, min_lag=4):
    """Window callable: lag of max positive autocorrelation in (min_lag, max_lag)."""
    valid = ~np.isnan(w)
    if valid.sum() < max_lag + 5:
        return np.nan
    v = w[valid] if not valid.all() else w
    m = v.mean()
    vc = v - m
    den = float((vc * vc).sum())
    if den == 0:
        return np.nan
    best_ac = -np.inf
    best_k = np.nan
    upper = min(max_lag, v.size - 5)
    for k in range(min_lag, upper):
        num = float((vc[k:] * vc[:-k]).sum())
        ac = num / den
        if ac > best_ac:
            best_ac = ac
            best_k = k
    return float(best_k)


def _autocorr_at_lag(w, k):
    """Window callable: autocorrelation at lag k."""
    valid = ~np.isnan(w)
    if valid.sum() < k + 5:
        return np.nan
    v = w[valid] if not valid.all() else w
    if v.size <= k:
        return np.nan
    m = v.mean()
    vc = v - m
    den = float((vc * vc).sum())
    if den == 0:
        return np.nan
    return float((vc[k:] * vc[:-k]).sum() / den)


def _dft_energy_at_period(w, period):
    """Energy at given period via single Fourier coefficient."""
    valid = ~np.isnan(w)
    if valid.sum() < period * 2:
        return np.nan
    v = w[valid] if not valid.all() else w
    v = v - v.mean()
    n = v.size
    if period <= 1 or period >= n:
        return np.nan
    k = float(n) / float(period)
    omega = 2.0 * np.pi * k / float(n)
    t = np.arange(n)
    re = float((v * np.cos(omega * t)).sum())
    im = float((v * np.sin(omega * t)).sum())
    return (re * re + im * im) / float(n)


def _spectral_entropy(w, max_period=120, min_period=4, step=2):
    """Shannon entropy of normalized DFT-energy spectrum across [min_period..max_period]."""
    valid = ~np.isnan(w)
    if valid.sum() < max_period * 2:
        return np.nan
    v = w[valid] if not valid.all() else w
    v = v - v.mean()
    n = v.size
    energies = []
    for p in range(min_period, max_period + 1, step):
        if p >= n:
            break
        k = float(n) / float(p)
        omega = 2.0 * np.pi * k / float(n)
        t = np.arange(n)
        re = float((v * np.cos(omega * t)).sum())
        im = float((v * np.sin(omega * t)).sum())
        energies.append((re * re + im * im) / float(n))
    if not energies:
        return np.nan
    e = np.array(energies)
    s = e.sum()
    if s <= 0:
        return np.nan
    p = e / s
    p = p[p > 0]
    return float(-(p * np.log(p)).sum())


def _hilbert_phase_lastpt(w):
    """Approximate Hilbert phase at last bar via finite-difference quadrature."""
    valid = ~np.isnan(w)
    if valid.sum() < 5:
        return np.nan
    v = w[valid] if not valid.all() else w
    n = v.size
    x = np.arange(n, dtype=float)
    # Linear detrend
    xm = x.mean(); ym = v.mean()
    den = float(((x - xm) ** 2).sum())
    if den <= 0:
        return np.nan
    b = float(((x - xm) * (v - ym)).sum() / den)
    a = ym - b * xm
    d = v - (a + b * x)
    if n < 5:
        return np.nan
    re = float(d[-1])
    # Quadrature via 2-bar centered difference of detrended series
    im = float(d[-1] - d[-3]) / 2.0
    return float(np.arctan2(im, re))


def _dpo(close, period):
    """Detrended Price Oscillator: close - SMA(close, period) shifted by period/2 + 1.
    PIT-safe by using only past data (no centered window — we shift the SMA backward, which
    inserts NaNs at the start, which is fine)."""
    sma = close.rolling(period, min_periods=max(period // 3, 2)).mean()
    return close - sma.shift(int(period // 2) + 1)


def f44_spca_076_dpo_logclose_10d_d1(close: pd.Series) -> pd.Series:
    out = _dpo(_safe_log(close), 10)
    return out.diff()


def f44_spca_077_dpo_logclose_21d_d1(close: pd.Series) -> pd.Series:
    out = _dpo(_safe_log(close), 21)
    return out.diff()


def f44_spca_078_dpo_logclose_42d_d1(close: pd.Series) -> pd.Series:
    out = _dpo(_safe_log(close), 42)
    return out.diff()


def f44_spca_079_dpo_logclose_63d_d1(close: pd.Series) -> pd.Series:
    out = _dpo(_safe_log(close), 63)
    return out.diff()


def f44_spca_080_dpo_logclose_126d_d1(close: pd.Series) -> pd.Series:
    out = _dpo(_safe_log(close), 126)
    return out.diff()


def f44_spca_081_dpo_logclose_252d_d1(close: pd.Series) -> pd.Series:
    out = _dpo(_safe_log(close), 252)
    return out.diff()


def f44_spca_082_dpo_sign_63d_d1(close: pd.Series) -> pd.Series:
    d = _dpo(_safe_log(close), 63)
    out = np.sign(d)
    return out.diff()


def f44_spca_083_dpo_sign_flip_count_63d_in_252d_d1(close: pd.Series) -> pd.Series:
    d = _dpo(_safe_log(close), 63)
    sg = np.sign(d)
    fl = (sg != sg.shift(1)).astype(float).where(d.notna() & d.shift(1).notna(), np.nan)
    out = fl.rolling(252, min_periods=84).sum()
    return out.diff()


def f44_spca_084_dpo_local_max_count_63d_in_252d_d1(close: pd.Series) -> pd.Series:
    d = _dpo(_safe_log(close), 63)
    is_max = (d == d.rolling(11, min_periods=5).max()) & d.notna()
    out = is_max.astype(float).rolling(252, min_periods=84).sum()
    return out.diff()


def f44_spca_085_dpo_amplitude_63d_in_252d_d1(close: pd.Series) -> pd.Series:
    d = _dpo(_safe_log(close), 63)
    out = d.rolling(252, min_periods=84).max() - d.rolling(252, min_periods=84).min()
    return out.diff()


def f44_spca_086_dpo_zscore_63d_in_252d_d1(close: pd.Series) -> pd.Series:
    d = _dpo(_safe_log(close), 63)
    out = _rolling_zscore(d, 252, min_periods=84)
    return out.diff()


def f44_spca_087_dpo_pct_rank_63d_in_252d_d1(close: pd.Series) -> pd.Series:
    d = _dpo(_safe_log(close), 63)
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
    out = d.rolling(252, min_periods=84).apply(_rk, raw=True)
    return out.diff()


def f44_spca_088_dpo_slope_21d_63d_d1(close: pd.Series) -> pd.Series:
    d = _dpo(_safe_log(close), 63)
    out = d - d.shift(21)
    return out.diff()


def f44_spca_089_dpo_sign_agree_21_vs_252_d1(close: pd.Series) -> pd.Series:
    d21 = _dpo(_safe_log(close), 21)
    d252 = _dpo(_safe_log(close), 252)
    out = (np.sign(d21) == np.sign(d252)).astype(float).where(d21.notna() & d252.notna(), np.nan)
    return out.diff()


def f44_spca_090_dpo_at_top_of_252d_range_63d_d1(close: pd.Series) -> pd.Series:
    d = _dpo(_safe_log(close), 63)
    rmax = d.rolling(252, min_periods=84).max()
    out = (d >= 0.95 * rmax).astype(float).where(rmax.notna(), np.nan)
    return out.diff()


def f44_spca_091_spectral_entropy_logret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _spectral_entropy(w, max_period=100, min_period=4, step=2)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_092_spectral_entropy_logret_504d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _spectral_entropy(w, max_period=200, min_period=4, step=4)
    out = r.rolling(504, min_periods=168).apply(_f, raw=True)
    return out.diff()


def f44_spca_093_spectral_entropy_norm_logret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        e = _spectral_entropy(w, max_period=100, min_period=4, step=2)
        n_bins = (100 - 4) // 2 + 1
        if np.isnan(e) or n_bins <= 1:
            return np.nan
        return e / np.log(n_bins)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_094_spectral_entropy_slope_63d_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _spectral_entropy(w, max_period=100, min_period=4, step=2)
    e = r.rolling(252, min_periods=84).apply(_f, raw=True)
    out = e - e.shift(63)
    return out.diff()


def f44_spca_095_spectral_entropy_zscore_252d_in_504d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _spectral_entropy(w, max_period=100, min_period=4, step=2)
    e = r.rolling(252, min_periods=84).apply(_f, raw=True)
    out = _rolling_zscore(e, 504, min_periods=168)
    return out.diff()


def f44_spca_096_spectral_concentration_inv_norm_entropy_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        e = _spectral_entropy(w, max_period=100, min_period=4, step=2)
        n_bins = (100 - 4) // 2 + 1
        if np.isnan(e) or n_bins <= 1:
            return np.nan
        return 1.0 - e / np.log(n_bins)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_097_psd_dominant_period_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        v = w[valid] if not valid.all() else w
        v = v - v.mean()
        best_p = np.nan; best_e = -np.inf
        for p in range(4, 100):
            if p >= v.size:
                break
            e = _dft_energy_at_period(v, p)
            if not np.isnan(e) and e > best_e:
                best_e = e; best_p = p
        return float(best_p)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_098_spectral_bandwidth_half_max_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        v = w[valid] if not valid.all() else w
        v = v - v.mean()
        energies = []
        for p in range(4, 100):
            if p >= v.size:
                break
            e = _dft_energy_at_period(v, p)
            if not np.isnan(e):
                energies.append(e)
        if not energies:
            return np.nan
        arr = np.array(energies)
        mx = arr.max()
        if mx <= 0:
            return np.nan
        return float((arr > 0.5 * mx).sum())
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_099_spectral_skewness_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        v = w[valid] if not valid.all() else w
        v = v - v.mean()
        energies = []
        for p in range(4, 100):
            if p >= v.size:
                break
            e = _dft_energy_at_period(v, p)
            if not np.isnan(e):
                energies.append(e)
        if len(energies) < 5:
            return np.nan
        arr = np.array(energies)
        m = arr.mean(); sd = arr.std(ddof=1)
        if sd <= 0:
            return np.nan
        return float(np.mean(((arr - m) / sd) ** 3))
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_100_high_freq_power_share_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        v = w[valid] if not valid.all() else w
        v = v - v.mean()
        energies = []
        hi_share = 0.0
        total = 0.0
        for p in range(4, 100):
            if p >= v.size:
                break
            e = _dft_energy_at_period(v, p)
            if not np.isnan(e):
                total += e
                if p < 21:
                    hi_share += e
        if total <= 0:
            return np.nan
        return float(hi_share / total)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_101_low_freq_power_share_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        v = w[valid] if not valid.all() else w
        v = v - v.mean()
        lo_share = 0.0
        total = 0.0
        for p in range(4, 100):
            if p >= v.size:
                break
            e = _dft_energy_at_period(v, p)
            if not np.isnan(e):
                total += e
                if p > 63:
                    lo_share += e
        if total <= 0:
            return np.nan
        return float(lo_share / total)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_102_mid_freq_power_share_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        v = w[valid] if not valid.all() else w
        v = v - v.mean()
        mid = 0.0
        total = 0.0
        for p in range(4, 100):
            if p >= v.size:
                break
            e = _dft_energy_at_period(v, p)
            if not np.isnan(e):
                total += e
                if 21 <= p <= 63:
                    mid += e
        if total <= 0:
            return np.nan
        return float(mid / total)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_103_high_over_low_freq_power_ratio_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        v = w[valid] if not valid.all() else w
        v = v - v.mean()
        hi = 0.0; lo = 0.0
        for p in range(4, 100):
            if p >= v.size:
                break
            e = _dft_energy_at_period(v, p)
            if not np.isnan(e):
                if p < 21:
                    hi += e
                elif p > 63:
                    lo += e
        if lo <= 0:
            return np.nan
        return float(hi / lo)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_104_spectral_centroid_period_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        v = w[valid] if not valid.all() else w
        v = v - v.mean()
        nums = 0.0; dens = 0.0
        for p in range(4, 100):
            if p >= v.size:
                break
            e = _dft_energy_at_period(v, p)
            if not np.isnan(e):
                nums += p * e
                dens += e
        if dens <= 0:
            return np.nan
        return float(nums / dens)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_105_spectral_flatness_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        v = w[valid] if not valid.all() else w
        v = v - v.mean()
        energies = []
        for p in range(4, 100):
            if p >= v.size:
                break
            e = _dft_energy_at_period(v, p)
            if not np.isnan(e) and e > 0:
                energies.append(e)
        if len(energies) < 5:
            return np.nan
        arr = np.array(energies)
        gm = np.exp(np.mean(np.log(arr)))
        am = np.mean(arr)
        if am <= 0:
            return np.nan
        return float(gm / am)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_106_supersmoother_period_21d_logclose_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    a1 = np.exp(-np.sqrt(2.0) * np.pi / 21.0)
    b1 = 2.0 * a1 * np.cos(np.sqrt(2.0) * np.pi / 21.0)
    c2 = b1; c3 = -a1 * a1; c1 = 1.0 - c2 - c3
    arr = lc.values
    n = arr.size
    out_arr = np.full(n, np.nan)
    for i in range(n):
        if np.isnan(arr[i]):
            continue
        if i < 2:
            out_arr[i] = arr[i]
            continue
        prev1 = out_arr[i-1] if not np.isnan(out_arr[i-1]) else arr[i-1]
        prev2 = out_arr[i-2] if not np.isnan(out_arr[i-2]) else arr[i-2]
        out_arr[i] = c1 * (arr[i] + (arr[i-1] if not np.isnan(arr[i-1]) else arr[i])) / 2.0 + c2 * prev1 + c3 * prev2
    out = pd.Series(out_arr, index=lc.index)
    return out.diff()


def f44_spca_107_supersmoother_period_63d_logclose_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    a1 = np.exp(-np.sqrt(2.0) * np.pi / 63.0)
    b1 = 2.0 * a1 * np.cos(np.sqrt(2.0) * np.pi / 63.0)
    c2 = b1; c3 = -a1 * a1; c1 = 1.0 - c2 - c3
    arr = lc.values
    n = arr.size
    out_arr = np.full(n, np.nan)
    for i in range(n):
        if np.isnan(arr[i]):
            continue
        if i < 2:
            out_arr[i] = arr[i]
            continue
        prev1 = out_arr[i-1] if not np.isnan(out_arr[i-1]) else arr[i-1]
        prev2 = out_arr[i-2] if not np.isnan(out_arr[i-2]) else arr[i-2]
        out_arr[i] = c1 * (arr[i] + (arr[i-1] if not np.isnan(arr[i-1]) else arr[i])) / 2.0 + c2 * prev1 + c3 * prev2
    out = pd.Series(out_arr, index=lc.index)
    return out.diff()


def f44_spca_108_supersmoother_period_252d_logclose_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    a1 = np.exp(-np.sqrt(2.0) * np.pi / 252.0)
    b1 = 2.0 * a1 * np.cos(np.sqrt(2.0) * np.pi / 252.0)
    c2 = b1; c3 = -a1 * a1; c1 = 1.0 - c2 - c3
    arr = lc.values
    n = arr.size
    out_arr = np.full(n, np.nan)
    for i in range(n):
        if np.isnan(arr[i]):
            continue
        if i < 2:
            out_arr[i] = arr[i]
            continue
        prev1 = out_arr[i-1] if not np.isnan(out_arr[i-1]) else arr[i-1]
        prev2 = out_arr[i-2] if not np.isnan(out_arr[i-2]) else arr[i-2]
        out_arr[i] = c1 * (arr[i] + (arr[i-1] if not np.isnan(arr[i-1]) else arr[i])) / 2.0 + c2 * prev1 + c3 * prev2
    out = pd.Series(out_arr, index=lc.index)
    return out.diff()


def f44_spca_109_highpass_logclose_minus_smoother_63d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    a1 = np.exp(-np.sqrt(2.0) * np.pi / 63.0)
    b1 = 2.0 * a1 * np.cos(np.sqrt(2.0) * np.pi / 63.0)
    c2 = b1; c3 = -a1 * a1; c1 = 1.0 - c2 - c3
    arr = lc.values
    n = arr.size
    ss = np.full(n, np.nan)
    for i in range(n):
        if np.isnan(arr[i]):
            continue
        if i < 2:
            ss[i] = arr[i]
            continue
        prev1 = ss[i-1] if not np.isnan(ss[i-1]) else arr[i-1]
        prev2 = ss[i-2] if not np.isnan(ss[i-2]) else arr[i-2]
        ss[i] = c1 * (arr[i] + (arr[i-1] if not np.isnan(arr[i-1]) else arr[i])) / 2.0 + c2 * prev1 + c3 * prev2
    out = pd.Series(arr - ss, index=lc.index)
    return out.diff()


def f44_spca_110_bandpass_smoother_21_minus_63_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    def _ss(arr, period):
        a1 = np.exp(-np.sqrt(2.0) * np.pi / period)
        b1 = 2.0 * a1 * np.cos(np.sqrt(2.0) * np.pi / period)
        c2 = b1; c3 = -a1 * a1; c1 = 1.0 - c2 - c3
        n = arr.size
        out_ = np.full(n, np.nan)
        for i in range(n):
            if np.isnan(arr[i]):
                continue
            if i < 2:
                out_[i] = arr[i]
                continue
            p1 = out_[i-1] if not np.isnan(out_[i-1]) else arr[i-1]
            p2 = out_[i-2] if not np.isnan(out_[i-2]) else arr[i-2]
            out_[i] = c1 * (arr[i] + (arr[i-1] if not np.isnan(arr[i-1]) else arr[i])) / 2.0 + c2 * p1 + c3 * p2
        return out_
    arr = lc.values
    out = pd.Series(_ss(arr, 21.0) - _ss(arr, 63.0), index=lc.index)
    return out.diff()


def f44_spca_111_ema_period_21_logclose_d1(close: pd.Series) -> pd.Series:
    out = _safe_log(close).ewm(span=21, adjust=False).mean()
    return out.diff()


def f44_spca_112_ema_period_63_logclose_d1(close: pd.Series) -> pd.Series:
    out = _safe_log(close).ewm(span=63, adjust=False).mean()
    return out.diff()


def f44_spca_113_ema_period_252_logclose_d1(close: pd.Series) -> pd.Series:
    out = _safe_log(close).ewm(span=252, adjust=False).mean()
    return out.diff()


def f44_spca_114_ema_diff_21_minus_63_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    out = lc.ewm(span=21, adjust=False).mean() - lc.ewm(span=63, adjust=False).mean()
    return out.diff()


def f44_spca_115_ema_diff_63_minus_252_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    out = lc.ewm(span=63, adjust=False).mean() - lc.ewm(span=252, adjust=False).mean()
    return out.diff()


def f44_spca_116_roofing_filter_proxy_logclose_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    # Highpass approx via 48d EMA subtract
    hp = lc - lc.ewm(span=48, adjust=False).mean()
    # Then SuperSmoother at period 10
    arr = hp.values
    period = 10.0
    a1 = np.exp(-np.sqrt(2.0) * np.pi / period)
    b1 = 2.0 * a1 * np.cos(np.sqrt(2.0) * np.pi / period)
    c2 = b1; c3 = -a1 * a1; c1 = 1.0 - c2 - c3
    n = arr.size
    out_arr = np.full(n, np.nan)
    for i in range(n):
        if np.isnan(arr[i]):
            continue
        if i < 2:
            out_arr[i] = arr[i]
            continue
        p1 = out_arr[i-1] if not np.isnan(out_arr[i-1]) else arr[i-1]
        p2 = out_arr[i-2] if not np.isnan(out_arr[i-2]) else arr[i-2]
        out_arr[i] = c1 * (arr[i] + (arr[i-1] if not np.isnan(arr[i-1]) else arr[i])) / 2.0 + c2 * p1 + c3 * p2
    out = pd.Series(out_arr, index=lc.index)
    return out.diff()


def f44_spca_117_hull_ma_period_21_logclose_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    def _wma(s, n):
        def _f(x):
            m = len(x); wts = np.arange(1, m + 1, dtype=float); mask = ~np.isnan(x)
            if mask.sum() < max(n // 3, 2):
                return np.nan
            d = float((wts * mask).sum())
            if d == 0:
                return np.nan
            return float(np.nansum(x * wts) / d)
        return s.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)
    h21 = (2.0 * _wma(lc, 10) - _wma(lc, 21))
    out = _wma(h21, 5)
    return out.diff()


def f44_spca_118_hull_ma_period_63_logclose_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    def _wma(s, n):
        def _f(x):
            m = len(x); wts = np.arange(1, m + 1, dtype=float); mask = ~np.isnan(x)
            if mask.sum() < max(n // 3, 2):
                return np.nan
            d = float((wts * mask).sum())
            if d == 0:
                return np.nan
            return float(np.nansum(x * wts) / d)
        return s.rolling(n, min_periods=max(n // 3, 2)).apply(_f, raw=True)
    h63 = (2.0 * _wma(lc, 32) - _wma(lc, 63))
    out = _wma(h63, 8)
    return out.diff()


def f44_spca_119_ema_diff_21_minus_42_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    out = lc.ewm(span=21, adjust=False).mean() - lc.ewm(span=42, adjust=False).mean()
    return out.diff()


def f44_spca_120_bandpass_amplitude_63d_rolling_max_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    bp = lc.ewm(span=21, adjust=False).mean() - lc.ewm(span=63, adjust=False).mean()
    out = bp.abs().rolling(63, min_periods=21).max()
    return out.diff()


def f44_spca_121_dom_period_gt_100d_indicator_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _dominant_period_autocorr(w, max_lag=120, min_lag=4)
    dp = r.rolling(252, min_periods=84).apply(_f, raw=True)
    out = (dp > 100).astype(float).where(dp.notna(), np.nan)
    return out.diff()


def f44_spca_122_dom_period_lt_21d_indicator_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _dominant_period_autocorr(w, max_lag=120, min_lag=4)
    dp = r.rolling(252, min_periods=84).apply(_f, raw=True)
    out = (dp < 21).astype(float).where(dp.notna(), np.nan)
    return out.diff()


def f44_spca_123_dom_period_change_event_21d_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _dominant_period_autocorr(w, max_lag=120, min_lag=4)
    dp = r.rolling(252, min_periods=84).apply(_f, raw=True)
    med = dp.rolling(252, min_periods=84).median()
    ch = (dp - dp.shift(21)).abs()
    out = (ch > 0.5 * med).astype(float).where(med.notna() & ch.notna(), np.nan)
    return out.diff()


def f44_spca_124_high_amplitude_regime_indicator_63d_in_252d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    amp = (lc - lc.rolling(63, min_periods=21).mean()).abs().rolling(63, min_periods=21).max()
    med = amp.rolling(252, min_periods=84).median()
    out = (amp > 2.0 * med).astype(float).where(med.notna(), np.nan)
    return out.diff()


def f44_spca_125_low_amplitude_regime_indicator_63d_in_252d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    amp = (lc - lc.rolling(63, min_periods=21).mean()).abs().rolling(63, min_periods=21).max()
    med = amp.rolling(252, min_periods=84).median()
    out = (amp < 0.5 * med).astype(float).where(med.notna(), np.nan)
    return out.diff()


def f44_spca_126_frac_high_amplitude_252d_63d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    amp = (lc - lc.rolling(63, min_periods=21).mean()).abs().rolling(63, min_periods=21).max()
    med = amp.rolling(252, min_periods=84).median()
    hi = (amp > 2.0 * med).astype(float).where(med.notna(), np.nan)
    out = hi.rolling(252, min_periods=84).mean()
    return out.diff()


def f44_spca_127_current_high_amplitude_streak_63d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    amp = (lc - lc.rolling(63, min_periods=21).mean()).abs().rolling(63, min_periods=21).max()
    med = amp.rolling(252, min_periods=84).median()
    hi = (amp > 2.0 * med).astype(int).where(med.notna(), 0)
    block = (hi != hi.shift(1)).fillna(False).cumsum()
    st = hi.groupby(block).cumcount().astype(float)
    out = (st * (hi > 0)).where(med.notna(), np.nan)
    return out.diff()


def f44_spca_128_cycle_regime_change_count_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _dominant_period_autocorr(w, max_lag=120, min_lag=4)
    dp = r.rolling(252, min_periods=84).apply(_f, raw=True)
    lc = _safe_log(close)
    amp = (lc - lc.rolling(63, min_periods=21).mean()).abs().rolling(63, min_periods=21).max()
    med_dp = dp.rolling(252, min_periods=84).median()
    med_amp = amp.rolling(252, min_periods=84).median()
    ch_dp = ((dp - dp.shift(21)).abs() > 0.5 * med_dp).astype(float)
    ch_amp = ((amp - amp.shift(21)).abs() > med_amp).astype(float)
    out = (ch_dp + ch_amp).rolling(252, min_periods=84).sum()
    return out.diff()


def f44_spca_129_spectral_entropy_above_80pct_504d_indicator_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _spectral_entropy(w, max_period=100, min_period=4, step=2)
    e = r.rolling(252, min_periods=84).apply(_f, raw=True)
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
    rk = e.rolling(504, min_periods=168).apply(_rk, raw=True)
    out = (rk > 0.8).astype(float).where(rk.notna(), np.nan)
    return out.diff()


def f44_spca_130_spectral_entropy_collapse_event_21d_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _spectral_entropy(w, max_period=100, min_period=4, step=2)
    e = r.rolling(252, min_periods=84).apply(_f, raw=True)
    sd = e.rolling(252, min_periods=84).std()
    de = (e.shift(21) - e)
    out = (de > sd).astype(float).where(de.notna() & sd.notna(), np.nan)
    return out.diff()


def f44_spca_131_spectral_flatness_change_21d_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        v = w[valid] if not valid.all() else w
        v = v - v.mean()
        energies = []
        for p in range(4, 100):
            if p >= v.size:
                break
            e = _dft_energy_at_period(v, p)
            if not np.isnan(e) and e > 0:
                energies.append(e)
        if len(energies) < 5:
            return np.nan
        arr = np.array(energies)
        gm = np.exp(np.mean(np.log(arr)))
        am = np.mean(arr)
        if am <= 0:
            return np.nan
        return float(gm / am)
    fl = r.rolling(252, min_periods=84).apply(_f, raw=True)
    out = fl - fl.shift(21)
    return out.diff()


def f44_spca_132_dom_period_slope_63d_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _dominant_period_autocorr(w, max_lag=120, min_lag=4)
    dp = r.rolling(252, min_periods=84).apply(_f, raw=True)
    out = _rolling_slope(dp, 63, min_periods=21)
    return out.diff()


def f44_spca_133_dom_period_inv_std_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _dominant_period_autocorr(w, max_lag=120, min_lag=4)
    dp = r.rolling(252, min_periods=84).apply(_f, raw=True)
    sd = dp.rolling(252, min_periods=84).std()
    out = 1.0 / sd.replace(0, np.nan)
    return out.diff()


def f44_spca_134_cycle_regime_class_entropy_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _dominant_period_autocorr(w, max_lag=120, min_lag=4)
    dp = r.rolling(252, min_periods=84).apply(_f, raw=True)
    cls = pd.Series(np.where(dp < 21, 0, np.where(dp > 100, 2, 1)), index=dp.index).where(dp.notna(), np.nan)
    def _ent(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        p = np.array([(v == k).sum() / v.size for k in (0, 1, 2)])
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    out = cls.rolling(252, min_periods=84).apply(_ent, raw=True)
    return out.diff()


def f44_spca_135_amplitude_x_dom_period_63d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    amp = (lc - lc.rolling(63, min_periods=21).mean()).abs().rolling(63, min_periods=21).max()
    r = lc.diff()
    def _f(w):
        return _dominant_period_autocorr(w, max_lag=120, min_lag=4)
    dp = r.rolling(252, min_periods=84).apply(_f, raw=True)
    out = amp * dp
    return out.diff()


def f44_spca_136_phase_top_high_amp_composite_63d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    r = lc.diff()
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    amp = (lc - lc.rolling(63, min_periods=21).mean()).abs().rolling(63, min_periods=21).max()
    med = amp.rolling(252, min_periods=84).median()
    top = (np.abs(ph) < 0.3).astype(float)
    hi = (amp > 2.0 * med).astype(float)
    out = (top * hi).where(ph.notna() & med.notna(), np.nan)
    return out.diff()


def f44_spca_137_phase_rollover_at_252d_high_composite_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    lc = _safe_log(close); lh = _safe_log(high)
    r = lc.diff()
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    rolled = ((ph.shift(5) > 0) & (ph < 0)).astype(float)
    rmax = lh.rolling(252, min_periods=84).max()
    at_high = (lh >= rmax - 0.05).astype(float)
    out = (rolled * at_high).where(ph.notna() & ph.shift(5).notna() & rmax.notna(), np.nan)
    return out.diff()


def f44_spca_138_spectral_entropy_collapse_at_high_composite_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    lc = _safe_log(close); lh = _safe_log(high)
    r = lc.diff()
    def _f(w):
        return _spectral_entropy(w, max_period=100, min_period=4, step=2)
    e = r.rolling(252, min_periods=84).apply(_f, raw=True)
    sd = e.rolling(252, min_periods=84).std()
    de = e.shift(21) - e
    coll = (de > sd).astype(float)
    rmax = lh.rolling(252, min_periods=84).max()
    at_high = (lh >= rmax - 0.05).astype(float)
    out = (coll * at_high).where(de.notna() & rmax.notna(), np.nan)
    return out.diff()


def f44_spca_139_long_cycle_dom_at_high_composite_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _dominant_period_autocorr(w, max_lag=120, min_lag=4)
    dp = r.rolling(252, min_periods=84).apply(_f, raw=True)
    long = (dp > 100).astype(float)
    lh = _safe_log(high)
    rmax = lh.rolling(252, min_periods=84).max()
    at_high = (lh >= rmax - 0.05).astype(float)
    out = (long * at_high).where(dp.notna() & rmax.notna(), np.nan)
    return out.diff()


def f44_spca_140_dpo_top_fisher_above1_composite_63d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    d = _dpo(lc, 63)
    rmax = d.rolling(252, min_periods=84).max()
    top = (d >= 0.95 * rmax).astype(float)
    x = _normalize_minmax_neg1_pos1(lc, 63, min_periods=21)
    fsh = _fisher_transform(x)
    out = (top * (fsh > 1.0).astype(float)).where(rmax.notna() & fsh.notna(), np.nan)
    return out.diff()


def f44_spca_141_hf_power_surge_at_top_composite_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        v = w[valid] if not valid.all() else w
        v = v - v.mean()
        hi_share = 0.0; total = 0.0
        for p in range(4, 100):
            if p >= v.size:
                break
            e = _dft_energy_at_period(v, p)
            if not np.isnan(e):
                total += e
                if p < 21:
                    hi_share += e
        if total <= 0:
            return np.nan
        return float(hi_share / total)
    hf = r.rolling(252, min_periods=84).apply(_f, raw=True)
    lh = _safe_log(high)
    rmax = lh.rolling(252, min_periods=84).max()
    at_high = (lh >= rmax - 0.05).astype(float)
    out = ((hf > 0.5).astype(float) * at_high).where(hf.notna() & rmax.notna(), np.nan)
    return out.diff()


def f44_spca_142_spec_concentration_with_rollover_composite_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        e = _spectral_entropy(w, max_period=100, min_period=4, step=2)
        n_bins = (100 - 4) // 2 + 1
        if np.isnan(e) or n_bins <= 1:
            return np.nan
        return 1.0 - e / np.log(n_bins)
    conc = r.rolling(252, min_periods=84).apply(_f, raw=True)
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    rolled = ((ph.shift(5) > 0) & (ph < 0)).astype(float)
    out = ((conc > 0.5).astype(float) * rolled).where(conc.notna() & ph.notna() & ph.shift(5).notna(), np.nan)
    return out.diff()


def f44_spca_143_supersmoother_63_slope_sign_flip_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    arr = lc.values
    period = 63.0
    a1 = np.exp(-np.sqrt(2.0) * np.pi / period)
    b1 = 2.0 * a1 * np.cos(np.sqrt(2.0) * np.pi / period)
    c2 = b1; c3 = -a1 * a1; c1 = 1.0 - c2 - c3
    n = arr.size
    ss = np.full(n, np.nan)
    for i in range(n):
        if np.isnan(arr[i]):
            continue
        if i < 2:
            ss[i] = arr[i]
            continue
        p1 = ss[i-1] if not np.isnan(ss[i-1]) else arr[i-1]
        p2 = ss[i-2] if not np.isnan(ss[i-2]) else arr[i-2]
        ss[i] = c1 * (arr[i] + (arr[i-1] if not np.isnan(arr[i-1]) else arr[i])) / 2.0 + c2 * p1 + c3 * p2
    ss_s = pd.Series(ss, index=lc.index)
    sl = ss_s.diff()
    sg = np.sign(sl)
    out = ((sg != sg.shift(1)) & sl.notna() & sl.shift(1).notna()).astype(float)
    return out.diff()


def f44_spca_144_amp_regime_fisher_extreme_composite_63d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    amp = (lc - lc.rolling(63, min_periods=21).mean()).abs().rolling(63, min_periods=21).max()
    med = amp.rolling(252, min_periods=84).median()
    hi = (amp > 2.0 * med).astype(float)
    x = _normalize_minmax_neg1_pos1(lc, 63, min_periods=21)
    fsh = _fisher_transform(x)
    ext = (fsh.abs() > 1.5).astype(float)
    out = (hi * ext).where(med.notna() & fsh.notna(), np.nan)
    return out.diff()


def f44_spca_145_short_cycle_at_high_composite_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _dominant_period_autocorr(w, max_lag=120, min_lag=4)
    dp = r.rolling(252, min_periods=84).apply(_f, raw=True)
    short = (dp < 21).astype(float)
    lh = _safe_log(high)
    rmax = lh.rolling(252, min_periods=84).max()
    at_high = (lh >= rmax - 0.05).astype(float)
    out = (short * at_high).where(dp.notna() & rmax.notna(), np.nan)
    return out.diff()


def f44_spca_146_phase_decoupling_relative_to_amp_63d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    r = lc.diff()
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    amp = (lc - lc.rolling(63, min_periods=21).mean()).abs().rolling(63, min_periods=21).max()
    out = _safe_div((ph - ph.shift(5)).abs(), amp.replace(0, np.nan))
    return out.diff()


def f44_spca_147_ema21_minus_ema63_sign_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    d = lc.ewm(span=21, adjust=False).mean() - lc.ewm(span=63, adjust=False).mean()
    out = np.sign(d)
    return out.diff()


def f44_spca_148_ema21_ema63_cross_flip_event_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    d = lc.ewm(span=21, adjust=False).mean() - lc.ewm(span=63, adjust=False).mean()
    sg = np.sign(d)
    out = (sg != sg.shift(1)).astype(float).where(d.notna() & d.shift(1).notna(), np.nan)
    return out.diff()


def f44_spca_149_bandpass_amplitude_top5pct_252d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    bp = lc.ewm(span=21, adjust=False).mean() - lc.ewm(span=63, adjust=False).mean()
    amp = bp.abs()
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
    rk = amp.rolling(252, min_periods=84).apply(_rk, raw=True)
    out = (rk > 0.95).astype(float).where(rk.notna(), np.nan)
    return out.diff()


def f44_spca_150_comp_ultimate_cycle_topping_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    lc = _safe_log(close); lh = _safe_log(high)
    def _f(w):
        return _dominant_period_autocorr(w, max_lag=120, min_lag=4)
    dp = r.rolling(252, min_periods=84).apply(_f, raw=True)
    long = (dp > 100).astype(float)
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    rolled = ((ph.shift(5) > 0) & (ph < 0)).astype(float)
    x = _normalize_minmax_neg1_pos1(lc, 63, min_periods=21)
    fsh = _fisher_transform(x)
    fsh_hi = (fsh > 1.0).astype(float)
    rmax = lh.rolling(252, min_periods=84).max()
    at_high = (lh >= rmax - 0.05).astype(float)
    out = (long + rolled + fsh_hi + at_high).where(dp.notna() & ph.notna() & ph.shift(5).notna() & fsh.notna() & rmax.notna(), np.nan)
    return out.diff()


# ============================================================
#                         REGISTRY 076_150 (d1)
# ============================================================

SPECTRAL_CYCLE_ANALYSIS_D1_REGISTRY_076_150 = {
    "f44_spca_076_dpo_logclose_10d_d1": {"inputs": ["close"], "func": f44_spca_076_dpo_logclose_10d_d1},
    "f44_spca_077_dpo_logclose_21d_d1": {"inputs": ["close"], "func": f44_spca_077_dpo_logclose_21d_d1},
    "f44_spca_078_dpo_logclose_42d_d1": {"inputs": ["close"], "func": f44_spca_078_dpo_logclose_42d_d1},
    "f44_spca_079_dpo_logclose_63d_d1": {"inputs": ["close"], "func": f44_spca_079_dpo_logclose_63d_d1},
    "f44_spca_080_dpo_logclose_126d_d1": {"inputs": ["close"], "func": f44_spca_080_dpo_logclose_126d_d1},
    "f44_spca_081_dpo_logclose_252d_d1": {"inputs": ["close"], "func": f44_spca_081_dpo_logclose_252d_d1},
    "f44_spca_082_dpo_sign_63d_d1": {"inputs": ["close"], "func": f44_spca_082_dpo_sign_63d_d1},
    "f44_spca_083_dpo_sign_flip_count_63d_in_252d_d1": {"inputs": ["close"], "func": f44_spca_083_dpo_sign_flip_count_63d_in_252d_d1},
    "f44_spca_084_dpo_local_max_count_63d_in_252d_d1": {"inputs": ["close"], "func": f44_spca_084_dpo_local_max_count_63d_in_252d_d1},
    "f44_spca_085_dpo_amplitude_63d_in_252d_d1": {"inputs": ["close"], "func": f44_spca_085_dpo_amplitude_63d_in_252d_d1},
    "f44_spca_086_dpo_zscore_63d_in_252d_d1": {"inputs": ["close"], "func": f44_spca_086_dpo_zscore_63d_in_252d_d1},
    "f44_spca_087_dpo_pct_rank_63d_in_252d_d1": {"inputs": ["close"], "func": f44_spca_087_dpo_pct_rank_63d_in_252d_d1},
    "f44_spca_088_dpo_slope_21d_63d_d1": {"inputs": ["close"], "func": f44_spca_088_dpo_slope_21d_63d_d1},
    "f44_spca_089_dpo_sign_agree_21_vs_252_d1": {"inputs": ["close"], "func": f44_spca_089_dpo_sign_agree_21_vs_252_d1},
    "f44_spca_090_dpo_at_top_of_252d_range_63d_d1": {"inputs": ["close"], "func": f44_spca_090_dpo_at_top_of_252d_range_63d_d1},
    "f44_spca_091_spectral_entropy_logret_252d_d1": {"inputs": ["close"], "func": f44_spca_091_spectral_entropy_logret_252d_d1},
    "f44_spca_092_spectral_entropy_logret_504d_d1": {"inputs": ["close"], "func": f44_spca_092_spectral_entropy_logret_504d_d1},
    "f44_spca_093_spectral_entropy_norm_logret_252d_d1": {"inputs": ["close"], "func": f44_spca_093_spectral_entropy_norm_logret_252d_d1},
    "f44_spca_094_spectral_entropy_slope_63d_252d_d1": {"inputs": ["close"], "func": f44_spca_094_spectral_entropy_slope_63d_252d_d1},
    "f44_spca_095_spectral_entropy_zscore_252d_in_504d_d1": {"inputs": ["close"], "func": f44_spca_095_spectral_entropy_zscore_252d_in_504d_d1},
    "f44_spca_096_spectral_concentration_inv_norm_entropy_252d_d1": {"inputs": ["close"], "func": f44_spca_096_spectral_concentration_inv_norm_entropy_252d_d1},
    "f44_spca_097_psd_dominant_period_252d_d1": {"inputs": ["close"], "func": f44_spca_097_psd_dominant_period_252d_d1},
    "f44_spca_098_spectral_bandwidth_half_max_252d_d1": {"inputs": ["close"], "func": f44_spca_098_spectral_bandwidth_half_max_252d_d1},
    "f44_spca_099_spectral_skewness_252d_d1": {"inputs": ["close"], "func": f44_spca_099_spectral_skewness_252d_d1},
    "f44_spca_100_high_freq_power_share_252d_d1": {"inputs": ["close"], "func": f44_spca_100_high_freq_power_share_252d_d1},
    "f44_spca_101_low_freq_power_share_252d_d1": {"inputs": ["close"], "func": f44_spca_101_low_freq_power_share_252d_d1},
    "f44_spca_102_mid_freq_power_share_252d_d1": {"inputs": ["close"], "func": f44_spca_102_mid_freq_power_share_252d_d1},
    "f44_spca_103_high_over_low_freq_power_ratio_252d_d1": {"inputs": ["close"], "func": f44_spca_103_high_over_low_freq_power_ratio_252d_d1},
    "f44_spca_104_spectral_centroid_period_252d_d1": {"inputs": ["close"], "func": f44_spca_104_spectral_centroid_period_252d_d1},
    "f44_spca_105_spectral_flatness_252d_d1": {"inputs": ["close"], "func": f44_spca_105_spectral_flatness_252d_d1},
    "f44_spca_106_supersmoother_period_21d_logclose_d1": {"inputs": ["close"], "func": f44_spca_106_supersmoother_period_21d_logclose_d1},
    "f44_spca_107_supersmoother_period_63d_logclose_d1": {"inputs": ["close"], "func": f44_spca_107_supersmoother_period_63d_logclose_d1},
    "f44_spca_108_supersmoother_period_252d_logclose_d1": {"inputs": ["close"], "func": f44_spca_108_supersmoother_period_252d_logclose_d1},
    "f44_spca_109_highpass_logclose_minus_smoother_63d_d1": {"inputs": ["close"], "func": f44_spca_109_highpass_logclose_minus_smoother_63d_d1},
    "f44_spca_110_bandpass_smoother_21_minus_63_d1": {"inputs": ["close"], "func": f44_spca_110_bandpass_smoother_21_minus_63_d1},
    "f44_spca_111_ema_period_21_logclose_d1": {"inputs": ["close"], "func": f44_spca_111_ema_period_21_logclose_d1},
    "f44_spca_112_ema_period_63_logclose_d1": {"inputs": ["close"], "func": f44_spca_112_ema_period_63_logclose_d1},
    "f44_spca_113_ema_period_252_logclose_d1": {"inputs": ["close"], "func": f44_spca_113_ema_period_252_logclose_d1},
    "f44_spca_114_ema_diff_21_minus_63_d1": {"inputs": ["close"], "func": f44_spca_114_ema_diff_21_minus_63_d1},
    "f44_spca_115_ema_diff_63_minus_252_d1": {"inputs": ["close"], "func": f44_spca_115_ema_diff_63_minus_252_d1},
    "f44_spca_116_roofing_filter_proxy_logclose_d1": {"inputs": ["close"], "func": f44_spca_116_roofing_filter_proxy_logclose_d1},
    "f44_spca_117_hull_ma_period_21_logclose_d1": {"inputs": ["close"], "func": f44_spca_117_hull_ma_period_21_logclose_d1},
    "f44_spca_118_hull_ma_period_63_logclose_d1": {"inputs": ["close"], "func": f44_spca_118_hull_ma_period_63_logclose_d1},
    "f44_spca_119_ema_diff_21_minus_42_d1": {"inputs": ["close"], "func": f44_spca_119_ema_diff_21_minus_42_d1},
    "f44_spca_120_bandpass_amplitude_63d_rolling_max_d1": {"inputs": ["close"], "func": f44_spca_120_bandpass_amplitude_63d_rolling_max_d1},
    "f44_spca_121_dom_period_gt_100d_indicator_252d_d1": {"inputs": ["close"], "func": f44_spca_121_dom_period_gt_100d_indicator_252d_d1},
    "f44_spca_122_dom_period_lt_21d_indicator_252d_d1": {"inputs": ["close"], "func": f44_spca_122_dom_period_lt_21d_indicator_252d_d1},
    "f44_spca_123_dom_period_change_event_21d_252d_d1": {"inputs": ["close"], "func": f44_spca_123_dom_period_change_event_21d_252d_d1},
    "f44_spca_124_high_amplitude_regime_indicator_63d_in_252d_d1": {"inputs": ["close"], "func": f44_spca_124_high_amplitude_regime_indicator_63d_in_252d_d1},
    "f44_spca_125_low_amplitude_regime_indicator_63d_in_252d_d1": {"inputs": ["close"], "func": f44_spca_125_low_amplitude_regime_indicator_63d_in_252d_d1},
    "f44_spca_126_frac_high_amplitude_252d_63d_d1": {"inputs": ["close"], "func": f44_spca_126_frac_high_amplitude_252d_63d_d1},
    "f44_spca_127_current_high_amplitude_streak_63d_d1": {"inputs": ["close"], "func": f44_spca_127_current_high_amplitude_streak_63d_d1},
    "f44_spca_128_cycle_regime_change_count_252d_d1": {"inputs": ["close"], "func": f44_spca_128_cycle_regime_change_count_252d_d1},
    "f44_spca_129_spectral_entropy_above_80pct_504d_indicator_d1": {"inputs": ["close"], "func": f44_spca_129_spectral_entropy_above_80pct_504d_indicator_d1},
    "f44_spca_130_spectral_entropy_collapse_event_21d_252d_d1": {"inputs": ["close"], "func": f44_spca_130_spectral_entropy_collapse_event_21d_252d_d1},
    "f44_spca_131_spectral_flatness_change_21d_252d_d1": {"inputs": ["close"], "func": f44_spca_131_spectral_flatness_change_21d_252d_d1},
    "f44_spca_132_dom_period_slope_63d_252d_d1": {"inputs": ["close"], "func": f44_spca_132_dom_period_slope_63d_252d_d1},
    "f44_spca_133_dom_period_inv_std_252d_d1": {"inputs": ["close"], "func": f44_spca_133_dom_period_inv_std_252d_d1},
    "f44_spca_134_cycle_regime_class_entropy_252d_d1": {"inputs": ["close"], "func": f44_spca_134_cycle_regime_class_entropy_252d_d1},
    "f44_spca_135_amplitude_x_dom_period_63d_d1": {"inputs": ["close"], "func": f44_spca_135_amplitude_x_dom_period_63d_d1},
    "f44_spca_136_phase_top_high_amp_composite_63d_d1": {"inputs": ["close"], "func": f44_spca_136_phase_top_high_amp_composite_63d_d1},
    "f44_spca_137_phase_rollover_at_252d_high_composite_d1": {"inputs": ["high", "close"], "func": f44_spca_137_phase_rollover_at_252d_high_composite_d1},
    "f44_spca_138_spectral_entropy_collapse_at_high_composite_d1": {"inputs": ["high", "close"], "func": f44_spca_138_spectral_entropy_collapse_at_high_composite_d1},
    "f44_spca_139_long_cycle_dom_at_high_composite_d1": {"inputs": ["high", "close"], "func": f44_spca_139_long_cycle_dom_at_high_composite_d1},
    "f44_spca_140_dpo_top_fisher_above1_composite_63d_d1": {"inputs": ["close"], "func": f44_spca_140_dpo_top_fisher_above1_composite_63d_d1},
    "f44_spca_141_hf_power_surge_at_top_composite_d1": {"inputs": ["high", "close"], "func": f44_spca_141_hf_power_surge_at_top_composite_d1},
    "f44_spca_142_spec_concentration_with_rollover_composite_d1": {"inputs": ["close"], "func": f44_spca_142_spec_concentration_with_rollover_composite_d1},
    "f44_spca_143_supersmoother_63_slope_sign_flip_d1": {"inputs": ["close"], "func": f44_spca_143_supersmoother_63_slope_sign_flip_d1},
    "f44_spca_144_amp_regime_fisher_extreme_composite_63d_d1": {"inputs": ["close"], "func": f44_spca_144_amp_regime_fisher_extreme_composite_63d_d1},
    "f44_spca_145_short_cycle_at_high_composite_d1": {"inputs": ["high", "close"], "func": f44_spca_145_short_cycle_at_high_composite_d1},
    "f44_spca_146_phase_decoupling_relative_to_amp_63d_d1": {"inputs": ["close"], "func": f44_spca_146_phase_decoupling_relative_to_amp_63d_d1},
    "f44_spca_147_ema21_minus_ema63_sign_d1": {"inputs": ["close"], "func": f44_spca_147_ema21_minus_ema63_sign_d1},
    "f44_spca_148_ema21_ema63_cross_flip_event_d1": {"inputs": ["close"], "func": f44_spca_148_ema21_ema63_cross_flip_event_d1},
    "f44_spca_149_bandpass_amplitude_top5pct_252d_d1": {"inputs": ["close"], "func": f44_spca_149_bandpass_amplitude_top5pct_252d_d1},
    "f44_spca_150_comp_ultimate_cycle_topping_d1": {"inputs": ["high", "close"], "func": f44_spca_150_comp_ultimate_cycle_topping_d1},
}
