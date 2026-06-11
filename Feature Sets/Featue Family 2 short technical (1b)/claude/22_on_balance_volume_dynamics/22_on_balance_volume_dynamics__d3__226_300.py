"""on_balance_volume_dynamics d3 features 226-300 — Pipeline 1b-technical (extension).

Continuation of the gap-fill extension. New buckets:
- VPT (Price Volume Trend) — distinct from OBV (uses pct_change weighting vs sign)
- Second-order OBV divergences (divergence on divergence — OBV-RSI divergence with price-RSI)
- OBV wavelet / multi-resolution decomposition
- OBV mutual information with future returns (lag-safe)
- OBV-based regime-switching and persistence
- Composite OBV-distribution-detection scores

CAREFUL — sibling family 23 (accumulation_distribution_line) owns CMF, MFI, KVO, AD, Force.
This file's PVT uses pct_change * volume cumulative (Granville's PVT, distinct primitive).

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


# ---------------------------- OBV primitives ----------------------------

def _obv(close: pd.Series, volume: pd.Series) -> pd.Series:
    sgn = np.sign(close.diff()).fillna(0.0)
    return (sgn * volume).cumsum()


def _pvt(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price Volume Trend (Granville): cumulative sum of (pct_change × volume). Distinct from OBV."""
    return (close.pct_change().fillna(0.0) * volume).cumsum()


# ---------------------------- family helpers ----------------------------

def _rolling_pct_rank(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _rk(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return s.rolling(window, min_periods=min_periods).apply(_rk, raw=True)


def _rolling_quantile(s, window, q, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).quantile(q)


def _consecutive_true_streak(b: pd.Series) -> pd.Series:
    grp = (~b.fillna(False)).cumsum()
    return b.fillna(False).astype(int).groupby(grp).cumsum()


def _rsi(s: pd.Series, n: int = 14) -> pd.Series:
    d = s.diff()
    g = d.clip(lower=0.0)
    l = (-d).clip(lower=0.0)
    ag = g.ewm(alpha=1.0 / n, min_periods=n, adjust=False).mean()
    al = l.ewm(alpha=1.0 / n, min_periods=n, adjust=False).mean()
    return 100.0 * _safe_div(ag, ag + al)


def _mutual_info_binned(x, y, bins=8):
    mask = (~np.isnan(x)) & (~np.isnan(y))
    if mask.sum() < 4 * bins:
        return np.nan
    x = x[mask]; y = y[mask]
    if x.size == 0 or x.max() == x.min() or y.max() == y.min():
        return np.nan
    xe = np.linspace(x.min(), x.max(), bins + 1)
    ye = np.linspace(y.min(), y.max(), bins + 1)
    hxy, _, _ = np.histogram2d(x, y, bins=[xe, ye])
    pxy = hxy / hxy.sum()
    px = pxy.sum(axis=1)
    py = pxy.sum(axis=0)
    def H(p):
        p = p[p > 0]
        return float(-(p * np.log(p)).sum()) if p.size > 0 else 0.0
    return float(H(px) + H(py) - H(pxy.ravel()))


# ============================================================
# Bucket V — PVT cumulative (distinct from OBV) (226-235)
# ============================================================

def f22_obvd_226_pvt_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope(63d) of PVT (Price Volume Trend) — pct-change-weighted cumulative-flow trend."""
    return _rolling_slope(_pvt(close, volume), QDAYS)


def f22_obvd_227_pvt_slope_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope(252d) of PVT."""
    return _rolling_slope(_pvt(close, volume), YDAYS)


def f22_obvd_228_pvt_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of PVT level."""
    return _rolling_zscore(_pvt(close, volume), YDAYS)


def f22_obvd_229_pvt_minus_price_slope_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """PVT slope(252d) minus log-price slope(252d) — PVT-price divergence."""
    return _rolling_slope(_pvt(close, volume), YDAYS) - _rolling_slope(_safe_log(close), YDAYS)


def f22_obvd_230_pvt_minus_obv_slope_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """PVT slope(252d) minus OBV slope(252d) — pct-weighted vs sign-weighted cumulative flow divergence."""
    return _rolling_slope(_pvt(close, volume), YDAYS) - _rolling_slope(_obv(close, volume), YDAYS)


def f22_obvd_231_pvt_drawdown_from_max_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """PVT minus 252d trailing max — flow-trend drawdown."""
    pvt = _pvt(close, volume)
    return pvt - pvt.rolling(YDAYS, min_periods=QDAYS).max()


def f22_obvd_232_pvt_below_max_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive-bar streak with PVT below trailing 252d max."""
    pvt = _pvt(close, volume)
    rmax = pvt.rolling(YDAYS, min_periods=QDAYS).max()
    return _consecutive_true_streak(pvt < rmax).astype(float)


def f22_obvd_233_pvt_age_of_max_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since 252d-trailing PVT max."""
    def _a(w):
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        idx = int(np.argmax(w))
        return float(len(w) - 1 - idx)
    return _pvt(close, volume).rolling(YDAYS, min_periods=QDAYS).apply(_a, raw=True)


def f22_obvd_234_pvt_minus_ema63_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of (PVT - EMA63(PVT)) — PVT position relative to its quarterly trend."""
    pvt = _pvt(close, volume)
    return _rolling_zscore(pvt - pvt.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean(), YDAYS)


def f22_obvd_235_pvt_diff_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of daily PVT change (pct_change × volume)."""
    return _rolling_zscore(_pvt(close, volume).diff(), YDAYS)


# ============================================================
# Bucket W — Second-order OBV divergences (236-245)
# ============================================================

def f22_obvd_236_obv_rsi_vs_price_rsi_diff_14d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """RSI(14, OBV) - RSI(14, close) — divergence at oscillator level."""
    obv = _obv(close, volume)
    return _rsi(obv, 14) - _rsi(close, 14)


def f22_obvd_237_obv_rsi_vs_price_rsi_diff_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """RSI(21, OBV) - RSI(21, close) — divergence at 21d horizon."""
    obv = _obv(close, volume)
    return _rsi(obv, MDAYS) - _rsi(close, MDAYS)


def f22_obvd_238_obv_rsi_below_50_with_price_rsi_above_70_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when RSI(OBV)<50 but RSI(close)>70 — classic bearish divergence with extreme price."""
    obv = _obv(close, volume)
    return ((_rsi(obv, 14) < 50) & (_rsi(close, 14) > 70)).astype(float)


def f22_obvd_239_obv_rsi_below_50_price_rsi_above_70_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of OBV-RSI/price-RSI strong-divergence events."""
    obv = _obv(close, volume)
    flag = ((_rsi(obv, 14) < 50) & (_rsi(close, 14) > 70)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_240_obv_macd_hist_minus_price_macd_hist(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV MACD histogram minus close MACD histogram — second-order momentum divergence."""
    obv = _obv(close, volume)
    obv_macd = obv.ewm(span=12, min_periods=6, adjust=False).mean() - obv.ewm(span=26, min_periods=12, adjust=False).mean()
    obv_sig = obv_macd.ewm(span=9, min_periods=4, adjust=False).mean()
    obv_hist = obv_macd - obv_sig
    p_macd = close.ewm(span=12, min_periods=6, adjust=False).mean() - close.ewm(span=26, min_periods=12, adjust=False).mean()
    p_sig = p_macd.ewm(span=9, min_periods=4, adjust=False).mean()
    p_hist = p_macd - p_sig
    return obv_hist - p_hist


def f22_obvd_241_obv_macd_negative_price_macd_positive_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where OBV-MACD < 0 AND close-MACD > 0 — top-of-range divergence."""
    obv = _obv(close, volume)
    obv_macd = obv.ewm(span=12, min_periods=6, adjust=False).mean() - obv.ewm(span=26, min_periods=12, adjust=False).mean()
    p_macd = close.ewm(span=12, min_periods=6, adjust=False).mean() - close.ewm(span=26, min_periods=12, adjust=False).mean()
    return ((obv_macd < 0) & (p_macd > 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_242_obv_stoch_minus_price_stoch_14d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Stoch %K(14, OBV) minus Stoch %K(14, close) — relative oscillator divergence."""
    obv = _obv(close, volume)
    o_rmax = obv.rolling(14, min_periods=5).max()
    o_rmin = obv.rolling(14, min_periods=5).min()
    o_k = 100.0 * _safe_div(obv - o_rmin, o_rmax - o_rmin)
    c_rmax = close.rolling(14, min_periods=5).max()
    c_rmin = close.rolling(14, min_periods=5).min()
    c_k = 100.0 * _safe_div(close - c_rmin, c_rmax - c_rmin)
    return o_k - c_k


def f22_obvd_243_obv_pct_rank_minus_close_pct_rank_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV pct rank(63d) minus close pct rank(63d). Negative = OBV underperforming on quarterly horizon."""
    obv = _obv(close, volume)
    return _rolling_pct_rank(obv, QDAYS) - _rolling_pct_rank(close, QDAYS)


def f22_obvd_244_obv_pct_rank_minus_close_pct_rank_504d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV pct rank(504d) minus close pct rank(504d). Long-horizon rank divergence."""
    obv = _obv(close, volume)
    return _rolling_pct_rank(obv, DDAYS_2Y) - _rolling_pct_rank(close, DDAYS_2Y)


def f22_obvd_245_double_divergence_score_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count over 252d of bars satisfying BOTH OBV-RSI/price-RSI<-10 AND OBV-pct-rank/close-pct-rank<-0.1."""
    obv = _obv(close, volume)
    rsi_d = _rsi(obv, 14) - _rsi(close, 14)
    rank_d = _rolling_pct_rank(obv, YDAYS) - _rolling_pct_rank(close, YDAYS)
    return ((rsi_d < -10.0) & (rank_d < -0.1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


# ============================================================
# Bucket X — OBV wavelet / multi-resolution (246-255)
# ============================================================

def f22_obvd_246_haar_wavelet_level1_obv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Haar level-1 detail std of OBV — high-freq flow-volatility."""
    obv = _obv(close, volume)
    detail = (obv - obv.shift(1)) / np.sqrt(2.0)
    return detail.rolling(YDAYS, min_periods=QDAYS).std()


def f22_obvd_247_haar_wavelet_level2_obv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Haar level-2 detail std of OBV (2-bar scale)."""
    obv = _obv(close, volume)
    s1 = (obv + obv.shift(1)) / np.sqrt(2.0)
    detail2 = (s1 - s1.shift(2)) / np.sqrt(2.0)
    return detail2.rolling(YDAYS, min_periods=QDAYS).std()


def f22_obvd_248_haar_wavelet_level3_obv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Haar level-3 detail std of OBV (4-bar scale)."""
    obv = _obv(close, volume)
    s1 = (obv + obv.shift(1)) / np.sqrt(2.0)
    s2 = (s1 + s1.shift(2)) / np.sqrt(2.0)
    detail3 = (s2 - s2.shift(4)) / np.sqrt(2.0)
    return detail3.rolling(YDAYS, min_periods=QDAYS).std()


def f22_obvd_249_obv_wavelet_low_to_high_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV wavelet level-3 std / level-1 std — > 1 means low-freq dominates flow."""
    obv = _obv(close, volume)
    d1 = (obv - obv.shift(1)) / np.sqrt(2.0)
    s1 = (obv + obv.shift(1)) / np.sqrt(2.0)
    s2 = (s1 + s1.shift(2)) / np.sqrt(2.0)
    d3 = (s2 - s2.shift(4)) / np.sqrt(2.0)
    return _safe_div(d3.rolling(YDAYS, min_periods=QDAYS).std(), d1.rolling(YDAYS, min_periods=QDAYS).std())


def f22_obvd_250_obv_ema_diff_5_21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EMA5(OBV) minus EMA21(OBV) — very-short vs short flow regime contrast."""
    obv = _obv(close, volume)
    return obv.ewm(span=5, min_periods=2, adjust=False).mean() - obv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()


def f22_obvd_251_obv_multi_horizon_zscore_aggregate(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(z(OBV, 21) + z(OBV, 63) + z(OBV, 252)) / 3 — aggregate multi-horizon OBV z."""
    obv = _obv(close, volume)
    return (_rolling_zscore(obv, MDAYS) + _rolling_zscore(obv, QDAYS) + _rolling_zscore(obv, YDAYS)) / 3.0


def f22_obvd_252_obv_multi_horizon_zscore_dispersion(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Std across (z(OBV,21), z(OBV,63), z(OBV,252)) — multi-horizon disagreement."""
    obv = _obv(close, volume)
    z21 = _rolling_zscore(obv, MDAYS); z63 = _rolling_zscore(obv, QDAYS); z252 = _rolling_zscore(obv, YDAYS)
    return pd.concat([z21, z63, z252], axis=1).std(axis=1)


def f22_obvd_253_obv_smooth_minus_raw_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score(252d) of (EMA21(OBV) - OBV) — distance of OBV from its smoothed trend."""
    obv = _obv(close, volume)
    return _rolling_zscore(obv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean() - obv, YDAYS)


def f22_obvd_254_obv_hp_filter_residual_std_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """HP-style: 252d std of (OBV - EMA126(OBV)) — residual flow noise."""
    obv = _obv(close, volume)
    trend = obv.ewm(span=QDAYS * 2, min_periods=QDAYS, adjust=False).mean()
    return (obv - trend).rolling(YDAYS, min_periods=QDAYS).std()


def f22_obvd_255_obv_decay_constant_emadiff_63_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """EMA63(OBV) minus EMA252(OBV) — quarterly vs annual flow drift."""
    obv = _obv(close, volume)
    return obv.ewm(span=QDAYS, min_periods=MDAYS, adjust=False).mean() - obv.ewm(span=YDAYS, min_periods=QDAYS, adjust=False).mean()


# ============================================================
# Bucket Y — OBV information-theoretic (256-265)
# ============================================================

def f22_obvd_256_mi_obvdiff_close_diff_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """MI between OBV-diff and close-diff over 63d — signed-flow coupling with price change."""
    obv = _obv(close, volume)
    d_obv = obv.diff(); d_c = close.diff()
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(QDAYS - 1, n):
        out.iloc[i] = _mutual_info_binned(d_obv.iloc[i - QDAYS + 1 : i + 1].values, d_c.iloc[i - QDAYS + 1 : i + 1].values, bins=6)
    return out


def f22_obvd_257_mi_obvdiff_close_diff_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """MI between OBV-diff and close-diff over 252d."""
    obv = _obv(close, volume)
    d_obv = obv.diff(); d_c = close.diff()
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _mutual_info_binned(d_obv.iloc[i - YDAYS + 1 : i + 1].values, d_c.iloc[i - YDAYS + 1 : i + 1].values, bins=8)
    return out


def f22_obvd_258_mi_obvdiff_lagged_close_diff_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """MI between OBV-diff(t-1) and close-diff(t) over 63d — lagged predictive coupling (PIT-safe)."""
    obv = _obv(close, volume)
    d_obv_lag = obv.diff().shift(1); d_c = close.diff()
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(QDAYS, n):
        out.iloc[i] = _mutual_info_binned(d_obv_lag.iloc[i - QDAYS + 1 : i + 1].values, d_c.iloc[i - QDAYS + 1 : i + 1].values, bins=6)
    return out


def f22_obvd_259_obv_kl_divergence_recent_vs_baseline_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """KL divergence between trailing 21d OBV-diff distribution and trailing 252d baseline."""
    obv = _obv(close, volume).diff()
    bins = 8
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        x252 = obv.iloc[i - YDAYS + 1 : i + 1].dropna().values
        x21 = obv.iloc[i - MDAYS + 1 : i + 1].dropna().values
        if x252.size < 50 or x21.size < 10 or x252.max() == x252.min():
            continue
        edges = np.linspace(x252.min(), x252.max(), bins + 1)
        q, _ = np.histogram(x252, bins=edges)
        q = q.astype(float) / max(q.sum(), 1)
        p, _ = np.histogram(x21, bins=edges)
        p = p.astype(float) / max(p.sum(), 1)
        q = np.where(q == 0, 1e-9, q)
        p_pos = p > 0
        out.iloc[i] = float((p[p_pos] * np.log(p[p_pos] / q[p_pos])).sum())
    return out


def f22_obvd_260_obv_shannon_entropy_diff_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Shannon entropy(252d) of binned OBV-diff."""
    obv = _obv(close, volume).diff()
    bins = 10
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        v = obv.iloc[i - YDAYS + 1 : i + 1].dropna().values
        if v.size < 50 or v.max() == v.min():
            continue
        edges = np.linspace(v.min(), v.max(), bins + 1)
        h, _ = np.histogram(v, bins=edges)
        p = h.astype(float) / max(h.sum(), 1)
        p = p[p > 0]
        out.iloc[i] = float(-(p * np.log(p)).sum())
    return out


def f22_obvd_261_obv_information_share_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """MI(OBV-diff, |close-diff|) / H(|close-diff|) over 252d — fraction of price-magnitude explained by OBV-flow."""
    obv = _obv(close, volume).diff()
    ac = close.diff().abs()
    bins = 8
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        x = obv.iloc[i - YDAYS + 1 : i + 1].values
        y = ac.iloc[i - YDAYS + 1 : i + 1].values
        mi = _mutual_info_binned(x, y, bins=bins)
        if np.isnan(mi):
            continue
        ymask = ~np.isnan(y)
        if ymask.sum() < 50:
            continue
        yv = y[ymask]
        if yv.max() == yv.min():
            continue
        ye = np.linspace(yv.min(), yv.max(), bins + 1)
        hy, _ = np.histogram(yv, bins=ye)
        py = hy.astype(float) / hy.sum()
        py = py[py > 0]
        Hy = float(-(py * np.log(py)).sum()) if py.size > 0 else np.nan
        if Hy and Hy > 0:
            out.iloc[i] = mi / Hy
    return out


def f22_obvd_262_conditional_entropy_obv_given_return_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """H(OBV-diff | binned close-return) over 252d."""
    obv_d = _obv(close, volume).diff()
    r = close.pct_change()
    bins = 6
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        x = r.iloc[i - YDAYS + 1 : i + 1].values
        y = obv_d.iloc[i - YDAYS + 1 : i + 1].values
        mask = (~np.isnan(x)) & (~np.isnan(y))
        if mask.sum() < 50:
            continue
        x = x[mask]; y = y[mask]
        if x.max() == x.min() or y.max() == y.min():
            continue
        xe = np.linspace(x.min(), x.max(), bins + 1)
        ye = np.linspace(y.min(), y.max(), bins + 1)
        hxy, _, _ = np.histogram2d(x, y, bins=[xe, ye])
        pxy = hxy / hxy.sum()
        px = pxy.sum(axis=1)
        nz = px > 0
        h_y_given_x = 0.0
        for j in np.where(nz)[0]:
            cond = pxy[j, :] / px[j]
            cond = cond[cond > 0]
            h_y_given_x += px[j] * float(-(cond * np.log(cond)).sum())
        out.iloc[i] = h_y_given_x
    return out


def f22_obvd_263_obv_signed_volume_perm_entropy_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Permutation entropy (order-3) on OBV-diff over 63d — ordinal-pattern diversity of signed flow."""
    obv_d = _obv(close, volume).diff()
    def _pe(w, order=3):
        v = w[~np.isnan(w)]
        if v.size < 4 * order:
            return np.nan
        m = v.size - order + 1
        patterns = {}
        for i in range(m):
            pat = tuple(np.argsort(v[i:i+order]))
            patterns[pat] = patterns.get(pat, 0) + 1
        total = sum(patterns.values())
        p = np.array(list(patterns.values()), dtype=float) / total
        return float(-(p * np.log(p)).sum())
    return obv_d.rolling(QDAYS, min_periods=MDAYS).apply(_pe, raw=True)


def f22_obvd_264_obv_signed_volume_perm_entropy_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Permutation entropy (order-3) on OBV-diff over 252d."""
    obv_d = _obv(close, volume).diff()
    def _pe(w, order=3):
        v = w[~np.isnan(w)]
        if v.size < 4 * order:
            return np.nan
        m = v.size - order + 1
        patterns = {}
        for i in range(m):
            pat = tuple(np.argsort(v[i:i+order]))
            patterns[pat] = patterns.get(pat, 0) + 1
        total = sum(patterns.values())
        p = np.array(list(patterns.values()), dtype=float) / total
        return float(-(p * np.log(p)).sum())
    return obv_d.rolling(YDAYS, min_periods=QDAYS).apply(_pe, raw=True)


def f22_obvd_265_obv_entropy_decay_63_minus_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Permutation entropy(63d) minus permutation entropy(252d) of OBV-diff."""
    obv_d = _obv(close, volume).diff()
    def _pe(w, order=3):
        v = w[~np.isnan(w)]
        if v.size < 4 * order:
            return np.nan
        m = v.size - order + 1
        patterns = {}
        for i in range(m):
            pat = tuple(np.argsort(v[i:i+order]))
            patterns[pat] = patterns.get(pat, 0) + 1
        total = sum(patterns.values())
        p = np.array(list(patterns.values()), dtype=float) / total
        return float(-(p * np.log(p)).sum())
    e63 = obv_d.rolling(QDAYS, min_periods=MDAYS).apply(_pe, raw=True)
    e252 = obv_d.rolling(YDAYS, min_periods=QDAYS).apply(_pe, raw=True)
    return e63 - e252


# ============================================================
# Bucket Z — OBV regime-switching / persistence (266-280)
# ============================================================

def f22_obvd_266_obv_regime_label_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """3-state regime label from z-score(OBV, 252d): -1 (low, z<-0.5), 0, +1 (high, z>0.5)."""
    z = _rolling_zscore(_obv(close, volume), YDAYS)
    return np.sign(z.where(z.abs() > 0.5, 0.0))


def f22_obvd_267_obv_regime_transitions_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of OBV regime transitions."""
    z = _rolling_zscore(_obv(close, volume), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return (label != label.shift(1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_268_obv_high_regime_dwell_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d fraction in high-OBV regime (z>0.5)."""
    z = _rolling_zscore(_obv(close, volume), YDAYS)
    return (z > 0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_269_obv_low_regime_dwell_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d fraction in low-OBV regime (z<-0.5)."""
    z = _rolling_zscore(_obv(close, volume), YDAYS)
    return (z < -0.5).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_270_obv_high_to_low_regime_transition_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of high→low regime transitions."""
    z = _rolling_zscore(_obv(close, volume), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    return ((label.shift(1) == 1) & (label == -1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_271_obv_regime_current_label(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current OBV regime label."""
    z = _rolling_zscore(_obv(close, volume), YDAYS)
    return np.sign(z.where(z.abs() > 0.5, 0.0))


def f22_obvd_272_obv_regime_current_age(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in current OBV regime."""
    z = _rolling_zscore(_obv(close, volume), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    diff = (label != label.shift(1))
    grp = diff.cumsum()
    return label.groupby(grp).cumcount().astype(float)


def f22_obvd_273_obv_diff_variance_ratio_q_2_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Lo-MacKinlay variance ratio (q=2) on OBV-diff over 252d. < 1 = mean-reverting flow."""
    obv = _obv(close, volume)
    d = obv.diff()
    def _vr(w, q=2):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        v_q = np.array([v[i] + v[i + 1] for i in range(v.size - 1)])
        var1 = np.var(v, ddof=1)
        varq = np.var(v_q, ddof=1)
        if var1 <= 0:
            return np.nan
        return float(varq / (q * var1))
    return d.rolling(YDAYS, min_periods=QDAYS).apply(_vr, raw=True)


def f22_obvd_274_obv_diff_vol_of_vol_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Std(63d) of rolling 21d-std of OBV-diff — vol-of-vol of signed flow."""
    obv = _obv(close, volume)
    s21 = obv.diff().rolling(MDAYS, min_periods=WDAYS).std()
    return s21.rolling(QDAYS, min_periods=MDAYS).std()


def f22_obvd_275_obv_diff_garch_persistence_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """GARCH-style proxy: lag-1 autocorr of squared OBV-diff over 252d."""
    obv = _obv(close, volume)
    sq = obv.diff() ** 2
    def _ac(w):
        v = w[~np.isnan(w)]
        if v.size < 30:
            return np.nan
        a = v[:-1] - v[:-1].mean()
        b = v[1:] - v[1:].mean()
        d = np.sqrt((a * a).sum() * (b * b).sum())
        if d <= 0:
            return np.nan
        return float((a * b).sum() / d)
    return sq.rolling(YDAYS, min_periods=QDAYS).apply(_ac, raw=True)


def f22_obvd_276_obv_diff_neg_to_pos_var_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of variance of negative OBV-diffs to variance of positive OBV-diffs over 252d — asymmetric flow vol."""
    obv = _obv(close, volume)
    d = obv.diff()
    var_neg = d.where(d < 0).rolling(YDAYS, min_periods=QDAYS).var()
    var_pos = d.where(d > 0).rolling(YDAYS, min_periods=QDAYS).var()
    return _safe_div(var_neg, var_pos + 1.0)


def f22_obvd_277_obv_diff_q90_q10_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """|q90(OBV-diff, 252d) / q10(OBV-diff, 252d)| — tail-ratio of flow."""
    obv = _obv(close, volume)
    d = obv.diff()
    q90 = _rolling_quantile(d, YDAYS, 0.90)
    q10 = _rolling_quantile(d, YDAYS, 0.10)
    return _safe_div(q90.abs(), q10.abs() + 1e-9)


def f22_obvd_278_obv_diff_neg_persistence_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where (OBV-diff < 0 AND OBV-diff(t-1) < 0 AND OBV-diff(t-2) < 0) — persistent negative flow."""
    obv = _obv(close, volume)
    d = obv.diff()
    persist = (d < 0) & (d.shift(1) < 0) & (d.shift(2) < 0)
    return persist.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_279_obv_oscillation_amplitude_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Std(63d) of (OBV - 21d-EMA(OBV)) — oscillation amplitude of OBV around short trend."""
    obv = _obv(close, volume)
    return (obv - obv.ewm(span=MDAYS, min_periods=WDAYS, adjust=False).mean()).rolling(QDAYS, min_periods=MDAYS).std()


def f22_obvd_280_obv_regime_entropy_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Shannon entropy of OBV regime-label distribution over 252d."""
    z = _rolling_zscore(_obv(close, volume), YDAYS)
    label = np.sign(z.where(z.abs() > 0.5, 0.0))
    def _ent(idx):
        v = label.iloc[idx].dropna().values
        if v.size < 30:
            return np.nan
        p = np.array([np.mean(v == -1), np.mean(v == 0), np.mean(v == 1)])
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        out.iloc[i] = _ent(range(i - YDAYS + 1, i + 1))
    return out


# ============================================================
# Bucket AA — Composite OBV-distribution-detection scores (281-300)
# ============================================================

def f22_obvd_281_obv_distribution_composite_score(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: {OBV slope 63<0} + {OBV pct rank vs close pct rank<-0.2} + {price new 252d-high and OBV below 252d max}."""
    obv = _obv(close, volume)
    s63 = _rolling_slope(obv, QDAYS)
    rank_diff = _rolling_pct_rank(obv, YDAYS) - _rolling_pct_rank(close, YDAYS)
    pmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    omax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    div = (high >= pmax) & (obv < omax)
    return ((s63 < 0).astype(float) + (rank_diff < -0.2).astype(float) + div.astype(float))


def f22_obvd_282_obv_distribution_score_streak(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive-bar streak where OBV distribution composite >= 2."""
    obv = _obv(close, volume)
    s63 = _rolling_slope(obv, QDAYS)
    rank_diff = _rolling_pct_rank(obv, YDAYS) - _rolling_pct_rank(close, YDAYS)
    pmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    omax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    div = (high >= pmax) & (obv < omax)
    score = ((s63 < 0).astype(float) + (rank_diff < -0.2).astype(float) + div.astype(float))
    return _consecutive_true_streak(score >= 2).astype(float)


def f22_obvd_283_obv_climax_then_distribution_count_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Climax-then-distribution: count of bars where (OBV z>3 in past 21d AND OBV distribution day today)."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv, YDAYS)
    climax_recent = (z > 3.0).astype(float).rolling(MDAYS, min_periods=WDAYS).max()
    pc = close.pct_change()
    obv_d = obv.diff()
    dd = (pc < -0.002) & (obv_d < 0)
    return ((climax_recent > 0) & dd).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_284_obv_failure_to_make_new_high_score(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d sum of (price at trailing 252d max AND OBV at less than 95% of its 252d max)."""
    obv = _obv(close, volume)
    pmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    omax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    flag = ((high >= pmax) & (obv < 0.95 * omax)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_285_obv_silent_distribution_score_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where (pct change > 0 AND OBV-diff < 0) — buying-with-selling-volume divergence."""
    pc = close.pct_change()
    obv_d = _obv(close, volume).diff()
    return ((pc > 0) & (obv_d < 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_286_obv_lower_high_with_higher_price_high_count_63d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 63d count of bars where high prints a new 21d high AND OBV is below its 21d-trailing OBV-max."""
    obv = _obv(close, volume)
    pmax21 = high.rolling(MDAYS, min_periods=WDAYS).max()
    omax21 = obv.rolling(MDAYS, min_periods=WDAYS).max()
    return ((high >= pmax21) & (obv < omax21)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f22_obvd_287_obv_negative_run_with_price_up_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where (OBV negative-diff streak >= 3) AND close > close.shift(3)."""
    obv = _obv(close, volume)
    d = obv.diff()
    neg_streak = _consecutive_true_streak(d < 0).astype(float)
    return ((neg_streak >= 3) & (close > close.shift(3))).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_288_obv_distribution_intensity_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d sum of (|OBV-diff z(252d)|) on bars satisfying distribution-day condition (close down AND OBV-diff<0)."""
    obv = _obv(close, volume)
    z = _rolling_zscore(obv.diff(), YDAYS)
    pc = close.pct_change()
    flag = (pc < -0.002) & (obv.diff() < 0)
    return z.abs().where(flag, 0.0).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_289_obv_post_peak_distribution_signature_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when OBV peak occurred in trailing 63d but OBV is now < 90% of that peak AND price is at new 252d max."""
    obv = _obv(close, volume)
    omax63 = obv.rolling(QDAYS, min_periods=MDAYS).max()
    cur_below_peak = obv < 0.9 * omax63
    pmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((high >= pmax) & cur_below_peak).astype(float)


def f22_obvd_290_obv_post_peak_distribution_count_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of post-peak distribution signature events."""
    obv = _obv(close, volume)
    omax63 = obv.rolling(QDAYS, min_periods=MDAYS).max()
    cur_below_peak = obv < 0.9 * omax63
    pmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((high >= pmax) & cur_below_peak).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_291_obv_compound_topping_score_252d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: sum of {OBV-rsi<50, price-rsi>70, OBV slope<0, price slope>0, OBV<252d-max, price=252d-max}."""
    obv = _obv(close, volume)
    o_rsi = _rsi(obv, 14)
    p_rsi = _rsi(close, 14)
    s_obv = _rolling_slope(obv, QDAYS)
    s_p = _rolling_slope(close, QDAYS)
    omax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    pmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return ((o_rsi < 50).astype(float)
            + (p_rsi > 70).astype(float)
            + (s_obv < 0).astype(float)
            + (s_p > 0).astype(float)
            + (obv < omax).astype(float)
            + (high >= pmax).astype(float))


def f22_obvd_292_obv_distribution_zone_dwell_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d fraction of bars in OBV high-regime then transitioning to low-regime — distribution zone."""
    z = _rolling_zscore(_obv(close, volume), YDAYS)
    high_to_neutral = ((z.shift(MDAYS) > 0.5) & (z < 0.5)).astype(float)
    return high_to_neutral.rolling(YDAYS, min_periods=QDAYS).mean()


def f22_obvd_293_obv_no_followthrough_after_jump_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count over 252d of (OBV-LM-jump > 3 AND OBV-diff < 0 within next 5 bars). PIT-safe via lag-back logic."""
    obv = _obv(close, volume)
    d = obv.diff()
    bp = (d.abs() * d.shift(1).abs()).rolling(MDAYS, min_periods=WDAYS).sum() * (np.pi / 2.0)
    sigma = (bp / MDAYS).pow(0.5)
    jstat = _safe_div(d.abs(), sigma)
    pos_jump = (jstat > 3.0) & (d > 0)
    # bars within 5 of a positive jump:
    recent_jump = pos_jump.shift(1).rolling(5, min_periods=1).max().fillna(0.0)
    failure = (recent_jump > 0) & (d < 0)
    return failure.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_294_obv_distribution_during_rally_indicator(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 when 21d close return > 5% AND 21d OBV-diff sum < 0 — rally on net selling flow."""
    obv = _obv(close, volume)
    r21 = (close / close.shift(MDAYS)) - 1.0
    obv_change = obv.diff().rolling(MDAYS, min_periods=WDAYS).sum()
    return ((r21 > 0.05) & (obv_change < 0)).astype(float)


def f22_obvd_295_obv_distribution_during_rally_count_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of rally-on-net-selling-flow bars."""
    obv = _obv(close, volume)
    r21 = (close / close.shift(MDAYS)) - 1.0
    obv_change = obv.diff().rolling(MDAYS, min_periods=WDAYS).sum()
    return ((r21 > 0.05) & (obv_change < 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_296_obv_corr_pct_change_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Pearson correlation between OBV-diff and close pct_change over 252d. Low or negative = decoupled."""
    return _obv(close, volume).diff().rolling(YDAYS, min_periods=QDAYS).corr(close.pct_change())


def f22_obvd_297_obv_rank_corr_close_5d_lead_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rank correlation between OBV(t) and close(t+5) — PIT-safe: use close at lag(-5)? No — use OBV at lag(+5) instead.

    Implementation: For each t, correlate OBV(t-5+i, i=0..N-1) with close(t+i, i=0..N-1). To be PIT-safe, compute
    rank correlation of OBV(t-5) and close(t) over trailing 252d — i.e., does past OBV predict current close-rank.
    """
    obv_lag5 = _obv(close, volume).shift(5)
    ra = obv_lag5.rolling(YDAYS, min_periods=QDAYS).rank()
    rc = close.rolling(YDAYS, min_periods=QDAYS).rank()
    return ra.rolling(YDAYS, min_periods=QDAYS).corr(rc)


def f22_obvd_298_obv_failure_to_pred_close_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d count of bars where OBV(t-5) was at a new 252d-high but close(t) is NOT — failed prediction."""
    obv_lag5 = _obv(close, volume).shift(5)
    om = obv_lag5.rolling(YDAYS, min_periods=QDAYS).max()
    cm = close.rolling(YDAYS, min_periods=QDAYS).max()
    flag = (obv_lag5 >= om) & (close < cm)
    return flag.astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f22_obvd_299_obv_information_share_in_top_decile_close_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Trailing 252d MI(OBV-diff, |close-diff|) computed only on bars where close pct-rank > 0.9 (top-decile-close)."""
    obv_d = _obv(close, volume).diff()
    ac = close.diff().abs()
    pr = _rolling_pct_rank(close, YDAYS)
    bins = 6
    out = pd.Series(np.nan, index=close.index, dtype=float)
    n = len(close)
    for i in range(YDAYS - 1, n):
        mask_top = (pr.iloc[i - YDAYS + 1 : i + 1] > 0.9)
        x = obv_d.iloc[i - YDAYS + 1 : i + 1].values
        y = ac.iloc[i - YDAYS + 1 : i + 1].values
        m = mask_top.values & (~np.isnan(x)) & (~np.isnan(y))
        if m.sum() < 4 * bins:
            continue
        x = x[m]; y = y[m]
        if x.max() == x.min() or y.max() == y.min():
            continue
        out.iloc[i] = _mutual_info_binned(x, y, bins=bins)
    return out


def f22_obvd_300_obv_master_distribution_intensity_score(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Master composite combining OBV-distribution score + OBV-MACD bear + post-peak signature + silent distribution."""
    obv = _obv(close, volume)
    s63 = _rolling_slope(obv, QDAYS)
    rank_diff = _rolling_pct_rank(obv, YDAYS) - _rolling_pct_rank(close, YDAYS)
    pmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    omax = obv.rolling(YDAYS, min_periods=QDAYS).max()
    div = (high >= pmax) & (obv < omax)
    obv_macd = obv.ewm(span=12, min_periods=6, adjust=False).mean() - obv.ewm(span=26, min_periods=12, adjust=False).mean()
    macd_bear = (obv_macd < 0).astype(float)
    omax63 = obv.rolling(QDAYS, min_periods=MDAYS).max()
    cur_below_peak = obv < 0.9 * omax63
    post_peak = ((high >= pmax) & cur_below_peak).astype(float)
    pc = close.pct_change()
    obv_d = obv.diff()
    silent_dist = ((pc > 0) & (obv_d < 0)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()
    return ((s63 < 0).astype(float)
            + (rank_diff < -0.2).astype(float)
            + div.astype(float)
            + macd_bear
            + 2.0 * post_peak
            + silent_dist / 10.0)


def f22_obvd_226_pvt_slope_63d_d3(close, volume):
    return f22_obvd_226_pvt_slope_63d(close, volume).diff().diff().diff()


def f22_obvd_227_pvt_slope_252d_d3(close, volume):
    return f22_obvd_227_pvt_slope_252d(close, volume).diff().diff().diff()


def f22_obvd_228_pvt_zscore_252d_d3(close, volume):
    return f22_obvd_228_pvt_zscore_252d(close, volume).diff().diff().diff()


def f22_obvd_229_pvt_minus_price_slope_252d_d3(close, volume):
    return f22_obvd_229_pvt_minus_price_slope_252d(close, volume).diff().diff().diff()


def f22_obvd_230_pvt_minus_obv_slope_252d_d3(close, volume):
    return f22_obvd_230_pvt_minus_obv_slope_252d(close, volume).diff().diff().diff()


def f22_obvd_231_pvt_drawdown_from_max_252d_d3(close, volume):
    return f22_obvd_231_pvt_drawdown_from_max_252d(close, volume).diff().diff().diff()


def f22_obvd_232_pvt_below_max_streak_d3(close, volume):
    return f22_obvd_232_pvt_below_max_streak(close, volume).diff().diff().diff()


def f22_obvd_233_pvt_age_of_max_252d_d3(close, volume):
    return f22_obvd_233_pvt_age_of_max_252d(close, volume).diff().diff().diff()


def f22_obvd_234_pvt_minus_ema63_zscore_252d_d3(close, volume):
    return f22_obvd_234_pvt_minus_ema63_zscore_252d(close, volume).diff().diff().diff()


def f22_obvd_235_pvt_diff_zscore_252d_d3(close, volume):
    return f22_obvd_235_pvt_diff_zscore_252d(close, volume).diff().diff().diff()


def f22_obvd_236_obv_rsi_vs_price_rsi_diff_14d_d3(close, volume):
    return f22_obvd_236_obv_rsi_vs_price_rsi_diff_14d(close, volume).diff().diff().diff()


def f22_obvd_237_obv_rsi_vs_price_rsi_diff_21d_d3(close, volume):
    return f22_obvd_237_obv_rsi_vs_price_rsi_diff_21d(close, volume).diff().diff().diff()


def f22_obvd_238_obv_rsi_below_50_with_price_rsi_above_70_indicator_d3(close, volume):
    return f22_obvd_238_obv_rsi_below_50_with_price_rsi_above_70_indicator(close, volume).diff().diff().diff()


def f22_obvd_239_obv_rsi_below_50_price_rsi_above_70_count_252d_d3(close, volume):
    return f22_obvd_239_obv_rsi_below_50_price_rsi_above_70_count_252d(close, volume).diff().diff().diff()


def f22_obvd_240_obv_macd_hist_minus_price_macd_hist_d3(close, volume):
    return f22_obvd_240_obv_macd_hist_minus_price_macd_hist(close, volume).diff().diff().diff()


def f22_obvd_241_obv_macd_negative_price_macd_positive_count_252d_d3(close, volume):
    return f22_obvd_241_obv_macd_negative_price_macd_positive_count_252d(close, volume).diff().diff().diff()


def f22_obvd_242_obv_stoch_minus_price_stoch_14d_d3(close, volume):
    return f22_obvd_242_obv_stoch_minus_price_stoch_14d(close, volume).diff().diff().diff()


def f22_obvd_243_obv_pct_rank_minus_close_pct_rank_63d_d3(close, volume):
    return f22_obvd_243_obv_pct_rank_minus_close_pct_rank_63d(close, volume).diff().diff().diff()


def f22_obvd_244_obv_pct_rank_minus_close_pct_rank_504d_d3(close, volume):
    return f22_obvd_244_obv_pct_rank_minus_close_pct_rank_504d(close, volume).diff().diff().diff()


def f22_obvd_245_double_divergence_score_252d_d3(close, volume):
    return f22_obvd_245_double_divergence_score_252d(close, volume).diff().diff().diff()


def f22_obvd_246_haar_wavelet_level1_obv_252d_d3(close, volume):
    return f22_obvd_246_haar_wavelet_level1_obv_252d(close, volume).diff().diff().diff()


def f22_obvd_247_haar_wavelet_level2_obv_252d_d3(close, volume):
    return f22_obvd_247_haar_wavelet_level2_obv_252d(close, volume).diff().diff().diff()


def f22_obvd_248_haar_wavelet_level3_obv_252d_d3(close, volume):
    return f22_obvd_248_haar_wavelet_level3_obv_252d(close, volume).diff().diff().diff()


def f22_obvd_249_obv_wavelet_low_to_high_ratio_252d_d3(close, volume):
    return f22_obvd_249_obv_wavelet_low_to_high_ratio_252d(close, volume).diff().diff().diff()


def f22_obvd_250_obv_ema_diff_5_21_d3(close, volume):
    return f22_obvd_250_obv_ema_diff_5_21(close, volume).diff().diff().diff()


def f22_obvd_251_obv_multi_horizon_zscore_aggregate_d3(close, volume):
    return f22_obvd_251_obv_multi_horizon_zscore_aggregate(close, volume).diff().diff().diff()


def f22_obvd_252_obv_multi_horizon_zscore_dispersion_d3(close, volume):
    return f22_obvd_252_obv_multi_horizon_zscore_dispersion(close, volume).diff().diff().diff()


def f22_obvd_253_obv_smooth_minus_raw_zscore_252d_d3(close, volume):
    return f22_obvd_253_obv_smooth_minus_raw_zscore_252d(close, volume).diff().diff().diff()


def f22_obvd_254_obv_hp_filter_residual_std_252d_d3(close, volume):
    return f22_obvd_254_obv_hp_filter_residual_std_252d(close, volume).diff().diff().diff()


def f22_obvd_255_obv_decay_constant_emadiff_63_252_d3(close, volume):
    return f22_obvd_255_obv_decay_constant_emadiff_63_252(close, volume).diff().diff().diff()


def f22_obvd_256_mi_obvdiff_close_diff_63d_d3(close, volume):
    return f22_obvd_256_mi_obvdiff_close_diff_63d(close, volume).diff().diff().diff()


def f22_obvd_257_mi_obvdiff_close_diff_252d_d3(close, volume):
    return f22_obvd_257_mi_obvdiff_close_diff_252d(close, volume).diff().diff().diff()


def f22_obvd_258_mi_obvdiff_lagged_close_diff_63d_d3(close, volume):
    return f22_obvd_258_mi_obvdiff_lagged_close_diff_63d(close, volume).diff().diff().diff()


def f22_obvd_259_obv_kl_divergence_recent_vs_baseline_252d_d3(close, volume):
    return f22_obvd_259_obv_kl_divergence_recent_vs_baseline_252d(close, volume).diff().diff().diff()


def f22_obvd_260_obv_shannon_entropy_diff_252d_d3(close, volume):
    return f22_obvd_260_obv_shannon_entropy_diff_252d(close, volume).diff().diff().diff()


def f22_obvd_261_obv_information_share_252d_d3(close, volume):
    return f22_obvd_261_obv_information_share_252d(close, volume).diff().diff().diff()


def f22_obvd_262_conditional_entropy_obv_given_return_252d_d3(close, volume):
    return f22_obvd_262_conditional_entropy_obv_given_return_252d(close, volume).diff().diff().diff()


def f22_obvd_263_obv_signed_volume_perm_entropy_63d_d3(close, volume):
    return f22_obvd_263_obv_signed_volume_perm_entropy_63d(close, volume).diff().diff().diff()


def f22_obvd_264_obv_signed_volume_perm_entropy_252d_d3(close, volume):
    return f22_obvd_264_obv_signed_volume_perm_entropy_252d(close, volume).diff().diff().diff()


def f22_obvd_265_obv_entropy_decay_63_minus_252_d3(close, volume):
    return f22_obvd_265_obv_entropy_decay_63_minus_252(close, volume).diff().diff().diff()


def f22_obvd_266_obv_regime_label_252d_d3(close, volume):
    return f22_obvd_266_obv_regime_label_252d(close, volume).diff().diff().diff()


def f22_obvd_267_obv_regime_transitions_count_252d_d3(close, volume):
    return f22_obvd_267_obv_regime_transitions_count_252d(close, volume).diff().diff().diff()


def f22_obvd_268_obv_high_regime_dwell_252d_d3(close, volume):
    return f22_obvd_268_obv_high_regime_dwell_252d(close, volume).diff().diff().diff()


def f22_obvd_269_obv_low_regime_dwell_252d_d3(close, volume):
    return f22_obvd_269_obv_low_regime_dwell_252d(close, volume).diff().diff().diff()


def f22_obvd_270_obv_high_to_low_regime_transition_count_252d_d3(close, volume):
    return f22_obvd_270_obv_high_to_low_regime_transition_count_252d(close, volume).diff().diff().diff()


def f22_obvd_271_obv_regime_current_label_d3(close, volume):
    return f22_obvd_271_obv_regime_current_label(close, volume).diff().diff().diff()


def f22_obvd_272_obv_regime_current_age_d3(close, volume):
    return f22_obvd_272_obv_regime_current_age(close, volume).diff().diff().diff()


def f22_obvd_273_obv_diff_variance_ratio_q_2_252d_d3(close, volume):
    return f22_obvd_273_obv_diff_variance_ratio_q_2_252d(close, volume).diff().diff().diff()


def f22_obvd_274_obv_diff_vol_of_vol_63d_d3(close, volume):
    return f22_obvd_274_obv_diff_vol_of_vol_63d(close, volume).diff().diff().diff()


def f22_obvd_275_obv_diff_garch_persistence_252d_d3(close, volume):
    return f22_obvd_275_obv_diff_garch_persistence_252d(close, volume).diff().diff().diff()


def f22_obvd_276_obv_diff_neg_to_pos_var_ratio_252d_d3(close, volume):
    return f22_obvd_276_obv_diff_neg_to_pos_var_ratio_252d(close, volume).diff().diff().diff()


def f22_obvd_277_obv_diff_q90_q10_ratio_252d_d3(close, volume):
    return f22_obvd_277_obv_diff_q90_q10_ratio_252d(close, volume).diff().diff().diff()


def f22_obvd_278_obv_diff_neg_persistence_count_252d_d3(close, volume):
    return f22_obvd_278_obv_diff_neg_persistence_count_252d(close, volume).diff().diff().diff()


def f22_obvd_279_obv_oscillation_amplitude_63d_d3(close, volume):
    return f22_obvd_279_obv_oscillation_amplitude_63d(close, volume).diff().diff().diff()


def f22_obvd_280_obv_regime_entropy_252d_d3(close, volume):
    return f22_obvd_280_obv_regime_entropy_252d(close, volume).diff().diff().diff()


def f22_obvd_281_obv_distribution_composite_score_d3(high, close, volume):
    return f22_obvd_281_obv_distribution_composite_score(high, close, volume).diff().diff().diff()


def f22_obvd_282_obv_distribution_score_streak_d3(high, close, volume):
    return f22_obvd_282_obv_distribution_score_streak(high, close, volume).diff().diff().diff()


def f22_obvd_283_obv_climax_then_distribution_count_252d_d3(high, close, volume):
    return f22_obvd_283_obv_climax_then_distribution_count_252d(high, close, volume).diff().diff().diff()


def f22_obvd_284_obv_failure_to_make_new_high_score_d3(high, close, volume):
    return f22_obvd_284_obv_failure_to_make_new_high_score(high, close, volume).diff().diff().diff()


def f22_obvd_285_obv_silent_distribution_score_252d_d3(close, volume):
    return f22_obvd_285_obv_silent_distribution_score_252d(close, volume).diff().diff().diff()


def f22_obvd_286_obv_lower_high_with_higher_price_high_count_63d_d3(high, close, volume):
    return f22_obvd_286_obv_lower_high_with_higher_price_high_count_63d(high, close, volume).diff().diff().diff()


def f22_obvd_287_obv_negative_run_with_price_up_count_252d_d3(close, volume):
    return f22_obvd_287_obv_negative_run_with_price_up_count_252d(close, volume).diff().diff().diff()


def f22_obvd_288_obv_distribution_intensity_252d_d3(high, close, volume):
    return f22_obvd_288_obv_distribution_intensity_252d(high, close, volume).diff().diff().diff()


def f22_obvd_289_obv_post_peak_distribution_signature_252d_d3(high, close, volume):
    return f22_obvd_289_obv_post_peak_distribution_signature_252d(high, close, volume).diff().diff().diff()


def f22_obvd_290_obv_post_peak_distribution_count_252d_d3(high, close, volume):
    return f22_obvd_290_obv_post_peak_distribution_count_252d(high, close, volume).diff().diff().diff()


def f22_obvd_291_obv_compound_topping_score_252d_d3(high, close, volume):
    return f22_obvd_291_obv_compound_topping_score_252d(high, close, volume).diff().diff().diff()


def f22_obvd_292_obv_distribution_zone_dwell_252d_d3(close, volume):
    return f22_obvd_292_obv_distribution_zone_dwell_252d(close, volume).diff().diff().diff()


def f22_obvd_293_obv_no_followthrough_after_jump_count_252d_d3(close, volume):
    return f22_obvd_293_obv_no_followthrough_after_jump_count_252d(close, volume).diff().diff().diff()


def f22_obvd_294_obv_distribution_during_rally_indicator_d3(close, volume):
    return f22_obvd_294_obv_distribution_during_rally_indicator(close, volume).diff().diff().diff()


def f22_obvd_295_obv_distribution_during_rally_count_252d_d3(close, volume):
    return f22_obvd_295_obv_distribution_during_rally_count_252d(close, volume).diff().diff().diff()


def f22_obvd_296_obv_corr_pct_change_252d_d3(close, volume):
    return f22_obvd_296_obv_corr_pct_change_252d(close, volume).diff().diff().diff()


def f22_obvd_297_obv_rank_corr_close_5d_lead_252d_d3(close, volume):
    return f22_obvd_297_obv_rank_corr_close_5d_lead_252d(close, volume).diff().diff().diff()


def f22_obvd_298_obv_failure_to_pred_close_252d_d3(close, volume):
    return f22_obvd_298_obv_failure_to_pred_close_252d(close, volume).diff().diff().diff()


def f22_obvd_299_obv_information_share_in_top_decile_close_252d_d3(close, volume):
    return f22_obvd_299_obv_information_share_in_top_decile_close_252d(close, volume).diff().diff().diff()


def f22_obvd_300_obv_master_distribution_intensity_score_d3(high, low, close, volume):
    return f22_obvd_300_obv_master_distribution_intensity_score(high, low, close, volume).diff().diff().diff()


# ============================================================
#                         REGISTRY 226-300
# ============================================================


ON_BALANCE_VOLUME_DYNAMICS_D3_REGISTRY_226_300 = {
    "f22_obvd_226_pvt_slope_63d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_226_pvt_slope_63d_d3},
    "f22_obvd_227_pvt_slope_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_227_pvt_slope_252d_d3},
    "f22_obvd_228_pvt_zscore_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_228_pvt_zscore_252d_d3},
    "f22_obvd_229_pvt_minus_price_slope_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_229_pvt_minus_price_slope_252d_d3},
    "f22_obvd_230_pvt_minus_obv_slope_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_230_pvt_minus_obv_slope_252d_d3},
    "f22_obvd_231_pvt_drawdown_from_max_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_231_pvt_drawdown_from_max_252d_d3},
    "f22_obvd_232_pvt_below_max_streak_d3": {"inputs": ["close", "volume"], "func": f22_obvd_232_pvt_below_max_streak_d3},
    "f22_obvd_233_pvt_age_of_max_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_233_pvt_age_of_max_252d_d3},
    "f22_obvd_234_pvt_minus_ema63_zscore_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_234_pvt_minus_ema63_zscore_252d_d3},
    "f22_obvd_235_pvt_diff_zscore_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_235_pvt_diff_zscore_252d_d3},
    "f22_obvd_236_obv_rsi_vs_price_rsi_diff_14d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_236_obv_rsi_vs_price_rsi_diff_14d_d3},
    "f22_obvd_237_obv_rsi_vs_price_rsi_diff_21d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_237_obv_rsi_vs_price_rsi_diff_21d_d3},
    "f22_obvd_238_obv_rsi_below_50_with_price_rsi_above_70_indicator_d3": {"inputs": ["close", "volume"], "func": f22_obvd_238_obv_rsi_below_50_with_price_rsi_above_70_indicator_d3},
    "f22_obvd_239_obv_rsi_below_50_price_rsi_above_70_count_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_239_obv_rsi_below_50_price_rsi_above_70_count_252d_d3},
    "f22_obvd_240_obv_macd_hist_minus_price_macd_hist_d3": {"inputs": ["close", "volume"], "func": f22_obvd_240_obv_macd_hist_minus_price_macd_hist_d3},
    "f22_obvd_241_obv_macd_negative_price_macd_positive_count_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_241_obv_macd_negative_price_macd_positive_count_252d_d3},
    "f22_obvd_242_obv_stoch_minus_price_stoch_14d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_242_obv_stoch_minus_price_stoch_14d_d3},
    "f22_obvd_243_obv_pct_rank_minus_close_pct_rank_63d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_243_obv_pct_rank_minus_close_pct_rank_63d_d3},
    "f22_obvd_244_obv_pct_rank_minus_close_pct_rank_504d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_244_obv_pct_rank_minus_close_pct_rank_504d_d3},
    "f22_obvd_245_double_divergence_score_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_245_double_divergence_score_252d_d3},
    "f22_obvd_246_haar_wavelet_level1_obv_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_246_haar_wavelet_level1_obv_252d_d3},
    "f22_obvd_247_haar_wavelet_level2_obv_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_247_haar_wavelet_level2_obv_252d_d3},
    "f22_obvd_248_haar_wavelet_level3_obv_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_248_haar_wavelet_level3_obv_252d_d3},
    "f22_obvd_249_obv_wavelet_low_to_high_ratio_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_249_obv_wavelet_low_to_high_ratio_252d_d3},
    "f22_obvd_250_obv_ema_diff_5_21_d3": {"inputs": ["close", "volume"], "func": f22_obvd_250_obv_ema_diff_5_21_d3},
    "f22_obvd_251_obv_multi_horizon_zscore_aggregate_d3": {"inputs": ["close", "volume"], "func": f22_obvd_251_obv_multi_horizon_zscore_aggregate_d3},
    "f22_obvd_252_obv_multi_horizon_zscore_dispersion_d3": {"inputs": ["close", "volume"], "func": f22_obvd_252_obv_multi_horizon_zscore_dispersion_d3},
    "f22_obvd_253_obv_smooth_minus_raw_zscore_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_253_obv_smooth_minus_raw_zscore_252d_d3},
    "f22_obvd_254_obv_hp_filter_residual_std_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_254_obv_hp_filter_residual_std_252d_d3},
    "f22_obvd_255_obv_decay_constant_emadiff_63_252_d3": {"inputs": ["close", "volume"], "func": f22_obvd_255_obv_decay_constant_emadiff_63_252_d3},
    "f22_obvd_256_mi_obvdiff_close_diff_63d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_256_mi_obvdiff_close_diff_63d_d3},
    "f22_obvd_257_mi_obvdiff_close_diff_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_257_mi_obvdiff_close_diff_252d_d3},
    "f22_obvd_258_mi_obvdiff_lagged_close_diff_63d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_258_mi_obvdiff_lagged_close_diff_63d_d3},
    "f22_obvd_259_obv_kl_divergence_recent_vs_baseline_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_259_obv_kl_divergence_recent_vs_baseline_252d_d3},
    "f22_obvd_260_obv_shannon_entropy_diff_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_260_obv_shannon_entropy_diff_252d_d3},
    "f22_obvd_261_obv_information_share_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_261_obv_information_share_252d_d3},
    "f22_obvd_262_conditional_entropy_obv_given_return_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_262_conditional_entropy_obv_given_return_252d_d3},
    "f22_obvd_263_obv_signed_volume_perm_entropy_63d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_263_obv_signed_volume_perm_entropy_63d_d3},
    "f22_obvd_264_obv_signed_volume_perm_entropy_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_264_obv_signed_volume_perm_entropy_252d_d3},
    "f22_obvd_265_obv_entropy_decay_63_minus_252_d3": {"inputs": ["close", "volume"], "func": f22_obvd_265_obv_entropy_decay_63_minus_252_d3},
    "f22_obvd_266_obv_regime_label_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_266_obv_regime_label_252d_d3},
    "f22_obvd_267_obv_regime_transitions_count_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_267_obv_regime_transitions_count_252d_d3},
    "f22_obvd_268_obv_high_regime_dwell_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_268_obv_high_regime_dwell_252d_d3},
    "f22_obvd_269_obv_low_regime_dwell_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_269_obv_low_regime_dwell_252d_d3},
    "f22_obvd_270_obv_high_to_low_regime_transition_count_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_270_obv_high_to_low_regime_transition_count_252d_d3},
    "f22_obvd_271_obv_regime_current_label_d3": {"inputs": ["close", "volume"], "func": f22_obvd_271_obv_regime_current_label_d3},
    "f22_obvd_272_obv_regime_current_age_d3": {"inputs": ["close", "volume"], "func": f22_obvd_272_obv_regime_current_age_d3},
    "f22_obvd_273_obv_diff_variance_ratio_q_2_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_273_obv_diff_variance_ratio_q_2_252d_d3},
    "f22_obvd_274_obv_diff_vol_of_vol_63d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_274_obv_diff_vol_of_vol_63d_d3},
    "f22_obvd_275_obv_diff_garch_persistence_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_275_obv_diff_garch_persistence_252d_d3},
    "f22_obvd_276_obv_diff_neg_to_pos_var_ratio_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_276_obv_diff_neg_to_pos_var_ratio_252d_d3},
    "f22_obvd_277_obv_diff_q90_q10_ratio_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_277_obv_diff_q90_q10_ratio_252d_d3},
    "f22_obvd_278_obv_diff_neg_persistence_count_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_278_obv_diff_neg_persistence_count_252d_d3},
    "f22_obvd_279_obv_oscillation_amplitude_63d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_279_obv_oscillation_amplitude_63d_d3},
    "f22_obvd_280_obv_regime_entropy_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_280_obv_regime_entropy_252d_d3},
    "f22_obvd_281_obv_distribution_composite_score_d3": {"inputs": ["high", "close", "volume"], "func": f22_obvd_281_obv_distribution_composite_score_d3},
    "f22_obvd_282_obv_distribution_score_streak_d3": {"inputs": ["high", "close", "volume"], "func": f22_obvd_282_obv_distribution_score_streak_d3},
    "f22_obvd_283_obv_climax_then_distribution_count_252d_d3": {"inputs": ["high", "close", "volume"], "func": f22_obvd_283_obv_climax_then_distribution_count_252d_d3},
    "f22_obvd_284_obv_failure_to_make_new_high_score_d3": {"inputs": ["high", "close", "volume"], "func": f22_obvd_284_obv_failure_to_make_new_high_score_d3},
    "f22_obvd_285_obv_silent_distribution_score_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_285_obv_silent_distribution_score_252d_d3},
    "f22_obvd_286_obv_lower_high_with_higher_price_high_count_63d_d3": {"inputs": ["high", "close", "volume"], "func": f22_obvd_286_obv_lower_high_with_higher_price_high_count_63d_d3},
    "f22_obvd_287_obv_negative_run_with_price_up_count_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_287_obv_negative_run_with_price_up_count_252d_d3},
    "f22_obvd_288_obv_distribution_intensity_252d_d3": {"inputs": ["high", "close", "volume"], "func": f22_obvd_288_obv_distribution_intensity_252d_d3},
    "f22_obvd_289_obv_post_peak_distribution_signature_252d_d3": {"inputs": ["high", "close", "volume"], "func": f22_obvd_289_obv_post_peak_distribution_signature_252d_d3},
    "f22_obvd_290_obv_post_peak_distribution_count_252d_d3": {"inputs": ["high", "close", "volume"], "func": f22_obvd_290_obv_post_peak_distribution_count_252d_d3},
    "f22_obvd_291_obv_compound_topping_score_252d_d3": {"inputs": ["high", "close", "volume"], "func": f22_obvd_291_obv_compound_topping_score_252d_d3},
    "f22_obvd_292_obv_distribution_zone_dwell_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_292_obv_distribution_zone_dwell_252d_d3},
    "f22_obvd_293_obv_no_followthrough_after_jump_count_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_293_obv_no_followthrough_after_jump_count_252d_d3},
    "f22_obvd_294_obv_distribution_during_rally_indicator_d3": {"inputs": ["close", "volume"], "func": f22_obvd_294_obv_distribution_during_rally_indicator_d3},
    "f22_obvd_295_obv_distribution_during_rally_count_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_295_obv_distribution_during_rally_count_252d_d3},
    "f22_obvd_296_obv_corr_pct_change_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_296_obv_corr_pct_change_252d_d3},
    "f22_obvd_297_obv_rank_corr_close_5d_lead_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_297_obv_rank_corr_close_5d_lead_252d_d3},
    "f22_obvd_298_obv_failure_to_pred_close_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_298_obv_failure_to_pred_close_252d_d3},
    "f22_obvd_299_obv_information_share_in_top_decile_close_252d_d3": {"inputs": ["close", "volume"], "func": f22_obvd_299_obv_information_share_in_top_decile_close_252d_d3},
    "f22_obvd_300_obv_master_distribution_intensity_score_d3": {"inputs": ["high", "low", "close", "volume"], "func": f22_obvd_300_obv_master_distribution_intensity_score_d3},
}
