"""spectral_cycle_analysis d1 features 001-075 — Pipeline 1b-technical.

150 distinct hypotheses across this file and __d1__076_150.py. Each
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


def f44_spca_001_fisher_norm_logclose_21d_d1(close: pd.Series) -> pd.Series:
    x = _normalize_minmax_neg1_pos1(_safe_log(close), 21, min_periods=7)
    out = _fisher_transform(x)
    return out.diff()


def f44_spca_002_fisher_norm_logclose_63d_d1(close: pd.Series) -> pd.Series:
    x = _normalize_minmax_neg1_pos1(_safe_log(close), 63, min_periods=21)
    out = _fisher_transform(x)
    return out.diff()


def f44_spca_003_fisher_norm_logclose_252d_d1(close: pd.Series) -> pd.Series:
    x = _normalize_minmax_neg1_pos1(_safe_log(close), 252, min_periods=84)
    out = _fisher_transform(x)
    return out.diff()


def f44_spca_004_fisher_stoch_k_14d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmin = low.rolling(14, min_periods=5).min()
    rmax = high.rolling(14, min_periods=5).max()
    k = _safe_div(2.0 * (close - rmin), (rmax - rmin)) - 1.0
    out = _fisher_transform(k)
    return out.diff()


def f44_spca_005_fisher_stoch_k_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmin = low.rolling(63, min_periods=21).min()
    rmax = high.rolling(63, min_periods=21).max()
    k = _safe_div(2.0 * (close - rmin), (rmax - rmin)) - 1.0
    out = _fisher_transform(k)
    return out.diff()


def f44_spca_006_fisher_cci_proxy_21d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    m = tp.rolling(21, min_periods=7).mean()
    md = (tp - m).abs().rolling(21, min_periods=7).mean()
    cci = _safe_div(tp - m, 0.015 * md)
    out = _fisher_transform(cci.clip(-300.0, 300.0) / 300.0)
    return out.diff()


def f44_spca_007_fisher_cci_proxy_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    m = tp.rolling(63, min_periods=21).mean()
    md = (tp - m).abs().rolling(63, min_periods=21).mean()
    cci = _safe_div(tp - m, 0.015 * md)
    out = _fisher_transform(cci.clip(-300.0, 300.0) / 300.0)
    return out.diff()


def f44_spca_008_fisher_logret_volnorm_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    x = (_safe_div(r, sd)).clip(-3.0, 3.0) / 3.0
    out = _fisher_transform(x)
    return out.diff()


def f44_spca_009_fisher_rsi14_proxy_d1(close: pd.Series) -> pd.Series:
    d = close.diff()
    gain = d.clip(lower=0).rolling(14, min_periods=5).mean()
    loss = (-d.clip(upper=0)).rolling(14, min_periods=5).mean()
    rs = _safe_div(gain, loss.replace(0, np.nan))
    rsi = 100.0 - 100.0 / (1.0 + rs)
    out = _fisher_transform((rsi - 50.0) / 50.0)
    return out.diff()


def f44_spca_010_fisher_rsi63_proxy_d1(close: pd.Series) -> pd.Series:
    d = close.diff()
    gain = d.clip(lower=0).rolling(63, min_periods=21).mean()
    loss = (-d.clip(upper=0)).rolling(63, min_periods=21).mean()
    rs = _safe_div(gain, loss.replace(0, np.nan))
    rsi = 100.0 - 100.0 / (1.0 + rs)
    out = _fisher_transform((rsi - 50.0) / 50.0)
    return out.diff()


def f44_spca_011_fisher_macd_proxy_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    e1 = lc.ewm(span=12, adjust=False).mean()
    e2 = lc.ewm(span=26, adjust=False).mean()
    macd = e1 - e2
    sd = macd.rolling(63, min_periods=21).std()
    x = (_safe_div(macd, sd)).clip(-3.0, 3.0) / 3.0
    out = _fisher_transform(x)
    return out.diff()


def f44_spca_012_fisher_channel_pos_63d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rmin = low.rolling(63, min_periods=21).min()
    rmax = high.rolling(63, min_periods=21).max()
    p = _safe_div(2.0 * (close - rmin), rmax - rmin) - 1.0
    out = _fisher_transform(p)
    return out.diff()


def f44_spca_013_inv_fisher_norm_logclose_21d_d1(close: pd.Series) -> pd.Series:
    x = _normalize_minmax_neg1_pos1(_safe_log(close), 21, min_periods=7)
    out = (np.exp(2.0 * x) - 1.0) / (np.exp(2.0 * x) + 1.0)
    return out.diff()


def f44_spca_014_fisher_5d_mean_return_63d_norm_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    m5 = r.rolling(5, min_periods=2).mean()
    sd = m5.rolling(63, min_periods=21).std()
    x = (_safe_div(m5, sd)).clip(-3.0, 3.0) / 3.0
    out = _fisher_transform(x)
    return out.diff()


def f44_spca_015_fisher_range_pct_close_63d_norm_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    rp = _safe_div(high - low, close)
    z = _rolling_zscore(rp, 63, min_periods=21)
    x = z.clip(-3.0, 3.0) / 3.0
    out = _fisher_transform(x)
    return out.diff()


def f44_spca_016_dom_period_autocorr_logret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _dominant_period_autocorr(w, max_lag=100, min_lag=4)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_017_dom_period_autocorr_logret_504d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _dominant_period_autocorr(w, max_lag=120, min_lag=4)
    out = r.rolling(504, min_periods=168).apply(_f, raw=True)
    return out.diff()


def f44_spca_018_dom_period_autocorr_dt_logclose_252d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    sl = _rolling_slope(lc, 63, min_periods=21)
    d = lc.diff() - sl.shift(1) * 0.0  # subtract local trend
    d = lc - lc.rolling(63, min_periods=21).mean()
    def _f(w):
        return _dominant_period_autocorr(w, max_lag=100, min_lag=4)
    out = d.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_019_autocorr_logret_lag5_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _autocorr_at_lag(w, 5)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_020_autocorr_logret_lag21_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _autocorr_at_lag(w, 21)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_021_autocorr_logret_lag63_504d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _autocorr_at_lag(w, 63)
    out = r.rolling(504, min_periods=168).apply(_f, raw=True)
    return out.diff()


def f44_spca_022_ar1_logret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _autocorr_at_lag(w, 1)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_023_logret_sign_flip_density_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sg = np.sign(r)
    fl = (sg != sg.shift(1)).astype(float).where(sg.notna() & sg.shift(1).notna(), np.nan)
    out = fl.rolling(63, min_periods=21).mean()
    return out.diff()


def f44_spca_024_logret_sign_flip_density_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sg = np.sign(r)
    fl = (sg != sg.shift(1)).astype(float).where(sg.notna() & sg.shift(1).notna(), np.nan)
    out = fl.rolling(252, min_periods=84).mean()
    return out.diff()


def f44_spca_025_variance_ratio_5d_over_1d_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    r5 = _safe_log(close).diff(5)
    v1 = r.rolling(252, min_periods=84).var()
    v5 = r5.rolling(252, min_periods=84).var()
    out = _safe_div(v5, 5.0 * v1)
    return out.diff()


def f44_spca_026_variance_ratio_21d_over_1d_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    r21 = _safe_log(close).diff(21)
    v1 = r.rolling(252, min_periods=84).var()
    v21 = r21.rolling(252, min_periods=84).var()
    out = _safe_div(v21, 21.0 * v1)
    return out.diff()


def f44_spca_027_dom_period_vs_504d_median_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _dominant_period_autocorr(w, max_lag=100, min_lag=4)
    dp = r.rolling(252, min_periods=84).apply(_f, raw=True)
    out = _safe_div(dp, dp.rolling(504, min_periods=168).median())
    return out.diff()


def f44_spca_028_dom_period_std_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _dominant_period_autocorr(w, max_lag=100, min_lag=4)
    dp = r.rolling(252, min_periods=84).apply(_f, raw=True)
    out = dp.rolling(252, min_periods=84).std()
    return out.diff()


def f44_spca_029_hurst_exponent_logret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _hurst(w):
        valid = ~np.isnan(w)
        if valid.sum() < 40:
            return np.nan
        v = w[valid]
        lags = [2, 4, 8, 16, 32]
        tau = []
        for L in lags:
            if L >= v.size:
                continue
            d = v[L:] - v[:-L]
            s = float(np.std(d, ddof=1))
            if s > 0:
                tau.append((np.log(L), np.log(s)))
        if len(tau) < 3:
            return np.nan
        xs = np.array([t[0] for t in tau]); ys = np.array([t[1] for t in tau])
        xm = xs.mean(); ym = ys.mean()
        den = float(((xs - xm) ** 2).sum())
        if den <= 0:
            return np.nan
        return float(((xs - xm) * (ys - ym)).sum() / den)
    out = r.rolling(252, min_periods=84).apply(_hurst, raw=True)
    return out.diff()


def f44_spca_030_hurst_exponent_logret_504d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _hurst(w):
        valid = ~np.isnan(w)
        if valid.sum() < 80:
            return np.nan
        v = w[valid]
        lags = [2, 4, 8, 16, 32, 64]
        tau = []
        for L in lags:
            if L >= v.size:
                continue
            d = v[L:] - v[:-L]
            s = float(np.std(d, ddof=1))
            if s > 0:
                tau.append((np.log(L), np.log(s)))
        if len(tau) < 3:
            return np.nan
        xs = np.array([t[0] for t in tau]); ys = np.array([t[1] for t in tau])
        xm = xs.mean(); ym = ys.mean()
        den = float(((xs - xm) ** 2).sum())
        if den <= 0:
            return np.nan
        return float(((xs - xm) * (ys - ym)).sum() / den)
    out = r.rolling(504, min_periods=168).apply(_hurst, raw=True)
    return out.diff()


def f44_spca_031_dft_energy_period_5d_in_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _dft_energy_at_period(w, 5)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_032_dft_energy_period_10d_in_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _dft_energy_at_period(w, 10)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_033_dft_energy_period_21d_in_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _dft_energy_at_period(w, 21)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_034_dft_energy_period_42d_in_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _dft_energy_at_period(w, 42)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_035_dft_energy_period_63d_in_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _dft_energy_at_period(w, 63)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_036_dft_energy_period_126d_in_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _dft_energy_at_period(w, 126)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_037_dft_energy_period_252d_in_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _dft_energy_at_period(w, 252)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_038_dft_energy_ratio_5d_over_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f5(w):
        return _dft_energy_at_period(w, 5)
    def _f252(w):
        return _dft_energy_at_period(w, 252)
    e5 = r.rolling(252, min_periods=84).apply(_f5, raw=True)
    e252 = r.rolling(252, min_periods=84).apply(_f252, raw=True)
    out = _safe_div(e5, e252.replace(0, np.nan))
    return out.diff()


def f44_spca_039_dft_energy_ratio_21d_over_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f1(w):
        return _dft_energy_at_period(w, 21)
    def _f2(w):
        return _dft_energy_at_period(w, 63)
    e1 = r.rolling(252, min_periods=84).apply(_f1, raw=True)
    e2 = r.rolling(252, min_periods=84).apply(_f2, raw=True)
    out = _safe_div(e1, e2.replace(0, np.nan))
    return out.diff()


def f44_spca_040_dft_total_power_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        v = w[valid] if not valid.all() else w
        v = v - v.mean()
        return float((v * v).sum())
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_041_dft_peak_period_252d_d1(close: pd.Series) -> pd.Series:
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
            if np.isnan(e):
                continue
            if e > best_e:
                best_e = e; best_p = p
        return float(best_p)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_042_dft_peak_energy_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        v = w[valid] if not valid.all() else w
        v = v - v.mean()
        best_e = -np.inf
        for p in range(4, 100):
            if p >= v.size:
                break
            e = _dft_energy_at_period(v, p)
            if np.isnan(e):
                continue
            if e > best_e:
                best_e = e
        return float(best_e) if best_e > -np.inf else np.nan
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_043_dft_peak_share_of_total_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 60:
            return np.nan
        v = w[valid] if not valid.all() else w
        v = v - v.mean()
        total = float((v * v).sum())
        if total <= 0:
            return np.nan
        best_e = -np.inf
        for p in range(4, 100):
            if p >= v.size:
                break
            e = _dft_energy_at_period(v, p)
            if np.isnan(e):
                continue
            if e > best_e:
                best_e = e
        if best_e < 0:
            return np.nan
        return float(best_e / total)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_044_dft_energy_period_252d_in_504d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    def _f(w):
        return _dft_energy_at_period(w, 252)
    out = r.rolling(504, min_periods=168).apply(_f, raw=True)
    return out.diff()


def f44_spca_045_dft_top3_period_concentration_252d_d1(close: pd.Series) -> pd.Series:
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
        if len(energies) < 3:
            return np.nan
        arr = np.array(energies)
        s = arr.sum()
        if s <= 0:
            return np.nan
        top3 = np.sort(arr)[-3:].sum()
        return float(top3 / s)
    out = r.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f44_spca_046_hilbert_phase_logret_21d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(21, min_periods=7).apply(_hilbert_phase_lastpt, raw=True)
    return out.diff()


def f44_spca_047_hilbert_phase_logret_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    return out.diff()


def f44_spca_048_hilbert_phase_logret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = r.rolling(252, min_periods=84).apply(_hilbert_phase_lastpt, raw=True)
    return out.diff()


def f44_spca_049_envelope_amplitude_21d_logclose_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    m = lc.rolling(21, min_periods=7).mean()
    d = lc - m
    out = d.abs().rolling(21, min_periods=7).max()
    return out.diff()


def f44_spca_050_envelope_amplitude_63d_logclose_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    m = lc.rolling(63, min_periods=21).mean()
    d = lc - m
    out = d.abs().rolling(63, min_periods=21).max()
    return out.diff()


def f44_spca_051_envelope_amplitude_252d_logclose_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    m = lc.rolling(252, min_periods=84).mean()
    d = lc - m
    out = d.abs().rolling(252, min_periods=84).max()
    return out.diff()


def f44_spca_052_hilbert_phase_delta_5d_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    out = ph - ph.shift(5)
    return out.diff()


def f44_spca_053_hilbert_phase_delta_21d_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    out = ph - ph.shift(21)
    return out.diff()


def f44_spca_054_hilbert_phase_flip_count_252d_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    sg = np.sign(ph)
    fl = (sg != sg.shift(1)).astype(float).where(sg.notna() & sg.shift(1).notna(), np.nan)
    out = fl.rolling(252, min_periods=84).sum()
    return out.diff()


def f44_spca_055_envelope_amplitude_zscore_63d_in_252d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    m = lc.rolling(63, min_periods=21).mean()
    d = lc - m
    amp = d.abs().rolling(63, min_periods=21).max()
    out = _rolling_zscore(amp, 252, min_periods=84)
    return out.diff()


def f44_spca_056_envelope_amplitude_pct_rank_63d_in_252d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    m = lc.rolling(63, min_periods=21).mean()
    amp = (lc - m).abs().rolling(63, min_periods=21).max()
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
    out = amp.rolling(252, min_periods=84).apply(_rk, raw=True)
    return out.diff()


def f44_spca_057_amplitude_mod_index_21_over_252_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    amp21 = (lc - lc.rolling(21, min_periods=7).mean()).abs().rolling(21, min_periods=7).max()
    amp252 = (lc - lc.rolling(252, min_periods=84).mean()).abs().rolling(252, min_periods=84).max()
    out = _safe_div(amp21, amp252)
    return out.diff()


def f44_spca_058_envelope_amplitude_slope_21d_63d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    amp = (lc - lc.rolling(63, min_periods=21).mean()).abs().rolling(63, min_periods=21).max()
    out = amp - amp.shift(21)
    return out.diff()


def f44_spca_059_phase_above_dt_mean_indicator_63d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    m = lc.rolling(63, min_periods=21).mean()
    out = (lc > m).astype(float).where(m.notna(), np.nan)
    return out.diff()


def f44_spca_060_frac_above_63d_mean_252d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    m = lc.rolling(63, min_periods=21).mean()
    above = (lc > m).astype(float).where(m.notna(), np.nan)
    out = above.rolling(252, min_periods=84).mean()
    return out.diff()


def f44_spca_061_hilbert_phase_mod_pi_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    out = ph - np.pi * np.floor(ph / np.pi)
    return out.diff()


def f44_spca_062_sin_hilbert_phase_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    out = np.sin(ph)
    return out.diff()


def f44_spca_063_cos_hilbert_phase_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    out = np.cos(ph)
    return out.diff()


def f44_spca_064_hilbert_phase_diff_21_vs_63_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    p21 = r.rolling(21, min_periods=7).apply(_hilbert_phase_lastpt, raw=True)
    p63 = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    out = p21 - p63
    return out.diff()


def f44_spca_065_hilbert_phase_entropy_252d_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    def _ent(w):
        v = w[~np.isnan(w)]
        if v.size < 10:
            return np.nan
        b, _ = np.histogram(v, bins=10, range=(-np.pi, np.pi))
        if b.sum() == 0:
            return np.nan
        p = b / b.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    out = ph.rolling(252, min_periods=84).apply(_ent, raw=True)
    return out.diff()


def f44_spca_066_bars_since_phase_near_pi_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    at_bot = (np.abs(ph - np.pi) < 0.3) | (np.abs(ph + np.pi) < 0.3)
    arr = at_bot.fillna(False).astype(bool).values
    n = arr.size
    out_arr = np.full(n, np.nan)
    last = -1
    for i in range(n):
        if arr[i]:
            last = i
        if last >= 0:
            out_arr[i] = float(i - last)
    out = pd.Series(out_arr, index=ph.index)
    return out.diff()


def f44_spca_067_bars_since_phase_near_0_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    at_top = np.abs(ph) < 0.3
    arr = at_top.fillna(False).astype(bool).values
    n = arr.size
    out_arr = np.full(n, np.nan)
    last = -1
    for i in range(n):
        if arr[i]:
            last = i
        if last >= 0:
            out_arr[i] = float(i - last)
    out = pd.Series(out_arr, index=ph.index)
    return out.diff()


def f44_spca_068_hilbert_angular_velocity_5d_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    out = (ph - ph.shift(5)) / 5.0
    return out.diff()


def f44_spca_069_hilbert_phase_coherence_lag5_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    out = np.cos(ph - ph.shift(5))
    return out.diff()


def f44_spca_070_hilbert_phase_coherence_lag21_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    out = np.cos(ph - ph.shift(21))
    return out.diff()


def f44_spca_071_hilbert_phase_mean_21d_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    out = ph.rolling(21, min_periods=7).mean()
    return out.diff()


def f44_spca_072_hilbert_phase_var_252d_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    out = ph.rolling(252, min_periods=84).var()
    return out.diff()


def f44_spca_073_hilbert_phase_slope_63d_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    out = _rolling_slope(ph, 63, min_periods=21)
    return out.diff()


def f44_spca_074_phase_wrap_count_252d_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    wrap = (ph.diff().abs() > np.pi).astype(float).where(ph.notna() & ph.shift(1).notna(), np.nan)
    out = wrap.rolling(252, min_periods=84).sum()
    return out.diff()


def f44_spca_075_inst_power_sinphase_x_amp_63d_d1(close: pd.Series) -> pd.Series:
    lc = _safe_log(close)
    r = lc.diff()
    ph = r.rolling(63, min_periods=21).apply(_hilbert_phase_lastpt, raw=True)
    amp = (lc - lc.rolling(63, min_periods=21).mean()).abs().rolling(63, min_periods=21).max()
    out = np.abs(np.sin(ph)) * amp
    return out.diff()


# ============================================================
#                         REGISTRY 001_075 (d1)
# ============================================================

SPECTRAL_CYCLE_ANALYSIS_D1_REGISTRY_001_075 = {
    "f44_spca_001_fisher_norm_logclose_21d_d1": {"inputs": ["close"], "func": f44_spca_001_fisher_norm_logclose_21d_d1},
    "f44_spca_002_fisher_norm_logclose_63d_d1": {"inputs": ["close"], "func": f44_spca_002_fisher_norm_logclose_63d_d1},
    "f44_spca_003_fisher_norm_logclose_252d_d1": {"inputs": ["close"], "func": f44_spca_003_fisher_norm_logclose_252d_d1},
    "f44_spca_004_fisher_stoch_k_14d_d1": {"inputs": ["high", "low", "close"], "func": f44_spca_004_fisher_stoch_k_14d_d1},
    "f44_spca_005_fisher_stoch_k_63d_d1": {"inputs": ["high", "low", "close"], "func": f44_spca_005_fisher_stoch_k_63d_d1},
    "f44_spca_006_fisher_cci_proxy_21d_d1": {"inputs": ["high", "low", "close"], "func": f44_spca_006_fisher_cci_proxy_21d_d1},
    "f44_spca_007_fisher_cci_proxy_63d_d1": {"inputs": ["high", "low", "close"], "func": f44_spca_007_fisher_cci_proxy_63d_d1},
    "f44_spca_008_fisher_logret_volnorm_63d_d1": {"inputs": ["close"], "func": f44_spca_008_fisher_logret_volnorm_63d_d1},
    "f44_spca_009_fisher_rsi14_proxy_d1": {"inputs": ["close"], "func": f44_spca_009_fisher_rsi14_proxy_d1},
    "f44_spca_010_fisher_rsi63_proxy_d1": {"inputs": ["close"], "func": f44_spca_010_fisher_rsi63_proxy_d1},
    "f44_spca_011_fisher_macd_proxy_d1": {"inputs": ["close"], "func": f44_spca_011_fisher_macd_proxy_d1},
    "f44_spca_012_fisher_channel_pos_63d_d1": {"inputs": ["high", "low", "close"], "func": f44_spca_012_fisher_channel_pos_63d_d1},
    "f44_spca_013_inv_fisher_norm_logclose_21d_d1": {"inputs": ["close"], "func": f44_spca_013_inv_fisher_norm_logclose_21d_d1},
    "f44_spca_014_fisher_5d_mean_return_63d_norm_d1": {"inputs": ["close"], "func": f44_spca_014_fisher_5d_mean_return_63d_norm_d1},
    "f44_spca_015_fisher_range_pct_close_63d_norm_d1": {"inputs": ["high", "low", "close"], "func": f44_spca_015_fisher_range_pct_close_63d_norm_d1},
    "f44_spca_016_dom_period_autocorr_logret_252d_d1": {"inputs": ["close"], "func": f44_spca_016_dom_period_autocorr_logret_252d_d1},
    "f44_spca_017_dom_period_autocorr_logret_504d_d1": {"inputs": ["close"], "func": f44_spca_017_dom_period_autocorr_logret_504d_d1},
    "f44_spca_018_dom_period_autocorr_dt_logclose_252d_d1": {"inputs": ["close"], "func": f44_spca_018_dom_period_autocorr_dt_logclose_252d_d1},
    "f44_spca_019_autocorr_logret_lag5_252d_d1": {"inputs": ["close"], "func": f44_spca_019_autocorr_logret_lag5_252d_d1},
    "f44_spca_020_autocorr_logret_lag21_252d_d1": {"inputs": ["close"], "func": f44_spca_020_autocorr_logret_lag21_252d_d1},
    "f44_spca_021_autocorr_logret_lag63_504d_d1": {"inputs": ["close"], "func": f44_spca_021_autocorr_logret_lag63_504d_d1},
    "f44_spca_022_ar1_logret_252d_d1": {"inputs": ["close"], "func": f44_spca_022_ar1_logret_252d_d1},
    "f44_spca_023_logret_sign_flip_density_63d_d1": {"inputs": ["close"], "func": f44_spca_023_logret_sign_flip_density_63d_d1},
    "f44_spca_024_logret_sign_flip_density_252d_d1": {"inputs": ["close"], "func": f44_spca_024_logret_sign_flip_density_252d_d1},
    "f44_spca_025_variance_ratio_5d_over_1d_252d_d1": {"inputs": ["close"], "func": f44_spca_025_variance_ratio_5d_over_1d_252d_d1},
    "f44_spca_026_variance_ratio_21d_over_1d_252d_d1": {"inputs": ["close"], "func": f44_spca_026_variance_ratio_21d_over_1d_252d_d1},
    "f44_spca_027_dom_period_vs_504d_median_d1": {"inputs": ["close"], "func": f44_spca_027_dom_period_vs_504d_median_d1},
    "f44_spca_028_dom_period_std_252d_d1": {"inputs": ["close"], "func": f44_spca_028_dom_period_std_252d_d1},
    "f44_spca_029_hurst_exponent_logret_252d_d1": {"inputs": ["close"], "func": f44_spca_029_hurst_exponent_logret_252d_d1},
    "f44_spca_030_hurst_exponent_logret_504d_d1": {"inputs": ["close"], "func": f44_spca_030_hurst_exponent_logret_504d_d1},
    "f44_spca_031_dft_energy_period_5d_in_252d_d1": {"inputs": ["close"], "func": f44_spca_031_dft_energy_period_5d_in_252d_d1},
    "f44_spca_032_dft_energy_period_10d_in_252d_d1": {"inputs": ["close"], "func": f44_spca_032_dft_energy_period_10d_in_252d_d1},
    "f44_spca_033_dft_energy_period_21d_in_252d_d1": {"inputs": ["close"], "func": f44_spca_033_dft_energy_period_21d_in_252d_d1},
    "f44_spca_034_dft_energy_period_42d_in_252d_d1": {"inputs": ["close"], "func": f44_spca_034_dft_energy_period_42d_in_252d_d1},
    "f44_spca_035_dft_energy_period_63d_in_252d_d1": {"inputs": ["close"], "func": f44_spca_035_dft_energy_period_63d_in_252d_d1},
    "f44_spca_036_dft_energy_period_126d_in_252d_d1": {"inputs": ["close"], "func": f44_spca_036_dft_energy_period_126d_in_252d_d1},
    "f44_spca_037_dft_energy_period_252d_in_252d_d1": {"inputs": ["close"], "func": f44_spca_037_dft_energy_period_252d_in_252d_d1},
    "f44_spca_038_dft_energy_ratio_5d_over_252d_d1": {"inputs": ["close"], "func": f44_spca_038_dft_energy_ratio_5d_over_252d_d1},
    "f44_spca_039_dft_energy_ratio_21d_over_63d_d1": {"inputs": ["close"], "func": f44_spca_039_dft_energy_ratio_21d_over_63d_d1},
    "f44_spca_040_dft_total_power_252d_d1": {"inputs": ["close"], "func": f44_spca_040_dft_total_power_252d_d1},
    "f44_spca_041_dft_peak_period_252d_d1": {"inputs": ["close"], "func": f44_spca_041_dft_peak_period_252d_d1},
    "f44_spca_042_dft_peak_energy_252d_d1": {"inputs": ["close"], "func": f44_spca_042_dft_peak_energy_252d_d1},
    "f44_spca_043_dft_peak_share_of_total_252d_d1": {"inputs": ["close"], "func": f44_spca_043_dft_peak_share_of_total_252d_d1},
    "f44_spca_044_dft_energy_period_252d_in_504d_d1": {"inputs": ["close"], "func": f44_spca_044_dft_energy_period_252d_in_504d_d1},
    "f44_spca_045_dft_top3_period_concentration_252d_d1": {"inputs": ["close"], "func": f44_spca_045_dft_top3_period_concentration_252d_d1},
    "f44_spca_046_hilbert_phase_logret_21d_d1": {"inputs": ["close"], "func": f44_spca_046_hilbert_phase_logret_21d_d1},
    "f44_spca_047_hilbert_phase_logret_63d_d1": {"inputs": ["close"], "func": f44_spca_047_hilbert_phase_logret_63d_d1},
    "f44_spca_048_hilbert_phase_logret_252d_d1": {"inputs": ["close"], "func": f44_spca_048_hilbert_phase_logret_252d_d1},
    "f44_spca_049_envelope_amplitude_21d_logclose_d1": {"inputs": ["close"], "func": f44_spca_049_envelope_amplitude_21d_logclose_d1},
    "f44_spca_050_envelope_amplitude_63d_logclose_d1": {"inputs": ["close"], "func": f44_spca_050_envelope_amplitude_63d_logclose_d1},
    "f44_spca_051_envelope_amplitude_252d_logclose_d1": {"inputs": ["close"], "func": f44_spca_051_envelope_amplitude_252d_logclose_d1},
    "f44_spca_052_hilbert_phase_delta_5d_63d_d1": {"inputs": ["close"], "func": f44_spca_052_hilbert_phase_delta_5d_63d_d1},
    "f44_spca_053_hilbert_phase_delta_21d_63d_d1": {"inputs": ["close"], "func": f44_spca_053_hilbert_phase_delta_21d_63d_d1},
    "f44_spca_054_hilbert_phase_flip_count_252d_63d_d1": {"inputs": ["close"], "func": f44_spca_054_hilbert_phase_flip_count_252d_63d_d1},
    "f44_spca_055_envelope_amplitude_zscore_63d_in_252d_d1": {"inputs": ["close"], "func": f44_spca_055_envelope_amplitude_zscore_63d_in_252d_d1},
    "f44_spca_056_envelope_amplitude_pct_rank_63d_in_252d_d1": {"inputs": ["close"], "func": f44_spca_056_envelope_amplitude_pct_rank_63d_in_252d_d1},
    "f44_spca_057_amplitude_mod_index_21_over_252_d1": {"inputs": ["close"], "func": f44_spca_057_amplitude_mod_index_21_over_252_d1},
    "f44_spca_058_envelope_amplitude_slope_21d_63d_d1": {"inputs": ["close"], "func": f44_spca_058_envelope_amplitude_slope_21d_63d_d1},
    "f44_spca_059_phase_above_dt_mean_indicator_63d_d1": {"inputs": ["close"], "func": f44_spca_059_phase_above_dt_mean_indicator_63d_d1},
    "f44_spca_060_frac_above_63d_mean_252d_d1": {"inputs": ["close"], "func": f44_spca_060_frac_above_63d_mean_252d_d1},
    "f44_spca_061_hilbert_phase_mod_pi_63d_d1": {"inputs": ["close"], "func": f44_spca_061_hilbert_phase_mod_pi_63d_d1},
    "f44_spca_062_sin_hilbert_phase_63d_d1": {"inputs": ["close"], "func": f44_spca_062_sin_hilbert_phase_63d_d1},
    "f44_spca_063_cos_hilbert_phase_63d_d1": {"inputs": ["close"], "func": f44_spca_063_cos_hilbert_phase_63d_d1},
    "f44_spca_064_hilbert_phase_diff_21_vs_63_d1": {"inputs": ["close"], "func": f44_spca_064_hilbert_phase_diff_21_vs_63_d1},
    "f44_spca_065_hilbert_phase_entropy_252d_63d_d1": {"inputs": ["close"], "func": f44_spca_065_hilbert_phase_entropy_252d_63d_d1},
    "f44_spca_066_bars_since_phase_near_pi_63d_d1": {"inputs": ["close"], "func": f44_spca_066_bars_since_phase_near_pi_63d_d1},
    "f44_spca_067_bars_since_phase_near_0_63d_d1": {"inputs": ["close"], "func": f44_spca_067_bars_since_phase_near_0_63d_d1},
    "f44_spca_068_hilbert_angular_velocity_5d_63d_d1": {"inputs": ["close"], "func": f44_spca_068_hilbert_angular_velocity_5d_63d_d1},
    "f44_spca_069_hilbert_phase_coherence_lag5_63d_d1": {"inputs": ["close"], "func": f44_spca_069_hilbert_phase_coherence_lag5_63d_d1},
    "f44_spca_070_hilbert_phase_coherence_lag21_63d_d1": {"inputs": ["close"], "func": f44_spca_070_hilbert_phase_coherence_lag21_63d_d1},
    "f44_spca_071_hilbert_phase_mean_21d_63d_d1": {"inputs": ["close"], "func": f44_spca_071_hilbert_phase_mean_21d_63d_d1},
    "f44_spca_072_hilbert_phase_var_252d_63d_d1": {"inputs": ["close"], "func": f44_spca_072_hilbert_phase_var_252d_63d_d1},
    "f44_spca_073_hilbert_phase_slope_63d_63d_d1": {"inputs": ["close"], "func": f44_spca_073_hilbert_phase_slope_63d_63d_d1},
    "f44_spca_074_phase_wrap_count_252d_63d_d1": {"inputs": ["close"], "func": f44_spca_074_phase_wrap_count_252d_63d_d1},
    "f44_spca_075_inst_power_sinphase_x_amp_63d_d1": {"inputs": ["close"], "func": f44_spca_075_inst_power_sinphase_x_amp_63d_d1},
}
